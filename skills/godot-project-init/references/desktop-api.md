# 无 computer-use 的 Desktop 实例创建与可见性验证

`scripts/desktop_instance.py` 适配 Comfy Desktop **1.1.7** 的内部 renderer bridge，通过临时本机 CDP 调用 Desktop 自己的安装和生命周期 API。`scripts/desktop_launch.py` 通过 **当前用户 Explorer 进程中的 Shell 对象**启动应用，使用与开始菜单相同的环境；不点击界面，不修改应用、快捷方式或手写 `installations.json`。内部接口升级后需重新验证。

## 为什么不能直接启动子进程

Codex 的 MSIX 运行环境可能将同一个 `%APPDATA%\Comfy Desktop` 路径重定向到包的 `LocalCache\Roaming`。在那里成功创建的实例不会出现在开始菜单打开的 Desktop 中。相同 exe、用户、APPDATA 字符串、`GetPackageFullName` 返回无包身份，甚至 `PROC_THREAD_ATTRIBUTE_DESKTOP_APP_POLICY` 启动策略，都不足以证明使用正常配置。

固定使用 Explorer 托管的 `Shell.Application`：`Windows().FindWindowSW(..., SWC_DESKTOP, ..., SWFO_NEEDDISPATCH).Document.Application.ShellExecute(...)`。不是在当前进程直接调用 ShellExecute，也不是普通 `Start-Process` / `subprocess.Popen`。启动工作进程先核对配置文件的真实解析路径，再启动 Desktop。无法取得 Explorer Shell 时停止，不能回退到已知会继承隔离的方式。微软依据：[Execute In Explorer](https://learn.microsoft.com/en-us/windows/win32/shell/samples-execinexplorer)、[Explorer 托管的 Shell 对象](https://devblogs.microsoft.com/oldnewthing/20131118-00/?p=2643)。

## 创建与启动

Python 取自本机配置的 `comfyui_bootstrap.mcp` 同目录 `python.exe`，已含 psutil/websocket-client。命令中使用技能、项目的绝对路径：

```text
<MCP Python> -B <技能>/scripts/desktop_instance.py open --project <项目>
<MCP Python> -B <技能>/scripts/desktop_instance.py probe --project <项目>
<MCP Python> -B <技能>/scripts/desktop_instance.py create --project <项目>
<MCP Python> -B <技能>/scripts/desktop_instance.py status --project <项目>
```

- `open` 通过 Explorer Shell 启动现有 Desktop，设置随机临时端口与 `--remote-debugging-address=127.0.0.1`，记录 `.local/comfyui-desktop-session.json`。只连接进程身份、端口所有者和本地应用页面匹配的 Desktop；拒绝替代配置目录。所有操作在读取配置前核对 `installations.json` 与 `settings.json` 的实际路径，发现重定向先恢复，不能继续创建。
- 已打开的普通 Desktop 返回 `restart_required`，不能第二次启动就给已有进程加调试参数。保存工作后正常退出，沿用已有明确重启授权；有未保存工作/运行任务且无授权时再询问，不强制结束。记录原先应用是否打开及本轮启动的实例。
- `create` 使用准确宿主项目显示名，先校验共享 WAI，再调用 `buildInstallation/addInstallation/installInstance` 安装稳定版 Windows NVIDIA 环境、跳过模板，设置共享模型、独立输入输出/会话和唯一端口。已有同名实例/目录先核实归属，不加后缀或默默认领。
- 实际 ID 保存到 `.local/comfyui-desktop-creation.json`；已有绑定/创建记录时复用，不反复安装。每 10–30 秒用 `status` 查看安装，按阶段更新用户；`installed` 后追加 `--desktop-instance <实际ID>` 重跑原初始化参数绑定。安装中的隐藏记录只从已核对路径的注册表读取。
- `start` / `stop` 调用 Desktop 生命周期；继续执行项目 status 和真实 MCP 预检。stop 拒绝有运行/排队生成任务的实例。`verify` 必须在实例列表页面使用。

## 必须完成的可见性验收

创建/绑定成功不能单独作为完成依据。停止本轮测试实例，等待安装、启动、下载和所有用户任务结束，再验证：

1. `verify --project <项目>`：实际 ID、名称、路径、installed/personal 状态在 Desktop API 与正常注册表中一致，且实例名称已渲染在列表页面。
2. `close` 正常退出，确认进程结束与临时端口关闭；重新 `open` 后再次 `verify`，验证跨进程持久性。不能只在创建时的进程中验证。
3. Windows 有开始菜单快捷方式时，用 `open --project <项目> --shortcut <实际开始菜单.lnk>` 做第二次启动。适配器只读核对快捷方式位于开始菜单、指向正确 exe 且没有自定义参数，再通过 Explorer 调用该快捷方式；不改写快捷方式。随后 `verify`。路径从当前用户/所有用户 Start Menu Programs 查找，不硬编码别人的机器路径。
4. `close` 并确认临时端口关闭；需恢复应用打开状态时执行 `reopen --project <项目> --shortcut <同一快捷方式>`，正常启动不带调试参数。无快捷方式时 `reopen` 仍走 Explorer Shell。不要修改自动启动设置；用户偏好可能启动默认实例。

保存验收时的 Desktop 版本、启动方式、前后 PID、真实配置路径、项目 ID/名称/路径、`dashboard_name_rendered`、实例数与临时端口关闭结果。普通 `reopen` 只证明无调试参数启动，不能冒充新一次页面检查；页面证据来自同一快捷方式的前一步。若实例已注册但页面未渲染，检查筛选/工作区/窗口选择，不手改全局偏好掩盖问题。

## 已有隔离注册表的恢复

先只读定位正常与隔离配置的**实际文件路径**、实例安装目录、原绑定 ID 和项目归属。不要清空 AppData、覆盖正常注册表或复制实例环境。

- 隔离配置与本项目的关系明确且修复已授权时，正常退出相关 Desktop 后，将需要隔离的 `installations.json`、`settings.json` 及各自 `.bak` 逐个备份到项目历史目录；核对每个精确路径。存在其他项目/设置时先说明影响，保留恢复材料。无需删除缓存、模型或实例目录。
- 用新启动器打开正常 Desktop。已安装且属于本项目的目录，在核对路径唯一、名称不冲突后，通过 Desktop 原生 `trackInstallation`（Add Existing）接入；根据当前版本处理器核对参数，不手写注册记录。保留独立输入输出/会话与唯一端口。目录不存在或归属不明时停止接入；用户已要求新建则使用正常 `create`。
- 原生接入会产生**新注册 ID**，并把 `.comfyui-desktop-2` 写为 `tracked`。不把它改成 ID。项目模板允许 `tracked`，但必须已有 `.godot-project-binding.json` 指向本项目且该目录在正常注册表中唯一。
- 备份旧项目绑定和报告，再显式重新绑定新 ID；旧绑定必须作为迁移记录保留，不静默复用失效 ID。核对正式绑定与归属标记 ID 一致，重新验证共享 WAI 和真实 MCP，完成上述重启/快捷方式验收后清理本轮无用文件。

## 兼容与检查

接口只验证了 Desktop 1.1.7；未知版本停止并检查本机 preload/实例处理器，不假定内部 API 永久稳定，也不默认转用 computer-use。相关源码：[preload API](https://github.com/Comfy-Org/Comfy-Desktop/blob/main/src/preload/api.ts)、[实例处理器](https://github.com/Comfy-Org/Comfy-Desktop/blob/main/src/main/lib/ipc/registerInstallationHandlers.ts)。

修改适配器后运行 `python -B -m unittest discover -s <技能>/scripts/tests -v`，并在生成的项目中运行 `tests/test_comfyui_binding.py`。测试替身只验证拒绝错误状态；发布前必须真实执行 Explorer 启动、快捷方式重新启动及 `verify`，确认没有重新生成隔离配置。
