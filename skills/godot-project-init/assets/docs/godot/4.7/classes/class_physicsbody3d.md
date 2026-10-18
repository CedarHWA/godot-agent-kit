> Source: https://docs.godotengine.org/en/4.7/classes/class_physicsbody3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="physicsbody3d"></a>

<a id="class-physicsbody3d"></a>

# PhysicsBody3D

**Inherits:** [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [CharacterBody3D](class_characterbody3d.md#class-characterbody3d), [PhysicalBone3D](class_physicalbone3d.md#class-physicalbone3d), [RigidBody3D](class_rigidbody3d.md#class-rigidbody3d), [StaticBody3D](class_staticbody3d.md#class-staticbody3d)

Abstract base class for 3D game objects affected by physics.

<a id="description"></a>

## Description

**PhysicsBody3D** is an abstract base class for 3D game objects affected by physics. All 3D physics bodies inherit from it.

**Warning:** With a non-uniform scale, this node will likely not behave as expected. It is advised to keep its scale the same on all axes and adjust its collision shape(s) instead.

<a id="tutorials"></a>

## Tutorials

- [Physics introduction](../tutorials/physics/physics_introduction.md)
- [Troubleshooting physics issues](../tutorials/physics/troubleshooting_physics_issues.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [axis_lock_angular_x](class_physicsbody3d.md#class-physicsbody3d-property-axis-lock-angular-x) | `false` |
| [bool](class_bool.md#class-bool) | [axis_lock_angular_y](class_physicsbody3d.md#class-physicsbody3d-property-axis-lock-angular-y) | `false` |
| [bool](class_bool.md#class-bool) | [axis_lock_angular_z](class_physicsbody3d.md#class-physicsbody3d-property-axis-lock-angular-z) | `false` |
| [bool](class_bool.md#class-bool) | [axis_lock_linear_x](class_physicsbody3d.md#class-physicsbody3d-property-axis-lock-linear-x) | `false` |
| [bool](class_bool.md#class-bool) | [axis_lock_linear_y](class_physicsbody3d.md#class-physicsbody3d-property-axis-lock-linear-y) | `false` |
| [bool](class_bool.md#class-bool) | [axis_lock_linear_z](class_physicsbody3d.md#class-physicsbody3d-property-axis-lock-linear-z) | `false` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_collision_exception_with](class_physicsbody3d.md#class-physicsbody3d-method-add-collision-exception-with)(body: [Node](class_node.md#class-node)) |
| [bool](class_bool.md#class-bool) | [get_axis_lock](class_physicsbody3d.md#class-physicsbody3d-method-get-axis-lock)(axis: [BodyAxis](class_physicsserver3d.md#enum-physicsserver3d-bodyaxis)) const |
| [Array](class_array.md#class-array)[[PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d)] | [get_collision_exceptions](class_physicsbody3d.md#class-physicsbody3d-method-get-collision-exceptions)() |
| [Vector3](class_vector3.md#class-vector3) | [get_gravity](class_physicsbody3d.md#class-physicsbody3d-method-get-gravity)() const |
| [KinematicCollision3D](class_kinematiccollision3d.md#class-kinematiccollision3d) | [move_and_collide](class_physicsbody3d.md#class-physicsbody3d-method-move-and-collide)(motion: [Vector3](class_vector3.md#class-vector3), test_only: [bool](class_bool.md#class-bool) = false, safe_margin: [float](class_float.md#class-float) = 0.001, recovery_as_collision: [bool](class_bool.md#class-bool) = false, max_collisions: [int](class_int.md#class-int) = 1) |
| void | [remove_collision_exception_with](class_physicsbody3d.md#class-physicsbody3d-method-remove-collision-exception-with)(body: [Node](class_node.md#class-node)) |
| void | [set_axis_lock](class_physicsbody3d.md#class-physicsbody3d-method-set-axis-lock)(axis: [BodyAxis](class_physicsserver3d.md#enum-physicsserver3d-bodyaxis), lock: [bool](class_bool.md#class-bool)) |
| [bool](class_bool.md#class-bool) | [test_move](class_physicsbody3d.md#class-physicsbody3d-method-test-move)(from: [Transform3D](class_transform3d.md#class-transform3d), motion: [Vector3](class_vector3.md#class-vector3), collision: [KinematicCollision3D](class_kinematiccollision3d.md#class-kinematiccollision3d) = null, safe_margin: [float](class_float.md#class-float) = 0.001, recovery_as_collision: [bool](class_bool.md#class-bool) = false, max_collisions: [int](class_int.md#class-int) = 1) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-physicsbody3d-property-axis-lock-angular-x"></a>

[bool](class_bool.md#class-bool) **axis_lock_angular_x** = `false` [🔗](class_physicsbody3d.md#class-physicsbody3d-property-axis-lock-angular-x)

- void **set_axis_lock**(axis: [BodyAxis](class_physicsserver3d.md#enum-physicsserver3d-bodyaxis), lock: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_axis_lock**(axis: [BodyAxis](class_physicsserver3d.md#enum-physicsserver3d-bodyaxis)) const

Lock the body's rotation in the X axis.

---


<a id="class-physicsbody3d-property-axis-lock-angular-y"></a>

[bool](class_bool.md#class-bool) **axis_lock_angular_y** = `false` [🔗](class_physicsbody3d.md#class-physicsbody3d-property-axis-lock-angular-y)

- void **set_axis_lock**(axis: [BodyAxis](class_physicsserver3d.md#enum-physicsserver3d-bodyaxis), lock: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_axis_lock**(axis: [BodyAxis](class_physicsserver3d.md#enum-physicsserver3d-bodyaxis)) const

Lock the body's rotation in the Y axis.

---


<a id="class-physicsbody3d-property-axis-lock-angular-z"></a>

[bool](class_bool.md#class-bool) **axis_lock_angular_z** = `false` [🔗](class_physicsbody3d.md#class-physicsbody3d-property-axis-lock-angular-z)

- void **set_axis_lock**(axis: [BodyAxis](class_physicsserver3d.md#enum-physicsserver3d-bodyaxis), lock: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_axis_lock**(axis: [BodyAxis](class_physicsserver3d.md#enum-physicsserver3d-bodyaxis)) const

Lock the body's rotation in the Z axis.

---


<a id="class-physicsbody3d-property-axis-lock-linear-x"></a>

[bool](class_bool.md#class-bool) **axis_lock_linear_x** = `false` [🔗](class_physicsbody3d.md#class-physicsbody3d-property-axis-lock-linear-x)

- void **set_axis_lock**(axis: [BodyAxis](class_physicsserver3d.md#enum-physicsserver3d-bodyaxis), lock: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_axis_lock**(axis: [BodyAxis](class_physicsserver3d.md#enum-physicsserver3d-bodyaxis)) const

Lock the body's linear movement in the X axis.

---


<a id="class-physicsbody3d-property-axis-lock-linear-y"></a>

[bool](class_bool.md#class-bool) **axis_lock_linear_y** = `false` [🔗](class_physicsbody3d.md#class-physicsbody3d-property-axis-lock-linear-y)

- void **set_axis_lock**(axis: [BodyAxis](class_physicsserver3d.md#enum-physicsserver3d-bodyaxis), lock: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_axis_lock**(axis: [BodyAxis](class_physicsserver3d.md#enum-physicsserver3d-bodyaxis)) const

Lock the body's linear movement in the Y axis.

---


<a id="class-physicsbody3d-property-axis-lock-linear-z"></a>

[bool](class_bool.md#class-bool) **axis_lock_linear_z** = `false` [🔗](class_physicsbody3d.md#class-physicsbody3d-property-axis-lock-linear-z)

- void **set_axis_lock**(axis: [BodyAxis](class_physicsserver3d.md#enum-physicsserver3d-bodyaxis), lock: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_axis_lock**(axis: [BodyAxis](class_physicsserver3d.md#enum-physicsserver3d-bodyaxis)) const

Lock the body's linear movement in the Z axis.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-physicsbody3d-method-add-collision-exception-with"></a>

void **add_collision_exception_with**(body: [Node](class_node.md#class-node)) [🔗](class_physicsbody3d.md#class-physicsbody3d-method-add-collision-exception-with)

Adds a body to the list of bodies that this body can't collide with.

---


<a id="class-physicsbody3d-method-get-axis-lock"></a>

[bool](class_bool.md#class-bool) **get_axis_lock**(axis: [BodyAxis](class_physicsserver3d.md#enum-physicsserver3d-bodyaxis)) const [🔗](class_physicsbody3d.md#class-physicsbody3d-method-get-axis-lock)

Returns `true` if the specified linear or rotational `axis` is locked.

---


<a id="class-physicsbody3d-method-get-collision-exceptions"></a>

[Array](class_array.md#class-array)[[PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d)] **get_collision_exceptions**() [🔗](class_physicsbody3d.md#class-physicsbody3d-method-get-collision-exceptions)

Returns an array of nodes that were added as collision exceptions for this body.

---


<a id="class-physicsbody3d-method-get-gravity"></a>

[Vector3](class_vector3.md#class-vector3) **get_gravity**() const [🔗](class_physicsbody3d.md#class-physicsbody3d-method-get-gravity)

Returns the gravity vector computed from all sources that can affect the body, including all gravity overrides from [Area3D](class_area3d.md#class-area3d) nodes and the global world gravity.

---


<a id="class-physicsbody3d-method-move-and-collide"></a>

[KinematicCollision3D](class_kinematiccollision3d.md#class-kinematiccollision3d) **move_and_collide**(motion: [Vector3](class_vector3.md#class-vector3), test_only: [bool](class_bool.md#class-bool) = false, safe_margin: [float](class_float.md#class-float) = 0.001, recovery_as_collision: [bool](class_bool.md#class-bool) = false, max_collisions: [int](class_int.md#class-int) = 1) [🔗](class_physicsbody3d.md#class-physicsbody3d-method-move-and-collide)

Moves the body along the vector `motion`. In order to be frame rate independent in [Node._physics_process()](class_node.md#class-node-private-method-physics-process) or [Node._process()](class_node.md#class-node-private-method-process), `motion` should be computed using `delta`.

The body will stop if it collides. Returns a [KinematicCollision3D](class_kinematiccollision3d.md#class-kinematiccollision3d), which contains information about the collision when stopped, or when touching another body along the motion.

If `test_only` is `true`, the body does not move but the would-be collision information is given.

`safe_margin` is the extra margin used for collision recovery (see [CharacterBody3D.safe_margin](class_characterbody3d.md#class-characterbody3d-property-safe-margin) for more details).

If `recovery_as_collision` is `true`, any depenetration from the recovery phase is also reported as a collision; this is used e.g. by [CharacterBody3D](class_characterbody3d.md#class-characterbody3d) for improving floor detection during floor snapping.

`max_collisions` allows to retrieve more than one collision result.

---


<a id="class-physicsbody3d-method-remove-collision-exception-with"></a>

void **remove_collision_exception_with**(body: [Node](class_node.md#class-node)) [🔗](class_physicsbody3d.md#class-physicsbody3d-method-remove-collision-exception-with)

Removes a body from the list of bodies that this body can't collide with.

---


<a id="class-physicsbody3d-method-set-axis-lock"></a>

void **set_axis_lock**(axis: [BodyAxis](class_physicsserver3d.md#enum-physicsserver3d-bodyaxis), lock: [bool](class_bool.md#class-bool)) [🔗](class_physicsbody3d.md#class-physicsbody3d-method-set-axis-lock)

Locks or unlocks the specified linear or rotational `axis` depending on the value of `lock`.

---


<a id="class-physicsbody3d-method-test-move"></a>

[bool](class_bool.md#class-bool) **test_move**(from: [Transform3D](class_transform3d.md#class-transform3d), motion: [Vector3](class_vector3.md#class-vector3), collision: [KinematicCollision3D](class_kinematiccollision3d.md#class-kinematiccollision3d) = null, safe_margin: [float](class_float.md#class-float) = 0.001, recovery_as_collision: [bool](class_bool.md#class-bool) = false, max_collisions: [int](class_int.md#class-int) = 1) [🔗](class_physicsbody3d.md#class-physicsbody3d-method-test-move)

Checks for collisions without moving the body. In order to be frame rate independent in [Node._physics_process()](class_node.md#class-node-private-method-physics-process) or [Node._process()](class_node.md#class-node-private-method-process), `motion` should be computed using `delta`.

Virtually sets the node's position, scale and rotation to that of the given [Transform3D](class_transform3d.md#class-transform3d), then tries to move the body along the vector `motion`. Returns `true` if a collision would stop the body from moving along the whole path.

`collision` is an optional object of type [KinematicCollision3D](class_kinematiccollision3d.md#class-kinematiccollision3d), which contains additional information about the collision when stopped, or when touching another body along the motion.

`safe_margin` is the extra margin used for collision recovery (see [CharacterBody3D.safe_margin](class_characterbody3d.md#class-characterbody3d-property-safe-margin) for more details).

If `recovery_as_collision` is `true`, any depenetration from the recovery phase is also reported as a collision; this is useful for checking whether the body would *touch* any other bodies.

`max_collisions` allows to retrieve more than one collision result.
