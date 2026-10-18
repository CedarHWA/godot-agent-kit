> Source: https://docs.godotengine.org/en/4.7/classes/class_primitivemesh.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="primitivemesh"></a>

<a id="class-primitivemesh"></a>

# PrimitiveMesh

**Inherits:** [Mesh](class_mesh.md#class-mesh) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [BoxMesh](class_boxmesh.md#class-boxmesh), [CapsuleMesh](class_capsulemesh.md#class-capsulemesh), [CylinderMesh](class_cylindermesh.md#class-cylindermesh), [PlaneMesh](class_planemesh.md#class-planemesh), [PointMesh](class_pointmesh.md#class-pointmesh), [PrismMesh](class_prismmesh.md#class-prismmesh), [RibbonTrailMesh](class_ribbontrailmesh.md#class-ribbontrailmesh), [SphereMesh](class_spheremesh.md#class-spheremesh), [TextMesh](class_textmesh.md#class-textmesh), [TorusMesh](class_torusmesh.md#class-torusmesh), [TubeTrailMesh](class_tubetrailmesh.md#class-tubetrailmesh)

Base class for all primitive meshes. Handles applying a [Material](class_material.md#class-material) to a primitive mesh.

<a id="description"></a>

## Description

Base class for all primitive meshes. Handles applying a [Material](class_material.md#class-material) to a primitive mesh. Examples include [BoxMesh](class_boxmesh.md#class-boxmesh), [CapsuleMesh](class_capsulemesh.md#class-capsulemesh), [CylinderMesh](class_cylindermesh.md#class-cylindermesh), [PlaneMesh](class_planemesh.md#class-planemesh), [PrismMesh](class_prismmesh.md#class-prismmesh), and [SphereMesh](class_spheremesh.md#class-spheremesh).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [add_uv2](class_primitivemesh.md#class-primitivemesh-property-add-uv2) | `false` |
| [AABB](class_aabb.md#class-aabb) | [custom_aabb](class_primitivemesh.md#class-primitivemesh-property-custom-aabb) | `AABB(0, 0, 0, 0, 0, 0)` |
| [bool](class_bool.md#class-bool) | [flip_faces](class_primitivemesh.md#class-primitivemesh-property-flip-faces) | `false` |
| [Material](class_material.md#class-material) | [material](class_primitivemesh.md#class-primitivemesh-property-material) |  |
| [float](class_float.md#class-float) | [uv2_padding](class_primitivemesh.md#class-primitivemesh-property-uv2-padding) | `2.0` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Array](class_array.md#class-array) | [_create_mesh_array](class_primitivemesh.md#class-primitivemesh-private-method-create-mesh-array)() virtual const |
| [Array](class_array.md#class-array) | [get_mesh_arrays](class_primitivemesh.md#class-primitivemesh-method-get-mesh-arrays)() const |
| void | [request_update](class_primitivemesh.md#class-primitivemesh-method-request-update)() |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-primitivemesh-property-add-uv2"></a>

[bool](class_bool.md#class-bool) **add_uv2** = `false` [🔗](class_primitivemesh.md#class-primitivemesh-property-add-uv2)

- void **set_add_uv2**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_add_uv2**()

If set, generates UV2 UV coordinates applying a padding using the [uv2_padding](class_primitivemesh.md#class-primitivemesh-property-uv2-padding) setting. UV2 is needed for lightmapping.

---


<a id="class-primitivemesh-property-custom-aabb"></a>

[AABB](class_aabb.md#class-aabb) **custom_aabb** = `AABB(0, 0, 0, 0, 0, 0)` [🔗](class_primitivemesh.md#class-primitivemesh-property-custom-aabb)

- void **set_custom_aabb**(value: [AABB](class_aabb.md#class-aabb))
- [AABB](class_aabb.md#class-aabb) **get_custom_aabb**()

Overrides the [AABB](class_aabb.md#class-aabb) with one defined by user for use with frustum culling. Especially useful to avoid unexpected culling when using a shader to offset vertices.

---


<a id="class-primitivemesh-property-flip-faces"></a>

[bool](class_bool.md#class-bool) **flip_faces** = `false` [🔗](class_primitivemesh.md#class-primitivemesh-property-flip-faces)

- void **set_flip_faces**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flip_faces**()

If `true`, the order of the vertices in each triangle is reversed, resulting in the backside of the mesh being drawn.

This gives the same result as using [BaseMaterial3D.CULL_FRONT](class_basematerial3d.md#class-basematerial3d-constant-cull-front) in [BaseMaterial3D.cull_mode](class_basematerial3d.md#class-basematerial3d-property-cull-mode).

---


<a id="class-primitivemesh-property-material"></a>

[Material](class_material.md#class-material) **material** [🔗](class_primitivemesh.md#class-primitivemesh-property-material)

- void **set_material**(value: [Material](class_material.md#class-material))
- [Material](class_material.md#class-material) **get_material**()

The current [Material](class_material.md#class-material) of the primitive mesh.

---


<a id="class-primitivemesh-property-uv2-padding"></a>

[float](class_float.md#class-float) **uv2_padding** = `2.0` [🔗](class_primitivemesh.md#class-primitivemesh-property-uv2-padding)

- void **set_uv2_padding**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_uv2_padding**()

If [add_uv2](class_primitivemesh.md#class-primitivemesh-property-add-uv2) is set, specifies the padding in pixels applied along seams of the mesh. Lower padding values allow making better use of the lightmap texture (resulting in higher texel density), but may introduce visible lightmap bleeding along edges.

If the size of the lightmap texture can't be determined when generating the mesh, UV2 is calculated assuming a texture size of 1024x1024.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-primitivemesh-private-method-create-mesh-array"></a>

[Array](class_array.md#class-array) **_create_mesh_array**() virtual const [🔗](class_primitivemesh.md#class-primitivemesh-private-method-create-mesh-array)

Override this method to customize how this primitive mesh should be generated. Should return an [Array](class_array.md#class-array) where each element is another Array of values required for the mesh (see the [ArrayType](class_mesh.md#enum-mesh-arraytype) constants).

---


<a id="class-primitivemesh-method-get-mesh-arrays"></a>

[Array](class_array.md#class-array) **get_mesh_arrays**() const [🔗](class_primitivemesh.md#class-primitivemesh-method-get-mesh-arrays)

Returns the mesh arrays used to make up the surface of this primitive mesh.

**Example:** Pass the result to [ArrayMesh.add_surface_from_arrays()](class_arraymesh.md#class-arraymesh-method-add-surface-from-arrays) to create a new surface:

```gdscript
var c = CylinderMesh.new()
var arr_mesh = ArrayMesh.new()
arr_mesh.add_surface_from_arrays(Mesh.PRIMITIVE_TRIANGLES, c.get_mesh_arrays())
```

```csharp
var c = new CylinderMesh();
var arrMesh = new ArrayMesh();
arrMesh.AddSurfaceFromArrays(Mesh.PrimitiveType.Triangles, c.GetMeshArrays());
```

---


<a id="class-primitivemesh-method-request-update"></a>

void **request_update**() [🔗](class_primitivemesh.md#class-primitivemesh-method-request-update)

Request an update of this primitive mesh based on its properties.
