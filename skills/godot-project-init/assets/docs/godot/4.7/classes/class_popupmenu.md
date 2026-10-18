> Source: https://docs.godotengine.org/en/4.7/classes/class_popupmenu.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="popupmenu"></a>

<a id="class-popupmenu"></a>

# PopupMenu

**Inherits:** [Popup](class_popup.md#class-popup) **<** [Window](class_window.md#class-window) **<** [Viewport](class_viewport.md#class-viewport) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A modal window used to display a list of options.

<a id="description"></a>

## Description

**PopupMenu** is a modal window used to display a list of options. Useful for toolbars and context menus.

The size of a **PopupMenu** can be limited by using [Window.max_size](class_window.md#class-window-property-max-size). If the height of the list of items is larger than the maximum height of the **PopupMenu**, a [ScrollContainer](class_scrollcontainer.md#class-scrollcontainer) within the popup will allow the user to scroll the contents. If no maximum size is set, or if it is set to `0`, the **PopupMenu** height will be limited by its parent rect.

All `set_*` methods allow negative item indices, i.e. `-1` to access the last item, `-2` to select the second-to-last item, and so on.

**Incremental search:** Like [ItemList](class_itemlist.md#class-itemlist) and [Tree](class_tree.md#class-tree), **PopupMenu** supports searching within the list while the control is focused. Press a key that matches the first letter of an item's name to select the first item starting with the given letter. After that point, there are two ways to perform incremental search: 1) Press the same key again before the timeout duration to select the next item starting with the same letter. 2) Press letter keys that match the rest of the word before the timeout duration to match to select the item in question directly. Both of these actions will be reset to the beginning of the list if the timeout duration has passed since the last keystroke was registered. You can adjust the timeout duration by changing [ProjectSettings.gui/timers/incremental_search_max_interval_msec](class_projectsettings.md#class-projectsettings-property-gui-timers-incremental-search-max-interval-msec).

**Note:** **PopupMenu** is invisible by default. To make it visible, call one of the `popup_*` methods from [Window](class_window.md#class-window) on the node, such as [Window.popup_centered_clamped()](class_window.md#class-window-method-popup-centered-clamped).

**Note:** The ID values used for items are limited to 32 bits, not full 64 bits of [int](class_int.md#class-int). This has a range of `-2^32` to `2^32 - 1`, i.e. `-2147483648` to `2147483647`.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [allow_search](class_popupmenu.md#class-popupmenu-property-allow-search) | `true` |
| [DefaultCanvasItemTextureFilter](class_viewport.md#enum-viewport-defaultcanvasitemtexturefilter) | canvas_item_default_texture_filter | `4` (overrides [Viewport](class_viewport.md#class-viewport-property-canvas-item-default-texture-filter)) |
| [DefaultCanvasItemTextureRepeat](class_viewport.md#enum-viewport-defaultcanvasitemtexturerepeat) | canvas_item_default_texture_repeat | `3` (overrides [Viewport](class_viewport.md#class-viewport-property-canvas-item-default-texture-repeat)) |
| [bool](class_bool.md#class-bool) | [hide_on_checkable_item_selection](class_popupmenu.md#class-popupmenu-property-hide-on-checkable-item-selection) | `true` |
| [bool](class_bool.md#class-bool) | [hide_on_item_selection](class_popupmenu.md#class-popupmenu-property-hide-on-item-selection) | `true` |
| [bool](class_bool.md#class-bool) | [hide_on_state_item_selection](class_popupmenu.md#class-popupmenu-property-hide-on-state-item-selection) | `false` |
| [int](class_int.md#class-int) | [item_count](class_popupmenu.md#class-popupmenu-property-item-count) | `0` |
| [int](class_int.md#class-int) | [item_{index}/checkable](class_popupmenu.md#class-popupmenu-property-item-index-checkable) | `0` |
| [bool](class_bool.md#class-bool) | [item_{index}/checked](class_popupmenu.md#class-popupmenu-property-item-index-checked) | `false` |
| [bool](class_bool.md#class-bool) | [item_{index}/disabled](class_popupmenu.md#class-popupmenu-property-item-index-disabled) | `false` |
| [Texture2D](class_texture2d.md#class-texture2d) | [item_{index}/icon](class_popupmenu.md#class-popupmenu-property-item-index-icon) |  |
| [int](class_int.md#class-int) | [item_{index}/id](class_popupmenu.md#class-popupmenu-property-item-index-id) | `0` |
| [bool](class_bool.md#class-bool) | [item_{index}/separator](class_popupmenu.md#class-popupmenu-property-item-index-separator) | `false` |
| [String](class_string.md#class-string) | [item_{index}/text](class_popupmenu.md#class-popupmenu-property-item-index-text) | `""` |
| [bool](class_bool.md#class-bool) | [prefer_native_menu](class_popupmenu.md#class-popupmenu-property-prefer-native-menu) | `false` |
| [bool](class_bool.md#class-bool) | [search_bar_enabled](class_popupmenu.md#class-popupmenu-property-search-bar-enabled) | `false` |
| [bool](class_bool.md#class-bool) | [search_bar_fuzzy_search_enabled](class_popupmenu.md#class-popupmenu-property-search-bar-fuzzy-search-enabled) | `true` |
| [int](class_int.md#class-int) | [search_bar_fuzzy_search_max_misses](class_popupmenu.md#class-popupmenu-property-search-bar-fuzzy-search-max-misses) | `2` |
| [int](class_int.md#class-int) | [search_bar_min_item_count](class_popupmenu.md#class-popupmenu-property-search-bar-min-item-count) | `0` |
| [bool](class_bool.md#class-bool) | [shrink_height](class_popupmenu.md#class-popupmenu-property-shrink-height) | `true` |
| [bool](class_bool.md#class-bool) | [shrink_width](class_popupmenu.md#class-popupmenu-property-shrink-width) | `true` |
| [float](class_float.md#class-float) | [submenu_popup_delay](class_popupmenu.md#class-popupmenu-property-submenu-popup-delay) | `0.2` |
| [SystemMenus](class_nativemenu.md#enum-nativemenu-systemmenus) | [system_menu_id](class_popupmenu.md#class-popupmenu-property-system-menu-id) | `0` |
| [bool](class_bool.md#class-bool) | transparent | `true` (overrides [Window](class_window.md#class-window-property-transparent)) |
| [bool](class_bool.md#class-bool) | transparent_bg | `true` (overrides [Viewport](class_viewport.md#class-viewport-property-transparent-bg)) |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [activate_item_by_event](class_popupmenu.md#class-popupmenu-method-activate-item-by-event)(event: [InputEvent](class_inputevent.md#class-inputevent), for_global_only: [bool](class_bool.md#class-bool) = false) |
| void | [add_check_item](class_popupmenu.md#class-popupmenu-method-add-check-item)(label: [String](class_string.md#class-string), id: [int](class_int.md#class-int) = -1, accel: [Key](class_@globalscope.md#enum-globalscope-key) = 0) |
| void | [add_check_shortcut](class_popupmenu.md#class-popupmenu-method-add-check-shortcut)(shortcut: [Shortcut](class_shortcut.md#class-shortcut), id: [int](class_int.md#class-int) = -1, global: [bool](class_bool.md#class-bool) = false) |
| void | [add_icon_check_item](class_popupmenu.md#class-popupmenu-method-add-icon-check-item)(texture: [Texture2D](class_texture2d.md#class-texture2d), label: [String](class_string.md#class-string), id: [int](class_int.md#class-int) = -1, accel: [Key](class_@globalscope.md#enum-globalscope-key) = 0) |
| void | [add_icon_check_shortcut](class_popupmenu.md#class-popupmenu-method-add-icon-check-shortcut)(texture: [Texture2D](class_texture2d.md#class-texture2d), shortcut: [Shortcut](class_shortcut.md#class-shortcut), id: [int](class_int.md#class-int) = -1, global: [bool](class_bool.md#class-bool) = false) |
| void | [add_icon_item](class_popupmenu.md#class-popupmenu-method-add-icon-item)(texture: [Texture2D](class_texture2d.md#class-texture2d), label: [String](class_string.md#class-string), id: [int](class_int.md#class-int) = -1, accel: [Key](class_@globalscope.md#enum-globalscope-key) = 0) |
| void | [add_icon_radio_check_item](class_popupmenu.md#class-popupmenu-method-add-icon-radio-check-item)(texture: [Texture2D](class_texture2d.md#class-texture2d), label: [String](class_string.md#class-string), id: [int](class_int.md#class-int) = -1, accel: [Key](class_@globalscope.md#enum-globalscope-key) = 0) |
| void | [add_icon_radio_check_shortcut](class_popupmenu.md#class-popupmenu-method-add-icon-radio-check-shortcut)(texture: [Texture2D](class_texture2d.md#class-texture2d), shortcut: [Shortcut](class_shortcut.md#class-shortcut), id: [int](class_int.md#class-int) = -1, global: [bool](class_bool.md#class-bool) = false) |
| void | [add_icon_shortcut](class_popupmenu.md#class-popupmenu-method-add-icon-shortcut)(texture: [Texture2D](class_texture2d.md#class-texture2d), shortcut: [Shortcut](class_shortcut.md#class-shortcut), id: [int](class_int.md#class-int) = -1, global: [bool](class_bool.md#class-bool) = false, allow_echo: [bool](class_bool.md#class-bool) = false) |
| void | [add_item](class_popupmenu.md#class-popupmenu-method-add-item)(label: [String](class_string.md#class-string), id: [int](class_int.md#class-int) = -1, accel: [Key](class_@globalscope.md#enum-globalscope-key) = 0) |
| void | [add_multistate_item](class_popupmenu.md#class-popupmenu-method-add-multistate-item)(label: [String](class_string.md#class-string), max_states: [int](class_int.md#class-int), default_state: [int](class_int.md#class-int) = 0, id: [int](class_int.md#class-int) = -1, accel: [Key](class_@globalscope.md#enum-globalscope-key) = 0) |
| void | [add_radio_check_item](class_popupmenu.md#class-popupmenu-method-add-radio-check-item)(label: [String](class_string.md#class-string), id: [int](class_int.md#class-int) = -1, accel: [Key](class_@globalscope.md#enum-globalscope-key) = 0) |
| void | [add_radio_check_shortcut](class_popupmenu.md#class-popupmenu-method-add-radio-check-shortcut)(shortcut: [Shortcut](class_shortcut.md#class-shortcut), id: [int](class_int.md#class-int) = -1, global: [bool](class_bool.md#class-bool) = false) |
| void | [add_separator](class_popupmenu.md#class-popupmenu-method-add-separator)(label: [String](class_string.md#class-string) = "", id: [int](class_int.md#class-int) = -1) |
| void | [add_shortcut](class_popupmenu.md#class-popupmenu-method-add-shortcut)(shortcut: [Shortcut](class_shortcut.md#class-shortcut), id: [int](class_int.md#class-int) = -1, global: [bool](class_bool.md#class-bool) = false, allow_echo: [bool](class_bool.md#class-bool) = false) |
| void | [add_submenu_item](class_popupmenu.md#class-popupmenu-method-add-submenu-item)(label: [String](class_string.md#class-string), submenu: [String](class_string.md#class-string), id: [int](class_int.md#class-int) = -1) |
| void | [add_submenu_node_item](class_popupmenu.md#class-popupmenu-method-add-submenu-node-item)(label: [String](class_string.md#class-string), submenu: [PopupMenu](class_popupmenu.md#class-popupmenu), id: [int](class_int.md#class-int) = -1) |
| void | [clear](class_popupmenu.md#class-popupmenu-method-clear)(free_submenus: [bool](class_bool.md#class-bool) = false) |
| [int](class_int.md#class-int) | [get_focused_item](class_popupmenu.md#class-popupmenu-method-get-focused-item)() const |
| [Key](class_@globalscope.md#enum-globalscope-key) | [get_item_accelerator](class_popupmenu.md#class-popupmenu-method-get-item-accelerator)(index: [int](class_int.md#class-int)) const |
| [AutoTranslateMode](class_node.md#enum-node-autotranslatemode) | [get_item_auto_translate_mode](class_popupmenu.md#class-popupmenu-method-get-item-auto-translate-mode)(index: [int](class_int.md#class-int)) const |
| [Texture2D](class_texture2d.md#class-texture2d) | [get_item_icon](class_popupmenu.md#class-popupmenu-method-get-item-icon)(index: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_item_icon_max_width](class_popupmenu.md#class-popupmenu-method-get-item-icon-max-width)(index: [int](class_int.md#class-int)) const |
| [Color](class_color.md#class-color) | [get_item_icon_modulate](class_popupmenu.md#class-popupmenu-method-get-item-icon-modulate)(index: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_item_id](class_popupmenu.md#class-popupmenu-method-get-item-id)(index: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_item_indent](class_popupmenu.md#class-popupmenu-method-get-item-indent)(index: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_item_index](class_popupmenu.md#class-popupmenu-method-get-item-index)(id: [int](class_int.md#class-int)) const |
| [String](class_string.md#class-string) | [get_item_language](class_popupmenu.md#class-popupmenu-method-get-item-language)(index: [int](class_int.md#class-int)) const |
| [Variant](class_variant.md#class-variant) | [get_item_metadata](class_popupmenu.md#class-popupmenu-method-get-item-metadata)(index: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_item_multistate](class_popupmenu.md#class-popupmenu-method-get-item-multistate)(index: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_item_multistate_max](class_popupmenu.md#class-popupmenu-method-get-item-multistate-max)(index: [int](class_int.md#class-int)) const |
| [Shortcut](class_shortcut.md#class-shortcut) | [get_item_shortcut](class_popupmenu.md#class-popupmenu-method-get-item-shortcut)(index: [int](class_int.md#class-int)) const |
| [String](class_string.md#class-string) | [get_item_submenu](class_popupmenu.md#class-popupmenu-method-get-item-submenu)(index: [int](class_int.md#class-int)) const |
| [PopupMenu](class_popupmenu.md#class-popupmenu) | [get_item_submenu_node](class_popupmenu.md#class-popupmenu-method-get-item-submenu-node)(index: [int](class_int.md#class-int)) const |
| [String](class_string.md#class-string) | [get_item_text](class_popupmenu.md#class-popupmenu-method-get-item-text)(index: [int](class_int.md#class-int)) const |
| [TextDirection](class_control.md#enum-control-textdirection) | [get_item_text_direction](class_popupmenu.md#class-popupmenu-method-get-item-text-direction)(index: [int](class_int.md#class-int)) const |
| [String](class_string.md#class-string) | [get_item_tooltip](class_popupmenu.md#class-popupmenu-method-get-item-tooltip)(index: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [is_item_checkable](class_popupmenu.md#class-popupmenu-method-is-item-checkable)(index: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [is_item_checked](class_popupmenu.md#class-popupmenu-method-is-item-checked)(index: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [is_item_disabled](class_popupmenu.md#class-popupmenu-method-is-item-disabled)(index: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [is_item_radio_checkable](class_popupmenu.md#class-popupmenu-method-is-item-radio-checkable)(index: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [is_item_separator](class_popupmenu.md#class-popupmenu-method-is-item-separator)(index: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [is_item_shortcut_disabled](class_popupmenu.md#class-popupmenu-method-is-item-shortcut-disabled)(index: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [is_native_menu](class_popupmenu.md#class-popupmenu-method-is-native-menu)() const |
| [bool](class_bool.md#class-bool) | [is_system_menu](class_popupmenu.md#class-popupmenu-method-is-system-menu)() const |
| void | [remove_item](class_popupmenu.md#class-popupmenu-method-remove-item)(index: [int](class_int.md#class-int)) |
| void | [scroll_to_item](class_popupmenu.md#class-popupmenu-method-scroll-to-item)(index: [int](class_int.md#class-int)) |
| void | [set_focused_item](class_popupmenu.md#class-popupmenu-method-set-focused-item)(index: [int](class_int.md#class-int)) |
| void | [set_item_accelerator](class_popupmenu.md#class-popupmenu-method-set-item-accelerator)(index: [int](class_int.md#class-int), accel: [Key](class_@globalscope.md#enum-globalscope-key)) |
| void | [set_item_as_checkable](class_popupmenu.md#class-popupmenu-method-set-item-as-checkable)(index: [int](class_int.md#class-int), enable: [bool](class_bool.md#class-bool)) |
| void | [set_item_as_radio_checkable](class_popupmenu.md#class-popupmenu-method-set-item-as-radio-checkable)(index: [int](class_int.md#class-int), enable: [bool](class_bool.md#class-bool)) |
| void | [set_item_as_separator](class_popupmenu.md#class-popupmenu-method-set-item-as-separator)(index: [int](class_int.md#class-int), enable: [bool](class_bool.md#class-bool)) |
| void | [set_item_auto_translate_mode](class_popupmenu.md#class-popupmenu-method-set-item-auto-translate-mode)(index: [int](class_int.md#class-int), mode: [AutoTranslateMode](class_node.md#enum-node-autotranslatemode)) |
| void | [set_item_checked](class_popupmenu.md#class-popupmenu-method-set-item-checked)(index: [int](class_int.md#class-int), checked: [bool](class_bool.md#class-bool)) |
| void | [set_item_disabled](class_popupmenu.md#class-popupmenu-method-set-item-disabled)(index: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool)) |
| void | [set_item_icon](class_popupmenu.md#class-popupmenu-method-set-item-icon)(index: [int](class_int.md#class-int), icon: [Texture2D](class_texture2d.md#class-texture2d)) |
| void | [set_item_icon_max_width](class_popupmenu.md#class-popupmenu-method-set-item-icon-max-width)(index: [int](class_int.md#class-int), width: [int](class_int.md#class-int)) |
| void | [set_item_icon_modulate](class_popupmenu.md#class-popupmenu-method-set-item-icon-modulate)(index: [int](class_int.md#class-int), modulate: [Color](class_color.md#class-color)) |
| void | [set_item_id](class_popupmenu.md#class-popupmenu-method-set-item-id)(index: [int](class_int.md#class-int), id: [int](class_int.md#class-int)) |
| void | [set_item_indent](class_popupmenu.md#class-popupmenu-method-set-item-indent)(index: [int](class_int.md#class-int), indent: [int](class_int.md#class-int)) |
| void | [set_item_index](class_popupmenu.md#class-popupmenu-method-set-item-index)(index: [int](class_int.md#class-int), target_index: [int](class_int.md#class-int)) |
| void | [set_item_language](class_popupmenu.md#class-popupmenu-method-set-item-language)(index: [int](class_int.md#class-int), language: [String](class_string.md#class-string)) |
| void | [set_item_metadata](class_popupmenu.md#class-popupmenu-method-set-item-metadata)(index: [int](class_int.md#class-int), metadata: [Variant](class_variant.md#class-variant)) |
| void | [set_item_multistate](class_popupmenu.md#class-popupmenu-method-set-item-multistate)(index: [int](class_int.md#class-int), state: [int](class_int.md#class-int)) |
| void | [set_item_multistate_max](class_popupmenu.md#class-popupmenu-method-set-item-multistate-max)(index: [int](class_int.md#class-int), max_states: [int](class_int.md#class-int)) |
| void | [set_item_shortcut](class_popupmenu.md#class-popupmenu-method-set-item-shortcut)(index: [int](class_int.md#class-int), shortcut: [Shortcut](class_shortcut.md#class-shortcut), global: [bool](class_bool.md#class-bool) = false) |
| void | [set_item_shortcut_disabled](class_popupmenu.md#class-popupmenu-method-set-item-shortcut-disabled)(index: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool)) |
| void | [set_item_submenu](class_popupmenu.md#class-popupmenu-method-set-item-submenu)(index: [int](class_int.md#class-int), submenu: [String](class_string.md#class-string)) |
| void | [set_item_submenu_node](class_popupmenu.md#class-popupmenu-method-set-item-submenu-node)(index: [int](class_int.md#class-int), submenu: [PopupMenu](class_popupmenu.md#class-popupmenu)) |
| void | [set_item_text](class_popupmenu.md#class-popupmenu-method-set-item-text)(index: [int](class_int.md#class-int), text: [String](class_string.md#class-string)) |
| void | [set_item_text_direction](class_popupmenu.md#class-popupmenu-method-set-item-text-direction)(index: [int](class_int.md#class-int), direction: [TextDirection](class_control.md#enum-control-textdirection)) |
| void | [set_item_tooltip](class_popupmenu.md#class-popupmenu-method-set-item-tooltip)(index: [int](class_int.md#class-int), tooltip: [String](class_string.md#class-string)) |
| void | [toggle_item_checked](class_popupmenu.md#class-popupmenu-method-toggle-item-checked)(index: [int](class_int.md#class-int)) |
| void | [toggle_item_multistate](class_popupmenu.md#class-popupmenu-method-toggle-item-multistate)(index: [int](class_int.md#class-int)) |

<a id="theme-properties"></a>

## Theme Properties

|  |  |  |
| --- | --- | --- |
| [Color](class_color.md#class-color) | [font_accelerator_color](class_popupmenu.md#class-popupmenu-theme-color-font-accelerator-color) | `Color(0.7, 0.7, 0.7, 0.8)` |
| [Color](class_color.md#class-color) | [font_color](class_popupmenu.md#class-popupmenu-theme-color-font-color) | `Color(0.875, 0.875, 0.875, 1)` |
| [Color](class_color.md#class-color) | [font_disabled_color](class_popupmenu.md#class-popupmenu-theme-color-font-disabled-color) | `Color(0.4, 0.4, 0.4, 0.8)` |
| [Color](class_color.md#class-color) | [font_hover_color](class_popupmenu.md#class-popupmenu-theme-color-font-hover-color) | `Color(0.875, 0.875, 0.875, 1)` |
| [Color](class_color.md#class-color) | [font_outline_color](class_popupmenu.md#class-popupmenu-theme-color-font-outline-color) | `Color(0, 0, 0, 1)` |
| [Color](class_color.md#class-color) | [font_separator_color](class_popupmenu.md#class-popupmenu-theme-color-font-separator-color) | `Color(0.875, 0.875, 0.875, 1)` |
| [Color](class_color.md#class-color) | [font_separator_outline_color](class_popupmenu.md#class-popupmenu-theme-color-font-separator-outline-color) | `Color(0, 0, 0, 1)` |
| [int](class_int.md#class-int) | [gutter_compact](class_popupmenu.md#class-popupmenu-theme-constant-gutter-compact) | `1` |
| [int](class_int.md#class-int) | [h_separation](class_popupmenu.md#class-popupmenu-theme-constant-h-separation) | `4` |
| [int](class_int.md#class-int) | [icon_max_width](class_popupmenu.md#class-popupmenu-theme-constant-icon-max-width) | `0` |
| [int](class_int.md#class-int) | [indent](class_popupmenu.md#class-popupmenu-theme-constant-indent) | `10` |
| [int](class_int.md#class-int) | [item_end_padding](class_popupmenu.md#class-popupmenu-theme-constant-item-end-padding) | `2` |
| [int](class_int.md#class-int) | [item_start_padding](class_popupmenu.md#class-popupmenu-theme-constant-item-start-padding) | `2` |
| [int](class_int.md#class-int) | [outline_size](class_popupmenu.md#class-popupmenu-theme-constant-outline-size) | `0` |
| [int](class_int.md#class-int) | [search_bar_separation](class_popupmenu.md#class-popupmenu-theme-constant-search-bar-separation) | `4` |
| [int](class_int.md#class-int) | [separator_outline_size](class_popupmenu.md#class-popupmenu-theme-constant-separator-outline-size) | `0` |
| [int](class_int.md#class-int) | [v_separation](class_popupmenu.md#class-popupmenu-theme-constant-v-separation) | `4` |
| [Font](class_font.md#class-font) | [font](class_popupmenu.md#class-popupmenu-theme-font-font) |  |
| [Font](class_font.md#class-font) | [font_separator](class_popupmenu.md#class-popupmenu-theme-font-font-separator) |  |
| [int](class_int.md#class-int) | [font_separator_size](class_popupmenu.md#class-popupmenu-theme-font-size-font-separator-size) |  |
| [int](class_int.md#class-int) | [font_size](class_popupmenu.md#class-popupmenu-theme-font-size-font-size) |  |
| [Texture2D](class_texture2d.md#class-texture2d) | [checked](class_popupmenu.md#class-popupmenu-theme-icon-checked) |  |
| [Texture2D](class_texture2d.md#class-texture2d) | [checked_disabled](class_popupmenu.md#class-popupmenu-theme-icon-checked-disabled) |  |
| [Texture2D](class_texture2d.md#class-texture2d) | [radio_checked](class_popupmenu.md#class-popupmenu-theme-icon-radio-checked) |  |
| [Texture2D](class_texture2d.md#class-texture2d) | [radio_checked_disabled](class_popupmenu.md#class-popupmenu-theme-icon-radio-checked-disabled) |  |
| [Texture2D](class_texture2d.md#class-texture2d) | [radio_unchecked](class_popupmenu.md#class-popupmenu-theme-icon-radio-unchecked) |  |
| [Texture2D](class_texture2d.md#class-texture2d) | [radio_unchecked_disabled](class_popupmenu.md#class-popupmenu-theme-icon-radio-unchecked-disabled) |  |
| [Texture2D](class_texture2d.md#class-texture2d) | [search](class_popupmenu.md#class-popupmenu-theme-icon-search) |  |
| [Texture2D](class_texture2d.md#class-texture2d) | [submenu](class_popupmenu.md#class-popupmenu-theme-icon-submenu) |  |
| [Texture2D](class_texture2d.md#class-texture2d) | [submenu_mirrored](class_popupmenu.md#class-popupmenu-theme-icon-submenu-mirrored) |  |
| [Texture2D](class_texture2d.md#class-texture2d) | [unchecked](class_popupmenu.md#class-popupmenu-theme-icon-unchecked) |  |
| [Texture2D](class_texture2d.md#class-texture2d) | [unchecked_disabled](class_popupmenu.md#class-popupmenu-theme-icon-unchecked-disabled) |  |
| [StyleBox](class_stylebox.md#class-stylebox) | [hover](class_popupmenu.md#class-popupmenu-theme-style-hover) |  |
| [StyleBox](class_stylebox.md#class-stylebox) | [labeled_separator_left](class_popupmenu.md#class-popupmenu-theme-style-labeled-separator-left) |  |
| [StyleBox](class_stylebox.md#class-stylebox) | [labeled_separator_right](class_popupmenu.md#class-popupmenu-theme-style-labeled-separator-right) |  |
| [StyleBox](class_stylebox.md#class-stylebox) | [panel](class_popupmenu.md#class-popupmenu-theme-style-panel) |  |
| [StyleBox](class_stylebox.md#class-stylebox) | [separator](class_popupmenu.md#class-popupmenu-theme-style-separator) |  |

---


<a id="signals"></a>

## Signals

<a id="class-popupmenu-signal-id-focused"></a>

**id_focused**(id: [int](class_int.md#class-int)) [🔗](class_popupmenu.md#class-popupmenu-signal-id-focused)

Emitted when the user navigated to an item of some `id` using the [ProjectSettings.input/ui_up](class_projectsettings.md#class-projectsettings-property-input-ui-up) or [ProjectSettings.input/ui_down](class_projectsettings.md#class-projectsettings-property-input-ui-down) input action.

---


<a id="class-popupmenu-signal-id-pressed"></a>

**id_pressed**(id: [int](class_int.md#class-int)) [🔗](class_popupmenu.md#class-popupmenu-signal-id-pressed)

Emitted when an item of some `id` is pressed. Also emitted when its accelerator is activated on macOS.

**Note:** If `id` is negative (either explicitly or due to overflow), this will return the corresponding index instead.

---


<a id="class-popupmenu-signal-index-pressed"></a>

**index_pressed**(index: [int](class_int.md#class-int)) [🔗](class_popupmenu.md#class-popupmenu-signal-index-pressed)

Emitted when an item of some `index` is pressed. Also emitted when its accelerator is activated on macOS.

---


<a id="class-popupmenu-signal-menu-changed"></a>

**menu_changed**() [🔗](class_popupmenu.md#class-popupmenu-signal-menu-changed)

Emitted when any item is added, modified or removed.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-popupmenu-property-allow-search"></a>

[bool](class_bool.md#class-bool) **allow_search** = `true` [🔗](class_popupmenu.md#class-popupmenu-property-allow-search)

- void **set_allow_search**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_allow_search**()

If `true`, allows navigating **PopupMenu** with letter keys.

---


<a id="class-popupmenu-property-hide-on-checkable-item-selection"></a>

[bool](class_bool.md#class-bool) **hide_on_checkable_item_selection** = `true` [🔗](class_popupmenu.md#class-popupmenu-property-hide-on-checkable-item-selection)

- void **set_hide_on_checkable_item_selection**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_hide_on_checkable_item_selection**()

If `true`, hides the **PopupMenu** when a checkbox or radio button is selected.

---


<a id="class-popupmenu-property-hide-on-item-selection"></a>

[bool](class_bool.md#class-bool) **hide_on_item_selection** = `true` [🔗](class_popupmenu.md#class-popupmenu-property-hide-on-item-selection)

- void **set_hide_on_item_selection**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_hide_on_item_selection**()

If `true`, hides the **PopupMenu** when an item is selected.

---


<a id="class-popupmenu-property-hide-on-state-item-selection"></a>

[bool](class_bool.md#class-bool) **hide_on_state_item_selection** = `false` [🔗](class_popupmenu.md#class-popupmenu-property-hide-on-state-item-selection)

- void **set_hide_on_state_item_selection**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_hide_on_state_item_selection**()

If `true`, hides the **PopupMenu** when a state item is selected.

---


<a id="class-popupmenu-property-item-count"></a>

[int](class_int.md#class-int) **item_count** = `0` [🔗](class_popupmenu.md#class-popupmenu-property-item-count)

- void **set_item_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_item_count**()

The number of items currently in the list.

---


<a id="class-popupmenu-property-item-index-checkable"></a>

[int](class_int.md#class-int) **item_{index}/checkable** = `0` [🔗](class_popupmenu.md#class-popupmenu-property-item-index-checkable)

The checkable item type of the item at `index`.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

---


<a id="class-popupmenu-property-item-index-checked"></a>

[bool](class_bool.md#class-bool) **item_{index}/checked** = `false` [🔗](class_popupmenu.md#class-popupmenu-property-item-index-checked)

If `true`, the item at `index` is checked.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

---


<a id="class-popupmenu-property-item-index-disabled"></a>

[bool](class_bool.md#class-bool) **item_{index}/disabled** = `false` [🔗](class_popupmenu.md#class-popupmenu-property-item-index-disabled)

If `true`, the item at `index` is disabled.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

---


<a id="class-popupmenu-property-item-index-icon"></a>

[Texture2D](class_texture2d.md#class-texture2d) **item_{index}/icon** [🔗](class_popupmenu.md#class-popupmenu-property-item-index-icon)

The icon of the item at `index`.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

---


<a id="class-popupmenu-property-item-index-id"></a>

[int](class_int.md#class-int) **item_{index}/id** = `0` [🔗](class_popupmenu.md#class-popupmenu-property-item-index-id)

The ID of the item at `index`.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

---


<a id="class-popupmenu-property-item-index-separator"></a>

[bool](class_bool.md#class-bool) **item_{index}/separator** = `false` [🔗](class_popupmenu.md#class-popupmenu-property-item-index-separator)

If `true`, the item at `index` is a separator.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

---


<a id="class-popupmenu-property-item-index-text"></a>

[String](class_string.md#class-string) **item_{index}/text** = `""` [🔗](class_popupmenu.md#class-popupmenu-property-item-index-text)

The text of the item at `index`.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

---


<a id="class-popupmenu-property-prefer-native-menu"></a>

[bool](class_bool.md#class-bool) **prefer_native_menu** = `false` [🔗](class_popupmenu.md#class-popupmenu-property-prefer-native-menu)

- void **set_prefer_native_menu**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_prefer_native_menu**()

If `true`, [MenuBar](class_menubar.md#class-menubar) will use native menu when supported.

**Note:** If **PopupMenu** is linked to [StatusIndicator](class_statusindicator.md#class-statusindicator), [MenuBar](class_menubar.md#class-menubar), or another **PopupMenu** item it can use native menu regardless of this property, use [is_native_menu()](class_popupmenu.md#class-popupmenu-method-is-native-menu) to check it.

---


<a id="class-popupmenu-property-search-bar-enabled"></a>

[bool](class_bool.md#class-bool) **search_bar_enabled** = `false` [🔗](class_popupmenu.md#class-popupmenu-property-search-bar-enabled)

- void **set_search_bar_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_search_bar_enabled**()

If `true`, shows a search bar at the top of the **PopupMenu** for filtering items. See [search_bar_min_item_count](class_popupmenu.md#class-popupmenu-property-search-bar-min-item-count) for dynamically controlling its visibility based on the number of items.

**Note:** When enabled, [allow_search](class_popupmenu.md#class-popupmenu-property-allow-search) is ignored.

---


<a id="class-popupmenu-property-search-bar-fuzzy-search-enabled"></a>

[bool](class_bool.md#class-bool) **search_bar_fuzzy_search_enabled** = `true` [🔗](class_popupmenu.md#class-popupmenu-property-search-bar-fuzzy-search-enabled)

- void **set_search_bar_fuzzy_search_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_search_bar_fuzzy_search_enabled**()

If `true`, enables fuzzy searching in the **PopupMenu** search bar. This allows the search results to include items that almost match the search query, as well items that match the individual characters of the search query, but not in sequence.

Use [search_bar_fuzzy_search_max_misses](class_popupmenu.md#class-popupmenu-property-search-bar-fuzzy-search-max-misses) to set the maximum number of mismatches allowed in the search results.

---


<a id="class-popupmenu-property-search-bar-fuzzy-search-max-misses"></a>

[int](class_int.md#class-int) **search_bar_fuzzy_search_max_misses** = `2` [🔗](class_popupmenu.md#class-popupmenu-property-search-bar-fuzzy-search-max-misses)

- void **set_search_bar_fuzzy_search_max_misses**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_search_bar_fuzzy_search_max_misses**()

Sets the maximum number of mismatches allowed in each search result when fuzzy searching is enabled for the **PopupMenu** search bar. Any item with more mismatches will be hidden from the search results.

---


<a id="class-popupmenu-property-search-bar-min-item-count"></a>

[int](class_int.md#class-int) **search_bar_min_item_count** = `0` [🔗](class_popupmenu.md#class-popupmenu-property-search-bar-min-item-count)

- void **set_search_bar_min_item_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_search_bar_min_item_count**()

Sets the minimum number of items required for the search bar to be visible. [search_bar_enabled](class_popupmenu.md#class-popupmenu-property-search-bar-enabled) must be `true` for this to have any effect. Separator items are not counted.

---


<a id="class-popupmenu-property-shrink-height"></a>

[bool](class_bool.md#class-bool) **shrink_height** = `true` [🔗](class_popupmenu.md#class-popupmenu-property-shrink-height)

- void **set_shrink_height**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_shrink_height**()

If `true`, shrinks **PopupMenu** to minimum height when it's shown.

---


<a id="class-popupmenu-property-shrink-width"></a>

[bool](class_bool.md#class-bool) **shrink_width** = `true` [🔗](class_popupmenu.md#class-popupmenu-property-shrink-width)

- void **set_shrink_width**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_shrink_width**()

If `true`, shrinks **PopupMenu** to minimum width when it's shown.

---


<a id="class-popupmenu-property-submenu-popup-delay"></a>

[float](class_float.md#class-float) **submenu_popup_delay** = `0.2` [🔗](class_popupmenu.md#class-popupmenu-property-submenu-popup-delay)

- void **set_submenu_popup_delay**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_submenu_popup_delay**()

Sets the delay time in seconds for the submenu item to popup on mouse hovering. If the popup menu is added as a child of another (acting as a submenu), it will inherit the delay time of the parent menu item.

**Note:** If the mouse is exiting a submenu item with an open submenu and enters a different submenu item, the submenu popup delay time is affected by the direction of the mouse movement toward the open submenu. If the mouse is moving toward the submenu, the open submenu will wait approximately `0.5` seconds before closing, which then allows the hovered submenu item to open. This additional delay allows the mouse time to move to the open submenu across other menu items without prematurely closing. If the mouse is not moving toward the open submenu, for example in a downward direction, the open submenu will close immediately.

---


<a id="class-popupmenu-property-system-menu-id"></a>

[SystemMenus](class_nativemenu.md#enum-nativemenu-systemmenus) **system_menu_id** = `0` [🔗](class_popupmenu.md#class-popupmenu-property-system-menu-id)

- void **set_system_menu**(value: [SystemMenus](class_nativemenu.md#enum-nativemenu-systemmenus))
- [SystemMenus](class_nativemenu.md#enum-nativemenu-systemmenus) **get_system_menu**()

If set to one of the values of [SystemMenus](class_nativemenu.md#enum-nativemenu-systemmenus), this **PopupMenu** is bound to the special system menu. Only one **PopupMenu** can be bound to each special menu at a time.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-popupmenu-method-activate-item-by-event"></a>

[bool](class_bool.md#class-bool) **activate_item_by_event**(event: [InputEvent](class_inputevent.md#class-inputevent), for_global_only: [bool](class_bool.md#class-bool) = false) [🔗](class_popupmenu.md#class-popupmenu-method-activate-item-by-event)

Checks the provided `event` against the **PopupMenu**'s shortcuts and accelerators, and activates the first item with matching events. If `for_global_only` is `true`, only shortcuts and accelerators with `global` set to `true` will be called.

Returns `true` if an item was successfully activated.

**Note:** Certain [Control](class_control.md#class-control)s, such as [MenuButton](class_menubutton.md#class-menubutton), will call this method automatically.

---


<a id="class-popupmenu-method-add-check-item"></a>

void **add_check_item**(label: [String](class_string.md#class-string), id: [int](class_int.md#class-int) = -1, accel: [Key](class_@globalscope.md#enum-globalscope-key) = 0) [🔗](class_popupmenu.md#class-popupmenu-method-add-check-item)

Adds a new checkable item with text `label`.

An `id` can optionally be provided, as well as an accelerator (`accel`). If no `id` is provided, one will be created from the index. If no `accel` is provided, then the default value of 0 (corresponding to [@GlobalScope.KEY_NONE](class_@globalscope.md#class-globalscope-constant-key-none)) will be assigned to the item (which means it won't have any accelerator). See [get_item_accelerator()](class_popupmenu.md#class-popupmenu-method-get-item-accelerator) for more info on accelerators.

**Note:** Checkable items just display a checkmark, but don't have any built-in checking behavior and must be checked/unchecked manually. See [set_item_checked()](class_popupmenu.md#class-popupmenu-method-set-item-checked) for more info on how to control it.

---


<a id="class-popupmenu-method-add-check-shortcut"></a>

void **add_check_shortcut**(shortcut: [Shortcut](class_shortcut.md#class-shortcut), id: [int](class_int.md#class-int) = -1, global: [bool](class_bool.md#class-bool) = false) [🔗](class_popupmenu.md#class-popupmenu-method-add-check-shortcut)

Adds a new checkable item and assigns the specified [Shortcut](class_shortcut.md#class-shortcut) to it. Sets the label of the checkbox to the [Shortcut](class_shortcut.md#class-shortcut)'s name.

An `id` can optionally be provided. If no `id` is provided, one will be created from the index.

**Note:** Checkable items just display a checkmark, but don't have any built-in checking behavior and must be checked/unchecked manually. See [set_item_checked()](class_popupmenu.md#class-popupmenu-method-set-item-checked) for more info on how to control it.

---


<a id="class-popupmenu-method-add-icon-check-item"></a>

void **add_icon_check_item**(texture: [Texture2D](class_texture2d.md#class-texture2d), label: [String](class_string.md#class-string), id: [int](class_int.md#class-int) = -1, accel: [Key](class_@globalscope.md#enum-globalscope-key) = 0) [🔗](class_popupmenu.md#class-popupmenu-method-add-icon-check-item)

Adds a new checkable item with text `label` and icon `texture`.

An `id` can optionally be provided, as well as an accelerator (`accel`). If no `id` is provided, one will be created from the index. If no `accel` is provided, then the default value of 0 (corresponding to [@GlobalScope.KEY_NONE](class_@globalscope.md#class-globalscope-constant-key-none)) will be assigned to the item (which means it won't have any accelerator). See [get_item_accelerator()](class_popupmenu.md#class-popupmenu-method-get-item-accelerator) for more info on accelerators.

**Note:** Checkable items just display a checkmark, but don't have any built-in checking behavior and must be checked/unchecked manually. See [set_item_checked()](class_popupmenu.md#class-popupmenu-method-set-item-checked) for more info on how to control it.

---


<a id="class-popupmenu-method-add-icon-check-shortcut"></a>

void **add_icon_check_shortcut**(texture: [Texture2D](class_texture2d.md#class-texture2d), shortcut: [Shortcut](class_shortcut.md#class-shortcut), id: [int](class_int.md#class-int) = -1, global: [bool](class_bool.md#class-bool) = false) [🔗](class_popupmenu.md#class-popupmenu-method-add-icon-check-shortcut)

Adds a new checkable item and assigns the specified [Shortcut](class_shortcut.md#class-shortcut) and icon `texture` to it. Sets the label of the checkbox to the [Shortcut](class_shortcut.md#class-shortcut)'s name.

An `id` can optionally be provided. If no `id` is provided, one will be created from the index.

**Note:** Checkable items just display a checkmark, but don't have any built-in checking behavior and must be checked/unchecked manually. See [set_item_checked()](class_popupmenu.md#class-popupmenu-method-set-item-checked) for more info on how to control it.

---


<a id="class-popupmenu-method-add-icon-item"></a>

void **add_icon_item**(texture: [Texture2D](class_texture2d.md#class-texture2d), label: [String](class_string.md#class-string), id: [int](class_int.md#class-int) = -1, accel: [Key](class_@globalscope.md#enum-globalscope-key) = 0) [🔗](class_popupmenu.md#class-popupmenu-method-add-icon-item)

Adds a new item with text `label` and icon `texture`.

An `id` can optionally be provided, as well as an accelerator (`accel`). If no `id` is provided, one will be created from the index. If no `accel` is provided, then the default value of 0 (corresponding to [@GlobalScope.KEY_NONE](class_@globalscope.md#class-globalscope-constant-key-none)) will be assigned to the item (which means it won't have any accelerator). See [get_item_accelerator()](class_popupmenu.md#class-popupmenu-method-get-item-accelerator) for more info on accelerators.

---


<a id="class-popupmenu-method-add-icon-radio-check-item"></a>

void **add_icon_radio_check_item**(texture: [Texture2D](class_texture2d.md#class-texture2d), label: [String](class_string.md#class-string), id: [int](class_int.md#class-int) = -1, accel: [Key](class_@globalscope.md#enum-globalscope-key) = 0) [🔗](class_popupmenu.md#class-popupmenu-method-add-icon-radio-check-item)

Same as [add_icon_check_item()](class_popupmenu.md#class-popupmenu-method-add-icon-check-item), but uses a radio check button.

---


<a id="class-popupmenu-method-add-icon-radio-check-shortcut"></a>

void **add_icon_radio_check_shortcut**(texture: [Texture2D](class_texture2d.md#class-texture2d), shortcut: [Shortcut](class_shortcut.md#class-shortcut), id: [int](class_int.md#class-int) = -1, global: [bool](class_bool.md#class-bool) = false) [🔗](class_popupmenu.md#class-popupmenu-method-add-icon-radio-check-shortcut)

Same as [add_icon_check_shortcut()](class_popupmenu.md#class-popupmenu-method-add-icon-check-shortcut), but uses a radio check button.

---


<a id="class-popupmenu-method-add-icon-shortcut"></a>

void **add_icon_shortcut**(texture: [Texture2D](class_texture2d.md#class-texture2d), shortcut: [Shortcut](class_shortcut.md#class-shortcut), id: [int](class_int.md#class-int) = -1, global: [bool](class_bool.md#class-bool) = false, allow_echo: [bool](class_bool.md#class-bool) = false) [🔗](class_popupmenu.md#class-popupmenu-method-add-icon-shortcut)

Adds a new item and assigns the specified [Shortcut](class_shortcut.md#class-shortcut) and icon `texture` to it. Sets the label of the checkbox to the [Shortcut](class_shortcut.md#class-shortcut)'s name.

An `id` can optionally be provided. If no `id` is provided, one will be created from the index.

If `allow_echo` is `true`, the shortcut can be activated with echo events.

---


<a id="class-popupmenu-method-add-item"></a>

void **add_item**(label: [String](class_string.md#class-string), id: [int](class_int.md#class-int) = -1, accel: [Key](class_@globalscope.md#enum-globalscope-key) = 0) [🔗](class_popupmenu.md#class-popupmenu-method-add-item)

Adds a new item with text `label`.

An `id` can optionally be provided, as well as an accelerator (`accel`). If no `id` is provided, one will be created from the index. If no `accel` is provided, then the default value of 0 (corresponding to [@GlobalScope.KEY_NONE](class_@globalscope.md#class-globalscope-constant-key-none)) will be assigned to the item (which means it won't have any accelerator). See [get_item_accelerator()](class_popupmenu.md#class-popupmenu-method-get-item-accelerator) for more info on accelerators.

**Note:** The provided `id` is used only in [id_pressed](class_popupmenu.md#class-popupmenu-signal-id-pressed) and [id_focused](class_popupmenu.md#class-popupmenu-signal-id-focused) signals. It's not related to the `index` arguments in e.g. [set_item_checked()](class_popupmenu.md#class-popupmenu-method-set-item-checked).

---


<a id="class-popupmenu-method-add-multistate-item"></a>

void **add_multistate_item**(label: [String](class_string.md#class-string), max_states: [int](class_int.md#class-int), default_state: [int](class_int.md#class-int) = 0, id: [int](class_int.md#class-int) = -1, accel: [Key](class_@globalscope.md#enum-globalscope-key) = 0) [🔗](class_popupmenu.md#class-popupmenu-method-add-multistate-item)

Adds a new multistate item with text `label`.

Contrarily to normal binary items, multistate items can have more than two states, as defined by `max_states`. The default value is defined by `default_state`.

An `id` can optionally be provided, as well as an accelerator (`accel`). If no `id` is provided, one will be created from the index. If no `accel` is provided, then the default value of 0 (corresponding to [@GlobalScope.KEY_NONE](class_@globalscope.md#class-globalscope-constant-key-none)) will be assigned to the item (which means it won't have any accelerator). See [get_item_accelerator()](class_popupmenu.md#class-popupmenu-method-get-item-accelerator) for more info on accelerators.

```gdscript
func _ready():
    add_multistate_item("Item", 3, 0)

    index_pressed.connect(func(index: int):
            toggle_item_multistate(index)
            match get_item_multistate(index):
                0:
                    print("First state")
                1:
                    print("Second state")
                2:
                    print("Third state")
        )
```

**Note:** Multistate items don't update their state automatically and must be done manually. See [toggle_item_multistate()](class_popupmenu.md#class-popupmenu-method-toggle-item-multistate), [set_item_multistate()](class_popupmenu.md#class-popupmenu-method-set-item-multistate) and [get_item_multistate()](class_popupmenu.md#class-popupmenu-method-get-item-multistate) for more info on how to control it.

---


<a id="class-popupmenu-method-add-radio-check-item"></a>

void **add_radio_check_item**(label: [String](class_string.md#class-string), id: [int](class_int.md#class-int) = -1, accel: [Key](class_@globalscope.md#enum-globalscope-key) = 0) [🔗](class_popupmenu.md#class-popupmenu-method-add-radio-check-item)

Adds a new radio check button with text `label`.

An `id` can optionally be provided, as well as an accelerator (`accel`). If no `id` is provided, one will be created from the index. If no `accel` is provided, then the default value of 0 (corresponding to [@GlobalScope.KEY_NONE](class_@globalscope.md#class-globalscope-constant-key-none)) will be assigned to the item (which means it won't have any accelerator). See [get_item_accelerator()](class_popupmenu.md#class-popupmenu-method-get-item-accelerator) for more info on accelerators.

**Note:** Checkable items just display a checkmark, but don't have any built-in checking behavior and must be checked/unchecked manually. See [set_item_checked()](class_popupmenu.md#class-popupmenu-method-set-item-checked) for more info on how to control it.

---


<a id="class-popupmenu-method-add-radio-check-shortcut"></a>

void **add_radio_check_shortcut**(shortcut: [Shortcut](class_shortcut.md#class-shortcut), id: [int](class_int.md#class-int) = -1, global: [bool](class_bool.md#class-bool) = false) [🔗](class_popupmenu.md#class-popupmenu-method-add-radio-check-shortcut)

Adds a new radio check button and assigns a [Shortcut](class_shortcut.md#class-shortcut) to it. Sets the label of the checkbox to the [Shortcut](class_shortcut.md#class-shortcut)'s name.

An `id` can optionally be provided. If no `id` is provided, one will be created from the index.

**Note:** Checkable items just display a checkmark, but don't have any built-in checking behavior and must be checked/unchecked manually. See [set_item_checked()](class_popupmenu.md#class-popupmenu-method-set-item-checked) for more info on how to control it.

---


<a id="class-popupmenu-method-add-separator"></a>

void **add_separator**(label: [String](class_string.md#class-string) = "", id: [int](class_int.md#class-int) = -1) [🔗](class_popupmenu.md#class-popupmenu-method-add-separator)

Adds a separator between items. Separators also occupy an index, which you can set by using the `id` parameter.

A `label` can optionally be provided, which will appear at the center of the separator.

---


<a id="class-popupmenu-method-add-shortcut"></a>

void **add_shortcut**(shortcut: [Shortcut](class_shortcut.md#class-shortcut), id: [int](class_int.md#class-int) = -1, global: [bool](class_bool.md#class-bool) = false, allow_echo: [bool](class_bool.md#class-bool) = false) [🔗](class_popupmenu.md#class-popupmenu-method-add-shortcut)

Adds a [Shortcut](class_shortcut.md#class-shortcut).

An `id` can optionally be provided. If no `id` is provided, one will be created from the index.

If `allow_echo` is `true`, the shortcut can be activated with echo events.

---


<a id="class-popupmenu-method-add-submenu-item"></a>

void **add_submenu_item**(label: [String](class_string.md#class-string), submenu: [String](class_string.md#class-string), id: [int](class_int.md#class-int) = -1) [🔗](class_popupmenu.md#class-popupmenu-method-add-submenu-item)

**Deprecated:** Prefer using [add_submenu_node_item()](class_popupmenu.md#class-popupmenu-method-add-submenu-node-item) instead.

Adds an item that will act as a submenu of the parent **PopupMenu** node when clicked. The `submenu` argument must be the name of an existing **PopupMenu** that has been added as a child to this node. This submenu will be shown when the item is clicked, hovered for long enough, or activated using the `ui_select` or `ui_right` input actions.

An `id` can optionally be provided. If no `id` is provided, one will be created from the index.

---


<a id="class-popupmenu-method-add-submenu-node-item"></a>

void **add_submenu_node_item**(label: [String](class_string.md#class-string), submenu: [PopupMenu](class_popupmenu.md#class-popupmenu), id: [int](class_int.md#class-int) = -1) [🔗](class_popupmenu.md#class-popupmenu-method-add-submenu-node-item)

Adds an item that will act as a submenu of the parent **PopupMenu** node when clicked. This submenu will be shown when the item is clicked, hovered for long enough, or activated using the `ui_select` or `ui_right` input actions.

`submenu` must be either child of this **PopupMenu** or has no parent node (in which case it will be automatically added as a child). If the `submenu` popup has another parent, this method will fail.

An `id` can optionally be provided. If no `id` is provided, one will be created from the index.

---


<a id="class-popupmenu-method-clear"></a>

void **clear**(free_submenus: [bool](class_bool.md#class-bool) = false) [🔗](class_popupmenu.md#class-popupmenu-method-clear)

Removes all items from the **PopupMenu**. If `free_submenus` is `true`, the submenu nodes are automatically freed.

---


<a id="class-popupmenu-method-get-focused-item"></a>

[int](class_int.md#class-int) **get_focused_item**() const [🔗](class_popupmenu.md#class-popupmenu-method-get-focused-item)

Returns the index of the currently focused item. Returns `-1` if no item is focused.

---


<a id="class-popupmenu-method-get-item-accelerator"></a>

[Key](class_@globalscope.md#enum-globalscope-key) **get_item_accelerator**(index: [int](class_int.md#class-int)) const [🔗](class_popupmenu.md#class-popupmenu-method-get-item-accelerator)

Returns the accelerator of the item at the given `index`. An accelerator is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The return value is an integer which is generally a combination of [KeyModifierMask](class_@globalscope.md#enum-globalscope-keymodifiermask)s and [Key](class_@globalscope.md#enum-globalscope-key)s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (`Ctrl + A`). If no accelerator is defined for the specified `index`, [get_item_accelerator()](class_popupmenu.md#class-popupmenu-method-get-item-accelerator) returns `0` (corresponding to [@GlobalScope.KEY_NONE](class_@globalscope.md#class-globalscope-constant-key-none)).

---


<a id="class-popupmenu-method-get-item-auto-translate-mode"></a>

[AutoTranslateMode](class_node.md#enum-node-autotranslatemode) **get_item_auto_translate_mode**(index: [int](class_int.md#class-int)) const [🔗](class_popupmenu.md#class-popupmenu-method-get-item-auto-translate-mode)

Returns the auto translate mode of the item at the given `index`.

---


<a id="class-popupmenu-method-get-item-icon"></a>

[Texture2D](class_texture2d.md#class-texture2d) **get_item_icon**(index: [int](class_int.md#class-int)) const [🔗](class_popupmenu.md#class-popupmenu-method-get-item-icon)

Returns the icon of the item at the given `index`.

---


<a id="class-popupmenu-method-get-item-icon-max-width"></a>

[int](class_int.md#class-int) **get_item_icon_max_width**(index: [int](class_int.md#class-int)) const [🔗](class_popupmenu.md#class-popupmenu-method-get-item-icon-max-width)

Returns the maximum allowed width of the icon for the item at the given `index`.

---


<a id="class-popupmenu-method-get-item-icon-modulate"></a>

[Color](class_color.md#class-color) **get_item_icon_modulate**(index: [int](class_int.md#class-int)) const [🔗](class_popupmenu.md#class-popupmenu-method-get-item-icon-modulate)

Returns a [Color](class_color.md#class-color) modulating the item's icon at the given `index`.

---


<a id="class-popupmenu-method-get-item-id"></a>

[int](class_int.md#class-int) **get_item_id**(index: [int](class_int.md#class-int)) const [🔗](class_popupmenu.md#class-popupmenu-method-get-item-id)

Returns the ID of the item at the given `index`.

---


<a id="class-popupmenu-method-get-item-indent"></a>

[int](class_int.md#class-int) **get_item_indent**(index: [int](class_int.md#class-int)) const [🔗](class_popupmenu.md#class-popupmenu-method-get-item-indent)

Returns the horizontal offset of the item at the given `index`.

---


<a id="class-popupmenu-method-get-item-index"></a>

[int](class_int.md#class-int) **get_item_index**(id: [int](class_int.md#class-int)) const [🔗](class_popupmenu.md#class-popupmenu-method-get-item-index)

Returns the index of the item containing the specified `id`. The index is automatically assigned to each item by the engine when added and represents the order items will be displayed.

---


<a id="class-popupmenu-method-get-item-language"></a>

[String](class_string.md#class-string) **get_item_language**(index: [int](class_int.md#class-int)) const [🔗](class_popupmenu.md#class-popupmenu-method-get-item-language)

Returns item's text language code.

---


<a id="class-popupmenu-method-get-item-metadata"></a>

[Variant](class_variant.md#class-variant) **get_item_metadata**(index: [int](class_int.md#class-int)) const [🔗](class_popupmenu.md#class-popupmenu-method-get-item-metadata)

Returns the metadata of the specified item, which might be of any type. You can set it with [set_item_metadata()](class_popupmenu.md#class-popupmenu-method-set-item-metadata), which provides a simple way of assigning context data to items.

---


<a id="class-popupmenu-method-get-item-multistate"></a>

[int](class_int.md#class-int) **get_item_multistate**(index: [int](class_int.md#class-int)) const [🔗](class_popupmenu.md#class-popupmenu-method-get-item-multistate)

Returns the state of the item at the given `index`.

---


<a id="class-popupmenu-method-get-item-multistate-max"></a>

[int](class_int.md#class-int) **get_item_multistate_max**(index: [int](class_int.md#class-int)) const [🔗](class_popupmenu.md#class-popupmenu-method-get-item-multistate-max)

Returns the max states of the item at the given `index`.

---


<a id="class-popupmenu-method-get-item-shortcut"></a>

[Shortcut](class_shortcut.md#class-shortcut) **get_item_shortcut**(index: [int](class_int.md#class-int)) const [🔗](class_popupmenu.md#class-popupmenu-method-get-item-shortcut)

Returns the [Shortcut](class_shortcut.md#class-shortcut) associated with the item at the given `index`.

---


<a id="class-popupmenu-method-get-item-submenu"></a>

[String](class_string.md#class-string) **get_item_submenu**(index: [int](class_int.md#class-int)) const [🔗](class_popupmenu.md#class-popupmenu-method-get-item-submenu)

**Deprecated:** Prefer using [get_item_submenu_node()](class_popupmenu.md#class-popupmenu-method-get-item-submenu-node) instead.

Returns the submenu name of the item at the given `index`. See [add_submenu_item()](class_popupmenu.md#class-popupmenu-method-add-submenu-item) for more info on how to add a submenu.

---


<a id="class-popupmenu-method-get-item-submenu-node"></a>

[PopupMenu](class_popupmenu.md#class-popupmenu) **get_item_submenu_node**(index: [int](class_int.md#class-int)) const [🔗](class_popupmenu.md#class-popupmenu-method-get-item-submenu-node)

Returns the submenu of the item at the given `index`, or `null` if no submenu was added. See [add_submenu_node_item()](class_popupmenu.md#class-popupmenu-method-add-submenu-node-item) for more info on how to add a submenu.

---


<a id="class-popupmenu-method-get-item-text"></a>

[String](class_string.md#class-string) **get_item_text**(index: [int](class_int.md#class-int)) const [🔗](class_popupmenu.md#class-popupmenu-method-get-item-text)

Returns the text of the item at the given `index`.

---


<a id="class-popupmenu-method-get-item-text-direction"></a>

[TextDirection](class_control.md#enum-control-textdirection) **get_item_text_direction**(index: [int](class_int.md#class-int)) const [🔗](class_popupmenu.md#class-popupmenu-method-get-item-text-direction)

Returns item's text base writing direction.

---


<a id="class-popupmenu-method-get-item-tooltip"></a>

[String](class_string.md#class-string) **get_item_tooltip**(index: [int](class_int.md#class-int)) const [🔗](class_popupmenu.md#class-popupmenu-method-get-item-tooltip)

Returns the tooltip associated with the item at the given `index`.

---


<a id="class-popupmenu-method-is-item-checkable"></a>

[bool](class_bool.md#class-bool) **is_item_checkable**(index: [int](class_int.md#class-int)) const [🔗](class_popupmenu.md#class-popupmenu-method-is-item-checkable)

Returns `true` if the item at the given `index` is checkable in some way, i.e. if it has a checkbox or radio button.

**Note:** Checkable items just display a checkmark or radio button, but don't have any built-in checking behavior and must be checked/unchecked manually.

---


<a id="class-popupmenu-method-is-item-checked"></a>

[bool](class_bool.md#class-bool) **is_item_checked**(index: [int](class_int.md#class-int)) const [🔗](class_popupmenu.md#class-popupmenu-method-is-item-checked)

Returns `true` if the item at the given `index` is checked.

---


<a id="class-popupmenu-method-is-item-disabled"></a>

[bool](class_bool.md#class-bool) **is_item_disabled**(index: [int](class_int.md#class-int)) const [🔗](class_popupmenu.md#class-popupmenu-method-is-item-disabled)

Returns `true` if the item at the given `index` is disabled. When it is disabled it can't be selected, or its action invoked.

See [set_item_disabled()](class_popupmenu.md#class-popupmenu-method-set-item-disabled) for more info on how to disable an item.

---


<a id="class-popupmenu-method-is-item-radio-checkable"></a>

[bool](class_bool.md#class-bool) **is_item_radio_checkable**(index: [int](class_int.md#class-int)) const [🔗](class_popupmenu.md#class-popupmenu-method-is-item-radio-checkable)

Returns `true` if the item at the given `index` has radio button-style checkability.

**Note:** This is purely cosmetic; you must add the logic for checking/unchecking items in radio groups.

---


<a id="class-popupmenu-method-is-item-separator"></a>

[bool](class_bool.md#class-bool) **is_item_separator**(index: [int](class_int.md#class-int)) const [🔗](class_popupmenu.md#class-popupmenu-method-is-item-separator)

Returns `true` if the item is a separator. If it is, it will be displayed as a line. See [add_separator()](class_popupmenu.md#class-popupmenu-method-add-separator) for more info on how to add a separator.

---


<a id="class-popupmenu-method-is-item-shortcut-disabled"></a>

[bool](class_bool.md#class-bool) **is_item_shortcut_disabled**(index: [int](class_int.md#class-int)) const [🔗](class_popupmenu.md#class-popupmenu-method-is-item-shortcut-disabled)

Returns `true` if the specified item's shortcut is disabled.

---


<a id="class-popupmenu-method-is-native-menu"></a>

[bool](class_bool.md#class-bool) **is_native_menu**() const [🔗](class_popupmenu.md#class-popupmenu-method-is-native-menu)

Returns `true` if the system native menu is supported and currently used by this **PopupMenu**.

---


<a id="class-popupmenu-method-is-system-menu"></a>

[bool](class_bool.md#class-bool) **is_system_menu**() const [🔗](class_popupmenu.md#class-popupmenu-method-is-system-menu)

Returns `true` if the menu is bound to the special system menu.

---


<a id="class-popupmenu-method-remove-item"></a>

void **remove_item**(index: [int](class_int.md#class-int)) [🔗](class_popupmenu.md#class-popupmenu-method-remove-item)

Removes the item at the given `index` from the menu.

**Note:** The indices of items after the removed item will be shifted by one.

---


<a id="class-popupmenu-method-scroll-to-item"></a>

void **scroll_to_item**(index: [int](class_int.md#class-int)) [🔗](class_popupmenu.md#class-popupmenu-method-scroll-to-item)

Moves the scroll view to make the item at the given `index` visible.

---


<a id="class-popupmenu-method-set-focused-item"></a>

void **set_focused_item**(index: [int](class_int.md#class-int)) [🔗](class_popupmenu.md#class-popupmenu-method-set-focused-item)

Sets the currently focused item as the given `index`.

Passing `-1` as the index makes so that no item is focused.

---


<a id="class-popupmenu-method-set-item-accelerator"></a>

void **set_item_accelerator**(index: [int](class_int.md#class-int), accel: [Key](class_@globalscope.md#enum-globalscope-key)) [🔗](class_popupmenu.md#class-popupmenu-method-set-item-accelerator)

Sets the accelerator of the item at the given `index`. An accelerator is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. `accel` is generally a combination of [KeyModifierMask](class_@globalscope.md#enum-globalscope-keymodifiermask)s and [Key](class_@globalscope.md#enum-globalscope-key)s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (`Ctrl + A`).

---


<a id="class-popupmenu-method-set-item-as-checkable"></a>

void **set_item_as_checkable**(index: [int](class_int.md#class-int), enable: [bool](class_bool.md#class-bool)) [🔗](class_popupmenu.md#class-popupmenu-method-set-item-as-checkable)

Sets whether the item at the given `index` has a checkbox. If `false`, sets the type of the item to plain text.

**Note:** Checkable items just display a checkmark, but don't have any built-in checking behavior and must be checked/unchecked manually.

---


<a id="class-popupmenu-method-set-item-as-radio-checkable"></a>

void **set_item_as_radio_checkable**(index: [int](class_int.md#class-int), enable: [bool](class_bool.md#class-bool)) [🔗](class_popupmenu.md#class-popupmenu-method-set-item-as-radio-checkable)

Sets the type of the item at the given `index` to radio button. If `false`, sets the type of the item to plain text.

---


<a id="class-popupmenu-method-set-item-as-separator"></a>

void **set_item_as_separator**(index: [int](class_int.md#class-int), enable: [bool](class_bool.md#class-bool)) [🔗](class_popupmenu.md#class-popupmenu-method-set-item-as-separator)

Mark the item at the given `index` as a separator, which means that it would be displayed as a line. If `false`, sets the type of the item to plain text.

---


<a id="class-popupmenu-method-set-item-auto-translate-mode"></a>

void **set_item_auto_translate_mode**(index: [int](class_int.md#class-int), mode: [AutoTranslateMode](class_node.md#enum-node-autotranslatemode)) [🔗](class_popupmenu.md#class-popupmenu-method-set-item-auto-translate-mode)

Sets the auto translate mode of the item at the given `index`.

Items use [Node.AUTO_TRANSLATE_MODE_INHERIT](class_node.md#class-node-constant-auto-translate-mode-inherit) by default, which uses the same auto translate mode as the **PopupMenu** itself.

---


<a id="class-popupmenu-method-set-item-checked"></a>

void **set_item_checked**(index: [int](class_int.md#class-int), checked: [bool](class_bool.md#class-bool)) [🔗](class_popupmenu.md#class-popupmenu-method-set-item-checked)

Sets the checkstate status of the item at the given `index`.

---


<a id="class-popupmenu-method-set-item-disabled"></a>

void **set_item_disabled**(index: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool)) [🔗](class_popupmenu.md#class-popupmenu-method-set-item-disabled)

Enables/disables the item at the given `index`. When it is disabled, it can't be selected and its action can't be invoked.

---


<a id="class-popupmenu-method-set-item-icon"></a>

void **set_item_icon**(index: [int](class_int.md#class-int), icon: [Texture2D](class_texture2d.md#class-texture2d)) [🔗](class_popupmenu.md#class-popupmenu-method-set-item-icon)

Replaces the [Texture2D](class_texture2d.md#class-texture2d) icon of the item at the given `index`.

---


<a id="class-popupmenu-method-set-item-icon-max-width"></a>

void **set_item_icon_max_width**(index: [int](class_int.md#class-int), width: [int](class_int.md#class-int)) [🔗](class_popupmenu.md#class-popupmenu-method-set-item-icon-max-width)

Sets the maximum allowed width of the icon for the item at the given `index`. This limit is applied on top of the default size of the icon and on top of [icon_max_width](class_popupmenu.md#class-popupmenu-theme-constant-icon-max-width). The height is adjusted according to the icon's ratio.

---


<a id="class-popupmenu-method-set-item-icon-modulate"></a>

void **set_item_icon_modulate**(index: [int](class_int.md#class-int), modulate: [Color](class_color.md#class-color)) [🔗](class_popupmenu.md#class-popupmenu-method-set-item-icon-modulate)

Sets a modulating [Color](class_color.md#class-color) of the item's icon at the given `index`.

---


<a id="class-popupmenu-method-set-item-id"></a>

void **set_item_id**(index: [int](class_int.md#class-int), id: [int](class_int.md#class-int)) [🔗](class_popupmenu.md#class-popupmenu-method-set-item-id)

Sets the `id` of the item at the given `index`.

The `id` is used in [id_pressed](class_popupmenu.md#class-popupmenu-signal-id-pressed) and [id_focused](class_popupmenu.md#class-popupmenu-signal-id-focused) signals.

---


<a id="class-popupmenu-method-set-item-indent"></a>

void **set_item_indent**(index: [int](class_int.md#class-int), indent: [int](class_int.md#class-int)) [🔗](class_popupmenu.md#class-popupmenu-method-set-item-indent)

Sets the horizontal offset of the item at the given `index`.

---


<a id="class-popupmenu-method-set-item-index"></a>

void **set_item_index**(index: [int](class_int.md#class-int), target_index: [int](class_int.md#class-int)) [🔗](class_popupmenu.md#class-popupmenu-method-set-item-index)

Changes the index of the item at index `index` to be at index `target_index`. This can be used to move an item above other items. The moved item will keep the same ID, even if it was generated from the original index.

**Note:** The indices of any items between index `index` and index `target_index` will be shifted by one.

---


<a id="class-popupmenu-method-set-item-language"></a>

void **set_item_language**(index: [int](class_int.md#class-int), language: [String](class_string.md#class-string)) [🔗](class_popupmenu.md#class-popupmenu-method-set-item-language)

Sets the language code of the text for the item at the given index to `language`. This is used for line-breaking and text shaping algorithms. If `language` is empty, the current locale is used.

---


<a id="class-popupmenu-method-set-item-metadata"></a>

void **set_item_metadata**(index: [int](class_int.md#class-int), metadata: [Variant](class_variant.md#class-variant)) [🔗](class_popupmenu.md#class-popupmenu-method-set-item-metadata)

Sets the metadata of an item, which may be of any type. You can later get it with [get_item_metadata()](class_popupmenu.md#class-popupmenu-method-get-item-metadata), which provides a simple way of assigning context data to items.

---


<a id="class-popupmenu-method-set-item-multistate"></a>

void **set_item_multistate**(index: [int](class_int.md#class-int), state: [int](class_int.md#class-int)) [🔗](class_popupmenu.md#class-popupmenu-method-set-item-multistate)

Sets the state of a multistate item. See [add_multistate_item()](class_popupmenu.md#class-popupmenu-method-add-multistate-item) for details.

---


<a id="class-popupmenu-method-set-item-multistate-max"></a>

void **set_item_multistate_max**(index: [int](class_int.md#class-int), max_states: [int](class_int.md#class-int)) [🔗](class_popupmenu.md#class-popupmenu-method-set-item-multistate-max)

Sets the max states of a multistate item. See [add_multistate_item()](class_popupmenu.md#class-popupmenu-method-add-multistate-item) for details.

---


<a id="class-popupmenu-method-set-item-shortcut"></a>

void **set_item_shortcut**(index: [int](class_int.md#class-int), shortcut: [Shortcut](class_shortcut.md#class-shortcut), global: [bool](class_bool.md#class-bool) = false) [🔗](class_popupmenu.md#class-popupmenu-method-set-item-shortcut)

Sets a [Shortcut](class_shortcut.md#class-shortcut) for the item at the given `index`.

---


<a id="class-popupmenu-method-set-item-shortcut-disabled"></a>

void **set_item_shortcut_disabled**(index: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool)) [🔗](class_popupmenu.md#class-popupmenu-method-set-item-shortcut-disabled)

Disables the [Shortcut](class_shortcut.md#class-shortcut) of the item at the given `index`.

---


<a id="class-popupmenu-method-set-item-submenu"></a>

void **set_item_submenu**(index: [int](class_int.md#class-int), submenu: [String](class_string.md#class-string)) [🔗](class_popupmenu.md#class-popupmenu-method-set-item-submenu)

**Deprecated:** Prefer using [set_item_submenu_node()](class_popupmenu.md#class-popupmenu-method-set-item-submenu-node) instead.

Sets the submenu of the item at the given `index`. The submenu is the name of a child **PopupMenu** node that would be shown when the item is clicked.

---


<a id="class-popupmenu-method-set-item-submenu-node"></a>

void **set_item_submenu_node**(index: [int](class_int.md#class-int), submenu: [PopupMenu](class_popupmenu.md#class-popupmenu)) [🔗](class_popupmenu.md#class-popupmenu-method-set-item-submenu-node)

Sets the submenu of the item at the given `index`. The submenu is a **PopupMenu** node that would be shown when the item is clicked. It must either be a child of this **PopupMenu** or has no parent (in which case it will be automatically added as a child). If the `submenu` popup has another parent, this method will fail.

---


<a id="class-popupmenu-method-set-item-text"></a>

void **set_item_text**(index: [int](class_int.md#class-int), text: [String](class_string.md#class-string)) [🔗](class_popupmenu.md#class-popupmenu-method-set-item-text)

Sets the text of the item at the given `index`.

---


<a id="class-popupmenu-method-set-item-text-direction"></a>

void **set_item_text_direction**(index: [int](class_int.md#class-int), direction: [TextDirection](class_control.md#enum-control-textdirection)) [🔗](class_popupmenu.md#class-popupmenu-method-set-item-text-direction)

Sets item's text base writing direction.

---


<a id="class-popupmenu-method-set-item-tooltip"></a>

void **set_item_tooltip**(index: [int](class_int.md#class-int), tooltip: [String](class_string.md#class-string)) [🔗](class_popupmenu.md#class-popupmenu-method-set-item-tooltip)

Sets the [String](class_string.md#class-string) tooltip of the item at the given `index`.

---


<a id="class-popupmenu-method-toggle-item-checked"></a>

void **toggle_item_checked**(index: [int](class_int.md#class-int)) [🔗](class_popupmenu.md#class-popupmenu-method-toggle-item-checked)

Toggles the check state of the item at the given `index`.

---


<a id="class-popupmenu-method-toggle-item-multistate"></a>

void **toggle_item_multistate**(index: [int](class_int.md#class-int)) [🔗](class_popupmenu.md#class-popupmenu-method-toggle-item-multistate)

Cycle to the next state of a multistate item. See [add_multistate_item()](class_popupmenu.md#class-popupmenu-method-add-multistate-item) for details.

---


<a id="theme-property-descriptions"></a>

## Theme Property Descriptions

<a id="class-popupmenu-theme-color-font-accelerator-color"></a>

[Color](class_color.md#class-color) **font_accelerator_color** = `Color(0.7, 0.7, 0.7, 0.8)` [🔗](class_popupmenu.md#class-popupmenu-theme-color-font-accelerator-color)

The text [Color](class_color.md#class-color) used for shortcuts and accelerators that show next to the menu item name when defined. See [get_item_accelerator()](class_popupmenu.md#class-popupmenu-method-get-item-accelerator) for more info on accelerators.

---


<a id="class-popupmenu-theme-color-font-color"></a>

[Color](class_color.md#class-color) **font_color** = `Color(0.875, 0.875, 0.875, 1)` [🔗](class_popupmenu.md#class-popupmenu-theme-color-font-color)

The default text [Color](class_color.md#class-color) for menu items' names.

---


<a id="class-popupmenu-theme-color-font-disabled-color"></a>

[Color](class_color.md#class-color) **font_disabled_color** = `Color(0.4, 0.4, 0.4, 0.8)` [🔗](class_popupmenu.md#class-popupmenu-theme-color-font-disabled-color)

[Color](class_color.md#class-color) used for disabled menu items' text.

---


<a id="class-popupmenu-theme-color-font-hover-color"></a>

[Color](class_color.md#class-color) **font_hover_color** = `Color(0.875, 0.875, 0.875, 1)` [🔗](class_popupmenu.md#class-popupmenu-theme-color-font-hover-color)

[Color](class_color.md#class-color) used for the hovered text.

---


<a id="class-popupmenu-theme-color-font-outline-color"></a>

[Color](class_color.md#class-color) **font_outline_color** = `Color(0, 0, 0, 1)` [🔗](class_popupmenu.md#class-popupmenu-theme-color-font-outline-color)

The tint of text outline of the menu item.

---


<a id="class-popupmenu-theme-color-font-separator-color"></a>

[Color](class_color.md#class-color) **font_separator_color** = `Color(0.875, 0.875, 0.875, 1)` [🔗](class_popupmenu.md#class-popupmenu-theme-color-font-separator-color)

[Color](class_color.md#class-color) used for labeled separators' text. See [add_separator()](class_popupmenu.md#class-popupmenu-method-add-separator).

---


<a id="class-popupmenu-theme-color-font-separator-outline-color"></a>

[Color](class_color.md#class-color) **font_separator_outline_color** = `Color(0, 0, 0, 1)` [🔗](class_popupmenu.md#class-popupmenu-theme-color-font-separator-outline-color)

The tint of text outline of the labeled separator.

---


<a id="class-popupmenu-theme-constant-gutter-compact"></a>

[int](class_int.md#class-int) **gutter_compact** = `1` [🔗](class_popupmenu.md#class-popupmenu-theme-constant-gutter-compact)

If not `0`, the icon gutter will be merged with the checkbox gutter when possible. This acts as a boolean.

---


<a id="class-popupmenu-theme-constant-h-separation"></a>

[int](class_int.md#class-int) **h_separation** = `4` [🔗](class_popupmenu.md#class-popupmenu-theme-constant-h-separation)

The horizontal space between the item's elements.

---


<a id="class-popupmenu-theme-constant-icon-max-width"></a>

[int](class_int.md#class-int) **icon_max_width** = `0` [🔗](class_popupmenu.md#class-popupmenu-theme-constant-icon-max-width)

The maximum allowed width of the item's icon. This limit is applied on top of the default size of the icon, but before the value set with [set_item_icon_max_width()](class_popupmenu.md#class-popupmenu-method-set-item-icon-max-width). The height is adjusted according to the icon's ratio.

---


<a id="class-popupmenu-theme-constant-indent"></a>

[int](class_int.md#class-int) **indent** = `10` [🔗](class_popupmenu.md#class-popupmenu-theme-constant-indent)

Width of the single indentation level.

---


<a id="class-popupmenu-theme-constant-item-end-padding"></a>

[int](class_int.md#class-int) **item_end_padding** = `2` [🔗](class_popupmenu.md#class-popupmenu-theme-constant-item-end-padding)

Horizontal padding to the right of the items (or left, in RTL layout).

---


<a id="class-popupmenu-theme-constant-item-start-padding"></a>

[int](class_int.md#class-int) **item_start_padding** = `2` [🔗](class_popupmenu.md#class-popupmenu-theme-constant-item-start-padding)

Horizontal padding to the left of the items (or right, in RTL layout).

---


<a id="class-popupmenu-theme-constant-outline-size"></a>

[int](class_int.md#class-int) **outline_size** = `0` [🔗](class_popupmenu.md#class-popupmenu-theme-constant-outline-size)

The size of the item text outline.

**Note:** If using a font with [FontFile.multichannel_signed_distance_field](class_fontfile.md#class-fontfile-property-multichannel-signed-distance-field) enabled, its [FontFile.msdf_pixel_range](class_fontfile.md#class-fontfile-property-msdf-pixel-range) must be set to at least *twice* the value of [outline_size](class_popupmenu.md#class-popupmenu-theme-constant-outline-size) for outline rendering to look correct. Otherwise, the outline may appear to be cut off earlier than intended.

---


<a id="class-popupmenu-theme-constant-search-bar-separation"></a>

[int](class_int.md#class-int) **search_bar_separation** = `4` [🔗](class_popupmenu.md#class-popupmenu-theme-constant-search-bar-separation)

The vertical space between search bar and menu items.

---


<a id="class-popupmenu-theme-constant-separator-outline-size"></a>

[int](class_int.md#class-int) **separator_outline_size** = `0` [🔗](class_popupmenu.md#class-popupmenu-theme-constant-separator-outline-size)

The size of the labeled separator text outline.

---


<a id="class-popupmenu-theme-constant-v-separation"></a>

[int](class_int.md#class-int) **v_separation** = `4` [🔗](class_popupmenu.md#class-popupmenu-theme-constant-v-separation)

The vertical space between each menu item.

---


<a id="class-popupmenu-theme-font-font"></a>

[Font](class_font.md#class-font) **font** [🔗](class_popupmenu.md#class-popupmenu-theme-font-font)

[Font](class_font.md#class-font) used for the menu items.

---


<a id="class-popupmenu-theme-font-font-separator"></a>

[Font](class_font.md#class-font) **font_separator** [🔗](class_popupmenu.md#class-popupmenu-theme-font-font-separator)

[Font](class_font.md#class-font) used for the labeled separator.

---


<a id="class-popupmenu-theme-font-size-font-separator-size"></a>

[int](class_int.md#class-int) **font_separator_size** [🔗](class_popupmenu.md#class-popupmenu-theme-font-size-font-separator-size)

Font size of the labeled separator.

---


<a id="class-popupmenu-theme-font-size-font-size"></a>

[int](class_int.md#class-int) **font_size** [🔗](class_popupmenu.md#class-popupmenu-theme-font-size-font-size)

Font size of the menu items.

---


<a id="class-popupmenu-theme-icon-checked"></a>

[Texture2D](class_texture2d.md#class-texture2d) **checked** [🔗](class_popupmenu.md#class-popupmenu-theme-icon-checked)

[Texture2D](class_texture2d.md#class-texture2d) icon for the checked checkbox items.

---


<a id="class-popupmenu-theme-icon-checked-disabled"></a>

[Texture2D](class_texture2d.md#class-texture2d) **checked_disabled** [🔗](class_popupmenu.md#class-popupmenu-theme-icon-checked-disabled)

[Texture2D](class_texture2d.md#class-texture2d) icon for the checked checkbox items when they are disabled.

---


<a id="class-popupmenu-theme-icon-radio-checked"></a>

[Texture2D](class_texture2d.md#class-texture2d) **radio_checked** [🔗](class_popupmenu.md#class-popupmenu-theme-icon-radio-checked)

[Texture2D](class_texture2d.md#class-texture2d) icon for the checked radio button items.

---


<a id="class-popupmenu-theme-icon-radio-checked-disabled"></a>

[Texture2D](class_texture2d.md#class-texture2d) **radio_checked_disabled** [🔗](class_popupmenu.md#class-popupmenu-theme-icon-radio-checked-disabled)

[Texture2D](class_texture2d.md#class-texture2d) icon for the checked radio button items when they are disabled.

---


<a id="class-popupmenu-theme-icon-radio-unchecked"></a>

[Texture2D](class_texture2d.md#class-texture2d) **radio_unchecked** [🔗](class_popupmenu.md#class-popupmenu-theme-icon-radio-unchecked)

[Texture2D](class_texture2d.md#class-texture2d) icon for the unchecked radio button items.

---


<a id="class-popupmenu-theme-icon-radio-unchecked-disabled"></a>

[Texture2D](class_texture2d.md#class-texture2d) **radio_unchecked_disabled** [🔗](class_popupmenu.md#class-popupmenu-theme-icon-radio-unchecked-disabled)

[Texture2D](class_texture2d.md#class-texture2d) icon for the unchecked radio button items when they are disabled.

---


<a id="class-popupmenu-theme-icon-search"></a>

[Texture2D](class_texture2d.md#class-texture2d) **search** [🔗](class_popupmenu.md#class-popupmenu-theme-icon-search)

[Texture2D](class_texture2d.md#class-texture2d) icon for the search bar's search icon.

---


<a id="class-popupmenu-theme-icon-submenu"></a>

[Texture2D](class_texture2d.md#class-texture2d) **submenu** [🔗](class_popupmenu.md#class-popupmenu-theme-icon-submenu)

[Texture2D](class_texture2d.md#class-texture2d) icon for the submenu arrow (for left-to-right layouts).

---


<a id="class-popupmenu-theme-icon-submenu-mirrored"></a>

[Texture2D](class_texture2d.md#class-texture2d) **submenu_mirrored** [🔗](class_popupmenu.md#class-popupmenu-theme-icon-submenu-mirrored)

[Texture2D](class_texture2d.md#class-texture2d) icon for the submenu arrow (for right-to-left layouts).

---


<a id="class-popupmenu-theme-icon-unchecked"></a>

[Texture2D](class_texture2d.md#class-texture2d) **unchecked** [🔗](class_popupmenu.md#class-popupmenu-theme-icon-unchecked)

[Texture2D](class_texture2d.md#class-texture2d) icon for the unchecked checkbox items.

---


<a id="class-popupmenu-theme-icon-unchecked-disabled"></a>

[Texture2D](class_texture2d.md#class-texture2d) **unchecked_disabled** [🔗](class_popupmenu.md#class-popupmenu-theme-icon-unchecked-disabled)

[Texture2D](class_texture2d.md#class-texture2d) icon for the unchecked checkbox items when they are disabled.

---


<a id="class-popupmenu-theme-style-hover"></a>

[StyleBox](class_stylebox.md#class-stylebox) **hover** [🔗](class_popupmenu.md#class-popupmenu-theme-style-hover)

[StyleBox](class_stylebox.md#class-stylebox) displayed when the **PopupMenu** item is hovered.

---


<a id="class-popupmenu-theme-style-labeled-separator-left"></a>

[StyleBox](class_stylebox.md#class-stylebox) **labeled_separator_left** [🔗](class_popupmenu.md#class-popupmenu-theme-style-labeled-separator-left)

[StyleBox](class_stylebox.md#class-stylebox) for the left side of labeled separator. See [add_separator()](class_popupmenu.md#class-popupmenu-method-add-separator).

---


<a id="class-popupmenu-theme-style-labeled-separator-right"></a>

[StyleBox](class_stylebox.md#class-stylebox) **labeled_separator_right** [🔗](class_popupmenu.md#class-popupmenu-theme-style-labeled-separator-right)

[StyleBox](class_stylebox.md#class-stylebox) for the right side of labeled separator. See [add_separator()](class_popupmenu.md#class-popupmenu-method-add-separator).

---


<a id="class-popupmenu-theme-style-panel"></a>

[StyleBox](class_stylebox.md#class-stylebox) **panel** [🔗](class_popupmenu.md#class-popupmenu-theme-style-panel)

[StyleBox](class_stylebox.md#class-stylebox) for the background panel.

---


<a id="class-popupmenu-theme-style-separator"></a>

[StyleBox](class_stylebox.md#class-stylebox) **separator** [🔗](class_popupmenu.md#class-popupmenu-theme-style-separator)

[StyleBox](class_stylebox.md#class-stylebox) used for the separators. See [add_separator()](class_popupmenu.md#class-popupmenu-method-add-separator).
