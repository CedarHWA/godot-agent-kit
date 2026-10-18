> Source: https://docs.godotengine.org/en/4.7/classes/class_placeholdertexturelayered.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="placeholdertexturelayered"></a>

<a id="class-placeholdertexturelayered"></a>

# PlaceholderTextureLayered

**Inherits:** [TextureLayered](class_texturelayered.md#class-texturelayered) **<** [Texture](class_texture.md#class-texture) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [PlaceholderCubemap](class_placeholdercubemap.md#class-placeholdercubemap), [PlaceholderCubemapArray](class_placeholdercubemaparray.md#class-placeholdercubemaparray), [PlaceholderTexture2DArray](class_placeholdertexture2darray.md#class-placeholdertexture2darray)

Placeholder class for a 2-dimensional texture array.

<a id="description"></a>

## Description

This class is used when loading a project that uses a [TextureLayered](class_texturelayered.md#class-texturelayered) subclass in 2 conditions:

- When running the project exported in dedicated server mode, only the texture's dimensions are kept (as they may be relied upon for gameplay purposes or positioning of other elements). This allows reducing the exported PCK's size significantly.
- When this subclass is missing due to using a different engine version or build (e.g. modules disabled).

**Note:** This is not intended to be used as an actual texture for rendering. It is not guaranteed to work like one in shaders or materials (for example when calculating UV).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [layers](class_placeholdertexturelayered.md#class-placeholdertexturelayered-property-layers) | `1` |
| [Vector2i](class_vector2i.md#class-vector2i) | [size](class_placeholdertexturelayered.md#class-placeholdertexturelayered-property-size) | `Vector2i(1, 1)` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-placeholdertexturelayered-property-layers"></a>

[int](class_int.md#class-int) **layers** = `1` [🔗](class_placeholdertexturelayered.md#class-placeholdertexturelayered-property-layers)

- void **set_layers**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_layers**()

The number of layers in the texture array.

---


<a id="class-placeholdertexturelayered-property-size"></a>

[Vector2i](class_vector2i.md#class-vector2i) **size** = `Vector2i(1, 1)` [🔗](class_placeholdertexturelayered.md#class-placeholdertexturelayered-property-size)

- void **set_size**(value: [Vector2i](class_vector2i.md#class-vector2i))
- [Vector2i](class_vector2i.md#class-vector2i) **get_size**()

The size of each texture layer (in pixels).
