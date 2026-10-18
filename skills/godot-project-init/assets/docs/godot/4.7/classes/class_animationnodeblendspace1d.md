> Source: https://docs.godotengine.org/en/4.7/classes/class_animationnodeblendspace1d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="animationnodeblendspace1d"></a>

<a id="class-animationnodeblendspace1d"></a>

# AnimationNodeBlendSpace1D

**Inherits:** [AnimationRootNode](class_animationrootnode.md#class-animationrootnode) **<** [AnimationNode](class_animationnode.md#class-animationnode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A set of [AnimationRootNode](class_animationrootnode.md#class-animationrootnode)s placed on a virtual axis, crossfading between the two adjacent ones. Used by [AnimationTree](class_animationtree.md#class-animationtree).

<a id="description"></a>

## Description

A resource used by [AnimationNodeBlendTree](class_animationnodeblendtree.md#class-animationnodeblendtree).

**AnimationNodeBlendSpace1D** represents a virtual axis on which any type of [AnimationRootNode](class_animationrootnode.md#class-animationrootnode)s can be added using [add_blend_point()](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-method-add-blend-point). Outputs the linear blend of the two [AnimationRootNode](class_animationrootnode.md#class-animationrootnode)s adjacent to the current value.

You can set the extents of the axis with [min_space](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-property-min-space) and [max_space](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-property-max-space).

<a id="tutorials"></a>

## Tutorials

- [Using AnimationTree](../tutorials/animation/animation_tree.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [BlendMode](class_animationnodeblendspace1d.md#enum-animationnodeblendspace1d-blendmode) | [blend_mode](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-property-blend-mode) | `0` |
| [float](class_float.md#class-float) | [cyclic_length](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-property-cyclic-length) | `0.0` |
| [float](class_float.md#class-float) | [max_space](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-property-max-space) | `1.0` |
| [float](class_float.md#class-float) | [min_space](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-property-min-space) | `-1.0` |
| [float](class_float.md#class-float) | [snap](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-property-snap) | `0.1` |
| [bool](class_bool.md#class-bool) | [sync](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-property-sync) |  |
| [SyncMode](class_animationnodeblendspace1d.md#enum-animationnodeblendspace1d-syncmode) | [sync_mode](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-property-sync-mode) | `0` |
| [String](class_string.md#class-string) | [value_label](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-property-value-label) | `"value"` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_blend_point](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-method-add-blend-point)(node: [AnimationRootNode](class_animationrootnode.md#class-animationrootnode), pos: [float](class_float.md#class-float), at_index: [int](class_int.md#class-int) = -1, name: [StringName](class_stringname.md#class-stringname) = &"") |
| [int](class_int.md#class-int) | [find_blend_point_by_name](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-method-find-blend-point-by-name)(name: [StringName](class_stringname.md#class-stringname)) const |
| [int](class_int.md#class-int) | [get_blend_point_count](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-method-get-blend-point-count)() const |
| [StringName](class_stringname.md#class-stringname) | [get_blend_point_name](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-method-get-blend-point-name)(point: [int](class_int.md#class-int)) const |
| [AnimationRootNode](class_animationrootnode.md#class-animationrootnode) | [get_blend_point_node](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-method-get-blend-point-node)(point: [int](class_int.md#class-int)) const |
| [float](class_float.md#class-float) | [get_blend_point_position](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-method-get-blend-point-position)(point: [int](class_int.md#class-int)) const |
| void | [remove_blend_point](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-method-remove-blend-point)(point: [int](class_int.md#class-int)) |
| void | [reorder_blend_point](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-method-reorder-blend-point)(from_index: [int](class_int.md#class-int), to_index: [int](class_int.md#class-int)) |
| void | [set_blend_point_name](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-method-set-blend-point-name)(point: [int](class_int.md#class-int), name: [StringName](class_stringname.md#class-stringname)) |
| void | [set_blend_point_node](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-method-set-blend-point-node)(point: [int](class_int.md#class-int), node: [AnimationRootNode](class_animationrootnode.md#class-animationrootnode)) |
| void | [set_blend_point_position](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-method-set-blend-point-position)(point: [int](class_int.md#class-int), pos: [float](class_float.md#class-float)) |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-animationnodeblendspace1d-blendmode"></a>

enum **BlendMode**: [🔗](class_animationnodeblendspace1d.md#enum-animationnodeblendspace1d-blendmode)

<a id="class-animationnodeblendspace1d-constant-blend-mode-interpolated"></a>

[BlendMode](class_animationnodeblendspace1d.md#enum-animationnodeblendspace1d-blendmode) **BLEND_MODE_INTERPOLATED** = `0`

The interpolation between animations is linear.

<a id="class-animationnodeblendspace1d-constant-blend-mode-discrete"></a>

[BlendMode](class_animationnodeblendspace1d.md#enum-animationnodeblendspace1d-blendmode) **BLEND_MODE_DISCRETE** = `1`

The blend space plays the animation of the animation node which blending position is closest to. Useful for frame-by-frame 2D animations.

<a id="class-animationnodeblendspace1d-constant-blend-mode-discrete-carry"></a>

[BlendMode](class_animationnodeblendspace1d.md#enum-animationnodeblendspace1d-blendmode) **BLEND_MODE_DISCRETE_CARRY** = `2`

Similar to [BLEND_MODE_DISCRETE](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-constant-blend-mode-discrete), but starts the new animation at the last animation's playback position.

---


<a id="enum-animationnodeblendspace1d-syncmode"></a>

enum **SyncMode**: [🔗](class_animationnodeblendspace1d.md#enum-animationnodeblendspace1d-syncmode)

<a id="class-animationnodeblendspace1d-constant-sync-mode-none"></a>

[SyncMode](class_animationnodeblendspace1d.md#enum-animationnodeblendspace1d-syncmode) **SYNC_MODE_NONE** = `0`

Inactive animations are frozen and do not advance.

<a id="class-animationnodeblendspace1d-constant-sync-mode-independent"></a>

[SyncMode](class_animationnodeblendspace1d.md#enum-animationnodeblendspace1d-syncmode) **SYNC_MODE_INDEPENDENT** = `1`

Inactive animations advance with a weight of `0`. This is equivalent to the previous `sync = true` behavior.

<a id="class-animationnodeblendspace1d-constant-sync-mode-cyclic-mutable"></a>

[SyncMode](class_animationnodeblendspace1d.md#enum-animationnodeblendspace1d-syncmode) **SYNC_MODE_CYCLIC_MUTABLE** = `2`

All animations are time-scaled so they stay in sync, with the cycle length dynamically computed from active blend weights. This is self-normalizing: a solo animation plays at normal speed.

**Note:** If you apply [AnimationNodeTimeSeek](class_animationnodetimeseek.md#class-animationnodetimeseek) to the result when handling animations of different lengths, synchronization will be broken. In such cases, it is recommended to use [AnimationNodeAnimation.use_custom_timeline](class_animationnodeanimation.md#class-animationnodeanimation-property-use-custom-timeline) to align the animation lengths.

<a id="class-animationnodeblendspace1d-constant-sync-mode-cyclic-constant"></a>

[SyncMode](class_animationnodeblendspace1d.md#enum-animationnodeblendspace1d-syncmode) **SYNC_MODE_CYCLIC_CONSTANT** = `3`

All animations are time-scaled so they complete one cycle in [cyclic_length](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-property-cyclic-length) seconds, keeping them in sync regardless of their individual lengths.

**Note:** If you apply [AnimationNodeTimeSeek](class_animationnodetimeseek.md#class-animationnodetimeseek) to the result when handling animations of different lengths, synchronization will be broken. In such cases, it is recommended to use [AnimationNodeAnimation.use_custom_timeline](class_animationnodeanimation.md#class-animationnodeanimation-property-use-custom-timeline) to align the animation lengths.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-animationnodeblendspace1d-property-blend-mode"></a>

[BlendMode](class_animationnodeblendspace1d.md#enum-animationnodeblendspace1d-blendmode) **blend_mode** = `0` [🔗](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-property-blend-mode)

- void **set_blend_mode**(value: [BlendMode](class_animationnodeblendspace1d.md#enum-animationnodeblendspace1d-blendmode))
- [BlendMode](class_animationnodeblendspace1d.md#enum-animationnodeblendspace1d-blendmode) **get_blend_mode**()

Controls the interpolation between animations.

---


<a id="class-animationnodeblendspace1d-property-cyclic-length"></a>

[float](class_float.md#class-float) **cyclic_length** = `0.0` [🔗](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-property-cyclic-length)

- void **set_cyclic_length**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_cyclic_length**()

The cycle length in seconds used by [SYNC_MODE_CYCLIC_CONSTANT](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-constant-sync-mode-cyclic-constant). All animations are time-scaled so they complete one full cycle in this duration. Must be greater than `0` for cyclic sync to take effect.

---


<a id="class-animationnodeblendspace1d-property-max-space"></a>

[float](class_float.md#class-float) **max_space** = `1.0` [🔗](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-property-max-space)

- void **set_max_space**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_max_space**()

The blend space's axis's upper limit for the points' position. See [add_blend_point()](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-method-add-blend-point).

---


<a id="class-animationnodeblendspace1d-property-min-space"></a>

[float](class_float.md#class-float) **min_space** = `-1.0` [🔗](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-property-min-space)

- void **set_min_space**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_min_space**()

The blend space's axis's lower limit for the points' position. See [add_blend_point()](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-method-add-blend-point).

---


<a id="class-animationnodeblendspace1d-property-snap"></a>

[float](class_float.md#class-float) **snap** = `0.1` [🔗](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-property-snap)

- void **set_snap**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_snap**()

Position increment to snap to when moving a point on the axis.

---


<a id="class-animationnodeblendspace1d-property-sync"></a>

[bool](class_bool.md#class-bool) **sync** [🔗](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-property-sync)

- void **set_use_sync**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_using_sync**()

**Deprecated:** Use [sync_mode](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-property-sync-mode) instead.

If `true`, sync mode is enabled (equivalent to [SYNC_MODE_INDEPENDENT](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-constant-sync-mode-independent)). This property is kept for backward compatibility.

---


<a id="class-animationnodeblendspace1d-property-sync-mode"></a>

[SyncMode](class_animationnodeblendspace1d.md#enum-animationnodeblendspace1d-syncmode) **sync_mode** = `0` [🔗](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-property-sync-mode)

- void **set_sync_mode**(value: [SyncMode](class_animationnodeblendspace1d.md#enum-animationnodeblendspace1d-syncmode))
- [SyncMode](class_animationnodeblendspace1d.md#enum-animationnodeblendspace1d-syncmode) **get_sync_mode**()

Controls how animations are synced when blended. See [SyncMode](class_animationnodeblendspace1d.md#enum-animationnodeblendspace1d-syncmode) for available options.

---


<a id="class-animationnodeblendspace1d-property-value-label"></a>

[String](class_string.md#class-string) **value_label** = `"value"` [🔗](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-property-value-label)

- void **set_value_label**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_value_label**()

Label of the virtual axis of the blend space.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-animationnodeblendspace1d-method-add-blend-point"></a>

void **add_blend_point**(node: [AnimationRootNode](class_animationrootnode.md#class-animationrootnode), pos: [float](class_float.md#class-float), at_index: [int](class_int.md#class-int) = -1, name: [StringName](class_stringname.md#class-stringname) = &"") [🔗](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-method-add-blend-point)

Adds a new point with `name` that represents a `node` on the virtual axis at a given position set by `pos`. You can insert it at a specific index using the `at_index` argument. If you use the default value for `at_index`, the point is inserted at the end of the blend points array.

**Note:** If no name is provided, safe index is used as reference. In the future, empty names will be deprecated, so explicitly passing a name is recommended.

---


<a id="class-animationnodeblendspace1d-method-find-blend-point-by-name"></a>

[int](class_int.md#class-int) **find_blend_point_by_name**(name: [StringName](class_stringname.md#class-stringname)) const [🔗](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-method-find-blend-point-by-name)

Returns the index of the blend point with the given `name`. Returns `-1` if no blend point with that name is found.

---


<a id="class-animationnodeblendspace1d-method-get-blend-point-count"></a>

[int](class_int.md#class-int) **get_blend_point_count**() const [🔗](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-method-get-blend-point-count)

Returns the number of points on the blend axis.

---


<a id="class-animationnodeblendspace1d-method-get-blend-point-name"></a>

[StringName](class_stringname.md#class-stringname) **get_blend_point_name**(point: [int](class_int.md#class-int)) const [🔗](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-method-get-blend-point-name)

Returns the name of the blend point at index `point`.

---


<a id="class-animationnodeblendspace1d-method-get-blend-point-node"></a>

[AnimationRootNode](class_animationrootnode.md#class-animationrootnode) **get_blend_point_node**(point: [int](class_int.md#class-int)) const [🔗](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-method-get-blend-point-node)

Returns the [AnimationNode](class_animationnode.md#class-animationnode) referenced by the point at index `point`.

---


<a id="class-animationnodeblendspace1d-method-get-blend-point-position"></a>

[float](class_float.md#class-float) **get_blend_point_position**(point: [int](class_int.md#class-int)) const [🔗](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-method-get-blend-point-position)

Returns the position of the point at index `point`.

---


<a id="class-animationnodeblendspace1d-method-remove-blend-point"></a>

void **remove_blend_point**(point: [int](class_int.md#class-int)) [🔗](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-method-remove-blend-point)

Removes the point at index `point` from the blend axis.

---


<a id="class-animationnodeblendspace1d-method-reorder-blend-point"></a>

void **reorder_blend_point**(from_index: [int](class_int.md#class-int), to_index: [int](class_int.md#class-int)) [🔗](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-method-reorder-blend-point)

Swaps the blend points at indices `from_index` and `to_index`, exchanging their positions and properties.

---


<a id="class-animationnodeblendspace1d-method-set-blend-point-name"></a>

void **set_blend_point_name**(point: [int](class_int.md#class-int), name: [StringName](class_stringname.md#class-stringname)) [🔗](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-method-set-blend-point-name)

Sets the name of the blend point at index `point`. If the name conflicts with an existing point, a unique name will be generated automatically.

---


<a id="class-animationnodeblendspace1d-method-set-blend-point-node"></a>

void **set_blend_point_node**(point: [int](class_int.md#class-int), node: [AnimationRootNode](class_animationrootnode.md#class-animationrootnode)) [🔗](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-method-set-blend-point-node)

Changes the [AnimationNode](class_animationnode.md#class-animationnode) referenced by the point at index `point`.

---


<a id="class-animationnodeblendspace1d-method-set-blend-point-position"></a>

void **set_blend_point_position**(point: [int](class_int.md#class-int), pos: [float](class_float.md#class-float)) [🔗](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d-method-set-blend-point-position)

Updates the position of the point at index `point` on the blend axis.
