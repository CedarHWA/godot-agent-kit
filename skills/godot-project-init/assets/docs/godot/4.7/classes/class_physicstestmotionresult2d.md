> Source: https://docs.godotengine.org/en/4.7/classes/class_physicstestmotionresult2d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="physicstestmotionresult2d"></a>

<a id="class-physicstestmotionresult2d"></a>

# PhysicsTestMotionResult2D

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Describes the motion and collision result from [PhysicsServer2D.body_test_motion()](class_physicsserver2d.md#class-physicsserver2d-method-body-test-motion).

<a id="description"></a>

## Description

Describes the motion and collision result from [PhysicsServer2D.body_test_motion()](class_physicsserver2d.md#class-physicsserver2d-method-body-test-motion).

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Object](class_object.md#class-object) | [get_collider](class_physicstestmotionresult2d.md#class-physicstestmotionresult2d-method-get-collider)() const |
| [int](class_int.md#class-int) | [get_collider_id](class_physicstestmotionresult2d.md#class-physicstestmotionresult2d-method-get-collider-id)() const |
| [RID](class_rid.md#class-rid) | [get_collider_rid](class_physicstestmotionresult2d.md#class-physicstestmotionresult2d-method-get-collider-rid)() const |
| [int](class_int.md#class-int) | [get_collider_shape](class_physicstestmotionresult2d.md#class-physicstestmotionresult2d-method-get-collider-shape)() const |
| [Vector2](class_vector2.md#class-vector2) | [get_collider_velocity](class_physicstestmotionresult2d.md#class-physicstestmotionresult2d-method-get-collider-velocity)() const |
| [float](class_float.md#class-float) | [get_collision_depth](class_physicstestmotionresult2d.md#class-physicstestmotionresult2d-method-get-collision-depth)() const |
| [int](class_int.md#class-int) | [get_collision_local_shape](class_physicstestmotionresult2d.md#class-physicstestmotionresult2d-method-get-collision-local-shape)() const |
| [Vector2](class_vector2.md#class-vector2) | [get_collision_normal](class_physicstestmotionresult2d.md#class-physicstestmotionresult2d-method-get-collision-normal)() const |
| [Vector2](class_vector2.md#class-vector2) | [get_collision_point](class_physicstestmotionresult2d.md#class-physicstestmotionresult2d-method-get-collision-point)() const |
| [float](class_float.md#class-float) | [get_collision_safe_fraction](class_physicstestmotionresult2d.md#class-physicstestmotionresult2d-method-get-collision-safe-fraction)() const |
| [float](class_float.md#class-float) | [get_collision_unsafe_fraction](class_physicstestmotionresult2d.md#class-physicstestmotionresult2d-method-get-collision-unsafe-fraction)() const |
| [Vector2](class_vector2.md#class-vector2) | [get_remainder](class_physicstestmotionresult2d.md#class-physicstestmotionresult2d-method-get-remainder)() const |
| [Vector2](class_vector2.md#class-vector2) | [get_travel](class_physicstestmotionresult2d.md#class-physicstestmotionresult2d-method-get-travel)() const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-physicstestmotionresult2d-method-get-collider"></a>

[Object](class_object.md#class-object) **get_collider**() const [🔗](class_physicstestmotionresult2d.md#class-physicstestmotionresult2d-method-get-collider)

Returns the colliding body's attached [Object](class_object.md#class-object), if a collision occurred.

---


<a id="class-physicstestmotionresult2d-method-get-collider-id"></a>

[int](class_int.md#class-int) **get_collider_id**() const [🔗](class_physicstestmotionresult2d.md#class-physicstestmotionresult2d-method-get-collider-id)

Returns the unique instance ID of the colliding body's attached [Object](class_object.md#class-object), if a collision occurred. See [Object.get_instance_id()](class_object.md#class-object-method-get-instance-id).

---


<a id="class-physicstestmotionresult2d-method-get-collider-rid"></a>

[RID](class_rid.md#class-rid) **get_collider_rid**() const [🔗](class_physicstestmotionresult2d.md#class-physicstestmotionresult2d-method-get-collider-rid)

Returns the colliding body's [RID](class_rid.md#class-rid) used by the [PhysicsServer2D](class_physicsserver2d.md#class-physicsserver2d), if a collision occurred.

---


<a id="class-physicstestmotionresult2d-method-get-collider-shape"></a>

[int](class_int.md#class-int) **get_collider_shape**() const [🔗](class_physicstestmotionresult2d.md#class-physicstestmotionresult2d-method-get-collider-shape)

Returns the colliding body's shape index, if a collision occurred. See [CollisionObject2D](class_collisionobject2d.md#class-collisionobject2d).

---


<a id="class-physicstestmotionresult2d-method-get-collider-velocity"></a>

[Vector2](class_vector2.md#class-vector2) **get_collider_velocity**() const [🔗](class_physicstestmotionresult2d.md#class-physicstestmotionresult2d-method-get-collider-velocity)

Returns the colliding body's velocity, if a collision occurred.

---


<a id="class-physicstestmotionresult2d-method-get-collision-depth"></a>

[float](class_float.md#class-float) **get_collision_depth**() const [🔗](class_physicstestmotionresult2d.md#class-physicstestmotionresult2d-method-get-collision-depth)

Returns the length of overlap along the collision normal, if a collision occurred.

---


<a id="class-physicstestmotionresult2d-method-get-collision-local-shape"></a>

[int](class_int.md#class-int) **get_collision_local_shape**() const [🔗](class_physicstestmotionresult2d.md#class-physicstestmotionresult2d-method-get-collision-local-shape)

Returns the moving object's colliding shape, if a collision occurred.

---


<a id="class-physicstestmotionresult2d-method-get-collision-normal"></a>

[Vector2](class_vector2.md#class-vector2) **get_collision_normal**() const [🔗](class_physicstestmotionresult2d.md#class-physicstestmotionresult2d-method-get-collision-normal)

Returns the colliding body's shape's normal at the point of collision, if a collision occurred.

---


<a id="class-physicstestmotionresult2d-method-get-collision-point"></a>

[Vector2](class_vector2.md#class-vector2) **get_collision_point**() const [🔗](class_physicstestmotionresult2d.md#class-physicstestmotionresult2d-method-get-collision-point)

Returns the point of collision in global coordinates, if a collision occurred.

---


<a id="class-physicstestmotionresult2d-method-get-collision-safe-fraction"></a>

[float](class_float.md#class-float) **get_collision_safe_fraction**() const [🔗](class_physicstestmotionresult2d.md#class-physicstestmotionresult2d-method-get-collision-safe-fraction)

Returns the maximum fraction of the motion that can occur without a collision, between `0` and `1`.

---


<a id="class-physicstestmotionresult2d-method-get-collision-unsafe-fraction"></a>

[float](class_float.md#class-float) **get_collision_unsafe_fraction**() const [🔗](class_physicstestmotionresult2d.md#class-physicstestmotionresult2d-method-get-collision-unsafe-fraction)

Returns the minimum fraction of the motion needed to collide, if a collision occurred, between `0` and `1`.

---


<a id="class-physicstestmotionresult2d-method-get-remainder"></a>

[Vector2](class_vector2.md#class-vector2) **get_remainder**() const [🔗](class_physicstestmotionresult2d.md#class-physicstestmotionresult2d-method-get-remainder)

Returns the moving object's remaining movement vector.

---


<a id="class-physicstestmotionresult2d-method-get-travel"></a>

[Vector2](class_vector2.md#class-vector2) **get_travel**() const [🔗](class_physicstestmotionresult2d.md#class-physicstestmotionresult2d-method-get-travel)

Returns the moving object's travel before collision.
