# __PROJECT_NAME__

引擎：Godot __ENGINE_VERSION__。目标平台：__PLATFORM__。

使用对应版本 Godot 打开 `project.godot`，运行主场景。项目规则见 `AGENTS.md`。

## 文件放在哪里

| 位置 | 用途 |
| --- | --- |
| `project.godot`、`AGENTS.md`、`README.md` | Godot 入口、开发约定与项目导航 |
| `scenes/` | 按功能细分的可编辑场景；初始入口为 main/main.tscn |
| `scripts/` | 按功能细分的行为、纯规则与 Resource 类脚本；初始为 main/main.gd |
| `resources/` | 按用途或功能细分的配置实例、Theme 等 .tres；有内容时再创建 |
| `assets/` | 按媒体类型与用途细分的图片、音频、字体及随附许可；有内容时再创建 |
| `docs/` | 需求、架构、素材流程/来源；`godot/__DOCS_VERSION__/` 是可检索的官方 Markdown 正文 |
| `tools/` | 验证和资源制作工具；`comfyui/` 保存 WAI 基础工作流及其模型说明 |
| `tests/` | 应保留的冒烟与行为测试源码 |
| `__SKILL_ROOT__/godot-dev/` | 项目开发技能 |
| `.codex/`、`.dsh/` | 按宿主生成的 MCP 配置/补丁 |
| `.bootstrap/` | 初始化文件归属与版本锁，用于安全重复执行 |
| `.local/` | 本机路径、Desktop 实例绑定、MCP 独立数据和初始化验收摘要，不提交 Git |
| `work/` | 每轮独立临时目录；本轮完成后清理其中不再需要的文件 |

已有项目沿用现有业务目录，不为套用表格移动场景或脚本。`.godot/` 是引擎导入缓存；保留有用的 `.uid` 和导入设置。
素材服务由 .bootstrap/state.json 的 profile 决定：core 不配置；desktop-wai 使用普通 Desktop 实例和共享模型；endpoint 接入明确给定的现有 API。具体边界与操作见 docs/asset-pipeline.md。
初始化结果保存在 `.local/initialization-report.json`，包括实际配置、检查结果、未验证项和清理结果。保留必要配置与证据，不堆积测试工程或一次性日志。

## 开发与检查

后续开发：Codex 使用 `$godot-dev`，Harness 使用 `/godot-dev`，然后提供任务书。
也可以选中 dev 技能后直接提供需求。它会按本次范围实现、按需生成并接入素材、验证和清理；每轮摘要保存在 `.local/dev-reports/`，素材来源保存在 `docs/assets/`。已有可用素材优先复用，无需每次启动 ComfyUI。

检查：`powershell -NoProfile -ExecutionPolicy Bypass -File tools/check.ps1`。
本机标准 Windows 便携版 Godot 推荐增加 `-IsolateEditor`，验证时临时复制引擎并自动清理，避免修改原有编辑器配置。
初始化时通过 `-ReportDir <本轮临时目录>/checks` 集中检查日志；提取验收摘要后清理该临时目录。
本机路径放在忽略提交的 `.local/toolchain.json`；换机器可传 `-Godot` 与 `-Python`，或重建该文件。

官方文档实际正文与许可证位于 `docs/godot/__DOCS_VERSION__/`。从 `CATALOG.md` 进入，按主题或类名检索。
`docs/requirements.md` 记录需求，`docs/architecture.md` 只记录实际采用的模块边界。

导出时使用 `docs/exporting.md` 中的排除规则。项目不依赖 ComfyUI、MCP 或网络即可运行。

资源制作见 [项目资源流程](docs/asset-pipeline.md)。只有 desktop-wai 预配置 WAI 文生图；其他图片、音乐与音效按实际模型和用途配置。游戏运行不需要 ComfyUI。

开发技能包含按任务读取的专题资料；初始化会一并安装，无需逐个添加。专题和来源取舍见 [__SKILL_ROOT__/godot-dev/SKILL.md](__SKILL_ROOT__/godot-dev/SKILL.md)。它们不会预装组件框架、测试插件或通用管理器。

推荐从用户级 `godot-project-init` 创建项目，在项目会话中使用这里生成的 `godot-dev`。本项目的 dev 是独立副本，可以随项目规则调整；更新或卸载用户级 init 不会自动改动它。项目级 init、用户级 dev 和独立 dev 也可按需使用。生成文件的更新归属由 `.bootstrap/state.json` 记录；更新项目 dev 前先审阅本项目修改。
