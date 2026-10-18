> Source: https://docs.godotengine.org/en/4.7/classes/class_texturelayeredrd.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="texturelayeredrd"></a>

<a id="class-texturelayeredrd"></a>

# TextureLayeredRD

**Inherits:** [TextureLayered](class_texturelayered.md#class-texturelayered) **<** [Texture](class_texture.md#class-texture) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [Texture2DArrayRD](class_texture2darrayrd.md#class-texture2darrayrd), [TextureCubemapArrayRD](class_texturecubemaparrayrd.md#class-texturecubemaparrayrd), [TextureCubemapRD](class_texturecubemaprd.md#class-texturecubemaprd)

Abstract base class for layered texture RD types.

<a id="description"></a>

## Description

Base class for [Texture2DArrayRD](class_texture2darrayrd.md#class-texture2darrayrd), [TextureCubemapRD](class_texturecubemaprd.md#class-texturecubemaprd) and [TextureCubemapArrayRD](class_texturecubemaparrayrd.md#class-texturecubemaparrayrd). Cannot be used directly, but contains all the functions necessary for accessing the derived resource types.

**Note:** **TextureLayeredRD** is intended for low-level usage with [RenderingDevice](class_renderingdevice.md#class-renderingdevice). For most use cases, use [TextureLayered](class_texturelayered.md#class-texturelayered) instead.

<a id="tutorials"></a>

## Tutorials

- [Compute Texture demo](https://godotengine.org/asset-library/asset/2764)

<a id="properties"></a>

## Properties

|  |  |
| --- | --- |
| [RID](class_rid.md#class-rid) | [texture_rd_rid](class_texturelayeredrd.md#class-texturelayeredrd-property-texture-rd-rid) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-texturelayeredrd-property-texture-rd-rid"></a>

[RID](class_rid.md#class-rid) **texture_rd_rid** [🔗](class_texturelayeredrd.md#class-texturelayeredrd-property-texture-rd-rid)

- void **set_texture_rd_rid**(value: [RID](class_rid.md#class-rid))
- [RID](class_rid.md#class-rid) **get_texture_rd_rid**()

The RID of the texture object created on the [RenderingDevice](class_renderingdevice.md#class-renderingdevice).
