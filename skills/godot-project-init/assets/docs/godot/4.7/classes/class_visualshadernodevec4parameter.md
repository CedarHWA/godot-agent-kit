> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodevec4parameter.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodevec4parameter"></a>

<a id="class-visualshadernodevec4parameter"></a>

# VisualShaderNodeVec4Parameter

**Inherits:** [VisualShaderNodeParameter](class_visualshadernodeparameter.md#class-visualshadernodeparameter) **<** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A 4D vector parameter to be used within the visual shader graph.

<a id="description"></a>

## Description

Translated to `uniform vec4` in the shader language.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Vector4](class_vector4.md#class-vector4) | [default_value](class_visualshadernodevec4parameter.md#class-visualshadernodevec4parameter-property-default-value) | `Vector4(0, 0, 0, 0)` |
| [bool](class_bool.md#class-bool) | [default_value_enabled](class_visualshadernodevec4parameter.md#class-visualshadernodevec4parameter-property-default-value-enabled) | `false` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodevec4parameter-property-default-value"></a>

[Vector4](class_vector4.md#class-vector4) **default_value** = `Vector4(0, 0, 0, 0)` [🔗](class_visualshadernodevec4parameter.md#class-visualshadernodevec4parameter-property-default-value)

- void **set_default_value**(value: [Vector4](class_vector4.md#class-vector4))
- [Vector4](class_vector4.md#class-vector4) **get_default_value**()

A default value to be assigned within the shader.

---


<a id="class-visualshadernodevec4parameter-property-default-value-enabled"></a>

[bool](class_bool.md#class-bool) **default_value_enabled** = `false` [🔗](class_visualshadernodevec4parameter.md#class-visualshadernodevec4parameter-property-default-value-enabled)

- void **set_default_value_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_default_value_enabled**()

Enables usage of the [default_value](class_visualshadernodevec4parameter.md#class-visualshadernodevec4parameter-property-default-value).
