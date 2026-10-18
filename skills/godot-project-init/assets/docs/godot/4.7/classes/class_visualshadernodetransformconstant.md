> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodetransformconstant.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodetransformconstant"></a>

<a id="class-visualshadernodetransformconstant"></a>

# VisualShaderNodeTransformConstant

**Inherits:** [VisualShaderNodeConstant](class_visualshadernodeconstant.md#class-visualshadernodeconstant) **<** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A [Transform3D](class_transform3d.md#class-transform3d) constant for use within the visual shader graph.

<a id="description"></a>

## Description

A constant [Transform3D](class_transform3d.md#class-transform3d), which can be used as an input node.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Transform3D](class_transform3d.md#class-transform3d) | [constant](class_visualshadernodetransformconstant.md#class-visualshadernodetransformconstant-property-constant) | `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodetransformconstant-property-constant"></a>

[Transform3D](class_transform3d.md#class-transform3d) **constant** = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)` [🔗](class_visualshadernodetransformconstant.md#class-visualshadernodetransformconstant-property-constant)

- void **set_constant**(value: [Transform3D](class_transform3d.md#class-transform3d))
- [Transform3D](class_transform3d.md#class-transform3d) **get_constant**()

A [Transform3D](class_transform3d.md#class-transform3d) constant which represents the state of this node.
