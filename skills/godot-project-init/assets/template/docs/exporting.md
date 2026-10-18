# 导出约定

目标平台：__PLATFORM__。导出前安装与 Godot __ENGINE_VERSION__ 完全对应的官方导出模板。
首次实际发布需求确定后再创建 export_presets.cfg，避免写入未验证的平台配置。

在每个导出预设的资源过滤器中明确排除：
`docs/*,tools/*,tests/*,.agents/*,.codex/*,.bootstrap/*,.local/*,work/*,builds/*`

docs/tools 已使用 .gdignore 阻止 Godot 导入。tests 不放 .gdignore，因为引擎需要执行其中的 GDScript。
导出后检查产物，确保测试、文档、凭据、原始生成缓存和模型未被包含。导出密码及签名材料不进 Git。
