> Source: https://docs.godotengine.org/en/4.7/classes/class_sliderjoint3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="sliderjoint3d"></a>

<a id="class-sliderjoint3d"></a>

# SliderJoint3D

**Inherits:** [Joint3D](class_joint3d.md#class-joint3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A physics joint that restricts the movement of a 3D physics body along an axis relative to another physics body.

<a id="description"></a>

## Description

A physics joint that restricts the movement of a 3D physics body along an axis relative to another physics body. For example, Body A could be a [StaticBody3D](class_staticbody3d.md#class-staticbody3d) representing a piston base, while Body B could be a [RigidBody3D](class_rigidbody3d.md#class-rigidbody3d) representing the piston head, moving up and down.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [angular_limit/damping](class_sliderjoint3d.md#class-sliderjoint3d-property-angular-limit-damping) | `0.0` |
| [float](class_float.md#class-float) | [angular_limit/lower_angle](class_sliderjoint3d.md#class-sliderjoint3d-property-angular-limit-lower-angle) | `0.0` |
| [float](class_float.md#class-float) | [angular_limit/restitution](class_sliderjoint3d.md#class-sliderjoint3d-property-angular-limit-restitution) | `0.7` |
| [float](class_float.md#class-float) | [angular_limit/softness](class_sliderjoint3d.md#class-sliderjoint3d-property-angular-limit-softness) | `1.0` |
| [float](class_float.md#class-float) | [angular_limit/upper_angle](class_sliderjoint3d.md#class-sliderjoint3d-property-angular-limit-upper-angle) | `0.0` |
| [float](class_float.md#class-float) | [angular_motion/damping](class_sliderjoint3d.md#class-sliderjoint3d-property-angular-motion-damping) | `1.0` |
| [float](class_float.md#class-float) | [angular_motion/restitution](class_sliderjoint3d.md#class-sliderjoint3d-property-angular-motion-restitution) | `0.7` |
| [float](class_float.md#class-float) | [angular_motion/softness](class_sliderjoint3d.md#class-sliderjoint3d-property-angular-motion-softness) | `1.0` |
| [float](class_float.md#class-float) | [angular_ortho/damping](class_sliderjoint3d.md#class-sliderjoint3d-property-angular-ortho-damping) | `1.0` |
| [float](class_float.md#class-float) | [angular_ortho/restitution](class_sliderjoint3d.md#class-sliderjoint3d-property-angular-ortho-restitution) | `0.7` |
| [float](class_float.md#class-float) | [angular_ortho/softness](class_sliderjoint3d.md#class-sliderjoint3d-property-angular-ortho-softness) | `1.0` |
| [float](class_float.md#class-float) | [linear_limit/damping](class_sliderjoint3d.md#class-sliderjoint3d-property-linear-limit-damping) | `1.0` |
| [float](class_float.md#class-float) | [linear_limit/lower_distance](class_sliderjoint3d.md#class-sliderjoint3d-property-linear-limit-lower-distance) | `-1.0` |
| [float](class_float.md#class-float) | [linear_limit/restitution](class_sliderjoint3d.md#class-sliderjoint3d-property-linear-limit-restitution) | `0.7` |
| [float](class_float.md#class-float) | [linear_limit/softness](class_sliderjoint3d.md#class-sliderjoint3d-property-linear-limit-softness) | `1.0` |
| [float](class_float.md#class-float) | [linear_limit/upper_distance](class_sliderjoint3d.md#class-sliderjoint3d-property-linear-limit-upper-distance) | `1.0` |
| [float](class_float.md#class-float) | [linear_motion/damping](class_sliderjoint3d.md#class-sliderjoint3d-property-linear-motion-damping) | `0.0` |
| [float](class_float.md#class-float) | [linear_motion/restitution](class_sliderjoint3d.md#class-sliderjoint3d-property-linear-motion-restitution) | `0.7` |
| [float](class_float.md#class-float) | [linear_motion/softness](class_sliderjoint3d.md#class-sliderjoint3d-property-linear-motion-softness) | `1.0` |
| [float](class_float.md#class-float) | [linear_ortho/damping](class_sliderjoint3d.md#class-sliderjoint3d-property-linear-ortho-damping) | `1.0` |
| [float](class_float.md#class-float) | [linear_ortho/restitution](class_sliderjoint3d.md#class-sliderjoint3d-property-linear-ortho-restitution) | `0.7` |
| [float](class_float.md#class-float) | [linear_ortho/softness](class_sliderjoint3d.md#class-sliderjoint3d-property-linear-ortho-softness) | `1.0` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [float](class_float.md#class-float) | [get_param](class_sliderjoint3d.md#class-sliderjoint3d-method-get-param)(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param)) const |
| void | [set_param](class_sliderjoint3d.md#class-sliderjoint3d-method-set-param)(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param), value: [float](class_float.md#class-float)) |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-sliderjoint3d-param"></a>

enum **Param**: [🔗](class_sliderjoint3d.md#enum-sliderjoint3d-param)

<a id="class-sliderjoint3d-constant-param-linear-limit-upper"></a>

[Param](class_sliderjoint3d.md#enum-sliderjoint3d-param) **PARAM_LINEAR_LIMIT_UPPER** = `0`

Constant for accessing [linear_limit/upper_distance](class_sliderjoint3d.md#class-sliderjoint3d-property-linear-limit-upper-distance). The maximum difference between the pivot points on their X axis before damping happens.

<a id="class-sliderjoint3d-constant-param-linear-limit-lower"></a>

[Param](class_sliderjoint3d.md#enum-sliderjoint3d-param) **PARAM_LINEAR_LIMIT_LOWER** = `1`

Constant for accessing [linear_limit/lower_distance](class_sliderjoint3d.md#class-sliderjoint3d-property-linear-limit-lower-distance). The minimum difference between the pivot points on their X axis before damping happens.

<a id="class-sliderjoint3d-constant-param-linear-limit-softness"></a>

[Param](class_sliderjoint3d.md#enum-sliderjoint3d-param) **PARAM_LINEAR_LIMIT_SOFTNESS** = `2`

Constant for accessing [linear_limit/softness](class_sliderjoint3d.md#class-sliderjoint3d-property-linear-limit-softness). A factor applied to the movement across the slider axis once the limits get surpassed. The lower, the slower the movement.

<a id="class-sliderjoint3d-constant-param-linear-limit-restitution"></a>

[Param](class_sliderjoint3d.md#enum-sliderjoint3d-param) **PARAM_LINEAR_LIMIT_RESTITUTION** = `3`

Constant for accessing [linear_limit/restitution](class_sliderjoint3d.md#class-sliderjoint3d-property-linear-limit-restitution). The amount of restitution once the limits are surpassed. The lower, the more velocity-energy gets lost.

<a id="class-sliderjoint3d-constant-param-linear-limit-damping"></a>

[Param](class_sliderjoint3d.md#enum-sliderjoint3d-param) **PARAM_LINEAR_LIMIT_DAMPING** = `4`

Constant for accessing [linear_limit/damping](class_sliderjoint3d.md#class-sliderjoint3d-property-linear-limit-damping). The amount of damping once the slider limits are surpassed.

<a id="class-sliderjoint3d-constant-param-linear-motion-softness"></a>

[Param](class_sliderjoint3d.md#enum-sliderjoint3d-param) **PARAM_LINEAR_MOTION_SOFTNESS** = `5`

Constant for accessing [linear_motion/softness](class_sliderjoint3d.md#class-sliderjoint3d-property-linear-motion-softness). A factor applied to the movement across the slider axis as long as the slider is in the limits. The lower, the slower the movement.

<a id="class-sliderjoint3d-constant-param-linear-motion-restitution"></a>

[Param](class_sliderjoint3d.md#enum-sliderjoint3d-param) **PARAM_LINEAR_MOTION_RESTITUTION** = `6`

Constant for accessing [linear_motion/restitution](class_sliderjoint3d.md#class-sliderjoint3d-property-linear-motion-restitution). The amount of restitution inside the slider limits.

<a id="class-sliderjoint3d-constant-param-linear-motion-damping"></a>

[Param](class_sliderjoint3d.md#enum-sliderjoint3d-param) **PARAM_LINEAR_MOTION_DAMPING** = `7`

Constant for accessing [linear_motion/damping](class_sliderjoint3d.md#class-sliderjoint3d-property-linear-motion-damping). The amount of damping inside the slider limits.

<a id="class-sliderjoint3d-constant-param-linear-orthogonal-softness"></a>

[Param](class_sliderjoint3d.md#enum-sliderjoint3d-param) **PARAM_LINEAR_ORTHOGONAL_SOFTNESS** = `8`

Constant for accessing [linear_ortho/softness](class_sliderjoint3d.md#class-sliderjoint3d-property-linear-ortho-softness). A factor applied to the movement across axes orthogonal to the slider.

<a id="class-sliderjoint3d-constant-param-linear-orthogonal-restitution"></a>

[Param](class_sliderjoint3d.md#enum-sliderjoint3d-param) **PARAM_LINEAR_ORTHOGONAL_RESTITUTION** = `9`

Constant for accessing [linear_motion/restitution](class_sliderjoint3d.md#class-sliderjoint3d-property-linear-motion-restitution). The amount of restitution when movement is across axes orthogonal to the slider.

<a id="class-sliderjoint3d-constant-param-linear-orthogonal-damping"></a>

[Param](class_sliderjoint3d.md#enum-sliderjoint3d-param) **PARAM_LINEAR_ORTHOGONAL_DAMPING** = `10`

Constant for accessing [linear_motion/damping](class_sliderjoint3d.md#class-sliderjoint3d-property-linear-motion-damping). The amount of damping when movement is across axes orthogonal to the slider.

<a id="class-sliderjoint3d-constant-param-angular-limit-upper"></a>

[Param](class_sliderjoint3d.md#enum-sliderjoint3d-param) **PARAM_ANGULAR_LIMIT_UPPER** = `11`

Constant for accessing [angular_limit/upper_angle](class_sliderjoint3d.md#class-sliderjoint3d-property-angular-limit-upper-angle). The upper limit of rotation in the slider.

<a id="class-sliderjoint3d-constant-param-angular-limit-lower"></a>

[Param](class_sliderjoint3d.md#enum-sliderjoint3d-param) **PARAM_ANGULAR_LIMIT_LOWER** = `12`

Constant for accessing [angular_limit/lower_angle](class_sliderjoint3d.md#class-sliderjoint3d-property-angular-limit-lower-angle). The lower limit of rotation in the slider.

<a id="class-sliderjoint3d-constant-param-angular-limit-softness"></a>

[Param](class_sliderjoint3d.md#enum-sliderjoint3d-param) **PARAM_ANGULAR_LIMIT_SOFTNESS** = `13`

Constant for accessing [angular_limit/softness](class_sliderjoint3d.md#class-sliderjoint3d-property-angular-limit-softness). A factor applied to the all rotation once the limit is surpassed.

<a id="class-sliderjoint3d-constant-param-angular-limit-restitution"></a>

[Param](class_sliderjoint3d.md#enum-sliderjoint3d-param) **PARAM_ANGULAR_LIMIT_RESTITUTION** = `14`

Constant for accessing [angular_limit/restitution](class_sliderjoint3d.md#class-sliderjoint3d-property-angular-limit-restitution). The amount of restitution of the rotation when the limit is surpassed.

<a id="class-sliderjoint3d-constant-param-angular-limit-damping"></a>

[Param](class_sliderjoint3d.md#enum-sliderjoint3d-param) **PARAM_ANGULAR_LIMIT_DAMPING** = `15`

Constant for accessing [angular_limit/damping](class_sliderjoint3d.md#class-sliderjoint3d-property-angular-limit-damping). The amount of damping of the rotation when the limit is surpassed.

<a id="class-sliderjoint3d-constant-param-angular-motion-softness"></a>

[Param](class_sliderjoint3d.md#enum-sliderjoint3d-param) **PARAM_ANGULAR_MOTION_SOFTNESS** = `16`

Constant for accessing [angular_motion/softness](class_sliderjoint3d.md#class-sliderjoint3d-property-angular-motion-softness). A factor applied to the all rotation in the limits.

<a id="class-sliderjoint3d-constant-param-angular-motion-restitution"></a>

[Param](class_sliderjoint3d.md#enum-sliderjoint3d-param) **PARAM_ANGULAR_MOTION_RESTITUTION** = `17`

Constant for accessing [angular_motion/restitution](class_sliderjoint3d.md#class-sliderjoint3d-property-angular-motion-restitution). The amount of restitution of the rotation in the limits.

<a id="class-sliderjoint3d-constant-param-angular-motion-damping"></a>

[Param](class_sliderjoint3d.md#enum-sliderjoint3d-param) **PARAM_ANGULAR_MOTION_DAMPING** = `18`

Constant for accessing [angular_motion/damping](class_sliderjoint3d.md#class-sliderjoint3d-property-angular-motion-damping). The amount of damping of the rotation in the limits.

<a id="class-sliderjoint3d-constant-param-angular-orthogonal-softness"></a>

[Param](class_sliderjoint3d.md#enum-sliderjoint3d-param) **PARAM_ANGULAR_ORTHOGONAL_SOFTNESS** = `19`

Constant for accessing [angular_ortho/softness](class_sliderjoint3d.md#class-sliderjoint3d-property-angular-ortho-softness). A factor applied to the all rotation across axes orthogonal to the slider.

<a id="class-sliderjoint3d-constant-param-angular-orthogonal-restitution"></a>

[Param](class_sliderjoint3d.md#enum-sliderjoint3d-param) **PARAM_ANGULAR_ORTHOGONAL_RESTITUTION** = `20`

Constant for accessing [angular_ortho/restitution](class_sliderjoint3d.md#class-sliderjoint3d-property-angular-ortho-restitution). The amount of restitution of the rotation across axes orthogonal to the slider.

<a id="class-sliderjoint3d-constant-param-angular-orthogonal-damping"></a>

[Param](class_sliderjoint3d.md#enum-sliderjoint3d-param) **PARAM_ANGULAR_ORTHOGONAL_DAMPING** = `21`

Constant for accessing [angular_ortho/damping](class_sliderjoint3d.md#class-sliderjoint3d-property-angular-ortho-damping). The amount of damping of the rotation across axes orthogonal to the slider.

<a id="class-sliderjoint3d-constant-param-max"></a>

[Param](class_sliderjoint3d.md#enum-sliderjoint3d-param) **PARAM_MAX** = `22`

Represents the size of the [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-sliderjoint3d-property-angular-limit-damping"></a>

[float](class_float.md#class-float) **angular_limit/damping** = `0.0` [🔗](class_sliderjoint3d.md#class-sliderjoint3d-property-angular-limit-damping)

- void **set_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param)) const

The amount of damping of the rotation when the limit is surpassed.

A lower damping value allows a rotation initiated by body A to travel to body B slower.

---


<a id="class-sliderjoint3d-property-angular-limit-lower-angle"></a>

[float](class_float.md#class-float) **angular_limit/lower_angle** = `0.0` [🔗](class_sliderjoint3d.md#class-sliderjoint3d-property-angular-limit-lower-angle)

- void **set_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param)) const

The lower limit of rotation in the slider.

---


<a id="class-sliderjoint3d-property-angular-limit-restitution"></a>

[float](class_float.md#class-float) **angular_limit/restitution** = `0.7` [🔗](class_sliderjoint3d.md#class-sliderjoint3d-property-angular-limit-restitution)

- void **set_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param)) const

The amount of restitution of the rotation when the limit is surpassed.

Does not affect damping.

---


<a id="class-sliderjoint3d-property-angular-limit-softness"></a>

[float](class_float.md#class-float) **angular_limit/softness** = `1.0` [🔗](class_sliderjoint3d.md#class-sliderjoint3d-property-angular-limit-softness)

- void **set_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param)) const

A factor applied to the all rotation once the limit is surpassed.

Makes all rotation slower when between 0 and 1.

---


<a id="class-sliderjoint3d-property-angular-limit-upper-angle"></a>

[float](class_float.md#class-float) **angular_limit/upper_angle** = `0.0` [🔗](class_sliderjoint3d.md#class-sliderjoint3d-property-angular-limit-upper-angle)

- void **set_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param)) const

The upper limit of rotation in the slider.

---


<a id="class-sliderjoint3d-property-angular-motion-damping"></a>

[float](class_float.md#class-float) **angular_motion/damping** = `1.0` [🔗](class_sliderjoint3d.md#class-sliderjoint3d-property-angular-motion-damping)

- void **set_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param)) const

The amount of damping of the rotation in the limits.

---


<a id="class-sliderjoint3d-property-angular-motion-restitution"></a>

[float](class_float.md#class-float) **angular_motion/restitution** = `0.7` [🔗](class_sliderjoint3d.md#class-sliderjoint3d-property-angular-motion-restitution)

- void **set_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param)) const

The amount of restitution of the rotation in the limits.

---


<a id="class-sliderjoint3d-property-angular-motion-softness"></a>

[float](class_float.md#class-float) **angular_motion/softness** = `1.0` [🔗](class_sliderjoint3d.md#class-sliderjoint3d-property-angular-motion-softness)

- void **set_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param)) const

A factor applied to the all rotation in the limits.

---


<a id="class-sliderjoint3d-property-angular-ortho-damping"></a>

[float](class_float.md#class-float) **angular_ortho/damping** = `1.0` [🔗](class_sliderjoint3d.md#class-sliderjoint3d-property-angular-ortho-damping)

- void **set_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param)) const

The amount of damping of the rotation across axes orthogonal to the slider.

---


<a id="class-sliderjoint3d-property-angular-ortho-restitution"></a>

[float](class_float.md#class-float) **angular_ortho/restitution** = `0.7` [🔗](class_sliderjoint3d.md#class-sliderjoint3d-property-angular-ortho-restitution)

- void **set_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param)) const

The amount of restitution of the rotation across axes orthogonal to the slider.

---


<a id="class-sliderjoint3d-property-angular-ortho-softness"></a>

[float](class_float.md#class-float) **angular_ortho/softness** = `1.0` [🔗](class_sliderjoint3d.md#class-sliderjoint3d-property-angular-ortho-softness)

- void **set_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param)) const

A factor applied to the all rotation across axes orthogonal to the slider.

---


<a id="class-sliderjoint3d-property-linear-limit-damping"></a>

[float](class_float.md#class-float) **linear_limit/damping** = `1.0` [🔗](class_sliderjoint3d.md#class-sliderjoint3d-property-linear-limit-damping)

- void **set_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param)) const

The amount of damping that happens once the limit defined by [linear_limit/lower_distance](class_sliderjoint3d.md#class-sliderjoint3d-property-linear-limit-lower-distance) and [linear_limit/upper_distance](class_sliderjoint3d.md#class-sliderjoint3d-property-linear-limit-upper-distance) is surpassed.

---


<a id="class-sliderjoint3d-property-linear-limit-lower-distance"></a>

[float](class_float.md#class-float) **linear_limit/lower_distance** = `-1.0` [🔗](class_sliderjoint3d.md#class-sliderjoint3d-property-linear-limit-lower-distance)

- void **set_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param)) const

The minimum difference between the pivot points on their X axis before damping happens.

---


<a id="class-sliderjoint3d-property-linear-limit-restitution"></a>

[float](class_float.md#class-float) **linear_limit/restitution** = `0.7` [🔗](class_sliderjoint3d.md#class-sliderjoint3d-property-linear-limit-restitution)

- void **set_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param)) const

The amount of restitution once the limits are surpassed. The lower, the more velocity-energy gets lost.

---


<a id="class-sliderjoint3d-property-linear-limit-softness"></a>

[float](class_float.md#class-float) **linear_limit/softness** = `1.0` [🔗](class_sliderjoint3d.md#class-sliderjoint3d-property-linear-limit-softness)

- void **set_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param)) const

A factor applied to the movement across the slider axis once the limits get surpassed. The lower, the slower the movement.

---


<a id="class-sliderjoint3d-property-linear-limit-upper-distance"></a>

[float](class_float.md#class-float) **linear_limit/upper_distance** = `1.0` [🔗](class_sliderjoint3d.md#class-sliderjoint3d-property-linear-limit-upper-distance)

- void **set_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param)) const

The maximum difference between the pivot points on their X axis before damping happens.

---


<a id="class-sliderjoint3d-property-linear-motion-damping"></a>

[float](class_float.md#class-float) **linear_motion/damping** = `0.0` [🔗](class_sliderjoint3d.md#class-sliderjoint3d-property-linear-motion-damping)

- void **set_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param)) const

The amount of damping inside the slider limits.

---


<a id="class-sliderjoint3d-property-linear-motion-restitution"></a>

[float](class_float.md#class-float) **linear_motion/restitution** = `0.7` [🔗](class_sliderjoint3d.md#class-sliderjoint3d-property-linear-motion-restitution)

- void **set_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param)) const

The amount of restitution inside the slider limits.

---


<a id="class-sliderjoint3d-property-linear-motion-softness"></a>

[float](class_float.md#class-float) **linear_motion/softness** = `1.0` [🔗](class_sliderjoint3d.md#class-sliderjoint3d-property-linear-motion-softness)

- void **set_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param)) const

A factor applied to the movement across the slider axis as long as the slider is in the limits. The lower, the slower the movement.

---


<a id="class-sliderjoint3d-property-linear-ortho-damping"></a>

[float](class_float.md#class-float) **linear_ortho/damping** = `1.0` [🔗](class_sliderjoint3d.md#class-sliderjoint3d-property-linear-ortho-damping)

- void **set_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param)) const

The amount of damping when movement is across axes orthogonal to the slider.

---


<a id="class-sliderjoint3d-property-linear-ortho-restitution"></a>

[float](class_float.md#class-float) **linear_ortho/restitution** = `0.7` [🔗](class_sliderjoint3d.md#class-sliderjoint3d-property-linear-ortho-restitution)

- void **set_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param)) const

The amount of restitution when movement is across axes orthogonal to the slider.

---


<a id="class-sliderjoint3d-property-linear-ortho-softness"></a>

[float](class_float.md#class-float) **linear_ortho/softness** = `1.0` [🔗](class_sliderjoint3d.md#class-sliderjoint3d-property-linear-ortho-softness)

- void **set_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param)) const

A factor applied to the movement across axes orthogonal to the slider.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-sliderjoint3d-method-get-param"></a>

[float](class_float.md#class-float) **get_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param)) const [🔗](class_sliderjoint3d.md#class-sliderjoint3d-method-get-param)

Returns the value of the given parameter.

---


<a id="class-sliderjoint3d-method-set-param"></a>

void **set_param**(param: [Param](class_sliderjoint3d.md#enum-sliderjoint3d-param), value: [float](class_float.md#class-float)) [🔗](class_sliderjoint3d.md#class-sliderjoint3d-method-set-param)

Assigns `value` to the given parameter.
