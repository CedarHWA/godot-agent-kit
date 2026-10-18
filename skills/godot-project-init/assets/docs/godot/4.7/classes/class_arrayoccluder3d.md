> Source: https://docs.godotengine.org/en/4.7/classes/class_arrayoccluder3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="arrayoccluder3d"></a>

<a id="class-arrayoccluder3d"></a>

# ArrayOccluder3D

**Inherits:** [Occluder3D](class_occluder3d.md#class-occluder3d) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

3D polygon shape for use with occlusion culling in [OccluderInstance3D](class_occluderinstance3d.md#class-occluderinstance3d).

<a id="description"></a>

## Description

**ArrayOccluder3D** stores an arbitrary 3D polygon shape that can be used by the engine's occlusion culling system. This is analogous to [ArrayMesh](class_arraymesh.md#class-arraymesh), but for occluders.

See [OccluderInstance3D](class_occluderinstance3d.md#class-occluderinstance3d)'s documentation for instructions on setting up occlusion culling.

<a id="tutorials"></a>

## Tutorials

- [Occlusion culling](../tutorials/3d/occlusion_culling.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array) | [indices](class_arrayoccluder3d.md#class-arrayoccluder3d-property-indices) | `PackedInt32Array()` |
| [PackedVector3Array](class_packedvector3array.md#class-packedvector3array) | [vertices](class_arrayoccluder3d.md#class-arrayoccluder3d-property-vertices) | `PackedVector3Array()` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [set_arrays](class_arrayoccluder3d.md#class-arrayoccluder3d-method-set-arrays)(vertices: [PackedVector3Array](class_packedvector3array.md#class-packedvector3array), indices: [PackedInt32Array](class_packedint32array.md#class-packedint32array)) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-arrayoccluder3d-property-indices"></a>

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **indices** = `PackedInt32Array()` [🔗](class_arrayoccluder3d.md#class-arrayoccluder3d-property-indices)

- void **set_indices**(value: [PackedInt32Array](class_packedint32array.md#class-packedint32array))
- [PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_indices**()

The occluder's index position. Indices determine which points from the [vertices](class_arrayoccluder3d.md#class-arrayoccluder3d-property-vertices) array should be drawn, and in which order.

**Note:** The occluder is always updated after setting this value. If creating occluders procedurally, consider using [set_arrays()](class_arrayoccluder3d.md#class-arrayoccluder3d-method-set-arrays) instead to avoid updating the occluder twice when it's created.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array](class_packedint32array.md#class-packedint32array) for more details.

---


<a id="class-arrayoccluder3d-property-vertices"></a>

[PackedVector3Array](class_packedvector3array.md#class-packedvector3array) **vertices** = `PackedVector3Array()` [🔗](class_arrayoccluder3d.md#class-arrayoccluder3d-property-vertices)

- void **set_vertices**(value: [PackedVector3Array](class_packedvector3array.md#class-packedvector3array))
- [PackedVector3Array](class_packedvector3array.md#class-packedvector3array) **get_vertices**()

The occluder's vertex positions in local 3D coordinates.

**Note:** The occluder is always updated after setting this value. If creating occluders procedurally, consider using [set_arrays()](class_arrayoccluder3d.md#class-arrayoccluder3d-method-set-arrays) instead to avoid updating the occluder twice when it's created.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector3Array](class_packedvector3array.md#class-packedvector3array) for more details.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-arrayoccluder3d-method-set-arrays"></a>

void **set_arrays**(vertices: [PackedVector3Array](class_packedvector3array.md#class-packedvector3array), indices: [PackedInt32Array](class_packedint32array.md#class-packedint32array)) [🔗](class_arrayoccluder3d.md#class-arrayoccluder3d-method-set-arrays)

Sets [indices](class_arrayoccluder3d.md#class-arrayoccluder3d-property-indices) and [vertices](class_arrayoccluder3d.md#class-arrayoccluder3d-property-vertices), while updating the final occluder only once after both values are set.
