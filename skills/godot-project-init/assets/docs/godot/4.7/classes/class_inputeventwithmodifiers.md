> Source: https://docs.godotengine.org/en/4.7/classes/class_inputeventwithmodifiers.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="inputeventwithmodifiers"></a>

<a id="class-inputeventwithmodifiers"></a>

# InputEventWithModifiers

**Inherits:** [InputEventFromWindow](class_inputeventfromwindow.md#class-inputeventfromwindow) **<** [InputEvent](class_inputevent.md#class-inputevent) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [InputEventGesture](class_inputeventgesture.md#class-inputeventgesture), [InputEventKey](class_inputeventkey.md#class-inputeventkey), [InputEventMouse](class_inputeventmouse.md#class-inputeventmouse)

Abstract base class for input events affected by modifier keys like `Shift` and `Alt`.

<a id="description"></a>

## Description

Stores information about mouse, keyboard, and touch gesture input events. This includes information about which modifier keys are pressed, such as `Shift` or `Alt`. See [Node._input()](class_node.md#class-node-private-method-input).

**Note:** Modifier keys are considered modifiers only when used in combination with another key. As a result, their corresponding member variables, such as [ctrl_pressed](class_inputeventwithmodifiers.md#class-inputeventwithmodifiers-property-ctrl-pressed), will return `false` if the key is pressed on its own.

<a id="tutorials"></a>

## Tutorials

- [Using InputEvent](../tutorials/inputs/inputevent.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [alt_pressed](class_inputeventwithmodifiers.md#class-inputeventwithmodifiers-property-alt-pressed) | `false` |
| [bool](class_bool.md#class-bool) | [command_or_control_autoremap](class_inputeventwithmodifiers.md#class-inputeventwithmodifiers-property-command-or-control-autoremap) | `false` |
| [bool](class_bool.md#class-bool) | [ctrl_pressed](class_inputeventwithmodifiers.md#class-inputeventwithmodifiers-property-ctrl-pressed) | `false` |
| [int](class_int.md#class-int) | device | `16` (overrides [InputEvent](class_inputevent.md#class-inputevent-property-device)) |
| [bool](class_bool.md#class-bool) | [meta_pressed](class_inputeventwithmodifiers.md#class-inputeventwithmodifiers-property-meta-pressed) | `false` |
| [bool](class_bool.md#class-bool) | [shift_pressed](class_inputeventwithmodifiers.md#class-inputeventwithmodifiers-property-shift-pressed) | `false` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| BitField[[KeyModifierMask](class_@globalscope.md#enum-globalscope-keymodifiermask)] | [get_modifiers_mask](class_inputeventwithmodifiers.md#class-inputeventwithmodifiers-method-get-modifiers-mask)() const |
| [bool](class_bool.md#class-bool) | [is_command_or_control_pressed](class_inputeventwithmodifiers.md#class-inputeventwithmodifiers-method-is-command-or-control-pressed)() const |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-inputeventwithmodifiers-property-alt-pressed"></a>

[bool](class_bool.md#class-bool) **alt_pressed** = `false` [🔗](class_inputeventwithmodifiers.md#class-inputeventwithmodifiers-property-alt-pressed)

- void **set_alt_pressed**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_alt_pressed**()

State of the `Alt` modifier.

---


<a id="class-inputeventwithmodifiers-property-command-or-control-autoremap"></a>

[bool](class_bool.md#class-bool) **command_or_control_autoremap** = `false` [🔗](class_inputeventwithmodifiers.md#class-inputeventwithmodifiers-property-command-or-control-autoremap)

- void **set_command_or_control_autoremap**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_command_or_control_autoremap**()

Automatically use `Meta` (`Cmd`) on macOS and `Ctrl` on other platforms. If `true`, [ctrl_pressed](class_inputeventwithmodifiers.md#class-inputeventwithmodifiers-property-ctrl-pressed) and [meta_pressed](class_inputeventwithmodifiers.md#class-inputeventwithmodifiers-property-meta-pressed) cannot be set.

---


<a id="class-inputeventwithmodifiers-property-ctrl-pressed"></a>

[bool](class_bool.md#class-bool) **ctrl_pressed** = `false` [🔗](class_inputeventwithmodifiers.md#class-inputeventwithmodifiers-property-ctrl-pressed)

- void **set_ctrl_pressed**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_ctrl_pressed**()

State of the `Ctrl` modifier.

---


<a id="class-inputeventwithmodifiers-property-meta-pressed"></a>

[bool](class_bool.md#class-bool) **meta_pressed** = `false` [🔗](class_inputeventwithmodifiers.md#class-inputeventwithmodifiers-property-meta-pressed)

- void **set_meta_pressed**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_meta_pressed**()

State of the `Meta` modifier. On Windows and Linux, this represents the Windows key (sometimes called "meta" or "super" on Linux). On macOS, this represents the Command key.

---


<a id="class-inputeventwithmodifiers-property-shift-pressed"></a>

[bool](class_bool.md#class-bool) **shift_pressed** = `false` [🔗](class_inputeventwithmodifiers.md#class-inputeventwithmodifiers-property-shift-pressed)

- void **set_shift_pressed**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_shift_pressed**()

State of the `Shift` modifier.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-inputeventwithmodifiers-method-get-modifiers-mask"></a>

BitField[[KeyModifierMask](class_@globalscope.md#enum-globalscope-keymodifiermask)] **get_modifiers_mask**() const [🔗](class_inputeventwithmodifiers.md#class-inputeventwithmodifiers-method-get-modifiers-mask)

Returns the keycode combination of modifier keys.

---


<a id="class-inputeventwithmodifiers-method-is-command-or-control-pressed"></a>

[bool](class_bool.md#class-bool) **is_command_or_control_pressed**() const [🔗](class_inputeventwithmodifiers.md#class-inputeventwithmodifiers-method-is-command-or-control-pressed)

On macOS, returns `true` if `Meta` (`Cmd`) is pressed.

On other platforms, returns `true` if `Ctrl` is pressed.
