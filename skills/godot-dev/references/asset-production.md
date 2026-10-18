# 项目素材生产

仅在需要制作或替换素材时读取。优先遵守项目已有 docs/asset-pipeline.md；没有该文档时，根据用户指定工具与当前实际绑定建立本次必要的资源记录。本页负责接入与质量边界。

## 按需制作素材

先检查任务是否需要新素材、项目现有素材能否满足；无需生成时不启动 ComfyUI。需要时读取已有 docs/asset-pipeline.md、docs/asset-policy.json 与素材服务绑定。desktop-wai 使用 .local/comfyui-instance.json；endpoint 使用 .local/comfyui-endpoint.json 和 tools/comfy_endpoint.py；没有这些文件时先确定用户现有服务，不默认创建 Desktop 实例。以下 Desktop 启动要求只适用于 desktop-wai：

- 根据用途选择图片生成/编辑、音乐、音效或 TTS；先检查绑定实例的节点、项目工作流及共享模型库。初始化只保证 WAI 基础文生图；其他模型已存在不等于本项目对应节点和工作流可用。
- 先运行 tools/project_comfyui.py status；绑定有效且已运行时直接复用。需要启动时，按项目 docs/asset-pipeline.md“自动启动与恢复”调用 godot-project-init 的 desktop_instance.py，由配套 desktop_launch.py 经 Explorer Shell 启动 Desktop，再调用原生接口启动绑定实例。此流程不使用 computer-use，不直接从 Codex 子进程启动 Desktop exe。当前聊天未加载 comfyui_project 时，用项目 call 的真实 stdio 入口；配置重定向、绑定无效或接口不兼容先定位问题，不改连全局实例或另建实例。
- 没有安装初始化技能的 Desktop 自动化脚本时，复用项目已有的受支持启动入口或已运行实例；确需该原生自动化时再安装 init 运行资源，不将其作为普通开发前提。endpoint 项目用自己的 CLI 或已配置 MCP，不调用 Desktop 生命周期。
- 先验证模型、节点、输入和工作流，再通过实际 MCP 或项目 CLI 提交、等待、取回。记录 prompt_id；超时后先查询原任务，不能直接重复提交。根据实际质量调整；达到验收条件即停止，重复失败先排查原因，不无限生成。
- 角色沿用本项目参考图/设计约束，配音沿用本项目音色档案；同一 GPU 的重任务串行，按实际空闲显存从小批次开始。模型与工作流按实际需求选择，不绑定其他项目的地址、角色或音色。
- 直接复用共享权重；新增节点/依赖仅进入绑定实例，正式工作流放 tools/comfyui/workflows/。确需扩展时核验来源、版本、许可和资源占用，遵守已有授权与用途。许可缺失标为未核实，不将开源或生成成功推断为可商用。
- 检查输出质量并处理实际用途所需的尺寸、透明背景、图集或音频参数。合格资源接入场景、Texture、AudioStream 或 Resource，确认 Godot 导入和引用有效。游戏运行不依赖 ComfyUI。
