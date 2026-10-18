> Source: https://docs.godotengine.org/en/4.7/classes/class_popup.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="popup"></a>

<a id="class-popup"></a>

# Popup

**Inherits:** [Window](class_window.md#class-window) **<** [Viewport](class_viewport.md#class-viewport) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [PopupMenu](class_popupmenu.md#class-popupmenu), [PopupPanel](class_popuppanel.md#class-popuppanel)

Base class for contextual windows and panels with fixed position.

<a id="description"></a>

## Description

**Popup** is a base class for contextual windows and panels with fixed position. It's a modal by default (see [Window.popup_window](class_window.md#class-window-property-popup-window)) and provides methods for implementing custom popup behavior.

**Note:** **Popup** is invisible by default. To make it visible, call one of the `popup_*` methods from [Window](class_window.md#class-window) on the node, such as [Window.popup_centered_clamped()](class_window.md#class-window-method-popup-centered-clamped).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | borderless | `true` (overrides [Window](class_window.md#class-window-property-borderless)) |
| [bool](class_bool.md#class-bool) | maximize_disabled | `true` (overrides [Window](class_window.md#class-window-property-maximize-disabled)) |
| [bool](class_bool.md#class-bool) | minimize_disabled | `true` (overrides [Window](class_window.md#class-window-property-minimize-disabled)) |
| [bool](class_bool.md#class-bool) | popup_window | `true` (overrides [Window](class_window.md#class-window-property-popup-window)) |
| [bool](class_bool.md#class-bool) | popup_wm_hint | `true` (overrides [Window](class_window.md#class-window-property-popup-wm-hint)) |
| [bool](class_bool.md#class-bool) | transient | `true` (overrides [Window](class_window.md#class-window-property-transient)) |
| [bool](class_bool.md#class-bool) | unresizable | `true` (overrides [Window](class_window.md#class-window-property-unresizable)) |
| [bool](class_bool.md#class-bool) | visible | `false` (overrides [Window](class_window.md#class-window-property-visible)) |
| [bool](class_bool.md#class-bool) | wrap_controls | `true` (overrides [Window](class_window.md#class-window-property-wrap-controls)) |

---


<a id="signals"></a>

## Signals

<a id="class-popup-signal-popup-hide"></a>

**popup_hide**() [🔗](class_popup.md#class-popup-signal-popup-hide)

Emitted when the popup is hidden.
