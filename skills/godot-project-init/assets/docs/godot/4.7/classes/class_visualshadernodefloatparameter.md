> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodefloatparameter.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodefloatparameter"></a>

<a id="class-visualshadernodefloatparameter"></a>

# VisualShaderNodeFloatParameter

**Inherits:** [VisualShaderNodeParameter](class_visualshadernodeparameter.md#class-visualshadernodeparameter) **<** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A scalar float parameter to be used within the visual shader graph.

<a id="description"></a>

## Description

Translated to `uniform float` in the shader language.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [default_value](class_visualshadernodefloatparameter.md#class-visualshadernodefloatparameter-property-default-value) | `0.0` |
| [bool](class_bool.md#class-bool) | [default_value_enabled](class_visualshadernodefloatparameter.md#class-visualshadernodefloatparameter-property-default-value-enabled) | `false` |
| [Hint](class_visualshadernodefloatparameter.md#enum-visualshadernodefloatparameter-hint) | [hint](class_visualshadernodefloatparameter.md#class-visualshadernodefloatparameter-property-hint) | `0` |
| [float](class_float.md#class-float) | [max](class_visualshadernodefloatparameter.md#class-visualshadernodefloatparameter-property-max) | `1.0` |
| [float](class_float.md#class-float) | [min](class_visualshadernodefloatparameter.md#class-visualshadernodefloatparameter-property-min) | `0.0` |
| [float](class_float.md#class-float) | [step](class_visualshadernodefloatparameter.md#class-visualshadernodefloatparameter-property-step) | `0.1` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-visualshadernodefloatparameter-hint"></a>

enum **Hint**: [🔗](class_visualshadernodefloatparameter.md#enum-visualshadernodefloatparameter-hint)

<a id="class-visualshadernodefloatparameter-constant-hint-none"></a>

[Hint](class_visualshadernodefloatparameter.md#enum-visualshadernodefloatparameter-hint) **HINT_NONE** = `0`

No hint used.

<a id="class-visualshadernodefloatparameter-constant-hint-range"></a>

[Hint](class_visualshadernodefloatparameter.md#enum-visualshadernodefloatparameter-hint) **HINT_RANGE** = `1`

A range hint for scalar value, which limits possible input values between [min](class_visualshadernodefloatparameter.md#class-visualshadernodefloatparameter-property-min) and [max](class_visualshadernodefloatparameter.md#class-visualshadernodefloatparameter-property-max). Translated to `hint_range(min, max)` in shader code.

<a id="class-visualshadernodefloatparameter-constant-hint-range-step"></a>

[Hint](class_visualshadernodefloatparameter.md#enum-visualshadernodefloatparameter-hint) **HINT_RANGE_STEP** = `2`

A range hint for scalar value with step, which limits possible input values between [min](class_visualshadernodefloatparameter.md#class-visualshadernodefloatparameter-property-min) and [max](class_visualshadernodefloatparameter.md#class-visualshadernodefloatparameter-property-max), with a step (increment) of [step](class_visualshadernodefloatparameter.md#class-visualshadernodefloatparameter-property-step)). Translated to `hint_range(min, max, step)` in shader code.

<a id="class-visualshadernodefloatparameter-constant-hint-max"></a>

[Hint](class_visualshadernodefloatparameter.md#enum-visualshadernodefloatparameter-hint) **HINT_MAX** = `3`

Represents the size of the [Hint](class_visualshadernodefloatparameter.md#enum-visualshadernodefloatparameter-hint) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodefloatparameter-property-default-value"></a>

[float](class_float.md#class-float) **default_value** = `0.0` [🔗](class_visualshadernodefloatparameter.md#class-visualshadernodefloatparameter-property-default-value)

- void **set_default_value**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_default_value**()

A default value to be assigned within the shader.

---


<a id="class-visualshadernodefloatparameter-property-default-value-enabled"></a>

[bool](class_bool.md#class-bool) **default_value_enabled** = `false` [🔗](class_visualshadernodefloatparameter.md#class-visualshadernodefloatparameter-property-default-value-enabled)

- void **set_default_value_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_default_value_enabled**()

Enables usage of the [default_value](class_visualshadernodefloatparameter.md#class-visualshadernodefloatparameter-property-default-value).

---


<a id="class-visualshadernodefloatparameter-property-hint"></a>

[Hint](class_visualshadernodefloatparameter.md#enum-visualshadernodefloatparameter-hint) **hint** = `0` [🔗](class_visualshadernodefloatparameter.md#class-visualshadernodefloatparameter-property-hint)

- void **set_hint**(value: [Hint](class_visualshadernodefloatparameter.md#enum-visualshadernodefloatparameter-hint))
- [Hint](class_visualshadernodefloatparameter.md#enum-visualshadernodefloatparameter-hint) **get_hint**()

A hint applied to the uniform, which controls the values it can take when set through the Inspector.

---


<a id="class-visualshadernodefloatparameter-property-max"></a>

[float](class_float.md#class-float) **max** = `1.0` [🔗](class_visualshadernodefloatparameter.md#class-visualshadernodefloatparameter-property-max)

- void **set_max**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_max**()

Minimum value for range hints. Used if [hint](class_visualshadernodefloatparameter.md#class-visualshadernodefloatparameter-property-hint) is set to [HINT_RANGE](class_visualshadernodefloatparameter.md#class-visualshadernodefloatparameter-constant-hint-range) or [HINT_RANGE_STEP](class_visualshadernodefloatparameter.md#class-visualshadernodefloatparameter-constant-hint-range-step).

---


<a id="class-visualshadernodefloatparameter-property-min"></a>

[float](class_float.md#class-float) **min** = `0.0` [🔗](class_visualshadernodefloatparameter.md#class-visualshadernodefloatparameter-property-min)

- void **set_min**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_min**()

Maximum value for range hints. Used if [hint](class_visualshadernodefloatparameter.md#class-visualshadernodefloatparameter-property-hint) is set to [HINT_RANGE](class_visualshadernodefloatparameter.md#class-visualshadernodefloatparameter-constant-hint-range) or [HINT_RANGE_STEP](class_visualshadernodefloatparameter.md#class-visualshadernodefloatparameter-constant-hint-range-step).

---


<a id="class-visualshadernodefloatparameter-property-step"></a>

[float](class_float.md#class-float) **step** = `0.1` [🔗](class_visualshadernodefloatparameter.md#class-visualshadernodefloatparameter-property-step)

- void **set_step**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_step**()

Step (increment) value for the range hint with step. Used if [hint](class_visualshadernodefloatparameter.md#class-visualshadernodefloatparameter-property-hint) is set to [HINT_RANGE_STEP](class_visualshadernodefloatparameter.md#class-visualshadernodefloatparameter-constant-hint-range-step).
