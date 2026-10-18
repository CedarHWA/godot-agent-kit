> Source: https://docs.godotengine.org/en/4.7/classes/class_physicsbody2d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="physicsbody2d"></a>

<a id="class-physicsbody2d"></a>

# PhysicsBody2D

**Inherits:** [CollisionObject2D](class_collisionobject2d.md#class-collisionobject2d) **<** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [CharacterBody2D](class_characterbody2d.md#class-characterbody2d), [RigidBody2D](class_rigidbody2d.md#class-rigidbody2d), [StaticBody2D](class_staticbody2d.md#class-staticbody2d)

Abstract base class for 2D game objects affected by physics.

<a id="description"></a>

## Description

**PhysicsBody2D** is an abstract base class for 2D game objects affected by physics. All 2D physics bodies inherit from it.

<a id="tutorials"></a>

## Tutorials

- [Physics introduction](../tutorials/physics/physics_introduction.md)
- [Troubleshooting physics issues](../tutorials/physics/troubleshooting_physics_issues.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | input_pickable | `false` (overrides [CollisionObject2D](class_collisionobject2d.md#class-collisionobject2d-property-input-pickable)) |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_collision_exception_with](class_physicsbody2d.md#class-physicsbody2d-method-add-collision-exception-with)(body: [Node](class_node.md#class-node)) |
| [Array](class_array.md#class-array)[[PhysicsBody2D](class_physicsbody2d.md#class-physicsbody2d)] | [get_collision_exceptions](class_physicsbody2d.md#class-physicsbody2d-method-get-collision-exceptions)() |
| [Vector2](class_vector2.md#class-vector2) | [get_gravity](class_physicsbody2d.md#class-physicsbody2d-method-get-gravity)() const |
| [KinematicCollision2D](class_kinematiccollision2d.md#class-kinematiccollision2d) | [move_and_collide](class_physicsbody2d.md#class-physicsbody2d-method-move-and-collide)(motion: [Vector2](class_vector2.md#class-vector2), test_only: [bool](class_bool.md#class-bool) = false, safe_margin: [float](class_float.md#class-float) = 0.08, recovery_as_collision: [bool](class_bool.md#class-bool) = false) |
| void | [remove_collision_exception_with](class_physicsbody2d.md#class-physicsbody2d-method-remove-collision-exception-with)(body: [Node](class_node.md#class-node)) |
| [bool](class_bool.md#class-bool) | [test_move](class_physicsbody2d.md#class-physicsbody2d-method-test-move)(from: [Transform2D](class_transform2d.md#class-transform2d), motion: [Vector2](class_vector2.md#class-vector2), collision: [KinematicCollision2D](class_kinematiccollision2d.md#class-kinematiccollision2d) = null, safe_margin: [float](class_float.md#class-float) = 0.08, recovery_as_collision: [bool](class_bool.md#class-bool) = false) |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-physicsbody2d-method-add-collision-exception-with"></a>

void **add_collision_exception_with**(body: [Node](class_node.md#class-node)) [🔗](class_physicsbody2d.md#class-physicsbody2d-method-add-collision-exception-with)

Adds a body to the list of bodies that this body can't collide with.

---


<a id="class-physicsbody2d-method-get-collision-exceptions"></a>

[Array](class_array.md#class-array)[[PhysicsBody2D](class_physicsbody2d.md#class-physicsbody2d)] **get_collision_exceptions**() [🔗](class_physicsbody2d.md#class-physicsbody2d-method-get-collision-exceptions)

Returns an array of nodes that were added as collision exceptions for this body.

---


<a id="class-physicsbody2d-method-get-gravity"></a>

[Vector2](class_vector2.md#class-vector2) **get_gravity**() const [🔗](class_physicsbody2d.md#class-physicsbody2d-method-get-gravity)

Returns the gravity vector computed from all sources that can affect the body, including all gravity overrides from [Area2D](class_area2d.md#class-area2d) nodes and the global world gravity.

---


<a id="class-physicsbody2d-method-move-and-collide"></a>

[KinematicCollision2D](class_kinematiccollision2d.md#class-kinematiccollision2d) **move_and_collide**(motion: [Vector2](class_vector2.md#class-vector2), test_only: [bool](class_bool.md#class-bool) = false, safe_margin: [float](class_float.md#class-float) = 0.08, recovery_as_collision: [bool](class_bool.md#class-bool) = false) [🔗](class_physicsbody2d.md#class-physicsbody2d-method-move-and-collide)

Moves the body along the vector `motion`. In order to be frame rate independent in [Node._physics_process()](class_node.md#class-node-private-method-physics-process) or [Node._process()](class_node.md#class-node-private-method-process), `motion` should be computed using `delta`.

Returns a [KinematicCollision2D](class_kinematiccollision2d.md#class-kinematiccollision2d), which contains information about the collision when stopped, or when touching another body along the motion.

If `test_only` is `true`, the body does not move but the would-be collision information is given.

`safe_margin` is the extra margin used for collision recovery (see [CharacterBody2D.safe_margin](class_characterbody2d.md#class-characterbody2d-property-safe-margin) for more details).

If `recovery_as_collision` is `true`, any depenetration from the recovery phase is also reported as a collision; this is used e.g. by [CharacterBody2D](class_characterbody2d.md#class-characterbody2d) for improving floor detection during floor snapping.

---


<a id="class-physicsbody2d-method-remove-collision-exception-with"></a>

void **remove_collision_exception_with**(body: [Node](class_node.md#class-node)) [🔗](class_physicsbody2d.md#class-physicsbody2d-method-remove-collision-exception-with)

Removes a body from the list of bodies that this body can't collide with.

---


<a id="class-physicsbody2d-method-test-move"></a>

[bool](class_bool.md#class-bool) **test_move**(from: [Transform2D](class_transform2d.md#class-transform2d), motion: [Vector2](class_vector2.md#class-vector2), collision: [KinematicCollision2D](class_kinematiccollision2d.md#class-kinematiccollision2d) = null, safe_margin: [float](class_float.md#class-float) = 0.08, recovery_as_collision: [bool](class_bool.md#class-bool) = false) [🔗](class_physicsbody2d.md#class-physicsbody2d-method-test-move)

Checks for collisions without moving the body. In order to be frame rate independent in [Node._physics_process()](class_node.md#class-node-private-method-physics-process) or [Node._process()](class_node.md#class-node-private-method-process), `motion` should be computed using `delta`.

Virtually sets the node's position, scale and rotation to that of the given [Transform2D](class_transform2d.md#class-transform2d), then tries to move the body along the vector `motion`. Returns `true` if a collision would stop the body from moving along the whole path.

`collision` is an optional object of type [KinematicCollision2D](class_kinematiccollision2d.md#class-kinematiccollision2d), which contains additional information about the collision when stopped, or when touching another body along the motion.

`safe_margin` is the extra margin used for collision recovery (see [CharacterBody2D.safe_margin](class_characterbody2d.md#class-characterbody2d-property-safe-margin) for more details).

If `recovery_as_collision` is `true`, any depenetration from the recovery phase is also reported as a collision; this is useful for checking whether the body would *touch* any other bodies.
