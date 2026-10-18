> Source: https://docs.godotengine.org/en/4.7/classes/class_stylebox.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="stylebox"></a>

<a id="class-stylebox"></a>

# StyleBox

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [StyleBoxEmpty](class_styleboxempty.md#class-styleboxempty), [StyleBoxFlat](class_styleboxflat.md#class-styleboxflat), [StyleBoxLine](class_styleboxline.md#class-styleboxline), [StyleBoxTexture](class_styleboxtexture.md#class-styleboxtexture)

Abstract base class for defining stylized boxes for UI elements.

<a id="description"></a>

## Description

**StyleBox** is an abstract base class for drawing stylized boxes for UI elements. It is used for panels, buttons, [LineEdit](class_lineedit.md#class-lineedit) backgrounds, [Tree](class_tree.md#class-tree) backgrounds, etc. and also for testing a transparency mask for pointer signals. If mask test fails on a **StyleBox** assigned as mask to a control, clicks and motion signals will go through it to the one below.

**Note:** For control nodes that have *Theme Properties*, the `focus` **StyleBox** is displayed over the `normal`, `hover` or `pressed` **StyleBox**. This makes the `focus` **StyleBox** more reusable across different nodes.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [content_margin_bottom](class_stylebox.md#class-stylebox-property-content-margin-bottom) | `-1.0` |
| [float](class_float.md#class-float) | [content_margin_left](class_stylebox.md#class-stylebox-property-content-margin-left) | `-1.0` |
| [float](class_float.md#class-float) | [content_margin_right](class_stylebox.md#class-stylebox-property-content-margin-right) | `-1.0` |
| [float](class_float.md#class-float) | [content_margin_top](class_stylebox.md#class-stylebox-property-content-margin-top) | `-1.0` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [_draw](class_stylebox.md#class-stylebox-private-method-draw)(to_canvas_item: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2)) virtual required const |
| [Rect2](class_rect2.md#class-rect2) | [_get_draw_rect](class_stylebox.md#class-stylebox-private-method-get-draw-rect)(rect: [Rect2](class_rect2.md#class-rect2)) virtual const |
| [Vector2](class_vector2.md#class-vector2) | [_get_minimum_size](class_stylebox.md#class-stylebox-private-method-get-minimum-size)() virtual const |
| [bool](class_bool.md#class-bool) | [_test_mask](class_stylebox.md#class-stylebox-private-method-test-mask)(point: [Vector2](class_vector2.md#class-vector2), rect: [Rect2](class_rect2.md#class-rect2)) virtual const |
| void | [draw](class_stylebox.md#class-stylebox-method-draw)(canvas_item: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2)) const |
| [float](class_float.md#class-float) | [get_content_margin](class_stylebox.md#class-stylebox-method-get-content-margin)(margin: [Side](class_@globalscope.md#enum-globalscope-side)) const |
| [CanvasItem](class_canvasitem.md#class-canvasitem) | [get_current_item_drawn](class_stylebox.md#class-stylebox-method-get-current-item-drawn)() const |
| [float](class_float.md#class-float) | [get_margin](class_stylebox.md#class-stylebox-method-get-margin)(margin: [Side](class_@globalscope.md#enum-globalscope-side)) const |
| [Vector2](class_vector2.md#class-vector2) | [get_minimum_size](class_stylebox.md#class-stylebox-method-get-minimum-size)() const |
| [Vector2](class_vector2.md#class-vector2) | [get_offset](class_stylebox.md#class-stylebox-method-get-offset)() const |
| void | [set_content_margin](class_stylebox.md#class-stylebox-method-set-content-margin)(margin: [Side](class_@globalscope.md#enum-globalscope-side), offset: [float](class_float.md#class-float)) |
| void | [set_content_margin_all](class_stylebox.md#class-stylebox-method-set-content-margin-all)(offset: [float](class_float.md#class-float)) |
| [bool](class_bool.md#class-bool) | [test_mask](class_stylebox.md#class-stylebox-method-test-mask)(point: [Vector2](class_vector2.md#class-vector2), rect: [Rect2](class_rect2.md#class-rect2)) const |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-stylebox-property-content-margin-bottom"></a>

[float](class_float.md#class-float) **content_margin_bottom** = `-1.0` [🔗](class_stylebox.md#class-stylebox-property-content-margin-bottom)

- void **set_content_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), offset: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_content_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) const

The bottom margin for the contents of this style box. Increasing this value reduces the space available to the contents from the bottom.

If this value is negative, it is ignored and a child-specific margin is used instead. For example, for [StyleBoxFlat](class_styleboxflat.md#class-styleboxflat), the border thickness (if any) is used instead.

It is up to the code using this style box to decide what these contents are: for example, a [Button](class_button.md#class-button) respects this content margin for the textual contents of the button.

[get_margin()](class_stylebox.md#class-stylebox-method-get-margin) should be used to fetch this value as consumer instead of reading these properties directly. This is because it correctly respects negative values and the fallback mentioned above.

---


<a id="class-stylebox-property-content-margin-left"></a>

[float](class_float.md#class-float) **content_margin_left** = `-1.0` [🔗](class_stylebox.md#class-stylebox-property-content-margin-left)

- void **set_content_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), offset: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_content_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) const

The left margin for the contents of this style box. Increasing this value reduces the space available to the contents from the left.

Refer to [content_margin_bottom](class_stylebox.md#class-stylebox-property-content-margin-bottom) for extra considerations.

---


<a id="class-stylebox-property-content-margin-right"></a>

[float](class_float.md#class-float) **content_margin_right** = `-1.0` [🔗](class_stylebox.md#class-stylebox-property-content-margin-right)

- void **set_content_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), offset: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_content_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) const

The right margin for the contents of this style box. Increasing this value reduces the space available to the contents from the right.

Refer to [content_margin_bottom](class_stylebox.md#class-stylebox-property-content-margin-bottom) for extra considerations.

---


<a id="class-stylebox-property-content-margin-top"></a>

[float](class_float.md#class-float) **content_margin_top** = `-1.0` [🔗](class_stylebox.md#class-stylebox-property-content-margin-top)

- void **set_content_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), offset: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_content_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) const

The top margin for the contents of this style box. Increasing this value reduces the space available to the contents from the top.

Refer to [content_margin_bottom](class_stylebox.md#class-stylebox-property-content-margin-bottom) for extra considerations.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-stylebox-private-method-draw"></a>

void **_draw**(to_canvas_item: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2)) virtual required const [🔗](class_stylebox.md#class-stylebox-private-method-draw)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-stylebox-private-method-get-draw-rect"></a>

[Rect2](class_rect2.md#class-rect2) **_get_draw_rect**(rect: [Rect2](class_rect2.md#class-rect2)) virtual const [🔗](class_stylebox.md#class-stylebox-private-method-get-draw-rect)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-stylebox-private-method-get-minimum-size"></a>

[Vector2](class_vector2.md#class-vector2) **_get_minimum_size**() virtual const [🔗](class_stylebox.md#class-stylebox-private-method-get-minimum-size)

Virtual method to be implemented by the user. Returns a custom minimum size that the stylebox must respect when drawing. By default [get_minimum_size()](class_stylebox.md#class-stylebox-method-get-minimum-size) only takes content margins into account. This method can be overridden to add another size restriction. A combination of the default behavior and the output of this method will be used, to account for both sizes.

---


<a id="class-stylebox-private-method-test-mask"></a>

[bool](class_bool.md#class-bool) **_test_mask**(point: [Vector2](class_vector2.md#class-vector2), rect: [Rect2](class_rect2.md#class-rect2)) virtual const [🔗](class_stylebox.md#class-stylebox-private-method-test-mask)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-stylebox-method-draw"></a>

void **draw**(canvas_item: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2)) const [🔗](class_stylebox.md#class-stylebox-method-draw)

Draws this stylebox using a canvas item identified by the given [RID](class_rid.md#class-rid).

The [RID](class_rid.md#class-rid) value can either be the result of [CanvasItem.get_canvas_item()](class_canvasitem.md#class-canvasitem-method-get-canvas-item) called on an existing [CanvasItem](class_canvasitem.md#class-canvasitem)-derived node, or directly from creating a canvas item in the [RenderingServer](class_renderingserver.md#class-renderingserver) with [RenderingServer.canvas_item_create()](class_renderingserver.md#class-renderingserver-method-canvas-item-create).

---


<a id="class-stylebox-method-get-content-margin"></a>

[float](class_float.md#class-float) **get_content_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) const [🔗](class_stylebox.md#class-stylebox-method-get-content-margin)

Returns the default margin of the specified [Side](class_@globalscope.md#enum-globalscope-side).

---


<a id="class-stylebox-method-get-current-item-drawn"></a>

[CanvasItem](class_canvasitem.md#class-canvasitem) **get_current_item_drawn**() const [🔗](class_stylebox.md#class-stylebox-method-get-current-item-drawn)

Returns the [CanvasItem](class_canvasitem.md#class-canvasitem) that handles its [CanvasItem.NOTIFICATION_DRAW](class_canvasitem.md#class-canvasitem-constant-notification-draw) or [CanvasItem._draw()](class_canvasitem.md#class-canvasitem-private-method-draw) callback at this moment.

---


<a id="class-stylebox-method-get-margin"></a>

[float](class_float.md#class-float) **get_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) const [🔗](class_stylebox.md#class-stylebox-method-get-margin)

Returns the content margin offset for the specified [Side](class_@globalscope.md#enum-globalscope-side).

Positive values reduce size inwards, unlike [Control](class_control.md#class-control)'s margin values.

---


<a id="class-stylebox-method-get-minimum-size"></a>

[Vector2](class_vector2.md#class-vector2) **get_minimum_size**() const [🔗](class_stylebox.md#class-stylebox-method-get-minimum-size)

Returns the minimum size that this stylebox can be shrunk to.

---


<a id="class-stylebox-method-get-offset"></a>

[Vector2](class_vector2.md#class-vector2) **get_offset**() const [🔗](class_stylebox.md#class-stylebox-method-get-offset)

Returns the "offset" of a stylebox. This helper function returns a value equivalent to `Vector2(style.get_margin(MARGIN_LEFT), style.get_margin(MARGIN_TOP))`.

---


<a id="class-stylebox-method-set-content-margin"></a>

void **set_content_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), offset: [float](class_float.md#class-float)) [🔗](class_stylebox.md#class-stylebox-method-set-content-margin)

Sets the default value of the specified [Side](class_@globalscope.md#enum-globalscope-side) to `offset` pixels.

---


<a id="class-stylebox-method-set-content-margin-all"></a>

void **set_content_margin_all**(offset: [float](class_float.md#class-float)) [🔗](class_stylebox.md#class-stylebox-method-set-content-margin-all)

Sets the default margin to `offset` pixels for all sides.

---


<a id="class-stylebox-method-test-mask"></a>

[bool](class_bool.md#class-bool) **test_mask**(point: [Vector2](class_vector2.md#class-vector2), rect: [Rect2](class_rect2.md#class-rect2)) const [🔗](class_stylebox.md#class-stylebox-method-test-mask)

Test a position in a rectangle, return whether it passes the mask test.
