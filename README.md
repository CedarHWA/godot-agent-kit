# Godot Agent Kit

面向 **Windows 上的 Codex 和 DeepSeek Harness** 的可安装 Godot 技能仓库，版本 **2.0.0**。包含项目初始化与需求开发两个技能，支持单独安装、项目级/用户级安装、冲突保护、升级回滚和环境检查。

**第一次使用？从 [安装与使用指南：Codex / DeepSeek Harness](docs/install-and-use.md) 开始。** 按步骤下载、配置 Godot、安装两个技能，再复制对应宿主的初始化和开发提示词。

[下载 v2.0.0 安装包](https://github.com/CedarHWA/godot-agent-kit/releases/tag/v2.0.0) · [Windows 环境与 ComfyUI](docs/windows.md) · [已有技能迁移](docs/migration.md)

## 快速开始

下载并解压发布包，或克隆本仓库，然后在仓库根目录打开 PowerShell。先准备 Python 3.11+ 和项目要求的 Godot。安装技能本身只用 Python 标准库；运行检查和维护工具建议建立隔离环境：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\setup.ps1
$python = (Resolve-Path .\.venv\Scripts\python.exe).Path
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Python $python -Agent both -Scope project -Project 'D:\Games\MyGame'
```

将示例项目路径换成自己的目标。`both` 把两个技能安装到项目 `.agents/skills`，Codex 和 Harness 共用一份。安装只复制技能，不修改游戏内容、不启动 ComfyUI。已有同名文件发生冲突时退出 2，保留原件并写候选文件；不会覆盖自己的旧技能。旧版个人技能迁移见 [迁移说明](docs/migration.md)。

只给 Harness 安装时用 `-Agent deepseek-harness`；只给 Codex 用 `-Agent codex`。用户级安装改成 `-Scope user`，省略 `-Project`；Codex 使用 CODEX_HOME/skills（默认 ~/.codex/skills），Harness 使用 DSH_HOME/skills（默认 ~/.dsh/skills），用户级 both 分别安装两份。仅安装开发技能加 `-Skills dev`。运行前加 `-DryRun` 可查看计划。

在目标项目打开新会话：

| 操作 | Codex | DeepSeek Harness |
| --- | --- | --- |
| 初始化 | `$godot-project-init 初始化当前项目，使用 core 配置档、agent=both。` | `/godot-project-init 初始化当前项目，使用 core 配置档、agent=both。` |
| 开发 | `$godot-dev 按 docs/requirements.md 完成功能与验收。` | `/godot-dev 按 docs/requirements.md 完成功能与验收。` |

## 配置和检查

工具发现顺序：明确 JSON 配置 → 环境变量 → 已有项目 `.local` → PATH。仓库不携带个人路径。复制配置示例到忽略提交的目录，填入本机路径：

```powershell
New-Item -ItemType Directory -Path .local -Force | Out-Null
Copy-Item config.example.json .local\machine.json
# 编辑 .local\machine.json 的 godot / python 等字段，然后检查。
powershell -NoProfile -ExecutionPolicy Bypass -File .\doctor.ps1 -Python $python -Config .local\machine.json -Profile core
```

若希望安装后的初始化技能记住这些路径，安装时加 `-Config .local\machine.json`；未传时安装器不会复制当前机器配置。换机器重新配置即可。Godot 不在 PATH 时需配置 `godot` 或 `GODOT_PATH`；没有 ComfyUI 不影响 core 与独立 godot-dev。

| 配置档 | 提供能力 | 边界 |
| --- | --- | --- |
| `core`（新项目默认） | 规范、完整 dev 技能、离线官方文档、可编辑入口、检查工具 | 不需要素材生成服务 |
| `desktop-wai` | 完整保留 Comfy Desktop 普通实例创建/恢复、Explorer Shell 启动、共享 WAI、独立环境/I/O、项目 MCP、来源/许可和验收 | 已验证 Desktop 1.1.7、Windows NVIDIA；不下载模型 |
| `endpoint` | 接入明确的现有 ComfyUI API，查节点、验证/提交工作流、记录回执、查询与下载输出 | 不接管外部实例生命周期；输入上传沿用现有 UI/MCP |

Godot 4.7.2 是已验证的新项目默认值；完整 4.7 官方 Markdown 快照随仓库发布（1,596 页，带来源/哈希/许可）。已有引擎不静默升级。其他版本显式给 `--engine-version` 与匹配 `--docs-root`，或 `--docs-mode online`；不会强套 4.7 文档。

直接运行初始化器也可以，不依赖 agent 调用：

```powershell
& $python toolkit/cli.py init --path 'D:\Games\MyGame' --profile core --agent both --config .local/machine.json --dry-run
& $python toolkit/cli.py init --path 'D:\Games\MyGame' --profile core --agent both --config .local/machine.json
```

CLI 文件生成完成后还需执行项目 `tools/check.ps1` 和文档检查；完整技能流程会继续这些步骤并保存报告。Desktop 配置档退出 3 表示等待正常实例创建/绑定，不能当成完成。详细操作见 [Windows 配置](docs/windows.md)、[宿主适配](docs/agents.md)、[功能与兼容矩阵](docs/compatibility.md)。

## 升级、回滚和卸载

升级仓库后用相同参数重跑安装器。只更新仍与记录哈希一致的文件；用户改动会保留。首次安装不认领内容相同的外部文件。不要用手工覆盖技能目录的方式升级。

```powershell
.\install.ps1 -Python $python -Agent both -Project 'D:\Games\MyGame' -Action rollback
.\install.ps1 -Python $python -Agent both -Project 'D:\Games\MyGame' -Action uninstall
.\install.ps1 -Python $python -Agent both -Project 'D:\Games\MyGame' -Action recover
```

`rollback` 恢复最后一次实际修改前的内容和归属记录；拒绝覆盖操作之后的用户编辑。`uninstall` 只删除仍由本工具拥有且未修改的文件，保留其它文件与恢复历史。`recover` 用于中断后有 pending 日志的事务。收据/备份在技能根 `.godot-agent-kit/`；它们是恢复依据，不作为垃圾自动清理。详见 [迁移与恢复](docs/migration.md)。

## 开发、验证和发布

```powershell
& $python toolkit/validate.py
& $python tests/run.py
& $python tests/integration.py --godot 'D:\Tools\Godot\Godot_console.exe'
& $python toolkit/build.py
```

最后一个命令生成 `dist/godot-agent-kit-2.0.0.zip`、SHA-256 和包内文件清单。包中无 `.local`、虚拟环境、模型、游戏素材或用户凭据。安装器从唯一的 `skills/godot-dev` 源构建初始化器内附的完整 dev 模板，避免两份源码漂移。

仓库结构：`skills/` 技能与自包含运行资源；`toolkit/` 安装/校验/打包；`adapters/` 宿主契约；`tests/` 行为与真实宿主/引擎测试；`docs/` 使用/维护/验收文档；`.github/workflows/` Windows CI。profile 在初始化技能 `assets/profiles/`。

[本次验收](docs/acceptance.md) 区分已执行测试、实际宿主加载和未执行的模型行为评测。安装/代码测试不会自动证明未来 agent 的视觉判断、听感或游戏质量。

本仓库代码采用 [MIT](LICENSE)；官方文档等第三方内容保留独立许可，见 [第三方说明](THIRD_PARTY_NOTICES.md)。模型权重不随仓库分发。
