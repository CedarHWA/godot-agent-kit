> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodetexture3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodetexture3d"></a>

<a id="class-visualshadernodetexture3d"></a>

# VisualShaderNodeTexture3D

**Inherits:** [VisualShaderNodeSample3D](class_visualshadernodesample3d.md#class-visualshadernodesample3d) **<** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Performs a 3D texture lookup within the visual shader graph.

<a id="description"></a>

## Description

Performs a lookup operation on the provided texture, with support for multiple texture sources to choose from.

<a id="properties"></a>

## Properties

|  |  |
| --- | --- |
| [Texture3D](class_texture3d.md#class-texture3d) | [texture](class_visualshadernodetexture3d.md#class-visualshadernodetexture3d-property-texture) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodetexture3d-property-texture"></a>

[Texture3D](class_texture3d.md#class-texture3d) **texture** [🔗](class_visualshadernodetexture3d.md#class-visualshadernodetexture3d-property-texture)

- void **set_texture**(value: [Texture3D](class_texture3d.md#class-texture3d))
- [Texture3D](class_texture3d.md#class-texture3d) **get_texture**()

A source texture. Used if [VisualShaderNodeSample3D.source](class_visualshadernodesample3d.md#class-visualshadernodesample3d-property-source) is set to [VisualShaderNodeSample3D.SOURCE_TEXTURE](class_visualshadernodesample3d.md#class-visualshadernodesample3d-constant-source-texture).
