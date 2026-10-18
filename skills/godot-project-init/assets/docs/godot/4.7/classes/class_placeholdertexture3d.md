> Source: https://docs.godotengine.org/en/4.7/classes/class_placeholdertexture3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="placeholdertexture3d"></a>

<a id="class-placeholdertexture3d"></a>

# PlaceholderTexture3D

**Inherits:** [Texture3D](class_texture3d.md#class-texture3d) **<** [Texture](class_texture.md#class-texture) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Placeholder class for a 3-dimensional texture.

<a id="description"></a>

## Description

This class is used when loading a project that uses a [Texture3D](class_texture3d.md#class-texture3d) subclass in 2 conditions:

- When running the project exported in dedicated server mode, only the texture's dimensions are kept (as they may be relied upon for gameplay purposes or positioning of other elements). This allows reducing the exported PCK's size significantly.
- When this subclass is missing due to using a different engine version or build (e.g. modules disabled).

**Note:** This is not intended to be used as an actual texture for rendering. It is not guaranteed to work like one in shaders or materials (for example when calculating UV).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Vector3i](class_vector3i.md#class-vector3i) | [size](class_placeholdertexture3d.md#class-placeholdertexture3d-property-size) | `Vector3i(1, 1, 1)` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-placeholdertexture3d-property-size"></a>

[Vector3i](class_vector3i.md#class-vector3i) **size** = `Vector3i(1, 1, 1)` [🔗](class_placeholdertexture3d.md#class-placeholdertexture3d-property-size)

- void **set_size**(value: [Vector3i](class_vector3i.md#class-vector3i))
- [Vector3i](class_vector3i.md#class-vector3i) **get_size**()

The texture's size (in pixels).
