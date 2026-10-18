> Source: https://docs.godotengine.org/en/4.7/classes/class_polygonpathfinder.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="polygonpathfinder"></a>

<a id="class-polygonpathfinder"></a>

# PolygonPathFinder

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

There is currently no description for this class. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) | [find_path](class_polygonpathfinder.md#class-polygonpathfinder-method-find-path)(from: [Vector2](class_vector2.md#class-vector2), to: [Vector2](class_vector2.md#class-vector2)) |
| [Rect2](class_rect2.md#class-rect2) | [get_bounds](class_polygonpathfinder.md#class-polygonpathfinder-method-get-bounds)() const |
| [Vector2](class_vector2.md#class-vector2) | [get_closest_point](class_polygonpathfinder.md#class-polygonpathfinder-method-get-closest-point)(point: [Vector2](class_vector2.md#class-vector2)) const |
| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) | [get_intersections](class_polygonpathfinder.md#class-polygonpathfinder-method-get-intersections)(from: [Vector2](class_vector2.md#class-vector2), to: [Vector2](class_vector2.md#class-vector2)) const |
| [float](class_float.md#class-float) | [get_point_penalty](class_polygonpathfinder.md#class-polygonpathfinder-method-get-point-penalty)(idx: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [is_point_inside](class_polygonpathfinder.md#class-polygonpathfinder-method-is-point-inside)(point: [Vector2](class_vector2.md#class-vector2)) const |
| void | [set_point_penalty](class_polygonpathfinder.md#class-polygonpathfinder-method-set-point-penalty)(idx: [int](class_int.md#class-int), penalty: [float](class_float.md#class-float)) |
| void | [setup](class_polygonpathfinder.md#class-polygonpathfinder-method-setup)(points: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), connections: [PackedInt32Array](class_packedint32array.md#class-packedint32array)) |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-polygonpathfinder-method-find-path"></a>

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **find_path**(from: [Vector2](class_vector2.md#class-vector2), to: [Vector2](class_vector2.md#class-vector2)) [🔗](class_polygonpathfinder.md#class-polygonpathfinder-method-find-path)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-polygonpathfinder-method-get-bounds"></a>

[Rect2](class_rect2.md#class-rect2) **get_bounds**() const [🔗](class_polygonpathfinder.md#class-polygonpathfinder-method-get-bounds)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-polygonpathfinder-method-get-closest-point"></a>

[Vector2](class_vector2.md#class-vector2) **get_closest_point**(point: [Vector2](class_vector2.md#class-vector2)) const [🔗](class_polygonpathfinder.md#class-polygonpathfinder-method-get-closest-point)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-polygonpathfinder-method-get-intersections"></a>

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **get_intersections**(from: [Vector2](class_vector2.md#class-vector2), to: [Vector2](class_vector2.md#class-vector2)) const [🔗](class_polygonpathfinder.md#class-polygonpathfinder-method-get-intersections)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-polygonpathfinder-method-get-point-penalty"></a>

[float](class_float.md#class-float) **get_point_penalty**(idx: [int](class_int.md#class-int)) const [🔗](class_polygonpathfinder.md#class-polygonpathfinder-method-get-point-penalty)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-polygonpathfinder-method-is-point-inside"></a>

[bool](class_bool.md#class-bool) **is_point_inside**(point: [Vector2](class_vector2.md#class-vector2)) const [🔗](class_polygonpathfinder.md#class-polygonpathfinder-method-is-point-inside)

Returns `true` if `point` falls inside the polygon area.

```gdscript
var polygon_path_finder = PolygonPathFinder.new()
var points = [Vector2(0.0, 0.0), Vector2(1.0, 0.0), Vector2(0.0, 1.0)]
var connections = [0, 1, 1, 2, 2, 0]
polygon_path_finder.setup(points, connections)
print(polygon_path_finder.is_point_inside(Vector2(0.2, 0.2))) # Prints true
print(polygon_path_finder.is_point_inside(Vector2(1.0, 1.0))) # Prints false
```

```csharp
var polygonPathFinder = new PolygonPathFinder();
Vector2[] points =
[
    new Vector2(0.0f, 0.0f),
    new Vector2(1.0f, 0.0f),
    new Vector2(0.0f, 1.0f)
];
int[] connections = [0, 1, 1, 2, 2, 0];
polygonPathFinder.Setup(points, connections);
GD.Print(polygonPathFinder.IsPointInside(new Vector2(0.2f, 0.2f))); // Prints True
GD.Print(polygonPathFinder.IsPointInside(new Vector2(1.0f, 1.0f))); // Prints False
```

---


<a id="class-polygonpathfinder-method-set-point-penalty"></a>

void **set_point_penalty**(idx: [int](class_int.md#class-int), penalty: [float](class_float.md#class-float)) [🔗](class_polygonpathfinder.md#class-polygonpathfinder-method-set-point-penalty)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-polygonpathfinder-method-setup"></a>

void **setup**(points: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), connections: [PackedInt32Array](class_packedint32array.md#class-packedint32array)) [🔗](class_polygonpathfinder.md#class-polygonpathfinder-method-setup)

Sets up **PolygonPathFinder** with an array of points that define the vertices of the polygon, and an array of indices that determine the edges of the polygon.

The length of `connections` must be even, returns an error if odd.

```gdscript
var polygon_path_finder = PolygonPathFinder.new()
var points = [Vector2(0.0, 0.0), Vector2(1.0, 0.0), Vector2(0.0, 1.0)]
var connections = [0, 1, 1, 2, 2, 0]
polygon_path_finder.setup(points, connections)
```

```csharp
var polygonPathFinder = new PolygonPathFinder();
Vector2[] points =
[
    new Vector2(0.0f, 0.0f),
    new Vector2(1.0f, 0.0f),
    new Vector2(0.0f, 1.0f)
];
int[] connections = [0, 1, 1, 2, 2, 0];
polygonPathFinder.Setup(points, connections);
```
