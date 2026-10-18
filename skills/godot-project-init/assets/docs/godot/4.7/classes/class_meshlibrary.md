> Source: https://docs.godotengine.org/en/4.7/classes/class_meshlibrary.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="meshlibrary"></a>

<a id="class-meshlibrary"></a>

# MeshLibrary

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Library of meshes.

<a id="description"></a>

## Description

A library of meshes. Contains a list of [Mesh](class_mesh.md#class-mesh) resources, each with a name and ID. Each item can also include collision and navigation shapes. This resource is used in [GridMap](class_gridmap.md#class-gridmap).

<a id="tutorials"></a>

## Tutorials

- [3D Kinematic Character Demo](https://godotengine.org/asset-library/asset/2739)
- [3D Platformer Demo](https://godotengine.org/asset-library/asset/2748)

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [clear](class_meshlibrary.md#class-meshlibrary-method-clear)() |
| void | [create_item](class_meshlibrary.md#class-meshlibrary-method-create-item)(id: [int](class_int.md#class-int)) |
| [int](class_int.md#class-int) | [find_item_by_name](class_meshlibrary.md#class-meshlibrary-method-find-item-by-name)(name: [String](class_string.md#class-string)) const |
| [int](class_int.md#class-int) | [get_item_count](class_meshlibrary.md#class-meshlibrary-method-get-item-count)() const |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array) | [get_item_list](class_meshlibrary.md#class-meshlibrary-method-get-item-list)() const |
| [Mesh](class_mesh.md#class-mesh) | [get_item_mesh](class_meshlibrary.md#class-meshlibrary-method-get-item-mesh)(id: [int](class_int.md#class-int)) const |
| [ShadowCastingSetting](class_renderingserver.md#enum-renderingserver-shadowcastingsetting) | [get_item_mesh_cast_shadow](class_meshlibrary.md#class-meshlibrary-method-get-item-mesh-cast-shadow)(id: [int](class_int.md#class-int)) const |
| [Transform3D](class_transform3d.md#class-transform3d) | [get_item_mesh_transform](class_meshlibrary.md#class-meshlibrary-method-get-item-mesh-transform)(id: [int](class_int.md#class-int)) const |
| [String](class_string.md#class-string) | [get_item_name](class_meshlibrary.md#class-meshlibrary-method-get-item-name)(id: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_item_navigation_layers](class_meshlibrary.md#class-meshlibrary-method-get-item-navigation-layers)(id: [int](class_int.md#class-int)) const |
| [NavigationMesh](class_navigationmesh.md#class-navigationmesh) | [get_item_navigation_mesh](class_meshlibrary.md#class-meshlibrary-method-get-item-navigation-mesh)(id: [int](class_int.md#class-int)) const |
| [Transform3D](class_transform3d.md#class-transform3d) | [get_item_navigation_mesh_transform](class_meshlibrary.md#class-meshlibrary-method-get-item-navigation-mesh-transform)(id: [int](class_int.md#class-int)) const |
| [Texture2D](class_texture2d.md#class-texture2d) | [get_item_preview](class_meshlibrary.md#class-meshlibrary-method-get-item-preview)(id: [int](class_int.md#class-int)) const |
| [Array](class_array.md#class-array) | [get_item_shapes](class_meshlibrary.md#class-meshlibrary-method-get-item-shapes)(id: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_last_unused_item_id](class_meshlibrary.md#class-meshlibrary-method-get-last-unused-item-id)() const |
| void | [remove_item](class_meshlibrary.md#class-meshlibrary-method-remove-item)(id: [int](class_int.md#class-int)) |
| void | [set_item_mesh](class_meshlibrary.md#class-meshlibrary-method-set-item-mesh)(id: [int](class_int.md#class-int), mesh: [Mesh](class_mesh.md#class-mesh)) |
| void | [set_item_mesh_cast_shadow](class_meshlibrary.md#class-meshlibrary-method-set-item-mesh-cast-shadow)(id: [int](class_int.md#class-int), shadow_casting_setting: [ShadowCastingSetting](class_renderingserver.md#enum-renderingserver-shadowcastingsetting)) |
| void | [set_item_mesh_transform](class_meshlibrary.md#class-meshlibrary-method-set-item-mesh-transform)(id: [int](class_int.md#class-int), mesh_transform: [Transform3D](class_transform3d.md#class-transform3d)) |
| void | [set_item_name](class_meshlibrary.md#class-meshlibrary-method-set-item-name)(id: [int](class_int.md#class-int), name: [String](class_string.md#class-string)) |
| void | [set_item_navigation_layers](class_meshlibrary.md#class-meshlibrary-method-set-item-navigation-layers)(id: [int](class_int.md#class-int), navigation_layers: [int](class_int.md#class-int)) |
| void | [set_item_navigation_mesh](class_meshlibrary.md#class-meshlibrary-method-set-item-navigation-mesh)(id: [int](class_int.md#class-int), navigation_mesh: [NavigationMesh](class_navigationmesh.md#class-navigationmesh)) |
| void | [set_item_navigation_mesh_transform](class_meshlibrary.md#class-meshlibrary-method-set-item-navigation-mesh-transform)(id: [int](class_int.md#class-int), navigation_mesh: [Transform3D](class_transform3d.md#class-transform3d)) |
| void | [set_item_preview](class_meshlibrary.md#class-meshlibrary-method-set-item-preview)(id: [int](class_int.md#class-int), texture: [Texture2D](class_texture2d.md#class-texture2d)) |
| void | [set_item_shapes](class_meshlibrary.md#class-meshlibrary-method-set-item-shapes)(id: [int](class_int.md#class-int), shapes: [Array](class_array.md#class-array)) |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-meshlibrary-method-clear"></a>

void **clear**() [🔗](class_meshlibrary.md#class-meshlibrary-method-clear)

Clears the library.

---


<a id="class-meshlibrary-method-create-item"></a>

void **create_item**(id: [int](class_int.md#class-int)) [🔗](class_meshlibrary.md#class-meshlibrary-method-create-item)

Creates a new item in the library with the given ID.

You can get an unused ID from [get_last_unused_item_id()](class_meshlibrary.md#class-meshlibrary-method-get-last-unused-item-id).

---


<a id="class-meshlibrary-method-find-item-by-name"></a>

[int](class_int.md#class-int) **find_item_by_name**(name: [String](class_string.md#class-string)) const [🔗](class_meshlibrary.md#class-meshlibrary-method-find-item-by-name)

Returns the first item with the given name, or `-1` if no item is found.

---


<a id="class-meshlibrary-method-get-item-count"></a>

[int](class_int.md#class-int) **get_item_count**() const [🔗](class_meshlibrary.md#class-meshlibrary-method-get-item-count)

Returns the number of items present in the library.

---


<a id="class-meshlibrary-method-get-item-list"></a>

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_item_list**() const [🔗](class_meshlibrary.md#class-meshlibrary-method-get-item-list)

Returns the list of item IDs in use.

---


<a id="class-meshlibrary-method-get-item-mesh"></a>

[Mesh](class_mesh.md#class-mesh) **get_item_mesh**(id: [int](class_int.md#class-int)) const [🔗](class_meshlibrary.md#class-meshlibrary-method-get-item-mesh)

Returns the item's mesh.

---


<a id="class-meshlibrary-method-get-item-mesh-cast-shadow"></a>

[ShadowCastingSetting](class_renderingserver.md#enum-renderingserver-shadowcastingsetting) **get_item_mesh_cast_shadow**(id: [int](class_int.md#class-int)) const [🔗](class_meshlibrary.md#class-meshlibrary-method-get-item-mesh-cast-shadow)

Returns the item's shadow casting mode.

---


<a id="class-meshlibrary-method-get-item-mesh-transform"></a>

[Transform3D](class_transform3d.md#class-transform3d) **get_item_mesh_transform**(id: [int](class_int.md#class-int)) const [🔗](class_meshlibrary.md#class-meshlibrary-method-get-item-mesh-transform)

Returns the transform applied to the item's mesh.

---


<a id="class-meshlibrary-method-get-item-name"></a>

[String](class_string.md#class-string) **get_item_name**(id: [int](class_int.md#class-int)) const [🔗](class_meshlibrary.md#class-meshlibrary-method-get-item-name)

Returns the item's name.

---


<a id="class-meshlibrary-method-get-item-navigation-layers"></a>

[int](class_int.md#class-int) **get_item_navigation_layers**(id: [int](class_int.md#class-int)) const [🔗](class_meshlibrary.md#class-meshlibrary-method-get-item-navigation-layers)

Returns the item's navigation layers bitmask.

---


<a id="class-meshlibrary-method-get-item-navigation-mesh"></a>

[NavigationMesh](class_navigationmesh.md#class-navigationmesh) **get_item_navigation_mesh**(id: [int](class_int.md#class-int)) const [🔗](class_meshlibrary.md#class-meshlibrary-method-get-item-navigation-mesh)

Returns the item's navigation mesh.

---


<a id="class-meshlibrary-method-get-item-navigation-mesh-transform"></a>

[Transform3D](class_transform3d.md#class-transform3d) **get_item_navigation_mesh_transform**(id: [int](class_int.md#class-int)) const [🔗](class_meshlibrary.md#class-meshlibrary-method-get-item-navigation-mesh-transform)

Returns the transform applied to the item's navigation mesh.

---


<a id="class-meshlibrary-method-get-item-preview"></a>

[Texture2D](class_texture2d.md#class-texture2d) **get_item_preview**(id: [int](class_int.md#class-int)) const [🔗](class_meshlibrary.md#class-meshlibrary-method-get-item-preview)

When running in the editor, returns a generated item preview (a 3D rendering in isometric perspective). When used in a running project, returns the manually-defined item preview which can be set using [set_item_preview()](class_meshlibrary.md#class-meshlibrary-method-set-item-preview). Returns an empty [Texture2D](class_texture2d.md#class-texture2d) if no preview was manually set in a running project.

---


<a id="class-meshlibrary-method-get-item-shapes"></a>

[Array](class_array.md#class-array) **get_item_shapes**(id: [int](class_int.md#class-int)) const [🔗](class_meshlibrary.md#class-meshlibrary-method-get-item-shapes)

Returns an item's collision shapes.

The array consists of each [Shape3D](class_shape3d.md#class-shape3d) followed by its [Transform3D](class_transform3d.md#class-transform3d).

---


<a id="class-meshlibrary-method-get-last-unused-item-id"></a>

[int](class_int.md#class-int) **get_last_unused_item_id**() const [🔗](class_meshlibrary.md#class-meshlibrary-method-get-last-unused-item-id)

Gets an unused ID for a new item.

---


<a id="class-meshlibrary-method-remove-item"></a>

void **remove_item**(id: [int](class_int.md#class-int)) [🔗](class_meshlibrary.md#class-meshlibrary-method-remove-item)

Removes the item.

---


<a id="class-meshlibrary-method-set-item-mesh"></a>

void **set_item_mesh**(id: [int](class_int.md#class-int), mesh: [Mesh](class_mesh.md#class-mesh)) [🔗](class_meshlibrary.md#class-meshlibrary-method-set-item-mesh)

Sets the item's mesh.

---


<a id="class-meshlibrary-method-set-item-mesh-cast-shadow"></a>

void **set_item_mesh_cast_shadow**(id: [int](class_int.md#class-int), shadow_casting_setting: [ShadowCastingSetting](class_renderingserver.md#enum-renderingserver-shadowcastingsetting)) [🔗](class_meshlibrary.md#class-meshlibrary-method-set-item-mesh-cast-shadow)

Sets the item's shadow casting mode to `shadow_casting_setting`.

---


<a id="class-meshlibrary-method-set-item-mesh-transform"></a>

void **set_item_mesh_transform**(id: [int](class_int.md#class-int), mesh_transform: [Transform3D](class_transform3d.md#class-transform3d)) [🔗](class_meshlibrary.md#class-meshlibrary-method-set-item-mesh-transform)

Sets the transform to apply to the item's mesh.

---


<a id="class-meshlibrary-method-set-item-name"></a>

void **set_item_name**(id: [int](class_int.md#class-int), name: [String](class_string.md#class-string)) [🔗](class_meshlibrary.md#class-meshlibrary-method-set-item-name)

Sets the item's name.

This name is shown in the editor. It can also be used to look up the item later using [find_item_by_name()](class_meshlibrary.md#class-meshlibrary-method-find-item-by-name).

---


<a id="class-meshlibrary-method-set-item-navigation-layers"></a>

void **set_item_navigation_layers**(id: [int](class_int.md#class-int), navigation_layers: [int](class_int.md#class-int)) [🔗](class_meshlibrary.md#class-meshlibrary-method-set-item-navigation-layers)

Sets the item's navigation layers bitmask.

---


<a id="class-meshlibrary-method-set-item-navigation-mesh"></a>

void **set_item_navigation_mesh**(id: [int](class_int.md#class-int), navigation_mesh: [NavigationMesh](class_navigationmesh.md#class-navigationmesh)) [🔗](class_meshlibrary.md#class-meshlibrary-method-set-item-navigation-mesh)

Sets the item's navigation mesh.

---


<a id="class-meshlibrary-method-set-item-navigation-mesh-transform"></a>

void **set_item_navigation_mesh_transform**(id: [int](class_int.md#class-int), navigation_mesh: [Transform3D](class_transform3d.md#class-transform3d)) [🔗](class_meshlibrary.md#class-meshlibrary-method-set-item-navigation-mesh-transform)

Sets the transform to apply to the item's navigation mesh.

---


<a id="class-meshlibrary-method-set-item-preview"></a>

void **set_item_preview**(id: [int](class_int.md#class-int), texture: [Texture2D](class_texture2d.md#class-texture2d)) [🔗](class_meshlibrary.md#class-meshlibrary-method-set-item-preview)

Sets a texture to use as the item's preview icon in the editor.

---


<a id="class-meshlibrary-method-set-item-shapes"></a>

void **set_item_shapes**(id: [int](class_int.md#class-int), shapes: [Array](class_array.md#class-array)) [🔗](class_meshlibrary.md#class-meshlibrary-method-set-item-shapes)

Sets an item's collision shapes.

The array should consist of [Shape3D](class_shape3d.md#class-shape3d) objects, each followed by a [Transform3D](class_transform3d.md#class-transform3d) that will be applied to it. For shapes that should not have a transform, use [Transform3D.IDENTITY](class_transform3d.md#class-transform3d-constant-identity).
