> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodetransformvecmult.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodetransformvecmult"></a>

<a id="class-visualshadernodetransformvecmult"></a>

# VisualShaderNodeTransformVecMult

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Multiplies a [Transform3D](class_transform3d.md#class-transform3d) and a [Vector3](class_vector3.md#class-vector3) within the visual shader graph.

<a id="description"></a>

## Description

A multiplication operation on a transform (4×4 matrix) and a vector, with support for different multiplication operators.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Operator](class_visualshadernodetransformvecmult.md#enum-visualshadernodetransformvecmult-operator) | [operator](class_visualshadernodetransformvecmult.md#class-visualshadernodetransformvecmult-property-operator) | `0` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-visualshadernodetransformvecmult-operator"></a>

enum **Operator**: [🔗](class_visualshadernodetransformvecmult.md#enum-visualshadernodetransformvecmult-operator)

<a id="class-visualshadernodetransformvecmult-constant-op-axb"></a>

[Operator](class_visualshadernodetransformvecmult.md#enum-visualshadernodetransformvecmult-operator) **OP_AxB** = `0`

Multiplies transform `a` by the vector `b`.

<a id="class-visualshadernodetransformvecmult-constant-op-bxa"></a>

[Operator](class_visualshadernodetransformvecmult.md#enum-visualshadernodetransformvecmult-operator) **OP_BxA** = `1`

Multiplies vector `b` by the transform `a`.

<a id="class-visualshadernodetransformvecmult-constant-op-3x3-axb"></a>

[Operator](class_visualshadernodetransformvecmult.md#enum-visualshadernodetransformvecmult-operator) **OP_3x3_AxB** = `2`

Multiplies transform `a` by the vector `b`, skipping the last row and column of the transform.

<a id="class-visualshadernodetransformvecmult-constant-op-3x3-bxa"></a>

[Operator](class_visualshadernodetransformvecmult.md#enum-visualshadernodetransformvecmult-operator) **OP_3x3_BxA** = `3`

Multiplies vector `b` by the transform `a`, skipping the last row and column of the transform.

<a id="class-visualshadernodetransformvecmult-constant-op-max"></a>

[Operator](class_visualshadernodetransformvecmult.md#enum-visualshadernodetransformvecmult-operator) **OP_MAX** = `4`

Represents the size of the [Operator](class_visualshadernodetransformvecmult.md#enum-visualshadernodetransformvecmult-operator) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodetransformvecmult-property-operator"></a>

[Operator](class_visualshadernodetransformvecmult.md#enum-visualshadernodetransformvecmult-operator) **operator** = `0` [🔗](class_visualshadernodetransformvecmult.md#class-visualshadernodetransformvecmult-property-operator)

- void **set_operator**(value: [Operator](class_visualshadernodetransformvecmult.md#enum-visualshadernodetransformvecmult-operator))
- [Operator](class_visualshadernodetransformvecmult.md#enum-visualshadernodetransformvecmult-operator) **get_operator**()

The multiplication type to be performed.
