> Source: https://docs.godotengine.org/en/4.7/classes/class_physicalbone3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="physicalbone3d"></a>

<a id="class-physicalbone3d"></a>

# PhysicalBone3D

**Inherits:** [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d) **<** [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A physics body used to make bones in a [Skeleton3D](class_skeleton3d.md#class-skeleton3d) react to physics.

<a id="description"></a>

## Description

The **PhysicalBone3D** node is a physics body that can be used to make bones in a [Skeleton3D](class_skeleton3d.md#class-skeleton3d) react to physics.

**Note:** In order to detect physical bones with raycasts, the [SkeletonModifier3D.active](class_skeletonmodifier3d.md#class-skeletonmodifier3d-property-active) property of the parent [PhysicalBoneSimulator3D](class_physicalbonesimulator3d.md#class-physicalbonesimulator3d) must be `true` and the [Skeleton3D](class_skeleton3d.md#class-skeleton3d)'s bone must be assigned to **PhysicalBone3D** correctly; it means that [get_bone_id()](class_physicalbone3d.md#class-physicalbone3d-method-get-bone-id) should return a valid id (`>= 0`).

<a id="tutorials"></a>

## Tutorials

- [Ragdoll System](../tutorials/physics/ragdoll_system.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [angular_damp](class_physicalbone3d.md#class-physicalbone3d-property-angular-damp) | `0.0` |
| [DampMode](class_physicalbone3d.md#enum-physicalbone3d-dampmode) | [angular_damp_mode](class_physicalbone3d.md#class-physicalbone3d-property-angular-damp-mode) | `0` |
| [Vector3](class_vector3.md#class-vector3) | [angular_velocity](class_physicalbone3d.md#class-physicalbone3d-property-angular-velocity) | `Vector3(0, 0, 0)` |
| [Transform3D](class_transform3d.md#class-transform3d) | [body_offset](class_physicalbone3d.md#class-physicalbone3d-property-body-offset) | `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)` |
| [float](class_float.md#class-float) | [bounce](class_physicalbone3d.md#class-physicalbone3d-property-bounce) | `0.0` |
| [bool](class_bool.md#class-bool) | [can_sleep](class_physicalbone3d.md#class-physicalbone3d-property-can-sleep) | `true` |
| [bool](class_bool.md#class-bool) | [custom_integrator](class_physicalbone3d.md#class-physicalbone3d-property-custom-integrator) | `false` |
| [float](class_float.md#class-float) | [friction](class_physicalbone3d.md#class-physicalbone3d-property-friction) | `1.0` |
| [float](class_float.md#class-float) | [gravity_scale](class_physicalbone3d.md#class-physicalbone3d-property-gravity-scale) | `1.0` |
| [Transform3D](class_transform3d.md#class-transform3d) | [joint_offset](class_physicalbone3d.md#class-physicalbone3d-property-joint-offset) | `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)` |
| [Vector3](class_vector3.md#class-vector3) | [joint_rotation](class_physicalbone3d.md#class-physicalbone3d-property-joint-rotation) | `Vector3(0, 0, 0)` |
| [JointType](class_physicalbone3d.md#enum-physicalbone3d-jointtype) | [joint_type](class_physicalbone3d.md#class-physicalbone3d-property-joint-type) | `0` |
| [float](class_float.md#class-float) | [linear_damp](class_physicalbone3d.md#class-physicalbone3d-property-linear-damp) | `0.0` |
| [DampMode](class_physicalbone3d.md#enum-physicalbone3d-dampmode) | [linear_damp_mode](class_physicalbone3d.md#class-physicalbone3d-property-linear-damp-mode) | `0` |
| [Vector3](class_vector3.md#class-vector3) | [linear_velocity](class_physicalbone3d.md#class-physicalbone3d-property-linear-velocity) | `Vector3(0, 0, 0)` |
| [float](class_float.md#class-float) | [mass](class_physicalbone3d.md#class-physicalbone3d-property-mass) | `1.0` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [_integrate_forces](class_physicalbone3d.md#class-physicalbone3d-private-method-integrate-forces)(state: [PhysicsDirectBodyState3D](class_physicsdirectbodystate3d.md#class-physicsdirectbodystate3d)) virtual |
| void | [apply_central_impulse](class_physicalbone3d.md#class-physicalbone3d-method-apply-central-impulse)(impulse: [Vector3](class_vector3.md#class-vector3)) |
| void | [apply_impulse](class_physicalbone3d.md#class-physicalbone3d-method-apply-impulse)(impulse: [Vector3](class_vector3.md#class-vector3), position: [Vector3](class_vector3.md#class-vector3) = Vector3(0, 0, 0)) |
| [int](class_int.md#class-int) | [get_bone_id](class_physicalbone3d.md#class-physicalbone3d-method-get-bone-id)() const |
| [bool](class_bool.md#class-bool) | [get_simulate_physics](class_physicalbone3d.md#class-physicalbone3d-method-get-simulate-physics)() |
| [bool](class_bool.md#class-bool) | [is_simulating_physics](class_physicalbone3d.md#class-physicalbone3d-method-is-simulating-physics)() |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-physicalbone3d-dampmode"></a>

enum **DampMode**: [🔗](class_physicalbone3d.md#enum-physicalbone3d-dampmode)

<a id="class-physicalbone3d-constant-damp-mode-combine"></a>

[DampMode](class_physicalbone3d.md#enum-physicalbone3d-dampmode) **DAMP_MODE_COMBINE** = `0`

In this mode, the body's damping value is added to any value set in areas or the default value.

<a id="class-physicalbone3d-constant-damp-mode-replace"></a>

[DampMode](class_physicalbone3d.md#enum-physicalbone3d-dampmode) **DAMP_MODE_REPLACE** = `1`

In this mode, the body's damping value replaces any value set in areas or the default value.

---


<a id="enum-physicalbone3d-jointtype"></a>

enum **JointType**: [🔗](class_physicalbone3d.md#enum-physicalbone3d-jointtype)

<a id="class-physicalbone3d-constant-joint-type-none"></a>

[JointType](class_physicalbone3d.md#enum-physicalbone3d-jointtype) **JOINT_TYPE_NONE** = `0`

No joint is applied to the PhysicsBone3D.

<a id="class-physicalbone3d-constant-joint-type-pin"></a>

[JointType](class_physicalbone3d.md#enum-physicalbone3d-jointtype) **JOINT_TYPE_PIN** = `1`

A pin joint is applied to the PhysicsBone3D.

<a id="class-physicalbone3d-constant-joint-type-cone"></a>

[JointType](class_physicalbone3d.md#enum-physicalbone3d-jointtype) **JOINT_TYPE_CONE** = `2`

A cone joint is applied to the PhysicsBone3D.

<a id="class-physicalbone3d-constant-joint-type-hinge"></a>

[JointType](class_physicalbone3d.md#enum-physicalbone3d-jointtype) **JOINT_TYPE_HINGE** = `3`

A hinge joint is applied to the PhysicsBone3D.

<a id="class-physicalbone3d-constant-joint-type-slider"></a>

[JointType](class_physicalbone3d.md#enum-physicalbone3d-jointtype) **JOINT_TYPE_SLIDER** = `4`

A slider joint is applied to the PhysicsBone3D.

<a id="class-physicalbone3d-constant-joint-type-6dof"></a>

[JointType](class_physicalbone3d.md#enum-physicalbone3d-jointtype) **JOINT_TYPE_6DOF** = `5`

A 6 degrees of freedom joint is applied to the PhysicsBone3D.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-physicalbone3d-property-angular-damp"></a>

[float](class_float.md#class-float) **angular_damp** = `0.0` [🔗](class_physicalbone3d.md#class-physicalbone3d-property-angular-damp)

- void **set_angular_damp**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_angular_damp**()

Damps the body's rotation. By default, the body will use the [ProjectSettings.physics/3d/default_angular_damp](class_projectsettings.md#class-projectsettings-property-physics-3d-default-angular-damp) project setting or any value override set by an [Area3D](class_area3d.md#class-area3d) the body is in. Depending on [angular_damp_mode](class_physicalbone3d.md#class-physicalbone3d-property-angular-damp-mode), you can set [angular_damp](class_physicalbone3d.md#class-physicalbone3d-property-angular-damp) to be added to or to replace the body's damping value.

See [ProjectSettings.physics/3d/default_angular_damp](class_projectsettings.md#class-projectsettings-property-physics-3d-default-angular-damp) for more details about damping.

---


<a id="class-physicalbone3d-property-angular-damp-mode"></a>

[DampMode](class_physicalbone3d.md#enum-physicalbone3d-dampmode) **angular_damp_mode** = `0` [🔗](class_physicalbone3d.md#class-physicalbone3d-property-angular-damp-mode)

- void **set_angular_damp_mode**(value: [DampMode](class_physicalbone3d.md#enum-physicalbone3d-dampmode))
- [DampMode](class_physicalbone3d.md#enum-physicalbone3d-dampmode) **get_angular_damp_mode**()

Defines how [angular_damp](class_physicalbone3d.md#class-physicalbone3d-property-angular-damp) is applied.

---


<a id="class-physicalbone3d-property-angular-velocity"></a>

[Vector3](class_vector3.md#class-vector3) **angular_velocity** = `Vector3(0, 0, 0)` [🔗](class_physicalbone3d.md#class-physicalbone3d-property-angular-velocity)

- void **set_angular_velocity**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_angular_velocity**()

The PhysicalBone3D's rotational velocity in *radians* per second.

---


<a id="class-physicalbone3d-property-body-offset"></a>

[Transform3D](class_transform3d.md#class-transform3d) **body_offset** = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)` [🔗](class_physicalbone3d.md#class-physicalbone3d-property-body-offset)

- void **set_body_offset**(value: [Transform3D](class_transform3d.md#class-transform3d))
- [Transform3D](class_transform3d.md#class-transform3d) **get_body_offset**()

Sets the body's transform.

---


<a id="class-physicalbone3d-property-bounce"></a>

[float](class_float.md#class-float) **bounce** = `0.0` [🔗](class_physicalbone3d.md#class-physicalbone3d-property-bounce)

- void **set_bounce**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_bounce**()

The body's bounciness. Values range from `0` (no bounce) to `1` (full bounciness).

**Note:** Even with [bounce](class_physicalbone3d.md#class-physicalbone3d-property-bounce) set to `1.0`, some energy will be lost over time due to linear and angular damping. To have a **PhysicalBone3D** that preserves all its energy over time, set [bounce](class_physicalbone3d.md#class-physicalbone3d-property-bounce) to `1.0`, [linear_damp_mode](class_physicalbone3d.md#class-physicalbone3d-property-linear-damp-mode) to [DAMP_MODE_REPLACE](class_physicalbone3d.md#class-physicalbone3d-constant-damp-mode-replace), [linear_damp](class_physicalbone3d.md#class-physicalbone3d-property-linear-damp) to `0.0`, [angular_damp_mode](class_physicalbone3d.md#class-physicalbone3d-property-angular-damp-mode) to [DAMP_MODE_REPLACE](class_physicalbone3d.md#class-physicalbone3d-constant-damp-mode-replace), and [angular_damp](class_physicalbone3d.md#class-physicalbone3d-property-angular-damp) to `0.0`.

---


<a id="class-physicalbone3d-property-can-sleep"></a>

[bool](class_bool.md#class-bool) **can_sleep** = `true` [🔗](class_physicalbone3d.md#class-physicalbone3d-property-can-sleep)

- void **set_can_sleep**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_able_to_sleep**()

If `true`, the body is deactivated when there is no movement, so it will not take part in the simulation until it is awakened by an external force.

---


<a id="class-physicalbone3d-property-custom-integrator"></a>

[bool](class_bool.md#class-bool) **custom_integrator** = `false` [🔗](class_physicalbone3d.md#class-physicalbone3d-property-custom-integrator)

- void **set_use_custom_integrator**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_using_custom_integrator**()

If `true`, the standard force integration (like gravity or damping) will be disabled for this body. Other than collision response, the body will only move as determined by the [_integrate_forces()](class_physicalbone3d.md#class-physicalbone3d-private-method-integrate-forces) method, if that virtual method is overridden.

Setting this property will call the method [PhysicsServer3D.body_set_omit_force_integration()](class_physicsserver3d.md#class-physicsserver3d-method-body-set-omit-force-integration) internally.

---


<a id="class-physicalbone3d-property-friction"></a>

[float](class_float.md#class-float) **friction** = `1.0` [🔗](class_physicalbone3d.md#class-physicalbone3d-property-friction)

- void **set_friction**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_friction**()

The body's friction, from `0` (frictionless) to `1` (max friction).

---


<a id="class-physicalbone3d-property-gravity-scale"></a>

[float](class_float.md#class-float) **gravity_scale** = `1.0` [🔗](class_physicalbone3d.md#class-physicalbone3d-property-gravity-scale)

- void **set_gravity_scale**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_gravity_scale**()

This is multiplied by [ProjectSettings.physics/3d/default_gravity](class_projectsettings.md#class-projectsettings-property-physics-3d-default-gravity) to produce this body's gravity. For example, a value of `1.0` will apply normal gravity, `2.0` will apply double the gravity, and `0.5` will apply half the gravity to this body.

---


<a id="class-physicalbone3d-property-joint-offset"></a>

[Transform3D](class_transform3d.md#class-transform3d) **joint_offset** = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)` [🔗](class_physicalbone3d.md#class-physicalbone3d-property-joint-offset)

- void **set_joint_offset**(value: [Transform3D](class_transform3d.md#class-transform3d))
- [Transform3D](class_transform3d.md#class-transform3d) **get_joint_offset**()

Sets the joint's transform.

---


<a id="class-physicalbone3d-property-joint-rotation"></a>

[Vector3](class_vector3.md#class-vector3) **joint_rotation** = `Vector3(0, 0, 0)` [🔗](class_physicalbone3d.md#class-physicalbone3d-property-joint-rotation)

- void **set_joint_rotation**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_joint_rotation**()

Sets the joint's rotation in radians.

---


<a id="class-physicalbone3d-property-joint-type"></a>

[JointType](class_physicalbone3d.md#enum-physicalbone3d-jointtype) **joint_type** = `0` [🔗](class_physicalbone3d.md#class-physicalbone3d-property-joint-type)

- void **set_joint_type**(value: [JointType](class_physicalbone3d.md#enum-physicalbone3d-jointtype))
- [JointType](class_physicalbone3d.md#enum-physicalbone3d-jointtype) **get_joint_type**()

Sets the joint type.

---


<a id="class-physicalbone3d-property-linear-damp"></a>

[float](class_float.md#class-float) **linear_damp** = `0.0` [🔗](class_physicalbone3d.md#class-physicalbone3d-property-linear-damp)

- void **set_linear_damp**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_linear_damp**()

Damps the body's movement. By default, the body will use [ProjectSettings.physics/3d/default_linear_damp](class_projectsettings.md#class-projectsettings-property-physics-3d-default-linear-damp) or any value override set by an [Area3D](class_area3d.md#class-area3d) the body is in. Depending on [linear_damp_mode](class_physicalbone3d.md#class-physicalbone3d-property-linear-damp-mode), [linear_damp](class_physicalbone3d.md#class-physicalbone3d-property-linear-damp) may be added to or replace the body's damping value.

See [ProjectSettings.physics/3d/default_linear_damp](class_projectsettings.md#class-projectsettings-property-physics-3d-default-linear-damp) for more details about damping.

---


<a id="class-physicalbone3d-property-linear-damp-mode"></a>

[DampMode](class_physicalbone3d.md#enum-physicalbone3d-dampmode) **linear_damp_mode** = `0` [🔗](class_physicalbone3d.md#class-physicalbone3d-property-linear-damp-mode)

- void **set_linear_damp_mode**(value: [DampMode](class_physicalbone3d.md#enum-physicalbone3d-dampmode))
- [DampMode](class_physicalbone3d.md#enum-physicalbone3d-dampmode) **get_linear_damp_mode**()

Defines how [linear_damp](class_physicalbone3d.md#class-physicalbone3d-property-linear-damp) is applied.

---


<a id="class-physicalbone3d-property-linear-velocity"></a>

[Vector3](class_vector3.md#class-vector3) **linear_velocity** = `Vector3(0, 0, 0)` [🔗](class_physicalbone3d.md#class-physicalbone3d-property-linear-velocity)

- void **set_linear_velocity**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_linear_velocity**()

The body's linear velocity in units per second. Can be used sporadically, but **don't set this every frame**, because physics may run in another thread and runs at a different granularity. Use [_integrate_forces()](class_physicalbone3d.md#class-physicalbone3d-private-method-integrate-forces) as your process loop for precise control of the body state.

---


<a id="class-physicalbone3d-property-mass"></a>

[float](class_float.md#class-float) **mass** = `1.0` [🔗](class_physicalbone3d.md#class-physicalbone3d-property-mass)

- void **set_mass**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_mass**()

The body's mass.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-physicalbone3d-private-method-integrate-forces"></a>

void **_integrate_forces**(state: [PhysicsDirectBodyState3D](class_physicsdirectbodystate3d.md#class-physicsdirectbodystate3d)) virtual [🔗](class_physicalbone3d.md#class-physicalbone3d-private-method-integrate-forces)

Called during physics processing, allowing you to read and safely modify the simulation state for the object. By default, it is called before the standard force integration, but the [custom_integrator](class_physicalbone3d.md#class-physicalbone3d-property-custom-integrator) property allows you to disable the standard force integration and do fully custom force integration for a body.

---


<a id="class-physicalbone3d-method-apply-central-impulse"></a>

void **apply_central_impulse**(impulse: [Vector3](class_vector3.md#class-vector3)) [🔗](class_physicalbone3d.md#class-physicalbone3d-method-apply-central-impulse)

Applies a directional impulse without affecting rotation.

An impulse is time-independent! Applying an impulse every frame would result in a framerate-dependent force. For this reason, it should only be used when simulating one-time impacts (use the "_integrate_forces" functions otherwise).

This is equivalent to using [apply_impulse()](class_physicalbone3d.md#class-physicalbone3d-method-apply-impulse) at the body's center of mass.

---


<a id="class-physicalbone3d-method-apply-impulse"></a>

void **apply_impulse**(impulse: [Vector3](class_vector3.md#class-vector3), position: [Vector3](class_vector3.md#class-vector3) = Vector3(0, 0, 0)) [🔗](class_physicalbone3d.md#class-physicalbone3d-method-apply-impulse)

Applies a positioned impulse to the PhysicsBone3D.

An impulse is time-independent! Applying an impulse every frame would result in a framerate-dependent force. For this reason, it should only be used when simulating one-time impacts (use the "_integrate_forces" functions otherwise).

`position` is the offset from the PhysicsBone3D origin in global coordinates.

---


<a id="class-physicalbone3d-method-get-bone-id"></a>

[int](class_int.md#class-int) **get_bone_id**() const [🔗](class_physicalbone3d.md#class-physicalbone3d-method-get-bone-id)

Returns the unique identifier of the PhysicsBone3D.

---


<a id="class-physicalbone3d-method-get-simulate-physics"></a>

[bool](class_bool.md#class-bool) **get_simulate_physics**() [🔗](class_physicalbone3d.md#class-physicalbone3d-method-get-simulate-physics)

Returns `true` if the PhysicsBone3D is allowed to simulate physics.

---


<a id="class-physicalbone3d-method-is-simulating-physics"></a>

[bool](class_bool.md#class-bool) **is_simulating_physics**() [🔗](class_physicalbone3d.md#class-physicalbone3d-method-is-simulating-physics)

Returns `true` if the PhysicsBone3D is currently simulating physics.
