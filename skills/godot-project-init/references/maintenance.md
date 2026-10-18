# 维护

初始化版本 2.0.0。受管理文件哈希保存在 .bootstrap/state.json；未修改文件可更新，用户修改保留并写入 .bootstrap/proposals/。退出码 2 表示冲突，3 表示已生成项目文件但等待普通 Desktop 实例创建/绑定，1 表示其他错误；desktop-wai 只有完成绑定与验收才能交付成功；core/endpoint 按各自配置档验收。dry-run 不写入。默认 --mode auto：存在 project.godot 时 supplement，否则 new；允许预先存在 Git、README、需求文档与临时工作目录，逐文件保护冲突。显式 --mode new 仍要求空目录或已有初始化状态。supplement 保留项目设置、主场景、测试与需求/架构。

对已经审阅/合并的冲突文件逐个使用 --keep-existing <相对路径>，脚本保留原件并移出受管理文件集合，不把合并后的用户文件冒充模板文件；再次初始化仍需审阅差异。未审阅的冲突不批量跳过。摘要中的 preserve 与 conflict 分别记录已决定保留和仍待处理的文件；完成后删除本轮已解决的 proposal，不留无用候选副本。

scripts/init_workspace.ps1 的 begin 返回本轮 work/init-<随机ID>；clean 仅接受该项目下有匹配标记的单个目录，拒绝 reparse point。随机ID仅用于临时目录，绝不用于 Desktop 实例显示名。验收日志通过 check.ps1 -ReportDir 写到该目录，必要结果提取至 .local/initialization-report.json 后再 clean。摘要不是脚本自动证明的完成状态：Codex 必须填入真实 Godot、文档和项目 MCP 结果，不能因文件生成成功就写全部通过。

## Desktop 创建与项目绑定

本机 JSON 配置（--config 或安装器生成的 local.json）提供现有 desktop_exe、desktop_data 与 MCP/CLI。project_comfyui.py 只读 Desktop 注册表及 settings.json 的 modelsDirs，不创建核心、不启动后端、不修改 Desktop 全局配置。核验实际 ID、standalone 类型、installed 状态、标记、独立 Python、存储开关和端口，再写项目绑定与 WAI/UI 工作流。Desktop 自身安装器负责独立环境、安装标记、版本和快照。优先通过 scripts/desktop_instance.py 调用已验证的内部接口，协议、版本边界及临时连接清理见 [desktop-api.md](desktop-api.md)。

创建步骤见 SKILL.md。通过 Desktop 内部 API 正常新建 Standalone，跳过模板下载；开启共享模型，关闭共享输入/输出，保持独立浏览器会话。直接读取 Desktop 现有共享库中的固定 WAI，核验 SHA256；模型复制字节数为 0，不创建符号链接或硬链接。Python/Torch 环境仍独立占用空间。共享库中的其他模型可以被发现，但初始化只生成 WAI API/UI 工作流。不要改全局共享目录或自动启动偏好。官方依据：[实例管理](https://docs.comfy.org/installation/desktop/usage/instance-management)；Desktop 更新后核对原生接口与实际配置。

实例名称使用 --project-display-name 传入的准确宿主项目显示名称，不加任何信息。CLI 未提供该参数时退回 --name、已有 Godot 名称或目录名；宿主提供项目列表时按路径核对名称；无列表时采用该回退并说明来源。现有实例重名或目标目录已存在时明确处理归属，不自动追加后缀。只更新技能不更名已有实例。

绑定 schema=3，model_storage 保存共享目录、实际 checkpoint 路径、大小和修改时间，model 保存固定 SHA256。首次绑定完整校验，后续连接检查文件状态/目录是否变动；变动后显式重新绑定并校验。多个模型目录存在同名 WAI，或实例内存在同名副本时报告歧义，保留原文件供显式处理。实例归属标记防止跨项目认领。Desktop 改名不影响 ID；路径/端口变更需重绑。项目移动时明确更新归属与本地路径。重跑不复制环境/模型，不覆盖用户 UI 工作流。

Codex 项目 .codex/config.toml 只追加 comfyui_project；Harness 生成 .dsh/comfyui.cordis.yml，需 --patch 加载；均保留同名冲突。官方 comfy-mcp 工具环境复用，CLI 的 USERPROFILE/jobs/cache 单独放在项目 .local/comfyui-mcp；后端用 Desktop 正常环境。MCP 建连前检查监听端口所有者、main.py 和实例 Python，启动后仍通过 server_info/system_stats 检查实际地址，禁止回退全局服务器。实例未运行时先从 Desktop 打开，再连接/重连 MCP；当前聊天可用 call 的真实 stdio 入口。

## Windows 启动与列表可见性

版本 1.6.2 使用 Explorer Shell 启动，不继承 Codex MSIX 的 Desktop 配置隔离。配置读取核对真实文件路径；无包身份不代表无重定向。创建后必须完成新进程及实际开始菜单快捷方式的 verify，再正常 reopen。历史隔离配置通过精确备份、原生 Add Existing 接入和显式重绑新 ID 恢复；tracked 标记只接受已有项目归属且目录唯一的情况。完整步骤与验收边界见 [desktop-api.md](desktop-api.md)。

## 旧项目迁移

v1.3 普通实例可以继续使用原 ID：用户要求迁移具体项目时，在 Desktop 开启共享模型，保持输入输出关闭共享并重启；核验实例内同名 WAI 与共享文件哈希，明确处理本地重复副本后用 setup --installation-id <原ID> 升级绑定。脚本不会自动删除副本或修改共享模型。

v1.2 的 .local/comfyui 是自建后端，需按正常向导创建 Standalone 实例，再迁移项目工作流/素材和必要节点依赖，模型直接使用共享库。迁移前保存配置，队列为空时安全停止旧进程；原后端在验证成功并获得清理授权后删除。仅更新技能不自动迁移已有游戏。

## 验证与交付

涉及实例创建机制时验证真实 Desktop 注册、安装成功、列表、管理及启动，不能仅用测试替身证明接口可用。脚本是版本锁定的内部 API 适配，不是公开稳定 CLI；安装中实例被 Desktop 列表 API 暂时隐藏时，只读注册表核对已记录 ID，不能另建实例。涉及模型路径变更时验证共享 WAI 实际解析、零模型复制、共享输入/输出拒绝绑定、缺失/歧义/修改检测、重复初始化和双项目独立配置。测试替身必须标明，不能冒充真实 Desktop 实例或 MCP 出图。正式项目初始化仍须通过 MCP 预检工作流，按任务要求验证出图及 Godot 检查。清理只针对本次核对路径的临时文件/实例，绝不删除共享库中的模型。

源技能与用户级安装按修改前哈希同步，遇到外部修改保留并报告；不把源模板更新当成安装已更新。历史报告保持原样，新增本轮报告。技能正文保持精简，项目操作细节集中在 docs/asset-pipeline.md。

开发技能模板支持从需求到资源、验证及清理的完整执行。只更新既有项目 dev 技能时，核对文件归属后同步技能、UI 元数据及实际需要的资源流程/验证工具，更新这些文件的受管理哈希；保留项目原初始化版本与其他配置，不冒充已执行全项目升级。新增功能仍由需求驱动，不因技能更新重建实例或预装模型。

## 1.7 编辑器可维护性

规范、godot-dev 和开发文档要求交付可编辑场景、类型化资源、局部信号/API 以及具体编辑入口。新工程生成最小 docs/editor-contract.json；补齐模式保留已有契约，缺失时由初始化流程按真实场景补写，避免对旧工程强加 Main/World/UI 层级。

检查器自动运行 tools/check_editor_structure.gd，真实加载声明的节点/资源并验证 Inspector 属性。缺少契约时明确记录未检查；契约检查不证明未声明部分或编辑体验。功能交付还需用临时副本实际重排布局、替换素材、修改参数并保存/重载，检查运行行为和实例状态隔离，另做视觉验证。纯对象、动态 PackedScene、数据驱动 Tween 等合理用途保留；不使用行数或 new() 数量作为硬门槛。

只升级开发规范时无需重建 Desktop 实例或复制官方文档。先审阅模板和项目差异，再同步所需文件；项目特有的契约和架构由项目维护，不更新为通用模板归属。quick_validate 只检查技能格式；可用真实标题页/卡牌编辑试验验证产物，不能据此保证未来每次模型执行都遵守规范。

## 1.8 社区经验的按需整合

保留单一 godot-dev 入口，递归安装 9 个开发专题及社区审阅/来源记录。来源固定提交，独立编写指导，不安装上游脚本、MCP 或框架。更新源目录时保留用户级安装和现有项目的冲突保护。

运行 `python -B scripts/tests/test_dev_bundle.py` 检查新工程生成、专题链接、幂等计划及用户修改冲突保护；以实际 build_plan 生成目录，不启动 ComfyUI。`scripts/tests/engine_semantics/` 是维护技能的引擎探针，复制到临时工程后用项目同版本引擎和隔离用户目录运行 `test_semantics.gd`，核验 owner、资源复制/磁盘、重入和信号。它们不计入游戏行为测试。针对具体项目仍运行 tools/check.ps1。

独立代理前测未自动执行；community-review.md 的评估题目是后续真实任务评估入口，不能把格式/安装/引擎检查称为代理行为评测通过。
