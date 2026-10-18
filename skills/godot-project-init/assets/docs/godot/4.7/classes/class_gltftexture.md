> Source: https://docs.godotengine.org/en/4.7/classes/class_gltftexture.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="gltftexture"></a>

<a id="class-gltftexture"></a>

# GLTFTexture

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

GLTFTexture represents a texture in a glTF file.

<a id="tutorials"></a>

## Tutorials

- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [sampler](class_gltftexture.md#class-gltftexture-property-sampler) | `-1` |
| [int](class_int.md#class-int) | [src_image](class_gltftexture.md#class-gltftexture-property-src-image) | `-1` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-gltftexture-property-sampler"></a>

[int](class_int.md#class-int) **sampler** = `-1` [🔗](class_gltftexture.md#class-gltftexture-property-sampler)

- void **set_sampler**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_sampler**()

ID of the texture sampler to use when sampling the image. If -1, then the default texture sampler is used (linear filtering, and repeat wrapping in both axes).

---


<a id="class-gltftexture-property-src-image"></a>

[int](class_int.md#class-int) **src_image** = `-1` [🔗](class_gltftexture.md#class-gltftexture-property-src-image)

- void **set_src_image**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_src_image**()

The index of the image associated with this texture, see [GLTFState.get_images()](class_gltfstate.md#class-gltfstate-method-get-images). If -1, then this texture does not have an image assigned.
