> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodecolorconstant.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodecolorconstant"></a>

<a id="class-visualshadernodecolorconstant"></a>

# VisualShaderNodeColorConstant

**Inherits:** [VisualShaderNodeConstant](class_visualshadernodeconstant.md#class-visualshadernodeconstant) **<** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A [Color](class_color.md#class-color) constant to be used within the visual shader graph.

<a id="description"></a>

## Description

Has two output ports representing RGB and alpha channels of [Color](class_color.md#class-color).

Translated to `vec3 rgb` and `float alpha` in the shader language.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Color](class_color.md#class-color) | [constant](class_visualshadernodecolorconstant.md#class-visualshadernodecolorconstant-property-constant) | `Color(1, 1, 1, 1)` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodecolorconstant-property-constant"></a>

[Color](class_color.md#class-color) **constant** = `Color(1, 1, 1, 1)` [🔗](class_visualshadernodecolorconstant.md#class-visualshadernodecolorconstant-property-constant)

- void **set_constant**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_constant**()

A [Color](class_color.md#class-color) constant which represents a state of this node.
