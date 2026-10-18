> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodebooleanparameter.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodebooleanparameter"></a>

<a id="class-visualshadernodebooleanparameter"></a>

# VisualShaderNodeBooleanParameter

**Inherits:** [VisualShaderNodeParameter](class_visualshadernodeparameter.md#class-visualshadernodeparameter) **<** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A boolean parameter to be used within the visual shader graph.

<a id="description"></a>

## Description

Translated to `uniform bool` in the shader language.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [default_value](class_visualshadernodebooleanparameter.md#class-visualshadernodebooleanparameter-property-default-value) | `false` |
| [bool](class_bool.md#class-bool) | [default_value_enabled](class_visualshadernodebooleanparameter.md#class-visualshadernodebooleanparameter-property-default-value-enabled) | `false` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodebooleanparameter-property-default-value"></a>

[bool](class_bool.md#class-bool) **default_value** = `false` [🔗](class_visualshadernodebooleanparameter.md#class-visualshadernodebooleanparameter-property-default-value)

- void **set_default_value**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_default_value**()

A default value to be assigned within the shader.

---


<a id="class-visualshadernodebooleanparameter-property-default-value-enabled"></a>

[bool](class_bool.md#class-bool) **default_value_enabled** = `false` [🔗](class_visualshadernodebooleanparameter.md#class-visualshadernodebooleanparameter-property-default-value-enabled)

- void **set_default_value_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_default_value_enabled**()

Enables usage of the [default_value](class_visualshadernodebooleanparameter.md#class-visualshadernodebooleanparameter-property-default-value).
