# 2.0.0 验收记录

执行日期：2026-10-17。平台：Windows，Python 3.14.7，Godot 4.7.2.stable.official.ed1daf0bf，gdtoolkit 4.5.0；Codex CLI 0.163.0-alpha.10.2，DeepSeek Harness 0.2.0-rc.2，Comfy Desktop 1.1.7.0。

| 验收项 | 实际执行与结果 |
| --- | --- |
| 回归测试 | 63 项通过：新增安装/环境/模式/宿主/回执/恢复 34 项，原 dev bundle 12 项、Desktop 可见性与启动失败回归 10 项、实例绑定 7 项 |
| 安装保护 | 实测重复安装、内容升级、完整回滚、写入失败还原、崩溃日志 recover、用户编辑/未管理文件保留、损坏备份拒绝、Windows junction 与路径越界拒绝 |
| Codex 实际发现 | 独立 app-server skills/list：项目级、both 共用项目根、隔离 CODEX_HOME 用户级，各发现两个唯一技能且 enabled=true，无目录错误 |
| Harness 实际加载 | 已安装的 FileSystemSkillProvider：project-dsh、project-agents、user-dsh，两个技能正文与资源目录均成功加载 |
| Harness MCP | 本机 dsh headless --patch ... --dump-config 正确组合项目 MCP insert patch；没有修改全局 profile |
| 安装包初始化 | 从完整已安装的 init 技能创建含中文/空格路径的新工程；二次执行无创建/更新/冲突；补齐保留需求、报告规则冲突，明确 keep-existing 后可继续 |
| Godot | 临时复制实际引擎，格式、静态检查、导入、编辑器结构契约、冒烟测试、运行均通过，共 7 个检查阶段 |
| 官方文档 | 1,596 页 SHA-256、148,893 个本地链接、3,766 个代码块检查通过；保留一个上游缺失锚点的已记录降级处理 |
| 环境检查 | 新 doctor 实际识别 Godot/Python/两个宿主/NVIDIA/Desktop/MCP 依赖；共享 WAI 全量 SHA-256 匹配；不启动服务、不复制权重 |
| 技能格式 | skill-creator quick_validate 以 UTF-8 模式验证两个技能通过；包级引用/JSON/Python 语法和隐私路径检查通过 |
| Comfy 工具安装 | setup.ps1 -Comfy 在新的私有环境安装固定顶层依赖，pip check 通过；实际 comfy-mcp initialize/tools/list 成功协商 2025-06-18，所需节点/工作流/任务/下载接口均存在；未启动后端或提交任务 |
| 发布包 | 解压候选 ZIP 后逐文件核验清单，运行包内安装器和安装后的初始化器成功；验证项目 work/.local/tools 的 Godot 忽略标记随包保留；最终包带独立 SHA-256 |

公开机器可读摘要见 [acceptance.json](acceptance.json)。endpoint 模式另用本机 HTTP 协议 fixture 实测请求、回执、下载和拒绝覆盖，未将 fixture 当作模型生成证据。

完整运行命令：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File tools/check.ps1 -Godot '<本机固定版本 Godot.exe>'
.\.venv\Scripts\python.exe -B tests/host_smoke.py --harness-runtime '<Harness.exe 或 node.exe>' --harness-module '<已安装 dsh-skill-filesystem/lib/index.js>'
.\.venv\Scripts\python.exe -B toolkit/build.py
.\.venv\Scripts\python.exe -B tests/release_smoke.py dist/godot-agent-kit-2.0.0.zip
```

机器相关完整报告在不发布的 `.local/`；本文件保留可公开的结果，脚本可在其他环境复现。CI 提供 Windows Python 3.11/3.14 矩阵；本次没有远程运行 GitHub Actions。

本次没有调用收费模型、运行独立 agent 完整开发前测、重新创建 Desktop 实例或重新生成美术/音乐；没有把技能发现、替身回归、headless 检查视为这些验收。感官判断、实际游戏输入与未来生成质量仍由具体开发任务验收。Desktop 创建和 Shell 行为代码保留原版本门禁，相关真实初始化要求继续留在技能中。

测试创建的安装目录、临时 Godot 工程、隔离宿主目录均由测试在退出后删除。发布包仅包含源码、模板、文档、许可证和测试，不包含个人配置、运行环境、权重、缓存或上层游戏素材。有效本地验证环境与紧凑报告保留供维护使用。
