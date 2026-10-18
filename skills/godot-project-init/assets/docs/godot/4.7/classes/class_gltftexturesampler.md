> Source: https://docs.godotengine.org/en/4.7/classes/class_gltftexturesampler.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="gltftexturesampler"></a>

<a id="class-gltftexturesampler"></a>

# GLTFTextureSampler

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Represents a glTF texture sampler

<a id="description"></a>

## Description

Represents a texture sampler as defined by the base glTF spec. Texture samplers in glTF specify how to sample data from the texture's base image, when rendering the texture on an object.

<a id="tutorials"></a>

## Tutorials

- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [mag_filter](class_gltftexturesampler.md#class-gltftexturesampler-property-mag-filter) | `9729` |
| [int](class_int.md#class-int) | [min_filter](class_gltftexturesampler.md#class-gltftexturesampler-property-min-filter) | `9987` |
| [int](class_int.md#class-int) | [wrap_s](class_gltftexturesampler.md#class-gltftexturesampler-property-wrap-s) | `10497` |
| [int](class_int.md#class-int) | [wrap_t](class_gltftexturesampler.md#class-gltftexturesampler-property-wrap-t) | `10497` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-gltftexturesampler-property-mag-filter"></a>

[int](class_int.md#class-int) **mag_filter** = `9729` [🔗](class_gltftexturesampler.md#class-gltftexturesampler-property-mag-filter)

- void **set_mag_filter**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_mag_filter**()

Texture's magnification filter, used when texture appears larger on screen than the source image.

---


<a id="class-gltftexturesampler-property-min-filter"></a>

[int](class_int.md#class-int) **min_filter** = `9987` [🔗](class_gltftexturesampler.md#class-gltftexturesampler-property-min-filter)

- void **set_min_filter**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_min_filter**()

Texture's minification filter, used when the texture appears smaller on screen than the source image.

---


<a id="class-gltftexturesampler-property-wrap-s"></a>

[int](class_int.md#class-int) **wrap_s** = `10497` [🔗](class_gltftexturesampler.md#class-gltftexturesampler-property-wrap-s)

- void **set_wrap_s**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_wrap_s**()

Wrapping mode to use for S-axis (horizontal) texture coordinates.

---


<a id="class-gltftexturesampler-property-wrap-t"></a>

[int](class_int.md#class-int) **wrap_t** = `10497` [🔗](class_gltftexturesampler.md#class-gltftexturesampler-property-wrap-t)

- void **set_wrap_t**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_wrap_t**()

Wrapping mode to use for T-axis (vertical) texture coordinates.
