> Source: https://docs.godotengine.org/en/4.7/classes/class_kinematiccollision2d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="kinematiccollision2d"></a>

<a id="class-kinematiccollision2d"></a>

# KinematicCollision2D

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Holds collision data from the movement of a [PhysicsBody2D](class_physicsbody2d.md#class-physicsbody2d).

<a id="description"></a>

## Description

Holds collision data from the movement of a [PhysicsBody2D](class_physicsbody2d.md#class-physicsbody2d), usually from [PhysicsBody2D.move_and_collide()](class_physicsbody2d.md#class-physicsbody2d-method-move-and-collide). When a [PhysicsBody2D](class_physicsbody2d.md#class-physicsbody2d) is moved, it stops if it detects a collision with another body. If a collision is detected, a **KinematicCollision2D** object is returned.

The collision data includes the colliding object, the remaining motion, and the collision position. This data can be used to determine a custom response to the collision.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [float](class_float.md#class-float) | [get_angle](class_kinematiccollision2d.md#class-kinematiccollision2d-method-get-angle)(up_direction: [Vector2](class_vector2.md#class-vector2) = Vector2(0, -1)) const |
| [Object](class_object.md#class-object) | [get_collider](class_kinematiccollision2d.md#class-kinematiccollision2d-method-get-collider)() const |
| [int](class_int.md#class-int) | [get_collider_id](class_kinematiccollision2d.md#class-kinematiccollision2d-method-get-collider-id)() const |
| [RID](class_rid.md#class-rid) | [get_collider_rid](class_kinematiccollision2d.md#class-kinematiccollision2d-method-get-collider-rid)() const |
| [Object](class_object.md#class-object) | [get_collider_shape](class_kinematiccollision2d.md#class-kinematiccollision2d-method-get-collider-shape)() const |
| [int](class_int.md#class-int) | [get_collider_shape_index](class_kinematiccollision2d.md#class-kinematiccollision2d-method-get-collider-shape-index)() const |
| [Vector2](class_vector2.md#class-vector2) | [get_collider_velocity](class_kinematiccollision2d.md#class-kinematiccollision2d-method-get-collider-velocity)() const |
| [float](class_float.md#class-float) | [get_depth](class_kinematiccollision2d.md#class-kinematiccollision2d-method-get-depth)() const |
| [Object](class_object.md#class-object) | [get_local_shape](class_kinematiccollision2d.md#class-kinematiccollision2d-method-get-local-shape)() const |
| [Vector2](class_vector2.md#class-vector2) | [get_normal](class_kinematiccollision2d.md#class-kinematiccollision2d-method-get-normal)() const |
| [Vector2](class_vector2.md#class-vector2) | [get_position](class_kinematiccollision2d.md#class-kinematiccollision2d-method-get-position)() const |
| [Vector2](class_vector2.md#class-vector2) | [get_remainder](class_kinematiccollision2d.md#class-kinematiccollision2d-method-get-remainder)() const |
| [Vector2](class_vector2.md#class-vector2) | [get_travel](class_kinematiccollision2d.md#class-kinematiccollision2d-method-get-travel)() const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-kinematiccollision2d-method-get-angle"></a>

[float](class_float.md#class-float) **get_angle**(up_direction: [Vector2](class_vector2.md#class-vector2) = Vector2(0, -1)) const [🔗](class_kinematiccollision2d.md#class-kinematiccollision2d-method-get-angle)

Returns the collision angle according to `up_direction`, which is [Vector2.UP](class_vector2.md#class-vector2-constant-up) by default. This value is always positive.

---


<a id="class-kinematiccollision2d-method-get-collider"></a>

[Object](class_object.md#class-object) **get_collider**() const [🔗](class_kinematiccollision2d.md#class-kinematiccollision2d-method-get-collider)

Returns the colliding body's attached [Object](class_object.md#class-object).

---


<a id="class-kinematiccollision2d-method-get-collider-id"></a>

[int](class_int.md#class-int) **get_collider_id**() const [🔗](class_kinematiccollision2d.md#class-kinematiccollision2d-method-get-collider-id)

Returns the unique instance ID of the colliding body's attached [Object](class_object.md#class-object). See [Object.get_instance_id()](class_object.md#class-object-method-get-instance-id).

---


<a id="class-kinematiccollision2d-method-get-collider-rid"></a>

[RID](class_rid.md#class-rid) **get_collider_rid**() const [🔗](class_kinematiccollision2d.md#class-kinematiccollision2d-method-get-collider-rid)

Returns the colliding body's [RID](class_rid.md#class-rid) used by the [PhysicsServer2D](class_physicsserver2d.md#class-physicsserver2d).

---


<a id="class-kinematiccollision2d-method-get-collider-shape"></a>

[Object](class_object.md#class-object) **get_collider_shape**() const [🔗](class_kinematiccollision2d.md#class-kinematiccollision2d-method-get-collider-shape)

Returns the colliding body's shape.

---


<a id="class-kinematiccollision2d-method-get-collider-shape-index"></a>

[int](class_int.md#class-int) **get_collider_shape_index**() const [🔗](class_kinematiccollision2d.md#class-kinematiccollision2d-method-get-collider-shape-index)

Returns the colliding body's shape index. See [CollisionObject2D](class_collisionobject2d.md#class-collisionobject2d).

---


<a id="class-kinematiccollision2d-method-get-collider-velocity"></a>

[Vector2](class_vector2.md#class-vector2) **get_collider_velocity**() const [🔗](class_kinematiccollision2d.md#class-kinematiccollision2d-method-get-collider-velocity)

Returns the colliding body's velocity.

---


<a id="class-kinematiccollision2d-method-get-depth"></a>

[float](class_float.md#class-float) **get_depth**() const [🔗](class_kinematiccollision2d.md#class-kinematiccollision2d-method-get-depth)

Returns the colliding body's length of overlap along the collision normal.

---


<a id="class-kinematiccollision2d-method-get-local-shape"></a>

[Object](class_object.md#class-object) **get_local_shape**() const [🔗](class_kinematiccollision2d.md#class-kinematiccollision2d-method-get-local-shape)

Returns the moving object's colliding shape.

---


<a id="class-kinematiccollision2d-method-get-normal"></a>

[Vector2](class_vector2.md#class-vector2) **get_normal**() const [🔗](class_kinematiccollision2d.md#class-kinematiccollision2d-method-get-normal)

Returns the colliding body's shape's normal at the point of collision.

---


<a id="class-kinematiccollision2d-method-get-position"></a>

[Vector2](class_vector2.md#class-vector2) **get_position**() const [🔗](class_kinematiccollision2d.md#class-kinematiccollision2d-method-get-position)

Returns the point of collision in global coordinates.

---


<a id="class-kinematiccollision2d-method-get-remainder"></a>

[Vector2](class_vector2.md#class-vector2) **get_remainder**() const [🔗](class_kinematiccollision2d.md#class-kinematiccollision2d-method-get-remainder)

Returns the moving object's remaining movement vector.

---


<a id="class-kinematiccollision2d-method-get-travel"></a>

[Vector2](class_vector2.md#class-vector2) **get_travel**() const [🔗](class_kinematiccollision2d.md#class-kinematiccollision2d-method-get-travel)

Returns the moving object's travel before collision.
