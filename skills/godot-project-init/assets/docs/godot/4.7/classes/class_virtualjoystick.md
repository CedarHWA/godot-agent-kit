> Source: https://docs.godotengine.org/en/4.7/classes/class_virtualjoystick.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="virtualjoystick"></a>

<a id="class-virtualjoystick"></a>

# VirtualJoystick

**Inherits:** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A virtual joystick control for touchscreen devices.

<a id="description"></a>

## Description

A customizable on-screen joystick control designed for touchscreen devices. It allows users to provide directional input by dragging a virtual tip within a defined circular area.

This control can simulate directional actions (see [action_up](class_virtualjoystick.md#class-virtualjoystick-property-action-up), [action_down](class_virtualjoystick.md#class-virtualjoystick-property-action-down), [action_left](class_virtualjoystick.md#class-virtualjoystick-property-action-left), and [action_right](class_virtualjoystick.md#class-virtualjoystick-property-action-right)), which are triggered when the joystick is moved in the corresponding directions.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [StringName](class_stringname.md#class-stringname) | [action_down](class_virtualjoystick.md#class-virtualjoystick-property-action-down) | `&"ui_down"` |
| [StringName](class_stringname.md#class-stringname) | [action_left](class_virtualjoystick.md#class-virtualjoystick-property-action-left) | `&"ui_left"` |
| [StringName](class_stringname.md#class-stringname) | [action_right](class_virtualjoystick.md#class-virtualjoystick-property-action-right) | `&"ui_right"` |
| [StringName](class_stringname.md#class-stringname) | [action_up](class_virtualjoystick.md#class-virtualjoystick-property-action-up) | `&"ui_up"` |
| [float](class_float.md#class-float) | [clampzone_ratio](class_virtualjoystick.md#class-virtualjoystick-property-clampzone-ratio) | `1.0` |
| [float](class_float.md#class-float) | [deadzone_ratio](class_virtualjoystick.md#class-virtualjoystick-property-deadzone-ratio) | `0.0` |
| [Vector2](class_vector2.md#class-vector2) | [initial_offset_ratio](class_virtualjoystick.md#class-virtualjoystick-property-initial-offset-ratio) | `Vector2(0.5, 0.5)` |
| [JoystickMode](class_virtualjoystick.md#enum-virtualjoystick-joystickmode) | [joystick_mode](class_virtualjoystick.md#class-virtualjoystick-property-joystick-mode) | `0` |
| [float](class_float.md#class-float) | [joystick_size](class_virtualjoystick.md#class-virtualjoystick-property-joystick-size) | `100.0` |
| [float](class_float.md#class-float) | [tip_size](class_virtualjoystick.md#class-virtualjoystick-property-tip-size) | `50.0` |
| [VisibilityMode](class_virtualjoystick.md#enum-virtualjoystick-visibilitymode) | [visibility_mode](class_virtualjoystick.md#class-virtualjoystick-property-visibility-mode) | `0` |

<a id="theme-properties"></a>

## Theme Properties

|  |  |
| --- | --- |
| [StyleBox](class_stylebox.md#class-stylebox) | [normal_joystick](class_virtualjoystick.md#class-virtualjoystick-theme-style-normal-joystick) |
| [StyleBox](class_stylebox.md#class-stylebox) | [normal_tip](class_virtualjoystick.md#class-virtualjoystick-theme-style-normal-tip) |
| [StyleBox](class_stylebox.md#class-stylebox) | [pressed_joystick](class_virtualjoystick.md#class-virtualjoystick-theme-style-pressed-joystick) |
| [StyleBox](class_stylebox.md#class-stylebox) | [pressed_tip](class_virtualjoystick.md#class-virtualjoystick-theme-style-pressed-tip) |

---


<a id="signals"></a>

## Signals

<a id="class-virtualjoystick-signal-flick-canceled"></a>

**flick_canceled**() [🔗](class_virtualjoystick.md#class-virtualjoystick-signal-flick-canceled)

Emitted when the tip enters the deadzone after being outside of it.

---


<a id="class-virtualjoystick-signal-flicked"></a>

**flicked**(input_vector: [Vector2](class_vector2.md#class-vector2)) [🔗](class_virtualjoystick.md#class-virtualjoystick-signal-flicked)

Emitted when the tip moved outside the deadzone and the joystick is released. The `input_vector` contains the last input direction and strength before release. Its length is between `0.0` and `1.0`.

---


<a id="class-virtualjoystick-signal-pressed"></a>

**pressed**() [🔗](class_virtualjoystick.md#class-virtualjoystick-signal-pressed)

Emitted when the joystick is pressed.

---


<a id="class-virtualjoystick-signal-released"></a>

**released**(input_vector: [Vector2](class_vector2.md#class-vector2)) [🔗](class_virtualjoystick.md#class-virtualjoystick-signal-released)

Emitted when the joystick is released. The `input_vector` is the final input direction and strength, with a length between `0.0` and `1.0`.

---


<a id="class-virtualjoystick-signal-tapped"></a>

**tapped**() [🔗](class_virtualjoystick.md#class-virtualjoystick-signal-tapped)

Emitted when the joystick is released without moving the tip.

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-virtualjoystick-joystickmode"></a>

enum **JoystickMode**: [🔗](class_virtualjoystick.md#enum-virtualjoystick-joystickmode)

<a id="class-virtualjoystick-constant-joystick-fixed"></a>

[JoystickMode](class_virtualjoystick.md#enum-virtualjoystick-joystickmode) **JOYSTICK_FIXED** = `0`

The joystick doesn't move.

<a id="class-virtualjoystick-constant-joystick-dynamic"></a>

[JoystickMode](class_virtualjoystick.md#enum-virtualjoystick-joystickmode) **JOYSTICK_DYNAMIC** = `1`

The joystick is moved to the initial touch position as long as it's within the joystick's bounds. It moves back to its original position when released.

<a id="class-virtualjoystick-constant-joystick-following"></a>

[JoystickMode](class_virtualjoystick.md#enum-virtualjoystick-joystickmode) **JOYSTICK_FOLLOWING** = `2`

The joystick is moved to the initial touch position as long as it's within the joystick's bounds. It will follow the touch input if it goes outside the joystick's range. It moves back to its original position when released.

---


<a id="enum-virtualjoystick-visibilitymode"></a>

enum **VisibilityMode**: [🔗](class_virtualjoystick.md#enum-virtualjoystick-visibilitymode)

<a id="class-virtualjoystick-constant-visibility-always"></a>

[VisibilityMode](class_virtualjoystick.md#enum-virtualjoystick-visibilitymode) **VISIBILITY_ALWAYS** = `0`

The joystick is always visible.

<a id="class-virtualjoystick-constant-visibility-when-touched"></a>

[VisibilityMode](class_virtualjoystick.md#enum-virtualjoystick-visibilitymode) **VISIBILITY_WHEN_TOUCHED** = `1`

The joystick is only visible when being touched.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-virtualjoystick-property-action-down"></a>

[StringName](class_stringname.md#class-stringname) **action_down** = `&"ui_down"` [🔗](class_virtualjoystick.md#class-virtualjoystick-property-action-down)

- void **set_action_down**(value: [StringName](class_stringname.md#class-stringname))
- [StringName](class_stringname.md#class-stringname) **get_action_down**()

The action to trigger when the joystick is moved down.

---


<a id="class-virtualjoystick-property-action-left"></a>

[StringName](class_stringname.md#class-stringname) **action_left** = `&"ui_left"` [🔗](class_virtualjoystick.md#class-virtualjoystick-property-action-left)

- void **set_action_left**(value: [StringName](class_stringname.md#class-stringname))
- [StringName](class_stringname.md#class-stringname) **get_action_left**()

The action to trigger when the joystick is moved left.

---


<a id="class-virtualjoystick-property-action-right"></a>

[StringName](class_stringname.md#class-stringname) **action_right** = `&"ui_right"` [🔗](class_virtualjoystick.md#class-virtualjoystick-property-action-right)

- void **set_action_right**(value: [StringName](class_stringname.md#class-stringname))
- [StringName](class_stringname.md#class-stringname) **get_action_right**()

The action to trigger when the joystick is moved right.

---


<a id="class-virtualjoystick-property-action-up"></a>

[StringName](class_stringname.md#class-stringname) **action_up** = `&"ui_up"` [🔗](class_virtualjoystick.md#class-virtualjoystick-property-action-up)

- void **set_action_up**(value: [StringName](class_stringname.md#class-stringname))
- [StringName](class_stringname.md#class-stringname) **get_action_up**()

The action to trigger when the joystick is moved up.

---


<a id="class-virtualjoystick-property-clampzone-ratio"></a>

[float](class_float.md#class-float) **clampzone_ratio** = `1.0` [🔗](class_virtualjoystick.md#class-virtualjoystick-property-clampzone-ratio)

- void **set_clampzone_ratio**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_clampzone_ratio**()

The multiplier applied to the joystick's radius that defines the clamp zone.

This zone limits how far the joystick tip can move from its center before being clamped.

A value of `1.0` means the tip can move up to the edge of the joystick's visual size.

In [JOYSTICK_FOLLOWING](class_virtualjoystick.md#class-virtualjoystick-constant-joystick-following) mode, this radius also determines how far the finger can move before the joystick base starts following the touch input.

---


<a id="class-virtualjoystick-property-deadzone-ratio"></a>

[float](class_float.md#class-float) **deadzone_ratio** = `0.0` [🔗](class_virtualjoystick.md#class-virtualjoystick-property-deadzone-ratio)

- void **set_deadzone_ratio**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_deadzone_ratio**()

The ratio of the joystick size that defines the joystick deadzone. The joystick tip must move beyond this ratio before being considered active.

This deadzone is applied before triggering input actions and affects the joystick's input vector and all related signals.

Note that input actions may also define their own deadzones in the InputMap. If both are set, the joystick deadzone is applied first, followed by the action's deadzone.

By default, this value is `0.0`, meaning the joystick does not apply its own deadzone and relies entirely on the InputMap action deadzones.

---


<a id="class-virtualjoystick-property-initial-offset-ratio"></a>

[Vector2](class_vector2.md#class-vector2) **initial_offset_ratio** = `Vector2(0.5, 0.5)` [🔗](class_virtualjoystick.md#class-virtualjoystick-property-initial-offset-ratio)

- void **set_initial_offset_ratio**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_initial_offset_ratio**()

The initial position of the joystick as a ratio of the control's size. `(0, 0)` is top-left and `(1, 1)` is bottom-right.

---


<a id="class-virtualjoystick-property-joystick-mode"></a>

[JoystickMode](class_virtualjoystick.md#enum-virtualjoystick-joystickmode) **joystick_mode** = `0` [🔗](class_virtualjoystick.md#class-virtualjoystick-property-joystick-mode)

- void **set_joystick_mode**(value: [JoystickMode](class_virtualjoystick.md#enum-virtualjoystick-joystickmode))
- [JoystickMode](class_virtualjoystick.md#enum-virtualjoystick-joystickmode) **get_joystick_mode**()

The joystick mode to use.

---


<a id="class-virtualjoystick-property-joystick-size"></a>

[float](class_float.md#class-float) **joystick_size** = `100.0` [🔗](class_virtualjoystick.md#class-virtualjoystick-property-joystick-size)

- void **set_joystick_size**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_joystick_size**()

The size of the joystick in pixels.

---


<a id="class-virtualjoystick-property-tip-size"></a>

[float](class_float.md#class-float) **tip_size** = `50.0` [🔗](class_virtualjoystick.md#class-virtualjoystick-property-tip-size)

- void **set_tip_size**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_tip_size**()

The size of the joystick tip in pixels.

---


<a id="class-virtualjoystick-property-visibility-mode"></a>

[VisibilityMode](class_virtualjoystick.md#enum-virtualjoystick-visibilitymode) **visibility_mode** = `0` [🔗](class_virtualjoystick.md#class-virtualjoystick-property-visibility-mode)

- void **set_visibility_mode**(value: [VisibilityMode](class_virtualjoystick.md#enum-virtualjoystick-visibilitymode))
- [VisibilityMode](class_virtualjoystick.md#enum-virtualjoystick-visibilitymode) **get_visibility_mode**()

The visibility mode to use.

---


<a id="theme-property-descriptions"></a>

## Theme Property Descriptions

<a id="class-virtualjoystick-theme-style-normal-joystick"></a>

[StyleBox](class_stylebox.md#class-stylebox) **normal_joystick** [🔗](class_virtualjoystick.md#class-virtualjoystick-theme-style-normal-joystick)

Base joystick [StyleBox](class_stylebox.md#class-stylebox).

---


<a id="class-virtualjoystick-theme-style-normal-tip"></a>

[StyleBox](class_stylebox.md#class-stylebox) **normal_tip** [🔗](class_virtualjoystick.md#class-virtualjoystick-theme-style-normal-tip)

Tip joystick [StyleBox](class_stylebox.md#class-stylebox).

---


<a id="class-virtualjoystick-theme-style-pressed-joystick"></a>

[StyleBox](class_stylebox.md#class-stylebox) **pressed_joystick** [🔗](class_virtualjoystick.md#class-virtualjoystick-theme-style-pressed-joystick)

Base joystick [StyleBox](class_stylebox.md#class-stylebox) when pressed.

---


<a id="class-virtualjoystick-theme-style-pressed-tip"></a>

[StyleBox](class_stylebox.md#class-stylebox) **pressed_tip** [🔗](class_virtualjoystick.md#class-virtualjoystick-theme-style-pressed-tip)

Tip joystick [StyleBox](class_stylebox.md#class-stylebox) when pressed.
