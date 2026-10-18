> Source: https://docs.godotengine.org/en/4.7/classes/class_concavepolygonshape3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="concavepolygonshape3d"></a>

<a id="class-concavepolygonshape3d"></a>

# ConcavePolygonShape3D

**Inherits:** [Shape3D](class_shape3d.md#class-shape3d) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A 3D trimesh shape used for physics collision.

<a id="description"></a>

## Description

A 3D trimesh shape, intended for use in physics. Usually used to provide a shape for a [CollisionShape3D](class_collisionshape3d.md#class-collisionshape3d).

Being just a collection of interconnected triangles, **ConcavePolygonShape3D** is the most freely configurable single 3D shape. It can be used to form polyhedra of any nature, or even shapes that don't enclose a volume. However, **ConcavePolygonShape3D** is *hollow* even if the interconnected triangles do enclose a volume, which often makes it unsuitable for physics or detection.

**Note:** When used for collision, **ConcavePolygonShape3D** is intended to work with static [CollisionShape3D](class_collisionshape3d.md#class-collisionshape3d) nodes like [StaticBody3D](class_staticbody3d.md#class-staticbody3d) and will likely not behave well for [CharacterBody3D](class_characterbody3d.md#class-characterbody3d)s or [RigidBody3D](class_rigidbody3d.md#class-rigidbody3d)s in a mode other than Static.

**Warning:** Physics bodies that are small have a chance to clip through this shape when moving fast. This happens because on one frame, the physics body may be on the "outside" of the shape, and on the next frame it may be "inside" it. **ConcavePolygonShape3D** is hollow, so it won't detect a collision.

**Performance:** Due to its complexity, **ConcavePolygonShape3D** is the slowest 3D collision shape to check collisions against. Its use should generally be limited to level geometry. For convex geometry, [ConvexPolygonShape3D](class_convexpolygonshape3d.md#class-convexpolygonshape3d) should be used. For dynamic physics bodies that need concave collision, several [ConvexPolygonShape3D](class_convexpolygonshape3d.md#class-convexpolygonshape3d)s can be used to represent its collision by using convex decomposition; see [ConvexPolygonShape3D](class_convexpolygonshape3d.md#class-convexpolygonshape3d)'s documentation for instructions.

<a id="tutorials"></a>

## Tutorials

- [3D Physics Tests Demo](https://godotengine.org/asset-library/asset/2747)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [backface_collision](class_concavepolygonshape3d.md#class-concavepolygonshape3d-property-backface-collision) | `false` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [PackedVector3Array](class_packedvector3array.md#class-packedvector3array) | [get_faces](class_concavepolygonshape3d.md#class-concavepolygonshape3d-method-get-faces)() const |
| void | [set_faces](class_concavepolygonshape3d.md#class-concavepolygonshape3d-method-set-faces)(faces: [PackedVector3Array](class_packedvector3array.md#class-packedvector3array)) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-concavepolygonshape3d-property-backface-collision"></a>

[bool](class_bool.md#class-bool) **backface_collision** = `false` [🔗](class_concavepolygonshape3d.md#class-concavepolygonshape3d-property-backface-collision)

- void **set_backface_collision_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_backface_collision_enabled**()

If set to `true`, collisions occur on both sides of the concave shape faces. Otherwise they occur only along the face normals.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-concavepolygonshape3d-method-get-faces"></a>

[PackedVector3Array](class_packedvector3array.md#class-packedvector3array) **get_faces**() const [🔗](class_concavepolygonshape3d.md#class-concavepolygonshape3d-method-get-faces)

Returns the faces of the trimesh shape as an array of vertices. The array (of length divisible by three) is naturally divided into triples; each triple of vertices defines a triangle.

---


<a id="class-concavepolygonshape3d-method-set-faces"></a>

void **set_faces**(faces: [PackedVector3Array](class_packedvector3array.md#class-packedvector3array)) [🔗](class_concavepolygonshape3d.md#class-concavepolygonshape3d-method-set-faces)

Sets the faces of the trimesh shape from an array of vertices. The `faces` array should be composed of triples such that each triple of vertices defines a triangle.
