"""Launch through the user's Explorer Shell, matching the Start-menu environment.

GetPackageFullName alone does not detect MSIX filesystem virtualization. A short
worker verifies physical config paths before spawning Desktop. No UI automation.
"""
from __future__ import annotations

import base64
import ctypes as C
from ctypes import wintypes as W
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time


def package_identity(pid):
    k = C.WinDLL("kernel32", use_last_error=True)
    k.OpenProcess.argtypes, k.OpenProcess.restype = [W.DWORD, W.BOOL, W.DWORD], W.HANDLE
    k.CloseHandle.argtypes = [W.HANDLE]
    k.GetPackageFullName.argtypes = [W.HANDLE, C.POINTER(W.UINT), W.LPWSTR]
    k.GetPackageFullName.restype = W.LONG
    handle = k.OpenProcess(0x1000, False, int(pid))
    if not handle:
        raise C.WinError(C.get_last_error())
    try:
        length = W.UINT()
        error = k.GetPackageFullName(handle, C.byref(length), None)
        if error == 15700:
            return None
        if error != 122:
            raise C.WinError(error)
        buf = C.create_unicode_buffer(length.value)
        error = k.GetPackageFullName(handle, C.byref(length), buf)
        if error:
            raise C.WinError(error)
        return buf.value
    finally:
        k.CloseHandle(handle)


def ps_literal(value):
    return "'" + str(value).replace("'", "''") + "'"


def powershell(command):
    encoded = base64.b64encode(command.encode("utf-16-le")).decode("ascii")
    exe = Path(os.environ["SystemRoot"]) / "System32/WindowsPowerShell/v1.0/powershell.exe"
    result = subprocess.run([str(exe), "-NoLogo", "-NoProfile", "-NonInteractive", "-EncodedCommand", encoded],
                            creationflags=subprocess.CREATE_NO_WINDOW, capture_output=True, timeout=20)
    if result.returncode:
        raise ValueError("Explorer Shell failed: " + result.stderr.decode("utf-8", errors="replace"))
    return result.stdout.decode("utf-8-sig")


def check_shortcut(path, exe):
    path = Path(path).resolve(strict=True)
    roots = [Path(os.environ["APPDATA"]) / "Microsoft/Windows/Start Menu/Programs",
             Path(os.environ["ProgramData"]) / "Microsoft/Windows/Start Menu/Programs"]
    if path.suffix.lower() != ".lnk" or not any(path.is_relative_to(root.resolve()) for root in roots):
        raise ValueError("Use an existing shortcut inside a normal Start-menu Programs directory")
    command = "\n".join([
        "$ErrorActionPreference = 'Stop'",
        "[Console]::OutputEncoding = New-Object System.Text.UTF8Encoding",
        "$shell = New-Object -ComObject WScript.Shell",
        "$link = $shell.CreateShortcut(" + ps_literal(path) + ")",
        "@{target=$link.TargetPath; arguments=$link.Arguments; cwd=$link.WorkingDirectory} | ConvertTo-Json -Compress",
    ])
    details = json.loads(powershell(command))
    if Path(details["target"]).resolve() != Path(exe).resolve() or details["arguments"].strip():
        raise ValueError("Start-menu shortcut target/arguments do not match the normal Desktop; inspect without modifying it")
    return path


def shell_open(target, arguments=(), *, cwd=None, visible=False):
    """Call the Shell object hosted by Explorer, not an in-process ShellExecute."""
    target = Path(target).resolve(strict=True)
    command = "\n".join([
        "$ErrorActionPreference = 'Stop'",
        "$shell = New-Object -ComObject 'Shell.Application'",
        "$desktopHwnd = 0",
        "$view = $shell.Windows().FindWindowSW(0,0,8,[ref]$desktopHwnd,1)",
        "if ($null -eq $view) { throw 'Explorer desktop Shell is unavailable; do not fall back to child-process launch' }",
        "$launcher = $view.Document.Application",
        "$launcher.ShellExecute(" + ",".join([
            ps_literal(target), ps_literal(subprocess.list2cmdline([str(x) for x in arguments])),
            ps_literal(cwd or target.parent), "'open'", "1" if visible else "0"]) + ")",
    ])
    powershell(command)


def launch_native(argv, *, cwd=None, visible=False, config_paths=()):
    if os.name != "nt":
        raise OSError("This Desktop launcher requires Windows")
    with tempfile.TemporaryDirectory(prefix="godot-desktop-launch-") as temp:
        result_path = Path(temp).resolve() / "result.json"
        payload = json.dumps({"argv": [str(a) for a in argv], "cwd": str(cwd or Path(argv[0]).parent),
                              "visible": visible, "config_paths": [str(p) for p in config_paths], "result": str(result_path)})
        python = getattr(sys, "_base_executable", sys.executable)
        shell_open(python, ["-B", str(Path(__file__).resolve()), "--worker", payload])
        deadline = time.monotonic() + 15
        while time.monotonic() < deadline:
            if result_path.is_file():
                result = json.loads(result_path.read_text(encoding="utf-8"))
                if "error" in result:
                    raise ValueError(result["error"])
                return result["pid"]
            time.sleep(0.1)
        raise ValueError("Native launcher timed out; inspect processes before retrying")


def _worker(payload):
    if package_identity(os.getpid()):
        raise ValueError("Explorer launch worker unexpectedly has package identity")
    for value in payload["config_paths"]:
        path = Path(value)
        actual = path.resolve(strict=True)
        if os.path.normcase(str(actual)) != os.path.normcase(os.path.abspath(path)):
            raise ValueError(f"Launch worker configuration is redirected: {actual}")
    startup = subprocess.STARTUPINFO()
    startup.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    startup.wShowWindow = 1 if payload["visible"] else 0
    proc = subprocess.Popen(payload["argv"], cwd=payload["cwd"], startupinfo=startup,
                            creationflags=subprocess.CREATE_NO_WINDOW,
                            stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return {"pid": proc.pid}


if __name__ == "__main__":
    mode, encoded = sys.argv[1:]
    payload = json.loads(encoded)
    try:
        if mode != "--worker":
            raise ValueError("Unknown native launch mode")
        value = _worker(payload)
    except Exception as exc:
        value = {"error": str(exc)}
    temporary = Path(payload["result"]).with_suffix(".tmp")
    temporary.write_text(json.dumps(value), encoding="utf-8")
    temporary.replace(payload["result"])
