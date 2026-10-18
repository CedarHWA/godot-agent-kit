> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodecolorparameter.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodecolorparameter"></a>

<a id="class-visualshadernodecolorparameter"></a>

# VisualShaderNodeColorParameter

**Inherits:** [VisualShaderNodeParameter](class_visualshadernodeparameter.md#class-visualshadernodeparameter) **<** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A [Color](class_color.md#class-color) parameter to be used within the visual shader graph.

<a id="description"></a>

## Description

Translated to `uniform vec4` in the shader language.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Color](class_color.md#class-color) | [default_value](class_visualshadernodecolorparameter.md#class-visualshadernodecolorparameter-property-default-value) | `Color(1, 1, 1, 1)` |
| [bool](class_bool.md#class-bool) | [default_value_enabled](class_visualshadernodecolorparameter.md#class-visualshadernodecolorparameter-property-default-value-enabled) | `false` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodecolorparameter-property-default-value"></a>

[Color](class_color.md#class-color) **default_value** = `Color(1, 1, 1, 1)` [🔗](class_visualshadernodecolorparameter.md#class-visualshadernodecolorparameter-property-default-value)

- void **set_default_value**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_default_value**()

A default value to be assigned within the shader.

---


<a id="class-visualshadernodecolorparameter-property-default-value-enabled"></a>

[bool](class_bool.md#class-bool) **default_value_enabled** = `false` [🔗](class_visualshadernodecolorparameter.md#class-visualshadernodecolorparameter-property-default-value-enabled)

- void **set_default_value_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_default_value_enabled**()

Enables usage of the [default_value](class_visualshadernodecolorparameter.md#class-visualshadernodecolorparameter-property-default-value).
