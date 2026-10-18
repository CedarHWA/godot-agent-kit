# Desktop/WAI 完整流程（仅 desktop-wai profile）

主入口 SKILL.md 的宿主、配置、profile 选择优先。以下保留完整 Desktop 创建、可见性验收与恢复要求。所有 init_project.py 命令追加 --profile desktop-wai --agent <宿主> --config <本机配置>。不要求 Harness 提供 Codex list_projects；宿主无列表工具时使用已确定的项目名。local.json 是安装器可选生成的本机文件，也可显式传 --config。

# Godot 项目初始化

初始引擎 4.7.2，附带完整 Godot 4.7 文档。每个项目由 **Comfy Desktop 自身安装流程**创建普通 Standalone 实例，再绑定实际 ID，显示在 Desktop 实例列表中。通过 Explorer Shell 启动与已验证的脚本接口调用，无需 computer-use。创建前检查实际配置路径，绑定后必须重启并验证开始菜单快捷方式打开时的实例列表。实例显示名称与 宿主项目显示名称完全一致，不加前缀、日期、随机串或后缀。模型共用 Desktop 现有目录；Python 依赖、节点、工作流、输入输出及 MCP 配置按项目隔离。初始化只生成 WAI-illustrious-SDXL 文生图工作流。

## 一句话执行

用户选中此技能并说“请帮我初始化这个项目”，就执行完整初始化，不只给计划、命令或模板，也不要求用户逐项重复提供可推断的参数。不因需求文档尚未写好而停止；只建立最小入口与基础环境，不替用户设计玩法。

- 目标优先采用用户指定路径，其次当前宿主项目/工作目录；在该目录直接处理，不额外嵌套同名游戏文件夹。已有 project.godot 自动补齐；否则新建。已有 Git、需求文档或 README 不代表不能初始化，保留并整合它们。多个候选项目无法确定时再询问。
- 参数优先级：本次明确要求 → 已有项目/初始化状态 → 需求文档中明确的约束 → 本机基线。没有这些信息的新项目默认 Godot 4.7.2、2D、Compatibility、Windows；在结果中说明实际采用的默认值，不为普通默认值单独求确认。补齐时保留引擎设置、入口和目录；文档版本必须匹配，不静默迁移。
- 宿主提供项目列表时（如 Codex list_projects），按规范化路径核对显示名，传入 --project-display-name，实例名称完全一致。没有宿主项目列表或尚未登记时采用用户给定名称、已有 Godot 名称或目标目录名，并说明来源；不能把聊天标题冒充项目名。路径/名称有实际歧义、未解决的文件冲突、应用重启涉及未保存内容或权限阻止时，提出具体问题并继续不受影响的工作。

## 执行到完成

1. 读取项目及上级 AGENTS.md、已有 project.godot 和相关需求，按上述规则确定参数。不在盘符根目录新建任何内容。
2. 读取本技能 local.json，验证已有 Godot/Python、Desktop 程序/数据目录及 MCP 工具。读取 Desktop 的共享模型目录配置，定位并校验现有 WAI；模型缺失时报告实际缺项，不复制权重、不自动重下载。复用 Desktop 与安装缓存，独立创建实例的 Python 环境。Desktop 正常创建可能需要联网更新核心。
3. 使用 scripts/init_project.py --path <目标> --mode auto --name <游戏名称> --project-display-name <Codex项目显示名称>，只为已确定的其他参数传值。先加 --dry-run 查看计划。再运行 scripts/init_workspace.ps1 -Action begin -Project <目标>，保存返回的 run_dir；本轮测试、请求副本、下载解压及检查日志集中放在其中。执行初始化；已授权的步骤不再索要确认。
4. 脚本生成规范、dev 技能及全部按需 references、文档、WAI API/UI 工作流。开发入口保持一个 godot-dev，不预装第三方技能框架。未绑定时退出码 **3**，并生成 .local/comfyui-request.json 的建议名称、安装父目录和空闲端口；这是中间步骤，继续完成以下 Desktop 创建流程，不能就此宣称初始化完成。已绑定项目复用原 ID，不另建实例。
5. 按 [Desktop 脚本接口](desktop-api.md)，使用现有 MCP 工具 Python 运行 scripts/desktop_instance.py 的 open → probe → create → status。open 必须走随附 Explorer Shell 启动器；不能直接 Start-Process/Popen 启动 Desktop。发现 MSIX 配置重定向先按该参考恢复，不继续创建。它调用 Desktop 的 buildInstallation/addInstallation/installInstance，选择稳定版 NVIDIA、跳过模板，并设置共享模型、独立输入输出/浏览器会话及唯一端口。Desktop 完成安装后，以原初始化参数加 --desktop-instance <实际ID> 重跑，核验共享 WAI 哈希并绑定项目。已有同名实例/目录不自动加后缀或认领；先核对归属。接口版本不兼容时明确报告，用户选择后再使用正常向导等备选方式；禁止直接伪造注册表或复制旧环境冒充新实例。
6. 退出码 2 表示用户文件冲突：审阅原件与 .bootstrap/proposals/，自动合并可兼容内容。对已经审阅、保留或合并好的文件，重跑时逐个加 --keep-existing <项目相对路径>，保持它们由用户管理；不能不看内容就跳过全部冲突。无歧义的合并不需要用户逐项批准，真正无法兼容的选择再询问。其他错误保留恢复依据；旧后端迁移见 references/maintenance.md。
7. 阅读生成的 AGENTS.md，运行 tools/check.ps1 -IsolateEditor -ReportDir <run_dir>/checks（IsolateEditor 适用于本机标准 Windows 引擎）。已有项目缺少可运行入口时补齐必要入口；已有入口不改写。用 scripts/verify_docs.py --path <项目>/docs/godot/<主次版本> --report <run_dir>/docs-check.json 验证正文、索引、链接、版本锁和许可证。架构遵守节点、场景、信号、Resource 与组合优于继承。生成的 AGENTS.md、godot-dev 和 development.md 必须包含编辑器可维护性验收；确认 dev 的任务表链接、全部专题和来源清单已随目录递归安装，不能只复制 SKILL.md；check_project.py 自动执行 editor-contract 的真实场景/资源加载检查。初始化仅声明最小入口契约，不替用户预建业务框架；后续功能由 godot-dev 扩展契约并验证无脚本编辑。补齐已有工程时保留其契约；缺失时根据真实入口和可编辑节点补写，不套用新工程 Main/World/UI 的路径。
8. 使用 desktop_instance.py start 从 Desktop 启动绑定实例，运行项目 tools/project_comfyui.py status 核对端口监听进程、main.py 和独立 Python。通过项目 MCP 的 server_info/system_stats、validate_workflow 验证 WAI API；需要出图时通过 MCP 生成并检查。当前会话未加载新 MCP 时使用 project_comfyui.py call 真实 stdio 入口，不连接全局 comfyui 或另起后端。
9. 按 desktop-api.md 执行 verify → close → 通过实际开始菜单快捷方式 open → verify，核对跨进程可见性、真实配置路径与同一实例 ID；结束临时接口并用 reopen 恢复正常启动。按下节保存验收摘要并清理。正式绑定、重启后列表可见、Godot 检查、文档校验、实际项目 MCP 预检均通过才称“初始化完成”。受阻时说明完成部分、实际阻碍及恢复入口，不用静态检查代替 MCP 或假装已创建实例。交付项目位置、实际参数、Desktop 名称/ID/位置、验收摘要和 $godot-dev 用法。

## 目录和收尾

- 按生成的 README 目录表组织：根目录保留 project.godot 和简要规则；新项目默认按类型＋功能子目录组织，入口为 scenes/main/main.tscn，脚本为 scripts/main/main.gd。scenes 放场景、scripts 放脚本、resources 放配置、assets 按媒体类型和用途放素材；docs 放需求、架构、官方文档和素材来源，tools 放开发工具，tests 放有效测试。目录分类不改变场景和资源优先、局部信号与 Inspector 编辑规范。不预建大量空目录；已有项目沿用其清晰结构，不无故搬迁文件或改资源路径。
- 在 `.local/initialization-report.json` 保存一份紧凑摘要：实际参数及默认值来源、实例 ID/路径、共享模型目录、Desktop 启动方式/真实配置路径/跨进程及快捷方式列表可见性、Godot/文档/MCP 的真实验收结果、未验证项和清理结果。将要删除的测试日志中必要证据提取到摘要；失败原因和恢复所需文件尚有用途时保留并说明。
- 测试启动的实例在队列为空时通过 Desktop stop 停止；关闭本轮临时调试端口并按 desktop-api.md 恢复 Desktop 原来状态。正式项目实例及共享模型保留。
- 先确认任务/进程已结束，再执行 `scripts/init_workspace.ps1 -Action clean -Project <目标> -RunDir <run_dir>`；脚本验证所属标记、范围和目录连接，不扫描删除其他工作目录。本轮已解决的 proposal、完成绑定后失去用途的请求副本/调试会话记录、空测试目录也逐一核对后清理；创建记录在安装未完成时用于恢复，不可先删。不要删除其他任务的日志或文件。
- 保留 `.bootstrap/state.json` 和版本锁、`.local` 的正式绑定/工具链/MCP 数据、`.codex` 配置、文档、有效测试、正式工作流、素材与许可记录，以及 `.uid`/导入设置；不把整个 .local、.bootstrap、.godot 或共享安装缓存当作垃圾删除。清理后检查本轮临时清单并更新摘要，不能仅宣称“已清理”。

## 边界

- 初始最小 Main/World/UI，不预建万能管理器、全局事件总线、ECS 或业务框架。
- 补齐模式保持已有项目设置、主场景、测试和需求/架构；旧项目里的旧资源包不会自动删除，但新 dev 指令只使用项目实例。合并冲突后才能认为新规则生效。
- 当前附带 4.7 文档；其他主次版本先按 references/documentation.md 制作和验证匹配快照。正文按需读取，不能整库塞入上下文。
- Standalone 实例的核心、Python/依赖、节点和用户数据独立；权重直接从共享模型目录读取。后续节点依赖只安装到绑定实例；共享权重按版本命名，避免覆盖或删除其他项目使用的文件。实例在 Desktop 正常安装目录；项目内保存绑定、工作流和 MCP 数据。迁移路径/端口或更改共享目录后显式重新核验绑定；只改实例名称无需重建。
- 仅新增项目级 MCP 配置，不改全局 Codex/ComfyUI 设置；项目受信任并重新加载后才能在 Codex 发现该 MCP。当前聊天可先使用 stdio 入口，不宣称热加载已经完成。

文档同步见 [documentation.md](documentation.md)，维护与验证见 [maintenance.md](maintenance.md)。资源生产细节只在生成项目的 docs/asset-pipeline.md 维护。
