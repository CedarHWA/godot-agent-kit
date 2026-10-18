> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodetransformop.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodetransformop"></a>

<a id="class-visualshadernodetransformop"></a>

# VisualShaderNodeTransformOp

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A [Transform3D](class_transform3d.md#class-transform3d) operator to be used within the visual shader graph.

<a id="description"></a>

## Description

Applies [operator](class_visualshadernodetransformop.md#class-visualshadernodetransformop-property-operator) to two transform (4×4 matrices) inputs.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Operator](class_visualshadernodetransformop.md#enum-visualshadernodetransformop-operator) | [operator](class_visualshadernodetransformop.md#class-visualshadernodetransformop-property-operator) | `0` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-visualshadernodetransformop-operator"></a>

enum **Operator**: [🔗](class_visualshadernodetransformop.md#enum-visualshadernodetransformop-operator)

<a id="class-visualshadernodetransformop-constant-op-axb"></a>

[Operator](class_visualshadernodetransformop.md#enum-visualshadernodetransformop-operator) **OP_AxB** = `0`

Multiplies transform `a` by the transform `b`.

<a id="class-visualshadernodetransformop-constant-op-bxa"></a>

[Operator](class_visualshadernodetransformop.md#enum-visualshadernodetransformop-operator) **OP_BxA** = `1`

Multiplies transform `b` by the transform `a`.

<a id="class-visualshadernodetransformop-constant-op-axb-comp"></a>

[Operator](class_visualshadernodetransformop.md#enum-visualshadernodetransformop-operator) **OP_AxB_COMP** = `2`

Performs a component-wise multiplication of transform `a` by the transform `b`.

<a id="class-visualshadernodetransformop-constant-op-bxa-comp"></a>

[Operator](class_visualshadernodetransformop.md#enum-visualshadernodetransformop-operator) **OP_BxA_COMP** = `3`

Performs a component-wise multiplication of transform `b` by the transform `a`.

<a id="class-visualshadernodetransformop-constant-op-add"></a>

[Operator](class_visualshadernodetransformop.md#enum-visualshadernodetransformop-operator) **OP_ADD** = `4`

Adds two transforms.

<a id="class-visualshadernodetransformop-constant-op-a-minus-b"></a>

[Operator](class_visualshadernodetransformop.md#enum-visualshadernodetransformop-operator) **OP_A_MINUS_B** = `5`

Subtracts the transform `a` from the transform `b`.

<a id="class-visualshadernodetransformop-constant-op-b-minus-a"></a>

[Operator](class_visualshadernodetransformop.md#enum-visualshadernodetransformop-operator) **OP_B_MINUS_A** = `6`

Subtracts the transform `b` from the transform `a`.

<a id="class-visualshadernodetransformop-constant-op-a-div-b"></a>

[Operator](class_visualshadernodetransformop.md#enum-visualshadernodetransformop-operator) **OP_A_DIV_B** = `7`

Divides the transform `a` by the transform `b`.

<a id="class-visualshadernodetransformop-constant-op-b-div-a"></a>

[Operator](class_visualshadernodetransformop.md#enum-visualshadernodetransformop-operator) **OP_B_DIV_A** = `8`

Divides the transform `b` by the transform `a`.

<a id="class-visualshadernodetransformop-constant-op-max"></a>

[Operator](class_visualshadernodetransformop.md#enum-visualshadernodetransformop-operator) **OP_MAX** = `9`

Represents the size of the [Operator](class_visualshadernodetransformop.md#enum-visualshadernodetransformop-operator) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodetransformop-property-operator"></a>

[Operator](class_visualshadernodetransformop.md#enum-visualshadernodetransformop-operator) **operator** = `0` [🔗](class_visualshadernodetransformop.md#class-visualshadernodetransformop-property-operator)

- void **set_operator**(value: [Operator](class_visualshadernodetransformop.md#enum-visualshadernodetransformop-operator))
- [Operator](class_visualshadernodetransformop.md#enum-visualshadernodetransformop-operator) **get_operator**()

The type of the operation to be performed on the transforms.
