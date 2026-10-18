> Source: https://docs.godotengine.org/en/4.7/classes/class_csgcylinder3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="csgcylinder3d"></a>

<a id="class-csgcylinder3d"></a>

# CSGCylinder3D

**Inherits:** [CSGPrimitive3D](class_csgprimitive3d.md#class-csgprimitive3d) **<** [CSGShape3D](class_csgshape3d.md#class-csgshape3d) **<** [GeometryInstance3D](class_geometryinstance3d.md#class-geometryinstance3d) **<** [VisualInstance3D](class_visualinstance3d.md#class-visualinstance3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A CSG Cylinder shape.

<a id="description"></a>

## Description

This node allows you to create a cylinder (or cone) for use with the CSG system.

**Note:** CSG nodes are intended to be used for level prototyping. Creating CSG nodes has a significant CPU cost compared to creating a [MeshInstance3D](class_meshinstance3d.md#class-meshinstance3d) with a [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh). Moving a CSG node within another CSG node also has a significant CPU cost, so it should be avoided during gameplay.

<a id="tutorials"></a>

## Tutorials

- [Prototyping levels with CSG](../tutorials/3d/csg_tools.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [cone](class_csgcylinder3d.md#class-csgcylinder3d-property-cone) | `false` |
| [float](class_float.md#class-float) | [height](class_csgcylinder3d.md#class-csgcylinder3d-property-height) | `2.0` |
| [Material](class_material.md#class-material) | [material](class_csgcylinder3d.md#class-csgcylinder3d-property-material) |  |
| [float](class_float.md#class-float) | [radius](class_csgcylinder3d.md#class-csgcylinder3d-property-radius) | `0.5` |
| [int](class_int.md#class-int) | [sides](class_csgcylinder3d.md#class-csgcylinder3d-property-sides) | `8` |
| [bool](class_bool.md#class-bool) | [smooth_faces](class_csgcylinder3d.md#class-csgcylinder3d-property-smooth-faces) | `true` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-csgcylinder3d-property-cone"></a>

[bool](class_bool.md#class-bool) **cone** = `false` [🔗](class_csgcylinder3d.md#class-csgcylinder3d-property-cone)

- void **set_cone**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_cone**()

If `true` a cone is created, the [radius](class_csgcylinder3d.md#class-csgcylinder3d-property-radius) will only apply to one side.

---


<a id="class-csgcylinder3d-property-height"></a>

[float](class_float.md#class-float) **height** = `2.0` [🔗](class_csgcylinder3d.md#class-csgcylinder3d-property-height)

- void **set_height**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_height**()

The height of the cylinder.

---


<a id="class-csgcylinder3d-property-material"></a>

[Material](class_material.md#class-material) **material** [🔗](class_csgcylinder3d.md#class-csgcylinder3d-property-material)

- void **set_material**(value: [Material](class_material.md#class-material))
- [Material](class_material.md#class-material) **get_material**()

The material used to render the cylinder.

---


<a id="class-csgcylinder3d-property-radius"></a>

[float](class_float.md#class-float) **radius** = `0.5` [🔗](class_csgcylinder3d.md#class-csgcylinder3d-property-radius)

- void **set_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_radius**()

The radius of the cylinder.

---


<a id="class-csgcylinder3d-property-sides"></a>

[int](class_int.md#class-int) **sides** = `8` [🔗](class_csgcylinder3d.md#class-csgcylinder3d-property-sides)

- void **set_sides**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_sides**()

The number of sides of the cylinder, the higher this number the more detail there will be in the cylinder.

---


<a id="class-csgcylinder3d-property-smooth-faces"></a>

[bool](class_bool.md#class-bool) **smooth_faces** = `true` [🔗](class_csgcylinder3d.md#class-csgcylinder3d-property-smooth-faces)

- void **set_smooth_faces**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_smooth_faces**()

If `true` the normals of the cylinder are set to give a smooth effect making the cylinder seem rounded. If `false` the cylinder will have a flat shaded look.
