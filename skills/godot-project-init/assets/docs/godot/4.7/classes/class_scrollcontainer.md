> Source: https://docs.godotengine.org/en/4.7/classes/class_scrollcontainer.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="scrollcontainer"></a>

<a id="class-scrollcontainer"></a>

# ScrollContainer

**Inherits:** [Container](class_container.md#class-container) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [EditorInspector](class_editorinspector.md#class-editorinspector)

A container used to provide scrollbars to a child control when needed.

<a id="description"></a>

## Description

A container used to provide a child control with scrollbars when needed. Scrollbars will automatically be drawn at the right (for vertical) or bottom (for horizontal) and will enable dragging to move the viewable Control (and its children) within the ScrollContainer. Scrollbars will also automatically resize the grabber based on the [Control.custom_minimum_size](class_control.md#class-control-property-custom-minimum-size) of the Control relative to the ScrollContainer.

<a id="tutorials"></a>

## Tutorials

- [Using Containers](../tutorials/ui/gui_containers.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | clip_contents | `true` (overrides [Control](class_control.md#class-control-property-clip-contents)) |
| [bool](class_bool.md#class-bool) | [draw_focus_border](class_scrollcontainer.md#class-scrollcontainer-property-draw-focus-border) | `false` |
| [bool](class_bool.md#class-bool) | [follow_focus](class_scrollcontainer.md#class-scrollcontainer-property-follow-focus) | `false` |
| [ScrollMode](class_scrollcontainer.md#enum-scrollcontainer-scrollmode) | [horizontal_scroll_mode](class_scrollcontainer.md#class-scrollcontainer-property-horizontal-scroll-mode) | `1` |
| [bool](class_bool.md#class-bool) | propagate_maximum_size | `false` (overrides [Control](class_control.md#class-control-property-propagate-maximum-size)) |
| [int](class_int.md#class-int) | [scroll_deadzone](class_scrollcontainer.md#class-scrollcontainer-property-scroll-deadzone) | `0` |
| [ScrollHintMode](class_scrollcontainer.md#enum-scrollcontainer-scrollhintmode) | [scroll_hint_mode](class_scrollcontainer.md#class-scrollcontainer-property-scroll-hint-mode) | `0` |
| [int](class_int.md#class-int) | [scroll_horizontal](class_scrollcontainer.md#class-scrollcontainer-property-scroll-horizontal) | `0` |
| [bool](class_bool.md#class-bool) | [scroll_horizontal_by_default](class_scrollcontainer.md#class-scrollcontainer-property-scroll-horizontal-by-default) | `false` |
| [float](class_float.md#class-float) | [scroll_horizontal_custom_step](class_scrollcontainer.md#class-scrollcontainer-property-scroll-horizontal-custom-step) | `-1.0` |
| [int](class_int.md#class-int) | [scroll_vertical](class_scrollcontainer.md#class-scrollcontainer-property-scroll-vertical) | `0` |
| [float](class_float.md#class-float) | [scroll_vertical_custom_step](class_scrollcontainer.md#class-scrollcontainer-property-scroll-vertical-custom-step) | `-1.0` |
| [bool](class_bool.md#class-bool) | [tile_scroll_hint](class_scrollcontainer.md#class-scrollcontainer-property-tile-scroll-hint) | `false` |
| [ScrollMode](class_scrollcontainer.md#enum-scrollcontainer-scrollmode) | [vertical_scroll_mode](class_scrollcontainer.md#class-scrollcontainer-property-vertical-scroll-mode) | `1` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [ensure_control_visible](class_scrollcontainer.md#class-scrollcontainer-method-ensure-control-visible)(control: [Control](class_control.md#class-control)) |
| [HScrollBar](class_hscrollbar.md#class-hscrollbar) | [get_h_scroll_bar](class_scrollcontainer.md#class-scrollcontainer-method-get-h-scroll-bar)() |
| [VScrollBar](class_vscrollbar.md#class-vscrollbar) | [get_v_scroll_bar](class_scrollcontainer.md#class-scrollcontainer-method-get-v-scroll-bar)() |

<a id="theme-properties"></a>

## Theme Properties

|  |  |  |
| --- | --- | --- |
| [Color](class_color.md#class-color) | [scroll_hint_horizontal_color](class_scrollcontainer.md#class-scrollcontainer-theme-color-scroll-hint-horizontal-color) | `Color(0, 0, 0, 1)` |
| [Color](class_color.md#class-color) | [scroll_hint_vertical_color](class_scrollcontainer.md#class-scrollcontainer-theme-color-scroll-hint-vertical-color) | `Color(0, 0, 0, 1)` |
| [int](class_int.md#class-int) | [scrollbar_h_separation](class_scrollcontainer.md#class-scrollcontainer-theme-constant-scrollbar-h-separation) | `0` |
| [int](class_int.md#class-int) | [scrollbar_v_separation](class_scrollcontainer.md#class-scrollcontainer-theme-constant-scrollbar-v-separation) | `0` |
| [Texture2D](class_texture2d.md#class-texture2d) | [scroll_hint_horizontal](class_scrollcontainer.md#class-scrollcontainer-theme-icon-scroll-hint-horizontal) |  |
| [Texture2D](class_texture2d.md#class-texture2d) | [scroll_hint_vertical](class_scrollcontainer.md#class-scrollcontainer-theme-icon-scroll-hint-vertical) |  |
| [StyleBox](class_stylebox.md#class-stylebox) | [focus](class_scrollcontainer.md#class-scrollcontainer-theme-style-focus) |  |
| [StyleBox](class_stylebox.md#class-stylebox) | [panel](class_scrollcontainer.md#class-scrollcontainer-theme-style-panel) |  |

---


<a id="signals"></a>

## Signals

<a id="class-scrollcontainer-signal-scroll-ended"></a>

**scroll_ended**() [🔗](class_scrollcontainer.md#class-scrollcontainer-signal-scroll-ended)

Emitted when scrolling stops when dragging the scrollable area *with a touch event*. This signal is *not* emitted when scrolling by dragging the scrollbar, scrolling with the mouse wheel or scrolling with keyboard/gamepad events.

**Note:** This signal is only emitted on Android or iOS, or on desktop/web platforms when [ProjectSettings.input_devices/pointing/emulate_touch_from_mouse](class_projectsettings.md#class-projectsettings-property-input-devices-pointing-emulate-touch-from-mouse) is enabled.

---


<a id="class-scrollcontainer-signal-scroll-started"></a>

**scroll_started**() [🔗](class_scrollcontainer.md#class-scrollcontainer-signal-scroll-started)

Emitted when scrolling starts when dragging the scrollable area *with a touch event*. This signal is *not* emitted when scrolling by dragging the scrollbar, scrolling with the mouse wheel or scrolling with keyboard/gamepad events.

**Note:** This signal is only emitted on Android or iOS, or on desktop/web platforms when [ProjectSettings.input_devices/pointing/emulate_touch_from_mouse](class_projectsettings.md#class-projectsettings-property-input-devices-pointing-emulate-touch-from-mouse) is enabled.

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-scrollcontainer-scrollmode"></a>

enum **ScrollMode**: [🔗](class_scrollcontainer.md#enum-scrollcontainer-scrollmode)

<a id="class-scrollcontainer-constant-scroll-mode-disabled"></a>

[ScrollMode](class_scrollcontainer.md#enum-scrollcontainer-scrollmode) **SCROLL_MODE_DISABLED** = `0`

Scrolling disabled, scrollbar will be invisible.

<a id="class-scrollcontainer-constant-scroll-mode-auto"></a>

[ScrollMode](class_scrollcontainer.md#enum-scrollcontainer-scrollmode) **SCROLL_MODE_AUTO** = `1`

Scrolling enabled, scrollbar will be visible only if necessary, i.e. container's content is bigger than the container.

<a id="class-scrollcontainer-constant-scroll-mode-show-always"></a>

[ScrollMode](class_scrollcontainer.md#enum-scrollcontainer-scrollmode) **SCROLL_MODE_SHOW_ALWAYS** = `2`

Scrolling enabled, scrollbar will be always visible.

<a id="class-scrollcontainer-constant-scroll-mode-show-never"></a>

[ScrollMode](class_scrollcontainer.md#enum-scrollcontainer-scrollmode) **SCROLL_MODE_SHOW_NEVER** = `3`

Scrolling enabled, scrollbar will be hidden.

<a id="class-scrollcontainer-constant-scroll-mode-reserve"></a>

[ScrollMode](class_scrollcontainer.md#enum-scrollcontainer-scrollmode) **SCROLL_MODE_RESERVE** = `4`

Combines [SCROLL_MODE_AUTO](class_scrollcontainer.md#class-scrollcontainer-constant-scroll-mode-auto) and [SCROLL_MODE_SHOW_ALWAYS](class_scrollcontainer.md#class-scrollcontainer-constant-scroll-mode-show-always). The scrollbar is only visible if necessary, but the content size is adjusted as if it was always visible. It's useful for ensuring that content size stays the same regardless if the scrollbar is visible.

<a id="class-scrollcontainer-constant-scroll-mode-maximize-first"></a>

[ScrollMode](class_scrollcontainer.md#enum-scrollcontainer-scrollmode) **SCROLL_MODE_MAXIMIZE_FIRST** = `5`

Behaves like [SCROLL_MODE_AUTO](class_scrollcontainer.md#class-scrollcontainer-constant-scroll-mode-auto), but makes the **ScrollContainer** report a minimum size based on its content (limited by [Control.custom_maximum_size](class_control.md#class-control-property-custom-maximum-size) when set on the corresponding axis). This allows it to grow first and only start scrolling once constrained.

---


<a id="enum-scrollcontainer-scrollhintmode"></a>

enum **ScrollHintMode**: [🔗](class_scrollcontainer.md#enum-scrollcontainer-scrollhintmode)

<a id="class-scrollcontainer-constant-scroll-hint-mode-disabled"></a>

[ScrollHintMode](class_scrollcontainer.md#enum-scrollcontainer-scrollhintmode) **SCROLL_HINT_MODE_DISABLED** = `0`

Scroll hints will never be shown.

<a id="class-scrollcontainer-constant-scroll-hint-mode-all"></a>

[ScrollHintMode](class_scrollcontainer.md#enum-scrollcontainer-scrollhintmode) **SCROLL_HINT_MODE_ALL** = `1`

Scroll hints will be shown at the top and bottom (if vertical), or left and right (if horizontal).

<a id="class-scrollcontainer-constant-scroll-hint-mode-top-and-left"></a>

[ScrollHintMode](class_scrollcontainer.md#enum-scrollcontainer-scrollhintmode) **SCROLL_HINT_MODE_TOP_AND_LEFT** = `2`

Scroll hints will be shown at the top (if vertical), or the left (if horizontal).

<a id="class-scrollcontainer-constant-scroll-hint-mode-bottom-and-right"></a>

[ScrollHintMode](class_scrollcontainer.md#enum-scrollcontainer-scrollhintmode) **SCROLL_HINT_MODE_BOTTOM_AND_RIGHT** = `3`

Scroll hints will be shown at the bottom (if horizontal), or the right (if horizontal).

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-scrollcontainer-property-draw-focus-border"></a>

[bool](class_bool.md#class-bool) **draw_focus_border** = `false` [🔗](class_scrollcontainer.md#class-scrollcontainer-property-draw-focus-border)

- void **set_draw_focus_border**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_draw_focus_border**()

If `true`, [focus](class_scrollcontainer.md#class-scrollcontainer-theme-style-focus) is drawn when the ScrollContainer or one of its descendant nodes is focused.

---


<a id="class-scrollcontainer-property-follow-focus"></a>

[bool](class_bool.md#class-bool) **follow_focus** = `false` [🔗](class_scrollcontainer.md#class-scrollcontainer-property-follow-focus)

- void **set_follow_focus**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_following_focus**()

If `true`, the ScrollContainer will automatically scroll to focused children (including indirect children) to make sure they are fully visible.

---


<a id="class-scrollcontainer-property-horizontal-scroll-mode"></a>

[ScrollMode](class_scrollcontainer.md#enum-scrollcontainer-scrollmode) **horizontal_scroll_mode** = `1` [🔗](class_scrollcontainer.md#class-scrollcontainer-property-horizontal-scroll-mode)

- void **set_horizontal_scroll_mode**(value: [ScrollMode](class_scrollcontainer.md#enum-scrollcontainer-scrollmode))
- [ScrollMode](class_scrollcontainer.md#enum-scrollcontainer-scrollmode) **get_horizontal_scroll_mode**()

Controls whether horizontal scrollbar can be used and when it should be visible.

---


<a id="class-scrollcontainer-property-scroll-deadzone"></a>

[int](class_int.md#class-int) **scroll_deadzone** = `0` [🔗](class_scrollcontainer.md#class-scrollcontainer-property-scroll-deadzone)

- void **set_deadzone**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_deadzone**()

Deadzone for touch scrolling. Lower deadzone makes the scrolling more sensitive.

---


<a id="class-scrollcontainer-property-scroll-hint-mode"></a>

[ScrollHintMode](class_scrollcontainer.md#enum-scrollcontainer-scrollhintmode) **scroll_hint_mode** = `0` [🔗](class_scrollcontainer.md#class-scrollcontainer-property-scroll-hint-mode)

- void **set_scroll_hint_mode**(value: [ScrollHintMode](class_scrollcontainer.md#enum-scrollcontainer-scrollhintmode))
- [ScrollHintMode](class_scrollcontainer.md#enum-scrollcontainer-scrollhintmode) **get_scroll_hint_mode**()

The way which scroll hints (indicators that show that the content can still be scrolled in a certain direction) will be shown.

**Note:** Hints won't be shown if the content can be scrolled both vertically and horizontally.

---


<a id="class-scrollcontainer-property-scroll-horizontal"></a>

[int](class_int.md#class-int) **scroll_horizontal** = `0` [🔗](class_scrollcontainer.md#class-scrollcontainer-property-scroll-horizontal)

- void **set_h_scroll**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_h_scroll**()

The current horizontal scroll value.

**Note:** If you are setting this value in the [Node._ready()](class_node.md#class-node-private-method-ready) function or earlier, it needs to be wrapped with [Object.set_deferred()](class_object.md#class-object-method-set-deferred), since scroll bar's [Range.max_value](class_range.md#class-range-property-max-value) is not initialized yet.

```gdscript
func _ready():
    set_deferred("scroll_horizontal", 600)
```

---


<a id="class-scrollcontainer-property-scroll-horizontal-by-default"></a>

[bool](class_bool.md#class-bool) **scroll_horizontal_by_default** = `false` [🔗](class_scrollcontainer.md#class-scrollcontainer-property-scroll-horizontal-by-default)

- void **set_scroll_horizontal_by_default**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_scroll_horizontal_by_default**()

If `true`, the mouse wheel scrolls the view horizontally, and holding `Shift` scrolls vertically.

If `false` (default), the mouse wheel scrolls the view vertically, and holding `Shift` scrolls horizontally.

---


<a id="class-scrollcontainer-property-scroll-horizontal-custom-step"></a>

[float](class_float.md#class-float) **scroll_horizontal_custom_step** = `-1.0` [🔗](class_scrollcontainer.md#class-scrollcontainer-property-scroll-horizontal-custom-step)

- void **set_horizontal_custom_step**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_horizontal_custom_step**()

Overrides the [ScrollBar.custom_step](class_scrollbar.md#class-scrollbar-property-custom-step) used when clicking the internal scroll bar's horizontal increment and decrement buttons or when using arrow keys when the [ScrollBar](class_scrollbar.md#class-scrollbar) is focused.

---


<a id="class-scrollcontainer-property-scroll-vertical"></a>

[int](class_int.md#class-int) **scroll_vertical** = `0` [🔗](class_scrollcontainer.md#class-scrollcontainer-property-scroll-vertical)

- void **set_v_scroll**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_v_scroll**()

The current vertical scroll value.

**Note:** Setting it early needs to be deferred, just like in [scroll_horizontal](class_scrollcontainer.md#class-scrollcontainer-property-scroll-horizontal).

```gdscript
func _ready():
    set_deferred("scroll_vertical", 600)
```

---


<a id="class-scrollcontainer-property-scroll-vertical-custom-step"></a>

[float](class_float.md#class-float) **scroll_vertical_custom_step** = `-1.0` [🔗](class_scrollcontainer.md#class-scrollcontainer-property-scroll-vertical-custom-step)

- void **set_vertical_custom_step**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_vertical_custom_step**()

Overrides the [ScrollBar.custom_step](class_scrollbar.md#class-scrollbar-property-custom-step) used when clicking the internal scroll bar's vertical increment and decrement buttons or when using arrow keys when the [ScrollBar](class_scrollbar.md#class-scrollbar) is focused.

---


<a id="class-scrollcontainer-property-tile-scroll-hint"></a>

[bool](class_bool.md#class-bool) **tile_scroll_hint** = `false` [🔗](class_scrollcontainer.md#class-scrollcontainer-property-tile-scroll-hint)

- void **set_tile_scroll_hint**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_scroll_hint_tiled**()

If `true`, the scroll hint texture will be tiled instead of stretched. See [scroll_hint_mode](class_scrollcontainer.md#class-scrollcontainer-property-scroll-hint-mode).

---


<a id="class-scrollcontainer-property-vertical-scroll-mode"></a>

[ScrollMode](class_scrollcontainer.md#enum-scrollcontainer-scrollmode) **vertical_scroll_mode** = `1` [🔗](class_scrollcontainer.md#class-scrollcontainer-property-vertical-scroll-mode)

- void **set_vertical_scroll_mode**(value: [ScrollMode](class_scrollcontainer.md#enum-scrollcontainer-scrollmode))
- [ScrollMode](class_scrollcontainer.md#enum-scrollcontainer-scrollmode) **get_vertical_scroll_mode**()

Controls whether vertical scrollbar can be used and when it should be visible.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-scrollcontainer-method-ensure-control-visible"></a>

void **ensure_control_visible**(control: [Control](class_control.md#class-control)) [🔗](class_scrollcontainer.md#class-scrollcontainer-method-ensure-control-visible)

Ensures the given `control` is visible (must be a direct or indirect child of the ScrollContainer). Used by [follow_focus](class_scrollcontainer.md#class-scrollcontainer-property-follow-focus).

**Note:** This will not work on a node that was just added during the same frame. If you want to scroll to a newly added child, you must wait until the next frame using [SceneTree.process_frame](class_scenetree.md#class-scenetree-signal-process-frame):

```gdscript
add_child(child_node)
await get_tree().process_frame
ensure_control_visible(child_node)
```

---


<a id="class-scrollcontainer-method-get-h-scroll-bar"></a>

[HScrollBar](class_hscrollbar.md#class-hscrollbar) **get_h_scroll_bar**() [🔗](class_scrollcontainer.md#class-scrollcontainer-method-get-h-scroll-bar)

Returns the horizontal scrollbar [HScrollBar](class_hscrollbar.md#class-hscrollbar) of this **ScrollContainer**.

**Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to disable or hide a scrollbar, you can use [horizontal_scroll_mode](class_scrollcontainer.md#class-scrollcontainer-property-horizontal-scroll-mode).

---


<a id="class-scrollcontainer-method-get-v-scroll-bar"></a>

[VScrollBar](class_vscrollbar.md#class-vscrollbar) **get_v_scroll_bar**() [🔗](class_scrollcontainer.md#class-scrollcontainer-method-get-v-scroll-bar)

Returns the vertical scrollbar [VScrollBar](class_vscrollbar.md#class-vscrollbar) of this **ScrollContainer**.

**Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to disable or hide a scrollbar, you can use [vertical_scroll_mode](class_scrollcontainer.md#class-scrollcontainer-property-vertical-scroll-mode).

---


<a id="theme-property-descriptions"></a>

## Theme Property Descriptions

<a id="class-scrollcontainer-theme-color-scroll-hint-horizontal-color"></a>

[Color](class_color.md#class-color) **scroll_hint_horizontal_color** = `Color(0, 0, 0, 1)` [🔗](class_scrollcontainer.md#class-scrollcontainer-theme-color-scroll-hint-horizontal-color)

[Color](class_color.md#class-color) used to modulate the [scroll_hint_horizontal](class_scrollcontainer.md#class-scrollcontainer-theme-icon-scroll-hint-horizontal) texture.

---


<a id="class-scrollcontainer-theme-color-scroll-hint-vertical-color"></a>

[Color](class_color.md#class-color) **scroll_hint_vertical_color** = `Color(0, 0, 0, 1)` [🔗](class_scrollcontainer.md#class-scrollcontainer-theme-color-scroll-hint-vertical-color)

[Color](class_color.md#class-color) used to modulate the [scroll_hint_vertical](class_scrollcontainer.md#class-scrollcontainer-theme-icon-scroll-hint-vertical) texture.

---


<a id="class-scrollcontainer-theme-constant-scrollbar-h-separation"></a>

[int](class_int.md#class-int) **scrollbar_h_separation** = `0` [🔗](class_scrollcontainer.md#class-scrollcontainer-theme-constant-scrollbar-h-separation)

The space between the ScrollContainer's vertical scroll bar and its content, in pixels. No space will be added when the content's minimum size is larger than the ScrollContainer's size.

---


<a id="class-scrollcontainer-theme-constant-scrollbar-v-separation"></a>

[int](class_int.md#class-int) **scrollbar_v_separation** = `0` [🔗](class_scrollcontainer.md#class-scrollcontainer-theme-constant-scrollbar-v-separation)

The space between the ScrollContainer's horizontal scroll bar and its content, in pixels. No space will be added when the content's minimum size is larger than the ScrollContainer's size.

---


<a id="class-scrollcontainer-theme-icon-scroll-hint-horizontal"></a>

[Texture2D](class_texture2d.md#class-texture2d) **scroll_hint_horizontal** [🔗](class_scrollcontainer.md#class-scrollcontainer-theme-icon-scroll-hint-horizontal)

The indicator that will be shown when the content can still be scrolled horizontally. See [scroll_hint_mode](class_scrollcontainer.md#class-scrollcontainer-property-scroll-hint-mode).

---


<a id="class-scrollcontainer-theme-icon-scroll-hint-vertical"></a>

[Texture2D](class_texture2d.md#class-texture2d) **scroll_hint_vertical** [🔗](class_scrollcontainer.md#class-scrollcontainer-theme-icon-scroll-hint-vertical)

The indicator that will be shown when the content can still be scrolled vertically. See [scroll_hint_mode](class_scrollcontainer.md#class-scrollcontainer-property-scroll-hint-mode).

---


<a id="class-scrollcontainer-theme-style-focus"></a>

[StyleBox](class_stylebox.md#class-stylebox) **focus** [🔗](class_scrollcontainer.md#class-scrollcontainer-theme-style-focus)

The focus border [StyleBox](class_stylebox.md#class-stylebox) of the **ScrollContainer**. Only used if [draw_focus_border](class_scrollcontainer.md#class-scrollcontainer-property-draw-focus-border) is `true`.

---


<a id="class-scrollcontainer-theme-style-panel"></a>

[StyleBox](class_stylebox.md#class-stylebox) **panel** [🔗](class_scrollcontainer.md#class-scrollcontainer-theme-style-panel)

The background [StyleBox](class_stylebox.md#class-stylebox) of the **ScrollContainer**.
