> Source: https://docs.godotengine.org/en/4.7/classes/class_boxoccluder3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="boxoccluder3d"></a>

<a id="class-boxoccluder3d"></a>

# BoxOccluder3D

**Inherits:** [Occluder3D](class_occluder3d.md#class-occluder3d) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Cuboid shape for use with occlusion culling in [OccluderInstance3D](class_occluderinstance3d.md#class-occluderinstance3d).

<a id="description"></a>

## Description

**BoxOccluder3D** stores a cuboid shape that can be used by the engine's occlusion culling system.

See [OccluderInstance3D](class_occluderinstance3d.md#class-occluderinstance3d)'s documentation for instructions on setting up occlusion culling.

<a id="tutorials"></a>

## Tutorials

- [Occlusion culling](../tutorials/3d/occlusion_culling.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Vector3](class_vector3.md#class-vector3) | [size](class_boxoccluder3d.md#class-boxoccluder3d-property-size) | `Vector3(1, 1, 1)` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-boxoccluder3d-property-size"></a>

[Vector3](class_vector3.md#class-vector3) **size** = `Vector3(1, 1, 1)` [🔗](class_boxoccluder3d.md#class-boxoccluder3d-property-size)

- void **set_size**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_size**()

The box's size in 3D units.
