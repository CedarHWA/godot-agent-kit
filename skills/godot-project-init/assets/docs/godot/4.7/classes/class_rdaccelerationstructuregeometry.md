> Source: https://docs.godotengine.org/en/4.7/classes/class_rdaccelerationstructuregeometry.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="rdaccelerationstructuregeometry"></a>

<a id="class-rdaccelerationstructuregeometry"></a>

# RDAccelerationStructureGeometry

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Acceleration structure geometry (used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice)).

<a id="description"></a>

## Description

**RDAccelerationStructureGeometry** describes a set of triangles used as raytracing geometry in the [RenderingDevice.blas_create()](class_renderingdevice.md#class-renderingdevice-method-blas-create) method.

The geometry is always in triangle list form, either indexed or non-indexed. Triangle strips are not supported.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| BitField[[AccelerationStructureGeometryFlagBits](class_renderingdevice.md#enum-renderingdevice-accelerationstructuregeometryflagbits)] | [flags](class_rdaccelerationstructuregeometry.md#class-rdaccelerationstructuregeometry-property-flags) | `0` |
| [RID](class_rid.md#class-rid) | [index_buffer](class_rdaccelerationstructuregeometry.md#class-rdaccelerationstructuregeometry-property-index-buffer) | `RID()` |
| [int](class_int.md#class-int) | [index_count](class_rdaccelerationstructuregeometry.md#class-rdaccelerationstructuregeometry-property-index-count) | `0` |
| [int](class_int.md#class-int) | [index_offset](class_rdaccelerationstructuregeometry.md#class-rdaccelerationstructuregeometry-property-index-offset) | `0` |
| [RID](class_rid.md#class-rid) | [vertex_buffer](class_rdaccelerationstructuregeometry.md#class-rdaccelerationstructuregeometry-property-vertex-buffer) | `RID()` |
| [int](class_int.md#class-int) | [vertex_count](class_rdaccelerationstructuregeometry.md#class-rdaccelerationstructuregeometry-property-vertex-count) | `0` |
| [DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat) | [vertex_format](class_rdaccelerationstructuregeometry.md#class-rdaccelerationstructuregeometry-property-vertex-format) | `232` |
| [int](class_int.md#class-int) | [vertex_offset](class_rdaccelerationstructuregeometry.md#class-rdaccelerationstructuregeometry-property-vertex-offset) | `0` |
| [int](class_int.md#class-int) | [vertex_stride](class_rdaccelerationstructuregeometry.md#class-rdaccelerationstructuregeometry-property-vertex-stride) | `0` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-rdaccelerationstructuregeometry-property-flags"></a>

BitField[[AccelerationStructureGeometryFlagBits](class_renderingdevice.md#enum-renderingdevice-accelerationstructuregeometryflagbits)] **flags** = `0` [🔗](class_rdaccelerationstructuregeometry.md#class-rdaccelerationstructuregeometry-property-flags)

- void **set_flags**(value: BitField[[AccelerationStructureGeometryFlagBits](class_renderingdevice.md#enum-renderingdevice-accelerationstructuregeometryflagbits)])
- BitField[[AccelerationStructureGeometryFlagBits](class_renderingdevice.md#enum-renderingdevice-accelerationstructuregeometryflagbits)] **get_flags**()

Flags for the geometry.

---


<a id="class-rdaccelerationstructuregeometry-property-index-buffer"></a>

[RID](class_rid.md#class-rid) **index_buffer** = `RID()` [🔗](class_rdaccelerationstructuregeometry.md#class-rdaccelerationstructuregeometry-property-index-buffer)

- void **set_index_buffer**(value: [RID](class_rid.md#class-rid))
- [RID](class_rid.md#class-rid) **get_index_buffer**()

Buffer containing vertex indices. If `null`, triangles are non-indexed.

---


<a id="class-rdaccelerationstructuregeometry-property-index-count"></a>

[int](class_int.md#class-int) **index_count** = `0` [🔗](class_rdaccelerationstructuregeometry.md#class-rdaccelerationstructuregeometry-property-index-count)

- void **set_index_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_index_count**()

Number of indices used by this geometry in [index_buffer](class_rdaccelerationstructuregeometry.md#class-rdaccelerationstructuregeometry-property-index-buffer).

---


<a id="class-rdaccelerationstructuregeometry-property-index-offset"></a>

[int](class_int.md#class-int) **index_offset** = `0` [🔗](class_rdaccelerationstructuregeometry.md#class-rdaccelerationstructuregeometry-property-index-offset)

- void **set_index_offset**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_index_offset**()

Byte offset of the first index in [index_buffer](class_rdaccelerationstructuregeometry.md#class-rdaccelerationstructuregeometry-property-index-buffer).

---


<a id="class-rdaccelerationstructuregeometry-property-vertex-buffer"></a>

[RID](class_rid.md#class-rid) **vertex_buffer** = `RID()` [🔗](class_rdaccelerationstructuregeometry.md#class-rdaccelerationstructuregeometry-property-vertex-buffer)

- void **set_vertex_buffer**(value: [RID](class_rid.md#class-rid))
- [RID](class_rid.md#class-rid) **get_vertex_buffer**()

Buffer containing vertices.

---


<a id="class-rdaccelerationstructuregeometry-property-vertex-count"></a>

[int](class_int.md#class-int) **vertex_count** = `0` [🔗](class_rdaccelerationstructuregeometry.md#class-rdaccelerationstructuregeometry-property-vertex-count)

- void **set_vertex_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_vertex_count**()

Number of vertices used by this geometry in [vertex_buffer](class_rdaccelerationstructuregeometry.md#class-rdaccelerationstructuregeometry-property-vertex-buffer).

---


<a id="class-rdaccelerationstructuregeometry-property-vertex-format"></a>

[DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat) **vertex_format** = `232` [🔗](class_rdaccelerationstructuregeometry.md#class-rdaccelerationstructuregeometry-property-vertex-format)

- void **set_vertex_format**(value: [DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat))
- [DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat) **get_vertex_format**()

Format of the vertices in [vertex_buffer](class_rdaccelerationstructuregeometry.md#class-rdaccelerationstructuregeometry-property-vertex-buffer).

---


<a id="class-rdaccelerationstructuregeometry-property-vertex-offset"></a>

[int](class_int.md#class-int) **vertex_offset** = `0` [🔗](class_rdaccelerationstructuregeometry.md#class-rdaccelerationstructuregeometry-property-vertex-offset)

- void **set_vertex_offset**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_vertex_offset**()

Byte offset of the first vertex in [vertex_buffer](class_rdaccelerationstructuregeometry.md#class-rdaccelerationstructuregeometry-property-vertex-buffer).

---


<a id="class-rdaccelerationstructuregeometry-property-vertex-stride"></a>

[int](class_int.md#class-int) **vertex_stride** = `0` [🔗](class_rdaccelerationstructuregeometry.md#class-rdaccelerationstructuregeometry-property-vertex-stride)

- void **set_vertex_stride**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_vertex_stride**()

Number of bytes between each vertex in [vertex_buffer](class_rdaccelerationstructuregeometry.md#class-rdaccelerationstructuregeometry-property-vertex-buffer).
