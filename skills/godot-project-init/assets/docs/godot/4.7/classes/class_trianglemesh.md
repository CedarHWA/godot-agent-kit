> Source: https://docs.godotengine.org/en/4.7/classes/class_trianglemesh.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="trianglemesh"></a>

<a id="class-trianglemesh"></a>

# TriangleMesh

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Triangle geometry for efficient, physicsless intersection queries.

<a id="description"></a>

## Description

Creates a bounding volume hierarchy (BVH) tree structure around triangle geometry.

The triangle BVH tree can be used for efficient intersection queries without involving a physics engine.

For example, this can be used in editor tools to select objects with complex shapes based on the mouse cursor position.

**Performance:** Creating the BVH tree for complex geometry is a slow process and best done in a background thread.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [create_from_faces](class_trianglemesh.md#class-trianglemesh-method-create-from-faces)(faces: [PackedVector3Array](class_packedvector3array.md#class-packedvector3array)) |
| [PackedVector3Array](class_packedvector3array.md#class-packedvector3array) | [get_faces](class_trianglemesh.md#class-trianglemesh-method-get-faces)() const |
| [Dictionary](class_dictionary.md#class-dictionary) | [intersect_ray](class_trianglemesh.md#class-trianglemesh-method-intersect-ray)(begin: [Vector3](class_vector3.md#class-vector3), dir: [Vector3](class_vector3.md#class-vector3)) const |
| [Dictionary](class_dictionary.md#class-dictionary) | [intersect_segment](class_trianglemesh.md#class-trianglemesh-method-intersect-segment)(begin: [Vector3](class_vector3.md#class-vector3), end: [Vector3](class_vector3.md#class-vector3)) const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-trianglemesh-method-create-from-faces"></a>

[bool](class_bool.md#class-bool) **create_from_faces**(faces: [PackedVector3Array](class_packedvector3array.md#class-packedvector3array)) [🔗](class_trianglemesh.md#class-trianglemesh-method-create-from-faces)

Creates the BVH tree from an array of faces. Each 3 vertices of the input `faces` array represent one triangle (face).

Returns `true` if the tree is successfully built, `false` otherwise.

---


<a id="class-trianglemesh-method-get-faces"></a>

[PackedVector3Array](class_packedvector3array.md#class-packedvector3array) **get_faces**() const [🔗](class_trianglemesh.md#class-trianglemesh-method-get-faces)

Returns a copy of the geometry faces. Each 3 vertices of the array represent one triangle (face).

---


<a id="class-trianglemesh-method-intersect-ray"></a>

[Dictionary](class_dictionary.md#class-dictionary) **intersect_ray**(begin: [Vector3](class_vector3.md#class-vector3), dir: [Vector3](class_vector3.md#class-vector3)) const [🔗](class_trianglemesh.md#class-trianglemesh-method-intersect-ray)

Tests for intersection with a ray starting at `begin` and facing `dir` and extending toward infinity.

If an intersection with a triangle happens, returns a [Dictionary](class_dictionary.md#class-dictionary) with the following fields:

`position`: The position on the intersected triangle.

`normal`: The normal of the intersected triangle.

`face_index`: The index of the intersected triangle.

Returns an empty [Dictionary](class_dictionary.md#class-dictionary) if no intersection happens.

See also [intersect_segment()](class_trianglemesh.md#class-trianglemesh-method-intersect-segment), which is similar but uses a finite-length segment.

---


<a id="class-trianglemesh-method-intersect-segment"></a>

[Dictionary](class_dictionary.md#class-dictionary) **intersect_segment**(begin: [Vector3](class_vector3.md#class-vector3), end: [Vector3](class_vector3.md#class-vector3)) const [🔗](class_trianglemesh.md#class-trianglemesh-method-intersect-segment)

Tests for intersection with a segment going from `begin` to `end`.

If an intersection with a triangle happens returns a [Dictionary](class_dictionary.md#class-dictionary) with the following fields:

`position`: The position on the intersected triangle.

`normal`: The normal of the intersected triangle.

`face_index`: The index of the intersected triangle.

Returns an empty [Dictionary](class_dictionary.md#class-dictionary) if no intersection happens.

See also [intersect_ray()](class_trianglemesh.md#class-trianglemesh-method-intersect-ray), which is similar but uses an infinite-length ray.
