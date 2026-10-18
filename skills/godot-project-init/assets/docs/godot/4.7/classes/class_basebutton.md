> Source: https://docs.godotengine.org/en/4.7/classes/class_basebutton.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="basebutton"></a>

<a id="class-basebutton"></a>

# BaseButton

**Inherits:** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [Button](class_button.md#class-button), [LinkButton](class_linkbutton.md#class-linkbutton), [TextureButton](class_texturebutton.md#class-texturebutton)

Abstract base class for GUI buttons.

<a id="description"></a>

## Description

**BaseButton** is an abstract base class for GUI buttons. It doesn't display anything by itself.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [ActionMode](class_basebutton.md#enum-basebutton-actionmode) | [action_mode](class_basebutton.md#class-basebutton-property-action-mode) | `1` |
| [ButtonGroup](class_buttongroup.md#class-buttongroup) | [button_group](class_basebutton.md#class-basebutton-property-button-group) |  |
| BitField[[MouseButtonMask](class_@globalscope.md#enum-globalscope-mousebuttonmask)] | [button_mask](class_basebutton.md#class-basebutton-property-button-mask) | `1` |
| [bool](class_bool.md#class-bool) | [button_pressed](class_basebutton.md#class-basebutton-property-button-pressed) | `false` |
| [bool](class_bool.md#class-bool) | [disabled](class_basebutton.md#class-basebutton-property-disabled) | `false` |
| [FocusMode](class_control.md#enum-control-focusmode) | focus_mode | `2` (overrides [Control](class_control.md#class-control-property-focus-mode)) |
| [bool](class_bool.md#class-bool) | [keep_pressed_outside](class_basebutton.md#class-basebutton-property-keep-pressed-outside) | `false` |
| [Shortcut](class_shortcut.md#class-shortcut) | [shortcut](class_basebutton.md#class-basebutton-property-shortcut) |  |
| [bool](class_bool.md#class-bool) | [shortcut_feedback](class_basebutton.md#class-basebutton-property-shortcut-feedback) | `true` |
| [bool](class_bool.md#class-bool) | [shortcut_in_tooltip](class_basebutton.md#class-basebutton-property-shortcut-in-tooltip) | `true` |
| [bool](class_bool.md#class-bool) | [toggle_mode](class_basebutton.md#class-basebutton-property-toggle-mode) | `false` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [_pressed](class_basebutton.md#class-basebutton-private-method-pressed)() virtual |
| void | [_toggled](class_basebutton.md#class-basebutton-private-method-toggled)(toggled_on: [bool](class_bool.md#class-bool)) virtual |
| [DrawMode](class_basebutton.md#enum-basebutton-drawmode) | [get_draw_mode](class_basebutton.md#class-basebutton-method-get-draw-mode)() const |
| [bool](class_bool.md#class-bool) | [is_hovered](class_basebutton.md#class-basebutton-method-is-hovered)() const |
| void | [set_pressed_no_signal](class_basebutton.md#class-basebutton-method-set-pressed-no-signal)(pressed: [bool](class_bool.md#class-bool)) |

---


<a id="signals"></a>

## Signals

<a id="class-basebutton-signal-button-down"></a>

**button_down**() [🔗](class_basebutton.md#class-basebutton-signal-button-down)

Emitted when the button starts being held down.

---


<a id="class-basebutton-signal-button-up"></a>

**button_up**() [🔗](class_basebutton.md#class-basebutton-signal-button-up)

Emitted when the button stops being held down.

---


<a id="class-basebutton-signal-pressed"></a>

**pressed**() [🔗](class_basebutton.md#class-basebutton-signal-pressed)

Emitted when the button is toggled or pressed. This is on [button_down](class_basebutton.md#class-basebutton-signal-button-down) if [action_mode](class_basebutton.md#class-basebutton-property-action-mode) is [ACTION_MODE_BUTTON_PRESS](class_basebutton.md#class-basebutton-constant-action-mode-button-press) and on [button_up](class_basebutton.md#class-basebutton-signal-button-up) otherwise.

If you need to know the button's pressed state (and [toggle_mode](class_basebutton.md#class-basebutton-property-toggle-mode) is active), use [toggled](class_basebutton.md#class-basebutton-signal-toggled) instead.

---


<a id="class-basebutton-signal-toggled"></a>

**toggled**(toggled_on: [bool](class_bool.md#class-bool)) [🔗](class_basebutton.md#class-basebutton-signal-toggled)

Emitted when the button was just toggled between pressed and normal states (only if [toggle_mode](class_basebutton.md#class-basebutton-property-toggle-mode) is active). The new state is contained in the `toggled_on` argument.

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-basebutton-drawmode"></a>

enum **DrawMode**: [🔗](class_basebutton.md#enum-basebutton-drawmode)

<a id="class-basebutton-constant-draw-normal"></a>

[DrawMode](class_basebutton.md#enum-basebutton-drawmode) **DRAW_NORMAL** = `0`

The normal state (i.e. not pressed, not hovered, not toggled and enabled) of buttons.

<a id="class-basebutton-constant-draw-pressed"></a>

[DrawMode](class_basebutton.md#enum-basebutton-drawmode) **DRAW_PRESSED** = `1`

The state of buttons are pressed.

<a id="class-basebutton-constant-draw-hover"></a>

[DrawMode](class_basebutton.md#enum-basebutton-drawmode) **DRAW_HOVER** = `2`

The state of buttons are hovered.

<a id="class-basebutton-constant-draw-disabled"></a>

[DrawMode](class_basebutton.md#enum-basebutton-drawmode) **DRAW_DISABLED** = `3`

The state of buttons are disabled.

<a id="class-basebutton-constant-draw-hover-pressed"></a>

[DrawMode](class_basebutton.md#enum-basebutton-drawmode) **DRAW_HOVER_PRESSED** = `4`

The state of buttons are both hovered and pressed.

---


<a id="enum-basebutton-actionmode"></a>

enum **ActionMode**: [🔗](class_basebutton.md#enum-basebutton-actionmode)

<a id="class-basebutton-constant-action-mode-button-press"></a>

[ActionMode](class_basebutton.md#enum-basebutton-actionmode) **ACTION_MODE_BUTTON_PRESS** = `0`

Require just a press to consider the button clicked.

<a id="class-basebutton-constant-action-mode-button-release"></a>

[ActionMode](class_basebutton.md#enum-basebutton-actionmode) **ACTION_MODE_BUTTON_RELEASE** = `1`

Require a press and a subsequent release before considering the button clicked.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-basebutton-property-action-mode"></a>

[ActionMode](class_basebutton.md#enum-basebutton-actionmode) **action_mode** = `1` [🔗](class_basebutton.md#class-basebutton-property-action-mode)

- void **set_action_mode**(value: [ActionMode](class_basebutton.md#enum-basebutton-actionmode))
- [ActionMode](class_basebutton.md#enum-basebutton-actionmode) **get_action_mode**()

Determines when the button is considered clicked.

---


<a id="class-basebutton-property-button-group"></a>

[ButtonGroup](class_buttongroup.md#class-buttongroup) **button_group** [🔗](class_basebutton.md#class-basebutton-property-button-group)

- void **set_button_group**(value: [ButtonGroup](class_buttongroup.md#class-buttongroup))
- [ButtonGroup](class_buttongroup.md#class-buttongroup) **get_button_group**()

The [ButtonGroup](class_buttongroup.md#class-buttongroup) associated with the button. Not to be confused with node groups.

**Note:** The button will be configured as a radio button if a [ButtonGroup](class_buttongroup.md#class-buttongroup) is assigned to it.

---


<a id="class-basebutton-property-button-mask"></a>

BitField[[MouseButtonMask](class_@globalscope.md#enum-globalscope-mousebuttonmask)] **button_mask** = `1` [🔗](class_basebutton.md#class-basebutton-property-button-mask)

- void **set_button_mask**(value: BitField[[MouseButtonMask](class_@globalscope.md#enum-globalscope-mousebuttonmask)])
- BitField[[MouseButtonMask](class_@globalscope.md#enum-globalscope-mousebuttonmask)] **get_button_mask**()

Binary mask to choose which mouse buttons this button will respond to.

To allow both left-click and right-click, use `MOUSE_BUTTON_MASK_LEFT | MOUSE_BUTTON_MASK_RIGHT`.

---


<a id="class-basebutton-property-button-pressed"></a>

[bool](class_bool.md#class-bool) **button_pressed** = `false` [🔗](class_basebutton.md#class-basebutton-property-button-pressed)

- void **set_pressed**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_pressed**()

If `true`, the button's state is pressed. Means the button is pressed down or toggled (if [toggle_mode](class_basebutton.md#class-basebutton-property-toggle-mode) is active). Only works if [toggle_mode](class_basebutton.md#class-basebutton-property-toggle-mode) is `true`.

**Note:** Changing the value of [button_pressed](class_basebutton.md#class-basebutton-property-button-pressed) will result in [toggled](class_basebutton.md#class-basebutton-signal-toggled) to be emitted. If you want to change the pressed state without emitting that signal, use [set_pressed_no_signal()](class_basebutton.md#class-basebutton-method-set-pressed-no-signal).

---


<a id="class-basebutton-property-disabled"></a>

[bool](class_bool.md#class-bool) **disabled** = `false` [🔗](class_basebutton.md#class-basebutton-property-disabled)

- void **set_disabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_disabled**()

If `true`, the button is in disabled state and can't be clicked or toggled.

**Note:** If the button is disabled while held down, [button_up](class_basebutton.md#class-basebutton-signal-button-up) will be emitted.

---


<a id="class-basebutton-property-keep-pressed-outside"></a>

[bool](class_bool.md#class-bool) **keep_pressed_outside** = `false` [🔗](class_basebutton.md#class-basebutton-property-keep-pressed-outside)

- void **set_keep_pressed_outside**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_keep_pressed_outside**()

If `true`, the button stays pressed when moving the cursor outside the button while pressing it.

**Note:** This property only affects the button's visual appearance. Signals will be emitted at the same moment regardless of this property's value.

---


<a id="class-basebutton-property-shortcut"></a>

[Shortcut](class_shortcut.md#class-shortcut) **shortcut** [🔗](class_basebutton.md#class-basebutton-property-shortcut)

- void **set_shortcut**(value: [Shortcut](class_shortcut.md#class-shortcut))
- [Shortcut](class_shortcut.md#class-shortcut) **get_shortcut**()

[Shortcut](class_shortcut.md#class-shortcut) associated to the button.

---


<a id="class-basebutton-property-shortcut-feedback"></a>

[bool](class_bool.md#class-bool) **shortcut_feedback** = `true` [🔗](class_basebutton.md#class-basebutton-property-shortcut-feedback)

- void **set_shortcut_feedback**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_shortcut_feedback**()

If `true`, the button will highlight for a short amount of time when its shortcut is activated. If `false` and [toggle_mode](class_basebutton.md#class-basebutton-property-toggle-mode) is `false`, the shortcut will activate without any visual feedback.

---


<a id="class-basebutton-property-shortcut-in-tooltip"></a>

[bool](class_bool.md#class-bool) **shortcut_in_tooltip** = `true` [🔗](class_basebutton.md#class-basebutton-property-shortcut-in-tooltip)

- void **set_shortcut_in_tooltip**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_shortcut_in_tooltip_enabled**()

If `true`, the button will add information about its shortcut in the tooltip. This includes the shortcut's events and its [Resource.resource_name](class_resource.md#class-resource-property-resource-name). If both events and name are empty, the shortcut will not be included.

**Note:** This property does nothing when the tooltip control is customized using [Control._make_custom_tooltip()](class_control.md#class-control-private-method-make-custom-tooltip).

---


<a id="class-basebutton-property-toggle-mode"></a>

[bool](class_bool.md#class-bool) **toggle_mode** = `false` [🔗](class_basebutton.md#class-basebutton-property-toggle-mode)

- void **set_toggle_mode**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_toggle_mode**()

If `true`, the button is in toggle mode. Makes the button flip state between pressed and unpressed each time its area is clicked.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-basebutton-private-method-pressed"></a>

void **_pressed**() virtual [🔗](class_basebutton.md#class-basebutton-private-method-pressed)

Called when the button is pressed. If you need to know the button's pressed state (and [toggle_mode](class_basebutton.md#class-basebutton-property-toggle-mode) is active), use [_toggled()](class_basebutton.md#class-basebutton-private-method-toggled) instead.

---


<a id="class-basebutton-private-method-toggled"></a>

void **_toggled**(toggled_on: [bool](class_bool.md#class-bool)) virtual [🔗](class_basebutton.md#class-basebutton-private-method-toggled)

Called when the button is toggled (only if [toggle_mode](class_basebutton.md#class-basebutton-property-toggle-mode) is active).

---


<a id="class-basebutton-method-get-draw-mode"></a>

[DrawMode](class_basebutton.md#enum-basebutton-drawmode) **get_draw_mode**() const [🔗](class_basebutton.md#class-basebutton-method-get-draw-mode)

Returns the visual state used to draw the button. This is useful mainly when implementing your own draw code by either overriding _draw() or connecting to "draw" signal. The visual state of the button is defined by the [DrawMode](class_basebutton.md#enum-basebutton-drawmode) enum.

---


<a id="class-basebutton-method-is-hovered"></a>

[bool](class_bool.md#class-bool) **is_hovered**() const [🔗](class_basebutton.md#class-basebutton-method-is-hovered)

Returns `true` if the mouse has entered the button and has not left it yet.

---


<a id="class-basebutton-method-set-pressed-no-signal"></a>

void **set_pressed_no_signal**(pressed: [bool](class_bool.md#class-bool)) [🔗](class_basebutton.md#class-basebutton-method-set-pressed-no-signal)

Changes the [button_pressed](class_basebutton.md#class-basebutton-property-button-pressed) state of the button, without emitting [toggled](class_basebutton.md#class-basebutton-signal-toggled). Use when you just want to change the state of the button without sending the pressed event (e.g. when initializing scene). Only works if [toggle_mode](class_basebutton.md#class-basebutton-property-toggle-mode) is `true`.

**Note:** This method doesn't unpress other buttons in [button_group](class_basebutton.md#class-basebutton-property-button-group).
