> Source: https://docs.godotengine.org/en/4.7/classes/class_particleprocessmaterial.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="particleprocessmaterial"></a>

<a id="class-particleprocessmaterial"></a>

# ParticleProcessMaterial

**Inherits:** [Material](class_material.md#class-material) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Holds a particle configuration for [GPUParticles2D](class_gpuparticles2d.md#class-gpuparticles2d) or [GPUParticles3D](class_gpuparticles3d.md#class-gpuparticles3d) nodes.

<a id="description"></a>

## Description

**ParticleProcessMaterial** defines particle properties and behavior. It is used in the `process_material` of the [GPUParticles2D](class_gpuparticles2d.md#class-gpuparticles2d) and [GPUParticles3D](class_gpuparticles3d.md#class-gpuparticles3d) nodes. Some of this material's properties are applied to each particle when emitted, while others can have a [CurveTexture](class_curvetexture.md#class-curvetexture) or a [GradientTexture1D](class_gradienttexture1d.md#class-gradienttexture1d) applied to vary numerical or color values over the lifetime of the particle.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Texture2D](class_texture2d.md#class-texture2d) | [alpha_curve](class_particleprocessmaterial.md#class-particleprocessmaterial-property-alpha-curve) |  |
| [Texture2D](class_texture2d.md#class-texture2d) | [angle_curve](class_particleprocessmaterial.md#class-particleprocessmaterial-property-angle-curve) |  |
| [float](class_float.md#class-float) | [angle_max](class_particleprocessmaterial.md#class-particleprocessmaterial-property-angle-max) | `0.0` |
| [float](class_float.md#class-float) | [angle_min](class_particleprocessmaterial.md#class-particleprocessmaterial-property-angle-min) | `0.0` |
| [Texture2D](class_texture2d.md#class-texture2d) | [angular_velocity_curve](class_particleprocessmaterial.md#class-particleprocessmaterial-property-angular-velocity-curve) |  |
| [float](class_float.md#class-float) | [angular_velocity_max](class_particleprocessmaterial.md#class-particleprocessmaterial-property-angular-velocity-max) | `0.0` |
| [float](class_float.md#class-float) | [angular_velocity_min](class_particleprocessmaterial.md#class-particleprocessmaterial-property-angular-velocity-min) | `0.0` |
| [Texture2D](class_texture2d.md#class-texture2d) | [anim_offset_curve](class_particleprocessmaterial.md#class-particleprocessmaterial-property-anim-offset-curve) |  |
| [float](class_float.md#class-float) | [anim_offset_max](class_particleprocessmaterial.md#class-particleprocessmaterial-property-anim-offset-max) | `0.0` |
| [float](class_float.md#class-float) | [anim_offset_min](class_particleprocessmaterial.md#class-particleprocessmaterial-property-anim-offset-min) | `0.0` |
| [Texture2D](class_texture2d.md#class-texture2d) | [anim_speed_curve](class_particleprocessmaterial.md#class-particleprocessmaterial-property-anim-speed-curve) |  |
| [float](class_float.md#class-float) | [anim_speed_max](class_particleprocessmaterial.md#class-particleprocessmaterial-property-anim-speed-max) | `0.0` |
| [float](class_float.md#class-float) | [anim_speed_min](class_particleprocessmaterial.md#class-particleprocessmaterial-property-anim-speed-min) | `0.0` |
| [bool](class_bool.md#class-bool) | [attractor_interaction_enabled](class_particleprocessmaterial.md#class-particleprocessmaterial-property-attractor-interaction-enabled) | `true` |
| [float](class_float.md#class-float) | [collision_bounce](class_particleprocessmaterial.md#class-particleprocessmaterial-property-collision-bounce) |  |
| [float](class_float.md#class-float) | [collision_friction](class_particleprocessmaterial.md#class-particleprocessmaterial-property-collision-friction) |  |
| [CollisionMode](class_particleprocessmaterial.md#enum-particleprocessmaterial-collisionmode) | [collision_mode](class_particleprocessmaterial.md#class-particleprocessmaterial-property-collision-mode) | `0` |
| [bool](class_bool.md#class-bool) | [collision_use_scale](class_particleprocessmaterial.md#class-particleprocessmaterial-property-collision-use-scale) | `false` |
| [Color](class_color.md#class-color) | [color](class_particleprocessmaterial.md#class-particleprocessmaterial-property-color) | `Color(1, 1, 1, 1)` |
| [Texture2D](class_texture2d.md#class-texture2d) | [color_initial_ramp](class_particleprocessmaterial.md#class-particleprocessmaterial-property-color-initial-ramp) |  |
| [Texture2D](class_texture2d.md#class-texture2d) | [color_ramp](class_particleprocessmaterial.md#class-particleprocessmaterial-property-color-ramp) |  |
| [Texture2D](class_texture2d.md#class-texture2d) | [damping_curve](class_particleprocessmaterial.md#class-particleprocessmaterial-property-damping-curve) |  |
| [float](class_float.md#class-float) | [damping_max](class_particleprocessmaterial.md#class-particleprocessmaterial-property-damping-max) | `0.0` |
| [float](class_float.md#class-float) | [damping_min](class_particleprocessmaterial.md#class-particleprocessmaterial-property-damping-min) | `0.0` |
| [Vector3](class_vector3.md#class-vector3) | [direction](class_particleprocessmaterial.md#class-particleprocessmaterial-property-direction) | `Vector3(1, 0, 0)` |
| [Texture2D](class_texture2d.md#class-texture2d) | [directional_velocity_curve](class_particleprocessmaterial.md#class-particleprocessmaterial-property-directional-velocity-curve) |  |
| [float](class_float.md#class-float) | [directional_velocity_max](class_particleprocessmaterial.md#class-particleprocessmaterial-property-directional-velocity-max) |  |
| [float](class_float.md#class-float) | [directional_velocity_min](class_particleprocessmaterial.md#class-particleprocessmaterial-property-directional-velocity-min) |  |
| [Vector3](class_vector3.md#class-vector3) | [emission_box_extents](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-box-extents) |  |
| [Texture2D](class_texture2d.md#class-texture2d) | [emission_color_texture](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-color-texture) |  |
| [Texture2D](class_texture2d.md#class-texture2d) | [emission_curve](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-curve) |  |
| [Texture2D](class_texture2d.md#class-texture2d) | [emission_normal_texture](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-normal-texture) |  |
| [int](class_int.md#class-int) | [emission_point_count](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-point-count) |  |
| [Texture2D](class_texture2d.md#class-texture2d) | [emission_point_texture](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-point-texture) |  |
| [Vector3](class_vector3.md#class-vector3) | [emission_ring_axis](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-ring-axis) |  |
| [float](class_float.md#class-float) | [emission_ring_cone_angle](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-ring-cone-angle) |  |
| [float](class_float.md#class-float) | [emission_ring_height](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-ring-height) |  |
| [float](class_float.md#class-float) | [emission_ring_inner_radius](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-ring-inner-radius) |  |
| [float](class_float.md#class-float) | [emission_ring_radius](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-ring-radius) |  |
| [EmissionShape](class_particleprocessmaterial.md#enum-particleprocessmaterial-emissionshape) | [emission_shape](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-shape) | `0` |
| [Vector3](class_vector3.md#class-vector3) | [emission_shape_offset](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-shape-offset) | `Vector3(0, 0, 0)` |
| [Vector3](class_vector3.md#class-vector3) | [emission_shape_scale](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-shape-scale) | `Vector3(1, 1, 1)` |
| [float](class_float.md#class-float) | [emission_sphere_radius](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-sphere-radius) |  |
| [float](class_float.md#class-float) | [flatness](class_particleprocessmaterial.md#class-particleprocessmaterial-property-flatness) | `0.0` |
| [Vector3](class_vector3.md#class-vector3) | [gravity](class_particleprocessmaterial.md#class-particleprocessmaterial-property-gravity) | `Vector3(0, -9.8, 0)` |
| [Texture2D](class_texture2d.md#class-texture2d) | [hue_variation_curve](class_particleprocessmaterial.md#class-particleprocessmaterial-property-hue-variation-curve) |  |
| [float](class_float.md#class-float) | [hue_variation_max](class_particleprocessmaterial.md#class-particleprocessmaterial-property-hue-variation-max) | `0.0` |
| [float](class_float.md#class-float) | [hue_variation_min](class_particleprocessmaterial.md#class-particleprocessmaterial-property-hue-variation-min) | `0.0` |
| [float](class_float.md#class-float) | [inherit_velocity_ratio](class_particleprocessmaterial.md#class-particleprocessmaterial-property-inherit-velocity-ratio) | `0.0` |
| [float](class_float.md#class-float) | [initial_velocity_max](class_particleprocessmaterial.md#class-particleprocessmaterial-property-initial-velocity-max) | `0.0` |
| [float](class_float.md#class-float) | [initial_velocity_min](class_particleprocessmaterial.md#class-particleprocessmaterial-property-initial-velocity-min) | `0.0` |
| [float](class_float.md#class-float) | [lifetime_randomness](class_particleprocessmaterial.md#class-particleprocessmaterial-property-lifetime-randomness) | `0.0` |
| [Texture2D](class_texture2d.md#class-texture2d) | [linear_accel_curve](class_particleprocessmaterial.md#class-particleprocessmaterial-property-linear-accel-curve) |  |
| [float](class_float.md#class-float) | [linear_accel_max](class_particleprocessmaterial.md#class-particleprocessmaterial-property-linear-accel-max) | `0.0` |
| [float](class_float.md#class-float) | [linear_accel_min](class_particleprocessmaterial.md#class-particleprocessmaterial-property-linear-accel-min) | `0.0` |
| [Texture2D](class_texture2d.md#class-texture2d) | [orbit_velocity_curve](class_particleprocessmaterial.md#class-particleprocessmaterial-property-orbit-velocity-curve) |  |
| [float](class_float.md#class-float) | [orbit_velocity_max](class_particleprocessmaterial.md#class-particleprocessmaterial-property-orbit-velocity-max) | `0.0` |
| [float](class_float.md#class-float) | [orbit_velocity_min](class_particleprocessmaterial.md#class-particleprocessmaterial-property-orbit-velocity-min) | `0.0` |
| [bool](class_bool.md#class-bool) | [particle_flag_align_y](class_particleprocessmaterial.md#class-particleprocessmaterial-property-particle-flag-align-y) | `false` |
| [bool](class_bool.md#class-bool) | [particle_flag_damping_as_friction](class_particleprocessmaterial.md#class-particleprocessmaterial-property-particle-flag-damping-as-friction) | `false` |
| [bool](class_bool.md#class-bool) | [particle_flag_disable_z](class_particleprocessmaterial.md#class-particleprocessmaterial-property-particle-flag-disable-z) | `false` |
| [bool](class_bool.md#class-bool) | [particle_flag_inherit_emitter_scale](class_particleprocessmaterial.md#class-particleprocessmaterial-property-particle-flag-inherit-emitter-scale) | `false` |
| [bool](class_bool.md#class-bool) | [particle_flag_rotate_y](class_particleprocessmaterial.md#class-particleprocessmaterial-property-particle-flag-rotate-y) | `false` |
| [Texture2D](class_texture2d.md#class-texture2d) | [radial_accel_curve](class_particleprocessmaterial.md#class-particleprocessmaterial-property-radial-accel-curve) |  |
| [float](class_float.md#class-float) | [radial_accel_max](class_particleprocessmaterial.md#class-particleprocessmaterial-property-radial-accel-max) | `0.0` |
| [float](class_float.md#class-float) | [radial_accel_min](class_particleprocessmaterial.md#class-particleprocessmaterial-property-radial-accel-min) | `0.0` |
| [Texture2D](class_texture2d.md#class-texture2d) | [radial_velocity_curve](class_particleprocessmaterial.md#class-particleprocessmaterial-property-radial-velocity-curve) |  |
| [float](class_float.md#class-float) | [radial_velocity_max](class_particleprocessmaterial.md#class-particleprocessmaterial-property-radial-velocity-max) | `0.0` |
| [float](class_float.md#class-float) | [radial_velocity_min](class_particleprocessmaterial.md#class-particleprocessmaterial-property-radial-velocity-min) | `0.0` |
| [Vector3](class_vector3.md#class-vector3) | [rotation_3d_max](class_particleprocessmaterial.md#class-particleprocessmaterial-property-rotation-3d-max) |  |
| [Vector3](class_vector3.md#class-vector3) | [rotation_3d_min](class_particleprocessmaterial.md#class-particleprocessmaterial-property-rotation-3d-min) |  |
| [Texture2D](class_texture2d.md#class-texture2d) | [rotation_velocity_3d_curve](class_particleprocessmaterial.md#class-particleprocessmaterial-property-rotation-velocity-3d-curve) |  |
| [Vector3](class_vector3.md#class-vector3) | [rotation_velocity_3d_max](class_particleprocessmaterial.md#class-particleprocessmaterial-property-rotation-velocity-3d-max) |  |
| [Vector3](class_vector3.md#class-vector3) | [rotation_velocity_3d_min](class_particleprocessmaterial.md#class-particleprocessmaterial-property-rotation-velocity-3d-min) |  |
| [Vector3](class_vector3.md#class-vector3) | [scale_3d_max](class_particleprocessmaterial.md#class-particleprocessmaterial-property-scale-3d-max) |  |
| [Vector3](class_vector3.md#class-vector3) | [scale_3d_min](class_particleprocessmaterial.md#class-particleprocessmaterial-property-scale-3d-min) |  |
| [Texture2D](class_texture2d.md#class-texture2d) | [scale_curve](class_particleprocessmaterial.md#class-particleprocessmaterial-property-scale-curve) |  |
| [float](class_float.md#class-float) | [scale_max](class_particleprocessmaterial.md#class-particleprocessmaterial-property-scale-max) | `1.0` |
| [float](class_float.md#class-float) | [scale_min](class_particleprocessmaterial.md#class-particleprocessmaterial-property-scale-min) | `1.0` |
| [Texture2D](class_texture2d.md#class-texture2d) | [scale_over_velocity_curve](class_particleprocessmaterial.md#class-particleprocessmaterial-property-scale-over-velocity-curve) |  |
| [float](class_float.md#class-float) | [scale_over_velocity_max](class_particleprocessmaterial.md#class-particleprocessmaterial-property-scale-over-velocity-max) | `0.0` |
| [float](class_float.md#class-float) | [scale_over_velocity_min](class_particleprocessmaterial.md#class-particleprocessmaterial-property-scale-over-velocity-min) | `0.0` |
| [float](class_float.md#class-float) | [spread](class_particleprocessmaterial.md#class-particleprocessmaterial-property-spread) | `45.0` |
| [int](class_int.md#class-int) | [sub_emitter_amount_at_collision](class_particleprocessmaterial.md#class-particleprocessmaterial-property-sub-emitter-amount-at-collision) |  |
| [int](class_int.md#class-int) | [sub_emitter_amount_at_end](class_particleprocessmaterial.md#class-particleprocessmaterial-property-sub-emitter-amount-at-end) |  |
| [int](class_int.md#class-int) | [sub_emitter_amount_at_start](class_particleprocessmaterial.md#class-particleprocessmaterial-property-sub-emitter-amount-at-start) |  |
| [float](class_float.md#class-float) | [sub_emitter_frequency](class_particleprocessmaterial.md#class-particleprocessmaterial-property-sub-emitter-frequency) |  |
| [bool](class_bool.md#class-bool) | [sub_emitter_keep_velocity](class_particleprocessmaterial.md#class-particleprocessmaterial-property-sub-emitter-keep-velocity) | `false` |
| [SubEmitterMode](class_particleprocessmaterial.md#enum-particleprocessmaterial-subemittermode) | [sub_emitter_mode](class_particleprocessmaterial.md#class-particleprocessmaterial-property-sub-emitter-mode) | `0` |
| [Texture2D](class_texture2d.md#class-texture2d) | [tangential_accel_curve](class_particleprocessmaterial.md#class-particleprocessmaterial-property-tangential-accel-curve) |  |
| [float](class_float.md#class-float) | [tangential_accel_max](class_particleprocessmaterial.md#class-particleprocessmaterial-property-tangential-accel-max) | `0.0` |
| [float](class_float.md#class-float) | [tangential_accel_min](class_particleprocessmaterial.md#class-particleprocessmaterial-property-tangential-accel-min) | `0.0` |
| [bool](class_bool.md#class-bool) | [turbulence_enabled](class_particleprocessmaterial.md#class-particleprocessmaterial-property-turbulence-enabled) | `false` |
| [float](class_float.md#class-float) | [turbulence_influence_max](class_particleprocessmaterial.md#class-particleprocessmaterial-property-turbulence-influence-max) | `0.1` |
| [float](class_float.md#class-float) | [turbulence_influence_min](class_particleprocessmaterial.md#class-particleprocessmaterial-property-turbulence-influence-min) | `0.1` |
| [Texture2D](class_texture2d.md#class-texture2d) | [turbulence_influence_over_life](class_particleprocessmaterial.md#class-particleprocessmaterial-property-turbulence-influence-over-life) |  |
| [float](class_float.md#class-float) | [turbulence_initial_displacement_max](class_particleprocessmaterial.md#class-particleprocessmaterial-property-turbulence-initial-displacement-max) | `0.0` |
| [float](class_float.md#class-float) | [turbulence_initial_displacement_min](class_particleprocessmaterial.md#class-particleprocessmaterial-property-turbulence-initial-displacement-min) | `0.0` |
| [float](class_float.md#class-float) | [turbulence_noise_scale](class_particleprocessmaterial.md#class-particleprocessmaterial-property-turbulence-noise-scale) | `9.0` |
| [Vector3](class_vector3.md#class-vector3) | [turbulence_noise_speed](class_particleprocessmaterial.md#class-particleprocessmaterial-property-turbulence-noise-speed) | `Vector3(0, 0, 0)` |
| [float](class_float.md#class-float) | [turbulence_noise_speed_random](class_particleprocessmaterial.md#class-particleprocessmaterial-property-turbulence-noise-speed-random) | `0.2` |
| [float](class_float.md#class-float) | [turbulence_noise_strength](class_particleprocessmaterial.md#class-particleprocessmaterial-property-turbulence-noise-strength) | `1.0` |
| [bool](class_bool.md#class-bool) | [use_rotation_3d](class_particleprocessmaterial.md#class-particleprocessmaterial-property-use-rotation-3d) | `false` |
| [bool](class_bool.md#class-bool) | [use_rotation_velocity_3d](class_particleprocessmaterial.md#class-particleprocessmaterial-property-use-rotation-velocity-3d) | `false` |
| [bool](class_bool.md#class-bool) | [use_scale_3d](class_particleprocessmaterial.md#class-particleprocessmaterial-property-use-scale-3d) | `false` |
| [Texture2D](class_texture2d.md#class-texture2d) | [velocity_limit_curve](class_particleprocessmaterial.md#class-particleprocessmaterial-property-velocity-limit-curve) |  |
| [Vector3](class_vector3.md#class-vector3) | [velocity_pivot](class_particleprocessmaterial.md#class-particleprocessmaterial-property-velocity-pivot) | `Vector3(0, 0, 0)` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Vector2](class_vector2.md#class-vector2) | [get_param](class_particleprocessmaterial.md#class-particleprocessmaterial-method-get-param)(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const |
| [float](class_float.md#class-float) | [get_param_max](class_particleprocessmaterial.md#class-particleprocessmaterial-method-get-param-max)(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const |
| [float](class_float.md#class-float) | [get_param_min](class_particleprocessmaterial.md#class-particleprocessmaterial-method-get-param-min)(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const |
| [Texture2D](class_texture2d.md#class-texture2d) | [get_param_texture](class_particleprocessmaterial.md#class-particleprocessmaterial-method-get-param-texture)(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const |
| [bool](class_bool.md#class-bool) | [get_particle_flag](class_particleprocessmaterial.md#class-particleprocessmaterial-method-get-particle-flag)(particle_flag: [ParticleFlags](class_particleprocessmaterial.md#enum-particleprocessmaterial-particleflags)) const |
| void | [set_param](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param)(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), value: [Vector2](class_vector2.md#class-vector2)) |
| void | [set_param_max](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-max)(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), value: [float](class_float.md#class-float)) |
| void | [set_param_min](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-min)(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), value: [float](class_float.md#class-float)) |
| void | [set_param_texture](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-texture)(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), texture: [Texture2D](class_texture2d.md#class-texture2d)) |
| void | [set_particle_flag](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-particle-flag)(particle_flag: [ParticleFlags](class_particleprocessmaterial.md#enum-particleprocessmaterial-particleflags), enable: [bool](class_bool.md#class-bool)) |

---


<a id="signals"></a>

## Signals

<a id="class-particleprocessmaterial-signal-emission-shape-changed"></a>

**emission_shape_changed**() [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-signal-emission-shape-changed)

Emitted when this material's emission shape is changed in any way. This includes changes to [emission_shape](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-shape), [emission_shape_scale](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-shape-scale), or [emission_sphere_radius](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-sphere-radius), and any other property that affects the emission shape's offset, size, scale, or orientation.

**Note:** This signal is only emitted inside the editor for performance reasons.

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-particleprocessmaterial-parameter"></a>

enum **Parameter**: [🔗](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)

<a id="class-particleprocessmaterial-constant-param-initial-linear-velocity"></a>

[Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter) **PARAM_INITIAL_LINEAR_VELOCITY** = `0`

Use with [set_param_min()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-min), [set_param_max()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-max), and [set_param_texture()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-texture) to set initial velocity properties.

<a id="class-particleprocessmaterial-constant-param-angular-velocity"></a>

[Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter) **PARAM_ANGULAR_VELOCITY** = `1`

Use with [set_param_min()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-min), [set_param_max()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-max), and [set_param_texture()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-texture) to set angular velocity properties.

<a id="class-particleprocessmaterial-constant-param-orbit-velocity"></a>

[Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter) **PARAM_ORBIT_VELOCITY** = `2`

Use with [set_param_min()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-min), [set_param_max()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-max), and [set_param_texture()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-texture) to set orbital velocity properties.

<a id="class-particleprocessmaterial-constant-param-linear-accel"></a>

[Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter) **PARAM_LINEAR_ACCEL** = `3`

Use with [set_param_min()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-min), [set_param_max()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-max), and [set_param_texture()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-texture) to set linear acceleration properties.

<a id="class-particleprocessmaterial-constant-param-radial-accel"></a>

[Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter) **PARAM_RADIAL_ACCEL** = `4`

Use with [set_param_min()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-min), [set_param_max()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-max), and [set_param_texture()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-texture) to set radial acceleration properties.

<a id="class-particleprocessmaterial-constant-param-tangential-accel"></a>

[Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter) **PARAM_TANGENTIAL_ACCEL** = `5`

Use with [set_param_min()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-min), [set_param_max()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-max), and [set_param_texture()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-texture) to set tangential acceleration properties.

<a id="class-particleprocessmaterial-constant-param-damping"></a>

[Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter) **PARAM_DAMPING** = `6`

Use with [set_param_min()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-min), [set_param_max()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-max), and [set_param_texture()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-texture) to set damping properties.

<a id="class-particleprocessmaterial-constant-param-angle"></a>

[Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter) **PARAM_ANGLE** = `7`

Use with [set_param_min()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-min), [set_param_max()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-max), and [set_param_texture()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-texture) to set angle properties.

<a id="class-particleprocessmaterial-constant-param-scale"></a>

[Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter) **PARAM_SCALE** = `8`

Use with [set_param_min()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-min), [set_param_max()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-max), and [set_param_texture()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-texture) to set scale properties.

<a id="class-particleprocessmaterial-constant-param-hue-variation"></a>

[Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter) **PARAM_HUE_VARIATION** = `9`

Use with [set_param_min()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-min), [set_param_max()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-max), and [set_param_texture()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-texture) to set hue variation properties.

<a id="class-particleprocessmaterial-constant-param-anim-speed"></a>

[Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter) **PARAM_ANIM_SPEED** = `10`

Use with [set_param_min()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-min), [set_param_max()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-max), and [set_param_texture()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-texture) to set animation speed properties.

<a id="class-particleprocessmaterial-constant-param-anim-offset"></a>

[Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter) **PARAM_ANIM_OFFSET** = `11`

Use with [set_param_min()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-min), [set_param_max()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-max), and [set_param_texture()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-texture) to set animation offset properties.

<a id="class-particleprocessmaterial-constant-param-radial-velocity"></a>

[Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter) **PARAM_RADIAL_VELOCITY** = `15`

Use with [set_param_min()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-min), [set_param_max()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-max), and [set_param_texture()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-texture) to set radial velocity properties.

<a id="class-particleprocessmaterial-constant-param-directional-velocity"></a>

[Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter) **PARAM_DIRECTIONAL_VELOCITY** = `16`

Use with [set_param_min()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-min), [set_param_max()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-max), and [set_param_texture()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-texture) to set directional velocity properties.

<a id="class-particleprocessmaterial-constant-param-scale-over-velocity"></a>

[Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter) **PARAM_SCALE_OVER_VELOCITY** = `17`

Use with [set_param_min()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-min), [set_param_max()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-max), and [set_param_texture()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-texture) to set scale over velocity properties.

<a id="class-particleprocessmaterial-constant-param-max"></a>

[Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter) **PARAM_MAX** = `18`

Represents the size of the [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter) enum.

<a id="class-particleprocessmaterial-constant-param-turb-vel-influence"></a>

[Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter) **PARAM_TURB_VEL_INFLUENCE** = `13`

Use with [set_param_min()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-min) and [set_param_max()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-max) to set the turbulence minimum und maximum influence on each particles velocity.

<a id="class-particleprocessmaterial-constant-param-turb-init-displacement"></a>

[Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter) **PARAM_TURB_INIT_DISPLACEMENT** = `14`

Use with [set_param_min()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-min) and [set_param_max()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-max) to set the turbulence minimum and maximum displacement of the particles spawn position.

<a id="class-particleprocessmaterial-constant-param-turb-influence-over-life"></a>

[Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter) **PARAM_TURB_INFLUENCE_OVER_LIFE** = `12`

Use with [set_param_texture()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-texture) to set the turbulence influence over the particles life time.

---


<a id="enum-particleprocessmaterial-particleflags"></a>

enum **ParticleFlags**: [🔗](class_particleprocessmaterial.md#enum-particleprocessmaterial-particleflags)

<a id="class-particleprocessmaterial-constant-particle-flag-align-y-to-velocity"></a>

[ParticleFlags](class_particleprocessmaterial.md#enum-particleprocessmaterial-particleflags) **PARTICLE_FLAG_ALIGN_Y_TO_VELOCITY** = `0`

Use with [set_particle_flag()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-particle-flag) to set [particle_flag_align_y](class_particleprocessmaterial.md#class-particleprocessmaterial-property-particle-flag-align-y).

<a id="class-particleprocessmaterial-constant-particle-flag-rotate-y"></a>

[ParticleFlags](class_particleprocessmaterial.md#enum-particleprocessmaterial-particleflags) **PARTICLE_FLAG_ROTATE_Y** = `1`

Use with [set_particle_flag()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-particle-flag) to set [particle_flag_rotate_y](class_particleprocessmaterial.md#class-particleprocessmaterial-property-particle-flag-rotate-y).

<a id="class-particleprocessmaterial-constant-particle-flag-disable-z"></a>

[ParticleFlags](class_particleprocessmaterial.md#enum-particleprocessmaterial-particleflags) **PARTICLE_FLAG_DISABLE_Z** = `2`

Use with [set_particle_flag()](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-particle-flag) to set [particle_flag_disable_z](class_particleprocessmaterial.md#class-particleprocessmaterial-property-particle-flag-disable-z).

<a id="class-particleprocessmaterial-constant-particle-flag-damping-as-friction"></a>

[ParticleFlags](class_particleprocessmaterial.md#enum-particleprocessmaterial-particleflags) **PARTICLE_FLAG_DAMPING_AS_FRICTION** = `3`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="class-particleprocessmaterial-constant-particle-flag-inherit-emitter-scale"></a>

[ParticleFlags](class_particleprocessmaterial.md#enum-particleprocessmaterial-particleflags) **PARTICLE_FLAG_INHERIT_EMITTER_SCALE** = `4`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="class-particleprocessmaterial-constant-particle-flag-max"></a>

[ParticleFlags](class_particleprocessmaterial.md#enum-particleprocessmaterial-particleflags) **PARTICLE_FLAG_MAX** = `5`

Represents the size of the [ParticleFlags](class_particleprocessmaterial.md#enum-particleprocessmaterial-particleflags) enum.

---


<a id="enum-particleprocessmaterial-emissionshape"></a>

enum **EmissionShape**: [🔗](class_particleprocessmaterial.md#enum-particleprocessmaterial-emissionshape)

<a id="class-particleprocessmaterial-constant-emission-shape-point"></a>

[EmissionShape](class_particleprocessmaterial.md#enum-particleprocessmaterial-emissionshape) **EMISSION_SHAPE_POINT** = `0`

All particles will be emitted from a single point.

<a id="class-particleprocessmaterial-constant-emission-shape-sphere"></a>

[EmissionShape](class_particleprocessmaterial.md#enum-particleprocessmaterial-emissionshape) **EMISSION_SHAPE_SPHERE** = `1`

Particles will be emitted in the volume of a sphere.

<a id="class-particleprocessmaterial-constant-emission-shape-sphere-surface"></a>

[EmissionShape](class_particleprocessmaterial.md#enum-particleprocessmaterial-emissionshape) **EMISSION_SHAPE_SPHERE_SURFACE** = `2`

Particles will be emitted on the surface of a sphere.

<a id="class-particleprocessmaterial-constant-emission-shape-box"></a>

[EmissionShape](class_particleprocessmaterial.md#enum-particleprocessmaterial-emissionshape) **EMISSION_SHAPE_BOX** = `3`

Particles will be emitted in the volume of a box.

<a id="class-particleprocessmaterial-constant-emission-shape-points"></a>

[EmissionShape](class_particleprocessmaterial.md#enum-particleprocessmaterial-emissionshape) **EMISSION_SHAPE_POINTS** = `4`

Particles will be emitted at a position determined by sampling a random point on the [emission_point_texture](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-point-texture). Particle color will be modulated by [emission_color_texture](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-color-texture).

<a id="class-particleprocessmaterial-constant-emission-shape-directed-points"></a>

[EmissionShape](class_particleprocessmaterial.md#enum-particleprocessmaterial-emissionshape) **EMISSION_SHAPE_DIRECTED_POINTS** = `5`

Particles will be emitted at a position determined by sampling a random point on the [emission_point_texture](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-point-texture). Particle velocity and rotation will be set based on [emission_normal_texture](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-normal-texture). Particle color will be modulated by [emission_color_texture](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-color-texture).

<a id="class-particleprocessmaterial-constant-emission-shape-ring"></a>

[EmissionShape](class_particleprocessmaterial.md#enum-particleprocessmaterial-emissionshape) **EMISSION_SHAPE_RING** = `6`

Particles will be emitted in a ring or cylinder.

<a id="class-particleprocessmaterial-constant-emission-shape-max"></a>

[EmissionShape](class_particleprocessmaterial.md#enum-particleprocessmaterial-emissionshape) **EMISSION_SHAPE_MAX** = `7`

Represents the size of the [EmissionShape](class_particleprocessmaterial.md#enum-particleprocessmaterial-emissionshape) enum.

---


<a id="enum-particleprocessmaterial-subemittermode"></a>

enum **SubEmitterMode**: [🔗](class_particleprocessmaterial.md#enum-particleprocessmaterial-subemittermode)

<a id="class-particleprocessmaterial-constant-sub-emitter-disabled"></a>

[SubEmitterMode](class_particleprocessmaterial.md#enum-particleprocessmaterial-subemittermode) **SUB_EMITTER_DISABLED** = `0`

The subemitter is disabled.

<a id="class-particleprocessmaterial-constant-sub-emitter-constant"></a>

[SubEmitterMode](class_particleprocessmaterial.md#enum-particleprocessmaterial-subemittermode) **SUB_EMITTER_CONSTANT** = `1`

The submitter is emitted on the constant interval defined by [sub_emitter_frequency](class_particleprocessmaterial.md#class-particleprocessmaterial-property-sub-emitter-frequency).

<a id="class-particleprocessmaterial-constant-sub-emitter-at-end"></a>

[SubEmitterMode](class_particleprocessmaterial.md#enum-particleprocessmaterial-subemittermode) **SUB_EMITTER_AT_END** = `2`

The subemitter is emitted at the end of the particle's lifetime.

<a id="class-particleprocessmaterial-constant-sub-emitter-at-collision"></a>

[SubEmitterMode](class_particleprocessmaterial.md#enum-particleprocessmaterial-subemittermode) **SUB_EMITTER_AT_COLLISION** = `3`

The subemitter is emitted when the particle collides.

<a id="class-particleprocessmaterial-constant-sub-emitter-at-start"></a>

[SubEmitterMode](class_particleprocessmaterial.md#enum-particleprocessmaterial-subemittermode) **SUB_EMITTER_AT_START** = `4`

The subemitter is emitted when the particle spawns.

<a id="class-particleprocessmaterial-constant-sub-emitter-max"></a>

[SubEmitterMode](class_particleprocessmaterial.md#enum-particleprocessmaterial-subemittermode) **SUB_EMITTER_MAX** = `5`

Represents the size of the [SubEmitterMode](class_particleprocessmaterial.md#enum-particleprocessmaterial-subemittermode) enum.

---


<a id="enum-particleprocessmaterial-collisionmode"></a>

enum **CollisionMode**: [🔗](class_particleprocessmaterial.md#enum-particleprocessmaterial-collisionmode)

<a id="class-particleprocessmaterial-constant-collision-disabled"></a>

[CollisionMode](class_particleprocessmaterial.md#enum-particleprocessmaterial-collisionmode) **COLLISION_DISABLED** = `0`

No collision for particles. Particles will go through [GPUParticlesCollision3D](class_gpuparticlescollision3d.md#class-gpuparticlescollision3d) nodes.

<a id="class-particleprocessmaterial-constant-collision-rigid"></a>

[CollisionMode](class_particleprocessmaterial.md#enum-particleprocessmaterial-collisionmode) **COLLISION_RIGID** = `1`

[RigidBody3D](class_rigidbody3d.md#class-rigidbody3d)-style collision for particles using [GPUParticlesCollision3D](class_gpuparticlescollision3d.md#class-gpuparticlescollision3d) nodes.

<a id="class-particleprocessmaterial-constant-collision-hide-on-contact"></a>

[CollisionMode](class_particleprocessmaterial.md#enum-particleprocessmaterial-collisionmode) **COLLISION_HIDE_ON_CONTACT** = `2`

Hide particles instantly when colliding with a [GPUParticlesCollision3D](class_gpuparticlescollision3d.md#class-gpuparticlescollision3d) node. This can be combined with a subemitter that uses the [COLLISION_RIGID](class_particleprocessmaterial.md#class-particleprocessmaterial-constant-collision-rigid) collision mode to "replace" the parent particle with the subemitter on impact.

<a id="class-particleprocessmaterial-constant-collision-max"></a>

[CollisionMode](class_particleprocessmaterial.md#enum-particleprocessmaterial-collisionmode) **COLLISION_MAX** = `3`

Represents the size of the [CollisionMode](class_particleprocessmaterial.md#enum-particleprocessmaterial-collisionmode) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-particleprocessmaterial-property-alpha-curve"></a>

[Texture2D](class_texture2d.md#class-texture2d) **alpha_curve** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-alpha-curve)

- void **set_alpha_curve**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_alpha_curve**()

The alpha value of each particle's color will be multiplied by this [CurveTexture](class_curvetexture.md#class-curvetexture) over its lifetime.

**Note:** [alpha_curve](class_particleprocessmaterial.md#class-particleprocessmaterial-property-alpha-curve) multiplies the particle mesh's vertex colors. To have a visible effect on a [BaseMaterial3D](class_basematerial3d.md#class-basematerial3d), [BaseMaterial3D.vertex_color_use_as_albedo](class_basematerial3d.md#class-basematerial3d-property-vertex-color-use-as-albedo) *must* be `true`. For a [ShaderMaterial](class_shadermaterial.md#class-shadermaterial), `ALPHA *= COLOR.a;` must be inserted in the shader's `fragment()` function. Otherwise, [alpha_curve](class_particleprocessmaterial.md#class-particleprocessmaterial-property-alpha-curve) will have no visible effect.

---


<a id="class-particleprocessmaterial-property-angle-curve"></a>

[Texture2D](class_texture2d.md#class-texture2d) **angle_curve** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-angle-curve)

- void **set_param_texture**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), texture: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_param_texture**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Each particle's rotation will be animated along this [CurveTexture](class_curvetexture.md#class-curvetexture).

---


<a id="class-particleprocessmaterial-property-angle-max"></a>

[float](class_float.md#class-float) **angle_max** = `0.0` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-angle-max)

- void **set_param_max**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Maximum initial rotation applied to each particle, in degrees.

Only applied when [particle_flag_disable_z](class_particleprocessmaterial.md#class-particleprocessmaterial-property-particle-flag-disable-z) or [particle_flag_rotate_y](class_particleprocessmaterial.md#class-particleprocessmaterial-property-particle-flag-rotate-y) are `true` or the [BaseMaterial3D](class_basematerial3d.md#class-basematerial3d) being used to draw the particle is using [BaseMaterial3D.BILLBOARD_PARTICLES](class_basematerial3d.md#class-basematerial3d-constant-billboard-particles).

---


<a id="class-particleprocessmaterial-property-angle-min"></a>

[float](class_float.md#class-float) **angle_min** = `0.0` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-angle-min)

- void **set_param_min**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Minimum equivalent of [angle_max](class_particleprocessmaterial.md#class-particleprocessmaterial-property-angle-max).

---


<a id="class-particleprocessmaterial-property-angular-velocity-curve"></a>

[Texture2D](class_texture2d.md#class-texture2d) **angular_velocity_curve** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-angular-velocity-curve)

- void **set_param_texture**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), texture: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_param_texture**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Each particle's angular velocity (rotation speed) will vary along this [CurveTexture](class_curvetexture.md#class-curvetexture) over its lifetime.

---


<a id="class-particleprocessmaterial-property-angular-velocity-max"></a>

[float](class_float.md#class-float) **angular_velocity_max** = `0.0` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-angular-velocity-max)

- void **set_param_max**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Maximum initial angular velocity (rotation speed) applied to each particle in *degrees* per second.

Only applied when [particle_flag_disable_z](class_particleprocessmaterial.md#class-particleprocessmaterial-property-particle-flag-disable-z) or [particle_flag_rotate_y](class_particleprocessmaterial.md#class-particleprocessmaterial-property-particle-flag-rotate-y) are `true` or the [BaseMaterial3D](class_basematerial3d.md#class-basematerial3d) being used to draw the particle is using [BaseMaterial3D.BILLBOARD_PARTICLES](class_basematerial3d.md#class-basematerial3d-constant-billboard-particles).

---


<a id="class-particleprocessmaterial-property-angular-velocity-min"></a>

[float](class_float.md#class-float) **angular_velocity_min** = `0.0` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-angular-velocity-min)

- void **set_param_min**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Minimum equivalent of [angular_velocity_max](class_particleprocessmaterial.md#class-particleprocessmaterial-property-angular-velocity-max).

---


<a id="class-particleprocessmaterial-property-anim-offset-curve"></a>

[Texture2D](class_texture2d.md#class-texture2d) **anim_offset_curve** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-anim-offset-curve)

- void **set_param_texture**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), texture: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_param_texture**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Each particle's animation offset will vary along this [CurveTexture](class_curvetexture.md#class-curvetexture).

---


<a id="class-particleprocessmaterial-property-anim-offset-max"></a>

[float](class_float.md#class-float) **anim_offset_max** = `0.0` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-anim-offset-max)

- void **set_param_max**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Maximum animation offset that corresponds to frame index in the texture. `0` is the first frame, `1` is the last one. See [CanvasItemMaterial.particles_animation](class_canvasitemmaterial.md#class-canvasitemmaterial-property-particles-animation).

---


<a id="class-particleprocessmaterial-property-anim-offset-min"></a>

[float](class_float.md#class-float) **anim_offset_min** = `0.0` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-anim-offset-min)

- void **set_param_min**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Minimum equivalent of [anim_offset_max](class_particleprocessmaterial.md#class-particleprocessmaterial-property-anim-offset-max).

---


<a id="class-particleprocessmaterial-property-anim-speed-curve"></a>

[Texture2D](class_texture2d.md#class-texture2d) **anim_speed_curve** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-anim-speed-curve)

- void **set_param_texture**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), texture: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_param_texture**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Each particle's animation speed will vary along this [CurveTexture](class_curvetexture.md#class-curvetexture).

---


<a id="class-particleprocessmaterial-property-anim-speed-max"></a>

[float](class_float.md#class-float) **anim_speed_max** = `0.0` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-anim-speed-max)

- void **set_param_max**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Maximum particle animation speed. Animation speed of `1` means that the particles will make full `0` to `1` offset cycle during lifetime, `2` means `2` cycles etc.

With animation speed greater than `1`, remember to enable [CanvasItemMaterial.particles_anim_loop](class_canvasitemmaterial.md#class-canvasitemmaterial-property-particles-anim-loop) property if you want the animation to repeat.

---


<a id="class-particleprocessmaterial-property-anim-speed-min"></a>

[float](class_float.md#class-float) **anim_speed_min** = `0.0` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-anim-speed-min)

- void **set_param_min**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Minimum equivalent of [anim_speed_max](class_particleprocessmaterial.md#class-particleprocessmaterial-property-anim-speed-max).

---


<a id="class-particleprocessmaterial-property-attractor-interaction-enabled"></a>

[bool](class_bool.md#class-bool) **attractor_interaction_enabled** = `true` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-attractor-interaction-enabled)

- void **set_attractor_interaction_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_attractor_interaction_enabled**()

If `true`, interaction with particle attractors is enabled. In 3D, attraction only occurs within the area defined by the [GPUParticles3D](class_gpuparticles3d.md#class-gpuparticles3d) node's [GPUParticles3D.visibility_aabb](class_gpuparticles3d.md#class-gpuparticles3d-property-visibility-aabb).

---


<a id="class-particleprocessmaterial-property-collision-bounce"></a>

[float](class_float.md#class-float) **collision_bounce** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-collision-bounce)

- void **set_collision_bounce**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_collision_bounce**()

The particles' bounciness. Values range from `0` (no bounce) to `1` (full bounciness). Only effective if [collision_mode](class_particleprocessmaterial.md#class-particleprocessmaterial-property-collision-mode) is [COLLISION_RIGID](class_particleprocessmaterial.md#class-particleprocessmaterial-constant-collision-rigid).

---


<a id="class-particleprocessmaterial-property-collision-friction"></a>

[float](class_float.md#class-float) **collision_friction** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-collision-friction)

- void **set_collision_friction**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_collision_friction**()

The particles' friction. Values range from `0` (frictionless) to `1` (maximum friction). Only effective if [collision_mode](class_particleprocessmaterial.md#class-particleprocessmaterial-property-collision-mode) is [COLLISION_RIGID](class_particleprocessmaterial.md#class-particleprocessmaterial-constant-collision-rigid).

---


<a id="class-particleprocessmaterial-property-collision-mode"></a>

[CollisionMode](class_particleprocessmaterial.md#enum-particleprocessmaterial-collisionmode) **collision_mode** = `0` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-collision-mode)

- void **set_collision_mode**(value: [CollisionMode](class_particleprocessmaterial.md#enum-particleprocessmaterial-collisionmode))
- [CollisionMode](class_particleprocessmaterial.md#enum-particleprocessmaterial-collisionmode) **get_collision_mode**()

The particles' collision mode.

**Note:** 3D Particles can only collide with [GPUParticlesCollision3D](class_gpuparticlescollision3d.md#class-gpuparticlescollision3d) nodes, not [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d) nodes. To make particles collide with various objects, you can add [GPUParticlesCollision3D](class_gpuparticlescollision3d.md#class-gpuparticlescollision3d) nodes as children of [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d) nodes. In 3D, collisions only occur within the area defined by the [GPUParticles3D](class_gpuparticles3d.md#class-gpuparticles3d) node's [GPUParticles3D.visibility_aabb](class_gpuparticles3d.md#class-gpuparticles3d-property-visibility-aabb).

**Note:** 2D Particles can only collide with [LightOccluder2D](class_lightoccluder2d.md#class-lightoccluder2d) nodes, not [PhysicsBody2D](class_physicsbody2d.md#class-physicsbody2d) nodes.

---


<a id="class-particleprocessmaterial-property-collision-use-scale"></a>

[bool](class_bool.md#class-bool) **collision_use_scale** = `false` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-collision-use-scale)

- void **set_collision_use_scale**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_collision_using_scale**()

If `true`, [GPUParticles3D.collision_base_size](class_gpuparticles3d.md#class-gpuparticles3d-property-collision-base-size) is multiplied by the particle's effective scale (see [scale_min](class_particleprocessmaterial.md#class-particleprocessmaterial-property-scale-min), [scale_max](class_particleprocessmaterial.md#class-particleprocessmaterial-property-scale-max), [scale_curve](class_particleprocessmaterial.md#class-particleprocessmaterial-property-scale-curve), and [scale_over_velocity_curve](class_particleprocessmaterial.md#class-particleprocessmaterial-property-scale-over-velocity-curve)).

---


<a id="class-particleprocessmaterial-property-color"></a>

[Color](class_color.md#class-color) **color** = `Color(1, 1, 1, 1)` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-color)

- void **set_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_color**()

Each particle's initial color. If the [GPUParticles2D](class_gpuparticles2d.md#class-gpuparticles2d)'s `texture` is defined, it will be multiplied by this color.

**Note:** [color](class_particleprocessmaterial.md#class-particleprocessmaterial-property-color) multiplies the particle mesh's vertex colors. To have a visible effect on a [BaseMaterial3D](class_basematerial3d.md#class-basematerial3d), [BaseMaterial3D.vertex_color_use_as_albedo](class_basematerial3d.md#class-basematerial3d-property-vertex-color-use-as-albedo) *must* be `true`. For a [ShaderMaterial](class_shadermaterial.md#class-shadermaterial), `ALBEDO *= COLOR.rgb;` must be inserted in the shader's `fragment()` function. Otherwise, [color](class_particleprocessmaterial.md#class-particleprocessmaterial-property-color) will have no visible effect.

---


<a id="class-particleprocessmaterial-property-color-initial-ramp"></a>

[Texture2D](class_texture2d.md#class-texture2d) **color_initial_ramp** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-color-initial-ramp)

- void **set_color_initial_ramp**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_color_initial_ramp**()

Each particle's initial color will vary along this [GradientTexture1D](class_gradienttexture1d.md#class-gradienttexture1d) (multiplied with [color](class_particleprocessmaterial.md#class-particleprocessmaterial-property-color)).

**Note:** [color_initial_ramp](class_particleprocessmaterial.md#class-particleprocessmaterial-property-color-initial-ramp) multiplies the particle mesh's vertex colors. To have a visible effect on a [BaseMaterial3D](class_basematerial3d.md#class-basematerial3d), [BaseMaterial3D.vertex_color_use_as_albedo](class_basematerial3d.md#class-basematerial3d-property-vertex-color-use-as-albedo) *must* be `true`. For a [ShaderMaterial](class_shadermaterial.md#class-shadermaterial), `ALBEDO *= COLOR.rgb;` must be inserted in the shader's `fragment()` function. Otherwise, [color_initial_ramp](class_particleprocessmaterial.md#class-particleprocessmaterial-property-color-initial-ramp) will have no visible effect.

---


<a id="class-particleprocessmaterial-property-color-ramp"></a>

[Texture2D](class_texture2d.md#class-texture2d) **color_ramp** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-color-ramp)

- void **set_color_ramp**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_color_ramp**()

Each particle's color will vary along this [GradientTexture1D](class_gradienttexture1d.md#class-gradienttexture1d) over its lifetime (multiplied with [color](class_particleprocessmaterial.md#class-particleprocessmaterial-property-color)).

**Note:** [color_ramp](class_particleprocessmaterial.md#class-particleprocessmaterial-property-color-ramp) multiplies the particle mesh's vertex colors. To have a visible effect on a [BaseMaterial3D](class_basematerial3d.md#class-basematerial3d), [BaseMaterial3D.vertex_color_use_as_albedo](class_basematerial3d.md#class-basematerial3d-property-vertex-color-use-as-albedo) *must* be `true`. For a [ShaderMaterial](class_shadermaterial.md#class-shadermaterial), `ALBEDO *= COLOR.rgb;` must be inserted in the shader's `fragment()` function. Otherwise, [color_ramp](class_particleprocessmaterial.md#class-particleprocessmaterial-property-color-ramp) will have no visible effect.

---


<a id="class-particleprocessmaterial-property-damping-curve"></a>

[Texture2D](class_texture2d.md#class-texture2d) **damping_curve** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-damping-curve)

- void **set_param_texture**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), texture: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_param_texture**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Damping will vary along this [CurveTexture](class_curvetexture.md#class-curvetexture).

---


<a id="class-particleprocessmaterial-property-damping-max"></a>

[float](class_float.md#class-float) **damping_max** = `0.0` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-damping-max)

- void **set_param_max**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

The maximum rate at which particles lose velocity. For example value of `100` means that the particle will go from `100` velocity to `0` in `1` second.

---


<a id="class-particleprocessmaterial-property-damping-min"></a>

[float](class_float.md#class-float) **damping_min** = `0.0` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-damping-min)

- void **set_param_min**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Minimum equivalent of [damping_max](class_particleprocessmaterial.md#class-particleprocessmaterial-property-damping-max).

---


<a id="class-particleprocessmaterial-property-direction"></a>

[Vector3](class_vector3.md#class-vector3) **direction** = `Vector3(1, 0, 0)` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-direction)

- void **set_direction**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_direction**()

Unit vector specifying the particles' emission direction.

---


<a id="class-particleprocessmaterial-property-directional-velocity-curve"></a>

[Texture2D](class_texture2d.md#class-texture2d) **directional_velocity_curve** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-directional-velocity-curve)

- void **set_param_texture**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), texture: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_param_texture**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

A curve that specifies the velocity along each of the axes of the particle system along its lifetime.

**Note:** Animated velocities will not be affected by damping, use [velocity_limit_curve](class_particleprocessmaterial.md#class-particleprocessmaterial-property-velocity-limit-curve) instead.

---


<a id="class-particleprocessmaterial-property-directional-velocity-max"></a>

[float](class_float.md#class-float) **directional_velocity_max** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-directional-velocity-max)

- void **set_param_max**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Maximum directional velocity value, which is multiplied by [directional_velocity_curve](class_particleprocessmaterial.md#class-particleprocessmaterial-property-directional-velocity-curve).

**Note:** Animated velocities will not be affected by damping, use [velocity_limit_curve](class_particleprocessmaterial.md#class-particleprocessmaterial-property-velocity-limit-curve) instead.

---


<a id="class-particleprocessmaterial-property-directional-velocity-min"></a>

[float](class_float.md#class-float) **directional_velocity_min** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-directional-velocity-min)

- void **set_param_min**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Minimum directional velocity value, which is multiplied by [directional_velocity_curve](class_particleprocessmaterial.md#class-particleprocessmaterial-property-directional-velocity-curve).

**Note:** Animated velocities will not be affected by damping, use [velocity_limit_curve](class_particleprocessmaterial.md#class-particleprocessmaterial-property-velocity-limit-curve) instead.

---


<a id="class-particleprocessmaterial-property-emission-box-extents"></a>

[Vector3](class_vector3.md#class-vector3) **emission_box_extents** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-box-extents)

- void **set_emission_box_extents**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_emission_box_extents**()

The box's extents if [emission_shape](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-shape) is set to [EMISSION_SHAPE_BOX](class_particleprocessmaterial.md#class-particleprocessmaterial-constant-emission-shape-box).

**Note:** [emission_box_extents](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-box-extents) starts from the center point and applies the X, Y, and Z values in both directions. The size is twice the area of the extents.

---


<a id="class-particleprocessmaterial-property-emission-color-texture"></a>

[Texture2D](class_texture2d.md#class-texture2d) **emission_color_texture** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-color-texture)

- void **set_emission_color_texture**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_emission_color_texture**()

Particle color will be modulated by color determined by sampling this texture at the same point as the [emission_point_texture](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-point-texture).

**Note:** [emission_color_texture](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-color-texture) multiplies the particle mesh's vertex colors. To have a visible effect on a [BaseMaterial3D](class_basematerial3d.md#class-basematerial3d), [BaseMaterial3D.vertex_color_use_as_albedo](class_basematerial3d.md#class-basematerial3d-property-vertex-color-use-as-albedo) *must* be `true`. For a [ShaderMaterial](class_shadermaterial.md#class-shadermaterial), `ALBEDO *= COLOR.rgb;` must be inserted in the shader's `fragment()` function. Otherwise, [emission_color_texture](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-color-texture) will have no visible effect.

---


<a id="class-particleprocessmaterial-property-emission-curve"></a>

[Texture2D](class_texture2d.md#class-texture2d) **emission_curve** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-curve)

- void **set_emission_curve**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_emission_curve**()

Each particle's color will be multiplied by this [CurveTexture](class_curvetexture.md#class-curvetexture) over its lifetime.

**Note:** [emission_curve](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-curve) multiplies the particle mesh's vertex colors. To have a visible effect on a [BaseMaterial3D](class_basematerial3d.md#class-basematerial3d), [BaseMaterial3D.vertex_color_use_as_albedo](class_basematerial3d.md#class-basematerial3d-property-vertex-color-use-as-albedo) *must* be `true`. For a [ShaderMaterial](class_shadermaterial.md#class-shadermaterial), `ALBEDO *= COLOR.rgb;` must be inserted in the shader's `fragment()` function. Otherwise, [emission_curve](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-curve) will have no visible effect.

---


<a id="class-particleprocessmaterial-property-emission-normal-texture"></a>

[Texture2D](class_texture2d.md#class-texture2d) **emission_normal_texture** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-normal-texture)

- void **set_emission_normal_texture**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_emission_normal_texture**()

Particle velocity and rotation will be set by sampling this texture at the same point as the [emission_point_texture](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-point-texture). Used only in [EMISSION_SHAPE_DIRECTED_POINTS](class_particleprocessmaterial.md#class-particleprocessmaterial-constant-emission-shape-directed-points). Can be created automatically from mesh or node by selecting "Create Emission Points from Mesh/Node" under the "Particles" tool in the toolbar.

---


<a id="class-particleprocessmaterial-property-emission-point-count"></a>

[int](class_int.md#class-int) **emission_point_count** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-point-count)

- void **set_emission_point_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_emission_point_count**()

The number of emission points if [emission_shape](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-shape) is set to [EMISSION_SHAPE_POINTS](class_particleprocessmaterial.md#class-particleprocessmaterial-constant-emission-shape-points) or [EMISSION_SHAPE_DIRECTED_POINTS](class_particleprocessmaterial.md#class-particleprocessmaterial-constant-emission-shape-directed-points).

---


<a id="class-particleprocessmaterial-property-emission-point-texture"></a>

[Texture2D](class_texture2d.md#class-texture2d) **emission_point_texture** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-point-texture)

- void **set_emission_point_texture**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_emission_point_texture**()

Particles will be emitted at positions determined by sampling this texture at a random position. Used with [EMISSION_SHAPE_POINTS](class_particleprocessmaterial.md#class-particleprocessmaterial-constant-emission-shape-points) and [EMISSION_SHAPE_DIRECTED_POINTS](class_particleprocessmaterial.md#class-particleprocessmaterial-constant-emission-shape-directed-points). Can be created automatically from mesh or node by selecting "Create Emission Points from Mesh/Node" under the "Particles" tool in the toolbar.

---


<a id="class-particleprocessmaterial-property-emission-ring-axis"></a>

[Vector3](class_vector3.md#class-vector3) **emission_ring_axis** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-ring-axis)

- void **set_emission_ring_axis**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_emission_ring_axis**()

The axis of the ring when using the emitter [EMISSION_SHAPE_RING](class_particleprocessmaterial.md#class-particleprocessmaterial-constant-emission-shape-ring).

---


<a id="class-particleprocessmaterial-property-emission-ring-cone-angle"></a>

[float](class_float.md#class-float) **emission_ring_cone_angle** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-ring-cone-angle)

- void **set_emission_ring_cone_angle**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_emission_ring_cone_angle**()

The angle of the cone when using the emitter [EMISSION_SHAPE_RING](class_particleprocessmaterial.md#class-particleprocessmaterial-constant-emission-shape-ring). The default angle of 90 degrees results in a ring, while an angle of 0 degrees results in a cone. Intermediate values will result in a ring where one end is larger than the other.

**Note:** Depending on [emission_ring_height](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-ring-height), the angle may be clamped if the ring's end is reached to form a perfect cone.

---


<a id="class-particleprocessmaterial-property-emission-ring-height"></a>

[float](class_float.md#class-float) **emission_ring_height** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-ring-height)

- void **set_emission_ring_height**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_emission_ring_height**()

The height of the ring when using the emitter [EMISSION_SHAPE_RING](class_particleprocessmaterial.md#class-particleprocessmaterial-constant-emission-shape-ring).

---


<a id="class-particleprocessmaterial-property-emission-ring-inner-radius"></a>

[float](class_float.md#class-float) **emission_ring_inner_radius** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-ring-inner-radius)

- void **set_emission_ring_inner_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_emission_ring_inner_radius**()

The inner radius of the ring when using the emitter [EMISSION_SHAPE_RING](class_particleprocessmaterial.md#class-particleprocessmaterial-constant-emission-shape-ring).

---


<a id="class-particleprocessmaterial-property-emission-ring-radius"></a>

[float](class_float.md#class-float) **emission_ring_radius** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-ring-radius)

- void **set_emission_ring_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_emission_ring_radius**()

The radius of the ring when using the emitter [EMISSION_SHAPE_RING](class_particleprocessmaterial.md#class-particleprocessmaterial-constant-emission-shape-ring).

---


<a id="class-particleprocessmaterial-property-emission-shape"></a>

[EmissionShape](class_particleprocessmaterial.md#enum-particleprocessmaterial-emissionshape) **emission_shape** = `0` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-shape)

- void **set_emission_shape**(value: [EmissionShape](class_particleprocessmaterial.md#enum-particleprocessmaterial-emissionshape))
- [EmissionShape](class_particleprocessmaterial.md#enum-particleprocessmaterial-emissionshape) **get_emission_shape**()

Particles will be emitted inside this region.

---


<a id="class-particleprocessmaterial-property-emission-shape-offset"></a>

[Vector3](class_vector3.md#class-vector3) **emission_shape_offset** = `Vector3(0, 0, 0)` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-shape-offset)

- void **set_emission_shape_offset**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_emission_shape_offset**()

The offset for the [emission_shape](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-shape), in local space.

---


<a id="class-particleprocessmaterial-property-emission-shape-scale"></a>

[Vector3](class_vector3.md#class-vector3) **emission_shape_scale** = `Vector3(1, 1, 1)` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-shape-scale)

- void **set_emission_shape_scale**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_emission_shape_scale**()

The scale of the [emission_shape](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-shape), in local space.

---


<a id="class-particleprocessmaterial-property-emission-sphere-radius"></a>

[float](class_float.md#class-float) **emission_sphere_radius** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-sphere-radius)

- void **set_emission_sphere_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_emission_sphere_radius**()

The sphere's radius if [emission_shape](class_particleprocessmaterial.md#class-particleprocessmaterial-property-emission-shape) is set to [EMISSION_SHAPE_SPHERE](class_particleprocessmaterial.md#class-particleprocessmaterial-constant-emission-shape-sphere).

---


<a id="class-particleprocessmaterial-property-flatness"></a>

[float](class_float.md#class-float) **flatness** = `0.0` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-flatness)

- void **set_flatness**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_flatness**()

Amount of [spread](class_particleprocessmaterial.md#class-particleprocessmaterial-property-spread) along the Y axis.

---


<a id="class-particleprocessmaterial-property-gravity"></a>

[Vector3](class_vector3.md#class-vector3) **gravity** = `Vector3(0, -9.8, 0)` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-gravity)

- void **set_gravity**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_gravity**()

Gravity applied to every particle.

---


<a id="class-particleprocessmaterial-property-hue-variation-curve"></a>

[Texture2D](class_texture2d.md#class-texture2d) **hue_variation_curve** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-hue-variation-curve)

- void **set_param_texture**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), texture: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_param_texture**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Each particle's hue will vary along this [CurveTexture](class_curvetexture.md#class-curvetexture).

---


<a id="class-particleprocessmaterial-property-hue-variation-max"></a>

[float](class_float.md#class-float) **hue_variation_max** = `0.0` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-hue-variation-max)

- void **set_param_max**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Maximum initial hue variation applied to each particle. It will shift the particle color's hue.

---


<a id="class-particleprocessmaterial-property-hue-variation-min"></a>

[float](class_float.md#class-float) **hue_variation_min** = `0.0` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-hue-variation-min)

- void **set_param_min**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Minimum equivalent of [hue_variation_max](class_particleprocessmaterial.md#class-particleprocessmaterial-property-hue-variation-max).

---


<a id="class-particleprocessmaterial-property-inherit-velocity-ratio"></a>

[float](class_float.md#class-float) **inherit_velocity_ratio** = `0.0` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-inherit-velocity-ratio)

- void **set_inherit_velocity_ratio**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_inherit_velocity_ratio**()

Percentage of the velocity of the respective [GPUParticles2D](class_gpuparticles2d.md#class-gpuparticles2d) or [GPUParticles3D](class_gpuparticles3d.md#class-gpuparticles3d) inherited by each particle when spawning.

---


<a id="class-particleprocessmaterial-property-initial-velocity-max"></a>

[float](class_float.md#class-float) **initial_velocity_max** = `0.0` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-initial-velocity-max)

- void **set_param_max**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Maximum initial velocity magnitude for each particle. Direction comes from [direction](class_particleprocessmaterial.md#class-particleprocessmaterial-property-direction) and [spread](class_particleprocessmaterial.md#class-particleprocessmaterial-property-spread).

---


<a id="class-particleprocessmaterial-property-initial-velocity-min"></a>

[float](class_float.md#class-float) **initial_velocity_min** = `0.0` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-initial-velocity-min)

- void **set_param_min**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Minimum equivalent of [initial_velocity_max](class_particleprocessmaterial.md#class-particleprocessmaterial-property-initial-velocity-max).

---


<a id="class-particleprocessmaterial-property-lifetime-randomness"></a>

[float](class_float.md#class-float) **lifetime_randomness** = `0.0` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-lifetime-randomness)

- void **set_lifetime_randomness**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_lifetime_randomness**()

Particle lifetime randomness ratio. The equation for the lifetime of a particle is `lifetime * (1.0 - randf() * lifetime_randomness)`. For example, a [lifetime_randomness](class_particleprocessmaterial.md#class-particleprocessmaterial-property-lifetime-randomness) of `0.4` scales the lifetime between `0.6` to `1.0` of its original value.

---


<a id="class-particleprocessmaterial-property-linear-accel-curve"></a>

[Texture2D](class_texture2d.md#class-texture2d) **linear_accel_curve** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-linear-accel-curve)

- void **set_param_texture**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), texture: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_param_texture**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Each particle's linear acceleration will vary along this [CurveTexture](class_curvetexture.md#class-curvetexture).

---


<a id="class-particleprocessmaterial-property-linear-accel-max"></a>

[float](class_float.md#class-float) **linear_accel_max** = `0.0` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-linear-accel-max)

- void **set_param_max**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Maximum linear acceleration applied to each particle in the direction of motion.

---


<a id="class-particleprocessmaterial-property-linear-accel-min"></a>

[float](class_float.md#class-float) **linear_accel_min** = `0.0` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-linear-accel-min)

- void **set_param_min**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Minimum equivalent of [linear_accel_max](class_particleprocessmaterial.md#class-particleprocessmaterial-property-linear-accel-max).

---


<a id="class-particleprocessmaterial-property-orbit-velocity-curve"></a>

[Texture2D](class_texture2d.md#class-texture2d) **orbit_velocity_curve** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-orbit-velocity-curve)

- void **set_param_texture**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), texture: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_param_texture**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Each particle's orbital velocity will vary along this [CurveTexture](class_curvetexture.md#class-curvetexture).

**Note:** For 3D orbital velocity, use a [CurveXYZTexture](class_curvexyztexture.md#class-curvexyztexture).

**Note:** Animated velocities will not be affected by damping, use [velocity_limit_curve](class_particleprocessmaterial.md#class-particleprocessmaterial-property-velocity-limit-curve) instead.

---


<a id="class-particleprocessmaterial-property-orbit-velocity-max"></a>

[float](class_float.md#class-float) **orbit_velocity_max** = `0.0` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-orbit-velocity-max)

- void **set_param_max**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Maximum orbital velocity applied to each particle. Makes the particles circle around origin. Specified in number of full rotations around origin per second.

**Note:** Animated velocities will not be affected by damping, use [velocity_limit_curve](class_particleprocessmaterial.md#class-particleprocessmaterial-property-velocity-limit-curve) instead.

---


<a id="class-particleprocessmaterial-property-orbit-velocity-min"></a>

[float](class_float.md#class-float) **orbit_velocity_min** = `0.0` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-orbit-velocity-min)

- void **set_param_min**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Minimum equivalent of [orbit_velocity_max](class_particleprocessmaterial.md#class-particleprocessmaterial-property-orbit-velocity-max).

**Note:** Animated velocities will not be affected by damping, use [velocity_limit_curve](class_particleprocessmaterial.md#class-particleprocessmaterial-property-velocity-limit-curve) instead.

---


<a id="class-particleprocessmaterial-property-particle-flag-align-y"></a>

[bool](class_bool.md#class-bool) **particle_flag_align_y** = `false` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-particle-flag-align-y)

- void **set_particle_flag**(particle_flag: [ParticleFlags](class_particleprocessmaterial.md#enum-particleprocessmaterial-particleflags), enable: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_particle_flag**(particle_flag: [ParticleFlags](class_particleprocessmaterial.md#enum-particleprocessmaterial-particleflags)) const

Align Y axis of particle with the direction of its velocity.

---


<a id="class-particleprocessmaterial-property-particle-flag-damping-as-friction"></a>

[bool](class_bool.md#class-bool) **particle_flag_damping_as_friction** = `false` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-particle-flag-damping-as-friction)

- void **set_particle_flag**(particle_flag: [ParticleFlags](class_particleprocessmaterial.md#enum-particleprocessmaterial-particleflags), enable: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_particle_flag**(particle_flag: [ParticleFlags](class_particleprocessmaterial.md#enum-particleprocessmaterial-particleflags)) const

Changes the behavior of the damping properties from a linear deceleration to a deceleration based on speed percentage.

---


<a id="class-particleprocessmaterial-property-particle-flag-disable-z"></a>

[bool](class_bool.md#class-bool) **particle_flag_disable_z** = `false` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-particle-flag-disable-z)

- void **set_particle_flag**(particle_flag: [ParticleFlags](class_particleprocessmaterial.md#enum-particleprocessmaterial-particleflags), enable: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_particle_flag**(particle_flag: [ParticleFlags](class_particleprocessmaterial.md#enum-particleprocessmaterial-particleflags)) const

If `true`, particles will not move on the z axis.

---


<a id="class-particleprocessmaterial-property-particle-flag-inherit-emitter-scale"></a>

[bool](class_bool.md#class-bool) **particle_flag_inherit_emitter_scale** = `false` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-particle-flag-inherit-emitter-scale)

- void **set_particle_flag**(particle_flag: [ParticleFlags](class_particleprocessmaterial.md#enum-particleprocessmaterial-particleflags), enable: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_particle_flag**(particle_flag: [ParticleFlags](class_particleprocessmaterial.md#enum-particleprocessmaterial-particleflags)) const

If `true`, particles will inherit the scale of the emitter.

**Note:** This has no effect when [GPUParticles3D.local_coords](class_gpuparticles3d.md#class-gpuparticles3d-property-local-coords) is `true`, since particles in local space are already affected by the emitter's scale.

---


<a id="class-particleprocessmaterial-property-particle-flag-rotate-y"></a>

[bool](class_bool.md#class-bool) **particle_flag_rotate_y** = `false` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-particle-flag-rotate-y)

- void **set_particle_flag**(particle_flag: [ParticleFlags](class_particleprocessmaterial.md#enum-particleprocessmaterial-particleflags), enable: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_particle_flag**(particle_flag: [ParticleFlags](class_particleprocessmaterial.md#enum-particleprocessmaterial-particleflags)) const

If `true`, particles rotate around Y axis by [angle_min](class_particleprocessmaterial.md#class-particleprocessmaterial-property-angle-min).

---


<a id="class-particleprocessmaterial-property-radial-accel-curve"></a>

[Texture2D](class_texture2d.md#class-texture2d) **radial_accel_curve** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-radial-accel-curve)

- void **set_param_texture**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), texture: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_param_texture**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Each particle's radial acceleration will vary along this [CurveTexture](class_curvetexture.md#class-curvetexture).

---


<a id="class-particleprocessmaterial-property-radial-accel-max"></a>

[float](class_float.md#class-float) **radial_accel_max** = `0.0` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-radial-accel-max)

- void **set_param_max**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Maximum radial acceleration applied to each particle. Makes particle accelerate away from the origin or towards it if negative.

---


<a id="class-particleprocessmaterial-property-radial-accel-min"></a>

[float](class_float.md#class-float) **radial_accel_min** = `0.0` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-radial-accel-min)

- void **set_param_min**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Minimum equivalent of [radial_accel_max](class_particleprocessmaterial.md#class-particleprocessmaterial-property-radial-accel-max).

---


<a id="class-particleprocessmaterial-property-radial-velocity-curve"></a>

[Texture2D](class_texture2d.md#class-texture2d) **radial_velocity_curve** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-radial-velocity-curve)

- void **set_param_texture**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), texture: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_param_texture**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

A [CurveTexture](class_curvetexture.md#class-curvetexture) that defines the velocity over the particle's lifetime away (or toward) the [velocity_pivot](class_particleprocessmaterial.md#class-particleprocessmaterial-property-velocity-pivot).

**Note:** Animated velocities will not be affected by damping, use [velocity_limit_curve](class_particleprocessmaterial.md#class-particleprocessmaterial-property-velocity-limit-curve) instead.

---


<a id="class-particleprocessmaterial-property-radial-velocity-max"></a>

[float](class_float.md#class-float) **radial_velocity_max** = `0.0` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-radial-velocity-max)

- void **set_param_max**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Maximum radial velocity applied to each particle. Makes particles move away from the [velocity_pivot](class_particleprocessmaterial.md#class-particleprocessmaterial-property-velocity-pivot), or toward it if negative.

**Note:** Animated velocities will not be affected by damping, use [velocity_limit_curve](class_particleprocessmaterial.md#class-particleprocessmaterial-property-velocity-limit-curve) instead.

---


<a id="class-particleprocessmaterial-property-radial-velocity-min"></a>

[float](class_float.md#class-float) **radial_velocity_min** = `0.0` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-radial-velocity-min)

- void **set_param_min**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Minimum radial velocity applied to each particle. Makes particles move away from the [velocity_pivot](class_particleprocessmaterial.md#class-particleprocessmaterial-property-velocity-pivot), or toward it if negative.

**Note:** Animated velocities will not be affected by damping, use [velocity_limit_curve](class_particleprocessmaterial.md#class-particleprocessmaterial-property-velocity-limit-curve) instead.

---


<a id="class-particleprocessmaterial-property-rotation-3d-max"></a>

[Vector3](class_vector3.md#class-vector3) **rotation_3d_max** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-rotation-3d-max)

- void **set_rotation_3d_max**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_rotation_3d_max**()

The maximum 3D orientation, in degrees. Works only in 3D and if [use_rotation_3d](class_particleprocessmaterial.md#class-particleprocessmaterial-property-use-rotation-3d) is enabled.

---


<a id="class-particleprocessmaterial-property-rotation-3d-min"></a>

[Vector3](class_vector3.md#class-vector3) **rotation_3d_min** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-rotation-3d-min)

- void **set_rotation_3d_min**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_rotation_3d_min**()

The minimum 3D orientation, in degrees. Works only in 3D and if [use_rotation_3d](class_particleprocessmaterial.md#class-particleprocessmaterial-property-use-rotation-3d) is enabled.

---


<a id="class-particleprocessmaterial-property-rotation-velocity-3d-curve"></a>

[Texture2D](class_texture2d.md#class-texture2d) **rotation_velocity_3d_curve** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-rotation-velocity-3d-curve)

- void **set_rotation_velocity_3d_curve**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_rotation_velocity_3d_curve**()

Rotation velocity curve over lifetime, per-axis. Enable [use_rotation_velocity_3d](class_particleprocessmaterial.md#class-particleprocessmaterial-property-use-rotation-velocity-3d) to use this.

---


<a id="class-particleprocessmaterial-property-rotation-velocity-3d-max"></a>

[Vector3](class_vector3.md#class-vector3) **rotation_velocity_3d_max** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-rotation-velocity-3d-max)

- void **set_rotation_velocity_3d_max**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_rotation_velocity_3d_max**()

Maximum 3D rotation velocity on the particle's local axis. Enable [use_rotation_velocity_3d](class_particleprocessmaterial.md#class-particleprocessmaterial-property-use-rotation-velocity-3d) to use this.

---


<a id="class-particleprocessmaterial-property-rotation-velocity-3d-min"></a>

[Vector3](class_vector3.md#class-vector3) **rotation_velocity_3d_min** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-rotation-velocity-3d-min)

- void **set_rotation_velocity_3d_min**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_rotation_velocity_3d_min**()

Minimum 3D rotation velocity on the particle's local axis. Enable [use_rotation_velocity_3d](class_particleprocessmaterial.md#class-particleprocessmaterial-property-use-rotation-velocity-3d) to use this.

---


<a id="class-particleprocessmaterial-property-scale-3d-max"></a>

[Vector3](class_vector3.md#class-vector3) **scale_3d_max** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-scale-3d-max)

- void **set_scale_3d_max**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_scale_3d_max**()

The maximum value of the random scale vector for each particle.

Works only if [use_scale_3d](class_particleprocessmaterial.md#class-particleprocessmaterial-property-use-scale-3d) is enabled.

---


<a id="class-particleprocessmaterial-property-scale-3d-min"></a>

[Vector3](class_vector3.md#class-vector3) **scale_3d_min** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-scale-3d-min)

- void **set_scale_3d_min**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_scale_3d_min**()

The minimum value of the random scale vector for each particle.

Works only if [use_scale_3d](class_particleprocessmaterial.md#class-particleprocessmaterial-property-use-scale-3d) is enabled.

---


<a id="class-particleprocessmaterial-property-scale-curve"></a>

[Texture2D](class_texture2d.md#class-texture2d) **scale_curve** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-scale-curve)

- void **set_param_texture**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), texture: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_param_texture**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Each particle's scale will vary along this [CurveTexture](class_curvetexture.md#class-curvetexture) over its lifetime. If a [CurveXYZTexture](class_curvexyztexture.md#class-curvexyztexture) is supplied instead, the scale will be separated per-axis.

---


<a id="class-particleprocessmaterial-property-scale-max"></a>

[float](class_float.md#class-float) **scale_max** = `1.0` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-scale-max)

- void **set_param_max**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Maximum initial scale applied to each particle.

---


<a id="class-particleprocessmaterial-property-scale-min"></a>

[float](class_float.md#class-float) **scale_min** = `1.0` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-scale-min)

- void **set_param_min**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Minimum equivalent of [scale_max](class_particleprocessmaterial.md#class-particleprocessmaterial-property-scale-max).

---


<a id="class-particleprocessmaterial-property-scale-over-velocity-curve"></a>

[Texture2D](class_texture2d.md#class-texture2d) **scale_over_velocity_curve** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-scale-over-velocity-curve)

- void **set_param_texture**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), texture: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_param_texture**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Either a [CurveTexture](class_curvetexture.md#class-curvetexture) or a [CurveXYZTexture](class_curvexyztexture.md#class-curvexyztexture) that scales each particle based on its velocity.

---


<a id="class-particleprocessmaterial-property-scale-over-velocity-max"></a>

[float](class_float.md#class-float) **scale_over_velocity_max** = `0.0` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-scale-over-velocity-max)

- void **set_param_max**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Maximum velocity value reference for [scale_over_velocity_curve](class_particleprocessmaterial.md#class-particleprocessmaterial-property-scale-over-velocity-curve).

[scale_over_velocity_curve](class_particleprocessmaterial.md#class-particleprocessmaterial-property-scale-over-velocity-curve) will be interpolated between [scale_over_velocity_min](class_particleprocessmaterial.md#class-particleprocessmaterial-property-scale-over-velocity-min) and [scale_over_velocity_max](class_particleprocessmaterial.md#class-particleprocessmaterial-property-scale-over-velocity-max).

---


<a id="class-particleprocessmaterial-property-scale-over-velocity-min"></a>

[float](class_float.md#class-float) **scale_over_velocity_min** = `0.0` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-scale-over-velocity-min)

- void **set_param_min**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Minimum velocity value reference for [scale_over_velocity_curve](class_particleprocessmaterial.md#class-particleprocessmaterial-property-scale-over-velocity-curve).

[scale_over_velocity_curve](class_particleprocessmaterial.md#class-particleprocessmaterial-property-scale-over-velocity-curve) will be interpolated between [scale_over_velocity_min](class_particleprocessmaterial.md#class-particleprocessmaterial-property-scale-over-velocity-min) and [scale_over_velocity_max](class_particleprocessmaterial.md#class-particleprocessmaterial-property-scale-over-velocity-max).

---


<a id="class-particleprocessmaterial-property-spread"></a>

[float](class_float.md#class-float) **spread** = `45.0` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-spread)

- void **set_spread**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_spread**()

Each particle's initial direction range from `+spread` to `-spread` degrees.

---


<a id="class-particleprocessmaterial-property-sub-emitter-amount-at-collision"></a>

[int](class_int.md#class-int) **sub_emitter_amount_at_collision** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-sub-emitter-amount-at-collision)

- void **set_sub_emitter_amount_at_collision**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_sub_emitter_amount_at_collision**()

The amount of particles to spawn from the subemitter node when a collision occurs. When combined with [COLLISION_HIDE_ON_CONTACT](class_particleprocessmaterial.md#class-particleprocessmaterial-constant-collision-hide-on-contact) on the main particles material, this can be used to achieve effects such as raindrops hitting the ground.

**Note:** This value shouldn't exceed [GPUParticles2D.amount](class_gpuparticles2d.md#class-gpuparticles2d-property-amount) or [GPUParticles3D.amount](class_gpuparticles3d.md#class-gpuparticles3d-property-amount) defined on the *subemitter node* (not the main node), relative to the subemitter's particle lifetime. If the number of particles is exceeded, no new particles will spawn from the subemitter until enough particles have expired.

---


<a id="class-particleprocessmaterial-property-sub-emitter-amount-at-end"></a>

[int](class_int.md#class-int) **sub_emitter_amount_at_end** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-sub-emitter-amount-at-end)

- void **set_sub_emitter_amount_at_end**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_sub_emitter_amount_at_end**()

The amount of particles to spawn from the subemitter node when the particle expires.

**Note:** This value shouldn't exceed [GPUParticles2D.amount](class_gpuparticles2d.md#class-gpuparticles2d-property-amount) or [GPUParticles3D.amount](class_gpuparticles3d.md#class-gpuparticles3d-property-amount) defined on the *subemitter node* (not the main node), relative to the subemitter's particle lifetime. If the number of particles is exceeded, no new particles will spawn from the subemitter until enough particles have expired.

---


<a id="class-particleprocessmaterial-property-sub-emitter-amount-at-start"></a>

[int](class_int.md#class-int) **sub_emitter_amount_at_start** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-sub-emitter-amount-at-start)

- void **set_sub_emitter_amount_at_start**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_sub_emitter_amount_at_start**()

The amount of particles to spawn from the subemitter node when the particle spawns.

**Note:** This value shouldn't exceed [GPUParticles2D.amount](class_gpuparticles2d.md#class-gpuparticles2d-property-amount) or [GPUParticles3D.amount](class_gpuparticles3d.md#class-gpuparticles3d-property-amount) defined on the *subemitter node* (not the main node), relative to the subemitter's particle lifetime. If the number of particles is exceeded, no new particles will spawn from the subemitter until enough particles have expired.

---


<a id="class-particleprocessmaterial-property-sub-emitter-frequency"></a>

[float](class_float.md#class-float) **sub_emitter_frequency** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-sub-emitter-frequency)

- void **set_sub_emitter_frequency**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_sub_emitter_frequency**()

The frequency at which particles should be emitted from the subemitter node. One particle will be spawned every [sub_emitter_frequency](class_particleprocessmaterial.md#class-particleprocessmaterial-property-sub-emitter-frequency) seconds.

**Note:** This value shouldn't exceed [GPUParticles2D.amount](class_gpuparticles2d.md#class-gpuparticles2d-property-amount) or [GPUParticles3D.amount](class_gpuparticles3d.md#class-gpuparticles3d-property-amount) defined on the *subemitter node* (not the main node), relative to the subemitter's particle lifetime. If the number of particles is exceeded, no new particles will spawn from the subemitter until enough particles have expired.

---


<a id="class-particleprocessmaterial-property-sub-emitter-keep-velocity"></a>

[bool](class_bool.md#class-bool) **sub_emitter_keep_velocity** = `false` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-sub-emitter-keep-velocity)

- void **set_sub_emitter_keep_velocity**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_sub_emitter_keep_velocity**()

If `true`, the subemitter inherits the parent particle's velocity when it spawns.

---


<a id="class-particleprocessmaterial-property-sub-emitter-mode"></a>

[SubEmitterMode](class_particleprocessmaterial.md#enum-particleprocessmaterial-subemittermode) **sub_emitter_mode** = `0` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-sub-emitter-mode)

- void **set_sub_emitter_mode**(value: [SubEmitterMode](class_particleprocessmaterial.md#enum-particleprocessmaterial-subemittermode))
- [SubEmitterMode](class_particleprocessmaterial.md#enum-particleprocessmaterial-subemittermode) **get_sub_emitter_mode**()

The particle subemitter mode (see [GPUParticles2D.sub_emitter](class_gpuparticles2d.md#class-gpuparticles2d-property-sub-emitter) and [GPUParticles3D.sub_emitter](class_gpuparticles3d.md#class-gpuparticles3d-property-sub-emitter)).

---


<a id="class-particleprocessmaterial-property-tangential-accel-curve"></a>

[Texture2D](class_texture2d.md#class-texture2d) **tangential_accel_curve** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-tangential-accel-curve)

- void **set_param_texture**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), texture: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_param_texture**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Each particle's tangential acceleration will vary along this [CurveTexture](class_curvetexture.md#class-curvetexture).

---


<a id="class-particleprocessmaterial-property-tangential-accel-max"></a>

[float](class_float.md#class-float) **tangential_accel_max** = `0.0` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-tangential-accel-max)

- void **set_param_max**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Maximum tangential acceleration applied to each particle. Tangential acceleration is perpendicular to the particle's velocity giving the particles a swirling motion.

---


<a id="class-particleprocessmaterial-property-tangential-accel-min"></a>

[float](class_float.md#class-float) **tangential_accel_min** = `0.0` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-tangential-accel-min)

- void **set_param_min**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Minimum equivalent of [tangential_accel_max](class_particleprocessmaterial.md#class-particleprocessmaterial-property-tangential-accel-max).

---


<a id="class-particleprocessmaterial-property-turbulence-enabled"></a>

[bool](class_bool.md#class-bool) **turbulence_enabled** = `false` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-turbulence-enabled)

- void **set_turbulence_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_turbulence_enabled**()

If `true`, enables turbulence for the particle system. Turbulence can be used to vary particle movement according to its position (based on a 3D noise pattern). In 3D, [GPUParticlesAttractorVectorField3D](class_gpuparticlesattractorvectorfield3d.md#class-gpuparticlesattractorvectorfield3d) with [NoiseTexture3D](class_noisetexture3d.md#class-noisetexture3d) can be used as an alternative to turbulence that works in world space and with multiple particle systems reacting in the same way.

**Note:** Enabling turbulence has a high performance cost on the GPU. Only enable turbulence on a few particle systems at once at most, and consider disabling it when targeting mobile/web platforms.

---


<a id="class-particleprocessmaterial-property-turbulence-influence-max"></a>

[float](class_float.md#class-float) **turbulence_influence_max** = `0.1` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-turbulence-influence-max)

- void **set_param_max**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Maximum turbulence influence on each particle.

The actual amount of turbulence influence on each particle is calculated as a random value between [turbulence_influence_min](class_particleprocessmaterial.md#class-particleprocessmaterial-property-turbulence-influence-min) and [turbulence_influence_max](class_particleprocessmaterial.md#class-particleprocessmaterial-property-turbulence-influence-max) and multiplied by the amount of turbulence influence from [turbulence_influence_over_life](class_particleprocessmaterial.md#class-particleprocessmaterial-property-turbulence-influence-over-life).

---


<a id="class-particleprocessmaterial-property-turbulence-influence-min"></a>

[float](class_float.md#class-float) **turbulence_influence_min** = `0.1` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-turbulence-influence-min)

- void **set_param_min**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Minimum turbulence influence on each particle.

The actual amount of turbulence influence on each particle is calculated as a random value between [turbulence_influence_min](class_particleprocessmaterial.md#class-particleprocessmaterial-property-turbulence-influence-min) and [turbulence_influence_max](class_particleprocessmaterial.md#class-particleprocessmaterial-property-turbulence-influence-max) and multiplied by the amount of turbulence influence from [turbulence_influence_over_life](class_particleprocessmaterial.md#class-particleprocessmaterial-property-turbulence-influence-over-life).

---


<a id="class-particleprocessmaterial-property-turbulence-influence-over-life"></a>

[Texture2D](class_texture2d.md#class-texture2d) **turbulence_influence_over_life** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-turbulence-influence-over-life)

- void **set_param_texture**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), texture: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_param_texture**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Each particle's amount of turbulence will be influenced along this [CurveTexture](class_curvetexture.md#class-curvetexture) over its life time.

---


<a id="class-particleprocessmaterial-property-turbulence-initial-displacement-max"></a>

[float](class_float.md#class-float) **turbulence_initial_displacement_max** = `0.0` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-turbulence-initial-displacement-max)

- void **set_param_max**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Maximum displacement of each particle's spawn position by the turbulence.

The actual amount of displacement will be a factor of the underlying turbulence multiplied by a random value between [turbulence_initial_displacement_min](class_particleprocessmaterial.md#class-particleprocessmaterial-property-turbulence-initial-displacement-min) and [turbulence_initial_displacement_max](class_particleprocessmaterial.md#class-particleprocessmaterial-property-turbulence-initial-displacement-max).

---


<a id="class-particleprocessmaterial-property-turbulence-initial-displacement-min"></a>

[float](class_float.md#class-float) **turbulence_initial_displacement_min** = `0.0` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-turbulence-initial-displacement-min)

- void **set_param_min**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const

Minimum displacement of each particle's spawn position by the turbulence.

The actual amount of displacement will be a factor of the underlying turbulence multiplied by a random value between [turbulence_initial_displacement_min](class_particleprocessmaterial.md#class-particleprocessmaterial-property-turbulence-initial-displacement-min) and [turbulence_initial_displacement_max](class_particleprocessmaterial.md#class-particleprocessmaterial-property-turbulence-initial-displacement-max).

---


<a id="class-particleprocessmaterial-property-turbulence-noise-scale"></a>

[float](class_float.md#class-float) **turbulence_noise_scale** = `9.0` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-turbulence-noise-scale)

- void **set_turbulence_noise_scale**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_turbulence_noise_scale**()

This value controls the overall scale/frequency of the turbulence noise pattern.

A small scale will result in smaller features with more detail while a high scale will result in smoother noise with larger features.

---


<a id="class-particleprocessmaterial-property-turbulence-noise-speed"></a>

[Vector3](class_vector3.md#class-vector3) **turbulence_noise_speed** = `Vector3(0, 0, 0)` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-turbulence-noise-speed)

- void **set_turbulence_noise_speed**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_turbulence_noise_speed**()

A scrolling velocity for the turbulence field. This sets a directional trend for the pattern to move in over time.

The default value of `Vector3(0, 0, 0)` turns off the scrolling.

---


<a id="class-particleprocessmaterial-property-turbulence-noise-speed-random"></a>

[float](class_float.md#class-float) **turbulence_noise_speed_random** = `0.2` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-turbulence-noise-speed-random)

- void **set_turbulence_noise_speed_random**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_turbulence_noise_speed_random**()

The in-place rate of change of the turbulence field. This defines how quickly the noise pattern varies over time.

A value of 0.0 will result in a fixed pattern.

---


<a id="class-particleprocessmaterial-property-turbulence-noise-strength"></a>

[float](class_float.md#class-float) **turbulence_noise_strength** = `1.0` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-turbulence-noise-strength)

- void **set_turbulence_noise_strength**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_turbulence_noise_strength**()

The turbulence noise strength. Increasing this will result in a stronger, more contrasting, flow pattern.

---


<a id="class-particleprocessmaterial-property-use-rotation-3d"></a>

[bool](class_bool.md#class-bool) **use_rotation_3d** = `false` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-use-rotation-3d)

- void **set_use_rotation_3d**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_using_rotation_3d**()

Enable the usage of [rotation_3d_min](class_particleprocessmaterial.md#class-particleprocessmaterial-property-rotation-3d-min) and [rotation_3d_max](class_particleprocessmaterial.md#class-particleprocessmaterial-property-rotation-3d-max).

---


<a id="class-particleprocessmaterial-property-use-rotation-velocity-3d"></a>

[bool](class_bool.md#class-bool) **use_rotation_velocity_3d** = `false` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-use-rotation-velocity-3d)

- void **set_using_rotation_velocity_3d**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_using_rotation_velocity_3d**()

Enable 3D rotation velocity.

---


<a id="class-particleprocessmaterial-property-use-scale-3d"></a>

[bool](class_bool.md#class-bool) **use_scale_3d** = `false` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-use-scale-3d)

- void **set_use_scale_3d**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_using_scale_3d**()

Enable the usage of [scale_3d_min](class_particleprocessmaterial.md#class-particleprocessmaterial-property-scale-3d-min) and [scale_3d_max](class_particleprocessmaterial.md#class-particleprocessmaterial-property-scale-3d-max).

---


<a id="class-particleprocessmaterial-property-velocity-limit-curve"></a>

[Texture2D](class_texture2d.md#class-texture2d) **velocity_limit_curve** [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-velocity-limit-curve)

- void **set_velocity_limit_curve**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_velocity_limit_curve**()

A [CurveTexture](class_curvetexture.md#class-curvetexture) that defines the maximum velocity of a particle during its lifetime.

---


<a id="class-particleprocessmaterial-property-velocity-pivot"></a>

[Vector3](class_vector3.md#class-vector3) **velocity_pivot** = `Vector3(0, 0, 0)` [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-property-velocity-pivot)

- void **set_velocity_pivot**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_velocity_pivot**()

A pivot point used to calculate radial and orbital velocity of particles.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-particleprocessmaterial-method-get-param"></a>

[Vector2](class_vector2.md#class-vector2) **get_param**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-method-get-param)

Returns the minimum and maximum values of the given `param` as a vector.

The `x` component of the returned vector corresponds to minimum and the `y` component corresponds to maximum.

---


<a id="class-particleprocessmaterial-method-get-param-max"></a>

[float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-method-get-param-max)

Returns the maximum value range for the given parameter.

---


<a id="class-particleprocessmaterial-method-get-param-min"></a>

[float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-method-get-param-min)

Returns the minimum value range for the given parameter.

---


<a id="class-particleprocessmaterial-method-get-param-texture"></a>

[Texture2D](class_texture2d.md#class-texture2d) **get_param_texture**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter)) const [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-method-get-param-texture)

Returns the [Texture2D](class_texture2d.md#class-texture2d) used by the specified parameter.

---


<a id="class-particleprocessmaterial-method-get-particle-flag"></a>

[bool](class_bool.md#class-bool) **get_particle_flag**(particle_flag: [ParticleFlags](class_particleprocessmaterial.md#enum-particleprocessmaterial-particleflags)) const [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-method-get-particle-flag)

Returns `true` if the specified particle flag is enabled.

---


<a id="class-particleprocessmaterial-method-set-param"></a>

void **set_param**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), value: [Vector2](class_vector2.md#class-vector2)) [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param)

Sets the minimum and maximum values of the given `param`.

The `x` component of the argument vector corresponds to minimum and the `y` component corresponds to maximum.

---


<a id="class-particleprocessmaterial-method-set-param-max"></a>

void **set_param_max**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), value: [float](class_float.md#class-float)) [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-max)

Sets the maximum value range for the given parameter.

---


<a id="class-particleprocessmaterial-method-set-param-min"></a>

void **set_param_min**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), value: [float](class_float.md#class-float)) [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-min)

Sets the minimum value range for the given parameter.

---


<a id="class-particleprocessmaterial-method-set-param-texture"></a>

void **set_param_texture**(param: [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter), texture: [Texture2D](class_texture2d.md#class-texture2d)) [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-param-texture)

Sets the [Texture2D](class_texture2d.md#class-texture2d) for the specified [Parameter](class_particleprocessmaterial.md#enum-particleprocessmaterial-parameter).

---


<a id="class-particleprocessmaterial-method-set-particle-flag"></a>

void **set_particle_flag**(particle_flag: [ParticleFlags](class_particleprocessmaterial.md#enum-particleprocessmaterial-particleflags), enable: [bool](class_bool.md#class-bool)) [🔗](class_particleprocessmaterial.md#class-particleprocessmaterial-method-set-particle-flag)

Sets the `particle_flag` to `enable`.
