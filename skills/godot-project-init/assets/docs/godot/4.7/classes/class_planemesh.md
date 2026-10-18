> Source: https://docs.godotengine.org/en/4.7/classes/class_planemesh.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="planemesh"></a>

<a id="class-planemesh"></a>

# PlaneMesh

**Inherits:** [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh) **<** [Mesh](class_mesh.md#class-mesh) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [QuadMesh](class_quadmesh.md#class-quadmesh)

Class representing a planar [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh).

<a id="description"></a>

## Description

Class representing a planar [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh). This flat mesh does not have a thickness. By default, this mesh is aligned on the X and Z axes; this default rotation isn't suited for use with billboarded materials. For billboarded materials, change [orientation](class_planemesh.md#class-planemesh-property-orientation) to [FACE_Z](class_planemesh.md#class-planemesh-constant-face-z).

**Note:** When using a large textured **PlaneMesh** (e.g. as a floor), you may stumble upon UV jittering issues depending on the camera angle. To solve this, increase [subdivide_depth](class_planemesh.md#class-planemesh-property-subdivide-depth) and [subdivide_width](class_planemesh.md#class-planemesh-property-subdivide-width) until you no longer notice UV jittering.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Vector3](class_vector3.md#class-vector3) | [center_offset](class_planemesh.md#class-planemesh-property-center-offset) | `Vector3(0, 0, 0)` |
| [Orientation](class_planemesh.md#enum-planemesh-orientation) | [orientation](class_planemesh.md#class-planemesh-property-orientation) | `1` |
| [Vector2](class_vector2.md#class-vector2) | [size](class_planemesh.md#class-planemesh-property-size) | `Vector2(2, 2)` |
| [int](class_int.md#class-int) | [subdivide_depth](class_planemesh.md#class-planemesh-property-subdivide-depth) | `0` |
| [int](class_int.md#class-int) | [subdivide_width](class_planemesh.md#class-planemesh-property-subdivide-width) | `0` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-planemesh-orientation"></a>

enum **Orientation**: [🔗](class_planemesh.md#enum-planemesh-orientation)

<a id="class-planemesh-constant-face-x"></a>

[Orientation](class_planemesh.md#enum-planemesh-orientation) **FACE_X** = `0`

**PlaneMesh** will face the positive X-axis.

<a id="class-planemesh-constant-face-y"></a>

[Orientation](class_planemesh.md#enum-planemesh-orientation) **FACE_Y** = `1`

**PlaneMesh** will face the positive Y-axis. This matches the behavior of the **PlaneMesh** in Godot 3.x.

<a id="class-planemesh-constant-face-z"></a>

[Orientation](class_planemesh.md#enum-planemesh-orientation) **FACE_Z** = `2`

**PlaneMesh** will face the positive Z-axis. This matches the behavior of the QuadMesh in Godot 3.x.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-planemesh-property-center-offset"></a>

[Vector3](class_vector3.md#class-vector3) **center_offset** = `Vector3(0, 0, 0)` [🔗](class_planemesh.md#class-planemesh-property-center-offset)

- void **set_center_offset**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_center_offset**()

Offset of the generated plane. Useful for particles.

---


<a id="class-planemesh-property-orientation"></a>

[Orientation](class_planemesh.md#enum-planemesh-orientation) **orientation** = `1` [🔗](class_planemesh.md#class-planemesh-property-orientation)

- void **set_orientation**(value: [Orientation](class_planemesh.md#enum-planemesh-orientation))
- [Orientation](class_planemesh.md#enum-planemesh-orientation) **get_orientation**()

Direction that the **PlaneMesh** is facing.

---


<a id="class-planemesh-property-size"></a>

[Vector2](class_vector2.md#class-vector2) **size** = `Vector2(2, 2)` [🔗](class_planemesh.md#class-planemesh-property-size)

- void **set_size**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_size**()

Size of the generated plane.

---


<a id="class-planemesh-property-subdivide-depth"></a>

[int](class_int.md#class-int) **subdivide_depth** = `0` [🔗](class_planemesh.md#class-planemesh-property-subdivide-depth)

- void **set_subdivide_depth**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_subdivide_depth**()

Number of subdivision along the Z axis.

---


<a id="class-planemesh-property-subdivide-width"></a>

[int](class_int.md#class-int) **subdivide_width** = `0` [🔗](class_planemesh.md#class-planemesh-property-subdivide-width)

- void **set_subdivide_width**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_subdivide_width**()

Number of subdivision along the X axis.
