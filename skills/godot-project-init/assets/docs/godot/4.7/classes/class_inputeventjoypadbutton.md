> Source: https://docs.godotengine.org/en/4.7/classes/class_inputeventjoypadbutton.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="inputeventjoypadbutton"></a>

<a id="class-inputeventjoypadbutton"></a>

# InputEventJoypadButton

**Inherits:** [InputEvent](class_inputevent.md#class-inputevent) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Represents a gamepad button being pressed or released.

<a id="description"></a>

## Description

Input event type for gamepad buttons. For gamepad analog sticks and joysticks, see [InputEventJoypadMotion](class_inputeventjoypadmotion.md#class-inputeventjoypadmotion).

<a id="tutorials"></a>

## Tutorials

- [Using InputEvent](../tutorials/inputs/inputevent.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [JoyButton](class_@globalscope.md#enum-globalscope-joybutton) | [button_index](class_inputeventjoypadbutton.md#class-inputeventjoypadbutton-property-button-index) | `0` |
| [bool](class_bool.md#class-bool) | [pressed](class_inputeventjoypadbutton.md#class-inputeventjoypadbutton-property-pressed) | `false` |
| [float](class_float.md#class-float) | [pressure](class_inputeventjoypadbutton.md#class-inputeventjoypadbutton-property-pressure) | `0.0` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-inputeventjoypadbutton-property-button-index"></a>

[JoyButton](class_@globalscope.md#enum-globalscope-joybutton) **button_index** = `0` [🔗](class_inputeventjoypadbutton.md#class-inputeventjoypadbutton-property-button-index)

- void **set_button_index**(value: [JoyButton](class_@globalscope.md#enum-globalscope-joybutton))
- [JoyButton](class_@globalscope.md#enum-globalscope-joybutton) **get_button_index**()

Button identifier. One of the [JoyButton](class_@globalscope.md#enum-globalscope-joybutton) button constants.

---


<a id="class-inputeventjoypadbutton-property-pressed"></a>

[bool](class_bool.md#class-bool) **pressed** = `false` [🔗](class_inputeventjoypadbutton.md#class-inputeventjoypadbutton-property-pressed)

- void **set_pressed**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_pressed**()

If `true`, the button's state is pressed. If `false`, the button's state is released.

---


<a id="class-inputeventjoypadbutton-property-pressure"></a>

[float](class_float.md#class-float) **pressure** = `0.0` [🔗](class_inputeventjoypadbutton.md#class-inputeventjoypadbutton-property-pressure)

- void **set_pressure**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_pressure**()

**Deprecated:** This property is never set by the engine and is always `0`.
