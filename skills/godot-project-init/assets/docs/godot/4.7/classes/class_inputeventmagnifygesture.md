> Source: https://docs.godotengine.org/en/4.7/classes/class_inputeventmagnifygesture.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="inputeventmagnifygesture"></a>

<a id="class-inputeventmagnifygesture"></a>

# InputEventMagnifyGesture

**Inherits:** [InputEventGesture](class_inputeventgesture.md#class-inputeventgesture) **<** [InputEventWithModifiers](class_inputeventwithmodifiers.md#class-inputeventwithmodifiers) **<** [InputEventFromWindow](class_inputeventfromwindow.md#class-inputeventfromwindow) **<** [InputEvent](class_inputevent.md#class-inputevent) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Represents a magnifying touch gesture.

<a id="description"></a>

## Description

Stores the factor of a magnifying touch gesture. This is usually performed when the user pinches the touch screen and used for zooming in/out.

**Note:** On Android, this requires the [ProjectSettings.input_devices/pointing/android/enable_pan_and_scale_gestures](class_projectsettings.md#class-projectsettings-property-input-devices-pointing-android-enable-pan-and-scale-gestures) project setting to be enabled.

<a id="tutorials"></a>

## Tutorials

- [Using InputEvent](../tutorials/inputs/inputevent.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [factor](class_inputeventmagnifygesture.md#class-inputeventmagnifygesture-property-factor) | `1.0` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-inputeventmagnifygesture-property-factor"></a>

[float](class_float.md#class-float) **factor** = `1.0` [🔗](class_inputeventmagnifygesture.md#class-inputeventmagnifygesture-property-factor)

- void **set_factor**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_factor**()

The amount (or delta) of the event. This value is closer to `1.0` the slower the gesture is performed.
