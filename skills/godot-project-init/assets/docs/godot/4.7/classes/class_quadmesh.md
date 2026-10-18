> Source: https://docs.godotengine.org/en/4.7/classes/class_quadmesh.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="quadmesh"></a>

<a id="class-quadmesh"></a>

# QuadMesh

**Inherits:** [PlaneMesh](class_planemesh.md#class-planemesh) **<** [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh) **<** [Mesh](class_mesh.md#class-mesh) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Class representing a square mesh facing the camera.

<a id="description"></a>

## Description

Class representing a square [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh). This flat mesh does not have a thickness. By default, this mesh is aligned on the X and Y axes; this rotation is more suited for use with billboarded materials. A **QuadMesh** is equivalent to a [PlaneMesh](class_planemesh.md#class-planemesh) except its default [PlaneMesh.orientation](class_planemesh.md#class-planemesh-property-orientation) is [PlaneMesh.FACE_Z](class_planemesh.md#class-planemesh-constant-face-z).

<a id="tutorials"></a>

## Tutorials

- [GUI in 3D Viewport Demo](https://godotengine.org/asset-library/asset/2807)
- [2D in 3D Viewport Demo](https://godotengine.org/asset-library/asset/2803)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Orientation](class_planemesh.md#enum-planemesh-orientation) | orientation | `2` (overrides [PlaneMesh](class_planemesh.md#class-planemesh-property-orientation)) |
| [Vector2](class_vector2.md#class-vector2) | size | `Vector2(1, 1)` (overrides [PlaneMesh](class_planemesh.md#class-planemesh-property-size)) |
