> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodecubemap.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodecubemap"></a>

<a id="class-visualshadernodecubemap"></a>

# VisualShaderNodeCubemap

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A [Cubemap](class_cubemap.md#class-cubemap) sampling node to be used within the visual shader graph.

<a id="description"></a>

## Description

Translated to `texture(cubemap, vec3)` in the shader language. Returns a color vector and alpha channel as scalar.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [TextureLayered](class_texturelayered.md#class-texturelayered) | [cube_map](class_visualshadernodecubemap.md#class-visualshadernodecubemap-property-cube-map) |  |
| [Source](class_visualshadernodecubemap.md#enum-visualshadernodecubemap-source) | [source](class_visualshadernodecubemap.md#class-visualshadernodecubemap-property-source) | `0` |
| [TextureType](class_visualshadernodecubemap.md#enum-visualshadernodecubemap-texturetype) | [texture_type](class_visualshadernodecubemap.md#class-visualshadernodecubemap-property-texture-type) | `0` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-visualshadernodecubemap-source"></a>

enum **Source**: [🔗](class_visualshadernodecubemap.md#enum-visualshadernodecubemap-source)

<a id="class-visualshadernodecubemap-constant-source-texture"></a>

[Source](class_visualshadernodecubemap.md#enum-visualshadernodecubemap-source) **SOURCE_TEXTURE** = `0`

Use the [Cubemap](class_cubemap.md#class-cubemap) set via [cube_map](class_visualshadernodecubemap.md#class-visualshadernodecubemap-property-cube-map). If this is set to [source](class_visualshadernodecubemap.md#class-visualshadernodecubemap-property-source), the `samplerCube` port is ignored.

<a id="class-visualshadernodecubemap-constant-source-port"></a>

[Source](class_visualshadernodecubemap.md#enum-visualshadernodecubemap-source) **SOURCE_PORT** = `1`

Use the [Cubemap](class_cubemap.md#class-cubemap) sampler reference passed via the `samplerCube` port. If this is set to [source](class_visualshadernodecubemap.md#class-visualshadernodecubemap-property-source), the [cube_map](class_visualshadernodecubemap.md#class-visualshadernodecubemap-property-cube-map) texture is ignored.

<a id="class-visualshadernodecubemap-constant-source-max"></a>

[Source](class_visualshadernodecubemap.md#enum-visualshadernodecubemap-source) **SOURCE_MAX** = `2`

Represents the size of the [Source](class_visualshadernodecubemap.md#enum-visualshadernodecubemap-source) enum.

---


<a id="enum-visualshadernodecubemap-texturetype"></a>

enum **TextureType**: [🔗](class_visualshadernodecubemap.md#enum-visualshadernodecubemap-texturetype)

<a id="class-visualshadernodecubemap-constant-type-data"></a>

[TextureType](class_visualshadernodecubemap.md#enum-visualshadernodecubemap-texturetype) **TYPE_DATA** = `0`

No hints are added to the uniform declaration.

<a id="class-visualshadernodecubemap-constant-type-color"></a>

[TextureType](class_visualshadernodecubemap.md#enum-visualshadernodecubemap-texturetype) **TYPE_COLOR** = `1`

Adds `source_color` as hint to the uniform declaration for proper conversion from nonlinear sRGB encoding to linear encoding.

<a id="class-visualshadernodecubemap-constant-type-normal-map"></a>

[TextureType](class_visualshadernodecubemap.md#enum-visualshadernodecubemap-texturetype) **TYPE_NORMAL_MAP** = `2`

Adds `hint_normal` as hint to the uniform declaration, which internally converts the texture for proper usage as normal map.

<a id="class-visualshadernodecubemap-constant-type-max"></a>

[TextureType](class_visualshadernodecubemap.md#enum-visualshadernodecubemap-texturetype) **TYPE_MAX** = `3`

Represents the size of the [TextureType](class_visualshadernodecubemap.md#enum-visualshadernodecubemap-texturetype) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodecubemap-property-cube-map"></a>

[TextureLayered](class_texturelayered.md#class-texturelayered) **cube_map** [🔗](class_visualshadernodecubemap.md#class-visualshadernodecubemap-property-cube-map)

- void **set_cube_map**(value: [TextureLayered](class_texturelayered.md#class-texturelayered))
- [TextureLayered](class_texturelayered.md#class-texturelayered) **get_cube_map**()

The [Cubemap](class_cubemap.md#class-cubemap) texture to sample when using [SOURCE_TEXTURE](class_visualshadernodecubemap.md#class-visualshadernodecubemap-constant-source-texture) as [source](class_visualshadernodecubemap.md#class-visualshadernodecubemap-property-source).

---


<a id="class-visualshadernodecubemap-property-source"></a>

[Source](class_visualshadernodecubemap.md#enum-visualshadernodecubemap-source) **source** = `0` [🔗](class_visualshadernodecubemap.md#class-visualshadernodecubemap-property-source)

- void **set_source**(value: [Source](class_visualshadernodecubemap.md#enum-visualshadernodecubemap-source))
- [Source](class_visualshadernodecubemap.md#enum-visualshadernodecubemap-source) **get_source**()

Defines which source should be used for the sampling.

---


<a id="class-visualshadernodecubemap-property-texture-type"></a>

[TextureType](class_visualshadernodecubemap.md#enum-visualshadernodecubemap-texturetype) **texture_type** = `0` [🔗](class_visualshadernodecubemap.md#class-visualshadernodecubemap-property-texture-type)

- void **set_texture_type**(value: [TextureType](class_visualshadernodecubemap.md#enum-visualshadernodecubemap-texturetype))
- [TextureType](class_visualshadernodecubemap.md#enum-visualshadernodecubemap-texturetype) **get_texture_type**()

Defines the type of data provided by the source texture.
