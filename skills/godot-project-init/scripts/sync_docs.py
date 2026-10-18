"""Convert an official Godot offline HTML archive into a versioned Markdown snapshot.

Requires beautifulsoup4 and markdownify. Never updates a project implicitly.
Read ZIP members without extracting its assets or executing any downloaded code.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import posixpath
import re
import time
import urllib.request
import zipfile
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urljoin, urlsplit

from bs4 import BeautifulSoup
from markdownify import MarkdownConverter

CONVERTER_VERSION = "1.0.1"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_json(path: Path, value: object) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(path)


def download(url: str, target: Path, expected_hash: str | None = None) -> None:
    if target.is_file() and (not expected_hash or sha(target.read_bytes()) == expected_hash):
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    part = target.with_suffix(target.suffix + ".part")
    for attempt in range(3):
        try:
            offset = part.stat().st_size if part.exists() else 0
            headers = {"User-Agent": "GodotLocalDocs/1.0"}
            if offset:
                headers["Range"] = f"bytes={offset}-"
            with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=60) as response:
                mode = "ab" if offset and response.status == 206 else "wb"
                with part.open(mode) as stream:
                    while block := response.read(1024 * 1024):
                        stream.write(block)
            if expected_hash and sha(part.read_bytes()) != expected_hash:
                part.unlink()
                raise ValueError("Archive SHA256 mismatch")
            part.replace(target)
            return
        except Exception:
            if attempt == 2:
                raise
            time.sleep(2 ** attempt)


class Converter(MarkdownConverter):
    def convert_a(self, el, text, parent_tags):
        if el.get("id") and not el.get("href"):
            return '\n<a id="' + html.escape(el["id"], quote=True) + '"></a>\n'
        return super().convert_a(el, text, parent_tags)

    def convert_pre(self, el, text, parent_tags):
        language = ""
        for ancestor in [el, *list(el.parents)[:3]]:
            for cls in ancestor.get("class", []):
                if cls.startswith(("highlight-", "language-")):
                    language = cls.split("-", 1)[1]
                    break
            if language:
                break
        code = el.get_text().rstrip("\n")
        longest = max((len(x) for x in re.findall(r"`+", code)), default=0)
        fence = "`" * max(3, longest + 1)
        return f"\n\n{fence}{language}\n{code}\n{fence}\n\n"


def article_fragment(raw: str) -> str:
    # Avoid parsing megabytes of repeated sidebar navigation on every page.
    start = re.search(r'<div\s+[^>]*itemprop=[\"\']articleBody[\"\'][^>]*>', raw)
    if not start:
        raise ValueError("Missing articleBody; refusing to mirror page chrome")
    fragment = raw[start.start():]
    return re.split(r"<footer(?:\s|>)", fragment, maxsplit=1)[0]


def convert_page(raw: str, rel: str, pages: set[str], base: str):
    soup = BeautifulSoup(article_fragment(raw), "html.parser")
    body = soup.select_one('[itemprop="articleBody"]')
    if body is None:
        raise ValueError("No article body")
    for tag in list(body.select('script, style, button, [role="tablist"], .headerlink, .viewcode-link, .rst-footer-buttons, #disqus_thread, .admonition-grid, .godot-contribute')):
        if tag.parent is None:
            continue
        tag.decompose()
    # A comment widget is not part of the authored documentation.
    comments = body.find(id="user-contributed-notes")
    if comments:
        comments.decompose()
    h1 = body.find("h1")
    title = h1.get_text(" ", strip=True) if h1 else rel
    anchors = []
    for tag in list(body.find_all(id=True)):
        ident = tag["id"]
        if ident.startswith(("tab-", "panel-")):
            del tag["id"]
            continue
        if ident not in anchors:
            marker = soup.new_tag("a", id=ident)
            tag.insert_before(marker)
            anchors.append(ident)
        del tag["id"]
    links = []
    externalized = []
    page_url = base + rel
    for tag in body.find_all("a", href=True):
        href = tag["href"]
        absolute = urljoin(page_url, href)
        parts = urlsplit(absolute)
        if absolute.startswith(base):
            target = unquote(parts.path[len(urlsplit(base).path):])
            if target.endswith("/"):
                target += "index.html"
            if target in pages:
                local = posixpath.relpath(target[:-5] + ".md", posixpath.dirname(rel) or ".")
                tag["href"] = local + ("#" + parts.fragment if parts.fragment else "")
                links.append({"page": target, "anchor": unquote(parts.fragment)})
            else:
                tag["href"] = absolute
                if target.endswith(".html"):
                    externalized.append(absolute)
        elif not parts.scheme or parts.scheme in ("http", "https"):
            tag["href"] = absolute
    images = []
    for tag in body.find_all(["img", "video", "audio", "source"]):
        if tag.get("src"):
            tag["src"] = urljoin(page_url, tag["src"])
            images.append(tag["src"])
    md = Converter(heading_style="ATX", bullets="-", escape_underscores=False, escape_asterisks=True).convert(str(body))
    md = f"> Source: {page_url}\n> Godot documentation: {base.rstrip('/').split('/')[-1]}; format-converted, not summarized.\n\n" + md.strip() + "\n"
    if len(md) < 100:
        raise ValueError("Unexpectedly empty Markdown")
    return md, {"title": title, "anchors": anchors, "links": links, "externalized": externalized, "media": images}


def build(archive: Path, output: Path, version: str, source_url: str, expected_hash: str | None, license_dir: Path):
    output = output.resolve()
    if output == Path(output.anchor) or len(output.parts) < 3:
        raise ValueError("Refusing a drive root or top-level directory")
    if not (license_dir / "LICENSE-docs.txt").is_file():
        raise ValueError("Provide the official documentation license in --license-dir")
    archive_hash = sha(archive.read_bytes())
    if expected_hash and expected_hash != archive_hash:
        raise ValueError("Archive SHA256 mismatch")
    base = f"https://docs.godotengine.org/en/{version}/"
    with zipfile.ZipFile(archive) as z:
        entries = [n for n in z.namelist() if n.endswith("index.html") and "/_" not in n]
        roots = sorted(entries, key=lambda n: (n.count("/"), len(n)))
        if not roots:
            raise ValueError("Archive has no index.html")
        root_index = roots[0]
        prefix = root_index[:-len("index.html")]
        index_raw = z.read(root_index).decode("utf-8")
        options_name = prefix + "_static/documentation_options.js"
        options = z.read(options_name).decode("utf-8") if options_name in z.namelist() else ""
        versions = re.findall(r'(?:name="doc_version" content="|VERSION\s*:\s*[\"\'])([^\"\']+)', index_raw + options)
        if version not in versions:
            raise ValueError(f"Archive declares {versions}, requested {version}; refusing version drift")
        members = {}
        for n in z.namelist():
            if not n.startswith(prefix) or not n.endswith(".html"):
                continue
            rel = n[len(prefix):]
            path = PurePosixPath(rel)
            if path.is_absolute() or ".." in path.parts or ":" in rel or "\\" in rel:
                raise ValueError("Unsafe archive member: " + rel)
            if any(p.startswith("_") for p in path.parts):
                continue
            members[rel] = n
        excluded = [p for p in ("search.html", "genindex.html", "py-modindex.html") if p in members]
        for p in excluded:
            members.pop(p)
        pages = set(members)
        output.mkdir(parents=True, exist_ok=True)
        for license_file in license_dir.glob("*.txt"):
            (output / license_file.name).write_bytes(license_file.read_bytes())
        (output / "ATTRIBUTION.md").write_text(
            f"# 来源与许可\n\nCopyright Godot Engine contributors.\n\n"
            f"原文：{base}\n\n文档许可：Creative Commons Attribution 3.0 Unported，完整文本见 LICENSE-docs.txt。\n\n"
            "本镜像只进行 HTML→Markdown 格式转换、导航移除和链接重写，不代表官方认可，也不对正文进行摘要改写。"
            "每页原始 URL 和内容哈希见 manifest.json。引擎源码许可另保存在 LICENSE-engine.txt（如附带）。\n",
            encoding="utf-8")
        manifest_path = output / "manifest.json"
        previous = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {}
        if previous and (previous.get("archive_sha256") != archive_hash or previous.get("converter_version") != CONVERTER_VERSION):
            raise ValueError("Output contains another snapshot/converter. Use a new output directory, review, then update explicitly.")
        records = previous.get("pages", {})
        failures = {}
        metadata = {"schema": 1, "docs_version": version, "engine_baseline": "4.7.2" if version == "4.7" else None,
                    "language": "en", "source_base": base, "archive_url": source_url,
                    "archive_sha256": archive_hash, "snapshot_at": previous.get("snapshot_at", datetime.now(timezone.utc).isoformat()),
                    "converter_version": CONVERTER_VERSION, "expected_pages": len(pages),
                    "excluded_generated_search_pages": excluded, "pages": records}
        for i, rel in enumerate(sorted(pages), 1):
            dest = output / (rel[:-5] + ".md")
            old = records.get(rel)
            if old and dest.exists() and sha(dest.read_bytes()) == old["markdown_sha256"]:
                continue
            try:
                data = z.read(members[rel])
                md, record = convert_page(data.decode("utf-8"), rel, pages, base)
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(md, encoding="utf-8", newline="\n")
                record.update({"path": rel[:-5] + ".md", "source_url": base + rel,
                               "source_sha256": sha(data), "markdown_sha256": sha(dest.read_bytes()),
                               "source_bytes": len(data), "markdown_bytes": dest.stat().st_size})
                records[rel] = record
            except Exception as error:
                failures[rel] = f"{type(error).__name__}: {error}"
            if i % 100 == 0:
                metadata.update({"completed_pages": len(records), "failures": failures, "complete": False})
                write_json(manifest_path, metadata)
                print(f"Converted {i}/{len(pages)}; failures={len(failures)}", flush=True)
        broken = []
        for rel, record in records.items():
            for link in record["links"]:
                target = records.get(link["page"])
                if not target or (link["anchor"] and link["anchor"] not in target["anchors"]):
                    broken.append({"from": rel, **link})
        # Keep broken upstream anchors usable: point at the destination page and
        # report the original fragment. Do not invent a replacement API anchor.
        for issue in broken:
            source = output / records[issue["from"]]["path"]
            target = posixpath.relpath(issue["page"][:-5] + ".md", posixpath.dirname(issue["from"]) or ".")
            content = source.read_text(encoding="utf-8")
            content = content.replace("](" + target + "#" + issue["anchor"] + ")", "](" + target + ")")
            source.write_text(content, encoding="utf-8", newline="\n")
            records[issue["from"]]["markdown_sha256"] = sha(source.read_bytes())
            records[issue["from"]]["markdown_bytes"] = source.stat().st_size
        metadata.update({"completed_pages": len(records), "failures": failures,
                         "complete": len(records) == len(pages) and not failures,
                         "upstream_missing_anchors": broken,
                         "media_policy": "Online source URLs retained; images/audio/video are not embedded locally.",
                         "total_markdown_bytes": sum(r["markdown_bytes"] for r in records.values())})
        write_json(manifest_path, metadata)
        index = [f"# Godot {version} 本地官方文档", "", f"正文覆盖：{len(records)}/{len(pages)}。来源语言：英文。格式转换保留原文，不是摘要。", "",
                 "这是所记录时间的版本化官网离线归档快照；4.7 文档分支不保证严格等同每一个 4.7.2 补丁细节。",
                 "图片/音视频保留官网地址；纯文字、代码及 API 正文可离线阅读。完整来源、哈希和缺失锚点见 manifest.json。", "",
                 "## 常用入口", ""]
        quick = ["tutorials/best_practices/index.html", "tutorials/best_practices/scene_organization.html", "tutorials/scripting/resources.html", "tutorials/scripting/gdscript/gdscript_styleguide.html", "tutorials/editor/command_line_tutorial.html", "classes/class_node.html", "classes/class_resource.html", "classes/class_signal.html"]
        for rel in quick:
            if rel in records:
                index.append(f"- [{records[rel]['title']}]({records[rel]['path']})")
        index += ["", "## 全部页面", ""]
        for rel, record in sorted(records.items()):
            index.append(f"- [{record['title']}]({record['path']})")
        (output / "CATALOG.md").write_text("\n".join(index) + "\n", encoding="utf-8")
        write_json(output / "search_index.json", [{"title": r["title"], "path": r["path"]} for r in records.values()])
        print(json.dumps({k: metadata[k] for k in ("docs_version", "completed_pages", "expected_pages", "complete", "total_markdown_bytes")}, ensure_ascii=False), flush=True)
        if failures:
            raise RuntimeError(f"{len(failures)} pages failed; see manifest.json")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, required=True, help="Cached official ZIP; downloaded here when --url is supplied")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--version", required=True)
    parser.add_argument("--url", default="")
    parser.add_argument("--sha256")
    parser.add_argument("--license-dir", type=Path, default=Path(__file__).resolve().parents[1] / "assets/licenses")
    args = parser.parse_args()
    if not re.fullmatch(r"\d+\.\d+", args.version):
        parser.error("Use a fixed major.minor documentation version")
    if args.url:
        download(args.url, args.archive, args.sha256)
    build(args.archive, args.output, args.version, args.url or "local official archive", args.sha256, args.license_dir)


if __name__ == "__main__":
    main()
