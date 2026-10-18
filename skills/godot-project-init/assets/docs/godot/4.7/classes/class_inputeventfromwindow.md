> Source: https://docs.godotengine.org/en/4.7/classes/class_inputeventfromwindow.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="inputeventfromwindow"></a>

<a id="class-inputeventfromwindow"></a>

# InputEventFromWindow

**Inherits:** [InputEvent](class_inputevent.md#class-inputevent) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [InputEventScreenDrag](class_inputeventscreendrag.md#class-inputeventscreendrag), [InputEventScreenTouch](class_inputeventscreentouch.md#class-inputeventscreentouch), [InputEventWithModifiers](class_inputeventwithmodifiers.md#class-inputeventwithmodifiers)

Abstract base class for [Viewport](class_viewport.md#class-viewport)-based input events.

<a id="description"></a>

## Description

InputEventFromWindow represents events specifically received by windows. This includes mouse events, keyboard events in focused windows or touch screen actions.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [window_id](class_inputeventfromwindow.md#class-inputeventfromwindow-property-window-id) | `0` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-inputeventfromwindow-property-window-id"></a>

[int](class_int.md#class-int) **window_id** = `0` [🔗](class_inputeventfromwindow.md#class-inputeventfromwindow-property-window-id)

- void **set_window_id**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_window_id**()

The ID of a [Window](class_window.md#class-window) that received this event.
