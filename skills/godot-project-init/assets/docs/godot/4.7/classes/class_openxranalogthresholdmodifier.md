> Source: https://docs.godotengine.org/en/4.7/classes/class_openxranalogthresholdmodifier.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxranalogthresholdmodifier"></a>

<a id="class-openxranalogthresholdmodifier"></a>

# OpenXRAnalogThresholdModifier

**Inherits:** [OpenXRActionBindingModifier](class_openxractionbindingmodifier.md#class-openxractionbindingmodifier) **<** [OpenXRBindingModifier](class_openxrbindingmodifier.md#class-openxrbindingmodifier) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

The analog threshold binding modifier can modify a float input to a boolean input with specified thresholds.

<a id="description"></a>

## Description

The analog threshold binding modifier can modify a float input to a boolean input with specified thresholds.

See [XR_VALVE_analog_threshold](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_VALVE_analog_threshold) for in-depth details.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [OpenXRHapticBase](class_openxrhapticbase.md#class-openxrhapticbase) | [off_haptic](class_openxranalogthresholdmodifier.md#class-openxranalogthresholdmodifier-property-off-haptic) |  |
| [float](class_float.md#class-float) | [off_threshold](class_openxranalogthresholdmodifier.md#class-openxranalogthresholdmodifier-property-off-threshold) | `0.4` |
| [OpenXRHapticBase](class_openxrhapticbase.md#class-openxrhapticbase) | [on_haptic](class_openxranalogthresholdmodifier.md#class-openxranalogthresholdmodifier-property-on-haptic) |  |
| [float](class_float.md#class-float) | [on_threshold](class_openxranalogthresholdmodifier.md#class-openxranalogthresholdmodifier-property-on-threshold) | `0.6` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-openxranalogthresholdmodifier-property-off-haptic"></a>

[OpenXRHapticBase](class_openxrhapticbase.md#class-openxrhapticbase) **off_haptic** [🔗](class_openxranalogthresholdmodifier.md#class-openxranalogthresholdmodifier-property-off-haptic)

- void **set_off_haptic**(value: [OpenXRHapticBase](class_openxrhapticbase.md#class-openxrhapticbase))
- [OpenXRHapticBase](class_openxrhapticbase.md#class-openxrhapticbase) **get_off_haptic**()

Haptic pulse to emit when the user releases the input.

---


<a id="class-openxranalogthresholdmodifier-property-off-threshold"></a>

[float](class_float.md#class-float) **off_threshold** = `0.4` [🔗](class_openxranalogthresholdmodifier.md#class-openxranalogthresholdmodifier-property-off-threshold)

- void **set_off_threshold**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_off_threshold**()

When our input value falls below this, our output becomes `false`.

---


<a id="class-openxranalogthresholdmodifier-property-on-haptic"></a>

[OpenXRHapticBase](class_openxrhapticbase.md#class-openxrhapticbase) **on_haptic** [🔗](class_openxranalogthresholdmodifier.md#class-openxranalogthresholdmodifier-property-on-haptic)

- void **set_on_haptic**(value: [OpenXRHapticBase](class_openxrhapticbase.md#class-openxrhapticbase))
- [OpenXRHapticBase](class_openxrhapticbase.md#class-openxrhapticbase) **get_on_haptic**()

Haptic pulse to emit when the user presses the input.

---


<a id="class-openxranalogthresholdmodifier-property-on-threshold"></a>

[float](class_float.md#class-float) **on_threshold** = `0.6` [🔗](class_openxranalogthresholdmodifier.md#class-openxranalogthresholdmodifier-property-on-threshold)

- void **set_on_threshold**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_on_threshold**()

When our input value is equal or larger than this value, our output becomes `true`. It stays `true` until it falls under the [off_threshold](class_openxranalogthresholdmodifier.md#class-openxranalogthresholdmodifier-property-off-threshold) value.
