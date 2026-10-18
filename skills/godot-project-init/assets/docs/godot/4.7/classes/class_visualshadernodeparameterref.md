> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodeparameterref.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodeparameterref"></a>

<a id="class-visualshadernodeparameterref"></a>

# VisualShaderNodeParameterRef

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A reference to an existing [VisualShaderNodeParameter](class_visualshadernodeparameter.md#class-visualshadernodeparameter).

<a id="description"></a>

## Description

Creating a reference to a [VisualShaderNodeParameter](class_visualshadernodeparameter.md#class-visualshadernodeparameter) allows you to reuse this parameter in different shaders or shader stages easily.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [String](class_string.md#class-string) | [parameter_name](class_visualshadernodeparameterref.md#class-visualshadernodeparameterref-property-parameter-name) | `"[None]"` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodeparameterref-property-parameter-name"></a>

[String](class_string.md#class-string) **parameter_name** = `"[None]"` [🔗](class_visualshadernodeparameterref.md#class-visualshadernodeparameterref-property-parameter-name)

- void **set_parameter_name**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_parameter_name**()

The name of the parameter which this reference points to.
