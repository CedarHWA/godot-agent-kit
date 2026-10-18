> Source: https://docs.godotengine.org/en/4.7/classes/class_progressbar.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="progressbar"></a>

<a id="class-progressbar"></a>

# ProgressBar

**Inherits:** [Range](class_range.md#class-range) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A control used for visual representation of a percentage.

<a id="description"></a>

## Description

A control used for visual representation of a percentage. Shows the fill percentage in the center. Can also be used to show indeterminate progress. For more fill modes, use [TextureProgressBar](class_textureprogressbar.md#class-textureprogressbar) instead.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [editor_preview_indeterminate](class_progressbar.md#class-progressbar-property-editor-preview-indeterminate) |  |
| [int](class_int.md#class-int) | [fill_mode](class_progressbar.md#class-progressbar-property-fill-mode) | `0` |
| [bool](class_bool.md#class-bool) | [indeterminate](class_progressbar.md#class-progressbar-property-indeterminate) | `false` |
| [bool](class_bool.md#class-bool) | [show_percentage](class_progressbar.md#class-progressbar-property-show-percentage) | `true` |

<a id="theme-properties"></a>

## Theme Properties

|  |  |  |
| --- | --- | --- |
| [Color](class_color.md#class-color) | [font_color](class_progressbar.md#class-progressbar-theme-color-font-color) | `Color(0.95, 0.95, 0.95, 1)` |
| [Color](class_color.md#class-color) | [font_outline_color](class_progressbar.md#class-progressbar-theme-color-font-outline-color) | `Color(0, 0, 0, 1)` |
| [int](class_int.md#class-int) | [outline_size](class_progressbar.md#class-progressbar-theme-constant-outline-size) | `0` |
| [Font](class_font.md#class-font) | [font](class_progressbar.md#class-progressbar-theme-font-font) |  |
| [int](class_int.md#class-int) | [font_size](class_progressbar.md#class-progressbar-theme-font-size-font-size) |  |
| [StyleBox](class_stylebox.md#class-stylebox) | [background](class_progressbar.md#class-progressbar-theme-style-background) |  |
| [StyleBox](class_stylebox.md#class-stylebox) | [fill](class_progressbar.md#class-progressbar-theme-style-fill) |  |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-progressbar-fillmode"></a>

enum **FillMode**: [🔗](class_progressbar.md#enum-progressbar-fillmode)

<a id="class-progressbar-constant-fill-begin-to-end"></a>

[FillMode](class_progressbar.md#enum-progressbar-fillmode) **FILL_BEGIN_TO_END** = `0`

The progress bar fills from begin to end horizontally, according to the language direction. If [Control.is_layout_rtl()](class_control.md#class-control-method-is-layout-rtl) returns `false`, it fills from left to right, and if it returns `true`, it fills from right to left.

<a id="class-progressbar-constant-fill-end-to-begin"></a>

[FillMode](class_progressbar.md#enum-progressbar-fillmode) **FILL_END_TO_BEGIN** = `1`

The progress bar fills from end to begin horizontally, according to the language direction. If [Control.is_layout_rtl()](class_control.md#class-control-method-is-layout-rtl) returns `false`, it fills from right to left, and if it returns `true`, it fills from left to right.

<a id="class-progressbar-constant-fill-top-to-bottom"></a>

[FillMode](class_progressbar.md#enum-progressbar-fillmode) **FILL_TOP_TO_BOTTOM** = `2`

The progress fills from top to bottom.

<a id="class-progressbar-constant-fill-bottom-to-top"></a>

[FillMode](class_progressbar.md#enum-progressbar-fillmode) **FILL_BOTTOM_TO_TOP** = `3`

The progress fills from bottom to top.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-progressbar-property-editor-preview-indeterminate"></a>

[bool](class_bool.md#class-bool) **editor_preview_indeterminate** [🔗](class_progressbar.md#class-progressbar-property-editor-preview-indeterminate)

- void **set_editor_preview_indeterminate**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_editor_preview_indeterminate_enabled**()

If `false`, the [indeterminate](class_progressbar.md#class-progressbar-property-indeterminate) animation will be paused in the editor.

---


<a id="class-progressbar-property-fill-mode"></a>

[int](class_int.md#class-int) **fill_mode** = `0` [🔗](class_progressbar.md#class-progressbar-property-fill-mode)

- void **set_fill_mode**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_fill_mode**()

The fill direction. See [FillMode](class_progressbar.md#enum-progressbar-fillmode) for possible values.

---


<a id="class-progressbar-property-indeterminate"></a>

[bool](class_bool.md#class-bool) **indeterminate** = `false` [🔗](class_progressbar.md#class-progressbar-property-indeterminate)

- void **set_indeterminate**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_indeterminate**()

When set to `true`, the progress bar indicates that something is happening with an animation, but does not show the fill percentage or value.

---


<a id="class-progressbar-property-show-percentage"></a>

[bool](class_bool.md#class-bool) **show_percentage** = `true` [🔗](class_progressbar.md#class-progressbar-property-show-percentage)

- void **set_show_percentage**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_percentage_shown**()

If `true`, the fill percentage is displayed on the bar.

---


<a id="theme-property-descriptions"></a>

## Theme Property Descriptions

<a id="class-progressbar-theme-color-font-color"></a>

[Color](class_color.md#class-color) **font_color** = `Color(0.95, 0.95, 0.95, 1)` [🔗](class_progressbar.md#class-progressbar-theme-color-font-color)

The color of the text.

---


<a id="class-progressbar-theme-color-font-outline-color"></a>

[Color](class_color.md#class-color) **font_outline_color** = `Color(0, 0, 0, 1)` [🔗](class_progressbar.md#class-progressbar-theme-color-font-outline-color)

The tint of text outline of the **ProgressBar**.

---


<a id="class-progressbar-theme-constant-outline-size"></a>

[int](class_int.md#class-int) **outline_size** = `0` [🔗](class_progressbar.md#class-progressbar-theme-constant-outline-size)

The size of the text outline.

**Note:** If using a font with [FontFile.multichannel_signed_distance_field](class_fontfile.md#class-fontfile-property-multichannel-signed-distance-field) enabled, its [FontFile.msdf_pixel_range](class_fontfile.md#class-fontfile-property-msdf-pixel-range) must be set to at least *twice* the value of [outline_size](class_progressbar.md#class-progressbar-theme-constant-outline-size) for outline rendering to look correct. Otherwise, the outline may appear to be cut off earlier than intended.

---


<a id="class-progressbar-theme-font-font"></a>

[Font](class_font.md#class-font) **font** [🔗](class_progressbar.md#class-progressbar-theme-font-font)

Font used to draw the fill percentage if [show_percentage](class_progressbar.md#class-progressbar-property-show-percentage) is `true`.

---


<a id="class-progressbar-theme-font-size-font-size"></a>

[int](class_int.md#class-int) **font_size** [🔗](class_progressbar.md#class-progressbar-theme-font-size-font-size)

Font size used to draw the fill percentage if [show_percentage](class_progressbar.md#class-progressbar-property-show-percentage) is `true`.

---


<a id="class-progressbar-theme-style-background"></a>

[StyleBox](class_stylebox.md#class-stylebox) **background** [🔗](class_progressbar.md#class-progressbar-theme-style-background)

The style of the background.

---


<a id="class-progressbar-theme-style-fill"></a>

[StyleBox](class_stylebox.md#class-stylebox) **fill** [🔗](class_progressbar.md#class-progressbar-theme-style-fill)

The style of the progress (i.e. the part that fills the bar).
