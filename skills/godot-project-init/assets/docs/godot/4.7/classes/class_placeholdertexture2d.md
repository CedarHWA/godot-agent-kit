> Source: https://docs.godotengine.org/en/4.7/classes/class_placeholdertexture2d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="placeholdertexture2d"></a>

<a id="class-placeholdertexture2d"></a>

# PlaceholderTexture2D

**Inherits:** [Texture2D](class_texture2d.md#class-texture2d) **<** [Texture](class_texture.md#class-texture) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Placeholder class for a 2-dimensional texture.

<a id="description"></a>

## Description

This class is used when loading a project that uses a [Texture2D](class_texture2d.md#class-texture2d) subclass in 2 conditions:

- When running the project exported in dedicated server mode, only the texture's dimensions are kept (as they may be relied upon for gameplay purposes or positioning of other elements). This allows reducing the exported PCK's size significantly.
- When this subclass is missing due to using a different engine version or build (e.g. modules disabled).

**Note:** This is not intended to be used as an actual texture for rendering. It is not guaranteed to work like one in shaders or materials (for example when calculating UV).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | resource_local_to_scene | `false` (overrides [Resource](class_resource.md#class-resource-property-resource-local-to-scene)) |
| [Vector2](class_vector2.md#class-vector2) | [size](class_placeholdertexture2d.md#class-placeholdertexture2d-property-size) | `Vector2(1, 1)` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-placeholdertexture2d-property-size"></a>

[Vector2](class_vector2.md#class-vector2) **size** = `Vector2(1, 1)` [🔗](class_placeholdertexture2d.md#class-placeholdertexture2d-property-size)

- void **set_size**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_size**()

The texture's size (in pixels).
