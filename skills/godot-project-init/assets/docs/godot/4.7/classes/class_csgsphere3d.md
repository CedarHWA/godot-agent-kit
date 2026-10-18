> Source: https://docs.godotengine.org/en/4.7/classes/class_csgsphere3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="csgsphere3d"></a>

<a id="class-csgsphere3d"></a>

# CSGSphere3D

**Inherits:** [CSGPrimitive3D](class_csgprimitive3d.md#class-csgprimitive3d) **<** [CSGShape3D](class_csgshape3d.md#class-csgshape3d) **<** [GeometryInstance3D](class_geometryinstance3d.md#class-geometryinstance3d) **<** [VisualInstance3D](class_visualinstance3d.md#class-visualinstance3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A CSG Sphere shape.

<a id="description"></a>

## Description

This node allows you to create a sphere for use with the CSG system.

**Note:** CSG nodes are intended to be used for level prototyping. Creating CSG nodes has a significant CPU cost compared to creating a [MeshInstance3D](class_meshinstance3d.md#class-meshinstance3d) with a [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh). Moving a CSG node within another CSG node also has a significant CPU cost, so it should be avoided during gameplay.

<a id="tutorials"></a>

## Tutorials

- [Prototyping levels with CSG](../tutorials/3d/csg_tools.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Material](class_material.md#class-material) | [material](class_csgsphere3d.md#class-csgsphere3d-property-material) |  |
| [int](class_int.md#class-int) | [radial_segments](class_csgsphere3d.md#class-csgsphere3d-property-radial-segments) | `12` |
| [float](class_float.md#class-float) | [radius](class_csgsphere3d.md#class-csgsphere3d-property-radius) | `0.5` |
| [int](class_int.md#class-int) | [rings](class_csgsphere3d.md#class-csgsphere3d-property-rings) | `6` |
| [bool](class_bool.md#class-bool) | [smooth_faces](class_csgsphere3d.md#class-csgsphere3d-property-smooth-faces) | `true` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-csgsphere3d-property-material"></a>

[Material](class_material.md#class-material) **material** [🔗](class_csgsphere3d.md#class-csgsphere3d-property-material)

- void **set_material**(value: [Material](class_material.md#class-material))
- [Material](class_material.md#class-material) **get_material**()

The material used to render the sphere.

---


<a id="class-csgsphere3d-property-radial-segments"></a>

[int](class_int.md#class-int) **radial_segments** = `12` [🔗](class_csgsphere3d.md#class-csgsphere3d-property-radial-segments)

- void **set_radial_segments**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_radial_segments**()

Number of vertical slices for the sphere.

---


<a id="class-csgsphere3d-property-radius"></a>

[float](class_float.md#class-float) **radius** = `0.5` [🔗](class_csgsphere3d.md#class-csgsphere3d-property-radius)

- void **set_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_radius**()

Radius of the sphere.

---


<a id="class-csgsphere3d-property-rings"></a>

[int](class_int.md#class-int) **rings** = `6` [🔗](class_csgsphere3d.md#class-csgsphere3d-property-rings)

- void **set_rings**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_rings**()

Number of horizontal slices for the sphere.

---


<a id="class-csgsphere3d-property-smooth-faces"></a>

[bool](class_bool.md#class-bool) **smooth_faces** = `true` [🔗](class_csgsphere3d.md#class-csgsphere3d-property-smooth-faces)

- void **set_smooth_faces**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_smooth_faces**()

If `true` the normals of the sphere are set to give a smooth effect making the sphere seem rounded. If `false` the sphere will have a flat shaded look.
