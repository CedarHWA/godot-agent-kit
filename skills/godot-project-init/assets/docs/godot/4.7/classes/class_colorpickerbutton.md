> Source: https://docs.godotengine.org/en/4.7/classes/class_colorpickerbutton.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="colorpickerbutton"></a>

<a id="class-colorpickerbutton"></a>

# ColorPickerButton

**Inherits:** [Button](class_button.md#class-button) **<** [BaseButton](class_basebutton.md#class-basebutton) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A button that brings up a [ColorPicker](class_colorpicker.md#class-colorpicker) when pressed.

<a id="description"></a>

## Description

Encapsulates a [ColorPicker](class_colorpicker.md#class-colorpicker), making it accessible by pressing a button. Pressing the button will toggle the [ColorPicker](class_colorpicker.md#class-colorpicker)'s visibility.

See also [BaseButton](class_basebutton.md#class-basebutton) which contains common properties and methods associated with this node.

**Note:** By default, the button may not be wide enough for the color preview swatch to be visible. Make sure to set [Control.custom_minimum_size](class_control.md#class-control-property-custom-minimum-size) to a big enough value to give the button enough space.

<a id="tutorials"></a>

## Tutorials

- [2D GD Paint Demo](https://godotengine.org/asset-library/asset/2768)
- [GUI Drag And Drop Demo](https://godotengine.org/asset-library/asset/2767)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Color](class_color.md#class-color) | [color](class_colorpickerbutton.md#class-colorpickerbutton-property-color) | `Color(0, 0, 0, 1)` |
| [bool](class_bool.md#class-bool) | [edit_alpha](class_colorpickerbutton.md#class-colorpickerbutton-property-edit-alpha) | `true` |
| [bool](class_bool.md#class-bool) | [edit_intensity](class_colorpickerbutton.md#class-colorpickerbutton-property-edit-intensity) | `true` |
| [bool](class_bool.md#class-bool) | toggle_mode | `true` (overrides [BaseButton](class_basebutton.md#class-basebutton-property-toggle-mode)) |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [ColorPicker](class_colorpicker.md#class-colorpicker) | [get_picker](class_colorpickerbutton.md#class-colorpickerbutton-method-get-picker)() |
| [PopupPanel](class_popuppanel.md#class-popuppanel) | [get_popup](class_colorpickerbutton.md#class-colorpickerbutton-method-get-popup)() |

<a id="theme-properties"></a>

## Theme Properties

|  |  |
| --- | --- |
| [Texture2D](class_texture2d.md#class-texture2d) | [bg](class_colorpickerbutton.md#class-colorpickerbutton-theme-icon-bg) |

---


<a id="signals"></a>

## Signals

<a id="class-colorpickerbutton-signal-color-changed"></a>

**color_changed**(color: [Color](class_color.md#class-color)) [🔗](class_colorpickerbutton.md#class-colorpickerbutton-signal-color-changed)

Emitted when the color changes.

---


<a id="class-colorpickerbutton-signal-picker-created"></a>

**picker_created**() [🔗](class_colorpickerbutton.md#class-colorpickerbutton-signal-picker-created)

Emitted when the [ColorPicker](class_colorpicker.md#class-colorpicker) is created (the button is pressed for the first time).

---


<a id="class-colorpickerbutton-signal-popup-closed"></a>

**popup_closed**() [🔗](class_colorpickerbutton.md#class-colorpickerbutton-signal-popup-closed)

Emitted when the [ColorPicker](class_colorpicker.md#class-colorpicker) is closed.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-colorpickerbutton-property-color"></a>

[Color](class_color.md#class-color) **color** = `Color(0, 0, 0, 1)` [🔗](class_colorpickerbutton.md#class-colorpickerbutton-property-color)

- void **set_pick_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_pick_color**()

The currently selected color.

---


<a id="class-colorpickerbutton-property-edit-alpha"></a>

[bool](class_bool.md#class-bool) **edit_alpha** = `true` [🔗](class_colorpickerbutton.md#class-colorpickerbutton-property-edit-alpha)

- void **set_edit_alpha**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_editing_alpha**()

If `true`, the alpha channel in the displayed [ColorPicker](class_colorpicker.md#class-colorpicker) will be visible.

---


<a id="class-colorpickerbutton-property-edit-intensity"></a>

[bool](class_bool.md#class-bool) **edit_intensity** = `true` [🔗](class_colorpickerbutton.md#class-colorpickerbutton-property-edit-intensity)

- void **set_edit_intensity**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_editing_intensity**()

If `true`, the intensity slider in the displayed [ColorPicker](class_colorpicker.md#class-colorpicker) will be visible.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-colorpickerbutton-method-get-picker"></a>

[ColorPicker](class_colorpicker.md#class-colorpicker) **get_picker**() [🔗](class_colorpickerbutton.md#class-colorpickerbutton-method-get-picker)

Returns the [ColorPicker](class_colorpicker.md#class-colorpicker) that this node toggles.

**Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [CanvasItem.visible](class_canvasitem.md#class-canvasitem-property-visible) property.

---


<a id="class-colorpickerbutton-method-get-popup"></a>

[PopupPanel](class_popuppanel.md#class-popuppanel) **get_popup**() [🔗](class_colorpickerbutton.md#class-colorpickerbutton-method-get-popup)

Returns the control's [PopupPanel](class_popuppanel.md#class-popuppanel) which allows you to connect to popup signals. This allows you to handle events when the ColorPicker is shown or hidden.

**Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [Window.visible](class_window.md#class-window-property-visible) property.

---


<a id="theme-property-descriptions"></a>

## Theme Property Descriptions

<a id="class-colorpickerbutton-theme-icon-bg"></a>

[Texture2D](class_texture2d.md#class-texture2d) **bg** [🔗](class_colorpickerbutton.md#class-colorpickerbutton-theme-icon-bg)

The background of the color preview rect on the button.
