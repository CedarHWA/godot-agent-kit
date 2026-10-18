> Source: https://docs.godotengine.org/en/4.7/classes/class_editorspinslider.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="editorspinslider"></a>

<a id="class-editorspinslider"></a>

# EditorSpinSlider

**Inherits:** [Range](class_range.md#class-range) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Godot editor's control for editing numeric values.

<a id="description"></a>

## Description

This [Control](class_control.md#class-control) node is used in the editor's Inspector dock to allow editing of numeric values. Can be used with [EditorInspectorPlugin](class_editorinspectorplugin.md#class-editorinspectorplugin) to recreate the same behavior.

If the [Range.step](class_range.md#class-range-property-step) value is `1`, the **EditorSpinSlider** will display up/down arrows, similar to [SpinBox](class_spinbox.md#class-spinbox). If the [Range.step](class_range.md#class-range-property-step) value is not `1`, a slider will be displayed instead.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [ControlState](class_editorspinslider.md#enum-editorspinslider-controlstate) | [control_state](class_editorspinslider.md#class-editorspinslider-property-control-state) | `0` |
| [bool](class_bool.md#class-bool) | [deferred_drag_mode](class_editorspinslider.md#class-editorspinslider-property-deferred-drag-mode) | `false` |
| [bool](class_bool.md#class-bool) | [editing_integer](class_editorspinslider.md#class-editorspinslider-property-editing-integer) | `false` |
| [bool](class_bool.md#class-bool) | [flat](class_editorspinslider.md#class-editorspinslider-property-flat) | `false` |
| [FocusMode](class_control.md#enum-control-focusmode) | focus_mode | `2` (overrides [Control](class_control.md#class-control-property-focus-mode)) |
| [bool](class_bool.md#class-bool) | [hide_slider](class_editorspinslider.md#class-editorspinslider-property-hide-slider) | `false` |
| [String](class_string.md#class-string) | [label](class_editorspinslider.md#class-editorspinslider-property-label) | `""` |
| [bool](class_bool.md#class-bool) | [read_only](class_editorspinslider.md#class-editorspinslider-property-read-only) | `false` |
| BitField[[SizeFlags](class_control.md#enum-control-sizeflags)] | size_flags_vertical | `1` (overrides [Control](class_control.md#class-control-property-size-flags-vertical)) |
| [float](class_float.md#class-float) | step | `1.0` (overrides [Range](class_range.md#class-range-property-step)) |
| [String](class_string.md#class-string) | [suffix](class_editorspinslider.md#class-editorspinslider-property-suffix) | `""` |

<a id="theme-properties"></a>

## Theme Properties

|  |  |
| --- | --- |
| [Texture2D](class_texture2d.md#class-texture2d) | [updown](class_editorspinslider.md#class-editorspinslider-theme-icon-updown) |
| [Texture2D](class_texture2d.md#class-texture2d) | [updown_disabled](class_editorspinslider.md#class-editorspinslider-theme-icon-updown-disabled) |

---


<a id="signals"></a>

## Signals

<a id="class-editorspinslider-signal-grabbed"></a>

**grabbed**() [🔗](class_editorspinslider.md#class-editorspinslider-signal-grabbed)

Emitted when the spinner/slider is grabbed.

---


<a id="class-editorspinslider-signal-ungrabbed"></a>

**ungrabbed**() [🔗](class_editorspinslider.md#class-editorspinslider-signal-ungrabbed)

Emitted when the spinner/slider is ungrabbed.

---


<a id="class-editorspinslider-signal-updown-pressed"></a>

**updown_pressed**() [🔗](class_editorspinslider.md#class-editorspinslider-signal-updown-pressed)

Emitted when the updown button is pressed.

---


<a id="class-editorspinslider-signal-value-focus-entered"></a>

**value_focus_entered**() [🔗](class_editorspinslider.md#class-editorspinslider-signal-value-focus-entered)

Emitted when the value form gains focus.

---


<a id="class-editorspinslider-signal-value-focus-exited"></a>

**value_focus_exited**() [🔗](class_editorspinslider.md#class-editorspinslider-signal-value-focus-exited)

Emitted when the value form loses focus.

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-editorspinslider-controlstate"></a>

enum **ControlState**: [🔗](class_editorspinslider.md#enum-editorspinslider-controlstate)

<a id="class-editorspinslider-constant-control-state-default"></a>

[ControlState](class_editorspinslider.md#enum-editorspinslider-controlstate) **CONTROL_STATE_DEFAULT** = `0`

The type of control used will depend on the value of [editing_integer](class_editorspinslider.md#class-editorspinslider-property-editing-integer). Up-down arrows if `true`, a slider if `false`.

<a id="class-editorspinslider-constant-control-state-prefer-slider"></a>

[ControlState](class_editorspinslider.md#enum-editorspinslider-controlstate) **CONTROL_STATE_PREFER_SLIDER** = `1`

A slider will always be used, even if [editing_integer](class_editorspinslider.md#class-editorspinslider-property-editing-integer) is enabled.

<a id="class-editorspinslider-constant-control-state-hide"></a>

[ControlState](class_editorspinslider.md#enum-editorspinslider-controlstate) **CONTROL_STATE_HIDE** = `2`

Neither the up-down arrows nor the slider will be shown.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-editorspinslider-property-control-state"></a>

[ControlState](class_editorspinslider.md#enum-editorspinslider-controlstate) **control_state** = `0` [🔗](class_editorspinslider.md#class-editorspinslider-property-control-state)

- void **set_control_state**(value: [ControlState](class_editorspinslider.md#enum-editorspinslider-controlstate))
- [ControlState](class_editorspinslider.md#enum-editorspinslider-controlstate) **get_control_state**()

The state in which the control used to manipulate the value will be.

---


<a id="class-editorspinslider-property-deferred-drag-mode"></a>

[bool](class_bool.md#class-bool) **deferred_drag_mode** = `false` [🔗](class_editorspinslider.md#class-editorspinslider-property-deferred-drag-mode)

- void **set_deferred_drag_mode_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_deferred_drag_mode_enabled**()

If `true`, changing via dragging is applied only at the end of the input (for example, when the user releases a mouse button).

---


<a id="class-editorspinslider-property-editing-integer"></a>

[bool](class_bool.md#class-bool) **editing_integer** = `false` [🔗](class_editorspinslider.md#class-editorspinslider-property-editing-integer)

- void **set_editing_integer**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_editing_integer**()

If `true`, the **EditorSpinSlider** is considered to be editing an integer value. If `false`, the **EditorSpinSlider** is considered to be editing a floating-point value. This is used to determine whether a slider should be drawn by default. The slider is only drawn for floats; integers use up-down arrows similar to [SpinBox](class_spinbox.md#class-spinbox) instead, unless [control_state](class_editorspinslider.md#class-editorspinslider-property-control-state) is set to [CONTROL_STATE_PREFER_SLIDER](class_editorspinslider.md#class-editorspinslider-constant-control-state-prefer-slider). It will also use [EditorSettings.interface/inspector/integer_drag_speed](class_editorsettings.md#class-editorsettings-property-interface-inspector-integer-drag-speed) instead of [EditorSettings.interface/inspector/float_drag_speed](class_editorsettings.md#class-editorsettings-property-interface-inspector-float-drag-speed) if the slider is available.

---


<a id="class-editorspinslider-property-flat"></a>

[bool](class_bool.md#class-bool) **flat** = `false` [🔗](class_editorspinslider.md#class-editorspinslider-property-flat)

- void **set_flat**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_flat**()

If `true`, the slider will not draw background.

---


<a id="class-editorspinslider-property-hide-slider"></a>

[bool](class_bool.md#class-bool) **hide_slider** = `false` [🔗](class_editorspinslider.md#class-editorspinslider-property-hide-slider)

- void **set_hide_slider**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_hiding_slider**()

**Deprecated:** Use [control_state](class_editorspinslider.md#class-editorspinslider-property-control-state) instead.

If `true`, the slider and up/down arrows are hidden.

---


<a id="class-editorspinslider-property-label"></a>

[String](class_string.md#class-string) **label** = `""` [🔗](class_editorspinslider.md#class-editorspinslider-property-label)

- void **set_label**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_label**()

The text that displays to the left of the value.

---


<a id="class-editorspinslider-property-read-only"></a>

[bool](class_bool.md#class-bool) **read_only** = `false` [🔗](class_editorspinslider.md#class-editorspinslider-property-read-only)

- void **set_read_only**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_read_only**()

If `true`, the slider can't be interacted with.

---


<a id="class-editorspinslider-property-suffix"></a>

[String](class_string.md#class-string) **suffix** = `""` [🔗](class_editorspinslider.md#class-editorspinslider-property-suffix)

- void **set_suffix**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_suffix**()

The suffix to display after the value (in a faded color). This should generally be a plural word. You may have to use an abbreviation if the suffix is too long to be displayed.

---


<a id="theme-property-descriptions"></a>

## Theme Property Descriptions

<a id="class-editorspinslider-theme-icon-updown"></a>

[Texture2D](class_texture2d.md#class-texture2d) **updown** [🔗](class_editorspinslider.md#class-editorspinslider-theme-icon-updown)

Single texture representing both the up and down buttons.

---


<a id="class-editorspinslider-theme-icon-updown-disabled"></a>

[Texture2D](class_texture2d.md#class-texture2d) **updown_disabled** [🔗](class_editorspinslider.md#class-editorspinslider-theme-icon-updown-disabled)

Single texture representing both the up and down buttons, when the control is readonly or disabled.
