> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodeintop.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodeintop"></a>

<a id="class-visualshadernodeintop"></a>

# VisualShaderNodeIntOp

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

An integer scalar operator to be used within the visual shader graph.

<a id="description"></a>

## Description

Applies [operator](class_visualshadernodeintop.md#class-visualshadernodeintop-property-operator) to two integer inputs: `a` and `b`.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Operator](class_visualshadernodeintop.md#enum-visualshadernodeintop-operator) | [operator](class_visualshadernodeintop.md#class-visualshadernodeintop-property-operator) | `0` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-visualshadernodeintop-operator"></a>

enum **Operator**: [🔗](class_visualshadernodeintop.md#enum-visualshadernodeintop-operator)

<a id="class-visualshadernodeintop-constant-op-add"></a>

[Operator](class_visualshadernodeintop.md#enum-visualshadernodeintop-operator) **OP_ADD** = `0`

Sums two numbers using `a + b`.

<a id="class-visualshadernodeintop-constant-op-sub"></a>

[Operator](class_visualshadernodeintop.md#enum-visualshadernodeintop-operator) **OP_SUB** = `1`

Subtracts two numbers using `a - b`.

<a id="class-visualshadernodeintop-constant-op-mul"></a>

[Operator](class_visualshadernodeintop.md#enum-visualshadernodeintop-operator) **OP_MUL** = `2`

Multiplies two numbers using `a * b`.

<a id="class-visualshadernodeintop-constant-op-div"></a>

[Operator](class_visualshadernodeintop.md#enum-visualshadernodeintop-operator) **OP_DIV** = `3`

Divides two numbers using `a / b`.

<a id="class-visualshadernodeintop-constant-op-mod"></a>

[Operator](class_visualshadernodeintop.md#enum-visualshadernodeintop-operator) **OP_MOD** = `4`

Calculates the remainder of two numbers using `a % b`.

<a id="class-visualshadernodeintop-constant-op-max"></a>

[Operator](class_visualshadernodeintop.md#enum-visualshadernodeintop-operator) **OP_MAX** = `5`

Returns the greater of two numbers. Translates to `max(a, b)` in the Godot Shader Language.

<a id="class-visualshadernodeintop-constant-op-min"></a>

[Operator](class_visualshadernodeintop.md#enum-visualshadernodeintop-operator) **OP_MIN** = `6`

Returns the lesser of two numbers. Translates to `max(a, b)` in the Godot Shader Language.

<a id="class-visualshadernodeintop-constant-op-bitwise-and"></a>

[Operator](class_visualshadernodeintop.md#enum-visualshadernodeintop-operator) **OP_BITWISE_AND** = `7`

Returns the result of bitwise `AND` operation on the integer. Translates to `a & b` in the Godot Shader Language.

<a id="class-visualshadernodeintop-constant-op-bitwise-or"></a>

[Operator](class_visualshadernodeintop.md#enum-visualshadernodeintop-operator) **OP_BITWISE_OR** = `8`

Returns the result of bitwise `OR` operation for two integers. Translates to `a | b` in the Godot Shader Language.

<a id="class-visualshadernodeintop-constant-op-bitwise-xor"></a>

[Operator](class_visualshadernodeintop.md#enum-visualshadernodeintop-operator) **OP_BITWISE_XOR** = `9`

Returns the result of bitwise `XOR` operation for two integers. Translates to `a ^ b` in the Godot Shader Language.

<a id="class-visualshadernodeintop-constant-op-bitwise-left-shift"></a>

[Operator](class_visualshadernodeintop.md#enum-visualshadernodeintop-operator) **OP_BITWISE_LEFT_SHIFT** = `10`

Returns the result of bitwise left shift operation on the integer. Translates to `a << b` in the Godot Shader Language.

<a id="class-visualshadernodeintop-constant-op-bitwise-right-shift"></a>

[Operator](class_visualshadernodeintop.md#enum-visualshadernodeintop-operator) **OP_BITWISE_RIGHT_SHIFT** = `11`

Returns the result of bitwise right shift operation on the integer. Translates to `a >> b` in the Godot Shader Language.

<a id="class-visualshadernodeintop-constant-op-enum-size"></a>

[Operator](class_visualshadernodeintop.md#enum-visualshadernodeintop-operator) **OP_ENUM_SIZE** = `12`

Represents the size of the [Operator](class_visualshadernodeintop.md#enum-visualshadernodeintop-operator) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodeintop-property-operator"></a>

[Operator](class_visualshadernodeintop.md#enum-visualshadernodeintop-operator) **operator** = `0` [🔗](class_visualshadernodeintop.md#class-visualshadernodeintop-property-operator)

- void **set_operator**(value: [Operator](class_visualshadernodeintop.md#enum-visualshadernodeintop-operator))
- [Operator](class_visualshadernodeintop.md#enum-visualshadernodeintop-operator) **get_operator**()

An operator to be applied to the inputs.
