> Source: https://docs.godotengine.org/en/4.7/classes/class_rdvertexattribute.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="rdvertexattribute"></a>

<a id="class-rdvertexattribute"></a>

# RDVertexAttribute

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Vertex attribute (used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice)).

<a id="description"></a>

## Description

This object is used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [binding](class_rdvertexattribute.md#class-rdvertexattribute-property-binding) | `4294967295` |
| [DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat) | [format](class_rdvertexattribute.md#class-rdvertexattribute-property-format) | `232` |
| [VertexFrequency](class_renderingdevice.md#enum-renderingdevice-vertexfrequency) | [frequency](class_rdvertexattribute.md#class-rdvertexattribute-property-frequency) | `0` |
| [int](class_int.md#class-int) | [location](class_rdvertexattribute.md#class-rdvertexattribute-property-location) | `0` |
| [int](class_int.md#class-int) | [offset](class_rdvertexattribute.md#class-rdvertexattribute-property-offset) | `0` |
| [int](class_int.md#class-int) | [stride](class_rdvertexattribute.md#class-rdvertexattribute-property-stride) | `0` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-rdvertexattribute-property-binding"></a>

[int](class_int.md#class-int) **binding** = `4294967295` [🔗](class_rdvertexattribute.md#class-rdvertexattribute-property-binding)

- void **set_binding**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_binding**()

The index of the buffer in the vertex buffer array to bind this vertex attribute. When set to `-1`, it defaults to the index of the attribute.

**Note:** You cannot mix binding explicitly assigned attributes with implicitly assigned ones (i.e. `-1`). Either all attributes must have their binding set to `-1`, or all must have explicit bindings.

---


<a id="class-rdvertexattribute-property-format"></a>

[DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat) **format** = `232` [🔗](class_rdvertexattribute.md#class-rdvertexattribute-property-format)

- void **set_format**(value: [DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat))
- [DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat) **get_format**()

The way that this attribute's data is interpreted when sent to a shader.

---


<a id="class-rdvertexattribute-property-frequency"></a>

[VertexFrequency](class_renderingdevice.md#enum-renderingdevice-vertexfrequency) **frequency** = `0` [🔗](class_rdvertexattribute.md#class-rdvertexattribute-property-frequency)

- void **set_frequency**(value: [VertexFrequency](class_renderingdevice.md#enum-renderingdevice-vertexfrequency))
- [VertexFrequency](class_renderingdevice.md#enum-renderingdevice-vertexfrequency) **get_frequency**()

The rate at which this attribute is pulled from its vertex buffer.

---


<a id="class-rdvertexattribute-property-location"></a>

[int](class_int.md#class-int) **location** = `0` [🔗](class_rdvertexattribute.md#class-rdvertexattribute-property-location)

- void **set_location**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_location**()

The location in the shader that this attribute is bound to.

---


<a id="class-rdvertexattribute-property-offset"></a>

[int](class_int.md#class-int) **offset** = `0` [🔗](class_rdvertexattribute.md#class-rdvertexattribute-property-offset)

- void **set_offset**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_offset**()

The number of bytes between the start of the vertex buffer and the first instance of this attribute.

---


<a id="class-rdvertexattribute-property-stride"></a>

[int](class_int.md#class-int) **stride** = `0` [🔗](class_rdvertexattribute.md#class-rdvertexattribute-property-stride)

- void **set_stride**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_stride**()

The number of bytes between the starts of consecutive instances of this attribute.
