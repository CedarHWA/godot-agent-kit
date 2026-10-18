> Source: https://docs.godotengine.org/en/4.7/classes/class_animationnodeblendspace2d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="animationnodeblendspace2d"></a>

<a id="class-animationnodeblendspace2d"></a>

# AnimationNodeBlendSpace2D

**Inherits:** [AnimationRootNode](class_animationrootnode.md#class-animationrootnode) **<** [AnimationNode](class_animationnode.md#class-animationnode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A set of [AnimationRootNode](class_animationrootnode.md#class-animationrootnode)s placed on 2D coordinates, crossfading between the three adjacent ones. Used by [AnimationTree](class_animationtree.md#class-animationtree).

<a id="description"></a>

## Description

A resource used by [AnimationNodeBlendTree](class_animationnodeblendtree.md#class-animationnodeblendtree).

**AnimationNodeBlendSpace2D** represents a virtual 2D space on which [AnimationRootNode](class_animationrootnode.md#class-animationrootnode)s are placed. Outputs the linear blend of the three adjacent animations using a [Vector2](class_vector2.md#class-vector2) weight. Adjacent in this context means the three [AnimationRootNode](class_animationrootnode.md#class-animationrootnode)s making up the triangle that contains the current value.

You can add vertices to the blend space with [add_blend_point()](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-method-add-blend-point) and automatically triangulate it by setting [auto_triangles](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-property-auto-triangles) to `true`. Otherwise, use [add_triangle()](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-method-add-triangle) and [remove_triangle()](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-method-remove-triangle) to triangulate the blend space by hand.

<a id="tutorials"></a>

## Tutorials

- [Using AnimationTree](../tutorials/animation/animation_tree.md)
- [Third Person Shooter (TPS) Demo](https://godotengine.org/asset-library/asset/2710)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [auto_triangles](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-property-auto-triangles) | `true` |
| [BlendMode](class_animationnodeblendspace2d.md#enum-animationnodeblendspace2d-blendmode) | [blend_mode](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-property-blend-mode) | `0` |
| [float](class_float.md#class-float) | [cyclic_length](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-property-cyclic-length) | `0.0` |
| [Vector2](class_vector2.md#class-vector2) | [max_space](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-property-max-space) | `Vector2(1, 1)` |
| [Vector2](class_vector2.md#class-vector2) | [min_space](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-property-min-space) | `Vector2(-1, -1)` |
| [Vector2](class_vector2.md#class-vector2) | [snap](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-property-snap) | `Vector2(0.1, 0.1)` |
| [bool](class_bool.md#class-bool) | [sync](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-property-sync) |  |
| [SyncMode](class_animationnodeblendspace2d.md#enum-animationnodeblendspace2d-syncmode) | [sync_mode](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-property-sync-mode) | `0` |
| [String](class_string.md#class-string) | [x_label](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-property-x-label) | `"x"` |
| [String](class_string.md#class-string) | [y_label](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-property-y-label) | `"y"` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_blend_point](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-method-add-blend-point)(node: [AnimationRootNode](class_animationrootnode.md#class-animationrootnode), pos: [Vector2](class_vector2.md#class-vector2), at_index: [int](class_int.md#class-int) = -1, name: [StringName](class_stringname.md#class-stringname) = &"") |
| void | [add_triangle](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-method-add-triangle)(x: [int](class_int.md#class-int), y: [int](class_int.md#class-int), z: [int](class_int.md#class-int), at_index: [int](class_int.md#class-int) = -1) |
| [int](class_int.md#class-int) | [find_blend_point_by_name](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-method-find-blend-point-by-name)(name: [StringName](class_stringname.md#class-stringname)) const |
| [int](class_int.md#class-int) | [get_blend_point_count](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-method-get-blend-point-count)() const |
| [StringName](class_stringname.md#class-stringname) | [get_blend_point_name](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-method-get-blend-point-name)(point: [int](class_int.md#class-int)) const |
| [AnimationRootNode](class_animationrootnode.md#class-animationrootnode) | [get_blend_point_node](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-method-get-blend-point-node)(point: [int](class_int.md#class-int)) const |
| [Vector2](class_vector2.md#class-vector2) | [get_blend_point_position](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-method-get-blend-point-position)(point: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_triangle_count](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-method-get-triangle-count)() const |
| [int](class_int.md#class-int) | [get_triangle_point](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-method-get-triangle-point)(triangle: [int](class_int.md#class-int), point: [int](class_int.md#class-int)) |
| void | [remove_blend_point](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-method-remove-blend-point)(point: [int](class_int.md#class-int)) |
| void | [remove_triangle](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-method-remove-triangle)(triangle: [int](class_int.md#class-int)) |
| void | [reorder_blend_point](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-method-reorder-blend-point)(from_index: [int](class_int.md#class-int), to_index: [int](class_int.md#class-int)) |
| void | [set_blend_point_name](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-method-set-blend-point-name)(point: [int](class_int.md#class-int), name: [StringName](class_stringname.md#class-stringname)) |
| void | [set_blend_point_node](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-method-set-blend-point-node)(point: [int](class_int.md#class-int), node: [AnimationRootNode](class_animationrootnode.md#class-animationrootnode)) |
| void | [set_blend_point_position](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-method-set-blend-point-position)(point: [int](class_int.md#class-int), pos: [Vector2](class_vector2.md#class-vector2)) |

---


<a id="signals"></a>

## Signals

<a id="class-animationnodeblendspace2d-signal-triangles-updated"></a>

**triangles_updated**() [🔗](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-signal-triangles-updated)

Emitted every time the blend space's triangles are created, removed, or when one of their vertices changes position.

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-animationnodeblendspace2d-blendmode"></a>

enum **BlendMode**: [🔗](class_animationnodeblendspace2d.md#enum-animationnodeblendspace2d-blendmode)

<a id="class-animationnodeblendspace2d-constant-blend-mode-interpolated"></a>

[BlendMode](class_animationnodeblendspace2d.md#enum-animationnodeblendspace2d-blendmode) **BLEND_MODE_INTERPOLATED** = `0`

The interpolation between animations is linear.

<a id="class-animationnodeblendspace2d-constant-blend-mode-discrete"></a>

[BlendMode](class_animationnodeblendspace2d.md#enum-animationnodeblendspace2d-blendmode) **BLEND_MODE_DISCRETE** = `1`

The blend space plays the animation of the animation node which blending position is closest to. Useful for frame-by-frame 2D animations.

<a id="class-animationnodeblendspace2d-constant-blend-mode-discrete-carry"></a>

[BlendMode](class_animationnodeblendspace2d.md#enum-animationnodeblendspace2d-blendmode) **BLEND_MODE_DISCRETE_CARRY** = `2`

Similar to [BLEND_MODE_DISCRETE](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-constant-blend-mode-discrete), but starts the new animation at the last animation's playback position.

---


<a id="enum-animationnodeblendspace2d-syncmode"></a>

enum **SyncMode**: [🔗](class_animationnodeblendspace2d.md#enum-animationnodeblendspace2d-syncmode)

<a id="class-animationnodeblendspace2d-constant-sync-mode-none"></a>

[SyncMode](class_animationnodeblendspace2d.md#enum-animationnodeblendspace2d-syncmode) **SYNC_MODE_NONE** = `0`

Inactive animations are frozen and do not advance.

<a id="class-animationnodeblendspace2d-constant-sync-mode-independent"></a>

[SyncMode](class_animationnodeblendspace2d.md#enum-animationnodeblendspace2d-syncmode) **SYNC_MODE_INDEPENDENT** = `1`

Inactive animations advance with a weight of `0`. This is equivalent to the previous `sync = true` behavior.

<a id="class-animationnodeblendspace2d-constant-sync-mode-cyclic-mutable"></a>

[SyncMode](class_animationnodeblendspace2d.md#enum-animationnodeblendspace2d-syncmode) **SYNC_MODE_CYCLIC_MUTABLE** = `2`

All animations are time-scaled so they stay in sync, with the cycle length dynamically computed from active blend weights. This is self-normalizing: a solo animation plays at normal speed.

**Note:** If you apply [AnimationNodeTimeSeek](class_animationnodetimeseek.md#class-animationnodetimeseek) to the result when handling animations of different lengths, synchronization will be broken. In such cases, it is recommended to use [AnimationNodeAnimation.use_custom_timeline](class_animationnodeanimation.md#class-animationnodeanimation-property-use-custom-timeline) to align the animation lengths.

<a id="class-animationnodeblendspace2d-constant-sync-mode-cyclic-constant"></a>

[SyncMode](class_animationnodeblendspace2d.md#enum-animationnodeblendspace2d-syncmode) **SYNC_MODE_CYCLIC_CONSTANT** = `3`

All animations are time-scaled so they complete one cycle in [cyclic_length](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-property-cyclic-length) seconds, keeping them in sync regardless of their individual lengths.

**Note:** If you apply [AnimationNodeTimeSeek](class_animationnodetimeseek.md#class-animationnodetimeseek) to the result when handling animations of different lengths, synchronization will be broken. In such cases, it is recommended to use [AnimationNodeAnimation.use_custom_timeline](class_animationnodeanimation.md#class-animationnodeanimation-property-use-custom-timeline) to align the animation lengths.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-animationnodeblendspace2d-property-auto-triangles"></a>

[bool](class_bool.md#class-bool) **auto_triangles** = `true` [🔗](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-property-auto-triangles)

- void **set_auto_triangles**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_auto_triangles**()

If `true`, the blend space is triangulated automatically. The mesh updates every time you add or remove points with [add_blend_point()](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-method-add-blend-point) and [remove_blend_point()](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-method-remove-blend-point).

---


<a id="class-animationnodeblendspace2d-property-blend-mode"></a>

[BlendMode](class_animationnodeblendspace2d.md#enum-animationnodeblendspace2d-blendmode) **blend_mode** = `0` [🔗](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-property-blend-mode)

- void **set_blend_mode**(value: [BlendMode](class_animationnodeblendspace2d.md#enum-animationnodeblendspace2d-blendmode))
- [BlendMode](class_animationnodeblendspace2d.md#enum-animationnodeblendspace2d-blendmode) **get_blend_mode**()

Controls the interpolation between animations.

---


<a id="class-animationnodeblendspace2d-property-cyclic-length"></a>

[float](class_float.md#class-float) **cyclic_length** = `0.0` [🔗](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-property-cyclic-length)

- void **set_cyclic_length**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_cyclic_length**()

The cycle length in seconds used by [SYNC_MODE_CYCLIC_CONSTANT](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-constant-sync-mode-cyclic-constant). All animations are time-scaled so they complete one full cycle in this duration. Must be greater than `0` for cyclic sync to take effect.

---


<a id="class-animationnodeblendspace2d-property-max-space"></a>

[Vector2](class_vector2.md#class-vector2) **max_space** = `Vector2(1, 1)` [🔗](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-property-max-space)

- void **set_max_space**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_max_space**()

The blend space's X and Y axes' upper limit for the points' position. See [add_blend_point()](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-method-add-blend-point).

---


<a id="class-animationnodeblendspace2d-property-min-space"></a>

[Vector2](class_vector2.md#class-vector2) **min_space** = `Vector2(-1, -1)` [🔗](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-property-min-space)

- void **set_min_space**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_min_space**()

The blend space's X and Y axes' lower limit for the points' position. See [add_blend_point()](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-method-add-blend-point).

---


<a id="class-animationnodeblendspace2d-property-snap"></a>

[Vector2](class_vector2.md#class-vector2) **snap** = `Vector2(0.1, 0.1)` [🔗](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-property-snap)

- void **set_snap**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_snap**()

Position increment to snap to when moving a point.

---


<a id="class-animationnodeblendspace2d-property-sync"></a>

[bool](class_bool.md#class-bool) **sync** [🔗](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-property-sync)

- void **set_use_sync**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_using_sync**()

**Deprecated:** Use [sync_mode](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-property-sync-mode) instead.

If `true`, sync mode is enabled (equivalent to [SYNC_MODE_INDEPENDENT](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-constant-sync-mode-independent)). This property is kept for backward compatibility.

---


<a id="class-animationnodeblendspace2d-property-sync-mode"></a>

[SyncMode](class_animationnodeblendspace2d.md#enum-animationnodeblendspace2d-syncmode) **sync_mode** = `0` [🔗](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-property-sync-mode)

- void **set_sync_mode**(value: [SyncMode](class_animationnodeblendspace2d.md#enum-animationnodeblendspace2d-syncmode))
- [SyncMode](class_animationnodeblendspace2d.md#enum-animationnodeblendspace2d-syncmode) **get_sync_mode**()

Controls how animations are synced when blended. See [SyncMode](class_animationnodeblendspace2d.md#enum-animationnodeblendspace2d-syncmode) for available options.

---


<a id="class-animationnodeblendspace2d-property-x-label"></a>

[String](class_string.md#class-string) **x_label** = `"x"` [🔗](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-property-x-label)

- void **set_x_label**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_x_label**()

Name of the blend space's X axis.

---


<a id="class-animationnodeblendspace2d-property-y-label"></a>

[String](class_string.md#class-string) **y_label** = `"y"` [🔗](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-property-y-label)

- void **set_y_label**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_y_label**()

Name of the blend space's Y axis.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-animationnodeblendspace2d-method-add-blend-point"></a>

void **add_blend_point**(node: [AnimationRootNode](class_animationrootnode.md#class-animationrootnode), pos: [Vector2](class_vector2.md#class-vector2), at_index: [int](class_int.md#class-int) = -1, name: [StringName](class_stringname.md#class-stringname) = &"") [🔗](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-method-add-blend-point)

Adds a new point with `name` that represents a `node` at the position set by `pos`. You can insert it at a specific index using the `at_index` argument. If you use the default value for `at_index`, the point is inserted at the end of the blend points array.

**Note:** If no name is provided, safe index is used as reference. In the future, empty names will be deprecated, so explicitly passing a name is recommended.

---


<a id="class-animationnodeblendspace2d-method-add-triangle"></a>

void **add_triangle**(x: [int](class_int.md#class-int), y: [int](class_int.md#class-int), z: [int](class_int.md#class-int), at_index: [int](class_int.md#class-int) = -1) [🔗](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-method-add-triangle)

Creates a new triangle using three points `x`, `y`, and `z`. Triangles can overlap. You can insert the triangle at a specific index using the `at_index` argument. If you use the default value for `at_index`, the point is inserted at the end of the blend points array.

---


<a id="class-animationnodeblendspace2d-method-find-blend-point-by-name"></a>

[int](class_int.md#class-int) **find_blend_point_by_name**(name: [StringName](class_stringname.md#class-stringname)) const [🔗](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-method-find-blend-point-by-name)

Returns the index of the blend point with the given `name`. Returns `-1` if no blend point with that name is found.

---


<a id="class-animationnodeblendspace2d-method-get-blend-point-count"></a>

[int](class_int.md#class-int) **get_blend_point_count**() const [🔗](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-method-get-blend-point-count)

Returns the number of points in the blend space.

---


<a id="class-animationnodeblendspace2d-method-get-blend-point-name"></a>

[StringName](class_stringname.md#class-stringname) **get_blend_point_name**(point: [int](class_int.md#class-int)) const [🔗](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-method-get-blend-point-name)

Returns the name of the blend point at index `point`.

---


<a id="class-animationnodeblendspace2d-method-get-blend-point-node"></a>

[AnimationRootNode](class_animationrootnode.md#class-animationrootnode) **get_blend_point_node**(point: [int](class_int.md#class-int)) const [🔗](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-method-get-blend-point-node)

Returns the [AnimationRootNode](class_animationrootnode.md#class-animationrootnode) referenced by the point at index `point`.

---


<a id="class-animationnodeblendspace2d-method-get-blend-point-position"></a>

[Vector2](class_vector2.md#class-vector2) **get_blend_point_position**(point: [int](class_int.md#class-int)) const [🔗](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-method-get-blend-point-position)

Returns the position of the point at index `point`.

---


<a id="class-animationnodeblendspace2d-method-get-triangle-count"></a>

[int](class_int.md#class-int) **get_triangle_count**() const [🔗](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-method-get-triangle-count)

Returns the number of triangles in the blend space.

---


<a id="class-animationnodeblendspace2d-method-get-triangle-point"></a>

[int](class_int.md#class-int) **get_triangle_point**(triangle: [int](class_int.md#class-int), point: [int](class_int.md#class-int)) [🔗](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-method-get-triangle-point)

Returns the position of the point at index `point` in the triangle of index `triangle`.

---


<a id="class-animationnodeblendspace2d-method-remove-blend-point"></a>

void **remove_blend_point**(point: [int](class_int.md#class-int)) [🔗](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-method-remove-blend-point)

Removes the point at index `point` from the blend space.

---


<a id="class-animationnodeblendspace2d-method-remove-triangle"></a>

void **remove_triangle**(triangle: [int](class_int.md#class-int)) [🔗](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-method-remove-triangle)

Removes the triangle at index `triangle` from the blend space.

---


<a id="class-animationnodeblendspace2d-method-reorder-blend-point"></a>

void **reorder_blend_point**(from_index: [int](class_int.md#class-int), to_index: [int](class_int.md#class-int)) [🔗](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-method-reorder-blend-point)

Swaps the blend points at indices `from_index` and `to_index`, exchanging their positions and properties.

---


<a id="class-animationnodeblendspace2d-method-set-blend-point-name"></a>

void **set_blend_point_name**(point: [int](class_int.md#class-int), name: [StringName](class_stringname.md#class-stringname)) [🔗](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-method-set-blend-point-name)

Sets the name of the blend point at index `point`. If the name conflicts with an existing point, a unique name will be generated automatically.

---


<a id="class-animationnodeblendspace2d-method-set-blend-point-node"></a>

void **set_blend_point_node**(point: [int](class_int.md#class-int), node: [AnimationRootNode](class_animationrootnode.md#class-animationrootnode)) [🔗](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-method-set-blend-point-node)

Changes the [AnimationNode](class_animationnode.md#class-animationnode) referenced by the point at index `point`.

---


<a id="class-animationnodeblendspace2d-method-set-blend-point-position"></a>

void **set_blend_point_position**(point: [int](class_int.md#class-int), pos: [Vector2](class_vector2.md#class-vector2)) [🔗](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d-method-set-blend-point-position)

Updates the position of the point at index `point` in the blend space.
