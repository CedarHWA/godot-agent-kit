> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodeclamp.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodeclamp"></a>

<a id="class-visualshadernodeclamp"></a>

# VisualShaderNodeClamp

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Clamps a value within the visual shader graph.

<a id="description"></a>

## Description

Constrains a value to lie between `min` and `max` values.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [OpType](class_visualshadernodeclamp.md#enum-visualshadernodeclamp-optype) | [op_type](class_visualshadernodeclamp.md#class-visualshadernodeclamp-property-op-type) | `0` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-visualshadernodeclamp-optype"></a>

enum **OpType**: [🔗](class_visualshadernodeclamp.md#enum-visualshadernodeclamp-optype)

<a id="class-visualshadernodeclamp-constant-op-type-float"></a>

[OpType](class_visualshadernodeclamp.md#enum-visualshadernodeclamp-optype) **OP_TYPE_FLOAT** = `0`

A floating-point scalar.

<a id="class-visualshadernodeclamp-constant-op-type-int"></a>

[OpType](class_visualshadernodeclamp.md#enum-visualshadernodeclamp-optype) **OP_TYPE_INT** = `1`

An integer scalar.

<a id="class-visualshadernodeclamp-constant-op-type-uint"></a>

[OpType](class_visualshadernodeclamp.md#enum-visualshadernodeclamp-optype) **OP_TYPE_UINT** = `2`

An unsigned integer scalar.

<a id="class-visualshadernodeclamp-constant-op-type-vector-2d"></a>

[OpType](class_visualshadernodeclamp.md#enum-visualshadernodeclamp-optype) **OP_TYPE_VECTOR_2D** = `3`

A 2D vector type.

<a id="class-visualshadernodeclamp-constant-op-type-vector-3d"></a>

[OpType](class_visualshadernodeclamp.md#enum-visualshadernodeclamp-optype) **OP_TYPE_VECTOR_3D** = `4`

A 3D vector type.

<a id="class-visualshadernodeclamp-constant-op-type-vector-4d"></a>

[OpType](class_visualshadernodeclamp.md#enum-visualshadernodeclamp-optype) **OP_TYPE_VECTOR_4D** = `5`

A 4D vector type.

<a id="class-visualshadernodeclamp-constant-op-type-max"></a>

[OpType](class_visualshadernodeclamp.md#enum-visualshadernodeclamp-optype) **OP_TYPE_MAX** = `6`

Represents the size of the [OpType](class_visualshadernodeclamp.md#enum-visualshadernodeclamp-optype) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodeclamp-property-op-type"></a>

[OpType](class_visualshadernodeclamp.md#enum-visualshadernodeclamp-optype) **op_type** = `0` [🔗](class_visualshadernodeclamp.md#class-visualshadernodeclamp-property-op-type)

- void **set_op_type**(value: [OpType](class_visualshadernodeclamp.md#enum-visualshadernodeclamp-optype))
- [OpType](class_visualshadernodeclamp.md#enum-visualshadernodeclamp-optype) **get_op_type**()

A type of operands and returned value.
