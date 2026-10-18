> Source: https://docs.godotengine.org/en/4.7/classes/class_referencerect.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="referencerect"></a>

<a id="class-referencerect"></a>

# ReferenceRect

**Inherits:** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A rectangular box for designing UIs.

<a id="description"></a>

## Description

A rectangular box that displays only a colored border around its rectangle (see [Control.get_rect()](class_control.md#class-control-method-get-rect)). It can be used to visualize the extents of a [Control](class_control.md#class-control) node, for testing purposes.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Color](class_color.md#class-color) | [border_color](class_referencerect.md#class-referencerect-property-border-color) | `Color(1, 0, 0, 1)` |
| [float](class_float.md#class-float) | [border_width](class_referencerect.md#class-referencerect-property-border-width) | `1.0` |
| [bool](class_bool.md#class-bool) | [editor_only](class_referencerect.md#class-referencerect-property-editor-only) | `true` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-referencerect-property-border-color"></a>

[Color](class_color.md#class-color) **border_color** = `Color(1, 0, 0, 1)` [🔗](class_referencerect.md#class-referencerect-property-border-color)

- void **set_border_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_border_color**()

Sets the border color of the **ReferenceRect**.

---


<a id="class-referencerect-property-border-width"></a>

[float](class_float.md#class-float) **border_width** = `1.0` [🔗](class_referencerect.md#class-referencerect-property-border-width)

- void **set_border_width**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_border_width**()

Sets the border width of the **ReferenceRect**. The border grows both inwards and outwards with respect to the rectangle box.

---


<a id="class-referencerect-property-editor-only"></a>

[bool](class_bool.md#class-bool) **editor_only** = `true` [🔗](class_referencerect.md#class-referencerect-property-editor-only)

- void **set_editor_only**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_editor_only**()

If `true`, the **ReferenceRect** will only be visible while in editor. Otherwise, **ReferenceRect** will be visible in the running project.
