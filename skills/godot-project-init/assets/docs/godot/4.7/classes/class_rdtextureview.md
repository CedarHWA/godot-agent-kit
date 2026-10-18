> Source: https://docs.godotengine.org/en/4.7/classes/class_rdtextureview.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="rdtextureview"></a>

<a id="class-rdtextureview"></a>

# RDTextureView

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Texture view (used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice)).

<a id="description"></a>

## Description

This object is used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat) | [format_override](class_rdtextureview.md#class-rdtextureview-property-format-override) | `232` |
| [TextureSwizzle](class_renderingdevice.md#enum-renderingdevice-textureswizzle) | [swizzle_a](class_rdtextureview.md#class-rdtextureview-property-swizzle-a) | `6` |
| [TextureSwizzle](class_renderingdevice.md#enum-renderingdevice-textureswizzle) | [swizzle_b](class_rdtextureview.md#class-rdtextureview-property-swizzle-b) | `5` |
| [TextureSwizzle](class_renderingdevice.md#enum-renderingdevice-textureswizzle) | [swizzle_g](class_rdtextureview.md#class-rdtextureview-property-swizzle-g) | `4` |
| [TextureSwizzle](class_renderingdevice.md#enum-renderingdevice-textureswizzle) | [swizzle_r](class_rdtextureview.md#class-rdtextureview-property-swizzle-r) | `3` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-rdtextureview-property-format-override"></a>

[DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat) **format_override** = `232` [🔗](class_rdtextureview.md#class-rdtextureview-property-format-override)

- void **set_format_override**(value: [DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat))
- [DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat) **get_format_override**()

Optional override for the data format to return sampled values in. The corresponding [RDTextureFormat](class_rdtextureformat.md#class-rdtextureformat) must have had this added as a shareable format. The default value of [RenderingDevice.DATA_FORMAT_MAX](class_renderingdevice.md#class-renderingdevice-constant-data-format-max) does not override the format.

---


<a id="class-rdtextureview-property-swizzle-a"></a>

[TextureSwizzle](class_renderingdevice.md#enum-renderingdevice-textureswizzle) **swizzle_a** = `6` [🔗](class_rdtextureview.md#class-rdtextureview-property-swizzle-a)

- void **set_swizzle_a**(value: [TextureSwizzle](class_renderingdevice.md#enum-renderingdevice-textureswizzle))
- [TextureSwizzle](class_renderingdevice.md#enum-renderingdevice-textureswizzle) **get_swizzle_a**()

The channel to sample when sampling the alpha channel.

---


<a id="class-rdtextureview-property-swizzle-b"></a>

[TextureSwizzle](class_renderingdevice.md#enum-renderingdevice-textureswizzle) **swizzle_b** = `5` [🔗](class_rdtextureview.md#class-rdtextureview-property-swizzle-b)

- void **set_swizzle_b**(value: [TextureSwizzle](class_renderingdevice.md#enum-renderingdevice-textureswizzle))
- [TextureSwizzle](class_renderingdevice.md#enum-renderingdevice-textureswizzle) **get_swizzle_b**()

The channel to sample when sampling the blue color channel.

---


<a id="class-rdtextureview-property-swizzle-g"></a>

[TextureSwizzle](class_renderingdevice.md#enum-renderingdevice-textureswizzle) **swizzle_g** = `4` [🔗](class_rdtextureview.md#class-rdtextureview-property-swizzle-g)

- void **set_swizzle_g**(value: [TextureSwizzle](class_renderingdevice.md#enum-renderingdevice-textureswizzle))
- [TextureSwizzle](class_renderingdevice.md#enum-renderingdevice-textureswizzle) **get_swizzle_g**()

The channel to sample when sampling the green color channel.

---


<a id="class-rdtextureview-property-swizzle-r"></a>

[TextureSwizzle](class_renderingdevice.md#enum-renderingdevice-textureswizzle) **swizzle_r** = `3` [🔗](class_rdtextureview.md#class-rdtextureview-property-swizzle-r)

- void **set_swizzle_r**(value: [TextureSwizzle](class_renderingdevice.md#enum-renderingdevice-textureswizzle))
- [TextureSwizzle](class_renderingdevice.md#enum-renderingdevice-textureswizzle) **get_swizzle_r**()

The channel to sample when sampling the red color channel.
