> Source: https://docs.godotengine.org/en/4.7/classes/class_gradient.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="gradient"></a>

<a id="class-gradient"></a>

# Gradient

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A color transition.

<a id="description"></a>

## Description

This resource describes a color transition by defining a set of colored points and how to interpolate between them.

See also [Curve](class_curve.md#class-curve) which supports more complex easing methods, but does not support colors.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) | [colors](class_gradient.md#class-gradient-property-colors) | `PackedColorArray(0, 0, 0, 1, 1, 1, 1, 1)` |
| [ColorSpace](class_gradient.md#enum-gradient-colorspace) | [interpolation_color_space](class_gradient.md#class-gradient-property-interpolation-color-space) | `0` |
| [InterpolationMode](class_gradient.md#enum-gradient-interpolationmode) | [interpolation_mode](class_gradient.md#class-gradient-property-interpolation-mode) | `0` |
| [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) | [offsets](class_gradient.md#class-gradient-property-offsets) | `PackedFloat32Array(0, 1)` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_point](class_gradient.md#class-gradient-method-add-point)(offset: [float](class_float.md#class-float), color: [Color](class_color.md#class-color)) |
| [Color](class_color.md#class-color) | [get_color](class_gradient.md#class-gradient-method-get-color)(point: [int](class_int.md#class-int)) |
| [float](class_float.md#class-float) | [get_offset](class_gradient.md#class-gradient-method-get-offset)(point: [int](class_int.md#class-int)) |
| [int](class_int.md#class-int) | [get_point_count](class_gradient.md#class-gradient-method-get-point-count)() const |
| void | [remove_point](class_gradient.md#class-gradient-method-remove-point)(point: [int](class_int.md#class-int)) |
| void | [reverse](class_gradient.md#class-gradient-method-reverse)() |
| [Color](class_color.md#class-color) | [sample](class_gradient.md#class-gradient-method-sample)(offset: [float](class_float.md#class-float)) |
| void | [set_color](class_gradient.md#class-gradient-method-set-color)(point: [int](class_int.md#class-int), color: [Color](class_color.md#class-color)) |
| void | [set_offset](class_gradient.md#class-gradient-method-set-offset)(point: [int](class_int.md#class-int), offset: [float](class_float.md#class-float)) |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-gradient-interpolationmode"></a>

enum **InterpolationMode**: [🔗](class_gradient.md#enum-gradient-interpolationmode)

<a id="class-gradient-constant-gradient-interpolate-linear"></a>

[InterpolationMode](class_gradient.md#enum-gradient-interpolationmode) **GRADIENT_INTERPOLATE_LINEAR** = `0`

Linear interpolation.

<a id="class-gradient-constant-gradient-interpolate-constant"></a>

[InterpolationMode](class_gradient.md#enum-gradient-interpolationmode) **GRADIENT_INTERPOLATE_CONSTANT** = `1`

Constant interpolation, color changes abruptly at each point and stays uniform between. This might cause visible aliasing when used for a gradient texture in some cases.

<a id="class-gradient-constant-gradient-interpolate-cubic"></a>

[InterpolationMode](class_gradient.md#enum-gradient-interpolationmode) **GRADIENT_INTERPOLATE_CUBIC** = `2`

Cubic interpolation.

---


<a id="enum-gradient-colorspace"></a>

enum **ColorSpace**: [🔗](class_gradient.md#enum-gradient-colorspace)

<a id="class-gradient-constant-gradient-color-space-srgb"></a>

[ColorSpace](class_gradient.md#enum-gradient-colorspace) **GRADIENT_COLOR_SPACE_SRGB** = `0`

sRGB color space.

<a id="class-gradient-constant-gradient-color-space-linear-srgb"></a>

[ColorSpace](class_gradient.md#enum-gradient-colorspace) **GRADIENT_COLOR_SPACE_LINEAR_SRGB** = `1`

Linear sRGB color space.

<a id="class-gradient-constant-gradient-color-space-oklab"></a>

[ColorSpace](class_gradient.md#enum-gradient-colorspace) **GRADIENT_COLOR_SPACE_OKLAB** = `2`

[Oklab](https://bottosson.github.io/posts/oklab/) color space. This color space provides a smooth and uniform-looking transition between colors.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-gradient-property-colors"></a>

[PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) **colors** = `PackedColorArray(0, 0, 0, 1, 1, 1, 1, 1)` [🔗](class_gradient.md#class-gradient-property-colors)

- void **set_colors**(value: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray))
- [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) **get_colors**()

Gradient's colors as a [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray).

**Note:** Setting this property updates all colors at once. To update any color individually use [set_color()](class_gradient.md#class-gradient-method-set-color).

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) for more details.

---


<a id="class-gradient-property-interpolation-color-space"></a>

[ColorSpace](class_gradient.md#enum-gradient-colorspace) **interpolation_color_space** = `0` [🔗](class_gradient.md#class-gradient-property-interpolation-color-space)

- void **set_interpolation_color_space**(value: [ColorSpace](class_gradient.md#enum-gradient-colorspace))
- [ColorSpace](class_gradient.md#enum-gradient-colorspace) **get_interpolation_color_space**()

The color space used to interpolate between points of the gradient. It does not affect the returned colors, which will always use nonlinear sRGB encoding.

**Note:** This setting has no effect when [interpolation_mode](class_gradient.md#class-gradient-property-interpolation-mode) is set to [GRADIENT_INTERPOLATE_CONSTANT](class_gradient.md#class-gradient-constant-gradient-interpolate-constant).

---


<a id="class-gradient-property-interpolation-mode"></a>

[InterpolationMode](class_gradient.md#enum-gradient-interpolationmode) **interpolation_mode** = `0` [🔗](class_gradient.md#class-gradient-property-interpolation-mode)

- void **set_interpolation_mode**(value: [InterpolationMode](class_gradient.md#enum-gradient-interpolationmode))
- [InterpolationMode](class_gradient.md#enum-gradient-interpolationmode) **get_interpolation_mode**()

The algorithm used to interpolate between points of the gradient.

---


<a id="class-gradient-property-offsets"></a>

[PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) **offsets** = `PackedFloat32Array(0, 1)` [🔗](class_gradient.md#class-gradient-property-offsets)

- void **set_offsets**(value: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array))
- [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) **get_offsets**()

Gradient's offsets as a [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array).

**Note:** Setting this property updates all offsets at once. To update any offset individually use [set_offset()](class_gradient.md#class-gradient-method-set-offset).

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) for more details.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-gradient-method-add-point"></a>

void **add_point**(offset: [float](class_float.md#class-float), color: [Color](class_color.md#class-color)) [🔗](class_gradient.md#class-gradient-method-add-point)

Adds the specified color to the gradient, with the specified offset.

---


<a id="class-gradient-method-get-color"></a>

[Color](class_color.md#class-color) **get_color**(point: [int](class_int.md#class-int)) [🔗](class_gradient.md#class-gradient-method-get-color)

Returns the color of the gradient color at index `point`.

---


<a id="class-gradient-method-get-offset"></a>

[float](class_float.md#class-float) **get_offset**(point: [int](class_int.md#class-int)) [🔗](class_gradient.md#class-gradient-method-get-offset)

Returns the offset of the gradient color at index `point`.

---


<a id="class-gradient-method-get-point-count"></a>

[int](class_int.md#class-int) **get_point_count**() const [🔗](class_gradient.md#class-gradient-method-get-point-count)

Returns the number of colors in the gradient.

---


<a id="class-gradient-method-remove-point"></a>

void **remove_point**(point: [int](class_int.md#class-int)) [🔗](class_gradient.md#class-gradient-method-remove-point)

Removes the color at index `point`.

---


<a id="class-gradient-method-reverse"></a>

void **reverse**() [🔗](class_gradient.md#class-gradient-method-reverse)

Reverses/mirrors the gradient.

**Note:** This method mirrors all points around the middle of the gradient, which may produce unexpected results when [interpolation_mode](class_gradient.md#class-gradient-property-interpolation-mode) is set to [GRADIENT_INTERPOLATE_CONSTANT](class_gradient.md#class-gradient-constant-gradient-interpolate-constant).

---


<a id="class-gradient-method-sample"></a>

[Color](class_color.md#class-color) **sample**(offset: [float](class_float.md#class-float)) [🔗](class_gradient.md#class-gradient-method-sample)

Returns the interpolated color specified by `offset`. `offset` should be between `0.0` and `1.0` (inclusive). Using a value lower than `0.0` will return the same color as `0.0`, and using a value higher than `1.0` will return the same color as `1.0`. If your input value is not within this range, consider using [@GlobalScope.remap()](class_@globalscope.md#class-globalscope-method-remap) on the input value with output values set to `0.0` and `1.0`.

---


<a id="class-gradient-method-set-color"></a>

void **set_color**(point: [int](class_int.md#class-int), color: [Color](class_color.md#class-color)) [🔗](class_gradient.md#class-gradient-method-set-color)

Sets the color of the gradient color at index `point`.

---


<a id="class-gradient-method-set-offset"></a>

void **set_offset**(point: [int](class_int.md#class-int), offset: [float](class_float.md#class-float)) [🔗](class_gradient.md#class-gradient-method-set-offset)

Sets the offset for the gradient color at index `point`.
