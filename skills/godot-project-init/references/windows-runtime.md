# Windows 运行环境

核心安装器和初始化器只需 Python 3.11+ 标准库。检查 Godot 需要匹配项目基线的官方 Windows Godot；格式检查需要 gdtoolkit。仓库 `setup.ps1` 在仓库 `.venv` 安装固定依赖，`setup.ps1 -Comfy` 在 `.local/comfy-runtime` 单独安装 Comfy CLI/MCP 与 Desktop 适配器依赖。已安装技能内也可用已有 Python 环境；不要求运行机器保留原仓库。

配置 JSON 接受 `schema: 1`、`godot`、`python`、`comfyui_bootstrap`、`comfyui_endpoint`。路径写本机绝对路径；不要携带用户名/盘符预设发布。明确配置优先，其次环境变量、现有项目 `.local`、PATH。支持 `GODOT_PATH`、`GODOT_KIT_PYTHON`、`COMFY_DESKTOP_EXE`、`COMFY_DESKTOP_DATA`、`COMFY_MCP_EXE`、`COMFY_BIN`。

desktop-wai 的 bootstrap 字段：`desktop_exe` 是 Comfy Desktop 程序；`desktop_data` 是正常开始菜单实例使用的数据目录；`mcp` 是包含 comfy-mcp.exe 的独立 Python 环境；`comfy_bin` 是同环境 comfy.exe。Desktop 适配器要求 mcp 同目录的 python.exe 安装 psutil/websocket-client。只支持通过版本门禁的 Desktop 1.1.7 与 Windows NVIDIA 环境，模型目录从 Desktop settings.json 读取，不复制权重或手写实例注册表。

Comfy Desktop、Godot、驱动和模型由用户已有安装或明确安装任务提供；依赖 setup 不代为安装这些大型软件。初始化/doctor 发现缺项就报告准确恢复命令/配置项，继续独立工作，不宣称缺失部分已完成。

Codex MCP 写入项目 `.codex/config.toml`，保留已有配置，冲突停止并要求明确合并；Harness 生成 `.dsh/comfyui.cordis.yml`，从项目根运行 `dsh web --patch .dsh/comfyui.cordis.yml`（也可 headless）。此补丁不会自动改写全局 profile。项目实例需要先启动；新 MCP 尚未被当前会话发现时使用 `tools/project_comfyui.py call --request <JSON>` 的真实 stdio 入口。
