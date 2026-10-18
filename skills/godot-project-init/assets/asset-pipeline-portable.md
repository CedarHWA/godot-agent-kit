# 项目素材制作

以 `.bootstrap/state.json` 的 profile 为准。`core` 不配置生成服务；`endpoint` 使用 `.local/comfyui-endpoint.json` 中明确指定的现有 ComfyUI。已有素材满足需求时无需启动生成服务。

`core` 项目需要生成素材时，先沿用用户已有流程；若选择本工具的自动化，可用初始化器显式 `--profile endpoint --migrate-profile --config <本机配置>`，或选 `desktop-wai`。不要把共享库有模型当作工作流已经可用。切换模式不删除旧绑定或服务，审阅冲突后继续。

## 现有 ComfyUI API

`tools/comfy_endpoint.py` 使用 Python 标准库，不依赖特定 Agent 的 MCP 工具名。该模式不安装依赖、不改服务器全局配置、不启动或停止外部实例。服务端环境和输入输出的隔离由其所有者负责；需要自动创建隔离实例时选 `desktop-wai`。

```powershell
python tools/comfy_endpoint.py status
python tools/comfy_endpoint.py nodes
python tools/comfy_endpoint.py validate --workflow tools/comfyui/workflows/example.api.json
python tools/comfy_endpoint.py submit --workflow tools/comfyui/workflows/example.api.json --receipt work/dev-task/job.json
python tools/comfy_endpoint.py history --prompt-id <实际ID>
python tools/comfy_endpoint.py fetch --prompt-id <实际ID> --output work/dev-task/output
```

示例 workflow 路径需替换为本项目实际配置的工作流，不提供空图或静音模板。根据 `/object_info` 的真实节点、输入类型和可用模型配置图片、音乐或音效流程。预检只检查节点、必填输入、连接和模型枚举；提交时服务端继续验证。提交回执立即持久化。传输失败是未知结果，先查队列/历史，不能盲目重新提交。输出下载到新的本轮目录，已存在的文件不会覆盖。endpoint CLI 当前不负责上传输入文件；需编辑图片/音频时，使用现有 ComfyUI UI 或项目已配置并验证的 MCP 上传接口。

## 资源接入与验收

同一角色/场景保留风格与参考图；重任务根据实际可用显存串行安排。记录模型、来源、哈希、许可证/用途、工作流、种子、提示词、prompt_id 和后处理。许可未核实则明确标注。正式素材放 `assets/<媒体类型>/<用途>/`，证据放 `docs/assets/<素材ID>/`，工作流放 `tools/comfyui/workflows/`。遵守 `docs/asset-policy.json`。

实际查看图片的构图、透明度、边缘和风格，试听音乐的循环接缝、截断与响度、音效瞬态及尾音。空图、静音、文件存在或生成成功均不能代替验收。导入 Godot 后用 Texture2D/AudioStream/Resource 暴露编辑入口，游戏运行不依赖生成服务。

请求、副本和未采用样例集中在本轮 `work/` 目录；保存可恢复回执和最终来源证据，再清理已无用途的文件。未知提交结果、失败现场或进行中的任务先保留。
