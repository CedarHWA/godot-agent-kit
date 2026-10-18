> Source: https://docs.godotengine.org/en/4.7/classes/class_texture3drd.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="texture3drd"></a>

<a id="class-texture3drd"></a>

# Texture3DRD

**Inherits:** [Texture3D](class_texture3d.md#class-texture3d) **<** [Texture](class_texture.md#class-texture) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Texture for 3D that is bound to a texture created on the [RenderingDevice](class_renderingdevice.md#class-renderingdevice).

<a id="description"></a>

## Description

This texture class allows you to use a 3D texture created directly on the [RenderingDevice](class_renderingdevice.md#class-renderingdevice) as a texture for materials, meshes, etc.

**Note:** **Texture3DRD** is intended for low-level usage with [RenderingDevice](class_renderingdevice.md#class-renderingdevice). For most use cases, use [Texture3D](class_texture3d.md#class-texture3d) instead.

<a id="tutorials"></a>

## Tutorials

- [Compute Texture demo](https://godotengine.org/asset-library/asset/2764)

<a id="properties"></a>

## Properties

|  |  |
| --- | --- |
| [RID](class_rid.md#class-rid) | [texture_rd_rid](class_texture3drd.md#class-texture3drd-property-texture-rd-rid) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-texture3drd-property-texture-rd-rid"></a>

[RID](class_rid.md#class-rid) **texture_rd_rid** [🔗](class_texture3drd.md#class-texture3drd-property-texture-rd-rid)

- void **set_texture_rd_rid**(value: [RID](class_rid.md#class-rid))
- [RID](class_rid.md#class-rid) **get_texture_rd_rid**()

The RID of the texture object created on the [RenderingDevice](class_renderingdevice.md#class-renderingdevice).
