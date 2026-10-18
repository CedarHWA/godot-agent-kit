> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodestep.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodestep"></a>

<a id="class-visualshadernodestep"></a>

# VisualShaderNodeStep

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Calculates a Step function within the visual shader graph.

<a id="description"></a>

## Description

Translates to `step(edge, x)` in the shader language.

Returns `0.0` if `x` is smaller than `edge` and `1.0` otherwise.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [OpType](class_visualshadernodestep.md#enum-visualshadernodestep-optype) | [op_type](class_visualshadernodestep.md#class-visualshadernodestep-property-op-type) | `0` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-visualshadernodestep-optype"></a>

enum **OpType**: [🔗](class_visualshadernodestep.md#enum-visualshadernodestep-optype)

<a id="class-visualshadernodestep-constant-op-type-scalar"></a>

[OpType](class_visualshadernodestep.md#enum-visualshadernodestep-optype) **OP_TYPE_SCALAR** = `0`

A floating-point scalar type.

<a id="class-visualshadernodestep-constant-op-type-vector-2d"></a>

[OpType](class_visualshadernodestep.md#enum-visualshadernodestep-optype) **OP_TYPE_VECTOR_2D** = `1`

A 2D vector type.

<a id="class-visualshadernodestep-constant-op-type-vector-2d-scalar"></a>

[OpType](class_visualshadernodestep.md#enum-visualshadernodestep-optype) **OP_TYPE_VECTOR_2D_SCALAR** = `2`

The `x` port uses a 2D vector type, while the `edge` port uses a floating-point scalar type.

<a id="class-visualshadernodestep-constant-op-type-vector-3d"></a>

[OpType](class_visualshadernodestep.md#enum-visualshadernodestep-optype) **OP_TYPE_VECTOR_3D** = `3`

A 3D vector type.

<a id="class-visualshadernodestep-constant-op-type-vector-3d-scalar"></a>

[OpType](class_visualshadernodestep.md#enum-visualshadernodestep-optype) **OP_TYPE_VECTOR_3D_SCALAR** = `4`

The `x` port uses a 3D vector type, while the `edge` port uses a floating-point scalar type.

<a id="class-visualshadernodestep-constant-op-type-vector-4d"></a>

[OpType](class_visualshadernodestep.md#enum-visualshadernodestep-optype) **OP_TYPE_VECTOR_4D** = `5`

A 4D vector type.

<a id="class-visualshadernodestep-constant-op-type-vector-4d-scalar"></a>

[OpType](class_visualshadernodestep.md#enum-visualshadernodestep-optype) **OP_TYPE_VECTOR_4D_SCALAR** = `6`

The `a` and `b` ports use a 4D vector type. The `weight` port uses a scalar type.

<a id="class-visualshadernodestep-constant-op-type-max"></a>

[OpType](class_visualshadernodestep.md#enum-visualshadernodestep-optype) **OP_TYPE_MAX** = `7`

Represents the size of the [OpType](class_visualshadernodestep.md#enum-visualshadernodestep-optype) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodestep-property-op-type"></a>

[OpType](class_visualshadernodestep.md#enum-visualshadernodestep-optype) **op_type** = `0` [🔗](class_visualshadernodestep.md#class-visualshadernodestep-property-op-type)

- void **set_op_type**(value: [OpType](class_visualshadernodestep.md#enum-visualshadernodestep-optype))
- [OpType](class_visualshadernodestep.md#enum-visualshadernodestep-optype) **get_op_type**()

A type of operands and returned value.
