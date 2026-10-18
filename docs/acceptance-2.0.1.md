# 2.0.1 验收记录

执行日期：2026-10-17。Windows，Python 3.14.7，Godot 4.7.2，Codex CLI 0.163.0-alpha.10.2，DeepSeek Harness 0.2.0-rc.2。

本版将推荐流程明确为用户级 init → 目标项目初始化 → 项目级 dev，保留旧安装参数默认值和全部显式布局。没有迁移本机已有技能或修改上层游戏。

| 验收项 | 实际结果 |
| --- | --- |
| 回归测试 | 67 项通过：安装/环境/适配/推荐布局 38 项，dev bundle 12 项，Desktop 回归 10 项，实例绑定 7 项 |
| 推荐流程 | 分别从 Codex、Harness 和双宿主的隔离用户目录运行已安装 init；生成完整项目 dev，重复执行无创建/更新/冲突 |
| 入口与范围 | 初始化前仅发现用户 init；初始化后 Codex 为 init=user、dev=repo，Harness 为 init=user-dsh、dev=project-dsh 或 project-agents；内附 dev 模板没有重复入口 |
| 真实宿主 | 14 组发现/加载检查通过，包括推荐方式的 8 组初始化前后检查，以及原项目双技能、用户双技能、共享项目安装；未发送模型请求 |
| 项目独立性 | 修改项目 A 的 dev 不影响项目 B；更新配置并重装、卸载用户 init 后，两个已有项目逐文件保持原样 |
| 兼容与归属 | 原默认命令仍在项目安装两个技能；只重装 init 不删除已有用户 dev；原冲突、回滚、恢复、路径/junction 与用户修改保护回归通过 |
| 安装器与 Godot | PowerShell 用户级安装后创建中文/空格路径工程；版本、格式、静态检查、导入、编辑器契约、行为冒烟、运行共 7 阶段通过 |
| 项目补齐与 MCP | 保留用户需求、报告规则冲突、审阅 keep-existing；真实 Harness 解析项目 MCP overlay 成功 |
| 官方文档与格式 | 1,596 页官方快照校验通过；两项技能 quick_validate、包内引用/语法/隐私检查、指南 PowerShell 代码块解析和本地链接检查通过 |
| 发布包 | 解压 ZIP，逐文件核验 RELEASE-MANIFEST，使用包内安装器执行用户级 init 安装，再用安装后的脚本生成项目 dev；Godot 忽略标记保留 |

机器可读摘要见 [acceptance-2.0.1.json](acceptance-2.0.1.json)。完整本机报告保存在忽略提交的 `.local/`；临时用户目录、测试工程和本轮无用文件已清理。此前功能与边界见 [2.0.0 验收](acceptance.md)。

复现入口：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File tools/check.ps1 -Godot '<本机固定版本 Godot.exe>'
.\.venv\Scripts\python.exe -B tests/host_smoke.py --harness-runtime '<Harness.exe 或 node.exe>' --harness-module '<已安装 dsh-skill-filesystem/lib/index.js>'
.\.venv\Scripts\python.exe -B toolkit/build.py
.\.venv\Scripts\python.exe -B tests/release_smoke.py dist/godot-agent-kit-2.0.1.zip
```

Windows CI 在 Python 3.11/3.14 上执行回归、打包和解压安装验证；运行结果在仓库 Actions 中查看。真实宿主与 Godot 检查使用上述本机环境，不由没有这些软件的 CI 代替。

本次没有运行独立 Agent 的完整游戏开发评测、重新创建 Comfy Desktop 实例、生成素材、检查游戏画面或试听音频；这些不属于安装布局变更的验收。本次通过的发现、CLI 和引擎检查不代表未来每次 Agent 执行或素材质量必然通过。
