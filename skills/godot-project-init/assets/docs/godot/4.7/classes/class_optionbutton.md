> Source: https://docs.godotengine.org/en/4.7/classes/class_optionbutton.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="optionbutton"></a>

<a id="class-optionbutton"></a>

# OptionButton

**Inherits:** [Button](class_button.md#class-button) **<** [BaseButton](class_basebutton.md#class-basebutton) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A button that brings up a dropdown with selectable options when pressed.

<a id="description"></a>

## Description

**OptionButton** is a type of button that brings up a dropdown with selectable items when pressed. The item selected becomes the "current" item and is displayed as the button text.

See also [BaseButton](class_basebutton.md#class-basebutton) which contains common properties and methods associated with this node.

**Note:** The IDs used for items are limited to signed 32-bit integers, not the full 64 bits of [int](class_int.md#class-int). These have a range of `-2^31` to `2^31 - 1`, that is, `-2147483648` to `2147483647`.

**Note:** The [Button.text](class_button.md#class-button-property-text) and [Button.icon](class_button.md#class-button-property-icon) properties are set automatically based on the selected item. They shouldn't be changed manually.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [ActionMode](class_basebutton.md#enum-basebutton-actionmode) | action_mode | `0` (overrides [BaseButton](class_basebutton.md#class-basebutton-property-action-mode)) |
| [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) | alignment | `0` (overrides [Button](class_button.md#class-button-property-alignment)) |
| [bool](class_bool.md#class-bool) | [allow_reselect](class_optionbutton.md#class-optionbutton-property-allow-reselect) | `false` |
| [bool](class_bool.md#class-bool) | [fit_to_longest_item](class_optionbutton.md#class-optionbutton-property-fit-to-longest-item) | `true` |
| [int](class_int.md#class-int) | [item_count](class_optionbutton.md#class-optionbutton-property-item-count) | `0` |
| [bool](class_bool.md#class-bool) | [popup/item_{index}/disabled](class_optionbutton.md#class-optionbutton-property-popup-item-index-disabled) | `false` |
| [Texture2D](class_texture2d.md#class-texture2d) | [popup/item_{index}/icon](class_optionbutton.md#class-optionbutton-property-popup-item-index-icon) |  |
| [int](class_int.md#class-int) | [popup/item_{index}/id](class_optionbutton.md#class-optionbutton-property-popup-item-index-id) | `0` |
| [bool](class_bool.md#class-bool) | [popup/item_{index}/separator](class_optionbutton.md#class-optionbutton-property-popup-item-index-separator) | `false` |
| [String](class_string.md#class-string) | [popup/item_{index}/text](class_optionbutton.md#class-optionbutton-property-popup-item-index-text) | `""` |
| [bool](class_bool.md#class-bool) | [search_bar_enabled](class_optionbutton.md#class-optionbutton-property-search-bar-enabled) | `false` |
| [bool](class_bool.md#class-bool) | [search_bar_fuzzy_search_enabled](class_optionbutton.md#class-optionbutton-property-search-bar-fuzzy-search-enabled) | `true` |
| [int](class_int.md#class-int) | [search_bar_fuzzy_search_max_misses](class_optionbutton.md#class-optionbutton-property-search-bar-fuzzy-search-max-misses) | `2` |
| [int](class_int.md#class-int) | [search_bar_min_item_count](class_optionbutton.md#class-optionbutton-property-search-bar-min-item-count) | `0` |
| [int](class_int.md#class-int) | [selected](class_optionbutton.md#class-optionbutton-property-selected) | `-1` |
| [bool](class_bool.md#class-bool) | toggle_mode | `true` (overrides [BaseButton](class_basebutton.md#class-basebutton-property-toggle-mode)) |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_icon_item](class_optionbutton.md#class-optionbutton-method-add-icon-item)(texture: [Texture2D](class_texture2d.md#class-texture2d), label: [String](class_string.md#class-string), id: [int](class_int.md#class-int) = -1) |
| void | [add_item](class_optionbutton.md#class-optionbutton-method-add-item)(label: [String](class_string.md#class-string), id: [int](class_int.md#class-int) = -1) |
| void | [add_separator](class_optionbutton.md#class-optionbutton-method-add-separator)(text: [String](class_string.md#class-string) = "") |
| void | [clear](class_optionbutton.md#class-optionbutton-method-clear)() |
| [AutoTranslateMode](class_node.md#enum-node-autotranslatemode) | [get_item_auto_translate_mode](class_optionbutton.md#class-optionbutton-method-get-item-auto-translate-mode)(idx: [int](class_int.md#class-int)) const |
| [Texture2D](class_texture2d.md#class-texture2d) | [get_item_icon](class_optionbutton.md#class-optionbutton-method-get-item-icon)(idx: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_item_id](class_optionbutton.md#class-optionbutton-method-get-item-id)(idx: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_item_index](class_optionbutton.md#class-optionbutton-method-get-item-index)(id: [int](class_int.md#class-int)) const |
| [Variant](class_variant.md#class-variant) | [get_item_metadata](class_optionbutton.md#class-optionbutton-method-get-item-metadata)(idx: [int](class_int.md#class-int)) const |
| [String](class_string.md#class-string) | [get_item_text](class_optionbutton.md#class-optionbutton-method-get-item-text)(idx: [int](class_int.md#class-int)) const |
| [String](class_string.md#class-string) | [get_item_tooltip](class_optionbutton.md#class-optionbutton-method-get-item-tooltip)(idx: [int](class_int.md#class-int)) const |
| [PopupMenu](class_popupmenu.md#class-popupmenu) | [get_popup](class_optionbutton.md#class-optionbutton-method-get-popup)() const |
| [int](class_int.md#class-int) | [get_selectable_item](class_optionbutton.md#class-optionbutton-method-get-selectable-item)(from_last: [bool](class_bool.md#class-bool) = false) const |
| [int](class_int.md#class-int) | [get_selected_id](class_optionbutton.md#class-optionbutton-method-get-selected-id)() const |
| [Variant](class_variant.md#class-variant) | [get_selected_metadata](class_optionbutton.md#class-optionbutton-method-get-selected-metadata)() const |
| [bool](class_bool.md#class-bool) | [has_selectable_items](class_optionbutton.md#class-optionbutton-method-has-selectable-items)() const |
| [bool](class_bool.md#class-bool) | [is_item_disabled](class_optionbutton.md#class-optionbutton-method-is-item-disabled)(idx: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [is_item_separator](class_optionbutton.md#class-optionbutton-method-is-item-separator)(idx: [int](class_int.md#class-int)) const |
| void | [remove_item](class_optionbutton.md#class-optionbutton-method-remove-item)(idx: [int](class_int.md#class-int)) |
| void | [select](class_optionbutton.md#class-optionbutton-method-select)(idx: [int](class_int.md#class-int)) |
| void | [set_disable_shortcuts](class_optionbutton.md#class-optionbutton-method-set-disable-shortcuts)(disabled: [bool](class_bool.md#class-bool)) |
| void | [set_item_auto_translate_mode](class_optionbutton.md#class-optionbutton-method-set-item-auto-translate-mode)(idx: [int](class_int.md#class-int), mode: [AutoTranslateMode](class_node.md#enum-node-autotranslatemode)) |
| void | [set_item_disabled](class_optionbutton.md#class-optionbutton-method-set-item-disabled)(idx: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool)) |
| void | [set_item_icon](class_optionbutton.md#class-optionbutton-method-set-item-icon)(idx: [int](class_int.md#class-int), texture: [Texture2D](class_texture2d.md#class-texture2d)) |
| void | [set_item_id](class_optionbutton.md#class-optionbutton-method-set-item-id)(idx: [int](class_int.md#class-int), id: [int](class_int.md#class-int)) |
| void | [set_item_metadata](class_optionbutton.md#class-optionbutton-method-set-item-metadata)(idx: [int](class_int.md#class-int), metadata: [Variant](class_variant.md#class-variant)) |
| void | [set_item_text](class_optionbutton.md#class-optionbutton-method-set-item-text)(idx: [int](class_int.md#class-int), text: [String](class_string.md#class-string)) |
| void | [set_item_tooltip](class_optionbutton.md#class-optionbutton-method-set-item-tooltip)(idx: [int](class_int.md#class-int), tooltip: [String](class_string.md#class-string)) |
| void | [show_popup](class_optionbutton.md#class-optionbutton-method-show-popup)() |

<a id="theme-properties"></a>

## Theme Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [arrow_margin](class_optionbutton.md#class-optionbutton-theme-constant-arrow-margin) | `4` |
| [int](class_int.md#class-int) | [modulate_arrow](class_optionbutton.md#class-optionbutton-theme-constant-modulate-arrow) | `0` |
| [Texture2D](class_texture2d.md#class-texture2d) | [arrow](class_optionbutton.md#class-optionbutton-theme-icon-arrow) |  |

---


<a id="signals"></a>

## Signals

<a id="class-optionbutton-signal-item-focused"></a>

**item_focused**(index: [int](class_int.md#class-int)) [🔗](class_optionbutton.md#class-optionbutton-signal-item-focused)

Emitted when the user navigates to an item using the [ProjectSettings.input/ui_up](class_projectsettings.md#class-projectsettings-property-input-ui-up) or [ProjectSettings.input/ui_down](class_projectsettings.md#class-projectsettings-property-input-ui-down) input actions. The index of the item focused is passed as argument.

---


<a id="class-optionbutton-signal-item-selected"></a>

**item_selected**(index: [int](class_int.md#class-int)) [🔗](class_optionbutton.md#class-optionbutton-signal-item-selected)

Emitted when the current item has been changed by the user. The index of the item selected is passed as argument.

[allow_reselect](class_optionbutton.md#class-optionbutton-property-allow-reselect) must be enabled to reselect an item.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-optionbutton-property-allow-reselect"></a>

[bool](class_bool.md#class-bool) **allow_reselect** = `false` [🔗](class_optionbutton.md#class-optionbutton-property-allow-reselect)

- void **set_allow_reselect**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_allow_reselect**()

If `true`, the currently selected item can be selected again.

---


<a id="class-optionbutton-property-fit-to-longest-item"></a>

[bool](class_bool.md#class-bool) **fit_to_longest_item** = `true` [🔗](class_optionbutton.md#class-optionbutton-property-fit-to-longest-item)

- void **set_fit_to_longest_item**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_fit_to_longest_item**()

If `true`, minimum size will be determined by the longest item's text, instead of the currently selected one's.

**Note:** For performance reasons, the minimum size doesn't update immediately when adding, removing or modifying items.

---


<a id="class-optionbutton-property-item-count"></a>

[int](class_int.md#class-int) **item_count** = `0` [🔗](class_optionbutton.md#class-optionbutton-property-item-count)

- void **set_item_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_item_count**()

The number of items to select from.

---


<a id="class-optionbutton-property-popup-item-index-disabled"></a>

[bool](class_bool.md#class-bool) **popup/item_{index}/disabled** = `false` [🔗](class_optionbutton.md#class-optionbutton-property-popup-item-index-disabled)

If `true`, the item at `index` is disabled.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

---


<a id="class-optionbutton-property-popup-item-index-icon"></a>

[Texture2D](class_texture2d.md#class-texture2d) **popup/item_{index}/icon** [🔗](class_optionbutton.md#class-optionbutton-property-popup-item-index-icon)

The icon of the item at `index`.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

---


<a id="class-optionbutton-property-popup-item-index-id"></a>

[int](class_int.md#class-int) **popup/item_{index}/id** = `0` [🔗](class_optionbutton.md#class-optionbutton-property-popup-item-index-id)

The ID of the item at `index`.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

---


<a id="class-optionbutton-property-popup-item-index-separator"></a>

[bool](class_bool.md#class-bool) **popup/item_{index}/separator** = `false` [🔗](class_optionbutton.md#class-optionbutton-property-popup-item-index-separator)

If `true`, the item at `index` is a separator.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

---


<a id="class-optionbutton-property-popup-item-index-text"></a>

[String](class_string.md#class-string) **popup/item_{index}/text** = `""` [🔗](class_optionbutton.md#class-optionbutton-property-popup-item-index-text)

The text of the item at `index`.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

---


<a id="class-optionbutton-property-search-bar-enabled"></a>

[bool](class_bool.md#class-bool) **search_bar_enabled** = `false` [🔗](class_optionbutton.md#class-optionbutton-property-search-bar-enabled)

- void **set_search_bar_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_search_bar_enabled**()

If `true`, shows a search bar at the top of the [PopupMenu](class_popupmenu.md#class-popupmenu) for filtering items. See [search_bar_min_item_count](class_optionbutton.md#class-optionbutton-property-search-bar-min-item-count) for dynamically controlling its visibility based on the number of items.

---


<a id="class-optionbutton-property-search-bar-fuzzy-search-enabled"></a>

[bool](class_bool.md#class-bool) **search_bar_fuzzy_search_enabled** = `true` [🔗](class_optionbutton.md#class-optionbutton-property-search-bar-fuzzy-search-enabled)

- void **set_search_bar_fuzzy_search_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_search_bar_fuzzy_search_enabled**()

If `true`, enables fuzzy searching in the [PopupMenu](class_popupmenu.md#class-popupmenu) search bar. This allows the search results to include items that almost match the search query, as well items that match the individual characters of the search query, but not in sequence.

Use [search_bar_fuzzy_search_max_misses](class_optionbutton.md#class-optionbutton-property-search-bar-fuzzy-search-max-misses) to set the maximum number of mismatches allowed in the search results.

---


<a id="class-optionbutton-property-search-bar-fuzzy-search-max-misses"></a>

[int](class_int.md#class-int) **search_bar_fuzzy_search_max_misses** = `2` [🔗](class_optionbutton.md#class-optionbutton-property-search-bar-fuzzy-search-max-misses)

- void **set_search_bar_fuzzy_search_max_misses**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_search_bar_fuzzy_search_max_misses**()

Sets the maximum number of mismatches allowed in each search result when fuzzy searching is enabled for the [PopupMenu](class_popupmenu.md#class-popupmenu) search bar. Any item with more mismatches will be hidden from the search results.

---


<a id="class-optionbutton-property-search-bar-min-item-count"></a>

[int](class_int.md#class-int) **search_bar_min_item_count** = `0` [🔗](class_optionbutton.md#class-optionbutton-property-search-bar-min-item-count)

- void **set_search_bar_min_item_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_search_bar_min_item_count**()

Sets the minimum number of items required for the [PopupMenu](class_popupmenu.md#class-popupmenu) search bar to be visible. [search_bar_enabled](class_optionbutton.md#class-optionbutton-property-search-bar-enabled) must be `true` for this to have any effect.

---


<a id="class-optionbutton-property-selected"></a>

[int](class_int.md#class-int) **selected** = `-1` [🔗](class_optionbutton.md#class-optionbutton-property-selected)

- [int](class_int.md#class-int) **get_selected**()

The index of the currently selected item, or `-1` if no item is selected.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-optionbutton-method-add-icon-item"></a>

void **add_icon_item**(texture: [Texture2D](class_texture2d.md#class-texture2d), label: [String](class_string.md#class-string), id: [int](class_int.md#class-int) = -1) [🔗](class_optionbutton.md#class-optionbutton-method-add-icon-item)

Adds an item, with a `texture` icon, text `label` and (optionally) `id`. If no `id` is passed, the item index will be used as the item's ID. New items are appended at the end.

**Note:** The item will be selected if there are no other items.

---


<a id="class-optionbutton-method-add-item"></a>

void **add_item**(label: [String](class_string.md#class-string), id: [int](class_int.md#class-int) = -1) [🔗](class_optionbutton.md#class-optionbutton-method-add-item)

Adds an item, with text `label` and (optionally) `id`. If no `id` is passed, the item index will be used as the item's ID. New items are appended at the end.

**Note:** The item will be selected if there are no other items.

---


<a id="class-optionbutton-method-add-separator"></a>

void **add_separator**(text: [String](class_string.md#class-string) = "") [🔗](class_optionbutton.md#class-optionbutton-method-add-separator)

Adds a separator to the list of items. Separators help to group items, and can optionally be given a `text` header. A separator also gets an index assigned, and is appended at the end of the item list.

---


<a id="class-optionbutton-method-clear"></a>

void **clear**() [🔗](class_optionbutton.md#class-optionbutton-method-clear)

Clears all the items in the **OptionButton**.

---


<a id="class-optionbutton-method-get-item-auto-translate-mode"></a>

[AutoTranslateMode](class_node.md#enum-node-autotranslatemode) **get_item_auto_translate_mode**(idx: [int](class_int.md#class-int)) const [🔗](class_optionbutton.md#class-optionbutton-method-get-item-auto-translate-mode)

Returns the auto translate mode of the item at index `idx`.

---


<a id="class-optionbutton-method-get-item-icon"></a>

[Texture2D](class_texture2d.md#class-texture2d) **get_item_icon**(idx: [int](class_int.md#class-int)) const [🔗](class_optionbutton.md#class-optionbutton-method-get-item-icon)

Returns the icon of the item at index `idx`.

---


<a id="class-optionbutton-method-get-item-id"></a>

[int](class_int.md#class-int) **get_item_id**(idx: [int](class_int.md#class-int)) const [🔗](class_optionbutton.md#class-optionbutton-method-get-item-id)

Returns the ID of the item at index `idx`.

---


<a id="class-optionbutton-method-get-item-index"></a>

[int](class_int.md#class-int) **get_item_index**(id: [int](class_int.md#class-int)) const [🔗](class_optionbutton.md#class-optionbutton-method-get-item-index)

Returns the index of the item with the given `id`.

---


<a id="class-optionbutton-method-get-item-metadata"></a>

[Variant](class_variant.md#class-variant) **get_item_metadata**(idx: [int](class_int.md#class-int)) const [🔗](class_optionbutton.md#class-optionbutton-method-get-item-metadata)

Retrieves the metadata of an item. Metadata may be any type and can be used to store extra information about an item, such as an external string ID.

---


<a id="class-optionbutton-method-get-item-text"></a>

[String](class_string.md#class-string) **get_item_text**(idx: [int](class_int.md#class-int)) const [🔗](class_optionbutton.md#class-optionbutton-method-get-item-text)

Returns the text of the item at index `idx`.

---


<a id="class-optionbutton-method-get-item-tooltip"></a>

[String](class_string.md#class-string) **get_item_tooltip**(idx: [int](class_int.md#class-int)) const [🔗](class_optionbutton.md#class-optionbutton-method-get-item-tooltip)

Returns the tooltip of the item at index `idx`.

---


<a id="class-optionbutton-method-get-popup"></a>

[PopupMenu](class_popupmenu.md#class-popupmenu) **get_popup**() const [🔗](class_optionbutton.md#class-optionbutton-method-get-popup)

Returns the [PopupMenu](class_popupmenu.md#class-popupmenu) contained in this button.

**Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [Window.visible](class_window.md#class-window-property-visible) property.

---


<a id="class-optionbutton-method-get-selectable-item"></a>

[int](class_int.md#class-int) **get_selectable_item**(from_last: [bool](class_bool.md#class-bool) = false) const [🔗](class_optionbutton.md#class-optionbutton-method-get-selectable-item)

Returns the index of the first item which is not disabled, or marked as a separator. If `from_last` is `true`, the items will be searched in reverse order.

Returns `-1` if no item is found.

---


<a id="class-optionbutton-method-get-selected-id"></a>

[int](class_int.md#class-int) **get_selected_id**() const [🔗](class_optionbutton.md#class-optionbutton-method-get-selected-id)

Returns the ID of the selected item, or `-1` if no item is selected.

---


<a id="class-optionbutton-method-get-selected-metadata"></a>

[Variant](class_variant.md#class-variant) **get_selected_metadata**() const [🔗](class_optionbutton.md#class-optionbutton-method-get-selected-metadata)

Gets the metadata of the selected item. Metadata for items can be set using [set_item_metadata()](class_optionbutton.md#class-optionbutton-method-set-item-metadata).

---


<a id="class-optionbutton-method-has-selectable-items"></a>

[bool](class_bool.md#class-bool) **has_selectable_items**() const [🔗](class_optionbutton.md#class-optionbutton-method-has-selectable-items)

Returns `true` if this button contains at least one item which is not disabled, or marked as a separator.

---


<a id="class-optionbutton-method-is-item-disabled"></a>

[bool](class_bool.md#class-bool) **is_item_disabled**(idx: [int](class_int.md#class-int)) const [🔗](class_optionbutton.md#class-optionbutton-method-is-item-disabled)

Returns `true` if the item at index `idx` is disabled.

---


<a id="class-optionbutton-method-is-item-separator"></a>

[bool](class_bool.md#class-bool) **is_item_separator**(idx: [int](class_int.md#class-int)) const [🔗](class_optionbutton.md#class-optionbutton-method-is-item-separator)

Returns `true` if the item at index `idx` is marked as a separator.

---


<a id="class-optionbutton-method-remove-item"></a>

void **remove_item**(idx: [int](class_int.md#class-int)) [🔗](class_optionbutton.md#class-optionbutton-method-remove-item)

Removes the item at index `idx`.

---


<a id="class-optionbutton-method-select"></a>

void **select**(idx: [int](class_int.md#class-int)) [🔗](class_optionbutton.md#class-optionbutton-method-select)

Selects an item by index and makes it the current item. This will work even if the item is disabled.

Passing `-1` as the index deselects any currently selected item.

---


<a id="class-optionbutton-method-set-disable-shortcuts"></a>

void **set_disable_shortcuts**(disabled: [bool](class_bool.md#class-bool)) [🔗](class_optionbutton.md#class-optionbutton-method-set-disable-shortcuts)

If `true`, shortcuts are disabled and cannot be used to trigger the button.

---


<a id="class-optionbutton-method-set-item-auto-translate-mode"></a>

void **set_item_auto_translate_mode**(idx: [int](class_int.md#class-int), mode: [AutoTranslateMode](class_node.md#enum-node-autotranslatemode)) [🔗](class_optionbutton.md#class-optionbutton-method-set-item-auto-translate-mode)

Sets the auto translate mode of the item at index `idx`.

Items use [Node.AUTO_TRANSLATE_MODE_INHERIT](class_node.md#class-node-constant-auto-translate-mode-inherit) by default, which uses the same auto translate mode as the **OptionButton** itself.

---


<a id="class-optionbutton-method-set-item-disabled"></a>

void **set_item_disabled**(idx: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool)) [🔗](class_optionbutton.md#class-optionbutton-method-set-item-disabled)

Sets whether the item at index `idx` is disabled.

Disabled items are drawn differently in the dropdown and are not selectable by the user. If the current selected item is set as disabled, it will remain selected.

---


<a id="class-optionbutton-method-set-item-icon"></a>

void **set_item_icon**(idx: [int](class_int.md#class-int), texture: [Texture2D](class_texture2d.md#class-texture2d)) [🔗](class_optionbutton.md#class-optionbutton-method-set-item-icon)

Sets the icon of the item at index `idx`.

---


<a id="class-optionbutton-method-set-item-id"></a>

void **set_item_id**(idx: [int](class_int.md#class-int), id: [int](class_int.md#class-int)) [🔗](class_optionbutton.md#class-optionbutton-method-set-item-id)

Sets the ID of the item at index `idx`.

---


<a id="class-optionbutton-method-set-item-metadata"></a>

void **set_item_metadata**(idx: [int](class_int.md#class-int), metadata: [Variant](class_variant.md#class-variant)) [🔗](class_optionbutton.md#class-optionbutton-method-set-item-metadata)

Sets the metadata of an item. Metadata may be of any type and can be used to store extra information about an item, such as an external string ID.

---


<a id="class-optionbutton-method-set-item-text"></a>

void **set_item_text**(idx: [int](class_int.md#class-int), text: [String](class_string.md#class-string)) [🔗](class_optionbutton.md#class-optionbutton-method-set-item-text)

Sets the text of the item at index `idx`.

---


<a id="class-optionbutton-method-set-item-tooltip"></a>

void **set_item_tooltip**(idx: [int](class_int.md#class-int), tooltip: [String](class_string.md#class-string)) [🔗](class_optionbutton.md#class-optionbutton-method-set-item-tooltip)

Sets the tooltip of the item at index `idx`.

---


<a id="class-optionbutton-method-show-popup"></a>

void **show_popup**() [🔗](class_optionbutton.md#class-optionbutton-method-show-popup)

Adjusts popup position and sizing for the **OptionButton**, then shows the [PopupMenu](class_popupmenu.md#class-popupmenu). Prefer this over using `get_popup().popup()`.

---


<a id="theme-property-descriptions"></a>

## Theme Property Descriptions

<a id="class-optionbutton-theme-constant-arrow-margin"></a>

[int](class_int.md#class-int) **arrow_margin** = `4` [🔗](class_optionbutton.md#class-optionbutton-theme-constant-arrow-margin)

The horizontal space between the arrow icon and the right edge of the button.

---


<a id="class-optionbutton-theme-constant-modulate-arrow"></a>

[int](class_int.md#class-int) **modulate_arrow** = `0` [🔗](class_optionbutton.md#class-optionbutton-theme-constant-modulate-arrow)

If different than `0`, the arrow icon will be modulated to the font color.

---


<a id="class-optionbutton-theme-icon-arrow"></a>

[Texture2D](class_texture2d.md#class-texture2d) **arrow** [🔗](class_optionbutton.md#class-optionbutton-theme-icon-arrow)

The arrow icon to be drawn on the right end of the button.
