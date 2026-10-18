> Source: https://docs.godotengine.org/en/4.7/classes/class_inputeventjoypadmotion.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="inputeventjoypadmotion"></a>

<a id="class-inputeventjoypadmotion"></a>

# InputEventJoypadMotion

**Inherits:** [InputEvent](class_inputevent.md#class-inputevent) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Represents axis motions (such as joystick or analog triggers) from a gamepad.

<a id="description"></a>

## Description

Stores information about joystick motions. One **InputEventJoypadMotion** represents one axis at a time. For gamepad buttons, see [InputEventJoypadButton](class_inputeventjoypadbutton.md#class-inputeventjoypadbutton).

<a id="tutorials"></a>

## Tutorials

- [Using InputEvent](../tutorials/inputs/inputevent.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [JoyAxis](class_@globalscope.md#enum-globalscope-joyaxis) | [axis](class_inputeventjoypadmotion.md#class-inputeventjoypadmotion-property-axis) | `0` |
| [float](class_float.md#class-float) | [axis_value](class_inputeventjoypadmotion.md#class-inputeventjoypadmotion-property-axis-value) | `0.0` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-inputeventjoypadmotion-property-axis"></a>

[JoyAxis](class_@globalscope.md#enum-globalscope-joyaxis) **axis** = `0` [🔗](class_inputeventjoypadmotion.md#class-inputeventjoypadmotion-property-axis)

- void **set_axis**(value: [JoyAxis](class_@globalscope.md#enum-globalscope-joyaxis))
- [JoyAxis](class_@globalscope.md#enum-globalscope-joyaxis) **get_axis**()

Axis identifier.

---


<a id="class-inputeventjoypadmotion-property-axis-value"></a>

[float](class_float.md#class-float) **axis_value** = `0.0` [🔗](class_inputeventjoypadmotion.md#class-inputeventjoypadmotion-property-axis-value)

- void **set_axis_value**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_axis_value**()

Current position of the joystick on the given axis. The value ranges from `-1.0` to `1.0`. A value of `0` means the axis is in its resting position.
