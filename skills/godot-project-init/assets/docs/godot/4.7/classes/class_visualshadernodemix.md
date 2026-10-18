> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodemix.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodemix"></a>

<a id="class-visualshadernodemix"></a>

# VisualShaderNodeMix

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Linearly interpolates between two values within the visual shader graph.

<a id="description"></a>

## Description

Translates to `mix(a, b, weight)` in the shader language.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [OpType](class_visualshadernodemix.md#enum-visualshadernodemix-optype) | [op_type](class_visualshadernodemix.md#class-visualshadernodemix-property-op-type) | `0` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-visualshadernodemix-optype"></a>

enum **OpType**: [🔗](class_visualshadernodemix.md#enum-visualshadernodemix-optype)

<a id="class-visualshadernodemix-constant-op-type-scalar"></a>

[OpType](class_visualshadernodemix.md#enum-visualshadernodemix-optype) **OP_TYPE_SCALAR** = `0`

A floating-point scalar.

<a id="class-visualshadernodemix-constant-op-type-vector-2d"></a>

[OpType](class_visualshadernodemix.md#enum-visualshadernodemix-optype) **OP_TYPE_VECTOR_2D** = `1`

A 2D vector type.

<a id="class-visualshadernodemix-constant-op-type-vector-2d-scalar"></a>

[OpType](class_visualshadernodemix.md#enum-visualshadernodemix-optype) **OP_TYPE_VECTOR_2D_SCALAR** = `2`

The `a` and `b` ports use a 2D vector type. The `weight` port uses a scalar type.

<a id="class-visualshadernodemix-constant-op-type-vector-3d"></a>

[OpType](class_visualshadernodemix.md#enum-visualshadernodemix-optype) **OP_TYPE_VECTOR_3D** = `3`

A 3D vector type.

<a id="class-visualshadernodemix-constant-op-type-vector-3d-scalar"></a>

[OpType](class_visualshadernodemix.md#enum-visualshadernodemix-optype) **OP_TYPE_VECTOR_3D_SCALAR** = `4`

The `a` and `b` ports use a 3D vector type. The `weight` port uses a scalar type.

<a id="class-visualshadernodemix-constant-op-type-vector-4d"></a>

[OpType](class_visualshadernodemix.md#enum-visualshadernodemix-optype) **OP_TYPE_VECTOR_4D** = `5`

A 4D vector type.

<a id="class-visualshadernodemix-constant-op-type-vector-4d-scalar"></a>

[OpType](class_visualshadernodemix.md#enum-visualshadernodemix-optype) **OP_TYPE_VECTOR_4D_SCALAR** = `6`

The `a` and `b` ports use a 4D vector type. The `weight` port uses a scalar type.

<a id="class-visualshadernodemix-constant-op-type-max"></a>

[OpType](class_visualshadernodemix.md#enum-visualshadernodemix-optype) **OP_TYPE_MAX** = `7`

Represents the size of the [OpType](class_visualshadernodemix.md#enum-visualshadernodemix-optype) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodemix-property-op-type"></a>

[OpType](class_visualshadernodemix.md#enum-visualshadernodemix-optype) **op_type** = `0` [🔗](class_visualshadernodemix.md#class-visualshadernodemix-property-op-type)

- void **set_op_type**(value: [OpType](class_visualshadernodemix.md#enum-visualshadernodemix-optype))
- [OpType](class_visualshadernodemix.md#enum-visualshadernodemix-optype) **get_op_type**()

A type of operands and returned value.
