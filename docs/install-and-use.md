# 安装与使用：Codex 和 DeepSeek Harness

本指南适用于 Godot Agent Kit **2.0.0**，面向 Windows 用户。第一次使用推荐按第 1–6 步完成项目级安装：两个技能安装一次，Codex 和 DeepSeek Harness 共用。

| 技能 | 用途 |
| --- | --- |
| `godot-project-init` | 新建或补齐 Godot 项目的规范、开发技能、官方文档和检查工具，按配置接入 ComfyUI |
| `godot-dev` | 在已有项目中实现玩法、场景、UI、资源和素材，修复问题，完成验证与清理 |

[返回仓库首页](../README.md) · [下载 v2.0.0](https://github.com/CedarHWA/godot-agent-kit/releases/tag/v2.0.0) · [兼容范围](compatibility.md)

## 1. 准备环境

- Windows 10/11、PowerShell 5.1 或更新版本。
- Python 3.11+；在 PowerShell 执行 `python --version` 应显示正确版本。
- 已安装并能正常使用的 Codex 或 DeepSeek Harness，至少一个即可。
- 已安装 Godot。新项目默认基线为 **4.7.2**；已有项目保持原版本。其他版本需要在初始化请求中明确版本，并选择匹配的离线文档或 `docs-mode=online`。

ComfyUI 是可选项。普通初始化和代码开发先使用 `core` 配置档，需要生成素材时再按第 8 节配置。工具包不会替你安装宿主、Godot 或模型权重。

## 2. 从 GitHub 获取工具包

打开 [v2.0.0 发布页](https://github.com/CedarHWA/godot-agent-kit/releases/tag/v2.0.0)，下载 `godot-agent-kit-2.0.0.zip`，解压到准备长期保留的工具目录。发布页同时提供 SHA-256 文件，可用 `Get-FileHash -Algorithm SHA256 <下载的ZIP路径>` 对照校验。

如果已安装 Git，也可以在自己的工具目录中运行：

```powershell
git clone https://github.com/CedarHWA/godot-agent-kit.git
cd godot-agent-kit
```

后续安装命令均在**包含 `install.ps1`、`setup.ps1` 的工具包根目录**执行。ZIP 解压的目录层级可能不同，以这些文件所在位置为准。

工具包目录与目标游戏目录分开。不要把新游戏建在克隆下来的工具包仓库里面；Harness 会根据最近的 `.git` 上级目录确定项目根。

请使用本仓库安装器复制完整技能。安装器还会把唯一的 `godot-dev` 源码组装进初始化技能；仅复制 `SKILL.md` 或直接复制初始化技能源码目录，会缺少这一步。

## 3. 创建 Python 环境和本机配置

在工具包根目录的 PowerShell 中运行：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\setup.ps1
if ($LASTEXITCODE -ne 0) { throw 'Python 环境准备失败，请先处理上方错误。' }
$kitPython = (Resolve-Path .\.venv\Scripts\python.exe).Path
```

`setup.ps1` 创建工具包自己的 `.venv`，并联网安装检查依赖。无需先激活虚拟环境，后面的命令明确传入它的 Python。

如果 `python` 命令不可用，把第一条命令替换为下列形式，填入真实路径；成功后再设置 `$kitPython`：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\setup.ps1 -Python 'C:\你的Python目录\python.exe'
```

首次创建机器配置时，先把下面的 `godot` 路径改为自己电脑上真实的 Godot 可执行文件，建议使用标准 Windows 版的 `_console.exe`。已有配置时直接编辑 `.local\machine.json`，下面的命令会保留原文件：

```powershell
New-Item -ItemType Directory -Path .local -Force | Out-Null
if (-not (Test-Path -LiteralPath '.local\machine.json')) {
    $machineConfig = @{
        schema = 1
        godot  = 'C:\Tools\Godot\Godot_v4.7.2-stable_win64_console.exe'
        python = $kitPython
    }
    $machineConfig |
        ConvertTo-Json -Depth 8 |
        Set-Content -LiteralPath '.local\machine.json' -Encoding UTF8
}
```

机器配置只保存在本机。安装时传 `-Config`，初始化技能就能记住这些路径。该示例引用工具包内的 `.venv`，因此后续应保留工具包目录；移动目录或更换电脑后更新配置并重新安装。

如果关闭过 PowerShell，重新进入工具包目录后再次设置 `$kitPython`；第 4 节中的 `$targetProject` 也需要重新设置。变量只在当前终端有效。

## 4. 检查环境并安装两个技能

设置目标游戏目录，可以是空目录，也可以是已有 Godot 工程。下面默认放在当前用户目录中，可替换为自己的绝对路径：

```powershell
$targetProject = Join-Path $env:USERPROFILE 'GodotProjects\MyGame'
New-Item -ItemType Directory -Path $targetProject -Force | Out-Null
```

在工具包根目录检查环境：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\doctor.ps1 `
    -Python $kitPython `
    -Config .local\machine.json `
    -Project $targetProject `
    -Agent both `
    -Profile core
if ($LASTEXITCODE -ne 0) { throw '环境检查未通过，请处理必需项失败后重试。' }
```

输出为 JSON。必需项失败时先按提示修复；宿主 CLI 不在 PATH 可能只是 warning，桌面版仍可能正常加载技能。

安装到目标游戏目录：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 `
    -Python $kitPython `
    -Agent both `
    -Scope project `
    -Project $targetProject `
    -Skills both `
    -Config .local\machine.json
if ($LASTEXITCODE -ne 0) { throw '技能安装未完成，请按输出处理错误或文件冲突。' }
```

| 参数 | 含义 |
| --- | --- |
| `-Agent both` | 两个宿主共用目标项目的 `.agents\skills` |
| `-Skills both` | 安装初始化和开发两个技能 |
| `-Scope project` | 仅安装到指定项目 |
| `-Config` | 将本机工具配置写入已安装的初始化技能 |
| `-DryRun` | 可选，附加到安装命令只查看计划 |

安装成功后检查两个入口：

```powershell
Test-Path "$targetProject\.agents\skills\godot-project-init\SKILL.md"
Test-Path "$targetProject\.agents\skills\godot-dev\SKILL.md"
```

两项应为 `True`。文件检查只确认安装入口存在；下一步还要在宿主的新会话中确认实际识别。安装技能本身不会初始化游戏或启动 ComfyUI。

只使用一个宿主时，可以用下表的 `-Agent` 值替代 `both`；其余安装参数相同。Harness 单宿主安装后，入口检查路径相应改为 `.dsh\skills`。

| 宿主选择 | 参数 | 项目技能目录 |
| --- | --- | --- |
| 两者共用 | `-Agent both` | `.agents\skills` |
| 仅 Codex | `-Agent codex` | `.agents\skills` |
| 仅 DeepSeek Harness | `-Agent deepseek-harness` | `.dsh\skills` |

## 5. 在 Codex 中初始化和开发

在 Codex 中打开**目标游戏目录**，新建会话，输入 `$` 查找这两个技能。CLI/IDE 也可使用 `/skills`。如果新技能没有显示，重启宿主后再试。

以下提示词发给 Agent，**不要粘贴到 PowerShell**。双宿主项目初始化：

```text
$godot-project-init 初始化当前项目，使用 core 配置档。
Codex 和 DeepSeek Harness 共用这个项目，请使用 agent=both。
完成环境检查、项目初始化、验证和本轮临时文件清理。
```

只给 Codex 使用的项目，将第二行改为“本项目仅使用 Codex，请使用 agent=codex”。新项目初始化后应得到可编辑入口、开发规范、文档和检查工具；已有项目则补齐所缺内容并保留已有工作。

需要先设计游戏时：

```text
$godot-dev 为这个项目设计一个简单完整的测试游戏。
先编写需求、架构和验收文档，暂时不要实现游戏。
```

审阅需求后再开始开发：

```text
$godot-dev 按 docs/requirements.md 和 docs/architecture.md 开始开发。
完成完整游戏流程、适用的测试、编辑器可维护性验收和临时文件清理。
明确说明未验证项。
```

## 6. 在 DeepSeek Harness 中初始化和开发

在 Harness 中打开**目标游戏目录**并新建会话，用 `/技能名` 调用。双宿主项目初始化：

```text
/godot-project-init 初始化当前项目，使用 core 配置档。
Codex 和 DeepSeek Harness 共用这个项目，请使用 agent=both。
完成环境检查、项目初始化、验证和本轮临时文件清理。
```

只给 Harness 使用的项目，将第二行改为“本项目仅使用 DeepSeek Harness，请使用 agent=deepseek-harness”。

先生成需求文档：

```text
/godot-dev 为这个项目设计一个简单完整的测试游戏。
先编写需求、架构和验收文档，暂时不要实现游戏。
```

审阅后开始开发：

```text
/godot-dev 按 docs/requirements.md 和 docs/architecture.md 开始开发。
完成完整游戏流程、适用的测试、编辑器可维护性验收和临时文件清理。
明确说明未验证项。
```

Harness 以最近的 `.git` 上级目录作为项目根，没有 `.git` 才使用当前工作目录。嵌套仓库中的游戏需要将技能安装到实际项目根，或按[宿主适配](agents.md)配置自定义技能目录。

两个宿主均可直接在已有项目中使用 `godot-dev` 修改功能，不要求先重新初始化。切换宿主时继续使用同一份需求、架构和场景资源。

## 7. 可选：安装到用户目录

希望多个项目都能使用时，选择用户级安装，替代第 4 节的项目级安装命令：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 `
    -Python $kitPython `
    -Agent both `
    -Scope user `
    -Skills both `
    -Config .local\machine.json
```

用户级安装不传 `-Project`。本版安装器的默认位置如下；设置过对应环境变量时使用其指定目录：

| 宿主 | 用户技能根 |
| --- | --- |
| Codex | `CODEX_HOME\skills`，默认用户目录下的 `.codex\skills` |
| Harness | `DSH_HOME\skills`，默认用户目录下的 `.dsh\skills` |

`-Agent both -Scope user` 分别安装两份。同一技能通常选择一个安装范围；已有同名技能时先按[迁移说明](migration.md)处理，避免重复出现。Codex 官方还列出共享用户目录 `.agents\skills`；本工具包默认采用已实际验证的 `CODEX_HOME\skills`，自定义发现根可使用 `-SkillsDir`，详见[宿主适配](agents.md)。

## 8. 可选：配置 ComfyUI 生成素材

| 配置档 | 用途 |
| --- | --- |
| `core` | 普通 Godot 开发，无素材服务依赖 |
| `endpoint` | 接入已运行且可访问的 ComfyUI API |
| `desktop-wai` | 使用已适配的 Comfy Desktop/WAI 实例和项目 MCP 流程 |

### 已有 ComfyUI API

保留 `.local\machine.json` 原有字段，新增 `comfyui_endpoint` 对象。完整结构可参考工具包根目录的 `config.example.json`；这里展示新增字段：

```json
{
  "comfyui_endpoint": {
    "url": "http://127.0.0.1:8188"
  }
}
```

将地址改为实际服务地址，使用 `-Profile endpoint` 重跑第 4 节的环境检查，再用更新后的配置重跑原安装命令。新项目初始化提示词中的 `core` 改为 `endpoint`；已有项目需明确要求从旧配置档迁移，不能只改配置文件就视为接入完成。

### Comfy Desktop/WAI

当前已验证 Comfy Desktop **1.1.7**、Windows NVIDIA 环境，以及指定的 WAI-illustrious-SDXL v17 权重。先按 [Windows 环境与 ComfyUI](windows.md)配置 Desktop、共享模型库和独立工具环境，再选择 `desktop-wai` 初始化。其他 Desktop 版本需要验证适配，不能直接跳过版本门禁。

该流程生成项目 MCP 配置后，Codex 需要加载受信任项目的配置；Harness 按生成的 `.dsh/comfyui.cordis.yml` overlay 启动。具体命令见[宿主适配](agents.md)。新配置生成不代表当前聊天已加载 MCP。

安装包不包含模型权重。美术、音乐、音效工作流需按实际模型配置，并查看/试听输出、记录来源和许可。技能安装、服务连通或生成成功均不能替代素材质量验收。

## 9. 更新、回滚和卸载

Git 克隆用户在工具包目录执行 `git pull --ff-only`；ZIP 用户下载新版并解压到合适目录。然后核对本机配置中的工具路径，用**原来的 Agent、Scope、Project/SkillsDir 和 Config 参数**重跑安装命令。安装器更新未被用户修改的受管理文件；有冲突时保留原件并报告候选内容。

以下示例对应本指南的项目级双宿主安装。按需选择一项操作。

回滚最后一次实际变更：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Python $kitPython -Agent both -Scope project -Project $targetProject -Action rollback
```

卸载未修改的受管理技能文件：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Python $kitPython -Agent both -Scope project -Project $targetProject -Action uninstall
```

仅在安装中断、存在 pending 事务时恢复：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Python $kitPython -Agent both -Scope project -Project $targetProject -Action recover
```

用户级安装将 `-Scope project -Project $targetProject` 改成 `-Scope user`；单宿主安装保持原来的 `-Agent`。只安装过一个技能时，继续传入原来的 `-Skills init` 或 `-Skills dev`。

不要删除技能根 `.godot-agent-kit` 中的收据和恢复历史来解决冲突。旧版迁移、退出码和恢复边界见[迁移说明](migration.md)。

## 常见问题

| 现象 | 处理方式 |
| --- | --- |
| `python` 找不到或版本过旧 | 用 `setup.ps1 -Python <真实路径>` 指定 Python 3.11+ |
| Godot 找不到 | 编辑 `.local\machine.json` 的 `godot`，重新运行 doctor |
| `gdtoolkit` 缺失 | 重新运行 setup，并确认配置的 `python` 指向本工具包 `.venv` |
| 安装退出码为 2 | 查看冲突输出与技能根 `.godot-agent-kit/proposals/`，按迁移说明处理 |
| 文件存在但宿主看不到技能 | 核对实际项目根、安装范围和宿主设置，打开新会话，必要时重启宿主 |
| 同名技能出现多次 | 核查用户级和项目级安装；旧技能备份移到发现根之外，不只给目录加后缀 |
| 初始化退出码为 3 | Desktop 流程尚待创建/绑定，由初始化技能继续完成，不能当成完成 |
| headless 检查通过但画面/声音未确认 | 继续实际交互、画面和听感验收，未验证项应写入报告 |

本工具包的实际测试版本、证据和未验证项见[验收记录](acceptance.md)。宿主发现规则参考 [Codex 官方技能说明](https://learn.chatgpt.com/docs/build-skills)及 [Harness 文件系统技能提供者](https://github.com/deepseek-ai/deepseek-harness/tree/master/packages/skill/skill-filesystem)。
