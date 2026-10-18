# 宿主适配

技能正文使用相同 Agent Skills 目录格式。两种宿主差异仅限发现路径、调用语法、项目名信息和 MCP 配置；不依赖 Codex 独有的项目列表、工具命名或子代理能力。

推荐在下表的用户根只安装 `godot-project-init`，初始化时再按项目的 `--agent` 在项目根生成 `godot-dev`。安装时的 `-Agent` 选择哪些宿主能调用 init；初始化时的 `--agent` 决定目标项目的技能路径与 MCP 格式，两者可分别选择。表中所有范围仍支持 init、dev 或 both 的显式安装，不要求两个技能都全局安装。

| 模式 | 项目技能根 | 用户技能根 | 显式调用 |
| --- | --- | --- | --- |
| Codex | `.agents/skills` | `$CODEX_HOME/skills`，默认 `~/.codex/skills` | `$godot-project-init` / `$godot-dev` |
| Harness | `.dsh/skills` | `$DSH_HOME/skills`，默认 `~/.dsh/skills` | `/godot-project-init` / `/godot-dev` |
| both | `.agents/skills`（一份共用） | 分别安装到上述两个用户目录 | 按当前宿主语法 |

Codex 官方文档也列出共享 `~/.agents/skills`，但本次 Windows 隔离用户测试不能通过重定向 USERPROFILE 验证该目录，故默认使用实际验证通过的 CODEX_HOME/skills。已确认自己的宿主支持共享目录时可 `-SkillsDir` 显式选择。Harness 还支持 DSH_AGENTS_HOME 与自定义 roots；改过这些配置时指定实际目录。用户级 both 为两份安装，各自有收据/回滚历史；先预检两个根再应用。断电恢复按各自 pending 日志处理，不宣称跨目录全局事务。`-SkillsDir` 总是覆盖自动选根，只安装到指定的一个目录。

Harness 的 projectRoot 是最近的 `.git` 上级；无 `.git` 才使用 cwd。仓库子目录中的独立游戏需保证技能位于实际项目根，或显式配置 customSkillDirs。项目已有同名用户技能时注意优先级；Codex 同名技能可能同时出现，不能把多个名称当作合并。初始化器内部 dev 模板使用 `SKILL.md.template`，生成游戏时再恢复 SKILL.md，防止递归扫描误发现。

Codex 项目 MCP 使用 `.codex/config.toml`，合并时保留其他服务；已有同名配置不同则拒绝覆盖。Harness 使用独立的 `.dsh/comfyui.cordis.yml`，包含一个 insert patch：

```powershell
dsh web --patch .dsh/comfyui.cordis.yml
# 验证配置组合，不启动 MCP、不调用模型：
dsh headless --patch .dsh/comfyui.cordis.yml --dump-config
```

补丁不自动进入全局 profile。技能可先用项目 `tools/project_comfyui.py call` 调用真实 stdio 服务。新补丁生成不代表当前聊天已热加载。

测试入口 `tests/host_smoke.py` 使用 Codex app-server 的 skills/list 和已安装 Harness 的 FileSystemSkillProvider，核对推荐布局中用户 init 与项目 dev 的来源，同时保留项目双技能和用户双技能的加载验证；不发送模型请求。Harness Desktop 可用自身 Electron Node runtime 读取 app.asar 内模块；npm 安装可传 Node 和实际 module 路径。CLI 示例见 acceptance.md。

来源：官方 [Codex Skills](https://developers.openai.com/codex/skills)、[Codex MCP](https://developers.openai.com/codex/mcp)、[Harness 文件系统技能提供者](https://github.com/deepseek-ai/deepseek-harness/tree/master/packages/skill/skill-filesystem)、[Harness MCP 客户端](https://github.com/deepseek-ai/deepseek-harness/tree/master/packages/mcp/mcp-client)、[官方 MCP overlay 示例](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/user/guide/mcp-memory.md)。版本实测记录见 acceptance.md；Harness 仍为 developer preview，后续版本应复验。
