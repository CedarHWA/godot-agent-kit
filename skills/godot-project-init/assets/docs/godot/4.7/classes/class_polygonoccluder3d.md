> Source: https://docs.godotengine.org/en/4.7/classes/class_polygonoccluder3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="polygonoccluder3d"></a>

<a id="class-polygonoccluder3d"></a>

# PolygonOccluder3D

**Inherits:** [Occluder3D](class_occluder3d.md#class-occluder3d) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Flat 2D polygon shape for use with occlusion culling in [OccluderInstance3D](class_occluderinstance3d.md#class-occluderinstance3d).

<a id="description"></a>

## Description

**PolygonOccluder3D** stores a polygon shape that can be used by the engine's occlusion culling system. When an [OccluderInstance3D](class_occluderinstance3d.md#class-occluderinstance3d) with a **PolygonOccluder3D** is selected in the editor, an editor will appear at the top of the 3D viewport so you can add/remove points. All points must be placed on the same 2D plane, which means it is not possible to create arbitrary 3D shapes with a single **PolygonOccluder3D**. To use arbitrary 3D shapes as occluders, use [ArrayOccluder3D](class_arrayoccluder3d.md#class-arrayoccluder3d) or [OccluderInstance3D](class_occluderinstance3d.md#class-occluderinstance3d)'s baking feature instead.

See [OccluderInstance3D](class_occluderinstance3d.md#class-occluderinstance3d)'s documentation for instructions on setting up occlusion culling.

<a id="tutorials"></a>

## Tutorials

- [Occlusion culling](../tutorials/3d/occlusion_culling.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) | [polygon](class_polygonoccluder3d.md#class-polygonoccluder3d-property-polygon) | `PackedVector2Array()` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-polygonoccluder3d-property-polygon"></a>

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **polygon** = `PackedVector2Array()` [🔗](class_polygonoccluder3d.md#class-polygonoccluder3d-property-polygon)

- void **set_polygon**(value: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array))
- [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **get_polygon**()

The polygon to use for occlusion culling. The polygon can be convex or concave, but it should have as few points as possible to maximize performance.

The polygon must *not* have intersecting lines. Otherwise, triangulation will fail (with an error message printed).

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) for more details.
