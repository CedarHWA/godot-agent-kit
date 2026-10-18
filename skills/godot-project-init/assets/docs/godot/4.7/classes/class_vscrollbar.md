> Source: https://docs.godotengine.org/en/4.7/classes/class_vscrollbar.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="vscrollbar"></a>

<a id="class-vscrollbar"></a>

# VScrollBar

**Inherits:** [ScrollBar](class_scrollbar.md#class-scrollbar) **<** [Range](class_range.md#class-range) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A vertical scrollbar that goes from top (min) to bottom (max).

<a id="description"></a>

## Description

A vertical scrollbar, typically used to navigate through content that extends beyond the visible height of a control. It is a [Range](class_range.md#class-range)-based control and goes from top (min) to bottom (max). Note that this direction is the opposite of [VSlider](class_vslider.md#class-vslider)'s.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| BitField[[SizeFlags](class_control.md#enum-control-sizeflags)] | size_flags_horizontal | `0` (overrides [Control](class_control.md#class-control-property-size-flags-horizontal)) |
| BitField[[SizeFlags](class_control.md#enum-control-sizeflags)] | size_flags_vertical | `1` (overrides [Control](class_control.md#class-control-property-size-flags-vertical)) |

<a id="theme-properties"></a>

## Theme Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [padding_left](class_vscrollbar.md#class-vscrollbar-theme-constant-padding-left) | `0` |
| [int](class_int.md#class-int) | [padding_right](class_vscrollbar.md#class-vscrollbar-theme-constant-padding-right) | `0` |

---


<a id="theme-property-descriptions"></a>

## Theme Property Descriptions

<a id="class-vscrollbar-theme-constant-padding-left"></a>

[int](class_int.md#class-int) **padding_left** = `0` [🔗](class_vscrollbar.md#class-vscrollbar-theme-constant-padding-left)

Padding between the left of the [ScrollBar.scroll](class_scrollbar.md#class-scrollbar-theme-style-scroll) element and the [ScrollBar.grabber](class_scrollbar.md#class-scrollbar-theme-style-grabber).

**Note:** To apply vertical padding, modify the top/bottom content margins of [ScrollBar.scroll](class_scrollbar.md#class-scrollbar-theme-style-scroll) instead.

---


<a id="class-vscrollbar-theme-constant-padding-right"></a>

[int](class_int.md#class-int) **padding_right** = `0` [🔗](class_vscrollbar.md#class-vscrollbar-theme-constant-padding-right)

Padding between the right of the [ScrollBar.scroll](class_scrollbar.md#class-scrollbar-theme-style-scroll) element and the [ScrollBar.grabber](class_scrollbar.md#class-scrollbar-theme-style-grabber).

**Note:** To apply vertical padding, modify the top/bottom content margins of [ScrollBar.scroll](class_scrollbar.md#class-scrollbar-theme-style-scroll) instead.
