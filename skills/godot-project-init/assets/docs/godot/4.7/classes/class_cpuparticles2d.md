> Source: https://docs.godotengine.org/en/4.7/classes/class_cpuparticles2d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="cpuparticles2d"></a>

<a id="class-cpuparticles2d"></a>

# CPUParticles2D

**Inherits:** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A CPU-based 2D particle emitter.

<a id="description"></a>

## Description

CPU-based 2D particle node used to create a variety of particle systems and effects.

See also [GPUParticles2D](class_gpuparticles2d.md#class-gpuparticles2d), which provides the same functionality with hardware acceleration, but may not run on older devices.

<a id="tutorials"></a>

## Tutorials

- [Particle systems (2D)](../tutorials/2d/particle_systems_2d.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [amount](class_cpuparticles2d.md#class-cpuparticles2d-property-amount) | `8` |
| [Curve](class_curve.md#class-curve) | [angle_curve](class_cpuparticles2d.md#class-cpuparticles2d-property-angle-curve) |  |
| [float](class_float.md#class-float) | [angle_max](class_cpuparticles2d.md#class-cpuparticles2d-property-angle-max) | `0.0` |
| [float](class_float.md#class-float) | [angle_min](class_cpuparticles2d.md#class-cpuparticles2d-property-angle-min) | `0.0` |
| [Curve](class_curve.md#class-curve) | [angular_velocity_curve](class_cpuparticles2d.md#class-cpuparticles2d-property-angular-velocity-curve) |  |
| [float](class_float.md#class-float) | [angular_velocity_max](class_cpuparticles2d.md#class-cpuparticles2d-property-angular-velocity-max) | `0.0` |
| [float](class_float.md#class-float) | [angular_velocity_min](class_cpuparticles2d.md#class-cpuparticles2d-property-angular-velocity-min) | `0.0` |
| [Curve](class_curve.md#class-curve) | [anim_offset_curve](class_cpuparticles2d.md#class-cpuparticles2d-property-anim-offset-curve) |  |
| [float](class_float.md#class-float) | [anim_offset_max](class_cpuparticles2d.md#class-cpuparticles2d-property-anim-offset-max) | `0.0` |
| [float](class_float.md#class-float) | [anim_offset_min](class_cpuparticles2d.md#class-cpuparticles2d-property-anim-offset-min) | `0.0` |
| [Curve](class_curve.md#class-curve) | [anim_speed_curve](class_cpuparticles2d.md#class-cpuparticles2d-property-anim-speed-curve) |  |
| [float](class_float.md#class-float) | [anim_speed_max](class_cpuparticles2d.md#class-cpuparticles2d-property-anim-speed-max) | `0.0` |
| [float](class_float.md#class-float) | [anim_speed_min](class_cpuparticles2d.md#class-cpuparticles2d-property-anim-speed-min) | `0.0` |
| [Color](class_color.md#class-color) | [color](class_cpuparticles2d.md#class-cpuparticles2d-property-color) | `Color(1, 1, 1, 1)` |
| [Gradient](class_gradient.md#class-gradient) | [color_initial_ramp](class_cpuparticles2d.md#class-cpuparticles2d-property-color-initial-ramp) |  |
| [Gradient](class_gradient.md#class-gradient) | [color_ramp](class_cpuparticles2d.md#class-cpuparticles2d-property-color-ramp) |  |
| [Curve](class_curve.md#class-curve) | [damping_curve](class_cpuparticles2d.md#class-cpuparticles2d-property-damping-curve) |  |
| [float](class_float.md#class-float) | [damping_max](class_cpuparticles2d.md#class-cpuparticles2d-property-damping-max) | `0.0` |
| [float](class_float.md#class-float) | [damping_min](class_cpuparticles2d.md#class-cpuparticles2d-property-damping-min) | `0.0` |
| [Vector2](class_vector2.md#class-vector2) | [direction](class_cpuparticles2d.md#class-cpuparticles2d-property-direction) | `Vector2(1, 0)` |
| [DrawOrder](class_cpuparticles2d.md#enum-cpuparticles2d-draworder) | [draw_order](class_cpuparticles2d.md#class-cpuparticles2d-property-draw-order) | `0` |
| [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) | [emission_colors](class_cpuparticles2d.md#class-cpuparticles2d-property-emission-colors) |  |
| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) | [emission_normals](class_cpuparticles2d.md#class-cpuparticles2d-property-emission-normals) |  |
| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) | [emission_points](class_cpuparticles2d.md#class-cpuparticles2d-property-emission-points) |  |
| [Vector2](class_vector2.md#class-vector2) | [emission_rect_extents](class_cpuparticles2d.md#class-cpuparticles2d-property-emission-rect-extents) |  |
| [float](class_float.md#class-float) | [emission_ring_inner_radius](class_cpuparticles2d.md#class-cpuparticles2d-property-emission-ring-inner-radius) |  |
| [float](class_float.md#class-float) | [emission_ring_radius](class_cpuparticles2d.md#class-cpuparticles2d-property-emission-ring-radius) |  |
| [EmissionShape](class_cpuparticles2d.md#enum-cpuparticles2d-emissionshape) | [emission_shape](class_cpuparticles2d.md#class-cpuparticles2d-property-emission-shape) | `0` |
| [float](class_float.md#class-float) | [emission_sphere_radius](class_cpuparticles2d.md#class-cpuparticles2d-property-emission-sphere-radius) |  |
| [bool](class_bool.md#class-bool) | [emitting](class_cpuparticles2d.md#class-cpuparticles2d-property-emitting) | `true` |
| [float](class_float.md#class-float) | [explosiveness](class_cpuparticles2d.md#class-cpuparticles2d-property-explosiveness) | `0.0` |
| [int](class_int.md#class-int) | [fixed_fps](class_cpuparticles2d.md#class-cpuparticles2d-property-fixed-fps) | `0` |
| [bool](class_bool.md#class-bool) | [fract_delta](class_cpuparticles2d.md#class-cpuparticles2d-property-fract-delta) | `true` |
| [Vector2](class_vector2.md#class-vector2) | [gravity](class_cpuparticles2d.md#class-cpuparticles2d-property-gravity) | `Vector2(0, 980)` |
| [Curve](class_curve.md#class-curve) | [hue_variation_curve](class_cpuparticles2d.md#class-cpuparticles2d-property-hue-variation-curve) |  |
| [float](class_float.md#class-float) | [hue_variation_max](class_cpuparticles2d.md#class-cpuparticles2d-property-hue-variation-max) | `0.0` |
| [float](class_float.md#class-float) | [hue_variation_min](class_cpuparticles2d.md#class-cpuparticles2d-property-hue-variation-min) | `0.0` |
| [float](class_float.md#class-float) | [initial_velocity_max](class_cpuparticles2d.md#class-cpuparticles2d-property-initial-velocity-max) | `0.0` |
| [float](class_float.md#class-float) | [initial_velocity_min](class_cpuparticles2d.md#class-cpuparticles2d-property-initial-velocity-min) | `0.0` |
| [float](class_float.md#class-float) | [lifetime](class_cpuparticles2d.md#class-cpuparticles2d-property-lifetime) | `1.0` |
| [float](class_float.md#class-float) | [lifetime_randomness](class_cpuparticles2d.md#class-cpuparticles2d-property-lifetime-randomness) | `0.0` |
| [Curve](class_curve.md#class-curve) | [linear_accel_curve](class_cpuparticles2d.md#class-cpuparticles2d-property-linear-accel-curve) |  |
| [float](class_float.md#class-float) | [linear_accel_max](class_cpuparticles2d.md#class-cpuparticles2d-property-linear-accel-max) | `0.0` |
| [float](class_float.md#class-float) | [linear_accel_min](class_cpuparticles2d.md#class-cpuparticles2d-property-linear-accel-min) | `0.0` |
| [bool](class_bool.md#class-bool) | [local_coords](class_cpuparticles2d.md#class-cpuparticles2d-property-local-coords) | `false` |
| [bool](class_bool.md#class-bool) | [one_shot](class_cpuparticles2d.md#class-cpuparticles2d-property-one-shot) | `false` |
| [Curve](class_curve.md#class-curve) | [orbit_velocity_curve](class_cpuparticles2d.md#class-cpuparticles2d-property-orbit-velocity-curve) |  |
| [float](class_float.md#class-float) | [orbit_velocity_max](class_cpuparticles2d.md#class-cpuparticles2d-property-orbit-velocity-max) | `0.0` |
| [float](class_float.md#class-float) | [orbit_velocity_min](class_cpuparticles2d.md#class-cpuparticles2d-property-orbit-velocity-min) | `0.0` |
| [bool](class_bool.md#class-bool) | [particle_flag_align_y](class_cpuparticles2d.md#class-cpuparticles2d-property-particle-flag-align-y) | `false` |
| [PhysicsInterpolationMode](class_node.md#enum-node-physicsinterpolationmode) | physics_interpolation_mode | `2` (overrides [Node](class_node.md#class-node-property-physics-interpolation-mode)) |
| [float](class_float.md#class-float) | [preprocess](class_cpuparticles2d.md#class-cpuparticles2d-property-preprocess) | `0.0` |
| [Curve](class_curve.md#class-curve) | [radial_accel_curve](class_cpuparticles2d.md#class-cpuparticles2d-property-radial-accel-curve) |  |
| [float](class_float.md#class-float) | [radial_accel_max](class_cpuparticles2d.md#class-cpuparticles2d-property-radial-accel-max) | `0.0` |
| [float](class_float.md#class-float) | [radial_accel_min](class_cpuparticles2d.md#class-cpuparticles2d-property-radial-accel-min) | `0.0` |
| [float](class_float.md#class-float) | [randomness](class_cpuparticles2d.md#class-cpuparticles2d-property-randomness) | `0.0` |
| [Curve](class_curve.md#class-curve) | [scale_amount_curve](class_cpuparticles2d.md#class-cpuparticles2d-property-scale-amount-curve) |  |
| [float](class_float.md#class-float) | [scale_amount_max](class_cpuparticles2d.md#class-cpuparticles2d-property-scale-amount-max) | `1.0` |
| [float](class_float.md#class-float) | [scale_amount_min](class_cpuparticles2d.md#class-cpuparticles2d-property-scale-amount-min) | `1.0` |
| [Curve](class_curve.md#class-curve) | [scale_curve_x](class_cpuparticles2d.md#class-cpuparticles2d-property-scale-curve-x) |  |
| [Curve](class_curve.md#class-curve) | [scale_curve_y](class_cpuparticles2d.md#class-cpuparticles2d-property-scale-curve-y) |  |
| [int](class_int.md#class-int) | [seed](class_cpuparticles2d.md#class-cpuparticles2d-property-seed) | `0` |
| [float](class_float.md#class-float) | [speed_scale](class_cpuparticles2d.md#class-cpuparticles2d-property-speed-scale) | `1.0` |
| [bool](class_bool.md#class-bool) | [split_scale](class_cpuparticles2d.md#class-cpuparticles2d-property-split-scale) | `false` |
| [float](class_float.md#class-float) | [spread](class_cpuparticles2d.md#class-cpuparticles2d-property-spread) | `45.0` |
| [Curve](class_curve.md#class-curve) | [tangential_accel_curve](class_cpuparticles2d.md#class-cpuparticles2d-property-tangential-accel-curve) |  |
| [float](class_float.md#class-float) | [tangential_accel_max](class_cpuparticles2d.md#class-cpuparticles2d-property-tangential-accel-max) | `0.0` |
| [float](class_float.md#class-float) | [tangential_accel_min](class_cpuparticles2d.md#class-cpuparticles2d-property-tangential-accel-min) | `0.0` |
| [Texture2D](class_texture2d.md#class-texture2d) | [texture](class_cpuparticles2d.md#class-cpuparticles2d-property-texture) |  |
| [bool](class_bool.md#class-bool) | [use_fixed_seed](class_cpuparticles2d.md#class-cpuparticles2d-property-use-fixed-seed) | `false` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [convert_from_particles](class_cpuparticles2d.md#class-cpuparticles2d-method-convert-from-particles)(particles: [Node](class_node.md#class-node)) |
| [Curve](class_curve.md#class-curve) | [get_param_curve](class_cpuparticles2d.md#class-cpuparticles2d-method-get-param-curve)(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter)) const |
| [float](class_float.md#class-float) | [get_param_max](class_cpuparticles2d.md#class-cpuparticles2d-method-get-param-max)(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter)) const |
| [float](class_float.md#class-float) | [get_param_min](class_cpuparticles2d.md#class-cpuparticles2d-method-get-param-min)(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter)) const |
| [bool](class_bool.md#class-bool) | [get_particle_flag](class_cpuparticles2d.md#class-cpuparticles2d-method-get-particle-flag)(particle_flag: [ParticleFlags](class_cpuparticles2d.md#enum-cpuparticles2d-particleflags)) const |
| void | [request_particles_process](class_cpuparticles2d.md#class-cpuparticles2d-method-request-particles-process)(process_time: [float](class_float.md#class-float), process_time_residual: [float](class_float.md#class-float) = 0.0) |
| void | [restart](class_cpuparticles2d.md#class-cpuparticles2d-method-restart)(keep_seed: [bool](class_bool.md#class-bool) = false) |
| void | [set_param_curve](class_cpuparticles2d.md#class-cpuparticles2d-method-set-param-curve)(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter), curve: [Curve](class_curve.md#class-curve)) |
| void | [set_param_max](class_cpuparticles2d.md#class-cpuparticles2d-method-set-param-max)(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter), value: [float](class_float.md#class-float)) |
| void | [set_param_min](class_cpuparticles2d.md#class-cpuparticles2d-method-set-param-min)(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter), value: [float](class_float.md#class-float)) |
| void | [set_particle_flag](class_cpuparticles2d.md#class-cpuparticles2d-method-set-particle-flag)(particle_flag: [ParticleFlags](class_cpuparticles2d.md#enum-cpuparticles2d-particleflags), enable: [bool](class_bool.md#class-bool)) |

---


<a id="signals"></a>

## Signals

<a id="class-cpuparticles2d-signal-finished"></a>

**finished**() [🔗](class_cpuparticles2d.md#class-cpuparticles2d-signal-finished)

Emitted when all active particles have finished processing. When [one_shot](class_cpuparticles2d.md#class-cpuparticles2d-property-one-shot) is disabled, particles will process continuously, so this is never emitted.

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-cpuparticles2d-draworder"></a>

enum **DrawOrder**: [🔗](class_cpuparticles2d.md#enum-cpuparticles2d-draworder)

<a id="class-cpuparticles2d-constant-draw-order-index"></a>

[DrawOrder](class_cpuparticles2d.md#enum-cpuparticles2d-draworder) **DRAW_ORDER_INDEX** = `0`

Particles are drawn in the order emitted.

<a id="class-cpuparticles2d-constant-draw-order-lifetime"></a>

[DrawOrder](class_cpuparticles2d.md#enum-cpuparticles2d-draworder) **DRAW_ORDER_LIFETIME** = `1`

Particles are drawn in order of remaining lifetime. In other words, the particle with the highest lifetime is drawn at the front.

---


<a id="enum-cpuparticles2d-parameter"></a>

enum **Parameter**: [🔗](class_cpuparticles2d.md#enum-cpuparticles2d-parameter)

<a id="class-cpuparticles2d-constant-param-initial-linear-velocity"></a>

[Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter) **PARAM_INITIAL_LINEAR_VELOCITY** = `0`

Use with [set_param_min()](class_cpuparticles2d.md#class-cpuparticles2d-method-set-param-min), [set_param_max()](class_cpuparticles2d.md#class-cpuparticles2d-method-set-param-max), and [set_param_curve()](class_cpuparticles2d.md#class-cpuparticles2d-method-set-param-curve) to set initial velocity properties.

<a id="class-cpuparticles2d-constant-param-angular-velocity"></a>

[Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter) **PARAM_ANGULAR_VELOCITY** = `1`

Use with [set_param_min()](class_cpuparticles2d.md#class-cpuparticles2d-method-set-param-min), [set_param_max()](class_cpuparticles2d.md#class-cpuparticles2d-method-set-param-max), and [set_param_curve()](class_cpuparticles2d.md#class-cpuparticles2d-method-set-param-curve) to set angular velocity properties.

<a id="class-cpuparticles2d-constant-param-orbit-velocity"></a>

[Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter) **PARAM_ORBIT_VELOCITY** = `2`

Use with [set_param_min()](class_cpuparticles2d.md#class-cpuparticles2d-method-set-param-min), [set_param_max()](class_cpuparticles2d.md#class-cpuparticles2d-method-set-param-max), and [set_param_curve()](class_cpuparticles2d.md#class-cpuparticles2d-method-set-param-curve) to set orbital velocity properties.

<a id="class-cpuparticles2d-constant-param-linear-accel"></a>

[Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter) **PARAM_LINEAR_ACCEL** = `3`

Use with [set_param_min()](class_cpuparticles2d.md#class-cpuparticles2d-method-set-param-min), [set_param_max()](class_cpuparticles2d.md#class-cpuparticles2d-method-set-param-max), and [set_param_curve()](class_cpuparticles2d.md#class-cpuparticles2d-method-set-param-curve) to set linear acceleration properties.

<a id="class-cpuparticles2d-constant-param-radial-accel"></a>

[Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter) **PARAM_RADIAL_ACCEL** = `4`

Use with [set_param_min()](class_cpuparticles2d.md#class-cpuparticles2d-method-set-param-min), [set_param_max()](class_cpuparticles2d.md#class-cpuparticles2d-method-set-param-max), and [set_param_curve()](class_cpuparticles2d.md#class-cpuparticles2d-method-set-param-curve) to set radial acceleration properties.

<a id="class-cpuparticles2d-constant-param-tangential-accel"></a>

[Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter) **PARAM_TANGENTIAL_ACCEL** = `5`

Use with [set_param_min()](class_cpuparticles2d.md#class-cpuparticles2d-method-set-param-min), [set_param_max()](class_cpuparticles2d.md#class-cpuparticles2d-method-set-param-max), and [set_param_curve()](class_cpuparticles2d.md#class-cpuparticles2d-method-set-param-curve) to set tangential acceleration properties.

<a id="class-cpuparticles2d-constant-param-damping"></a>

[Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter) **PARAM_DAMPING** = `6`

Use with [set_param_min()](class_cpuparticles2d.md#class-cpuparticles2d-method-set-param-min), [set_param_max()](class_cpuparticles2d.md#class-cpuparticles2d-method-set-param-max), and [set_param_curve()](class_cpuparticles2d.md#class-cpuparticles2d-method-set-param-curve) to set damping properties.

<a id="class-cpuparticles2d-constant-param-angle"></a>

[Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter) **PARAM_ANGLE** = `7`

Use with [set_param_min()](class_cpuparticles2d.md#class-cpuparticles2d-method-set-param-min), [set_param_max()](class_cpuparticles2d.md#class-cpuparticles2d-method-set-param-max), and [set_param_curve()](class_cpuparticles2d.md#class-cpuparticles2d-method-set-param-curve) to set angle properties.

<a id="class-cpuparticles2d-constant-param-scale"></a>

[Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter) **PARAM_SCALE** = `8`

Use with [set_param_min()](class_cpuparticles2d.md#class-cpuparticles2d-method-set-param-min), [set_param_max()](class_cpuparticles2d.md#class-cpuparticles2d-method-set-param-max), and [set_param_curve()](class_cpuparticles2d.md#class-cpuparticles2d-method-set-param-curve) to set scale properties.

<a id="class-cpuparticles2d-constant-param-hue-variation"></a>

[Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter) **PARAM_HUE_VARIATION** = `9`

Use with [set_param_min()](class_cpuparticles2d.md#class-cpuparticles2d-method-set-param-min), [set_param_max()](class_cpuparticles2d.md#class-cpuparticles2d-method-set-param-max), and [set_param_curve()](class_cpuparticles2d.md#class-cpuparticles2d-method-set-param-curve) to set hue variation properties.

<a id="class-cpuparticles2d-constant-param-anim-speed"></a>

[Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter) **PARAM_ANIM_SPEED** = `10`

Use with [set_param_min()](class_cpuparticles2d.md#class-cpuparticles2d-method-set-param-min), [set_param_max()](class_cpuparticles2d.md#class-cpuparticles2d-method-set-param-max), and [set_param_curve()](class_cpuparticles2d.md#class-cpuparticles2d-method-set-param-curve) to set animation speed properties.

<a id="class-cpuparticles2d-constant-param-anim-offset"></a>

[Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter) **PARAM_ANIM_OFFSET** = `11`

Use with [set_param_min()](class_cpuparticles2d.md#class-cpuparticles2d-method-set-param-min), [set_param_max()](class_cpuparticles2d.md#class-cpuparticles2d-method-set-param-max), and [set_param_curve()](class_cpuparticles2d.md#class-cpuparticles2d-method-set-param-curve) to set animation offset properties.

<a id="class-cpuparticles2d-constant-param-max"></a>

[Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter) **PARAM_MAX** = `12`

Represents the size of the [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter) enum.

---


<a id="enum-cpuparticles2d-particleflags"></a>

enum **ParticleFlags**: [🔗](class_cpuparticles2d.md#enum-cpuparticles2d-particleflags)

<a id="class-cpuparticles2d-constant-particle-flag-align-y-to-velocity"></a>

[ParticleFlags](class_cpuparticles2d.md#enum-cpuparticles2d-particleflags) **PARTICLE_FLAG_ALIGN_Y_TO_VELOCITY** = `0`

Use with [set_particle_flag()](class_cpuparticles2d.md#class-cpuparticles2d-method-set-particle-flag) to set [particle_flag_align_y](class_cpuparticles2d.md#class-cpuparticles2d-property-particle-flag-align-y).

<a id="class-cpuparticles2d-constant-particle-flag-rotate-y"></a>

[ParticleFlags](class_cpuparticles2d.md#enum-cpuparticles2d-particleflags) **PARTICLE_FLAG_ROTATE_Y** = `1`

Present for consistency with 3D particle nodes, not used in 2D.

<a id="class-cpuparticles2d-constant-particle-flag-disable-z"></a>

[ParticleFlags](class_cpuparticles2d.md#enum-cpuparticles2d-particleflags) **PARTICLE_FLAG_DISABLE_Z** = `2`

Present for consistency with 3D particle nodes, not used in 2D.

<a id="class-cpuparticles2d-constant-particle-flag-max"></a>

[ParticleFlags](class_cpuparticles2d.md#enum-cpuparticles2d-particleflags) **PARTICLE_FLAG_MAX** = `3`

Represents the size of the [ParticleFlags](class_cpuparticles2d.md#enum-cpuparticles2d-particleflags) enum.

---


<a id="enum-cpuparticles2d-emissionshape"></a>

enum **EmissionShape**: [🔗](class_cpuparticles2d.md#enum-cpuparticles2d-emissionshape)

<a id="class-cpuparticles2d-constant-emission-shape-point"></a>

[EmissionShape](class_cpuparticles2d.md#enum-cpuparticles2d-emissionshape) **EMISSION_SHAPE_POINT** = `0`

All particles will be emitted from a single point.

<a id="class-cpuparticles2d-constant-emission-shape-sphere"></a>

[EmissionShape](class_cpuparticles2d.md#enum-cpuparticles2d-emissionshape) **EMISSION_SHAPE_SPHERE** = `1`

Particles will be emitted in the volume of a sphere flattened to two dimensions.

<a id="class-cpuparticles2d-constant-emission-shape-sphere-surface"></a>

[EmissionShape](class_cpuparticles2d.md#enum-cpuparticles2d-emissionshape) **EMISSION_SHAPE_SPHERE_SURFACE** = `2`

Particles will be emitted on the surface of a sphere flattened to two dimensions.

<a id="class-cpuparticles2d-constant-emission-shape-rectangle"></a>

[EmissionShape](class_cpuparticles2d.md#enum-cpuparticles2d-emissionshape) **EMISSION_SHAPE_RECTANGLE** = `3`

Particles will be emitted in the area of a rectangle.

<a id="class-cpuparticles2d-constant-emission-shape-points"></a>

[EmissionShape](class_cpuparticles2d.md#enum-cpuparticles2d-emissionshape) **EMISSION_SHAPE_POINTS** = `4`

Particles will be emitted at a position chosen randomly among [emission_points](class_cpuparticles2d.md#class-cpuparticles2d-property-emission-points). Particle color will be modulated by [emission_colors](class_cpuparticles2d.md#class-cpuparticles2d-property-emission-colors).

<a id="class-cpuparticles2d-constant-emission-shape-directed-points"></a>

[EmissionShape](class_cpuparticles2d.md#enum-cpuparticles2d-emissionshape) **EMISSION_SHAPE_DIRECTED_POINTS** = `5`

Particles will be emitted at a position chosen randomly among [emission_points](class_cpuparticles2d.md#class-cpuparticles2d-property-emission-points). Particle velocity and rotation will be set based on [emission_normals](class_cpuparticles2d.md#class-cpuparticles2d-property-emission-normals). Particle color will be modulated by [emission_colors](class_cpuparticles2d.md#class-cpuparticles2d-property-emission-colors).

<a id="class-cpuparticles2d-constant-emission-shape-ring"></a>

[EmissionShape](class_cpuparticles2d.md#enum-cpuparticles2d-emissionshape) **EMISSION_SHAPE_RING** = `6`

Particles will be emitted in the area of a ring parameterized by its outer and inner radius.

<a id="class-cpuparticles2d-constant-emission-shape-max"></a>

[EmissionShape](class_cpuparticles2d.md#enum-cpuparticles2d-emissionshape) **EMISSION_SHAPE_MAX** = `7`

Represents the size of the [EmissionShape](class_cpuparticles2d.md#enum-cpuparticles2d-emissionshape) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-cpuparticles2d-property-amount"></a>

[int](class_int.md#class-int) **amount** = `8` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-amount)

- void **set_amount**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_amount**()

Number of particles emitted in one emission cycle.

---


<a id="class-cpuparticles2d-property-angle-curve"></a>

[Curve](class_curve.md#class-curve) **angle_curve** [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-angle-curve)

- void **set_param_curve**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter), curve: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_param_curve**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter)) const

Each particle's rotation will be animated along this [Curve](class_curve.md#class-curve). Should be a unit [Curve](class_curve.md#class-curve).

---


<a id="class-cpuparticles2d-property-angle-max"></a>

[float](class_float.md#class-float) **angle_max** = `0.0` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-angle-max)

- void **set_param_max**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter)) const

Maximum initial rotation applied to each particle, in degrees.

---


<a id="class-cpuparticles2d-property-angle-min"></a>

[float](class_float.md#class-float) **angle_min** = `0.0` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-angle-min)

- void **set_param_min**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter)) const

Minimum equivalent of [angle_max](class_cpuparticles2d.md#class-cpuparticles2d-property-angle-max).

---


<a id="class-cpuparticles2d-property-angular-velocity-curve"></a>

[Curve](class_curve.md#class-curve) **angular_velocity_curve** [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-angular-velocity-curve)

- void **set_param_curve**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter), curve: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_param_curve**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter)) const

Each particle's angular velocity will vary along this [Curve](class_curve.md#class-curve). Should be a unit [Curve](class_curve.md#class-curve).

---


<a id="class-cpuparticles2d-property-angular-velocity-max"></a>

[float](class_float.md#class-float) **angular_velocity_max** = `0.0` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-angular-velocity-max)

- void **set_param_max**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter)) const

Maximum initial angular velocity (rotation speed) applied to each particle in *degrees* per second.

---


<a id="class-cpuparticles2d-property-angular-velocity-min"></a>

[float](class_float.md#class-float) **angular_velocity_min** = `0.0` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-angular-velocity-min)

- void **set_param_min**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter)) const

Minimum equivalent of [angular_velocity_max](class_cpuparticles2d.md#class-cpuparticles2d-property-angular-velocity-max).

---


<a id="class-cpuparticles2d-property-anim-offset-curve"></a>

[Curve](class_curve.md#class-curve) **anim_offset_curve** [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-anim-offset-curve)

- void **set_param_curve**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter), curve: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_param_curve**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter)) const

Each particle's animation offset will vary along this [Curve](class_curve.md#class-curve). Should be a unit [Curve](class_curve.md#class-curve).

---


<a id="class-cpuparticles2d-property-anim-offset-max"></a>

[float](class_float.md#class-float) **anim_offset_max** = `0.0` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-anim-offset-max)

- void **set_param_max**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter)) const

Maximum animation offset that corresponds to frame index in the texture. `0` is the first frame, `1` is the last one. See [CanvasItemMaterial.particles_animation](class_canvasitemmaterial.md#class-canvasitemmaterial-property-particles-animation).

---


<a id="class-cpuparticles2d-property-anim-offset-min"></a>

[float](class_float.md#class-float) **anim_offset_min** = `0.0` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-anim-offset-min)

- void **set_param_min**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter)) const

Minimum equivalent of [anim_offset_max](class_cpuparticles2d.md#class-cpuparticles2d-property-anim-offset-max).

---


<a id="class-cpuparticles2d-property-anim-speed-curve"></a>

[Curve](class_curve.md#class-curve) **anim_speed_curve** [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-anim-speed-curve)

- void **set_param_curve**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter), curve: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_param_curve**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter)) const

Each particle's animation speed will vary along this [Curve](class_curve.md#class-curve). Should be a unit [Curve](class_curve.md#class-curve).

---


<a id="class-cpuparticles2d-property-anim-speed-max"></a>

[float](class_float.md#class-float) **anim_speed_max** = `0.0` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-anim-speed-max)

- void **set_param_max**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter)) const

Maximum particle animation speed. Animation speed of `1` means that the particles will make full `0` to `1` offset cycle during lifetime, `2` means `2` cycles etc.

With animation speed greater than `1`, remember to enable [CanvasItemMaterial.particles_anim_loop](class_canvasitemmaterial.md#class-canvasitemmaterial-property-particles-anim-loop) property if you want the animation to repeat.

---


<a id="class-cpuparticles2d-property-anim-speed-min"></a>

[float](class_float.md#class-float) **anim_speed_min** = `0.0` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-anim-speed-min)

- void **set_param_min**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter)) const

Minimum equivalent of [anim_speed_max](class_cpuparticles2d.md#class-cpuparticles2d-property-anim-speed-max).

---


<a id="class-cpuparticles2d-property-color"></a>

[Color](class_color.md#class-color) **color** = `Color(1, 1, 1, 1)` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-color)

- void **set_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_color**()

Each particle's initial color. If [texture](class_cpuparticles2d.md#class-cpuparticles2d-property-texture) is defined, it will be multiplied by this color.

---


<a id="class-cpuparticles2d-property-color-initial-ramp"></a>

[Gradient](class_gradient.md#class-gradient) **color_initial_ramp** [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-color-initial-ramp)

- void **set_color_initial_ramp**(value: [Gradient](class_gradient.md#class-gradient))
- [Gradient](class_gradient.md#class-gradient) **get_color_initial_ramp**()

Each particle's initial color will vary along this [Gradient](class_gradient.md#class-gradient) (multiplied with [color](class_cpuparticles2d.md#class-cpuparticles2d-property-color)).

---


<a id="class-cpuparticles2d-property-color-ramp"></a>

[Gradient](class_gradient.md#class-gradient) **color_ramp** [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-color-ramp)

- void **set_color_ramp**(value: [Gradient](class_gradient.md#class-gradient))
- [Gradient](class_gradient.md#class-gradient) **get_color_ramp**()

Each particle's color will vary along this [Gradient](class_gradient.md#class-gradient) over its lifetime (multiplied with [color](class_cpuparticles2d.md#class-cpuparticles2d-property-color)).

---


<a id="class-cpuparticles2d-property-damping-curve"></a>

[Curve](class_curve.md#class-curve) **damping_curve** [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-damping-curve)

- void **set_param_curve**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter), curve: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_param_curve**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter)) const

Damping will vary along this [Curve](class_curve.md#class-curve). Should be a unit [Curve](class_curve.md#class-curve).

---


<a id="class-cpuparticles2d-property-damping-max"></a>

[float](class_float.md#class-float) **damping_max** = `0.0` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-damping-max)

- void **set_param_max**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter)) const

The maximum rate at which particles lose velocity. For example value of `100` means that the particle will go from `100` velocity to `0` in `1` second.

---


<a id="class-cpuparticles2d-property-damping-min"></a>

[float](class_float.md#class-float) **damping_min** = `0.0` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-damping-min)

- void **set_param_min**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter)) const

Minimum equivalent of [damping_max](class_cpuparticles2d.md#class-cpuparticles2d-property-damping-max).

---


<a id="class-cpuparticles2d-property-direction"></a>

[Vector2](class_vector2.md#class-vector2) **direction** = `Vector2(1, 0)` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-direction)

- void **set_direction**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_direction**()

Unit vector specifying the particles' emission direction.

---


<a id="class-cpuparticles2d-property-draw-order"></a>

[DrawOrder](class_cpuparticles2d.md#enum-cpuparticles2d-draworder) **draw_order** = `0` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-draw-order)

- void **set_draw_order**(value: [DrawOrder](class_cpuparticles2d.md#enum-cpuparticles2d-draworder))
- [DrawOrder](class_cpuparticles2d.md#enum-cpuparticles2d-draworder) **get_draw_order**()

Particle draw order.

---


<a id="class-cpuparticles2d-property-emission-colors"></a>

[PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) **emission_colors** [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-emission-colors)

- void **set_emission_colors**(value: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray))
- [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) **get_emission_colors**()

Sets the [Color](class_color.md#class-color)s to modulate particles by when using [EMISSION_SHAPE_POINTS](class_cpuparticles2d.md#class-cpuparticles2d-constant-emission-shape-points) or [EMISSION_SHAPE_DIRECTED_POINTS](class_cpuparticles2d.md#class-cpuparticles2d-constant-emission-shape-directed-points).

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) for more details.

---


<a id="class-cpuparticles2d-property-emission-normals"></a>

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **emission_normals** [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-emission-normals)

- void **set_emission_normals**(value: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array))
- [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **get_emission_normals**()

Sets the direction the particles will be emitted in when using [EMISSION_SHAPE_DIRECTED_POINTS](class_cpuparticles2d.md#class-cpuparticles2d-constant-emission-shape-directed-points).

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) for more details.

---


<a id="class-cpuparticles2d-property-emission-points"></a>

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **emission_points** [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-emission-points)

- void **set_emission_points**(value: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array))
- [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **get_emission_points**()

Sets the initial positions to spawn particles when using [EMISSION_SHAPE_POINTS](class_cpuparticles2d.md#class-cpuparticles2d-constant-emission-shape-points) or [EMISSION_SHAPE_DIRECTED_POINTS](class_cpuparticles2d.md#class-cpuparticles2d-constant-emission-shape-directed-points).

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) for more details.

---


<a id="class-cpuparticles2d-property-emission-rect-extents"></a>

[Vector2](class_vector2.md#class-vector2) **emission_rect_extents** [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-emission-rect-extents)

- void **set_emission_rect_extents**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_emission_rect_extents**()

The rectangle's extents if [emission_shape](class_cpuparticles2d.md#class-cpuparticles2d-property-emission-shape) is set to [EMISSION_SHAPE_RECTANGLE](class_cpuparticles2d.md#class-cpuparticles2d-constant-emission-shape-rectangle).

---


<a id="class-cpuparticles2d-property-emission-ring-inner-radius"></a>

[float](class_float.md#class-float) **emission_ring_inner_radius** [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-emission-ring-inner-radius)

- void **set_emission_ring_inner_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_emission_ring_inner_radius**()

The ring's inner radius if [emission_shape](class_cpuparticles2d.md#class-cpuparticles2d-property-emission-shape) is set to [EMISSION_SHAPE_RING](class_cpuparticles2d.md#class-cpuparticles2d-constant-emission-shape-ring).

---


<a id="class-cpuparticles2d-property-emission-ring-radius"></a>

[float](class_float.md#class-float) **emission_ring_radius** [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-emission-ring-radius)

- void **set_emission_ring_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_emission_ring_radius**()

The ring's outer radius if [emission_shape](class_cpuparticles2d.md#class-cpuparticles2d-property-emission-shape) is set to [EMISSION_SHAPE_RING](class_cpuparticles2d.md#class-cpuparticles2d-constant-emission-shape-ring).

---


<a id="class-cpuparticles2d-property-emission-shape"></a>

[EmissionShape](class_cpuparticles2d.md#enum-cpuparticles2d-emissionshape) **emission_shape** = `0` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-emission-shape)

- void **set_emission_shape**(value: [EmissionShape](class_cpuparticles2d.md#enum-cpuparticles2d-emissionshape))
- [EmissionShape](class_cpuparticles2d.md#enum-cpuparticles2d-emissionshape) **get_emission_shape**()

Particles will be emitted inside this region.

---


<a id="class-cpuparticles2d-property-emission-sphere-radius"></a>

[float](class_float.md#class-float) **emission_sphere_radius** [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-emission-sphere-radius)

- void **set_emission_sphere_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_emission_sphere_radius**()

The sphere's radius if [emission_shape](class_cpuparticles2d.md#class-cpuparticles2d-property-emission-shape) is set to [EMISSION_SHAPE_SPHERE](class_cpuparticles2d.md#class-cpuparticles2d-constant-emission-shape-sphere).

---


<a id="class-cpuparticles2d-property-emitting"></a>

[bool](class_bool.md#class-bool) **emitting** = `true` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-emitting)

- void **set_emitting**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_emitting**()

If `true`, particles are being emitted. [emitting](class_cpuparticles2d.md#class-cpuparticles2d-property-emitting) can be used to start and stop particles from emitting. However, if [one_shot](class_cpuparticles2d.md#class-cpuparticles2d-property-one-shot) is `true` setting [emitting](class_cpuparticles2d.md#class-cpuparticles2d-property-emitting) to `true` will not restart the emission cycle until after all active particles finish processing. You can use the [finished](class_cpuparticles2d.md#class-cpuparticles2d-signal-finished) signal to be notified once all active particles finish processing.

---


<a id="class-cpuparticles2d-property-explosiveness"></a>

[float](class_float.md#class-float) **explosiveness** = `0.0` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-explosiveness)

- void **set_explosiveness_ratio**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_explosiveness_ratio**()

How rapidly particles in an emission cycle are emitted. If greater than `0`, there will be a gap in emissions before the next cycle begins.

---


<a id="class-cpuparticles2d-property-fixed-fps"></a>

[int](class_int.md#class-int) **fixed_fps** = `0` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-fixed-fps)

- void **set_fixed_fps**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_fixed_fps**()

The particle system's frame rate is fixed to a value. For example, changing the value to 2 will make the particles render at 2 frames per second. Note this does not slow down the simulation of the particle system itself.

---


<a id="class-cpuparticles2d-property-fract-delta"></a>

[bool](class_bool.md#class-bool) **fract_delta** = `true` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-fract-delta)

- void **set_fractional_delta**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_fractional_delta**()

If `true`, results in fractional delta calculation which has a smoother particles display effect.

---


<a id="class-cpuparticles2d-property-gravity"></a>

[Vector2](class_vector2.md#class-vector2) **gravity** = `Vector2(0, 980)` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-gravity)

- void **set_gravity**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_gravity**()

Gravity applied to every particle.

---


<a id="class-cpuparticles2d-property-hue-variation-curve"></a>

[Curve](class_curve.md#class-curve) **hue_variation_curve** [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-hue-variation-curve)

- void **set_param_curve**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter), curve: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_param_curve**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter)) const

Each particle's hue will vary along this [Curve](class_curve.md#class-curve). Should be a unit [Curve](class_curve.md#class-curve).

---


<a id="class-cpuparticles2d-property-hue-variation-max"></a>

[float](class_float.md#class-float) **hue_variation_max** = `0.0` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-hue-variation-max)

- void **set_param_max**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter)) const

Maximum initial hue variation applied to each particle. It will shift the particle color's hue.

---


<a id="class-cpuparticles2d-property-hue-variation-min"></a>

[float](class_float.md#class-float) **hue_variation_min** = `0.0` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-hue-variation-min)

- void **set_param_min**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter)) const

Minimum equivalent of [hue_variation_max](class_cpuparticles2d.md#class-cpuparticles2d-property-hue-variation-max).

---


<a id="class-cpuparticles2d-property-initial-velocity-max"></a>

[float](class_float.md#class-float) **initial_velocity_max** = `0.0` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-initial-velocity-max)

- void **set_param_max**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter)) const

Maximum initial velocity magnitude for each particle. Direction comes from [direction](class_cpuparticles2d.md#class-cpuparticles2d-property-direction) and [spread](class_cpuparticles2d.md#class-cpuparticles2d-property-spread).

---


<a id="class-cpuparticles2d-property-initial-velocity-min"></a>

[float](class_float.md#class-float) **initial_velocity_min** = `0.0` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-initial-velocity-min)

- void **set_param_min**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter)) const

Minimum equivalent of [initial_velocity_max](class_cpuparticles2d.md#class-cpuparticles2d-property-initial-velocity-max).

---


<a id="class-cpuparticles2d-property-lifetime"></a>

[float](class_float.md#class-float) **lifetime** = `1.0` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-lifetime)

- void **set_lifetime**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_lifetime**()

Amount of time each particle will exist.

---


<a id="class-cpuparticles2d-property-lifetime-randomness"></a>

[float](class_float.md#class-float) **lifetime_randomness** = `0.0` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-lifetime-randomness)

- void **set_lifetime_randomness**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_lifetime_randomness**()

Particle lifetime randomness ratio.

---


<a id="class-cpuparticles2d-property-linear-accel-curve"></a>

[Curve](class_curve.md#class-curve) **linear_accel_curve** [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-linear-accel-curve)

- void **set_param_curve**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter), curve: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_param_curve**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter)) const

Each particle's linear acceleration will vary along this [Curve](class_curve.md#class-curve). Should be a unit [Curve](class_curve.md#class-curve).

---


<a id="class-cpuparticles2d-property-linear-accel-max"></a>

[float](class_float.md#class-float) **linear_accel_max** = `0.0` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-linear-accel-max)

- void **set_param_max**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter)) const

Maximum linear acceleration applied to each particle in the direction of motion.

---


<a id="class-cpuparticles2d-property-linear-accel-min"></a>

[float](class_float.md#class-float) **linear_accel_min** = `0.0` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-linear-accel-min)

- void **set_param_min**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter)) const

Minimum equivalent of [linear_accel_max](class_cpuparticles2d.md#class-cpuparticles2d-property-linear-accel-max).

---


<a id="class-cpuparticles2d-property-local-coords"></a>

[bool](class_bool.md#class-bool) **local_coords** = `false` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-local-coords)

- void **set_use_local_coordinates**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_use_local_coordinates**()

If `true`, particles use the parent node's coordinate space (known as local coordinates). This will cause particles to move and rotate along the **CPUParticles2D** node (and its parents) when it is moved or rotated. If `false`, particles use global coordinates; they will not move or rotate along the **CPUParticles2D** node (and its parents) when it is moved or rotated.

---


<a id="class-cpuparticles2d-property-one-shot"></a>

[bool](class_bool.md#class-bool) **one_shot** = `false` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-one-shot)

- void **set_one_shot**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_one_shot**()

If `true`, only one emission cycle occurs. If set `true` during a cycle, emission will stop at the cycle's end.

---


<a id="class-cpuparticles2d-property-orbit-velocity-curve"></a>

[Curve](class_curve.md#class-curve) **orbit_velocity_curve** [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-orbit-velocity-curve)

- void **set_param_curve**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter), curve: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_param_curve**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter)) const

Each particle's orbital velocity will vary along this [Curve](class_curve.md#class-curve). Should be a unit [Curve](class_curve.md#class-curve).

---


<a id="class-cpuparticles2d-property-orbit-velocity-max"></a>

[float](class_float.md#class-float) **orbit_velocity_max** = `0.0` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-orbit-velocity-max)

- void **set_param_max**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter)) const

Maximum orbital velocity applied to each particle. Makes the particles circle around origin. Specified in number of full rotations around origin per second.

---


<a id="class-cpuparticles2d-property-orbit-velocity-min"></a>

[float](class_float.md#class-float) **orbit_velocity_min** = `0.0` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-orbit-velocity-min)

- void **set_param_min**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter)) const

Minimum equivalent of [orbit_velocity_max](class_cpuparticles2d.md#class-cpuparticles2d-property-orbit-velocity-max).

---


<a id="class-cpuparticles2d-property-particle-flag-align-y"></a>

[bool](class_bool.md#class-bool) **particle_flag_align_y** = `false` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-particle-flag-align-y)

- void **set_particle_flag**(particle_flag: [ParticleFlags](class_cpuparticles2d.md#enum-cpuparticles2d-particleflags), enable: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_particle_flag**(particle_flag: [ParticleFlags](class_cpuparticles2d.md#enum-cpuparticles2d-particleflags)) const

Align Y axis of particle with the direction of its velocity.

---


<a id="class-cpuparticles2d-property-preprocess"></a>

[float](class_float.md#class-float) **preprocess** = `0.0` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-preprocess)

- void **set_pre_process_time**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_pre_process_time**()

Particle system starts as if it had already run for this many seconds.

---


<a id="class-cpuparticles2d-property-radial-accel-curve"></a>

[Curve](class_curve.md#class-curve) **radial_accel_curve** [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-radial-accel-curve)

- void **set_param_curve**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter), curve: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_param_curve**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter)) const

Each particle's radial acceleration will vary along this [Curve](class_curve.md#class-curve). Should be a unit [Curve](class_curve.md#class-curve).

---


<a id="class-cpuparticles2d-property-radial-accel-max"></a>

[float](class_float.md#class-float) **radial_accel_max** = `0.0` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-radial-accel-max)

- void **set_param_max**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter)) const

Maximum radial acceleration applied to each particle. Makes particle accelerate away from the origin or towards it if negative.

---


<a id="class-cpuparticles2d-property-radial-accel-min"></a>

[float](class_float.md#class-float) **radial_accel_min** = `0.0` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-radial-accel-min)

- void **set_param_min**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter)) const

Minimum equivalent of [radial_accel_max](class_cpuparticles2d.md#class-cpuparticles2d-property-radial-accel-max).

---


<a id="class-cpuparticles2d-property-randomness"></a>

[float](class_float.md#class-float) **randomness** = `0.0` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-randomness)

- void **set_randomness_ratio**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_randomness_ratio**()

Emission lifetime randomness ratio.

---


<a id="class-cpuparticles2d-property-scale-amount-curve"></a>

[Curve](class_curve.md#class-curve) **scale_amount_curve** [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-scale-amount-curve)

- void **set_param_curve**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter), curve: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_param_curve**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter)) const

Each particle's scale will vary along this [Curve](class_curve.md#class-curve). Should be a unit [Curve](class_curve.md#class-curve).

---


<a id="class-cpuparticles2d-property-scale-amount-max"></a>

[float](class_float.md#class-float) **scale_amount_max** = `1.0` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-scale-amount-max)

- void **set_param_max**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter)) const

Maximum initial scale applied to each particle.

---


<a id="class-cpuparticles2d-property-scale-amount-min"></a>

[float](class_float.md#class-float) **scale_amount_min** = `1.0` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-scale-amount-min)

- void **set_param_min**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter)) const

Minimum equivalent of [scale_amount_max](class_cpuparticles2d.md#class-cpuparticles2d-property-scale-amount-max).

---


<a id="class-cpuparticles2d-property-scale-curve-x"></a>

[Curve](class_curve.md#class-curve) **scale_curve_x** [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-scale-curve-x)

- void **set_scale_curve_x**(value: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_scale_curve_x**()

Each particle's horizontal scale will vary along this [Curve](class_curve.md#class-curve). Should be a unit [Curve](class_curve.md#class-curve).

[split_scale](class_cpuparticles2d.md#class-cpuparticles2d-property-split-scale) must be enabled.

---


<a id="class-cpuparticles2d-property-scale-curve-y"></a>

[Curve](class_curve.md#class-curve) **scale_curve_y** [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-scale-curve-y)

- void **set_scale_curve_y**(value: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_scale_curve_y**()

Each particle's vertical scale will vary along this [Curve](class_curve.md#class-curve). Should be a unit [Curve](class_curve.md#class-curve).

[split_scale](class_cpuparticles2d.md#class-cpuparticles2d-property-split-scale) must be enabled.

---


<a id="class-cpuparticles2d-property-seed"></a>

[int](class_int.md#class-int) **seed** = `0` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-seed)

- void **set_seed**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_seed**()

Sets the random seed used by the particle system. Only effective if [use_fixed_seed](class_cpuparticles2d.md#class-cpuparticles2d-property-use-fixed-seed) is `true`.

---


<a id="class-cpuparticles2d-property-speed-scale"></a>

[float](class_float.md#class-float) **speed_scale** = `1.0` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-speed-scale)

- void **set_speed_scale**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_speed_scale**()

Particle system's running speed scaling ratio. A value of `0` can be used to pause the particles.

---


<a id="class-cpuparticles2d-property-split-scale"></a>

[bool](class_bool.md#class-bool) **split_scale** = `false` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-split-scale)

- void **set_split_scale**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_split_scale**()

If `true`, the scale curve will be split into x and y components. See [scale_curve_x](class_cpuparticles2d.md#class-cpuparticles2d-property-scale-curve-x) and [scale_curve_y](class_cpuparticles2d.md#class-cpuparticles2d-property-scale-curve-y).

---


<a id="class-cpuparticles2d-property-spread"></a>

[float](class_float.md#class-float) **spread** = `45.0` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-spread)

- void **set_spread**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_spread**()

Each particle's initial direction range from `+spread` to `-spread` degrees.

---


<a id="class-cpuparticles2d-property-tangential-accel-curve"></a>

[Curve](class_curve.md#class-curve) **tangential_accel_curve** [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-tangential-accel-curve)

- void **set_param_curve**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter), curve: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_param_curve**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter)) const

Each particle's tangential acceleration will vary along this [Curve](class_curve.md#class-curve). Should be a unit [Curve](class_curve.md#class-curve).

---


<a id="class-cpuparticles2d-property-tangential-accel-max"></a>

[float](class_float.md#class-float) **tangential_accel_max** = `0.0` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-tangential-accel-max)

- void **set_param_max**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter)) const

Maximum tangential acceleration applied to each particle. Tangential acceleration is perpendicular to the particle's velocity giving the particles a swirling motion.

---


<a id="class-cpuparticles2d-property-tangential-accel-min"></a>

[float](class_float.md#class-float) **tangential_accel_min** = `0.0` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-tangential-accel-min)

- void **set_param_min**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter)) const

Minimum equivalent of [tangential_accel_max](class_cpuparticles2d.md#class-cpuparticles2d-property-tangential-accel-max).

---


<a id="class-cpuparticles2d-property-texture"></a>

[Texture2D](class_texture2d.md#class-texture2d) **texture** [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-texture)

- void **set_texture**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_texture**()

Particle texture. If `null`, particles will be squares.

---


<a id="class-cpuparticles2d-property-use-fixed-seed"></a>

[bool](class_bool.md#class-bool) **use_fixed_seed** = `false` [🔗](class_cpuparticles2d.md#class-cpuparticles2d-property-use-fixed-seed)

- void **set_use_fixed_seed**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_use_fixed_seed**()

If `true`, particles will use the same seed for every simulation using the seed defined in [seed](class_cpuparticles2d.md#class-cpuparticles2d-property-seed). This is useful for situations where the visual outcome should be consistent across replays, for example when using Movie Maker mode.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-cpuparticles2d-method-convert-from-particles"></a>

void **convert_from_particles**(particles: [Node](class_node.md#class-node)) [🔗](class_cpuparticles2d.md#class-cpuparticles2d-method-convert-from-particles)

Sets this node's properties to match a given [GPUParticles2D](class_gpuparticles2d.md#class-gpuparticles2d) node with an assigned [ParticleProcessMaterial](class_particleprocessmaterial.md#class-particleprocessmaterial).

---


<a id="class-cpuparticles2d-method-get-param-curve"></a>

[Curve](class_curve.md#class-curve) **get_param_curve**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter)) const [🔗](class_cpuparticles2d.md#class-cpuparticles2d-method-get-param-curve)

Returns the [Curve](class_curve.md#class-curve) of the parameter specified by [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter).

---


<a id="class-cpuparticles2d-method-get-param-max"></a>

[float](class_float.md#class-float) **get_param_max**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter)) const [🔗](class_cpuparticles2d.md#class-cpuparticles2d-method-get-param-max)

Returns the maximum value range for the given parameter.

---


<a id="class-cpuparticles2d-method-get-param-min"></a>

[float](class_float.md#class-float) **get_param_min**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter)) const [🔗](class_cpuparticles2d.md#class-cpuparticles2d-method-get-param-min)

Returns the minimum value range for the given parameter.

---


<a id="class-cpuparticles2d-method-get-particle-flag"></a>

[bool](class_bool.md#class-bool) **get_particle_flag**(particle_flag: [ParticleFlags](class_cpuparticles2d.md#enum-cpuparticles2d-particleflags)) const [🔗](class_cpuparticles2d.md#class-cpuparticles2d-method-get-particle-flag)

Returns the enabled state of the given particle flag.

---


<a id="class-cpuparticles2d-method-request-particles-process"></a>

void **request_particles_process**(process_time: [float](class_float.md#class-float), process_time_residual: [float](class_float.md#class-float) = 0.0) [🔗](class_cpuparticles2d.md#class-cpuparticles2d-method-request-particles-process)

Requests the particles to process for extra process time during a single frame.

`process_time` defines the time that the particles will process while emitting is on. `process_time_residual` defines the time that particles will process with emitting turned off for the simulation. When combined with [speed_scale](class_cpuparticles2d.md#class-cpuparticles2d-property-speed-scale) set to `0.0`, this is useful to be able to seek a particle system timeline.

---


<a id="class-cpuparticles2d-method-restart"></a>

void **restart**(keep_seed: [bool](class_bool.md#class-bool) = false) [🔗](class_cpuparticles2d.md#class-cpuparticles2d-method-restart)

Restarts the particle emitter.

If `keep_seed` is `true`, the current random seed will be preserved. Useful for seeking and playback.

---


<a id="class-cpuparticles2d-method-set-param-curve"></a>

void **set_param_curve**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter), curve: [Curve](class_curve.md#class-curve)) [🔗](class_cpuparticles2d.md#class-cpuparticles2d-method-set-param-curve)

Sets the [Curve](class_curve.md#class-curve) of the parameter specified by [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter). Should be a unit [Curve](class_curve.md#class-curve).

---


<a id="class-cpuparticles2d-method-set-param-max"></a>

void **set_param_max**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter), value: [float](class_float.md#class-float)) [🔗](class_cpuparticles2d.md#class-cpuparticles2d-method-set-param-max)

Sets the maximum value for the given parameter.

---


<a id="class-cpuparticles2d-method-set-param-min"></a>

void **set_param_min**(param: [Parameter](class_cpuparticles2d.md#enum-cpuparticles2d-parameter), value: [float](class_float.md#class-float)) [🔗](class_cpuparticles2d.md#class-cpuparticles2d-method-set-param-min)

Sets the minimum value for the given parameter.

---


<a id="class-cpuparticles2d-method-set-particle-flag"></a>

void **set_particle_flag**(particle_flag: [ParticleFlags](class_cpuparticles2d.md#enum-cpuparticles2d-particleflags), enable: [bool](class_bool.md#class-bool)) [🔗](class_cpuparticles2d.md#class-cpuparticles2d-method-set-particle-flag)

Enables or disables the given particle flag.
