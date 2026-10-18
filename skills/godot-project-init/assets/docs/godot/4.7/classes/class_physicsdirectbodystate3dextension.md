> Source: https://docs.godotengine.org/en/4.7/classes/class_physicsdirectbodystate3dextension.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="physicsdirectbodystate3dextension"></a>

<a id="class-physicsdirectbodystate3dextension"></a>

# PhysicsDirectBodyState3DExtension

**Inherits:** [PhysicsDirectBodyState3D](class_physicsdirectbodystate3d.md#class-physicsdirectbodystate3d) **<** [Object](class_object.md#class-object)

Provides virtual methods that can be overridden to create custom [PhysicsDirectBodyState3D](class_physicsdirectbodystate3d.md#class-physicsdirectbodystate3d) implementations.

<a id="description"></a>

## Description

This class extends [PhysicsDirectBodyState3D](class_physicsdirectbodystate3d.md#class-physicsdirectbodystate3d) by providing additional virtual methods that can be overridden. When these methods are overridden, they will be called instead of the internal methods of the physics server.

Intended for use with GDExtension to create custom implementations of [PhysicsDirectBodyState3D](class_physicsdirectbodystate3d.md#class-physicsdirectbodystate3d).

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [_add_constant_central_force](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-add-constant-central-force)(force: [Vector3](class_vector3.md#class-vector3)) virtual required |
| void | [_add_constant_force](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-add-constant-force)(force: [Vector3](class_vector3.md#class-vector3), position: [Vector3](class_vector3.md#class-vector3)) virtual required |
| void | [_add_constant_torque](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-add-constant-torque)(torque: [Vector3](class_vector3.md#class-vector3)) virtual required |
| void | [_apply_central_force](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-apply-central-force)(force: [Vector3](class_vector3.md#class-vector3)) virtual required |
| void | [_apply_central_impulse](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-apply-central-impulse)(impulse: [Vector3](class_vector3.md#class-vector3)) virtual required |
| void | [_apply_force](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-apply-force)(force: [Vector3](class_vector3.md#class-vector3), position: [Vector3](class_vector3.md#class-vector3)) virtual required |
| void | [_apply_impulse](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-apply-impulse)(impulse: [Vector3](class_vector3.md#class-vector3), position: [Vector3](class_vector3.md#class-vector3)) virtual required |
| void | [_apply_torque](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-apply-torque)(torque: [Vector3](class_vector3.md#class-vector3)) virtual required |
| void | [_apply_torque_impulse](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-apply-torque-impulse)(impulse: [Vector3](class_vector3.md#class-vector3)) virtual required |
| [Vector3](class_vector3.md#class-vector3) | [_get_angular_velocity](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-angular-velocity)() virtual required const |
| [Vector3](class_vector3.md#class-vector3) | [_get_center_of_mass](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-center-of-mass)() virtual required const |
| [Vector3](class_vector3.md#class-vector3) | [_get_center_of_mass_local](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-center-of-mass-local)() virtual required const |
| [int](class_int.md#class-int) | [_get_collision_layer](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-collision-layer)() virtual required const |
| [int](class_int.md#class-int) | [_get_collision_mask](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-collision-mask)() virtual required const |
| [Vector3](class_vector3.md#class-vector3) | [_get_constant_force](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-constant-force)() virtual required const |
| [Vector3](class_vector3.md#class-vector3) | [_get_constant_torque](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-constant-torque)() virtual required const |
| [RID](class_rid.md#class-rid) | [_get_contact_collider](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-contact-collider)(contact_idx: [int](class_int.md#class-int)) virtual required const |
| [int](class_int.md#class-int) | [_get_contact_collider_id](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-contact-collider-id)(contact_idx: [int](class_int.md#class-int)) virtual required const |
| [Object](class_object.md#class-object) | [_get_contact_collider_object](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-contact-collider-object)(contact_idx: [int](class_int.md#class-int)) virtual required const |
| [Vector3](class_vector3.md#class-vector3) | [_get_contact_collider_position](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-contact-collider-position)(contact_idx: [int](class_int.md#class-int)) virtual required const |
| [int](class_int.md#class-int) | [_get_contact_collider_shape](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-contact-collider-shape)(contact_idx: [int](class_int.md#class-int)) virtual required const |
| [Vector3](class_vector3.md#class-vector3) | [_get_contact_collider_velocity_at_position](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-contact-collider-velocity-at-position)(contact_idx: [int](class_int.md#class-int)) virtual required const |
| [int](class_int.md#class-int) | [_get_contact_count](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-contact-count)() virtual required const |
| [Vector3](class_vector3.md#class-vector3) | [_get_contact_impulse](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-contact-impulse)(contact_idx: [int](class_int.md#class-int)) virtual required const |
| [Vector3](class_vector3.md#class-vector3) | [_get_contact_local_normal](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-contact-local-normal)(contact_idx: [int](class_int.md#class-int)) virtual required const |
| [Vector3](class_vector3.md#class-vector3) | [_get_contact_local_position](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-contact-local-position)(contact_idx: [int](class_int.md#class-int)) virtual required const |
| [int](class_int.md#class-int) | [_get_contact_local_shape](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-contact-local-shape)(contact_idx: [int](class_int.md#class-int)) virtual required const |
| [Vector3](class_vector3.md#class-vector3) | [_get_contact_local_velocity_at_position](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-contact-local-velocity-at-position)(contact_idx: [int](class_int.md#class-int)) virtual required const |
| [Vector3](class_vector3.md#class-vector3) | [_get_inverse_inertia](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-inverse-inertia)() virtual required const |
| [Basis](class_basis.md#class-basis) | [_get_inverse_inertia_tensor](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-inverse-inertia-tensor)() virtual required const |
| [float](class_float.md#class-float) | [_get_inverse_mass](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-inverse-mass)() virtual required const |
| [Vector3](class_vector3.md#class-vector3) | [_get_linear_velocity](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-linear-velocity)() virtual required const |
| [Basis](class_basis.md#class-basis) | [_get_principal_inertia_axes](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-principal-inertia-axes)() virtual required const |
| [PhysicsDirectSpaceState3D](class_physicsdirectspacestate3d.md#class-physicsdirectspacestate3d) | [_get_space_state](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-space-state)() virtual required |
| [float](class_float.md#class-float) | [_get_step](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-step)() virtual required const |
| [float](class_float.md#class-float) | [_get_total_angular_damp](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-total-angular-damp)() virtual required const |
| [Vector3](class_vector3.md#class-vector3) | [_get_total_gravity](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-total-gravity)() virtual required const |
| [float](class_float.md#class-float) | [_get_total_linear_damp](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-total-linear-damp)() virtual required const |
| [Transform3D](class_transform3d.md#class-transform3d) | [_get_transform](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-transform)() virtual required const |
| [Vector3](class_vector3.md#class-vector3) | [_get_velocity_at_local_position](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-velocity-at-local-position)(local_position: [Vector3](class_vector3.md#class-vector3)) virtual required const |
| void | [_integrate_forces](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-integrate-forces)() virtual required |
| [bool](class_bool.md#class-bool) | [_is_sleeping](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-is-sleeping)() virtual required const |
| void | [_set_angular_velocity](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-set-angular-velocity)(velocity: [Vector3](class_vector3.md#class-vector3)) virtual required |
| void | [_set_collision_layer](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-set-collision-layer)(layer: [int](class_int.md#class-int)) virtual required |
| void | [_set_collision_mask](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-set-collision-mask)(mask: [int](class_int.md#class-int)) virtual required |
| void | [_set_constant_force](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-set-constant-force)(force: [Vector3](class_vector3.md#class-vector3)) virtual required |
| void | [_set_constant_torque](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-set-constant-torque)(torque: [Vector3](class_vector3.md#class-vector3)) virtual required |
| void | [_set_linear_velocity](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-set-linear-velocity)(velocity: [Vector3](class_vector3.md#class-vector3)) virtual required |
| void | [_set_sleep_state](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-set-sleep-state)(enabled: [bool](class_bool.md#class-bool)) virtual required |
| void | [_set_transform](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-set-transform)(transform: [Transform3D](class_transform3d.md#class-transform3d)) virtual required |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-physicsdirectbodystate3dextension-private-method-add-constant-central-force"></a>

void **_add_constant_central_force**(force: [Vector3](class_vector3.md#class-vector3)) virtual required [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-add-constant-central-force)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-add-constant-force"></a>

void **_add_constant_force**(force: [Vector3](class_vector3.md#class-vector3), position: [Vector3](class_vector3.md#class-vector3)) virtual required [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-add-constant-force)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-add-constant-torque"></a>

void **_add_constant_torque**(torque: [Vector3](class_vector3.md#class-vector3)) virtual required [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-add-constant-torque)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-apply-central-force"></a>

void **_apply_central_force**(force: [Vector3](class_vector3.md#class-vector3)) virtual required [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-apply-central-force)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-apply-central-impulse"></a>

void **_apply_central_impulse**(impulse: [Vector3](class_vector3.md#class-vector3)) virtual required [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-apply-central-impulse)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-apply-force"></a>

void **_apply_force**(force: [Vector3](class_vector3.md#class-vector3), position: [Vector3](class_vector3.md#class-vector3)) virtual required [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-apply-force)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-apply-impulse"></a>

void **_apply_impulse**(impulse: [Vector3](class_vector3.md#class-vector3), position: [Vector3](class_vector3.md#class-vector3)) virtual required [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-apply-impulse)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-apply-torque"></a>

void **_apply_torque**(torque: [Vector3](class_vector3.md#class-vector3)) virtual required [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-apply-torque)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-apply-torque-impulse"></a>

void **_apply_torque_impulse**(impulse: [Vector3](class_vector3.md#class-vector3)) virtual required [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-apply-torque-impulse)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-get-angular-velocity"></a>

[Vector3](class_vector3.md#class-vector3) **_get_angular_velocity**() virtual required const [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-angular-velocity)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-get-center-of-mass"></a>

[Vector3](class_vector3.md#class-vector3) **_get_center_of_mass**() virtual required const [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-center-of-mass)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-get-center-of-mass-local"></a>

[Vector3](class_vector3.md#class-vector3) **_get_center_of_mass_local**() virtual required const [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-center-of-mass-local)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-get-collision-layer"></a>

[int](class_int.md#class-int) **_get_collision_layer**() virtual required const [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-collision-layer)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-get-collision-mask"></a>

[int](class_int.md#class-int) **_get_collision_mask**() virtual required const [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-collision-mask)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-get-constant-force"></a>

[Vector3](class_vector3.md#class-vector3) **_get_constant_force**() virtual required const [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-constant-force)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-get-constant-torque"></a>

[Vector3](class_vector3.md#class-vector3) **_get_constant_torque**() virtual required const [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-constant-torque)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-get-contact-collider"></a>

[RID](class_rid.md#class-rid) **_get_contact_collider**(contact_idx: [int](class_int.md#class-int)) virtual required const [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-contact-collider)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-get-contact-collider-id"></a>

[int](class_int.md#class-int) **_get_contact_collider_id**(contact_idx: [int](class_int.md#class-int)) virtual required const [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-contact-collider-id)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-get-contact-collider-object"></a>

[Object](class_object.md#class-object) **_get_contact_collider_object**(contact_idx: [int](class_int.md#class-int)) virtual required const [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-contact-collider-object)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-get-contact-collider-position"></a>

[Vector3](class_vector3.md#class-vector3) **_get_contact_collider_position**(contact_idx: [int](class_int.md#class-int)) virtual required const [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-contact-collider-position)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-get-contact-collider-shape"></a>

[int](class_int.md#class-int) **_get_contact_collider_shape**(contact_idx: [int](class_int.md#class-int)) virtual required const [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-contact-collider-shape)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-get-contact-collider-velocity-at-position"></a>

[Vector3](class_vector3.md#class-vector3) **_get_contact_collider_velocity_at_position**(contact_idx: [int](class_int.md#class-int)) virtual required const [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-contact-collider-velocity-at-position)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-get-contact-count"></a>

[int](class_int.md#class-int) **_get_contact_count**() virtual required const [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-contact-count)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-get-contact-impulse"></a>

[Vector3](class_vector3.md#class-vector3) **_get_contact_impulse**(contact_idx: [int](class_int.md#class-int)) virtual required const [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-contact-impulse)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-get-contact-local-normal"></a>

[Vector3](class_vector3.md#class-vector3) **_get_contact_local_normal**(contact_idx: [int](class_int.md#class-int)) virtual required const [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-contact-local-normal)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-get-contact-local-position"></a>

[Vector3](class_vector3.md#class-vector3) **_get_contact_local_position**(contact_idx: [int](class_int.md#class-int)) virtual required const [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-contact-local-position)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-get-contact-local-shape"></a>

[int](class_int.md#class-int) **_get_contact_local_shape**(contact_idx: [int](class_int.md#class-int)) virtual required const [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-contact-local-shape)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-get-contact-local-velocity-at-position"></a>

[Vector3](class_vector3.md#class-vector3) **_get_contact_local_velocity_at_position**(contact_idx: [int](class_int.md#class-int)) virtual required const [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-contact-local-velocity-at-position)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-get-inverse-inertia"></a>

[Vector3](class_vector3.md#class-vector3) **_get_inverse_inertia**() virtual required const [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-inverse-inertia)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-get-inverse-inertia-tensor"></a>

[Basis](class_basis.md#class-basis) **_get_inverse_inertia_tensor**() virtual required const [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-inverse-inertia-tensor)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-get-inverse-mass"></a>

[float](class_float.md#class-float) **_get_inverse_mass**() virtual required const [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-inverse-mass)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-get-linear-velocity"></a>

[Vector3](class_vector3.md#class-vector3) **_get_linear_velocity**() virtual required const [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-linear-velocity)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-get-principal-inertia-axes"></a>

[Basis](class_basis.md#class-basis) **_get_principal_inertia_axes**() virtual required const [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-principal-inertia-axes)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-get-space-state"></a>

[PhysicsDirectSpaceState3D](class_physicsdirectspacestate3d.md#class-physicsdirectspacestate3d) **_get_space_state**() virtual required [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-space-state)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-get-step"></a>

[float](class_float.md#class-float) **_get_step**() virtual required const [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-step)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-get-total-angular-damp"></a>

[float](class_float.md#class-float) **_get_total_angular_damp**() virtual required const [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-total-angular-damp)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-get-total-gravity"></a>

[Vector3](class_vector3.md#class-vector3) **_get_total_gravity**() virtual required const [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-total-gravity)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-get-total-linear-damp"></a>

[float](class_float.md#class-float) **_get_total_linear_damp**() virtual required const [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-total-linear-damp)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-get-transform"></a>

[Transform3D](class_transform3d.md#class-transform3d) **_get_transform**() virtual required const [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-transform)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-get-velocity-at-local-position"></a>

[Vector3](class_vector3.md#class-vector3) **_get_velocity_at_local_position**(local_position: [Vector3](class_vector3.md#class-vector3)) virtual required const [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-get-velocity-at-local-position)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-integrate-forces"></a>

void **_integrate_forces**() virtual required [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-integrate-forces)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-is-sleeping"></a>

[bool](class_bool.md#class-bool) **_is_sleeping**() virtual required const [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-is-sleeping)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-set-angular-velocity"></a>

void **_set_angular_velocity**(velocity: [Vector3](class_vector3.md#class-vector3)) virtual required [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-set-angular-velocity)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-set-collision-layer"></a>

void **_set_collision_layer**(layer: [int](class_int.md#class-int)) virtual required [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-set-collision-layer)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-set-collision-mask"></a>

void **_set_collision_mask**(mask: [int](class_int.md#class-int)) virtual required [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-set-collision-mask)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-set-constant-force"></a>

void **_set_constant_force**(force: [Vector3](class_vector3.md#class-vector3)) virtual required [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-set-constant-force)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-set-constant-torque"></a>

void **_set_constant_torque**(torque: [Vector3](class_vector3.md#class-vector3)) virtual required [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-set-constant-torque)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-set-linear-velocity"></a>

void **_set_linear_velocity**(velocity: [Vector3](class_vector3.md#class-vector3)) virtual required [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-set-linear-velocity)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-set-sleep-state"></a>

void **_set_sleep_state**(enabled: [bool](class_bool.md#class-bool)) virtual required [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-set-sleep-state)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectbodystate3dextension-private-method-set-transform"></a>

void **_set_transform**(transform: [Transform3D](class_transform3d.md#class-transform3d)) virtual required [🔗](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension-private-method-set-transform)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!
