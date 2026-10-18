> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodeswitch.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodeswitch"></a>

<a id="class-visualshadernodeswitch"></a>

# VisualShaderNodeSwitch

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A selector function for use within the visual shader graph.

<a id="description"></a>

## Description

Returns an associated value of the [op_type](class_visualshadernodeswitch.md#class-visualshadernodeswitch-property-op-type) type if the provided boolean value is `true` or `false`.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [OpType](class_visualshadernodeswitch.md#enum-visualshadernodeswitch-optype) | [op_type](class_visualshadernodeswitch.md#class-visualshadernodeswitch-property-op-type) | `0` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-visualshadernodeswitch-optype"></a>

enum **OpType**: [🔗](class_visualshadernodeswitch.md#enum-visualshadernodeswitch-optype)

<a id="class-visualshadernodeswitch-constant-op-type-float"></a>

[OpType](class_visualshadernodeswitch.md#enum-visualshadernodeswitch-optype) **OP_TYPE_FLOAT** = `0`

A floating-point scalar.

<a id="class-visualshadernodeswitch-constant-op-type-int"></a>

[OpType](class_visualshadernodeswitch.md#enum-visualshadernodeswitch-optype) **OP_TYPE_INT** = `1`

An integer scalar.

<a id="class-visualshadernodeswitch-constant-op-type-uint"></a>

[OpType](class_visualshadernodeswitch.md#enum-visualshadernodeswitch-optype) **OP_TYPE_UINT** = `2`

An unsigned integer scalar.

<a id="class-visualshadernodeswitch-constant-op-type-vector-2d"></a>

[OpType](class_visualshadernodeswitch.md#enum-visualshadernodeswitch-optype) **OP_TYPE_VECTOR_2D** = `3`

A 2D vector type.

<a id="class-visualshadernodeswitch-constant-op-type-vector-3d"></a>

[OpType](class_visualshadernodeswitch.md#enum-visualshadernodeswitch-optype) **OP_TYPE_VECTOR_3D** = `4`

A 3D vector type.

<a id="class-visualshadernodeswitch-constant-op-type-vector-4d"></a>

[OpType](class_visualshadernodeswitch.md#enum-visualshadernodeswitch-optype) **OP_TYPE_VECTOR_4D** = `5`

A 4D vector type.

<a id="class-visualshadernodeswitch-constant-op-type-boolean"></a>

[OpType](class_visualshadernodeswitch.md#enum-visualshadernodeswitch-optype) **OP_TYPE_BOOLEAN** = `6`

A boolean type.

<a id="class-visualshadernodeswitch-constant-op-type-transform"></a>

[OpType](class_visualshadernodeswitch.md#enum-visualshadernodeswitch-optype) **OP_TYPE_TRANSFORM** = `7`

A transform type.

<a id="class-visualshadernodeswitch-constant-op-type-max"></a>

[OpType](class_visualshadernodeswitch.md#enum-visualshadernodeswitch-optype) **OP_TYPE_MAX** = `8`

Represents the size of the [OpType](class_visualshadernodeswitch.md#enum-visualshadernodeswitch-optype) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodeswitch-property-op-type"></a>

[OpType](class_visualshadernodeswitch.md#enum-visualshadernodeswitch-optype) **op_type** = `0` [🔗](class_visualshadernodeswitch.md#class-visualshadernodeswitch-property-op-type)

- void **set_op_type**(value: [OpType](class_visualshadernodeswitch.md#enum-visualshadernodeswitch-optype))
- [OpType](class_visualshadernodeswitch.md#enum-visualshadernodeswitch-optype) **get_op_type**()

A type of operands and returned value.
