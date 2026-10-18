> Source: https://docs.godotengine.org/en/4.7/classes/class_pathfollow2d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="pathfollow2d"></a>

<a id="class-pathfollow2d"></a>

# PathFollow2D

**Inherits:** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Point sampler for a [Path2D](class_path2d.md#class-path2d).

<a id="description"></a>

## Description

This node takes its parent [Path2D](class_path2d.md#class-path2d), and returns the coordinates of a point within it, given a distance from the first vertex.

It is useful for making other nodes follow a path, without coding the movement pattern. For that, the nodes must be children of this node. The descendant nodes will then move accordingly when setting the [progress](class_pathfollow2d.md#class-pathfollow2d-property-progress) in this node.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [cubic_interp](class_pathfollow2d.md#class-pathfollow2d-property-cubic-interp) | `true` |
| [float](class_float.md#class-float) | [h_offset](class_pathfollow2d.md#class-pathfollow2d-property-h-offset) | `0.0` |
| [bool](class_bool.md#class-bool) | [loop](class_pathfollow2d.md#class-pathfollow2d-property-loop) | `true` |
| [float](class_float.md#class-float) | [progress](class_pathfollow2d.md#class-pathfollow2d-property-progress) | `0.0` |
| [float](class_float.md#class-float) | [progress_ratio](class_pathfollow2d.md#class-pathfollow2d-property-progress-ratio) | `0.0` |
| [bool](class_bool.md#class-bool) | [rotates](class_pathfollow2d.md#class-pathfollow2d-property-rotates) | `true` |
| [float](class_float.md#class-float) | [v_offset](class_pathfollow2d.md#class-pathfollow2d-property-v-offset) | `0.0` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-pathfollow2d-property-cubic-interp"></a>

[bool](class_bool.md#class-bool) **cubic_interp** = `true` [🔗](class_pathfollow2d.md#class-pathfollow2d-property-cubic-interp)

- void **set_cubic_interpolation**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_cubic_interpolation**()

If `true`, the position between two cached points is interpolated cubically, and linearly otherwise.

The points along the [Curve2D](class_curve2d.md#class-curve2d) of the [Path2D](class_path2d.md#class-path2d) are precomputed before use, for faster calculations. The point at the requested offset is then calculated interpolating between two adjacent cached points. This may present a problem if the curve makes sharp turns, as the cached points may not follow the curve closely enough.

There are two answers to this problem: either increase the number of cached points and increase memory consumption, or make a cubic interpolation between two points at the cost of (slightly) slower calculations.

---


<a id="class-pathfollow2d-property-h-offset"></a>

[float](class_float.md#class-float) **h_offset** = `0.0` [🔗](class_pathfollow2d.md#class-pathfollow2d-property-h-offset)

- void **set_h_offset**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_h_offset**()

The node's offset along the curve.

---


<a id="class-pathfollow2d-property-loop"></a>

[bool](class_bool.md#class-bool) **loop** = `true` [🔗](class_pathfollow2d.md#class-pathfollow2d-property-loop)

- void **set_loop**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **has_loop**()

If `true`, any offset outside the path's length will wrap around, instead of stopping at the ends. Use it for cyclic paths.

---


<a id="class-pathfollow2d-property-progress"></a>

[float](class_float.md#class-float) **progress** = `0.0` [🔗](class_pathfollow2d.md#class-pathfollow2d-property-progress)

- void **set_progress**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_progress**()

The distance along the path, in pixels. Changing this value sets this node's position to a point within the path.

---


<a id="class-pathfollow2d-property-progress-ratio"></a>

[float](class_float.md#class-float) **progress_ratio** = `0.0` [🔗](class_pathfollow2d.md#class-pathfollow2d-property-progress-ratio)

- void **set_progress_ratio**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_progress_ratio**()

The distance along the path as a number in the range 0.0 (for the first vertex) to 1.0 (for the last). This is just another way of expressing the progress within the path, as the offset supplied is multiplied internally by the path's length.

It can be set or get only if the **PathFollow2D** is the child of a [Path2D](class_path2d.md#class-path2d) which is part of the scene tree, and that this [Path2D](class_path2d.md#class-path2d) has a [Curve2D](class_curve2d.md#class-curve2d) with a non-zero length. Otherwise, trying to set this field will print an error, and getting this field will return `0.0`.

---


<a id="class-pathfollow2d-property-rotates"></a>

[bool](class_bool.md#class-bool) **rotates** = `true` [🔗](class_pathfollow2d.md#class-pathfollow2d-property-rotates)

- void **set_rotates**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_rotating**()

If `true`, this node rotates to follow the path, with the +X direction facing forward on the path.

---


<a id="class-pathfollow2d-property-v-offset"></a>

[float](class_float.md#class-float) **v_offset** = `0.0` [🔗](class_pathfollow2d.md#class-pathfollow2d-property-v-offset)

- void **set_v_offset**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_v_offset**()

The node's offset perpendicular to the curve.
