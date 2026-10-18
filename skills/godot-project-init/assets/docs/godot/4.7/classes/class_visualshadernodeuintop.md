> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodeuintop.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodeuintop"></a>

<a id="class-visualshadernodeuintop"></a>

# VisualShaderNodeUIntOp

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

An unsigned integer scalar operator to be used within the visual shader graph.

<a id="description"></a>

## Description

Applies [operator](class_visualshadernodeuintop.md#class-visualshadernodeuintop-property-operator) to two unsigned integer inputs: `a` and `b`.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Operator](class_visualshadernodeuintop.md#enum-visualshadernodeuintop-operator) | [operator](class_visualshadernodeuintop.md#class-visualshadernodeuintop-property-operator) | `0` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-visualshadernodeuintop-operator"></a>

enum **Operator**: [🔗](class_visualshadernodeuintop.md#enum-visualshadernodeuintop-operator)

<a id="class-visualshadernodeuintop-constant-op-add"></a>

[Operator](class_visualshadernodeuintop.md#enum-visualshadernodeuintop-operator) **OP_ADD** = `0`

Sums two numbers using `a + b`.

<a id="class-visualshadernodeuintop-constant-op-sub"></a>

[Operator](class_visualshadernodeuintop.md#enum-visualshadernodeuintop-operator) **OP_SUB** = `1`

Subtracts two numbers using `a - b`.

<a id="class-visualshadernodeuintop-constant-op-mul"></a>

[Operator](class_visualshadernodeuintop.md#enum-visualshadernodeuintop-operator) **OP_MUL** = `2`

Multiplies two numbers using `a * b`.

<a id="class-visualshadernodeuintop-constant-op-div"></a>

[Operator](class_visualshadernodeuintop.md#enum-visualshadernodeuintop-operator) **OP_DIV** = `3`

Divides two numbers using `a / b`.

<a id="class-visualshadernodeuintop-constant-op-mod"></a>

[Operator](class_visualshadernodeuintop.md#enum-visualshadernodeuintop-operator) **OP_MOD** = `4`

Calculates the remainder of two numbers using `a % b`.

<a id="class-visualshadernodeuintop-constant-op-max"></a>

[Operator](class_visualshadernodeuintop.md#enum-visualshadernodeuintop-operator) **OP_MAX** = `5`

Returns the greater of two numbers. Translates to `max(a, b)` in the Godot Shader Language.

<a id="class-visualshadernodeuintop-constant-op-min"></a>

[Operator](class_visualshadernodeuintop.md#enum-visualshadernodeuintop-operator) **OP_MIN** = `6`

Returns the lesser of two numbers. Translates to `max(a, b)` in the Godot Shader Language.

<a id="class-visualshadernodeuintop-constant-op-bitwise-and"></a>

[Operator](class_visualshadernodeuintop.md#enum-visualshadernodeuintop-operator) **OP_BITWISE_AND** = `7`

Returns the result of bitwise `AND` operation on the integer. Translates to `a & b` in the Godot Shader Language.

<a id="class-visualshadernodeuintop-constant-op-bitwise-or"></a>

[Operator](class_visualshadernodeuintop.md#enum-visualshadernodeuintop-operator) **OP_BITWISE_OR** = `8`

Returns the result of bitwise `OR` operation for two integers. Translates to `a | b` in the Godot Shader Language.

<a id="class-visualshadernodeuintop-constant-op-bitwise-xor"></a>

[Operator](class_visualshadernodeuintop.md#enum-visualshadernodeuintop-operator) **OP_BITWISE_XOR** = `9`

Returns the result of bitwise `XOR` operation for two integers. Translates to `a ^ b` in the Godot Shader Language.

<a id="class-visualshadernodeuintop-constant-op-bitwise-left-shift"></a>

[Operator](class_visualshadernodeuintop.md#enum-visualshadernodeuintop-operator) **OP_BITWISE_LEFT_SHIFT** = `10`

Returns the result of bitwise left shift operation on the integer. Translates to `a << b` in the Godot Shader Language.

<a id="class-visualshadernodeuintop-constant-op-bitwise-right-shift"></a>

[Operator](class_visualshadernodeuintop.md#enum-visualshadernodeuintop-operator) **OP_BITWISE_RIGHT_SHIFT** = `11`

Returns the result of bitwise right shift operation on the integer. Translates to `a >> b` in the Godot Shader Language.

<a id="class-visualshadernodeuintop-constant-op-enum-size"></a>

[Operator](class_visualshadernodeuintop.md#enum-visualshadernodeuintop-operator) **OP_ENUM_SIZE** = `12`

Represents the size of the [Operator](class_visualshadernodeuintop.md#enum-visualshadernodeuintop-operator) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodeuintop-property-operator"></a>

[Operator](class_visualshadernodeuintop.md#enum-visualshadernodeuintop-operator) **operator** = `0` [🔗](class_visualshadernodeuintop.md#class-visualshadernodeuintop-property-operator)

- void **set_operator**(value: [Operator](class_visualshadernodeuintop.md#enum-visualshadernodeuintop-operator))
- [Operator](class_visualshadernodeuintop.md#enum-visualshadernodeuintop-operator) **get_operator**()

An operator to be applied to the inputs.
