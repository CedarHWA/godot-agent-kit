> Source: https://docs.godotengine.org/en/4.7/classes/class_kinematiccollision3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="kinematiccollision3d"></a>

<a id="class-kinematiccollision3d"></a>

# KinematicCollision3D

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Holds collision data from the movement of a [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d).

<a id="description"></a>

## Description

Holds collision data from the movement of a [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d), usually from [PhysicsBody3D.move_and_collide()](class_physicsbody3d.md#class-physicsbody3d-method-move-and-collide). When a [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d) is moved, it stops if it detects a collision with another body. If a collision is detected, a **KinematicCollision3D** object is returned.

The collision data includes the colliding object, the remaining motion, and the collision position. This data can be used to determine a custom response to the collision.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [float](class_float.md#class-float) | [get_angle](class_kinematiccollision3d.md#class-kinematiccollision3d-method-get-angle)(collision_index: [int](class_int.md#class-int) = 0, up_direction: [Vector3](class_vector3.md#class-vector3) = Vector3(0, 1, 0)) const |
| [Object](class_object.md#class-object) | [get_collider](class_kinematiccollision3d.md#class-kinematiccollision3d-method-get-collider)(collision_index: [int](class_int.md#class-int) = 0) const |
| [int](class_int.md#class-int) | [get_collider_id](class_kinematiccollision3d.md#class-kinematiccollision3d-method-get-collider-id)(collision_index: [int](class_int.md#class-int) = 0) const |
| [RID](class_rid.md#class-rid) | [get_collider_rid](class_kinematiccollision3d.md#class-kinematiccollision3d-method-get-collider-rid)(collision_index: [int](class_int.md#class-int) = 0) const |
| [Object](class_object.md#class-object) | [get_collider_shape](class_kinematiccollision3d.md#class-kinematiccollision3d-method-get-collider-shape)(collision_index: [int](class_int.md#class-int) = 0) const |
| [int](class_int.md#class-int) | [get_collider_shape_index](class_kinematiccollision3d.md#class-kinematiccollision3d-method-get-collider-shape-index)(collision_index: [int](class_int.md#class-int) = 0) const |
| [Vector3](class_vector3.md#class-vector3) | [get_collider_velocity](class_kinematiccollision3d.md#class-kinematiccollision3d-method-get-collider-velocity)(collision_index: [int](class_int.md#class-int) = 0) const |
| [int](class_int.md#class-int) | [get_collision_count](class_kinematiccollision3d.md#class-kinematiccollision3d-method-get-collision-count)() const |
| [float](class_float.md#class-float) | [get_depth](class_kinematiccollision3d.md#class-kinematiccollision3d-method-get-depth)() const |
| [Object](class_object.md#class-object) | [get_local_shape](class_kinematiccollision3d.md#class-kinematiccollision3d-method-get-local-shape)(collision_index: [int](class_int.md#class-int) = 0) const |
| [Vector3](class_vector3.md#class-vector3) | [get_normal](class_kinematiccollision3d.md#class-kinematiccollision3d-method-get-normal)(collision_index: [int](class_int.md#class-int) = 0) const |
| [Vector3](class_vector3.md#class-vector3) | [get_position](class_kinematiccollision3d.md#class-kinematiccollision3d-method-get-position)(collision_index: [int](class_int.md#class-int) = 0) const |
| [Vector3](class_vector3.md#class-vector3) | [get_remainder](class_kinematiccollision3d.md#class-kinematiccollision3d-method-get-remainder)() const |
| [Vector3](class_vector3.md#class-vector3) | [get_travel](class_kinematiccollision3d.md#class-kinematiccollision3d-method-get-travel)() const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-kinematiccollision3d-method-get-angle"></a>

[float](class_float.md#class-float) **get_angle**(collision_index: [int](class_int.md#class-int) = 0, up_direction: [Vector3](class_vector3.md#class-vector3) = Vector3(0, 1, 0)) const [🔗](class_kinematiccollision3d.md#class-kinematiccollision3d-method-get-angle)

Returns the collision angle according to `up_direction`, which is [Vector3.UP](class_vector3.md#class-vector3-constant-up) by default. This value is always positive.

---


<a id="class-kinematiccollision3d-method-get-collider"></a>

[Object](class_object.md#class-object) **get_collider**(collision_index: [int](class_int.md#class-int) = 0) const [🔗](class_kinematiccollision3d.md#class-kinematiccollision3d-method-get-collider)

Returns the colliding body's attached [Object](class_object.md#class-object) given a collision index (the deepest collision by default).

---


<a id="class-kinematiccollision3d-method-get-collider-id"></a>

[int](class_int.md#class-int) **get_collider_id**(collision_index: [int](class_int.md#class-int) = 0) const [🔗](class_kinematiccollision3d.md#class-kinematiccollision3d-method-get-collider-id)

Returns the unique instance ID of the colliding body's attached [Object](class_object.md#class-object) given a collision index (the deepest collision by default). See [Object.get_instance_id()](class_object.md#class-object-method-get-instance-id).

---


<a id="class-kinematiccollision3d-method-get-collider-rid"></a>

[RID](class_rid.md#class-rid) **get_collider_rid**(collision_index: [int](class_int.md#class-int) = 0) const [🔗](class_kinematiccollision3d.md#class-kinematiccollision3d-method-get-collider-rid)

Returns the colliding body's [RID](class_rid.md#class-rid) used by the [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d) given a collision index (the deepest collision by default).

---


<a id="class-kinematiccollision3d-method-get-collider-shape"></a>

[Object](class_object.md#class-object) **get_collider_shape**(collision_index: [int](class_int.md#class-int) = 0) const [🔗](class_kinematiccollision3d.md#class-kinematiccollision3d-method-get-collider-shape)

Returns the colliding body's shape given a collision index (the deepest collision by default).

---


<a id="class-kinematiccollision3d-method-get-collider-shape-index"></a>

[int](class_int.md#class-int) **get_collider_shape_index**(collision_index: [int](class_int.md#class-int) = 0) const [🔗](class_kinematiccollision3d.md#class-kinematiccollision3d-method-get-collider-shape-index)

Returns the colliding body's shape index given a collision index (the deepest collision by default). See [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d).

---


<a id="class-kinematiccollision3d-method-get-collider-velocity"></a>

[Vector3](class_vector3.md#class-vector3) **get_collider_velocity**(collision_index: [int](class_int.md#class-int) = 0) const [🔗](class_kinematiccollision3d.md#class-kinematiccollision3d-method-get-collider-velocity)

Returns the colliding body's velocity given a collision index (the deepest collision by default).

---


<a id="class-kinematiccollision3d-method-get-collision-count"></a>

[int](class_int.md#class-int) **get_collision_count**() const [🔗](class_kinematiccollision3d.md#class-kinematiccollision3d-method-get-collision-count)

Returns the number of detected collisions.

---


<a id="class-kinematiccollision3d-method-get-depth"></a>

[float](class_float.md#class-float) **get_depth**() const [🔗](class_kinematiccollision3d.md#class-kinematiccollision3d-method-get-depth)

Returns the colliding body's length of overlap along the collision normal.

---


<a id="class-kinematiccollision3d-method-get-local-shape"></a>

[Object](class_object.md#class-object) **get_local_shape**(collision_index: [int](class_int.md#class-int) = 0) const [🔗](class_kinematiccollision3d.md#class-kinematiccollision3d-method-get-local-shape)

Returns the moving object's colliding shape given a collision index (the deepest collision by default).

---


<a id="class-kinematiccollision3d-method-get-normal"></a>

[Vector3](class_vector3.md#class-vector3) **get_normal**(collision_index: [int](class_int.md#class-int) = 0) const [🔗](class_kinematiccollision3d.md#class-kinematiccollision3d-method-get-normal)

Returns the colliding body's shape's normal at the point of collision given a collision index (the deepest collision by default).

---


<a id="class-kinematiccollision3d-method-get-position"></a>

[Vector3](class_vector3.md#class-vector3) **get_position**(collision_index: [int](class_int.md#class-int) = 0) const [🔗](class_kinematiccollision3d.md#class-kinematiccollision3d-method-get-position)

Returns the point of collision in global coordinates given a collision index (the deepest collision by default).

---


<a id="class-kinematiccollision3d-method-get-remainder"></a>

[Vector3](class_vector3.md#class-vector3) **get_remainder**() const [🔗](class_kinematiccollision3d.md#class-kinematiccollision3d-method-get-remainder)

Returns the moving object's remaining movement vector.

---


<a id="class-kinematiccollision3d-method-get-travel"></a>

[Vector3](class_vector3.md#class-vector3) **get_travel**() const [🔗](class_kinematiccollision3d.md#class-kinematiccollision3d-method-get-travel)

Returns the moving object's travel before collision.
