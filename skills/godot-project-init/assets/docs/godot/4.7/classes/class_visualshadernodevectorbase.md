> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodevectorbase.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodevectorbase"></a>

<a id="class-visualshadernodevectorbase"></a>

# VisualShaderNodeVectorBase

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [VisualShaderNodeFaceForward](class_visualshadernodefaceforward.md#class-visualshadernodefaceforward), [VisualShaderNodeVectorCompose](class_visualshadernodevectorcompose.md#class-visualshadernodevectorcompose), [VisualShaderNodeVectorDecompose](class_visualshadernodevectordecompose.md#class-visualshadernodevectordecompose), [VisualShaderNodeVectorDistance](class_visualshadernodevectordistance.md#class-visualshadernodevectordistance), [VisualShaderNodeVectorFunc](class_visualshadernodevectorfunc.md#class-visualshadernodevectorfunc), [VisualShaderNodeVectorLen](class_visualshadernodevectorlen.md#class-visualshadernodevectorlen), [VisualShaderNodeVectorOp](class_visualshadernodevectorop.md#class-visualshadernodevectorop), [VisualShaderNodeVectorRefract](class_visualshadernodevectorrefract.md#class-visualshadernodevectorrefract)

A base type for the nodes that perform vector operations within the visual shader graph.

<a id="description"></a>

## Description

This is an abstract class. See the derived types for descriptions of the possible operations.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [OpType](class_visualshadernodevectorbase.md#enum-visualshadernodevectorbase-optype) | [op_type](class_visualshadernodevectorbase.md#class-visualshadernodevectorbase-property-op-type) | `1` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-visualshadernodevectorbase-optype"></a>

enum **OpType**: [🔗](class_visualshadernodevectorbase.md#enum-visualshadernodevectorbase-optype)

<a id="class-visualshadernodevectorbase-constant-op-type-vector-2d"></a>

[OpType](class_visualshadernodevectorbase.md#enum-visualshadernodevectorbase-optype) **OP_TYPE_VECTOR_2D** = `0`

A 2D vector type.

<a id="class-visualshadernodevectorbase-constant-op-type-vector-3d"></a>

[OpType](class_visualshadernodevectorbase.md#enum-visualshadernodevectorbase-optype) **OP_TYPE_VECTOR_3D** = `1`

A 3D vector type.

<a id="class-visualshadernodevectorbase-constant-op-type-vector-4d"></a>

[OpType](class_visualshadernodevectorbase.md#enum-visualshadernodevectorbase-optype) **OP_TYPE_VECTOR_4D** = `2`

A 4D vector type.

<a id="class-visualshadernodevectorbase-constant-op-type-max"></a>

[OpType](class_visualshadernodevectorbase.md#enum-visualshadernodevectorbase-optype) **OP_TYPE_MAX** = `3`

Represents the size of the [OpType](class_visualshadernodevectorbase.md#enum-visualshadernodevectorbase-optype) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodevectorbase-property-op-type"></a>

[OpType](class_visualshadernodevectorbase.md#enum-visualshadernodevectorbase-optype) **op_type** = `1` [🔗](class_visualshadernodevectorbase.md#class-visualshadernodevectorbase-property-op-type)

- void **set_op_type**(value: [OpType](class_visualshadernodevectorbase.md#enum-visualshadernodevectorbase-optype))
- [OpType](class_visualshadernodevectorbase.md#enum-visualshadernodevectorbase-optype) **get_op_type**()

A vector type that this operation is performed on.
