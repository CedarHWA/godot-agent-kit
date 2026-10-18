# 项目资源制作

初始化仅生成 WAI-illustrious-SDXL v17 文生图工作流。其他图片编辑、音乐、音效和 TTS 工作流在实际需求出现后再为本项目创建；不沿用其他项目的角色、音色、工作流目录或服务器地址。

## 开发任务中的自动执行

收到需要素材的需求后，Agent 先检查现有资源与本项目可用工作流，再完成选型、任务副本、MCP 生成、质量检查和 Godot 接入。需求已经给出用途、角色或风格时沿用，不重复询问普通参数；只缺少不影响身份/玩法的细节时采用可调整默认值并记入本轮报告。无需新素材的任务跳过资源生成。

| 用途 | 选择与验收重点 |
| --- | --- |
| 二次元文生图 | 优先已验证的 WAI 基础工作流；依据用途设尺寸与构图，检查透明通道、裁切和角色设计 |
| 换装或图片编辑 | 检查本项目已有编辑节点/工作流和共享权重，输入本项目角色参考；逐项对比脸、发型、配色与指定修改 |
| 音乐 | 按场景、时长、配器及是否循环选已有可用模型；检查截断、循环接缝和背景音乐音量 |
| 音效 | 按事件、长短、动作同步需求选音效工作流；检查静音、瞬态与尾音 |
| 角色 TTS | 按语言、角色音色与情绪选 TTS 工作流；复用本项目音色档案，检查文本、发音和音色一致性 |

表格用于选择任务类型，不证明编辑、音乐、音效或 TTS 已安装。先查实际节点、工作流和模型，再按“按需扩展”处理缺项。保留原始任务要求；占位资源、技术检查与视觉/试听验收分别记录。对未核实的模型许可只标注现状，不自动宣称可商用。

MCP 工具参数以当前服务器暴露的 schema 为准。先预检再提交，提交后立即记录 prompt_id；等待超时先查询原任务并取回已完成输出，避免重复排队。相同错误重复出现时检查原因与实际依赖，停止无意义重试并继续不依赖该素材的开发。按当前需求完成必要数量，避免无目的批量生成。

任务 JSON、日志和未采用样例写入本轮 work/dev-<任务标识>/；prepare_asset.py 的 work/assets-staging/<asset-id>/ 另记入本轮清单。正式素材按媒体类型与用途放 assets/ 下的子目录（如 images/cards、audio/music、audio/sfx、fonts），工作流保存在 tools/comfyui/workflows/，来源证据归档 docs/assets/<asset-id>/，验收摘要写 .local/dev-reports/<任务标识>.json。移入正式位置后检查所有引用，取回成功不等于已接入游戏。

## 实例与启动

从 Windows 开始菜单打开 Comfy Desktop 应能看到绑定实例。脚本启动统一使用初始化技能的 Explorer Shell 启动器；普通子进程启动可能继承 Codex MSIX 隔离，导致同一 APPDATA 路径实际落到 LocalCache。项目工具检查注册表和设置文件的实际路径，检测到重定向立即停止。先按初始化技能 references/desktop-api.md 恢复正常注册信息，不另建同名实例或更改 URL 绕过检查。原生 Add Existing 的 `tracked` 标记只在已有本项目归属且注册目录唯一时接受；正式绑定还需与归属标记的 ID 一致。

- 本项目绑定一个由 Comfy Desktop 正常安装流程创建的 **Standalone 普通实例**。它出现在 Desktop 实例列表，可直接打开、停止和管理；安装在 Desktop 正常安装目录，不嵌套在游戏目录。项目专属表示本项目只使用这个实例。初始化优先通过经过版本核验的 Desktop 内部接口调用正常安装器，无需逐步点击；新实例显示名称与 宿主项目显示名称一致。
- `.local/comfyui-instance.json` 保存 Desktop 实际 ID、端口、路径、绑定时的版本和 WAI 校验值；`.local/comfyui-bootstrap.json` 记录已有 Desktop/MCP 工具位置，共享模型路径从 Desktop 配置读取；`.local/comfyui-request.json` 是首次创建建议。实例内 `.godot-project-binding.json` 记录项目归属。
- 每实例拥有自己的核心、Python/Torch 依赖、节点、工作流、输入输出和用户数据。Desktop“管理 → 存储”中开启共享模型，关闭共享输入与共享输出，保持独立浏览器会话。模型直接读取 Desktop 已配置的共享库；初始化不复制、不创建模型链接，也不额外下载 WAI。实例环境仍占独立磁盘空间；MCP 工具程序和 Desktop 安装缓存复用。
- 绑定信息的 model_storage 记录共享目录、WAI 实际路径、大小与修改时间，model 记录固定版本和 SHA256。首次绑定验证完整哈希；每次连接/准备素材检查目录与文件状态，变化时要求重新核验。共享库可以显示其他模型，初始化仍仅生成 WAI 工作流，不复制其他实例的节点或工作流。共享权重属于各项目共同依赖，不能随某个项目的清理一起删除。
- 启动/停止交给 Desktop。`project_comfyui.py` 只绑定、核验和连接，不偷偷新起另一后端；Desktop 实例改名不影响 ID 绑定。路径/端口变更后必须显式重绑同一 ID。

项目检查工具的 Python 从 `.local/toolchain.json` 读取。在项目目录先检查状态：

```powershell
$projectTools = Get-Content .local/toolchain.json -Raw | ConvertFrom-Json
# 若 running=false，继续下方“自动启动与恢复”；检查报错则先处理原因。
& $projectTools.python -B tools/project_comfyui.py status
# 只读查看已注册实例：
& $projectTools.python -B tools/project_comfyui.py list
```

`setup --installation-id <实际ID>` 仅用于首次绑定或明确要求的重新核验，不属于日常启动流程。

初始化先生成建议端口，再由 Desktop 安装接口设置 `--port`（也可在“管理 → 启动参数”中查看），其余正常参数保留。存储设置修改后重启该实例，使共享模型及独立输入输出生效。端口占用或配置不匹配时拒绝连接；在 Desktop 处理后重绑，不直接改 URL 绕过检查。未完成正常创建/绑定返回退出码 3，需继续 Desktop 安装/绑定步骤。不要用全局 `comfyui` 或 comfy-cli 的启动/停止/升级工具管理此实例。

`.codex/config.toml` 添加 `comfyui_project` MCP，保留其他配置。它使用现有官方 comfy-mcp，并隔离 CLI 配置、任务记录和缓存。Codex 仅在项目受信任时加载项目配置；新开该项目聊天后核对工具。尚未加载时可使用 `tools/project_comfyui.py call --request <JSON文件>`，通过同一个官方服务器执行真实 MCP 请求，JSON 格式为 `{"name":"server_info","arguments":{}}`。不能回退到全局实例来冒充验证通过。

### 自动启动与恢复

本开发流程不使用 computer-use。复用已安装 godot-project-init 的 `scripts/desktop_instance.py` 和配套 `scripts/desktop_launch.py`，启动方式固定为 **Explorer Shell → Desktop 原生接口 → 绑定实例**。不复制一套旧适配器，不直接用 Start-Process/Popen 启动 Desktop exe；共享配置的实际路径检查必须生效。启动器说明和版本范围见该技能的 `references/desktop-api.md`，当前适配 Desktop 1.1.7。

1. 需要生成素材时先运行 `tools/project_comfyui.py status`。`ready=true` 且 `running=true` 就复用现有实例，不为获取调试连接重启 Desktop。`ready=true` 且 `running=false` 才进入启动步骤；配置/归属/端口身份检查报错先修复，不能将错误视为“未启动”。
2. 从当前已安装技能的位置定位两个脚本，读取其参考说明。Desktop 命令使用 `.local/comfyui-bootstrap.json` 中 `mcp` 同目录的 `python.exe`（含 psutil/websocket-client）；项目 status/call 使用 `.local/toolchain.json` 的 Python。不要把项目 MCP 的隔离 APPDATA 环境用于 Desktop 启动。记录原先应用、绑定实例、调试连接的状态和 PID/端口。
3. 执行适配器 `open --project <项目绝对路径>`；原有开始菜单快捷方式已核实时可加 `--shortcut <实际.lnk>`。`started` 表示本轮新开的调试会话；`existing` 仅复用，不据此认领关闭权限。`restart_required` 时先保存工作并正常退出原 Desktop；沿用已有明确重启授权，未保存内容/用户任务不明确时再询问。已确认可重启且无用户任务时，可用进程的正常关闭接口请求退出并等待；未退出则检查保存提示，不强杀，也不反复启动第二份应用。正常退出后再 `open`。
4. 接口就绪后 `probe` 核对版本、正常配置路径及绑定 ID/安装目录，再 `start --project <项目绝对路径>`。轮询项目 status，身份与地址匹配后执行真实 MCP 的 server_info/system_stats 和本次工作流预检。普通开发仅复用已有 ID，不运行 create、安装器或 setup 重绑。若本轮修复了启动器/注册信息，另按初始化技能完成 `verify` 和快捷方式重新启动验收；日常素材任务不重复整套初始化验收。
5. 结束时，仅对本轮启动的实例执行 `stop`，先确认队列为空并等待停止。仅关闭本轮创建的调试会话：Desktop 无其他运行实例、启动、安装、下载任务后执行 `close`，等待进程退出且临时端口关闭。用户原先打开了 Desktop 就用 `reopen --project <项目绝对路径>` 恢复；有已核实快捷方式时加同一 `--shortcut`。reopen 仍走 Explorer Shell，不带调试参数；原先关闭则保持关闭。不能关闭时保留会话记录并说明尚有何任务，不能把端口仍开放写成已清理。

所有适配器操作都使用同一个项目绝对路径。停止后窗口保留“ComfyUI 已停止”页面是正常行为，不代表实例丢失；可用 probe 核对注册信息。列表 `verify` 需在实例列表页面执行，不能在停止页失败后另建实例；普通 reopen 不是新的页面可见性证明。报告记录本轮复用/启动/停止/恢复结果，确认端口关闭后才删除本轮已失效的 `.local/comfyui-desktop-session.json`，保留正式绑定与其他任务的会话。

脚本缺失、Explorer Shell 不可用、配置被重定向或版本不兼容时，定位/修复本任务相关适配问题，确实受阻就说明原因并继续独立开发。不能回退到 computer-use、直接启动 Desktop exe、另起 ComfyUI 后端或改端口/ID绕过核验。

实例管理依据：[Comfy Desktop 官方说明](https://docs.comfy.org/installation/desktop/usage/instance-management)。

## 基础文生图

`tools/comfyui/workflows/wai-t2i.api.json` 供 MCP 使用，`wai-t2i.ui.json` 可在 ComfyUI 打开。UI 副本也位于本实例的工作流库。默认 1024×1024、单张、28 步、CFG 5.5、Euler a、normal、CLIP skip 2、内置 VAE，是可调整的基线；按实际可用显存与任务质量要求调整。示例只是测试提示词，不是项目默认角色。

1. 按需求确认用途、尺寸、风格和角色参考；沿用 `docs/asset-policy.json` 中的用途及许可记录。读取 [WAI 许可快照](../tools/comfyui/WAI-LICENSE.md) 和 [模型来源](../tools/comfyui/wai-model.json)。
2. 编写参数 JSON（`prompt` 必填；可选 `negative/seed/width/height/steps/cfg`）。运行 `tools/prepare_asset.py --asset-id <唯一名称> --params <文件>`，得到任务副本；`--list` 显示范围。不要直接提交源模板。
3. 按“自动启动与恢复”复用或启动绑定实例，运行 `project_comfyui.py status` 检查注册信息、监听进程、独立 Python 与共享模型来源。通过 **comfyui_project** 调用 `server_info`、`system_stats`，确认 URL/版本匹配，实际启动参数使用 Desktop 的共享模型配置，输入输出没有指向其他项目。节点列表须支持本工作流，checkpoint 列表须包含固定 WAI 文件名；允许显示共享库中的其他模型。记录可用显存，同一块 GPU 避免多个重任务并发。
4. `validate_workflow(workflow_path=<绝对路径>)` 必须 valid=true，再 `run_workflow(wait=false, workflow_path=...)`，用 `job(action="wait"/"status", prompt_id=...)` 检查完成；`fetch_outputs(prompt_id=..., out_dir=<项目任务目录>)` 取回。缺模型/节点按实际缺项处理，不能提交到旧的 8188 实例。
5. 将 prompt_id、实际实例/版本、输出路径及 SHA256 写入任务 asset.json；检查画面、手部、尺寸、透明通道和一致性。普通 PNG 不代表透明立绘或合格动画图集，固定种子也不保证跨姿势角色一致。
6. 合格素材放入对应功能目录，由场景/Resource/Texture/AudioStream 引用。将实际工作流、参数、来源和检查结论归档到 `docs/assets/<id>/`。保留需要的母版后再清理任务目录。

## 按需扩展

先明确用途，再按显存、质量、许可和依赖选择模型与节点；优先官方工作流和核心节点。先检查共享库已有权重并直接使用，记录确切版本/文件名/哈希。确有缺项才按任务授权下载到共享库，保留独立版本文件，避免覆盖其他项目使用的同名模型。自定义节点若只支持内部固定模型路径，先检查其路径配置能力，不能假定所有节点都遵循 Desktop 模型目录；必要例外需明确说明磁盘占用与维护方式。

新工作流保存在 `tools/comfyui/workflows/`，来源/许可证/依赖版本随项目留档，通过项目 MCP 实际验证；无需预装所有旧模型。将节点和依赖安装到绑定实例自身的 Python 环境，升级前记录版本并使用 Desktop 快照，避免修改其他实例。

涉及配音时建立本项目角色音色档案；重复角色使用同一经确认参考。音频检查采样率、声道、削波、响度、静音及循环接缝，并区分技术生成成功与实际试听通过。图片与音频最终质量需独立验收。

Godot 功能开发继续遵守 AGENTS.md 的节点、场景、信号、Resource 和组合规范。游戏运行不依赖 ComfyUI；Godot MCP 用于实际引擎操作，`tools/check.ps1` 验证导入与运行。
