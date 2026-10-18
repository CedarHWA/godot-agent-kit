> Source: https://docs.godotengine.org/en/4.7/classes/class_treeitem.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="treeitem"></a>

<a id="class-treeitem"></a>

# TreeItem

**Inherits:** [Object](class_object.md#class-object)

An internal control for a single item inside [Tree](class_tree.md#class-tree).

<a id="description"></a>

## Description

A single item of a [Tree](class_tree.md#class-tree) control. It can contain other **TreeItem**s as children, which allows it to create a hierarchy. It can also contain text and buttons. **TreeItem** is not a [Node](class_node.md#class-node), it is internal to the [Tree](class_tree.md#class-tree).

To create a **TreeItem**, use [Tree.create_item()](class_tree.md#class-tree-method-create-item) or [create_child()](class_treeitem.md#class-treeitem-method-create-child). To remove a **TreeItem**, use [Object.free()](class_object.md#class-object-method-free).

**Note:** The ID values used for buttons are 32-bit, unlike [int](class_int.md#class-int) which is always 64-bit. They go from `-2147483648` to `2147483647`.

<a id="properties"></a>

## Properties

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [collapsed](class_treeitem.md#class-treeitem-property-collapsed) |
| [int](class_int.md#class-int) | [custom_minimum_height](class_treeitem.md#class-treeitem-property-custom-minimum-height) |
| [bool](class_bool.md#class-bool) | [disable_folding](class_treeitem.md#class-treeitem-property-disable-folding) |
| [bool](class_bool.md#class-bool) | [visible](class_treeitem.md#class-treeitem-property-visible) |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_button](class_treeitem.md#class-treeitem-method-add-button)(column: [int](class_int.md#class-int), button: [Texture2D](class_texture2d.md#class-texture2d), id: [int](class_int.md#class-int) = -1, disabled: [bool](class_bool.md#class-bool) = false, tooltip_text: [String](class_string.md#class-string) = "", description: [String](class_string.md#class-string) = "") |
| void | [add_child](class_treeitem.md#class-treeitem-method-add-child)(child: [TreeItem](class_treeitem.md#class-treeitem)) |
| void | [call_recursive](class_treeitem.md#class-treeitem-method-call-recursive)(method: [StringName](class_stringname.md#class-stringname), ...) vararg |
| void | [clear_buttons](class_treeitem.md#class-treeitem-method-clear-buttons)() |
| void | [clear_custom_bg_color](class_treeitem.md#class-treeitem-method-clear-custom-bg-color)(column: [int](class_int.md#class-int)) |
| void | [clear_custom_color](class_treeitem.md#class-treeitem-method-clear-custom-color)(column: [int](class_int.md#class-int)) |
| [TreeItem](class_treeitem.md#class-treeitem) | [create_child](class_treeitem.md#class-treeitem-method-create-child)(index: [int](class_int.md#class-int) = -1) |
| void | [deselect](class_treeitem.md#class-treeitem-method-deselect)(column: [int](class_int.md#class-int)) |
| void | [erase_button](class_treeitem.md#class-treeitem-method-erase-button)(column: [int](class_int.md#class-int), button_index: [int](class_int.md#class-int)) |
| [AutoTranslateMode](class_node.md#enum-node-autotranslatemode) | [get_auto_translate_mode](class_treeitem.md#class-treeitem-method-get-auto-translate-mode)(column: [int](class_int.md#class-int)) const |
| [AutowrapMode](class_textserver.md#enum-textserver-autowrapmode) | [get_autowrap_mode](class_treeitem.md#class-treeitem-method-get-autowrap-mode)(column: [int](class_int.md#class-int)) const |
| BitField[[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)] | [get_autowrap_trim_flags](class_treeitem.md#class-treeitem-method-get-autowrap-trim-flags)(column: [int](class_int.md#class-int)) const |
| [Texture2D](class_texture2d.md#class-texture2d) | [get_button](class_treeitem.md#class-treeitem-method-get-button)(column: [int](class_int.md#class-int), button_index: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_button_by_id](class_treeitem.md#class-treeitem-method-get-button-by-id)(column: [int](class_int.md#class-int), id: [int](class_int.md#class-int)) const |
| [Color](class_color.md#class-color) | [get_button_color](class_treeitem.md#class-treeitem-method-get-button-color)(column: [int](class_int.md#class-int), id: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_button_count](class_treeitem.md#class-treeitem-method-get-button-count)(column: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_button_id](class_treeitem.md#class-treeitem-method-get-button-id)(column: [int](class_int.md#class-int), button_index: [int](class_int.md#class-int)) const |
| [String](class_string.md#class-string) | [get_button_tooltip_text](class_treeitem.md#class-treeitem-method-get-button-tooltip-text)(column: [int](class_int.md#class-int), button_index: [int](class_int.md#class-int)) const |
| [TreeCellMode](class_treeitem.md#enum-treeitem-treecellmode) | [get_cell_mode](class_treeitem.md#class-treeitem-method-get-cell-mode)(column: [int](class_int.md#class-int)) const |
| [TreeItem](class_treeitem.md#class-treeitem) | [get_child](class_treeitem.md#class-treeitem-method-get-child)(index: [int](class_int.md#class-int)) |
| [int](class_int.md#class-int) | [get_child_count](class_treeitem.md#class-treeitem-method-get-child-count)() |
| [Array](class_array.md#class-array)[[TreeItem](class_treeitem.md#class-treeitem)] | [get_children](class_treeitem.md#class-treeitem-method-get-children)() |
| [Color](class_color.md#class-color) | [get_custom_bg_color](class_treeitem.md#class-treeitem-method-get-custom-bg-color)(column: [int](class_int.md#class-int)) const |
| [Color](class_color.md#class-color) | [get_custom_color](class_treeitem.md#class-treeitem-method-get-custom-color)(column: [int](class_int.md#class-int)) const |
| [Callable](class_callable.md#class-callable) | [get_custom_draw_callback](class_treeitem.md#class-treeitem-method-get-custom-draw-callback)(column: [int](class_int.md#class-int)) const |
| [Font](class_font.md#class-font) | [get_custom_font](class_treeitem.md#class-treeitem-method-get-custom-font)(column: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_custom_font_size](class_treeitem.md#class-treeitem-method-get-custom-font-size)(column: [int](class_int.md#class-int)) const |
| [StyleBox](class_stylebox.md#class-stylebox) | [get_custom_stylebox](class_treeitem.md#class-treeitem-method-get-custom-stylebox)(column: [int](class_int.md#class-int)) const |
| [String](class_string.md#class-string) | [get_description](class_treeitem.md#class-treeitem-method-get-description)(column: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [get_expand_right](class_treeitem.md#class-treeitem-method-get-expand-right)(column: [int](class_int.md#class-int)) const |
| [TreeItem](class_treeitem.md#class-treeitem) | [get_first_child](class_treeitem.md#class-treeitem-method-get-first-child)() const |
| [Texture2D](class_texture2d.md#class-texture2d) | [get_icon](class_treeitem.md#class-treeitem-method-get-icon)(column: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_icon_max_width](class_treeitem.md#class-treeitem-method-get-icon-max-width)(column: [int](class_int.md#class-int)) const |
| [Color](class_color.md#class-color) | [get_icon_modulate](class_treeitem.md#class-treeitem-method-get-icon-modulate)(column: [int](class_int.md#class-int)) const |
| [Texture2D](class_texture2d.md#class-texture2d) | [get_icon_overlay](class_treeitem.md#class-treeitem-method-get-icon-overlay)(column: [int](class_int.md#class-int)) const |
| [Rect2](class_rect2.md#class-rect2) | [get_icon_region](class_treeitem.md#class-treeitem-method-get-icon-region)(column: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_index](class_treeitem.md#class-treeitem-method-get-index)() |
| [String](class_string.md#class-string) | [get_language](class_treeitem.md#class-treeitem-method-get-language)(column: [int](class_int.md#class-int)) const |
| [Variant](class_variant.md#class-variant) | [get_metadata](class_treeitem.md#class-treeitem-method-get-metadata)(column: [int](class_int.md#class-int)) const |
| [TreeItem](class_treeitem.md#class-treeitem) | [get_next](class_treeitem.md#class-treeitem-method-get-next)() const |
| [TreeItem](class_treeitem.md#class-treeitem) | [get_next_in_tree](class_treeitem.md#class-treeitem-method-get-next-in-tree)(wrap: [bool](class_bool.md#class-bool) = false) |
| [TreeItem](class_treeitem.md#class-treeitem) | [get_next_visible](class_treeitem.md#class-treeitem-method-get-next-visible)(wrap: [bool](class_bool.md#class-bool) = false) |
| [TreeItem](class_treeitem.md#class-treeitem) | [get_parent](class_treeitem.md#class-treeitem-method-get-parent)() const |
| [TreeItem](class_treeitem.md#class-treeitem) | [get_prev](class_treeitem.md#class-treeitem-method-get-prev)() |
| [TreeItem](class_treeitem.md#class-treeitem) | [get_prev_in_tree](class_treeitem.md#class-treeitem-method-get-prev-in-tree)(wrap: [bool](class_bool.md#class-bool) = false) |
| [TreeItem](class_treeitem.md#class-treeitem) | [get_prev_visible](class_treeitem.md#class-treeitem-method-get-prev-visible)(wrap: [bool](class_bool.md#class-bool) = false) |
| [float](class_float.md#class-float) | [get_range](class_treeitem.md#class-treeitem-method-get-range)(column: [int](class_int.md#class-int)) const |
| [Dictionary](class_dictionary.md#class-dictionary) | [get_range_config](class_treeitem.md#class-treeitem-method-get-range-config)(column: [int](class_int.md#class-int)) |
| [StructuredTextParser](class_textserver.md#enum-textserver-structuredtextparser) | [get_structured_text_bidi_override](class_treeitem.md#class-treeitem-method-get-structured-text-bidi-override)(column: [int](class_int.md#class-int)) const |
| [Array](class_array.md#class-array) | [get_structured_text_bidi_override_options](class_treeitem.md#class-treeitem-method-get-structured-text-bidi-override-options)(column: [int](class_int.md#class-int)) const |
| [String](class_string.md#class-string) | [get_suffix](class_treeitem.md#class-treeitem-method-get-suffix)(column: [int](class_int.md#class-int)) const |
| [String](class_string.md#class-string) | [get_text](class_treeitem.md#class-treeitem-method-get-text)(column: [int](class_int.md#class-int)) const |
| [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) | [get_text_alignment](class_treeitem.md#class-treeitem-method-get-text-alignment)(column: [int](class_int.md#class-int)) const |
| [TextDirection](class_control.md#enum-control-textdirection) | [get_text_direction](class_treeitem.md#class-treeitem-method-get-text-direction)(column: [int](class_int.md#class-int)) const |
| [OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior) | [get_text_overrun_behavior](class_treeitem.md#class-treeitem-method-get-text-overrun-behavior)(column: [int](class_int.md#class-int)) const |
| [String](class_string.md#class-string) | [get_tooltip_text](class_treeitem.md#class-treeitem-method-get-tooltip-text)(column: [int](class_int.md#class-int)) const |
| [Tree](class_tree.md#class-tree) | [get_tree](class_treeitem.md#class-treeitem-method-get-tree)() const |
| [bool](class_bool.md#class-bool) | [is_accepting_children](class_treeitem.md#class-treeitem-method-is-accepting-children)() const |
| [bool](class_bool.md#class-bool) | [is_any_collapsed](class_treeitem.md#class-treeitem-method-is-any-collapsed)(only_visible: [bool](class_bool.md#class-bool) = false) |
| [bool](class_bool.md#class-bool) | [is_button_disabled](class_treeitem.md#class-treeitem-method-is-button-disabled)(column: [int](class_int.md#class-int), button_index: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [is_checked](class_treeitem.md#class-treeitem-method-is-checked)(column: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [is_custom_set_as_button](class_treeitem.md#class-treeitem-method-is-custom-set-as-button)(column: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [is_edit_multiline](class_treeitem.md#class-treeitem-method-is-edit-multiline)(column: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [is_editable](class_treeitem.md#class-treeitem-method-is-editable)(column: [int](class_int.md#class-int)) |
| [bool](class_bool.md#class-bool) | [is_indeterminate](class_treeitem.md#class-treeitem-method-is-indeterminate)(column: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [is_selectable](class_treeitem.md#class-treeitem-method-is-selectable)(column: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [is_selected](class_treeitem.md#class-treeitem-method-is-selected)(column: [int](class_int.md#class-int)) |
| [bool](class_bool.md#class-bool) | [is_visible_in_tree](class_treeitem.md#class-treeitem-method-is-visible-in-tree)() const |
| void | [move_after](class_treeitem.md#class-treeitem-method-move-after)(item: [TreeItem](class_treeitem.md#class-treeitem)) |
| void | [move_before](class_treeitem.md#class-treeitem-method-move-before)(item: [TreeItem](class_treeitem.md#class-treeitem)) |
| void | [propagate_check](class_treeitem.md#class-treeitem-method-propagate-check)(column: [int](class_int.md#class-int), emit_signal: [bool](class_bool.md#class-bool) = true) |
| void | [remove_child](class_treeitem.md#class-treeitem-method-remove-child)(child: [TreeItem](class_treeitem.md#class-treeitem)) |
| void | [select](class_treeitem.md#class-treeitem-method-select)(column: [int](class_int.md#class-int), set_as_cursor: [bool](class_bool.md#class-bool) = true) |
| void | [set_accept_children](class_treeitem.md#class-treeitem-method-set-accept-children)(allowed: [bool](class_bool.md#class-bool)) |
| void | [set_auto_translate_mode](class_treeitem.md#class-treeitem-method-set-auto-translate-mode)(column: [int](class_int.md#class-int), mode: [AutoTranslateMode](class_node.md#enum-node-autotranslatemode)) |
| void | [set_autowrap_mode](class_treeitem.md#class-treeitem-method-set-autowrap-mode)(column: [int](class_int.md#class-int), autowrap_mode: [AutowrapMode](class_textserver.md#enum-textserver-autowrapmode)) |
| void | [set_autowrap_trim_flags](class_treeitem.md#class-treeitem-method-set-autowrap-trim-flags)(column: [int](class_int.md#class-int), flags: BitField[[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)]) |
| void | [set_button](class_treeitem.md#class-treeitem-method-set-button)(column: [int](class_int.md#class-int), button_index: [int](class_int.md#class-int), button: [Texture2D](class_texture2d.md#class-texture2d)) |
| void | [set_button_color](class_treeitem.md#class-treeitem-method-set-button-color)(column: [int](class_int.md#class-int), button_index: [int](class_int.md#class-int), color: [Color](class_color.md#class-color)) |
| void | [set_button_description](class_treeitem.md#class-treeitem-method-set-button-description)(column: [int](class_int.md#class-int), button_index: [int](class_int.md#class-int), description: [String](class_string.md#class-string)) |
| void | [set_button_disabled](class_treeitem.md#class-treeitem-method-set-button-disabled)(column: [int](class_int.md#class-int), button_index: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool)) |
| void | [set_button_tooltip_text](class_treeitem.md#class-treeitem-method-set-button-tooltip-text)(column: [int](class_int.md#class-int), button_index: [int](class_int.md#class-int), tooltip: [String](class_string.md#class-string)) |
| void | [set_cell_mode](class_treeitem.md#class-treeitem-method-set-cell-mode)(column: [int](class_int.md#class-int), mode: [TreeCellMode](class_treeitem.md#enum-treeitem-treecellmode)) |
| void | [set_checked](class_treeitem.md#class-treeitem-method-set-checked)(column: [int](class_int.md#class-int), checked: [bool](class_bool.md#class-bool)) |
| void | [set_collapsed_recursive](class_treeitem.md#class-treeitem-method-set-collapsed-recursive)(enable: [bool](class_bool.md#class-bool)) |
| void | [set_custom_as_button](class_treeitem.md#class-treeitem-method-set-custom-as-button)(column: [int](class_int.md#class-int), enable: [bool](class_bool.md#class-bool)) |
| void | [set_custom_bg_color](class_treeitem.md#class-treeitem-method-set-custom-bg-color)(column: [int](class_int.md#class-int), color: [Color](class_color.md#class-color), just_outline: [bool](class_bool.md#class-bool) = false) |
| void | [set_custom_color](class_treeitem.md#class-treeitem-method-set-custom-color)(column: [int](class_int.md#class-int), color: [Color](class_color.md#class-color)) |
| void | [set_custom_draw](class_treeitem.md#class-treeitem-method-set-custom-draw)(column: [int](class_int.md#class-int), object: [Object](class_object.md#class-object), callback: [StringName](class_stringname.md#class-stringname)) |
| void | [set_custom_draw_callback](class_treeitem.md#class-treeitem-method-set-custom-draw-callback)(column: [int](class_int.md#class-int), callback: [Callable](class_callable.md#class-callable)) |
| void | [set_custom_font](class_treeitem.md#class-treeitem-method-set-custom-font)(column: [int](class_int.md#class-int), font: [Font](class_font.md#class-font)) |
| void | [set_custom_font_size](class_treeitem.md#class-treeitem-method-set-custom-font-size)(column: [int](class_int.md#class-int), font_size: [int](class_int.md#class-int)) |
| void | [set_custom_stylebox](class_treeitem.md#class-treeitem-method-set-custom-stylebox)(column: [int](class_int.md#class-int), stylebox: [StyleBox](class_stylebox.md#class-stylebox)) |
| void | [set_description](class_treeitem.md#class-treeitem-method-set-description)(column: [int](class_int.md#class-int), description: [String](class_string.md#class-string)) |
| void | [set_edit_multiline](class_treeitem.md#class-treeitem-method-set-edit-multiline)(column: [int](class_int.md#class-int), multiline: [bool](class_bool.md#class-bool)) |
| void | [set_editable](class_treeitem.md#class-treeitem-method-set-editable)(column: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool)) |
| void | [set_expand_right](class_treeitem.md#class-treeitem-method-set-expand-right)(column: [int](class_int.md#class-int), enable: [bool](class_bool.md#class-bool)) |
| void | [set_icon](class_treeitem.md#class-treeitem-method-set-icon)(column: [int](class_int.md#class-int), texture: [Texture2D](class_texture2d.md#class-texture2d)) |
| void | [set_icon_max_width](class_treeitem.md#class-treeitem-method-set-icon-max-width)(column: [int](class_int.md#class-int), width: [int](class_int.md#class-int)) |
| void | [set_icon_modulate](class_treeitem.md#class-treeitem-method-set-icon-modulate)(column: [int](class_int.md#class-int), modulate: [Color](class_color.md#class-color)) |
| void | [set_icon_overlay](class_treeitem.md#class-treeitem-method-set-icon-overlay)(column: [int](class_int.md#class-int), texture: [Texture2D](class_texture2d.md#class-texture2d)) |
| void | [set_icon_region](class_treeitem.md#class-treeitem-method-set-icon-region)(column: [int](class_int.md#class-int), region: [Rect2](class_rect2.md#class-rect2)) |
| void | [set_indeterminate](class_treeitem.md#class-treeitem-method-set-indeterminate)(column: [int](class_int.md#class-int), indeterminate: [bool](class_bool.md#class-bool)) |
| void | [set_language](class_treeitem.md#class-treeitem-method-set-language)(column: [int](class_int.md#class-int), language: [String](class_string.md#class-string)) |
| void | [set_metadata](class_treeitem.md#class-treeitem-method-set-metadata)(column: [int](class_int.md#class-int), meta: [Variant](class_variant.md#class-variant)) |
| void | [set_range](class_treeitem.md#class-treeitem-method-set-range)(column: [int](class_int.md#class-int), value: [float](class_float.md#class-float)) |
| void | [set_range_config](class_treeitem.md#class-treeitem-method-set-range-config)(column: [int](class_int.md#class-int), min: [float](class_float.md#class-float), max: [float](class_float.md#class-float), step: [float](class_float.md#class-float), expr: [bool](class_bool.md#class-bool) = false) |
| void | [set_selectable](class_treeitem.md#class-treeitem-method-set-selectable)(column: [int](class_int.md#class-int), selectable: [bool](class_bool.md#class-bool)) |
| void | [set_structured_text_bidi_override](class_treeitem.md#class-treeitem-method-set-structured-text-bidi-override)(column: [int](class_int.md#class-int), parser: [StructuredTextParser](class_textserver.md#enum-textserver-structuredtextparser)) |
| void | [set_structured_text_bidi_override_options](class_treeitem.md#class-treeitem-method-set-structured-text-bidi-override-options)(column: [int](class_int.md#class-int), args: [Array](class_array.md#class-array)) |
| void | [set_suffix](class_treeitem.md#class-treeitem-method-set-suffix)(column: [int](class_int.md#class-int), text: [String](class_string.md#class-string)) |
| void | [set_text](class_treeitem.md#class-treeitem-method-set-text)(column: [int](class_int.md#class-int), text: [String](class_string.md#class-string)) |
| void | [set_text_alignment](class_treeitem.md#class-treeitem-method-set-text-alignment)(column: [int](class_int.md#class-int), text_alignment: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment)) |
| void | [set_text_direction](class_treeitem.md#class-treeitem-method-set-text-direction)(column: [int](class_int.md#class-int), direction: [TextDirection](class_control.md#enum-control-textdirection)) |
| void | [set_text_overrun_behavior](class_treeitem.md#class-treeitem-method-set-text-overrun-behavior)(column: [int](class_int.md#class-int), overrun_behavior: [OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior)) |
| void | [set_tooltip_text](class_treeitem.md#class-treeitem-method-set-tooltip-text)(column: [int](class_int.md#class-int), tooltip: [String](class_string.md#class-string)) |
| void | [uncollapse_tree](class_treeitem.md#class-treeitem-method-uncollapse-tree)() |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-treeitem-treecellmode"></a>

enum **TreeCellMode**: [🔗](class_treeitem.md#enum-treeitem-treecellmode)

<a id="class-treeitem-constant-cell-mode-string"></a>

[TreeCellMode](class_treeitem.md#enum-treeitem-treecellmode) **CELL_MODE_STRING** = `0`

Cell shows a string label, optionally with an icon. When editable, the text can be edited using a [LineEdit](class_lineedit.md#class-lineedit), or a [TextEdit](class_textedit.md#class-textedit) popup if [set_edit_multiline()](class_treeitem.md#class-treeitem-method-set-edit-multiline) is used.

<a id="class-treeitem-constant-cell-mode-check"></a>

[TreeCellMode](class_treeitem.md#enum-treeitem-treecellmode) **CELL_MODE_CHECK** = `1`

Cell shows a checkbox, optionally with text and an icon. The checkbox can be pressed, released, or indeterminate (via [set_indeterminate()](class_treeitem.md#class-treeitem-method-set-indeterminate)). The checkbox can't be clicked unless the cell is editable.

<a id="class-treeitem-constant-cell-mode-range"></a>

[TreeCellMode](class_treeitem.md#enum-treeitem-treecellmode) **CELL_MODE_RANGE** = `2`

Cell shows a numeric range. When editable, it can be edited using a range slider. Use [set_range()](class_treeitem.md#class-treeitem-method-set-range) to set the value and [set_range_config()](class_treeitem.md#class-treeitem-method-set-range-config) to configure the range.

This cell can also be used in a text dropdown mode when you assign a text with [set_text()](class_treeitem.md#class-treeitem-method-set-text). Separate options with a comma, e.g. `"Option1,Option2,Option3"`.

<a id="class-treeitem-constant-cell-mode-icon"></a>

[TreeCellMode](class_treeitem.md#enum-treeitem-treecellmode) **CELL_MODE_ICON** = `3`

Cell shows an icon. It can't be edited nor display text. The icon is always centered within the cell.

<a id="class-treeitem-constant-cell-mode-custom"></a>

[TreeCellMode](class_treeitem.md#enum-treeitem-treecellmode) **CELL_MODE_CUSTOM** = `4`

Cell shows as a clickable button. It will display an arrow similar to [OptionButton](class_optionbutton.md#class-optionbutton), but doesn't feature a dropdown (for that you can use [CELL_MODE_RANGE](class_treeitem.md#class-treeitem-constant-cell-mode-range)). Clicking the button emits the [Tree.item_edited](class_tree.md#class-tree-signal-item-edited) signal. The button is flat by default, you can use [set_custom_as_button()](class_treeitem.md#class-treeitem-method-set-custom-as-button) to display it with a [StyleBox](class_stylebox.md#class-stylebox).

This mode also supports custom drawing using [set_custom_draw_callback()](class_treeitem.md#class-treeitem-method-set-custom-draw-callback).

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-treeitem-property-collapsed"></a>

[bool](class_bool.md#class-bool) **collapsed** [🔗](class_treeitem.md#class-treeitem-property-collapsed)

- void **set_collapsed**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_collapsed**()

If `true`, the TreeItem is collapsed.

---


<a id="class-treeitem-property-custom-minimum-height"></a>

[int](class_int.md#class-int) **custom_minimum_height** [🔗](class_treeitem.md#class-treeitem-property-custom-minimum-height)

- void **set_custom_minimum_height**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_custom_minimum_height**()

The custom minimum height.

---


<a id="class-treeitem-property-disable-folding"></a>

[bool](class_bool.md#class-bool) **disable_folding** [🔗](class_treeitem.md#class-treeitem-property-disable-folding)

- void **set_disable_folding**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_folding_disabled**()

If `true`, folding is disabled for this TreeItem.

---


<a id="class-treeitem-property-visible"></a>

[bool](class_bool.md#class-bool) **visible** [🔗](class_treeitem.md#class-treeitem-property-visible)

- void **set_visible**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_visible**()

If `true`, the **TreeItem** is visible (default).

Note that if a **TreeItem** is set to not be visible, none of its children will be visible either.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-treeitem-method-add-button"></a>

void **add_button**(column: [int](class_int.md#class-int), button: [Texture2D](class_texture2d.md#class-texture2d), id: [int](class_int.md#class-int) = -1, disabled: [bool](class_bool.md#class-bool) = false, tooltip_text: [String](class_string.md#class-string) = "", description: [String](class_string.md#class-string) = "") [🔗](class_treeitem.md#class-treeitem-method-add-button)

Adds a button with [Texture2D](class_texture2d.md#class-texture2d) `button` to the end of the cell at column `column`. The `id` is used to identify the button in the according [Tree.button_clicked](class_tree.md#class-tree-signal-button-clicked) signal and can be different from the buttons index. If not specified, the next available index is used, which may be retrieved by calling [get_button_count()](class_treeitem.md#class-treeitem-method-get-button-count) immediately before this method. Optionally, the button can be `disabled` and have a `tooltip_text`. `description` is used as the button description for assistive apps.

---


<a id="class-treeitem-method-add-child"></a>

void **add_child**(child: [TreeItem](class_treeitem.md#class-treeitem)) [🔗](class_treeitem.md#class-treeitem-method-add-child)

Adds a previously unparented **TreeItem** as a direct child of this one. The `child` item must not be a part of any [Tree](class_tree.md#class-tree) or parented to any **TreeItem**. See also [remove_child()](class_treeitem.md#class-treeitem-method-remove-child).

---


<a id="class-treeitem-method-call-recursive"></a>

void **call_recursive**(method: [StringName](class_stringname.md#class-stringname), ...) vararg [🔗](class_treeitem.md#class-treeitem-method-call-recursive)

Calls the `method` on the actual TreeItem and its children recursively. Pass parameters as a comma separated list.

---


<a id="class-treeitem-method-clear-buttons"></a>

void **clear_buttons**() [🔗](class_treeitem.md#class-treeitem-method-clear-buttons)

Removes all buttons from all columns of this item.

---


<a id="class-treeitem-method-clear-custom-bg-color"></a>

void **clear_custom_bg_color**(column: [int](class_int.md#class-int)) [🔗](class_treeitem.md#class-treeitem-method-clear-custom-bg-color)

Resets the background color for the given column to default.

---


<a id="class-treeitem-method-clear-custom-color"></a>

void **clear_custom_color**(column: [int](class_int.md#class-int)) [🔗](class_treeitem.md#class-treeitem-method-clear-custom-color)

Resets the color for the given column to default.

---


<a id="class-treeitem-method-create-child"></a>

[TreeItem](class_treeitem.md#class-treeitem) **create_child**(index: [int](class_int.md#class-int) = -1) [🔗](class_treeitem.md#class-treeitem-method-create-child)

Creates an item and adds it as a child.

The new item will be inserted as position `index` (the default value `-1` means the last position), or it will be the last child if `index` is higher than the child count.

---


<a id="class-treeitem-method-deselect"></a>

void **deselect**(column: [int](class_int.md#class-int)) [🔗](class_treeitem.md#class-treeitem-method-deselect)

Deselects the given column.

---


<a id="class-treeitem-method-erase-button"></a>

void **erase_button**(column: [int](class_int.md#class-int), button_index: [int](class_int.md#class-int)) [🔗](class_treeitem.md#class-treeitem-method-erase-button)

Removes the button at index `button_index` in column `column`.

---


<a id="class-treeitem-method-get-auto-translate-mode"></a>

[AutoTranslateMode](class_node.md#enum-node-autotranslatemode) **get_auto_translate_mode**(column: [int](class_int.md#class-int)) const [🔗](class_treeitem.md#class-treeitem-method-get-auto-translate-mode)

Returns the column's auto translate mode.

---


<a id="class-treeitem-method-get-autowrap-mode"></a>

[AutowrapMode](class_textserver.md#enum-textserver-autowrapmode) **get_autowrap_mode**(column: [int](class_int.md#class-int)) const [🔗](class_treeitem.md#class-treeitem-method-get-autowrap-mode)

Returns the text autowrap mode in the given `column`. By default it is [TextServer.AUTOWRAP_OFF](class_textserver.md#class-textserver-constant-autowrap-off).

---


<a id="class-treeitem-method-get-autowrap-trim-flags"></a>

BitField[[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)] **get_autowrap_trim_flags**(column: [int](class_int.md#class-int)) const [🔗](class_treeitem.md#class-treeitem-method-get-autowrap-trim-flags)

Returns the autowrap trim flags for the given `column`. By default, both [TextServer.BREAK_TRIM_START_EDGE_SPACES](class_textserver.md#class-textserver-constant-break-trim-start-edge-spaces) and [TextServer.BREAK_TRIM_END_EDGE_SPACES](class_textserver.md#class-textserver-constant-break-trim-end-edge-spaces) are enabled.

---


<a id="class-treeitem-method-get-button"></a>

[Texture2D](class_texture2d.md#class-texture2d) **get_button**(column: [int](class_int.md#class-int), button_index: [int](class_int.md#class-int)) const [🔗](class_treeitem.md#class-treeitem-method-get-button)

Returns the [Texture2D](class_texture2d.md#class-texture2d) of the button at index `button_index` in column `column`.

---


<a id="class-treeitem-method-get-button-by-id"></a>

[int](class_int.md#class-int) **get_button_by_id**(column: [int](class_int.md#class-int), id: [int](class_int.md#class-int)) const [🔗](class_treeitem.md#class-treeitem-method-get-button-by-id)

Returns the button index if there is a button with ID `id` in column `column`, otherwise returns -1.

---


<a id="class-treeitem-method-get-button-color"></a>

[Color](class_color.md#class-color) **get_button_color**(column: [int](class_int.md#class-int), id: [int](class_int.md#class-int)) const [🔗](class_treeitem.md#class-treeitem-method-get-button-color)

Returns the color of the button with ID `id` in column `column`. If the specified button does not exist, returns [Color.BLACK](class_color.md#class-color-constant-black).

---


<a id="class-treeitem-method-get-button-count"></a>

[int](class_int.md#class-int) **get_button_count**(column: [int](class_int.md#class-int)) const [🔗](class_treeitem.md#class-treeitem-method-get-button-count)

Returns the number of buttons in column `column`.

---


<a id="class-treeitem-method-get-button-id"></a>

[int](class_int.md#class-int) **get_button_id**(column: [int](class_int.md#class-int), button_index: [int](class_int.md#class-int)) const [🔗](class_treeitem.md#class-treeitem-method-get-button-id)

Returns the ID for the button at index `button_index` in column `column`.

---


<a id="class-treeitem-method-get-button-tooltip-text"></a>

[String](class_string.md#class-string) **get_button_tooltip_text**(column: [int](class_int.md#class-int), button_index: [int](class_int.md#class-int)) const [🔗](class_treeitem.md#class-treeitem-method-get-button-tooltip-text)

Returns the tooltip text for the button at index `button_index` in column `column`.

---


<a id="class-treeitem-method-get-cell-mode"></a>

[TreeCellMode](class_treeitem.md#enum-treeitem-treecellmode) **get_cell_mode**(column: [int](class_int.md#class-int)) const [🔗](class_treeitem.md#class-treeitem-method-get-cell-mode)

Returns the column's cell mode.

---


<a id="class-treeitem-method-get-child"></a>

[TreeItem](class_treeitem.md#class-treeitem) **get_child**(index: [int](class_int.md#class-int)) [🔗](class_treeitem.md#class-treeitem-method-get-child)

Returns a child item by its `index` (see [get_child_count()](class_treeitem.md#class-treeitem-method-get-child-count)). This method is often used for iterating all children of an item.

Negative indices access the children from the last one.

---


<a id="class-treeitem-method-get-child-count"></a>

[int](class_int.md#class-int) **get_child_count**() [🔗](class_treeitem.md#class-treeitem-method-get-child-count)

Returns the number of child items.

---


<a id="class-treeitem-method-get-children"></a>

[Array](class_array.md#class-array)[[TreeItem](class_treeitem.md#class-treeitem)] **get_children**() [🔗](class_treeitem.md#class-treeitem-method-get-children)

Returns an array of references to the item's children.

---


<a id="class-treeitem-method-get-custom-bg-color"></a>

[Color](class_color.md#class-color) **get_custom_bg_color**(column: [int](class_int.md#class-int)) const [🔗](class_treeitem.md#class-treeitem-method-get-custom-bg-color)

Returns the custom background color of column `column`.

---


<a id="class-treeitem-method-get-custom-color"></a>

[Color](class_color.md#class-color) **get_custom_color**(column: [int](class_int.md#class-int)) const [🔗](class_treeitem.md#class-treeitem-method-get-custom-color)

Returns the custom color of column `column`.

---


<a id="class-treeitem-method-get-custom-draw-callback"></a>

[Callable](class_callable.md#class-callable) **get_custom_draw_callback**(column: [int](class_int.md#class-int)) const [🔗](class_treeitem.md#class-treeitem-method-get-custom-draw-callback)

Returns the custom callback of column `column`.

---


<a id="class-treeitem-method-get-custom-font"></a>

[Font](class_font.md#class-font) **get_custom_font**(column: [int](class_int.md#class-int)) const [🔗](class_treeitem.md#class-treeitem-method-get-custom-font)

Returns custom font used to draw text in the column `column`.

---


<a id="class-treeitem-method-get-custom-font-size"></a>

[int](class_int.md#class-int) **get_custom_font_size**(column: [int](class_int.md#class-int)) const [🔗](class_treeitem.md#class-treeitem-method-get-custom-font-size)

Returns custom font size used to draw text in the column `column`.

---


<a id="class-treeitem-method-get-custom-stylebox"></a>

[StyleBox](class_stylebox.md#class-stylebox) **get_custom_stylebox**(column: [int](class_int.md#class-int)) const [🔗](class_treeitem.md#class-treeitem-method-get-custom-stylebox)

Returns the given column's custom [StyleBox](class_stylebox.md#class-stylebox) used to draw the background.

---


<a id="class-treeitem-method-get-description"></a>

[String](class_string.md#class-string) **get_description**(column: [int](class_int.md#class-int)) const [🔗](class_treeitem.md#class-treeitem-method-get-description)

Returns the given column's description for assistive apps.

---


<a id="class-treeitem-method-get-expand-right"></a>

[bool](class_bool.md#class-bool) **get_expand_right**(column: [int](class_int.md#class-int)) const [🔗](class_treeitem.md#class-treeitem-method-get-expand-right)

Returns `true` if `expand_right` is set.

---


<a id="class-treeitem-method-get-first-child"></a>

[TreeItem](class_treeitem.md#class-treeitem) **get_first_child**() const [🔗](class_treeitem.md#class-treeitem-method-get-first-child)

Returns the TreeItem's first child.

---


<a id="class-treeitem-method-get-icon"></a>

[Texture2D](class_texture2d.md#class-texture2d) **get_icon**(column: [int](class_int.md#class-int)) const [🔗](class_treeitem.md#class-treeitem-method-get-icon)

Returns the given column's icon [Texture2D](class_texture2d.md#class-texture2d). Error if no icon is set.

---


<a id="class-treeitem-method-get-icon-max-width"></a>

[int](class_int.md#class-int) **get_icon_max_width**(column: [int](class_int.md#class-int)) const [🔗](class_treeitem.md#class-treeitem-method-get-icon-max-width)

Returns the maximum allowed width of the icon in the given `column`.

---


<a id="class-treeitem-method-get-icon-modulate"></a>

[Color](class_color.md#class-color) **get_icon_modulate**(column: [int](class_int.md#class-int)) const [🔗](class_treeitem.md#class-treeitem-method-get-icon-modulate)

Returns the [Color](class_color.md#class-color) modulating the column's icon.

---


<a id="class-treeitem-method-get-icon-overlay"></a>

[Texture2D](class_texture2d.md#class-texture2d) **get_icon_overlay**(column: [int](class_int.md#class-int)) const [🔗](class_treeitem.md#class-treeitem-method-get-icon-overlay)

Returns the given column's icon overlay [Texture2D](class_texture2d.md#class-texture2d).

---


<a id="class-treeitem-method-get-icon-region"></a>

[Rect2](class_rect2.md#class-rect2) **get_icon_region**(column: [int](class_int.md#class-int)) const [🔗](class_treeitem.md#class-treeitem-method-get-icon-region)

Returns the icon [Texture2D](class_texture2d.md#class-texture2d) region as [Rect2](class_rect2.md#class-rect2).

---


<a id="class-treeitem-method-get-index"></a>

[int](class_int.md#class-int) **get_index**() [🔗](class_treeitem.md#class-treeitem-method-get-index)

Returns the node's order in the tree. For example, if called on the first child item the position is `0`.

---


<a id="class-treeitem-method-get-language"></a>

[String](class_string.md#class-string) **get_language**(column: [int](class_int.md#class-int)) const [🔗](class_treeitem.md#class-treeitem-method-get-language)

Returns item's text language code.

---


<a id="class-treeitem-method-get-metadata"></a>

[Variant](class_variant.md#class-variant) **get_metadata**(column: [int](class_int.md#class-int)) const [🔗](class_treeitem.md#class-treeitem-method-get-metadata)

Returns the metadata value that was set for the given column using [set_metadata()](class_treeitem.md#class-treeitem-method-set-metadata).

---


<a id="class-treeitem-method-get-next"></a>

[TreeItem](class_treeitem.md#class-treeitem) **get_next**() const [🔗](class_treeitem.md#class-treeitem-method-get-next)

Returns the next sibling TreeItem in the tree or a `null` object if there is none.

---


<a id="class-treeitem-method-get-next-in-tree"></a>

[TreeItem](class_treeitem.md#class-treeitem) **get_next_in_tree**(wrap: [bool](class_bool.md#class-bool) = false) [🔗](class_treeitem.md#class-treeitem-method-get-next-in-tree)

Returns the next TreeItem in the tree (in the context of a depth-first search) or a `null` object if there is none.

If `wrap` is enabled, the method will wrap around to the first element in the tree when called on the last element, otherwise it returns `null`.

---


<a id="class-treeitem-method-get-next-visible"></a>

[TreeItem](class_treeitem.md#class-treeitem) **get_next_visible**(wrap: [bool](class_bool.md#class-bool) = false) [🔗](class_treeitem.md#class-treeitem-method-get-next-visible)

Returns the next visible TreeItem in the tree (in the context of a depth-first search) or a `null` object if there is none.

If `wrap` is enabled, the method will wrap around to the first visible element in the tree when called on the last visible element, otherwise it returns `null`.

---


<a id="class-treeitem-method-get-parent"></a>

[TreeItem](class_treeitem.md#class-treeitem) **get_parent**() const [🔗](class_treeitem.md#class-treeitem-method-get-parent)

Returns the parent TreeItem or a `null` object if there is none.

---


<a id="class-treeitem-method-get-prev"></a>

[TreeItem](class_treeitem.md#class-treeitem) **get_prev**() [🔗](class_treeitem.md#class-treeitem-method-get-prev)

Returns the previous sibling TreeItem in the tree or a `null` object if there is none.

---


<a id="class-treeitem-method-get-prev-in-tree"></a>

[TreeItem](class_treeitem.md#class-treeitem) **get_prev_in_tree**(wrap: [bool](class_bool.md#class-bool) = false) [🔗](class_treeitem.md#class-treeitem-method-get-prev-in-tree)

Returns the previous TreeItem in the tree (in the context of a depth-first search) or a `null` object if there is none.

If `wrap` is enabled, the method will wrap around to the last element in the tree when called on the first visible element, otherwise it returns `null`.

---


<a id="class-treeitem-method-get-prev-visible"></a>

[TreeItem](class_treeitem.md#class-treeitem) **get_prev_visible**(wrap: [bool](class_bool.md#class-bool) = false) [🔗](class_treeitem.md#class-treeitem-method-get-prev-visible)

Returns the previous visible sibling TreeItem in the tree (in the context of a depth-first search) or a `null` object if there is none.

If `wrap` is enabled, the method will wrap around to the last visible element in the tree when called on the first visible element, otherwise it returns `null`.

---


<a id="class-treeitem-method-get-range"></a>

[float](class_float.md#class-float) **get_range**(column: [int](class_int.md#class-int)) const [🔗](class_treeitem.md#class-treeitem-method-get-range)

Returns the value of a [CELL_MODE_RANGE](class_treeitem.md#class-treeitem-constant-cell-mode-range) column.

---


<a id="class-treeitem-method-get-range-config"></a>

[Dictionary](class_dictionary.md#class-dictionary) **get_range_config**(column: [int](class_int.md#class-int)) [🔗](class_treeitem.md#class-treeitem-method-get-range-config)

Returns a dictionary containing the range parameters for a given column. The keys are "min", "max", "step", and "expr".

---


<a id="class-treeitem-method-get-structured-text-bidi-override"></a>

[StructuredTextParser](class_textserver.md#enum-textserver-structuredtextparser) **get_structured_text_bidi_override**(column: [int](class_int.md#class-int)) const [🔗](class_treeitem.md#class-treeitem-method-get-structured-text-bidi-override)

Returns the BiDi algorithm override set for this cell.

---


<a id="class-treeitem-method-get-structured-text-bidi-override-options"></a>

[Array](class_array.md#class-array) **get_structured_text_bidi_override_options**(column: [int](class_int.md#class-int)) const [🔗](class_treeitem.md#class-treeitem-method-get-structured-text-bidi-override-options)

Returns the additional BiDi options set for this cell.

---


<a id="class-treeitem-method-get-suffix"></a>

[String](class_string.md#class-string) **get_suffix**(column: [int](class_int.md#class-int)) const [🔗](class_treeitem.md#class-treeitem-method-get-suffix)

Gets the suffix string shown after the column value.

---


<a id="class-treeitem-method-get-text"></a>

[String](class_string.md#class-string) **get_text**(column: [int](class_int.md#class-int)) const [🔗](class_treeitem.md#class-treeitem-method-get-text)

Returns the given column's text.

---


<a id="class-treeitem-method-get-text-alignment"></a>

[HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) **get_text_alignment**(column: [int](class_int.md#class-int)) const [🔗](class_treeitem.md#class-treeitem-method-get-text-alignment)

Returns the given column's text alignment.

---


<a id="class-treeitem-method-get-text-direction"></a>

[TextDirection](class_control.md#enum-control-textdirection) **get_text_direction**(column: [int](class_int.md#class-int)) const [🔗](class_treeitem.md#class-treeitem-method-get-text-direction)

Returns item's text base writing direction.

---


<a id="class-treeitem-method-get-text-overrun-behavior"></a>

[OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior) **get_text_overrun_behavior**(column: [int](class_int.md#class-int)) const [🔗](class_treeitem.md#class-treeitem-method-get-text-overrun-behavior)

Returns the clipping behavior when the text exceeds the item's bounding rectangle in the given `column`. By default it is [TextServer.OVERRUN_TRIM_ELLIPSIS](class_textserver.md#class-textserver-constant-overrun-trim-ellipsis).

---


<a id="class-treeitem-method-get-tooltip-text"></a>

[String](class_string.md#class-string) **get_tooltip_text**(column: [int](class_int.md#class-int)) const [🔗](class_treeitem.md#class-treeitem-method-get-tooltip-text)

Returns the given column's tooltip text.

---


<a id="class-treeitem-method-get-tree"></a>

[Tree](class_tree.md#class-tree) **get_tree**() const [🔗](class_treeitem.md#class-treeitem-method-get-tree)

Returns the [Tree](class_tree.md#class-tree) that owns this TreeItem.

---


<a id="class-treeitem-method-is-accepting-children"></a>

[bool](class_bool.md#class-bool) **is_accepting_children**() const [🔗](class_treeitem.md#class-treeitem-method-is-accepting-children)

Returns `true` if this **TreeItem** is allowed to accept children.

---


<a id="class-treeitem-method-is-any-collapsed"></a>

[bool](class_bool.md#class-bool) **is_any_collapsed**(only_visible: [bool](class_bool.md#class-bool) = false) [🔗](class_treeitem.md#class-treeitem-method-is-any-collapsed)

Returns `true` if this **TreeItem**, or any of its descendants, is collapsed.

If `only_visible` is `true` it ignores non-visible **TreeItem**s.

---


<a id="class-treeitem-method-is-button-disabled"></a>

[bool](class_bool.md#class-bool) **is_button_disabled**(column: [int](class_int.md#class-int), button_index: [int](class_int.md#class-int)) const [🔗](class_treeitem.md#class-treeitem-method-is-button-disabled)

Returns `true` if the button at index `button_index` for the given `column` is disabled.

---


<a id="class-treeitem-method-is-checked"></a>

[bool](class_bool.md#class-bool) **is_checked**(column: [int](class_int.md#class-int)) const [🔗](class_treeitem.md#class-treeitem-method-is-checked)

Returns `true` if the given `column` is checked.

---


<a id="class-treeitem-method-is-custom-set-as-button"></a>

[bool](class_bool.md#class-bool) **is_custom_set_as_button**(column: [int](class_int.md#class-int)) const [🔗](class_treeitem.md#class-treeitem-method-is-custom-set-as-button)

Returns `true` if the cell was made into a button with [set_custom_as_button()](class_treeitem.md#class-treeitem-method-set-custom-as-button).

---


<a id="class-treeitem-method-is-edit-multiline"></a>

[bool](class_bool.md#class-bool) **is_edit_multiline**(column: [int](class_int.md#class-int)) const [🔗](class_treeitem.md#class-treeitem-method-is-edit-multiline)

Returns `true` if the given `column` is multiline editable.

---


<a id="class-treeitem-method-is-editable"></a>

[bool](class_bool.md#class-bool) **is_editable**(column: [int](class_int.md#class-int)) [🔗](class_treeitem.md#class-treeitem-method-is-editable)

Returns `true` if the given `column` is editable.

---


<a id="class-treeitem-method-is-indeterminate"></a>

[bool](class_bool.md#class-bool) **is_indeterminate**(column: [int](class_int.md#class-int)) const [🔗](class_treeitem.md#class-treeitem-method-is-indeterminate)

Returns `true` if the given `column` is indeterminate.

---


<a id="class-treeitem-method-is-selectable"></a>

[bool](class_bool.md#class-bool) **is_selectable**(column: [int](class_int.md#class-int)) const [🔗](class_treeitem.md#class-treeitem-method-is-selectable)

Returns `true` if the given `column` is selectable.

---


<a id="class-treeitem-method-is-selected"></a>

[bool](class_bool.md#class-bool) **is_selected**(column: [int](class_int.md#class-int)) [🔗](class_treeitem.md#class-treeitem-method-is-selected)

Returns `true` if the given `column` is selected.

---


<a id="class-treeitem-method-is-visible-in-tree"></a>

[bool](class_bool.md#class-bool) **is_visible_in_tree**() const [🔗](class_treeitem.md#class-treeitem-method-is-visible-in-tree)

Returns `true` if [visible](class_treeitem.md#class-treeitem-property-visible) is `true` and all its ancestors are also visible.

---


<a id="class-treeitem-method-move-after"></a>

void **move_after**(item: [TreeItem](class_treeitem.md#class-treeitem)) [🔗](class_treeitem.md#class-treeitem-method-move-after)

Moves this TreeItem right after the given `item`.

**Note:** You can't move to the root or move the root.

---


<a id="class-treeitem-method-move-before"></a>

void **move_before**(item: [TreeItem](class_treeitem.md#class-treeitem)) [🔗](class_treeitem.md#class-treeitem-method-move-before)

Moves this TreeItem right before the given `item`.

**Note:** You can't move to the root or move the root.

---


<a id="class-treeitem-method-propagate-check"></a>

void **propagate_check**(column: [int](class_int.md#class-int), emit_signal: [bool](class_bool.md#class-bool) = true) [🔗](class_treeitem.md#class-treeitem-method-propagate-check)

Propagates this item's checked status to its children and parents for the given `column`. It is possible to process the items affected by this method call by connecting to [Tree.check_propagated_to_item](class_tree.md#class-tree-signal-check-propagated-to-item). The order that the items affected will be processed is as follows: the item invoking this method, children of that item, and finally parents of that item. If `emit_signal` is `false`, then [Tree.check_propagated_to_item](class_tree.md#class-tree-signal-check-propagated-to-item) will not be emitted.

---


<a id="class-treeitem-method-remove-child"></a>

void **remove_child**(child: [TreeItem](class_treeitem.md#class-treeitem)) [🔗](class_treeitem.md#class-treeitem-method-remove-child)

Removes the given child **TreeItem** and all its children from the [Tree](class_tree.md#class-tree). Note that it doesn't free the item from memory, so it can be reused later (see [add_child()](class_treeitem.md#class-treeitem-method-add-child)). To completely remove a **TreeItem** use [Object.free()](class_object.md#class-object-method-free).

**Note:** If you want to move a child from one [Tree](class_tree.md#class-tree) to another, then instead of removing and adding it manually you can use [move_before()](class_treeitem.md#class-treeitem-method-move-before) or [move_after()](class_treeitem.md#class-treeitem-method-move-after).

---


<a id="class-treeitem-method-select"></a>

void **select**(column: [int](class_int.md#class-int), set_as_cursor: [bool](class_bool.md#class-bool) = true) [🔗](class_treeitem.md#class-treeitem-method-select)

Selects the given `column`. If `set_as_cursor` is `true`, the [Tree](class_tree.md#class-tree)'s cursor will be moved to this item (only matters if [Tree.select_mode](class_tree.md#class-tree-property-select-mode) is set to [Tree.SELECT_MULTI](class_tree.md#class-tree-constant-select-multi)).

---


<a id="class-treeitem-method-set-accept-children"></a>

void **set_accept_children**(allowed: [bool](class_bool.md#class-bool)) [🔗](class_treeitem.md#class-treeitem-method-set-accept-children)

Sets **TreeItem**'s ability to accept children.

---


<a id="class-treeitem-method-set-auto-translate-mode"></a>

void **set_auto_translate_mode**(column: [int](class_int.md#class-int), mode: [AutoTranslateMode](class_node.md#enum-node-autotranslatemode)) [🔗](class_treeitem.md#class-treeitem-method-set-auto-translate-mode)

Sets the given column's auto translate mode to `mode`.

All columns use [Node.AUTO_TRANSLATE_MODE_INHERIT](class_node.md#class-node-constant-auto-translate-mode-inherit) by default, which uses the same auto translate mode as the [Tree](class_tree.md#class-tree) itself.

---


<a id="class-treeitem-method-set-autowrap-mode"></a>

void **set_autowrap_mode**(column: [int](class_int.md#class-int), autowrap_mode: [AutowrapMode](class_textserver.md#enum-textserver-autowrapmode)) [🔗](class_treeitem.md#class-treeitem-method-set-autowrap-mode)

Sets the autowrap mode in the given `column`. If set to something other than [TextServer.AUTOWRAP_OFF](class_textserver.md#class-textserver-constant-autowrap-off), the text gets wrapped inside the cell's bounding rectangle.

---


<a id="class-treeitem-method-set-autowrap-trim-flags"></a>

void **set_autowrap_trim_flags**(column: [int](class_int.md#class-int), flags: BitField[[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)]) [🔗](class_treeitem.md#class-treeitem-method-set-autowrap-trim-flags)

Sets the autowrap trim flags for the given `column`. These flags control whether leading and trailing spaces are trimmed on wrapped lines. Set to `0` to disable all trimming.

---


<a id="class-treeitem-method-set-button"></a>

void **set_button**(column: [int](class_int.md#class-int), button_index: [int](class_int.md#class-int), button: [Texture2D](class_texture2d.md#class-texture2d)) [🔗](class_treeitem.md#class-treeitem-method-set-button)

Sets the given column's button [Texture2D](class_texture2d.md#class-texture2d) at index `button_index` to `button`.

---


<a id="class-treeitem-method-set-button-color"></a>

void **set_button_color**(column: [int](class_int.md#class-int), button_index: [int](class_int.md#class-int), color: [Color](class_color.md#class-color)) [🔗](class_treeitem.md#class-treeitem-method-set-button-color)

Sets the given column's button color at index `button_index` to `color`.

---


<a id="class-treeitem-method-set-button-description"></a>

void **set_button_description**(column: [int](class_int.md#class-int), button_index: [int](class_int.md#class-int), description: [String](class_string.md#class-string)) [🔗](class_treeitem.md#class-treeitem-method-set-button-description)

Sets the given column's button description at index `button_index` for assistive apps.

---


<a id="class-treeitem-method-set-button-disabled"></a>

void **set_button_disabled**(column: [int](class_int.md#class-int), button_index: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool)) [🔗](class_treeitem.md#class-treeitem-method-set-button-disabled)

If `true`, disables the button at index `button_index` in the given `column`.

---


<a id="class-treeitem-method-set-button-tooltip-text"></a>

void **set_button_tooltip_text**(column: [int](class_int.md#class-int), button_index: [int](class_int.md#class-int), tooltip: [String](class_string.md#class-string)) [🔗](class_treeitem.md#class-treeitem-method-set-button-tooltip-text)

Sets the tooltip text for the button at index `button_index` in the given `column`.

---


<a id="class-treeitem-method-set-cell-mode"></a>

void **set_cell_mode**(column: [int](class_int.md#class-int), mode: [TreeCellMode](class_treeitem.md#enum-treeitem-treecellmode)) [🔗](class_treeitem.md#class-treeitem-method-set-cell-mode)

Sets the given column's cell mode to `mode`. This determines how the cell is displayed and edited.

---


<a id="class-treeitem-method-set-checked"></a>

void **set_checked**(column: [int](class_int.md#class-int), checked: [bool](class_bool.md#class-bool)) [🔗](class_treeitem.md#class-treeitem-method-set-checked)

If `checked` is `true`, the given `column` is checked. Clears column's indeterminate status.

---


<a id="class-treeitem-method-set-collapsed-recursive"></a>

void **set_collapsed_recursive**(enable: [bool](class_bool.md#class-bool)) [🔗](class_treeitem.md#class-treeitem-method-set-collapsed-recursive)

Collapses or uncollapses this **TreeItem** and all the descendants of this item.

---


<a id="class-treeitem-method-set-custom-as-button"></a>

void **set_custom_as_button**(column: [int](class_int.md#class-int), enable: [bool](class_bool.md#class-bool)) [🔗](class_treeitem.md#class-treeitem-method-set-custom-as-button)

Makes a cell with [CELL_MODE_CUSTOM](class_treeitem.md#class-treeitem-constant-cell-mode-custom) display as a non-flat button with a [StyleBox](class_stylebox.md#class-stylebox).

---


<a id="class-treeitem-method-set-custom-bg-color"></a>

void **set_custom_bg_color**(column: [int](class_int.md#class-int), color: [Color](class_color.md#class-color), just_outline: [bool](class_bool.md#class-bool) = false) [🔗](class_treeitem.md#class-treeitem-method-set-custom-bg-color)

Sets the given column's custom background color and whether to just use it as an outline.

**Note:** If a custom [StyleBox](class_stylebox.md#class-stylebox) is set, the background color will be drawn behind it.

---


<a id="class-treeitem-method-set-custom-color"></a>

void **set_custom_color**(column: [int](class_int.md#class-int), color: [Color](class_color.md#class-color)) [🔗](class_treeitem.md#class-treeitem-method-set-custom-color)

Sets the given column's custom color.

---


<a id="class-treeitem-method-set-custom-draw"></a>

void **set_custom_draw**(column: [int](class_int.md#class-int), object: [Object](class_object.md#class-object), callback: [StringName](class_stringname.md#class-stringname)) [🔗](class_treeitem.md#class-treeitem-method-set-custom-draw)

**Deprecated:** Use [set_custom_draw_callback()](class_treeitem.md#class-treeitem-method-set-custom-draw-callback) instead.

Sets the given column's custom draw callback to the `callback` method on `object`.

The method named `callback` should accept two arguments: the **TreeItem** that is drawn and its position and size as a [Rect2](class_rect2.md#class-rect2).

---


<a id="class-treeitem-method-set-custom-draw-callback"></a>

void **set_custom_draw_callback**(column: [int](class_int.md#class-int), callback: [Callable](class_callable.md#class-callable)) [🔗](class_treeitem.md#class-treeitem-method-set-custom-draw-callback)

Sets the given column's custom draw callback. Use an empty [Callable](class_callable.md#class-callable) (`Callable()`) to clear the custom callback. The cell has to be in [CELL_MODE_CUSTOM](class_treeitem.md#class-treeitem-constant-cell-mode-custom) to use this feature.

The `callback` should accept two arguments: the **TreeItem** that is drawn and its position and size as a [Rect2](class_rect2.md#class-rect2).

To draw custom content over the native style, please use [Tree.get_custom_drawing_canvas_item()](class_tree.md#class-tree-method-get-custom-drawing-canvas-item).

---


<a id="class-treeitem-method-set-custom-font"></a>

void **set_custom_font**(column: [int](class_int.md#class-int), font: [Font](class_font.md#class-font)) [🔗](class_treeitem.md#class-treeitem-method-set-custom-font)

Sets custom font used to draw text in the given `column`.

---


<a id="class-treeitem-method-set-custom-font-size"></a>

void **set_custom_font_size**(column: [int](class_int.md#class-int), font_size: [int](class_int.md#class-int)) [🔗](class_treeitem.md#class-treeitem-method-set-custom-font-size)

Sets custom font size used to draw text in the given `column`.

---


<a id="class-treeitem-method-set-custom-stylebox"></a>

void **set_custom_stylebox**(column: [int](class_int.md#class-int), stylebox: [StyleBox](class_stylebox.md#class-stylebox)) [🔗](class_treeitem.md#class-treeitem-method-set-custom-stylebox)

Sets the given column's custom [StyleBox](class_stylebox.md#class-stylebox) used to draw the background.

**Note:** If a custom background color is set, the [StyleBox](class_stylebox.md#class-stylebox) will be drawn in front of it.

---


<a id="class-treeitem-method-set-description"></a>

void **set_description**(column: [int](class_int.md#class-int), description: [String](class_string.md#class-string)) [🔗](class_treeitem.md#class-treeitem-method-set-description)

Sets the given column's description for assistive apps.

---


<a id="class-treeitem-method-set-edit-multiline"></a>

void **set_edit_multiline**(column: [int](class_int.md#class-int), multiline: [bool](class_bool.md#class-bool)) [🔗](class_treeitem.md#class-treeitem-method-set-edit-multiline)

If `multiline` is `true`, the given `column` is multiline editable.

**Note:** This option only affects the type of control ([LineEdit](class_lineedit.md#class-lineedit) or [TextEdit](class_textedit.md#class-textedit)) that appears when editing the column. You can set multiline values with [set_text()](class_treeitem.md#class-treeitem-method-set-text) even if the column is not multiline editable.

---


<a id="class-treeitem-method-set-editable"></a>

void **set_editable**(column: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool)) [🔗](class_treeitem.md#class-treeitem-method-set-editable)

If `enabled` is `true`, the given `column` is editable.

---


<a id="class-treeitem-method-set-expand-right"></a>

void **set_expand_right**(column: [int](class_int.md#class-int), enable: [bool](class_bool.md#class-bool)) [🔗](class_treeitem.md#class-treeitem-method-set-expand-right)

If `enable` is `true`, the given `column` is expanded to the right.

---


<a id="class-treeitem-method-set-icon"></a>

void **set_icon**(column: [int](class_int.md#class-int), texture: [Texture2D](class_texture2d.md#class-texture2d)) [🔗](class_treeitem.md#class-treeitem-method-set-icon)

Sets the given cell's icon [Texture2D](class_texture2d.md#class-texture2d). If the cell is in [CELL_MODE_ICON](class_treeitem.md#class-treeitem-constant-cell-mode-icon) mode, the icon is displayed in the center of the cell. Otherwise, the icon is displayed before the cell's text. [CELL_MODE_RANGE](class_treeitem.md#class-treeitem-constant-cell-mode-range) does not display an icon.

---


<a id="class-treeitem-method-set-icon-max-width"></a>

void **set_icon_max_width**(column: [int](class_int.md#class-int), width: [int](class_int.md#class-int)) [🔗](class_treeitem.md#class-treeitem-method-set-icon-max-width)

Sets the maximum allowed width of the icon in the given `column`. This limit is applied on top of the default size of the icon and on top of [Tree.icon_max_width](class_tree.md#class-tree-theme-constant-icon-max-width). The height is adjusted according to the icon's ratio.

---


<a id="class-treeitem-method-set-icon-modulate"></a>

void **set_icon_modulate**(column: [int](class_int.md#class-int), modulate: [Color](class_color.md#class-color)) [🔗](class_treeitem.md#class-treeitem-method-set-icon-modulate)

Modulates the given column's icon with `modulate`.

---


<a id="class-treeitem-method-set-icon-overlay"></a>

void **set_icon_overlay**(column: [int](class_int.md#class-int), texture: [Texture2D](class_texture2d.md#class-texture2d)) [🔗](class_treeitem.md#class-treeitem-method-set-icon-overlay)

Sets the given cell's icon overlay [Texture2D](class_texture2d.md#class-texture2d). The cell has to be in [CELL_MODE_ICON](class_treeitem.md#class-treeitem-constant-cell-mode-icon) mode, and icon has to be set. Overlay is drawn on top of icon, in the bottom left corner.

---


<a id="class-treeitem-method-set-icon-region"></a>

void **set_icon_region**(column: [int](class_int.md#class-int), region: [Rect2](class_rect2.md#class-rect2)) [🔗](class_treeitem.md#class-treeitem-method-set-icon-region)

Sets the given column's icon's texture region.

---


<a id="class-treeitem-method-set-indeterminate"></a>

void **set_indeterminate**(column: [int](class_int.md#class-int), indeterminate: [bool](class_bool.md#class-bool)) [🔗](class_treeitem.md#class-treeitem-method-set-indeterminate)

If `indeterminate` is `true`, the given `column` is marked indeterminate.

**Note:** If set `true` from `false`, then column is cleared of checked status.

---


<a id="class-treeitem-method-set-language"></a>

void **set_language**(column: [int](class_int.md#class-int), language: [String](class_string.md#class-string)) [🔗](class_treeitem.md#class-treeitem-method-set-language)

Sets the language code of the given `column`'s text to `language`. This is used for line-breaking and text shaping algorithms. If `language` is empty, the current locale is used.

---


<a id="class-treeitem-method-set-metadata"></a>

void **set_metadata**(column: [int](class_int.md#class-int), meta: [Variant](class_variant.md#class-variant)) [🔗](class_treeitem.md#class-treeitem-method-set-metadata)

Sets the metadata value for the given column, which can be retrieved later using [get_metadata()](class_treeitem.md#class-treeitem-method-get-metadata). This can be used, for example, to store a reference to the original data.

---


<a id="class-treeitem-method-set-range"></a>

void **set_range**(column: [int](class_int.md#class-int), value: [float](class_float.md#class-float)) [🔗](class_treeitem.md#class-treeitem-method-set-range)

Sets the value of a [CELL_MODE_RANGE](class_treeitem.md#class-treeitem-constant-cell-mode-range) column.

---


<a id="class-treeitem-method-set-range-config"></a>

void **set_range_config**(column: [int](class_int.md#class-int), min: [float](class_float.md#class-float), max: [float](class_float.md#class-float), step: [float](class_float.md#class-float), expr: [bool](class_bool.md#class-bool) = false) [🔗](class_treeitem.md#class-treeitem-method-set-range-config)

Sets the range of accepted values for a column. The column must be in the [CELL_MODE_RANGE](class_treeitem.md#class-treeitem-constant-cell-mode-range) mode.

If `expr` is `true`, the edit mode slider will use an exponential scale as with [Range.exp_edit](class_range.md#class-range-property-exp-edit).

---


<a id="class-treeitem-method-set-selectable"></a>

void **set_selectable**(column: [int](class_int.md#class-int), selectable: [bool](class_bool.md#class-bool)) [🔗](class_treeitem.md#class-treeitem-method-set-selectable)

If `selectable` is `true`, the given `column` is selectable.

---


<a id="class-treeitem-method-set-structured-text-bidi-override"></a>

void **set_structured_text_bidi_override**(column: [int](class_int.md#class-int), parser: [StructuredTextParser](class_textserver.md#enum-textserver-structuredtextparser)) [🔗](class_treeitem.md#class-treeitem-method-set-structured-text-bidi-override)

Set BiDi algorithm override for the structured text. Has effect for cells that display text.

---


<a id="class-treeitem-method-set-structured-text-bidi-override-options"></a>

void **set_structured_text_bidi_override_options**(column: [int](class_int.md#class-int), args: [Array](class_array.md#class-array)) [🔗](class_treeitem.md#class-treeitem-method-set-structured-text-bidi-override-options)

Set additional options for BiDi override. Has effect for cells that display text.

---


<a id="class-treeitem-method-set-suffix"></a>

void **set_suffix**(column: [int](class_int.md#class-int), text: [String](class_string.md#class-string)) [🔗](class_treeitem.md#class-treeitem-method-set-suffix)

Sets a string to be shown after a column's value (for example, a unit abbreviation).

---


<a id="class-treeitem-method-set-text"></a>

void **set_text**(column: [int](class_int.md#class-int), text: [String](class_string.md#class-string)) [🔗](class_treeitem.md#class-treeitem-method-set-text)

Sets the given column's text value.

---


<a id="class-treeitem-method-set-text-alignment"></a>

void **set_text_alignment**(column: [int](class_int.md#class-int), text_alignment: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment)) [🔗](class_treeitem.md#class-treeitem-method-set-text-alignment)

Sets the given column's text alignment to `text_alignment`.

---


<a id="class-treeitem-method-set-text-direction"></a>

void **set_text_direction**(column: [int](class_int.md#class-int), direction: [TextDirection](class_control.md#enum-control-textdirection)) [🔗](class_treeitem.md#class-treeitem-method-set-text-direction)

Sets item's text base writing direction.

---


<a id="class-treeitem-method-set-text-overrun-behavior"></a>

void **set_text_overrun_behavior**(column: [int](class_int.md#class-int), overrun_behavior: [OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior)) [🔗](class_treeitem.md#class-treeitem-method-set-text-overrun-behavior)

Sets the clipping behavior when the text exceeds the item's bounding rectangle in the given `column`.

---


<a id="class-treeitem-method-set-tooltip-text"></a>

void **set_tooltip_text**(column: [int](class_int.md#class-int), tooltip: [String](class_string.md#class-string)) [🔗](class_treeitem.md#class-treeitem-method-set-tooltip-text)

Sets the given column's tooltip text.

---


<a id="class-treeitem-method-uncollapse-tree"></a>

void **uncollapse_tree**() [🔗](class_treeitem.md#class-treeitem-method-uncollapse-tree)

Uncollapses all **TreeItem**s necessary to reveal this **TreeItem**, i.e. all ancestor **TreeItem**s.
