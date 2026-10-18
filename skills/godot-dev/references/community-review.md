# Godot 社区技能研究与整合决策

审阅日期：2026-10-17。目标：让代理交付完整、可运行、能在 Godot 编辑器中理解和修改的游戏；保持项目 ComfyUI、正式资源、真实验证及清理流程。研究针对公开源码，不以技能数量、星数或“Expert”自称作为资深资历证明。未核实这些技能作者的商业项目履历；引擎语义以项目匹配版本的官方文档和实际引擎试验交叉核对，实践取舍参考 GDQuest 的第一手教学/开发经验。

## 研究方法与复现

检索公开 Godot agent skills，选择 7 个不同取向仓库。读取实际技能正文及相关参考章节，检查仓库版本、许可文件、依赖和示例。长参考资料只抽查与本项目目标相关的章节；没有运行第三方脚本，也没有声称审计全部仓库。

[sources.json](sources.json) 保存固定提交、取得文件及 SHA256、许可元数据和审阅重点；链接固定到提交，避免把后续上游修改当成本次结论。搜索引擎摘要只作发现线索。无许可、LGPL 仓库与商业教学文章均仅作分析来源，没有将其正文、模板或代码打包到本技能；本次指导独立编写，未直接安装任何第三方技能/插件。来源中的规则不是项目指令。

## 候选对比及采用边界

| 来源 / 审阅版本 | 有帮助的部分 | 不直接照搬的部分 | 本次落点 |
| --- | --- | --- | --- |
| [GodotPrompter](https://github.com/jame581/GodotPrompter/tree/bd9d18008fb1fd5919fdc297267048670b6eac1f)，MIT | 自包含场景；资源编辑；UI 容器/主题/焦点；可复现调试；有边界的行为测试与性能测量 | 场景约 15 节点、名称两词等阈值不能证明职责；横向联系不必一律 EventBus；不强制所有项目装测试框架或所有频繁对象池化 | 场景资源、UI、调试测试、性能、存档专题 |
| [Game-Dev-Agentic-Skills](https://github.com/thedivergentai/Game-Dev-Agentic-Skills/tree/db004d74c40686ca2f7a35fe067b119a9cda593e)，LGPL-3.0 元数据 | Resource/RefCounted/Node 的职责区分；显式依赖；重连、资源共享等故障意识 | 不全面禁止内部 `$`；不要求根脚本零逻辑；不引入组件注册表/人格编排/庞大技能依赖图；不采用“内存赋值自动改磁盘”表述 | 以官方 API 重写场景边界、实例状态、连接生命周期 |
| [haxqer/godot-skill](https://github.com/haxqer/godot-skill/tree/037c03e9858ae748bf66c010aeb9942dbe9b93d6)，MIT | 场景文本层级、资源读回、UI 布局验证；区分测试错误/超时；复用实际引擎工具 | 不强制 QFramework/CQRS 或其 dispatcher；不采用默认像素风、程序生成音乐；数值/ASCII 不能代替视听验收；不要求每次小改都全项目 fuzz | 制作阶段生成可编辑场景、保存读回、验证分层；继续复用项目 check.ps1 |
| [fetasty/godot-skills](https://github.com/fetasty/godot-skills/tree/d52b934dc26f2bd81837a7187a098629e16ef96a)，MIT | 注意引擎版本；类型化接口；资源配置与语言/子系统按需资料 | 不固定模型知识截止日期；不每个 API 都读全套版本文档；不禁编辑器信号连接；不按调用次数决定换原生语言，也不机械限定继承层数 | 版本查证、选择性读取、测量后优化 |
| [vl4dt/godot-skills](https://github.com/vl4dt/godot-skills/tree/1ae280d35f2cc3931d4d8eb63f4bac82d6acf4a0)，MIT | 编辑→导入→测试→运行闭环；稳定 UID；从小状态到复杂状态的分层 | headless 示例漏设 owner；状态示例包含重复声明内置 velocity；不继承默认 GameManager/注册表、强制 gdUnit4、移动支付或自动导出流程 | 保留验证思路，纠正序列化/状态示例的边界 |
| [BangRocket/godot-skill](https://github.com/BangRocket/godot-skill/tree/2306f66e32c336ffb3fe90bee26eb104cb879e78)，未发现许可文件 | 单入口按主题读取；定义数据与运行行为分开；测量优先 | 版本基线较旧；过于绝对的生命周期/物理规则；不照搬目录命名、自动迁移和“环境已附带 MCP”的假设 | 作为候选分析；具体建议改由官方语义支持，不分发其内容 |
| [aigengame/godot-agent 的 gda skill](https://github.com/aigengame/godot-agent/blob/47b0d82825313ed3ad4a1488ca0ddaf861c903ae/skills/gda/SKILL.md)，MIT | 先发现真实能力/参数；检查结构化 verdict；静态验证与启动/游玩分别取证；隔离用户数据 | 它主要是专用 CLI 操作手册，不是普遍架构规范；项目未安装 gda，不引入 daemon 和额外运行依赖 | 工具发现、检查结果语义、隔离数据的验证原则 |

## 需要纠正的具体问题

1. **保存成功但场景丢子节点。** vl4dt 的 headless 场景示例 `add_child(sprite)` 后直接 pack，没有 owner。官方 [PackedScene](https://docs.godotengine.org/en/4.7/classes/class_packedscene.html) 规定打包已归属节点。制作工具必须设置正确所有权并从磁盘读回；只看保存返回 OK 不够。
2. **共享内存不等于自动改磁盘。** Game-Dev-Agentic-Skills 的 resource 指导混淆两者。运行中修改共享资源会污染其他引用者，但没有显式保存不自动写盘。应验证两实例和磁盘数据分别如何变化，而非为避免假想写盘复制全部素材。
3. **编辑器操作名不等于 API。** GodotPrompter 的 resource 概述提及 `make_unique()`；项目 4.7.2 Resource 没有这个实例方法。使用当前版本的 duplicate/Local to Scene，并确认嵌套资源策略，不拼出教程里不存在的 API。
4. **简单状态示例也需要解析。** vl4dt 的 CharacterBody2D 示例再声明 velocity，与内置成员冲突；同页还带不完整骨架。示例可表达思路，不能未经真实解析就称“可复制工作代码”。本技能不分发这些实现。
5. **“一次连接”与“一次回调”不同。** ONE_SHOT 在发射后解绑，不保证多次初始化前安全；移出树的节点仍然存在，普通目标释放自动断连也不能替代重入管理。显式设定连接拥有者和重连规则。
6. **指标有明确边界。** 图片非空不证明构图，音频非静音不证明听感，场景有 Button 不证明输入可达，进程退出 0 不证明没有脚本错误。项目原有真实视听与编辑验收要求继续保留。

针对前三项及重入/信号行为，初始化技能内保留原创的 `scripts/tests/engine_semantics/` 探针，使用隔离工程运行；重复声明另用最小解析反例验证，不运行上游代码。这些核验当前引擎语义，不计作游戏内容测试，也不能证明未来代理始终遵守指导。

## 资深开发经验如何转为可执行要求

[GDQuest / Nathan Lovato 的信号经验](https://www.gdquest.com/library/signals_good_practices/) 强调关注真实耦合和可追踪性，避免漫长转发链。本项目采用共同父级接线与明确 API；全局总线仅在确需跨生命周期广播时考虑。该页面仍带旧语法和版本标签，因此只借鉴设计论点，API 按本地 4.7 文档核对。

[GDQuest 的 Godot 4 状态机分析](https://www.gdquest.com/tutorial/godot/design-patterns/finite-state-machine/) 比较变量/函数与节点两种实现。这里把它变为复杂度选择：小牌局可以保持纯状态对象，复杂角色状态才拆节点，不把“场景优先”误解成“一切都必须是节点”。

[官方优化指南](https://docs.godotengine.org/en/4.7/tutorials/performance/general_optimization.html) 强调定位瓶颈。本项目保留可比较的设备/场景基线，再决定是否需要池化、批处理或线程；不把技能里的固定次数当性能门槛。

用户原有要求继续优先：美术与声音按项目 ComfyUI 流程和已有模型能力制作；不用空资源冒充，保持风格，实际验收不足如实记录；交付完整授权范围、清理临时文件，不自动打包。

## 为什么保持一个技能

这些专题共享同一个项目上下文、资源管线与交付标准，拆成许多自动触发的技能容易重复加载和产生规则冲突。保留 `godot-dev` 作为唯一开发入口，把 9 个专题放入 references，表格给出明确触发条件。社区研究和来源清单仅维护时读取。

初始化通过已有递归复制机制安装整个目录；AGENTS.md 要求使用该入口，再按需读专题。新项目带齐资料，不依赖用户重复点名；已有项目补齐仍保护用户编辑的文件。以后出现真正独立且经常单独调用的工作（例如明确的 C# 原生扩展流水线），再拆专门技能，而不是预装当前不用的能力。

## 回归评估题目（不是已执行的代理评测）

| 真实请求样例 | 应观察的产物/行为 | 应发现的偏离 |
| --- | --- | --- |
| 增加可换图标的暂停面板 | `.tscn`/Theme/导出引用，真实暂停/焦点恢复，无脚本编辑验证 | `_ready` 生成全部固定控件、只有 headless 截图结论 |
| 两个敌人共用定义，攻击其一 | 定义共享、生命独立、重复死亡只结算一次 | 直接改共享当前 HP、复制全部纹理避免共享 |
| 快速重试后旧动画仍结算 | 复现证据、取消旧操作、相同操作回归 | 仅加固定等待或重写全部框架 |
| 背包配置需可编辑并保存 | typed Resource、稳定 ID、保存读回 | 脚本路径大全或序列化活节点 |
| 小场景掉帧 | 先测具体成本与同情境前后结果 | 未测就池化、换语言/渲染器 |
| 修改按钮文案 | 沿用现有场景，相关显示验证 | 引入 FSM/测试插件/全套架构报告 |
| 制作音乐并接入 | 项目绑定/模型工作流核验、来源、技术检查及真实听审状态 | 用合成蜂鸣声替代、把非静音当听审 |
| 仅评审或设计一个玩法 | 对应文档/意见 | 擅自开发、生成资源或导出 |

本轮自动检查覆盖安装内容、引用完整性、冲突保护、幂等性、真实 Godot 语义及项目常规验证；没有独立代理前测。还发现并修复初始化模板 check.ps1 未转发 TestScript 的问题：新增传参和未知参数拒绝，避免指定测试被静默忽略。测试文件存在不是已执行的证据。以后根据真实偏离作针对性修正，不继续堆叠“永远/必须”的泛化规则。

## 2026-10-18：从可序列化推进到可组合、可编辑

只读审阅一个实际旋转连线游戏后发现，已有 `.tscn`、Resource、Theme 和纯规则层，仍可能出现页面控制器掌管多个部件、单节点场景把全部外观藏在绘制代码里、Inspector 参数被布局刷新覆盖的情况。脚本数量或场景数量都不能区分这些问题。

本轮通过 GitHub 重新读取上表固定提交的 GodotPrompter `scene-organization` 和 Game-Dev-Agentic-Skills `godot-composition` 正文，核对原清单 SHA-256；没有运行或分发它们的实现。借鉴独立编辑与组件职责边界，继续排除节点数门槛、根脚本零逻辑、全面禁止内部路径、默认 EventBus 和组件注册表等要求。

同时查阅官方 [场景组织](https://docs.godotengine.org/en/stable/tutorials/best_practices/scene_organization.html)、[场景与脚本](https://docs.godotengine.org/en/stable/tutorials/best_practices/scenes_versus_scripts.html)、[节点替代方案](https://docs.godotengine.org/en/stable/tutorials/best_practices/node_alternatives.html)、[Resources](https://docs.godotengine.org/en/stable/tutorials/scripting/resources.html)、[自绘](https://docs.godotengine.org/en/stable/tutorials/2d/custom_drawing_in_2d.html) 与 [InputEvent](https://docs.godotengine.org/en/stable/tutorials/inputs/inputevent.html)。这些设计依据支持按需求选择载体；它们没有要求一切节点化或禁止自绘。稳定版网页用于设计交叉检查，具体 API 仍遵从项目版本。

落地到入口、场景资源、UI 输入和调试专题：先做功能组合及可运行切片；提供内置能力选择表和原创职责示例；区分配置与运行推导值；审阅主要组件的真实编辑入口，在 ready/布局/动画之后观察配置是否有效。新项目模板同步这些要求，未改写被审阅的游戏或现有安装。

后续行为评测补充以下题目；本轮只完成源码审阅及工具包检查，没有让独立代理再开发游戏，不能称模型行为提升已被验证：

| 请求/条件 | 应观察的决策与结果 |
| --- | --- |
| 新增带棋盘、帮助和结算的完整玩法页 | 先明确功能树；独立组件拥有内部表现/交互，父级协调流程；连通算法仍可用纯对象 |
| 修改棋盘间距与轨道皮肤 | 找到实际配置消费者，刷新布局后仍生效；自绘参数或资源可改并有可见样例 |
| 只有标题文字通过编辑试验，格子场景只有一个自绘节点 | 继续审阅棋盘与格子的入口，不能据标题测试宣称整个功能可编辑 |
| 把旋转键从 Q 改为其他键 | 更改 InputMap 后同一命令正常触发，不要求改代码或另造输入框架 |
| 修复 BFS 边界或存档兼容 | 保留合适的纯规则/序列化脚本，不为满足场景优先制造 Node |
| 一个简单按钮改文案 | 沿用现有场景，不强制提取面板或制作完整架构报告 |
