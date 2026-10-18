> Source: https://docs.godotengine.org/en/4.7/classes/class_prismmesh.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="prismmesh"></a>

<a id="class-prismmesh"></a>

# PrismMesh

**Inherits:** [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh) **<** [Mesh](class_mesh.md#class-mesh) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Class representing a prism-shaped [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh).

<a id="description"></a>

## Description

Class representing a prism-shaped [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [left_to_right](class_prismmesh.md#class-prismmesh-property-left-to-right) | `0.5` |
| [Vector3](class_vector3.md#class-vector3) | [size](class_prismmesh.md#class-prismmesh-property-size) | `Vector3(1, 1, 1)` |
| [int](class_int.md#class-int) | [subdivide_depth](class_prismmesh.md#class-prismmesh-property-subdivide-depth) | `0` |
| [int](class_int.md#class-int) | [subdivide_height](class_prismmesh.md#class-prismmesh-property-subdivide-height) | `0` |
| [int](class_int.md#class-int) | [subdivide_width](class_prismmesh.md#class-prismmesh-property-subdivide-width) | `0` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-prismmesh-property-left-to-right"></a>

[float](class_float.md#class-float) **left_to_right** = `0.5` [🔗](class_prismmesh.md#class-prismmesh-property-left-to-right)

- void **set_left_to_right**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_left_to_right**()

Displacement of the upper edge along the X axis. 0.0 positions edge straight above the bottom-left edge.

---


<a id="class-prismmesh-property-size"></a>

[Vector3](class_vector3.md#class-vector3) **size** = `Vector3(1, 1, 1)` [🔗](class_prismmesh.md#class-prismmesh-property-size)

- void **set_size**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_size**()

Size of the prism.

---


<a id="class-prismmesh-property-subdivide-depth"></a>

[int](class_int.md#class-int) **subdivide_depth** = `0` [🔗](class_prismmesh.md#class-prismmesh-property-subdivide-depth)

- void **set_subdivide_depth**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_subdivide_depth**()

Number of added edge loops along the Z axis.

---


<a id="class-prismmesh-property-subdivide-height"></a>

[int](class_int.md#class-int) **subdivide_height** = `0` [🔗](class_prismmesh.md#class-prismmesh-property-subdivide-height)

- void **set_subdivide_height**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_subdivide_height**()

Number of added edge loops along the Y axis.

---


<a id="class-prismmesh-property-subdivide-width"></a>

[int](class_int.md#class-int) **subdivide_width** = `0` [🔗](class_prismmesh.md#class-prismmesh-property-subdivide-width)

- void **set_subdivide_width**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_subdivide_width**()

Number of added edge loops along the X axis.
