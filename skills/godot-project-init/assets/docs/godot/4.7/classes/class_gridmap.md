> Source: https://docs.godotengine.org/en/4.7/classes/class_gridmap.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="gridmap"></a>

<a id="class-gridmap"></a>

# GridMap

**Inherits:** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Node for 3D tile-based maps.

<a id="description"></a>

## Description

GridMap lets you place meshes on a grid interactively. It works both from the editor and from scripts, which can help you create in-game level editors.

GridMaps use a [MeshLibrary](class_meshlibrary.md#class-meshlibrary) which contains a list of tiles. Each tile is a mesh with materials plus optional collision and navigation shapes.

A GridMap contains a collection of cells. Each grid cell refers to a tile in the [MeshLibrary](class_meshlibrary.md#class-meshlibrary). All cells in the map have the same dimensions.

Internally, a GridMap is split into a sparse collection of octants for efficient rendering and physics processing. Every octant has the same dimensions and can contain several cells.

**Note:** GridMap doesn't extend [VisualInstance3D](class_visualinstance3d.md#class-visualinstance3d) and therefore can't be hidden or cull masked based on [VisualInstance3D.layers](class_visualinstance3d.md#class-visualinstance3d-property-layers). If you make a light not affect the first layer, the whole GridMap won't be lit by the light in question.

<a id="tutorials"></a>

## Tutorials

- [Using gridmaps](../tutorials/3d/using_gridmaps.md)
- [3D Platformer Demo](https://godotengine.org/asset-library/asset/2748)
- [3D Kinematic Character Demo](https://godotengine.org/asset-library/asset/2739)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [bake_navigation](class_gridmap.md#class-gridmap-property-bake-navigation) | `false` |
| [bool](class_bool.md#class-bool) | [cell_center_x](class_gridmap.md#class-gridmap-property-cell-center-x) | `true` |
| [bool](class_bool.md#class-bool) | [cell_center_y](class_gridmap.md#class-gridmap-property-cell-center-y) | `true` |
| [bool](class_bool.md#class-bool) | [cell_center_z](class_gridmap.md#class-gridmap-property-cell-center-z) | `true` |
| [int](class_int.md#class-int) | [cell_octant_size](class_gridmap.md#class-gridmap-property-cell-octant-size) | `8` |
| [float](class_float.md#class-float) | [cell_scale](class_gridmap.md#class-gridmap-property-cell-scale) | `1.0` |
| [Vector3](class_vector3.md#class-vector3) | [cell_size](class_gridmap.md#class-gridmap-property-cell-size) | `Vector3(2, 2, 2)` |
| [int](class_int.md#class-int) | [collision_layer](class_gridmap.md#class-gridmap-property-collision-layer) | `1` |
| [int](class_int.md#class-int) | [collision_mask](class_gridmap.md#class-gridmap-property-collision-mask) | `1` |
| [float](class_float.md#class-float) | [collision_priority](class_gridmap.md#class-gridmap-property-collision-priority) | `1.0` |
| [DebugVisibilityMode](class_gridmap.md#enum-gridmap-debugvisibilitymode) | [collision_visibility_mode](class_gridmap.md#class-gridmap-property-collision-visibility-mode) | `0` |
| [MeshLibrary](class_meshlibrary.md#class-meshlibrary) | [mesh_library](class_gridmap.md#class-gridmap-property-mesh-library) |  |
| [PhysicsMaterial](class_physicsmaterial.md#class-physicsmaterial) | [physics_material](class_gridmap.md#class-gridmap-property-physics-material) |  |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [clear](class_gridmap.md#class-gridmap-method-clear)() |
| void | [clear_baked_meshes](class_gridmap.md#class-gridmap-method-clear-baked-meshes)() |
| [RID](class_rid.md#class-rid) | [get_bake_mesh_instance](class_gridmap.md#class-gridmap-method-get-bake-mesh-instance)(idx: [int](class_int.md#class-int)) |
| [Array](class_array.md#class-array) | [get_bake_meshes](class_gridmap.md#class-gridmap-method-get-bake-meshes)() |
| [Basis](class_basis.md#class-basis) | [get_basis_with_orthogonal_index](class_gridmap.md#class-gridmap-method-get-basis-with-orthogonal-index)(index: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_cell_item](class_gridmap.md#class-gridmap-method-get-cell-item)(position: [Vector3i](class_vector3i.md#class-vector3i)) const |
| [Basis](class_basis.md#class-basis) | [get_cell_item_basis](class_gridmap.md#class-gridmap-method-get-cell-item-basis)(position: [Vector3i](class_vector3i.md#class-vector3i)) const |
| [int](class_int.md#class-int) | [get_cell_item_orientation](class_gridmap.md#class-gridmap-method-get-cell-item-orientation)(position: [Vector3i](class_vector3i.md#class-vector3i)) const |
| [bool](class_bool.md#class-bool) | [get_collision_layer_value](class_gridmap.md#class-gridmap-method-get-collision-layer-value)(layer_number: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [get_collision_mask_value](class_gridmap.md#class-gridmap-method-get-collision-mask-value)(layer_number: [int](class_int.md#class-int)) const |
| [Array](class_array.md#class-array) | [get_meshes](class_gridmap.md#class-gridmap-method-get-meshes)() const |
| [RID](class_rid.md#class-rid) | [get_navigation_map](class_gridmap.md#class-gridmap-method-get-navigation-map)() const |
| [Vector3i](class_vector3i.md#class-vector3i) | [get_octant_coords_from_cell_coords](class_gridmap.md#class-gridmap-method-get-octant-coords-from-cell-coords)(cell_coords: [Vector3i](class_vector3i.md#class-vector3i)) const |
| [Array](class_array.md#class-array)[[Vector3i](class_vector3i.md#class-vector3i)] | [get_octants_in_bounds](class_gridmap.md#class-gridmap-method-get-octants-in-bounds)(bounds: [AABB](class_aabb.md#class-aabb)) const |
| [int](class_int.md#class-int) | [get_orthogonal_index_from_basis](class_gridmap.md#class-gridmap-method-get-orthogonal-index-from-basis)(basis: [Basis](class_basis.md#class-basis)) const |
| [Array](class_array.md#class-array)[[Vector3i](class_vector3i.md#class-vector3i)] | [get_used_cells](class_gridmap.md#class-gridmap-method-get-used-cells)() const |
| [Array](class_array.md#class-array)[[Vector3i](class_vector3i.md#class-vector3i)] | [get_used_cells_by_item](class_gridmap.md#class-gridmap-method-get-used-cells-by-item)(item: [int](class_int.md#class-int)) const |
| [Array](class_array.md#class-array)[[Vector3i](class_vector3i.md#class-vector3i)] | [get_used_cells_in_octant](class_gridmap.md#class-gridmap-method-get-used-cells-in-octant)(octant_coords: [Vector3i](class_vector3i.md#class-vector3i)) const |
| [Array](class_array.md#class-array)[[Vector3i](class_vector3i.md#class-vector3i)] | [get_used_cells_in_octant_by_item](class_gridmap.md#class-gridmap-method-get-used-cells-in-octant-by-item)(octant_coords: [Vector3i](class_vector3i.md#class-vector3i), item: [int](class_int.md#class-int)) const |
| [Array](class_array.md#class-array)[[Vector3i](class_vector3i.md#class-vector3i)] | [get_used_octants](class_gridmap.md#class-gridmap-method-get-used-octants)() const |
| [Array](class_array.md#class-array)[[Vector3i](class_vector3i.md#class-vector3i)] | [get_used_octants_by_item](class_gridmap.md#class-gridmap-method-get-used-octants-by-item)(item: [int](class_int.md#class-int)) const |
| [Array](class_array.md#class-array)[[Vector3i](class_vector3i.md#class-vector3i)] | [get_used_octants_in_bounds](class_gridmap.md#class-gridmap-method-get-used-octants-in-bounds)(bounds: [AABB](class_aabb.md#class-aabb)) const |
| [Vector3i](class_vector3i.md#class-vector3i) | [local_to_map](class_gridmap.md#class-gridmap-method-local-to-map)(local_position: [Vector3](class_vector3.md#class-vector3)) const |
| void | [make_baked_meshes](class_gridmap.md#class-gridmap-method-make-baked-meshes)(gen_lightmap_uv: [bool](class_bool.md#class-bool) = false, lightmap_uv_texel_size: [float](class_float.md#class-float) = 0.1) |
| [Vector3](class_vector3.md#class-vector3) | [map_to_local](class_gridmap.md#class-gridmap-method-map-to-local)(map_position: [Vector3i](class_vector3i.md#class-vector3i)) const |
| void | [resource_changed](class_gridmap.md#class-gridmap-method-resource-changed)(resource: [Resource](class_resource.md#class-resource)) |
| void | [set_cell_item](class_gridmap.md#class-gridmap-method-set-cell-item)(position: [Vector3i](class_vector3i.md#class-vector3i), item: [int](class_int.md#class-int), orientation: [int](class_int.md#class-int) = 0) |
| void | [set_collision_layer_value](class_gridmap.md#class-gridmap-method-set-collision-layer-value)(layer_number: [int](class_int.md#class-int), value: [bool](class_bool.md#class-bool)) |
| void | [set_collision_mask_value](class_gridmap.md#class-gridmap-method-set-collision-mask-value)(layer_number: [int](class_int.md#class-int), value: [bool](class_bool.md#class-bool)) |
| void | [set_navigation_map](class_gridmap.md#class-gridmap-method-set-navigation-map)(navigation_map: [RID](class_rid.md#class-rid)) |

---


<a id="signals"></a>

## Signals

<a id="class-gridmap-signal-cell-size-changed"></a>

**cell_size_changed**(cell_size: [Vector3](class_vector3.md#class-vector3)) [🔗](class_gridmap.md#class-gridmap-signal-cell-size-changed)

Emitted when [cell_size](class_gridmap.md#class-gridmap-property-cell-size) changes.

---


<a id="class-gridmap-signal-changed"></a>

**changed**() [🔗](class_gridmap.md#class-gridmap-signal-changed)

Emitted when the [MeshLibrary](class_meshlibrary.md#class-meshlibrary) of this GridMap changes.

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-gridmap-debugvisibilitymode"></a>

enum **DebugVisibilityMode**: [🔗](class_gridmap.md#enum-gridmap-debugvisibilitymode)

<a id="class-gridmap-constant-debug-visibility-mode-default"></a>

[DebugVisibilityMode](class_gridmap.md#enum-gridmap-debugvisibilitymode) **DEBUG_VISIBILITY_MODE_DEFAULT** = `0`

Hide the collisions debug shapes in the editor, and use the debug settings to determine their visibility in game (i.e. [SceneTree.debug_collisions_hint](class_scenetree.md#class-scenetree-property-debug-collisions-hint) or [SceneTree.debug_navigation_hint](class_scenetree.md#class-scenetree-property-debug-navigation-hint)).

<a id="class-gridmap-constant-debug-visibility-mode-force-show"></a>

[DebugVisibilityMode](class_gridmap.md#enum-gridmap-debugvisibilitymode) **DEBUG_VISIBILITY_MODE_FORCE_SHOW** = `1`

Always show the collisions debug shapes.

<a id="class-gridmap-constant-debug-visibility-mode-force-hide"></a>

[DebugVisibilityMode](class_gridmap.md#enum-gridmap-debugvisibilitymode) **DEBUG_VISIBILITY_MODE_FORCE_HIDE** = `2`

Always hide the collisions debug shapes.

---


<a id="constants"></a>

## Constants

<a id="class-gridmap-constant-invalid-cell-item"></a>

**INVALID_CELL_ITEM** = `-1` [🔗](class_gridmap.md#class-gridmap-constant-invalid-cell-item)

Invalid cell item that can be used in [set_cell_item()](class_gridmap.md#class-gridmap-method-set-cell-item) to clear cells (or represent an empty cell in [get_cell_item()](class_gridmap.md#class-gridmap-method-get-cell-item)).

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-gridmap-property-bake-navigation"></a>

[bool](class_bool.md#class-bool) **bake_navigation** = `false` [🔗](class_gridmap.md#class-gridmap-property-bake-navigation)

- void **set_bake_navigation**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_baking_navigation**()

If `true`, this GridMap creates a navigation region for each cell that uses a [mesh_library](class_gridmap.md#class-gridmap-property-mesh-library) item with a navigation mesh. The created navigation region will use the navigation layers bitmask assigned to the [MeshLibrary](class_meshlibrary.md#class-meshlibrary)'s item.

---


<a id="class-gridmap-property-cell-center-x"></a>

[bool](class_bool.md#class-bool) **cell_center_x** = `true` [🔗](class_gridmap.md#class-gridmap-property-cell-center-x)

- void **set_center_x**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_center_x**()

If `true`, grid items are centered on the X axis.

---


<a id="class-gridmap-property-cell-center-y"></a>

[bool](class_bool.md#class-bool) **cell_center_y** = `true` [🔗](class_gridmap.md#class-gridmap-property-cell-center-y)

- void **set_center_y**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_center_y**()

If `true`, grid items are centered on the Y axis.

---


<a id="class-gridmap-property-cell-center-z"></a>

[bool](class_bool.md#class-bool) **cell_center_z** = `true` [🔗](class_gridmap.md#class-gridmap-property-cell-center-z)

- void **set_center_z**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_center_z**()

If `true`, grid items are centered on the Z axis.

---


<a id="class-gridmap-property-cell-octant-size"></a>

[int](class_int.md#class-int) **cell_octant_size** = `8` [🔗](class_gridmap.md#class-gridmap-property-cell-octant-size)

- void **set_octant_size**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_octant_size**()

The size of each octant measured in number of cells. This applies to all three axis.

---


<a id="class-gridmap-property-cell-scale"></a>

[float](class_float.md#class-float) **cell_scale** = `1.0` [🔗](class_gridmap.md#class-gridmap-property-cell-scale)

- void **set_cell_scale**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_cell_scale**()

The scale of the cell items.

This does not affect the size of the grid cells themselves, only the items in them. This can be used to make cell items overlap their neighbors.

---


<a id="class-gridmap-property-cell-size"></a>

[Vector3](class_vector3.md#class-vector3) **cell_size** = `Vector3(2, 2, 2)` [🔗](class_gridmap.md#class-gridmap-property-cell-size)

- void **set_cell_size**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_cell_size**()

The dimensions of the grid's cells.

This does not affect the size of the meshes. See [cell_scale](class_gridmap.md#class-gridmap-property-cell-scale).

---


<a id="class-gridmap-property-collision-layer"></a>

[int](class_int.md#class-int) **collision_layer** = `1` [🔗](class_gridmap.md#class-gridmap-property-collision-layer)

- void **set_collision_layer**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_collision_layer**()

The physics layers this GridMap is in.

GridMaps act as static bodies, meaning they aren't affected by gravity or other forces. They only affect other physics bodies that collide with them.

---


<a id="class-gridmap-property-collision-mask"></a>

[int](class_int.md#class-int) **collision_mask** = `1` [🔗](class_gridmap.md#class-gridmap-property-collision-mask)

- void **set_collision_mask**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_collision_mask**()

The physics layers this GridMap detects collisions in. See [Collision layers and masks](../tutorials/physics/physics_introduction.md#collision-layers-and-masks) in the documentation for more information.

---


<a id="class-gridmap-property-collision-priority"></a>

[float](class_float.md#class-float) **collision_priority** = `1.0` [🔗](class_gridmap.md#class-gridmap-property-collision-priority)

- void **set_collision_priority**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_collision_priority**()

The priority used to solve colliding when occurring penetration. The higher the priority is, the lower the penetration into the object will be. This can for example be used to prevent the player from breaking through the boundaries of a level.

---


<a id="class-gridmap-property-collision-visibility-mode"></a>

[DebugVisibilityMode](class_gridmap.md#enum-gridmap-debugvisibilitymode) **collision_visibility_mode** = `0` [🔗](class_gridmap.md#class-gridmap-property-collision-visibility-mode)

- void **set_collision_visibility_mode**(value: [DebugVisibilityMode](class_gridmap.md#enum-gridmap-debugvisibilitymode))
- [DebugVisibilityMode](class_gridmap.md#enum-gridmap-debugvisibilitymode) **get_collision_visibility_mode**()

Show or hide the **GridMap**'s collision shapes. If set to [DEBUG_VISIBILITY_MODE_DEFAULT](class_gridmap.md#class-gridmap-constant-debug-visibility-mode-default), this depends on the show collision debug settings.

---


<a id="class-gridmap-property-mesh-library"></a>

[MeshLibrary](class_meshlibrary.md#class-meshlibrary) **mesh_library** [🔗](class_gridmap.md#class-gridmap-property-mesh-library)

- void **set_mesh_library**(value: [MeshLibrary](class_meshlibrary.md#class-meshlibrary))
- [MeshLibrary](class_meshlibrary.md#class-meshlibrary) **get_mesh_library**()

The assigned [MeshLibrary](class_meshlibrary.md#class-meshlibrary).

---


<a id="class-gridmap-property-physics-material"></a>

[PhysicsMaterial](class_physicsmaterial.md#class-physicsmaterial) **physics_material** [🔗](class_gridmap.md#class-gridmap-property-physics-material)

- void **set_physics_material**(value: [PhysicsMaterial](class_physicsmaterial.md#class-physicsmaterial))
- [PhysicsMaterial](class_physicsmaterial.md#class-physicsmaterial) **get_physics_material**()

Overrides the default friction and bounce physics properties for the whole **GridMap**.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-gridmap-method-clear"></a>

void **clear**() [🔗](class_gridmap.md#class-gridmap-method-clear)

Clear all cells.

---


<a id="class-gridmap-method-clear-baked-meshes"></a>

void **clear_baked_meshes**() [🔗](class_gridmap.md#class-gridmap-method-clear-baked-meshes)

Clears all baked meshes. See [make_baked_meshes()](class_gridmap.md#class-gridmap-method-make-baked-meshes).

---


<a id="class-gridmap-method-get-bake-mesh-instance"></a>

[RID](class_rid.md#class-rid) **get_bake_mesh_instance**(idx: [int](class_int.md#class-int)) [🔗](class_gridmap.md#class-gridmap-method-get-bake-mesh-instance)

Returns [RID](class_rid.md#class-rid) of a baked mesh with the given `idx`.

---


<a id="class-gridmap-method-get-bake-meshes"></a>

[Array](class_array.md#class-array) **get_bake_meshes**() [🔗](class_gridmap.md#class-gridmap-method-get-bake-meshes)

Returns an array of [ArrayMesh](class_arraymesh.md#class-arraymesh)es and [Transform3D](class_transform3d.md#class-transform3d) references of all bake meshes that exist within the current GridMap. Even indices contain [ArrayMesh](class_arraymesh.md#class-arraymesh)es, while odd indices contain [Transform3D](class_transform3d.md#class-transform3d)s that are always equal to [Transform3D.IDENTITY](class_transform3d.md#class-transform3d-constant-identity).

This method relies on the output of [make_baked_meshes()](class_gridmap.md#class-gridmap-method-make-baked-meshes), which will be called with `gen_lightmap_uv` set to `true` and `lightmap_uv_texel_size` set to `0.1` if it hasn't been called yet.

---


<a id="class-gridmap-method-get-basis-with-orthogonal-index"></a>

[Basis](class_basis.md#class-basis) **get_basis_with_orthogonal_index**(index: [int](class_int.md#class-int)) const [🔗](class_gridmap.md#class-gridmap-method-get-basis-with-orthogonal-index)

Returns one of 24 possible rotations that lie along the vectors (x,y,z) with each component being either -1, 0, or 1. For further details, refer to the Godot source code.

---


<a id="class-gridmap-method-get-cell-item"></a>

[int](class_int.md#class-int) **get_cell_item**(position: [Vector3i](class_vector3i.md#class-vector3i)) const [🔗](class_gridmap.md#class-gridmap-method-get-cell-item)

The [MeshLibrary](class_meshlibrary.md#class-meshlibrary) item index located at the given grid coordinates. If the cell is empty, [INVALID_CELL_ITEM](class_gridmap.md#class-gridmap-constant-invalid-cell-item) will be returned.

---


<a id="class-gridmap-method-get-cell-item-basis"></a>

[Basis](class_basis.md#class-basis) **get_cell_item_basis**(position: [Vector3i](class_vector3i.md#class-vector3i)) const [🔗](class_gridmap.md#class-gridmap-method-get-cell-item-basis)

Returns the basis that gives the specified cell its orientation.

---


<a id="class-gridmap-method-get-cell-item-orientation"></a>

[int](class_int.md#class-int) **get_cell_item_orientation**(position: [Vector3i](class_vector3i.md#class-vector3i)) const [🔗](class_gridmap.md#class-gridmap-method-get-cell-item-orientation)

The orientation of the cell at the given grid coordinates. `-1` is returned if the cell is empty.

---


<a id="class-gridmap-method-get-collision-layer-value"></a>

[bool](class_bool.md#class-bool) **get_collision_layer_value**(layer_number: [int](class_int.md#class-int)) const [🔗](class_gridmap.md#class-gridmap-method-get-collision-layer-value)

Returns whether or not the specified layer of the [collision_layer](class_gridmap.md#class-gridmap-property-collision-layer) is enabled, given a `layer_number` between 1 and 32.

---


<a id="class-gridmap-method-get-collision-mask-value"></a>

[bool](class_bool.md#class-bool) **get_collision_mask_value**(layer_number: [int](class_int.md#class-int)) const [🔗](class_gridmap.md#class-gridmap-method-get-collision-mask-value)

Returns whether or not the specified layer of the [collision_mask](class_gridmap.md#class-gridmap-property-collision-mask) is enabled, given a `layer_number` between 1 and 32.

---


<a id="class-gridmap-method-get-meshes"></a>

[Array](class_array.md#class-array) **get_meshes**() const [🔗](class_gridmap.md#class-gridmap-method-get-meshes)

Returns an array of [Transform3D](class_transform3d.md#class-transform3d) and [Mesh](class_mesh.md#class-mesh) references corresponding to the non-empty cells in the grid. The transforms are specified in local space. Even indices contain [Transform3D](class_transform3d.md#class-transform3d)s, while odd indices contain [Mesh](class_mesh.md#class-mesh)es related to the [Transform3D](class_transform3d.md#class-transform3d) in the index preceding it.

---


<a id="class-gridmap-method-get-navigation-map"></a>

[RID](class_rid.md#class-rid) **get_navigation_map**() const [🔗](class_gridmap.md#class-gridmap-method-get-navigation-map)

Returns the [RID](class_rid.md#class-rid) of the navigation map this GridMap node uses for its cell baked navigation meshes.

This function returns always the map set on the GridMap node and not the map on the NavigationServer. If the map is changed directly with the NavigationServer API the GridMap node will not be aware of the map change.

---


<a id="class-gridmap-method-get-octant-coords-from-cell-coords"></a>

[Vector3i](class_vector3i.md#class-vector3i) **get_octant_coords_from_cell_coords**(cell_coords: [Vector3i](class_vector3i.md#class-vector3i)) const [🔗](class_gridmap.md#class-gridmap-method-get-octant-coords-from-cell-coords)

Returns the [Vector3i](class_vector3i.md#class-vector3i) octant coordinates of the octant that the cell at `cell_coords` belongs to.

---


<a id="class-gridmap-method-get-octants-in-bounds"></a>

[Array](class_array.md#class-array)[[Vector3i](class_vector3i.md#class-vector3i)] **get_octants_in_bounds**(bounds: [AABB](class_aabb.md#class-aabb)) const [🔗](class_gridmap.md#class-gridmap-method-get-octants-in-bounds)

Returns an array of [Vector3i](class_vector3i.md#class-vector3i) octant coordinates that are inside the given `bounds`, including octants that have no cells in use.

---


<a id="class-gridmap-method-get-orthogonal-index-from-basis"></a>

[int](class_int.md#class-int) **get_orthogonal_index_from_basis**(basis: [Basis](class_basis.md#class-basis)) const [🔗](class_gridmap.md#class-gridmap-method-get-orthogonal-index-from-basis)

This function considers a discretization of rotations into 24 points on unit sphere, lying along the vectors (x,y,z) with each component being either -1, 0, or 1, and returns the index (in the range from 0 to 23) of the point best representing the orientation of the object. For further details, refer to the Godot source code.

---


<a id="class-gridmap-method-get-used-cells"></a>

[Array](class_array.md#class-array)[[Vector3i](class_vector3i.md#class-vector3i)] **get_used_cells**() const [🔗](class_gridmap.md#class-gridmap-method-get-used-cells)

Returns an array of [Vector3](class_vector3.md#class-vector3) with the non-empty cell coordinates in the grid map.

---


<a id="class-gridmap-method-get-used-cells-by-item"></a>

[Array](class_array.md#class-array)[[Vector3i](class_vector3i.md#class-vector3i)] **get_used_cells_by_item**(item: [int](class_int.md#class-int)) const [🔗](class_gridmap.md#class-gridmap-method-get-used-cells-by-item)

Returns an array of all cells with the given item index specified in `item`.

---


<a id="class-gridmap-method-get-used-cells-in-octant"></a>

[Array](class_array.md#class-array)[[Vector3i](class_vector3i.md#class-vector3i)] **get_used_cells_in_octant**(octant_coords: [Vector3i](class_vector3i.md#class-vector3i)) const [🔗](class_gridmap.md#class-gridmap-method-get-used-cells-in-octant)

Returns an array of [Vector3i](class_vector3i.md#class-vector3i)s with the cell coordinates of non-empty cells inside the octant at `octant_coords`.

---


<a id="class-gridmap-method-get-used-cells-in-octant-by-item"></a>

[Array](class_array.md#class-array)[[Vector3i](class_vector3i.md#class-vector3i)] **get_used_cells_in_octant_by_item**(octant_coords: [Vector3i](class_vector3i.md#class-vector3i), item: [int](class_int.md#class-int)) const [🔗](class_gridmap.md#class-gridmap-method-get-used-cells-in-octant-by-item)

Returns an array of [Vector3i](class_vector3i.md#class-vector3i)s with the cell coordinates of cells inside the octant at `octant_coords` that use the specified cell `item`.

---


<a id="class-gridmap-method-get-used-octants"></a>

[Array](class_array.md#class-array)[[Vector3i](class_vector3i.md#class-vector3i)] **get_used_octants**() const [🔗](class_gridmap.md#class-gridmap-method-get-used-octants)

Returns an array of [Vector3i](class_vector3i.md#class-vector3i)s with the octant coordinates of the non-empty octants in the grid map.

---


<a id="class-gridmap-method-get-used-octants-by-item"></a>

[Array](class_array.md#class-array)[[Vector3i](class_vector3i.md#class-vector3i)] **get_used_octants_by_item**(item: [int](class_int.md#class-int)) const [🔗](class_gridmap.md#class-gridmap-method-get-used-octants-by-item)

Returns an array of [Vector3i](class_vector3i.md#class-vector3i)s with the octant coordinates of the octants that use the specified `item` in the grid map.

---


<a id="class-gridmap-method-get-used-octants-in-bounds"></a>

[Array](class_array.md#class-array)[[Vector3i](class_vector3i.md#class-vector3i)] **get_used_octants_in_bounds**(bounds: [AABB](class_aabb.md#class-aabb)) const [🔗](class_gridmap.md#class-gridmap-method-get-used-octants-in-bounds)

Returns an array of [Vector3i](class_vector3i.md#class-vector3i)s with the octant coordinates of non-empty octants that are inside the local `bounds`.

---


<a id="class-gridmap-method-local-to-map"></a>

[Vector3i](class_vector3i.md#class-vector3i) **local_to_map**(local_position: [Vector3](class_vector3.md#class-vector3)) const [🔗](class_gridmap.md#class-gridmap-method-local-to-map)

Returns the map coordinates of the cell containing the given `local_position`. If `local_position` is in global coordinates, consider using [Node3D.to_local()](class_node3d.md#class-node3d-method-to-local) before passing it to this method. See also [map_to_local()](class_gridmap.md#class-gridmap-method-map-to-local).

---


<a id="class-gridmap-method-make-baked-meshes"></a>

void **make_baked_meshes**(gen_lightmap_uv: [bool](class_bool.md#class-bool) = false, lightmap_uv_texel_size: [float](class_float.md#class-float) = 0.1) [🔗](class_gridmap.md#class-gridmap-method-make-baked-meshes)

Generates a baked mesh that represents all meshes in the assigned [MeshLibrary](class_meshlibrary.md#class-meshlibrary) for use with [LightmapGI](class_lightmapgi.md#class-lightmapgi). If `gen_lightmap_uv` is `true`, UV2 data will be generated for each mesh currently used in the **GridMap**. Otherwise, only meshes that already have UV2 data present will be able to use baked lightmaps. When generating UV2, `lightmap_uv_texel_size` controls the texel density for lightmaps, with lower values resulting in more detailed lightmaps. `lightmap_uv_texel_size` is ignored if `gen_lightmap_uv` is `false`. See also [get_bake_meshes()](class_gridmap.md#class-gridmap-method-get-bake-meshes), which relies on the output of this method.

**Note:** Calling this method will not actually bake lightmaps, as lightmap baking is performed using the [LightmapGI](class_lightmapgi.md#class-lightmapgi) node.

---


<a id="class-gridmap-method-map-to-local"></a>

[Vector3](class_vector3.md#class-vector3) **map_to_local**(map_position: [Vector3i](class_vector3i.md#class-vector3i)) const [🔗](class_gridmap.md#class-gridmap-method-map-to-local)

Returns the position of a grid cell in the GridMap's local coordinate space. To convert the returned value into global coordinates, use [Node3D.to_global()](class_node3d.md#class-node3d-method-to-global). See also [local_to_map()](class_gridmap.md#class-gridmap-method-local-to-map).

---


<a id="class-gridmap-method-resource-changed"></a>

void **resource_changed**(resource: [Resource](class_resource.md#class-resource)) [🔗](class_gridmap.md#class-gridmap-method-resource-changed)

**Deprecated:** Use [Resource.changed](class_resource.md#class-resource-signal-changed) instead.

This method does nothing.

---


<a id="class-gridmap-method-set-cell-item"></a>

void **set_cell_item**(position: [Vector3i](class_vector3i.md#class-vector3i), item: [int](class_int.md#class-int), orientation: [int](class_int.md#class-int) = 0) [🔗](class_gridmap.md#class-gridmap-method-set-cell-item)

Sets the mesh index for the cell referenced by its grid coordinates.

A negative item index such as [INVALID_CELL_ITEM](class_gridmap.md#class-gridmap-constant-invalid-cell-item) will clear the cell.

Optionally, the item's orientation can be passed. For valid orientation values, see [get_orthogonal_index_from_basis()](class_gridmap.md#class-gridmap-method-get-orthogonal-index-from-basis).

---


<a id="class-gridmap-method-set-collision-layer-value"></a>

void **set_collision_layer_value**(layer_number: [int](class_int.md#class-int), value: [bool](class_bool.md#class-bool)) [🔗](class_gridmap.md#class-gridmap-method-set-collision-layer-value)

Based on `value`, enables or disables the specified layer in the [collision_layer](class_gridmap.md#class-gridmap-property-collision-layer), given a `layer_number` between 1 and 32.

---


<a id="class-gridmap-method-set-collision-mask-value"></a>

void **set_collision_mask_value**(layer_number: [int](class_int.md#class-int), value: [bool](class_bool.md#class-bool)) [🔗](class_gridmap.md#class-gridmap-method-set-collision-mask-value)

Based on `value`, enables or disables the specified layer in the [collision_mask](class_gridmap.md#class-gridmap-property-collision-mask), given a `layer_number` between 1 and 32.

---


<a id="class-gridmap-method-set-navigation-map"></a>

void **set_navigation_map**(navigation_map: [RID](class_rid.md#class-rid)) [🔗](class_gridmap.md#class-gridmap-method-set-navigation-map)

Sets the [RID](class_rid.md#class-rid) of the navigation map this GridMap node should use for its cell baked navigation meshes.
