> Source: https://docs.godotengine.org/en/4.7/classes/class_noise.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="noise"></a>

<a id="class-noise"></a>

# Noise

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [FastNoiseLite](class_fastnoiselite.md#class-fastnoiselite)

Abstract base class for noise generators.

<a id="description"></a>

## Description

This class defines the interface for noise generation libraries to inherit from.

A default [get_seamless_image()](class_noise.md#class-noise-method-get-seamless-image) implementation is provided for libraries that do not provide seamless noise. This function requests a larger image from the [get_image()](class_noise.md#class-noise-method-get-image) method, reverses the quadrants of the image, then uses the strips of extra width to blend over the seams.

Inheriting noise classes can optionally override this function to provide a more optimal algorithm.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Image](class_image.md#class-image) | [get_image](class_noise.md#class-noise-method-get-image)(width: [int](class_int.md#class-int), height: [int](class_int.md#class-int), invert: [bool](class_bool.md#class-bool) = false, in_3d_space: [bool](class_bool.md#class-bool) = false, normalize: [bool](class_bool.md#class-bool) = true) const |
| [Array](class_array.md#class-array)[[Image](class_image.md#class-image)] | [get_image_3d](class_noise.md#class-noise-method-get-image-3d)(width: [int](class_int.md#class-int), height: [int](class_int.md#class-int), depth: [int](class_int.md#class-int), invert: [bool](class_bool.md#class-bool) = false, normalize: [bool](class_bool.md#class-bool) = true) const |
| [float](class_float.md#class-float) | [get_noise_1d](class_noise.md#class-noise-method-get-noise-1d)(x: [float](class_float.md#class-float)) const |
| [float](class_float.md#class-float) | [get_noise_2d](class_noise.md#class-noise-method-get-noise-2d)(x: [float](class_float.md#class-float), y: [float](class_float.md#class-float)) const |
| [float](class_float.md#class-float) | [get_noise_2dv](class_noise.md#class-noise-method-get-noise-2dv)(v: [Vector2](class_vector2.md#class-vector2)) const |
| [float](class_float.md#class-float) | [get_noise_3d](class_noise.md#class-noise-method-get-noise-3d)(x: [float](class_float.md#class-float), y: [float](class_float.md#class-float), z: [float](class_float.md#class-float)) const |
| [float](class_float.md#class-float) | [get_noise_3dv](class_noise.md#class-noise-method-get-noise-3dv)(v: [Vector3](class_vector3.md#class-vector3)) const |
| [Image](class_image.md#class-image) | [get_seamless_image](class_noise.md#class-noise-method-get-seamless-image)(width: [int](class_int.md#class-int), height: [int](class_int.md#class-int), invert: [bool](class_bool.md#class-bool) = false, in_3d_space: [bool](class_bool.md#class-bool) = false, skirt: [float](class_float.md#class-float) = 0.1, normalize: [bool](class_bool.md#class-bool) = true) const |
| [Array](class_array.md#class-array)[[Image](class_image.md#class-image)] | [get_seamless_image_3d](class_noise.md#class-noise-method-get-seamless-image-3d)(width: [int](class_int.md#class-int), height: [int](class_int.md#class-int), depth: [int](class_int.md#class-int), invert: [bool](class_bool.md#class-bool) = false, skirt: [float](class_float.md#class-float) = 0.1, normalize: [bool](class_bool.md#class-bool) = true) const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-noise-method-get-image"></a>

[Image](class_image.md#class-image) **get_image**(width: [int](class_int.md#class-int), height: [int](class_int.md#class-int), invert: [bool](class_bool.md#class-bool) = false, in_3d_space: [bool](class_bool.md#class-bool) = false, normalize: [bool](class_bool.md#class-bool) = true) const [🔗](class_noise.md#class-noise-method-get-image)

Returns an [Image](class_image.md#class-image) containing 2D noise values.

**Note:** With `normalize` set to `false`, the default implementation expects the noise generator to return values in the range `-1.0` to `1.0`.

---


<a id="class-noise-method-get-image-3d"></a>

[Array](class_array.md#class-array)[[Image](class_image.md#class-image)] **get_image_3d**(width: [int](class_int.md#class-int), height: [int](class_int.md#class-int), depth: [int](class_int.md#class-int), invert: [bool](class_bool.md#class-bool) = false, normalize: [bool](class_bool.md#class-bool) = true) const [🔗](class_noise.md#class-noise-method-get-image-3d)

Returns an [Array](class_array.md#class-array) of [Image](class_image.md#class-image)s containing 3D noise values for use with [ImageTexture3D.create()](class_imagetexture3d.md#class-imagetexture3d-method-create).

**Note:** With `normalize` set to `false`, the default implementation expects the noise generator to return values in the range `-1.0` to `1.0`.

---


<a id="class-noise-method-get-noise-1d"></a>

[float](class_float.md#class-float) **get_noise_1d**(x: [float](class_float.md#class-float)) const [🔗](class_noise.md#class-noise-method-get-noise-1d)

Returns the 1D noise value at the given (x) coordinate.

---


<a id="class-noise-method-get-noise-2d"></a>

[float](class_float.md#class-float) **get_noise_2d**(x: [float](class_float.md#class-float), y: [float](class_float.md#class-float)) const [🔗](class_noise.md#class-noise-method-get-noise-2d)

Returns the 2D noise value at the given position.

---


<a id="class-noise-method-get-noise-2dv"></a>

[float](class_float.md#class-float) **get_noise_2dv**(v: [Vector2](class_vector2.md#class-vector2)) const [🔗](class_noise.md#class-noise-method-get-noise-2dv)

Returns the 2D noise value at the given position.

---


<a id="class-noise-method-get-noise-3d"></a>

[float](class_float.md#class-float) **get_noise_3d**(x: [float](class_float.md#class-float), y: [float](class_float.md#class-float), z: [float](class_float.md#class-float)) const [🔗](class_noise.md#class-noise-method-get-noise-3d)

Returns the 3D noise value at the given position.

---


<a id="class-noise-method-get-noise-3dv"></a>

[float](class_float.md#class-float) **get_noise_3dv**(v: [Vector3](class_vector3.md#class-vector3)) const [🔗](class_noise.md#class-noise-method-get-noise-3dv)

Returns the 3D noise value at the given position.

---


<a id="class-noise-method-get-seamless-image"></a>

[Image](class_image.md#class-image) **get_seamless_image**(width: [int](class_int.md#class-int), height: [int](class_int.md#class-int), invert: [bool](class_bool.md#class-bool) = false, in_3d_space: [bool](class_bool.md#class-bool) = false, skirt: [float](class_float.md#class-float) = 0.1, normalize: [bool](class_bool.md#class-bool) = true) const [🔗](class_noise.md#class-noise-method-get-seamless-image)

Returns an [Image](class_image.md#class-image) containing seamless 2D noise values.

**Note:** With `normalize` set to `false`, the default implementation expects the noise generator to return values in the range `-1.0` to `1.0`.

---


<a id="class-noise-method-get-seamless-image-3d"></a>

[Array](class_array.md#class-array)[[Image](class_image.md#class-image)] **get_seamless_image_3d**(width: [int](class_int.md#class-int), height: [int](class_int.md#class-int), depth: [int](class_int.md#class-int), invert: [bool](class_bool.md#class-bool) = false, skirt: [float](class_float.md#class-float) = 0.1, normalize: [bool](class_bool.md#class-bool) = true) const [🔗](class_noise.md#class-noise-method-get-seamless-image-3d)

Returns an [Array](class_array.md#class-array) of [Image](class_image.md#class-image)s containing seamless 3D noise values for use with [ImageTexture3D.create()](class_imagetexture3d.md#class-imagetexture3d-method-create).

**Note:** With `normalize` set to `false`, the default implementation expects the noise generator to return values in the range `-1.0` to `1.0`.
