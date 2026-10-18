# Godot Agent Kit 维护约定

本目录是独立 Python/PowerShell 技能仓库，不是上层游戏工程。不要修改上层游戏、现有用户技能或 Comfy 实例来完成工具包维护。

- 先读 README.md、docs/compatibility.md 和相关实现。新增宿主适配先核对其当前官方文档与本机接口。
- godot-dev 只有 skills/godot-dev 一份源码；安装时生成 init 内的 SKILL.md.template，防止 Codex 递归重复发现。
- Python 标准库可完成安装、初始化与 doctor。额外依赖进入独立环境并维护版本清单；不写个人路径/凭据，不打包权重或缓存。
- Windows 路径、中文/空格、已有配置、用户修改、重复运行、中断恢复、junction 与卸载归属是必要边界。
- 保留 Desktop/WAI 已有流程的版本门禁、Shell 启动、归属与哈希校验；涉及其行为更改时做对应真实验证，不以替身断言冒充。
- 执行 `powershell -NoProfile -ExecutionPolicy Bypass -File tools/check.ps1`；有 Godot 时传 `-Godot <绝对路径>`。宿主发现另用 tests/host_smoke.py。仅声称实际执行的验收。
- 临时任务放本仓库 work/，有效环境放 .venv/.local；报告保留紧凑证据，发布前清理本轮无用目录。原文档快照不可就地修改。
- 发布通过 toolkit/build.py；核对包清单、个人路径、许可证和 SHA-256。外部发布需用户明确要求。
