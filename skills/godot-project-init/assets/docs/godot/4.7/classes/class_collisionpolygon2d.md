> Source: https://docs.godotengine.org/en/4.7/classes/class_collisionpolygon2d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="collisionpolygon2d"></a>

<a id="class-collisionpolygon2d"></a>

# CollisionPolygon2D

**Inherits:** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A node that provides a polygon shape to a [CollisionObject2D](class_collisionobject2d.md#class-collisionobject2d) parent.

<a id="description"></a>

## Description

A node that provides a polygon shape to a [CollisionObject2D](class_collisionobject2d.md#class-collisionobject2d) parent and allows it to be edited. The polygon can be concave or convex. This can give a detection shape to an [Area2D](class_area2d.md#class-area2d), turn a [PhysicsBody2D](class_physicsbody2d.md#class-physicsbody2d) into a solid object, or give a hollow shape to a [StaticBody2D](class_staticbody2d.md#class-staticbody2d).

**Warning:** A non-uniformly scaled **CollisionPolygon2D** will likely not behave as expected. Make sure to keep its scale the same on all axes and adjust its polygon instead.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [BuildMode](class_collisionpolygon2d.md#enum-collisionpolygon2d-buildmode) | [build_mode](class_collisionpolygon2d.md#class-collisionpolygon2d-property-build-mode) | `0` |
| [bool](class_bool.md#class-bool) | [disabled](class_collisionpolygon2d.md#class-collisionpolygon2d-property-disabled) | `false` |
| [bool](class_bool.md#class-bool) | [one_way_collision](class_collisionpolygon2d.md#class-collisionpolygon2d-property-one-way-collision) | `false` |
| [Vector2](class_vector2.md#class-vector2) | [one_way_collision_direction](class_collisionpolygon2d.md#class-collisionpolygon2d-property-one-way-collision-direction) | `Vector2(0, 1)` |
| [float](class_float.md#class-float) | [one_way_collision_margin](class_collisionpolygon2d.md#class-collisionpolygon2d-property-one-way-collision-margin) | `1.0` |
| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) | [polygon](class_collisionpolygon2d.md#class-collisionpolygon2d-property-polygon) | `PackedVector2Array()` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-collisionpolygon2d-buildmode"></a>

enum **BuildMode**: [🔗](class_collisionpolygon2d.md#enum-collisionpolygon2d-buildmode)

<a id="class-collisionpolygon2d-constant-build-solids"></a>

[BuildMode](class_collisionpolygon2d.md#enum-collisionpolygon2d-buildmode) **BUILD_SOLIDS** = `0`

Collisions will include the polygon and its contained area. In this mode the node has the same effect as several [ConvexPolygonShape2D](class_convexpolygonshape2d.md#class-convexpolygonshape2d) nodes, one for each convex shape in the convex decomposition of the polygon (but without the overhead of multiple nodes).

<a id="class-collisionpolygon2d-constant-build-segments"></a>

[BuildMode](class_collisionpolygon2d.md#enum-collisionpolygon2d-buildmode) **BUILD_SEGMENTS** = `1`

Collisions will only include the polygon edges. In this mode the node has the same effect as a single [ConcavePolygonShape2D](class_concavepolygonshape2d.md#class-concavepolygonshape2d) made of segments, with the restriction that each segment (after the first one) starts where the previous one ends, and the last one ends where the first one starts (forming a closed but hollow polygon).

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-collisionpolygon2d-property-build-mode"></a>

[BuildMode](class_collisionpolygon2d.md#enum-collisionpolygon2d-buildmode) **build_mode** = `0` [🔗](class_collisionpolygon2d.md#class-collisionpolygon2d-property-build-mode)

- void **set_build_mode**(value: [BuildMode](class_collisionpolygon2d.md#enum-collisionpolygon2d-buildmode))
- [BuildMode](class_collisionpolygon2d.md#enum-collisionpolygon2d-buildmode) **get_build_mode**()

Collision build mode.

---


<a id="class-collisionpolygon2d-property-disabled"></a>

[bool](class_bool.md#class-bool) **disabled** = `false` [🔗](class_collisionpolygon2d.md#class-collisionpolygon2d-property-disabled)

- void **set_disabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_disabled**()

If `true`, no collisions will be detected. This property should be changed with [Object.set_deferred()](class_object.md#class-object-method-set-deferred).

---


<a id="class-collisionpolygon2d-property-one-way-collision"></a>

[bool](class_bool.md#class-bool) **one_way_collision** = `false` [🔗](class_collisionpolygon2d.md#class-collisionpolygon2d-property-one-way-collision)

- void **set_one_way_collision**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_one_way_collision_enabled**()

If `true`, only edges that face up, relative to **CollisionPolygon2D**'s rotation, will collide with other objects.

**Note:** This property has no effect if this **CollisionPolygon2D** is a child of an [Area2D](class_area2d.md#class-area2d) node.

**Note:** The one way collision direction can be configured by setting [one_way_collision_direction](class_collisionpolygon2d.md#class-collisionpolygon2d-property-one-way-collision-direction).

---


<a id="class-collisionpolygon2d-property-one-way-collision-direction"></a>

[Vector2](class_vector2.md#class-vector2) **one_way_collision_direction** = `Vector2(0, 1)` [🔗](class_collisionpolygon2d.md#class-collisionpolygon2d-property-one-way-collision-direction)

- void **set_one_way_collision_direction**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_one_way_collision_direction**()

The direction used for one-way collision.

---


<a id="class-collisionpolygon2d-property-one-way-collision-margin"></a>

[float](class_float.md#class-float) **one_way_collision_margin** = `1.0` [🔗](class_collisionpolygon2d.md#class-collisionpolygon2d-property-one-way-collision-margin)

- void **set_one_way_collision_margin**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_one_way_collision_margin**()

The margin used for one-way collision (in pixels). Higher values will make the shape thicker, and work better for colliders that enter the polygon at a high velocity.

---


<a id="class-collisionpolygon2d-property-polygon"></a>

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **polygon** = `PackedVector2Array()` [🔗](class_collisionpolygon2d.md#class-collisionpolygon2d-property-polygon)

- void **set_polygon**(value: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array))
- [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **get_polygon**()

The polygon's list of vertices. Each point will be connected to the next, and the final point will be connected to the first.

**Note:** The returned vertices are in the local coordinate space of the given **CollisionPolygon2D**.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) for more details.
