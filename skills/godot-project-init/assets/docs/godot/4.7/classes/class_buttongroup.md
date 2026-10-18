> Source: https://docs.godotengine.org/en/4.7/classes/class_buttongroup.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="buttongroup"></a>

<a id="class-buttongroup"></a>

# ButtonGroup

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A group of buttons that doesn't allow more than one button to be pressed at a time.

<a id="description"></a>

## Description

A group of [BaseButton](class_basebutton.md#class-basebutton)-derived buttons. The buttons in a **ButtonGroup** are treated like radio buttons: No more than one button can be pressed at a time. Some types of buttons (such as [CheckBox](class_checkbox.md#class-checkbox)) may have a special appearance in this state.

Every member of a **ButtonGroup** should have [BaseButton.toggle_mode](class_basebutton.md#class-basebutton-property-toggle-mode) set to `true`.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [allow_unpress](class_buttongroup.md#class-buttongroup-property-allow-unpress) | `false` |
| [bool](class_bool.md#class-bool) | resource_local_to_scene | `true` (overrides [Resource](class_resource.md#class-resource-property-resource-local-to-scene)) |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Array](class_array.md#class-array)[[BaseButton](class_basebutton.md#class-basebutton)] | [get_buttons](class_buttongroup.md#class-buttongroup-method-get-buttons)() |
| [BaseButton](class_basebutton.md#class-basebutton) | [get_pressed_button](class_buttongroup.md#class-buttongroup-method-get-pressed-button)() |

---


<a id="signals"></a>

## Signals

<a id="class-buttongroup-signal-pressed"></a>

**pressed**(button: [BaseButton](class_basebutton.md#class-basebutton)) [🔗](class_buttongroup.md#class-buttongroup-signal-pressed)

Emitted when one of the buttons of the group is pressed.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-buttongroup-property-allow-unpress"></a>

[bool](class_bool.md#class-bool) **allow_unpress** = `false` [🔗](class_buttongroup.md#class-buttongroup-property-allow-unpress)

- void **set_allow_unpress**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_allow_unpress**()

If `true`, it is possible to unpress all buttons in this **ButtonGroup**.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-buttongroup-method-get-buttons"></a>

[Array](class_array.md#class-array)[[BaseButton](class_basebutton.md#class-basebutton)] **get_buttons**() [🔗](class_buttongroup.md#class-buttongroup-method-get-buttons)

Returns an [Array](class_array.md#class-array) of [Button](class_button.md#class-button)s who have this as their **ButtonGroup** (see [BaseButton.button_group](class_basebutton.md#class-basebutton-property-button-group)).

---


<a id="class-buttongroup-method-get-pressed-button"></a>

[BaseButton](class_basebutton.md#class-basebutton) **get_pressed_button**() [🔗](class_buttongroup.md#class-buttongroup-method-get-pressed-button)

Returns the current pressed button.
