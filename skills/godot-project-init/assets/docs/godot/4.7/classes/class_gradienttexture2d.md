> Source: https://docs.godotengine.org/en/4.7/classes/class_gradienttexture2d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="gradienttexture2d"></a>

<a id="class-gradienttexture2d"></a>

# GradientTexture2D

**Inherits:** [Texture2D](class_texture2d.md#class-texture2d) **<** [Texture](class_texture.md#class-texture) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A 2D texture that creates a pattern with colors obtained from a [Gradient](class_gradient.md#class-gradient).

<a id="description"></a>

## Description

A 2D texture that obtains colors from a [Gradient](class_gradient.md#class-gradient) to fill the texture data. This texture is able to transform a color transition into different patterns such as a linear or a radial gradient. The texture is filled by interpolating colors starting from [fill_from](class_gradienttexture2d.md#class-gradienttexture2d-property-fill-from) to [fill_to](class_gradienttexture2d.md#class-gradienttexture2d-property-fill-to) offsets by default, but the gradient fill can be repeated to cover the entire texture.

The gradient is sampled individually for each pixel so it does not necessarily represent an exact copy of the gradient (see [width](class_gradienttexture2d.md#class-gradienttexture2d-property-width) and [height](class_gradienttexture2d.md#class-gradienttexture2d-property-height)). See also [GradientTexture1D](class_gradienttexture1d.md#class-gradienttexture1d), [CurveTexture](class_curvetexture.md#class-curvetexture) and [CurveXYZTexture](class_curvexyztexture.md#class-curvexyztexture).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Fill](class_gradienttexture2d.md#enum-gradienttexture2d-fill) | [fill](class_gradienttexture2d.md#class-gradienttexture2d-property-fill) | `0` |
| [Vector2](class_vector2.md#class-vector2) | [fill_from](class_gradienttexture2d.md#class-gradienttexture2d-property-fill-from) | `Vector2(0, 0)` |
| [Vector2](class_vector2.md#class-vector2) | [fill_to](class_gradienttexture2d.md#class-gradienttexture2d-property-fill-to) | `Vector2(1, 0)` |
| [Gradient](class_gradient.md#class-gradient) | [gradient](class_gradienttexture2d.md#class-gradienttexture2d-property-gradient) |  |
| [int](class_int.md#class-int) | [height](class_gradienttexture2d.md#class-gradienttexture2d-property-height) | `64` |
| [Repeat](class_gradienttexture2d.md#enum-gradienttexture2d-repeat) | [repeat](class_gradienttexture2d.md#class-gradienttexture2d-property-repeat) | `0` |
| [bool](class_bool.md#class-bool) | resource_local_to_scene | `false` (overrides [Resource](class_resource.md#class-resource-property-resource-local-to-scene)) |
| [bool](class_bool.md#class-bool) | [use_hdr](class_gradienttexture2d.md#class-gradienttexture2d-property-use-hdr) | `false` |
| [int](class_int.md#class-int) | [width](class_gradienttexture2d.md#class-gradienttexture2d-property-width) | `64` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-gradienttexture2d-fill"></a>

enum **Fill**: [🔗](class_gradienttexture2d.md#enum-gradienttexture2d-fill)

<a id="class-gradienttexture2d-constant-fill-linear"></a>

[Fill](class_gradienttexture2d.md#enum-gradienttexture2d-fill) **FILL_LINEAR** = `0`

The colors are linearly interpolated in a straight line.

<a id="class-gradienttexture2d-constant-fill-radial"></a>

[Fill](class_gradienttexture2d.md#enum-gradienttexture2d-fill) **FILL_RADIAL** = `1`

The colors are linearly interpolated in a circular pattern.

<a id="class-gradienttexture2d-constant-fill-square"></a>

[Fill](class_gradienttexture2d.md#enum-gradienttexture2d-fill) **FILL_SQUARE** = `2`

The colors are linearly interpolated in a square pattern.

<a id="class-gradienttexture2d-constant-fill-conic"></a>

[Fill](class_gradienttexture2d.md#enum-gradienttexture2d-fill) **FILL_CONIC** = `3`

The colors are linearly interpolated in a cone pattern.

---


<a id="enum-gradienttexture2d-repeat"></a>

enum **Repeat**: [🔗](class_gradienttexture2d.md#enum-gradienttexture2d-repeat)

<a id="class-gradienttexture2d-constant-repeat-none"></a>

[Repeat](class_gradienttexture2d.md#enum-gradienttexture2d-repeat) **REPEAT_NONE** = `0`

The gradient fill is restricted to the range defined by [fill_from](class_gradienttexture2d.md#class-gradienttexture2d-property-fill-from) to [fill_to](class_gradienttexture2d.md#class-gradienttexture2d-property-fill-to) offsets.

<a id="class-gradienttexture2d-constant-repeat"></a>

[Repeat](class_gradienttexture2d.md#enum-gradienttexture2d-repeat) **REPEAT** = `1`

The texture is filled starting from [fill_from](class_gradienttexture2d.md#class-gradienttexture2d-property-fill-from) to [fill_to](class_gradienttexture2d.md#class-gradienttexture2d-property-fill-to) offsets, repeating the same pattern in both directions.

<a id="class-gradienttexture2d-constant-repeat-mirror"></a>

[Repeat](class_gradienttexture2d.md#enum-gradienttexture2d-repeat) **REPEAT_MIRROR** = `2`

The texture is filled starting from [fill_from](class_gradienttexture2d.md#class-gradienttexture2d-property-fill-from) to [fill_to](class_gradienttexture2d.md#class-gradienttexture2d-property-fill-to) offsets, mirroring the pattern in both directions.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-gradienttexture2d-property-fill"></a>

[Fill](class_gradienttexture2d.md#enum-gradienttexture2d-fill) **fill** = `0` [🔗](class_gradienttexture2d.md#class-gradienttexture2d-property-fill)

- void **set_fill**(value: [Fill](class_gradienttexture2d.md#enum-gradienttexture2d-fill))
- [Fill](class_gradienttexture2d.md#enum-gradienttexture2d-fill) **get_fill**()

The gradient's fill type.

---


<a id="class-gradienttexture2d-property-fill-from"></a>

[Vector2](class_vector2.md#class-vector2) **fill_from** = `Vector2(0, 0)` [🔗](class_gradienttexture2d.md#class-gradienttexture2d-property-fill-from)

- void **set_fill_from**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_fill_from**()

The initial offset used to fill the texture specified in UV coordinates.

---


<a id="class-gradienttexture2d-property-fill-to"></a>

[Vector2](class_vector2.md#class-vector2) **fill_to** = `Vector2(1, 0)` [🔗](class_gradienttexture2d.md#class-gradienttexture2d-property-fill-to)

- void **set_fill_to**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_fill_to**()

The final offset used to fill the texture specified in UV coordinates.

---


<a id="class-gradienttexture2d-property-gradient"></a>

[Gradient](class_gradient.md#class-gradient) **gradient** [🔗](class_gradienttexture2d.md#class-gradienttexture2d-property-gradient)

- void **set_gradient**(value: [Gradient](class_gradient.md#class-gradient))
- [Gradient](class_gradient.md#class-gradient) **get_gradient**()

The [Gradient](class_gradient.md#class-gradient) used to fill the texture.

---


<a id="class-gradienttexture2d-property-height"></a>

[int](class_int.md#class-int) **height** = `64` [🔗](class_gradienttexture2d.md#class-gradienttexture2d-property-height)

- void **set_height**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_height**()

The number of vertical color samples that will be obtained from the [Gradient](class_gradient.md#class-gradient), which also represents the texture's height.

---


<a id="class-gradienttexture2d-property-repeat"></a>

[Repeat](class_gradienttexture2d.md#enum-gradienttexture2d-repeat) **repeat** = `0` [🔗](class_gradienttexture2d.md#class-gradienttexture2d-property-repeat)

- void **set_repeat**(value: [Repeat](class_gradienttexture2d.md#enum-gradienttexture2d-repeat))
- [Repeat](class_gradienttexture2d.md#enum-gradienttexture2d-repeat) **get_repeat**()

The gradient's repeat type.

---


<a id="class-gradienttexture2d-property-use-hdr"></a>

[bool](class_bool.md#class-bool) **use_hdr** = `false` [🔗](class_gradienttexture2d.md#class-gradienttexture2d-property-use-hdr)

- void **set_use_hdr**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_using_hdr**()

If `true`, the generated texture will support high dynamic range ([Image.FORMAT_RGBAF](class_image.md#class-image-constant-format-rgbaf) format). This allows for glow effects to work if [Environment.glow_enabled](class_environment.md#class-environment-property-glow-enabled) is `true`. If `false`, the generated texture will use low dynamic range; overbright colors will be clamped ([Image.FORMAT_RGBA8](class_image.md#class-image-constant-format-rgba8) format).

---


<a id="class-gradienttexture2d-property-width"></a>

[int](class_int.md#class-int) **width** = `64` [🔗](class_gradienttexture2d.md#class-gradienttexture2d-property-width)

- void **set_width**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_width**()

The number of horizontal color samples that will be obtained from the [Gradient](class_gradient.md#class-gradient), which also represents the texture's width.
