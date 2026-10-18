> Source: https://docs.godotengine.org/en/4.7/classes/class_accessibilityserver.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="accessibilityserver"></a>

<a id="class-accessibilityserver"></a>

# AccessibilityServer

**Inherits:** [Object](class_object.md#class-object)

A server interface for screen reader support.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [RID](class_rid.md#class-rid) | [create_element](class_accessibilityserver.md#class-accessibilityserver-method-create-element)(window_id: [int](class_int.md#class-int), role: [AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole)) |
| [RID](class_rid.md#class-rid) | [create_sub_element](class_accessibilityserver.md#class-accessibilityserver-method-create-sub-element)(parent_rid: [RID](class_rid.md#class-rid), role: [AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole), insert_pos: [int](class_int.md#class-int) = -1) |
| [RID](class_rid.md#class-rid) | [create_sub_text_edit_elements](class_accessibilityserver.md#class-accessibilityserver-method-create-sub-text-edit-elements)(parent_rid: [RID](class_rid.md#class-rid), shaped_text: [RID](class_rid.md#class-rid), min_height: [float](class_float.md#class-float), insert_pos: [int](class_int.md#class-int) = -1, is_last_line: [bool](class_bool.md#class-bool) = false) |
| [Variant](class_variant.md#class-variant) | [element_get_meta](class_accessibilityserver.md#class-accessibilityserver-method-element-get-meta)(id: [RID](class_rid.md#class-rid)) const |
| void | [element_set_meta](class_accessibilityserver.md#class-accessibilityserver-method-element-set-meta)(id: [RID](class_rid.md#class-rid), meta: [Variant](class_variant.md#class-variant)) |
| void | [free_element](class_accessibilityserver.md#class-accessibilityserver-method-free-element)(id: [RID](class_rid.md#class-rid)) |
| [RID](class_rid.md#class-rid) | [get_window_root](class_accessibilityserver.md#class-accessibilityserver-method-get-window-root)(window_id: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [has_element](class_accessibilityserver.md#class-accessibilityserver-method-has-element)(id: [RID](class_rid.md#class-rid)) const |
| [bool](class_bool.md#class-bool) | [is_supported](class_accessibilityserver.md#class-accessibilityserver-method-is-supported)() const |
| void | [set_window_focused](class_accessibilityserver.md#class-accessibilityserver-method-set-window-focused)(window_id: [int](class_int.md#class-int), focused: [bool](class_bool.md#class-bool)) |
| void | [set_window_rect](class_accessibilityserver.md#class-accessibilityserver-method-set-window-rect)(window_id: [int](class_int.md#class-int), rect_out: [Rect2](class_rect2.md#class-rect2), rect_in: [Rect2](class_rect2.md#class-rect2)) |
| void | [update_add_action](class_accessibilityserver.md#class-accessibilityserver-method-update-add-action)(id: [RID](class_rid.md#class-rid), action: [AccessibilityAction](class_accessibilityserver.md#enum-accessibilityserver-accessibilityaction), callable: [Callable](class_callable.md#class-callable)) |
| void | [update_add_child](class_accessibilityserver.md#class-accessibilityserver-method-update-add-child)(id: [RID](class_rid.md#class-rid), child_id: [RID](class_rid.md#class-rid)) |
| void | [update_add_custom_action](class_accessibilityserver.md#class-accessibilityserver-method-update-add-custom-action)(id: [RID](class_rid.md#class-rid), action_id: [int](class_int.md#class-int), action_description: [String](class_string.md#class-string)) |
| void | [update_add_related_controls](class_accessibilityserver.md#class-accessibilityserver-method-update-add-related-controls)(id: [RID](class_rid.md#class-rid), related_id: [RID](class_rid.md#class-rid)) |
| void | [update_add_related_described_by](class_accessibilityserver.md#class-accessibilityserver-method-update-add-related-described-by)(id: [RID](class_rid.md#class-rid), related_id: [RID](class_rid.md#class-rid)) |
| void | [update_add_related_details](class_accessibilityserver.md#class-accessibilityserver-method-update-add-related-details)(id: [RID](class_rid.md#class-rid), related_id: [RID](class_rid.md#class-rid)) |
| void | [update_add_related_flow_to](class_accessibilityserver.md#class-accessibilityserver-method-update-add-related-flow-to)(id: [RID](class_rid.md#class-rid), related_id: [RID](class_rid.md#class-rid)) |
| void | [update_add_related_labeled_by](class_accessibilityserver.md#class-accessibilityserver-method-update-add-related-labeled-by)(id: [RID](class_rid.md#class-rid), related_id: [RID](class_rid.md#class-rid)) |
| void | [update_add_related_radio_group](class_accessibilityserver.md#class-accessibilityserver-method-update-add-related-radio-group)(id: [RID](class_rid.md#class-rid), related_id: [RID](class_rid.md#class-rid)) |
| void | [update_set_active_descendant](class_accessibilityserver.md#class-accessibilityserver-method-update-set-active-descendant)(id: [RID](class_rid.md#class-rid), other_id: [RID](class_rid.md#class-rid)) |
| void | [update_set_background_color](class_accessibilityserver.md#class-accessibilityserver-method-update-set-background-color)(id: [RID](class_rid.md#class-rid), color: [Color](class_color.md#class-color)) |
| void | [update_set_bounds](class_accessibilityserver.md#class-accessibilityserver-method-update-set-bounds)(id: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2)) |
| void | [update_set_braille_label](class_accessibilityserver.md#class-accessibilityserver-method-update-set-braille-label)(id: [RID](class_rid.md#class-rid), name: [String](class_string.md#class-string)) |
| void | [update_set_braille_role_description](class_accessibilityserver.md#class-accessibilityserver-method-update-set-braille-role-description)(id: [RID](class_rid.md#class-rid), description: [String](class_string.md#class-string)) |
| void | [update_set_checked](class_accessibilityserver.md#class-accessibilityserver-method-update-set-checked)(id: [RID](class_rid.md#class-rid), checekd: [bool](class_bool.md#class-bool)) |
| void | [update_set_classname](class_accessibilityserver.md#class-accessibilityserver-method-update-set-classname)(id: [RID](class_rid.md#class-rid), classname: [String](class_string.md#class-string)) |
| void | [update_set_color_value](class_accessibilityserver.md#class-accessibilityserver-method-update-set-color-value)(id: [RID](class_rid.md#class-rid), color: [Color](class_color.md#class-color)) |
| void | [update_set_description](class_accessibilityserver.md#class-accessibilityserver-method-update-set-description)(id: [RID](class_rid.md#class-rid), description: [String](class_string.md#class-string)) |
| void | [update_set_error_message](class_accessibilityserver.md#class-accessibilityserver-method-update-set-error-message)(id: [RID](class_rid.md#class-rid), other_id: [RID](class_rid.md#class-rid)) |
| void | [update_set_extra_info](class_accessibilityserver.md#class-accessibilityserver-method-update-set-extra-info)(id: [RID](class_rid.md#class-rid), name: [String](class_string.md#class-string)) |
| void | [update_set_flag](class_accessibilityserver.md#class-accessibilityserver-method-update-set-flag)(id: [RID](class_rid.md#class-rid), flag: [AccessibilityFlags](class_accessibilityserver.md#enum-accessibilityserver-accessibilityflags), value: [bool](class_bool.md#class-bool)) |
| void | [update_set_focus](class_accessibilityserver.md#class-accessibilityserver-method-update-set-focus)(id: [RID](class_rid.md#class-rid)) |
| void | [update_set_foreground_color](class_accessibilityserver.md#class-accessibilityserver-method-update-set-foreground-color)(id: [RID](class_rid.md#class-rid), color: [Color](class_color.md#class-color)) |
| void | [update_set_in_page_link_target](class_accessibilityserver.md#class-accessibilityserver-method-update-set-in-page-link-target)(id: [RID](class_rid.md#class-rid), other_id: [RID](class_rid.md#class-rid)) |
| void | [update_set_language](class_accessibilityserver.md#class-accessibilityserver-method-update-set-language)(id: [RID](class_rid.md#class-rid), language: [String](class_string.md#class-string)) |
| void | [update_set_list_item_count](class_accessibilityserver.md#class-accessibilityserver-method-update-set-list-item-count)(id: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int)) |
| void | [update_set_list_item_expanded](class_accessibilityserver.md#class-accessibilityserver-method-update-set-list-item-expanded)(id: [RID](class_rid.md#class-rid), expanded: [bool](class_bool.md#class-bool)) |
| void | [update_set_list_item_index](class_accessibilityserver.md#class-accessibilityserver-method-update-set-list-item-index)(id: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) |
| void | [update_set_list_item_level](class_accessibilityserver.md#class-accessibilityserver-method-update-set-list-item-level)(id: [RID](class_rid.md#class-rid), level: [int](class_int.md#class-int)) |
| void | [update_set_list_item_selected](class_accessibilityserver.md#class-accessibilityserver-method-update-set-list-item-selected)(id: [RID](class_rid.md#class-rid), selected: [bool](class_bool.md#class-bool)) |
| void | [update_set_list_orientation](class_accessibilityserver.md#class-accessibilityserver-method-update-set-list-orientation)(id: [RID](class_rid.md#class-rid), vertical: [bool](class_bool.md#class-bool)) |
| void | [update_set_live](class_accessibilityserver.md#class-accessibilityserver-method-update-set-live)(id: [RID](class_rid.md#class-rid), live: [AccessibilityLiveMode](class_accessibilityserver.md#enum-accessibilityserver-accessibilitylivemode)) |
| void | [update_set_member_of](class_accessibilityserver.md#class-accessibilityserver-method-update-set-member-of)(id: [RID](class_rid.md#class-rid), group_id: [RID](class_rid.md#class-rid)) |
| void | [update_set_name](class_accessibilityserver.md#class-accessibilityserver-method-update-set-name)(id: [RID](class_rid.md#class-rid), name: [String](class_string.md#class-string)) |
| void | [update_set_next_on_line](class_accessibilityserver.md#class-accessibilityserver-method-update-set-next-on-line)(id: [RID](class_rid.md#class-rid), other_id: [RID](class_rid.md#class-rid)) |
| void | [update_set_num_jump](class_accessibilityserver.md#class-accessibilityserver-method-update-set-num-jump)(id: [RID](class_rid.md#class-rid), jump: [float](class_float.md#class-float)) |
| void | [update_set_num_range](class_accessibilityserver.md#class-accessibilityserver-method-update-set-num-range)(id: [RID](class_rid.md#class-rid), min: [float](class_float.md#class-float), max: [float](class_float.md#class-float)) |
| void | [update_set_num_step](class_accessibilityserver.md#class-accessibilityserver-method-update-set-num-step)(id: [RID](class_rid.md#class-rid), step: [float](class_float.md#class-float)) |
| void | [update_set_num_value](class_accessibilityserver.md#class-accessibilityserver-method-update-set-num-value)(id: [RID](class_rid.md#class-rid), position: [float](class_float.md#class-float)) |
| void | [update_set_placeholder](class_accessibilityserver.md#class-accessibilityserver-method-update-set-placeholder)(id: [RID](class_rid.md#class-rid), placeholder: [String](class_string.md#class-string)) |
| void | [update_set_popup_type](class_accessibilityserver.md#class-accessibilityserver-method-update-set-popup-type)(id: [RID](class_rid.md#class-rid), popup: [AccessibilityPopupType](class_accessibilityserver.md#enum-accessibilityserver-accessibilitypopuptype)) |
| void | [update_set_previous_on_line](class_accessibilityserver.md#class-accessibilityserver-method-update-set-previous-on-line)(id: [RID](class_rid.md#class-rid), other_id: [RID](class_rid.md#class-rid)) |
| void | [update_set_role](class_accessibilityserver.md#class-accessibilityserver-method-update-set-role)(id: [RID](class_rid.md#class-rid), role: [AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole)) |
| void | [update_set_role_description](class_accessibilityserver.md#class-accessibilityserver-method-update-set-role-description)(id: [RID](class_rid.md#class-rid), description: [String](class_string.md#class-string)) |
| void | [update_set_scroll_x](class_accessibilityserver.md#class-accessibilityserver-method-update-set-scroll-x)(id: [RID](class_rid.md#class-rid), position: [float](class_float.md#class-float)) |
| void | [update_set_scroll_x_range](class_accessibilityserver.md#class-accessibilityserver-method-update-set-scroll-x-range)(id: [RID](class_rid.md#class-rid), min: [float](class_float.md#class-float), max: [float](class_float.md#class-float)) |
| void | [update_set_scroll_y](class_accessibilityserver.md#class-accessibilityserver-method-update-set-scroll-y)(id: [RID](class_rid.md#class-rid), position: [float](class_float.md#class-float)) |
| void | [update_set_scroll_y_range](class_accessibilityserver.md#class-accessibilityserver-method-update-set-scroll-y-range)(id: [RID](class_rid.md#class-rid), min: [float](class_float.md#class-float), max: [float](class_float.md#class-float)) |
| void | [update_set_shortcut](class_accessibilityserver.md#class-accessibilityserver-method-update-set-shortcut)(id: [RID](class_rid.md#class-rid), shortcut: [String](class_string.md#class-string)) |
| void | [update_set_state_description](class_accessibilityserver.md#class-accessibilityserver-method-update-set-state-description)(id: [RID](class_rid.md#class-rid), description: [String](class_string.md#class-string)) |
| void | [update_set_table_cell_position](class_accessibilityserver.md#class-accessibilityserver-method-update-set-table-cell-position)(id: [RID](class_rid.md#class-rid), row_index: [int](class_int.md#class-int), column_index: [int](class_int.md#class-int)) |
| void | [update_set_table_cell_span](class_accessibilityserver.md#class-accessibilityserver-method-update-set-table-cell-span)(id: [RID](class_rid.md#class-rid), row_span: [int](class_int.md#class-int), column_span: [int](class_int.md#class-int)) |
| void | [update_set_table_column_count](class_accessibilityserver.md#class-accessibilityserver-method-update-set-table-column-count)(id: [RID](class_rid.md#class-rid), count: [int](class_int.md#class-int)) |
| void | [update_set_table_column_index](class_accessibilityserver.md#class-accessibilityserver-method-update-set-table-column-index)(id: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) |
| void | [update_set_table_row_count](class_accessibilityserver.md#class-accessibilityserver-method-update-set-table-row-count)(id: [RID](class_rid.md#class-rid), count: [int](class_int.md#class-int)) |
| void | [update_set_table_row_index](class_accessibilityserver.md#class-accessibilityserver-method-update-set-table-row-index)(id: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) |
| void | [update_set_text_align](class_accessibilityserver.md#class-accessibilityserver-method-update-set-text-align)(id: [RID](class_rid.md#class-rid), align: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment)) |
| void | [update_set_text_decorations](class_accessibilityserver.md#class-accessibilityserver-method-update-set-text-decorations)(id: [RID](class_rid.md#class-rid), underline: [bool](class_bool.md#class-bool), strikethrough: [bool](class_bool.md#class-bool), overline: [bool](class_bool.md#class-bool), color: [Color](class_color.md#class-color) = Color(0, 0, 0, 1)) |
| void | [update_set_text_orientation](class_accessibilityserver.md#class-accessibilityserver-method-update-set-text-orientation)(id: [RID](class_rid.md#class-rid), vertical: [bool](class_bool.md#class-bool)) |
| void | [update_set_text_selection](class_accessibilityserver.md#class-accessibilityserver-method-update-set-text-selection)(id: [RID](class_rid.md#class-rid), text_start_id: [RID](class_rid.md#class-rid), start_char: [int](class_int.md#class-int), text_end_id: [RID](class_rid.md#class-rid), end_char: [int](class_int.md#class-int)) |
| void | [update_set_tooltip](class_accessibilityserver.md#class-accessibilityserver-method-update-set-tooltip)(id: [RID](class_rid.md#class-rid), tooltip: [String](class_string.md#class-string)) |
| void | [update_set_transform](class_accessibilityserver.md#class-accessibilityserver-method-update-set-transform)(id: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d)) |
| void | [update_set_url](class_accessibilityserver.md#class-accessibilityserver-method-update-set-url)(id: [RID](class_rid.md#class-rid), url: [String](class_string.md#class-string)) |
| void | [update_set_value](class_accessibilityserver.md#class-accessibilityserver-method-update-set-value)(id: [RID](class_rid.md#class-rid), value: [String](class_string.md#class-string)) |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-accessibilityserver-accessibilityrole"></a>

enum **AccessibilityRole**: [🔗](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole)

<a id="class-accessibilityserver-constant-role-unknown"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_UNKNOWN** = `0`

Unknown or custom role.

<a id="class-accessibilityserver-constant-role-default-button"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_DEFAULT_BUTTON** = `1`

Default dialog button element.

<a id="class-accessibilityserver-constant-role-audio"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_AUDIO** = `2`

Audio player element.

<a id="class-accessibilityserver-constant-role-video"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_VIDEO** = `3`

Video player element.

<a id="class-accessibilityserver-constant-role-static-text"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_STATIC_TEXT** = `4`

Non-editable text label.

<a id="class-accessibilityserver-constant-role-container"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_CONTAINER** = `5`

Container element. Elements with this role are used for internal structure and ignored by screen readers.

<a id="class-accessibilityserver-constant-role-panel"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_PANEL** = `6`

Panel container element.

<a id="class-accessibilityserver-constant-role-button"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_BUTTON** = `7`

Button element.

<a id="class-accessibilityserver-constant-role-link"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_LINK** = `8`

Link element.

<a id="class-accessibilityserver-constant-role-check-box"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_CHECK_BOX** = `9`

Check box element.

<a id="class-accessibilityserver-constant-role-radio-button"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_RADIO_BUTTON** = `10`

Radio button element.

<a id="class-accessibilityserver-constant-role-check-button"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_CHECK_BUTTON** = `11`

Check button element.

<a id="class-accessibilityserver-constant-role-scroll-bar"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_SCROLL_BAR** = `12`

Scroll bar element.

<a id="class-accessibilityserver-constant-role-scroll-view"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_SCROLL_VIEW** = `13`

Scroll container element.

<a id="class-accessibilityserver-constant-role-splitter"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_SPLITTER** = `14`

Container splitter handle element.

<a id="class-accessibilityserver-constant-role-slider"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_SLIDER** = `15`

Slider element.

<a id="class-accessibilityserver-constant-role-spin-button"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_SPIN_BUTTON** = `16`

Spin box element.

<a id="class-accessibilityserver-constant-role-progress-indicator"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_PROGRESS_INDICATOR** = `17`

Progress indicator element.

<a id="class-accessibilityserver-constant-role-text-field"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_TEXT_FIELD** = `18`

Editable text field element.

<a id="class-accessibilityserver-constant-role-multiline-text-field"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_MULTILINE_TEXT_FIELD** = `19`

Multiline editable text field element.

<a id="class-accessibilityserver-constant-role-color-picker"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_COLOR_PICKER** = `20`

Color picker element.

<a id="class-accessibilityserver-constant-role-table"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_TABLE** = `21`

Table element.

<a id="class-accessibilityserver-constant-role-cell"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_CELL** = `22`

Table/tree cell element.

<a id="class-accessibilityserver-constant-role-row"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_ROW** = `23`

Table/tree row element.

<a id="class-accessibilityserver-constant-role-row-group"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_ROW_GROUP** = `24`

Table/tree row group element.

<a id="class-accessibilityserver-constant-role-row-header"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_ROW_HEADER** = `25`

Table/tree row header element.

<a id="class-accessibilityserver-constant-role-column-header"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_COLUMN_HEADER** = `26`

Table/tree column header element.

<a id="class-accessibilityserver-constant-role-tree"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_TREE** = `27`

Tree view element.

<a id="class-accessibilityserver-constant-role-tree-item"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_TREE_ITEM** = `28`

Tree view item element.

<a id="class-accessibilityserver-constant-role-list"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_LIST** = `29`

List element.

<a id="class-accessibilityserver-constant-role-list-item"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_LIST_ITEM** = `30`

List item element.

<a id="class-accessibilityserver-constant-role-list-box"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_LIST_BOX** = `31`

List view element.

<a id="class-accessibilityserver-constant-role-list-box-option"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_LIST_BOX_OPTION** = `32`

List view item element.

<a id="class-accessibilityserver-constant-role-tab-bar"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_TAB_BAR** = `33`

Tab bar element.

<a id="class-accessibilityserver-constant-role-tab"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_TAB** = `34`

Tab bar item element.

<a id="class-accessibilityserver-constant-role-tab-panel"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_TAB_PANEL** = `35`

Tab panel element.

<a id="class-accessibilityserver-constant-role-menu-bar"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_MENU_BAR** = `36`

Menu bar element.

<a id="class-accessibilityserver-constant-role-menu"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_MENU** = `37`

Popup menu element.

<a id="class-accessibilityserver-constant-role-menu-item"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_MENU_ITEM** = `38`

Popup menu item element.

<a id="class-accessibilityserver-constant-role-menu-item-check-box"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_MENU_ITEM_CHECK_BOX** = `39`

Popup menu check button item element.

<a id="class-accessibilityserver-constant-role-menu-item-radio"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_MENU_ITEM_RADIO** = `40`

Popup menu radio button item element.

<a id="class-accessibilityserver-constant-role-image"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_IMAGE** = `41`

Image element.

<a id="class-accessibilityserver-constant-role-window"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_WINDOW** = `42`

Window element.

<a id="class-accessibilityserver-constant-role-title-bar"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_TITLE_BAR** = `43`

Embedded window title bar element.

<a id="class-accessibilityserver-constant-role-dialog"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_DIALOG** = `44`

Dialog window element.

<a id="class-accessibilityserver-constant-role-tooltip"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_TOOLTIP** = `45`

Tooltip element.

<a id="class-accessibilityserver-constant-role-region"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_REGION** = `46`

Region/landmark element. Screen readers can navigate between regions using landmark navigation.

<a id="class-accessibilityserver-constant-role-text-run"></a>

[AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole) **ROLE_TEXT_RUN** = `47`

Unifor text run.

Note: This role is used for internal text elements, and should not be assigned to nodes.

---


<a id="enum-accessibilityserver-accessibilitypopuptype"></a>

enum **AccessibilityPopupType**: [🔗](class_accessibilityserver.md#enum-accessibilityserver-accessibilitypopuptype)

<a id="class-accessibilityserver-constant-popup-menu"></a>

[AccessibilityPopupType](class_accessibilityserver.md#enum-accessibilityserver-accessibilitypopuptype) **POPUP_MENU** = `0`

Popup menu.

<a id="class-accessibilityserver-constant-popup-list"></a>

[AccessibilityPopupType](class_accessibilityserver.md#enum-accessibilityserver-accessibilitypopuptype) **POPUP_LIST** = `1`

Popup list.

<a id="class-accessibilityserver-constant-popup-tree"></a>

[AccessibilityPopupType](class_accessibilityserver.md#enum-accessibilityserver-accessibilitypopuptype) **POPUP_TREE** = `2`

Popup tree view.

<a id="class-accessibilityserver-constant-popup-dialog"></a>

[AccessibilityPopupType](class_accessibilityserver.md#enum-accessibilityserver-accessibilitypopuptype) **POPUP_DIALOG** = `3`

Popup dialog.

---


<a id="enum-accessibilityserver-accessibilityflags"></a>

enum **AccessibilityFlags**: [🔗](class_accessibilityserver.md#enum-accessibilityserver-accessibilityflags)

<a id="class-accessibilityserver-constant-flag-hidden"></a>

[AccessibilityFlags](class_accessibilityserver.md#enum-accessibilityserver-accessibilityflags) **FLAG_HIDDEN** = `0`

Element is hidden for accessibility tools.

<a id="class-accessibilityserver-constant-flag-multiselectable"></a>

[AccessibilityFlags](class_accessibilityserver.md#enum-accessibilityserver-accessibilityflags) **FLAG_MULTISELECTABLE** = `1`

Element supports multiple item selection.

<a id="class-accessibilityserver-constant-flag-required"></a>

[AccessibilityFlags](class_accessibilityserver.md#enum-accessibilityserver-accessibilityflags) **FLAG_REQUIRED** = `2`

Element require user input.

<a id="class-accessibilityserver-constant-flag-visited"></a>

[AccessibilityFlags](class_accessibilityserver.md#enum-accessibilityserver-accessibilityflags) **FLAG_VISITED** = `3`

Element is a visited link.

<a id="class-accessibilityserver-constant-flag-busy"></a>

[AccessibilityFlags](class_accessibilityserver.md#enum-accessibilityserver-accessibilityflags) **FLAG_BUSY** = `4`

Element content is not ready (e.g. loading).

<a id="class-accessibilityserver-constant-flag-modal"></a>

[AccessibilityFlags](class_accessibilityserver.md#enum-accessibilityserver-accessibilityflags) **FLAG_MODAL** = `5`

Element is modal window.

<a id="class-accessibilityserver-constant-flag-touch-passthrough"></a>

[AccessibilityFlags](class_accessibilityserver.md#enum-accessibilityserver-accessibilityflags) **FLAG_TOUCH_PASSTHROUGH** = `6`

Element allows touches to be passed through when a screen reader is in touch exploration mode.

<a id="class-accessibilityserver-constant-flag-readonly"></a>

[AccessibilityFlags](class_accessibilityserver.md#enum-accessibilityserver-accessibilityflags) **FLAG_READONLY** = `7`

Element is text field with selectable but read-only text.

<a id="class-accessibilityserver-constant-flag-disabled"></a>

[AccessibilityFlags](class_accessibilityserver.md#enum-accessibilityserver-accessibilityflags) **FLAG_DISABLED** = `8`

Element is disabled.

<a id="class-accessibilityserver-constant-flag-clips-children"></a>

[AccessibilityFlags](class_accessibilityserver.md#enum-accessibilityserver-accessibilityflags) **FLAG_CLIPS_CHILDREN** = `9`

Element clips children.

---


<a id="enum-accessibilityserver-accessibilityaction"></a>

enum **AccessibilityAction**: [🔗](class_accessibilityserver.md#enum-accessibilityserver-accessibilityaction)

<a id="class-accessibilityserver-constant-action-click"></a>

[AccessibilityAction](class_accessibilityserver.md#enum-accessibilityserver-accessibilityaction) **ACTION_CLICK** = `0`

Single click action, callback argument is not set.

<a id="class-accessibilityserver-constant-action-focus"></a>

[AccessibilityAction](class_accessibilityserver.md#enum-accessibilityserver-accessibilityaction) **ACTION_FOCUS** = `1`

Focus action, callback argument is not set.

<a id="class-accessibilityserver-constant-action-blur"></a>

[AccessibilityAction](class_accessibilityserver.md#enum-accessibilityserver-accessibilityaction) **ACTION_BLUR** = `2`

Blur action, callback argument is not set.

<a id="class-accessibilityserver-constant-action-collapse"></a>

[AccessibilityAction](class_accessibilityserver.md#enum-accessibilityserver-accessibilityaction) **ACTION_COLLAPSE** = `3`

Collapse action, callback argument is not set.

<a id="class-accessibilityserver-constant-action-expand"></a>

[AccessibilityAction](class_accessibilityserver.md#enum-accessibilityserver-accessibilityaction) **ACTION_EXPAND** = `4`

Expand action, callback argument is not set.

<a id="class-accessibilityserver-constant-action-decrement"></a>

[AccessibilityAction](class_accessibilityserver.md#enum-accessibilityserver-accessibilityaction) **ACTION_DECREMENT** = `5`

Decrement action, callback argument is not set.

<a id="class-accessibilityserver-constant-action-increment"></a>

[AccessibilityAction](class_accessibilityserver.md#enum-accessibilityserver-accessibilityaction) **ACTION_INCREMENT** = `6`

Increment action, callback argument is not set.

<a id="class-accessibilityserver-constant-action-hide-tooltip"></a>

[AccessibilityAction](class_accessibilityserver.md#enum-accessibilityserver-accessibilityaction) **ACTION_HIDE_TOOLTIP** = `7`

Hide tooltip action, callback argument is not set.

<a id="class-accessibilityserver-constant-action-show-tooltip"></a>

[AccessibilityAction](class_accessibilityserver.md#enum-accessibilityserver-accessibilityaction) **ACTION_SHOW_TOOLTIP** = `8`

Show tooltip action, callback argument is not set.

<a id="class-accessibilityserver-constant-action-set-text-selection"></a>

[AccessibilityAction](class_accessibilityserver.md#enum-accessibilityserver-accessibilityaction) **ACTION_SET_TEXT_SELECTION** = `9`

Set text selection action, callback argument is set to [Dictionary](class_dictionary.md#class-dictionary) with the following keys:

- `"start_element"` accessibility element of the selection start.
- `"start_char"` character offset relative to the accessibility element of the selection start.
- `"end_element"` accessibility element of the selection end.
- `"end_char"` character offset relative to the accessibility element of the selection end.

<a id="class-accessibilityserver-constant-action-replace-selected-text"></a>

[AccessibilityAction](class_accessibilityserver.md#enum-accessibilityserver-accessibilityaction) **ACTION_REPLACE_SELECTED_TEXT** = `10`

Replace text action, callback argument is set to [String](class_string.md#class-string) with the replacement text.

<a id="class-accessibilityserver-constant-action-scroll-backward"></a>

[AccessibilityAction](class_accessibilityserver.md#enum-accessibilityserver-accessibilityaction) **ACTION_SCROLL_BACKWARD** = `11`

Scroll backward action, callback argument is not set.

<a id="class-accessibilityserver-constant-action-scroll-down"></a>

[AccessibilityAction](class_accessibilityserver.md#enum-accessibilityserver-accessibilityaction) **ACTION_SCROLL_DOWN** = `12`

Scroll down action, callback argument is set to [AccessibilityScrollUnit](class_accessibilityserver.md#enum-accessibilityserver-accessibilityscrollunit).

<a id="class-accessibilityserver-constant-action-scroll-forward"></a>

[AccessibilityAction](class_accessibilityserver.md#enum-accessibilityserver-accessibilityaction) **ACTION_SCROLL_FORWARD** = `13`

Scroll forward action, callback argument is not set.

<a id="class-accessibilityserver-constant-action-scroll-left"></a>

[AccessibilityAction](class_accessibilityserver.md#enum-accessibilityserver-accessibilityaction) **ACTION_SCROLL_LEFT** = `14`

Scroll left action, callback argument is set to [AccessibilityScrollUnit](class_accessibilityserver.md#enum-accessibilityserver-accessibilityscrollunit).

<a id="class-accessibilityserver-constant-action-scroll-right"></a>

[AccessibilityAction](class_accessibilityserver.md#enum-accessibilityserver-accessibilityaction) **ACTION_SCROLL_RIGHT** = `15`

Scroll right action, callback argument is set to [AccessibilityScrollUnit](class_accessibilityserver.md#enum-accessibilityserver-accessibilityscrollunit).

<a id="class-accessibilityserver-constant-action-scroll-up"></a>

[AccessibilityAction](class_accessibilityserver.md#enum-accessibilityserver-accessibilityaction) **ACTION_SCROLL_UP** = `16`

Scroll up action, callback argument is set to [AccessibilityScrollUnit](class_accessibilityserver.md#enum-accessibilityserver-accessibilityscrollunit).

<a id="class-accessibilityserver-constant-action-scroll-into-view"></a>

[AccessibilityAction](class_accessibilityserver.md#enum-accessibilityserver-accessibilityaction) **ACTION_SCROLL_INTO_VIEW** = `17`

Scroll into view action, callback argument is set to [AccessibilityScrollHint](class_accessibilityserver.md#enum-accessibilityserver-accessibilityscrollhint).

<a id="class-accessibilityserver-constant-action-scroll-to-point"></a>

[AccessibilityAction](class_accessibilityserver.md#enum-accessibilityserver-accessibilityaction) **ACTION_SCROLL_TO_POINT** = `18`

Scroll to point action, callback argument is set to [Vector2](class_vector2.md#class-vector2) with the relative point coordinates.

<a id="class-accessibilityserver-constant-action-set-scroll-offset"></a>

[AccessibilityAction](class_accessibilityserver.md#enum-accessibilityserver-accessibilityaction) **ACTION_SET_SCROLL_OFFSET** = `19`

Set scroll offset action, callback argument is set to [Vector2](class_vector2.md#class-vector2) with the scroll offset.

<a id="class-accessibilityserver-constant-action-set-value"></a>

[AccessibilityAction](class_accessibilityserver.md#enum-accessibilityserver-accessibilityaction) **ACTION_SET_VALUE** = `20`

Set value action, callback argument is set to [String](class_string.md#class-string) or number with the new value.

<a id="class-accessibilityserver-constant-action-show-context-menu"></a>

[AccessibilityAction](class_accessibilityserver.md#enum-accessibilityserver-accessibilityaction) **ACTION_SHOW_CONTEXT_MENU** = `21`

Show context menu action, callback argument is not set.

<a id="class-accessibilityserver-constant-action-custom"></a>

[AccessibilityAction](class_accessibilityserver.md#enum-accessibilityserver-accessibilityaction) **ACTION_CUSTOM** = `22`

Custom action, callback argument is set to the integer action ID.

---


<a id="enum-accessibilityserver-accessibilitylivemode"></a>

enum **AccessibilityLiveMode**: [🔗](class_accessibilityserver.md#enum-accessibilityserver-accessibilitylivemode)

<a id="class-accessibilityserver-constant-live-off"></a>

[AccessibilityLiveMode](class_accessibilityserver.md#enum-accessibilityserver-accessibilitylivemode) **LIVE_OFF** = `0`

Indicates that updates to the live region should not be presented.

<a id="class-accessibilityserver-constant-live-polite"></a>

[AccessibilityLiveMode](class_accessibilityserver.md#enum-accessibilityserver-accessibilitylivemode) **LIVE_POLITE** = `1`

Indicates that updates to the live region should be presented at the next opportunity (for example at the end of speaking the current sentence).

<a id="class-accessibilityserver-constant-live-assertive"></a>

[AccessibilityLiveMode](class_accessibilityserver.md#enum-accessibilityserver-accessibilitylivemode) **LIVE_ASSERTIVE** = `2`

Indicates that updates to the live region have the highest priority and should be presented immediately.

---


<a id="enum-accessibilityserver-accessibilityscrollunit"></a>

enum **AccessibilityScrollUnit**: [🔗](class_accessibilityserver.md#enum-accessibilityserver-accessibilityscrollunit)

<a id="class-accessibilityserver-constant-scroll-unit-item"></a>

[AccessibilityScrollUnit](class_accessibilityserver.md#enum-accessibilityserver-accessibilityscrollunit) **SCROLL_UNIT_ITEM** = `0`

The amount by which to scroll. A single item of a list, line of text.

<a id="class-accessibilityserver-constant-scroll-unit-page"></a>

[AccessibilityScrollUnit](class_accessibilityserver.md#enum-accessibilityserver-accessibilityscrollunit) **SCROLL_UNIT_PAGE** = `1`

The amount by which to scroll. A single page.

---


<a id="enum-accessibilityserver-accessibilityscrollhint"></a>

enum **AccessibilityScrollHint**: [🔗](class_accessibilityserver.md#enum-accessibilityserver-accessibilityscrollhint)

<a id="class-accessibilityserver-constant-scroll-hint-top-left"></a>

[AccessibilityScrollHint](class_accessibilityserver.md#enum-accessibilityserver-accessibilityscrollhint) **SCROLL_HINT_TOP_LEFT** = `0`

A preferred position for the node scrolled into view. Top-left edge of the scroll container.

<a id="class-accessibilityserver-constant-scroll-hint-bottom-right"></a>

[AccessibilityScrollHint](class_accessibilityserver.md#enum-accessibilityserver-accessibilityscrollhint) **SCROLL_HINT_BOTTOM_RIGHT** = `1`

A preferred position for the node scrolled into view. Bottom-right edge of the scroll container.

<a id="class-accessibilityserver-constant-scroll-hint-top-edge"></a>

[AccessibilityScrollHint](class_accessibilityserver.md#enum-accessibilityserver-accessibilityscrollhint) **SCROLL_HINT_TOP_EDGE** = `2`

A preferred position for the node scrolled into view. Top edge of the scroll container.

<a id="class-accessibilityserver-constant-scroll-hint-bottom-edge"></a>

[AccessibilityScrollHint](class_accessibilityserver.md#enum-accessibilityserver-accessibilityscrollhint) **SCROLL_HINT_BOTTOM_EDGE** = `3`

A preferred position for the node scrolled into view. Bottom edge of the scroll container.

<a id="class-accessibilityserver-constant-scroll-hint-left-edge"></a>

[AccessibilityScrollHint](class_accessibilityserver.md#enum-accessibilityserver-accessibilityscrollhint) **SCROLL_HINT_LEFT_EDGE** = `4`

A preferred position for the node scrolled into view. Left edge of the scroll container.

<a id="class-accessibilityserver-constant-scroll-hint-right-edge"></a>

[AccessibilityScrollHint](class_accessibilityserver.md#enum-accessibilityserver-accessibilityscrollhint) **SCROLL_HINT_RIGHT_EDGE** = `5`

A preferred position for the node scrolled into view. Right edge of the scroll container.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-accessibilityserver-method-create-element"></a>

[RID](class_rid.md#class-rid) **create_element**(window_id: [int](class_int.md#class-int), role: [AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-create-element)

Creates a new, empty accessibility element resource.

**Note:** An accessibility element is created and freed automatically for each [Node](class_node.md#class-node). In general, this function should not be called manually.

---


<a id="class-accessibilityserver-method-create-sub-element"></a>

[RID](class_rid.md#class-rid) **create_sub_element**(parent_rid: [RID](class_rid.md#class-rid), role: [AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole), insert_pos: [int](class_int.md#class-int) = -1) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-create-sub-element)

Creates a new, empty accessibility sub-element resource. Sub-elements can be used to provide accessibility information for objects which are not [Node](class_node.md#class-node)s, such as list items, table cells, or menu items. Sub-elements are freed automatically when the parent element is freed, or can be freed early using the [free_element()](class_accessibilityserver.md#class-accessibilityserver-method-free-element) method.

---


<a id="class-accessibilityserver-method-create-sub-text-edit-elements"></a>

[RID](class_rid.md#class-rid) **create_sub_text_edit_elements**(parent_rid: [RID](class_rid.md#class-rid), shaped_text: [RID](class_rid.md#class-rid), min_height: [float](class_float.md#class-float), insert_pos: [int](class_int.md#class-int) = -1, is_last_line: [bool](class_bool.md#class-bool) = false) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-create-sub-text-edit-elements)

Creates a new, empty accessibility sub-element from the shaped text buffer. Sub-elements are freed automatically when the parent element is freed, or can be freed early using the [free_element()](class_accessibilityserver.md#class-accessibilityserver-method-free-element) method.

If `is_last_line` is `true`, no trailing newline is appended to the text content. Set to `true` for the last line in multi-line text fields and for single-line text fields.

---


<a id="class-accessibilityserver-method-element-get-meta"></a>

[Variant](class_variant.md#class-variant) **element_get_meta**(id: [RID](class_rid.md#class-rid)) const [🔗](class_accessibilityserver.md#class-accessibilityserver-method-element-get-meta)

Returns the metadata of the accessibility element `id`.

---


<a id="class-accessibilityserver-method-element-set-meta"></a>

void **element_set_meta**(id: [RID](class_rid.md#class-rid), meta: [Variant](class_variant.md#class-variant)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-element-set-meta)

Sets the metadata of the accessibility element `id` to `meta`.

---


<a id="class-accessibilityserver-method-free-element"></a>

void **free_element**(id: [RID](class_rid.md#class-rid)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-free-element)

Frees the accessibility element `id` created by [create_element()](class_accessibilityserver.md#class-accessibilityserver-method-create-element), [create_sub_element()](class_accessibilityserver.md#class-accessibilityserver-method-create-sub-element), or [create_sub_text_edit_elements()](class_accessibilityserver.md#class-accessibilityserver-method-create-sub-text-edit-elements).

---


<a id="class-accessibilityserver-method-get-window-root"></a>

[RID](class_rid.md#class-rid) **get_window_root**(window_id: [int](class_int.md#class-int)) const [🔗](class_accessibilityserver.md#class-accessibilityserver-method-get-window-root)

Returns the main accessibility element of the OS native window.

---


<a id="class-accessibilityserver-method-has-element"></a>

[bool](class_bool.md#class-bool) **has_element**(id: [RID](class_rid.md#class-rid)) const [🔗](class_accessibilityserver.md#class-accessibilityserver-method-has-element)

Returns `true` if `id` is a valid accessibility element.

---


<a id="class-accessibilityserver-method-is-supported"></a>

[bool](class_bool.md#class-bool) **is_supported**() const [🔗](class_accessibilityserver.md#class-accessibilityserver-method-is-supported)

Returns `true` if screen reader is support by this implementation.

---


<a id="class-accessibilityserver-method-set-window-focused"></a>

void **set_window_focused**(window_id: [int](class_int.md#class-int), focused: [bool](class_bool.md#class-bool)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-set-window-focused)

Sets the window focused state for assistive apps.

**Note:** This method is implemented on Linux, macOS, and Windows.

**Note:** Advanced users only! [Window](class_window.md#class-window) objects call this method automatically.

---


<a id="class-accessibilityserver-method-set-window-rect"></a>

void **set_window_rect**(window_id: [int](class_int.md#class-int), rect_out: [Rect2](class_rect2.md#class-rect2), rect_in: [Rect2](class_rect2.md#class-rect2)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-set-window-rect)

Sets window outer (with decorations) and inner (without decorations) bounds for assistive apps.

**Note:** This method is implemented on Linux, macOS, and Windows.

**Note:** Advanced users only! [Window](class_window.md#class-window) objects call this method automatically.

---


<a id="class-accessibilityserver-method-update-add-action"></a>

void **update_add_action**(id: [RID](class_rid.md#class-rid), action: [AccessibilityAction](class_accessibilityserver.md#enum-accessibilityserver-accessibilityaction), callable: [Callable](class_callable.md#class-callable)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-add-action)

Adds a callback for the accessibility action (action which can be performed by using a special screen reader command or buttons on the Braille display), and marks this action as supported. The action callback receives one [Variant](class_variant.md#class-variant) argument, which value depends on action type.

---


<a id="class-accessibilityserver-method-update-add-child"></a>

void **update_add_child**(id: [RID](class_rid.md#class-rid), child_id: [RID](class_rid.md#class-rid)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-add-child)

Adds a child accessibility element.

**Note:** [Node](class_node.md#class-node) children and sub-elements are added to the child list automatically.

---


<a id="class-accessibilityserver-method-update-add-custom-action"></a>

void **update_add_custom_action**(id: [RID](class_rid.md#class-rid), action_id: [int](class_int.md#class-int), action_description: [String](class_string.md#class-string)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-add-custom-action)

Adds support for a custom accessibility action. `action_id` is passed as an argument to the callback of [ACTION_CUSTOM](class_accessibilityserver.md#class-accessibilityserver-constant-action-custom) action.

---


<a id="class-accessibilityserver-method-update-add-related-controls"></a>

void **update_add_related_controls**(id: [RID](class_rid.md#class-rid), related_id: [RID](class_rid.md#class-rid)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-add-related-controls)

Adds an element that is controlled by this element.

---


<a id="class-accessibilityserver-method-update-add-related-described-by"></a>

void **update_add_related_described_by**(id: [RID](class_rid.md#class-rid), related_id: [RID](class_rid.md#class-rid)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-add-related-described-by)

Adds an element that describes this element.

---


<a id="class-accessibilityserver-method-update-add-related-details"></a>

void **update_add_related_details**(id: [RID](class_rid.md#class-rid), related_id: [RID](class_rid.md#class-rid)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-add-related-details)

Adds an element that details this element.

---


<a id="class-accessibilityserver-method-update-add-related-flow-to"></a>

void **update_add_related_flow_to**(id: [RID](class_rid.md#class-rid), related_id: [RID](class_rid.md#class-rid)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-add-related-flow-to)

Adds an element that this element flow into.

---


<a id="class-accessibilityserver-method-update-add-related-labeled-by"></a>

void **update_add_related_labeled_by**(id: [RID](class_rid.md#class-rid), related_id: [RID](class_rid.md#class-rid)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-add-related-labeled-by)

Adds an element that labels this element.

---


<a id="class-accessibilityserver-method-update-add-related-radio-group"></a>

void **update_add_related_radio_group**(id: [RID](class_rid.md#class-rid), related_id: [RID](class_rid.md#class-rid)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-add-related-radio-group)

Adds an element that is part of the same radio group.

**Note:** This method should be called on each element of the group, using all other elements as `related_id`.

---


<a id="class-accessibilityserver-method-update-set-active-descendant"></a>

void **update_set_active_descendant**(id: [RID](class_rid.md#class-rid), other_id: [RID](class_rid.md#class-rid)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-active-descendant)

Adds an element that is an active descendant of this element.

---


<a id="class-accessibilityserver-method-update-set-background-color"></a>

void **update_set_background_color**(id: [RID](class_rid.md#class-rid), color: [Color](class_color.md#class-color)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-background-color)

Sets element background color.

---


<a id="class-accessibilityserver-method-update-set-bounds"></a>

void **update_set_bounds**(id: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-bounds)

Sets element bounding box, relative to the node position.

---


<a id="class-accessibilityserver-method-update-set-braille-label"></a>

void **update_set_braille_label**(id: [RID](class_rid.md#class-rid), name: [String](class_string.md#class-string)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-braille-label)

Sets element accessibility label for Braille display.

---


<a id="class-accessibilityserver-method-update-set-braille-role-description"></a>

void **update_set_braille_role_description**(id: [RID](class_rid.md#class-rid), description: [String](class_string.md#class-string)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-braille-role-description)

Sets element accessibility role description for Braille display.

---


<a id="class-accessibilityserver-method-update-set-checked"></a>

void **update_set_checked**(id: [RID](class_rid.md#class-rid), checekd: [bool](class_bool.md#class-bool)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-checked)

Sets element checked state.

---


<a id="class-accessibilityserver-method-update-set-classname"></a>

void **update_set_classname**(id: [RID](class_rid.md#class-rid), classname: [String](class_string.md#class-string)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-classname)

Sets element class name.

---


<a id="class-accessibilityserver-method-update-set-color-value"></a>

void **update_set_color_value**(id: [RID](class_rid.md#class-rid), color: [Color](class_color.md#class-color)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-color-value)

Sets element color value.

---


<a id="class-accessibilityserver-method-update-set-description"></a>

void **update_set_description**(id: [RID](class_rid.md#class-rid), description: [String](class_string.md#class-string)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-description)

Sets element accessibility description.

---


<a id="class-accessibilityserver-method-update-set-error-message"></a>

void **update_set_error_message**(id: [RID](class_rid.md#class-rid), other_id: [RID](class_rid.md#class-rid)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-error-message)

Sets an element which contains an error message for this element.

---


<a id="class-accessibilityserver-method-update-set-extra-info"></a>

void **update_set_extra_info**(id: [RID](class_rid.md#class-rid), name: [String](class_string.md#class-string)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-extra-info)

Sets element accessibility extra information added to the element name.

---


<a id="class-accessibilityserver-method-update-set-flag"></a>

void **update_set_flag**(id: [RID](class_rid.md#class-rid), flag: [AccessibilityFlags](class_accessibilityserver.md#enum-accessibilityserver-accessibilityflags), value: [bool](class_bool.md#class-bool)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-flag)

Sets element flag.

---


<a id="class-accessibilityserver-method-update-set-focus"></a>

void **update_set_focus**(id: [RID](class_rid.md#class-rid)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-focus)

Sets currently focused element.

---


<a id="class-accessibilityserver-method-update-set-foreground-color"></a>

void **update_set_foreground_color**(id: [RID](class_rid.md#class-rid), color: [Color](class_color.md#class-color)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-foreground-color)

Sets element foreground color.

---


<a id="class-accessibilityserver-method-update-set-in-page-link-target"></a>

void **update_set_in_page_link_target**(id: [RID](class_rid.md#class-rid), other_id: [RID](class_rid.md#class-rid)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-in-page-link-target)

Sets target element for the link.

---


<a id="class-accessibilityserver-method-update-set-language"></a>

void **update_set_language**(id: [RID](class_rid.md#class-rid), language: [String](class_string.md#class-string)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-language)

Sets element text language.

---


<a id="class-accessibilityserver-method-update-set-list-item-count"></a>

void **update_set_list_item_count**(id: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-list-item-count)

Sets number of items in the list.

---


<a id="class-accessibilityserver-method-update-set-list-item-expanded"></a>

void **update_set_list_item_expanded**(id: [RID](class_rid.md#class-rid), expanded: [bool](class_bool.md#class-bool)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-list-item-expanded)

Sets list/tree item expanded status.

---


<a id="class-accessibilityserver-method-update-set-list-item-index"></a>

void **update_set_list_item_index**(id: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-list-item-index)

Sets the position of the element in the list.

---


<a id="class-accessibilityserver-method-update-set-list-item-level"></a>

void **update_set_list_item_level**(id: [RID](class_rid.md#class-rid), level: [int](class_int.md#class-int)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-list-item-level)

Sets the hierarchical level of the element in the list.

---


<a id="class-accessibilityserver-method-update-set-list-item-selected"></a>

void **update_set_list_item_selected**(id: [RID](class_rid.md#class-rid), selected: [bool](class_bool.md#class-bool)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-list-item-selected)

Sets list/tree item selected status.

---


<a id="class-accessibilityserver-method-update-set-list-orientation"></a>

void **update_set_list_orientation**(id: [RID](class_rid.md#class-rid), vertical: [bool](class_bool.md#class-bool)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-list-orientation)

Sets the orientation of the list elements.

---


<a id="class-accessibilityserver-method-update-set-live"></a>

void **update_set_live**(id: [RID](class_rid.md#class-rid), live: [AccessibilityLiveMode](class_accessibilityserver.md#enum-accessibilityserver-accessibilitylivemode)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-live)

Sets the priority of the live region updates.

---


<a id="class-accessibilityserver-method-update-set-member-of"></a>

void **update_set_member_of**(id: [RID](class_rid.md#class-rid), group_id: [RID](class_rid.md#class-rid)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-member-of)

Sets the element to be a member of the group.

---


<a id="class-accessibilityserver-method-update-set-name"></a>

void **update_set_name**(id: [RID](class_rid.md#class-rid), name: [String](class_string.md#class-string)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-name)

Sets element accessibility name.

---


<a id="class-accessibilityserver-method-update-set-next-on-line"></a>

void **update_set_next_on_line**(id: [RID](class_rid.md#class-rid), other_id: [RID](class_rid.md#class-rid)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-next-on-line)

Sets next element on the line.

---


<a id="class-accessibilityserver-method-update-set-num-jump"></a>

void **update_set_num_jump**(id: [RID](class_rid.md#class-rid), jump: [float](class_float.md#class-float)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-num-jump)

Sets numeric value jump.

---


<a id="class-accessibilityserver-method-update-set-num-range"></a>

void **update_set_num_range**(id: [RID](class_rid.md#class-rid), min: [float](class_float.md#class-float), max: [float](class_float.md#class-float)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-num-range)

Sets numeric value range.

---


<a id="class-accessibilityserver-method-update-set-num-step"></a>

void **update_set_num_step**(id: [RID](class_rid.md#class-rid), step: [float](class_float.md#class-float)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-num-step)

Sets numeric value step.

---


<a id="class-accessibilityserver-method-update-set-num-value"></a>

void **update_set_num_value**(id: [RID](class_rid.md#class-rid), position: [float](class_float.md#class-float)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-num-value)

Sets numeric value.

---


<a id="class-accessibilityserver-method-update-set-placeholder"></a>

void **update_set_placeholder**(id: [RID](class_rid.md#class-rid), placeholder: [String](class_string.md#class-string)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-placeholder)

Sets placeholder text.

---


<a id="class-accessibilityserver-method-update-set-popup-type"></a>

void **update_set_popup_type**(id: [RID](class_rid.md#class-rid), popup: [AccessibilityPopupType](class_accessibilityserver.md#enum-accessibilityserver-accessibilitypopuptype)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-popup-type)

Sets popup type for popup buttons.

---


<a id="class-accessibilityserver-method-update-set-previous-on-line"></a>

void **update_set_previous_on_line**(id: [RID](class_rid.md#class-rid), other_id: [RID](class_rid.md#class-rid)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-previous-on-line)

Sets previous element on the line.

---


<a id="class-accessibilityserver-method-update-set-role"></a>

void **update_set_role**(id: [RID](class_rid.md#class-rid), role: [AccessibilityRole](class_accessibilityserver.md#enum-accessibilityserver-accessibilityrole)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-role)

Sets element accessibility role.

---


<a id="class-accessibilityserver-method-update-set-role-description"></a>

void **update_set_role_description**(id: [RID](class_rid.md#class-rid), description: [String](class_string.md#class-string)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-role-description)

Sets element accessibility role description text.

---


<a id="class-accessibilityserver-method-update-set-scroll-x"></a>

void **update_set_scroll_x**(id: [RID](class_rid.md#class-rid), position: [float](class_float.md#class-float)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-scroll-x)

Sets scroll bar x position.

---


<a id="class-accessibilityserver-method-update-set-scroll-x-range"></a>

void **update_set_scroll_x_range**(id: [RID](class_rid.md#class-rid), min: [float](class_float.md#class-float), max: [float](class_float.md#class-float)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-scroll-x-range)

Sets scroll bar x range.

---


<a id="class-accessibilityserver-method-update-set-scroll-y"></a>

void **update_set_scroll_y**(id: [RID](class_rid.md#class-rid), position: [float](class_float.md#class-float)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-scroll-y)

Sets scroll bar y position.

---


<a id="class-accessibilityserver-method-update-set-scroll-y-range"></a>

void **update_set_scroll_y_range**(id: [RID](class_rid.md#class-rid), min: [float](class_float.md#class-float), max: [float](class_float.md#class-float)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-scroll-y-range)

Sets scroll bar y range.

---


<a id="class-accessibilityserver-method-update-set-shortcut"></a>

void **update_set_shortcut**(id: [RID](class_rid.md#class-rid), shortcut: [String](class_string.md#class-string)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-shortcut)

Sets the list of keyboard shortcuts used by element.

---


<a id="class-accessibilityserver-method-update-set-state-description"></a>

void **update_set_state_description**(id: [RID](class_rid.md#class-rid), description: [String](class_string.md#class-string)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-state-description)

Sets human-readable description of the current checked state.

---


<a id="class-accessibilityserver-method-update-set-table-cell-position"></a>

void **update_set_table_cell_position**(id: [RID](class_rid.md#class-rid), row_index: [int](class_int.md#class-int), column_index: [int](class_int.md#class-int)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-table-cell-position)

Sets cell position in the table.

---


<a id="class-accessibilityserver-method-update-set-table-cell-span"></a>

void **update_set_table_cell_span**(id: [RID](class_rid.md#class-rid), row_span: [int](class_int.md#class-int), column_span: [int](class_int.md#class-int)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-table-cell-span)

Sets cell row/column span.

---


<a id="class-accessibilityserver-method-update-set-table-column-count"></a>

void **update_set_table_column_count**(id: [RID](class_rid.md#class-rid), count: [int](class_int.md#class-int)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-table-column-count)

Sets number of columns in the table.

---


<a id="class-accessibilityserver-method-update-set-table-column-index"></a>

void **update_set_table_column_index**(id: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-table-column-index)

Sets position of the column.

---


<a id="class-accessibilityserver-method-update-set-table-row-count"></a>

void **update_set_table_row_count**(id: [RID](class_rid.md#class-rid), count: [int](class_int.md#class-int)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-table-row-count)

Sets number of rows in the table.

---


<a id="class-accessibilityserver-method-update-set-table-row-index"></a>

void **update_set_table_row_index**(id: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-table-row-index)

Sets position of the row in the table.

---


<a id="class-accessibilityserver-method-update-set-text-align"></a>

void **update_set_text_align**(id: [RID](class_rid.md#class-rid), align: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-text-align)

Sets element text alignment.

---


<a id="class-accessibilityserver-method-update-set-text-decorations"></a>

void **update_set_text_decorations**(id: [RID](class_rid.md#class-rid), underline: [bool](class_bool.md#class-bool), strikethrough: [bool](class_bool.md#class-bool), overline: [bool](class_bool.md#class-bool), color: [Color](class_color.md#class-color) = Color(0, 0, 0, 1)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-text-decorations)

Sets text underline/overline/strikethrough.

---


<a id="class-accessibilityserver-method-update-set-text-orientation"></a>

void **update_set_text_orientation**(id: [RID](class_rid.md#class-rid), vertical: [bool](class_bool.md#class-bool)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-text-orientation)

Sets text orientation.

---


<a id="class-accessibilityserver-method-update-set-text-selection"></a>

void **update_set_text_selection**(id: [RID](class_rid.md#class-rid), text_start_id: [RID](class_rid.md#class-rid), start_char: [int](class_int.md#class-int), text_end_id: [RID](class_rid.md#class-rid), end_char: [int](class_int.md#class-int)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-text-selection)

Sets text selection to the text field. `text_start_id` and `text_end_id` should be elements created by [create_sub_text_edit_elements()](class_accessibilityserver.md#class-accessibilityserver-method-create-sub-text-edit-elements). Character offsets are relative to the corresponding element.

---


<a id="class-accessibilityserver-method-update-set-tooltip"></a>

void **update_set_tooltip**(id: [RID](class_rid.md#class-rid), tooltip: [String](class_string.md#class-string)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-tooltip)

Sets tooltip text.

---


<a id="class-accessibilityserver-method-update-set-transform"></a>

void **update_set_transform**(id: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-transform)

Sets element 2D transform.

---


<a id="class-accessibilityserver-method-update-set-url"></a>

void **update_set_url**(id: [RID](class_rid.md#class-rid), url: [String](class_string.md#class-string)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-url)

Sets link URL.

---


<a id="class-accessibilityserver-method-update-set-value"></a>

void **update_set_value**(id: [RID](class_rid.md#class-rid), value: [String](class_string.md#class-string)) [🔗](class_accessibilityserver.md#class-accessibilityserver-method-update-set-value)

Sets element text value.
