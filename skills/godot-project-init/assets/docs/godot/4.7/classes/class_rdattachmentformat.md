> Source: https://docs.godotengine.org/en/4.7/classes/class_rdattachmentformat.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="rdattachmentformat"></a>

<a id="class-rdattachmentformat"></a>

# RDAttachmentFormat

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Attachment format (used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice)).

<a id="description"></a>

## Description

This object is used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat) | [format](class_rdattachmentformat.md#class-rdattachmentformat-property-format) | `36` |
| [TextureSamples](class_renderingdevice.md#enum-renderingdevice-texturesamples) | [samples](class_rdattachmentformat.md#class-rdattachmentformat-property-samples) | `0` |
| [int](class_int.md#class-int) | [usage_flags](class_rdattachmentformat.md#class-rdattachmentformat-property-usage-flags) | `0` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-rdattachmentformat-property-format"></a>

[DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat) **format** = `36` [🔗](class_rdattachmentformat.md#class-rdattachmentformat-property-format)

- void **set_format**(value: [DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat))
- [DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat) **get_format**()

The attachment's data format.

---


<a id="class-rdattachmentformat-property-samples"></a>

[TextureSamples](class_renderingdevice.md#enum-renderingdevice-texturesamples) **samples** = `0` [🔗](class_rdattachmentformat.md#class-rdattachmentformat-property-samples)

- void **set_samples**(value: [TextureSamples](class_renderingdevice.md#enum-renderingdevice-texturesamples))
- [TextureSamples](class_renderingdevice.md#enum-renderingdevice-texturesamples) **get_samples**()

The number of samples used when sampling the attachment.

---


<a id="class-rdattachmentformat-property-usage-flags"></a>

[int](class_int.md#class-int) **usage_flags** = `0` [🔗](class_rdattachmentformat.md#class-rdattachmentformat-property-usage-flags)

- void **set_usage_flags**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_usage_flags**()

The attachment's usage flags, which determine what can be done with it.
