> Source: https://docs.godotengine.org/en/4.7/classes/class_texture2drd.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="texture2drd"></a>

<a id="class-texture2drd"></a>

# Texture2DRD

**Inherits:** [Texture2D](class_texture2d.md#class-texture2d) **<** [Texture](class_texture.md#class-texture) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Texture for 2D that is bound to a texture created on the [RenderingDevice](class_renderingdevice.md#class-renderingdevice).

<a id="description"></a>

## Description

This texture class allows you to use a 2D texture created directly on the [RenderingDevice](class_renderingdevice.md#class-renderingdevice) as a texture for materials, meshes, etc.

**Note:** **Texture2DRD** is intended for low-level usage with [RenderingDevice](class_renderingdevice.md#class-renderingdevice). For most use cases, use [Texture2D](class_texture2d.md#class-texture2d) instead.

<a id="tutorials"></a>

## Tutorials

- [Compute Texture demo](https://godotengine.org/asset-library/asset/2764)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | resource_local_to_scene | `false` (overrides [Resource](class_resource.md#class-resource-property-resource-local-to-scene)) |
| [RID](class_rid.md#class-rid) | [texture_rd_rid](class_texture2drd.md#class-texture2drd-property-texture-rd-rid) |  |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-texture2drd-property-texture-rd-rid"></a>

[RID](class_rid.md#class-rid) **texture_rd_rid** [🔗](class_texture2drd.md#class-texture2drd-property-texture-rd-rid)

- void **set_texture_rd_rid**(value: [RID](class_rid.md#class-rid))
- [RID](class_rid.md#class-rid) **get_texture_rd_rid**()

The RID of the texture object created on the [RenderingDevice](class_renderingdevice.md#class-renderingdevice).
