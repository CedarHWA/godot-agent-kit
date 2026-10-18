> Source: https://docs.godotengine.org/en/4.7/classes/class_physicstestmotionresult3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="physicstestmotionresult3d"></a>

<a id="class-physicstestmotionresult3d"></a>

# PhysicsTestMotionResult3D

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Describes the motion and collision result from [PhysicsServer3D.body_test_motion()](class_physicsserver3d.md#class-physicsserver3d-method-body-test-motion).

<a id="description"></a>

## Description

Describes the motion and collision result from [PhysicsServer3D.body_test_motion()](class_physicsserver3d.md#class-physicsserver3d-method-body-test-motion).

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Object](class_object.md#class-object) | [get_collider](class_physicstestmotionresult3d.md#class-physicstestmotionresult3d-method-get-collider)(collision_index: [int](class_int.md#class-int) = 0) const |
| [int](class_int.md#class-int) | [get_collider_id](class_physicstestmotionresult3d.md#class-physicstestmotionresult3d-method-get-collider-id)(collision_index: [int](class_int.md#class-int) = 0) const |
| [RID](class_rid.md#class-rid) | [get_collider_rid](class_physicstestmotionresult3d.md#class-physicstestmotionresult3d-method-get-collider-rid)(collision_index: [int](class_int.md#class-int) = 0) const |
| [int](class_int.md#class-int) | [get_collider_shape](class_physicstestmotionresult3d.md#class-physicstestmotionresult3d-method-get-collider-shape)(collision_index: [int](class_int.md#class-int) = 0) const |
| [Vector3](class_vector3.md#class-vector3) | [get_collider_velocity](class_physicstestmotionresult3d.md#class-physicstestmotionresult3d-method-get-collider-velocity)(collision_index: [int](class_int.md#class-int) = 0) const |
| [int](class_int.md#class-int) | [get_collision_count](class_physicstestmotionresult3d.md#class-physicstestmotionresult3d-method-get-collision-count)() const |
| [float](class_float.md#class-float) | [get_collision_depth](class_physicstestmotionresult3d.md#class-physicstestmotionresult3d-method-get-collision-depth)(collision_index: [int](class_int.md#class-int) = 0) const |
| [int](class_int.md#class-int) | [get_collision_local_shape](class_physicstestmotionresult3d.md#class-physicstestmotionresult3d-method-get-collision-local-shape)(collision_index: [int](class_int.md#class-int) = 0) const |
| [Vector3](class_vector3.md#class-vector3) | [get_collision_normal](class_physicstestmotionresult3d.md#class-physicstestmotionresult3d-method-get-collision-normal)(collision_index: [int](class_int.md#class-int) = 0) const |
| [Vector3](class_vector3.md#class-vector3) | [get_collision_point](class_physicstestmotionresult3d.md#class-physicstestmotionresult3d-method-get-collision-point)(collision_index: [int](class_int.md#class-int) = 0) const |
| [float](class_float.md#class-float) | [get_collision_safe_fraction](class_physicstestmotionresult3d.md#class-physicstestmotionresult3d-method-get-collision-safe-fraction)() const |
| [float](class_float.md#class-float) | [get_collision_unsafe_fraction](class_physicstestmotionresult3d.md#class-physicstestmotionresult3d-method-get-collision-unsafe-fraction)() const |
| [Vector3](class_vector3.md#class-vector3) | [get_remainder](class_physicstestmotionresult3d.md#class-physicstestmotionresult3d-method-get-remainder)() const |
| [Vector3](class_vector3.md#class-vector3) | [get_travel](class_physicstestmotionresult3d.md#class-physicstestmotionresult3d-method-get-travel)() const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-physicstestmotionresult3d-method-get-collider"></a>

[Object](class_object.md#class-object) **get_collider**(collision_index: [int](class_int.md#class-int) = 0) const [🔗](class_physicstestmotionresult3d.md#class-physicstestmotionresult3d-method-get-collider)

Returns the colliding body's attached [Object](class_object.md#class-object) given a collision index (the deepest collision by default), if a collision occurred.

---


<a id="class-physicstestmotionresult3d-method-get-collider-id"></a>

[int](class_int.md#class-int) **get_collider_id**(collision_index: [int](class_int.md#class-int) = 0) const [🔗](class_physicstestmotionresult3d.md#class-physicstestmotionresult3d-method-get-collider-id)

Returns the unique instance ID of the colliding body's attached [Object](class_object.md#class-object) given a collision index (the deepest collision by default), if a collision occurred. See [Object.get_instance_id()](class_object.md#class-object-method-get-instance-id).

---


<a id="class-physicstestmotionresult3d-method-get-collider-rid"></a>

[RID](class_rid.md#class-rid) **get_collider_rid**(collision_index: [int](class_int.md#class-int) = 0) const [🔗](class_physicstestmotionresult3d.md#class-physicstestmotionresult3d-method-get-collider-rid)

Returns the colliding body's [RID](class_rid.md#class-rid) used by the [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d) given a collision index (the deepest collision by default), if a collision occurred.

---


<a id="class-physicstestmotionresult3d-method-get-collider-shape"></a>

[int](class_int.md#class-int) **get_collider_shape**(collision_index: [int](class_int.md#class-int) = 0) const [🔗](class_physicstestmotionresult3d.md#class-physicstestmotionresult3d-method-get-collider-shape)

Returns the colliding body's shape index given a collision index (the deepest collision by default), if a collision occurred. See [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d).

---


<a id="class-physicstestmotionresult3d-method-get-collider-velocity"></a>

[Vector3](class_vector3.md#class-vector3) **get_collider_velocity**(collision_index: [int](class_int.md#class-int) = 0) const [🔗](class_physicstestmotionresult3d.md#class-physicstestmotionresult3d-method-get-collider-velocity)

Returns the colliding body's velocity given a collision index (the deepest collision by default), if a collision occurred.

---


<a id="class-physicstestmotionresult3d-method-get-collision-count"></a>

[int](class_int.md#class-int) **get_collision_count**() const [🔗](class_physicstestmotionresult3d.md#class-physicstestmotionresult3d-method-get-collision-count)

Returns the number of detected collisions.

---


<a id="class-physicstestmotionresult3d-method-get-collision-depth"></a>

[float](class_float.md#class-float) **get_collision_depth**(collision_index: [int](class_int.md#class-int) = 0) const [🔗](class_physicstestmotionresult3d.md#class-physicstestmotionresult3d-method-get-collision-depth)

Returns the length of overlap along the collision normal given a collision index (the deepest collision by default), if a collision occurred.

---


<a id="class-physicstestmotionresult3d-method-get-collision-local-shape"></a>

[int](class_int.md#class-int) **get_collision_local_shape**(collision_index: [int](class_int.md#class-int) = 0) const [🔗](class_physicstestmotionresult3d.md#class-physicstestmotionresult3d-method-get-collision-local-shape)

Returns the moving object's colliding shape given a collision index (the deepest collision by default), if a collision occurred.

---


<a id="class-physicstestmotionresult3d-method-get-collision-normal"></a>

[Vector3](class_vector3.md#class-vector3) **get_collision_normal**(collision_index: [int](class_int.md#class-int) = 0) const [🔗](class_physicstestmotionresult3d.md#class-physicstestmotionresult3d-method-get-collision-normal)

Returns the colliding body's shape's normal at the point of collision given a collision index (the deepest collision by default), if a collision occurred.

---


<a id="class-physicstestmotionresult3d-method-get-collision-point"></a>

[Vector3](class_vector3.md#class-vector3) **get_collision_point**(collision_index: [int](class_int.md#class-int) = 0) const [🔗](class_physicstestmotionresult3d.md#class-physicstestmotionresult3d-method-get-collision-point)

Returns the point of collision in global coordinates given a collision index (the deepest collision by default), if a collision occurred.

---


<a id="class-physicstestmotionresult3d-method-get-collision-safe-fraction"></a>

[float](class_float.md#class-float) **get_collision_safe_fraction**() const [🔗](class_physicstestmotionresult3d.md#class-physicstestmotionresult3d-method-get-collision-safe-fraction)

Returns the maximum fraction of the motion that can occur without a collision, between `0` and `1`.

---


<a id="class-physicstestmotionresult3d-method-get-collision-unsafe-fraction"></a>

[float](class_float.md#class-float) **get_collision_unsafe_fraction**() const [🔗](class_physicstestmotionresult3d.md#class-physicstestmotionresult3d-method-get-collision-unsafe-fraction)

Returns the minimum fraction of the motion needed to collide, if a collision occurred, between `0` and `1`.

---


<a id="class-physicstestmotionresult3d-method-get-remainder"></a>

[Vector3](class_vector3.md#class-vector3) **get_remainder**() const [🔗](class_physicstestmotionresult3d.md#class-physicstestmotionresult3d-method-get-remainder)

Returns the moving object's remaining movement vector.

---


<a id="class-physicstestmotionresult3d-method-get-travel"></a>

[Vector3](class_vector3.md#class-vector3) **get_travel**() const [🔗](class_physicstestmotionresult3d.md#class-physicstestmotionresult3d-method-get-travel)

Returns the moving object's travel before collision.
