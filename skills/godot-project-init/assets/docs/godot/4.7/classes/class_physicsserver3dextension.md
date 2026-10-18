> Source: https://docs.godotengine.org/en/4.7/classes/class_physicsserver3dextension.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="physicsserver3dextension"></a>

<a id="class-physicsserver3dextension"></a>

# PhysicsServer3DExtension

**Inherits:** [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d) **<** [Object](class_object.md#class-object)

Provides virtual methods that can be overridden to create custom [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d) implementations.

<a id="description"></a>

## Description

This class extends [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d) by providing additional virtual methods that can be overridden. When these methods are overridden, they will be called instead of the internal methods of the physics server.

Intended for use with GDExtension to create custom implementations of [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d).

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [_area_add_shape](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-add-shape)(area: [RID](class_rid.md#class-rid), shape: [RID](class_rid.md#class-rid), transform: [Transform3D](class_transform3d.md#class-transform3d), disabled: [bool](class_bool.md#class-bool)) virtual required |
| void | [_area_attach_object_instance_id](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-attach-object-instance-id)(area: [RID](class_rid.md#class-rid), id: [int](class_int.md#class-int)) virtual required |
| void | [_area_clear_shapes](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-clear-shapes)(area: [RID](class_rid.md#class-rid)) virtual required |
| [RID](class_rid.md#class-rid) | [_area_create](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-create)() virtual required |
| [int](class_int.md#class-int) | [_area_get_collision_layer](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-get-collision-layer)(area: [RID](class_rid.md#class-rid)) virtual required const |
| [int](class_int.md#class-int) | [_area_get_collision_mask](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-get-collision-mask)(area: [RID](class_rid.md#class-rid)) virtual required const |
| [int](class_int.md#class-int) | [_area_get_object_instance_id](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-get-object-instance-id)(area: [RID](class_rid.md#class-rid)) virtual required const |
| [Variant](class_variant.md#class-variant) | [_area_get_param](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-get-param)(area: [RID](class_rid.md#class-rid), param: [AreaParameter](class_physicsserver3d.md#enum-physicsserver3d-areaparameter)) virtual required const |
| [RID](class_rid.md#class-rid) | [_area_get_shape](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-get-shape)(area: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int)) virtual required const |
| [int](class_int.md#class-int) | [_area_get_shape_count](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-get-shape-count)(area: [RID](class_rid.md#class-rid)) virtual required const |
| [Transform3D](class_transform3d.md#class-transform3d) | [_area_get_shape_transform](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-get-shape-transform)(area: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int)) virtual required const |
| [RID](class_rid.md#class-rid) | [_area_get_space](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-get-space)(area: [RID](class_rid.md#class-rid)) virtual required const |
| [Transform3D](class_transform3d.md#class-transform3d) | [_area_get_transform](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-get-transform)(area: [RID](class_rid.md#class-rid)) virtual required const |
| void | [_area_remove_shape](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-remove-shape)(area: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int)) virtual required |
| void | [_area_set_area_monitor_callback](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-set-area-monitor-callback)(area: [RID](class_rid.md#class-rid), callback: [Callable](class_callable.md#class-callable)) virtual required |
| void | [_area_set_collision_layer](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-set-collision-layer)(area: [RID](class_rid.md#class-rid), layer: [int](class_int.md#class-int)) virtual required |
| void | [_area_set_collision_mask](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-set-collision-mask)(area: [RID](class_rid.md#class-rid), mask: [int](class_int.md#class-int)) virtual required |
| void | [_area_set_monitor_callback](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-set-monitor-callback)(area: [RID](class_rid.md#class-rid), callback: [Callable](class_callable.md#class-callable)) virtual required |
| void | [_area_set_monitorable](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-set-monitorable)(area: [RID](class_rid.md#class-rid), monitorable: [bool](class_bool.md#class-bool)) virtual required |
| void | [_area_set_param](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-set-param)(area: [RID](class_rid.md#class-rid), param: [AreaParameter](class_physicsserver3d.md#enum-physicsserver3d-areaparameter), value: [Variant](class_variant.md#class-variant)) virtual required |
| void | [_area_set_ray_pickable](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-set-ray-pickable)(area: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool)) virtual required |
| void | [_area_set_shape](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-set-shape)(area: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int), shape: [RID](class_rid.md#class-rid)) virtual required |
| void | [_area_set_shape_disabled](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-set-shape-disabled)(area: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool)) virtual required |
| void | [_area_set_shape_transform](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-set-shape-transform)(area: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int), transform: [Transform3D](class_transform3d.md#class-transform3d)) virtual required |
| void | [_area_set_space](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-set-space)(area: [RID](class_rid.md#class-rid), space: [RID](class_rid.md#class-rid)) virtual required |
| void | [_area_set_transform](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-set-transform)(area: [RID](class_rid.md#class-rid), transform: [Transform3D](class_transform3d.md#class-transform3d)) virtual required |
| void | [_body_add_collision_exception](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-add-collision-exception)(body: [RID](class_rid.md#class-rid), excepted_body: [RID](class_rid.md#class-rid)) virtual required |
| void | [_body_add_constant_central_force](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-add-constant-central-force)(body: [RID](class_rid.md#class-rid), force: [Vector3](class_vector3.md#class-vector3)) virtual required |
| void | [_body_add_constant_force](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-add-constant-force)(body: [RID](class_rid.md#class-rid), force: [Vector3](class_vector3.md#class-vector3), position: [Vector3](class_vector3.md#class-vector3)) virtual required |
| void | [_body_add_constant_torque](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-add-constant-torque)(body: [RID](class_rid.md#class-rid), torque: [Vector3](class_vector3.md#class-vector3)) virtual required |
| void | [_body_add_shape](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-add-shape)(body: [RID](class_rid.md#class-rid), shape: [RID](class_rid.md#class-rid), transform: [Transform3D](class_transform3d.md#class-transform3d), disabled: [bool](class_bool.md#class-bool)) virtual required |
| void | [_body_apply_central_force](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-apply-central-force)(body: [RID](class_rid.md#class-rid), force: [Vector3](class_vector3.md#class-vector3)) virtual required |
| void | [_body_apply_central_impulse](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-apply-central-impulse)(body: [RID](class_rid.md#class-rid), impulse: [Vector3](class_vector3.md#class-vector3)) virtual required |
| void | [_body_apply_force](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-apply-force)(body: [RID](class_rid.md#class-rid), force: [Vector3](class_vector3.md#class-vector3), position: [Vector3](class_vector3.md#class-vector3)) virtual required |
| void | [_body_apply_impulse](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-apply-impulse)(body: [RID](class_rid.md#class-rid), impulse: [Vector3](class_vector3.md#class-vector3), position: [Vector3](class_vector3.md#class-vector3)) virtual required |
| void | [_body_apply_torque](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-apply-torque)(body: [RID](class_rid.md#class-rid), torque: [Vector3](class_vector3.md#class-vector3)) virtual required |
| void | [_body_apply_torque_impulse](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-apply-torque-impulse)(body: [RID](class_rid.md#class-rid), impulse: [Vector3](class_vector3.md#class-vector3)) virtual required |
| void | [_body_attach_object_instance_id](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-attach-object-instance-id)(body: [RID](class_rid.md#class-rid), id: [int](class_int.md#class-int)) virtual required |
| void | [_body_clear_shapes](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-clear-shapes)(body: [RID](class_rid.md#class-rid)) virtual required |
| [RID](class_rid.md#class-rid) | [_body_create](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-create)() virtual required |
| [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] | [_body_get_collision_exceptions](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-get-collision-exceptions)(body: [RID](class_rid.md#class-rid)) virtual required const |
| [int](class_int.md#class-int) | [_body_get_collision_layer](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-get-collision-layer)(body: [RID](class_rid.md#class-rid)) virtual required const |
| [int](class_int.md#class-int) | [_body_get_collision_mask](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-get-collision-mask)(body: [RID](class_rid.md#class-rid)) virtual required const |
| [float](class_float.md#class-float) | [_body_get_collision_priority](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-get-collision-priority)(body: [RID](class_rid.md#class-rid)) virtual required const |
| [Vector3](class_vector3.md#class-vector3) | [_body_get_constant_force](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-get-constant-force)(body: [RID](class_rid.md#class-rid)) virtual required const |
| [Vector3](class_vector3.md#class-vector3) | [_body_get_constant_torque](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-get-constant-torque)(body: [RID](class_rid.md#class-rid)) virtual required const |
| [float](class_float.md#class-float) | [_body_get_contacts_reported_depth_threshold](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-get-contacts-reported-depth-threshold)(body: [RID](class_rid.md#class-rid)) virtual required const |
| [PhysicsDirectBodyState3D](class_physicsdirectbodystate3d.md#class-physicsdirectbodystate3d) | [_body_get_direct_state](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-get-direct-state)(body: [RID](class_rid.md#class-rid)) virtual required |
| [int](class_int.md#class-int) | [_body_get_max_contacts_reported](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-get-max-contacts-reported)(body: [RID](class_rid.md#class-rid)) virtual required const |
| [BodyMode](class_physicsserver3d.md#enum-physicsserver3d-bodymode) | [_body_get_mode](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-get-mode)(body: [RID](class_rid.md#class-rid)) virtual required const |
| [int](class_int.md#class-int) | [_body_get_object_instance_id](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-get-object-instance-id)(body: [RID](class_rid.md#class-rid)) virtual required const |
| [Variant](class_variant.md#class-variant) | [_body_get_param](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-get-param)(body: [RID](class_rid.md#class-rid), param: [BodyParameter](class_physicsserver3d.md#enum-physicsserver3d-bodyparameter)) virtual required const |
| [RID](class_rid.md#class-rid) | [_body_get_shape](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-get-shape)(body: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int)) virtual required const |
| [int](class_int.md#class-int) | [_body_get_shape_count](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-get-shape-count)(body: [RID](class_rid.md#class-rid)) virtual required const |
| [Transform3D](class_transform3d.md#class-transform3d) | [_body_get_shape_transform](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-get-shape-transform)(body: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int)) virtual required const |
| [RID](class_rid.md#class-rid) | [_body_get_space](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-get-space)(body: [RID](class_rid.md#class-rid)) virtual required const |
| [Variant](class_variant.md#class-variant) | [_body_get_state](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-get-state)(body: [RID](class_rid.md#class-rid), state: [BodyState](class_physicsserver3d.md#enum-physicsserver3d-bodystate)) virtual required const |
| [int](class_int.md#class-int) | [_body_get_user_flags](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-get-user-flags)(body: [RID](class_rid.md#class-rid)) virtual required const |
| [bool](class_bool.md#class-bool) | [_body_is_axis_locked](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-is-axis-locked)(body: [RID](class_rid.md#class-rid), axis: [BodyAxis](class_physicsserver3d.md#enum-physicsserver3d-bodyaxis)) virtual required const |
| [bool](class_bool.md#class-bool) | [_body_is_continuous_collision_detection_enabled](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-is-continuous-collision-detection-enabled)(body: [RID](class_rid.md#class-rid)) virtual required const |
| [bool](class_bool.md#class-bool) | [_body_is_omitting_force_integration](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-is-omitting-force-integration)(body: [RID](class_rid.md#class-rid)) virtual required const |
| void | [_body_remove_collision_exception](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-remove-collision-exception)(body: [RID](class_rid.md#class-rid), excepted_body: [RID](class_rid.md#class-rid)) virtual required |
| void | [_body_remove_shape](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-remove-shape)(body: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int)) virtual required |
| void | [_body_reset_mass_properties](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-reset-mass-properties)(body: [RID](class_rid.md#class-rid)) virtual required |
| void | [_body_set_axis_lock](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-axis-lock)(body: [RID](class_rid.md#class-rid), axis: [BodyAxis](class_physicsserver3d.md#enum-physicsserver3d-bodyaxis), lock: [bool](class_bool.md#class-bool)) virtual required |
| void | [_body_set_axis_velocity](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-axis-velocity)(body: [RID](class_rid.md#class-rid), axis_velocity: [Vector3](class_vector3.md#class-vector3)) virtual required |
| void | [_body_set_collision_layer](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-collision-layer)(body: [RID](class_rid.md#class-rid), layer: [int](class_int.md#class-int)) virtual required |
| void | [_body_set_collision_mask](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-collision-mask)(body: [RID](class_rid.md#class-rid), mask: [int](class_int.md#class-int)) virtual required |
| void | [_body_set_collision_priority](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-collision-priority)(body: [RID](class_rid.md#class-rid), priority: [float](class_float.md#class-float)) virtual required |
| void | [_body_set_constant_force](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-constant-force)(body: [RID](class_rid.md#class-rid), force: [Vector3](class_vector3.md#class-vector3)) virtual required |
| void | [_body_set_constant_torque](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-constant-torque)(body: [RID](class_rid.md#class-rid), torque: [Vector3](class_vector3.md#class-vector3)) virtual required |
| void | [_body_set_contacts_reported_depth_threshold](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-contacts-reported-depth-threshold)(body: [RID](class_rid.md#class-rid), threshold: [float](class_float.md#class-float)) virtual required |
| void | [_body_set_enable_continuous_collision_detection](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-enable-continuous-collision-detection)(body: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool)) virtual required |
| void | [_body_set_force_integration_callback](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-force-integration-callback)(body: [RID](class_rid.md#class-rid), callable: [Callable](class_callable.md#class-callable), userdata: [Variant](class_variant.md#class-variant)) virtual required |
| void | [_body_set_max_contacts_reported](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-max-contacts-reported)(body: [RID](class_rid.md#class-rid), amount: [int](class_int.md#class-int)) virtual required |
| void | [_body_set_mode](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-mode)(body: [RID](class_rid.md#class-rid), mode: [BodyMode](class_physicsserver3d.md#enum-physicsserver3d-bodymode)) virtual required |
| void | [_body_set_omit_force_integration](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-omit-force-integration)(body: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool)) virtual required |
| void | [_body_set_param](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-param)(body: [RID](class_rid.md#class-rid), param: [BodyParameter](class_physicsserver3d.md#enum-physicsserver3d-bodyparameter), value: [Variant](class_variant.md#class-variant)) virtual required |
| void | [_body_set_ray_pickable](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-ray-pickable)(body: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool)) virtual required |
| void | [_body_set_shape](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-shape)(body: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int), shape: [RID](class_rid.md#class-rid)) virtual required |
| void | [_body_set_shape_disabled](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-shape-disabled)(body: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool)) virtual required |
| void | [_body_set_shape_transform](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-shape-transform)(body: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int), transform: [Transform3D](class_transform3d.md#class-transform3d)) virtual required |
| void | [_body_set_space](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-space)(body: [RID](class_rid.md#class-rid), space: [RID](class_rid.md#class-rid)) virtual required |
| void | [_body_set_state](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-state)(body: [RID](class_rid.md#class-rid), state: [BodyState](class_physicsserver3d.md#enum-physicsserver3d-bodystate), value: [Variant](class_variant.md#class-variant)) virtual required |
| void | [_body_set_state_sync_callback](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-state-sync-callback)(body: [RID](class_rid.md#class-rid), callable: [Callable](class_callable.md#class-callable)) virtual required |
| void | [_body_set_user_flags](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-user-flags)(body: [RID](class_rid.md#class-rid), flags: [int](class_int.md#class-int)) virtual required |
| [bool](class_bool.md#class-bool) | [_body_test_motion](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-test-motion)(body: [RID](class_rid.md#class-rid), from: [Transform3D](class_transform3d.md#class-transform3d), motion: [Vector3](class_vector3.md#class-vector3), margin: [float](class_float.md#class-float), max_collisions: [int](class_int.md#class-int), collide_separation_ray: [bool](class_bool.md#class-bool), recovery_as_collision: [bool](class_bool.md#class-bool), r_result: `PhysicsServer3DExtensionMotionResult*`) virtual required const |
| [RID](class_rid.md#class-rid) | [_box_shape_create](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-box-shape-create)() virtual required |
| [RID](class_rid.md#class-rid) | [_capsule_shape_create](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-capsule-shape-create)() virtual required |
| [RID](class_rid.md#class-rid) | [_concave_polygon_shape_create](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-concave-polygon-shape-create)() virtual required |
| [float](class_float.md#class-float) | [_cone_twist_joint_get_param](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-cone-twist-joint-get-param)(joint: [RID](class_rid.md#class-rid), param: [ConeTwistJointParam](class_physicsserver3d.md#enum-physicsserver3d-conetwistjointparam)) virtual required const |
| void | [_cone_twist_joint_set_param](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-cone-twist-joint-set-param)(joint: [RID](class_rid.md#class-rid), param: [ConeTwistJointParam](class_physicsserver3d.md#enum-physicsserver3d-conetwistjointparam), value: [float](class_float.md#class-float)) virtual required |
| [RID](class_rid.md#class-rid) | [_convex_polygon_shape_create](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-convex-polygon-shape-create)() virtual required |
| [RID](class_rid.md#class-rid) | [_custom_shape_create](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-custom-shape-create)() virtual required |
| [RID](class_rid.md#class-rid) | [_cylinder_shape_create](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-cylinder-shape-create)() virtual required |
| void | [_end_sync](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-end-sync)() virtual required |
| void | [_finish](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-finish)() virtual required |
| void | [_flush_queries](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-flush-queries)() virtual required |
| void | [_free_rid](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-free-rid)(rid: [RID](class_rid.md#class-rid)) virtual required |
| [bool](class_bool.md#class-bool) | [_generic_6dof_joint_get_flag](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-generic-6dof-joint-get-flag)(joint: [RID](class_rid.md#class-rid), axis: [Axis](class_vector3.md#enum-vector3-axis), flag: [G6DOFJointAxisFlag](class_physicsserver3d.md#enum-physicsserver3d-g6dofjointaxisflag)) virtual required const |
| [float](class_float.md#class-float) | [_generic_6dof_joint_get_param](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-generic-6dof-joint-get-param)(joint: [RID](class_rid.md#class-rid), axis: [Axis](class_vector3.md#enum-vector3-axis), param: [G6DOFJointAxisParam](class_physicsserver3d.md#enum-physicsserver3d-g6dofjointaxisparam)) virtual required const |
| void | [_generic_6dof_joint_set_flag](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-generic-6dof-joint-set-flag)(joint: [RID](class_rid.md#class-rid), axis: [Axis](class_vector3.md#enum-vector3-axis), flag: [G6DOFJointAxisFlag](class_physicsserver3d.md#enum-physicsserver3d-g6dofjointaxisflag), enable: [bool](class_bool.md#class-bool)) virtual required |
| void | [_generic_6dof_joint_set_param](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-generic-6dof-joint-set-param)(joint: [RID](class_rid.md#class-rid), axis: [Axis](class_vector3.md#enum-vector3-axis), param: [G6DOFJointAxisParam](class_physicsserver3d.md#enum-physicsserver3d-g6dofjointaxisparam), value: [float](class_float.md#class-float)) virtual required |
| [int](class_int.md#class-int) | [_get_process_info](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-get-process-info)(process_info: [ProcessInfo](class_physicsserver3d.md#enum-physicsserver3d-processinfo)) virtual required |
| [RID](class_rid.md#class-rid) | [_heightmap_shape_create](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-heightmap-shape-create)() virtual required |
| [bool](class_bool.md#class-bool) | [_hinge_joint_get_flag](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-hinge-joint-get-flag)(joint: [RID](class_rid.md#class-rid), flag: [HingeJointFlag](class_physicsserver3d.md#enum-physicsserver3d-hingejointflag)) virtual required const |
| [float](class_float.md#class-float) | [_hinge_joint_get_param](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-hinge-joint-get-param)(joint: [RID](class_rid.md#class-rid), param: [HingeJointParam](class_physicsserver3d.md#enum-physicsserver3d-hingejointparam)) virtual required const |
| void | [_hinge_joint_set_flag](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-hinge-joint-set-flag)(joint: [RID](class_rid.md#class-rid), flag: [HingeJointFlag](class_physicsserver3d.md#enum-physicsserver3d-hingejointflag), enabled: [bool](class_bool.md#class-bool)) virtual required |
| void | [_hinge_joint_set_param](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-hinge-joint-set-param)(joint: [RID](class_rid.md#class-rid), param: [HingeJointParam](class_physicsserver3d.md#enum-physicsserver3d-hingejointparam), value: [float](class_float.md#class-float)) virtual required |
| void | [_init](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-init)() virtual required |
| [bool](class_bool.md#class-bool) | [_is_flushing_queries](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-is-flushing-queries)() virtual required const |
| void | [_joint_clear](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-joint-clear)(joint: [RID](class_rid.md#class-rid)) virtual required |
| [RID](class_rid.md#class-rid) | [_joint_create](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-joint-create)() virtual required |
| void | [_joint_disable_collisions_between_bodies](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-joint-disable-collisions-between-bodies)(joint: [RID](class_rid.md#class-rid), disable: [bool](class_bool.md#class-bool)) virtual required |
| [int](class_int.md#class-int) | [_joint_get_solver_priority](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-joint-get-solver-priority)(joint: [RID](class_rid.md#class-rid)) virtual required const |
| [JointType](class_physicsserver3d.md#enum-physicsserver3d-jointtype) | [_joint_get_type](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-joint-get-type)(joint: [RID](class_rid.md#class-rid)) virtual required const |
| [bool](class_bool.md#class-bool) | [_joint_is_disabled_collisions_between_bodies](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-joint-is-disabled-collisions-between-bodies)(joint: [RID](class_rid.md#class-rid)) virtual required const |
| void | [_joint_make_cone_twist](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-joint-make-cone-twist)(joint: [RID](class_rid.md#class-rid), body_A: [RID](class_rid.md#class-rid), local_ref_A: [Transform3D](class_transform3d.md#class-transform3d), body_B: [RID](class_rid.md#class-rid), local_ref_B: [Transform3D](class_transform3d.md#class-transform3d)) virtual required |
| void | [_joint_make_generic_6dof](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-joint-make-generic-6dof)(joint: [RID](class_rid.md#class-rid), body_A: [RID](class_rid.md#class-rid), local_ref_A: [Transform3D](class_transform3d.md#class-transform3d), body_B: [RID](class_rid.md#class-rid), local_ref_B: [Transform3D](class_transform3d.md#class-transform3d)) virtual required |
| void | [_joint_make_hinge](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-joint-make-hinge)(joint: [RID](class_rid.md#class-rid), body_A: [RID](class_rid.md#class-rid), hinge_A: [Transform3D](class_transform3d.md#class-transform3d), body_B: [RID](class_rid.md#class-rid), hinge_B: [Transform3D](class_transform3d.md#class-transform3d)) virtual required |
| void | [_joint_make_hinge_simple](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-joint-make-hinge-simple)(joint: [RID](class_rid.md#class-rid), body_A: [RID](class_rid.md#class-rid), pivot_A: [Vector3](class_vector3.md#class-vector3), axis_A: [Vector3](class_vector3.md#class-vector3), body_B: [RID](class_rid.md#class-rid), pivot_B: [Vector3](class_vector3.md#class-vector3), axis_B: [Vector3](class_vector3.md#class-vector3)) virtual required |
| void | [_joint_make_pin](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-joint-make-pin)(joint: [RID](class_rid.md#class-rid), body_A: [RID](class_rid.md#class-rid), local_A: [Vector3](class_vector3.md#class-vector3), body_B: [RID](class_rid.md#class-rid), local_B: [Vector3](class_vector3.md#class-vector3)) virtual required |
| void | [_joint_make_slider](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-joint-make-slider)(joint: [RID](class_rid.md#class-rid), body_A: [RID](class_rid.md#class-rid), local_ref_A: [Transform3D](class_transform3d.md#class-transform3d), body_B: [RID](class_rid.md#class-rid), local_ref_B: [Transform3D](class_transform3d.md#class-transform3d)) virtual required |
| void | [_joint_set_solver_priority](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-joint-set-solver-priority)(joint: [RID](class_rid.md#class-rid), priority: [int](class_int.md#class-int)) virtual required |
| [Vector3](class_vector3.md#class-vector3) | [_pin_joint_get_local_a](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-pin-joint-get-local-a)(joint: [RID](class_rid.md#class-rid)) virtual required const |
| [Vector3](class_vector3.md#class-vector3) | [_pin_joint_get_local_b](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-pin-joint-get-local-b)(joint: [RID](class_rid.md#class-rid)) virtual required const |
| [float](class_float.md#class-float) | [_pin_joint_get_param](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-pin-joint-get-param)(joint: [RID](class_rid.md#class-rid), param: [PinJointParam](class_physicsserver3d.md#enum-physicsserver3d-pinjointparam)) virtual required const |
| void | [_pin_joint_set_local_a](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-pin-joint-set-local-a)(joint: [RID](class_rid.md#class-rid), local_A: [Vector3](class_vector3.md#class-vector3)) virtual required |
| void | [_pin_joint_set_local_b](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-pin-joint-set-local-b)(joint: [RID](class_rid.md#class-rid), local_B: [Vector3](class_vector3.md#class-vector3)) virtual required |
| void | [_pin_joint_set_param](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-pin-joint-set-param)(joint: [RID](class_rid.md#class-rid), param: [PinJointParam](class_physicsserver3d.md#enum-physicsserver3d-pinjointparam), value: [float](class_float.md#class-float)) virtual required |
| [RID](class_rid.md#class-rid) | [_separation_ray_shape_create](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-separation-ray-shape-create)() virtual required |
| void | [_set_active](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-set-active)(active: [bool](class_bool.md#class-bool)) virtual required |
| [float](class_float.md#class-float) | [_shape_get_custom_solver_bias](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-shape-get-custom-solver-bias)(shape: [RID](class_rid.md#class-rid)) virtual required const |
| [Variant](class_variant.md#class-variant) | [_shape_get_data](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-shape-get-data)(shape: [RID](class_rid.md#class-rid)) virtual required const |
| [float](class_float.md#class-float) | [_shape_get_margin](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-shape-get-margin)(shape: [RID](class_rid.md#class-rid)) virtual required const |
| [ShapeType](class_physicsserver3d.md#enum-physicsserver3d-shapetype) | [_shape_get_type](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-shape-get-type)(shape: [RID](class_rid.md#class-rid)) virtual required const |
| void | [_shape_set_custom_solver_bias](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-shape-set-custom-solver-bias)(shape: [RID](class_rid.md#class-rid), bias: [float](class_float.md#class-float)) virtual required |
| void | [_shape_set_data](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-shape-set-data)(shape: [RID](class_rid.md#class-rid), data: [Variant](class_variant.md#class-variant)) virtual required |
| void | [_shape_set_margin](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-shape-set-margin)(shape: [RID](class_rid.md#class-rid), margin: [float](class_float.md#class-float)) virtual required |
| [float](class_float.md#class-float) | [_slider_joint_get_param](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-slider-joint-get-param)(joint: [RID](class_rid.md#class-rid), param: [SliderJointParam](class_physicsserver3d.md#enum-physicsserver3d-sliderjointparam)) virtual required const |
| void | [_slider_joint_set_param](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-slider-joint-set-param)(joint: [RID](class_rid.md#class-rid), param: [SliderJointParam](class_physicsserver3d.md#enum-physicsserver3d-sliderjointparam), value: [float](class_float.md#class-float)) virtual required |
| void | [_soft_body_add_collision_exception](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-add-collision-exception)(body: [RID](class_rid.md#class-rid), body_b: [RID](class_rid.md#class-rid)) virtual required |
| void | [_soft_body_apply_central_force](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-apply-central-force)(body: [RID](class_rid.md#class-rid), force: [Vector3](class_vector3.md#class-vector3)) virtual required |
| void | [_soft_body_apply_central_impulse](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-apply-central-impulse)(body: [RID](class_rid.md#class-rid), impulse: [Vector3](class_vector3.md#class-vector3)) virtual required |
| void | [_soft_body_apply_point_force](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-apply-point-force)(body: [RID](class_rid.md#class-rid), point_index: [int](class_int.md#class-int), force: [Vector3](class_vector3.md#class-vector3)) virtual required |
| void | [_soft_body_apply_point_impulse](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-apply-point-impulse)(body: [RID](class_rid.md#class-rid), point_index: [int](class_int.md#class-int), impulse: [Vector3](class_vector3.md#class-vector3)) virtual required |
| [RID](class_rid.md#class-rid) | [_soft_body_create](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-create)() virtual required |
| [AABB](class_aabb.md#class-aabb) | [_soft_body_get_bounds](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-get-bounds)(body: [RID](class_rid.md#class-rid)) virtual required const |
| [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] | [_soft_body_get_collision_exceptions](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-get-collision-exceptions)(body: [RID](class_rid.md#class-rid)) virtual required const |
| [int](class_int.md#class-int) | [_soft_body_get_collision_layer](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-get-collision-layer)(body: [RID](class_rid.md#class-rid)) virtual required const |
| [int](class_int.md#class-int) | [_soft_body_get_collision_mask](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-get-collision-mask)(body: [RID](class_rid.md#class-rid)) virtual required const |
| [float](class_float.md#class-float) | [_soft_body_get_damping_coefficient](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-get-damping-coefficient)(body: [RID](class_rid.md#class-rid)) virtual required const |
| [float](class_float.md#class-float) | [_soft_body_get_drag_coefficient](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-get-drag-coefficient)(body: [RID](class_rid.md#class-rid)) virtual required const |
| [float](class_float.md#class-float) | [_soft_body_get_linear_stiffness](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-get-linear-stiffness)(body: [RID](class_rid.md#class-rid)) virtual required const |
| [Vector3](class_vector3.md#class-vector3) | [_soft_body_get_point_global_position](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-get-point-global-position)(body: [RID](class_rid.md#class-rid), point_index: [int](class_int.md#class-int)) virtual required const |
| [float](class_float.md#class-float) | [_soft_body_get_pressure_coefficient](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-get-pressure-coefficient)(body: [RID](class_rid.md#class-rid)) virtual required const |
| [float](class_float.md#class-float) | [_soft_body_get_shrinking_factor](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-get-shrinking-factor)(body: [RID](class_rid.md#class-rid)) virtual required const |
| [int](class_int.md#class-int) | [_soft_body_get_simulation_precision](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-get-simulation-precision)(body: [RID](class_rid.md#class-rid)) virtual required const |
| [RID](class_rid.md#class-rid) | [_soft_body_get_space](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-get-space)(body: [RID](class_rid.md#class-rid)) virtual required const |
| [Variant](class_variant.md#class-variant) | [_soft_body_get_state](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-get-state)(body: [RID](class_rid.md#class-rid), state: [BodyState](class_physicsserver3d.md#enum-physicsserver3d-bodystate)) virtual required const |
| [float](class_float.md#class-float) | [_soft_body_get_total_mass](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-get-total-mass)(body: [RID](class_rid.md#class-rid)) virtual required const |
| [bool](class_bool.md#class-bool) | [_soft_body_is_point_pinned](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-is-point-pinned)(body: [RID](class_rid.md#class-rid), point_index: [int](class_int.md#class-int)) virtual required const |
| void | [_soft_body_move_point](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-move-point)(body: [RID](class_rid.md#class-rid), point_index: [int](class_int.md#class-int), global_position: [Vector3](class_vector3.md#class-vector3)) virtual required |
| void | [_soft_body_pin_point](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-pin-point)(body: [RID](class_rid.md#class-rid), point_index: [int](class_int.md#class-int), pin: [bool](class_bool.md#class-bool)) virtual required |
| void | [_soft_body_remove_all_pinned_points](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-remove-all-pinned-points)(body: [RID](class_rid.md#class-rid)) virtual required |
| void | [_soft_body_remove_collision_exception](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-remove-collision-exception)(body: [RID](class_rid.md#class-rid), body_b: [RID](class_rid.md#class-rid)) virtual required |
| void | [_soft_body_set_collision_layer](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-set-collision-layer)(body: [RID](class_rid.md#class-rid), layer: [int](class_int.md#class-int)) virtual required |
| void | [_soft_body_set_collision_mask](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-set-collision-mask)(body: [RID](class_rid.md#class-rid), mask: [int](class_int.md#class-int)) virtual required |
| void | [_soft_body_set_damping_coefficient](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-set-damping-coefficient)(body: [RID](class_rid.md#class-rid), damping_coefficient: [float](class_float.md#class-float)) virtual required |
| void | [_soft_body_set_drag_coefficient](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-set-drag-coefficient)(body: [RID](class_rid.md#class-rid), drag_coefficient: [float](class_float.md#class-float)) virtual required |
| void | [_soft_body_set_linear_stiffness](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-set-linear-stiffness)(body: [RID](class_rid.md#class-rid), linear_stiffness: [float](class_float.md#class-float)) virtual required |
| void | [_soft_body_set_mesh](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-set-mesh)(body: [RID](class_rid.md#class-rid), mesh: [RID](class_rid.md#class-rid)) virtual required |
| void | [_soft_body_set_pressure_coefficient](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-set-pressure-coefficient)(body: [RID](class_rid.md#class-rid), pressure_coefficient: [float](class_float.md#class-float)) virtual required |
| void | [_soft_body_set_ray_pickable](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-set-ray-pickable)(body: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool)) virtual required |
| void | [_soft_body_set_shrinking_factor](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-set-shrinking-factor)(body: [RID](class_rid.md#class-rid), shrinking_factor: [float](class_float.md#class-float)) virtual required |
| void | [_soft_body_set_simulation_precision](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-set-simulation-precision)(body: [RID](class_rid.md#class-rid), simulation_precision: [int](class_int.md#class-int)) virtual required |
| void | [_soft_body_set_space](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-set-space)(body: [RID](class_rid.md#class-rid), space: [RID](class_rid.md#class-rid)) virtual required |
| void | [_soft_body_set_state](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-set-state)(body: [RID](class_rid.md#class-rid), state: [BodyState](class_physicsserver3d.md#enum-physicsserver3d-bodystate), variant: [Variant](class_variant.md#class-variant)) virtual required |
| void | [_soft_body_set_total_mass](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-set-total-mass)(body: [RID](class_rid.md#class-rid), total_mass: [float](class_float.md#class-float)) virtual required |
| void | [_soft_body_set_transform](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-set-transform)(body: [RID](class_rid.md#class-rid), transform: [Transform3D](class_transform3d.md#class-transform3d)) virtual required |
| void | [_soft_body_update_rendering_server](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-update-rendering-server)(body: [RID](class_rid.md#class-rid), rendering_server_handler: [PhysicsServer3DRenderingServerHandler](class_physicsserver3drenderingserverhandler.md#class-physicsserver3drenderingserverhandler)) virtual required |
| [RID](class_rid.md#class-rid) | [_space_create](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-space-create)() virtual required |
| [int](class_int.md#class-int) | [_space_get_contact_count](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-space-get-contact-count)(space: [RID](class_rid.md#class-rid)) virtual required const |
| [PackedVector3Array](class_packedvector3array.md#class-packedvector3array) | [_space_get_contacts](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-space-get-contacts)(space: [RID](class_rid.md#class-rid)) virtual required const |
| [PhysicsDirectSpaceState3D](class_physicsdirectspacestate3d.md#class-physicsdirectspacestate3d) | [_space_get_direct_state](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-space-get-direct-state)(space: [RID](class_rid.md#class-rid)) virtual required |
| [float](class_float.md#class-float) | [_space_get_param](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-space-get-param)(space: [RID](class_rid.md#class-rid), param: [SpaceParameter](class_physicsserver3d.md#enum-physicsserver3d-spaceparameter)) virtual required const |
| [bool](class_bool.md#class-bool) | [_space_is_active](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-space-is-active)(space: [RID](class_rid.md#class-rid)) virtual required const |
| void | [_space_set_active](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-space-set-active)(space: [RID](class_rid.md#class-rid), active: [bool](class_bool.md#class-bool)) virtual required |
| void | [_space_set_debug_contacts](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-space-set-debug-contacts)(space: [RID](class_rid.md#class-rid), max_contacts: [int](class_int.md#class-int)) virtual required |
| void | [_space_set_param](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-space-set-param)(space: [RID](class_rid.md#class-rid), param: [SpaceParameter](class_physicsserver3d.md#enum-physicsserver3d-spaceparameter), value: [float](class_float.md#class-float)) virtual required |
| [RID](class_rid.md#class-rid) | [_sphere_shape_create](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-sphere-shape-create)() virtual required |
| void | [_step](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-step)(step: [float](class_float.md#class-float)) virtual required |
| void | [_sync](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-sync)() virtual required |
| [RID](class_rid.md#class-rid) | [_world_boundary_shape_create](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-world-boundary-shape-create)() virtual required |
| [bool](class_bool.md#class-bool) | [body_test_motion_is_excluding_body](class_physicsserver3dextension.md#class-physicsserver3dextension-method-body-test-motion-is-excluding-body)(body: [RID](class_rid.md#class-rid)) const |
| [bool](class_bool.md#class-bool) | [body_test_motion_is_excluding_object](class_physicsserver3dextension.md#class-physicsserver3dextension-method-body-test-motion-is-excluding-object)(object: [int](class_int.md#class-int)) const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-physicsserver3dextension-private-method-area-add-shape"></a>

void **_area_add_shape**(area: [RID](class_rid.md#class-rid), shape: [RID](class_rid.md#class-rid), transform: [Transform3D](class_transform3d.md#class-transform3d), disabled: [bool](class_bool.md#class-bool)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-add-shape)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-area-attach-object-instance-id"></a>

void **_area_attach_object_instance_id**(area: [RID](class_rid.md#class-rid), id: [int](class_int.md#class-int)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-attach-object-instance-id)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-area-clear-shapes"></a>

void **_area_clear_shapes**(area: [RID](class_rid.md#class-rid)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-clear-shapes)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-area-create"></a>

[RID](class_rid.md#class-rid) **_area_create**() virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-create)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-area-get-collision-layer"></a>

[int](class_int.md#class-int) **_area_get_collision_layer**(area: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-get-collision-layer)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-area-get-collision-mask"></a>

[int](class_int.md#class-int) **_area_get_collision_mask**(area: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-get-collision-mask)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-area-get-object-instance-id"></a>

[int](class_int.md#class-int) **_area_get_object_instance_id**(area: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-get-object-instance-id)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-area-get-param"></a>

[Variant](class_variant.md#class-variant) **_area_get_param**(area: [RID](class_rid.md#class-rid), param: [AreaParameter](class_physicsserver3d.md#enum-physicsserver3d-areaparameter)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-get-param)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-area-get-shape"></a>

[RID](class_rid.md#class-rid) **_area_get_shape**(area: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-get-shape)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-area-get-shape-count"></a>

[int](class_int.md#class-int) **_area_get_shape_count**(area: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-get-shape-count)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-area-get-shape-transform"></a>

[Transform3D](class_transform3d.md#class-transform3d) **_area_get_shape_transform**(area: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-get-shape-transform)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-area-get-space"></a>

[RID](class_rid.md#class-rid) **_area_get_space**(area: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-get-space)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-area-get-transform"></a>

[Transform3D](class_transform3d.md#class-transform3d) **_area_get_transform**(area: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-get-transform)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-area-remove-shape"></a>

void **_area_remove_shape**(area: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-remove-shape)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-area-set-area-monitor-callback"></a>

void **_area_set_area_monitor_callback**(area: [RID](class_rid.md#class-rid), callback: [Callable](class_callable.md#class-callable)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-set-area-monitor-callback)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-area-set-collision-layer"></a>

void **_area_set_collision_layer**(area: [RID](class_rid.md#class-rid), layer: [int](class_int.md#class-int)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-set-collision-layer)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-area-set-collision-mask"></a>

void **_area_set_collision_mask**(area: [RID](class_rid.md#class-rid), mask: [int](class_int.md#class-int)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-set-collision-mask)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-area-set-monitor-callback"></a>

void **_area_set_monitor_callback**(area: [RID](class_rid.md#class-rid), callback: [Callable](class_callable.md#class-callable)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-set-monitor-callback)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-area-set-monitorable"></a>

void **_area_set_monitorable**(area: [RID](class_rid.md#class-rid), monitorable: [bool](class_bool.md#class-bool)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-set-monitorable)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-area-set-param"></a>

void **_area_set_param**(area: [RID](class_rid.md#class-rid), param: [AreaParameter](class_physicsserver3d.md#enum-physicsserver3d-areaparameter), value: [Variant](class_variant.md#class-variant)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-set-param)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-area-set-ray-pickable"></a>

void **_area_set_ray_pickable**(area: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-set-ray-pickable)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-area-set-shape"></a>

void **_area_set_shape**(area: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int), shape: [RID](class_rid.md#class-rid)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-set-shape)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-area-set-shape-disabled"></a>

void **_area_set_shape_disabled**(area: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-set-shape-disabled)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-area-set-shape-transform"></a>

void **_area_set_shape_transform**(area: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int), transform: [Transform3D](class_transform3d.md#class-transform3d)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-set-shape-transform)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-area-set-space"></a>

void **_area_set_space**(area: [RID](class_rid.md#class-rid), space: [RID](class_rid.md#class-rid)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-set-space)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-area-set-transform"></a>

void **_area_set_transform**(area: [RID](class_rid.md#class-rid), transform: [Transform3D](class_transform3d.md#class-transform3d)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-area-set-transform)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-add-collision-exception"></a>

void **_body_add_collision_exception**(body: [RID](class_rid.md#class-rid), excepted_body: [RID](class_rid.md#class-rid)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-add-collision-exception)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-add-constant-central-force"></a>

void **_body_add_constant_central_force**(body: [RID](class_rid.md#class-rid), force: [Vector3](class_vector3.md#class-vector3)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-add-constant-central-force)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-add-constant-force"></a>

void **_body_add_constant_force**(body: [RID](class_rid.md#class-rid), force: [Vector3](class_vector3.md#class-vector3), position: [Vector3](class_vector3.md#class-vector3)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-add-constant-force)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-add-constant-torque"></a>

void **_body_add_constant_torque**(body: [RID](class_rid.md#class-rid), torque: [Vector3](class_vector3.md#class-vector3)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-add-constant-torque)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-add-shape"></a>

void **_body_add_shape**(body: [RID](class_rid.md#class-rid), shape: [RID](class_rid.md#class-rid), transform: [Transform3D](class_transform3d.md#class-transform3d), disabled: [bool](class_bool.md#class-bool)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-add-shape)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-apply-central-force"></a>

void **_body_apply_central_force**(body: [RID](class_rid.md#class-rid), force: [Vector3](class_vector3.md#class-vector3)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-apply-central-force)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-apply-central-impulse"></a>

void **_body_apply_central_impulse**(body: [RID](class_rid.md#class-rid), impulse: [Vector3](class_vector3.md#class-vector3)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-apply-central-impulse)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-apply-force"></a>

void **_body_apply_force**(body: [RID](class_rid.md#class-rid), force: [Vector3](class_vector3.md#class-vector3), position: [Vector3](class_vector3.md#class-vector3)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-apply-force)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-apply-impulse"></a>

void **_body_apply_impulse**(body: [RID](class_rid.md#class-rid), impulse: [Vector3](class_vector3.md#class-vector3), position: [Vector3](class_vector3.md#class-vector3)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-apply-impulse)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-apply-torque"></a>

void **_body_apply_torque**(body: [RID](class_rid.md#class-rid), torque: [Vector3](class_vector3.md#class-vector3)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-apply-torque)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-apply-torque-impulse"></a>

void **_body_apply_torque_impulse**(body: [RID](class_rid.md#class-rid), impulse: [Vector3](class_vector3.md#class-vector3)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-apply-torque-impulse)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-attach-object-instance-id"></a>

void **_body_attach_object_instance_id**(body: [RID](class_rid.md#class-rid), id: [int](class_int.md#class-int)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-attach-object-instance-id)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-clear-shapes"></a>

void **_body_clear_shapes**(body: [RID](class_rid.md#class-rid)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-clear-shapes)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-create"></a>

[RID](class_rid.md#class-rid) **_body_create**() virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-create)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-get-collision-exceptions"></a>

[Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] **_body_get_collision_exceptions**(body: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-get-collision-exceptions)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-get-collision-layer"></a>

[int](class_int.md#class-int) **_body_get_collision_layer**(body: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-get-collision-layer)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-get-collision-mask"></a>

[int](class_int.md#class-int) **_body_get_collision_mask**(body: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-get-collision-mask)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-get-collision-priority"></a>

[float](class_float.md#class-float) **_body_get_collision_priority**(body: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-get-collision-priority)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-get-constant-force"></a>

[Vector3](class_vector3.md#class-vector3) **_body_get_constant_force**(body: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-get-constant-force)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-get-constant-torque"></a>

[Vector3](class_vector3.md#class-vector3) **_body_get_constant_torque**(body: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-get-constant-torque)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-get-contacts-reported-depth-threshold"></a>

[float](class_float.md#class-float) **_body_get_contacts_reported_depth_threshold**(body: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-get-contacts-reported-depth-threshold)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-get-direct-state"></a>

[PhysicsDirectBodyState3D](class_physicsdirectbodystate3d.md#class-physicsdirectbodystate3d) **_body_get_direct_state**(body: [RID](class_rid.md#class-rid)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-get-direct-state)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-get-max-contacts-reported"></a>

[int](class_int.md#class-int) **_body_get_max_contacts_reported**(body: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-get-max-contacts-reported)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-get-mode"></a>

[BodyMode](class_physicsserver3d.md#enum-physicsserver3d-bodymode) **_body_get_mode**(body: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-get-mode)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-get-object-instance-id"></a>

[int](class_int.md#class-int) **_body_get_object_instance_id**(body: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-get-object-instance-id)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-get-param"></a>

[Variant](class_variant.md#class-variant) **_body_get_param**(body: [RID](class_rid.md#class-rid), param: [BodyParameter](class_physicsserver3d.md#enum-physicsserver3d-bodyparameter)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-get-param)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-get-shape"></a>

[RID](class_rid.md#class-rid) **_body_get_shape**(body: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-get-shape)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-get-shape-count"></a>

[int](class_int.md#class-int) **_body_get_shape_count**(body: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-get-shape-count)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-get-shape-transform"></a>

[Transform3D](class_transform3d.md#class-transform3d) **_body_get_shape_transform**(body: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-get-shape-transform)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-get-space"></a>

[RID](class_rid.md#class-rid) **_body_get_space**(body: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-get-space)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-get-state"></a>

[Variant](class_variant.md#class-variant) **_body_get_state**(body: [RID](class_rid.md#class-rid), state: [BodyState](class_physicsserver3d.md#enum-physicsserver3d-bodystate)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-get-state)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-get-user-flags"></a>

[int](class_int.md#class-int) **_body_get_user_flags**(body: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-get-user-flags)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-is-axis-locked"></a>

[bool](class_bool.md#class-bool) **_body_is_axis_locked**(body: [RID](class_rid.md#class-rid), axis: [BodyAxis](class_physicsserver3d.md#enum-physicsserver3d-bodyaxis)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-is-axis-locked)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-is-continuous-collision-detection-enabled"></a>

[bool](class_bool.md#class-bool) **_body_is_continuous_collision_detection_enabled**(body: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-is-continuous-collision-detection-enabled)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-is-omitting-force-integration"></a>

[bool](class_bool.md#class-bool) **_body_is_omitting_force_integration**(body: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-is-omitting-force-integration)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-remove-collision-exception"></a>

void **_body_remove_collision_exception**(body: [RID](class_rid.md#class-rid), excepted_body: [RID](class_rid.md#class-rid)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-remove-collision-exception)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-remove-shape"></a>

void **_body_remove_shape**(body: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-remove-shape)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-reset-mass-properties"></a>

void **_body_reset_mass_properties**(body: [RID](class_rid.md#class-rid)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-reset-mass-properties)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-set-axis-lock"></a>

void **_body_set_axis_lock**(body: [RID](class_rid.md#class-rid), axis: [BodyAxis](class_physicsserver3d.md#enum-physicsserver3d-bodyaxis), lock: [bool](class_bool.md#class-bool)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-axis-lock)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-set-axis-velocity"></a>

void **_body_set_axis_velocity**(body: [RID](class_rid.md#class-rid), axis_velocity: [Vector3](class_vector3.md#class-vector3)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-axis-velocity)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-set-collision-layer"></a>

void **_body_set_collision_layer**(body: [RID](class_rid.md#class-rid), layer: [int](class_int.md#class-int)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-collision-layer)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-set-collision-mask"></a>

void **_body_set_collision_mask**(body: [RID](class_rid.md#class-rid), mask: [int](class_int.md#class-int)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-collision-mask)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-set-collision-priority"></a>

void **_body_set_collision_priority**(body: [RID](class_rid.md#class-rid), priority: [float](class_float.md#class-float)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-collision-priority)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-set-constant-force"></a>

void **_body_set_constant_force**(body: [RID](class_rid.md#class-rid), force: [Vector3](class_vector3.md#class-vector3)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-constant-force)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-set-constant-torque"></a>

void **_body_set_constant_torque**(body: [RID](class_rid.md#class-rid), torque: [Vector3](class_vector3.md#class-vector3)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-constant-torque)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-set-contacts-reported-depth-threshold"></a>

void **_body_set_contacts_reported_depth_threshold**(body: [RID](class_rid.md#class-rid), threshold: [float](class_float.md#class-float)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-contacts-reported-depth-threshold)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-set-enable-continuous-collision-detection"></a>

void **_body_set_enable_continuous_collision_detection**(body: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-enable-continuous-collision-detection)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-set-force-integration-callback"></a>

void **_body_set_force_integration_callback**(body: [RID](class_rid.md#class-rid), callable: [Callable](class_callable.md#class-callable), userdata: [Variant](class_variant.md#class-variant)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-force-integration-callback)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-set-max-contacts-reported"></a>

void **_body_set_max_contacts_reported**(body: [RID](class_rid.md#class-rid), amount: [int](class_int.md#class-int)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-max-contacts-reported)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-set-mode"></a>

void **_body_set_mode**(body: [RID](class_rid.md#class-rid), mode: [BodyMode](class_physicsserver3d.md#enum-physicsserver3d-bodymode)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-mode)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-set-omit-force-integration"></a>

void **_body_set_omit_force_integration**(body: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-omit-force-integration)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-set-param"></a>

void **_body_set_param**(body: [RID](class_rid.md#class-rid), param: [BodyParameter](class_physicsserver3d.md#enum-physicsserver3d-bodyparameter), value: [Variant](class_variant.md#class-variant)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-param)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-set-ray-pickable"></a>

void **_body_set_ray_pickable**(body: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-ray-pickable)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-set-shape"></a>

void **_body_set_shape**(body: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int), shape: [RID](class_rid.md#class-rid)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-shape)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-set-shape-disabled"></a>

void **_body_set_shape_disabled**(body: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-shape-disabled)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-set-shape-transform"></a>

void **_body_set_shape_transform**(body: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int), transform: [Transform3D](class_transform3d.md#class-transform3d)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-shape-transform)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-set-space"></a>

void **_body_set_space**(body: [RID](class_rid.md#class-rid), space: [RID](class_rid.md#class-rid)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-space)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-set-state"></a>

void **_body_set_state**(body: [RID](class_rid.md#class-rid), state: [BodyState](class_physicsserver3d.md#enum-physicsserver3d-bodystate), value: [Variant](class_variant.md#class-variant)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-state)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-set-state-sync-callback"></a>

void **_body_set_state_sync_callback**(body: [RID](class_rid.md#class-rid), callable: [Callable](class_callable.md#class-callable)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-state-sync-callback)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-set-user-flags"></a>

void **_body_set_user_flags**(body: [RID](class_rid.md#class-rid), flags: [int](class_int.md#class-int)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-set-user-flags)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-body-test-motion"></a>

[bool](class_bool.md#class-bool) **_body_test_motion**(body: [RID](class_rid.md#class-rid), from: [Transform3D](class_transform3d.md#class-transform3d), motion: [Vector3](class_vector3.md#class-vector3), margin: [float](class_float.md#class-float), max_collisions: [int](class_int.md#class-int), collide_separation_ray: [bool](class_bool.md#class-bool), recovery_as_collision: [bool](class_bool.md#class-bool), r_result: `PhysicsServer3DExtensionMotionResult*`) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-body-test-motion)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-box-shape-create"></a>

[RID](class_rid.md#class-rid) **_box_shape_create**() virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-box-shape-create)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-capsule-shape-create"></a>

[RID](class_rid.md#class-rid) **_capsule_shape_create**() virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-capsule-shape-create)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-concave-polygon-shape-create"></a>

[RID](class_rid.md#class-rid) **_concave_polygon_shape_create**() virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-concave-polygon-shape-create)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-cone-twist-joint-get-param"></a>

[float](class_float.md#class-float) **_cone_twist_joint_get_param**(joint: [RID](class_rid.md#class-rid), param: [ConeTwistJointParam](class_physicsserver3d.md#enum-physicsserver3d-conetwistjointparam)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-cone-twist-joint-get-param)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-cone-twist-joint-set-param"></a>

void **_cone_twist_joint_set_param**(joint: [RID](class_rid.md#class-rid), param: [ConeTwistJointParam](class_physicsserver3d.md#enum-physicsserver3d-conetwistjointparam), value: [float](class_float.md#class-float)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-cone-twist-joint-set-param)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-convex-polygon-shape-create"></a>

[RID](class_rid.md#class-rid) **_convex_polygon_shape_create**() virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-convex-polygon-shape-create)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-custom-shape-create"></a>

[RID](class_rid.md#class-rid) **_custom_shape_create**() virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-custom-shape-create)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-cylinder-shape-create"></a>

[RID](class_rid.md#class-rid) **_cylinder_shape_create**() virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-cylinder-shape-create)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-end-sync"></a>

void **_end_sync**() virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-end-sync)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-finish"></a>

void **_finish**() virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-finish)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-flush-queries"></a>

void **_flush_queries**() virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-flush-queries)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-free-rid"></a>

void **_free_rid**(rid: [RID](class_rid.md#class-rid)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-free-rid)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-generic-6dof-joint-get-flag"></a>

[bool](class_bool.md#class-bool) **_generic_6dof_joint_get_flag**(joint: [RID](class_rid.md#class-rid), axis: [Axis](class_vector3.md#enum-vector3-axis), flag: [G6DOFJointAxisFlag](class_physicsserver3d.md#enum-physicsserver3d-g6dofjointaxisflag)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-generic-6dof-joint-get-flag)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-generic-6dof-joint-get-param"></a>

[float](class_float.md#class-float) **_generic_6dof_joint_get_param**(joint: [RID](class_rid.md#class-rid), axis: [Axis](class_vector3.md#enum-vector3-axis), param: [G6DOFJointAxisParam](class_physicsserver3d.md#enum-physicsserver3d-g6dofjointaxisparam)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-generic-6dof-joint-get-param)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-generic-6dof-joint-set-flag"></a>

void **_generic_6dof_joint_set_flag**(joint: [RID](class_rid.md#class-rid), axis: [Axis](class_vector3.md#enum-vector3-axis), flag: [G6DOFJointAxisFlag](class_physicsserver3d.md#enum-physicsserver3d-g6dofjointaxisflag), enable: [bool](class_bool.md#class-bool)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-generic-6dof-joint-set-flag)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-generic-6dof-joint-set-param"></a>

void **_generic_6dof_joint_set_param**(joint: [RID](class_rid.md#class-rid), axis: [Axis](class_vector3.md#enum-vector3-axis), param: [G6DOFJointAxisParam](class_physicsserver3d.md#enum-physicsserver3d-g6dofjointaxisparam), value: [float](class_float.md#class-float)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-generic-6dof-joint-set-param)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-get-process-info"></a>

[int](class_int.md#class-int) **_get_process_info**(process_info: [ProcessInfo](class_physicsserver3d.md#enum-physicsserver3d-processinfo)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-get-process-info)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-heightmap-shape-create"></a>

[RID](class_rid.md#class-rid) **_heightmap_shape_create**() virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-heightmap-shape-create)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-hinge-joint-get-flag"></a>

[bool](class_bool.md#class-bool) **_hinge_joint_get_flag**(joint: [RID](class_rid.md#class-rid), flag: [HingeJointFlag](class_physicsserver3d.md#enum-physicsserver3d-hingejointflag)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-hinge-joint-get-flag)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-hinge-joint-get-param"></a>

[float](class_float.md#class-float) **_hinge_joint_get_param**(joint: [RID](class_rid.md#class-rid), param: [HingeJointParam](class_physicsserver3d.md#enum-physicsserver3d-hingejointparam)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-hinge-joint-get-param)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-hinge-joint-set-flag"></a>

void **_hinge_joint_set_flag**(joint: [RID](class_rid.md#class-rid), flag: [HingeJointFlag](class_physicsserver3d.md#enum-physicsserver3d-hingejointflag), enabled: [bool](class_bool.md#class-bool)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-hinge-joint-set-flag)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-hinge-joint-set-param"></a>

void **_hinge_joint_set_param**(joint: [RID](class_rid.md#class-rid), param: [HingeJointParam](class_physicsserver3d.md#enum-physicsserver3d-hingejointparam), value: [float](class_float.md#class-float)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-hinge-joint-set-param)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-init"></a>

void **_init**() virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-init)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-is-flushing-queries"></a>

[bool](class_bool.md#class-bool) **_is_flushing_queries**() virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-is-flushing-queries)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-joint-clear"></a>

void **_joint_clear**(joint: [RID](class_rid.md#class-rid)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-joint-clear)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-joint-create"></a>

[RID](class_rid.md#class-rid) **_joint_create**() virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-joint-create)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-joint-disable-collisions-between-bodies"></a>

void **_joint_disable_collisions_between_bodies**(joint: [RID](class_rid.md#class-rid), disable: [bool](class_bool.md#class-bool)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-joint-disable-collisions-between-bodies)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-joint-get-solver-priority"></a>

[int](class_int.md#class-int) **_joint_get_solver_priority**(joint: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-joint-get-solver-priority)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-joint-get-type"></a>

[JointType](class_physicsserver3d.md#enum-physicsserver3d-jointtype) **_joint_get_type**(joint: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-joint-get-type)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-joint-is-disabled-collisions-between-bodies"></a>

[bool](class_bool.md#class-bool) **_joint_is_disabled_collisions_between_bodies**(joint: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-joint-is-disabled-collisions-between-bodies)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-joint-make-cone-twist"></a>

void **_joint_make_cone_twist**(joint: [RID](class_rid.md#class-rid), body_A: [RID](class_rid.md#class-rid), local_ref_A: [Transform3D](class_transform3d.md#class-transform3d), body_B: [RID](class_rid.md#class-rid), local_ref_B: [Transform3D](class_transform3d.md#class-transform3d)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-joint-make-cone-twist)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-joint-make-generic-6dof"></a>

void **_joint_make_generic_6dof**(joint: [RID](class_rid.md#class-rid), body_A: [RID](class_rid.md#class-rid), local_ref_A: [Transform3D](class_transform3d.md#class-transform3d), body_B: [RID](class_rid.md#class-rid), local_ref_B: [Transform3D](class_transform3d.md#class-transform3d)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-joint-make-generic-6dof)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-joint-make-hinge"></a>

void **_joint_make_hinge**(joint: [RID](class_rid.md#class-rid), body_A: [RID](class_rid.md#class-rid), hinge_A: [Transform3D](class_transform3d.md#class-transform3d), body_B: [RID](class_rid.md#class-rid), hinge_B: [Transform3D](class_transform3d.md#class-transform3d)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-joint-make-hinge)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-joint-make-hinge-simple"></a>

void **_joint_make_hinge_simple**(joint: [RID](class_rid.md#class-rid), body_A: [RID](class_rid.md#class-rid), pivot_A: [Vector3](class_vector3.md#class-vector3), axis_A: [Vector3](class_vector3.md#class-vector3), body_B: [RID](class_rid.md#class-rid), pivot_B: [Vector3](class_vector3.md#class-vector3), axis_B: [Vector3](class_vector3.md#class-vector3)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-joint-make-hinge-simple)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-joint-make-pin"></a>

void **_joint_make_pin**(joint: [RID](class_rid.md#class-rid), body_A: [RID](class_rid.md#class-rid), local_A: [Vector3](class_vector3.md#class-vector3), body_B: [RID](class_rid.md#class-rid), local_B: [Vector3](class_vector3.md#class-vector3)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-joint-make-pin)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-joint-make-slider"></a>

void **_joint_make_slider**(joint: [RID](class_rid.md#class-rid), body_A: [RID](class_rid.md#class-rid), local_ref_A: [Transform3D](class_transform3d.md#class-transform3d), body_B: [RID](class_rid.md#class-rid), local_ref_B: [Transform3D](class_transform3d.md#class-transform3d)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-joint-make-slider)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-joint-set-solver-priority"></a>

void **_joint_set_solver_priority**(joint: [RID](class_rid.md#class-rid), priority: [int](class_int.md#class-int)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-joint-set-solver-priority)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-pin-joint-get-local-a"></a>

[Vector3](class_vector3.md#class-vector3) **_pin_joint_get_local_a**(joint: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-pin-joint-get-local-a)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-pin-joint-get-local-b"></a>

[Vector3](class_vector3.md#class-vector3) **_pin_joint_get_local_b**(joint: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-pin-joint-get-local-b)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-pin-joint-get-param"></a>

[float](class_float.md#class-float) **_pin_joint_get_param**(joint: [RID](class_rid.md#class-rid), param: [PinJointParam](class_physicsserver3d.md#enum-physicsserver3d-pinjointparam)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-pin-joint-get-param)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-pin-joint-set-local-a"></a>

void **_pin_joint_set_local_a**(joint: [RID](class_rid.md#class-rid), local_A: [Vector3](class_vector3.md#class-vector3)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-pin-joint-set-local-a)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-pin-joint-set-local-b"></a>

void **_pin_joint_set_local_b**(joint: [RID](class_rid.md#class-rid), local_B: [Vector3](class_vector3.md#class-vector3)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-pin-joint-set-local-b)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-pin-joint-set-param"></a>

void **_pin_joint_set_param**(joint: [RID](class_rid.md#class-rid), param: [PinJointParam](class_physicsserver3d.md#enum-physicsserver3d-pinjointparam), value: [float](class_float.md#class-float)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-pin-joint-set-param)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-separation-ray-shape-create"></a>

[RID](class_rid.md#class-rid) **_separation_ray_shape_create**() virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-separation-ray-shape-create)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-set-active"></a>

void **_set_active**(active: [bool](class_bool.md#class-bool)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-set-active)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-shape-get-custom-solver-bias"></a>

[float](class_float.md#class-float) **_shape_get_custom_solver_bias**(shape: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-shape-get-custom-solver-bias)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-shape-get-data"></a>

[Variant](class_variant.md#class-variant) **_shape_get_data**(shape: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-shape-get-data)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-shape-get-margin"></a>

[float](class_float.md#class-float) **_shape_get_margin**(shape: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-shape-get-margin)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-shape-get-type"></a>

[ShapeType](class_physicsserver3d.md#enum-physicsserver3d-shapetype) **_shape_get_type**(shape: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-shape-get-type)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-shape-set-custom-solver-bias"></a>

void **_shape_set_custom_solver_bias**(shape: [RID](class_rid.md#class-rid), bias: [float](class_float.md#class-float)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-shape-set-custom-solver-bias)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-shape-set-data"></a>

void **_shape_set_data**(shape: [RID](class_rid.md#class-rid), data: [Variant](class_variant.md#class-variant)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-shape-set-data)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-shape-set-margin"></a>

void **_shape_set_margin**(shape: [RID](class_rid.md#class-rid), margin: [float](class_float.md#class-float)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-shape-set-margin)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-slider-joint-get-param"></a>

[float](class_float.md#class-float) **_slider_joint_get_param**(joint: [RID](class_rid.md#class-rid), param: [SliderJointParam](class_physicsserver3d.md#enum-physicsserver3d-sliderjointparam)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-slider-joint-get-param)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-slider-joint-set-param"></a>

void **_slider_joint_set_param**(joint: [RID](class_rid.md#class-rid), param: [SliderJointParam](class_physicsserver3d.md#enum-physicsserver3d-sliderjointparam), value: [float](class_float.md#class-float)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-slider-joint-set-param)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-soft-body-add-collision-exception"></a>

void **_soft_body_add_collision_exception**(body: [RID](class_rid.md#class-rid), body_b: [RID](class_rid.md#class-rid)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-add-collision-exception)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-soft-body-apply-central-force"></a>

void **_soft_body_apply_central_force**(body: [RID](class_rid.md#class-rid), force: [Vector3](class_vector3.md#class-vector3)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-apply-central-force)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-soft-body-apply-central-impulse"></a>

void **_soft_body_apply_central_impulse**(body: [RID](class_rid.md#class-rid), impulse: [Vector3](class_vector3.md#class-vector3)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-apply-central-impulse)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-soft-body-apply-point-force"></a>

void **_soft_body_apply_point_force**(body: [RID](class_rid.md#class-rid), point_index: [int](class_int.md#class-int), force: [Vector3](class_vector3.md#class-vector3)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-apply-point-force)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-soft-body-apply-point-impulse"></a>

void **_soft_body_apply_point_impulse**(body: [RID](class_rid.md#class-rid), point_index: [int](class_int.md#class-int), impulse: [Vector3](class_vector3.md#class-vector3)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-apply-point-impulse)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-soft-body-create"></a>

[RID](class_rid.md#class-rid) **_soft_body_create**() virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-create)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-soft-body-get-bounds"></a>

[AABB](class_aabb.md#class-aabb) **_soft_body_get_bounds**(body: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-get-bounds)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-soft-body-get-collision-exceptions"></a>

[Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] **_soft_body_get_collision_exceptions**(body: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-get-collision-exceptions)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-soft-body-get-collision-layer"></a>

[int](class_int.md#class-int) **_soft_body_get_collision_layer**(body: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-get-collision-layer)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-soft-body-get-collision-mask"></a>

[int](class_int.md#class-int) **_soft_body_get_collision_mask**(body: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-get-collision-mask)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-soft-body-get-damping-coefficient"></a>

[float](class_float.md#class-float) **_soft_body_get_damping_coefficient**(body: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-get-damping-coefficient)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-soft-body-get-drag-coefficient"></a>

[float](class_float.md#class-float) **_soft_body_get_drag_coefficient**(body: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-get-drag-coefficient)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-soft-body-get-linear-stiffness"></a>

[float](class_float.md#class-float) **_soft_body_get_linear_stiffness**(body: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-get-linear-stiffness)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-soft-body-get-point-global-position"></a>

[Vector3](class_vector3.md#class-vector3) **_soft_body_get_point_global_position**(body: [RID](class_rid.md#class-rid), point_index: [int](class_int.md#class-int)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-get-point-global-position)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-soft-body-get-pressure-coefficient"></a>

[float](class_float.md#class-float) **_soft_body_get_pressure_coefficient**(body: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-get-pressure-coefficient)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-soft-body-get-shrinking-factor"></a>

[float](class_float.md#class-float) **_soft_body_get_shrinking_factor**(body: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-get-shrinking-factor)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-soft-body-get-simulation-precision"></a>

[int](class_int.md#class-int) **_soft_body_get_simulation_precision**(body: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-get-simulation-precision)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-soft-body-get-space"></a>

[RID](class_rid.md#class-rid) **_soft_body_get_space**(body: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-get-space)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-soft-body-get-state"></a>

[Variant](class_variant.md#class-variant) **_soft_body_get_state**(body: [RID](class_rid.md#class-rid), state: [BodyState](class_physicsserver3d.md#enum-physicsserver3d-bodystate)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-get-state)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-soft-body-get-total-mass"></a>

[float](class_float.md#class-float) **_soft_body_get_total_mass**(body: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-get-total-mass)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-soft-body-is-point-pinned"></a>

[bool](class_bool.md#class-bool) **_soft_body_is_point_pinned**(body: [RID](class_rid.md#class-rid), point_index: [int](class_int.md#class-int)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-is-point-pinned)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-soft-body-move-point"></a>

void **_soft_body_move_point**(body: [RID](class_rid.md#class-rid), point_index: [int](class_int.md#class-int), global_position: [Vector3](class_vector3.md#class-vector3)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-move-point)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-soft-body-pin-point"></a>

void **_soft_body_pin_point**(body: [RID](class_rid.md#class-rid), point_index: [int](class_int.md#class-int), pin: [bool](class_bool.md#class-bool)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-pin-point)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-soft-body-remove-all-pinned-points"></a>

void **_soft_body_remove_all_pinned_points**(body: [RID](class_rid.md#class-rid)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-remove-all-pinned-points)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-soft-body-remove-collision-exception"></a>

void **_soft_body_remove_collision_exception**(body: [RID](class_rid.md#class-rid), body_b: [RID](class_rid.md#class-rid)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-remove-collision-exception)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-soft-body-set-collision-layer"></a>

void **_soft_body_set_collision_layer**(body: [RID](class_rid.md#class-rid), layer: [int](class_int.md#class-int)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-set-collision-layer)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-soft-body-set-collision-mask"></a>

void **_soft_body_set_collision_mask**(body: [RID](class_rid.md#class-rid), mask: [int](class_int.md#class-int)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-set-collision-mask)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-soft-body-set-damping-coefficient"></a>

void **_soft_body_set_damping_coefficient**(body: [RID](class_rid.md#class-rid), damping_coefficient: [float](class_float.md#class-float)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-set-damping-coefficient)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-soft-body-set-drag-coefficient"></a>

void **_soft_body_set_drag_coefficient**(body: [RID](class_rid.md#class-rid), drag_coefficient: [float](class_float.md#class-float)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-set-drag-coefficient)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-soft-body-set-linear-stiffness"></a>

void **_soft_body_set_linear_stiffness**(body: [RID](class_rid.md#class-rid), linear_stiffness: [float](class_float.md#class-float)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-set-linear-stiffness)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-soft-body-set-mesh"></a>

void **_soft_body_set_mesh**(body: [RID](class_rid.md#class-rid), mesh: [RID](class_rid.md#class-rid)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-set-mesh)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-soft-body-set-pressure-coefficient"></a>

void **_soft_body_set_pressure_coefficient**(body: [RID](class_rid.md#class-rid), pressure_coefficient: [float](class_float.md#class-float)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-set-pressure-coefficient)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-soft-body-set-ray-pickable"></a>

void **_soft_body_set_ray_pickable**(body: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-set-ray-pickable)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-soft-body-set-shrinking-factor"></a>

void **_soft_body_set_shrinking_factor**(body: [RID](class_rid.md#class-rid), shrinking_factor: [float](class_float.md#class-float)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-set-shrinking-factor)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-soft-body-set-simulation-precision"></a>

void **_soft_body_set_simulation_precision**(body: [RID](class_rid.md#class-rid), simulation_precision: [int](class_int.md#class-int)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-set-simulation-precision)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-soft-body-set-space"></a>

void **_soft_body_set_space**(body: [RID](class_rid.md#class-rid), space: [RID](class_rid.md#class-rid)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-set-space)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-soft-body-set-state"></a>

void **_soft_body_set_state**(body: [RID](class_rid.md#class-rid), state: [BodyState](class_physicsserver3d.md#enum-physicsserver3d-bodystate), variant: [Variant](class_variant.md#class-variant)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-set-state)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-soft-body-set-total-mass"></a>

void **_soft_body_set_total_mass**(body: [RID](class_rid.md#class-rid), total_mass: [float](class_float.md#class-float)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-set-total-mass)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-soft-body-set-transform"></a>

void **_soft_body_set_transform**(body: [RID](class_rid.md#class-rid), transform: [Transform3D](class_transform3d.md#class-transform3d)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-set-transform)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-soft-body-update-rendering-server"></a>

void **_soft_body_update_rendering_server**(body: [RID](class_rid.md#class-rid), rendering_server_handler: [PhysicsServer3DRenderingServerHandler](class_physicsserver3drenderingserverhandler.md#class-physicsserver3drenderingserverhandler)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-update-rendering-server)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-space-create"></a>

[RID](class_rid.md#class-rid) **_space_create**() virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-space-create)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-space-get-contact-count"></a>

[int](class_int.md#class-int) **_space_get_contact_count**(space: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-space-get-contact-count)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-space-get-contacts"></a>

[PackedVector3Array](class_packedvector3array.md#class-packedvector3array) **_space_get_contacts**(space: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-space-get-contacts)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-space-get-direct-state"></a>

[PhysicsDirectSpaceState3D](class_physicsdirectspacestate3d.md#class-physicsdirectspacestate3d) **_space_get_direct_state**(space: [RID](class_rid.md#class-rid)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-space-get-direct-state)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-space-get-param"></a>

[float](class_float.md#class-float) **_space_get_param**(space: [RID](class_rid.md#class-rid), param: [SpaceParameter](class_physicsserver3d.md#enum-physicsserver3d-spaceparameter)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-space-get-param)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-space-is-active"></a>

[bool](class_bool.md#class-bool) **_space_is_active**(space: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-space-is-active)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-space-set-active"></a>

void **_space_set_active**(space: [RID](class_rid.md#class-rid), active: [bool](class_bool.md#class-bool)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-space-set-active)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-space-set-debug-contacts"></a>

void **_space_set_debug_contacts**(space: [RID](class_rid.md#class-rid), max_contacts: [int](class_int.md#class-int)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-space-set-debug-contacts)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-space-set-param"></a>

void **_space_set_param**(space: [RID](class_rid.md#class-rid), param: [SpaceParameter](class_physicsserver3d.md#enum-physicsserver3d-spaceparameter), value: [float](class_float.md#class-float)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-space-set-param)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-sphere-shape-create"></a>

[RID](class_rid.md#class-rid) **_sphere_shape_create**() virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-sphere-shape-create)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-step"></a>

void **_step**(step: [float](class_float.md#class-float)) virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-step)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-sync"></a>

void **_sync**() virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-sync)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-private-method-world-boundary-shape-create"></a>

[RID](class_rid.md#class-rid) **_world_boundary_shape_create**() virtual required [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-world-boundary-shape-create)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-method-body-test-motion-is-excluding-body"></a>

[bool](class_bool.md#class-bool) **body_test_motion_is_excluding_body**(body: [RID](class_rid.md#class-rid)) const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-method-body-test-motion-is-excluding-body)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsserver3dextension-method-body-test-motion-is-excluding-object"></a>

[bool](class_bool.md#class-bool) **body_test_motion_is_excluding_object**(object: [int](class_int.md#class-int)) const [🔗](class_physicsserver3dextension.md#class-physicsserver3dextension-method-body-test-motion-is-excluding-object)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!
