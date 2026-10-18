> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodemultiplyadd.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodemultiplyadd"></a>

<a id="class-visualshadernodemultiplyadd"></a>

# VisualShaderNodeMultiplyAdd

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Performs a fused multiply-add operation within the visual shader graph.

<a id="description"></a>

## Description

Uses three operands to compute `(a * b + c)` expression.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [OpType](class_visualshadernodemultiplyadd.md#enum-visualshadernodemultiplyadd-optype) | [op_type](class_visualshadernodemultiplyadd.md#class-visualshadernodemultiplyadd-property-op-type) | `0` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-visualshadernodemultiplyadd-optype"></a>

enum **OpType**: [🔗](class_visualshadernodemultiplyadd.md#enum-visualshadernodemultiplyadd-optype)

<a id="class-visualshadernodemultiplyadd-constant-op-type-scalar"></a>

[OpType](class_visualshadernodemultiplyadd.md#enum-visualshadernodemultiplyadd-optype) **OP_TYPE_SCALAR** = `0`

A floating-point scalar type.

<a id="class-visualshadernodemultiplyadd-constant-op-type-vector-2d"></a>

[OpType](class_visualshadernodemultiplyadd.md#enum-visualshadernodemultiplyadd-optype) **OP_TYPE_VECTOR_2D** = `1`

A 2D vector type.

<a id="class-visualshadernodemultiplyadd-constant-op-type-vector-3d"></a>

[OpType](class_visualshadernodemultiplyadd.md#enum-visualshadernodemultiplyadd-optype) **OP_TYPE_VECTOR_3D** = `2`

A 3D vector type.

<a id="class-visualshadernodemultiplyadd-constant-op-type-vector-4d"></a>

[OpType](class_visualshadernodemultiplyadd.md#enum-visualshadernodemultiplyadd-optype) **OP_TYPE_VECTOR_4D** = `3`

A 4D vector type.

<a id="class-visualshadernodemultiplyadd-constant-op-type-max"></a>

[OpType](class_visualshadernodemultiplyadd.md#enum-visualshadernodemultiplyadd-optype) **OP_TYPE_MAX** = `4`

Represents the size of the [OpType](class_visualshadernodemultiplyadd.md#enum-visualshadernodemultiplyadd-optype) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodemultiplyadd-property-op-type"></a>

[OpType](class_visualshadernodemultiplyadd.md#enum-visualshadernodemultiplyadd-optype) **op_type** = `0` [🔗](class_visualshadernodemultiplyadd.md#class-visualshadernodemultiplyadd-property-op-type)

- void **set_op_type**(value: [OpType](class_visualshadernodemultiplyadd.md#enum-visualshadernodemultiplyadd-optype))
- [OpType](class_visualshadernodemultiplyadd.md#enum-visualshadernodemultiplyadd-optype) **get_op_type**()

A type of operands and returned value.
