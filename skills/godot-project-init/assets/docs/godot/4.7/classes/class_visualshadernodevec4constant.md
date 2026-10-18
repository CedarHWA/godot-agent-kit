> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodevec4constant.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodevec4constant"></a>

<a id="class-visualshadernodevec4constant"></a>

# VisualShaderNodeVec4Constant

**Inherits:** [VisualShaderNodeConstant](class_visualshadernodeconstant.md#class-visualshadernodeconstant) **<** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A 4D vector constant to be used within the visual shader graph.

<a id="description"></a>

## Description

A constant 4D vector, which can be used as an input node.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Quaternion](class_quaternion.md#class-quaternion) | [constant](class_visualshadernodevec4constant.md#class-visualshadernodevec4constant-property-constant) | `Quaternion(0, 0, 0, 1)` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodevec4constant-property-constant"></a>

[Quaternion](class_quaternion.md#class-quaternion) **constant** = `Quaternion(0, 0, 0, 1)` [🔗](class_visualshadernodevec4constant.md#class-visualshadernodevec4constant-property-constant)

- void **set_constant**(value: [Quaternion](class_quaternion.md#class-quaternion))
- [Quaternion](class_quaternion.md#class-quaternion) **get_constant**()

A 4D vector (represented as a [Quaternion](class_quaternion.md#class-quaternion)) constant which represents the state of this node.
