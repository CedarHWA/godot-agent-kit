> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodetexture.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodetexture"></a>

<a id="class-visualshadernodetexture"></a>

# VisualShaderNodeTexture

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Performs a 2D texture lookup within the visual shader graph.

<a id="description"></a>

## Description

Performs a lookup operation on the provided texture, with support for multiple texture sources to choose from.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Source](class_visualshadernodetexture.md#enum-visualshadernodetexture-source) | [source](class_visualshadernodetexture.md#class-visualshadernodetexture-property-source) | `0` |
| [Texture2D](class_texture2d.md#class-texture2d) | [texture](class_visualshadernodetexture.md#class-visualshadernodetexture-property-texture) |  |
| [TextureType](class_visualshadernodetexture.md#enum-visualshadernodetexture-texturetype) | [texture_type](class_visualshadernodetexture.md#class-visualshadernodetexture-property-texture-type) | `0` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-visualshadernodetexture-source"></a>

enum **Source**: [🔗](class_visualshadernodetexture.md#enum-visualshadernodetexture-source)

<a id="class-visualshadernodetexture-constant-source-texture"></a>

[Source](class_visualshadernodetexture.md#enum-visualshadernodetexture-source) **SOURCE_TEXTURE** = `0`

Use the texture given as an argument for this function.

<a id="class-visualshadernodetexture-constant-source-screen"></a>

[Source](class_visualshadernodetexture.md#enum-visualshadernodetexture-source) **SOURCE_SCREEN** = `1`

Use the current viewport's texture as the source.

<a id="class-visualshadernodetexture-constant-source-2d-texture"></a>

[Source](class_visualshadernodetexture.md#enum-visualshadernodetexture-source) **SOURCE_2D_TEXTURE** = `2`

Use the texture from this shader's texture built-in (e.g. a texture of a [Sprite2D](class_sprite2d.md#class-sprite2d)).

<a id="class-visualshadernodetexture-constant-source-2d-normal"></a>

[Source](class_visualshadernodetexture.md#enum-visualshadernodetexture-source) **SOURCE_2D_NORMAL** = `3`

Use the texture from this shader's normal map built-in.

<a id="class-visualshadernodetexture-constant-source-depth"></a>

[Source](class_visualshadernodetexture.md#enum-visualshadernodetexture-source) **SOURCE_DEPTH** = `4`

Use the depth texture captured during the depth prepass. Only available when the depth prepass is used (i.e. in spatial shaders and in the forward_plus or gl_compatibility renderers).

<a id="class-visualshadernodetexture-constant-source-port"></a>

[Source](class_visualshadernodetexture.md#enum-visualshadernodetexture-source) **SOURCE_PORT** = `5`

Use the texture provided in the input port for this function.

<a id="class-visualshadernodetexture-constant-source-3d-normal"></a>

[Source](class_visualshadernodetexture.md#enum-visualshadernodetexture-source) **SOURCE_3D_NORMAL** = `6`

Use the normal buffer captured during the depth prepass. Only available when the normal-roughness buffer is available (i.e. in spatial shaders and in the forward_plus renderer).

<a id="class-visualshadernodetexture-constant-source-roughness"></a>

[Source](class_visualshadernodetexture.md#enum-visualshadernodetexture-source) **SOURCE_ROUGHNESS** = `7`

Use the roughness buffer captured during the depth prepass. Only available when the normal-roughness buffer is available (i.e. in spatial shaders and in the forward_plus renderer).

<a id="class-visualshadernodetexture-constant-source-max"></a>

[Source](class_visualshadernodetexture.md#enum-visualshadernodetexture-source) **SOURCE_MAX** = `8`

Represents the size of the [Source](class_visualshadernodetexture.md#enum-visualshadernodetexture-source) enum.

---


<a id="enum-visualshadernodetexture-texturetype"></a>

enum **TextureType**: [🔗](class_visualshadernodetexture.md#enum-visualshadernodetexture-texturetype)

<a id="class-visualshadernodetexture-constant-type-data"></a>

[TextureType](class_visualshadernodetexture.md#enum-visualshadernodetexture-texturetype) **TYPE_DATA** = `0`

No hints are added to the uniform declaration.

<a id="class-visualshadernodetexture-constant-type-color"></a>

[TextureType](class_visualshadernodetexture.md#enum-visualshadernodetexture-texturetype) **TYPE_COLOR** = `1`

Adds `source_color` as hint to the uniform declaration for proper conversion from nonlinear sRGB encoding to linear encoding.

<a id="class-visualshadernodetexture-constant-type-normal-map"></a>

[TextureType](class_visualshadernodetexture.md#enum-visualshadernodetexture-texturetype) **TYPE_NORMAL_MAP** = `2`

Adds `hint_normal` as hint to the uniform declaration, which internally converts the texture for proper usage as normal map.

<a id="class-visualshadernodetexture-constant-type-max"></a>

[TextureType](class_visualshadernodetexture.md#enum-visualshadernodetexture-texturetype) **TYPE_MAX** = `3`

Represents the size of the [TextureType](class_visualshadernodetexture.md#enum-visualshadernodetexture-texturetype) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodetexture-property-source"></a>

[Source](class_visualshadernodetexture.md#enum-visualshadernodetexture-source) **source** = `0` [🔗](class_visualshadernodetexture.md#class-visualshadernodetexture-property-source)

- void **set_source**(value: [Source](class_visualshadernodetexture.md#enum-visualshadernodetexture-source))
- [Source](class_visualshadernodetexture.md#enum-visualshadernodetexture-source) **get_source**()

Determines the source for the lookup.

---


<a id="class-visualshadernodetexture-property-texture"></a>

[Texture2D](class_texture2d.md#class-texture2d) **texture** [🔗](class_visualshadernodetexture.md#class-visualshadernodetexture-property-texture)

- void **set_texture**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_texture**()

The source texture, if needed for the selected [source](class_visualshadernodetexture.md#class-visualshadernodetexture-property-source).

---


<a id="class-visualshadernodetexture-property-texture-type"></a>

[TextureType](class_visualshadernodetexture.md#enum-visualshadernodetexture-texturetype) **texture_type** = `0` [🔗](class_visualshadernodetexture.md#class-visualshadernodetexture-property-texture-type)

- void **set_texture_type**(value: [TextureType](class_visualshadernodetexture.md#enum-visualshadernodetexture-texturetype))
- [TextureType](class_visualshadernodetexture.md#enum-visualshadernodetexture-texturetype) **get_texture_type**()

Specifies the type of the texture if [source](class_visualshadernodetexture.md#class-visualshadernodetexture-property-source) is set to [SOURCE_TEXTURE](class_visualshadernodetexture.md#class-visualshadernodetexture-constant-source-texture).
