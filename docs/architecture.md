# 工具包结构与边界

`skills/godot-dev` 是开发技能的唯一源码。`skills/godot-project-init` 包含初始化脚本、项目模板、官方快照和可选素材 profile，能在没有 Agent 专属工具的环境由 CLI 直接运行。`toolkit/cli.py` 安装整个技能，构建 init 内的 dev 模板时改名 SKILL.md.template，防止 Codex 递归发现重复入口。

安装器和项目初始化器使用两层独立状态：技能根 `.godot-agent-kit` 保存安装事务/文件哈希；游戏 `.bootstrap` 保存项目模板归属。升级保留用户修改，不以内容相同为由认领外部文件。安装回滚先核验全部目标和备份，再按单个根恢复；用户级 both 两个根分别有恢复记录。

推荐生命周期是用户级 init → 在选定游戏目录运行初始化器 → 生成项目级 dev。内附 dev 使用非入口文件名，只有生成到项目后才作为技能被发现。各项目获得独立副本，更新或卸载用户级 init 不扫描或改写已有项目；显式升级某个项目时由 `.bootstrap` 保护其定制。独立安装 dev、项目级 init、双技能安装与自定义技能根仍由原安装器支持。命令默认值保持兼容，推荐路径用显式 `--scope user --skills init` 选择。

宿主适配只决定技能发现根与 MCP 输出。Codex 使用 TOML 的单个服务段；Harness 使用明确传给 --patch 的项目 Cordis overlay。两个宿主共享技能正文、文件工具和行为要求，工具参数以实际能力为准。

环境发现位于 environment.py；doctor.py 只探测，不安装或启动服务。core 与 endpoint 不调用 Desktop。desktop-wai 的原有 Desktop 创建、Shell 启动、共享模型、归属和 MCP 隔离代码保留，host_mcp.py 负责配置宿主差异。已有 API 的轻量客户端不取得服务器生命周期所有权。

项目检查在生成的 tools/check.ps1/check_project.py 中执行真实 Godot CLI，隔离便携引擎配置。技能仓库 tools/check.ps1 运行 Python 回归和包校验，可选安装包 Godot 集成。host_smoke.py 用实际宿主加载器，模型行为/感官验收独立列为边界。

发布白名单位于 toolkit/build.py；不包含本机配置、虚拟环境、工作缓存、权重或游戏素材。离线文档原始字节受 .gitattributes 保护并逐页核验哈希。新增宿主无需修改玩法技能内容，只增加明确适配与实际发现测试。
