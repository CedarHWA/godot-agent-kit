> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodevectorop.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodevectorop"></a>

<a id="class-visualshadernodevectorop"></a>

# VisualShaderNodeVectorOp

**Inherits:** [VisualShaderNodeVectorBase](class_visualshadernodevectorbase.md#class-visualshadernodevectorbase) **<** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A vector operator to be used within the visual shader graph.

<a id="description"></a>

## Description

A visual shader node for use of vector operators. Operates on vector `a` and vector `b`.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Operator](class_visualshadernodevectorop.md#enum-visualshadernodevectorop-operator) | [operator](class_visualshadernodevectorop.md#class-visualshadernodevectorop-property-operator) | `0` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-visualshadernodevectorop-operator"></a>

enum **Operator**: [🔗](class_visualshadernodevectorop.md#enum-visualshadernodevectorop-operator)

<a id="class-visualshadernodevectorop-constant-op-add"></a>

[Operator](class_visualshadernodevectorop.md#enum-visualshadernodevectorop-operator) **OP_ADD** = `0`

Adds two vectors.

<a id="class-visualshadernodevectorop-constant-op-sub"></a>

[Operator](class_visualshadernodevectorop.md#enum-visualshadernodevectorop-operator) **OP_SUB** = `1`

Subtracts a vector from a vector.

<a id="class-visualshadernodevectorop-constant-op-mul"></a>

[Operator](class_visualshadernodevectorop.md#enum-visualshadernodevectorop-operator) **OP_MUL** = `2`

Multiplies two vectors.

<a id="class-visualshadernodevectorop-constant-op-div"></a>

[Operator](class_visualshadernodevectorop.md#enum-visualshadernodevectorop-operator) **OP_DIV** = `3`

Divides vector by vector.

<a id="class-visualshadernodevectorop-constant-op-mod"></a>

[Operator](class_visualshadernodevectorop.md#enum-visualshadernodevectorop-operator) **OP_MOD** = `4`

Returns the remainder of the two vectors.

<a id="class-visualshadernodevectorop-constant-op-pow"></a>

[Operator](class_visualshadernodevectorop.md#enum-visualshadernodevectorop-operator) **OP_POW** = `5`

Returns the value of the first parameter raised to the power of the second, for each component of the vectors.

<a id="class-visualshadernodevectorop-constant-op-max"></a>

[Operator](class_visualshadernodevectorop.md#enum-visualshadernodevectorop-operator) **OP_MAX** = `6`

Returns the greater of two values, for each component of the vectors.

<a id="class-visualshadernodevectorop-constant-op-min"></a>

[Operator](class_visualshadernodevectorop.md#enum-visualshadernodevectorop-operator) **OP_MIN** = `7`

Returns the lesser of two values, for each component of the vectors.

<a id="class-visualshadernodevectorop-constant-op-cross"></a>

[Operator](class_visualshadernodevectorop.md#enum-visualshadernodevectorop-operator) **OP_CROSS** = `8`

Calculates the cross product of two vectors.

<a id="class-visualshadernodevectorop-constant-op-atan2"></a>

[Operator](class_visualshadernodevectorop.md#enum-visualshadernodevectorop-operator) **OP_ATAN2** = `9`

Returns the arc-tangent of the parameters.

<a id="class-visualshadernodevectorop-constant-op-reflect"></a>

[Operator](class_visualshadernodevectorop.md#enum-visualshadernodevectorop-operator) **OP_REFLECT** = `10`

Returns the vector that points in the direction of reflection. `a` is incident vector and `b` is the normal vector.

<a id="class-visualshadernodevectorop-constant-op-step"></a>

[Operator](class_visualshadernodevectorop.md#enum-visualshadernodevectorop-operator) **OP_STEP** = `11`

Vector step operator. Returns `0.0` if `a` is smaller than `b` and `1.0` otherwise.

<a id="class-visualshadernodevectorop-constant-op-enum-size"></a>

[Operator](class_visualshadernodevectorop.md#enum-visualshadernodevectorop-operator) **OP_ENUM_SIZE** = `12`

Represents the size of the [Operator](class_visualshadernodevectorop.md#enum-visualshadernodevectorop-operator) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodevectorop-property-operator"></a>

[Operator](class_visualshadernodevectorop.md#enum-visualshadernodevectorop-operator) **operator** = `0` [🔗](class_visualshadernodevectorop.md#class-visualshadernodevectorop-property-operator)

- void **set_operator**(value: [Operator](class_visualshadernodevectorop.md#enum-visualshadernodevectorop-operator))
- [Operator](class_visualshadernodevectorop.md#enum-visualshadernodevectorop-operator) **get_operator**()

The operator to be used.
