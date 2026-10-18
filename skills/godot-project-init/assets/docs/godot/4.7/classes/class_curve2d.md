> Source: https://docs.godotengine.org/en/4.7/classes/class_curve2d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="curve2d"></a>

<a id="class-curve2d"></a>

# Curve2D

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Describes a Bézier curve in 2D space.

<a id="description"></a>

## Description

This class describes a Bézier curve in 2D space. It is mainly used to give a shape to a [Path2D](class_path2d.md#class-path2d), but can be manually sampled for other purposes.

It keeps a cache of precalculated points along the curve, to speed up further calculations.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [bake_interval](class_curve2d.md#class-curve2d-property-bake-interval) | `5.0` |
| [int](class_int.md#class-int) | [point_count](class_curve2d.md#class-curve2d-property-point-count) | `0` |
| [Vector2](class_vector2.md#class-vector2) | [point_{index}/in](class_curve2d.md#class-curve2d-property-point-index-in) | `Vector2(0, 0)` |
| [Vector2](class_vector2.md#class-vector2) | [point_{index}/out](class_curve2d.md#class-curve2d-property-point-index-out) | `Vector2(0, 0)` |
| [Vector2](class_vector2.md#class-vector2) | [point_{index}/position](class_curve2d.md#class-curve2d-property-point-index-position) | `Vector2(0, 0)` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_point](class_curve2d.md#class-curve2d-method-add-point)(position: [Vector2](class_vector2.md#class-vector2), in: [Vector2](class_vector2.md#class-vector2) = Vector2(0, 0), out: [Vector2](class_vector2.md#class-vector2) = Vector2(0, 0), index: [int](class_int.md#class-int) = -1) |
| void | [clear_points](class_curve2d.md#class-curve2d-method-clear-points)() |
| [float](class_float.md#class-float) | [get_baked_length](class_curve2d.md#class-curve2d-method-get-baked-length)() const |
| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) | [get_baked_points](class_curve2d.md#class-curve2d-method-get-baked-points)() const |
| [float](class_float.md#class-float) | [get_closest_offset](class_curve2d.md#class-curve2d-method-get-closest-offset)(to_point: [Vector2](class_vector2.md#class-vector2)) const |
| [Vector2](class_vector2.md#class-vector2) | [get_closest_point](class_curve2d.md#class-curve2d-method-get-closest-point)(to_point: [Vector2](class_vector2.md#class-vector2)) const |
| [Vector2](class_vector2.md#class-vector2) | [get_point_in](class_curve2d.md#class-curve2d-method-get-point-in)(idx: [int](class_int.md#class-int)) const |
| [Vector2](class_vector2.md#class-vector2) | [get_point_out](class_curve2d.md#class-curve2d-method-get-point-out)(idx: [int](class_int.md#class-int)) const |
| [Vector2](class_vector2.md#class-vector2) | [get_point_position](class_curve2d.md#class-curve2d-method-get-point-position)(idx: [int](class_int.md#class-int)) const |
| void | [remove_point](class_curve2d.md#class-curve2d-method-remove-point)(idx: [int](class_int.md#class-int)) |
| [Vector2](class_vector2.md#class-vector2) | [sample](class_curve2d.md#class-curve2d-method-sample)(idx: [int](class_int.md#class-int), t: [float](class_float.md#class-float)) const |
| [Vector2](class_vector2.md#class-vector2) | [sample_baked](class_curve2d.md#class-curve2d-method-sample-baked)(offset: [float](class_float.md#class-float) = 0.0, cubic: [bool](class_bool.md#class-bool) = false) const |
| [Transform2D](class_transform2d.md#class-transform2d) | [sample_baked_with_rotation](class_curve2d.md#class-curve2d-method-sample-baked-with-rotation)(offset: [float](class_float.md#class-float) = 0.0, cubic: [bool](class_bool.md#class-bool) = false) const |
| [Vector2](class_vector2.md#class-vector2) | [samplef](class_curve2d.md#class-curve2d-method-samplef)(fofs: [float](class_float.md#class-float)) const |
| void | [set_point_in](class_curve2d.md#class-curve2d-method-set-point-in)(idx: [int](class_int.md#class-int), position: [Vector2](class_vector2.md#class-vector2)) |
| void | [set_point_out](class_curve2d.md#class-curve2d-method-set-point-out)(idx: [int](class_int.md#class-int), position: [Vector2](class_vector2.md#class-vector2)) |
| void | [set_point_position](class_curve2d.md#class-curve2d-method-set-point-position)(idx: [int](class_int.md#class-int), position: [Vector2](class_vector2.md#class-vector2)) |
| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) | [tessellate](class_curve2d.md#class-curve2d-method-tessellate)(max_stages: [int](class_int.md#class-int) = 5, tolerance_degrees: [float](class_float.md#class-float) = 4) const |
| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) | [tessellate_even_length](class_curve2d.md#class-curve2d-method-tessellate-even-length)(max_stages: [int](class_int.md#class-int) = 5, tolerance_length: [float](class_float.md#class-float) = 20.0) const |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-curve2d-property-bake-interval"></a>

[float](class_float.md#class-float) **bake_interval** = `5.0` [🔗](class_curve2d.md#class-curve2d-property-bake-interval)

- void **set_bake_interval**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_bake_interval**()

The distance in pixels between two adjacent cached points. Changing it forces the cache to be recomputed the next time the [get_baked_points()](class_curve2d.md#class-curve2d-method-get-baked-points) or [get_baked_length()](class_curve2d.md#class-curve2d-method-get-baked-length) function is called. The smaller the distance, the more points in the cache and the more memory it will consume, so use with care.

---


<a id="class-curve2d-property-point-count"></a>

[int](class_int.md#class-int) **point_count** = `0` [🔗](class_curve2d.md#class-curve2d-property-point-count)

- void **set_point_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_point_count**()

The number of points describing the curve.

---


<a id="class-curve2d-property-point-index-in"></a>

[Vector2](class_vector2.md#class-vector2) **point_{index}/in** = `Vector2(0, 0)` [🔗](class_curve2d.md#class-curve2d-property-point-index-in)

The position of the control point leading to the vertex at `index`.

**Note:** `index` is a value in the `0 .. point_count - 1` range.

---


<a id="class-curve2d-property-point-index-out"></a>

[Vector2](class_vector2.md#class-vector2) **point_{index}/out** = `Vector2(0, 0)` [🔗](class_curve2d.md#class-curve2d-property-point-index-out)

The position of the control point leading out of the vertex at `index`.

**Note:** `index` is a value in the `0 .. point_count - 1` range.

---


<a id="class-curve2d-property-point-index-position"></a>

[Vector2](class_vector2.md#class-vector2) **point_{index}/position** = `Vector2(0, 0)` [🔗](class_curve2d.md#class-curve2d-property-point-index-position)

The position of for the vertex at `index`.

**Note:** `index` is a value in the `0 .. point_count - 1` range.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-curve2d-method-add-point"></a>

void **add_point**(position: [Vector2](class_vector2.md#class-vector2), in: [Vector2](class_vector2.md#class-vector2) = Vector2(0, 0), out: [Vector2](class_vector2.md#class-vector2) = Vector2(0, 0), index: [int](class_int.md#class-int) = -1) [🔗](class_curve2d.md#class-curve2d-method-add-point)

Adds a point with the specified `position` relative to the curve's own position, with control points `in` and `out`. Appends the new point at the end of the point list.

If `index` is given, the new point is inserted before the existing point identified by index `index`. Every existing point starting from `index` is shifted further down the list of points. The index must be greater than or equal to `0` and must not exceed the number of existing points in the line. See [point_count](class_curve2d.md#class-curve2d-property-point-count).

---


<a id="class-curve2d-method-clear-points"></a>

void **clear_points**() [🔗](class_curve2d.md#class-curve2d-method-clear-points)

Removes all points from the curve.

---


<a id="class-curve2d-method-get-baked-length"></a>

[float](class_float.md#class-float) **get_baked_length**() const [🔗](class_curve2d.md#class-curve2d-method-get-baked-length)

Returns the total length of the curve, based on the cached points. Given enough density (see [bake_interval](class_curve2d.md#class-curve2d-property-bake-interval)), it should be approximate enough.

---


<a id="class-curve2d-method-get-baked-points"></a>

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **get_baked_points**() const [🔗](class_curve2d.md#class-curve2d-method-get-baked-points)

Returns the cache of points as a [PackedVector2Array](class_packedvector2array.md#class-packedvector2array).

---


<a id="class-curve2d-method-get-closest-offset"></a>

[float](class_float.md#class-float) **get_closest_offset**(to_point: [Vector2](class_vector2.md#class-vector2)) const [🔗](class_curve2d.md#class-curve2d-method-get-closest-offset)

Returns the closest offset to `to_point`. This offset is meant to be used in [sample_baked()](class_curve2d.md#class-curve2d-method-sample-baked).

`to_point` must be in this curve's local space.

---


<a id="class-curve2d-method-get-closest-point"></a>

[Vector2](class_vector2.md#class-vector2) **get_closest_point**(to_point: [Vector2](class_vector2.md#class-vector2)) const [🔗](class_curve2d.md#class-curve2d-method-get-closest-point)

Returns the closest point on baked segments (in curve's local space) to `to_point`.

`to_point` must be in this curve's local space.

---


<a id="class-curve2d-method-get-point-in"></a>

[Vector2](class_vector2.md#class-vector2) **get_point_in**(idx: [int](class_int.md#class-int)) const [🔗](class_curve2d.md#class-curve2d-method-get-point-in)

Returns the position of the control point leading to the vertex `idx`. The returned position is relative to the vertex `idx`. If the index is out of bounds, the function sends an error to the console, and returns `(0, 0)`.

---


<a id="class-curve2d-method-get-point-out"></a>

[Vector2](class_vector2.md#class-vector2) **get_point_out**(idx: [int](class_int.md#class-int)) const [🔗](class_curve2d.md#class-curve2d-method-get-point-out)

Returns the position of the control point leading out of the vertex `idx`. The returned position is relative to the vertex `idx`. If the index is out of bounds, the function sends an error to the console, and returns `(0, 0)`.

---


<a id="class-curve2d-method-get-point-position"></a>

[Vector2](class_vector2.md#class-vector2) **get_point_position**(idx: [int](class_int.md#class-int)) const [🔗](class_curve2d.md#class-curve2d-method-get-point-position)

Returns the position of the vertex `idx`. If the index is out of bounds, the function sends an error to the console, and returns `(0, 0)`.

---


<a id="class-curve2d-method-remove-point"></a>

void **remove_point**(idx: [int](class_int.md#class-int)) [🔗](class_curve2d.md#class-curve2d-method-remove-point)

Deletes the point `idx` from the curve. Sends an error to the console if `idx` is out of bounds.

---


<a id="class-curve2d-method-sample"></a>

[Vector2](class_vector2.md#class-vector2) **sample**(idx: [int](class_int.md#class-int), t: [float](class_float.md#class-float)) const [🔗](class_curve2d.md#class-curve2d-method-sample)

Returns the position between the vertex `idx` and the vertex `idx + 1`, where `t` controls if the point is the first vertex (`t = 0.0`), the last vertex (`t = 1.0`), or in between. Values of `t` outside the range (`0.0 <= t <= 1.0`) give strange, but predictable results.

If `idx` is out of bounds it is truncated to the first or last vertex, and `t` is ignored. If the curve has no points, the function sends an error to the console, and returns `(0, 0)`.

---


<a id="class-curve2d-method-sample-baked"></a>

[Vector2](class_vector2.md#class-vector2) **sample_baked**(offset: [float](class_float.md#class-float) = 0.0, cubic: [bool](class_bool.md#class-bool) = false) const [🔗](class_curve2d.md#class-curve2d-method-sample-baked)

Returns a point within the curve at position `offset`, where `offset` is measured as a pixel distance along the curve.

To do that, it finds the two cached points where the `offset` lies between, then interpolates the values. This interpolation is cubic if `cubic` is set to `true`, or linear if set to `false`.

Cubic interpolation tends to follow the curves better, but linear is faster (and often, precise enough).

---


<a id="class-curve2d-method-sample-baked-with-rotation"></a>

[Transform2D](class_transform2d.md#class-transform2d) **sample_baked_with_rotation**(offset: [float](class_float.md#class-float) = 0.0, cubic: [bool](class_bool.md#class-bool) = false) const [🔗](class_curve2d.md#class-curve2d-method-sample-baked-with-rotation)

Similar to [sample_baked()](class_curve2d.md#class-curve2d-method-sample-baked), but returns [Transform2D](class_transform2d.md#class-transform2d) that includes a rotation along the curve, with [Transform2D.origin](class_transform2d.md#class-transform2d-property-origin) as the point position and the [Transform2D.x](class_transform2d.md#class-transform2d-property-x) vector pointing in the direction of the path at that point. Returns an empty transform if the length of the curve is `0`.

```gdscript
var baked = curve.sample_baked_with_rotation(offset)
# The returned Transform2D can be set directly.
transform = baked
# You can also read the origin and rotation separately from the returned Transform2D.
position = baked.get_origin()
rotation = baked.get_rotation()
```

---


<a id="class-curve2d-method-samplef"></a>

[Vector2](class_vector2.md#class-vector2) **samplef**(fofs: [float](class_float.md#class-float)) const [🔗](class_curve2d.md#class-curve2d-method-samplef)

Returns the position at the vertex `fofs`. It calls [sample()](class_curve2d.md#class-curve2d-method-sample) using the integer part of `fofs` as `idx`, and its fractional part as `t`.

---


<a id="class-curve2d-method-set-point-in"></a>

void **set_point_in**(idx: [int](class_int.md#class-int), position: [Vector2](class_vector2.md#class-vector2)) [🔗](class_curve2d.md#class-curve2d-method-set-point-in)

Sets the position of the control point leading to the vertex `idx`. If the index is out of bounds, the function sends an error to the console. The position is relative to the vertex.

---


<a id="class-curve2d-method-set-point-out"></a>

void **set_point_out**(idx: [int](class_int.md#class-int), position: [Vector2](class_vector2.md#class-vector2)) [🔗](class_curve2d.md#class-curve2d-method-set-point-out)

Sets the position of the control point leading out of the vertex `idx`. If the index is out of bounds, the function sends an error to the console. The position is relative to the vertex.

---


<a id="class-curve2d-method-set-point-position"></a>

void **set_point_position**(idx: [int](class_int.md#class-int), position: [Vector2](class_vector2.md#class-vector2)) [🔗](class_curve2d.md#class-curve2d-method-set-point-position)

Sets the position for the vertex `idx`. If the index is out of bounds, the function sends an error to the console.

---


<a id="class-curve2d-method-tessellate"></a>

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **tessellate**(max_stages: [int](class_int.md#class-int) = 5, tolerance_degrees: [float](class_float.md#class-float) = 4) const [🔗](class_curve2d.md#class-curve2d-method-tessellate)

Returns a list of points along the curve, with a curvature controlled point density. That is, the curvier parts will have more points than the straighter parts.

This approximation makes straight segments between each point, then subdivides those segments until the resulting shape is similar enough.

`max_stages` controls how many subdivisions a curve segment may face before it is considered approximate enough. Each subdivision splits the segment in half, so the default 5 stages may mean up to 32 subdivisions per curve segment. Increase with care!

`tolerance_degrees` controls how many degrees the midpoint of a segment may deviate from the real curve, before the segment has to be subdivided.

---


<a id="class-curve2d-method-tessellate-even-length"></a>

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **tessellate_even_length**(max_stages: [int](class_int.md#class-int) = 5, tolerance_length: [float](class_float.md#class-float) = 20.0) const [🔗](class_curve2d.md#class-curve2d-method-tessellate-even-length)

Returns a list of points along the curve, with almost uniform density. `max_stages` controls how many subdivisions a curve segment may face before it is considered approximate enough. Each subdivision splits the segment in half, so the default 5 stages may mean up to 32 subdivisions per curve segment. Increase with care!

`tolerance_length` controls the maximal distance between two neighboring points, before the segment has to be subdivided.
