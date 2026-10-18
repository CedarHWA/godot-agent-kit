> Source: https://docs.godotengine.org/en/4.7/classes/class_labelsettings.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="labelsettings"></a>

<a id="class-labelsettings"></a>

# LabelSettings

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Provides common settings to customize the text in a [Label](class_label.md#class-label).

<a id="description"></a>

## Description

**LabelSettings** is a resource that provides common settings to customize the text in a [Label](class_label.md#class-label). It will take priority over the properties defined in [Control.theme](class_control.md#class-control-property-theme). The resource can be shared between multiple labels and changed on the fly, so it's convenient and flexible way to setup text style.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Font](class_font.md#class-font) | [font](class_labelsettings.md#class-labelsettings-property-font) |  |
| [Color](class_color.md#class-color) | [font_color](class_labelsettings.md#class-labelsettings-property-font-color) | `Color(1, 1, 1, 1)` |
| [int](class_int.md#class-int) | [font_size](class_labelsettings.md#class-labelsettings-property-font-size) | `16` |
| [float](class_float.md#class-float) | [line_spacing](class_labelsettings.md#class-labelsettings-property-line-spacing) | `3.0` |
| [Color](class_color.md#class-color) | [outline_color](class_labelsettings.md#class-labelsettings-property-outline-color) | `Color(1, 1, 1, 1)` |
| [int](class_int.md#class-int) | [outline_size](class_labelsettings.md#class-labelsettings-property-outline-size) | `0` |
| [float](class_float.md#class-float) | [paragraph_spacing](class_labelsettings.md#class-labelsettings-property-paragraph-spacing) | `0.0` |
| [Color](class_color.md#class-color) | [shadow_color](class_labelsettings.md#class-labelsettings-property-shadow-color) | `Color(0, 0, 0, 0)` |
| [Vector2](class_vector2.md#class-vector2) | [shadow_offset](class_labelsettings.md#class-labelsettings-property-shadow-offset) | `Vector2(1, 1)` |
| [int](class_int.md#class-int) | [shadow_size](class_labelsettings.md#class-labelsettings-property-shadow-size) | `1` |
| [int](class_int.md#class-int) | [stacked_outline_count](class_labelsettings.md#class-labelsettings-property-stacked-outline-count) | `0` |
| [Color](class_color.md#class-color) | [stacked_outline_{index}/color](class_labelsettings.md#class-labelsettings-property-stacked-outline-index-color) | `Color(0, 0, 0, 1)` |
| [int](class_int.md#class-int) | [stacked_outline_{index}/size](class_labelsettings.md#class-labelsettings-property-stacked-outline-index-size) | `0` |
| [int](class_int.md#class-int) | [stacked_shadow_count](class_labelsettings.md#class-labelsettings-property-stacked-shadow-count) | `0` |
| [Color](class_color.md#class-color) | [stacked_shadow_{index}/color](class_labelsettings.md#class-labelsettings-property-stacked-shadow-index-color) | `Color(0, 0, 0, 1)` |
| [Vector2](class_vector2.md#class-vector2) | [stacked_shadow_{index}/offset](class_labelsettings.md#class-labelsettings-property-stacked-shadow-index-offset) | `Vector2(1, 1)` |
| [int](class_int.md#class-int) | [stacked_shadow_{index}/outline_size](class_labelsettings.md#class-labelsettings-property-stacked-shadow-index-outline-size) | `0` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_stacked_outline](class_labelsettings.md#class-labelsettings-method-add-stacked-outline)(index: [int](class_int.md#class-int) = -1) |
| void | [add_stacked_shadow](class_labelsettings.md#class-labelsettings-method-add-stacked-shadow)(index: [int](class_int.md#class-int) = -1) |
| [Color](class_color.md#class-color) | [get_stacked_outline_color](class_labelsettings.md#class-labelsettings-method-get-stacked-outline-color)(index: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_stacked_outline_size](class_labelsettings.md#class-labelsettings-method-get-stacked-outline-size)(index: [int](class_int.md#class-int)) const |
| [Color](class_color.md#class-color) | [get_stacked_shadow_color](class_labelsettings.md#class-labelsettings-method-get-stacked-shadow-color)(index: [int](class_int.md#class-int)) const |
| [Vector2](class_vector2.md#class-vector2) | [get_stacked_shadow_offset](class_labelsettings.md#class-labelsettings-method-get-stacked-shadow-offset)(index: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_stacked_shadow_outline_size](class_labelsettings.md#class-labelsettings-method-get-stacked-shadow-outline-size)(index: [int](class_int.md#class-int)) const |
| void | [move_stacked_outline](class_labelsettings.md#class-labelsettings-method-move-stacked-outline)(from_index: [int](class_int.md#class-int), to_position: [int](class_int.md#class-int)) |
| void | [move_stacked_shadow](class_labelsettings.md#class-labelsettings-method-move-stacked-shadow)(from_index: [int](class_int.md#class-int), to_position: [int](class_int.md#class-int)) |
| void | [remove_stacked_outline](class_labelsettings.md#class-labelsettings-method-remove-stacked-outline)(index: [int](class_int.md#class-int)) |
| void | [remove_stacked_shadow](class_labelsettings.md#class-labelsettings-method-remove-stacked-shadow)(index: [int](class_int.md#class-int)) |
| void | [set_stacked_outline_color](class_labelsettings.md#class-labelsettings-method-set-stacked-outline-color)(index: [int](class_int.md#class-int), color: [Color](class_color.md#class-color)) |
| void | [set_stacked_outline_size](class_labelsettings.md#class-labelsettings-method-set-stacked-outline-size)(index: [int](class_int.md#class-int), size: [int](class_int.md#class-int)) |
| void | [set_stacked_shadow_color](class_labelsettings.md#class-labelsettings-method-set-stacked-shadow-color)(index: [int](class_int.md#class-int), color: [Color](class_color.md#class-color)) |
| void | [set_stacked_shadow_offset](class_labelsettings.md#class-labelsettings-method-set-stacked-shadow-offset)(index: [int](class_int.md#class-int), offset: [Vector2](class_vector2.md#class-vector2)) |
| void | [set_stacked_shadow_outline_size](class_labelsettings.md#class-labelsettings-method-set-stacked-shadow-outline-size)(index: [int](class_int.md#class-int), size: [int](class_int.md#class-int)) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-labelsettings-property-font"></a>

[Font](class_font.md#class-font) **font** [🔗](class_labelsettings.md#class-labelsettings-property-font)

- void **set_font**(value: [Font](class_font.md#class-font))
- [Font](class_font.md#class-font) **get_font**()

[Font](class_font.md#class-font) used for the text.

---


<a id="class-labelsettings-property-font-color"></a>

[Color](class_color.md#class-color) **font_color** = `Color(1, 1, 1, 1)` [🔗](class_labelsettings.md#class-labelsettings-property-font-color)

- void **set_font_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_font_color**()

Color of the text.

---


<a id="class-labelsettings-property-font-size"></a>

[int](class_int.md#class-int) **font_size** = `16` [🔗](class_labelsettings.md#class-labelsettings-property-font-size)

- void **set_font_size**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_font_size**()

Size of the text.

---


<a id="class-labelsettings-property-line-spacing"></a>

[float](class_float.md#class-float) **line_spacing** = `3.0` [🔗](class_labelsettings.md#class-labelsettings-property-line-spacing)

- void **set_line_spacing**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_line_spacing**()

Additional vertical spacing between lines (in pixels), spacing is added to line descent. This value can be negative.

---


<a id="class-labelsettings-property-outline-color"></a>

[Color](class_color.md#class-color) **outline_color** = `Color(1, 1, 1, 1)` [🔗](class_labelsettings.md#class-labelsettings-property-outline-color)

- void **set_outline_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_outline_color**()

The color of the outline.

---


<a id="class-labelsettings-property-outline-size"></a>

[int](class_int.md#class-int) **outline_size** = `0` [🔗](class_labelsettings.md#class-labelsettings-property-outline-size)

- void **set_outline_size**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_outline_size**()

Text outline size.

---


<a id="class-labelsettings-property-paragraph-spacing"></a>

[float](class_float.md#class-float) **paragraph_spacing** = `0.0` [🔗](class_labelsettings.md#class-labelsettings-property-paragraph-spacing)

- void **set_paragraph_spacing**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_paragraph_spacing**()

Vertical space between paragraphs. Added on top of [line_spacing](class_labelsettings.md#class-labelsettings-property-line-spacing).

---


<a id="class-labelsettings-property-shadow-color"></a>

[Color](class_color.md#class-color) **shadow_color** = `Color(0, 0, 0, 0)` [🔗](class_labelsettings.md#class-labelsettings-property-shadow-color)

- void **set_shadow_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_shadow_color**()

Color of the shadow effect. If alpha is `0`, no shadow will be drawn.

---


<a id="class-labelsettings-property-shadow-offset"></a>

[Vector2](class_vector2.md#class-vector2) **shadow_offset** = `Vector2(1, 1)` [🔗](class_labelsettings.md#class-labelsettings-property-shadow-offset)

- void **set_shadow_offset**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_shadow_offset**()

Offset of the shadow effect, in pixels.

---


<a id="class-labelsettings-property-shadow-size"></a>

[int](class_int.md#class-int) **shadow_size** = `1` [🔗](class_labelsettings.md#class-labelsettings-property-shadow-size)

- void **set_shadow_size**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_shadow_size**()

Size of the shadow effect.

---


<a id="class-labelsettings-property-stacked-outline-count"></a>

[int](class_int.md#class-int) **stacked_outline_count** = `0` [🔗](class_labelsettings.md#class-labelsettings-property-stacked-outline-count)

- void **set_stacked_outline_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_stacked_outline_count**()

The number of stacked outlines.

---


<a id="class-labelsettings-property-stacked-outline-index-color"></a>

[Color](class_color.md#class-color) **stacked_outline_{index}/color** = `Color(0, 0, 0, 1)` [🔗](class_labelsettings.md#class-labelsettings-property-stacked-outline-index-color)

The color of the outline at `index`.

**Note:** `index` is a value in the `0 .. stacked_outline_count - 1` range.

---


<a id="class-labelsettings-property-stacked-outline-index-size"></a>

[int](class_int.md#class-int) **stacked_outline_{index}/size** = `0` [🔗](class_labelsettings.md#class-labelsettings-property-stacked-outline-index-size)

The size of the outline at `index`.

**Note:** `index` is a value in the `0 .. stacked_outline_count - 1` range.

---


<a id="class-labelsettings-property-stacked-shadow-count"></a>

[int](class_int.md#class-int) **stacked_shadow_count** = `0` [🔗](class_labelsettings.md#class-labelsettings-property-stacked-shadow-count)

- void **set_stacked_shadow_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_stacked_shadow_count**()

The number of stacked shadows.

---


<a id="class-labelsettings-property-stacked-shadow-index-color"></a>

[Color](class_color.md#class-color) **stacked_shadow_{index}/color** = `Color(0, 0, 0, 1)` [🔗](class_labelsettings.md#class-labelsettings-property-stacked-shadow-index-color)

The color of the shadow at `index`.

**Note:** `index` is a value in the `0 .. stacked_shadow_count - 1` range.

---


<a id="class-labelsettings-property-stacked-shadow-index-offset"></a>

[Vector2](class_vector2.md#class-vector2) **stacked_shadow_{index}/offset** = `Vector2(1, 1)` [🔗](class_labelsettings.md#class-labelsettings-property-stacked-shadow-index-offset)

The offset of the shadow at `index`.

**Note:** `index` is a value in the `0 .. stacked_shadow_count - 1` range.

---


<a id="class-labelsettings-property-stacked-shadow-index-outline-size"></a>

[int](class_int.md#class-int) **stacked_shadow_{index}/outline_size** = `0` [🔗](class_labelsettings.md#class-labelsettings-property-stacked-shadow-index-outline-size)

The size of the shadow outline at `index`.

**Note:** `index` is a value in the `0 .. stacked_shadow_count - 1` range.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-labelsettings-method-add-stacked-outline"></a>

void **add_stacked_outline**(index: [int](class_int.md#class-int) = -1) [🔗](class_labelsettings.md#class-labelsettings-method-add-stacked-outline)

Adds a new stacked outline to the label at the given `index`. If `index` is `-1`, the new stacked outline will be added at the end of the list.

---


<a id="class-labelsettings-method-add-stacked-shadow"></a>

void **add_stacked_shadow**(index: [int](class_int.md#class-int) = -1) [🔗](class_labelsettings.md#class-labelsettings-method-add-stacked-shadow)

Adds a new stacked shadow to the label at the given `index`. If `index` is `-1`, the new stacked shadow will be added at the end of the list.

---


<a id="class-labelsettings-method-get-stacked-outline-color"></a>

[Color](class_color.md#class-color) **get_stacked_outline_color**(index: [int](class_int.md#class-int)) const [🔗](class_labelsettings.md#class-labelsettings-method-get-stacked-outline-color)

Returns the color of the stacked outline at `index`.

---


<a id="class-labelsettings-method-get-stacked-outline-size"></a>

[int](class_int.md#class-int) **get_stacked_outline_size**(index: [int](class_int.md#class-int)) const [🔗](class_labelsettings.md#class-labelsettings-method-get-stacked-outline-size)

Returns the size of the stacked outline at `index`.

---


<a id="class-labelsettings-method-get-stacked-shadow-color"></a>

[Color](class_color.md#class-color) **get_stacked_shadow_color**(index: [int](class_int.md#class-int)) const [🔗](class_labelsettings.md#class-labelsettings-method-get-stacked-shadow-color)

Returns the color of the stacked shadow at `index`.

---


<a id="class-labelsettings-method-get-stacked-shadow-offset"></a>

[Vector2](class_vector2.md#class-vector2) **get_stacked_shadow_offset**(index: [int](class_int.md#class-int)) const [🔗](class_labelsettings.md#class-labelsettings-method-get-stacked-shadow-offset)

Returns the offset of the stacked shadow at `index`.

---


<a id="class-labelsettings-method-get-stacked-shadow-outline-size"></a>

[int](class_int.md#class-int) **get_stacked_shadow_outline_size**(index: [int](class_int.md#class-int)) const [🔗](class_labelsettings.md#class-labelsettings-method-get-stacked-shadow-outline-size)

Returns the outline size of the stacked shadow at `index`.

---


<a id="class-labelsettings-method-move-stacked-outline"></a>

void **move_stacked_outline**(from_index: [int](class_int.md#class-int), to_position: [int](class_int.md#class-int)) [🔗](class_labelsettings.md#class-labelsettings-method-move-stacked-outline)

Moves the stacked outline at index `from_index` to the given position `to_position` in the array.

---


<a id="class-labelsettings-method-move-stacked-shadow"></a>

void **move_stacked_shadow**(from_index: [int](class_int.md#class-int), to_position: [int](class_int.md#class-int)) [🔗](class_labelsettings.md#class-labelsettings-method-move-stacked-shadow)

Moves the stacked shadow at index `from_index` to the given position `to_position` in the array.

---


<a id="class-labelsettings-method-remove-stacked-outline"></a>

void **remove_stacked_outline**(index: [int](class_int.md#class-int)) [🔗](class_labelsettings.md#class-labelsettings-method-remove-stacked-outline)

Removes the stacked outline at index `index`.

---


<a id="class-labelsettings-method-remove-stacked-shadow"></a>

void **remove_stacked_shadow**(index: [int](class_int.md#class-int)) [🔗](class_labelsettings.md#class-labelsettings-method-remove-stacked-shadow)

Removes the stacked shadow at index `index`.

---


<a id="class-labelsettings-method-set-stacked-outline-color"></a>

void **set_stacked_outline_color**(index: [int](class_int.md#class-int), color: [Color](class_color.md#class-color)) [🔗](class_labelsettings.md#class-labelsettings-method-set-stacked-outline-color)

Sets the color of the stacked outline identified by the given `index` to `color`.

---


<a id="class-labelsettings-method-set-stacked-outline-size"></a>

void **set_stacked_outline_size**(index: [int](class_int.md#class-int), size: [int](class_int.md#class-int)) [🔗](class_labelsettings.md#class-labelsettings-method-set-stacked-outline-size)

Sets the size of the stacked outline identified by the given `index` to `size`.

---


<a id="class-labelsettings-method-set-stacked-shadow-color"></a>

void **set_stacked_shadow_color**(index: [int](class_int.md#class-int), color: [Color](class_color.md#class-color)) [🔗](class_labelsettings.md#class-labelsettings-method-set-stacked-shadow-color)

Sets the color of the stacked shadow identified by the given `index` to `color`.

---


<a id="class-labelsettings-method-set-stacked-shadow-offset"></a>

void **set_stacked_shadow_offset**(index: [int](class_int.md#class-int), offset: [Vector2](class_vector2.md#class-vector2)) [🔗](class_labelsettings.md#class-labelsettings-method-set-stacked-shadow-offset)

Sets the offset of the stacked shadow identified by the given `index` to `offset`.

---


<a id="class-labelsettings-method-set-stacked-shadow-outline-size"></a>

void **set_stacked_shadow_outline_size**(index: [int](class_int.md#class-int), size: [int](class_int.md#class-int)) [🔗](class_labelsettings.md#class-labelsettings-method-set-stacked-shadow-outline-size)

Sets the outline size of the stacked shadow identified by the given `index` to `size`.
