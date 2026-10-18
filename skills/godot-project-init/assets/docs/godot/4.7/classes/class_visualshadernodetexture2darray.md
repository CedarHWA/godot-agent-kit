> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodetexture2darray.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodetexture2darray"></a>

<a id="class-visualshadernodetexture2darray"></a>

# VisualShaderNodeTexture2DArray

**Inherits:** [VisualShaderNodeSample3D](class_visualshadernodesample3d.md#class-visualshadernodesample3d) **<** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A 2D texture uniform array to be used within the visual shader graph.

<a id="description"></a>

## Description

Translated to `uniform sampler2DArray` in the shader language.

<a id="properties"></a>

## Properties

|  |  |
| --- | --- |
| [TextureLayered](class_texturelayered.md#class-texturelayered) | [texture_array](class_visualshadernodetexture2darray.md#class-visualshadernodetexture2darray-property-texture-array) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodetexture2darray-property-texture-array"></a>

[TextureLayered](class_texturelayered.md#class-texturelayered) **texture_array** [🔗](class_visualshadernodetexture2darray.md#class-visualshadernodetexture2darray-property-texture-array)

- void **set_texture_array**(value: [TextureLayered](class_texturelayered.md#class-texturelayered))
- [TextureLayered](class_texturelayered.md#class-texturelayered) **get_texture_array**()

A source texture array. Used if [VisualShaderNodeSample3D.source](class_visualshadernodesample3d.md#class-visualshadernodesample3d-property-source) is set to [VisualShaderNodeSample3D.SOURCE_TEXTURE](class_visualshadernodesample3d.md#class-visualshadernodesample3d-constant-source-texture).
