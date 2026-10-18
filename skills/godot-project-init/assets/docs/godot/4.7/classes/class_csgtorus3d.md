> Source: https://docs.godotengine.org/en/4.7/classes/class_csgtorus3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="csgtorus3d"></a>

<a id="class-csgtorus3d"></a>

# CSGTorus3D

**Inherits:** [CSGPrimitive3D](class_csgprimitive3d.md#class-csgprimitive3d) **<** [CSGShape3D](class_csgshape3d.md#class-csgshape3d) **<** [GeometryInstance3D](class_geometryinstance3d.md#class-geometryinstance3d) **<** [VisualInstance3D](class_visualinstance3d.md#class-visualinstance3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A CSG Torus shape.

<a id="description"></a>

## Description

This node allows you to create a torus for use with the CSG system.

**Note:** CSG nodes are intended to be used for level prototyping. Creating CSG nodes has a significant CPU cost compared to creating a [MeshInstance3D](class_meshinstance3d.md#class-meshinstance3d) with a [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh). Moving a CSG node within another CSG node also has a significant CPU cost, so it should be avoided during gameplay.

<a id="tutorials"></a>

## Tutorials

- [Prototyping levels with CSG](../tutorials/3d/csg_tools.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [inner_radius](class_csgtorus3d.md#class-csgtorus3d-property-inner-radius) | `0.5` |
| [Material](class_material.md#class-material) | [material](class_csgtorus3d.md#class-csgtorus3d-property-material) |  |
| [float](class_float.md#class-float) | [outer_radius](class_csgtorus3d.md#class-csgtorus3d-property-outer-radius) | `1.0` |
| [int](class_int.md#class-int) | [ring_sides](class_csgtorus3d.md#class-csgtorus3d-property-ring-sides) | `6` |
| [int](class_int.md#class-int) | [sides](class_csgtorus3d.md#class-csgtorus3d-property-sides) | `8` |
| [bool](class_bool.md#class-bool) | [smooth_faces](class_csgtorus3d.md#class-csgtorus3d-property-smooth-faces) | `true` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-csgtorus3d-property-inner-radius"></a>

[float](class_float.md#class-float) **inner_radius** = `0.5` [🔗](class_csgtorus3d.md#class-csgtorus3d-property-inner-radius)

- void **set_inner_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_inner_radius**()

The inner radius of the torus.

---


<a id="class-csgtorus3d-property-material"></a>

[Material](class_material.md#class-material) **material** [🔗](class_csgtorus3d.md#class-csgtorus3d-property-material)

- void **set_material**(value: [Material](class_material.md#class-material))
- [Material](class_material.md#class-material) **get_material**()

The material used to render the torus.

---


<a id="class-csgtorus3d-property-outer-radius"></a>

[float](class_float.md#class-float) **outer_radius** = `1.0` [🔗](class_csgtorus3d.md#class-csgtorus3d-property-outer-radius)

- void **set_outer_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_outer_radius**()

The outer radius of the torus.

---


<a id="class-csgtorus3d-property-ring-sides"></a>

[int](class_int.md#class-int) **ring_sides** = `6` [🔗](class_csgtorus3d.md#class-csgtorus3d-property-ring-sides)

- void **set_ring_sides**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_ring_sides**()

The number of edges each ring of the torus is constructed of.

---


<a id="class-csgtorus3d-property-sides"></a>

[int](class_int.md#class-int) **sides** = `8` [🔗](class_csgtorus3d.md#class-csgtorus3d-property-sides)

- void **set_sides**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_sides**()

The number of slices the torus is constructed of.

---


<a id="class-csgtorus3d-property-smooth-faces"></a>

[bool](class_bool.md#class-bool) **smooth_faces** = `true` [🔗](class_csgtorus3d.md#class-csgtorus3d-property-smooth-faces)

- void **set_smooth_faces**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_smooth_faces**()

If `true` the normals of the torus are set to give a smooth effect making the torus seem rounded. If `false` the torus will have a flat shaded look.
