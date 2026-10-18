> Source: https://docs.godotengine.org/en/4.7/classes/class_pinjoint3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="pinjoint3d"></a>

<a id="class-pinjoint3d"></a>

# PinJoint3D

**Inherits:** [Joint3D](class_joint3d.md#class-joint3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A physics joint that attaches two 3D physics bodies at a single point, allowing them to freely rotate.

<a id="description"></a>

## Description

A physics joint that attaches two 3D physics bodies at a single point, allowing them to freely rotate. For example, a [RigidBody3D](class_rigidbody3d.md#class-rigidbody3d) can be attached to a [StaticBody3D](class_staticbody3d.md#class-staticbody3d) to create a pendulum or a seesaw.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [params/bias](class_pinjoint3d.md#class-pinjoint3d-property-params-bias) | `0.3` |
| [float](class_float.md#class-float) | [params/damping](class_pinjoint3d.md#class-pinjoint3d-property-params-damping) | `1.0` |
| [float](class_float.md#class-float) | [params/impulse_clamp](class_pinjoint3d.md#class-pinjoint3d-property-params-impulse-clamp) | `0.0` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [float](class_float.md#class-float) | [get_param](class_pinjoint3d.md#class-pinjoint3d-method-get-param)(param: [Param](class_pinjoint3d.md#enum-pinjoint3d-param)) const |
| void | [set_param](class_pinjoint3d.md#class-pinjoint3d-method-set-param)(param: [Param](class_pinjoint3d.md#enum-pinjoint3d-param), value: [float](class_float.md#class-float)) |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-pinjoint3d-param"></a>

enum **Param**: [🔗](class_pinjoint3d.md#enum-pinjoint3d-param)

<a id="class-pinjoint3d-constant-param-bias"></a>

[Param](class_pinjoint3d.md#enum-pinjoint3d-param) **PARAM_BIAS** = `0`

The force with which the pinned objects stay in positional relation to each other. The higher, the stronger.

<a id="class-pinjoint3d-constant-param-damping"></a>

[Param](class_pinjoint3d.md#enum-pinjoint3d-param) **PARAM_DAMPING** = `1`

The force with which the pinned objects stay in velocity relation to each other. The higher, the stronger.

<a id="class-pinjoint3d-constant-param-impulse-clamp"></a>

[Param](class_pinjoint3d.md#enum-pinjoint3d-param) **PARAM_IMPULSE_CLAMP** = `2`

If above 0, this value is the maximum value for an impulse that this Joint3D produces.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-pinjoint3d-property-params-bias"></a>

[float](class_float.md#class-float) **params/bias** = `0.3` [🔗](class_pinjoint3d.md#class-pinjoint3d-property-params-bias)

- void **set_param**(param: [Param](class_pinjoint3d.md#enum-pinjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: [Param](class_pinjoint3d.md#enum-pinjoint3d-param)) const

The force with which the pinned objects stay in positional relation to each other. The higher, the stronger.

---


<a id="class-pinjoint3d-property-params-damping"></a>

[float](class_float.md#class-float) **params/damping** = `1.0` [🔗](class_pinjoint3d.md#class-pinjoint3d-property-params-damping)

- void **set_param**(param: [Param](class_pinjoint3d.md#enum-pinjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: [Param](class_pinjoint3d.md#enum-pinjoint3d-param)) const

The force with which the pinned objects stay in velocity relation to each other. The higher, the stronger.

---


<a id="class-pinjoint3d-property-params-impulse-clamp"></a>

[float](class_float.md#class-float) **params/impulse_clamp** = `0.0` [🔗](class_pinjoint3d.md#class-pinjoint3d-property-params-impulse-clamp)

- void **set_param**(param: [Param](class_pinjoint3d.md#enum-pinjoint3d-param), value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: [Param](class_pinjoint3d.md#enum-pinjoint3d-param)) const

If above 0, this value is the maximum value for an impulse that this Joint3D produces.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-pinjoint3d-method-get-param"></a>

[float](class_float.md#class-float) **get_param**(param: [Param](class_pinjoint3d.md#enum-pinjoint3d-param)) const [🔗](class_pinjoint3d.md#class-pinjoint3d-method-get-param)

Returns the value of the specified parameter.

---


<a id="class-pinjoint3d-method-set-param"></a>

void **set_param**(param: [Param](class_pinjoint3d.md#enum-pinjoint3d-param), value: [float](class_float.md#class-float)) [🔗](class_pinjoint3d.md#class-pinjoint3d-method-set-param)

Sets the value of the specified parameter.
