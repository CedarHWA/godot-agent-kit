> Source: https://docs.godotengine.org/en/4.7/classes/class_itemlist.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="itemlist"></a>

<a id="class-itemlist"></a>

# ItemList

**Inherits:** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A vertical list of selectable items with one or multiple columns.

<a id="description"></a>

## Description

This control provides a vertical list of selectable items that may be in a single or in multiple columns, with each item having options for text and an icon. Tooltips are supported and may be different for every item in the list.

Selectable items in the list may be selected or deselected and multiple selection may be enabled. Selection with right mouse button may also be enabled to allow use of popup context menus. Items may also be "activated" by double-clicking them or by pressing `Enter`.

Item text only supports single-line strings. Newline characters (e.g. `\n`) in the string won't produce a newline. Text wrapping is enabled in [ICON_MODE_TOP](class_itemlist.md#class-itemlist-constant-icon-mode-top) mode, but the column's width is adjusted to fully fit its content by default. You need to set [fixed_column_width](class_itemlist.md#class-itemlist-property-fixed-column-width) greater than zero to wrap the text.

All `set_*` methods allow negative item indices, i.e. `-1` to access the last item, `-2` to select the second-to-last item, and so on.

**Incremental search:** Like [PopupMenu](class_popupmenu.md#class-popupmenu) and [Tree](class_tree.md#class-tree), **ItemList** supports searching within the list while the control is focused. Press a key that matches the first letter of an item's name to select the first item starting with the given letter. After that point, there are two ways to perform incremental search: 1) Press the same key again before the timeout duration to select the next item starting with the same letter. 2) Press letter keys that match the rest of the word before the timeout duration to match to select the item in question directly. Both of these actions will be reset to the beginning of the list if the timeout duration has passed since the last keystroke was registered. You can adjust the timeout duration by changing [ProjectSettings.gui/timers/incremental_search_max_interval_msec](class_projectsettings.md#class-projectsettings-property-gui-timers-incremental-search-max-interval-msec).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [allow_reselect](class_itemlist.md#class-itemlist-property-allow-reselect) | `false` |
| [bool](class_bool.md#class-bool) | [allow_rmb_select](class_itemlist.md#class-itemlist-property-allow-rmb-select) | `false` |
| [bool](class_bool.md#class-bool) | [allow_search](class_itemlist.md#class-itemlist-property-allow-search) | `true` |
| [bool](class_bool.md#class-bool) | [auto_height](class_itemlist.md#class-itemlist-property-auto-height) | `false` |
| [bool](class_bool.md#class-bool) | [auto_width](class_itemlist.md#class-itemlist-property-auto-width) | `false` |
| [bool](class_bool.md#class-bool) | clip_contents | `true` (overrides [Control](class_control.md#class-control-property-clip-contents)) |
| [int](class_int.md#class-int) | [fixed_column_width](class_itemlist.md#class-itemlist-property-fixed-column-width) | `0` |
| [Vector2i](class_vector2i.md#class-vector2i) | [fixed_icon_size](class_itemlist.md#class-itemlist-property-fixed-icon-size) | `Vector2i(0, 0)` |
| [FocusMode](class_control.md#enum-control-focusmode) | focus_mode | `2` (overrides [Control](class_control.md#class-control-property-focus-mode)) |
| [IconMode](class_itemlist.md#enum-itemlist-iconmode) | [icon_mode](class_itemlist.md#class-itemlist-property-icon-mode) | `1` |
| [float](class_float.md#class-float) | [icon_scale](class_itemlist.md#class-itemlist-property-icon-scale) | `1.0` |
| [int](class_int.md#class-int) | [item_count](class_itemlist.md#class-itemlist-property-item-count) | `0` |
| [bool](class_bool.md#class-bool) | [item_{index}/disabled](class_itemlist.md#class-itemlist-property-item-index-disabled) | `false` |
| [Texture2D](class_texture2d.md#class-texture2d) | [item_{index}/icon](class_itemlist.md#class-itemlist-property-item-index-icon) |  |
| [bool](class_bool.md#class-bool) | [item_{index}/selectable](class_itemlist.md#class-itemlist-property-item-index-selectable) | `true` |
| [String](class_string.md#class-string) | [item_{index}/text](class_itemlist.md#class-itemlist-property-item-index-text) | `""` |
| [int](class_int.md#class-int) | [max_columns](class_itemlist.md#class-itemlist-property-max-columns) | `1` |
| [int](class_int.md#class-int) | [max_text_lines](class_itemlist.md#class-itemlist-property-max-text-lines) | `1` |
| [bool](class_bool.md#class-bool) | [same_column_width](class_itemlist.md#class-itemlist-property-same-column-width) | `false` |
| [ScrollHintMode](class_itemlist.md#enum-itemlist-scrollhintmode) | [scroll_hint_mode](class_itemlist.md#class-itemlist-property-scroll-hint-mode) | `0` |
| [SelectMode](class_itemlist.md#enum-itemlist-selectmode) | [select_mode](class_itemlist.md#class-itemlist-property-select-mode) | `0` |
| [OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior) | [text_overrun_behavior](class_itemlist.md#class-itemlist-property-text-overrun-behavior) | `3` |
| [bool](class_bool.md#class-bool) | [tile_scroll_hint](class_itemlist.md#class-itemlist-property-tile-scroll-hint) | `false` |
| [bool](class_bool.md#class-bool) | [wraparound_items](class_itemlist.md#class-itemlist-property-wraparound-items) | `true` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [int](class_int.md#class-int) | [add_icon_item](class_itemlist.md#class-itemlist-method-add-icon-item)(icon: [Texture2D](class_texture2d.md#class-texture2d), selectable: [bool](class_bool.md#class-bool) = true) |
| [int](class_int.md#class-int) | [add_item](class_itemlist.md#class-itemlist-method-add-item)(text: [String](class_string.md#class-string), icon: [Texture2D](class_texture2d.md#class-texture2d) = null, selectable: [bool](class_bool.md#class-bool) = true) |
| void | [center_on_current](class_itemlist.md#class-itemlist-method-center-on-current)(center_verically: [bool](class_bool.md#class-bool) = true, center_horizontally: [bool](class_bool.md#class-bool) = true) |
| void | [clear](class_itemlist.md#class-itemlist-method-clear)() |
| void | [deselect](class_itemlist.md#class-itemlist-method-deselect)(idx: [int](class_int.md#class-int)) |
| void | [deselect_all](class_itemlist.md#class-itemlist-method-deselect-all)() |
| void | [ensure_current_is_visible](class_itemlist.md#class-itemlist-method-ensure-current-is-visible)() |
| void | [force_update_list_size](class_itemlist.md#class-itemlist-method-force-update-list-size)() |
| [HScrollBar](class_hscrollbar.md#class-hscrollbar) | [get_h_scroll_bar](class_itemlist.md#class-itemlist-method-get-h-scroll-bar)() |
| [int](class_int.md#class-int) | [get_item_at_position](class_itemlist.md#class-itemlist-method-get-item-at-position)(position: [Vector2](class_vector2.md#class-vector2), exact: [bool](class_bool.md#class-bool) = false) const |
| [AutoTranslateMode](class_node.md#enum-node-autotranslatemode) | [get_item_auto_translate_mode](class_itemlist.md#class-itemlist-method-get-item-auto-translate-mode)(idx: [int](class_int.md#class-int)) const |
| [Color](class_color.md#class-color) | [get_item_custom_bg_color](class_itemlist.md#class-itemlist-method-get-item-custom-bg-color)(idx: [int](class_int.md#class-int)) const |
| [Color](class_color.md#class-color) | [get_item_custom_fg_color](class_itemlist.md#class-itemlist-method-get-item-custom-fg-color)(idx: [int](class_int.md#class-int)) const |
| [Texture2D](class_texture2d.md#class-texture2d) | [get_item_icon](class_itemlist.md#class-itemlist-method-get-item-icon)(idx: [int](class_int.md#class-int)) const |
| [Color](class_color.md#class-color) | [get_item_icon_modulate](class_itemlist.md#class-itemlist-method-get-item-icon-modulate)(idx: [int](class_int.md#class-int)) const |
| [Rect2](class_rect2.md#class-rect2) | [get_item_icon_region](class_itemlist.md#class-itemlist-method-get-item-icon-region)(idx: [int](class_int.md#class-int)) const |
| [String](class_string.md#class-string) | [get_item_language](class_itemlist.md#class-itemlist-method-get-item-language)(idx: [int](class_int.md#class-int)) const |
| [Variant](class_variant.md#class-variant) | [get_item_metadata](class_itemlist.md#class-itemlist-method-get-item-metadata)(idx: [int](class_int.md#class-int)) const |
| [Rect2](class_rect2.md#class-rect2) | [get_item_rect](class_itemlist.md#class-itemlist-method-get-item-rect)(idx: [int](class_int.md#class-int), expand: [bool](class_bool.md#class-bool) = true) const |
| [String](class_string.md#class-string) | [get_item_text](class_itemlist.md#class-itemlist-method-get-item-text)(idx: [int](class_int.md#class-int)) const |
| [TextDirection](class_control.md#enum-control-textdirection) | [get_item_text_direction](class_itemlist.md#class-itemlist-method-get-item-text-direction)(idx: [int](class_int.md#class-int)) const |
| [String](class_string.md#class-string) | [get_item_tooltip](class_itemlist.md#class-itemlist-method-get-item-tooltip)(idx: [int](class_int.md#class-int)) const |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array) | [get_selected_items](class_itemlist.md#class-itemlist-method-get-selected-items)() |
| [VScrollBar](class_vscrollbar.md#class-vscrollbar) | [get_v_scroll_bar](class_itemlist.md#class-itemlist-method-get-v-scroll-bar)() |
| [bool](class_bool.md#class-bool) | [is_anything_selected](class_itemlist.md#class-itemlist-method-is-anything-selected)() |
| [bool](class_bool.md#class-bool) | [is_item_disabled](class_itemlist.md#class-itemlist-method-is-item-disabled)(idx: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [is_item_icon_transposed](class_itemlist.md#class-itemlist-method-is-item-icon-transposed)(idx: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [is_item_selectable](class_itemlist.md#class-itemlist-method-is-item-selectable)(idx: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [is_item_tooltip_enabled](class_itemlist.md#class-itemlist-method-is-item-tooltip-enabled)(idx: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [is_selected](class_itemlist.md#class-itemlist-method-is-selected)(idx: [int](class_int.md#class-int)) const |
| void | [move_item](class_itemlist.md#class-itemlist-method-move-item)(from_idx: [int](class_int.md#class-int), to_idx: [int](class_int.md#class-int)) |
| void | [remove_item](class_itemlist.md#class-itemlist-method-remove-item)(idx: [int](class_int.md#class-int)) |
| void | [select](class_itemlist.md#class-itemlist-method-select)(idx: [int](class_int.md#class-int), single: [bool](class_bool.md#class-bool) = true) |
| void | [set_item_auto_translate_mode](class_itemlist.md#class-itemlist-method-set-item-auto-translate-mode)(idx: [int](class_int.md#class-int), mode: [AutoTranslateMode](class_node.md#enum-node-autotranslatemode)) |
| void | [set_item_custom_bg_color](class_itemlist.md#class-itemlist-method-set-item-custom-bg-color)(idx: [int](class_int.md#class-int), custom_bg_color: [Color](class_color.md#class-color)) |
| void | [set_item_custom_fg_color](class_itemlist.md#class-itemlist-method-set-item-custom-fg-color)(idx: [int](class_int.md#class-int), custom_fg_color: [Color](class_color.md#class-color)) |
| void | [set_item_disabled](class_itemlist.md#class-itemlist-method-set-item-disabled)(idx: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool)) |
| void | [set_item_icon](class_itemlist.md#class-itemlist-method-set-item-icon)(idx: [int](class_int.md#class-int), icon: [Texture2D](class_texture2d.md#class-texture2d)) |
| void | [set_item_icon_modulate](class_itemlist.md#class-itemlist-method-set-item-icon-modulate)(idx: [int](class_int.md#class-int), modulate: [Color](class_color.md#class-color)) |
| void | [set_item_icon_region](class_itemlist.md#class-itemlist-method-set-item-icon-region)(idx: [int](class_int.md#class-int), rect: [Rect2](class_rect2.md#class-rect2)) |
| void | [set_item_icon_transposed](class_itemlist.md#class-itemlist-method-set-item-icon-transposed)(idx: [int](class_int.md#class-int), transposed: [bool](class_bool.md#class-bool)) |
| void | [set_item_language](class_itemlist.md#class-itemlist-method-set-item-language)(idx: [int](class_int.md#class-int), language: [String](class_string.md#class-string)) |
| void | [set_item_metadata](class_itemlist.md#class-itemlist-method-set-item-metadata)(idx: [int](class_int.md#class-int), metadata: [Variant](class_variant.md#class-variant)) |
| void | [set_item_selectable](class_itemlist.md#class-itemlist-method-set-item-selectable)(idx: [int](class_int.md#class-int), selectable: [bool](class_bool.md#class-bool)) |
| void | [set_item_text](class_itemlist.md#class-itemlist-method-set-item-text)(idx: [int](class_int.md#class-int), text: [String](class_string.md#class-string)) |
| void | [set_item_text_direction](class_itemlist.md#class-itemlist-method-set-item-text-direction)(idx: [int](class_int.md#class-int), direction: [TextDirection](class_control.md#enum-control-textdirection)) |
| void | [set_item_tooltip](class_itemlist.md#class-itemlist-method-set-item-tooltip)(idx: [int](class_int.md#class-int), tooltip: [String](class_string.md#class-string)) |
| void | [set_item_tooltip_enabled](class_itemlist.md#class-itemlist-method-set-item-tooltip-enabled)(idx: [int](class_int.md#class-int), enable: [bool](class_bool.md#class-bool)) |
| void | [sort_items_by_text](class_itemlist.md#class-itemlist-method-sort-items-by-text)() |

<a id="theme-properties"></a>

## Theme Properties

|  |  |  |
| --- | --- | --- |
| [Color](class_color.md#class-color) | [font_color](class_itemlist.md#class-itemlist-theme-color-font-color) | `Color(0.65, 0.65, 0.65, 1)` |
| [Color](class_color.md#class-color) | [font_hovered_color](class_itemlist.md#class-itemlist-theme-color-font-hovered-color) | `Color(0.95, 0.95, 0.95, 1)` |
| [Color](class_color.md#class-color) | [font_hovered_selected_color](class_itemlist.md#class-itemlist-theme-color-font-hovered-selected-color) | `Color(1, 1, 1, 1)` |
| [Color](class_color.md#class-color) | [font_outline_color](class_itemlist.md#class-itemlist-theme-color-font-outline-color) | `Color(0, 0, 0, 1)` |
| [Color](class_color.md#class-color) | [font_selected_color](class_itemlist.md#class-itemlist-theme-color-font-selected-color) | `Color(1, 1, 1, 1)` |
| [Color](class_color.md#class-color) | [guide_color](class_itemlist.md#class-itemlist-theme-color-guide-color) | `Color(0.7, 0.7, 0.7, 0.25)` |
| [Color](class_color.md#class-color) | [scroll_hint_color](class_itemlist.md#class-itemlist-theme-color-scroll-hint-color) | `Color(0, 0, 0, 1)` |
| [int](class_int.md#class-int) | [h_separation](class_itemlist.md#class-itemlist-theme-constant-h-separation) | `4` |
| [int](class_int.md#class-int) | [icon_margin](class_itemlist.md#class-itemlist-theme-constant-icon-margin) | `4` |
| [int](class_int.md#class-int) | [line_separation](class_itemlist.md#class-itemlist-theme-constant-line-separation) | `2` |
| [int](class_int.md#class-int) | [outline_size](class_itemlist.md#class-itemlist-theme-constant-outline-size) | `0` |
| [int](class_int.md#class-int) | [v_separation](class_itemlist.md#class-itemlist-theme-constant-v-separation) | `4` |
| [Font](class_font.md#class-font) | [font](class_itemlist.md#class-itemlist-theme-font-font) |  |
| [int](class_int.md#class-int) | [font_size](class_itemlist.md#class-itemlist-theme-font-size-font-size) |  |
| [Texture2D](class_texture2d.md#class-texture2d) | [scroll_hint](class_itemlist.md#class-itemlist-theme-icon-scroll-hint) |  |
| [StyleBox](class_stylebox.md#class-stylebox) | [cursor](class_itemlist.md#class-itemlist-theme-style-cursor) |  |
| [StyleBox](class_stylebox.md#class-stylebox) | [cursor_unfocused](class_itemlist.md#class-itemlist-theme-style-cursor-unfocused) |  |
| [StyleBox](class_stylebox.md#class-stylebox) | [focus](class_itemlist.md#class-itemlist-theme-style-focus) |  |
| [StyleBox](class_stylebox.md#class-stylebox) | [hovered](class_itemlist.md#class-itemlist-theme-style-hovered) |  |
| [StyleBox](class_stylebox.md#class-stylebox) | [hovered_selected](class_itemlist.md#class-itemlist-theme-style-hovered-selected) |  |
| [StyleBox](class_stylebox.md#class-stylebox) | [hovered_selected_focus](class_itemlist.md#class-itemlist-theme-style-hovered-selected-focus) |  |
| [StyleBox](class_stylebox.md#class-stylebox) | [panel](class_itemlist.md#class-itemlist-theme-style-panel) |  |
| [StyleBox](class_stylebox.md#class-stylebox) | [selected](class_itemlist.md#class-itemlist-theme-style-selected) |  |
| [StyleBox](class_stylebox.md#class-stylebox) | [selected_focus](class_itemlist.md#class-itemlist-theme-style-selected-focus) |  |

---


<a id="signals"></a>

## Signals

<a id="class-itemlist-signal-empty-clicked"></a>

**empty_clicked**(at_position: [Vector2](class_vector2.md#class-vector2), mouse_button_index: [int](class_int.md#class-int)) [🔗](class_itemlist.md#class-itemlist-signal-empty-clicked)

Emitted when any mouse click is issued within the rect of the list but on empty space.

`at_position` is the click position in this control's local coordinate system.

---


<a id="class-itemlist-signal-item-activated"></a>

**item_activated**(index: [int](class_int.md#class-int)) [🔗](class_itemlist.md#class-itemlist-signal-item-activated)

Emitted when specified list item is activated via double-clicking or by pressing `Enter`.

---


<a id="class-itemlist-signal-item-clicked"></a>

**item_clicked**(index: [int](class_int.md#class-int), at_position: [Vector2](class_vector2.md#class-vector2), mouse_button_index: [int](class_int.md#class-int)) [🔗](class_itemlist.md#class-itemlist-signal-item-clicked)

Emitted when specified list item has been clicked with any mouse button.

`at_position` is the click position in this control's local coordinate system.

---


<a id="class-itemlist-signal-item-selected"></a>

**item_selected**(index: [int](class_int.md#class-int)) [🔗](class_itemlist.md#class-itemlist-signal-item-selected)

Emitted when specified item has been selected. Only applicable in single selection mode.

[allow_reselect](class_itemlist.md#class-itemlist-property-allow-reselect) must be enabled to reselect an item.

---


<a id="class-itemlist-signal-multi-selected"></a>

**multi_selected**(index: [int](class_int.md#class-int), selected: [bool](class_bool.md#class-bool)) [🔗](class_itemlist.md#class-itemlist-signal-multi-selected)

Emitted when a multiple selection is altered on a list allowing multiple selection.

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-itemlist-iconmode"></a>

enum **IconMode**: [🔗](class_itemlist.md#enum-itemlist-iconmode)

<a id="class-itemlist-constant-icon-mode-top"></a>

[IconMode](class_itemlist.md#enum-itemlist-iconmode) **ICON_MODE_TOP** = `0`

Icon is drawn above the text.

<a id="class-itemlist-constant-icon-mode-left"></a>

[IconMode](class_itemlist.md#enum-itemlist-iconmode) **ICON_MODE_LEFT** = `1`

Icon is drawn to the left of the text.

---


<a id="enum-itemlist-selectmode"></a>

enum **SelectMode**: [🔗](class_itemlist.md#enum-itemlist-selectmode)

<a id="class-itemlist-constant-select-single"></a>

[SelectMode](class_itemlist.md#enum-itemlist-selectmode) **SELECT_SINGLE** = `0`

Only allow selecting a single item.

<a id="class-itemlist-constant-select-multi"></a>

[SelectMode](class_itemlist.md#enum-itemlist-selectmode) **SELECT_MULTI** = `1`

Allows selecting multiple items by holding `Ctrl` or `Shift`.

<a id="class-itemlist-constant-select-toggle"></a>

[SelectMode](class_itemlist.md#enum-itemlist-selectmode) **SELECT_TOGGLE** = `2`

Allows selecting multiple items by toggling them on and off.

---


<a id="enum-itemlist-scrollhintmode"></a>

enum **ScrollHintMode**: [🔗](class_itemlist.md#enum-itemlist-scrollhintmode)

<a id="class-itemlist-constant-scroll-hint-mode-disabled"></a>

[ScrollHintMode](class_itemlist.md#enum-itemlist-scrollhintmode) **SCROLL_HINT_MODE_DISABLED** = `0`

Scroll hints will never be shown.

<a id="class-itemlist-constant-scroll-hint-mode-both"></a>

[ScrollHintMode](class_itemlist.md#enum-itemlist-scrollhintmode) **SCROLL_HINT_MODE_BOTH** = `1`

Scroll hints will be shown at the top and bottom.

<a id="class-itemlist-constant-scroll-hint-mode-top"></a>

[ScrollHintMode](class_itemlist.md#enum-itemlist-scrollhintmode) **SCROLL_HINT_MODE_TOP** = `2`

Only the top scroll hint will be shown.

<a id="class-itemlist-constant-scroll-hint-mode-bottom"></a>

[ScrollHintMode](class_itemlist.md#enum-itemlist-scrollhintmode) **SCROLL_HINT_MODE_BOTTOM** = `3`

Only the bottom scroll hint will be shown.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-itemlist-property-allow-reselect"></a>

[bool](class_bool.md#class-bool) **allow_reselect** = `false` [🔗](class_itemlist.md#class-itemlist-property-allow-reselect)

- void **set_allow_reselect**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_allow_reselect**()

If `true`, the currently selected item can be selected again.

---


<a id="class-itemlist-property-allow-rmb-select"></a>

[bool](class_bool.md#class-bool) **allow_rmb_select** = `false` [🔗](class_itemlist.md#class-itemlist-property-allow-rmb-select)

- void **set_allow_rmb_select**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_allow_rmb_select**()

If `true`, right mouse button click can select items.

---


<a id="class-itemlist-property-allow-search"></a>

[bool](class_bool.md#class-bool) **allow_search** = `true` [🔗](class_itemlist.md#class-itemlist-property-allow-search)

- void **set_allow_search**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_allow_search**()

If `true`, allows navigating the **ItemList** with letter keys through incremental search.

---


<a id="class-itemlist-property-auto-height"></a>

[bool](class_bool.md#class-bool) **auto_height** = `false` [🔗](class_itemlist.md#class-itemlist-property-auto-height)

- void **set_auto_height**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **has_auto_height**()

If `true`, the control will automatically resize the height to fit its content.

---


<a id="class-itemlist-property-auto-width"></a>

[bool](class_bool.md#class-bool) **auto_width** = `false` [🔗](class_itemlist.md#class-itemlist-property-auto-width)

- void **set_auto_width**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **has_auto_width**()

If `true`, the control will automatically resize the width to fit its content.

---


<a id="class-itemlist-property-fixed-column-width"></a>

[int](class_int.md#class-int) **fixed_column_width** = `0` [🔗](class_itemlist.md#class-itemlist-property-fixed-column-width)

- void **set_fixed_column_width**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_fixed_column_width**()

The width all columns will be adjusted to.

A value of zero disables the adjustment, each item will have a width equal to the width of its content and the columns will have an uneven width.

---


<a id="class-itemlist-property-fixed-icon-size"></a>

[Vector2i](class_vector2i.md#class-vector2i) **fixed_icon_size** = `Vector2i(0, 0)` [🔗](class_itemlist.md#class-itemlist-property-fixed-icon-size)

- void **set_fixed_icon_size**(value: [Vector2i](class_vector2i.md#class-vector2i))
- [Vector2i](class_vector2i.md#class-vector2i) **get_fixed_icon_size**()

The size all icons will be adjusted to.

If either X or Y component is not greater than zero, icon size won't be affected.

---


<a id="class-itemlist-property-icon-mode"></a>

[IconMode](class_itemlist.md#enum-itemlist-iconmode) **icon_mode** = `1` [🔗](class_itemlist.md#class-itemlist-property-icon-mode)

- void **set_icon_mode**(value: [IconMode](class_itemlist.md#enum-itemlist-iconmode))
- [IconMode](class_itemlist.md#enum-itemlist-iconmode) **get_icon_mode**()

The icon position, whether above or to the left of the text. See the [IconMode](class_itemlist.md#enum-itemlist-iconmode) constants.

---


<a id="class-itemlist-property-icon-scale"></a>

[float](class_float.md#class-float) **icon_scale** = `1.0` [🔗](class_itemlist.md#class-itemlist-property-icon-scale)

- void **set_icon_scale**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_icon_scale**()

The scale of icon applied after [fixed_icon_size](class_itemlist.md#class-itemlist-property-fixed-icon-size) and transposing takes effect.

---


<a id="class-itemlist-property-item-count"></a>

[int](class_int.md#class-int) **item_count** = `0` [🔗](class_itemlist.md#class-itemlist-property-item-count)

- void **set_item_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_item_count**()

The number of items currently in the list.

---


<a id="class-itemlist-property-item-index-disabled"></a>

[bool](class_bool.md#class-bool) **item_{index}/disabled** = `false` [🔗](class_itemlist.md#class-itemlist-property-item-index-disabled)

If `true`, the item at `index` is disabled.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

---


<a id="class-itemlist-property-item-index-icon"></a>

[Texture2D](class_texture2d.md#class-texture2d) **item_{index}/icon** [🔗](class_itemlist.md#class-itemlist-property-item-index-icon)

The icon of the item at `index`.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

---


<a id="class-itemlist-property-item-index-selectable"></a>

[bool](class_bool.md#class-bool) **item_{index}/selectable** = `true` [🔗](class_itemlist.md#class-itemlist-property-item-index-selectable)

If `true`, the item at `index` is selectable.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

---


<a id="class-itemlist-property-item-index-text"></a>

[String](class_string.md#class-string) **item_{index}/text** = `""` [🔗](class_itemlist.md#class-itemlist-property-item-index-text)

The text of the item at `index`.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

---


<a id="class-itemlist-property-max-columns"></a>

[int](class_int.md#class-int) **max_columns** = `1` [🔗](class_itemlist.md#class-itemlist-property-max-columns)

- void **set_max_columns**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_max_columns**()

Maximum columns the list will have.

If greater than zero, the content will be split among the specified columns.

A value of zero means unlimited columns, i.e. all items will be put in the same row.

---


<a id="class-itemlist-property-max-text-lines"></a>

[int](class_int.md#class-int) **max_text_lines** = `1` [🔗](class_itemlist.md#class-itemlist-property-max-text-lines)

- void **set_max_text_lines**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_max_text_lines**()

Maximum lines of text allowed in each item. Space will be reserved even when there is not enough lines of text to display.

**Note:** This property takes effect only when [icon_mode](class_itemlist.md#class-itemlist-property-icon-mode) is [ICON_MODE_TOP](class_itemlist.md#class-itemlist-constant-icon-mode-top). To make the text wrap, [fixed_column_width](class_itemlist.md#class-itemlist-property-fixed-column-width) should be greater than zero.

---


<a id="class-itemlist-property-same-column-width"></a>

[bool](class_bool.md#class-bool) **same_column_width** = `false` [🔗](class_itemlist.md#class-itemlist-property-same-column-width)

- void **set_same_column_width**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_same_column_width**()

Whether all columns will have the same width.

If `true`, the width is equal to the largest column width of all columns.

---


<a id="class-itemlist-property-scroll-hint-mode"></a>

[ScrollHintMode](class_itemlist.md#enum-itemlist-scrollhintmode) **scroll_hint_mode** = `0` [🔗](class_itemlist.md#class-itemlist-property-scroll-hint-mode)

- void **set_scroll_hint_mode**(value: [ScrollHintMode](class_itemlist.md#enum-itemlist-scrollhintmode))
- [ScrollHintMode](class_itemlist.md#enum-itemlist-scrollhintmode) **get_scroll_hint_mode**()

The way which scroll hints (indicators that show that the content can still be scrolled in a certain direction) will be shown.

---


<a id="class-itemlist-property-select-mode"></a>

[SelectMode](class_itemlist.md#enum-itemlist-selectmode) **select_mode** = `0` [🔗](class_itemlist.md#class-itemlist-property-select-mode)

- void **set_select_mode**(value: [SelectMode](class_itemlist.md#enum-itemlist-selectmode))
- [SelectMode](class_itemlist.md#enum-itemlist-selectmode) **get_select_mode**()

Allows single or multiple item selection. See the [SelectMode](class_itemlist.md#enum-itemlist-selectmode) constants.

---


<a id="class-itemlist-property-text-overrun-behavior"></a>

[OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior) **text_overrun_behavior** = `3` [🔗](class_itemlist.md#class-itemlist-property-text-overrun-behavior)

- void **set_text_overrun_behavior**(value: [OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior))
- [OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior) **get_text_overrun_behavior**()

The clipping behavior when the text exceeds an item's bounding rectangle.

---


<a id="class-itemlist-property-tile-scroll-hint"></a>

[bool](class_bool.md#class-bool) **tile_scroll_hint** = `false` [🔗](class_itemlist.md#class-itemlist-property-tile-scroll-hint)

- void **set_tile_scroll_hint**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_scroll_hint_tiled**()

If `true`, the scroll hint texture will be tiled instead of stretched. See [scroll_hint_mode](class_itemlist.md#class-itemlist-property-scroll-hint-mode).

---


<a id="class-itemlist-property-wraparound-items"></a>

[bool](class_bool.md#class-bool) **wraparound_items** = `true` [🔗](class_itemlist.md#class-itemlist-property-wraparound-items)

- void **set_wraparound_items**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **has_wraparound_items**()

If `true`, the control will automatically move items into a new row to fit its content. See also [HFlowContainer](class_hflowcontainer.md#class-hflowcontainer) for this behavior.

If `false`, the control will add a horizontal scrollbar to make all items visible.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-itemlist-method-add-icon-item"></a>

[int](class_int.md#class-int) **add_icon_item**(icon: [Texture2D](class_texture2d.md#class-texture2d), selectable: [bool](class_bool.md#class-bool) = true) [🔗](class_itemlist.md#class-itemlist-method-add-icon-item)

Adds an item to the item list with no text, only an icon. Returns the index of an added item.

---


<a id="class-itemlist-method-add-item"></a>

[int](class_int.md#class-int) **add_item**(text: [String](class_string.md#class-string), icon: [Texture2D](class_texture2d.md#class-texture2d) = null, selectable: [bool](class_bool.md#class-bool) = true) [🔗](class_itemlist.md#class-itemlist-method-add-item)

Adds an item to the item list with specified text. Returns the index of an added item.

Specify an `icon`, or use `null` as the `icon` for a list item with no icon.

If `selectable` is `true`, the list item will be selectable.

---


<a id="class-itemlist-method-center-on-current"></a>

void **center_on_current**(center_verically: [bool](class_bool.md#class-bool) = true, center_horizontally: [bool](class_bool.md#class-bool) = true) [🔗](class_itemlist.md#class-itemlist-method-center-on-current)

Ensures the currently selected item (the first selected item if multiple selection is enabled) is visible, adjusting the scroll position as necessary to place the item at the center of the list if possible. See also [ensure_current_is_visible()](class_itemlist.md#class-itemlist-method-ensure-current-is-visible).

Fails and prints an error if both arguments are `false`.

---


<a id="class-itemlist-method-clear"></a>

void **clear**() [🔗](class_itemlist.md#class-itemlist-method-clear)

Removes all items from the list.

---


<a id="class-itemlist-method-deselect"></a>

void **deselect**(idx: [int](class_int.md#class-int)) [🔗](class_itemlist.md#class-itemlist-method-deselect)

Ensures the item associated with the specified index is not selected.

---


<a id="class-itemlist-method-deselect-all"></a>

void **deselect_all**() [🔗](class_itemlist.md#class-itemlist-method-deselect-all)

Ensures there are no items selected.

---


<a id="class-itemlist-method-ensure-current-is-visible"></a>

void **ensure_current_is_visible**() [🔗](class_itemlist.md#class-itemlist-method-ensure-current-is-visible)

Ensures the currently selected item (the first selected item if multiple selection is enabled) is visible, adjusting the scroll position as necessary. See also [center_on_current()](class_itemlist.md#class-itemlist-method-center-on-current).

---


<a id="class-itemlist-method-force-update-list-size"></a>

void **force_update_list_size**() [🔗](class_itemlist.md#class-itemlist-method-force-update-list-size)

Forces an update to the list size based on its items. This happens automatically whenever size of the items, or other relevant settings like [auto_height](class_itemlist.md#class-itemlist-property-auto-height), change. The method can be used to trigger the update ahead of next drawing pass.

---


<a id="class-itemlist-method-get-h-scroll-bar"></a>

[HScrollBar](class_hscrollbar.md#class-hscrollbar) **get_h_scroll_bar**() [🔗](class_itemlist.md#class-itemlist-method-get-h-scroll-bar)

Returns the horizontal scrollbar.

**Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [CanvasItem.visible](class_canvasitem.md#class-canvasitem-property-visible) property.

---


<a id="class-itemlist-method-get-item-at-position"></a>

[int](class_int.md#class-int) **get_item_at_position**(position: [Vector2](class_vector2.md#class-vector2), exact: [bool](class_bool.md#class-bool) = false) const [🔗](class_itemlist.md#class-itemlist-method-get-item-at-position)

Returns the item index at the given `position`.

When there is no item at that point, -1 will be returned if `exact` is `true`, and the closest item index will be returned otherwise.

**Note:** The returned value is unreliable if called right after modifying the **ItemList**, before it redraws in the next frame.

---


<a id="class-itemlist-method-get-item-auto-translate-mode"></a>

[AutoTranslateMode](class_node.md#enum-node-autotranslatemode) **get_item_auto_translate_mode**(idx: [int](class_int.md#class-int)) const [🔗](class_itemlist.md#class-itemlist-method-get-item-auto-translate-mode)

Returns item's auto translate mode.

---


<a id="class-itemlist-method-get-item-custom-bg-color"></a>

[Color](class_color.md#class-color) **get_item_custom_bg_color**(idx: [int](class_int.md#class-int)) const [🔗](class_itemlist.md#class-itemlist-method-get-item-custom-bg-color)

Returns the custom background color of the item specified by `idx` index.

---


<a id="class-itemlist-method-get-item-custom-fg-color"></a>

[Color](class_color.md#class-color) **get_item_custom_fg_color**(idx: [int](class_int.md#class-int)) const [🔗](class_itemlist.md#class-itemlist-method-get-item-custom-fg-color)

Returns the custom foreground color of the item specified by `idx` index.

---


<a id="class-itemlist-method-get-item-icon"></a>

[Texture2D](class_texture2d.md#class-texture2d) **get_item_icon**(idx: [int](class_int.md#class-int)) const [🔗](class_itemlist.md#class-itemlist-method-get-item-icon)

Returns the icon associated with the specified index.

---


<a id="class-itemlist-method-get-item-icon-modulate"></a>

[Color](class_color.md#class-color) **get_item_icon_modulate**(idx: [int](class_int.md#class-int)) const [🔗](class_itemlist.md#class-itemlist-method-get-item-icon-modulate)

Returns a [Color](class_color.md#class-color) modulating item's icon at the specified index.

---


<a id="class-itemlist-method-get-item-icon-region"></a>

[Rect2](class_rect2.md#class-rect2) **get_item_icon_region**(idx: [int](class_int.md#class-int)) const [🔗](class_itemlist.md#class-itemlist-method-get-item-icon-region)

Returns the region of item's icon used. The whole icon will be used if the region has no area.

---


<a id="class-itemlist-method-get-item-language"></a>

[String](class_string.md#class-string) **get_item_language**(idx: [int](class_int.md#class-int)) const [🔗](class_itemlist.md#class-itemlist-method-get-item-language)

Returns item's text language code.

---


<a id="class-itemlist-method-get-item-metadata"></a>

[Variant](class_variant.md#class-variant) **get_item_metadata**(idx: [int](class_int.md#class-int)) const [🔗](class_itemlist.md#class-itemlist-method-get-item-metadata)

Returns the metadata value of the specified index.

---


<a id="class-itemlist-method-get-item-rect"></a>

[Rect2](class_rect2.md#class-rect2) **get_item_rect**(idx: [int](class_int.md#class-int), expand: [bool](class_bool.md#class-bool) = true) const [🔗](class_itemlist.md#class-itemlist-method-get-item-rect)

Returns the position and size of the item with the specified index, in the coordinate system of the **ItemList** node. If `expand` is `true` the last column expands to fill the rest of the row.

**Note:** The returned value is unreliable if called right after modifying the **ItemList**, before it redraws in the next frame.

---


<a id="class-itemlist-method-get-item-text"></a>

[String](class_string.md#class-string) **get_item_text**(idx: [int](class_int.md#class-int)) const [🔗](class_itemlist.md#class-itemlist-method-get-item-text)

Returns the text associated with the specified index.

---


<a id="class-itemlist-method-get-item-text-direction"></a>

[TextDirection](class_control.md#enum-control-textdirection) **get_item_text_direction**(idx: [int](class_int.md#class-int)) const [🔗](class_itemlist.md#class-itemlist-method-get-item-text-direction)

Returns item's text base writing direction.

---


<a id="class-itemlist-method-get-item-tooltip"></a>

[String](class_string.md#class-string) **get_item_tooltip**(idx: [int](class_int.md#class-int)) const [🔗](class_itemlist.md#class-itemlist-method-get-item-tooltip)

Returns the tooltip hint associated with the specified index.

---


<a id="class-itemlist-method-get-selected-items"></a>

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_selected_items**() [🔗](class_itemlist.md#class-itemlist-method-get-selected-items)

Returns an array with the indexes of the selected items.

---


<a id="class-itemlist-method-get-v-scroll-bar"></a>

[VScrollBar](class_vscrollbar.md#class-vscrollbar) **get_v_scroll_bar**() [🔗](class_itemlist.md#class-itemlist-method-get-v-scroll-bar)

Returns the vertical scrollbar.

**Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [CanvasItem.visible](class_canvasitem.md#class-canvasitem-property-visible) property.

---


<a id="class-itemlist-method-is-anything-selected"></a>

[bool](class_bool.md#class-bool) **is_anything_selected**() [🔗](class_itemlist.md#class-itemlist-method-is-anything-selected)

Returns `true` if one or more items are selected.

---


<a id="class-itemlist-method-is-item-disabled"></a>

[bool](class_bool.md#class-bool) **is_item_disabled**(idx: [int](class_int.md#class-int)) const [🔗](class_itemlist.md#class-itemlist-method-is-item-disabled)

Returns `true` if the item at the specified index is disabled.

---


<a id="class-itemlist-method-is-item-icon-transposed"></a>

[bool](class_bool.md#class-bool) **is_item_icon_transposed**(idx: [int](class_int.md#class-int)) const [🔗](class_itemlist.md#class-itemlist-method-is-item-icon-transposed)

Returns `true` if the item icon will be drawn transposed, i.e. the X and Y axes are swapped.

---


<a id="class-itemlist-method-is-item-selectable"></a>

[bool](class_bool.md#class-bool) **is_item_selectable**(idx: [int](class_int.md#class-int)) const [🔗](class_itemlist.md#class-itemlist-method-is-item-selectable)

Returns `true` if the item at the specified index is selectable.

---


<a id="class-itemlist-method-is-item-tooltip-enabled"></a>

[bool](class_bool.md#class-bool) **is_item_tooltip_enabled**(idx: [int](class_int.md#class-int)) const [🔗](class_itemlist.md#class-itemlist-method-is-item-tooltip-enabled)

Returns `true` if the tooltip is enabled for specified item index.

---


<a id="class-itemlist-method-is-selected"></a>

[bool](class_bool.md#class-bool) **is_selected**(idx: [int](class_int.md#class-int)) const [🔗](class_itemlist.md#class-itemlist-method-is-selected)

Returns `true` if the item at the specified index is currently selected.

---


<a id="class-itemlist-method-move-item"></a>

void **move_item**(from_idx: [int](class_int.md#class-int), to_idx: [int](class_int.md#class-int)) [🔗](class_itemlist.md#class-itemlist-method-move-item)

Moves item from index `from_idx` to `to_idx`.

---


<a id="class-itemlist-method-remove-item"></a>

void **remove_item**(idx: [int](class_int.md#class-int)) [🔗](class_itemlist.md#class-itemlist-method-remove-item)

Removes the item specified by `idx` index from the list.

---


<a id="class-itemlist-method-select"></a>

void **select**(idx: [int](class_int.md#class-int), single: [bool](class_bool.md#class-bool) = true) [🔗](class_itemlist.md#class-itemlist-method-select)

Selects the item at the specified index.

**Note:** This method does not trigger the item selection signal.

---


<a id="class-itemlist-method-set-item-auto-translate-mode"></a>

void **set_item_auto_translate_mode**(idx: [int](class_int.md#class-int), mode: [AutoTranslateMode](class_node.md#enum-node-autotranslatemode)) [🔗](class_itemlist.md#class-itemlist-method-set-item-auto-translate-mode)

Sets the auto translate mode of the item associated with the specified index.

Items use [Node.AUTO_TRANSLATE_MODE_INHERIT](class_node.md#class-node-constant-auto-translate-mode-inherit) by default, which uses the same auto translate mode as the **ItemList** itself.

---


<a id="class-itemlist-method-set-item-custom-bg-color"></a>

void **set_item_custom_bg_color**(idx: [int](class_int.md#class-int), custom_bg_color: [Color](class_color.md#class-color)) [🔗](class_itemlist.md#class-itemlist-method-set-item-custom-bg-color)

Sets the background color of the item specified by `idx` index to the specified [Color](class_color.md#class-color).

---


<a id="class-itemlist-method-set-item-custom-fg-color"></a>

void **set_item_custom_fg_color**(idx: [int](class_int.md#class-int), custom_fg_color: [Color](class_color.md#class-color)) [🔗](class_itemlist.md#class-itemlist-method-set-item-custom-fg-color)

Sets the foreground color of the item specified by `idx` index to the specified [Color](class_color.md#class-color).

---


<a id="class-itemlist-method-set-item-disabled"></a>

void **set_item_disabled**(idx: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool)) [🔗](class_itemlist.md#class-itemlist-method-set-item-disabled)

Disables (or enables) the item at the specified index.

Disabled items cannot be selected and do not trigger activation signals (when double-clicking or pressing `Enter`).

---


<a id="class-itemlist-method-set-item-icon"></a>

void **set_item_icon**(idx: [int](class_int.md#class-int), icon: [Texture2D](class_texture2d.md#class-texture2d)) [🔗](class_itemlist.md#class-itemlist-method-set-item-icon)

Sets (or replaces) the icon's [Texture2D](class_texture2d.md#class-texture2d) associated with the specified index.

---


<a id="class-itemlist-method-set-item-icon-modulate"></a>

void **set_item_icon_modulate**(idx: [int](class_int.md#class-int), modulate: [Color](class_color.md#class-color)) [🔗](class_itemlist.md#class-itemlist-method-set-item-icon-modulate)

Sets a modulating [Color](class_color.md#class-color) of the item associated with the specified index.

---


<a id="class-itemlist-method-set-item-icon-region"></a>

void **set_item_icon_region**(idx: [int](class_int.md#class-int), rect: [Rect2](class_rect2.md#class-rect2)) [🔗](class_itemlist.md#class-itemlist-method-set-item-icon-region)

Sets the region of item's icon used. The whole icon will be used if the region has no area.

---


<a id="class-itemlist-method-set-item-icon-transposed"></a>

void **set_item_icon_transposed**(idx: [int](class_int.md#class-int), transposed: [bool](class_bool.md#class-bool)) [🔗](class_itemlist.md#class-itemlist-method-set-item-icon-transposed)

Sets whether the item icon will be drawn transposed.

---


<a id="class-itemlist-method-set-item-language"></a>

void **set_item_language**(idx: [int](class_int.md#class-int), language: [String](class_string.md#class-string)) [🔗](class_itemlist.md#class-itemlist-method-set-item-language)

Sets the language code of the text for the item at the given index to `language`. This is used for line-breaking and text shaping algorithms. If `language` is empty, the current locale is used.

---


<a id="class-itemlist-method-set-item-metadata"></a>

void **set_item_metadata**(idx: [int](class_int.md#class-int), metadata: [Variant](class_variant.md#class-variant)) [🔗](class_itemlist.md#class-itemlist-method-set-item-metadata)

Sets a value (of any type) to be stored with the item associated with the specified index.

---


<a id="class-itemlist-method-set-item-selectable"></a>

void **set_item_selectable**(idx: [int](class_int.md#class-int), selectable: [bool](class_bool.md#class-bool)) [🔗](class_itemlist.md#class-itemlist-method-set-item-selectable)

Allows or disallows selection of the item associated with the specified index.

---


<a id="class-itemlist-method-set-item-text"></a>

void **set_item_text**(idx: [int](class_int.md#class-int), text: [String](class_string.md#class-string)) [🔗](class_itemlist.md#class-itemlist-method-set-item-text)

Sets text of the item associated with the specified index.

---


<a id="class-itemlist-method-set-item-text-direction"></a>

void **set_item_text_direction**(idx: [int](class_int.md#class-int), direction: [TextDirection](class_control.md#enum-control-textdirection)) [🔗](class_itemlist.md#class-itemlist-method-set-item-text-direction)

Sets item's text base writing direction.

---


<a id="class-itemlist-method-set-item-tooltip"></a>

void **set_item_tooltip**(idx: [int](class_int.md#class-int), tooltip: [String](class_string.md#class-string)) [🔗](class_itemlist.md#class-itemlist-method-set-item-tooltip)

Sets the tooltip hint for the item associated with the specified index.

---


<a id="class-itemlist-method-set-item-tooltip-enabled"></a>

void **set_item_tooltip_enabled**(idx: [int](class_int.md#class-int), enable: [bool](class_bool.md#class-bool)) [🔗](class_itemlist.md#class-itemlist-method-set-item-tooltip-enabled)

Sets whether the tooltip hint is enabled for specified item index.

---


<a id="class-itemlist-method-sort-items-by-text"></a>

void **sort_items_by_text**() [🔗](class_itemlist.md#class-itemlist-method-sort-items-by-text)

Sorts items in the list by their text.

---


<a id="theme-property-descriptions"></a>

## Theme Property Descriptions

<a id="class-itemlist-theme-color-font-color"></a>

[Color](class_color.md#class-color) **font_color** = `Color(0.65, 0.65, 0.65, 1)` [🔗](class_itemlist.md#class-itemlist-theme-color-font-color)

Default text [Color](class_color.md#class-color) of the item.

---


<a id="class-itemlist-theme-color-font-hovered-color"></a>

[Color](class_color.md#class-color) **font_hovered_color** = `Color(0.95, 0.95, 0.95, 1)` [🔗](class_itemlist.md#class-itemlist-theme-color-font-hovered-color)

Text [Color](class_color.md#class-color) used when the item is hovered and not selected yet.

---


<a id="class-itemlist-theme-color-font-hovered-selected-color"></a>

[Color](class_color.md#class-color) **font_hovered_selected_color** = `Color(1, 1, 1, 1)` [🔗](class_itemlist.md#class-itemlist-theme-color-font-hovered-selected-color)

Text [Color](class_color.md#class-color) used when the item is hovered and selected.

---


<a id="class-itemlist-theme-color-font-outline-color"></a>

[Color](class_color.md#class-color) **font_outline_color** = `Color(0, 0, 0, 1)` [🔗](class_itemlist.md#class-itemlist-theme-color-font-outline-color)

The tint of text outline of the item.

---


<a id="class-itemlist-theme-color-font-selected-color"></a>

[Color](class_color.md#class-color) **font_selected_color** = `Color(1, 1, 1, 1)` [🔗](class_itemlist.md#class-itemlist-theme-color-font-selected-color)

Text [Color](class_color.md#class-color) used when the item is selected, but not hovered.

---


<a id="class-itemlist-theme-color-guide-color"></a>

[Color](class_color.md#class-color) **guide_color** = `Color(0.7, 0.7, 0.7, 0.25)` [🔗](class_itemlist.md#class-itemlist-theme-color-guide-color)

[Color](class_color.md#class-color) of the guideline. The guideline is a line drawn between each row of items.

---


<a id="class-itemlist-theme-color-scroll-hint-color"></a>

[Color](class_color.md#class-color) **scroll_hint_color** = `Color(0, 0, 0, 1)` [🔗](class_itemlist.md#class-itemlist-theme-color-scroll-hint-color)

[Color](class_color.md#class-color) used to modulate the [scroll_hint](class_itemlist.md#class-itemlist-theme-icon-scroll-hint) texture.

---


<a id="class-itemlist-theme-constant-h-separation"></a>

[int](class_int.md#class-int) **h_separation** = `4` [🔗](class_itemlist.md#class-itemlist-theme-constant-h-separation)

The horizontal spacing between items.

---


<a id="class-itemlist-theme-constant-icon-margin"></a>

[int](class_int.md#class-int) **icon_margin** = `4` [🔗](class_itemlist.md#class-itemlist-theme-constant-icon-margin)

The spacing between item's icon and text.

---


<a id="class-itemlist-theme-constant-line-separation"></a>

[int](class_int.md#class-int) **line_separation** = `2` [🔗](class_itemlist.md#class-itemlist-theme-constant-line-separation)

The vertical spacing between each line of text.

---


<a id="class-itemlist-theme-constant-outline-size"></a>

[int](class_int.md#class-int) **outline_size** = `0` [🔗](class_itemlist.md#class-itemlist-theme-constant-outline-size)

The size of the item text outline.

**Note:** If using a font with [FontFile.multichannel_signed_distance_field](class_fontfile.md#class-fontfile-property-multichannel-signed-distance-field) enabled, its [FontFile.msdf_pixel_range](class_fontfile.md#class-fontfile-property-msdf-pixel-range) must be set to at least *twice* the value of [outline_size](class_itemlist.md#class-itemlist-theme-constant-outline-size) for outline rendering to look correct. Otherwise, the outline may appear to be cut off earlier than intended.

---


<a id="class-itemlist-theme-constant-v-separation"></a>

[int](class_int.md#class-int) **v_separation** = `4` [🔗](class_itemlist.md#class-itemlist-theme-constant-v-separation)

The vertical spacing between items.

---


<a id="class-itemlist-theme-font-font"></a>

[Font](class_font.md#class-font) **font** [🔗](class_itemlist.md#class-itemlist-theme-font-font)

[Font](class_font.md#class-font) of the item's text.

---


<a id="class-itemlist-theme-font-size-font-size"></a>

[int](class_int.md#class-int) **font_size** [🔗](class_itemlist.md#class-itemlist-theme-font-size-font-size)

Font size of the item's text.

---


<a id="class-itemlist-theme-icon-scroll-hint"></a>

[Texture2D](class_texture2d.md#class-texture2d) **scroll_hint** [🔗](class_itemlist.md#class-itemlist-theme-icon-scroll-hint)

The indicator that will be shown when the content can still be scrolled. See [scroll_hint_mode](class_itemlist.md#class-itemlist-property-scroll-hint-mode).

---


<a id="class-itemlist-theme-style-cursor"></a>

[StyleBox](class_stylebox.md#class-stylebox) **cursor** [🔗](class_itemlist.md#class-itemlist-theme-style-cursor)

[StyleBox](class_stylebox.md#class-stylebox) used for the cursor, when the **ItemList** is being focused.

---


<a id="class-itemlist-theme-style-cursor-unfocused"></a>

[StyleBox](class_stylebox.md#class-stylebox) **cursor_unfocused** [🔗](class_itemlist.md#class-itemlist-theme-style-cursor-unfocused)

[StyleBox](class_stylebox.md#class-stylebox) used for the cursor, when the **ItemList** is not being focused.

---


<a id="class-itemlist-theme-style-focus"></a>

[StyleBox](class_stylebox.md#class-stylebox) **focus** [🔗](class_itemlist.md#class-itemlist-theme-style-focus)

The focused style for the **ItemList**, drawn on top of everything.

---


<a id="class-itemlist-theme-style-hovered"></a>

[StyleBox](class_stylebox.md#class-stylebox) **hovered** [🔗](class_itemlist.md#class-itemlist-theme-style-hovered)

[StyleBox](class_stylebox.md#class-stylebox) for the hovered, but not selected items.

---


<a id="class-itemlist-theme-style-hovered-selected"></a>

[StyleBox](class_stylebox.md#class-stylebox) **hovered_selected** [🔗](class_itemlist.md#class-itemlist-theme-style-hovered-selected)

[StyleBox](class_stylebox.md#class-stylebox) for the hovered and selected items, used when the **ItemList** is not being focused.

---


<a id="class-itemlist-theme-style-hovered-selected-focus"></a>

[StyleBox](class_stylebox.md#class-stylebox) **hovered_selected_focus** [🔗](class_itemlist.md#class-itemlist-theme-style-hovered-selected-focus)

[StyleBox](class_stylebox.md#class-stylebox) for the hovered and selected items, used when the **ItemList** is being focused.

---


<a id="class-itemlist-theme-style-panel"></a>

[StyleBox](class_stylebox.md#class-stylebox) **panel** [🔗](class_itemlist.md#class-itemlist-theme-style-panel)

The background style for the **ItemList**.

---


<a id="class-itemlist-theme-style-selected"></a>

[StyleBox](class_stylebox.md#class-stylebox) **selected** [🔗](class_itemlist.md#class-itemlist-theme-style-selected)

[StyleBox](class_stylebox.md#class-stylebox) for the selected items, used when the **ItemList** is not being focused.

---


<a id="class-itemlist-theme-style-selected-focus"></a>

[StyleBox](class_stylebox.md#class-stylebox) **selected_focus** [🔗](class_itemlist.md#class-itemlist-theme-style-selected-focus)

[StyleBox](class_stylebox.md#class-stylebox) for the selected items, used when the **ItemList** is being focused.
