> Source: https://docs.godotengine.org/en/4.7/classes/class_generic6dofjoint3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="generic6dofjoint3d"></a>

<a id="class-generic6dofjoint3d"></a>

# Generic6DOFJoint3D

**Inherits:** [Joint3D](class_joint3d.md#class-joint3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A physics joint that allows for complex movement and rotation between two 3D physics bodies.

<a id="description"></a>

## Description

The **Generic6DOFJoint3D** (6 Degrees Of Freedom) joint allows for implementing custom types of joints by locking the rotation and translation of certain axes.

The first 3 DOF represent the linear motion of the physics bodies and the last 3 DOF represent the angular motion of the physics bodies. Each axis can be either locked, or limited.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [angular_limit_x/damping](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-x-damping) | `1.0` |
| [bool](class_bool.md#class-bool) | [angular_limit_x/enabled](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-x-enabled) | `true` |
| [float](class_float.md#class-float) | [angular_limit_x/erp](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-x-erp) | `0.5` |
| [float](class_float.md#class-float) | [angular_limit_x/force_limit](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-x-force-limit) | `0.0` |
| [float](class_float.md#class-float) | [angular_limit_x/lower_angle](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-x-lower-angle) | `0.0` |
| [float](class_float.md#class-float) | [angular_limit_x/restitution](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-x-restitution) | `0.0` |
| [float](class_float.md#class-float) | [angular_limit_x/softness](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-x-softness) | `0.5` |
| [float](class_float.md#class-float) | [angular_limit_x/upper_angle](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-x-upper-angle) | `0.0` |
| [float](class_float.md#class-float) | [angular_limit_y/damping](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-y-damping) | `1.0` |
| [bool](class_bool.md#class-bool) | [angular_limit_y/enabled](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-y-enabled) | `true` |
| [float](class_float.md#class-float) | [angular_limit_y/erp](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-y-erp) | `0.5` |
| [float](class_float.md#class-float) | [angular_limit_y/force_limit](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-y-force-limit) | `0.0` |
| [float](class_float.md#class-float) | [angular_limit_y/lower_angle](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-y-lower-angle) | `0.0` |
| [float](class_float.md#class-float) | [angular_limit_y/restitution](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-y-restitution) | `0.0` |
| [float](class_float.md#class-float) | [angular_limit_y/softness](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-y-softness) | `0.5` |
| [float](class_float.md#class-float) | [angular_limit_y/upper_angle](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-y-upper-angle) | `0.0` |
| [float](class_float.md#class-float) | [angular_limit_z/damping](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-z-damping) | `1.0` |
| [bool](class_bool.md#class-bool) | [angular_limit_z/enabled](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-z-enabled) | `true` |
| [float](class_float.md#class-float) | [angular_limit_z/erp](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-z-erp) | `0.5` |
| [float](class_float.md#class-float) | [angular_limit_z/force_limit](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-z-force-limit) | `0.0` |
| [float](class_float.md#class-float) | [angular_limit_z/lower_angle](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-z-lower-angle) | `0.0` |
| [float](class_float.md#class-float) | [angular_limit_z/restitution](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-z-restitution) | `0.0` |
| [float](class_float.md#class-float) | [angular_limit_z/softness](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-z-softness) | `0.5` |
| [float](class_float.md#class-float) | [angular_limit_z/upper_angle](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-z-upper-angle) | `0.0` |
| [bool](class_bool.md#class-bool) | [angular_motor_x/enabled](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-motor-x-enabled) | `false` |
| [float](class_float.md#class-float) | [angular_motor_x/force_limit](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-motor-x-force-limit) | `300.0` |
| [float](class_float.md#class-float) | [angular_motor_x/target_velocity](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-motor-x-target-velocity) | `0.0` |
| [bool](class_bool.md#class-bool) | [angular_motor_y/enabled](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-motor-y-enabled) | `false` |
| [float](class_float.md#class-float) | [angular_motor_y/force_limit](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-motor-y-force-limit) | `300.0` |
| [float](class_float.md#class-float) | [angular_motor_y/target_velocity](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-motor-y-target-velocity) | `0.0` |
| [bool](class_bool.md#class-bool) | [angular_motor_z/enabled](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-motor-z-enabled) | `false` |
| [float](class_float.md#class-float) | [angular_motor_z/force_limit](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-motor-z-force-limit) | `300.0` |
| [float](class_float.md#class-float) | [angular_motor_z/target_velocity](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-motor-z-target-velocity) | `0.0` |
| [float](class_float.md#class-float) | [angular_spring_x/damping](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-spring-x-damping) | `0.0` |
| [bool](class_bool.md#class-bool) | [angular_spring_x/enabled](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-spring-x-enabled) | `false` |
| [float](class_float.md#class-float) | [angular_spring_x/equilibrium_point](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-spring-x-equilibrium-point) | `0.0` |
| [float](class_float.md#class-float) | [angular_spring_x/stiffness](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-spring-x-stiffness) | `0.0` |
| [float](class_float.md#class-float) | [angular_spring_y/damping](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-spring-y-damping) | `0.0` |
| [bool](class_bool.md#class-bool) | [angular_spring_y/enabled](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-spring-y-enabled) | `false` |
| [float](class_float.md#class-float) | [angular_spring_y/equilibrium_point](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-spring-y-equilibrium-point) | `0.0` |
| [float](class_float.md#class-float) | [angular_spring_y/stiffness](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-spring-y-stiffness) | `0.0` |
| [float](class_float.md#class-float) | [angular_spring_z/damping](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-spring-z-damping) | `0.0` |
| [bool](class_bool.md#class-bool) | [angular_spring_z/enabled](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-spring-z-enabled) | `false` |
| [float](class_float.md#class-float) | [angular_spring_z/equilibrium_point](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-spring-z-equilibrium-point) | `0.0` |
| [float](class_float.md#class-float) | [angular_spring_z/stiffness](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-spring-z-stiffness) | `0.0` |
| [float](class_float.md#class-float) | [linear_limit_x/damping](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-limit-x-damping) | `1.0` |
| [bool](class_bool.md#class-bool) | [linear_limit_x/enabled](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-limit-x-enabled) | `true` |
| [float](class_float.md#class-float) | [linear_limit_x/lower_distance](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-limit-x-lower-distance) | `0.0` |
| [float](class_float.md#class-float) | [linear_limit_x/restitution](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-limit-x-restitution) | `0.5` |
| [float](class_float.md#class-float) | [linear_limit_x/softness](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-limit-x-softness) | `0.7` |
| [float](class_float.md#class-float) | [linear_limit_x/upper_distance](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-limit-x-upper-distance) | `0.0` |
| [float](class_float.md#class-float) | [linear_limit_y/damping](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-limit-y-damping) | `1.0` |
| [bool](class_bool.md#class-bool) | [linear_limit_y/enabled](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-limit-y-enabled) | `true` |
| [float](class_float.md#class-float) | [linear_limit_y/lower_distance](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-limit-y-lower-distance) | `0.0` |
| [float](class_float.md#class-float) | [linear_limit_y/restitution](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-limit-y-restitution) | `0.5` |
| [float](class_float.md#class-float) | [linear_limit_y/softness](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-limit-y-softness) | `0.7` |
| [float](class_float.md#class-float) | [linear_limit_y/upper_distance](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-limit-y-upper-distance) | `0.0` |
| [float](class_float.md#class-float) | [linear_limit_z/damping](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-limit-z-damping) | `1.0` |
| [bool](class_bool.md#class-bool) | [linear_limit_z/enabled](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-limit-z-enabled) | `true` |
| [float](class_float.md#class-float) | [linear_limit_z/lower_distance](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-limit-z-lower-distance) | `0.0` |
| [float](class_float.md#class-float) | [linear_limit_z/restitution](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-limit-z-restitution) | `0.5` |
| [float](class_float.md#class-float) | [linear_limit_z/softness](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-limit-z-softness) | `0.7` |
| [float](class_float.md#class-float) | [linear_limit_z/upper_distance](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-limit-z-upper-distance) | `0.0` |
| [bool](class_bool.md#class-bool) | [linear_motor_x/enabled](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-motor-x-enabled) | `false` |
| [float](class_float.md#class-float) | [linear_motor_x/force_limit](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-motor-x-force-limit) | `0.0` |
| [float](class_float.md#class-float) | [linear_motor_x/target_velocity](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-motor-x-target-velocity) | `0.0` |
| [bool](class_bool.md#class-bool) | [linear_motor_y/enabled](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-motor-y-enabled) | `false` |
| [float](class_float.md#class-float) | [linear_motor_y/force_limit](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-motor-y-force-limit) | `0.0` |
| [float](class_float.md#class-float) | [linear_motor_y/target_velocity](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-motor-y-target-velocity) | `0.0` |
| [bool](class_bool.md#class-bool) | [linear_motor_z/enabled](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-motor-z-enabled) | `false` |
| [float](class_float.md#class-float) | [linear_motor_z/force_limit](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-motor-z-force-limit) | `0.0` |
| [float](class_float.md#class-float) | [linear_motor_z/target_velocity](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-motor-z-target-velocity) | `0.0` |
| [float](class_float.md#class-float) | [linear_spring_x/damping](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-spring-x-damping) | `0.01` |
| [bool](class_bool.md#class-bool) | [linear_spring_x/enabled](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-spring-x-enabled) | `false` |
| [float](class_float.md#class-float) | [linear_spring_x/equilibrium_point](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-spring-x-equilibrium-point) | `0.0` |
| [float](class_float.md#class-float) | [linear_spring_x/stiffness](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-spring-x-stiffness) | `0.01` |
| [float](class_float.md#class-float) | [linear_spring_y/damping](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-spring-y-damping) | `0.01` |
| [bool](class_bool.md#class-bool) | [linear_spring_y/enabled](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-spring-y-enabled) | `false` |
| [float](class_float.md#class-float) | [linear_spring_y/equilibrium_point](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-spring-y-equilibrium-point) | `0.0` |
| [float](class_float.md#class-float) | [linear_spring_y/stiffness](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-spring-y-stiffness) | `0.01` |
| [float](class_float.md#class-float) | [linear_spring_z/damping](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-spring-z-damping) | `0.01` |
| [bool](class_bool.md#class-bool) | [linear_spring_z/enabled](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-spring-z-enabled) | `false` |
| [float](class_float.md#class-float) | [linear_spring_z/equilibrium_point](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-spring-z-equilibrium-point) | `0.0` |
| [float](class_float.md#class-float) | [linear_spring_z/stiffness](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-spring-z-stiffness) | `0.01` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [get_flag_x](class_generic6dofjoint3d.md#class-generic6dofjoint3d-method-get-flag-x)(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag)) const |
| [bool](class_bool.md#class-bool) | [get_flag_y](class_generic6dofjoint3d.md#class-generic6dofjoint3d-method-get-flag-y)(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag)) const |
| [bool](class_bool.md#class-bool) | [get_flag_z](class_generic6dofjoint3d.md#class-generic6dofjoint3d-method-get-flag-z)(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag)) const |
| [float](class_float.md#class-float) | [get_param_x](class_generic6dofjoint3d.md#class-generic6dofjoint3d-method-get-param-x)(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const |
| [float](class_float.md#class-float) | [get_param_y](class_generic6dofjoint3d.md#class-generic6dofjoint3d-method-get-param-y)(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const |
| [float](class_float.md#class-float) | [get_param_z](class_generic6dofjoint3d.md#class-generic6dofjoint3d-method-get-param-z)(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const |
| void | [set_flag_x](class_generic6dofjoint3d.md#class-generic6dofjoint3d-method-set-flag-x)(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag), value: [bool](class_bool.md#class-bool)) |
| void | [set_flag_y](class_generic6dofjoint3d.md#class-generic6dofjoint3d-method-set-flag-y)(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag), value: [bool](class_bool.md#class-bool)) |
| void | [set_flag_z](class_generic6dofjoint3d.md#class-generic6dofjoint3d-method-set-flag-z)(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag), value: [bool](class_bool.md#class-bool)) |
| void | [set_param_x](class_generic6dofjoint3d.md#class-generic6dofjoint3d-method-set-param-x)(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float)) |
| void | [set_param_y](class_generic6dofjoint3d.md#class-generic6dofjoint3d-method-set-param-y)(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float)) |
| void | [set_param_z](class_generic6dofjoint3d.md#class-generic6dofjoint3d-method-set-param-z)(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float)) |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-generic6dofjoint3d-param"></a>

enum **Param**: [🔗](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)

<a id="class-generic6dofjoint3d-constant-param-linear-lower-limit"></a>

[Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param) **PARAM_LINEAR_LOWER_LIMIT** = `0`

The minimum difference between the pivot points' axes.

<a id="class-generic6dofjoint3d-constant-param-linear-upper-limit"></a>

[Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param) **PARAM_LINEAR_UPPER_LIMIT** = `1`

The maximum difference between the pivot points' axes.

<a id="class-generic6dofjoint3d-constant-param-linear-limit-softness"></a>

[Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param) **PARAM_LINEAR_LIMIT_SOFTNESS** = `2`

A factor applied to the movement across the axes. The lower, the slower the movement.

<a id="class-generic6dofjoint3d-constant-param-linear-restitution"></a>

[Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param) **PARAM_LINEAR_RESTITUTION** = `3`

The amount of restitution on the axes' movement. The lower, the more momentum gets lost.

<a id="class-generic6dofjoint3d-constant-param-linear-damping"></a>

[Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param) **PARAM_LINEAR_DAMPING** = `4`

The amount of damping that happens at the linear motion across the axes.

<a id="class-generic6dofjoint3d-constant-param-linear-motor-target-velocity"></a>

[Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param) **PARAM_LINEAR_MOTOR_TARGET_VELOCITY** = `5`

The velocity the linear motor will try to reach.

<a id="class-generic6dofjoint3d-constant-param-linear-motor-force-limit"></a>

[Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param) **PARAM_LINEAR_MOTOR_FORCE_LIMIT** = `6`

The maximum force the linear motor will apply while trying to reach the velocity target.

<a id="class-generic6dofjoint3d-constant-param-linear-spring-stiffness"></a>

[Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param) **PARAM_LINEAR_SPRING_STIFFNESS** = `7`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="class-generic6dofjoint3d-constant-param-linear-spring-damping"></a>

[Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param) **PARAM_LINEAR_SPRING_DAMPING** = `8`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="class-generic6dofjoint3d-constant-param-linear-spring-equilibrium-point"></a>

[Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param) **PARAM_LINEAR_SPRING_EQUILIBRIUM_POINT** = `9`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="class-generic6dofjoint3d-constant-param-angular-lower-limit"></a>

[Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param) **PARAM_ANGULAR_LOWER_LIMIT** = `10`

The minimum rotation in negative direction to break loose and rotate around the axes.

<a id="class-generic6dofjoint3d-constant-param-angular-upper-limit"></a>

[Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param) **PARAM_ANGULAR_UPPER_LIMIT** = `11`

The minimum rotation in positive direction to break loose and rotate around the axes.

<a id="class-generic6dofjoint3d-constant-param-angular-limit-softness"></a>

[Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param) **PARAM_ANGULAR_LIMIT_SOFTNESS** = `12`

The speed of all rotations across the axes.

<a id="class-generic6dofjoint3d-constant-param-angular-damping"></a>

[Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param) **PARAM_ANGULAR_DAMPING** = `13`

The amount of rotational damping across the axes. The lower, the more damping occurs.

<a id="class-generic6dofjoint3d-constant-param-angular-restitution"></a>

[Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param) **PARAM_ANGULAR_RESTITUTION** = `14`

The amount of rotational restitution across the axes. The lower, the more restitution occurs.

<a id="class-generic6dofjoint3d-constant-param-angular-force-limit"></a>

[Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param) **PARAM_ANGULAR_FORCE_LIMIT** = `15`

The maximum amount of force that can occur, when rotating around the axes.

<a id="class-generic6dofjoint3d-constant-param-angular-erp"></a>

[Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param) **PARAM_ANGULAR_ERP** = `16`

When rotating across the axes, this error tolerance factor defines how much the correction gets slowed down. The lower, the slower.

<a id="class-generic6dofjoint3d-constant-param-angular-motor-target-velocity"></a>

[Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param) **PARAM_ANGULAR_MOTOR_TARGET_VELOCITY** = `17`

Target speed for the motor at the axes.

<a id="class-generic6dofjoint3d-constant-param-angular-motor-force-limit"></a>

[Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param) **PARAM_ANGULAR_MOTOR_FORCE_LIMIT** = `18`

Maximum acceleration for the motor at the axes.

<a id="class-generic6dofjoint3d-constant-param-angular-spring-stiffness"></a>

[Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param) **PARAM_ANGULAR_SPRING_STIFFNESS** = `19`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="class-generic6dofjoint3d-constant-param-angular-spring-damping"></a>

[Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param) **PARAM_ANGULAR_SPRING_DAMPING** = `20`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="class-generic6dofjoint3d-constant-param-angular-spring-equilibrium-point"></a>

[Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param) **PARAM_ANGULAR_SPRING_EQUILIBRIUM_POINT** = `21`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="class-generic6dofjoint3d-constant-param-max"></a>

[Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param) **PARAM_MAX** = `22`

Represents the size of the [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param) enum.

---


<a id="enum-generic6dofjoint3d-flag"></a>

enum **Flag**: [🔗](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag)

<a id="class-generic6dofjoint3d-constant-flag-enable-linear-limit"></a>

[Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag) **FLAG_ENABLE_LINEAR_LIMIT** = `0`

If enabled, linear motion is possible within the given limits.

<a id="class-generic6dofjoint3d-constant-flag-enable-angular-limit"></a>

[Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag) **FLAG_ENABLE_ANGULAR_LIMIT** = `1`

If enabled, rotational motion is possible within the given limits.

<a id="class-generic6dofjoint3d-constant-flag-enable-linear-spring"></a>

[Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag) **FLAG_ENABLE_LINEAR_SPRING** = `3`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="class-generic6dofjoint3d-constant-flag-enable-angular-spring"></a>

[Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag) **FLAG_ENABLE_ANGULAR_SPRING** = `2`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="class-generic6dofjoint3d-constant-flag-enable-motor"></a>

[Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag) **FLAG_ENABLE_MOTOR** = `4`

If enabled, there is a rotational motor across these axes.

<a id="class-generic6dofjoint3d-constant-flag-enable-linear-motor"></a>

[Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag) **FLAG_ENABLE_LINEAR_MOTOR** = `5`

If enabled, there is a linear motor across these axes.

<a id="class-generic6dofjoint3d-constant-flag-max"></a>

[Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag) **FLAG_MAX** = `6`

Represents the size of the [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-generic6dofjoint3d-property-angular-limit-x-damping"></a>

[float](class_float.md#class-float) **angular_limit_x/damping** = `1.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-x-damping)

- void **set_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

The amount of rotational damping across the X axis.

The lower, the longer an impulse from one side takes to travel to the other side.

---


<a id="class-generic6dofjoint3d-property-angular-limit-x-enabled"></a>

[bool](class_bool.md#class-bool) **angular_limit_x/enabled** = `true` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-x-enabled)

- void **set_flag_x**(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag), value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flag_x**(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag)) const

If `true`, rotation across the X axis is limited.

---


<a id="class-generic6dofjoint3d-property-angular-limit-x-erp"></a>

[float](class_float.md#class-float) **angular_limit_x/erp** = `0.5` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-x-erp)

- void **set_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

When rotating across the X axis, this error tolerance factor defines how much the correction gets slowed down. The lower, the slower.

---


<a id="class-generic6dofjoint3d-property-angular-limit-x-force-limit"></a>

[float](class_float.md#class-float) **angular_limit_x/force_limit** = `0.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-x-force-limit)

- void **set_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

The maximum amount of force that can occur, when rotating around the X axis.

---


<a id="class-generic6dofjoint3d-property-angular-limit-x-lower-angle"></a>

[float](class_float.md#class-float) **angular_limit_x/lower_angle** = `0.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-x-lower-angle)

- void **set_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

The minimum rotation in negative direction to break loose and rotate around the X axis.

---


<a id="class-generic6dofjoint3d-property-angular-limit-x-restitution"></a>

[float](class_float.md#class-float) **angular_limit_x/restitution** = `0.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-x-restitution)

- void **set_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

The amount of rotational restitution across the X axis. The lower, the more restitution occurs.

---


<a id="class-generic6dofjoint3d-property-angular-limit-x-softness"></a>

[float](class_float.md#class-float) **angular_limit_x/softness** = `0.5` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-x-softness)

- void **set_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

The speed of all rotations across the X axis.

---


<a id="class-generic6dofjoint3d-property-angular-limit-x-upper-angle"></a>

[float](class_float.md#class-float) **angular_limit_x/upper_angle** = `0.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-x-upper-angle)

- void **set_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

The minimum rotation in positive direction to break loose and rotate around the X axis.

---


<a id="class-generic6dofjoint3d-property-angular-limit-y-damping"></a>

[float](class_float.md#class-float) **angular_limit_y/damping** = `1.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-y-damping)

- void **set_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

The amount of rotational damping across the Y axis. The lower, the more damping occurs.

---


<a id="class-generic6dofjoint3d-property-angular-limit-y-enabled"></a>

[bool](class_bool.md#class-bool) **angular_limit_y/enabled** = `true` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-y-enabled)

- void **set_flag_y**(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag), value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flag_y**(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag)) const

If `true`, rotation across the Y axis is limited.

---


<a id="class-generic6dofjoint3d-property-angular-limit-y-erp"></a>

[float](class_float.md#class-float) **angular_limit_y/erp** = `0.5` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-y-erp)

- void **set_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

When rotating across the Y axis, this error tolerance factor defines how much the correction gets slowed down. The lower, the slower.

---


<a id="class-generic6dofjoint3d-property-angular-limit-y-force-limit"></a>

[float](class_float.md#class-float) **angular_limit_y/force_limit** = `0.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-y-force-limit)

- void **set_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

The maximum amount of force that can occur, when rotating around the Y axis.

---


<a id="class-generic6dofjoint3d-property-angular-limit-y-lower-angle"></a>

[float](class_float.md#class-float) **angular_limit_y/lower_angle** = `0.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-y-lower-angle)

- void **set_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

The minimum rotation in negative direction to break loose and rotate around the Y axis.

---


<a id="class-generic6dofjoint3d-property-angular-limit-y-restitution"></a>

[float](class_float.md#class-float) **angular_limit_y/restitution** = `0.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-y-restitution)

- void **set_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

The amount of rotational restitution across the Y axis. The lower, the more restitution occurs.

---


<a id="class-generic6dofjoint3d-property-angular-limit-y-softness"></a>

[float](class_float.md#class-float) **angular_limit_y/softness** = `0.5` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-y-softness)

- void **set_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

The speed of all rotations across the Y axis.

---


<a id="class-generic6dofjoint3d-property-angular-limit-y-upper-angle"></a>

[float](class_float.md#class-float) **angular_limit_y/upper_angle** = `0.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-y-upper-angle)

- void **set_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

The minimum rotation in positive direction to break loose and rotate around the Y axis.

---


<a id="class-generic6dofjoint3d-property-angular-limit-z-damping"></a>

[float](class_float.md#class-float) **angular_limit_z/damping** = `1.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-z-damping)

- void **set_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

The amount of rotational damping across the Z axis. The lower, the more damping occurs.

---


<a id="class-generic6dofjoint3d-property-angular-limit-z-enabled"></a>

[bool](class_bool.md#class-bool) **angular_limit_z/enabled** = `true` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-z-enabled)

- void **set_flag_z**(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag), value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flag_z**(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag)) const

If `true`, rotation across the Z axis is limited.

---


<a id="class-generic6dofjoint3d-property-angular-limit-z-erp"></a>

[float](class_float.md#class-float) **angular_limit_z/erp** = `0.5` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-z-erp)

- void **set_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

When rotating across the Z axis, this error tolerance factor defines how much the correction gets slowed down. The lower, the slower.

---


<a id="class-generic6dofjoint3d-property-angular-limit-z-force-limit"></a>

[float](class_float.md#class-float) **angular_limit_z/force_limit** = `0.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-z-force-limit)

- void **set_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

The maximum amount of force that can occur, when rotating around the Z axis.

---


<a id="class-generic6dofjoint3d-property-angular-limit-z-lower-angle"></a>

[float](class_float.md#class-float) **angular_limit_z/lower_angle** = `0.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-z-lower-angle)

- void **set_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

The minimum rotation in negative direction to break loose and rotate around the Z axis.

---


<a id="class-generic6dofjoint3d-property-angular-limit-z-restitution"></a>

[float](class_float.md#class-float) **angular_limit_z/restitution** = `0.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-z-restitution)

- void **set_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

The amount of rotational restitution across the Z axis. The lower, the more restitution occurs.

---


<a id="class-generic6dofjoint3d-property-angular-limit-z-softness"></a>

[float](class_float.md#class-float) **angular_limit_z/softness** = `0.5` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-z-softness)

- void **set_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

The speed of all rotations across the Z axis.

---


<a id="class-generic6dofjoint3d-property-angular-limit-z-upper-angle"></a>

[float](class_float.md#class-float) **angular_limit_z/upper_angle** = `0.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-limit-z-upper-angle)

- void **set_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

The minimum rotation in positive direction to break loose and rotate around the Z axis.

---


<a id="class-generic6dofjoint3d-property-angular-motor-x-enabled"></a>

[bool](class_bool.md#class-bool) **angular_motor_x/enabled** = `false` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-motor-x-enabled)

- void **set_flag_x**(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag), value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flag_x**(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag)) const

If `true`, a rotating motor at the X axis is enabled.

---


<a id="class-generic6dofjoint3d-property-angular-motor-x-force-limit"></a>

[float](class_float.md#class-float) **angular_motor_x/force_limit** = `300.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-motor-x-force-limit)

- void **set_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

Maximum acceleration for the motor at the X axis.

---


<a id="class-generic6dofjoint3d-property-angular-motor-x-target-velocity"></a>

[float](class_float.md#class-float) **angular_motor_x/target_velocity** = `0.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-motor-x-target-velocity)

- void **set_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

Target speed for the motor at the X axis.

---


<a id="class-generic6dofjoint3d-property-angular-motor-y-enabled"></a>

[bool](class_bool.md#class-bool) **angular_motor_y/enabled** = `false` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-motor-y-enabled)

- void **set_flag_y**(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag), value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flag_y**(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag)) const

If `true`, a rotating motor at the Y axis is enabled.

---


<a id="class-generic6dofjoint3d-property-angular-motor-y-force-limit"></a>

[float](class_float.md#class-float) **angular_motor_y/force_limit** = `300.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-motor-y-force-limit)

- void **set_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

Maximum acceleration for the motor at the Y axis.

---


<a id="class-generic6dofjoint3d-property-angular-motor-y-target-velocity"></a>

[float](class_float.md#class-float) **angular_motor_y/target_velocity** = `0.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-motor-y-target-velocity)

- void **set_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

Target speed for the motor at the Y axis.

---


<a id="class-generic6dofjoint3d-property-angular-motor-z-enabled"></a>

[bool](class_bool.md#class-bool) **angular_motor_z/enabled** = `false` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-motor-z-enabled)

- void **set_flag_z**(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag), value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flag_z**(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag)) const

If `true`, a rotating motor at the Z axis is enabled.

---


<a id="class-generic6dofjoint3d-property-angular-motor-z-force-limit"></a>

[float](class_float.md#class-float) **angular_motor_z/force_limit** = `300.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-motor-z-force-limit)

- void **set_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

Maximum acceleration for the motor at the Z axis.

---


<a id="class-generic6dofjoint3d-property-angular-motor-z-target-velocity"></a>

[float](class_float.md#class-float) **angular_motor_z/target_velocity** = `0.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-motor-z-target-velocity)

- void **set_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

Target speed for the motor at the Z axis.

---


<a id="class-generic6dofjoint3d-property-angular-spring-x-damping"></a>

[float](class_float.md#class-float) **angular_spring_x/damping** = `0.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-spring-x-damping)

- void **set_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-generic6dofjoint3d-property-angular-spring-x-enabled"></a>

[bool](class_bool.md#class-bool) **angular_spring_x/enabled** = `false` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-spring-x-enabled)

- void **set_flag_x**(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag), value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flag_x**(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag)) const

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-generic6dofjoint3d-property-angular-spring-x-equilibrium-point"></a>

[float](class_float.md#class-float) **angular_spring_x/equilibrium_point** = `0.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-spring-x-equilibrium-point)

- void **set_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-generic6dofjoint3d-property-angular-spring-x-stiffness"></a>

[float](class_float.md#class-float) **angular_spring_x/stiffness** = `0.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-spring-x-stiffness)

- void **set_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-generic6dofjoint3d-property-angular-spring-y-damping"></a>

[float](class_float.md#class-float) **angular_spring_y/damping** = `0.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-spring-y-damping)

- void **set_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-generic6dofjoint3d-property-angular-spring-y-enabled"></a>

[bool](class_bool.md#class-bool) **angular_spring_y/enabled** = `false` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-spring-y-enabled)

- void **set_flag_y**(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag), value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flag_y**(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag)) const

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-generic6dofjoint3d-property-angular-spring-y-equilibrium-point"></a>

[float](class_float.md#class-float) **angular_spring_y/equilibrium_point** = `0.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-spring-y-equilibrium-point)

- void **set_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-generic6dofjoint3d-property-angular-spring-y-stiffness"></a>

[float](class_float.md#class-float) **angular_spring_y/stiffness** = `0.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-spring-y-stiffness)

- void **set_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-generic6dofjoint3d-property-angular-spring-z-damping"></a>

[float](class_float.md#class-float) **angular_spring_z/damping** = `0.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-spring-z-damping)

- void **set_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-generic6dofjoint3d-property-angular-spring-z-enabled"></a>

[bool](class_bool.md#class-bool) **angular_spring_z/enabled** = `false` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-spring-z-enabled)

- void **set_flag_z**(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag), value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flag_z**(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag)) const

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-generic6dofjoint3d-property-angular-spring-z-equilibrium-point"></a>

[float](class_float.md#class-float) **angular_spring_z/equilibrium_point** = `0.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-spring-z-equilibrium-point)

- void **set_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-generic6dofjoint3d-property-angular-spring-z-stiffness"></a>

[float](class_float.md#class-float) **angular_spring_z/stiffness** = `0.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-angular-spring-z-stiffness)

- void **set_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-generic6dofjoint3d-property-linear-limit-x-damping"></a>

[float](class_float.md#class-float) **linear_limit_x/damping** = `1.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-limit-x-damping)

- void **set_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

The amount of damping that happens at the X motion.

---


<a id="class-generic6dofjoint3d-property-linear-limit-x-enabled"></a>

[bool](class_bool.md#class-bool) **linear_limit_x/enabled** = `true` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-limit-x-enabled)

- void **set_flag_x**(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag), value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flag_x**(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag)) const

If `true`, the linear motion across the X axis is limited.

---


<a id="class-generic6dofjoint3d-property-linear-limit-x-lower-distance"></a>

[float](class_float.md#class-float) **linear_limit_x/lower_distance** = `0.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-limit-x-lower-distance)

- void **set_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

The minimum difference between the pivot points' X axis.

---


<a id="class-generic6dofjoint3d-property-linear-limit-x-restitution"></a>

[float](class_float.md#class-float) **linear_limit_x/restitution** = `0.5` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-limit-x-restitution)

- void **set_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

The amount of restitution on the X axis movement. The lower, the more momentum gets lost.

---


<a id="class-generic6dofjoint3d-property-linear-limit-x-softness"></a>

[float](class_float.md#class-float) **linear_limit_x/softness** = `0.7` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-limit-x-softness)

- void **set_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

A factor applied to the movement across the X axis. The lower, the slower the movement.

---


<a id="class-generic6dofjoint3d-property-linear-limit-x-upper-distance"></a>

[float](class_float.md#class-float) **linear_limit_x/upper_distance** = `0.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-limit-x-upper-distance)

- void **set_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

The maximum difference between the pivot points' X axis.

---


<a id="class-generic6dofjoint3d-property-linear-limit-y-damping"></a>

[float](class_float.md#class-float) **linear_limit_y/damping** = `1.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-limit-y-damping)

- void **set_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

The amount of damping that happens at the Y motion.

---


<a id="class-generic6dofjoint3d-property-linear-limit-y-enabled"></a>

[bool](class_bool.md#class-bool) **linear_limit_y/enabled** = `true` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-limit-y-enabled)

- void **set_flag_y**(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag), value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flag_y**(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag)) const

If `true`, the linear motion across the Y axis is limited.

---


<a id="class-generic6dofjoint3d-property-linear-limit-y-lower-distance"></a>

[float](class_float.md#class-float) **linear_limit_y/lower_distance** = `0.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-limit-y-lower-distance)

- void **set_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

The minimum difference between the pivot points' Y axis.

---


<a id="class-generic6dofjoint3d-property-linear-limit-y-restitution"></a>

[float](class_float.md#class-float) **linear_limit_y/restitution** = `0.5` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-limit-y-restitution)

- void **set_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

The amount of restitution on the Y axis movement. The lower, the more momentum gets lost.

---


<a id="class-generic6dofjoint3d-property-linear-limit-y-softness"></a>

[float](class_float.md#class-float) **linear_limit_y/softness** = `0.7` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-limit-y-softness)

- void **set_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

A factor applied to the movement across the Y axis. The lower, the slower the movement.

---


<a id="class-generic6dofjoint3d-property-linear-limit-y-upper-distance"></a>

[float](class_float.md#class-float) **linear_limit_y/upper_distance** = `0.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-limit-y-upper-distance)

- void **set_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

The maximum difference between the pivot points' Y axis.

---


<a id="class-generic6dofjoint3d-property-linear-limit-z-damping"></a>

[float](class_float.md#class-float) **linear_limit_z/damping** = `1.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-limit-z-damping)

- void **set_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

The amount of damping that happens at the Z motion.

---


<a id="class-generic6dofjoint3d-property-linear-limit-z-enabled"></a>

[bool](class_bool.md#class-bool) **linear_limit_z/enabled** = `true` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-limit-z-enabled)

- void **set_flag_z**(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag), value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flag_z**(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag)) const

If `true`, the linear motion across the Z axis is limited.

---


<a id="class-generic6dofjoint3d-property-linear-limit-z-lower-distance"></a>

[float](class_float.md#class-float) **linear_limit_z/lower_distance** = `0.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-limit-z-lower-distance)

- void **set_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

The minimum difference between the pivot points' Z axis.

---


<a id="class-generic6dofjoint3d-property-linear-limit-z-restitution"></a>

[float](class_float.md#class-float) **linear_limit_z/restitution** = `0.5` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-limit-z-restitution)

- void **set_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

The amount of restitution on the Z axis movement. The lower, the more momentum gets lost.

---


<a id="class-generic6dofjoint3d-property-linear-limit-z-softness"></a>

[float](class_float.md#class-float) **linear_limit_z/softness** = `0.7` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-limit-z-softness)

- void **set_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

A factor applied to the movement across the Z axis. The lower, the slower the movement.

---


<a id="class-generic6dofjoint3d-property-linear-limit-z-upper-distance"></a>

[float](class_float.md#class-float) **linear_limit_z/upper_distance** = `0.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-limit-z-upper-distance)

- void **set_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

The maximum difference between the pivot points' Z axis.

---


<a id="class-generic6dofjoint3d-property-linear-motor-x-enabled"></a>

[bool](class_bool.md#class-bool) **linear_motor_x/enabled** = `false` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-motor-x-enabled)

- void **set_flag_x**(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag), value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flag_x**(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag)) const

If `true`, then there is a linear motor on the X axis. It will attempt to reach the target velocity while staying within the force limits.

---


<a id="class-generic6dofjoint3d-property-linear-motor-x-force-limit"></a>

[float](class_float.md#class-float) **linear_motor_x/force_limit** = `0.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-motor-x-force-limit)

- void **set_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

The maximum force the linear motor can apply on the X axis while trying to reach the target velocity.

---


<a id="class-generic6dofjoint3d-property-linear-motor-x-target-velocity"></a>

[float](class_float.md#class-float) **linear_motor_x/target_velocity** = `0.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-motor-x-target-velocity)

- void **set_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

The speed that the linear motor will attempt to reach on the X axis.

---


<a id="class-generic6dofjoint3d-property-linear-motor-y-enabled"></a>

[bool](class_bool.md#class-bool) **linear_motor_y/enabled** = `false` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-motor-y-enabled)

- void **set_flag_y**(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag), value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flag_y**(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag)) const

If `true`, then there is a linear motor on the Y axis. It will attempt to reach the target velocity while staying within the force limits.

---


<a id="class-generic6dofjoint3d-property-linear-motor-y-force-limit"></a>

[float](class_float.md#class-float) **linear_motor_y/force_limit** = `0.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-motor-y-force-limit)

- void **set_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

The maximum force the linear motor can apply on the Y axis while trying to reach the target velocity.

---


<a id="class-generic6dofjoint3d-property-linear-motor-y-target-velocity"></a>

[float](class_float.md#class-float) **linear_motor_y/target_velocity** = `0.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-motor-y-target-velocity)

- void **set_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

The speed that the linear motor will attempt to reach on the Y axis.

---


<a id="class-generic6dofjoint3d-property-linear-motor-z-enabled"></a>

[bool](class_bool.md#class-bool) **linear_motor_z/enabled** = `false` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-motor-z-enabled)

- void **set_flag_z**(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag), value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flag_z**(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag)) const

If `true`, then there is a linear motor on the Z axis. It will attempt to reach the target velocity while staying within the force limits.

---


<a id="class-generic6dofjoint3d-property-linear-motor-z-force-limit"></a>

[float](class_float.md#class-float) **linear_motor_z/force_limit** = `0.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-motor-z-force-limit)

- void **set_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

The maximum force the linear motor can apply on the Z axis while trying to reach the target velocity.

---


<a id="class-generic6dofjoint3d-property-linear-motor-z-target-velocity"></a>

[float](class_float.md#class-float) **linear_motor_z/target_velocity** = `0.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-motor-z-target-velocity)

- void **set_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

The speed that the linear motor will attempt to reach on the Z axis.

---


<a id="class-generic6dofjoint3d-property-linear-spring-x-damping"></a>

[float](class_float.md#class-float) **linear_spring_x/damping** = `0.01` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-spring-x-damping)

- void **set_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-generic6dofjoint3d-property-linear-spring-x-enabled"></a>

[bool](class_bool.md#class-bool) **linear_spring_x/enabled** = `false` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-spring-x-enabled)

- void **set_flag_x**(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag), value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flag_x**(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag)) const

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-generic6dofjoint3d-property-linear-spring-x-equilibrium-point"></a>

[float](class_float.md#class-float) **linear_spring_x/equilibrium_point** = `0.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-spring-x-equilibrium-point)

- void **set_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-generic6dofjoint3d-property-linear-spring-x-stiffness"></a>

[float](class_float.md#class-float) **linear_spring_x/stiffness** = `0.01` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-spring-x-stiffness)

- void **set_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-generic6dofjoint3d-property-linear-spring-y-damping"></a>

[float](class_float.md#class-float) **linear_spring_y/damping** = `0.01` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-spring-y-damping)

- void **set_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-generic6dofjoint3d-property-linear-spring-y-enabled"></a>

[bool](class_bool.md#class-bool) **linear_spring_y/enabled** = `false` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-spring-y-enabled)

- void **set_flag_y**(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag), value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flag_y**(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag)) const

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-generic6dofjoint3d-property-linear-spring-y-equilibrium-point"></a>

[float](class_float.md#class-float) **linear_spring_y/equilibrium_point** = `0.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-spring-y-equilibrium-point)

- void **set_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-generic6dofjoint3d-property-linear-spring-y-stiffness"></a>

[float](class_float.md#class-float) **linear_spring_y/stiffness** = `0.01` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-spring-y-stiffness)

- void **set_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-generic6dofjoint3d-property-linear-spring-z-damping"></a>

[float](class_float.md#class-float) **linear_spring_z/damping** = `0.01` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-spring-z-damping)

- void **set_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-generic6dofjoint3d-property-linear-spring-z-enabled"></a>

[bool](class_bool.md#class-bool) **linear_spring_z/enabled** = `false` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-spring-z-enabled)

- void **set_flag_z**(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag), value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flag_z**(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag)) const

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-generic6dofjoint3d-property-linear-spring-z-equilibrium-point"></a>

[float](class_float.md#class-float) **linear_spring_z/equilibrium_point** = `0.0` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-spring-z-equilibrium-point)

- void **set_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-generic6dofjoint3d-property-linear-spring-z-stiffness"></a>

[float](class_float.md#class-float) **linear_spring_z/stiffness** = `0.01` [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-property-linear-spring-z-stiffness)

- void **set_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-generic6dofjoint3d-method-get-flag-x"></a>

[bool](class_bool.md#class-bool) **get_flag_x**(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag)) const [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-method-get-flag-x)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-generic6dofjoint3d-method-get-flag-y"></a>

[bool](class_bool.md#class-bool) **get_flag_y**(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag)) const [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-method-get-flag-y)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-generic6dofjoint3d-method-get-flag-z"></a>

[bool](class_bool.md#class-bool) **get_flag_z**(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag)) const [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-method-get-flag-z)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-generic6dofjoint3d-method-get-param-x"></a>

[float](class_float.md#class-float) **get_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-method-get-param-x)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-generic6dofjoint3d-method-get-param-y"></a>

[float](class_float.md#class-float) **get_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-method-get-param-y)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-generic6dofjoint3d-method-get-param-z"></a>

[float](class_float.md#class-float) **get_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param)) const [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-method-get-param-z)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-generic6dofjoint3d-method-set-flag-x"></a>

void **set_flag_x**(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag), value: [bool](class_bool.md#class-bool)) [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-method-set-flag-x)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-generic6dofjoint3d-method-set-flag-y"></a>

void **set_flag_y**(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag), value: [bool](class_bool.md#class-bool)) [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-method-set-flag-y)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-generic6dofjoint3d-method-set-flag-z"></a>

void **set_flag_z**(flag: [Flag](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-flag), value: [bool](class_bool.md#class-bool)) [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-method-set-flag-z)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-generic6dofjoint3d-method-set-param-x"></a>

void **set_param_x**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float)) [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-method-set-param-x)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-generic6dofjoint3d-method-set-param-y"></a>

void **set_param_y**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float)) [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-method-set-param-y)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-generic6dofjoint3d-method-set-param-z"></a>

void **set_param_z**(param: [Param](class_generic6dofjoint3d.md#enum-generic6dofjoint3d-param), value: [float](class_float.md#class-float)) [🔗](class_generic6dofjoint3d.md#class-generic6dofjoint3d-method-set-param-z)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!
