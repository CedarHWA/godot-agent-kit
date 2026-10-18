> Source: https://docs.godotengine.org/en/4.7/classes/class_cpuparticles3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="cpuparticles3d"></a>

<a id="class-cpuparticles3d"></a>

# CPUParticles3D

**Inherits:** [GeometryInstance3D](class_geometryinstance3d.md#class-geometryinstance3d) **<** [VisualInstance3D](class_visualinstance3d.md#class-visualinstance3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A CPU-based 3D particle emitter.

<a id="description"></a>

## Description

CPU-based 3D particle node used to create a variety of particle systems and effects.

See also [GPUParticles3D](class_gpuparticles3d.md#class-gpuparticles3d), which provides the same functionality with hardware acceleration, but may not run on older devices.

<a id="tutorials"></a>

## Tutorials

- [Particle systems (3D)](../tutorials/3d/particles/index.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [amount](class_cpuparticles3d.md#class-cpuparticles3d-property-amount) | `8` |
| [Curve](class_curve.md#class-curve) | [angle_curve](class_cpuparticles3d.md#class-cpuparticles3d-property-angle-curve) |  |
| [float](class_float.md#class-float) | [angle_max](class_cpuparticles3d.md#class-cpuparticles3d-property-angle-max) | `0.0` |
| [float](class_float.md#class-float) | [angle_min](class_cpuparticles3d.md#class-cpuparticles3d-property-angle-min) | `0.0` |
| [Curve](class_curve.md#class-curve) | [angular_velocity_curve](class_cpuparticles3d.md#class-cpuparticles3d-property-angular-velocity-curve) |  |
| [float](class_float.md#class-float) | [angular_velocity_max](class_cpuparticles3d.md#class-cpuparticles3d-property-angular-velocity-max) | `0.0` |
| [float](class_float.md#class-float) | [angular_velocity_min](class_cpuparticles3d.md#class-cpuparticles3d-property-angular-velocity-min) | `0.0` |
| [Curve](class_curve.md#class-curve) | [anim_offset_curve](class_cpuparticles3d.md#class-cpuparticles3d-property-anim-offset-curve) |  |
| [float](class_float.md#class-float) | [anim_offset_max](class_cpuparticles3d.md#class-cpuparticles3d-property-anim-offset-max) | `0.0` |
| [float](class_float.md#class-float) | [anim_offset_min](class_cpuparticles3d.md#class-cpuparticles3d-property-anim-offset-min) | `0.0` |
| [Curve](class_curve.md#class-curve) | [anim_speed_curve](class_cpuparticles3d.md#class-cpuparticles3d-property-anim-speed-curve) |  |
| [float](class_float.md#class-float) | [anim_speed_max](class_cpuparticles3d.md#class-cpuparticles3d-property-anim-speed-max) | `0.0` |
| [float](class_float.md#class-float) | [anim_speed_min](class_cpuparticles3d.md#class-cpuparticles3d-property-anim-speed-min) | `0.0` |
| [Color](class_color.md#class-color) | [color](class_cpuparticles3d.md#class-cpuparticles3d-property-color) | `Color(1, 1, 1, 1)` |
| [Gradient](class_gradient.md#class-gradient) | [color_initial_ramp](class_cpuparticles3d.md#class-cpuparticles3d-property-color-initial-ramp) |  |
| [Gradient](class_gradient.md#class-gradient) | [color_ramp](class_cpuparticles3d.md#class-cpuparticles3d-property-color-ramp) |  |
| [Curve](class_curve.md#class-curve) | [damping_curve](class_cpuparticles3d.md#class-cpuparticles3d-property-damping-curve) |  |
| [float](class_float.md#class-float) | [damping_max](class_cpuparticles3d.md#class-cpuparticles3d-property-damping-max) | `0.0` |
| [float](class_float.md#class-float) | [damping_min](class_cpuparticles3d.md#class-cpuparticles3d-property-damping-min) | `0.0` |
| [Vector3](class_vector3.md#class-vector3) | [direction](class_cpuparticles3d.md#class-cpuparticles3d-property-direction) | `Vector3(1, 0, 0)` |
| [DrawOrder](class_cpuparticles3d.md#enum-cpuparticles3d-draworder) | [draw_order](class_cpuparticles3d.md#class-cpuparticles3d-property-draw-order) | `0` |
| [Vector3](class_vector3.md#class-vector3) | [emission_box_extents](class_cpuparticles3d.md#class-cpuparticles3d-property-emission-box-extents) |  |
| [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) | [emission_colors](class_cpuparticles3d.md#class-cpuparticles3d-property-emission-colors) | `PackedColorArray()` |
| [PackedVector3Array](class_packedvector3array.md#class-packedvector3array) | [emission_normals](class_cpuparticles3d.md#class-cpuparticles3d-property-emission-normals) |  |
| [PackedVector3Array](class_packedvector3array.md#class-packedvector3array) | [emission_points](class_cpuparticles3d.md#class-cpuparticles3d-property-emission-points) |  |
| [Vector3](class_vector3.md#class-vector3) | [emission_ring_axis](class_cpuparticles3d.md#class-cpuparticles3d-property-emission-ring-axis) |  |
| [float](class_float.md#class-float) | [emission_ring_cone_angle](class_cpuparticles3d.md#class-cpuparticles3d-property-emission-ring-cone-angle) |  |
| [float](class_float.md#class-float) | [emission_ring_height](class_cpuparticles3d.md#class-cpuparticles3d-property-emission-ring-height) |  |
| [float](class_float.md#class-float) | [emission_ring_inner_radius](class_cpuparticles3d.md#class-cpuparticles3d-property-emission-ring-inner-radius) |  |
| [float](class_float.md#class-float) | [emission_ring_radius](class_cpuparticles3d.md#class-cpuparticles3d-property-emission-ring-radius) |  |
| [EmissionShape](class_cpuparticles3d.md#enum-cpuparticles3d-emissionshape) | [emission_shape](class_cpuparticles3d.md#class-cpuparticles3d-property-emission-shape) | `0` |
| [float](class_float.md#class-float) | [emission_sphere_radius](class_cpuparticles3d.md#class-cpuparticles3d-property-emission-sphere-radius) |  |
| [bool](class_bool.md#class-bool) | [emitting](class_cpuparticles3d.md#class-cpuparticles3d-property-emitting) | `true` |
| [float](class_float.md#class-float) | [explosiveness](class_cpuparticles3d.md#class-cpuparticles3d-property-explosiveness) | `0.0` |
| [int](class_int.md#class-int) | [fixed_fps](class_cpuparticles3d.md#class-cpuparticles3d-property-fixed-fps) | `0` |
| [float](class_float.md#class-float) | [flatness](class_cpuparticles3d.md#class-cpuparticles3d-property-flatness) | `0.0` |
| [bool](class_bool.md#class-bool) | [fract_delta](class_cpuparticles3d.md#class-cpuparticles3d-property-fract-delta) | `true` |
| [Vector3](class_vector3.md#class-vector3) | [gravity](class_cpuparticles3d.md#class-cpuparticles3d-property-gravity) | `Vector3(0, -9.8, 0)` |
| [Curve](class_curve.md#class-curve) | [hue_variation_curve](class_cpuparticles3d.md#class-cpuparticles3d-property-hue-variation-curve) |  |
| [float](class_float.md#class-float) | [hue_variation_max](class_cpuparticles3d.md#class-cpuparticles3d-property-hue-variation-max) | `0.0` |
| [float](class_float.md#class-float) | [hue_variation_min](class_cpuparticles3d.md#class-cpuparticles3d-property-hue-variation-min) | `0.0` |
| [float](class_float.md#class-float) | [initial_velocity_max](class_cpuparticles3d.md#class-cpuparticles3d-property-initial-velocity-max) | `0.0` |
| [float](class_float.md#class-float) | [initial_velocity_min](class_cpuparticles3d.md#class-cpuparticles3d-property-initial-velocity-min) | `0.0` |
| [float](class_float.md#class-float) | [lifetime](class_cpuparticles3d.md#class-cpuparticles3d-property-lifetime) | `1.0` |
| [float](class_float.md#class-float) | [lifetime_randomness](class_cpuparticles3d.md#class-cpuparticles3d-property-lifetime-randomness) | `0.0` |
| [Curve](class_curve.md#class-curve) | [linear_accel_curve](class_cpuparticles3d.md#class-cpuparticles3d-property-linear-accel-curve) |  |
| [float](class_float.md#class-float) | [linear_accel_max](class_cpuparticles3d.md#class-cpuparticles3d-property-linear-accel-max) | `0.0` |
| [float](class_float.md#class-float) | [linear_accel_min](class_cpuparticles3d.md#class-cpuparticles3d-property-linear-accel-min) | `0.0` |
| [bool](class_bool.md#class-bool) | [local_coords](class_cpuparticles3d.md#class-cpuparticles3d-property-local-coords) | `false` |
| [Mesh](class_mesh.md#class-mesh) | [mesh](class_cpuparticles3d.md#class-cpuparticles3d-property-mesh) |  |
| [bool](class_bool.md#class-bool) | [one_shot](class_cpuparticles3d.md#class-cpuparticles3d-property-one-shot) | `false` |
| [Curve](class_curve.md#class-curve) | [orbit_velocity_curve](class_cpuparticles3d.md#class-cpuparticles3d-property-orbit-velocity-curve) |  |
| [float](class_float.md#class-float) | [orbit_velocity_max](class_cpuparticles3d.md#class-cpuparticles3d-property-orbit-velocity-max) |  |
| [float](class_float.md#class-float) | [orbit_velocity_min](class_cpuparticles3d.md#class-cpuparticles3d-property-orbit-velocity-min) |  |
| [bool](class_bool.md#class-bool) | [particle_flag_align_y](class_cpuparticles3d.md#class-cpuparticles3d-property-particle-flag-align-y) | `false` |
| [bool](class_bool.md#class-bool) | [particle_flag_disable_z](class_cpuparticles3d.md#class-cpuparticles3d-property-particle-flag-disable-z) | `false` |
| [bool](class_bool.md#class-bool) | [particle_flag_rotate_y](class_cpuparticles3d.md#class-cpuparticles3d-property-particle-flag-rotate-y) | `false` |
| [float](class_float.md#class-float) | [preprocess](class_cpuparticles3d.md#class-cpuparticles3d-property-preprocess) | `0.0` |
| [Curve](class_curve.md#class-curve) | [radial_accel_curve](class_cpuparticles3d.md#class-cpuparticles3d-property-radial-accel-curve) |  |
| [float](class_float.md#class-float) | [radial_accel_max](class_cpuparticles3d.md#class-cpuparticles3d-property-radial-accel-max) | `0.0` |
| [float](class_float.md#class-float) | [radial_accel_min](class_cpuparticles3d.md#class-cpuparticles3d-property-radial-accel-min) | `0.0` |
| [float](class_float.md#class-float) | [randomness](class_cpuparticles3d.md#class-cpuparticles3d-property-randomness) | `0.0` |
| [Curve](class_curve.md#class-curve) | [scale_amount_curve](class_cpuparticles3d.md#class-cpuparticles3d-property-scale-amount-curve) |  |
| [float](class_float.md#class-float) | [scale_amount_max](class_cpuparticles3d.md#class-cpuparticles3d-property-scale-amount-max) | `1.0` |
| [float](class_float.md#class-float) | [scale_amount_min](class_cpuparticles3d.md#class-cpuparticles3d-property-scale-amount-min) | `1.0` |
| [Curve](class_curve.md#class-curve) | [scale_curve_x](class_cpuparticles3d.md#class-cpuparticles3d-property-scale-curve-x) |  |
| [Curve](class_curve.md#class-curve) | [scale_curve_y](class_cpuparticles3d.md#class-cpuparticles3d-property-scale-curve-y) |  |
| [Curve](class_curve.md#class-curve) | [scale_curve_z](class_cpuparticles3d.md#class-cpuparticles3d-property-scale-curve-z) |  |
| [int](class_int.md#class-int) | [seed](class_cpuparticles3d.md#class-cpuparticles3d-property-seed) | `0` |
| [float](class_float.md#class-float) | [speed_scale](class_cpuparticles3d.md#class-cpuparticles3d-property-speed-scale) | `1.0` |
| [bool](class_bool.md#class-bool) | [split_scale](class_cpuparticles3d.md#class-cpuparticles3d-property-split-scale) | `false` |
| [float](class_float.md#class-float) | [spread](class_cpuparticles3d.md#class-cpuparticles3d-property-spread) | `45.0` |
| [Curve](class_curve.md#class-curve) | [tangential_accel_curve](class_cpuparticles3d.md#class-cpuparticles3d-property-tangential-accel-curve) |  |
| [float](class_float.md#class-float) | [tangential_accel_max](class_cpuparticles3d.md#class-cpuparticles3d-property-tangential-accel-max) | `0.0` |
| [float](class_float.md#class-float) | [tangential_accel_min](class_cpuparticles3d.md#class-cpuparticles3d-property-tangential-accel-min) | `0.0` |
| [bool](class_bool.md#class-bool) | [use_fixed_seed](class_cpuparticles3d.md#class-cpuparticles3d-property-use-fixed-seed) | `false` |
| [AABB](class_aabb.md#class-aabb) | [visibility_aabb](class_cpuparticles3d.md#class-cpuparticles3d-property-visibility-aabb) | `AABB(0, 0, 0, 0, 0, 0)` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [AABB](class_aabb.md#class-aabb) | [capture_aabb](class_cpuparticles3d.md#class-cpuparticles3d-method-capture-aabb)() const |
| void | [convert_from_particles](class_cpuparticles3d.md#class-cpuparticles3d-method-convert-from-particles)(particles: [Node](class_node.md#class-node)) |
| [Curve](class_curve.md#class-curve) | [get_param_curve](class_cpuparticles3d.md#class-cpuparticles3d-method-get-param-curve)(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter)) const |
| [float](class_float.md#class-float) | [get_param_max](class_cpuparticles3d.md#class-cpuparticles3d-method-get-param-max)(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter)) const |
| [float](class_float.md#class-float) | [get_param_min](class_cpuparticles3d.md#class-cpuparticles3d-method-get-param-min)(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter)) const |
| [bool](class_bool.md#class-bool) | [get_particle_flag](class_cpuparticles3d.md#class-cpuparticles3d-method-get-particle-flag)(particle_flag: [ParticleFlags](class_cpuparticles3d.md#enum-cpuparticles3d-particleflags)) const |
| void | [request_particles_process](class_cpuparticles3d.md#class-cpuparticles3d-method-request-particles-process)(process_time: [float](class_float.md#class-float), process_time_residual: [float](class_float.md#class-float) = 0.0) |
| void | [restart](class_cpuparticles3d.md#class-cpuparticles3d-method-restart)(keep_seed: [bool](class_bool.md#class-bool) = false) |
| void | [set_param_curve](class_cpuparticles3d.md#class-cpuparticles3d-method-set-param-curve)(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter), curve: [Curve](class_curve.md#class-curve)) |
| void | [set_param_max](class_cpuparticles3d.md#class-cpuparticles3d-method-set-param-max)(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter), value: [float](class_float.md#class-float)) |
| void | [set_param_min](class_cpuparticles3d.md#class-cpuparticles3d-method-set-param-min)(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter), value: [float](class_float.md#class-float)) |
| void | [set_particle_flag](class_cpuparticles3d.md#class-cpuparticles3d-method-set-particle-flag)(particle_flag: [ParticleFlags](class_cpuparticles3d.md#enum-cpuparticles3d-particleflags), enable: [bool](class_bool.md#class-bool)) |

---


<a id="signals"></a>

## Signals

<a id="class-cpuparticles3d-signal-finished"></a>

**finished**() [🔗](class_cpuparticles3d.md#class-cpuparticles3d-signal-finished)

Emitted when all active particles have finished processing. When [one_shot](class_cpuparticles3d.md#class-cpuparticles3d-property-one-shot) is disabled, particles will process continuously, so this is never emitted.

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-cpuparticles3d-draworder"></a>

enum **DrawOrder**: [🔗](class_cpuparticles3d.md#enum-cpuparticles3d-draworder)

<a id="class-cpuparticles3d-constant-draw-order-index"></a>

[DrawOrder](class_cpuparticles3d.md#enum-cpuparticles3d-draworder) **DRAW_ORDER_INDEX** = `0`

Particles are drawn in the order emitted.

<a id="class-cpuparticles3d-constant-draw-order-lifetime"></a>

[DrawOrder](class_cpuparticles3d.md#enum-cpuparticles3d-draworder) **DRAW_ORDER_LIFETIME** = `1`

Particles are drawn in order of remaining lifetime. In other words, the particle with the highest lifetime is drawn at the front.

<a id="class-cpuparticles3d-constant-draw-order-view-depth"></a>

[DrawOrder](class_cpuparticles3d.md#enum-cpuparticles3d-draworder) **DRAW_ORDER_VIEW_DEPTH** = `2`

Particles are drawn in order of depth.

---


<a id="enum-cpuparticles3d-parameter"></a>

enum **Parameter**: [🔗](class_cpuparticles3d.md#enum-cpuparticles3d-parameter)

<a id="class-cpuparticles3d-constant-param-initial-linear-velocity"></a>

[Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter) **PARAM_INITIAL_LINEAR_VELOCITY** = `0`

Use with [set_param_min()](class_cpuparticles3d.md#class-cpuparticles3d-method-set-param-min), [set_param_max()](class_cpuparticles3d.md#class-cpuparticles3d-method-set-param-max), and [set_param_curve()](class_cpuparticles3d.md#class-cpuparticles3d-method-set-param-curve) to set initial velocity properties.

<a id="class-cpuparticles3d-constant-param-angular-velocity"></a>

[Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter) **PARAM_ANGULAR_VELOCITY** = `1`

Use with [set_param_min()](class_cpuparticles3d.md#class-cpuparticles3d-method-set-param-min), [set_param_max()](class_cpuparticles3d.md#class-cpuparticles3d-method-set-param-max), and [set_param_curve()](class_cpuparticles3d.md#class-cpuparticles3d-method-set-param-curve) to set angular velocity properties.

<a id="class-cpuparticles3d-constant-param-orbit-velocity"></a>

[Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter) **PARAM_ORBIT_VELOCITY** = `2`

Use with [set_param_min()](class_cpuparticles3d.md#class-cpuparticles3d-method-set-param-min), [set_param_max()](class_cpuparticles3d.md#class-cpuparticles3d-method-set-param-max), and [set_param_curve()](class_cpuparticles3d.md#class-cpuparticles3d-method-set-param-curve) to set orbital velocity properties.

<a id="class-cpuparticles3d-constant-param-linear-accel"></a>

[Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter) **PARAM_LINEAR_ACCEL** = `3`

Use with [set_param_min()](class_cpuparticles3d.md#class-cpuparticles3d-method-set-param-min), [set_param_max()](class_cpuparticles3d.md#class-cpuparticles3d-method-set-param-max), and [set_param_curve()](class_cpuparticles3d.md#class-cpuparticles3d-method-set-param-curve) to set linear acceleration properties.

<a id="class-cpuparticles3d-constant-param-radial-accel"></a>

[Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter) **PARAM_RADIAL_ACCEL** = `4`

Use with [set_param_min()](class_cpuparticles3d.md#class-cpuparticles3d-method-set-param-min), [set_param_max()](class_cpuparticles3d.md#class-cpuparticles3d-method-set-param-max), and [set_param_curve()](class_cpuparticles3d.md#class-cpuparticles3d-method-set-param-curve) to set radial acceleration properties.

<a id="class-cpuparticles3d-constant-param-tangential-accel"></a>

[Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter) **PARAM_TANGENTIAL_ACCEL** = `5`

Use with [set_param_min()](class_cpuparticles3d.md#class-cpuparticles3d-method-set-param-min), [set_param_max()](class_cpuparticles3d.md#class-cpuparticles3d-method-set-param-max), and [set_param_curve()](class_cpuparticles3d.md#class-cpuparticles3d-method-set-param-curve) to set tangential acceleration properties.

<a id="class-cpuparticles3d-constant-param-damping"></a>

[Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter) **PARAM_DAMPING** = `6`

Use with [set_param_min()](class_cpuparticles3d.md#class-cpuparticles3d-method-set-param-min), [set_param_max()](class_cpuparticles3d.md#class-cpuparticles3d-method-set-param-max), and [set_param_curve()](class_cpuparticles3d.md#class-cpuparticles3d-method-set-param-curve) to set damping properties.

<a id="class-cpuparticles3d-constant-param-angle"></a>

[Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter) **PARAM_ANGLE** = `7`

Use with [set_param_min()](class_cpuparticles3d.md#class-cpuparticles3d-method-set-param-min), [set_param_max()](class_cpuparticles3d.md#class-cpuparticles3d-method-set-param-max), and [set_param_curve()](class_cpuparticles3d.md#class-cpuparticles3d-method-set-param-curve) to set angle properties.

<a id="class-cpuparticles3d-constant-param-scale"></a>

[Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter) **PARAM_SCALE** = `8`

Use with [set_param_min()](class_cpuparticles3d.md#class-cpuparticles3d-method-set-param-min), [set_param_max()](class_cpuparticles3d.md#class-cpuparticles3d-method-set-param-max), and [set_param_curve()](class_cpuparticles3d.md#class-cpuparticles3d-method-set-param-curve) to set scale properties.

<a id="class-cpuparticles3d-constant-param-hue-variation"></a>

[Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter) **PARAM_HUE_VARIATION** = `9`

Use with [set_param_min()](class_cpuparticles3d.md#class-cpuparticles3d-method-set-param-min), [set_param_max()](class_cpuparticles3d.md#class-cpuparticles3d-method-set-param-max), and [set_param_curve()](class_cpuparticles3d.md#class-cpuparticles3d-method-set-param-curve) to set hue variation properties.

<a id="class-cpuparticles3d-constant-param-anim-speed"></a>

[Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter) **PARAM_ANIM_SPEED** = `10`

Use with [set_param_min()](class_cpuparticles3d.md#class-cpuparticles3d-method-set-param-min), [set_param_max()](class_cpuparticles3d.md#class-cpuparticles3d-method-set-param-max), and [set_param_curve()](class_cpuparticles3d.md#class-cpuparticles3d-method-set-param-curve) to set animation speed properties.

<a id="class-cpuparticles3d-constant-param-anim-offset"></a>

[Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter) **PARAM_ANIM_OFFSET** = `11`

Use with [set_param_min()](class_cpuparticles3d.md#class-cpuparticles3d-method-set-param-min), [set_param_max()](class_cpuparticles3d.md#class-cpuparticles3d-method-set-param-max), and [set_param_curve()](class_cpuparticles3d.md#class-cpuparticles3d-method-set-param-curve) to set animation offset properties.

<a id="class-cpuparticles3d-constant-param-max"></a>

[Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter) **PARAM_MAX** = `12`

Represents the size of the [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter) enum.

---


<a id="enum-cpuparticles3d-particleflags"></a>

enum **ParticleFlags**: [🔗](class_cpuparticles3d.md#enum-cpuparticles3d-particleflags)

<a id="class-cpuparticles3d-constant-particle-flag-align-y-to-velocity"></a>

[ParticleFlags](class_cpuparticles3d.md#enum-cpuparticles3d-particleflags) **PARTICLE_FLAG_ALIGN_Y_TO_VELOCITY** = `0`

Use with [set_particle_flag()](class_cpuparticles3d.md#class-cpuparticles3d-method-set-particle-flag) to set [particle_flag_align_y](class_cpuparticles3d.md#class-cpuparticles3d-property-particle-flag-align-y).

<a id="class-cpuparticles3d-constant-particle-flag-rotate-y"></a>

[ParticleFlags](class_cpuparticles3d.md#enum-cpuparticles3d-particleflags) **PARTICLE_FLAG_ROTATE_Y** = `1`

Use with [set_particle_flag()](class_cpuparticles3d.md#class-cpuparticles3d-method-set-particle-flag) to set [particle_flag_rotate_y](class_cpuparticles3d.md#class-cpuparticles3d-property-particle-flag-rotate-y).

<a id="class-cpuparticles3d-constant-particle-flag-disable-z"></a>

[ParticleFlags](class_cpuparticles3d.md#enum-cpuparticles3d-particleflags) **PARTICLE_FLAG_DISABLE_Z** = `2`

Use with [set_particle_flag()](class_cpuparticles3d.md#class-cpuparticles3d-method-set-particle-flag) to set [particle_flag_disable_z](class_cpuparticles3d.md#class-cpuparticles3d-property-particle-flag-disable-z).

<a id="class-cpuparticles3d-constant-particle-flag-max"></a>

[ParticleFlags](class_cpuparticles3d.md#enum-cpuparticles3d-particleflags) **PARTICLE_FLAG_MAX** = `3`

Represents the size of the [ParticleFlags](class_cpuparticles3d.md#enum-cpuparticles3d-particleflags) enum.

---


<a id="enum-cpuparticles3d-emissionshape"></a>

enum **EmissionShape**: [🔗](class_cpuparticles3d.md#enum-cpuparticles3d-emissionshape)

<a id="class-cpuparticles3d-constant-emission-shape-point"></a>

[EmissionShape](class_cpuparticles3d.md#enum-cpuparticles3d-emissionshape) **EMISSION_SHAPE_POINT** = `0`

All particles will be emitted from a single point.

<a id="class-cpuparticles3d-constant-emission-shape-sphere"></a>

[EmissionShape](class_cpuparticles3d.md#enum-cpuparticles3d-emissionshape) **EMISSION_SHAPE_SPHERE** = `1`

Particles will be emitted in the volume of a sphere.

<a id="class-cpuparticles3d-constant-emission-shape-sphere-surface"></a>

[EmissionShape](class_cpuparticles3d.md#enum-cpuparticles3d-emissionshape) **EMISSION_SHAPE_SPHERE_SURFACE** = `2`

Particles will be emitted on the surface of a sphere.

<a id="class-cpuparticles3d-constant-emission-shape-box"></a>

[EmissionShape](class_cpuparticles3d.md#enum-cpuparticles3d-emissionshape) **EMISSION_SHAPE_BOX** = `3`

Particles will be emitted in the volume of a box.

<a id="class-cpuparticles3d-constant-emission-shape-points"></a>

[EmissionShape](class_cpuparticles3d.md#enum-cpuparticles3d-emissionshape) **EMISSION_SHAPE_POINTS** = `4`

Particles will be emitted at a position chosen randomly among [emission_points](class_cpuparticles3d.md#class-cpuparticles3d-property-emission-points). Particle color will be modulated by [emission_colors](class_cpuparticles3d.md#class-cpuparticles3d-property-emission-colors).

<a id="class-cpuparticles3d-constant-emission-shape-directed-points"></a>

[EmissionShape](class_cpuparticles3d.md#enum-cpuparticles3d-emissionshape) **EMISSION_SHAPE_DIRECTED_POINTS** = `5`

Particles will be emitted at a position chosen randomly among [emission_points](class_cpuparticles3d.md#class-cpuparticles3d-property-emission-points). Particle velocity and rotation will be set based on [emission_normals](class_cpuparticles3d.md#class-cpuparticles3d-property-emission-normals). Particle color will be modulated by [emission_colors](class_cpuparticles3d.md#class-cpuparticles3d-property-emission-colors).

<a id="class-cpuparticles3d-constant-emission-shape-ring"></a>

[EmissionShape](class_cpuparticles3d.md#enum-cpuparticles3d-emissionshape) **EMISSION_SHAPE_RING** = `6`

Particles will be emitted in a ring or cylinder.

<a id="class-cpuparticles3d-constant-emission-shape-max"></a>

[EmissionShape](class_cpuparticles3d.md#enum-cpuparticles3d-emissionshape) **EMISSION_SHAPE_MAX** = `7`

Represents the size of the [EmissionShape](class_cpuparticles3d.md#enum-cpuparticles3d-emissionshape) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-cpuparticles3d-property-amount"></a>

[int](class_int.md#class-int) **amount** = `8` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-amount)

- void **set_amount**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_amount**()

Number of particles emitted in one emission cycle.

---


<a id="class-cpuparticles3d-property-angle-curve"></a>

[Curve](class_curve.md#class-curve) **angle_curve** [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-angle-curve)

- void **set_param_curve**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter), curve: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_param_curve**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter)) const

Each particle's rotation will be animated along this [Curve](class_curve.md#class-curve). Should be a unit [Curve](class_curve.md#class-curve).

---


<a id="class-cpuparticles3d-property-angle-max"></a>

[float](class_float.md#class-float) **angle_max** = `0.0` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-angle-max)

- void **set_param_max**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter)) const

Maximum angle.

---


<a id="class-cpuparticles3d-property-angle-min"></a>

[float](class_float.md#class-float) **angle_min** = `0.0` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-angle-min)

- void **set_param_min**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter)) const

Minimum angle.

---


<a id="class-cpuparticles3d-property-angular-velocity-curve"></a>

[Curve](class_curve.md#class-curve) **angular_velocity_curve** [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-angular-velocity-curve)

- void **set_param_curve**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter), curve: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_param_curve**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter)) const

Each particle's angular velocity (rotation speed) will vary along this [Curve](class_curve.md#class-curve) over its lifetime. Should be a unit [Curve](class_curve.md#class-curve).

---


<a id="class-cpuparticles3d-property-angular-velocity-max"></a>

[float](class_float.md#class-float) **angular_velocity_max** = `0.0` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-angular-velocity-max)

- void **set_param_max**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter)) const

Maximum initial angular velocity (rotation speed) applied to each particle in *degrees* per second.

---


<a id="class-cpuparticles3d-property-angular-velocity-min"></a>

[float](class_float.md#class-float) **angular_velocity_min** = `0.0` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-angular-velocity-min)

- void **set_param_min**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter)) const

Minimum initial angular velocity (rotation speed) applied to each particle in *degrees* per second.

---


<a id="class-cpuparticles3d-property-anim-offset-curve"></a>

[Curve](class_curve.md#class-curve) **anim_offset_curve** [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-anim-offset-curve)

- void **set_param_curve**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter), curve: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_param_curve**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter)) const

Each particle's animation offset will vary along this [Curve](class_curve.md#class-curve). Should be a unit [Curve](class_curve.md#class-curve).

---


<a id="class-cpuparticles3d-property-anim-offset-max"></a>

[float](class_float.md#class-float) **anim_offset_max** = `0.0` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-anim-offset-max)

- void **set_param_max**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter)) const

Maximum animation offset.

---


<a id="class-cpuparticles3d-property-anim-offset-min"></a>

[float](class_float.md#class-float) **anim_offset_min** = `0.0` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-anim-offset-min)

- void **set_param_min**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter)) const

Minimum animation offset.

---


<a id="class-cpuparticles3d-property-anim-speed-curve"></a>

[Curve](class_curve.md#class-curve) **anim_speed_curve** [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-anim-speed-curve)

- void **set_param_curve**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter), curve: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_param_curve**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter)) const

Each particle's animation speed will vary along this [Curve](class_curve.md#class-curve). Should be a unit [Curve](class_curve.md#class-curve).

---


<a id="class-cpuparticles3d-property-anim-speed-max"></a>

[float](class_float.md#class-float) **anim_speed_max** = `0.0` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-anim-speed-max)

- void **set_param_max**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter)) const

Maximum particle animation speed.

---


<a id="class-cpuparticles3d-property-anim-speed-min"></a>

[float](class_float.md#class-float) **anim_speed_min** = `0.0` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-anim-speed-min)

- void **set_param_min**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter)) const

Minimum particle animation speed.

---


<a id="class-cpuparticles3d-property-color"></a>

[Color](class_color.md#class-color) **color** = `Color(1, 1, 1, 1)` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-color)

- void **set_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_color**()

Each particle's initial color.

**Note:** [color](class_cpuparticles3d.md#class-cpuparticles3d-property-color) multiplies the particle mesh's vertex colors. To have a visible effect on a [BaseMaterial3D](class_basematerial3d.md#class-basematerial3d), [BaseMaterial3D.vertex_color_use_as_albedo](class_basematerial3d.md#class-basematerial3d-property-vertex-color-use-as-albedo) *must* be `true`. For a [ShaderMaterial](class_shadermaterial.md#class-shadermaterial), `ALBEDO *= COLOR.rgb;` must be inserted in the shader's `fragment()` function. Otherwise, [color](class_cpuparticles3d.md#class-cpuparticles3d-property-color) will have no visible effect.

---


<a id="class-cpuparticles3d-property-color-initial-ramp"></a>

[Gradient](class_gradient.md#class-gradient) **color_initial_ramp** [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-color-initial-ramp)

- void **set_color_initial_ramp**(value: [Gradient](class_gradient.md#class-gradient))
- [Gradient](class_gradient.md#class-gradient) **get_color_initial_ramp**()

Each particle's initial color will vary along this [Gradient](class_gradient.md#class-gradient) (multiplied with [color](class_cpuparticles3d.md#class-cpuparticles3d-property-color)).

**Note:** [color_initial_ramp](class_cpuparticles3d.md#class-cpuparticles3d-property-color-initial-ramp) multiplies the particle mesh's vertex colors. To have a visible effect on a [BaseMaterial3D](class_basematerial3d.md#class-basematerial3d), [BaseMaterial3D.vertex_color_use_as_albedo](class_basematerial3d.md#class-basematerial3d-property-vertex-color-use-as-albedo) *must* be `true`. For a [ShaderMaterial](class_shadermaterial.md#class-shadermaterial), `ALBEDO *= COLOR.rgb;` must be inserted in the shader's `fragment()` function. Otherwise, [color_initial_ramp](class_cpuparticles3d.md#class-cpuparticles3d-property-color-initial-ramp) will have no visible effect.

---


<a id="class-cpuparticles3d-property-color-ramp"></a>

[Gradient](class_gradient.md#class-gradient) **color_ramp** [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-color-ramp)

- void **set_color_ramp**(value: [Gradient](class_gradient.md#class-gradient))
- [Gradient](class_gradient.md#class-gradient) **get_color_ramp**()

Each particle's color will vary along this [Gradient](class_gradient.md#class-gradient) over its lifetime (multiplied with [color](class_cpuparticles3d.md#class-cpuparticles3d-property-color)).

**Note:** [color_ramp](class_cpuparticles3d.md#class-cpuparticles3d-property-color-ramp) multiplies the particle mesh's vertex colors. To have a visible effect on a [BaseMaterial3D](class_basematerial3d.md#class-basematerial3d), [BaseMaterial3D.vertex_color_use_as_albedo](class_basematerial3d.md#class-basematerial3d-property-vertex-color-use-as-albedo) *must* be `true`. For a [ShaderMaterial](class_shadermaterial.md#class-shadermaterial), `ALBEDO *= COLOR.rgb;` must be inserted in the shader's `fragment()` function. Otherwise, [color_ramp](class_cpuparticles3d.md#class-cpuparticles3d-property-color-ramp) will have no visible effect.

---


<a id="class-cpuparticles3d-property-damping-curve"></a>

[Curve](class_curve.md#class-curve) **damping_curve** [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-damping-curve)

- void **set_param_curve**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter), curve: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_param_curve**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter)) const

Damping will vary along this [Curve](class_curve.md#class-curve). Should be a unit [Curve](class_curve.md#class-curve).

---


<a id="class-cpuparticles3d-property-damping-max"></a>

[float](class_float.md#class-float) **damping_max** = `0.0` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-damping-max)

- void **set_param_max**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter)) const

Maximum damping.

---


<a id="class-cpuparticles3d-property-damping-min"></a>

[float](class_float.md#class-float) **damping_min** = `0.0` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-damping-min)

- void **set_param_min**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter)) const

Minimum damping.

---


<a id="class-cpuparticles3d-property-direction"></a>

[Vector3](class_vector3.md#class-vector3) **direction** = `Vector3(1, 0, 0)` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-direction)

- void **set_direction**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_direction**()

Unit vector specifying the particles' emission direction.

---


<a id="class-cpuparticles3d-property-draw-order"></a>

[DrawOrder](class_cpuparticles3d.md#enum-cpuparticles3d-draworder) **draw_order** = `0` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-draw-order)

- void **set_draw_order**(value: [DrawOrder](class_cpuparticles3d.md#enum-cpuparticles3d-draworder))
- [DrawOrder](class_cpuparticles3d.md#enum-cpuparticles3d-draworder) **get_draw_order**()

Particle draw order.

---


<a id="class-cpuparticles3d-property-emission-box-extents"></a>

[Vector3](class_vector3.md#class-vector3) **emission_box_extents** [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-emission-box-extents)

- void **set_emission_box_extents**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_emission_box_extents**()

The rectangle's extents if [emission_shape](class_cpuparticles3d.md#class-cpuparticles3d-property-emission-shape) is set to [EMISSION_SHAPE_BOX](class_cpuparticles3d.md#class-cpuparticles3d-constant-emission-shape-box).

---


<a id="class-cpuparticles3d-property-emission-colors"></a>

[PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) **emission_colors** = `PackedColorArray()` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-emission-colors)

- void **set_emission_colors**(value: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray))
- [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) **get_emission_colors**()

Sets the [Color](class_color.md#class-color)s to modulate particles by when using [EMISSION_SHAPE_POINTS](class_cpuparticles3d.md#class-cpuparticles3d-constant-emission-shape-points) or [EMISSION_SHAPE_DIRECTED_POINTS](class_cpuparticles3d.md#class-cpuparticles3d-constant-emission-shape-directed-points).

**Note:** [emission_colors](class_cpuparticles3d.md#class-cpuparticles3d-property-emission-colors) multiplies the particle mesh's vertex colors. To have a visible effect on a [BaseMaterial3D](class_basematerial3d.md#class-basematerial3d), [BaseMaterial3D.vertex_color_use_as_albedo](class_basematerial3d.md#class-basematerial3d-property-vertex-color-use-as-albedo) *must* be `true`. For a [ShaderMaterial](class_shadermaterial.md#class-shadermaterial), `ALBEDO *= COLOR.rgb;` must be inserted in the shader's `fragment()` function. Otherwise, [emission_colors](class_cpuparticles3d.md#class-cpuparticles3d-property-emission-colors) will have no visible effect.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) for more details.

---


<a id="class-cpuparticles3d-property-emission-normals"></a>

[PackedVector3Array](class_packedvector3array.md#class-packedvector3array) **emission_normals** [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-emission-normals)

- void **set_emission_normals**(value: [PackedVector3Array](class_packedvector3array.md#class-packedvector3array))
- [PackedVector3Array](class_packedvector3array.md#class-packedvector3array) **get_emission_normals**()

Sets the direction the particles will be emitted in when using [EMISSION_SHAPE_DIRECTED_POINTS](class_cpuparticles3d.md#class-cpuparticles3d-constant-emission-shape-directed-points).

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector3Array](class_packedvector3array.md#class-packedvector3array) for more details.

---


<a id="class-cpuparticles3d-property-emission-points"></a>

[PackedVector3Array](class_packedvector3array.md#class-packedvector3array) **emission_points** [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-emission-points)

- void **set_emission_points**(value: [PackedVector3Array](class_packedvector3array.md#class-packedvector3array))
- [PackedVector3Array](class_packedvector3array.md#class-packedvector3array) **get_emission_points**()

Sets the initial positions to spawn particles when using [EMISSION_SHAPE_POINTS](class_cpuparticles3d.md#class-cpuparticles3d-constant-emission-shape-points) or [EMISSION_SHAPE_DIRECTED_POINTS](class_cpuparticles3d.md#class-cpuparticles3d-constant-emission-shape-directed-points).

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector3Array](class_packedvector3array.md#class-packedvector3array) for more details.

---


<a id="class-cpuparticles3d-property-emission-ring-axis"></a>

[Vector3](class_vector3.md#class-vector3) **emission_ring_axis** [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-emission-ring-axis)

- void **set_emission_ring_axis**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_emission_ring_axis**()

The axis of the ring when using the emitter [EMISSION_SHAPE_RING](class_cpuparticles3d.md#class-cpuparticles3d-constant-emission-shape-ring).

---


<a id="class-cpuparticles3d-property-emission-ring-cone-angle"></a>

[float](class_float.md#class-float) **emission_ring_cone_angle** [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-emission-ring-cone-angle)

- void **set_emission_ring_cone_angle**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_emission_ring_cone_angle**()

The angle of the cone when using the emitter [EMISSION_SHAPE_RING](class_cpuparticles3d.md#class-cpuparticles3d-constant-emission-shape-ring). The default angle of 90 degrees results in a ring, while an angle of 0 degrees results in a cone. Intermediate values will result in a ring where one end is larger than the other.

**Note:** Depending on [emission_ring_height](class_cpuparticles3d.md#class-cpuparticles3d-property-emission-ring-height), the angle may be clamped if the ring's end is reached to form a perfect cone.

---


<a id="class-cpuparticles3d-property-emission-ring-height"></a>

[float](class_float.md#class-float) **emission_ring_height** [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-emission-ring-height)

- void **set_emission_ring_height**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_emission_ring_height**()

The height of the ring when using the emitter [EMISSION_SHAPE_RING](class_cpuparticles3d.md#class-cpuparticles3d-constant-emission-shape-ring).

---


<a id="class-cpuparticles3d-property-emission-ring-inner-radius"></a>

[float](class_float.md#class-float) **emission_ring_inner_radius** [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-emission-ring-inner-radius)

- void **set_emission_ring_inner_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_emission_ring_inner_radius**()

The inner radius of the ring when using the emitter [EMISSION_SHAPE_RING](class_cpuparticles3d.md#class-cpuparticles3d-constant-emission-shape-ring).

---


<a id="class-cpuparticles3d-property-emission-ring-radius"></a>

[float](class_float.md#class-float) **emission_ring_radius** [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-emission-ring-radius)

- void **set_emission_ring_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_emission_ring_radius**()

The radius of the ring when using the emitter [EMISSION_SHAPE_RING](class_cpuparticles3d.md#class-cpuparticles3d-constant-emission-shape-ring).

---


<a id="class-cpuparticles3d-property-emission-shape"></a>

[EmissionShape](class_cpuparticles3d.md#enum-cpuparticles3d-emissionshape) **emission_shape** = `0` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-emission-shape)

- void **set_emission_shape**(value: [EmissionShape](class_cpuparticles3d.md#enum-cpuparticles3d-emissionshape))
- [EmissionShape](class_cpuparticles3d.md#enum-cpuparticles3d-emissionshape) **get_emission_shape**()

Particles will be emitted inside this region.

---


<a id="class-cpuparticles3d-property-emission-sphere-radius"></a>

[float](class_float.md#class-float) **emission_sphere_radius** [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-emission-sphere-radius)

- void **set_emission_sphere_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_emission_sphere_radius**()

The sphere's radius if [EmissionShape](class_cpuparticles3d.md#enum-cpuparticles3d-emissionshape) is set to [EMISSION_SHAPE_SPHERE](class_cpuparticles3d.md#class-cpuparticles3d-constant-emission-shape-sphere).

---


<a id="class-cpuparticles3d-property-emitting"></a>

[bool](class_bool.md#class-bool) **emitting** = `true` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-emitting)

- void **set_emitting**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_emitting**()

If `true`, particles are being emitted. [emitting](class_cpuparticles3d.md#class-cpuparticles3d-property-emitting) can be used to start and stop particles from emitting. However, if [one_shot](class_cpuparticles3d.md#class-cpuparticles3d-property-one-shot) is `true` setting [emitting](class_cpuparticles3d.md#class-cpuparticles3d-property-emitting) to `true` will not restart the emission cycle until after all active particles finish processing. You can use the [finished](class_cpuparticles3d.md#class-cpuparticles3d-signal-finished) signal to be notified once all active particles finish processing.

---


<a id="class-cpuparticles3d-property-explosiveness"></a>

[float](class_float.md#class-float) **explosiveness** = `0.0` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-explosiveness)

- void **set_explosiveness_ratio**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_explosiveness_ratio**()

How rapidly particles in an emission cycle are emitted. If greater than `0`, there will be a gap in emissions before the next cycle begins.

---


<a id="class-cpuparticles3d-property-fixed-fps"></a>

[int](class_int.md#class-int) **fixed_fps** = `0` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-fixed-fps)

- void **set_fixed_fps**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_fixed_fps**()

The particle system's frame rate is fixed to a value. For example, changing the value to 2 will make the particles render at 2 frames per second. Note this does not slow down the particle system itself.

---


<a id="class-cpuparticles3d-property-flatness"></a>

[float](class_float.md#class-float) **flatness** = `0.0` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-flatness)

- void **set_flatness**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_flatness**()

Amount of [spread](class_cpuparticles3d.md#class-cpuparticles3d-property-spread) in Y/Z plane. A value of `1` restricts particles to X/Z plane.

---


<a id="class-cpuparticles3d-property-fract-delta"></a>

[bool](class_bool.md#class-bool) **fract_delta** = `true` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-fract-delta)

- void **set_fractional_delta**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_fractional_delta**()

If `true`, results in fractional delta calculation which has a smoother particles display effect.

---


<a id="class-cpuparticles3d-property-gravity"></a>

[Vector3](class_vector3.md#class-vector3) **gravity** = `Vector3(0, -9.8, 0)` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-gravity)

- void **set_gravity**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_gravity**()

Gravity applied to every particle.

---


<a id="class-cpuparticles3d-property-hue-variation-curve"></a>

[Curve](class_curve.md#class-curve) **hue_variation_curve** [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-hue-variation-curve)

- void **set_param_curve**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter), curve: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_param_curve**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter)) const

Each particle's hue will vary along this [Curve](class_curve.md#class-curve). Should be a unit [Curve](class_curve.md#class-curve).

---


<a id="class-cpuparticles3d-property-hue-variation-max"></a>

[float](class_float.md#class-float) **hue_variation_max** = `0.0` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-hue-variation-max)

- void **set_param_max**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter)) const

Maximum hue variation.

---


<a id="class-cpuparticles3d-property-hue-variation-min"></a>

[float](class_float.md#class-float) **hue_variation_min** = `0.0` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-hue-variation-min)

- void **set_param_min**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter)) const

Minimum hue variation.

---


<a id="class-cpuparticles3d-property-initial-velocity-max"></a>

[float](class_float.md#class-float) **initial_velocity_max** = `0.0` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-initial-velocity-max)

- void **set_param_max**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter)) const

Maximum value of the initial velocity.

---


<a id="class-cpuparticles3d-property-initial-velocity-min"></a>

[float](class_float.md#class-float) **initial_velocity_min** = `0.0` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-initial-velocity-min)

- void **set_param_min**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter)) const

Minimum value of the initial velocity.

---


<a id="class-cpuparticles3d-property-lifetime"></a>

[float](class_float.md#class-float) **lifetime** = `1.0` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-lifetime)

- void **set_lifetime**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_lifetime**()

Amount of time each particle will exist.

---


<a id="class-cpuparticles3d-property-lifetime-randomness"></a>

[float](class_float.md#class-float) **lifetime_randomness** = `0.0` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-lifetime-randomness)

- void **set_lifetime_randomness**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_lifetime_randomness**()

Particle lifetime randomness ratio.

---


<a id="class-cpuparticles3d-property-linear-accel-curve"></a>

[Curve](class_curve.md#class-curve) **linear_accel_curve** [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-linear-accel-curve)

- void **set_param_curve**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter), curve: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_param_curve**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter)) const

Each particle's linear acceleration will vary along this [Curve](class_curve.md#class-curve). Should be a unit [Curve](class_curve.md#class-curve).

---


<a id="class-cpuparticles3d-property-linear-accel-max"></a>

[float](class_float.md#class-float) **linear_accel_max** = `0.0` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-linear-accel-max)

- void **set_param_max**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter)) const

Maximum linear acceleration.

---


<a id="class-cpuparticles3d-property-linear-accel-min"></a>

[float](class_float.md#class-float) **linear_accel_min** = `0.0` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-linear-accel-min)

- void **set_param_min**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter)) const

Minimum linear acceleration.

---


<a id="class-cpuparticles3d-property-local-coords"></a>

[bool](class_bool.md#class-bool) **local_coords** = `false` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-local-coords)

- void **set_use_local_coordinates**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_use_local_coordinates**()

If `true`, particles use the parent node's coordinate space (known as local coordinates). This will cause particles to move and rotate along the **CPUParticles3D** node (and its parents) when it is moved or rotated. If `false`, particles use global coordinates; they will not move or rotate along the **CPUParticles3D** node (and its parents) when it is moved or rotated.

---


<a id="class-cpuparticles3d-property-mesh"></a>

[Mesh](class_mesh.md#class-mesh) **mesh** [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-mesh)

- void **set_mesh**(value: [Mesh](class_mesh.md#class-mesh))
- [Mesh](class_mesh.md#class-mesh) **get_mesh**()

The [Mesh](class_mesh.md#class-mesh) used for each particle. If `null`, particles will be spheres.

---


<a id="class-cpuparticles3d-property-one-shot"></a>

[bool](class_bool.md#class-bool) **one_shot** = `false` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-one-shot)

- void **set_one_shot**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_one_shot**()

If `true`, only one emission cycle occurs. If set `true` during a cycle, emission will stop at the cycle's end.

---


<a id="class-cpuparticles3d-property-orbit-velocity-curve"></a>

[Curve](class_curve.md#class-curve) **orbit_velocity_curve** [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-orbit-velocity-curve)

- void **set_param_curve**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter), curve: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_param_curve**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter)) const

Each particle's orbital velocity will vary along this [Curve](class_curve.md#class-curve). Should be a unit [Curve](class_curve.md#class-curve).

---


<a id="class-cpuparticles3d-property-orbit-velocity-max"></a>

[float](class_float.md#class-float) **orbit_velocity_max** [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-orbit-velocity-max)

- void **set_param_max**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter)) const

Maximum orbit velocity.

---


<a id="class-cpuparticles3d-property-orbit-velocity-min"></a>

[float](class_float.md#class-float) **orbit_velocity_min** [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-orbit-velocity-min)

- void **set_param_min**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter)) const

Minimum orbit velocity.

---


<a id="class-cpuparticles3d-property-particle-flag-align-y"></a>

[bool](class_bool.md#class-bool) **particle_flag_align_y** = `false` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-particle-flag-align-y)

- void **set_particle_flag**(particle_flag: [ParticleFlags](class_cpuparticles3d.md#enum-cpuparticles3d-particleflags), enable: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_particle_flag**(particle_flag: [ParticleFlags](class_cpuparticles3d.md#enum-cpuparticles3d-particleflags)) const

Align Y axis of particle with the direction of its velocity.

---


<a id="class-cpuparticles3d-property-particle-flag-disable-z"></a>

[bool](class_bool.md#class-bool) **particle_flag_disable_z** = `false` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-particle-flag-disable-z)

- void **set_particle_flag**(particle_flag: [ParticleFlags](class_cpuparticles3d.md#enum-cpuparticles3d-particleflags), enable: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_particle_flag**(particle_flag: [ParticleFlags](class_cpuparticles3d.md#enum-cpuparticles3d-particleflags)) const

If `true`, particles will not move on the Z axis.

---


<a id="class-cpuparticles3d-property-particle-flag-rotate-y"></a>

[bool](class_bool.md#class-bool) **particle_flag_rotate_y** = `false` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-particle-flag-rotate-y)

- void **set_particle_flag**(particle_flag: [ParticleFlags](class_cpuparticles3d.md#enum-cpuparticles3d-particleflags), enable: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_particle_flag**(particle_flag: [ParticleFlags](class_cpuparticles3d.md#enum-cpuparticles3d-particleflags)) const

If `true`, particles rotate around Y axis by [angle_min](class_cpuparticles3d.md#class-cpuparticles3d-property-angle-min).

---


<a id="class-cpuparticles3d-property-preprocess"></a>

[float](class_float.md#class-float) **preprocess** = `0.0` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-preprocess)

- void **set_pre_process_time**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_pre_process_time**()

Particle system starts as if it had already run for this many seconds.

---


<a id="class-cpuparticles3d-property-radial-accel-curve"></a>

[Curve](class_curve.md#class-curve) **radial_accel_curve** [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-radial-accel-curve)

- void **set_param_curve**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter), curve: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_param_curve**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter)) const

Each particle's radial acceleration will vary along this [Curve](class_curve.md#class-curve). Should be a unit [Curve](class_curve.md#class-curve).

---


<a id="class-cpuparticles3d-property-radial-accel-max"></a>

[float](class_float.md#class-float) **radial_accel_max** = `0.0` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-radial-accel-max)

- void **set_param_max**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter)) const

Maximum radial acceleration.

---


<a id="class-cpuparticles3d-property-radial-accel-min"></a>

[float](class_float.md#class-float) **radial_accel_min** = `0.0` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-radial-accel-min)

- void **set_param_min**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter)) const

Minimum radial acceleration.

---


<a id="class-cpuparticles3d-property-randomness"></a>

[float](class_float.md#class-float) **randomness** = `0.0` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-randomness)

- void **set_randomness_ratio**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_randomness_ratio**()

Emission lifetime randomness ratio.

---


<a id="class-cpuparticles3d-property-scale-amount-curve"></a>

[Curve](class_curve.md#class-curve) **scale_amount_curve** [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-scale-amount-curve)

- void **set_param_curve**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter), curve: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_param_curve**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter)) const

Each particle's scale will vary along this [Curve](class_curve.md#class-curve). Should be a unit [Curve](class_curve.md#class-curve).

---


<a id="class-cpuparticles3d-property-scale-amount-max"></a>

[float](class_float.md#class-float) **scale_amount_max** = `1.0` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-scale-amount-max)

- void **set_param_max**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter)) const

Maximum scale.

---


<a id="class-cpuparticles3d-property-scale-amount-min"></a>

[float](class_float.md#class-float) **scale_amount_min** = `1.0` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-scale-amount-min)

- void **set_param_min**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter)) const

Minimum scale.

---


<a id="class-cpuparticles3d-property-scale-curve-x"></a>

[Curve](class_curve.md#class-curve) **scale_curve_x** [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-scale-curve-x)

- void **set_scale_curve_x**(value: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_scale_curve_x**()

Curve for the scale over life, along the x axis.

---


<a id="class-cpuparticles3d-property-scale-curve-y"></a>

[Curve](class_curve.md#class-curve) **scale_curve_y** [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-scale-curve-y)

- void **set_scale_curve_y**(value: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_scale_curve_y**()

Curve for the scale over life, along the y axis.

---


<a id="class-cpuparticles3d-property-scale-curve-z"></a>

[Curve](class_curve.md#class-curve) **scale_curve_z** [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-scale-curve-z)

- void **set_scale_curve_z**(value: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_scale_curve_z**()

Curve for the scale over life, along the z axis.

---


<a id="class-cpuparticles3d-property-seed"></a>

[int](class_int.md#class-int) **seed** = `0` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-seed)

- void **set_seed**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_seed**()

Sets the random seed used by the particle system. Only effective if [use_fixed_seed](class_cpuparticles3d.md#class-cpuparticles3d-property-use-fixed-seed) is `true`.

---


<a id="class-cpuparticles3d-property-speed-scale"></a>

[float](class_float.md#class-float) **speed_scale** = `1.0` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-speed-scale)

- void **set_speed_scale**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_speed_scale**()

Particle system's running speed scaling ratio. A value of `0` can be used to pause the particles.

---


<a id="class-cpuparticles3d-property-split-scale"></a>

[bool](class_bool.md#class-bool) **split_scale** = `false` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-split-scale)

- void **set_split_scale**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_split_scale**()

If set to `true`, three different scale curves can be specified, one per scale axis.

---


<a id="class-cpuparticles3d-property-spread"></a>

[float](class_float.md#class-float) **spread** = `45.0` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-spread)

- void **set_spread**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_spread**()

Each particle's initial direction range from `+spread` to `-spread` degrees. Applied to X/Z plane and Y/Z planes.

---


<a id="class-cpuparticles3d-property-tangential-accel-curve"></a>

[Curve](class_curve.md#class-curve) **tangential_accel_curve** [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-tangential-accel-curve)

- void **set_param_curve**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter), curve: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_param_curve**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter)) const

Each particle's tangential acceleration will vary along this [Curve](class_curve.md#class-curve). Should be a unit [Curve](class_curve.md#class-curve).

---


<a id="class-cpuparticles3d-property-tangential-accel-max"></a>

[float](class_float.md#class-float) **tangential_accel_max** = `0.0` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-tangential-accel-max)

- void **set_param_max**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter)) const

Maximum tangent acceleration.

---


<a id="class-cpuparticles3d-property-tangential-accel-min"></a>

[float](class_float.md#class-float) **tangential_accel_min** = `0.0` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-tangential-accel-min)

- void **set_param_min**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter)) const

Minimum tangent acceleration.

---


<a id="class-cpuparticles3d-property-use-fixed-seed"></a>

[bool](class_bool.md#class-bool) **use_fixed_seed** = `false` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-use-fixed-seed)

- void **set_use_fixed_seed**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_use_fixed_seed**()

If `true`, particles will use the same seed for every simulation using the seed defined in [seed](class_cpuparticles3d.md#class-cpuparticles3d-property-seed). This is useful for situations where the visual outcome should be consistent across replays, for example when using Movie Maker mode.

---


<a id="class-cpuparticles3d-property-visibility-aabb"></a>

[AABB](class_aabb.md#class-aabb) **visibility_aabb** = `AABB(0, 0, 0, 0, 0, 0)` [🔗](class_cpuparticles3d.md#class-cpuparticles3d-property-visibility-aabb)

- void **set_visibility_aabb**(value: [AABB](class_aabb.md#class-aabb))
- [AABB](class_aabb.md#class-aabb) **get_visibility_aabb**()

The [AABB](class_aabb.md#class-aabb) that determines the node's region which needs to be visible on screen for the particle system to be active.

Grow the box if particles suddenly appear/disappear when the node enters/exits the screen. The [AABB](class_aabb.md#class-aabb) can be grown via code or with the **Particles → Generate AABB** editor tool.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-cpuparticles3d-method-capture-aabb"></a>

[AABB](class_aabb.md#class-aabb) **capture_aabb**() const [🔗](class_cpuparticles3d.md#class-cpuparticles3d-method-capture-aabb)

Returns the axis-aligned bounding box that contains all the particles that are active in the current frame.

---


<a id="class-cpuparticles3d-method-convert-from-particles"></a>

void **convert_from_particles**(particles: [Node](class_node.md#class-node)) [🔗](class_cpuparticles3d.md#class-cpuparticles3d-method-convert-from-particles)

Sets this node's properties to match a given [GPUParticles3D](class_gpuparticles3d.md#class-gpuparticles3d) node with an assigned [ParticleProcessMaterial](class_particleprocessmaterial.md#class-particleprocessmaterial).

---


<a id="class-cpuparticles3d-method-get-param-curve"></a>

[Curve](class_curve.md#class-curve) **get_param_curve**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter)) const [🔗](class_cpuparticles3d.md#class-cpuparticles3d-method-get-param-curve)

Returns the [Curve](class_curve.md#class-curve) of the parameter specified by [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter).

---


<a id="class-cpuparticles3d-method-get-param-max"></a>

[float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter)) const [🔗](class_cpuparticles3d.md#class-cpuparticles3d-method-get-param-max)

Returns the maximum value range for the given parameter.

---


<a id="class-cpuparticles3d-method-get-param-min"></a>

[float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter)) const [🔗](class_cpuparticles3d.md#class-cpuparticles3d-method-get-param-min)

Returns the minimum value range for the given parameter.

---


<a id="class-cpuparticles3d-method-get-particle-flag"></a>

[bool](class_bool.md#class-bool) **get_particle_flag**(particle_flag: [ParticleFlags](class_cpuparticles3d.md#enum-cpuparticles3d-particleflags)) const [🔗](class_cpuparticles3d.md#class-cpuparticles3d-method-get-particle-flag)

Returns the enabled state of the given particle flag.

---


<a id="class-cpuparticles3d-method-request-particles-process"></a>

void **request_particles_process**(process_time: [float](class_float.md#class-float), process_time_residual: [float](class_float.md#class-float) = 0.0) [🔗](class_cpuparticles3d.md#class-cpuparticles3d-method-request-particles-process)

Requests the particles to process for extra process time during a single frame.

`process_time` defines the time that the particles will process while emitting is on. `process_time_residual` defines the time that particles will process with emitting turned off for the simulation. When combined with [speed_scale](class_cpuparticles3d.md#class-cpuparticles3d-property-speed-scale) set to `0.0`, this is useful to be able to seek a particle system timeline.

---


<a id="class-cpuparticles3d-method-restart"></a>

void **restart**(keep_seed: [bool](class_bool.md#class-bool) = false) [🔗](class_cpuparticles3d.md#class-cpuparticles3d-method-restart)

Restarts the particle emitter.

If `keep_seed` is `true`, the current random seed will be preserved. Useful for seeking and playback.

---


<a id="class-cpuparticles3d-method-set-param-curve"></a>

void **set_param_curve**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter), curve: [Curve](class_curve.md#class-curve)) [🔗](class_cpuparticles3d.md#class-cpuparticles3d-method-set-param-curve)

Sets the [Curve](class_curve.md#class-curve) of the parameter specified by [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter). Should be a unit [Curve](class_curve.md#class-curve).

---


<a id="class-cpuparticles3d-method-set-param-max"></a>

void **set_param_max**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter), value: [float](class_float.md#class-float)) [🔗](class_cpuparticles3d.md#class-cpuparticles3d-method-set-param-max)

Sets the maximum value for the given parameter.

---


<a id="class-cpuparticles3d-method-set-param-min"></a>

void **set_param_min**(param: [Parameter](class_cpuparticles3d.md#enum-cpuparticles3d-parameter), value: [float](class_float.md#class-float)) [🔗](class_cpuparticles3d.md#class-cpuparticles3d-method-set-param-min)

Sets the minimum value for the given parameter.

---


<a id="class-cpuparticles3d-method-set-particle-flag"></a>

void **set_particle_flag**(particle_flag: [ParticleFlags](class_cpuparticles3d.md#enum-cpuparticles3d-particleflags), enable: [bool](class_bool.md#class-bool)) [🔗](class_cpuparticles3d.md#class-cpuparticles3d-method-set-particle-flag)

Enables or disables the given particle flag.
