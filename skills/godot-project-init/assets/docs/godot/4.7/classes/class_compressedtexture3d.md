> Source: https://docs.godotengine.org/en/4.7/classes/class_compressedtexture3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="compressedtexture3d"></a>

<a id="class-compressedtexture3d"></a>

# CompressedTexture3D

**Inherits:** [Texture3D](class_texture3d.md#class-texture3d) **<** [Texture](class_texture.md#class-texture) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Texture with 3 dimensions, optionally compressed.

<a id="description"></a>

## Description

**CompressedTexture3D** is the VRAM-compressed counterpart of [ImageTexture3D](class_imagetexture3d.md#class-imagetexture3d). The file extension for **CompressedTexture3D** files is `.ctex3d`. This file format is internal to Godot; it is created by importing other image formats with the import system.

**CompressedTexture3D** uses VRAM compression, which allows to reduce memory usage on the GPU when rendering the texture. This also improves loading times, as VRAM-compressed textures are faster to load compared to textures using lossless compression. VRAM compression can exhibit noticeable artifacts and is intended to be used for 3D rendering, not 2D.

See [Texture3D](class_texture3d.md#class-texture3d) for a general description of 3D textures.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [String](class_string.md#class-string) | [load_path](class_compressedtexture3d.md#class-compressedtexture3d-property-load-path) | `""` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Error](class_@globalscope.md#enum-globalscope-error) | [load](class_compressedtexture3d.md#class-compressedtexture3d-method-load)(path: [String](class_string.md#class-string)) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-compressedtexture3d-property-load-path"></a>

[String](class_string.md#class-string) **load_path** = `""` [🔗](class_compressedtexture3d.md#class-compressedtexture3d-property-load-path)

- [Error](class_@globalscope.md#enum-globalscope-error) **load**(path: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_load_path**()

The **CompressedTexture3D**'s file path to a `.ctex3d` file.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-compressedtexture3d-method-load"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **load**(path: [String](class_string.md#class-string)) [🔗](class_compressedtexture3d.md#class-compressedtexture3d-method-load)

Loads the texture from the specified `path`.
