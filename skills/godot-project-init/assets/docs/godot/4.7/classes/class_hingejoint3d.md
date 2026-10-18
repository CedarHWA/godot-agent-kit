> Source: https://docs.godotengine.org/en/4.7/classes/class_hingejoint3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="hingejoint3d"></a>

<a id="class-hingejoint3d"></a>

# HingeJoint3D

**Inherits:** [Joint3D](class_joint3d.md#class-joint3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A physics joint that restricts the rotation of a 3D physics body around an axis relative to another physics body.

<a id="description"></a>

## Description

A physics joint that restricts the rotation of a 3D physics body around an axis relative to another physics body. For example, Body A can be a [StaticBody3D](class_staticbody3d.md#class-staticbody3d) representing a door hinge that a [RigidBody3D](class_rigidbody3d.md#class-rigidbody3d) rotates around.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [angular_limit/bias](class_hingejoint3d.md#class-hingejoint3d-property-angular-limit-bias) | `0.3` |
| [bool](class_bool.md#class-bool) | [angular_limit/enable](class_hingejoint3d.md#class-hingejoint3d-property-angular-limit-enable) | `false` |
| [float](class_float.md#class-float) | [angular_limit/lower](class_hingejoint3d.md#class-hingejoint3d-property-angular-limit-lower) | `-1.5707964` |
| [float](class_float.md#class-float) | [angular_limit/relaxation](class_hingejoint3d.md#class-hingejoint3d-property-angular-limit-relaxation) | `1.0` |
| [float](class_float.md#class-float) | [angular_limit/softness](class_hingejoint3d.md#class-hingejoint3d-property-angular-limit-softness) | `0.9` |
| [float](class_float.md#class-float) | [angular_limit/upper](class_hingejoint3d.md#class-hingejoint3d-property-angular-limit-upper) | `1.5707964` |
| [bool](class_bool.md#class-bool) | [motor/enable](class_hingejoint3d.md#class-hingejoint3d-property-motor-enable) | `false` |
| [float](class_float.md#class-float) | [motor/max_impulse](class_hingejoint3d.md#class-hingejoint3d-property-motor-max-impulse) | `1.0` |
| [float](class_float.md#class-float) | [motor/target_velocity](class_hingejoint3d.md#class-hingejoint3d-property-motor-target-velocity) | `1.0` |
| [float](class_float.md#class-float) | [params/bias](class_hingejoint3d.md#class-hingejoint3d-property-params-bias) | `0.3` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [get_flag](class_hingejoint3d.md#class-hingejoint3d-method-get-flag)(flag: [Flag](class_hingejoint3d.md#enum-hingejoint3d-flag)) const |
| [float](class_float.md#class-float) | [get_param](class_hingejoint3d.md#class-hingejoint3d-method-get-param)(param: [Param](class_hingejoint3d.md#enum-hingejoint3d-param)) const |
| void | [set_flag](class_hingejoint3d.md#class-hingejoint3d-method-set-flag)(flag: [Flag](class_hingejoint3d.md#enum-hingejoint3d-flag), enabled: [bool](class_bool.md#class-bool)) |
| void | [set_param](class_hingejoint3d.md#class-hingejoint3d-method-set-param)(param: [Param](class_hingejoint3d.md#enum-hingejoint3d-param), value: [float](class_float.md#class-float)) |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-hingejoint3d-param"></a>

enum **Param**: [🔗](class_hingejoint3d.md#enum-hingejoint3d-param)

<a id="class-hingejoint3d-constant-param-bias"></a>

[Param](class_hingejoint3d.md#enum-hingejoint3d-param) **PARAM_BIAS** = `0`

The speed with which the two bodies get pulled together when they move in different directions.

<a id="class-hingejoint3d-constant-param-limit-upper"></a>

[Param](class_hingejoint3d.md#enum-hingejoint3d-param) **PARAM_LIMIT_UPPER** = `1`

The maximum rotation. Only active if [angular_limit/enable](class_hingejoint3d.md#class-hingejoint3d-property-angular-limit-enable) is `true`.

<a id="class-hingejoint3d-constant-param-limit-lower"></a>

[Param](class_hingejoint3d.md#enum-hingejoint3d-param) **PARAM_LIMIT_LOWER** = `2`

The minimum rotation. Only active if [angular_limit/enable](class_hingejoint3d.md#class-hingejoint3d-property-angular-limit-enable) is `true`.

<a id="class-hingejoint3d-constant-param-limit-bias"></a>

[Param](class_hingejoint3d.md#enum-hingejoint3d-param) **PARAM_LIMIT_BIAS** = `3`

The speed with which the rotation across the axis perpendicular to the hinge gets corrected.

<a id="class-hingejoint3d-constant-param-limit-softness"></a>

[Param](class_hingejoint3d.md#enum-hingejoint3d-param) **PARAM_LIMIT_SOFTNESS** = `4`

**Deprecated:** This property is never used by the engine and is kept for compatibility purpose.

<a id="class-hingejoint3d-constant-param-limit-relaxation"></a>

[Param](class_hingejoint3d.md#enum-hingejoint3d-param) **PARAM_LIMIT_RELAXATION** = `5`

The lower this value, the more the rotation gets slowed down.

<a id="class-hingejoint3d-constant-param-motor-target-velocity"></a>

[Param](class_hingejoint3d.md#enum-hingejoint3d-param) **PARAM_MOTOR_TARGET_VELOCITY** = `6`

Target speed for the motor.

<a id="class-hingejoint3d-constant-param-motor-max-impulse"></a>

[Param](class_hingejoint3d.md#enum-hingejoint3d-param) **PARAM_MOTOR_MAX_IMPULSE** = `7`

Maximum acceleration for the motor.

<a id="class-hingejoint3d-constant-param-max"></a>

[Param](class_hingejoint3d.md#enum-hingejoint3d-param) **PARAM_MAX** = `8`

Represents the size of the [Param](class_hingejoint3d.md#enum-hingejoint3d-param) enum.

---


<a id="enum-hingejoint3d-flag"></a>

enum **Flag**: [🔗](class_hingejoint3d.md#enum-hingejoint3d-flag)

<a id="class-hingejoint3d-constant-flag-use-limit"></a>

[Flag](class_hingejoint3d.md#enum-hingejoint3d-flag) **FLAG_USE_LIMIT** = `0`

If `true`, the hinges maximum and minimum rotation, defined by [angular_limit/lower](class_hingejoint3d.md#class-hingejoint3d-property-angular-limit-lower) and [angular_limit/upper](class_hingejoint3d.md#class-hingejoint3d-property-angular-limit-upper) has effects.

<a id="class-hingejoint3d-constant-flag-enable-motor"></a>

[Flag](class_hingejoint3d.md#enum-hingejoint3d-flag) **FLAG_ENABLE_MOTOR** = `1`

When activated, a motor turns the hinge.

<a id="class-hingejoint3d-constant-flag-max"></a>

[Flag](class_hingejoint3d.md#enum-hingejoint3d-flag) **FLAG_MAX** = `2`

Represents the size of the [Flag](class_hingejoint3d.md#enum-hingejoint3d-flag) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-hingejoint3d-property-angular-limit-bias"></a>

[float](class_float.md#class-float) **angular_limit/bias** = `0.3` [🔗](class_hingejoint3d.md#class-hingejoint3d-property-angular-limit-bias)

- void **set_param**(param: [Param](class_hingejoint3d.md#enum-hingejoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: [Param](class_hingejoint3d.md#enum-hingejoint3d-param)) const

The speed with which the rotation across the axis perpendicular to the hinge gets corrected.

---


<a id="class-hingejoint3d-property-angular-limit-enable"></a>

[bool](class_bool.md#class-bool) **angular_limit/enable** = `false` [🔗](class_hingejoint3d.md#class-hingejoint3d-property-angular-limit-enable)

- void **set_flag**(flag: [Flag](class_hingejoint3d.md#enum-hingejoint3d-flag), enabled: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flag**(flag: [Flag](class_hingejoint3d.md#enum-hingejoint3d-flag)) const

If `true`, the hinges maximum and minimum rotation, defined by [angular_limit/lower](class_hingejoint3d.md#class-hingejoint3d-property-angular-limit-lower) and [angular_limit/upper](class_hingejoint3d.md#class-hingejoint3d-property-angular-limit-upper) has effects.

---


<a id="class-hingejoint3d-property-angular-limit-lower"></a>

[float](class_float.md#class-float) **angular_limit/lower** = `-1.5707964` [🔗](class_hingejoint3d.md#class-hingejoint3d-property-angular-limit-lower)

- void **set_param**(param: [Param](class_hingejoint3d.md#enum-hingejoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: [Param](class_hingejoint3d.md#enum-hingejoint3d-param)) const

The minimum rotation. Only active if [angular_limit/enable](class_hingejoint3d.md#class-hingejoint3d-property-angular-limit-enable) is `true`.

---


<a id="class-hingejoint3d-property-angular-limit-relaxation"></a>

[float](class_float.md#class-float) **angular_limit/relaxation** = `1.0` [🔗](class_hingejoint3d.md#class-hingejoint3d-property-angular-limit-relaxation)

- void **set_param**(param: [Param](class_hingejoint3d.md#enum-hingejoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: [Param](class_hingejoint3d.md#enum-hingejoint3d-param)) const

The lower this value, the more the rotation gets slowed down.

---


<a id="class-hingejoint3d-property-angular-limit-softness"></a>

[float](class_float.md#class-float) **angular_limit/softness** = `0.9` [🔗](class_hingejoint3d.md#class-hingejoint3d-property-angular-limit-softness)

- void **set_param**(param: [Param](class_hingejoint3d.md#enum-hingejoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: [Param](class_hingejoint3d.md#enum-hingejoint3d-param)) const

**Deprecated:** This property is never set by the engine and is kept for compatibility purposes.

---


<a id="class-hingejoint3d-property-angular-limit-upper"></a>

[float](class_float.md#class-float) **angular_limit/upper** = `1.5707964` [🔗](class_hingejoint3d.md#class-hingejoint3d-property-angular-limit-upper)

- void **set_param**(param: [Param](class_hingejoint3d.md#enum-hingejoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: [Param](class_hingejoint3d.md#enum-hingejoint3d-param)) const

The maximum rotation. Only active if [angular_limit/enable](class_hingejoint3d.md#class-hingejoint3d-property-angular-limit-enable) is `true`.

---


<a id="class-hingejoint3d-property-motor-enable"></a>

[bool](class_bool.md#class-bool) **motor/enable** = `false` [🔗](class_hingejoint3d.md#class-hingejoint3d-property-motor-enable)

- void **set_flag**(flag: [Flag](class_hingejoint3d.md#enum-hingejoint3d-flag), enabled: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flag**(flag: [Flag](class_hingejoint3d.md#enum-hingejoint3d-flag)) const

When activated, a motor turns the hinge.

---


<a id="class-hingejoint3d-property-motor-max-impulse"></a>

[float](class_float.md#class-float) **motor/max_impulse** = `1.0` [🔗](class_hingejoint3d.md#class-hingejoint3d-property-motor-max-impulse)

- void **set_param**(param: [Param](class_hingejoint3d.md#enum-hingejoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: [Param](class_hingejoint3d.md#enum-hingejoint3d-param)) const

Maximum acceleration for the motor.

---


<a id="class-hingejoint3d-property-motor-target-velocity"></a>

[float](class_float.md#class-float) **motor/target_velocity** = `1.0` [🔗](class_hingejoint3d.md#class-hingejoint3d-property-motor-target-velocity)

- void **set_param**(param: [Param](class_hingejoint3d.md#enum-hingejoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: [Param](class_hingejoint3d.md#enum-hingejoint3d-param)) const

Target speed for the motor.

---


<a id="class-hingejoint3d-property-params-bias"></a>

[float](class_float.md#class-float) **params/bias** = `0.3` [🔗](class_hingejoint3d.md#class-hingejoint3d-property-params-bias)

- void **set_param**(param: [Param](class_hingejoint3d.md#enum-hingejoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: [Param](class_hingejoint3d.md#enum-hingejoint3d-param)) const

The speed with which the two bodies get pulled together when they move in different directions.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-hingejoint3d-method-get-flag"></a>

[bool](class_bool.md#class-bool) **get_flag**(flag: [Flag](class_hingejoint3d.md#enum-hingejoint3d-flag)) const [🔗](class_hingejoint3d.md#class-hingejoint3d-method-get-flag)

Returns the value of the specified flag.

---


<a id="class-hingejoint3d-method-get-param"></a>

[float](class_float.md#class-float) **get_param**(param: [Param](class_hingejoint3d.md#enum-hingejoint3d-param)) const [🔗](class_hingejoint3d.md#class-hingejoint3d-method-get-param)

Returns the value of the specified parameter.

---


<a id="class-hingejoint3d-method-set-flag"></a>

void **set_flag**(flag: [Flag](class_hingejoint3d.md#enum-hingejoint3d-flag), enabled: [bool](class_bool.md#class-bool)) [🔗](class_hingejoint3d.md#class-hingejoint3d-method-set-flag)

If `true`, enables the specified flag.

---


<a id="class-hingejoint3d-method-set-param"></a>

void **set_param**(param: [Param](class_hingejoint3d.md#enum-hingejoint3d-param), value: [float](class_float.md#class-float)) [🔗](class_hingejoint3d.md#class-hingejoint3d-method-set-param)

Sets the value of the specified parameter.
