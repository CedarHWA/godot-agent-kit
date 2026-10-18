> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodesmoothstep.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodesmoothstep"></a>

<a id="class-visualshadernodesmoothstep"></a>

# VisualShaderNodeSmoothStep

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Calculates a SmoothStep function within the visual shader graph.

<a id="description"></a>

## Description

Translates to `smoothstep(edge0, edge1, x)` in the shader language.

Returns `0.0` if `x` is smaller than `edge0` and `1.0` if `x` is larger than `edge1`. Otherwise, the return value is interpolated between `0.0` and `1.0` using Hermite polynomials.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [OpType](class_visualshadernodesmoothstep.md#enum-visualshadernodesmoothstep-optype) | [op_type](class_visualshadernodesmoothstep.md#class-visualshadernodesmoothstep-property-op-type) | `0` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-visualshadernodesmoothstep-optype"></a>

enum **OpType**: [🔗](class_visualshadernodesmoothstep.md#enum-visualshadernodesmoothstep-optype)

<a id="class-visualshadernodesmoothstep-constant-op-type-scalar"></a>

[OpType](class_visualshadernodesmoothstep.md#enum-visualshadernodesmoothstep-optype) **OP_TYPE_SCALAR** = `0`

A floating-point scalar type.

<a id="class-visualshadernodesmoothstep-constant-op-type-vector-2d"></a>

[OpType](class_visualshadernodesmoothstep.md#enum-visualshadernodesmoothstep-optype) **OP_TYPE_VECTOR_2D** = `1`

A 2D vector type.

<a id="class-visualshadernodesmoothstep-constant-op-type-vector-2d-scalar"></a>

[OpType](class_visualshadernodesmoothstep.md#enum-visualshadernodesmoothstep-optype) **OP_TYPE_VECTOR_2D_SCALAR** = `2`

The `x` port uses a 2D vector type. The first two ports use a floating-point scalar type.

<a id="class-visualshadernodesmoothstep-constant-op-type-vector-3d"></a>

[OpType](class_visualshadernodesmoothstep.md#enum-visualshadernodesmoothstep-optype) **OP_TYPE_VECTOR_3D** = `3`

A 3D vector type.

<a id="class-visualshadernodesmoothstep-constant-op-type-vector-3d-scalar"></a>

[OpType](class_visualshadernodesmoothstep.md#enum-visualshadernodesmoothstep-optype) **OP_TYPE_VECTOR_3D_SCALAR** = `4`

The `x` port uses a 3D vector type. The first two ports use a floating-point scalar type.

<a id="class-visualshadernodesmoothstep-constant-op-type-vector-4d"></a>

[OpType](class_visualshadernodesmoothstep.md#enum-visualshadernodesmoothstep-optype) **OP_TYPE_VECTOR_4D** = `5`

A 4D vector type.

<a id="class-visualshadernodesmoothstep-constant-op-type-vector-4d-scalar"></a>

[OpType](class_visualshadernodesmoothstep.md#enum-visualshadernodesmoothstep-optype) **OP_TYPE_VECTOR_4D_SCALAR** = `6`

The `a` and `b` ports use a 4D vector type. The `weight` port uses a scalar type.

<a id="class-visualshadernodesmoothstep-constant-op-type-max"></a>

[OpType](class_visualshadernodesmoothstep.md#enum-visualshadernodesmoothstep-optype) **OP_TYPE_MAX** = `7`

Represents the size of the [OpType](class_visualshadernodesmoothstep.md#enum-visualshadernodesmoothstep-optype) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodesmoothstep-property-op-type"></a>

[OpType](class_visualshadernodesmoothstep.md#enum-visualshadernodesmoothstep-optype) **op_type** = `0` [🔗](class_visualshadernodesmoothstep.md#class-visualshadernodesmoothstep-property-op-type)

- void **set_op_type**(value: [OpType](class_visualshadernodesmoothstep.md#enum-visualshadernodesmoothstep-optype))
- [OpType](class_visualshadernodesmoothstep.md#enum-visualshadernodesmoothstep-optype) **get_op_type**()

A type of operands and returned value.
