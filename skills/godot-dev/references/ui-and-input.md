# UI、输入与多分辨率

用于菜单、HUD、弹窗、布局、焦点和交互。先确定玩家要完成的操作、支持的输入设备、最小窗口和信息层级；不默认添加用户未要求的平台。

## 布局与皮肤

固定界面保存为场景。列表/排列由合适的 Container 管理，屏幕边界或覆盖层用锚点；自由布局画布、棋盘或特殊 HUD 可以有明确坐标方案。不要强迫所有 UI 都变为容器。

容器负责其直接子 Control 的位置/尺寸，优先调整 minimum size、size flags、stretch ratio、容器间距及 Theme；逐帧写 position/size 会与布局竞争。需要装饰位移/动画时隔开布局节点和表现节点，或核验当前版本支持的变换属性。

字体、颜色、StyleBox、间距与状态外观优先 Theme 及主题类型变体；局部例外允许覆盖。源子场景应能独立预览正确皮肤。确认 normal、hover、pressed、disabled、focus 的视觉区别，不能只靠颜色表达关键状态。中文字体检查缺字、字号、换行和实际字宽；长文本/翻译使用容器、换行或滚动，避免运行时硬改字体补救固定布局。

## 事件路由不能靠遮罩猜测

- 语义操作使用 InputMap；沿用已有动作并检查确实配置。游戏的一次性输入通常用 `_unhandled_input`，控件用 GUI 事件/内置信号。全局 `_input` 只用于确需优先捕获的行为。
- `Input.is_action_pressed()` 等轮询读取全局输入状态，不受 GUI `accept_event()` 影响。打开弹窗/暂停时，还要由 gameplay 状态或 process_mode 阻止相应轮询。
- 装饰层确认 `mouse_filter`；透明 Control 也可能挡点击。模态层应明确阻断下面的鼠标/键盘行为，不能只绘制一张半透明背景。
- 按本功能决定长按、重复键、按下/释放语义。屏幕上存在 Button 不等于玩家输入真正能触发，至少验证一条真实输入路径。

## 焦点与暂停

打开页面/弹窗时在可见且启用的合适控件设置焦点；隐藏/关闭时恢复仍有效的原焦点，否则回到明确默认项。检查 Tab/方向键邻居，动态列表刷新后不保留已释放/隐藏控件路径。模态焦点留在当前面板，Esc 只处理最高层，不能一次关闭对话框又恢复下面牌局。

SceneTree 暂停时菜单仍需能处理输入；分别检查菜单、背景、Timer、Tween 和音频的暂停策略。失焦、重试和返回路径按需求保持一致。

## 验收看玩家实际操作

按目标平台检查基准窗口与最小窗口；有宽屏要求再覆盖宽屏。等待布局完成，检查可见内容、裁切、溢出、点击区域和焦点，区分有意重叠与错误堆叠。至少走“打开 → 操作 → 取消/确认 → 返回”的完整路径。

结构和矩形检查用于定位问题；截图用于检查表现，真实输入用于检查操作。三者不能替代彼此。替换较长中文标题、重排按钮、改 Theme 后保存/重载，应无需改脚本仍正常。报告明确支持/未验证的分辨率和设备。

本地官方入口：Control、Container、Theme、Input、InputMap、Viewport；`tutorials/inputs/inputevent.md`、`tutorials/ui/gui_containers.md`、`tutorials/ui/gui_navigation.md`、`tutorials/ui/gui_using_theme_editor.md`、`tutorials/rendering/multiple_resolutions.md`。
