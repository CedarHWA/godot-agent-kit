> Source: https://docs.godotengine.org/en/4.7/classes/class_sphereoccluder3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="sphereoccluder3d"></a>

<a id="class-sphereoccluder3d"></a>

# SphereOccluder3D

**Inherits:** [Occluder3D](class_occluder3d.md#class-occluder3d) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Spherical shape for use with occlusion culling in [OccluderInstance3D](class_occluderinstance3d.md#class-occluderinstance3d).

<a id="description"></a>

## Description

**SphereOccluder3D** stores a sphere shape that can be used by the engine's occlusion culling system.

See [OccluderInstance3D](class_occluderinstance3d.md#class-occluderinstance3d)'s documentation for instructions on setting up occlusion culling.

<a id="tutorials"></a>

## Tutorials

- [Occlusion culling](../tutorials/3d/occlusion_culling.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [radius](class_sphereoccluder3d.md#class-sphereoccluder3d-property-radius) | `1.0` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-sphereoccluder3d-property-radius"></a>

[float](class_float.md#class-float) **radius** = `1.0` [🔗](class_sphereoccluder3d.md#class-sphereoccluder3d-property-radius)

- void **set_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_radius**()

The sphere's radius in 3D units.
