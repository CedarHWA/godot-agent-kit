# Windows 安装与环境

支持 Windows 10/11、PowerShell 5.1+、Python 3.11+；标准 Godot Windows 版按项目固定版本。测试使用 Python 3.14、Godot 4.7.2。不要把预装于某人机器的 Python 虚拟环境拷贝给其他用户。

1. 把仓库放在已有的工作目录下。`setup.ps1 -Python <python.exe>` 创建仓库 `.venv` 并按 requirements.txt 安装检查/维护依赖。项目的 Godot 可放任意位置，通过 JSON 配置或 GODOT_PATH 指定。
2. 推荐 `install.ps1 -Python <python.exe> -Agent <codex|deepseek-harness|both> -Scope user -Skills init`：用户级 init 可复用于多个项目，初始化目标游戏时生成项目级 dev。其他布局仍支持 `-Scope project -Project <游戏目录>`、`-Skills dev/both` 或 `-SkillsDir <实际技能根>`。脚本路径包含空格和中文可正常传参。完整步骤见[安装与使用](install-and-use.md)。
3. `doctor.ps1` 返回 JSON，required 失败退出 1；宿主 CLI 缺失是 warning，因为桌面版仍可能加载技能。图形、真实输入、听感始终单独标为未验证；安装 agent CLI 不会自动证明这些能力。

配置示例中的空字符串表示未设置，不是有效文件。推荐明确配置 `godot`、`python`。环境变量支持 GODOT_PATH、GODOT_KIT_PYTHON、COMFY_DESKTOP_EXE、COMFY_DESKTOP_DATA、COMFY_MCP_EXE、COMFY_BIN。没有固定工具安装路径时让 doctor 报缺项，再填真实路径，不扫描盘符或猜用户名。

## Desktop/WAI

先有 Comfy Desktop 1.1.7、NVIDIA 驱动和已下载的 WAI-illustrious-SDXL v17 权重。Desktop 设置的共享模型目录需包含检查点；doctor 的 `-VerifyModel` 会核验完整 SHA-256。多份同名文件在正式绑定时会拒绝，以免加载错误模型。

```powershell
.\setup.ps1 -Comfy
.\doctor.ps1 -Python .\.venv\Scripts\python.exe -Config .local\machine.json -Profile desktop-wai -VerifyModel
```

`setup.ps1 -Comfy` 仅建立 `.local/comfy-runtime`（comfy-cli、comfy-mcp、psutil、websocket-client）；在 JSON `comfyui_bootstrap` 中填写该环境的 `Scripts/comfy-mcp.exe` 和 `Scripts/comfy.exe`，以及 Desktop 程序和正常配置目录。共享模型路径来自 Desktop 自身设置。

初始化时明确 `--profile desktop-wai`。它保留完整原生实例流程，未绑定退出 3 后由技能继续：Explorer Shell 启动 → 核查真实配置/版本 → 正常安装 Standalone → 记录 ID → 绑定与哈希校验 → 真实 MCP 预检 → 新进程与开始菜单可见性验收 → 恢复原状态。完整命令、状态恢复和旧实例迁移在技能 references/desktop-api.md 与 desktop-workflow.md。

此内部 API 有明确 1.1.7 版本门禁；新版本要先验证，不删除门禁假称兼容。普通启动不能证明没有 MSIX 配置重定向。不得手写 installations.json、复制旧环境冒充新实例或在同名冲突时随意追加名称。

## 已有 ComfyUI API

JSON 配置 `comfyui_endpoint.url`，初始化选 `--profile endpoint`。doctor 对 `/system_stats` 与 `/object_info` 做有界只读请求；节点/模型与 API 工作流按实际环境验证。核心 CLI 不要求 WebSocket、MCP 或 Desktop。外部服务器隔离由其所有者负责，本模式不自动安装节点、上传输入、启动或停止服务。

`tools/comfy_endpoint.py submit --receipt <本轮文件>` 先保存提交中记录再发送；未知结果不能重新排队。保留 prompt_id，用 history/fetch 恢复。正式美术、音乐、音效要实际查看/试听并记录来源/许可；工具不会提供空白图片或静音来充当正式素材。

## 常见问题

- Godot 找不到：设置 GODOT_PATH 或 JSON 的 godot。版本不一致：使用原项目固定版本，显式迁移才改基线。
- gdtoolkit 缺失：在选择的 Python 环境安装 requirements.txt，不装入 ComfyUI 实例环境。
- MCP 没出现：Codex 检查项目受信任并重新加载；Harness 用项目生成的 `--patch` 文件。当前会话可直接使用项目 stdio CLI。
- 模型缺失/哈希不符：核对共享库真实文件和来源，不自动重下/覆盖。
- 文件冲突：读取 proposals 与原件，合并后对具体初始化文件 `--keep-existing`；技能安装冲突按迁移文档处理。
- 需要精确依赖重现：requirements-lock.txt 与 requirements-comfy-lock.txt 分别记录本次两个环境的完整依赖；需要更新依赖时单独提交清单与测试结果。在对应环境运行 `python -m pip install -r <对应锁文件>` 可重现。
