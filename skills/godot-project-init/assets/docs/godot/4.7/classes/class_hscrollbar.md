> Source: https://docs.godotengine.org/en/4.7/classes/class_hscrollbar.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="hscrollbar"></a>

<a id="class-hscrollbar"></a>

# HScrollBar

**Inherits:** [ScrollBar](class_scrollbar.md#class-scrollbar) **<** [Range](class_range.md#class-range) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A horizontal scrollbar that goes from left (min) to right (max).

<a id="description"></a>

## Description

A horizontal scrollbar, typically used to navigate through content that extends beyond the visible width of a control. It is a [Range](class_range.md#class-range)-based control and goes from left (min) to right (max).

<a id="theme-properties"></a>

## Theme Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [padding_bottom](class_hscrollbar.md#class-hscrollbar-theme-constant-padding-bottom) | `0` |
| [int](class_int.md#class-int) | [padding_top](class_hscrollbar.md#class-hscrollbar-theme-constant-padding-top) | `0` |

---


<a id="theme-property-descriptions"></a>

## Theme Property Descriptions

<a id="class-hscrollbar-theme-constant-padding-bottom"></a>

[int](class_int.md#class-int) **padding_bottom** = `0` [🔗](class_hscrollbar.md#class-hscrollbar-theme-constant-padding-bottom)

Padding between the bottom of the [ScrollBar.scroll](class_scrollbar.md#class-scrollbar-theme-style-scroll) element and the [ScrollBar.grabber](class_scrollbar.md#class-scrollbar-theme-style-grabber).

**Note:** To apply horizontal padding, modify the left/right content margins of [ScrollBar.scroll](class_scrollbar.md#class-scrollbar-theme-style-scroll) instead.

---


<a id="class-hscrollbar-theme-constant-padding-top"></a>

[int](class_int.md#class-int) **padding_top** = `0` [🔗](class_hscrollbar.md#class-hscrollbar-theme-constant-padding-top)

Padding between the top of the [ScrollBar.scroll](class_scrollbar.md#class-scrollbar-theme-style-scroll) element and the [ScrollBar.grabber](class_scrollbar.md#class-scrollbar-theme-style-grabber).

**Note:** To apply horizontal padding, modify the left/right content margins of [ScrollBar.scroll](class_scrollbar.md#class-scrollbar-theme-style-scroll) instead.
