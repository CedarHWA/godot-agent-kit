> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodeparticlerandomness.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodeparticlerandomness"></a>

<a id="class-visualshadernodeparticlerandomness"></a>

# VisualShaderNodeParticleRandomness

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Visual shader node for randomizing particle values.

<a id="description"></a>

## Description

Randomness node will output pseudo-random values of the given type based on the specified minimum and maximum values.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [OpType](class_visualshadernodeparticlerandomness.md#enum-visualshadernodeparticlerandomness-optype) | [op_type](class_visualshadernodeparticlerandomness.md#class-visualshadernodeparticlerandomness-property-op-type) | `0` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-visualshadernodeparticlerandomness-optype"></a>

enum **OpType**: [🔗](class_visualshadernodeparticlerandomness.md#enum-visualshadernodeparticlerandomness-optype)

<a id="class-visualshadernodeparticlerandomness-constant-op-type-scalar"></a>

[OpType](class_visualshadernodeparticlerandomness.md#enum-visualshadernodeparticlerandomness-optype) **OP_TYPE_SCALAR** = `0`

A floating-point scalar.

<a id="class-visualshadernodeparticlerandomness-constant-op-type-vector-2d"></a>

[OpType](class_visualshadernodeparticlerandomness.md#enum-visualshadernodeparticlerandomness-optype) **OP_TYPE_VECTOR_2D** = `1`

A 2D vector type.

<a id="class-visualshadernodeparticlerandomness-constant-op-type-vector-3d"></a>

[OpType](class_visualshadernodeparticlerandomness.md#enum-visualshadernodeparticlerandomness-optype) **OP_TYPE_VECTOR_3D** = `2`

A 3D vector type.

<a id="class-visualshadernodeparticlerandomness-constant-op-type-vector-4d"></a>

[OpType](class_visualshadernodeparticlerandomness.md#enum-visualshadernodeparticlerandomness-optype) **OP_TYPE_VECTOR_4D** = `3`

A 4D vector type.

<a id="class-visualshadernodeparticlerandomness-constant-op-type-max"></a>

[OpType](class_visualshadernodeparticlerandomness.md#enum-visualshadernodeparticlerandomness-optype) **OP_TYPE_MAX** = `4`

Represents the size of the [OpType](class_visualshadernodeparticlerandomness.md#enum-visualshadernodeparticlerandomness-optype) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodeparticlerandomness-property-op-type"></a>

[OpType](class_visualshadernodeparticlerandomness.md#enum-visualshadernodeparticlerandomness-optype) **op_type** = `0` [🔗](class_visualshadernodeparticlerandomness.md#class-visualshadernodeparticlerandomness-property-op-type)

- void **set_op_type**(value: [OpType](class_visualshadernodeparticlerandomness.md#enum-visualshadernodeparticlerandomness-optype))
- [OpType](class_visualshadernodeparticlerandomness.md#enum-visualshadernodeparticlerandomness-optype) **get_op_type**()

A type of operands and returned value.
