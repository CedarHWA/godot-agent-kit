> Source: https://docs.godotengine.org/en/4.7/classes/class_styleboxflat.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="styleboxflat"></a>

<a id="class-styleboxflat"></a>

# StyleBoxFlat

**Inherits:** [StyleBox](class_stylebox.md#class-stylebox) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A customizable [StyleBox](class_stylebox.md#class-stylebox) that doesn't use a texture.

<a id="description"></a>

## Description

By configuring various properties of this style box, you can achieve many common looks without the need of a texture. This includes optionally rounded borders, antialiasing, shadows, and skew.

Setting corner radius to high values is allowed. As soon as corners overlap, the stylebox will switch to a relative system:

```text
height = 30
corner_radius_top_left = 50
corner_radius_bottom_left = 100
```

The relative system now would take the 1:2 ratio of the two left corners to calculate the actual corner width. Both corners added will **never** be more than the height. Result:

```text
corner_radius_top_left: 10
corner_radius_bottom_left: 20
```

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [anti_aliasing](class_styleboxflat.md#class-styleboxflat-property-anti-aliasing) | `true` |
| [float](class_float.md#class-float) | [anti_aliasing_size](class_styleboxflat.md#class-styleboxflat-property-anti-aliasing-size) | `1.0` |
| [Color](class_color.md#class-color) | [bg_color](class_styleboxflat.md#class-styleboxflat-property-bg-color) | `Color(0.6, 0.6, 0.6, 1)` |
| [bool](class_bool.md#class-bool) | [border_blend](class_styleboxflat.md#class-styleboxflat-property-border-blend) | `false` |
| [Color](class_color.md#class-color) | [border_color](class_styleboxflat.md#class-styleboxflat-property-border-color) | `Color(0.8, 0.8, 0.8, 1)` |
| [int](class_int.md#class-int) | [border_width_bottom](class_styleboxflat.md#class-styleboxflat-property-border-width-bottom) | `0` |
| [int](class_int.md#class-int) | [border_width_left](class_styleboxflat.md#class-styleboxflat-property-border-width-left) | `0` |
| [int](class_int.md#class-int) | [border_width_right](class_styleboxflat.md#class-styleboxflat-property-border-width-right) | `0` |
| [int](class_int.md#class-int) | [border_width_top](class_styleboxflat.md#class-styleboxflat-property-border-width-top) | `0` |
| [int](class_int.md#class-int) | [corner_detail](class_styleboxflat.md#class-styleboxflat-property-corner-detail) | `8` |
| [int](class_int.md#class-int) | [corner_radius_bottom_left](class_styleboxflat.md#class-styleboxflat-property-corner-radius-bottom-left) | `0` |
| [int](class_int.md#class-int) | [corner_radius_bottom_right](class_styleboxflat.md#class-styleboxflat-property-corner-radius-bottom-right) | `0` |
| [int](class_int.md#class-int) | [corner_radius_top_left](class_styleboxflat.md#class-styleboxflat-property-corner-radius-top-left) | `0` |
| [int](class_int.md#class-int) | [corner_radius_top_right](class_styleboxflat.md#class-styleboxflat-property-corner-radius-top-right) | `0` |
| [bool](class_bool.md#class-bool) | [draw_center](class_styleboxflat.md#class-styleboxflat-property-draw-center) | `true` |
| [float](class_float.md#class-float) | [expand_margin_bottom](class_styleboxflat.md#class-styleboxflat-property-expand-margin-bottom) | `0.0` |
| [float](class_float.md#class-float) | [expand_margin_left](class_styleboxflat.md#class-styleboxflat-property-expand-margin-left) | `0.0` |
| [float](class_float.md#class-float) | [expand_margin_right](class_styleboxflat.md#class-styleboxflat-property-expand-margin-right) | `0.0` |
| [float](class_float.md#class-float) | [expand_margin_top](class_styleboxflat.md#class-styleboxflat-property-expand-margin-top) | `0.0` |
| [Color](class_color.md#class-color) | [shadow_color](class_styleboxflat.md#class-styleboxflat-property-shadow-color) | `Color(0, 0, 0, 0.6)` |
| [Vector2](class_vector2.md#class-vector2) | [shadow_offset](class_styleboxflat.md#class-styleboxflat-property-shadow-offset) | `Vector2(0, 0)` |
| [int](class_int.md#class-int) | [shadow_size](class_styleboxflat.md#class-styleboxflat-property-shadow-size) | `0` |
| [Vector2](class_vector2.md#class-vector2) | [skew](class_styleboxflat.md#class-styleboxflat-property-skew) | `Vector2(0, 0)` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [int](class_int.md#class-int) | [get_border_width](class_styleboxflat.md#class-styleboxflat-method-get-border-width)(margin: [Side](class_@globalscope.md#enum-globalscope-side)) const |
| [int](class_int.md#class-int) | [get_border_width_min](class_styleboxflat.md#class-styleboxflat-method-get-border-width-min)() const |
| [int](class_int.md#class-int) | [get_corner_radius](class_styleboxflat.md#class-styleboxflat-method-get-corner-radius)(corner: [Corner](class_@globalscope.md#enum-globalscope-corner)) const |
| [float](class_float.md#class-float) | [get_expand_margin](class_styleboxflat.md#class-styleboxflat-method-get-expand-margin)(margin: [Side](class_@globalscope.md#enum-globalscope-side)) const |
| void | [set_border_width](class_styleboxflat.md#class-styleboxflat-method-set-border-width)(margin: [Side](class_@globalscope.md#enum-globalscope-side), width: [int](class_int.md#class-int)) |
| void | [set_border_width_all](class_styleboxflat.md#class-styleboxflat-method-set-border-width-all)(width: [int](class_int.md#class-int)) |
| void | [set_corner_radius](class_styleboxflat.md#class-styleboxflat-method-set-corner-radius)(corner: [Corner](class_@globalscope.md#enum-globalscope-corner), radius: [int](class_int.md#class-int)) |
| void | [set_corner_radius_all](class_styleboxflat.md#class-styleboxflat-method-set-corner-radius-all)(radius: [int](class_int.md#class-int)) |
| void | [set_expand_margin](class_styleboxflat.md#class-styleboxflat-method-set-expand-margin)(margin: [Side](class_@globalscope.md#enum-globalscope-side), size: [float](class_float.md#class-float)) |
| void | [set_expand_margin_all](class_styleboxflat.md#class-styleboxflat-method-set-expand-margin-all)(size: [float](class_float.md#class-float)) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-styleboxflat-property-anti-aliasing"></a>

[bool](class_bool.md#class-bool) **anti_aliasing** = `true` [🔗](class_styleboxflat.md#class-styleboxflat-property-anti-aliasing)

- void **set_anti_aliased**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_anti_aliased**()

Antialiasing draws a small ring around the edges, which fades to transparency. As a result, edges look much smoother. This is only noticeable when using rounded corners or [skew](class_styleboxflat.md#class-styleboxflat-property-skew).

**Note:** When using beveled corners with 45-degree angles ([corner_detail](class_styleboxflat.md#class-styleboxflat-property-corner-detail) = 1), it is recommended to set [anti_aliasing](class_styleboxflat.md#class-styleboxflat-property-anti-aliasing) to `false` to ensure crisp visuals and avoid possible visual glitches.

---


<a id="class-styleboxflat-property-anti-aliasing-size"></a>

[float](class_float.md#class-float) **anti_aliasing_size** = `1.0` [🔗](class_styleboxflat.md#class-styleboxflat-property-anti-aliasing-size)

- void **set_aa_size**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_aa_size**()

This changes the size of the antialiasing effect. `1.0` is recommended for an optimal result at 100% scale, identical to how rounded rectangles are rendered in web browsers and most vector drawing software.

**Note:** Higher values may produce a blur effect but can also create undesired artifacts on small boxes with large-radius corners.

---


<a id="class-styleboxflat-property-bg-color"></a>

[Color](class_color.md#class-color) **bg_color** = `Color(0.6, 0.6, 0.6, 1)` [🔗](class_styleboxflat.md#class-styleboxflat-property-bg-color)

- void **set_bg_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_bg_color**()

The background color of the stylebox.

---


<a id="class-styleboxflat-property-border-blend"></a>

[bool](class_bool.md#class-bool) **border_blend** = `false` [🔗](class_styleboxflat.md#class-styleboxflat-property-border-blend)

- void **set_border_blend**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_border_blend**()

If `true`, the border will fade into the background color.

---


<a id="class-styleboxflat-property-border-color"></a>

[Color](class_color.md#class-color) **border_color** = `Color(0.8, 0.8, 0.8, 1)` [🔗](class_styleboxflat.md#class-styleboxflat-property-border-color)

- void **set_border_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_border_color**()

Sets the color of the border.

---


<a id="class-styleboxflat-property-border-width-bottom"></a>

[int](class_int.md#class-int) **border_width_bottom** = `0` [🔗](class_styleboxflat.md#class-styleboxflat-property-border-width-bottom)

- void **set_border_width**(margin: [Side](class_@globalscope.md#enum-globalscope-side), width: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_border_width**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) const

Border width for the bottom border.

---


<a id="class-styleboxflat-property-border-width-left"></a>

[int](class_int.md#class-int) **border_width_left** = `0` [🔗](class_styleboxflat.md#class-styleboxflat-property-border-width-left)

- void **set_border_width**(margin: [Side](class_@globalscope.md#enum-globalscope-side), width: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_border_width**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) const

Border width for the left border.

---


<a id="class-styleboxflat-property-border-width-right"></a>

[int](class_int.md#class-int) **border_width_right** = `0` [🔗](class_styleboxflat.md#class-styleboxflat-property-border-width-right)

- void **set_border_width**(margin: [Side](class_@globalscope.md#enum-globalscope-side), width: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_border_width**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) const

Border width for the right border.

---


<a id="class-styleboxflat-property-border-width-top"></a>

[int](class_int.md#class-int) **border_width_top** = `0` [🔗](class_styleboxflat.md#class-styleboxflat-property-border-width-top)

- void **set_border_width**(margin: [Side](class_@globalscope.md#enum-globalscope-side), width: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_border_width**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) const

Border width for the top border.

---


<a id="class-styleboxflat-property-corner-detail"></a>

[int](class_int.md#class-int) **corner_detail** = `8` [🔗](class_styleboxflat.md#class-styleboxflat-property-corner-detail)

- void **set_corner_detail**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_corner_detail**()

This sets the number of vertices used for each corner. Higher values result in rounder corners but take more processing power to compute. When choosing a value, you should take the corner radius ([set_corner_radius_all()](class_styleboxflat.md#class-styleboxflat-method-set-corner-radius-all)) into account.

For corner radii less than 10, `4` or `5` should be enough. For corner radii less than 30, values between `8` and `12` should be enough.

A corner detail of `1` will result in chamfered corners instead of rounded corners, which is useful for some artistic effects.

---


<a id="class-styleboxflat-property-corner-radius-bottom-left"></a>

[int](class_int.md#class-int) **corner_radius_bottom_left** = `0` [🔗](class_styleboxflat.md#class-styleboxflat-property-corner-radius-bottom-left)

- void **set_corner_radius**(corner: [Corner](class_@globalscope.md#enum-globalscope-corner), radius: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_corner_radius**(corner: [Corner](class_@globalscope.md#enum-globalscope-corner)) const

The bottom-left corner's radius. If `0`, the corner is not rounded.

---


<a id="class-styleboxflat-property-corner-radius-bottom-right"></a>

[int](class_int.md#class-int) **corner_radius_bottom_right** = `0` [🔗](class_styleboxflat.md#class-styleboxflat-property-corner-radius-bottom-right)

- void **set_corner_radius**(corner: [Corner](class_@globalscope.md#enum-globalscope-corner), radius: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_corner_radius**(corner: [Corner](class_@globalscope.md#enum-globalscope-corner)) const

The bottom-right corner's radius. If `0`, the corner is not rounded.

---


<a id="class-styleboxflat-property-corner-radius-top-left"></a>

[int](class_int.md#class-int) **corner_radius_top_left** = `0` [🔗](class_styleboxflat.md#class-styleboxflat-property-corner-radius-top-left)

- void **set_corner_radius**(corner: [Corner](class_@globalscope.md#enum-globalscope-corner), radius: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_corner_radius**(corner: [Corner](class_@globalscope.md#enum-globalscope-corner)) const

The top-left corner's radius. If `0`, the corner is not rounded.

---


<a id="class-styleboxflat-property-corner-radius-top-right"></a>

[int](class_int.md#class-int) **corner_radius_top_right** = `0` [🔗](class_styleboxflat.md#class-styleboxflat-property-corner-radius-top-right)

- void **set_corner_radius**(corner: [Corner](class_@globalscope.md#enum-globalscope-corner), radius: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_corner_radius**(corner: [Corner](class_@globalscope.md#enum-globalscope-corner)) const

The top-right corner's radius. If `0`, the corner is not rounded.

---


<a id="class-styleboxflat-property-draw-center"></a>

[bool](class_bool.md#class-bool) **draw_center** = `true` [🔗](class_styleboxflat.md#class-styleboxflat-property-draw-center)

- void **set_draw_center**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_draw_center_enabled**()

Toggles drawing of the inner part of the stylebox.

---


<a id="class-styleboxflat-property-expand-margin-bottom"></a>

[float](class_float.md#class-float) **expand_margin_bottom** = `0.0` [🔗](class_styleboxflat.md#class-styleboxflat-property-expand-margin-bottom)

- void **set_expand_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), size: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_expand_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) const

Expands the stylebox outside of the control rect on the bottom edge. Useful in combination with [border_width_bottom](class_styleboxflat.md#class-styleboxflat-property-border-width-bottom) to draw a border outside the control rect.

**Note:** Unlike [StyleBox.content_margin_bottom](class_stylebox.md#class-stylebox-property-content-margin-bottom), [expand_margin_bottom](class_styleboxflat.md#class-styleboxflat-property-expand-margin-bottom) does *not* affect the size of the clickable area for [Control](class_control.md#class-control)s. This can negatively impact usability if used wrong, as the user may try to click an area of the StyleBox that cannot actually receive clicks.

---


<a id="class-styleboxflat-property-expand-margin-left"></a>

[float](class_float.md#class-float) **expand_margin_left** = `0.0` [🔗](class_styleboxflat.md#class-styleboxflat-property-expand-margin-left)

- void **set_expand_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), size: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_expand_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) const

Expands the stylebox outside of the control rect on the left edge. Useful in combination with [border_width_left](class_styleboxflat.md#class-styleboxflat-property-border-width-left) to draw a border outside the control rect.

**Note:** Unlike [StyleBox.content_margin_left](class_stylebox.md#class-stylebox-property-content-margin-left), [expand_margin_left](class_styleboxflat.md#class-styleboxflat-property-expand-margin-left) does *not* affect the size of the clickable area for [Control](class_control.md#class-control)s. This can negatively impact usability if used wrong, as the user may try to click an area of the StyleBox that cannot actually receive clicks.

---


<a id="class-styleboxflat-property-expand-margin-right"></a>

[float](class_float.md#class-float) **expand_margin_right** = `0.0` [🔗](class_styleboxflat.md#class-styleboxflat-property-expand-margin-right)

- void **set_expand_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), size: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_expand_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) const

Expands the stylebox outside of the control rect on the right edge. Useful in combination with [border_width_right](class_styleboxflat.md#class-styleboxflat-property-border-width-right) to draw a border outside the control rect.

**Note:** Unlike [StyleBox.content_margin_right](class_stylebox.md#class-stylebox-property-content-margin-right), [expand_margin_right](class_styleboxflat.md#class-styleboxflat-property-expand-margin-right) does *not* affect the size of the clickable area for [Control](class_control.md#class-control)s. This can negatively impact usability if used wrong, as the user may try to click an area of the StyleBox that cannot actually receive clicks.

---


<a id="class-styleboxflat-property-expand-margin-top"></a>

[float](class_float.md#class-float) **expand_margin_top** = `0.0` [🔗](class_styleboxflat.md#class-styleboxflat-property-expand-margin-top)

- void **set_expand_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), size: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_expand_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) const

Expands the stylebox outside of the control rect on the top edge. Useful in combination with [border_width_top](class_styleboxflat.md#class-styleboxflat-property-border-width-top) to draw a border outside the control rect.

**Note:** Unlike [StyleBox.content_margin_top](class_stylebox.md#class-stylebox-property-content-margin-top), [expand_margin_top](class_styleboxflat.md#class-styleboxflat-property-expand-margin-top) does *not* affect the size of the clickable area for [Control](class_control.md#class-control)s. This can negatively impact usability if used wrong, as the user may try to click an area of the StyleBox that cannot actually receive clicks.

---


<a id="class-styleboxflat-property-shadow-color"></a>

[Color](class_color.md#class-color) **shadow_color** = `Color(0, 0, 0, 0.6)` [🔗](class_styleboxflat.md#class-styleboxflat-property-shadow-color)

- void **set_shadow_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_shadow_color**()

The color of the shadow. This has no effect if [shadow_size](class_styleboxflat.md#class-styleboxflat-property-shadow-size) is lower than 1.

---


<a id="class-styleboxflat-property-shadow-offset"></a>

[Vector2](class_vector2.md#class-vector2) **shadow_offset** = `Vector2(0, 0)` [🔗](class_styleboxflat.md#class-styleboxflat-property-shadow-offset)

- void **set_shadow_offset**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_shadow_offset**()

The shadow offset in pixels. Adjusts the position of the shadow relatively to the stylebox.

---


<a id="class-styleboxflat-property-shadow-size"></a>

[int](class_int.md#class-int) **shadow_size** = `0` [🔗](class_styleboxflat.md#class-styleboxflat-property-shadow-size)

- void **set_shadow_size**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_shadow_size**()

The shadow size in pixels.

---


<a id="class-styleboxflat-property-skew"></a>

[Vector2](class_vector2.md#class-vector2) **skew** = `Vector2(0, 0)` [🔗](class_styleboxflat.md#class-styleboxflat-property-skew)

- void **set_skew**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_skew**()

If set to a non-zero value on either axis, [skew](class_styleboxflat.md#class-styleboxflat-property-skew) distorts the StyleBox horizontally and/or vertically. This can be used for "futuristic"-style UIs. Positive values skew the StyleBox towards the right (X axis) and upwards (Y axis), while negative values skew the StyleBox towards the left (X axis) and downwards (Y axis).

**Note:** To ensure text does not touch the StyleBox's edges, consider increasing the [StyleBox](class_stylebox.md#class-stylebox)'s content margin (see [StyleBox.content_margin_bottom](class_stylebox.md#class-stylebox-property-content-margin-bottom)). It is preferable to increase the content margin instead of the expand margin (see [expand_margin_bottom](class_styleboxflat.md#class-styleboxflat-property-expand-margin-bottom)), as increasing the expand margin does not increase the size of the clickable area for [Control](class_control.md#class-control)s.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-styleboxflat-method-get-border-width"></a>

[int](class_int.md#class-int) **get_border_width**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) const [🔗](class_styleboxflat.md#class-styleboxflat-method-get-border-width)

Returns the specified [Side](class_@globalscope.md#enum-globalscope-side)'s border width.

---


<a id="class-styleboxflat-method-get-border-width-min"></a>

[int](class_int.md#class-int) **get_border_width_min**() const [🔗](class_styleboxflat.md#class-styleboxflat-method-get-border-width-min)

Returns the smallest border width out of all four borders.

---


<a id="class-styleboxflat-method-get-corner-radius"></a>

[int](class_int.md#class-int) **get_corner_radius**(corner: [Corner](class_@globalscope.md#enum-globalscope-corner)) const [🔗](class_styleboxflat.md#class-styleboxflat-method-get-corner-radius)

Returns the given `corner`'s radius.

---


<a id="class-styleboxflat-method-get-expand-margin"></a>

[float](class_float.md#class-float) **get_expand_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) const [🔗](class_styleboxflat.md#class-styleboxflat-method-get-expand-margin)

Returns the size of the specified [Side](class_@globalscope.md#enum-globalscope-side)'s expand margin.

---


<a id="class-styleboxflat-method-set-border-width"></a>

void **set_border_width**(margin: [Side](class_@globalscope.md#enum-globalscope-side), width: [int](class_int.md#class-int)) [🔗](class_styleboxflat.md#class-styleboxflat-method-set-border-width)

Sets the specified [Side](class_@globalscope.md#enum-globalscope-side)'s border width to `width` pixels.

---


<a id="class-styleboxflat-method-set-border-width-all"></a>

void **set_border_width_all**(width: [int](class_int.md#class-int)) [🔗](class_styleboxflat.md#class-styleboxflat-method-set-border-width-all)

Sets the border width to `width` pixels for all sides.

---


<a id="class-styleboxflat-method-set-corner-radius"></a>

void **set_corner_radius**(corner: [Corner](class_@globalscope.md#enum-globalscope-corner), radius: [int](class_int.md#class-int)) [🔗](class_styleboxflat.md#class-styleboxflat-method-set-corner-radius)

Sets the corner radius to `radius` pixels for the given `corner`.

---


<a id="class-styleboxflat-method-set-corner-radius-all"></a>

void **set_corner_radius_all**(radius: [int](class_int.md#class-int)) [🔗](class_styleboxflat.md#class-styleboxflat-method-set-corner-radius-all)

Sets the corner radius to `radius` pixels for all corners.

---


<a id="class-styleboxflat-method-set-expand-margin"></a>

void **set_expand_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), size: [float](class_float.md#class-float)) [🔗](class_styleboxflat.md#class-styleboxflat-method-set-expand-margin)

Sets the expand margin to `size` pixels for the specified [Side](class_@globalscope.md#enum-globalscope-side).

---


<a id="class-styleboxflat-method-set-expand-margin-all"></a>

void **set_expand_margin_all**(size: [float](class_float.md#class-float)) [🔗](class_styleboxflat.md#class-styleboxflat-method-set-expand-margin-all)

Sets the expand margin to `size` pixels for all sides.
