> Source: https://docs.godotengine.org/en/4.7/classes/class_drawabletexture2d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="drawabletexture2d"></a>

<a id="class-drawabletexture2d"></a>

# DrawableTexture2D

**Inherits:** [Texture2D](class_texture2d.md#class-texture2d) **<** [Texture](class_texture.md#class-texture) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A 2D texture that supports drawing to itself via Blit calls.

<a id="description"></a>

## Description

A 2D texture that can be modified via blit calls, copying from a target texture to itself. Primarily intended to be managed in code, a user must call [setup()](class_drawabletexture2d.md#class-drawabletexture2d-method-setup) to initialize the state before drawing. Each [blit_rect()](class_drawabletexture2d.md#class-drawabletexture2d-method-blit-rect) call takes at least a rectangle, the area to draw to, and another texture, what to be drawn. The draw calls use a Texture_Blit Shader to process and calculate the result, pixel by pixel. Users can supply their own ShaderMaterial with custom Texture_Blit shaders for more complex behaviors.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | resource_local_to_scene | `false` (overrides [Resource](class_resource.md#class-resource-property-resource-local-to-scene)) |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [blit_rect](class_drawabletexture2d.md#class-drawabletexture2d-method-blit-rect)(rect: [Rect2i](class_rect2i.md#class-rect2i), source: [Texture2D](class_texture2d.md#class-texture2d), modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), mipmap: [int](class_int.md#class-int) = 0, material: [Material](class_material.md#class-material) = null) |
| void | [blit_rect_multi](class_drawabletexture2d.md#class-drawabletexture2d-method-blit-rect-multi)(rect: [Rect2i](class_rect2i.md#class-rect2i), sources: [Array](class_array.md#class-array)[[Texture2D](class_texture2d.md#class-texture2d)], extra_targets: [Array](class_array.md#class-array)[[DrawableTexture2D](class_drawabletexture2d.md#class-drawabletexture2d)], modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), mipmap: [int](class_int.md#class-int) = 0, material: [Material](class_material.md#class-material) = null) |
| void | [generate_mipmaps](class_drawabletexture2d.md#class-drawabletexture2d-method-generate-mipmaps)() |
| [bool](class_bool.md#class-bool) | [get_use_mipmaps](class_drawabletexture2d.md#class-drawabletexture2d-method-get-use-mipmaps)() const |
| void | [set_format](class_drawabletexture2d.md#class-drawabletexture2d-method-set-format)(format: [DrawableFormat](class_drawabletexture2d.md#enum-drawabletexture2d-drawableformat)) |
| void | [set_use_mipmaps](class_drawabletexture2d.md#class-drawabletexture2d-method-set-use-mipmaps)(mipmaps: [bool](class_bool.md#class-bool)) |
| void | [setup](class_drawabletexture2d.md#class-drawabletexture2d-method-setup)(width: [int](class_int.md#class-int), height: [int](class_int.md#class-int), format: [DrawableFormat](class_drawabletexture2d.md#enum-drawabletexture2d-drawableformat), color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), use_mipmaps: [bool](class_bool.md#class-bool) = false) |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-drawabletexture2d-drawableformat"></a>

enum **DrawableFormat**: [🔗](class_drawabletexture2d.md#enum-drawabletexture2d-drawableformat)

<a id="class-drawabletexture2d-constant-drawable-format-rgba8"></a>

[DrawableFormat](class_drawabletexture2d.md#enum-drawabletexture2d-drawableformat) **DRAWABLE_FORMAT_RGBA8** = `0`

OpenGL texture format RGBA with four components, each with a bitdepth of 8.

<a id="class-drawabletexture2d-constant-drawable-format-rgba8-srgb"></a>

[DrawableFormat](class_drawabletexture2d.md#enum-drawabletexture2d-drawableformat) **DRAWABLE_FORMAT_RGBA8_SRGB** = `1`

OpenGL texture format RGBA with four components, each with a bitdepth of 8.

When drawn to, an sRGB to linear color space conversion is performed.

<a id="class-drawabletexture2d-constant-drawable-format-rgbah"></a>

[DrawableFormat](class_drawabletexture2d.md#enum-drawabletexture2d-drawableformat) **DRAWABLE_FORMAT_RGBAH** = `2`

OpenGL texture format GL_RGBA16F where there are four components, each a 16-bit "half-precision" floating-point value.

<a id="class-drawabletexture2d-constant-drawable-format-rgbaf"></a>

[DrawableFormat](class_drawabletexture2d.md#enum-drawabletexture2d-drawableformat) **DRAWABLE_FORMAT_RGBAF** = `3`

OpenGL texture format GL_RGBA32F where there are four components, each a 32-bit floating-point value.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-drawabletexture2d-method-blit-rect"></a>

void **blit_rect**(rect: [Rect2i](class_rect2i.md#class-rect2i), source: [Texture2D](class_texture2d.md#class-texture2d), modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), mipmap: [int](class_int.md#class-int) = 0, material: [Material](class_material.md#class-material) = null) [🔗](class_drawabletexture2d.md#class-drawabletexture2d-method-blit-rect)

**Experimental:** This method may be changed or removed in future versions.

Draws to given `rect` on this texture by copying from the given `source`. A `modulate` color can be passed in for the shader to use, but defaults to White. The `mipmap` value can specify a draw to a lower mipmap level. The `material` parameter can take a ShaderMaterial with a TextureBlit Shader for custom drawing behavior.

---


<a id="class-drawabletexture2d-method-blit-rect-multi"></a>

void **blit_rect_multi**(rect: [Rect2i](class_rect2i.md#class-rect2i), sources: [Array](class_array.md#class-array)[[Texture2D](class_texture2d.md#class-texture2d)], extra_targets: [Array](class_array.md#class-array)[[DrawableTexture2D](class_drawabletexture2d.md#class-drawabletexture2d)], modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), mipmap: [int](class_int.md#class-int) = 0, material: [Material](class_material.md#class-material) = null) [🔗](class_drawabletexture2d.md#class-drawabletexture2d-method-blit-rect-multi)

**Experimental:** This method may be changed or removed in future versions.

Draws to the given `rect` on this texture, as well as on up to 3 DrawableTexture `extra_targets`. All `extra_targets` must be the same size and DrawableFormat as the original target, otherwise the Shader may fail. Expects up to 4 Texture `sources`, but will replace missing `sources` with default Black Textures.

---


<a id="class-drawabletexture2d-method-generate-mipmaps"></a>

void **generate_mipmaps**() [🔗](class_drawabletexture2d.md#class-drawabletexture2d-method-generate-mipmaps)

Re-calculates the mipmaps for this texture on demand.

---


<a id="class-drawabletexture2d-method-get-use-mipmaps"></a>

[bool](class_bool.md#class-bool) **get_use_mipmaps**() const [🔗](class_drawabletexture2d.md#class-drawabletexture2d-method-get-use-mipmaps)

Returns `true` if mipmaps are set to be used on this DrawableTexture.

---


<a id="class-drawabletexture2d-method-set-format"></a>

void **set_format**(format: [DrawableFormat](class_drawabletexture2d.md#enum-drawabletexture2d-drawableformat)) [🔗](class_drawabletexture2d.md#class-drawabletexture2d-method-set-format)

Sets the format of this DrawableTexture.

---


<a id="class-drawabletexture2d-method-set-use-mipmaps"></a>

void **set_use_mipmaps**(mipmaps: [bool](class_bool.md#class-bool)) [🔗](class_drawabletexture2d.md#class-drawabletexture2d-method-set-use-mipmaps)

Sets if mipmaps should be used on this DrawableTexture.

---


<a id="class-drawabletexture2d-method-setup"></a>

void **setup**(width: [int](class_int.md#class-int), height: [int](class_int.md#class-int), format: [DrawableFormat](class_drawabletexture2d.md#enum-drawabletexture2d-drawableformat), color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), use_mipmaps: [bool](class_bool.md#class-bool) = false) [🔗](class_drawabletexture2d.md#class-drawabletexture2d-method-setup)

**Experimental:** This method may be changed or removed in future versions.

Initializes the DrawableTexture to a White texture of the given `width`, `height`, and `format`.
