# Godot 原生组合指导修订

日期：2026-10-18。范围：开发技能、后续项目模板与维护文档。只读审阅用户指定的 `test-4`；没有运行该游戏、启动其编辑器、更新项目技能或本机安装。

## 观察与判断

游戏有 10 个 `.tscn`、16 个业务 `.gd`、9 个 `.tres`（不含测试/工具脚本和媒体）。已有 Main 组装、动态 PackedScene 实例、关卡 Resource、Theme、音频总线及独立 PuzzleState。不能把“脚本单独存放”或脚本较多直接等同于没用 Godot。

以下路径均相对于被审阅的游戏，仅记录证据，不是本仓库的修改目标。行号对应本轮读取版本；数量只帮助定位，不是质量阈值。

| 证据 | 意义与优化方向 |
| --- | --- |
| `scripts/game/game_screen.gd` 共 531 行；`scenes/game/game_screen.tscn` 有 72 个节点声明，其中一个是 ConfirmDialog 子场景实例 | 页面脚本同时负责棋盘创建/布局/选择、HUD、帮助、暂停与结算。问题是职责与编辑边界集中，适合评估 BoardView、独立面板等组合，不是超过行数就拆分 |
| `scenes/game/tile.tscn` 是一个 Control，内嵌四个 StyleBox；`scripts/ui/tile.gd:137` 起自绘轨道、灯源、目标、选中和提示框，未标注 `@tool` | 自绘轨道有合理性，颜色和 StyleBox 已可调；但图形比例、线宽、图标形状及反馈时长仍在脚本，缺少编辑状态的样例预览路径。应提供适当资源/参数或拆表现节点，不一律禁止自绘 |
| `scripts/game/game_screen.gd:202` 的布局方法写入固定间距 8、格子尺寸上下限 64/132 和棋盘最小尺寸 | `docs/editor-contract.json` 声明 BoardPanel.custom_minimum_size 可在 Inspector 编辑，只能证明属性存在；运行时算法会重新写值。编辑指南应指向真正被算法消费的上游参数 |
| `scripts/game/game_screen.gd:486` 用 `match key.keycode` 处理旋转/提示等；project.godot 没有自定义 `[input]` 段 | 玩法动作可由 InputMap 承载，语义映射不应只能修改脚本；无需因此增加未要求的改键菜单 |
| `scripts/data/level_definition.gd` 导出位掩码数组并校验；`scripts/rules/puzzle_state.gd` 为 RefCounted | 规则与定义已分离，应保留。手工关卡编辑可进一步提供布局预览和字段解释，不强制改成物理节点或 TileMap |

上述为静态结构及调用路径判断；没有对游戏做新的输入、视听或编辑器运行验收。原项目报告中的测试不计作本轮执行。

## 技能改动

- 入口从泛化的“场景/资源可编辑”推进到可执行顺序：功能与载体对应 → 落地场景组合 → 可运行切片 → 行为脚本与扩展。小修沿用原边界。
- 场景资源专题增加内置功能选择表、组件提取条件、原创旋转连线结构示意，以及纯规则/自绘/过程生成的适用边界。
- UI 专题明确 InputMap、布局参数来源和面板内部职责；测试专题检查保存/重载之后、ready/布局/动画运行之后的实际消费者。
- 后续生成项目的 AGENTS.md、development.md、architecture.md 同步核心要求。未改安装器、宿主发现、Comfy/Desktop 行为或官方文档快照。

来源及固定版本核验见 [社区研究](../skills/godot-dev/references/community-review.md) 与 [来源清单](../skills/godot-dev/references/sources.json)。采用官方场景/资源设计原则，分析两份社区技能的职责划分；未复制第三方代码或模板，未加入依赖。

## 验证边界

仓库检查验证技能格式、引用、分发与初始化工具；真实 Godot 集成检查在仓库拥有的临时工程执行，与只读游戏隔离。它们不能证明后续模型必定形成良好组件边界，也不能替代新游戏的交互与编辑器验收。社区研究中保留下一轮行为评测题目，不把题目当已通过测试。

本轮实际结果：

- `powershell -NoProfile -ExecutionPolicy Bypass -File tools/check.ps1 -Godot <本机 Godot 4.7.2 绝对路径>`：通过。首次沙盒运行被回环 HTTP 权限和 junction 创建限制阻断；取得执行权限后重跑，67 项回归全部通过，真实引擎导入、场景结构加载、冒烟运行、离线文档和隔离安装集成通过。未改测试绕过限制。
- 技能创建工具的 `quick_validate.py skills/godot-dev`：以 Python UTF-8 模式运行通过。仓库校验通过，含 1,722 个分发文件及 1,596 页原始文档完整性检查；`git diff --check` 通过。
- 被审阅游戏的 69 个源码/场景/资源/测试、入口及相关 sidecar 文件前后 SHA-256 一致。未运行该游戏或其工具；未同步本机技能、导出游戏或发布工具包。
- 紧凑执行证据保存在忽略提交的 `.local/native-composition-review.json`。本轮临时研究文件和日志在提取证据后清理；原版本验收文档保持不变。

没有执行独立代理生成游戏的行为前后对照、宿主发现专项 smoke 或新的 Desktop/WAI 真实操作验收；本轮未改变这些运行机制。
