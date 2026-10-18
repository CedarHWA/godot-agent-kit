# 开发规范与依据

这些是本项目采用的约定。官方并不强制某一套目录、组件框架或固定数量的 Autoload。

## 场景、组合和协作

优先让场景自行完成单一职责。可复用场景只知道自己拥有的节点；父级连接事件并提供外部对象。
场景内部稳定路径和唯一节点名可以正常使用。需要跨场景引用时优先导出引用、明确方法或由父级建立关系。
不要以“解耦”为理由让明确的同步查询绕过全局信号总线，也不要把每一个小数据对象都变成节点。
官方依据：[场景组织](godot/__DOCS_VERSION__/tutorials/best_practices/scene_organization.md)、[场景与脚本](godot/__DOCS_VERSION__/tutorials/best_practices/scenes_versus_scripts.md)、[节点使用边界](godot/__DOCS_VERSION__/tutorials/best_practices/node_alternatives.md)。

## 配置与运行状态

例如多个角色可共享一份 HealthConfig.tres，但当前生命值存于各实例的 Health 节点中。
若资源确实包含可变状态，检查所有嵌套 Array、Dictionary、Resource 的复制深度。
`duplicate()`、`duplicate(true)`、`resource_local_to_scene` 有不同语义；先查当前版本并做两实例行为测试。
不要用“资源已经复制”作为所有嵌套状态都独立的证明。
官方依据：[Resources](godot/__DOCS_VERSION__/tutorials/scripting/resources.md)、[Resource API](godot/__DOCS_VERSION__/classes/class_resource.md)。

## 生命周期和全局服务

明确节点初始化和树内外边界。依赖需要在进入树之前设置还是 _ready 之后使用，应由接口保证。
池化、移除再加入场景、延迟调用和 await 后需要重新判断对象有效性。
Autoload 适用于确实跨场景、独立存在的服务；功能内部对象优先由功能场景拥有。
官方依据：[Autoload 与普通节点](godot/__DOCS_VERSION__/tutorials/best_practices/autoloads_versus_internal_nodes.md)、[Node API](godot/__DOCS_VERSION__/classes/class_node.md)。

## 编码与验证

使用官方 GDScript 命名、缩进和类型指南；文件/目录 snake_case，类型和节点 PascalCase。
`gdformat`/`gdlint` 只是辅助工具；新语法支持滞后时记录限制，不为适配 linter 随意降低引擎功能。
本项目默认附带独立的 SceneTree 冒烟脚本，避免空项目先依赖大型测试插件。业务测试增长后可引入固定兼容版本 GUT。
用真实输入、状态变化、信号结果验证行为。图形、交互、音频另外验证；不要宣称 headless 已覆盖它们。
官方依据：[GDScript 风格](godot/__DOCS_VERSION__/tutorials/scripting/gdscript/gdscript_styleguide.md)、[命令行](godot/__DOCS_VERSION__/tutorials/editor/command_line_tutorial.md)。

## 可维护性

实现前先明确本次功能的场景/内置节点、配置和状态边界，再随可运行切片提炼有证据的复用点。独立编辑或生命周期也能成为拆场景的理由，不必等到出现第二个使用者。没有需求不引入 ECS、消息总线、服务定位器或通用存档框架。
需求变更时先找到该行为由哪个场景/资源拥有，再修改最小职责边界；公共接口变更同步调用方。
架构决定记录动机和影响，不记录会快速过时的逐行实现说明。
官方依据：[项目组织](godot/__DOCS_VERSION__/tutorials/best_practices/project_organization.md)、[版本控制](godot/__DOCS_VERSION__/tutorials/best_practices/version_control_systems.md)。


## 编辑器可维护性的实施与验收

本项目把“用户能在 Godot 编辑器中理解和修改”作为交付结果。先在架构里列出本次功能的场景、配置 Resource、运行状态及事件方向，再实现；不要先写完一个脚本生成器，最后只补一个空场景壳。

固定界面保存在 `.tscn`；例如标题页的按钮、文字和间距应在场景树中可见。动态牌组、敌人或列表可以用 PackedScene 实例化，源场景包含完整外观。可复用组件拥有自己的节点路径，对外用事件信号及命令/查询；组装层不依赖组件内部层级。

配置保存为有类型的 `.tres`，直接引用 Texture2D、AudioStream、PackedScene 等；用 `@export`、分组、范围和注释暴露真正需要调节的参数。运行状态不写回共享资源。Theme、StyleBox、字体和固定编排动画也优先保存为资源；数据驱动 Tween、过程生成、运行时声部池以及纯计算对象有合理用途，不一概禁止。

实现完整功能时读 godot-dev 的场景资源专题，对照内置能力表再选择自定义方案。棋盘、HUD、独立面板等组件拥有内部表现和交互，父级协调流程；只把节点搬到子场景而继续由父级逐个控制不算形成边界。纯规则可继续独立为 RefCounted，脚本不必一一对应场景。

每个可调值有明确来源和消费者：例如布局计算读取 Theme/导出间距，文案读取对应资源，玩法按键来自 InputMap。运行推导的尺寸/文本不冒充编辑入口。自绘允许保留，但应能修改相应样式/几何参数并查看样例；手工关卡的整数数组/位掩码还需说明、校验与可见布局预览，不能仅靠可序列化宣称容易制作。

验收同时检查三个层次：
1. `docs/editor-contract.json` 声明需要预先存在的场景节点及正式资源；`tools/check_editor_structure.gd` 由检查器自动运行，用真实 Godot 加载并验证。它检查声明的契约，不自动证明整个项目的架构正确。
2. 审阅本次每个主要组件的编辑入口与实际消费者，再按风险做无脚本编辑试验：完整页面/功能覆盖重排固定控件、替换素材、调整设计参数，保存到本轮临时副本并重新加载/实例化；纯规则修复不制造无关 UI 测试。观察 ready、布局刷新及相关动画之后的结果，排除常量覆盖配置，并检查两实例隔离；无需为每个属性建立重复测试，也不能用一个标题控件代表所有组件。
3. 查看实际页面/编辑入口，确认布局、素材和参数可找到、修改有效。headless 不代替画面检查；报告未验证项。交付一张简洁的“要改什么 → 打开哪个场景/资源”表。

`.new()`、长脚本和跨节点路径是审阅线索，不能仅凭计数否决有效设计。新增自动检查应测可观察结果，而不是要求出现某个关键字；例外写明用途、编辑入口及验收方式，无需单独审批。

## 开发技能的按需资料

项目自动安装一个 godot-dev 入口及其 references。按当前功能读取场景资源、生命周期、UI 输入、动画音频、存档加载、调试测试或性能专题；素材生产继续以本项目 asset-pipeline.md 为准。来源审阅和固定版本清单在技能 references/community-review.md 与 sources.json，仅追溯技能依据时读取。无需每轮手动指定所有专题，也不自动安装第三方框架。

## 目录组织：按类型＋功能子目录

这是项目的查找偏好，不是 Godot 的架构限制。`scenes/garden/card/card.tscn` 与 `scripts/garden/card/card.gd` 使用对应的功能路径；纯规则和 Resource 类脚本也放 scripts，无需为了对称而创建空场景。配置实例放 `resources/levels/`、`resources/cards/` 等用途目录；图片、音乐、音效、字体放 `assets/images/`、`assets/audio/music/`、`assets/audio/sfx/`、`assets/fonts/`。Godot 将媒体也视为 Resource，这里的命名只为查找方便。

每个功能仍由场景拥有内部节点、用 Resource 提供编辑参数、通过方法和局部信号协作；分目录不意味着运行时拼接路径或在脚本中生成固定页面。tests、tools、docs 分别保留测试、工具和文档；第三方插件可保留 addons 内的自包含结构。仅创建实际用到的目录，避免无需求的空框架。

移动现有工程必须同步项目设置、场景/资源/脚本引用、动态路径、测试、工具、编辑指南和素材清单；保留 .uid、导入 UID 与导入参数。验证无旧缓存的新副本可以导入、加载与运行，且媒体哈希、设计数值和场景结构未变。历史验收报告保留当时路径，用迁移映射追溯。
