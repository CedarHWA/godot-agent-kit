> Source: https://docs.godotengine.org/en/4.7/classes/class_quadoccluder3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="quadoccluder3d"></a>

<a id="class-quadoccluder3d"></a>

# QuadOccluder3D

**Inherits:** [Occluder3D](class_occluder3d.md#class-occluder3d) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Flat plane shape for use with occlusion culling in [OccluderInstance3D](class_occluderinstance3d.md#class-occluderinstance3d).

<a id="description"></a>

## Description

**QuadOccluder3D** stores a flat plane shape that can be used by the engine's occlusion culling system. See also [PolygonOccluder3D](class_polygonoccluder3d.md#class-polygonoccluder3d) if you need to customize the quad's shape.

See [OccluderInstance3D](class_occluderinstance3d.md#class-occluderinstance3d)'s documentation for instructions on setting up occlusion culling.

<a id="tutorials"></a>

## Tutorials

- [Occlusion culling](../tutorials/3d/occlusion_culling.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Vector2](class_vector2.md#class-vector2) | [size](class_quadoccluder3d.md#class-quadoccluder3d-property-size) | `Vector2(1, 1)` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-quadoccluder3d-property-size"></a>

[Vector2](class_vector2.md#class-vector2) **size** = `Vector2(1, 1)` [🔗](class_quadoccluder3d.md#class-quadoccluder3d-property-size)

- void **set_size**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_size**()

The quad's size in 3D units.
