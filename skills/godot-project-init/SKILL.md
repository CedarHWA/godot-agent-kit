---
name: godot-project-init
description: 在 Windows 下新建或补齐 Godot 项目的开发规范、开发技能、官方文档和验证工具；按配置接入 Comfy Desktop/WAI 或现有 ComfyUI。用于初始化和环境搭建，普通玩法开发使用 godot-dev。
metadata:
  runtime: Windows 10/11, Python 3.11+, Codex or DeepSeek Harness; Godot for runtime checks; ComfyUI optional.
---

# Godot 项目初始化

在用户指定目录或当前项目内执行完整初始化，已有 project.godot 时补齐；不另外嵌套游戏目录，不替用户设计玩法。保留已有项目、用户修改与引擎版本，只有明确要求才迁移。脚本目录相对于本 SKILL.md，不依赖固定用户名、盘符、Codex 专属 API 或全局 MCP 名称。

## 选择环境与宿主

先读项目及上级 AGENTS.md、已有需求、project.godot 和 `.bootstrap/state.json`。参数优先级：用户要求 → 已有项目/状态 → 已有需求约束 → profile 默认。没有版本约束的新项目默认 Godot 4.7.2、2D、Compatibility、Windows；安装的官方快照为 4.7。其他版本提供匹配 `--docs-root` 或显式 `--docs-mode online`，不能把 4.7 正文当其他版本使用。

- Codex：`--agent codex`；项目技能位于 `.agents/skills`。若能调用项目列表，按路径取得显示名，否则用明确名称、Godot 名称或目录名；聊天标题不作为项目名。
- DeepSeek Harness：`--agent deepseek-harness`；项目技能位于 `.dsh/skills`。显式调用 `/godot-project-init`，不依赖 `$skill` 语法。
- 两者共用：`--agent both`；技能只放 `.agents/skills`，两者均可发现，避免维护两份。Harness 以最近 `.git` 为项目根；无 `.git` 时使用 cwd，确保会话根与目标相符。

安装后的本机 `local.json` 可选；也可 `--config <机器配置JSON>`。脚本从明确配置、环境变量、现有项目绑定、PATH 发现工具，不把这些路径发布进技能仓库。环境检查：`python scripts/doctor.py --config <配置> --project <项目> --profile <配置档> --agent <宿主>`。失败项给出实际原因；可选图像/听审能力不足应记录未验证，不能假称通过。

## 选择配置档

| 配置档 | 适用范围 | 需要读取 |
| --- | --- | --- |
| `core` | 只搭建 Godot；不要求 ComfyUI。新项目未指定素材环境时采用 | 本页 |
| `desktop-wai` | 保留原有完整流程：普通 Desktop Standalone 实例、共享现有 WAI、独立依赖/节点/I/O、项目 MCP | [完整 Desktop 流程](references/desktop-workflow.md)，执行时按需查 [原生接口](references/desktop-api.md) |
| `endpoint` | 接入用户明确给定的现有 ComfyUI API，不接管其生命周期 | 生成的 docs/asset-pipeline.md |

已初始化工程沿用原配置档；旧 Desktop 绑定按 desktop-wai 识别，不默默降级到 core。切换必须明确 `--migrate-profile`；旧实例、绑定和未管理文件不自动删除。WAI 仅是一个可选基线；其它图片、音乐、音效模型按实际任务配置，不承诺已有工作流。

## 执行与验证

1. 确定目标、宿主、配置档、工具链、准确项目显示名称。先运行环境检查。初始化脚本不自动装系统软件、改全局配置或下载权重；依赖安装方法见 [Windows 运行环境](references/windows-runtime.md)。Desktop 的正常安装器可以联网安装独立核心和 Python 环境。
2. `scripts/init_workspace.ps1 -Action begin -Project <目标>` 建立有所有权标记的临时目录，保存返回的 run_dir。先以 `scripts/init_project.py --path <目标> --mode auto --profile <配置档> --agent <宿主> --config <配置> --project-display-name <显示名> --dry-run` 看计划，随后去掉 dry-run 执行。参数已知时不再重复确认。
3. 新建时生成可编辑 Main/World/UI 最小入口、规范、完整 godot-dev 专题、检查工具和文档。补齐时保持已有入口、场景、资源、测试、需求与架构。dev 的唯一源码是仓库 skills/godot-dev；已安装 init 内带构建出的完整副本，不从网络临时拉取第三方技能。
4. 退出码 2 是冲突：审阅原件与 `.bootstrap/proposals/` 并合并可兼容内容；已明确保留的文件逐个 `--keep-existing <相对路径>`。不要跳过所有冲突或覆盖用户文件。退出码 3 只表示 Desktop 等待创建/绑定，继续完整 Desktop 流程；不把它报成成功。其它错误保留恢复依据。
5. 读生成的 AGENTS.md，执行 `tools/check.ps1 -IsolateEditor -ReportDir <run_dir>/checks`（仅标准 Windows Godot 可隔离复制）。验证格式、静态诊断、真实导入/运行和声明的编辑器契约。已有项目无契约时根据实际场景补写，不能套用新工程节点路径。离线文档运行 `scripts/verify_docs.py --path <项目>/docs/godot/<主次版本> --report <run_dir>/docs.json`；online 模式明确没有离线快照。
6. `desktop-wai` 完成实例归属、共享模型哈希、MCP 与新进程/实际开始菜单快捷方式可见性验证；`endpoint` 运行 `tools/comfy_endpoint.py status`、读取节点并验证实际选用的 API 工作流。core 无素材服务验收项。调用 schema 以实际工具为准；不编造宿主/MCP 能力。
7. 保存 `.local/initialization-report.json`：参数及来源、配置档、宿主、工具版本、Godot/文档/素材服务实际证据、未验证项和清理结果。行为、图形输入、音频听感分别记录。初始化完成不等于游戏开发完成。
8. 提取证据并确认任务/进程结束，使用 `init_workspace.ps1 -Action clean -Project <目标> -RunDir <run_dir>` 清理本轮无用文件。只停止本轮启动且队列为空的 Desktop 实例，恢复原应用状态。保留绑定、来源/许可、有效测试、状态/哈希锁、.uid 和导入设置；不整目录清空 work/.local/.godot。

普通开发继续 godot-dev。它也可以单独安装到没有本初始化器的项目。用户只要求讨论/计划时不实施。大任务按授权范围持续完成，真正影响内容或权限且无法推断的选择才询问，继续不依赖答案的工作。

文档更新见 [documentation.md](references/documentation.md)；既有项目与 Desktop 绑定迁移见 [maintenance.md](references/maintenance.md)。
