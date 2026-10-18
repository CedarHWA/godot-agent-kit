> Source: https://docs.godotengine.org/en/4.7/classes/class_inputeventgesture.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="inputeventgesture"></a>

<a id="class-inputeventgesture"></a>

# InputEventGesture

**Inherits:** [InputEventWithModifiers](class_inputeventwithmodifiers.md#class-inputeventwithmodifiers) **<** [InputEventFromWindow](class_inputeventfromwindow.md#class-inputeventfromwindow) **<** [InputEvent](class_inputevent.md#class-inputevent) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [InputEventMagnifyGesture](class_inputeventmagnifygesture.md#class-inputeventmagnifygesture), [InputEventPanGesture](class_inputeventpangesture.md#class-inputeventpangesture)

Abstract base class for touch gestures.

<a id="description"></a>

## Description

InputEventGestures are sent when a user performs a supported gesture on a touch screen. Gestures can't be emulated using mouse, because they typically require multi-touch.

<a id="tutorials"></a>

## Tutorials

- [Using InputEvent](../tutorials/inputs/inputevent.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | device | `0` (overrides [InputEvent](class_inputevent.md#class-inputevent-property-device)) |
| [Vector2](class_vector2.md#class-vector2) | [position](class_inputeventgesture.md#class-inputeventgesture-property-position) | `Vector2(0, 0)` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-inputeventgesture-property-position"></a>

[Vector2](class_vector2.md#class-vector2) **position** = `Vector2(0, 0)` [🔗](class_inputeventgesture.md#class-inputeventgesture-property-position)

- void **set_position**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_position**()

The local gesture position relative to the [Viewport](class_viewport.md#class-viewport). If used in [Control._gui_input()](class_control.md#class-control-private-method-gui-input), the position is relative to the current [Control](class_control.md#class-control) that received this gesture.
