# 版本记录

## 2.0.0 — 2026-10-17

- 从个人初始化器与项目 dev 技能整理为独立 Windows 技能仓库。
- 支持 Codex、DeepSeek Harness 和双宿主共用目录，补充实际宿主发现与 Harness MCP overlay 验证。
- 移除发布包中的本机配置；工具发现、环境检查与 core / desktop-wai / endpoint 分离。
- 保留原有完整 Desktop/WAI 流程、官方文档快照、Godot 检查、项目归属保护与安全清理。
- dev 可在未经初始化器处理的 Godot 项目独立使用。
- 新增安装/升级/回滚/恢复/卸载、冲突保护、测试、Windows CI 与确定性发布包。
- 内附 dev 模板在安装时从唯一源码生成，避免 Codex 递归发现重复技能。
