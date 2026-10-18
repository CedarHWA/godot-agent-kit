> Source: https://docs.godotengine.org/en/4.7/classes/class_arraymesh.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="arraymesh"></a>

<a id="class-arraymesh"></a>

# ArrayMesh

**Inherits:** [Mesh](class_mesh.md#class-mesh) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

[Mesh](class_mesh.md#class-mesh) type that provides utility for constructing a surface from arrays.

<a id="description"></a>

## Description

The **ArrayMesh** is used to construct a [Mesh](class_mesh.md#class-mesh) by specifying the attributes as arrays.

The most basic example is the creation of a single triangle:

```gdscript
var vertices = PackedVector3Array()
vertices.push_back(Vector3(0, 1, 0))
vertices.push_back(Vector3(1, 0, 0))
vertices.push_back(Vector3(0, 0, 1))

# Initialize the ArrayMesh.
var arr_mesh = ArrayMesh.new()
var arrays = []
arrays.resize(Mesh.ARRAY_MAX)
arrays[Mesh.ARRAY_VERTEX] = vertices

# Create the Mesh.
arr_mesh.add_surface_from_arrays(Mesh.PRIMITIVE_TRIANGLES, arrays)
var m = MeshInstance3D.new()
m.mesh = arr_mesh
```

```csharp
Vector3[] vertices =
[
    new Vector3(0, 1, 0),
    new Vector3(1, 0, 0),
    new Vector3(0, 0, 1),
];

// Initialize the ArrayMesh.
var arrMesh = new ArrayMesh();
Godot.Collections.Array arrays = [];
arrays.Resize((int)Mesh.ArrayType.Max);
arrays[(int)Mesh.ArrayType.Vertex] = vertices;

// Create the Mesh.
arrMesh.AddSurfaceFromArrays(Mesh.PrimitiveType.Triangles, arrays);
var m = new MeshInstance3D();
m.Mesh = arrMesh;
```

The [MeshInstance3D](class_meshinstance3d.md#class-meshinstance3d) is ready to be added to the [SceneTree](class_scenetree.md#class-scenetree) to be shown.

See also [ImmediateMesh](class_immediatemesh.md#class-immediatemesh), [MeshDataTool](class_meshdatatool.md#class-meshdatatool) and [SurfaceTool](class_surfacetool.md#class-surfacetool) for procedural geometry generation.

**Note:** Godot uses clockwise [winding order](https://learnopengl.com/Advanced-OpenGL/Face-culling) for front faces of triangle primitive modes.

<a id="tutorials"></a>

## Tutorials

- [Procedural geometry using the ArrayMesh](../tutorials/3d/procedural_geometry/arraymesh.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [BlendShapeMode](class_mesh.md#enum-mesh-blendshapemode) | [blend_shape_mode](class_arraymesh.md#class-arraymesh-property-blend-shape-mode) | `1` |
| [AABB](class_aabb.md#class-aabb) | [custom_aabb](class_arraymesh.md#class-arraymesh-property-custom-aabb) | `AABB(0, 0, 0, 0, 0, 0)` |
| [ArrayMesh](class_arraymesh.md#class-arraymesh) | [shadow_mesh](class_arraymesh.md#class-arraymesh-property-shadow-mesh) |  |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_blend_shape](class_arraymesh.md#class-arraymesh-method-add-blend-shape)(name: [StringName](class_stringname.md#class-stringname)) |
| void | [add_surface_from_arrays](class_arraymesh.md#class-arraymesh-method-add-surface-from-arrays)(primitive: [PrimitiveType](class_mesh.md#enum-mesh-primitivetype), arrays: [Array](class_array.md#class-array), blend_shapes: [Array](class_array.md#class-array)[[Array](class_array.md#class-array)] = [], lods: [Dictionary](class_dictionary.md#class-dictionary) = {}, flags: BitField[[ArrayFormat](class_mesh.md#enum-mesh-arrayformat)] = 0) |
| void | [clear_blend_shapes](class_arraymesh.md#class-arraymesh-method-clear-blend-shapes)() |
| void | [clear_surfaces](class_arraymesh.md#class-arraymesh-method-clear-surfaces)() |
| [int](class_int.md#class-int) | [get_blend_shape_count](class_arraymesh.md#class-arraymesh-method-get-blend-shape-count)() const |
| [StringName](class_stringname.md#class-stringname) | [get_blend_shape_name](class_arraymesh.md#class-arraymesh-method-get-blend-shape-name)(index: [int](class_int.md#class-int)) const |
| [Error](class_@globalscope.md#enum-globalscope-error) | [lightmap_unwrap](class_arraymesh.md#class-arraymesh-method-lightmap-unwrap)(transform: [Transform3D](class_transform3d.md#class-transform3d), texel_size: [float](class_float.md#class-float)) |
| void | [regen_normal_maps](class_arraymesh.md#class-arraymesh-method-regen-normal-maps)() |
| void | [set_blend_shape_name](class_arraymesh.md#class-arraymesh-method-set-blend-shape-name)(index: [int](class_int.md#class-int), name: [StringName](class_stringname.md#class-stringname)) |
| [int](class_int.md#class-int) | [surface_find_by_name](class_arraymesh.md#class-arraymesh-method-surface-find-by-name)(name: [String](class_string.md#class-string)) const |
| [int](class_int.md#class-int) | [surface_get_array_index_len](class_arraymesh.md#class-arraymesh-method-surface-get-array-index-len)(surf_idx: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [surface_get_array_len](class_arraymesh.md#class-arraymesh-method-surface-get-array-len)(surf_idx: [int](class_int.md#class-int)) const |
| BitField[[ArrayFormat](class_mesh.md#enum-mesh-arrayformat)] | [surface_get_format](class_arraymesh.md#class-arraymesh-method-surface-get-format)(surf_idx: [int](class_int.md#class-int)) const |
| [String](class_string.md#class-string) | [surface_get_name](class_arraymesh.md#class-arraymesh-method-surface-get-name)(surf_idx: [int](class_int.md#class-int)) const |
| [PrimitiveType](class_mesh.md#enum-mesh-primitivetype) | [surface_get_primitive_type](class_arraymesh.md#class-arraymesh-method-surface-get-primitive-type)(surf_idx: [int](class_int.md#class-int)) const |
| void | [surface_remove](class_arraymesh.md#class-arraymesh-method-surface-remove)(surf_idx: [int](class_int.md#class-int)) |
| void | [surface_set_name](class_arraymesh.md#class-arraymesh-method-surface-set-name)(surf_idx: [int](class_int.md#class-int), name: [String](class_string.md#class-string)) |
| void | [surface_update_attribute_region](class_arraymesh.md#class-arraymesh-method-surface-update-attribute-region)(surf_idx: [int](class_int.md#class-int), offset: [int](class_int.md#class-int), data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray)) |
| void | [surface_update_skin_region](class_arraymesh.md#class-arraymesh-method-surface-update-skin-region)(surf_idx: [int](class_int.md#class-int), offset: [int](class_int.md#class-int), data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray)) |
| void | [surface_update_vertex_region](class_arraymesh.md#class-arraymesh-method-surface-update-vertex-region)(surf_idx: [int](class_int.md#class-int), offset: [int](class_int.md#class-int), data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray)) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-arraymesh-property-blend-shape-mode"></a>

[BlendShapeMode](class_mesh.md#enum-mesh-blendshapemode) **blend_shape_mode** = `1` [🔗](class_arraymesh.md#class-arraymesh-property-blend-shape-mode)

- void **set_blend_shape_mode**(value: [BlendShapeMode](class_mesh.md#enum-mesh-blendshapemode))
- [BlendShapeMode](class_mesh.md#enum-mesh-blendshapemode) **get_blend_shape_mode**()

The blend shape mode.

---


<a id="class-arraymesh-property-custom-aabb"></a>

[AABB](class_aabb.md#class-aabb) **custom_aabb** = `AABB(0, 0, 0, 0, 0, 0)` [🔗](class_arraymesh.md#class-arraymesh-property-custom-aabb)

- void **set_custom_aabb**(value: [AABB](class_aabb.md#class-aabb))
- [AABB](class_aabb.md#class-aabb) **get_custom_aabb**()

Overrides the [AABB](class_aabb.md#class-aabb) with one defined by user for use with frustum culling. Especially useful to avoid unexpected culling when using a shader to offset vertices.

---


<a id="class-arraymesh-property-shadow-mesh"></a>

[ArrayMesh](class_arraymesh.md#class-arraymesh) **shadow_mesh** [🔗](class_arraymesh.md#class-arraymesh-property-shadow-mesh)

- void **set_shadow_mesh**(value: [ArrayMesh](class_arraymesh.md#class-arraymesh))
- [ArrayMesh](class_arraymesh.md#class-arraymesh) **get_shadow_mesh**()

An optional mesh which can be used for rendering shadows and the depth prepass. Can be used to increase performance by supplying a mesh with fused vertices and only vertex position data (without normals, UVs, colors, etc.).

**Note:** This mesh must have exactly the same vertex positions as the source mesh (including the source mesh's LODs, if present). If vertex positions differ, then the mesh will not draw correctly.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-arraymesh-method-add-blend-shape"></a>

void **add_blend_shape**(name: [StringName](class_stringname.md#class-stringname)) [🔗](class_arraymesh.md#class-arraymesh-method-add-blend-shape)

Adds name for a blend shape that will be added with [add_surface_from_arrays()](class_arraymesh.md#class-arraymesh-method-add-surface-from-arrays). Must be called before surface is added.

---


<a id="class-arraymesh-method-add-surface-from-arrays"></a>

void **add_surface_from_arrays**(primitive: [PrimitiveType](class_mesh.md#enum-mesh-primitivetype), arrays: [Array](class_array.md#class-array), blend_shapes: [Array](class_array.md#class-array)[[Array](class_array.md#class-array)] = [], lods: [Dictionary](class_dictionary.md#class-dictionary) = {}, flags: BitField[[ArrayFormat](class_mesh.md#enum-mesh-arrayformat)] = 0) [🔗](class_arraymesh.md#class-arraymesh-method-add-surface-from-arrays)

Creates a new surface. [Mesh.get_surface_count()](class_mesh.md#class-mesh-method-get-surface-count) will become the `surf_idx` for this new surface.

Surfaces are created to be rendered using a `primitive`, which may be any of the values defined in [PrimitiveType](class_mesh.md#enum-mesh-primitivetype).

The `arrays` argument is an array of arrays. Each of the [Mesh.ARRAY_MAX](class_mesh.md#class-mesh-constant-array-max) elements contains an array with some of the mesh data for this surface as described by the corresponding member of [ArrayType](class_mesh.md#enum-mesh-arraytype) or `null` if it is not used by the surface. For example, `arrays[0]` is the array of vertices. That first vertex sub-array is always required; the others are optional. Adding an index array puts this surface into "index mode" where the vertex and other arrays become the sources of data and the index array defines the vertex order. All sub-arrays must have the same length as the vertex array (or be an exact multiple of the vertex array's length, when multiple elements of a sub-array correspond to a single vertex) or be empty, except for [Mesh.ARRAY_INDEX](class_mesh.md#class-mesh-constant-array-index) if it is used.

The `blend_shapes` argument is an array of vertex data for each blend shape. Each element is an array of the same structure as `arrays`, but [Mesh.ARRAY_VERTEX](class_mesh.md#class-mesh-constant-array-vertex), [Mesh.ARRAY_NORMAL](class_mesh.md#class-mesh-constant-array-normal), and [Mesh.ARRAY_TANGENT](class_mesh.md#class-mesh-constant-array-tangent) are set if and only if they are set in `arrays` and all other entries are `null`.

The `lods` argument is a dictionary with [float](class_float.md#class-float) keys and [PackedInt32Array](class_packedint32array.md#class-packedint32array) values. Each entry in the dictionary represents an LOD level of the surface, where the value is the [Mesh.ARRAY_INDEX](class_mesh.md#class-mesh-constant-array-index) array to use for the LOD level and the key is roughly proportional to the distance at which the LOD stats being used. I.e., increasing the key of an LOD also increases the distance that the objects has to be from the camera before the LOD is used.

The `flags` argument is the bitwise OR of, as required: One value of [ArrayCustomFormat](class_mesh.md#enum-mesh-arraycustomformat) left shifted by `ARRAY_FORMAT_CUSTOMn_SHIFT` for each custom channel in use, [Mesh.ARRAY_FLAG_USE_DYNAMIC_UPDATE](class_mesh.md#class-mesh-constant-array-flag-use-dynamic-update), [Mesh.ARRAY_FLAG_USE_8_BONE_WEIGHTS](class_mesh.md#class-mesh-constant-array-flag-use-8-bone-weights), or [Mesh.ARRAY_FLAG_USES_EMPTY_VERTEX_ARRAY](class_mesh.md#class-mesh-constant-array-flag-uses-empty-vertex-array).

**Note:** When using indices, it is recommended to only use points, lines, or triangles.

---


<a id="class-arraymesh-method-clear-blend-shapes"></a>

void **clear_blend_shapes**() [🔗](class_arraymesh.md#class-arraymesh-method-clear-blend-shapes)

Removes all blend shapes from this **ArrayMesh**.

---


<a id="class-arraymesh-method-clear-surfaces"></a>

void **clear_surfaces**() [🔗](class_arraymesh.md#class-arraymesh-method-clear-surfaces)

Removes all surfaces from this **ArrayMesh**.

---


<a id="class-arraymesh-method-get-blend-shape-count"></a>

[int](class_int.md#class-int) **get_blend_shape_count**() const [🔗](class_arraymesh.md#class-arraymesh-method-get-blend-shape-count)

Returns the number of blend shapes that the **ArrayMesh** holds.

---


<a id="class-arraymesh-method-get-blend-shape-name"></a>

[StringName](class_stringname.md#class-stringname) **get_blend_shape_name**(index: [int](class_int.md#class-int)) const [🔗](class_arraymesh.md#class-arraymesh-method-get-blend-shape-name)

Returns the name of the blend shape at this index.

---


<a id="class-arraymesh-method-lightmap-unwrap"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **lightmap_unwrap**(transform: [Transform3D](class_transform3d.md#class-transform3d), texel_size: [float](class_float.md#class-float)) [🔗](class_arraymesh.md#class-arraymesh-method-lightmap-unwrap)

Performs a UV unwrap on the **ArrayMesh** to prepare the mesh for lightmapping.

---


<a id="class-arraymesh-method-regen-normal-maps"></a>

void **regen_normal_maps**() [🔗](class_arraymesh.md#class-arraymesh-method-regen-normal-maps)

Regenerates tangents for each of the **ArrayMesh**'s surfaces.

---


<a id="class-arraymesh-method-set-blend-shape-name"></a>

void **set_blend_shape_name**(index: [int](class_int.md#class-int), name: [StringName](class_stringname.md#class-stringname)) [🔗](class_arraymesh.md#class-arraymesh-method-set-blend-shape-name)

Sets the name of the blend shape at this index.

---


<a id="class-arraymesh-method-surface-find-by-name"></a>

[int](class_int.md#class-int) **surface_find_by_name**(name: [String](class_string.md#class-string)) const [🔗](class_arraymesh.md#class-arraymesh-method-surface-find-by-name)

Returns the index of the first surface with this name held within this **ArrayMesh**. If none are found, -1 is returned.

---


<a id="class-arraymesh-method-surface-get-array-index-len"></a>

[int](class_int.md#class-int) **surface_get_array_index_len**(surf_idx: [int](class_int.md#class-int)) const [🔗](class_arraymesh.md#class-arraymesh-method-surface-get-array-index-len)

Returns the length in indices of the index array in the requested surface (see [add_surface_from_arrays()](class_arraymesh.md#class-arraymesh-method-add-surface-from-arrays)).

---


<a id="class-arraymesh-method-surface-get-array-len"></a>

[int](class_int.md#class-int) **surface_get_array_len**(surf_idx: [int](class_int.md#class-int)) const [🔗](class_arraymesh.md#class-arraymesh-method-surface-get-array-len)

Returns the length in vertices of the vertex array in the requested surface (see [add_surface_from_arrays()](class_arraymesh.md#class-arraymesh-method-add-surface-from-arrays)).

---


<a id="class-arraymesh-method-surface-get-format"></a>

BitField[[ArrayFormat](class_mesh.md#enum-mesh-arrayformat)] **surface_get_format**(surf_idx: [int](class_int.md#class-int)) const [🔗](class_arraymesh.md#class-arraymesh-method-surface-get-format)

Returns the format mask of the requested surface (see [add_surface_from_arrays()](class_arraymesh.md#class-arraymesh-method-add-surface-from-arrays)).

---


<a id="class-arraymesh-method-surface-get-name"></a>

[String](class_string.md#class-string) **surface_get_name**(surf_idx: [int](class_int.md#class-int)) const [🔗](class_arraymesh.md#class-arraymesh-method-surface-get-name)

Gets the name assigned to this surface.

---


<a id="class-arraymesh-method-surface-get-primitive-type"></a>

[PrimitiveType](class_mesh.md#enum-mesh-primitivetype) **surface_get_primitive_type**(surf_idx: [int](class_int.md#class-int)) const [🔗](class_arraymesh.md#class-arraymesh-method-surface-get-primitive-type)

Returns the primitive type of the requested surface (see [add_surface_from_arrays()](class_arraymesh.md#class-arraymesh-method-add-surface-from-arrays)).

---


<a id="class-arraymesh-method-surface-remove"></a>

void **surface_remove**(surf_idx: [int](class_int.md#class-int)) [🔗](class_arraymesh.md#class-arraymesh-method-surface-remove)

Removes the surface at the given index from the Mesh, shifting surfaces with higher index down by one.

---


<a id="class-arraymesh-method-surface-set-name"></a>

void **surface_set_name**(surf_idx: [int](class_int.md#class-int), name: [String](class_string.md#class-string)) [🔗](class_arraymesh.md#class-arraymesh-method-surface-set-name)

Sets a name for a given surface.

---


<a id="class-arraymesh-method-surface-update-attribute-region"></a>

void **surface_update_attribute_region**(surf_idx: [int](class_int.md#class-int), offset: [int](class_int.md#class-int), data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray)) [🔗](class_arraymesh.md#class-arraymesh-method-surface-update-attribute-region)

Updates the attribute buffer of this mesh's surface with the given `data`. The expected data per attribute is 12 or 8 bytes (4 bytes per float, 2 floats per [Vector2](class_vector2.md#class-vector2), and 3 floats per [Vector3](class_vector3.md#class-vector3)) depending on if the mesh is using [Vector3](class_vector3.md#class-vector3) or [Vector2](class_vector2.md#class-vector2) vertices. This value can be determined with [RenderingServer.mesh_surface_get_format_attribute_stride()](class_renderingserver.md#class-renderingserver-method-mesh-surface-get-format-attribute-stride).

The starting point of the updates can be changed with `offset`. The value of `offset` should be a multiple of 12 bytes in most cases to align to each attribute.

A [PackedVector3Array](class_packedvector3array.md#class-packedvector3array) of attribute locations can be converted into a [PackedByteArray](class_packedbytearray.md#class-packedbytearray) using [PackedVector3Array.to_byte_array()](class_packedvector3array.md#class-packedvector3array-method-to-byte-array) for use in `data`.

---


<a id="class-arraymesh-method-surface-update-skin-region"></a>

void **surface_update_skin_region**(surf_idx: [int](class_int.md#class-int), offset: [int](class_int.md#class-int), data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray)) [🔗](class_arraymesh.md#class-arraymesh-method-surface-update-skin-region)

Updates the skin buffer of this mesh's surface with the given `data`. The expected data per skin is 12 or 8 bytes (4 bytes per float, 2 floats per [Vector2](class_vector2.md#class-vector2), and 3 floats per [Vector3](class_vector3.md#class-vector3)) depending on if the mesh is using [Vector3](class_vector3.md#class-vector3) or [Vector2](class_vector2.md#class-vector2) vertices. This value can be determined with [RenderingServer.mesh_surface_get_format_skin_stride()](class_renderingserver.md#class-renderingserver-method-mesh-surface-get-format-skin-stride).

The starting point of the updates can be changed with `offset`. The value of `offset` should be a multiple of 12 bytes in most cases to align to each skin.

A [PackedVector3Array](class_packedvector3array.md#class-packedvector3array) of skin locations can be converted into a [PackedByteArray](class_packedbytearray.md#class-packedbytearray) using [PackedVector3Array.to_byte_array()](class_packedvector3array.md#class-packedvector3array-method-to-byte-array) for use in `data`.

---


<a id="class-arraymesh-method-surface-update-vertex-region"></a>

void **surface_update_vertex_region**(surf_idx: [int](class_int.md#class-int), offset: [int](class_int.md#class-int), data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray)) [🔗](class_arraymesh.md#class-arraymesh-method-surface-update-vertex-region)

Updates the vertex buffer of this mesh's surface with the given `data`. The expected data per vertex is 12 or 8 bytes (4 bytes per float, 2 floats per [Vector2](class_vector2.md#class-vector2), and 3 floats per [Vector3](class_vector3.md#class-vector3)) depending on if the mesh is using [Vector3](class_vector3.md#class-vector3) or [Vector2](class_vector2.md#class-vector2) vertices. This value can be determined with [RenderingServer.mesh_surface_get_format_vertex_stride()](class_renderingserver.md#class-renderingserver-method-mesh-surface-get-format-vertex-stride).

The starting point of the updates can be changed with `offset`. The value of `offset` should be a multiple of 12 bytes in most cases to align to each vertex.

A [PackedVector3Array](class_packedvector3array.md#class-packedvector3array) of vertex locations can be converted into a [PackedByteArray](class_packedbytearray.md#class-packedbytearray) using [PackedVector3Array.to_byte_array()](class_packedvector3array.md#class-packedvector3array-method-to-byte-array) for use in `data`.
