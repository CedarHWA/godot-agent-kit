> Source: https://docs.godotengine.org/en/4.7/classes/class_navigationmeshsourcegeometrydata3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="navigationmeshsourcegeometrydata3d"></a>

<a id="class-navigationmeshsourcegeometrydata3d"></a>

# NavigationMeshSourceGeometryData3D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Container for parsed source geometry data used in navigation mesh baking.

<a id="description"></a>

## Description

Container for parsed source geometry data used in navigation mesh baking.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_faces](class_navigationmeshsourcegeometrydata3d.md#class-navigationmeshsourcegeometrydata3d-method-add-faces)(faces: [PackedVector3Array](class_packedvector3array.md#class-packedvector3array), xform: [Transform3D](class_transform3d.md#class-transform3d)) |
| void | [add_mesh](class_navigationmeshsourcegeometrydata3d.md#class-navigationmeshsourcegeometrydata3d-method-add-mesh)(mesh: [Mesh](class_mesh.md#class-mesh), xform: [Transform3D](class_transform3d.md#class-transform3d)) |
| void | [add_mesh_array](class_navigationmeshsourcegeometrydata3d.md#class-navigationmeshsourcegeometrydata3d-method-add-mesh-array)(mesh_array: [Array](class_array.md#class-array), xform: [Transform3D](class_transform3d.md#class-transform3d)) |
| void | [add_projected_obstruction](class_navigationmeshsourcegeometrydata3d.md#class-navigationmeshsourcegeometrydata3d-method-add-projected-obstruction)(vertices: [PackedVector3Array](class_packedvector3array.md#class-packedvector3array), elevation: [float](class_float.md#class-float), height: [float](class_float.md#class-float), carve: [bool](class_bool.md#class-bool)) |
| void | [append_arrays](class_navigationmeshsourcegeometrydata3d.md#class-navigationmeshsourcegeometrydata3d-method-append-arrays)(vertices: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array), indices: [PackedInt32Array](class_packedint32array.md#class-packedint32array)) |
| void | [clear](class_navigationmeshsourcegeometrydata3d.md#class-navigationmeshsourcegeometrydata3d-method-clear)() |
| void | [clear_projected_obstructions](class_navigationmeshsourcegeometrydata3d.md#class-navigationmeshsourcegeometrydata3d-method-clear-projected-obstructions)() |
| [AABB](class_aabb.md#class-aabb) | [get_bounds](class_navigationmeshsourcegeometrydata3d.md#class-navigationmeshsourcegeometrydata3d-method-get-bounds)() |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array) | [get_indices](class_navigationmeshsourcegeometrydata3d.md#class-navigationmeshsourcegeometrydata3d-method-get-indices)() const |
| [Array](class_array.md#class-array) | [get_projected_obstructions](class_navigationmeshsourcegeometrydata3d.md#class-navigationmeshsourcegeometrydata3d-method-get-projected-obstructions)() const |
| [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) | [get_vertices](class_navigationmeshsourcegeometrydata3d.md#class-navigationmeshsourcegeometrydata3d-method-get-vertices)() const |
| [bool](class_bool.md#class-bool) | [has_data](class_navigationmeshsourcegeometrydata3d.md#class-navigationmeshsourcegeometrydata3d-method-has-data)() |
| void | [merge](class_navigationmeshsourcegeometrydata3d.md#class-navigationmeshsourcegeometrydata3d-method-merge)(other_geometry: [NavigationMeshSourceGeometryData3D](class_navigationmeshsourcegeometrydata3d.md#class-navigationmeshsourcegeometrydata3d)) |
| void | [set_indices](class_navigationmeshsourcegeometrydata3d.md#class-navigationmeshsourcegeometrydata3d-method-set-indices)(indices: [PackedInt32Array](class_packedint32array.md#class-packedint32array)) |
| void | [set_projected_obstructions](class_navigationmeshsourcegeometrydata3d.md#class-navigationmeshsourcegeometrydata3d-method-set-projected-obstructions)(projected_obstructions: [Array](class_array.md#class-array)) |
| void | [set_vertices](class_navigationmeshsourcegeometrydata3d.md#class-navigationmeshsourcegeometrydata3d-method-set-vertices)(vertices: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array)) |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-navigationmeshsourcegeometrydata3d-method-add-faces"></a>

void **add_faces**(faces: [PackedVector3Array](class_packedvector3array.md#class-packedvector3array), xform: [Transform3D](class_transform3d.md#class-transform3d)) [🔗](class_navigationmeshsourcegeometrydata3d.md#class-navigationmeshsourcegeometrydata3d-method-add-faces)

Adds an array of vertex positions to the geometry data for navigation mesh baking to form triangulated faces. For each face the array must have three vertex positions in clockwise winding order. Since [NavigationMesh](class_navigationmesh.md#class-navigationmesh) resources have no transform, all vertex positions need to be offset by the node's transform using `xform`.

---


<a id="class-navigationmeshsourcegeometrydata3d-method-add-mesh"></a>

void **add_mesh**(mesh: [Mesh](class_mesh.md#class-mesh), xform: [Transform3D](class_transform3d.md#class-transform3d)) [🔗](class_navigationmeshsourcegeometrydata3d.md#class-navigationmeshsourcegeometrydata3d-method-add-mesh)

Adds the geometry data of a [Mesh](class_mesh.md#class-mesh) resource to the navigation mesh baking data. The mesh must have valid triangulated mesh data to be considered. Since [NavigationMesh](class_navigationmesh.md#class-navigationmesh) resources have no transform, all vertex positions need to be offset by the node's transform using `xform`.

---


<a id="class-navigationmeshsourcegeometrydata3d-method-add-mesh-array"></a>

void **add_mesh_array**(mesh_array: [Array](class_array.md#class-array), xform: [Transform3D](class_transform3d.md#class-transform3d)) [🔗](class_navigationmeshsourcegeometrydata3d.md#class-navigationmeshsourcegeometrydata3d-method-add-mesh-array)

Adds an [Array](class_array.md#class-array) the size of [Mesh.ARRAY_MAX](class_mesh.md#class-mesh-constant-array-max) and with vertices at index [Mesh.ARRAY_VERTEX](class_mesh.md#class-mesh-constant-array-vertex) and indices at index [Mesh.ARRAY_INDEX](class_mesh.md#class-mesh-constant-array-index) to the navigation mesh baking data. The array must have valid triangulated mesh data to be considered. Since [NavigationMesh](class_navigationmesh.md#class-navigationmesh) resources have no transform, all vertex positions need to be offset by the node's transform using `xform`.

---


<a id="class-navigationmeshsourcegeometrydata3d-method-add-projected-obstruction"></a>

void **add_projected_obstruction**(vertices: [PackedVector3Array](class_packedvector3array.md#class-packedvector3array), elevation: [float](class_float.md#class-float), height: [float](class_float.md#class-float), carve: [bool](class_bool.md#class-bool)) [🔗](class_navigationmeshsourcegeometrydata3d.md#class-navigationmeshsourcegeometrydata3d-method-add-projected-obstruction)

Adds a projected obstruction shape to the source geometry. The `vertices` are considered projected on an xz-axes plane, placed at the global y-axis `elevation` and extruded by `height`. If `carve` is `true` the carved shape will not be affected by additional offsets (e.g. agent radius) of the navigation mesh baking process.

---


<a id="class-navigationmeshsourcegeometrydata3d-method-append-arrays"></a>

void **append_arrays**(vertices: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array), indices: [PackedInt32Array](class_packedint32array.md#class-packedint32array)) [🔗](class_navigationmeshsourcegeometrydata3d.md#class-navigationmeshsourcegeometrydata3d-method-append-arrays)

Appends arrays of `vertices` and `indices` at the end of the existing arrays. Adds the existing index as an offset to the appended indices.

---


<a id="class-navigationmeshsourcegeometrydata3d-method-clear"></a>

void **clear**() [🔗](class_navigationmeshsourcegeometrydata3d.md#class-navigationmeshsourcegeometrydata3d-method-clear)

Clears the internal data.

---


<a id="class-navigationmeshsourcegeometrydata3d-method-clear-projected-obstructions"></a>

void **clear_projected_obstructions**() [🔗](class_navigationmeshsourcegeometrydata3d.md#class-navigationmeshsourcegeometrydata3d-method-clear-projected-obstructions)

Clears all projected obstructions.

---


<a id="class-navigationmeshsourcegeometrydata3d-method-get-bounds"></a>

[AABB](class_aabb.md#class-aabb) **get_bounds**() [🔗](class_navigationmeshsourcegeometrydata3d.md#class-navigationmeshsourcegeometrydata3d-method-get-bounds)

Returns an axis-aligned bounding box that covers all the stored geometry data. The bounds are calculated when calling this function with the result cached until further geometry changes are made.

---


<a id="class-navigationmeshsourcegeometrydata3d-method-get-indices"></a>

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_indices**() const [🔗](class_navigationmeshsourcegeometrydata3d.md#class-navigationmeshsourcegeometrydata3d-method-get-indices)

Returns the parsed source geometry data indices array.

---


<a id="class-navigationmeshsourcegeometrydata3d-method-get-projected-obstructions"></a>

[Array](class_array.md#class-array) **get_projected_obstructions**() const [🔗](class_navigationmeshsourcegeometrydata3d.md#class-navigationmeshsourcegeometrydata3d-method-get-projected-obstructions)

Returns the projected obstructions as an [Array](class_array.md#class-array) of dictionaries. Each [Dictionary](class_dictionary.md#class-dictionary) contains the following entries:

- `vertices` - A [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) that defines the outline points of the projected shape.
- `elevation` - A [float](class_float.md#class-float) that defines the projected shape placement on the y-axis.
- `height` - A [float](class_float.md#class-float) that defines how much the projected shape is extruded along the y-axis.
- `carve` - A [bool](class_bool.md#class-bool) that defines how the obstacle affects the navigation mesh baking. If `true` the projected shape will not be affected by addition offsets, e.g. agent radius.

---


<a id="class-navigationmeshsourcegeometrydata3d-method-get-vertices"></a>

[PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) **get_vertices**() const [🔗](class_navigationmeshsourcegeometrydata3d.md#class-navigationmeshsourcegeometrydata3d-method-get-vertices)

Returns the parsed source geometry data vertices array.

---


<a id="class-navigationmeshsourcegeometrydata3d-method-has-data"></a>

[bool](class_bool.md#class-bool) **has_data**() [🔗](class_navigationmeshsourcegeometrydata3d.md#class-navigationmeshsourcegeometrydata3d-method-has-data)

Returns `true` when parsed source geometry data exists.

---


<a id="class-navigationmeshsourcegeometrydata3d-method-merge"></a>

void **merge**(other_geometry: [NavigationMeshSourceGeometryData3D](class_navigationmeshsourcegeometrydata3d.md#class-navigationmeshsourcegeometrydata3d)) [🔗](class_navigationmeshsourcegeometrydata3d.md#class-navigationmeshsourcegeometrydata3d-method-merge)

Adds the geometry data of another **NavigationMeshSourceGeometryData3D** to the navigation mesh baking data.

---


<a id="class-navigationmeshsourcegeometrydata3d-method-set-indices"></a>

void **set_indices**(indices: [PackedInt32Array](class_packedint32array.md#class-packedint32array)) [🔗](class_navigationmeshsourcegeometrydata3d.md#class-navigationmeshsourcegeometrydata3d-method-set-indices)

Sets the parsed source geometry data indices. The indices need to be matched with appropriated vertices.

**Warning:** Inappropriate data can crash the baking process of the involved third-party libraries.

---


<a id="class-navigationmeshsourcegeometrydata3d-method-set-projected-obstructions"></a>

void **set_projected_obstructions**(projected_obstructions: [Array](class_array.md#class-array)) [🔗](class_navigationmeshsourcegeometrydata3d.md#class-navigationmeshsourcegeometrydata3d-method-set-projected-obstructions)

Sets the projected obstructions with an Array of Dictionaries with the following key value pairs:

```gdscript
"vertices" : PackedFloat32Array
"elevation" : float
"height" : float
"carve" : bool
```

---


<a id="class-navigationmeshsourcegeometrydata3d-method-set-vertices"></a>

void **set_vertices**(vertices: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array)) [🔗](class_navigationmeshsourcegeometrydata3d.md#class-navigationmeshsourcegeometrydata3d-method-set-vertices)

Sets the parsed source geometry data vertices. The vertices need to be matched with appropriated indices.

**Warning:** Inappropriate data can crash the baking process of the involved third-party libraries.
