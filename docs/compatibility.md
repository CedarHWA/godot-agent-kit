# 功能与兼容范围

| 原有能力 | 2.0 位置/状态 |
| --- | --- |
| 新建、已有工程补齐、受管理哈希、冲突候选与恢复 | init_project.py 保留；新增配置档和宿主参数 |
| Godot 4.7 全文 Markdown、索引、来源哈希、许可与增量同步 | 原快照完整保留；其他版本可显式快照或官网模式 |
| Main/World/UI 可编辑场景、typed GDScript、Resource、信号规范 | 保留在项目模板与 godot-dev 专题 |
| 场景/资源真实加载、格式、诊断、导入、运行、行为检查 | 原 check.ps1/check_project.py/check_editor_structure.gd 保留 |
| init 工作目录标记、边界校验、定向清理 | 原 init_workspace.ps1 保留 |
| Explorer Shell 启动、MSIX 重定向保护、原生 Desktop API | desktop-wai 保留；Desktop 1.1.7 门禁不放宽 |
| Standalone 创建、实际 ID/路径归属、共享权重校验、独立依赖/节点/I/O | desktop-wai 完整保留，不复制权重 |
| WAI API/UI 工作流、来源/许可、预检与任务回执 | desktop-wai 保留；其他媒体由 dev 按实际模型配置 |
| 项目 MCP stdio、隔离缓存、端口进程身份、无全局 fallback | 保留；新增 Harness overlay，Codex 配置继续可用 |
| 新进程、实际开始菜单可见性、队列为空再停止、状态恢复 | 原 Desktop 流程与失败回归保留 |
| 九类 dev 专题、社区来源审阅、正式素材、行为/编辑器/视听验收 | 保留；缺少 init 文档/工具的普通项目可直接使用 |
| 新增 | 双宿主安装器、事务回滚、doctor、现有 API 模式、发布包、CI |

本次 Windows 实测版本：Godot 4.7.2，Codex CLI 0.163.0-alpha.10.2，Harness 0.2.0-rc.2，Comfy Desktop 1.1.7.0。跨版本兼容不得从此自动推断。普通 dev 不限制某个 Godot 次版本，以实际项目为准；引擎/文档有差异时真实解析运行结果优先。

不会自动安装新模型、绕过许可、上传到云端、发布远程仓库或更改已有游戏。端点连接与 MCP 加载验证不同于出图/音乐质量验收；本次重构没有重复完整游戏生成或独立模型行为前测。
