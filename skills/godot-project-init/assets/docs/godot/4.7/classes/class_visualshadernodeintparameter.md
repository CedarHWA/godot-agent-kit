> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodeintparameter.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodeintparameter"></a>

<a id="class-visualshadernodeintparameter"></a>

# VisualShaderNodeIntParameter

**Inherits:** [VisualShaderNodeParameter](class_visualshadernodeparameter.md#class-visualshadernodeparameter) **<** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A visual shader node for shader parameter (uniform) of type [int](class_int.md#class-int).

<a id="description"></a>

## Description

A [VisualShaderNodeParameter](class_visualshadernodeparameter.md#class-visualshadernodeparameter) of type [int](class_int.md#class-int). Offers additional customization for range of accepted values.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [default_value](class_visualshadernodeintparameter.md#class-visualshadernodeintparameter-property-default-value) | `0` |
| [bool](class_bool.md#class-bool) | [default_value_enabled](class_visualshadernodeintparameter.md#class-visualshadernodeintparameter-property-default-value-enabled) | `false` |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [enum_names](class_visualshadernodeintparameter.md#class-visualshadernodeintparameter-property-enum-names) | `PackedStringArray()` |
| [Hint](class_visualshadernodeintparameter.md#enum-visualshadernodeintparameter-hint) | [hint](class_visualshadernodeintparameter.md#class-visualshadernodeintparameter-property-hint) | `0` |
| [int](class_int.md#class-int) | [max](class_visualshadernodeintparameter.md#class-visualshadernodeintparameter-property-max) | `100` |
| [int](class_int.md#class-int) | [min](class_visualshadernodeintparameter.md#class-visualshadernodeintparameter-property-min) | `0` |
| [int](class_int.md#class-int) | [step](class_visualshadernodeintparameter.md#class-visualshadernodeintparameter-property-step) | `1` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-visualshadernodeintparameter-hint"></a>

enum **Hint**: [🔗](class_visualshadernodeintparameter.md#enum-visualshadernodeintparameter-hint)

<a id="class-visualshadernodeintparameter-constant-hint-none"></a>

[Hint](class_visualshadernodeintparameter.md#enum-visualshadernodeintparameter-hint) **HINT_NONE** = `0`

The parameter will not constrain its value.

<a id="class-visualshadernodeintparameter-constant-hint-range"></a>

[Hint](class_visualshadernodeintparameter.md#enum-visualshadernodeintparameter-hint) **HINT_RANGE** = `1`

The parameter's value must be within the specified [min](class_visualshadernodeintparameter.md#class-visualshadernodeintparameter-property-min)/[max](class_visualshadernodeintparameter.md#class-visualshadernodeintparameter-property-max) range.

<a id="class-visualshadernodeintparameter-constant-hint-range-step"></a>

[Hint](class_visualshadernodeintparameter.md#enum-visualshadernodeintparameter-hint) **HINT_RANGE_STEP** = `2`

The parameter's value must be within the specified range, with the given [step](class_visualshadernodeintparameter.md#class-visualshadernodeintparameter-property-step) between values.

<a id="class-visualshadernodeintparameter-constant-hint-enum"></a>

[Hint](class_visualshadernodeintparameter.md#enum-visualshadernodeintparameter-hint) **HINT_ENUM** = `3`

The parameter uses an enum to associate preset values to names in the editor.

<a id="class-visualshadernodeintparameter-constant-hint-max"></a>

[Hint](class_visualshadernodeintparameter.md#enum-visualshadernodeintparameter-hint) **HINT_MAX** = `4`

Represents the size of the [Hint](class_visualshadernodeintparameter.md#enum-visualshadernodeintparameter-hint) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodeintparameter-property-default-value"></a>

[int](class_int.md#class-int) **default_value** = `0` [🔗](class_visualshadernodeintparameter.md#class-visualshadernodeintparameter-property-default-value)

- void **set_default_value**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_default_value**()

Default value of this parameter, which will be used if not set externally. [default_value_enabled](class_visualshadernodeintparameter.md#class-visualshadernodeintparameter-property-default-value-enabled) must be enabled; defaults to `0` otherwise.

---


<a id="class-visualshadernodeintparameter-property-default-value-enabled"></a>

[bool](class_bool.md#class-bool) **default_value_enabled** = `false` [🔗](class_visualshadernodeintparameter.md#class-visualshadernodeintparameter-property-default-value-enabled)

- void **set_default_value_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_default_value_enabled**()

If `true`, the node will have a custom default value.

---


<a id="class-visualshadernodeintparameter-property-enum-names"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **enum_names** = `PackedStringArray()` [🔗](class_visualshadernodeintparameter.md#class-visualshadernodeintparameter-property-enum-names)

- void **set_enum_names**(value: [PackedStringArray](class_packedstringarray.md#class-packedstringarray))
- [PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_enum_names**()

The names used for the enum select in the editor. [hint](class_visualshadernodeintparameter.md#class-visualshadernodeintparameter-property-hint) must be [HINT_ENUM](class_visualshadernodeintparameter.md#class-visualshadernodeintparameter-constant-hint-enum) for this to take effect.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedStringArray](class_packedstringarray.md#class-packedstringarray) for more details.

---


<a id="class-visualshadernodeintparameter-property-hint"></a>

[Hint](class_visualshadernodeintparameter.md#enum-visualshadernodeintparameter-hint) **hint** = `0` [🔗](class_visualshadernodeintparameter.md#class-visualshadernodeintparameter-property-hint)

- void **set_hint**(value: [Hint](class_visualshadernodeintparameter.md#enum-visualshadernodeintparameter-hint))
- [Hint](class_visualshadernodeintparameter.md#enum-visualshadernodeintparameter-hint) **get_hint**()

Range hint of this node. Use it to customize valid parameter range.

---


<a id="class-visualshadernodeintparameter-property-max"></a>

[int](class_int.md#class-int) **max** = `100` [🔗](class_visualshadernodeintparameter.md#class-visualshadernodeintparameter-property-max)

- void **set_max**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_max**()

The maximum value this parameter can take. [hint](class_visualshadernodeintparameter.md#class-visualshadernodeintparameter-property-hint) must be either [HINT_RANGE](class_visualshadernodeintparameter.md#class-visualshadernodeintparameter-constant-hint-range) or [HINT_RANGE_STEP](class_visualshadernodeintparameter.md#class-visualshadernodeintparameter-constant-hint-range-step) for this to take effect.

---


<a id="class-visualshadernodeintparameter-property-min"></a>

[int](class_int.md#class-int) **min** = `0` [🔗](class_visualshadernodeintparameter.md#class-visualshadernodeintparameter-property-min)

- void **set_min**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_min**()

The minimum value this parameter can take. [hint](class_visualshadernodeintparameter.md#class-visualshadernodeintparameter-property-hint) must be either [HINT_RANGE](class_visualshadernodeintparameter.md#class-visualshadernodeintparameter-constant-hint-range) or [HINT_RANGE_STEP](class_visualshadernodeintparameter.md#class-visualshadernodeintparameter-constant-hint-range-step) for this to take effect.

---


<a id="class-visualshadernodeintparameter-property-step"></a>

[int](class_int.md#class-int) **step** = `1` [🔗](class_visualshadernodeintparameter.md#class-visualshadernodeintparameter-property-step)

- void **set_step**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_step**()

The step between parameter's values. Forces the parameter to be a multiple of the given value. [hint](class_visualshadernodeintparameter.md#class-visualshadernodeintparameter-property-hint) must be [HINT_RANGE_STEP](class_visualshadernodeintparameter.md#class-visualshadernodeintparameter-constant-hint-range-step) for this to take effect.
