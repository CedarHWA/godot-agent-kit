> Source: https://docs.godotengine.org/en/4.7/classes/class_compressedtexturelayered.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="compressedtexturelayered"></a>

<a id="class-compressedtexturelayered"></a>

# CompressedTextureLayered

**Inherits:** [TextureLayered](class_texturelayered.md#class-texturelayered) **<** [Texture](class_texture.md#class-texture) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [CompressedCubemap](class_compressedcubemap.md#class-compressedcubemap), [CompressedCubemapArray](class_compressedcubemaparray.md#class-compressedcubemaparray), [CompressedTexture2DArray](class_compressedtexture2darray.md#class-compressedtexture2darray)

Base class for texture arrays that can optionally be compressed.

<a id="description"></a>

## Description

Base class for [CompressedTexture2DArray](class_compressedtexture2darray.md#class-compressedtexture2darray) and [CompressedTexture3D](class_compressedtexture3d.md#class-compressedtexture3d). Cannot be used directly, but contains all the functions necessary for accessing the derived resource types. See also [TextureLayered](class_texturelayered.md#class-texturelayered).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [String](class_string.md#class-string) | [load_path](class_compressedtexturelayered.md#class-compressedtexturelayered-property-load-path) | `""` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Error](class_@globalscope.md#enum-globalscope-error) | [load](class_compressedtexturelayered.md#class-compressedtexturelayered-method-load)(path: [String](class_string.md#class-string)) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-compressedtexturelayered-property-load-path"></a>

[String](class_string.md#class-string) **load_path** = `""` [🔗](class_compressedtexturelayered.md#class-compressedtexturelayered-property-load-path)

- [Error](class_@globalscope.md#enum-globalscope-error) **load**(path: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_load_path**()

The path the texture should be loaded from.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-compressedtexturelayered-method-load"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **load**(path: [String](class_string.md#class-string)) [🔗](class_compressedtexturelayered.md#class-compressedtexturelayered-method-load)

Loads the texture at `path`.
