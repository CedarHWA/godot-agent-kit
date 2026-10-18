> Source: https://docs.godotengine.org/en/4.7/classes/class_rdtextureformat.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="rdtextureformat"></a>

<a id="class-rdtextureformat"></a>

# RDTextureFormat

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Texture format (used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice)).

<a id="description"></a>

## Description

This object is used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [array_layers](class_rdtextureformat.md#class-rdtextureformat-property-array-layers) | `1` |
| [int](class_int.md#class-int) | [depth](class_rdtextureformat.md#class-rdtextureformat-property-depth) | `1` |
| [DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat) | [format](class_rdtextureformat.md#class-rdtextureformat-property-format) | `8` |
| [int](class_int.md#class-int) | [height](class_rdtextureformat.md#class-rdtextureformat-property-height) | `1` |
| [bool](class_bool.md#class-bool) | [is_discardable](class_rdtextureformat.md#class-rdtextureformat-property-is-discardable) | `false` |
| [bool](class_bool.md#class-bool) | [is_resolve_buffer](class_rdtextureformat.md#class-rdtextureformat-property-is-resolve-buffer) | `false` |
| [int](class_int.md#class-int) | [mipmaps](class_rdtextureformat.md#class-rdtextureformat-property-mipmaps) | `1` |
| [TextureSamples](class_renderingdevice.md#enum-renderingdevice-texturesamples) | [samples](class_rdtextureformat.md#class-rdtextureformat-property-samples) | `0` |
| [TextureType](class_renderingdevice.md#enum-renderingdevice-texturetype) | [texture_type](class_rdtextureformat.md#class-rdtextureformat-property-texture-type) | `1` |
| BitField[[TextureUsageBits](class_renderingdevice.md#enum-renderingdevice-textureusagebits)] | [usage_bits](class_rdtextureformat.md#class-rdtextureformat-property-usage-bits) | `0` |
| [int](class_int.md#class-int) | [width](class_rdtextureformat.md#class-rdtextureformat-property-width) | `1` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_shareable_format](class_rdtextureformat.md#class-rdtextureformat-method-add-shareable-format)(format: [DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat)) |
| void | [remove_shareable_format](class_rdtextureformat.md#class-rdtextureformat-method-remove-shareable-format)(format: [DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat)) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-rdtextureformat-property-array-layers"></a>

[int](class_int.md#class-int) **array_layers** = `1` [🔗](class_rdtextureformat.md#class-rdtextureformat-property-array-layers)

- void **set_array_layers**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_array_layers**()

The number of layers in the texture. Only relevant for 2D texture arrays.

---


<a id="class-rdtextureformat-property-depth"></a>

[int](class_int.md#class-int) **depth** = `1` [🔗](class_rdtextureformat.md#class-rdtextureformat-property-depth)

- void **set_depth**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_depth**()

The texture's depth (in pixels). This is always `1` for 2D textures.

---


<a id="class-rdtextureformat-property-format"></a>

[DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat) **format** = `8` [🔗](class_rdtextureformat.md#class-rdtextureformat-property-format)

- void **set_format**(value: [DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat))
- [DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat) **get_format**()

The texture's pixel data format.

---


<a id="class-rdtextureformat-property-height"></a>

[int](class_int.md#class-int) **height** = `1` [🔗](class_rdtextureformat.md#class-rdtextureformat-property-height)

- void **set_height**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_height**()

The texture's height (in pixels).

---


<a id="class-rdtextureformat-property-is-discardable"></a>

[bool](class_bool.md#class-bool) **is_discardable** = `false` [🔗](class_rdtextureformat.md#class-rdtextureformat-property-is-discardable)

- void **set_is_discardable**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_is_discardable**()

If a texture is discardable, its contents do not need to be preserved between frames. This flag is only relevant when the texture is used as target in a draw list.

This information is used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice) to figure out if a texture's contents can be discarded, eliminating unnecessary writes to memory and boosting performance.

---


<a id="class-rdtextureformat-property-is-resolve-buffer"></a>

[bool](class_bool.md#class-bool) **is_resolve_buffer** = `false` [🔗](class_rdtextureformat.md#class-rdtextureformat-property-is-resolve-buffer)

- void **set_is_resolve_buffer**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_is_resolve_buffer**()

The texture will be used as the destination of a resolve operation.

---


<a id="class-rdtextureformat-property-mipmaps"></a>

[int](class_int.md#class-int) **mipmaps** = `1` [🔗](class_rdtextureformat.md#class-rdtextureformat-property-mipmaps)

- void **set_mipmaps**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_mipmaps**()

The number of mipmaps available in the texture.

---


<a id="class-rdtextureformat-property-samples"></a>

[TextureSamples](class_renderingdevice.md#enum-renderingdevice-texturesamples) **samples** = `0` [🔗](class_rdtextureformat.md#class-rdtextureformat-property-samples)

- void **set_samples**(value: [TextureSamples](class_renderingdevice.md#enum-renderingdevice-texturesamples))
- [TextureSamples](class_renderingdevice.md#enum-renderingdevice-texturesamples) **get_samples**()

The number of samples used when sampling the texture.

---


<a id="class-rdtextureformat-property-texture-type"></a>

[TextureType](class_renderingdevice.md#enum-renderingdevice-texturetype) **texture_type** = `1` [🔗](class_rdtextureformat.md#class-rdtextureformat-property-texture-type)

- void **set_texture_type**(value: [TextureType](class_renderingdevice.md#enum-renderingdevice-texturetype))
- [TextureType](class_renderingdevice.md#enum-renderingdevice-texturetype) **get_texture_type**()

The texture type.

---


<a id="class-rdtextureformat-property-usage-bits"></a>

BitField[[TextureUsageBits](class_renderingdevice.md#enum-renderingdevice-textureusagebits)] **usage_bits** = `0` [🔗](class_rdtextureformat.md#class-rdtextureformat-property-usage-bits)

- void **set_usage_bits**(value: BitField[[TextureUsageBits](class_renderingdevice.md#enum-renderingdevice-textureusagebits)])
- BitField[[TextureUsageBits](class_renderingdevice.md#enum-renderingdevice-textureusagebits)] **get_usage_bits**()

The texture's usage bits, which determine what can be done using the texture.

---


<a id="class-rdtextureformat-property-width"></a>

[int](class_int.md#class-int) **width** = `1` [🔗](class_rdtextureformat.md#class-rdtextureformat-property-width)

- void **set_width**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_width**()

The texture's width (in pixels).

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-rdtextureformat-method-add-shareable-format"></a>

void **add_shareable_format**(format: [DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat)) [🔗](class_rdtextureformat.md#class-rdtextureformat-method-add-shareable-format)

Adds `format` as a valid format for the corresponding [RDTextureView](class_rdtextureview.md#class-rdtextureview)'s [RDTextureView.format_override](class_rdtextureview.md#class-rdtextureview-property-format-override) property. If any format is added as shareable, then the main [format](class_rdtextureformat.md#class-rdtextureformat-property-format) must also be added.

---


<a id="class-rdtextureformat-method-remove-shareable-format"></a>

void **remove_shareable_format**(format: [DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat)) [🔗](class_rdtextureformat.md#class-rdtextureformat-method-remove-shareable-format)

Removes `format` from the list of valid formats that the corresponding [RDTextureView](class_rdtextureview.md#class-rdtextureview)'s [RDTextureView.format_override](class_rdtextureview.md#class-rdtextureview-property-format-override) property can be set to.
