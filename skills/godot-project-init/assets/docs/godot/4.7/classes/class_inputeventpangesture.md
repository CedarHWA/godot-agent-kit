> Source: https://docs.godotengine.org/en/4.7/classes/class_inputeventpangesture.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="inputeventpangesture"></a>

<a id="class-inputeventpangesture"></a>

# InputEventPanGesture

**Inherits:** [InputEventGesture](class_inputeventgesture.md#class-inputeventgesture) **<** [InputEventWithModifiers](class_inputeventwithmodifiers.md#class-inputeventwithmodifiers) **<** [InputEventFromWindow](class_inputeventfromwindow.md#class-inputeventfromwindow) **<** [InputEvent](class_inputevent.md#class-inputevent) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Represents a panning touch gesture.

<a id="description"></a>

## Description

Stores information about pan gestures. A pan gesture is performed when the user swipes the touch screen with two fingers. It's typically used for panning/scrolling.

**Note:** On Android, this requires the [ProjectSettings.input_devices/pointing/android/enable_pan_and_scale_gestures](class_projectsettings.md#class-projectsettings-property-input-devices-pointing-android-enable-pan-and-scale-gestures) project setting to be enabled.

<a id="tutorials"></a>

## Tutorials

- [Using InputEvent](../tutorials/inputs/inputevent.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Vector2](class_vector2.md#class-vector2) | [delta](class_inputeventpangesture.md#class-inputeventpangesture-property-delta) | `Vector2(0, 0)` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-inputeventpangesture-property-delta"></a>

[Vector2](class_vector2.md#class-vector2) **delta** = `Vector2(0, 0)` [🔗](class_inputeventpangesture.md#class-inputeventpangesture-property-delta)

- void **set_delta**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_delta**()

Panning amount since last pan event.
