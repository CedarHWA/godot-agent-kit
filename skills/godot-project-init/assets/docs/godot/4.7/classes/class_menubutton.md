> Source: https://docs.godotengine.org/en/4.7/classes/class_menubutton.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="menubutton"></a>

<a id="class-menubutton"></a>

# MenuButton

**Inherits:** [Button](class_button.md#class-button) **<** [BaseButton](class_basebutton.md#class-basebutton) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A button that brings up a [PopupMenu](class_popupmenu.md#class-popupmenu) when clicked.

<a id="description"></a>

## Description

A button that brings up a [PopupMenu](class_popupmenu.md#class-popupmenu) when clicked. To create new items inside this [PopupMenu](class_popupmenu.md#class-popupmenu), use `get_popup().add_item("My Item Name")`. You can also create them directly from Godot editor's inspector.

See also [BaseButton](class_basebutton.md#class-basebutton) which contains common properties and methods associated with this node.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [ActionMode](class_basebutton.md#enum-basebutton-actionmode) | action_mode | `0` (overrides [BaseButton](class_basebutton.md#class-basebutton-property-action-mode)) |
| [bool](class_bool.md#class-bool) | flat | `true` (overrides [Button](class_button.md#class-button-property-flat)) |
| [FocusMode](class_control.md#enum-control-focusmode) | focus_mode | `3` (overrides [Control](class_control.md#class-control-property-focus-mode)) |
| [int](class_int.md#class-int) | [item_count](class_menubutton.md#class-menubutton-property-item-count) | `0` |
| [int](class_int.md#class-int) | [popup/item_{index}/checkable](class_menubutton.md#class-menubutton-property-popup-item-index-checkable) | `0` |
| [bool](class_bool.md#class-bool) | [popup/item_{index}/checked](class_menubutton.md#class-menubutton-property-popup-item-index-checked) | `false` |
| [bool](class_bool.md#class-bool) | [popup/item_{index}/disabled](class_menubutton.md#class-menubutton-property-popup-item-index-disabled) | `false` |
| [Texture2D](class_texture2d.md#class-texture2d) | [popup/item_{index}/icon](class_menubutton.md#class-menubutton-property-popup-item-index-icon) |  |
| [int](class_int.md#class-int) | [popup/item_{index}/id](class_menubutton.md#class-menubutton-property-popup-item-index-id) | `0` |
| [bool](class_bool.md#class-bool) | [popup/item_{index}/separator](class_menubutton.md#class-menubutton-property-popup-item-index-separator) | `false` |
| [String](class_string.md#class-string) | [popup/item_{index}/text](class_menubutton.md#class-menubutton-property-popup-item-index-text) | `""` |
| [bool](class_bool.md#class-bool) | [switch_on_hover](class_menubutton.md#class-menubutton-property-switch-on-hover) | `false` |
| [bool](class_bool.md#class-bool) | toggle_mode | `true` (overrides [BaseButton](class_basebutton.md#class-basebutton-property-toggle-mode)) |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [PopupMenu](class_popupmenu.md#class-popupmenu) | [get_popup](class_menubutton.md#class-menubutton-method-get-popup)() const |
| void | [set_disable_shortcuts](class_menubutton.md#class-menubutton-method-set-disable-shortcuts)(disabled: [bool](class_bool.md#class-bool)) |
| void | [show_popup](class_menubutton.md#class-menubutton-method-show-popup)() |

---


<a id="signals"></a>

## Signals

<a id="class-menubutton-signal-about-to-popup"></a>

**about_to_popup**() [🔗](class_menubutton.md#class-menubutton-signal-about-to-popup)

Emitted when the [PopupMenu](class_popupmenu.md#class-popupmenu) of this MenuButton is about to show.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-menubutton-property-item-count"></a>

[int](class_int.md#class-int) **item_count** = `0` [🔗](class_menubutton.md#class-menubutton-property-item-count)

- void **set_item_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_item_count**()

The number of items currently in the list.

---


<a id="class-menubutton-property-popup-item-index-checkable"></a>

[int](class_int.md#class-int) **popup/item_{index}/checkable** = `0` [🔗](class_menubutton.md#class-menubutton-property-popup-item-index-checkable)

The checkable item type of the item at `index`.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

---


<a id="class-menubutton-property-popup-item-index-checked"></a>

[bool](class_bool.md#class-bool) **popup/item_{index}/checked** = `false` [🔗](class_menubutton.md#class-menubutton-property-popup-item-index-checked)

If `true`, the item at `index` is checked.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

---


<a id="class-menubutton-property-popup-item-index-disabled"></a>

[bool](class_bool.md#class-bool) **popup/item_{index}/disabled** = `false` [🔗](class_menubutton.md#class-menubutton-property-popup-item-index-disabled)

If `true`, the item at `index` is disabled.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

---


<a id="class-menubutton-property-popup-item-index-icon"></a>

[Texture2D](class_texture2d.md#class-texture2d) **popup/item_{index}/icon** [🔗](class_menubutton.md#class-menubutton-property-popup-item-index-icon)

The icon of the item at `index`.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

---


<a id="class-menubutton-property-popup-item-index-id"></a>

[int](class_int.md#class-int) **popup/item_{index}/id** = `0` [🔗](class_menubutton.md#class-menubutton-property-popup-item-index-id)

The ID of the item at `index`.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

---


<a id="class-menubutton-property-popup-item-index-separator"></a>

[bool](class_bool.md#class-bool) **popup/item_{index}/separator** = `false` [🔗](class_menubutton.md#class-menubutton-property-popup-item-index-separator)

If `true`, the item at `index` is a separator.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

---


<a id="class-menubutton-property-popup-item-index-text"></a>

[String](class_string.md#class-string) **popup/item_{index}/text** = `""` [🔗](class_menubutton.md#class-menubutton-property-popup-item-index-text)

The text of the item at `index`.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

---


<a id="class-menubutton-property-switch-on-hover"></a>

[bool](class_bool.md#class-bool) **switch_on_hover** = `false` [🔗](class_menubutton.md#class-menubutton-property-switch-on-hover)

- void **set_switch_on_hover**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_switch_on_hover**()

If `true`, when the cursor hovers above another **MenuButton** within the same parent which also has [switch_on_hover](class_menubutton.md#class-menubutton-property-switch-on-hover) enabled, it will close the current **MenuButton** and open the other one.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-menubutton-method-get-popup"></a>

[PopupMenu](class_popupmenu.md#class-popupmenu) **get_popup**() const [🔗](class_menubutton.md#class-menubutton-method-get-popup)

Returns the [PopupMenu](class_popupmenu.md#class-popupmenu) contained in this button.

**Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [Window.visible](class_window.md#class-window-property-visible) property.

---


<a id="class-menubutton-method-set-disable-shortcuts"></a>

void **set_disable_shortcuts**(disabled: [bool](class_bool.md#class-bool)) [🔗](class_menubutton.md#class-menubutton-method-set-disable-shortcuts)

If `true`, shortcuts are disabled and cannot be used to trigger the button.

---


<a id="class-menubutton-method-show-popup"></a>

void **show_popup**() [🔗](class_menubutton.md#class-menubutton-method-show-popup)

Adjusts popup position and sizing for the **MenuButton**, then shows the [PopupMenu](class_popupmenu.md#class-popupmenu). Prefer this over using `get_popup().popup()`.
