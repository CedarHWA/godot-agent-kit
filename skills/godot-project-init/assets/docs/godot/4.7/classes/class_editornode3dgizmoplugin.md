> Source: https://docs.godotengine.org/en/4.7/classes/class_editornode3dgizmoplugin.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="editornode3dgizmoplugin"></a>

<a id="class-editornode3dgizmoplugin"></a>

# EditorNode3DGizmoPlugin

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A class used by the editor to define Node3D gizmo types.

<a id="description"></a>

## Description

**EditorNode3DGizmoPlugin** allows you to define a new type of Gizmo. There are two main ways to do so: extending **EditorNode3DGizmoPlugin** for the simpler gizmos, or creating a new [EditorNode3DGizmo](class_editornode3dgizmo.md#class-editornode3dgizmo) type. See the tutorial in the documentation for more info.

To use **EditorNode3DGizmoPlugin**, register it using the [EditorPlugin.add_node_3d_gizmo_plugin()](class_editorplugin.md#class-editorplugin-method-add-node-3d-gizmo-plugin) method first.

<a id="tutorials"></a>

## Tutorials

- [Node3D gizmo plugins](../tutorials/plugins/editor/3d_gizmos.md)

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [_begin_handle_action](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-begin-handle-action)(gizmo: [EditorNode3DGizmo](class_editornode3dgizmo.md#class-editornode3dgizmo), handle_id: [int](class_int.md#class-int), secondary: [bool](class_bool.md#class-bool)) virtual |
| [bool](class_bool.md#class-bool) | [_can_be_hidden](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-can-be-hidden)() virtual const |
| [bool](class_bool.md#class-bool) | [_can_commit_handle_on_click](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-can-commit-handle-on-click)() virtual const |
| void | [_commit_handle](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-commit-handle)(gizmo: [EditorNode3DGizmo](class_editornode3dgizmo.md#class-editornode3dgizmo), handle_id: [int](class_int.md#class-int), secondary: [bool](class_bool.md#class-bool), restore: [Variant](class_variant.md#class-variant), cancel: [bool](class_bool.md#class-bool)) virtual |
| void | [_commit_subgizmos](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-commit-subgizmos)(gizmo: [EditorNode3DGizmo](class_editornode3dgizmo.md#class-editornode3dgizmo), ids: [PackedInt32Array](class_packedint32array.md#class-packedint32array), restores: [Array](class_array.md#class-array)[[Transform3D](class_transform3d.md#class-transform3d)], cancel: [bool](class_bool.md#class-bool)) virtual |
| [EditorNode3DGizmo](class_editornode3dgizmo.md#class-editornode3dgizmo) | [_create_gizmo](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-create-gizmo)(for_node_3d: [Node3D](class_node3d.md#class-node3d)) virtual const |
| [String](class_string.md#class-string) | [_get_gizmo_name](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-get-gizmo-name)() virtual const |
| [String](class_string.md#class-string) | [_get_handle_name](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-get-handle-name)(gizmo: [EditorNode3DGizmo](class_editornode3dgizmo.md#class-editornode3dgizmo), handle_id: [int](class_int.md#class-int), secondary: [bool](class_bool.md#class-bool)) virtual const |
| [Variant](class_variant.md#class-variant) | [_get_handle_value](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-get-handle-value)(gizmo: [EditorNode3DGizmo](class_editornode3dgizmo.md#class-editornode3dgizmo), handle_id: [int](class_int.md#class-int), secondary: [bool](class_bool.md#class-bool)) virtual const |
| [int](class_int.md#class-int) | [_get_priority](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-get-priority)() virtual const |
| [Transform3D](class_transform3d.md#class-transform3d) | [_get_subgizmo_transform](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-get-subgizmo-transform)(gizmo: [EditorNode3DGizmo](class_editornode3dgizmo.md#class-editornode3dgizmo), subgizmo_id: [int](class_int.md#class-int)) virtual const |
| [bool](class_bool.md#class-bool) | [_has_gizmo](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-has-gizmo)(for_node_3d: [Node3D](class_node3d.md#class-node3d)) virtual const |
| [bool](class_bool.md#class-bool) | [_is_handle_highlighted](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-is-handle-highlighted)(gizmo: [EditorNode3DGizmo](class_editornode3dgizmo.md#class-editornode3dgizmo), handle_id: [int](class_int.md#class-int), secondary: [bool](class_bool.md#class-bool)) virtual const |
| [bool](class_bool.md#class-bool) | [_is_selectable_when_hidden](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-is-selectable-when-hidden)() virtual const |
| void | [_redraw](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-redraw)(gizmo: [EditorNode3DGizmo](class_editornode3dgizmo.md#class-editornode3dgizmo)) virtual |
| void | [_set_handle](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-set-handle)(gizmo: [EditorNode3DGizmo](class_editornode3dgizmo.md#class-editornode3dgizmo), handle_id: [int](class_int.md#class-int), secondary: [bool](class_bool.md#class-bool), camera: [Camera3D](class_camera3d.md#class-camera3d), screen_pos: [Vector2](class_vector2.md#class-vector2)) virtual |
| void | [_set_subgizmo_transform](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-set-subgizmo-transform)(gizmo: [EditorNode3DGizmo](class_editornode3dgizmo.md#class-editornode3dgizmo), subgizmo_id: [int](class_int.md#class-int), transform: [Transform3D](class_transform3d.md#class-transform3d)) virtual |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array) | [_subgizmos_intersect_frustum](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-subgizmos-intersect-frustum)(gizmo: [EditorNode3DGizmo](class_editornode3dgizmo.md#class-editornode3dgizmo), camera: [Camera3D](class_camera3d.md#class-camera3d), frustum_planes: [Array](class_array.md#class-array)[[Plane](class_plane.md#class-plane)]) virtual const |
| [int](class_int.md#class-int) | [_subgizmos_intersect_ray](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-subgizmos-intersect-ray)(gizmo: [EditorNode3DGizmo](class_editornode3dgizmo.md#class-editornode3dgizmo), camera: [Camera3D](class_camera3d.md#class-camera3d), screen_pos: [Vector2](class_vector2.md#class-vector2)) virtual const |
| void | [add_material](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-method-add-material)(name: [String](class_string.md#class-string), material: [StandardMaterial3D](class_standardmaterial3d.md#class-standardmaterial3d)) |
| void | [create_handle_material](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-method-create-handle-material)(name: [String](class_string.md#class-string), billboard: [bool](class_bool.md#class-bool) = false, texture: [Texture2D](class_texture2d.md#class-texture2d) = null) |
| void | [create_icon_material](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-method-create-icon-material)(name: [String](class_string.md#class-string), texture: [Texture2D](class_texture2d.md#class-texture2d), on_top: [bool](class_bool.md#class-bool) = false, color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1)) |
| void | [create_material](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-method-create-material)(name: [String](class_string.md#class-string), color: [Color](class_color.md#class-color), billboard: [bool](class_bool.md#class-bool) = false, on_top: [bool](class_bool.md#class-bool) = false, use_vertex_color: [bool](class_bool.md#class-bool) = false) |
| [StandardMaterial3D](class_standardmaterial3d.md#class-standardmaterial3d) | [get_material](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-method-get-material)(name: [String](class_string.md#class-string), gizmo: [EditorNode3DGizmo](class_editornode3dgizmo.md#class-editornode3dgizmo) = null) |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-editornode3dgizmoplugin-private-method-begin-handle-action"></a>

void **_begin_handle_action**(gizmo: [EditorNode3DGizmo](class_editornode3dgizmo.md#class-editornode3dgizmo), handle_id: [int](class_int.md#class-int), secondary: [bool](class_bool.md#class-bool)) virtual [🔗](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-begin-handle-action)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-editornode3dgizmoplugin-private-method-can-be-hidden"></a>

[bool](class_bool.md#class-bool) **_can_be_hidden**() virtual const [🔗](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-can-be-hidden)

Override this method to define whether the gizmos handled by this plugin can be hidden or not. Returns `true` if not overridden.

---


<a id="class-editornode3dgizmoplugin-private-method-can-commit-handle-on-click"></a>

[bool](class_bool.md#class-bool) **_can_commit_handle_on_click**() virtual const [🔗](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-can-commit-handle-on-click)

Override this method to define whether the gizmos should commit when the final handle position is the same as the initial one. Returns `false` if not overridden.

---


<a id="class-editornode3dgizmoplugin-private-method-commit-handle"></a>

void **_commit_handle**(gizmo: [EditorNode3DGizmo](class_editornode3dgizmo.md#class-editornode3dgizmo), handle_id: [int](class_int.md#class-int), secondary: [bool](class_bool.md#class-bool), restore: [Variant](class_variant.md#class-variant), cancel: [bool](class_bool.md#class-bool)) virtual [🔗](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-commit-handle)

Override this method to commit a handle being edited (handles must have been previously added by [EditorNode3DGizmo.add_handles()](class_editornode3dgizmo.md#class-editornode3dgizmo-method-add-handles) during [_redraw()](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-redraw)). This usually means creating an [UndoRedo](class_undoredo.md#class-undoredo) action for the change, using the current handle value as "do" and the `restore` argument as "undo".

If the `cancel` argument is `true`, the `restore` value should be directly set, without any [UndoRedo](class_undoredo.md#class-undoredo) action.

The `secondary` argument is `true` when the committed handle is secondary (see [EditorNode3DGizmo.add_handles()](class_editornode3dgizmo.md#class-editornode3dgizmo-method-add-handles) for more information).

Called for this plugin's active gizmos.

---


<a id="class-editornode3dgizmoplugin-private-method-commit-subgizmos"></a>

void **_commit_subgizmos**(gizmo: [EditorNode3DGizmo](class_editornode3dgizmo.md#class-editornode3dgizmo), ids: [PackedInt32Array](class_packedint32array.md#class-packedint32array), restores: [Array](class_array.md#class-array)[[Transform3D](class_transform3d.md#class-transform3d)], cancel: [bool](class_bool.md#class-bool)) virtual [🔗](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-commit-subgizmos)

Override this method to commit a group of subgizmos being edited (see [_subgizmos_intersect_ray()](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-subgizmos-intersect-ray) and [_subgizmos_intersect_frustum()](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-subgizmos-intersect-frustum)). This usually means creating an [UndoRedo](class_undoredo.md#class-undoredo) action for the change, using the current transforms as "do" and the `restores` transforms as "undo".

If the `cancel` argument is `true`, the `restores` transforms should be directly set, without any [UndoRedo](class_undoredo.md#class-undoredo) action. As with all subgizmo methods, transforms are given in local space respect to the gizmo's Node3D. Called for this plugin's active gizmos.

---


<a id="class-editornode3dgizmoplugin-private-method-create-gizmo"></a>

[EditorNode3DGizmo](class_editornode3dgizmo.md#class-editornode3dgizmo) **_create_gizmo**(for_node_3d: [Node3D](class_node3d.md#class-node3d)) virtual const [🔗](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-create-gizmo)

Override this method to return a custom [EditorNode3DGizmo](class_editornode3dgizmo.md#class-editornode3dgizmo) for the 3D nodes of your choice, return `null` for the rest of nodes. See also [_has_gizmo()](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-has-gizmo).

---


<a id="class-editornode3dgizmoplugin-private-method-get-gizmo-name"></a>

[String](class_string.md#class-string) **_get_gizmo_name**() virtual const [🔗](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-get-gizmo-name)

Override this method to provide the name that will appear in the gizmo visibility menu.

---


<a id="class-editornode3dgizmoplugin-private-method-get-handle-name"></a>

[String](class_string.md#class-string) **_get_handle_name**(gizmo: [EditorNode3DGizmo](class_editornode3dgizmo.md#class-editornode3dgizmo), handle_id: [int](class_int.md#class-int), secondary: [bool](class_bool.md#class-bool)) virtual const [🔗](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-get-handle-name)

Override this method to provide gizmo's handle names. The `secondary` argument is `true` when the requested handle is secondary (see [EditorNode3DGizmo.add_handles()](class_editornode3dgizmo.md#class-editornode3dgizmo-method-add-handles) for more information). Called for this plugin's active gizmos.

---


<a id="class-editornode3dgizmoplugin-private-method-get-handle-value"></a>

[Variant](class_variant.md#class-variant) **_get_handle_value**(gizmo: [EditorNode3DGizmo](class_editornode3dgizmo.md#class-editornode3dgizmo), handle_id: [int](class_int.md#class-int), secondary: [bool](class_bool.md#class-bool)) virtual const [🔗](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-get-handle-value)

Override this method to return the current value of a handle. This value will be requested at the start of an edit and used as the `restore` argument in [_commit_handle()](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-commit-handle).

The `secondary` argument is `true` when the requested handle is secondary (see [EditorNode3DGizmo.add_handles()](class_editornode3dgizmo.md#class-editornode3dgizmo-method-add-handles) for more information).

Called for this plugin's active gizmos.

---


<a id="class-editornode3dgizmoplugin-private-method-get-priority"></a>

[int](class_int.md#class-int) **_get_priority**() virtual const [🔗](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-get-priority)

Override this method to set the gizmo's priority. Gizmos with higher priority will have precedence when processing inputs like handles or subgizmos selection.

All built-in editor gizmos return a priority of `-1`. If not overridden, this method will return `0`, which means custom gizmos will automatically get higher priority than built-in gizmos.

---


<a id="class-editornode3dgizmoplugin-private-method-get-subgizmo-transform"></a>

[Transform3D](class_transform3d.md#class-transform3d) **_get_subgizmo_transform**(gizmo: [EditorNode3DGizmo](class_editornode3dgizmo.md#class-editornode3dgizmo), subgizmo_id: [int](class_int.md#class-int)) virtual const [🔗](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-get-subgizmo-transform)

Override this method to return the current transform of a subgizmo. As with all subgizmo methods, the transform should be in local space respect to the gizmo's Node3D. This transform will be requested at the start of an edit and used in the `restore` argument in [_commit_subgizmos()](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-commit-subgizmos). Called for this plugin's active gizmos.

---


<a id="class-editornode3dgizmoplugin-private-method-has-gizmo"></a>

[bool](class_bool.md#class-bool) **_has_gizmo**(for_node_3d: [Node3D](class_node3d.md#class-node3d)) virtual const [🔗](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-has-gizmo)

Override this method to define which Node3D nodes have a gizmo from this plugin. Whenever a [Node3D](class_node3d.md#class-node3d) node is added to a scene this method is called, if it returns `true` the node gets a generic [EditorNode3DGizmo](class_editornode3dgizmo.md#class-editornode3dgizmo) assigned and is added to this plugin's list of active gizmos.

---


<a id="class-editornode3dgizmoplugin-private-method-is-handle-highlighted"></a>

[bool](class_bool.md#class-bool) **_is_handle_highlighted**(gizmo: [EditorNode3DGizmo](class_editornode3dgizmo.md#class-editornode3dgizmo), handle_id: [int](class_int.md#class-int), secondary: [bool](class_bool.md#class-bool)) virtual const [🔗](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-is-handle-highlighted)

Override this method to return `true` whenever to given handle should be highlighted in the editor. The `secondary` argument is `true` when the requested handle is secondary (see [EditorNode3DGizmo.add_handles()](class_editornode3dgizmo.md#class-editornode3dgizmo-method-add-handles) for more information). Called for this plugin's active gizmos.

---


<a id="class-editornode3dgizmoplugin-private-method-is-selectable-when-hidden"></a>

[bool](class_bool.md#class-bool) **_is_selectable_when_hidden**() virtual const [🔗](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-is-selectable-when-hidden)

Override this method to define whether Node3D with this gizmo should be selectable even when the gizmo is hidden.

---


<a id="class-editornode3dgizmoplugin-private-method-redraw"></a>

void **_redraw**(gizmo: [EditorNode3DGizmo](class_editornode3dgizmo.md#class-editornode3dgizmo)) virtual [🔗](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-redraw)

Override this method to add all the gizmo elements whenever a gizmo update is requested. It's common to call [EditorNode3DGizmo.clear()](class_editornode3dgizmo.md#class-editornode3dgizmo-method-clear) at the beginning of this method and then add visual elements depending on the node's properties.

---


<a id="class-editornode3dgizmoplugin-private-method-set-handle"></a>

void **_set_handle**(gizmo: [EditorNode3DGizmo](class_editornode3dgizmo.md#class-editornode3dgizmo), handle_id: [int](class_int.md#class-int), secondary: [bool](class_bool.md#class-bool), camera: [Camera3D](class_camera3d.md#class-camera3d), screen_pos: [Vector2](class_vector2.md#class-vector2)) virtual [🔗](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-set-handle)

Override this method to update the node's properties when the user drags a gizmo handle (previously added with [EditorNode3DGizmo.add_handles()](class_editornode3dgizmo.md#class-editornode3dgizmo-method-add-handles)). The provided `screen_pos` is the mouse position in screen coordinates and the `camera` can be used to convert it to raycasts.

The `secondary` argument is `true` when the edited handle is secondary (see [EditorNode3DGizmo.add_handles()](class_editornode3dgizmo.md#class-editornode3dgizmo-method-add-handles) for more information).

Called for this plugin's active gizmos.

---


<a id="class-editornode3dgizmoplugin-private-method-set-subgizmo-transform"></a>

void **_set_subgizmo_transform**(gizmo: [EditorNode3DGizmo](class_editornode3dgizmo.md#class-editornode3dgizmo), subgizmo_id: [int](class_int.md#class-int), transform: [Transform3D](class_transform3d.md#class-transform3d)) virtual [🔗](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-set-subgizmo-transform)

Override this method to update the node properties during subgizmo editing (see [_subgizmos_intersect_ray()](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-subgizmos-intersect-ray) and [_subgizmos_intersect_frustum()](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-subgizmos-intersect-frustum)). The `transform` is given in the Node3D's local coordinate system. Called for this plugin's active gizmos.

---


<a id="class-editornode3dgizmoplugin-private-method-subgizmos-intersect-frustum"></a>

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **_subgizmos_intersect_frustum**(gizmo: [EditorNode3DGizmo](class_editornode3dgizmo.md#class-editornode3dgizmo), camera: [Camera3D](class_camera3d.md#class-camera3d), frustum_planes: [Array](class_array.md#class-array)[[Plane](class_plane.md#class-plane)]) virtual const [🔗](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-subgizmos-intersect-frustum)

Override this method to allow selecting subgizmos using mouse drag box selection. Given a `camera` and `frustum_planes`, this method should return which subgizmos are contained within the frustums. The `frustum_planes` argument consists of an array with all the [Plane](class_plane.md#class-plane)s that make up the selection frustum. The returned value should contain a list of unique subgizmo identifiers, these identifiers can have any non-negative value and will be used in other virtual methods like [_get_subgizmo_transform()](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-get-subgizmo-transform) or [_commit_subgizmos()](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-commit-subgizmos). Called for this plugin's active gizmos.

---


<a id="class-editornode3dgizmoplugin-private-method-subgizmos-intersect-ray"></a>

[int](class_int.md#class-int) **_subgizmos_intersect_ray**(gizmo: [EditorNode3DGizmo](class_editornode3dgizmo.md#class-editornode3dgizmo), camera: [Camera3D](class_camera3d.md#class-camera3d), screen_pos: [Vector2](class_vector2.md#class-vector2)) virtual const [🔗](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-subgizmos-intersect-ray)

Override this method to allow selecting subgizmos using mouse clicks. Given a `camera` and a `screen_pos` in screen coordinates, this method should return which subgizmo should be selected. The returned value should be a unique subgizmo identifier, which can have any non-negative value and will be used in other virtual methods like [_get_subgizmo_transform()](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-get-subgizmo-transform) or [_commit_subgizmos()](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-private-method-commit-subgizmos). Called for this plugin's active gizmos.

---


<a id="class-editornode3dgizmoplugin-method-add-material"></a>

void **add_material**(name: [String](class_string.md#class-string), material: [StandardMaterial3D](class_standardmaterial3d.md#class-standardmaterial3d)) [🔗](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-method-add-material)

Adds a new material to the internal material list for the plugin. It can then be accessed with [get_material()](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-method-get-material). Should not be overridden.

---


<a id="class-editornode3dgizmoplugin-method-create-handle-material"></a>

void **create_handle_material**(name: [String](class_string.md#class-string), billboard: [bool](class_bool.md#class-bool) = false, texture: [Texture2D](class_texture2d.md#class-texture2d) = null) [🔗](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-method-create-handle-material)

Creates a handle material with its variants (selected and/or editable) and adds them to the internal material list. They can then be accessed with [get_material()](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-method-get-material) and used in [EditorNode3DGizmo.add_handles()](class_editornode3dgizmo.md#class-editornode3dgizmo-method-add-handles). Should not be overridden.

You can optionally provide a texture to use instead of the default icon.

---


<a id="class-editornode3dgizmoplugin-method-create-icon-material"></a>

void **create_icon_material**(name: [String](class_string.md#class-string), texture: [Texture2D](class_texture2d.md#class-texture2d), on_top: [bool](class_bool.md#class-bool) = false, color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1)) [🔗](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-method-create-icon-material)

Creates an icon material with its variants (selected and/or editable) and adds them to the internal material list. They can then be accessed with [get_material()](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-method-get-material) and used in [EditorNode3DGizmo.add_unscaled_billboard()](class_editornode3dgizmo.md#class-editornode3dgizmo-method-add-unscaled-billboard). Should not be overridden.

---


<a id="class-editornode3dgizmoplugin-method-create-material"></a>

void **create_material**(name: [String](class_string.md#class-string), color: [Color](class_color.md#class-color), billboard: [bool](class_bool.md#class-bool) = false, on_top: [bool](class_bool.md#class-bool) = false, use_vertex_color: [bool](class_bool.md#class-bool) = false) [🔗](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-method-create-material)

Creates an unshaded material with its variants (selected and/or editable) and adds them to the internal material list. They can then be accessed with [get_material()](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-method-get-material) and used in [EditorNode3DGizmo.add_mesh()](class_editornode3dgizmo.md#class-editornode3dgizmo-method-add-mesh) and [EditorNode3DGizmo.add_lines()](class_editornode3dgizmo.md#class-editornode3dgizmo-method-add-lines). Should not be overridden.

---


<a id="class-editornode3dgizmoplugin-method-get-material"></a>

[StandardMaterial3D](class_standardmaterial3d.md#class-standardmaterial3d) **get_material**(name: [String](class_string.md#class-string), gizmo: [EditorNode3DGizmo](class_editornode3dgizmo.md#class-editornode3dgizmo) = null) [🔗](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-method-get-material)

Gets material from the internal list of materials. If an [EditorNode3DGizmo](class_editornode3dgizmo.md#class-editornode3dgizmo) is provided, it will try to get the corresponding variant (selected and/or editable).
