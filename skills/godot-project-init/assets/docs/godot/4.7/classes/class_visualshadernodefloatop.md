> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodefloatop.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodefloatop"></a>

<a id="class-visualshadernodefloatop"></a>

# VisualShaderNodeFloatOp

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A floating-point scalar operator to be used within the visual shader graph.

<a id="description"></a>

## Description

Applies [operator](class_visualshadernodefloatop.md#class-visualshadernodefloatop-property-operator) to two floating-point inputs: `a` and `b`.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Operator](class_visualshadernodefloatop.md#enum-visualshadernodefloatop-operator) | [operator](class_visualshadernodefloatop.md#class-visualshadernodefloatop-property-operator) | `0` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-visualshadernodefloatop-operator"></a>

enum **Operator**: [🔗](class_visualshadernodefloatop.md#enum-visualshadernodefloatop-operator)

<a id="class-visualshadernodefloatop-constant-op-add"></a>

[Operator](class_visualshadernodefloatop.md#enum-visualshadernodefloatop-operator) **OP_ADD** = `0`

Sums two numbers using `a + b`.

<a id="class-visualshadernodefloatop-constant-op-sub"></a>

[Operator](class_visualshadernodefloatop.md#enum-visualshadernodefloatop-operator) **OP_SUB** = `1`

Subtracts two numbers using `a - b`.

<a id="class-visualshadernodefloatop-constant-op-mul"></a>

[Operator](class_visualshadernodefloatop.md#enum-visualshadernodefloatop-operator) **OP_MUL** = `2`

Multiplies two numbers using `a * b`.

<a id="class-visualshadernodefloatop-constant-op-div"></a>

[Operator](class_visualshadernodefloatop.md#enum-visualshadernodefloatop-operator) **OP_DIV** = `3`

Divides two numbers using `a / b`.

<a id="class-visualshadernodefloatop-constant-op-mod"></a>

[Operator](class_visualshadernodefloatop.md#enum-visualshadernodefloatop-operator) **OP_MOD** = `4`

Calculates the remainder of two numbers. Translates to `mod(a, b)` in the Godot Shader Language.

<a id="class-visualshadernodefloatop-constant-op-pow"></a>

[Operator](class_visualshadernodefloatop.md#enum-visualshadernodefloatop-operator) **OP_POW** = `5`

Raises the `a` to the power of `b`. Translates to `pow(a, b)` in the Godot Shader Language.

<a id="class-visualshadernodefloatop-constant-op-max"></a>

[Operator](class_visualshadernodefloatop.md#enum-visualshadernodefloatop-operator) **OP_MAX** = `6`

Returns the greater of two numbers. Translates to `max(a, b)` in the Godot Shader Language.

<a id="class-visualshadernodefloatop-constant-op-min"></a>

[Operator](class_visualshadernodefloatop.md#enum-visualshadernodefloatop-operator) **OP_MIN** = `7`

Returns the lesser of two numbers. Translates to `min(a, b)` in the Godot Shader Language.

<a id="class-visualshadernodefloatop-constant-op-atan2"></a>

[Operator](class_visualshadernodefloatop.md#enum-visualshadernodefloatop-operator) **OP_ATAN2** = `8`

Returns the arc-tangent of the parameters. Translates to `atan(a, b)` in the Godot Shader Language.

<a id="class-visualshadernodefloatop-constant-op-step"></a>

[Operator](class_visualshadernodefloatop.md#enum-visualshadernodefloatop-operator) **OP_STEP** = `9`

Generates a step function by comparing `b`(x) to `a`(edge). Returns 0.0 if `x` is smaller than `edge` and otherwise 1.0. Translates to `step(a, b)` in the Godot Shader Language.

<a id="class-visualshadernodefloatop-constant-op-enum-size"></a>

[Operator](class_visualshadernodefloatop.md#enum-visualshadernodefloatop-operator) **OP_ENUM_SIZE** = `10`

Represents the size of the [Operator](class_visualshadernodefloatop.md#enum-visualshadernodefloatop-operator) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodefloatop-property-operator"></a>

[Operator](class_visualshadernodefloatop.md#enum-visualshadernodefloatop-operator) **operator** = `0` [🔗](class_visualshadernodefloatop.md#class-visualshadernodefloatop-property-operator)

- void **set_operator**(value: [Operator](class_visualshadernodefloatop.md#enum-visualshadernodefloatop-operator))
- [Operator](class_visualshadernodefloatop.md#enum-visualshadernodefloatop-operator) **get_operator**()

An operator to be applied to the inputs.
