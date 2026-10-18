> Source: https://docs.godotengine.org/en/4.7/classes/class_physicsdirectbodystate2dextension.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="physicsdirectbodystate2dextension"></a>

<a id="class-physicsdirectbodystate2dextension"></a>

# PhysicsDirectBodyState2DExtension

**Inherits:** [PhysicsDirectBodyState2D](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d) **<** [Object](class_object.md#class-object)

Provides virtual methods that can be overridden to create custom [PhysicsDirectBodyState2D](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d) implementations.

<a id="description"></a>

## Description

This class extends [PhysicsDirectBodyState2D](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d) by providing additional virtual methods that can be overridden. When these methods are overridden, they will be called instead of the internal methods of the physics server.

Intended for use with GDExtension to create custom implementations of [PhysicsDirectBodyState2D](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d).

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [_add_constant_central_force](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-add-constant-central-force)(force: [Vector2](class_vector2.md#class-vector2)) virtual required |
| void | [_add_constant_force](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-add-constant-force)(force: [Vector2](class_vector2.md#class-vector2), position: [Vector2](class_vector2.md#class-vector2)) virtual required |
| void | [_add_constant_torque](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-add-constant-torque)(torque: [float](class_float.md#class-float)) virtual required |
| void | [_apply_central_force](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-apply-central-force)(force: [Vector2](class_vector2.md#class-vector2)) virtual required |
| void | [_apply_central_impulse](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-apply-central-impulse)(impulse: [Vector2](class_vector2.md#class-vector2)) virtual required |
| void | [_apply_force](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-apply-force)(force: [Vector2](class_vector2.md#class-vector2), position: [Vector2](class_vector2.md#class-vector2)) virtual required |
| void | [_apply_impulse](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-apply-impulse)(impulse: [Vector2](class_vector2.md#class-vector2), position: [Vector2](class_vector2.md#class-vector2)) virtual required |
| void | [_apply_torque](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-apply-torque)(torque: [float](class_float.md#class-float)) virtual required |
| void | [_apply_torque_impulse](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-apply-torque-impulse)(impulse: [float](class_float.md#class-float)) virtual required |
| [float](class_float.md#class-float) | [_get_angular_velocity](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-angular-velocity)() virtual required const |
| [Vector2](class_vector2.md#class-vector2) | [_get_center_of_mass](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-center-of-mass)() virtual required const |
| [Vector2](class_vector2.md#class-vector2) | [_get_center_of_mass_local](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-center-of-mass-local)() virtual required const |
| [int](class_int.md#class-int) | [_get_collision_layer](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-collision-layer)() virtual required const |
| [int](class_int.md#class-int) | [_get_collision_mask](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-collision-mask)() virtual required const |
| [Vector2](class_vector2.md#class-vector2) | [_get_constant_force](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-constant-force)() virtual required const |
| [float](class_float.md#class-float) | [_get_constant_torque](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-constant-torque)() virtual required const |
| [RID](class_rid.md#class-rid) | [_get_contact_collider](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-contact-collider)(contact_idx: [int](class_int.md#class-int)) virtual required const |
| [int](class_int.md#class-int) | [_get_contact_collider_id](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-contact-collider-id)(contact_idx: [int](class_int.md#class-int)) virtual required const |
| [Object](class_object.md#class-object) | [_get_contact_collider_object](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-contact-collider-object)(contact_idx: [int](class_int.md#class-int)) virtual required const |
| [Vector2](class_vector2.md#class-vector2) | [_get_contact_collider_position](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-contact-collider-position)(contact_idx: [int](class_int.md#class-int)) virtual required const |
| [int](class_int.md#class-int) | [_get_contact_collider_shape](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-contact-collider-shape)(contact_idx: [int](class_int.md#class-int)) virtual required const |
| [Vector2](class_vector2.md#class-vector2) | [_get_contact_collider_velocity_at_position](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-contact-collider-velocity-at-position)(contact_idx: [int](class_int.md#class-int)) virtual required const |
| [int](class_int.md#class-int) | [_get_contact_count](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-contact-count)() virtual required const |
| [Vector2](class_vector2.md#class-vector2) | [_get_contact_impulse](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-contact-impulse)(contact_idx: [int](class_int.md#class-int)) virtual required const |
| [Vector2](class_vector2.md#class-vector2) | [_get_contact_local_normal](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-contact-local-normal)(contact_idx: [int](class_int.md#class-int)) virtual required const |
| [Vector2](class_vector2.md#class-vector2) | [_get_contact_local_position](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-contact-local-position)(contact_idx: [int](class_int.md#class-int)) virtual required const |
| [int](class_int.md#class-int) | [_get_contact_local_shape](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-contact-local-shape)(contact_idx: [int](class_int.md#class-int)) virtual required const |
| [Vector2](class_vector2.md#class-vector2) | [_get_contact_local_velocity_at_position](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-contact-local-velocity-at-position)(contact_idx: [int](class_int.md#class-int)) virtual required const |
| [float](class_float.md#class-float) | [_get_inverse_inertia](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-inverse-inertia)() virtual required const |
| [float](class_float.md#class-float) | [_get_inverse_mass](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-inverse-mass)() virtual required const |
| [Vector2](class_vector2.md#class-vector2) | [_get_linear_velocity](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-linear-velocity)() virtual required const |
| [PhysicsDirectSpaceState2D](class_physicsdirectspacestate2d.md#class-physicsdirectspacestate2d) | [_get_space_state](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-space-state)() virtual required |
| [float](class_float.md#class-float) | [_get_step](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-step)() virtual required const |
| [float](class_float.md#class-float) | [_get_total_angular_damp](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-total-angular-damp)() virtual required const |
| [Vector2](class_vector2.md#class-vector2) | [_get_total_gravity](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-total-gravity)() virtual required const |
| [float](class_float.md#class-float) | [_get_total_linear_damp](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-total-linear-damp)() virtual required const |
| [Transform2D](class_transform2d.md#class-transform2d) | [_get_transform](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-transform)() virtual required const |
| [Vector2](class_vector2.md#class-vector2) | [_get_velocity_at_local_position](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-velocity-at-local-position)(local_position: [Vector2](class_vector2.md#class-vector2)) virtual required const |
| void | [_integrate_forces](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-integrate-forces)() virtual required |
| [bool](class_bool.md#class-bool) | [_is_sleeping](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-is-sleeping)() virtual required const |
| void | [_set_angular_velocity](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-set-angular-velocity)(velocity: [float](class_float.md#class-float)) virtual required |
| void | [_set_collision_layer](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-set-collision-layer)(layer: [int](class_int.md#class-int)) virtual required |
| void | [_set_collision_mask](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-set-collision-mask)(mask: [int](class_int.md#class-int)) virtual required |
| void | [_set_constant_force](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-set-constant-force)(force: [Vector2](class_vector2.md#class-vector2)) virtual required |
| void | [_set_constant_torque](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-set-constant-torque)(torque: [float](class_float.md#class-float)) virtual required |
| void | [_set_linear_velocity](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-set-linear-velocity)(velocity: [Vector2](class_vector2.md#class-vector2)) virtual required |
| void | [_set_sleep_state](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-set-sleep-state)(enabled: [bool](class_bool.md#class-bool)) virtual required |
| void | [_set_transform](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-set-transform)(transform: [Transform2D](class_transform2d.md#class-transform2d)) virtual required |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-physicsdirectbodystate2dextension-private-method-add-constant-central-force"></a>

void **_add_constant_central_force**(force: [Vector2](class_vector2.md#class-vector2)) virtual required [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-add-constant-central-force)

Overridable version of [PhysicsDirectBodyState2D.add_constant_central_force()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-add-constant-central-force).

---


<a id="class-physicsdirectbodystate2dextension-private-method-add-constant-force"></a>

void **_add_constant_force**(force: [Vector2](class_vector2.md#class-vector2), position: [Vector2](class_vector2.md#class-vector2)) virtual required [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-add-constant-force)

Overridable version of [PhysicsDirectBodyState2D.add_constant_force()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-add-constant-force).

---


<a id="class-physicsdirectbodystate2dextension-private-method-add-constant-torque"></a>

void **_add_constant_torque**(torque: [float](class_float.md#class-float)) virtual required [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-add-constant-torque)

Overridable version of [PhysicsDirectBodyState2D.add_constant_torque()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-add-constant-torque).

---


<a id="class-physicsdirectbodystate2dextension-private-method-apply-central-force"></a>

void **_apply_central_force**(force: [Vector2](class_vector2.md#class-vector2)) virtual required [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-apply-central-force)

Overridable version of [PhysicsDirectBodyState2D.apply_central_force()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-apply-central-force).

---


<a id="class-physicsdirectbodystate2dextension-private-method-apply-central-impulse"></a>

void **_apply_central_impulse**(impulse: [Vector2](class_vector2.md#class-vector2)) virtual required [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-apply-central-impulse)

Overridable version of [PhysicsDirectBodyState2D.apply_central_impulse()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-apply-central-impulse).

---


<a id="class-physicsdirectbodystate2dextension-private-method-apply-force"></a>

void **_apply_force**(force: [Vector2](class_vector2.md#class-vector2), position: [Vector2](class_vector2.md#class-vector2)) virtual required [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-apply-force)

Overridable version of [PhysicsDirectBodyState2D.apply_force()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-apply-force).

---


<a id="class-physicsdirectbodystate2dextension-private-method-apply-impulse"></a>

void **_apply_impulse**(impulse: [Vector2](class_vector2.md#class-vector2), position: [Vector2](class_vector2.md#class-vector2)) virtual required [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-apply-impulse)

Overridable version of [PhysicsDirectBodyState2D.apply_impulse()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-apply-impulse).

---


<a id="class-physicsdirectbodystate2dextension-private-method-apply-torque"></a>

void **_apply_torque**(torque: [float](class_float.md#class-float)) virtual required [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-apply-torque)

Overridable version of [PhysicsDirectBodyState2D.apply_torque()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-apply-torque).

---


<a id="class-physicsdirectbodystate2dextension-private-method-apply-torque-impulse"></a>

void **_apply_torque_impulse**(impulse: [float](class_float.md#class-float)) virtual required [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-apply-torque-impulse)

Overridable version of [PhysicsDirectBodyState2D.apply_torque_impulse()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-apply-torque-impulse).

---


<a id="class-physicsdirectbodystate2dextension-private-method-get-angular-velocity"></a>

[float](class_float.md#class-float) **_get_angular_velocity**() virtual required const [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-angular-velocity)

Implement to override the behavior of [PhysicsDirectBodyState2D.angular_velocity](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-property-angular-velocity) and its respective getter.

---


<a id="class-physicsdirectbodystate2dextension-private-method-get-center-of-mass"></a>

[Vector2](class_vector2.md#class-vector2) **_get_center_of_mass**() virtual required const [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-center-of-mass)

Implement to override the behavior of [PhysicsDirectBodyState2D.center_of_mass](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-property-center-of-mass) and its respective getter.

---


<a id="class-physicsdirectbodystate2dextension-private-method-get-center-of-mass-local"></a>

[Vector2](class_vector2.md#class-vector2) **_get_center_of_mass_local**() virtual required const [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-center-of-mass-local)

Implement to override the behavior of [PhysicsDirectBodyState2D.center_of_mass_local](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-property-center-of-mass-local) and its respective getter.

---


<a id="class-physicsdirectbodystate2dextension-private-method-get-collision-layer"></a>

[int](class_int.md#class-int) **_get_collision_layer**() virtual required const [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-collision-layer)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate2dextension-private-method-get-collision-mask"></a>

[int](class_int.md#class-int) **_get_collision_mask**() virtual required const [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-collision-mask)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate2dextension-private-method-get-constant-force"></a>

[Vector2](class_vector2.md#class-vector2) **_get_constant_force**() virtual required const [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-constant-force)

Overridable version of [PhysicsDirectBodyState2D.get_constant_force()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-get-constant-force).

---


<a id="class-physicsdirectbodystate2dextension-private-method-get-constant-torque"></a>

[float](class_float.md#class-float) **_get_constant_torque**() virtual required const [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-constant-torque)

Overridable version of [PhysicsDirectBodyState2D.get_constant_torque()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-get-constant-torque).

---


<a id="class-physicsdirectbodystate2dextension-private-method-get-contact-collider"></a>

[RID](class_rid.md#class-rid) **_get_contact_collider**(contact_idx: [int](class_int.md#class-int)) virtual required const [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-contact-collider)

Overridable version of [PhysicsDirectBodyState2D.get_contact_collider()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-get-contact-collider).

---


<a id="class-physicsdirectbodystate2dextension-private-method-get-contact-collider-id"></a>

[int](class_int.md#class-int) **_get_contact_collider_id**(contact_idx: [int](class_int.md#class-int)) virtual required const [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-contact-collider-id)

Overridable version of [PhysicsDirectBodyState2D.get_contact_collider_id()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-get-contact-collider-id).

---


<a id="class-physicsdirectbodystate2dextension-private-method-get-contact-collider-object"></a>

[Object](class_object.md#class-object) **_get_contact_collider_object**(contact_idx: [int](class_int.md#class-int)) virtual required const [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-contact-collider-object)

Overridable version of [PhysicsDirectBodyState2D.get_contact_collider_object()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-get-contact-collider-object).

---


<a id="class-physicsdirectbodystate2dextension-private-method-get-contact-collider-position"></a>

[Vector2](class_vector2.md#class-vector2) **_get_contact_collider_position**(contact_idx: [int](class_int.md#class-int)) virtual required const [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-contact-collider-position)

Overridable version of [PhysicsDirectBodyState2D.get_contact_collider_position()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-get-contact-collider-position).

---


<a id="class-physicsdirectbodystate2dextension-private-method-get-contact-collider-shape"></a>

[int](class_int.md#class-int) **_get_contact_collider_shape**(contact_idx: [int](class_int.md#class-int)) virtual required const [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-contact-collider-shape)

Overridable version of [PhysicsDirectBodyState2D.get_contact_collider_shape()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-get-contact-collider-shape).

---


<a id="class-physicsdirectbodystate2dextension-private-method-get-contact-collider-velocity-at-position"></a>

[Vector2](class_vector2.md#class-vector2) **_get_contact_collider_velocity_at_position**(contact_idx: [int](class_int.md#class-int)) virtual required const [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-contact-collider-velocity-at-position)

Overridable version of [PhysicsDirectBodyState2D.get_contact_collider_velocity_at_position()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-get-contact-collider-velocity-at-position).

---


<a id="class-physicsdirectbodystate2dextension-private-method-get-contact-count"></a>

[int](class_int.md#class-int) **_get_contact_count**() virtual required const [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-contact-count)

Overridable version of [PhysicsDirectBodyState2D.get_contact_count()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-get-contact-count).

---


<a id="class-physicsdirectbodystate2dextension-private-method-get-contact-impulse"></a>

[Vector2](class_vector2.md#class-vector2) **_get_contact_impulse**(contact_idx: [int](class_int.md#class-int)) virtual required const [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-contact-impulse)

Overridable version of [PhysicsDirectBodyState2D.get_contact_impulse()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-get-contact-impulse).

---


<a id="class-physicsdirectbodystate2dextension-private-method-get-contact-local-normal"></a>

[Vector2](class_vector2.md#class-vector2) **_get_contact_local_normal**(contact_idx: [int](class_int.md#class-int)) virtual required const [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-contact-local-normal)

Overridable version of [PhysicsDirectBodyState2D.get_contact_local_normal()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-get-contact-local-normal).

---


<a id="class-physicsdirectbodystate2dextension-private-method-get-contact-local-position"></a>

[Vector2](class_vector2.md#class-vector2) **_get_contact_local_position**(contact_idx: [int](class_int.md#class-int)) virtual required const [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-contact-local-position)

Overridable version of [PhysicsDirectBodyState2D.get_contact_local_position()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-get-contact-local-position).

---


<a id="class-physicsdirectbodystate2dextension-private-method-get-contact-local-shape"></a>

[int](class_int.md#class-int) **_get_contact_local_shape**(contact_idx: [int](class_int.md#class-int)) virtual required const [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-contact-local-shape)

Overridable version of [PhysicsDirectBodyState2D.get_contact_local_shape()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-get-contact-local-shape).

---


<a id="class-physicsdirectbodystate2dextension-private-method-get-contact-local-velocity-at-position"></a>

[Vector2](class_vector2.md#class-vector2) **_get_contact_local_velocity_at_position**(contact_idx: [int](class_int.md#class-int)) virtual required const [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-contact-local-velocity-at-position)

Overridable version of [PhysicsDirectBodyState2D.get_contact_local_velocity_at_position()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-get-contact-local-velocity-at-position).

---


<a id="class-physicsdirectbodystate2dextension-private-method-get-inverse-inertia"></a>

[float](class_float.md#class-float) **_get_inverse_inertia**() virtual required const [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-inverse-inertia)

Implement to override the behavior of [PhysicsDirectBodyState2D.inverse_inertia](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-property-inverse-inertia) and its respective getter.

---


<a id="class-physicsdirectbodystate2dextension-private-method-get-inverse-mass"></a>

[float](class_float.md#class-float) **_get_inverse_mass**() virtual required const [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-inverse-mass)

Implement to override the behavior of [PhysicsDirectBodyState2D.inverse_mass](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-property-inverse-mass) and its respective getter.

---


<a id="class-physicsdirectbodystate2dextension-private-method-get-linear-velocity"></a>

[Vector2](class_vector2.md#class-vector2) **_get_linear_velocity**() virtual required const [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-linear-velocity)

Implement to override the behavior of [PhysicsDirectBodyState2D.linear_velocity](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-property-linear-velocity) and its respective getter.

---


<a id="class-physicsdirectbodystate2dextension-private-method-get-space-state"></a>

[PhysicsDirectSpaceState2D](class_physicsdirectspacestate2d.md#class-physicsdirectspacestate2d) **_get_space_state**() virtual required [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-space-state)

Overridable version of [PhysicsDirectBodyState2D.get_space_state()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-get-space-state).

---


<a id="class-physicsdirectbodystate2dextension-private-method-get-step"></a>

[float](class_float.md#class-float) **_get_step**() virtual required const [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-step)

Implement to override the behavior of [PhysicsDirectBodyState2D.step](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-property-step) and its respective getter.

---


<a id="class-physicsdirectbodystate2dextension-private-method-get-total-angular-damp"></a>

[float](class_float.md#class-float) **_get_total_angular_damp**() virtual required const [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-total-angular-damp)

Implement to override the behavior of [PhysicsDirectBodyState2D.total_angular_damp](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-property-total-angular-damp) and its respective getter.

---


<a id="class-physicsdirectbodystate2dextension-private-method-get-total-gravity"></a>

[Vector2](class_vector2.md#class-vector2) **_get_total_gravity**() virtual required const [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-total-gravity)

Implement to override the behavior of [PhysicsDirectBodyState2D.total_gravity](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-property-total-gravity) and its respective getter.

---


<a id="class-physicsdirectbodystate2dextension-private-method-get-total-linear-damp"></a>

[float](class_float.md#class-float) **_get_total_linear_damp**() virtual required const [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-total-linear-damp)

Implement to override the behavior of [PhysicsDirectBodyState2D.total_linear_damp](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-property-total-linear-damp) and its respective getter.

---


<a id="class-physicsdirectbodystate2dextension-private-method-get-transform"></a>

[Transform2D](class_transform2d.md#class-transform2d) **_get_transform**() virtual required const [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-transform)

Implement to override the behavior of [PhysicsDirectBodyState2D.transform](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-property-transform) and its respective getter.

---


<a id="class-physicsdirectbodystate2dextension-private-method-get-velocity-at-local-position"></a>

[Vector2](class_vector2.md#class-vector2) **_get_velocity_at_local_position**(local_position: [Vector2](class_vector2.md#class-vector2)) virtual required const [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-get-velocity-at-local-position)

Overridable version of [PhysicsDirectBodyState2D.get_velocity_at_local_position()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-get-velocity-at-local-position).

---


<a id="class-physicsdirectbodystate2dextension-private-method-integrate-forces"></a>

void **_integrate_forces**() virtual required [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-integrate-forces)

Overridable version of [PhysicsDirectBodyState2D.integrate_forces()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-integrate-forces).

---


<a id="class-physicsdirectbodystate2dextension-private-method-is-sleeping"></a>

[bool](class_bool.md#class-bool) **_is_sleeping**() virtual required const [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-is-sleeping)

Implement to override the behavior of [PhysicsDirectBodyState2D.sleeping](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-property-sleeping) and its respective getter.

---


<a id="class-physicsdirectbodystate2dextension-private-method-set-angular-velocity"></a>

void **_set_angular_velocity**(velocity: [float](class_float.md#class-float)) virtual required [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-set-angular-velocity)

Implement to override the behavior of [PhysicsDirectBodyState2D.angular_velocity](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-property-angular-velocity) and its respective setter.

---


<a id="class-physicsdirectbodystate2dextension-private-method-set-collision-layer"></a>

void **_set_collision_layer**(layer: [int](class_int.md#class-int)) virtual required [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-set-collision-layer)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate2dextension-private-method-set-collision-mask"></a>

void **_set_collision_mask**(mask: [int](class_int.md#class-int)) virtual required [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-set-collision-mask)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate2dextension-private-method-set-constant-force"></a>

void **_set_constant_force**(force: [Vector2](class_vector2.md#class-vector2)) virtual required [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-set-constant-force)

Overridable version of [PhysicsDirectBodyState2D.set_constant_force()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-set-constant-force).

---


<a id="class-physicsdirectbodystate2dextension-private-method-set-constant-torque"></a>

void **_set_constant_torque**(torque: [float](class_float.md#class-float)) virtual required [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-set-constant-torque)

Overridable version of [PhysicsDirectBodyState2D.set_constant_torque()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-set-constant-torque).

---


<a id="class-physicsdirectbodystate2dextension-private-method-set-linear-velocity"></a>

void **_set_linear_velocity**(velocity: [Vector2](class_vector2.md#class-vector2)) virtual required [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-set-linear-velocity)

Implement to override the behavior of [PhysicsDirectBodyState2D.linear_velocity](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-property-linear-velocity) and its respective setter.

---


<a id="class-physicsdirectbodystate2dextension-private-method-set-sleep-state"></a>

void **_set_sleep_state**(enabled: [bool](class_bool.md#class-bool)) virtual required [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-set-sleep-state)

Implement to override the behavior of [PhysicsDirectBodyState2D.sleeping](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-property-sleeping) and its respective setter.

---


<a id="class-physicsdirectbodystate2dextension-private-method-set-transform"></a>

void **_set_transform**(transform: [Transform2D](class_transform2d.md#class-transform2d)) virtual required [🔗](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension-private-method-set-transform)

Implement to override the behavior of [PhysicsDirectBodyState2D.transform](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-property-transform) and its respective setter.
