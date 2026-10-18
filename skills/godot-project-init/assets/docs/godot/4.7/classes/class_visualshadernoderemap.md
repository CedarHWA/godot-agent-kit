> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernoderemap.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernoderemap"></a>

<a id="class-visualshadernoderemap"></a>

# VisualShaderNodeRemap

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A visual shader node for remap function.

<a id="description"></a>

## Description

Remap will transform the input range into output range, e.g. you can change a `0..1` value to `-2..2` etc. See [@GlobalScope.remap()](class_@globalscope.md#class-globalscope-method-remap) for more details.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [OpType](class_visualshadernoderemap.md#enum-visualshadernoderemap-optype) | [op_type](class_visualshadernoderemap.md#class-visualshadernoderemap-property-op-type) | `0` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-visualshadernoderemap-optype"></a>

enum **OpType**: [🔗](class_visualshadernoderemap.md#enum-visualshadernoderemap-optype)

<a id="class-visualshadernoderemap-constant-op-type-scalar"></a>

[OpType](class_visualshadernoderemap.md#enum-visualshadernoderemap-optype) **OP_TYPE_SCALAR** = `0`

A floating-point scalar type.

<a id="class-visualshadernoderemap-constant-op-type-vector-2d"></a>

[OpType](class_visualshadernoderemap.md#enum-visualshadernoderemap-optype) **OP_TYPE_VECTOR_2D** = `1`

A 2D vector type.

<a id="class-visualshadernoderemap-constant-op-type-vector-2d-scalar"></a>

[OpType](class_visualshadernoderemap.md#enum-visualshadernoderemap-optype) **OP_TYPE_VECTOR_2D_SCALAR** = `2`

The `value` port uses a 2D vector type, while the `input min`, `input max`, `output min`, and `output max` ports use a floating-point scalar type.

<a id="class-visualshadernoderemap-constant-op-type-vector-3d"></a>

[OpType](class_visualshadernoderemap.md#enum-visualshadernoderemap-optype) **OP_TYPE_VECTOR_3D** = `3`

A 3D vector type.

<a id="class-visualshadernoderemap-constant-op-type-vector-3d-scalar"></a>

[OpType](class_visualshadernoderemap.md#enum-visualshadernoderemap-optype) **OP_TYPE_VECTOR_3D_SCALAR** = `4`

The `value` port uses a 3D vector type, while the `input min`, `input max`, `output min`, and `output max` ports use a floating-point scalar type.

<a id="class-visualshadernoderemap-constant-op-type-vector-4d"></a>

[OpType](class_visualshadernoderemap.md#enum-visualshadernoderemap-optype) **OP_TYPE_VECTOR_4D** = `5`

A 4D vector type.

<a id="class-visualshadernoderemap-constant-op-type-vector-4d-scalar"></a>

[OpType](class_visualshadernoderemap.md#enum-visualshadernoderemap-optype) **OP_TYPE_VECTOR_4D_SCALAR** = `6`

The `value` port uses a 4D vector type, while the `input min`, `input max`, `output min`, and `output max` ports use a floating-point scalar type.

<a id="class-visualshadernoderemap-constant-op-type-max"></a>

[OpType](class_visualshadernoderemap.md#enum-visualshadernoderemap-optype) **OP_TYPE_MAX** = `7`

Represents the size of the [OpType](class_visualshadernoderemap.md#enum-visualshadernoderemap-optype) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernoderemap-property-op-type"></a>

[OpType](class_visualshadernoderemap.md#enum-visualshadernoderemap-optype) **op_type** = `0` [🔗](class_visualshadernoderemap.md#class-visualshadernoderemap-property-op-type)

- void **set_op_type**(value: [OpType](class_visualshadernoderemap.md#enum-visualshadernoderemap-optype))
- [OpType](class_visualshadernoderemap.md#enum-visualshadernoderemap-optype) **get_op_type**()

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!
