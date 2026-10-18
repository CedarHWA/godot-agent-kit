> Source: https://docs.godotengine.org/en/4.7/classes/class_inputeventscreentouch.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="inputeventscreentouch"></a>

<a id="class-inputeventscreentouch"></a>

# InputEventScreenTouch

**Inherits:** [InputEventFromWindow](class_inputeventfromwindow.md#class-inputeventfromwindow) **<** [InputEvent](class_inputevent.md#class-inputevent) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Represents a screen touch event.

<a id="description"></a>

## Description

Stores information about multi-touch press/release input events. Supports touch press, touch release and [index](class_inputeventscreentouch.md#class-inputeventscreentouch-property-index) for multi-touch count and order.

<a id="tutorials"></a>

## Tutorials

- [Using InputEvent](../tutorials/inputs/inputevent.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [canceled](class_inputeventscreentouch.md#class-inputeventscreentouch-property-canceled) | `false` |
| [bool](class_bool.md#class-bool) | [double_tap](class_inputeventscreentouch.md#class-inputeventscreentouch-property-double-tap) | `false` |
| [int](class_int.md#class-int) | [index](class_inputeventscreentouch.md#class-inputeventscreentouch-property-index) | `0` |
| [Vector2](class_vector2.md#class-vector2) | [position](class_inputeventscreentouch.md#class-inputeventscreentouch-property-position) | `Vector2(0, 0)` |
| [bool](class_bool.md#class-bool) | [pressed](class_inputeventscreentouch.md#class-inputeventscreentouch-property-pressed) | `false` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-inputeventscreentouch-property-canceled"></a>

[bool](class_bool.md#class-bool) **canceled** = `false` [🔗](class_inputeventscreentouch.md#class-inputeventscreentouch-property-canceled)

- void **set_canceled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_canceled**()

If `true`, the touch event has been canceled.

---


<a id="class-inputeventscreentouch-property-double-tap"></a>

[bool](class_bool.md#class-bool) **double_tap** = `false` [🔗](class_inputeventscreentouch.md#class-inputeventscreentouch-property-double-tap)

- void **set_double_tap**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_double_tap**()

If `true`, the touch's state is a double tap.

---


<a id="class-inputeventscreentouch-property-index"></a>

[int](class_int.md#class-int) **index** = `0` [🔗](class_inputeventscreentouch.md#class-inputeventscreentouch-property-index)

- void **set_index**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_index**()

The touch index in the case of a multi-touch event. One index = one finger.

---


<a id="class-inputeventscreentouch-property-position"></a>

[Vector2](class_vector2.md#class-vector2) **position** = `Vector2(0, 0)` [🔗](class_inputeventscreentouch.md#class-inputeventscreentouch-property-position)

- void **set_position**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_position**()

The touch position in the viewport the node is in, using the coordinate system of this viewport.

---


<a id="class-inputeventscreentouch-property-pressed"></a>

[bool](class_bool.md#class-bool) **pressed** = `false` [🔗](class_inputeventscreentouch.md#class-inputeventscreentouch-property-pressed)

- void **set_pressed**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_pressed**()

If `true`, the touch's state is pressed. If `false`, the touch's state is released.
