> Source: https://docs.godotengine.org/en/4.7/classes/class_bitmap.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="bitmap"></a>

<a id="class-bitmap"></a>

# BitMap

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Boolean matrix.

<a id="description"></a>

## Description

A two-dimensional array of boolean values, can be used to efficiently store a binary matrix (every matrix element takes only one bit) and query the values using natural cartesian coordinates.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Image](class_image.md#class-image) | [convert_to_image](class_bitmap.md#class-bitmap-method-convert-to-image)() const |
| void | [create](class_bitmap.md#class-bitmap-method-create)(size: [Vector2i](class_vector2i.md#class-vector2i)) |
| void | [create_from_image_alpha](class_bitmap.md#class-bitmap-method-create-from-image-alpha)(image: [Image](class_image.md#class-image), threshold: [float](class_float.md#class-float) = 0.1) |
| [bool](class_bool.md#class-bool) | [get_bit](class_bitmap.md#class-bitmap-method-get-bit)(x: [int](class_int.md#class-int), y: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [get_bitv](class_bitmap.md#class-bitmap-method-get-bitv)(position: [Vector2i](class_vector2i.md#class-vector2i)) const |
| [Vector2i](class_vector2i.md#class-vector2i) | [get_size](class_bitmap.md#class-bitmap-method-get-size)() const |
| [int](class_int.md#class-int) | [get_true_bit_count](class_bitmap.md#class-bitmap-method-get-true-bit-count)() const |
| void | [grow_mask](class_bitmap.md#class-bitmap-method-grow-mask)(pixels: [int](class_int.md#class-int), rect: [Rect2i](class_rect2i.md#class-rect2i)) |
| [Array](class_array.md#class-array)[[PackedVector2Array](class_packedvector2array.md#class-packedvector2array)] | [opaque_to_polygons](class_bitmap.md#class-bitmap-method-opaque-to-polygons)(rect: [Rect2i](class_rect2i.md#class-rect2i), epsilon: [float](class_float.md#class-float) = 2.0) const |
| void | [resize](class_bitmap.md#class-bitmap-method-resize)(new_size: [Vector2i](class_vector2i.md#class-vector2i)) |
| void | [set_bit](class_bitmap.md#class-bitmap-method-set-bit)(x: [int](class_int.md#class-int), y: [int](class_int.md#class-int), bit: [bool](class_bool.md#class-bool)) |
| void | [set_bit_rect](class_bitmap.md#class-bitmap-method-set-bit-rect)(rect: [Rect2i](class_rect2i.md#class-rect2i), bit: [bool](class_bool.md#class-bool)) |
| void | [set_bitv](class_bitmap.md#class-bitmap-method-set-bitv)(position: [Vector2i](class_vector2i.md#class-vector2i), bit: [bool](class_bool.md#class-bool)) |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-bitmap-method-convert-to-image"></a>

[Image](class_image.md#class-image) **convert_to_image**() const [🔗](class_bitmap.md#class-bitmap-method-convert-to-image)

Returns an image of the same size as the bitmap and with an [Format](class_image.md#enum-image-format) of type [Image.FORMAT_L8](class_image.md#class-image-constant-format-l8). `true` bits of the bitmap are being converted into white pixels, and `false` bits into black.

---


<a id="class-bitmap-method-create"></a>

void **create**(size: [Vector2i](class_vector2i.md#class-vector2i)) [🔗](class_bitmap.md#class-bitmap-method-create)

Creates a bitmap with the specified size, filled with `false`.

---


<a id="class-bitmap-method-create-from-image-alpha"></a>

void **create_from_image_alpha**(image: [Image](class_image.md#class-image), threshold: [float](class_float.md#class-float) = 0.1) [🔗](class_bitmap.md#class-bitmap-method-create-from-image-alpha)

Creates a bitmap that matches the given image dimensions, every element of the bitmap is set to `false` if the alpha value of the image at that position is equal to `threshold` or less, and `true` in other case.

---


<a id="class-bitmap-method-get-bit"></a>

[bool](class_bool.md#class-bool) **get_bit**(x: [int](class_int.md#class-int), y: [int](class_int.md#class-int)) const [🔗](class_bitmap.md#class-bitmap-method-get-bit)

Returns bitmap's value at the specified position.

---


<a id="class-bitmap-method-get-bitv"></a>

[bool](class_bool.md#class-bool) **get_bitv**(position: [Vector2i](class_vector2i.md#class-vector2i)) const [🔗](class_bitmap.md#class-bitmap-method-get-bitv)

Returns bitmap's value at the specified position.

---


<a id="class-bitmap-method-get-size"></a>

[Vector2i](class_vector2i.md#class-vector2i) **get_size**() const [🔗](class_bitmap.md#class-bitmap-method-get-size)

Returns bitmap's dimensions.

---


<a id="class-bitmap-method-get-true-bit-count"></a>

[int](class_int.md#class-int) **get_true_bit_count**() const [🔗](class_bitmap.md#class-bitmap-method-get-true-bit-count)

Returns the number of bitmap elements that are set to `true`.

---


<a id="class-bitmap-method-grow-mask"></a>

void **grow_mask**(pixels: [int](class_int.md#class-int), rect: [Rect2i](class_rect2i.md#class-rect2i)) [🔗](class_bitmap.md#class-bitmap-method-grow-mask)

Applies morphological dilation or erosion to the bitmap. If `pixels` is positive, dilation is applied to the bitmap. If `pixels` is negative, erosion is applied to the bitmap. `rect` defines the area where the morphological operation is applied. Pixels located outside the `rect` are unaffected by [grow_mask()](class_bitmap.md#class-bitmap-method-grow-mask).

---


<a id="class-bitmap-method-opaque-to-polygons"></a>

[Array](class_array.md#class-array)[[PackedVector2Array](class_packedvector2array.md#class-packedvector2array)] **opaque_to_polygons**(rect: [Rect2i](class_rect2i.md#class-rect2i), epsilon: [float](class_float.md#class-float) = 2.0) const [🔗](class_bitmap.md#class-bitmap-method-opaque-to-polygons)

Creates an [Array](class_array.md#class-array) of polygons covering a rectangular portion of the bitmap. It uses a marching squares algorithm, followed by Ramer-Douglas-Peucker (RDP) reduction of the number of vertices. Each polygon is described as a [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) of its vertices.

To get polygons covering the whole bitmap, pass:

```gdscript
Rect2(Vector2(), get_size())
```

`epsilon` is passed to RDP to control how accurately the polygons cover the bitmap: a lower `epsilon` corresponds to more points in the polygons.

---


<a id="class-bitmap-method-resize"></a>

void **resize**(new_size: [Vector2i](class_vector2i.md#class-vector2i)) [🔗](class_bitmap.md#class-bitmap-method-resize)

Resizes the image to `new_size`.

---


<a id="class-bitmap-method-set-bit"></a>

void **set_bit**(x: [int](class_int.md#class-int), y: [int](class_int.md#class-int), bit: [bool](class_bool.md#class-bool)) [🔗](class_bitmap.md#class-bitmap-method-set-bit)

Sets the bitmap's element at the specified position, to the specified value.

---


<a id="class-bitmap-method-set-bit-rect"></a>

void **set_bit_rect**(rect: [Rect2i](class_rect2i.md#class-rect2i), bit: [bool](class_bool.md#class-bool)) [🔗](class_bitmap.md#class-bitmap-method-set-bit-rect)

Sets a rectangular portion of the bitmap to the specified value.

---


<a id="class-bitmap-method-set-bitv"></a>

void **set_bitv**(position: [Vector2i](class_vector2i.md#class-vector2i), bit: [bool](class_bool.md#class-bool)) [🔗](class_bitmap.md#class-bitmap-method-set-bitv)

Sets the bitmap's element at the specified position, to the specified value.
