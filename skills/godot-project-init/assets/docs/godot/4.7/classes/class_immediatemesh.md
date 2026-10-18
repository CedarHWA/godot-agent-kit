> Source: https://docs.godotengine.org/en/4.7/classes/class_immediatemesh.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="immediatemesh"></a>

<a id="class-immediatemesh"></a>

# ImmediateMesh

**Inherits:** [Mesh](class_mesh.md#class-mesh) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Mesh optimized for creating geometry manually.

<a id="description"></a>

## Description

A mesh type optimized for creating geometry manually, similar to OpenGL 1.x immediate mode.

Here's a sample on how to generate a triangular face:

```gdscript
var mesh = ImmediateMesh.new()
mesh.surface_begin(Mesh.PRIMITIVE_TRIANGLES)
mesh.surface_add_vertex(Vector3.LEFT)
mesh.surface_add_vertex(Vector3.FORWARD)
mesh.surface_add_vertex(Vector3.ZERO)
mesh.surface_end()
```

```csharp
var mesh = new ImmediateMesh();
mesh.SurfaceBegin(Mesh.PrimitiveType.Triangles);
mesh.SurfaceAddVertex(Vector3.Left);
mesh.SurfaceAddVertex(Vector3.Forward);
mesh.SurfaceAddVertex(Vector3.Zero);
mesh.SurfaceEnd();
```

**Note:** Generating complex geometries with **ImmediateMesh** is highly inefficient. Instead, it is designed to generate simple geometry that changes often.

<a id="tutorials"></a>

## Tutorials

- [Using ImmediateMesh](../tutorials/3d/procedural_geometry/immediatemesh.md)

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [clear_surfaces](class_immediatemesh.md#class-immediatemesh-method-clear-surfaces)() |
| void | [surface_add_vertex](class_immediatemesh.md#class-immediatemesh-method-surface-add-vertex)(vertex: [Vector3](class_vector3.md#class-vector3)) |
| void | [surface_add_vertex_2d](class_immediatemesh.md#class-immediatemesh-method-surface-add-vertex-2d)(vertex: [Vector2](class_vector2.md#class-vector2)) |
| void | [surface_begin](class_immediatemesh.md#class-immediatemesh-method-surface-begin)(primitive: [PrimitiveType](class_mesh.md#enum-mesh-primitivetype), material: [Material](class_material.md#class-material) = null) |
| void | [surface_end](class_immediatemesh.md#class-immediatemesh-method-surface-end)() |
| void | [surface_set_color](class_immediatemesh.md#class-immediatemesh-method-surface-set-color)(color: [Color](class_color.md#class-color)) |
| void | [surface_set_normal](class_immediatemesh.md#class-immediatemesh-method-surface-set-normal)(normal: [Vector3](class_vector3.md#class-vector3)) |
| void | [surface_set_tangent](class_immediatemesh.md#class-immediatemesh-method-surface-set-tangent)(tangent: [Plane](class_plane.md#class-plane)) |
| void | [surface_set_uv](class_immediatemesh.md#class-immediatemesh-method-surface-set-uv)(uv: [Vector2](class_vector2.md#class-vector2)) |
| void | [surface_set_uv2](class_immediatemesh.md#class-immediatemesh-method-surface-set-uv2)(uv2: [Vector2](class_vector2.md#class-vector2)) |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-immediatemesh-method-clear-surfaces"></a>

void **clear_surfaces**() [🔗](class_immediatemesh.md#class-immediatemesh-method-clear-surfaces)

Clear all surfaces.

---


<a id="class-immediatemesh-method-surface-add-vertex"></a>

void **surface_add_vertex**(vertex: [Vector3](class_vector3.md#class-vector3)) [🔗](class_immediatemesh.md#class-immediatemesh-method-surface-add-vertex)

Add a 3D vertex using the current attributes previously set.

---


<a id="class-immediatemesh-method-surface-add-vertex-2d"></a>

void **surface_add_vertex_2d**(vertex: [Vector2](class_vector2.md#class-vector2)) [🔗](class_immediatemesh.md#class-immediatemesh-method-surface-add-vertex-2d)

Add a 2D vertex using the current attributes previously set.

---


<a id="class-immediatemesh-method-surface-begin"></a>

void **surface_begin**(primitive: [PrimitiveType](class_mesh.md#enum-mesh-primitivetype), material: [Material](class_material.md#class-material) = null) [🔗](class_immediatemesh.md#class-immediatemesh-method-surface-begin)

Begin a new surface.

---


<a id="class-immediatemesh-method-surface-end"></a>

void **surface_end**() [🔗](class_immediatemesh.md#class-immediatemesh-method-surface-end)

End and commit current surface. Note that surface being created will not be visible until this function is called.

---


<a id="class-immediatemesh-method-surface-set-color"></a>

void **surface_set_color**(color: [Color](class_color.md#class-color)) [🔗](class_immediatemesh.md#class-immediatemesh-method-surface-set-color)

Set the color attribute that will be pushed with the next vertex.

---


<a id="class-immediatemesh-method-surface-set-normal"></a>

void **surface_set_normal**(normal: [Vector3](class_vector3.md#class-vector3)) [🔗](class_immediatemesh.md#class-immediatemesh-method-surface-set-normal)

Set the normal attribute that will be pushed with the next vertex.

---


<a id="class-immediatemesh-method-surface-set-tangent"></a>

void **surface_set_tangent**(tangent: [Plane](class_plane.md#class-plane)) [🔗](class_immediatemesh.md#class-immediatemesh-method-surface-set-tangent)

Set the tangent attribute that will be pushed with the next vertex.

**Note:** Even though `tangent` is a [Plane](class_plane.md#class-plane), it does not directly represent the tangent plane. Its [Plane.x](class_plane.md#class-plane-property-x), [Plane.y](class_plane.md#class-plane-property-y), and [Plane.z](class_plane.md#class-plane-property-z) represent the tangent vector and [Plane.d](class_plane.md#class-plane-property-d) should be either `-1` or `1`. See also [Mesh.ARRAY_TANGENT](class_mesh.md#class-mesh-constant-array-tangent).

---


<a id="class-immediatemesh-method-surface-set-uv"></a>

void **surface_set_uv**(uv: [Vector2](class_vector2.md#class-vector2)) [🔗](class_immediatemesh.md#class-immediatemesh-method-surface-set-uv)

Set the UV attribute that will be pushed with the next vertex.

---


<a id="class-immediatemesh-method-surface-set-uv2"></a>

void **surface_set_uv2**(uv2: [Vector2](class_vector2.md#class-vector2)) [🔗](class_immediatemesh.md#class-immediatemesh-method-surface-set-uv2)

Set the UV2 attribute that will be pushed with the next vertex.
