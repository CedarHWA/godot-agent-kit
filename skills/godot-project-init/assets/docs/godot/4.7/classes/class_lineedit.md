> Source: https://docs.godotengine.org/en/4.7/classes/class_lineedit.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="lineedit"></a>

<a id="class-lineedit"></a>

# LineEdit

**Inherits:** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

An input field for single-line text.

<a id="description"></a>

## Description

**LineEdit** provides an input field for editing a single line of text.

- When the **LineEdit** control is focused using the keyboard arrow keys, it will only gain focus and not enter edit mode.
- To enter edit mode, click on the control with the mouse, see also [keep_editing_on_text_submit](class_lineedit.md#class-lineedit-property-keep-editing-on-text-submit).
- To exit edit mode, press `ui_text_submit` or `ui_cancel` (by default `Escape`) actions.
- Check [edit()](class_lineedit.md#class-lineedit-method-edit), [unedit()](class_lineedit.md#class-lineedit-method-unedit), [is_editing()](class_lineedit.md#class-lineedit-method-is-editing), and [editing_toggled](class_lineedit.md#class-lineedit-signal-editing-toggled) for more information.

While entering text, it is possible to insert special characters using Unicode, OEM or Windows alt codes:

- To enter Unicode codepoints, hold `Alt` and type the codepoint on the numpad. For example, to enter the character `á` (U+00E1), hold `Alt` and type `+E1` on the numpad (the leading zeroes can be omitted).
- To enter OEM codepoints, hold `Alt` and type the code on the numpad. For example, to enter the character `á` (OEM 160), hold `Alt` and type `160` on the numpad.
- To enter Windows codepoints, hold `Alt` and type the code on the numpad. For example, to enter the character `á` (Windows 0225), hold `Alt` and type `0`, `2`, `2`, `5` on the numpad. The leading zero here must **not** be omitted, as this is how Windows codepoints are distinguished from OEM codepoints.

**Important:**

- Focusing the **LineEdit** with `ui_focus_next` (by default `Tab`) or `ui_focus_prev` (by default `Shift + Tab`) or [Control.grab_focus()](class_control.md#class-control-method-grab-focus) still enters edit mode (for compatibility).

**LineEdit** features many built-in shortcuts that are always available (`Ctrl` here maps to `Cmd` on macOS):

- `Ctrl + C`: Copy
- `Ctrl + X`: Cut
- `Ctrl + V` or `Ctrl + Y`: Paste/"yank"
- `Ctrl + Z`: Undo
- `Ctrl + ~`: Swap input direction.
- `Ctrl + Shift + Z`: Redo
- `Ctrl + U`: Delete text from the caret position to the beginning of the line
- `Ctrl + K`: Delete text from the caret position to the end of the line
- `Ctrl + A`: Select all text
- `Up Arrow`/`Down Arrow`: Move the caret to the beginning/end of the line

On macOS, some extra keyboard shortcuts are available:

- `Cmd + F`: Same as `Right Arrow`, move the caret one character right
- `Cmd + B`: Same as `Left Arrow`, move the caret one character left
- `Cmd + P`: Same as `Up Arrow`, move the caret to the previous line
- `Cmd + N`: Same as `Down Arrow`, move the caret to the next line
- `Cmd + D`: Same as `Delete`, delete the character on the right side of caret
- `Cmd + H`: Same as `Backspace`, delete the character on the left side of the caret
- `Cmd + A`: Same as `Home`, move the caret to the beginning of the line
- `Cmd + E`: Same as `End`, move the caret to the end of the line
- `Cmd + Left Arrow`: Same as `Home`, move the caret to the beginning of the line
- `Cmd + Right Arrow`: Same as `End`, move the caret to the end of the line

**Note:** Caret movement shortcuts listed above are not affected by [shortcut_keys_enabled](class_lineedit.md#class-lineedit-property-shortcut-keys-enabled).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) | [alignment](class_lineedit.md#class-lineedit-property-alignment) | `0` |
| [bool](class_bool.md#class-bool) | [backspace_deletes_composite_character_enabled](class_lineedit.md#class-lineedit-property-backspace-deletes-composite-character-enabled) | `false` |
| [bool](class_bool.md#class-bool) | [caret_blink](class_lineedit.md#class-lineedit-property-caret-blink) | `false` |
| [float](class_float.md#class-float) | [caret_blink_interval](class_lineedit.md#class-lineedit-property-caret-blink-interval) | `0.65` |
| [int](class_int.md#class-int) | [caret_column](class_lineedit.md#class-lineedit-property-caret-column) | `0` |
| [bool](class_bool.md#class-bool) | [caret_force_displayed](class_lineedit.md#class-lineedit-property-caret-force-displayed) | `false` |
| [bool](class_bool.md#class-bool) | [caret_mid_grapheme](class_lineedit.md#class-lineedit-property-caret-mid-grapheme) | `false` |
| [bool](class_bool.md#class-bool) | [clear_button_enabled](class_lineedit.md#class-lineedit-property-clear-button-enabled) | `false` |
| [bool](class_bool.md#class-bool) | [context_menu_enabled](class_lineedit.md#class-lineedit-property-context-menu-enabled) | `true` |
| [bool](class_bool.md#class-bool) | [deselect_on_focus_loss_enabled](class_lineedit.md#class-lineedit-property-deselect-on-focus-loss-enabled) | `true` |
| [bool](class_bool.md#class-bool) | [drag_and_drop_selection_enabled](class_lineedit.md#class-lineedit-property-drag-and-drop-selection-enabled) | `true` |
| [bool](class_bool.md#class-bool) | [draw_control_chars](class_lineedit.md#class-lineedit-property-draw-control-chars) | `false` |
| [bool](class_bool.md#class-bool) | [editable](class_lineedit.md#class-lineedit-property-editable) | `true` |
| [bool](class_bool.md#class-bool) | [emoji_menu_enabled](class_lineedit.md#class-lineedit-property-emoji-menu-enabled) | `true` |
| [bool](class_bool.md#class-bool) | [expand_to_text_length](class_lineedit.md#class-lineedit-property-expand-to-text-length) | `false` |
| [bool](class_bool.md#class-bool) | [flat](class_lineedit.md#class-lineedit-property-flat) | `false` |
| [FocusMode](class_control.md#enum-control-focusmode) | focus_mode | `2` (overrides [Control](class_control.md#class-control-property-focus-mode)) |
| [ExpandMode](class_lineedit.md#enum-lineedit-expandmode) | [icon_expand_mode](class_lineedit.md#class-lineedit-property-icon-expand-mode) | `0` |
| [bool](class_bool.md#class-bool) | [keep_editing_on_text_submit](class_lineedit.md#class-lineedit-property-keep-editing-on-text-submit) | `false` |
| [String](class_string.md#class-string) | [language](class_lineedit.md#class-lineedit-property-language) | `""` |
| [int](class_int.md#class-int) | [max_length](class_lineedit.md#class-lineedit-property-max-length) | `0` |
| [bool](class_bool.md#class-bool) | [middle_mouse_paste_enabled](class_lineedit.md#class-lineedit-property-middle-mouse-paste-enabled) | `true` |
| [CursorShape](class_control.md#enum-control-cursorshape) | mouse_default_cursor_shape | `1` (overrides [Control](class_control.md#class-control-property-mouse-default-cursor-shape)) |
| [String](class_string.md#class-string) | [placeholder_text](class_lineedit.md#class-lineedit-property-placeholder-text) | `""` |
| [Texture2D](class_texture2d.md#class-texture2d) | [right_icon](class_lineedit.md#class-lineedit-property-right-icon) |  |
| [float](class_float.md#class-float) | [right_icon_scale](class_lineedit.md#class-lineedit-property-right-icon-scale) | `1.0` |
| [bool](class_bool.md#class-bool) | [secret](class_lineedit.md#class-lineedit-property-secret) | `false` |
| [String](class_string.md#class-string) | [secret_character](class_lineedit.md#class-lineedit-property-secret-character) | `"•"` |
| [bool](class_bool.md#class-bool) | [select_all_on_focus](class_lineedit.md#class-lineedit-property-select-all-on-focus) | `false` |
| [bool](class_bool.md#class-bool) | [selecting_enabled](class_lineedit.md#class-lineedit-property-selecting-enabled) | `true` |
| [bool](class_bool.md#class-bool) | [shortcut_keys_enabled](class_lineedit.md#class-lineedit-property-shortcut-keys-enabled) | `true` |
| [StructuredTextParser](class_textserver.md#enum-textserver-structuredtextparser) | [structured_text_bidi_override](class_lineedit.md#class-lineedit-property-structured-text-bidi-override) | `0` |
| [Array](class_array.md#class-array) | [structured_text_bidi_override_options](class_lineedit.md#class-lineedit-property-structured-text-bidi-override-options) | `[]` |
| [String](class_string.md#class-string) | [text](class_lineedit.md#class-lineedit-property-text) | `""` |
| [TextDirection](class_control.md#enum-control-textdirection) | [text_direction](class_lineedit.md#class-lineedit-property-text-direction) | `0` |
| [bool](class_bool.md#class-bool) | [virtual_keyboard_enabled](class_lineedit.md#class-lineedit-property-virtual-keyboard-enabled) | `true` |
| [bool](class_bool.md#class-bool) | [virtual_keyboard_show_on_focus](class_lineedit.md#class-lineedit-property-virtual-keyboard-show-on-focus) | `true` |
| [VirtualKeyboardType](class_lineedit.md#enum-lineedit-virtualkeyboardtype) | [virtual_keyboard_type](class_lineedit.md#class-lineedit-property-virtual-keyboard-type) | `0` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [apply_ime](class_lineedit.md#class-lineedit-method-apply-ime)() |
| void | [cancel_ime](class_lineedit.md#class-lineedit-method-cancel-ime)() |
| void | [clear](class_lineedit.md#class-lineedit-method-clear)() |
| void | [delete_char_at_caret](class_lineedit.md#class-lineedit-method-delete-char-at-caret)() |
| void | [delete_text](class_lineedit.md#class-lineedit-method-delete-text)(from_column: [int](class_int.md#class-int), to_column: [int](class_int.md#class-int)) |
| void | [deselect](class_lineedit.md#class-lineedit-method-deselect)() |
| void | [edit](class_lineedit.md#class-lineedit-method-edit)(hide_focus: [bool](class_bool.md#class-bool) = false) |
| [PopupMenu](class_popupmenu.md#class-popupmenu) | [get_menu](class_lineedit.md#class-lineedit-method-get-menu)() const |
| [int](class_int.md#class-int) | [get_next_composite_character_column](class_lineedit.md#class-lineedit-method-get-next-composite-character-column)(column: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_previous_composite_character_column](class_lineedit.md#class-lineedit-method-get-previous-composite-character-column)(column: [int](class_int.md#class-int)) const |
| [float](class_float.md#class-float) | [get_scroll_offset](class_lineedit.md#class-lineedit-method-get-scroll-offset)() const |
| [String](class_string.md#class-string) | [get_selected_text](class_lineedit.md#class-lineedit-method-get-selected-text)() |
| [int](class_int.md#class-int) | [get_selection_from_column](class_lineedit.md#class-lineedit-method-get-selection-from-column)() const |
| [int](class_int.md#class-int) | [get_selection_to_column](class_lineedit.md#class-lineedit-method-get-selection-to-column)() const |
| [bool](class_bool.md#class-bool) | [has_ime_text](class_lineedit.md#class-lineedit-method-has-ime-text)() const |
| [bool](class_bool.md#class-bool) | [has_redo](class_lineedit.md#class-lineedit-method-has-redo)() const |
| [bool](class_bool.md#class-bool) | [has_selection](class_lineedit.md#class-lineedit-method-has-selection)() const |
| [bool](class_bool.md#class-bool) | [has_undo](class_lineedit.md#class-lineedit-method-has-undo)() const |
| void | [insert_text_at_caret](class_lineedit.md#class-lineedit-method-insert-text-at-caret)(text: [String](class_string.md#class-string)) |
| [bool](class_bool.md#class-bool) | [is_editing](class_lineedit.md#class-lineedit-method-is-editing)() const |
| [bool](class_bool.md#class-bool) | [is_menu_visible](class_lineedit.md#class-lineedit-method-is-menu-visible)() const |
| void | [menu_option](class_lineedit.md#class-lineedit-method-menu-option)(option: [int](class_int.md#class-int)) |
| void | [select](class_lineedit.md#class-lineedit-method-select)(from: [int](class_int.md#class-int) = 0, to: [int](class_int.md#class-int) = -1) |
| void | [select_all](class_lineedit.md#class-lineedit-method-select-all)() |
| void | [unedit](class_lineedit.md#class-lineedit-method-unedit)() |

<a id="theme-properties"></a>

## Theme Properties

|  |  |  |
| --- | --- | --- |
| [Color](class_color.md#class-color) | [caret_color](class_lineedit.md#class-lineedit-theme-color-caret-color) | `Color(0.95, 0.95, 0.95, 1)` |
| [Color](class_color.md#class-color) | [clear_button_color](class_lineedit.md#class-lineedit-theme-color-clear-button-color) | `Color(0.875, 0.875, 0.875, 1)` |
| [Color](class_color.md#class-color) | [clear_button_color_pressed](class_lineedit.md#class-lineedit-theme-color-clear-button-color-pressed) | `Color(1, 1, 1, 1)` |
| [Color](class_color.md#class-color) | [font_color](class_lineedit.md#class-lineedit-theme-color-font-color) | `Color(0.875, 0.875, 0.875, 1)` |
| [Color](class_color.md#class-color) | [font_outline_color](class_lineedit.md#class-lineedit-theme-color-font-outline-color) | `Color(0, 0, 0, 1)` |
| [Color](class_color.md#class-color) | [font_placeholder_color](class_lineedit.md#class-lineedit-theme-color-font-placeholder-color) | `Color(0.875, 0.875, 0.875, 0.6)` |
| [Color](class_color.md#class-color) | [font_selected_color](class_lineedit.md#class-lineedit-theme-color-font-selected-color) | `Color(1, 1, 1, 1)` |
| [Color](class_color.md#class-color) | [font_uneditable_color](class_lineedit.md#class-lineedit-theme-color-font-uneditable-color) | `Color(0.875, 0.875, 0.875, 0.5)` |
| [Color](class_color.md#class-color) | [selection_color](class_lineedit.md#class-lineedit-theme-color-selection-color) | `Color(0.5, 0.5, 0.5, 1)` |
| [int](class_int.md#class-int) | [caret_width](class_lineedit.md#class-lineedit-theme-constant-caret-width) | `1` |
| [int](class_int.md#class-int) | [minimum_character_width](class_lineedit.md#class-lineedit-theme-constant-minimum-character-width) | `4` |
| [int](class_int.md#class-int) | [outline_size](class_lineedit.md#class-lineedit-theme-constant-outline-size) | `0` |
| [Font](class_font.md#class-font) | [font](class_lineedit.md#class-lineedit-theme-font-font) |  |
| [int](class_int.md#class-int) | [font_size](class_lineedit.md#class-lineedit-theme-font-size-font-size) |  |
| [Texture2D](class_texture2d.md#class-texture2d) | [clear](class_lineedit.md#class-lineedit-theme-icon-clear) |  |
| [StyleBox](class_stylebox.md#class-stylebox) | [focus](class_lineedit.md#class-lineedit-theme-style-focus) |  |
| [StyleBox](class_stylebox.md#class-stylebox) | [normal](class_lineedit.md#class-lineedit-theme-style-normal) |  |
| [StyleBox](class_stylebox.md#class-stylebox) | [read_only](class_lineedit.md#class-lineedit-theme-style-read-only) |  |

---


<a id="signals"></a>

## Signals

<a id="class-lineedit-signal-editing-toggled"></a>

**editing_toggled**(toggled_on: [bool](class_bool.md#class-bool)) [🔗](class_lineedit.md#class-lineedit-signal-editing-toggled)

Emitted when the **LineEdit** switches in or out of edit mode.

---


<a id="class-lineedit-signal-text-change-rejected"></a>

**text_change_rejected**(rejected_substring: [String](class_string.md#class-string)) [🔗](class_lineedit.md#class-lineedit-signal-text-change-rejected)

Emitted when appending text that overflows the [max_length](class_lineedit.md#class-lineedit-property-max-length). The appended text is truncated to fit [max_length](class_lineedit.md#class-lineedit-property-max-length), and the part that couldn't fit is passed as the `rejected_substring` argument.

---


<a id="class-lineedit-signal-text-changed"></a>

**text_changed**(new_text: [String](class_string.md#class-string)) [🔗](class_lineedit.md#class-lineedit-signal-text-changed)

Emitted when the text changes.

---


<a id="class-lineedit-signal-text-submitted"></a>

**text_submitted**(new_text: [String](class_string.md#class-string)) [🔗](class_lineedit.md#class-lineedit-signal-text-submitted)

Emitted when the user presses the `ui_text_submit` action (by default: `Enter` or `Kp Enter`) while the **LineEdit** has focus.

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-lineedit-menuitems"></a>

enum **MenuItems**: [🔗](class_lineedit.md#enum-lineedit-menuitems)

<a id="class-lineedit-constant-menu-cut"></a>

[MenuItems](class_lineedit.md#enum-lineedit-menuitems) **MENU_CUT** = `0`

Cuts (copies and clears) the selected text.

<a id="class-lineedit-constant-menu-copy"></a>

[MenuItems](class_lineedit.md#enum-lineedit-menuitems) **MENU_COPY** = `1`

Copies the selected text.

<a id="class-lineedit-constant-menu-paste"></a>

[MenuItems](class_lineedit.md#enum-lineedit-menuitems) **MENU_PASTE** = `2`

Pastes the clipboard text over the selected text (or at the caret's position).

Non-printable escape characters are automatically stripped from the OS clipboard via [String.strip_escapes()](class_string.md#class-string-method-strip-escapes).

<a id="class-lineedit-constant-menu-clear"></a>

[MenuItems](class_lineedit.md#enum-lineedit-menuitems) **MENU_CLEAR** = `3`

Erases the whole **LineEdit** text.

<a id="class-lineedit-constant-menu-select-all"></a>

[MenuItems](class_lineedit.md#enum-lineedit-menuitems) **MENU_SELECT_ALL** = `4`

Selects the whole **LineEdit** text.

<a id="class-lineedit-constant-menu-undo"></a>

[MenuItems](class_lineedit.md#enum-lineedit-menuitems) **MENU_UNDO** = `5`

Undoes the previous action.

<a id="class-lineedit-constant-menu-redo"></a>

[MenuItems](class_lineedit.md#enum-lineedit-menuitems) **MENU_REDO** = `6`

Reverse the last undo action.

<a id="class-lineedit-constant-menu-submenu-text-dir"></a>

[MenuItems](class_lineedit.md#enum-lineedit-menuitems) **MENU_SUBMENU_TEXT_DIR** = `7`

ID of "Text Writing Direction" submenu.

<a id="class-lineedit-constant-menu-dir-inherited"></a>

[MenuItems](class_lineedit.md#enum-lineedit-menuitems) **MENU_DIR_INHERITED** = `8`

Sets text direction to inherited.

<a id="class-lineedit-constant-menu-dir-auto"></a>

[MenuItems](class_lineedit.md#enum-lineedit-menuitems) **MENU_DIR_AUTO** = `9`

Sets text direction to automatic.

<a id="class-lineedit-constant-menu-dir-ltr"></a>

[MenuItems](class_lineedit.md#enum-lineedit-menuitems) **MENU_DIR_LTR** = `10`

Sets text direction to left-to-right.

<a id="class-lineedit-constant-menu-dir-rtl"></a>

[MenuItems](class_lineedit.md#enum-lineedit-menuitems) **MENU_DIR_RTL** = `11`

Sets text direction to right-to-left.

<a id="class-lineedit-constant-menu-display-ucc"></a>

[MenuItems](class_lineedit.md#enum-lineedit-menuitems) **MENU_DISPLAY_UCC** = `12`

Toggles control character display.

<a id="class-lineedit-constant-menu-submenu-insert-ucc"></a>

[MenuItems](class_lineedit.md#enum-lineedit-menuitems) **MENU_SUBMENU_INSERT_UCC** = `13`

ID of "Insert Control Character" submenu.

<a id="class-lineedit-constant-menu-insert-lrm"></a>

[MenuItems](class_lineedit.md#enum-lineedit-menuitems) **MENU_INSERT_LRM** = `14`

Inserts left-to-right mark (LRM) character.

<a id="class-lineedit-constant-menu-insert-rlm"></a>

[MenuItems](class_lineedit.md#enum-lineedit-menuitems) **MENU_INSERT_RLM** = `15`

Inserts right-to-left mark (RLM) character.

<a id="class-lineedit-constant-menu-insert-lre"></a>

[MenuItems](class_lineedit.md#enum-lineedit-menuitems) **MENU_INSERT_LRE** = `16`

Inserts start of left-to-right embedding (LRE) character.

<a id="class-lineedit-constant-menu-insert-rle"></a>

[MenuItems](class_lineedit.md#enum-lineedit-menuitems) **MENU_INSERT_RLE** = `17`

Inserts start of right-to-left embedding (RLE) character.

<a id="class-lineedit-constant-menu-insert-lro"></a>

[MenuItems](class_lineedit.md#enum-lineedit-menuitems) **MENU_INSERT_LRO** = `18`

Inserts start of left-to-right override (LRO) character.

<a id="class-lineedit-constant-menu-insert-rlo"></a>

[MenuItems](class_lineedit.md#enum-lineedit-menuitems) **MENU_INSERT_RLO** = `19`

Inserts start of right-to-left override (RLO) character.

<a id="class-lineedit-constant-menu-insert-pdf"></a>

[MenuItems](class_lineedit.md#enum-lineedit-menuitems) **MENU_INSERT_PDF** = `20`

Inserts pop direction formatting (PDF) character.

<a id="class-lineedit-constant-menu-insert-alm"></a>

[MenuItems](class_lineedit.md#enum-lineedit-menuitems) **MENU_INSERT_ALM** = `21`

Inserts Arabic letter mark (ALM) character.

<a id="class-lineedit-constant-menu-insert-lri"></a>

[MenuItems](class_lineedit.md#enum-lineedit-menuitems) **MENU_INSERT_LRI** = `22`

Inserts left-to-right isolate (LRI) character.

<a id="class-lineedit-constant-menu-insert-rli"></a>

[MenuItems](class_lineedit.md#enum-lineedit-menuitems) **MENU_INSERT_RLI** = `23`

Inserts right-to-left isolate (RLI) character.

<a id="class-lineedit-constant-menu-insert-fsi"></a>

[MenuItems](class_lineedit.md#enum-lineedit-menuitems) **MENU_INSERT_FSI** = `24`

Inserts first strong isolate (FSI) character.

<a id="class-lineedit-constant-menu-insert-pdi"></a>

[MenuItems](class_lineedit.md#enum-lineedit-menuitems) **MENU_INSERT_PDI** = `25`

Inserts pop direction isolate (PDI) character.

<a id="class-lineedit-constant-menu-insert-zwj"></a>

[MenuItems](class_lineedit.md#enum-lineedit-menuitems) **MENU_INSERT_ZWJ** = `26`

Inserts zero width joiner (ZWJ) character.

<a id="class-lineedit-constant-menu-insert-zwnj"></a>

[MenuItems](class_lineedit.md#enum-lineedit-menuitems) **MENU_INSERT_ZWNJ** = `27`

Inserts zero width non-joiner (ZWNJ) character.

<a id="class-lineedit-constant-menu-insert-wj"></a>

[MenuItems](class_lineedit.md#enum-lineedit-menuitems) **MENU_INSERT_WJ** = `28`

Inserts word joiner (WJ) character.

<a id="class-lineedit-constant-menu-insert-shy"></a>

[MenuItems](class_lineedit.md#enum-lineedit-menuitems) **MENU_INSERT_SHY** = `29`

Inserts soft hyphen (SHY) character.

<a id="class-lineedit-constant-menu-emoji-and-symbol"></a>

[MenuItems](class_lineedit.md#enum-lineedit-menuitems) **MENU_EMOJI_AND_SYMBOL** = `30`

Opens system emoji and symbol picker.

<a id="class-lineedit-constant-menu-max"></a>

[MenuItems](class_lineedit.md#enum-lineedit-menuitems) **MENU_MAX** = `31`

Represents the size of the [MenuItems](class_lineedit.md#enum-lineedit-menuitems) enum.

---


<a id="enum-lineedit-virtualkeyboardtype"></a>

enum **VirtualKeyboardType**: [🔗](class_lineedit.md#enum-lineedit-virtualkeyboardtype)

<a id="class-lineedit-constant-keyboard-type-default"></a>

[VirtualKeyboardType](class_lineedit.md#enum-lineedit-virtualkeyboardtype) **KEYBOARD_TYPE_DEFAULT** = `0`

Default text virtual keyboard.

<a id="class-lineedit-constant-keyboard-type-multiline"></a>

[VirtualKeyboardType](class_lineedit.md#enum-lineedit-virtualkeyboardtype) **KEYBOARD_TYPE_MULTILINE** = `1`

Multiline virtual keyboard.

<a id="class-lineedit-constant-keyboard-type-number"></a>

[VirtualKeyboardType](class_lineedit.md#enum-lineedit-virtualkeyboardtype) **KEYBOARD_TYPE_NUMBER** = `2`

Virtual number keypad, useful for PIN entry.

<a id="class-lineedit-constant-keyboard-type-number-decimal"></a>

[VirtualKeyboardType](class_lineedit.md#enum-lineedit-virtualkeyboardtype) **KEYBOARD_TYPE_NUMBER_DECIMAL** = `3`

Virtual number keypad, useful for entering fractional numbers.

<a id="class-lineedit-constant-keyboard-type-phone"></a>

[VirtualKeyboardType](class_lineedit.md#enum-lineedit-virtualkeyboardtype) **KEYBOARD_TYPE_PHONE** = `4`

Virtual phone number keypad.

<a id="class-lineedit-constant-keyboard-type-email-address"></a>

[VirtualKeyboardType](class_lineedit.md#enum-lineedit-virtualkeyboardtype) **KEYBOARD_TYPE_EMAIL_ADDRESS** = `5`

Virtual keyboard with additional keys to assist with typing email addresses.

<a id="class-lineedit-constant-keyboard-type-password"></a>

[VirtualKeyboardType](class_lineedit.md#enum-lineedit-virtualkeyboardtype) **KEYBOARD_TYPE_PASSWORD** = `6`

Virtual keyboard for entering a password. On most platforms, this should disable autocomplete and autocapitalization.

**Note:** This is not supported on Web. Instead, this behaves identically to [KEYBOARD_TYPE_DEFAULT](class_lineedit.md#class-lineedit-constant-keyboard-type-default).

<a id="class-lineedit-constant-keyboard-type-url"></a>

[VirtualKeyboardType](class_lineedit.md#enum-lineedit-virtualkeyboardtype) **KEYBOARD_TYPE_URL** = `7`

Virtual keyboard with additional keys to assist with typing URLs.

---


<a id="enum-lineedit-expandmode"></a>

enum **ExpandMode**: [🔗](class_lineedit.md#enum-lineedit-expandmode)

<a id="class-lineedit-constant-expand-mode-original-size"></a>

[ExpandMode](class_lineedit.md#enum-lineedit-expandmode) **EXPAND_MODE_ORIGINAL_SIZE** = `0`

Use the original size for the right icon.

<a id="class-lineedit-constant-expand-mode-fit-to-text"></a>

[ExpandMode](class_lineedit.md#enum-lineedit-expandmode) **EXPAND_MODE_FIT_TO_TEXT** = `1`

Scale the right icon's size to match the size of the text.

<a id="class-lineedit-constant-expand-mode-fit-to-line-edit"></a>

[ExpandMode](class_lineedit.md#enum-lineedit-expandmode) **EXPAND_MODE_FIT_TO_LINE_EDIT** = `2`

Scale the right icon to fit the LineEdit.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-lineedit-property-alignment"></a>

[HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) **alignment** = `0` [🔗](class_lineedit.md#class-lineedit-property-alignment)

- void **set_horizontal_alignment**(value: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment))
- [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) **get_horizontal_alignment**()

The text's horizontal alignment.

---


<a id="class-lineedit-property-backspace-deletes-composite-character-enabled"></a>

[bool](class_bool.md#class-bool) **backspace_deletes_composite_character_enabled** = `false` [🔗](class_lineedit.md#class-lineedit-property-backspace-deletes-composite-character-enabled)

- void **set_backspace_deletes_composite_character_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_backspace_deletes_composite_character_enabled**()

If `true` and [caret_mid_grapheme](class_lineedit.md#class-lineedit-property-caret-mid-grapheme) is `false`, backspace deletes an entire composite character such as ❤️‍🩹, instead of deleting part of the composite character.

---


<a id="class-lineedit-property-caret-blink"></a>

[bool](class_bool.md#class-bool) **caret_blink** = `false` [🔗](class_lineedit.md#class-lineedit-property-caret-blink)

- void **set_caret_blink_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_caret_blink_enabled**()

If `true`, makes the caret blink.

---


<a id="class-lineedit-property-caret-blink-interval"></a>

[float](class_float.md#class-float) **caret_blink_interval** = `0.65` [🔗](class_lineedit.md#class-lineedit-property-caret-blink-interval)

- void **set_caret_blink_interval**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_caret_blink_interval**()

The interval at which the caret blinks (in seconds).

---


<a id="class-lineedit-property-caret-column"></a>

[int](class_int.md#class-int) **caret_column** = `0` [🔗](class_lineedit.md#class-lineedit-property-caret-column)

- void **set_caret_column**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_caret_column**()

The caret's column position inside the **LineEdit**. When set, the text may scroll to accommodate it.

---


<a id="class-lineedit-property-caret-force-displayed"></a>

[bool](class_bool.md#class-bool) **caret_force_displayed** = `false` [🔗](class_lineedit.md#class-lineedit-property-caret-force-displayed)

- void **set_caret_force_displayed**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_caret_force_displayed**()

If `true`, the **LineEdit** will always show the caret, even if not editing or focus is lost.

---


<a id="class-lineedit-property-caret-mid-grapheme"></a>

[bool](class_bool.md#class-bool) **caret_mid_grapheme** = `false` [🔗](class_lineedit.md#class-lineedit-property-caret-mid-grapheme)

- void **set_caret_mid_grapheme_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_caret_mid_grapheme_enabled**()

Allow moving caret, selecting and removing the individual composite character components.

**Note:** `Backspace` is always removing individual composite character components.

---


<a id="class-lineedit-property-clear-button-enabled"></a>

[bool](class_bool.md#class-bool) **clear_button_enabled** = `false` [🔗](class_lineedit.md#class-lineedit-property-clear-button-enabled)

- void **set_clear_button_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_clear_button_enabled**()

If `true`, the **LineEdit** will show a clear button if [text](class_lineedit.md#class-lineedit-property-text) is not empty, which can be used to clear the text quickly.

---


<a id="class-lineedit-property-context-menu-enabled"></a>

[bool](class_bool.md#class-bool) **context_menu_enabled** = `true` [🔗](class_lineedit.md#class-lineedit-property-context-menu-enabled)

- void **set_context_menu_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_context_menu_enabled**()

If `true`, the context menu will appear when right-clicked.

---


<a id="class-lineedit-property-deselect-on-focus-loss-enabled"></a>

[bool](class_bool.md#class-bool) **deselect_on_focus_loss_enabled** = `true` [🔗](class_lineedit.md#class-lineedit-property-deselect-on-focus-loss-enabled)

- void **set_deselect_on_focus_loss_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_deselect_on_focus_loss_enabled**()

If `true`, the selected text will be deselected when focus is lost.

---


<a id="class-lineedit-property-drag-and-drop-selection-enabled"></a>

[bool](class_bool.md#class-bool) **drag_and_drop_selection_enabled** = `true` [🔗](class_lineedit.md#class-lineedit-property-drag-and-drop-selection-enabled)

- void **set_drag_and_drop_selection_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_drag_and_drop_selection_enabled**()

If `true`, allow drag and drop of selected text.

---


<a id="class-lineedit-property-draw-control-chars"></a>

[bool](class_bool.md#class-bool) **draw_control_chars** = `false` [🔗](class_lineedit.md#class-lineedit-property-draw-control-chars)

- void **set_draw_control_chars**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_draw_control_chars**()

If `true`, control characters are displayed.

---


<a id="class-lineedit-property-editable"></a>

[bool](class_bool.md#class-bool) **editable** = `true` [🔗](class_lineedit.md#class-lineedit-property-editable)

- void **set_editable**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_editable**()

If `false`, existing text cannot be modified and new text cannot be added.

---


<a id="class-lineedit-property-emoji-menu-enabled"></a>

[bool](class_bool.md#class-bool) **emoji_menu_enabled** = `true` [🔗](class_lineedit.md#class-lineedit-property-emoji-menu-enabled)

- void **set_emoji_menu_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_emoji_menu_enabled**()

If `true`, "Emoji and Symbols" menu is enabled.

---


<a id="class-lineedit-property-expand-to-text-length"></a>

[bool](class_bool.md#class-bool) **expand_to_text_length** = `false` [🔗](class_lineedit.md#class-lineedit-property-expand-to-text-length)

- void **set_expand_to_text_length_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_expand_to_text_length_enabled**()

If `true`, the **LineEdit** width will increase to stay longer than the [text](class_lineedit.md#class-lineedit-property-text). It will **not** compress if the [text](class_lineedit.md#class-lineedit-property-text) is shortened.

---


<a id="class-lineedit-property-flat"></a>

[bool](class_bool.md#class-bool) **flat** = `false` [🔗](class_lineedit.md#class-lineedit-property-flat)

- void **set_flat**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_flat**()

If `true`, the **LineEdit** doesn't display decoration.

---


<a id="class-lineedit-property-icon-expand-mode"></a>

[ExpandMode](class_lineedit.md#enum-lineedit-expandmode) **icon_expand_mode** = `0` [🔗](class_lineedit.md#class-lineedit-property-icon-expand-mode)

- void **set_icon_expand_mode**(value: [ExpandMode](class_lineedit.md#enum-lineedit-expandmode))
- [ExpandMode](class_lineedit.md#enum-lineedit-expandmode) **get_icon_expand_mode**()

Define the scaling behavior of the [right_icon](class_lineedit.md#class-lineedit-property-right-icon).

---


<a id="class-lineedit-property-keep-editing-on-text-submit"></a>

[bool](class_bool.md#class-bool) **keep_editing_on_text_submit** = `false` [🔗](class_lineedit.md#class-lineedit-property-keep-editing-on-text-submit)

- void **set_keep_editing_on_text_submit**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_editing_kept_on_text_submit**()

If `true`, the **LineEdit** will not exit edit mode when text is submitted by pressing `ui_text_submit` action (by default: `Enter` or `Kp Enter`).

---


<a id="class-lineedit-property-language"></a>

[String](class_string.md#class-string) **language** = `""` [🔗](class_lineedit.md#class-lineedit-property-language)

- void **set_language**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_language**()

Language code used for line-breaking and text shaping algorithms. If left empty, the current locale is used instead.

---


<a id="class-lineedit-property-max-length"></a>

[int](class_int.md#class-int) **max_length** = `0` [🔗](class_lineedit.md#class-lineedit-property-max-length)

- void **set_max_length**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_max_length**()

Maximum number of characters that can be entered inside the **LineEdit**. If `0`, there is no limit.

When a limit is defined, characters that would exceed [max_length](class_lineedit.md#class-lineedit-property-max-length) are truncated. This happens both for existing [text](class_lineedit.md#class-lineedit-property-text) contents when setting the max length, or for new text inserted in the **LineEdit**, including pasting.

If any input text is truncated, the [text_change_rejected](class_lineedit.md#class-lineedit-signal-text-change-rejected) signal is emitted with the truncated substring as a parameter:

```gdscript
text = "Hello world"
max_length = 5
# `text` becomes "Hello".
max_length = 10
text += " goodbye"
# `text` becomes "Hello good".
# `text_change_rejected` is emitted with "bye" as a parameter.
```

```csharp
Text = "Hello world";
MaxLength = 5;
// `Text` becomes "Hello".
MaxLength = 10;
Text += " goodbye";
// `Text` becomes "Hello good".
// `text_change_rejected` is emitted with "bye" as a parameter.
```

---


<a id="class-lineedit-property-middle-mouse-paste-enabled"></a>

[bool](class_bool.md#class-bool) **middle_mouse_paste_enabled** = `true` [🔗](class_lineedit.md#class-lineedit-property-middle-mouse-paste-enabled)

- void **set_middle_mouse_paste_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_middle_mouse_paste_enabled**()

If `false`, using middle mouse button to paste clipboard will be disabled.

**Note:** This method is only implemented on Linux.

---


<a id="class-lineedit-property-placeholder-text"></a>

[String](class_string.md#class-string) **placeholder_text** = `""` [🔗](class_lineedit.md#class-lineedit-property-placeholder-text)

- void **set_placeholder**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_placeholder**()

Text shown when the **LineEdit** is empty. It is **not** the **LineEdit**'s default value (see [text](class_lineedit.md#class-lineedit-property-text)).

---


<a id="class-lineedit-property-right-icon"></a>

[Texture2D](class_texture2d.md#class-texture2d) **right_icon** [🔗](class_lineedit.md#class-lineedit-property-right-icon)

- void **set_right_icon**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_right_icon**()

Sets the icon that will appear in the right end of the **LineEdit** if there's no [text](class_lineedit.md#class-lineedit-property-text), or always, if [clear_button_enabled](class_lineedit.md#class-lineedit-property-clear-button-enabled) is set to `false`.

---


<a id="class-lineedit-property-right-icon-scale"></a>

[float](class_float.md#class-float) **right_icon_scale** = `1.0` [🔗](class_lineedit.md#class-lineedit-property-right-icon-scale)

- void **set_right_icon_scale**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_right_icon_scale**()

Scale ratio of the icon when [icon_expand_mode](class_lineedit.md#class-lineedit-property-icon-expand-mode) is set to [EXPAND_MODE_FIT_TO_LINE_EDIT](class_lineedit.md#class-lineedit-constant-expand-mode-fit-to-line-edit).

---


<a id="class-lineedit-property-secret"></a>

[bool](class_bool.md#class-bool) **secret** = `false` [🔗](class_lineedit.md#class-lineedit-property-secret)

- void **set_secret**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_secret**()

If `true`, every character is replaced with the secret character (see [secret_character](class_lineedit.md#class-lineedit-property-secret-character)).

---


<a id="class-lineedit-property-secret-character"></a>

[String](class_string.md#class-string) **secret_character** = `"•"` [🔗](class_lineedit.md#class-lineedit-property-secret-character)

- void **set_secret_character**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_secret_character**()

The character to use to mask secret input. Only a single character can be used as the secret character. If it is longer than one character, only the first one will be used. If it is empty, a space will be used instead.

---


<a id="class-lineedit-property-select-all-on-focus"></a>

[bool](class_bool.md#class-bool) **select_all_on_focus** = `false` [🔗](class_lineedit.md#class-lineedit-property-select-all-on-focus)

- void **set_select_all_on_focus**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_select_all_on_focus**()

If `true`, the **LineEdit** will select the whole text when it gains focus.

---


<a id="class-lineedit-property-selecting-enabled"></a>

[bool](class_bool.md#class-bool) **selecting_enabled** = `true` [🔗](class_lineedit.md#class-lineedit-property-selecting-enabled)

- void **set_selecting_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_selecting_enabled**()

If `false`, it's impossible to select the text using mouse nor keyboard.

---


<a id="class-lineedit-property-shortcut-keys-enabled"></a>

[bool](class_bool.md#class-bool) **shortcut_keys_enabled** = `true` [🔗](class_lineedit.md#class-lineedit-property-shortcut-keys-enabled)

- void **set_shortcut_keys_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_shortcut_keys_enabled**()

If `true`, shortcut keys for context menu items are enabled, even if the context menu is disabled.

---


<a id="class-lineedit-property-structured-text-bidi-override"></a>

[StructuredTextParser](class_textserver.md#enum-textserver-structuredtextparser) **structured_text_bidi_override** = `0` [🔗](class_lineedit.md#class-lineedit-property-structured-text-bidi-override)

- void **set_structured_text_bidi_override**(value: [StructuredTextParser](class_textserver.md#enum-textserver-structuredtextparser))
- [StructuredTextParser](class_textserver.md#enum-textserver-structuredtextparser) **get_structured_text_bidi_override**()

Set BiDi algorithm override for the structured text.

---


<a id="class-lineedit-property-structured-text-bidi-override-options"></a>

[Array](class_array.md#class-array) **structured_text_bidi_override_options** = `[]` [🔗](class_lineedit.md#class-lineedit-property-structured-text-bidi-override-options)

- void **set_structured_text_bidi_override_options**(value: [Array](class_array.md#class-array))
- [Array](class_array.md#class-array) **get_structured_text_bidi_override_options**()

Set additional options for BiDi override.

---


<a id="class-lineedit-property-text"></a>

[String](class_string.md#class-string) **text** = `""` [🔗](class_lineedit.md#class-lineedit-property-text)

- void **set_text**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_text**()

String value of the **LineEdit**.

**Note:** Changing text using this property won't emit the [text_changed](class_lineedit.md#class-lineedit-signal-text-changed) signal.

---


<a id="class-lineedit-property-text-direction"></a>

[TextDirection](class_control.md#enum-control-textdirection) **text_direction** = `0` [🔗](class_lineedit.md#class-lineedit-property-text-direction)

- void **set_text_direction**(value: [TextDirection](class_control.md#enum-control-textdirection))
- [TextDirection](class_control.md#enum-control-textdirection) **get_text_direction**()

Base text writing direction.

---


<a id="class-lineedit-property-virtual-keyboard-enabled"></a>

[bool](class_bool.md#class-bool) **virtual_keyboard_enabled** = `true` [🔗](class_lineedit.md#class-lineedit-property-virtual-keyboard-enabled)

- void **set_virtual_keyboard_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_virtual_keyboard_enabled**()

If `true`, the native virtual keyboard is enabled on platforms that support it.

---


<a id="class-lineedit-property-virtual-keyboard-show-on-focus"></a>

[bool](class_bool.md#class-bool) **virtual_keyboard_show_on_focus** = `true` [🔗](class_lineedit.md#class-lineedit-property-virtual-keyboard-show-on-focus)

- void **set_virtual_keyboard_show_on_focus**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_virtual_keyboard_show_on_focus**()

If `true`, the native virtual keyboard is shown on focus events on platforms that support it.

---


<a id="class-lineedit-property-virtual-keyboard-type"></a>

[VirtualKeyboardType](class_lineedit.md#enum-lineedit-virtualkeyboardtype) **virtual_keyboard_type** = `0` [🔗](class_lineedit.md#class-lineedit-property-virtual-keyboard-type)

- void **set_virtual_keyboard_type**(value: [VirtualKeyboardType](class_lineedit.md#enum-lineedit-virtualkeyboardtype))
- [VirtualKeyboardType](class_lineedit.md#enum-lineedit-virtualkeyboardtype) **get_virtual_keyboard_type**()

Specifies the type of virtual keyboard to show.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-lineedit-method-apply-ime"></a>

void **apply_ime**() [🔗](class_lineedit.md#class-lineedit-method-apply-ime)

Applies text from the [Input Method Editor](https://en.wikipedia.org/wiki/Input_method) (IME) and closes the IME if it is open.

---


<a id="class-lineedit-method-cancel-ime"></a>

void **cancel_ime**() [🔗](class_lineedit.md#class-lineedit-method-cancel-ime)

Closes the [Input Method Editor](https://en.wikipedia.org/wiki/Input_method) (IME) if it is open. Any text in the IME will be lost.

---


<a id="class-lineedit-method-clear"></a>

void **clear**() [🔗](class_lineedit.md#class-lineedit-method-clear)

Erases the **LineEdit**'s [text](class_lineedit.md#class-lineedit-property-text).

---


<a id="class-lineedit-method-delete-char-at-caret"></a>

void **delete_char_at_caret**() [🔗](class_lineedit.md#class-lineedit-method-delete-char-at-caret)

Deletes one character at the caret's current position (equivalent to pressing `Delete`).

---


<a id="class-lineedit-method-delete-text"></a>

void **delete_text**(from_column: [int](class_int.md#class-int), to_column: [int](class_int.md#class-int)) [🔗](class_lineedit.md#class-lineedit-method-delete-text)

Deletes a section of the [text](class_lineedit.md#class-lineedit-property-text) going from position `from_column` to `to_column`. Both parameters should be within the text's length.

---


<a id="class-lineedit-method-deselect"></a>

void **deselect**() [🔗](class_lineedit.md#class-lineedit-method-deselect)

Clears the current selection.

---


<a id="class-lineedit-method-edit"></a>

void **edit**(hide_focus: [bool](class_bool.md#class-bool) = false) [🔗](class_lineedit.md#class-lineedit-method-edit)

Allows entering edit mode whether the **LineEdit** is focused or not. If `hide_focus` is `true`, the focused state will not be shown (see [Control.grab_focus()](class_control.md#class-control-method-grab-focus)).

See also [keep_editing_on_text_submit](class_lineedit.md#class-lineedit-property-keep-editing-on-text-submit).

---


<a id="class-lineedit-method-get-menu"></a>

[PopupMenu](class_popupmenu.md#class-popupmenu) **get_menu**() const [🔗](class_lineedit.md#class-lineedit-method-get-menu)

Returns the [PopupMenu](class_popupmenu.md#class-popupmenu) of this **LineEdit**. By default, this menu is displayed when right-clicking on the **LineEdit**.

You can add custom menu items or remove standard ones. Make sure your IDs don't conflict with the standard ones (see [MenuItems](class_lineedit.md#enum-lineedit-menuitems)). For example:

```gdscript
func _ready():
    var menu = get_menu()
    # Remove all items after "Redo".
    menu.item_count = menu.get_item_index(MENU_REDO) + 1
    # Add custom items.
    menu.add_separator()
    menu.add_item("Insert Date", MENU_MAX + 1)
    # Connect callback.
    menu.id_pressed.connect(_on_item_pressed)

func _on_item_pressed(id):
    if id == MENU_MAX + 1:
        insert_text_at_caret(Time.get_date_string_from_system())
```

```csharp
public override void _Ready()
{
    var menu = GetMenu();
    // Remove all items after "Redo".
    menu.ItemCount = menu.GetItemIndex(LineEdit.MenuItems.Redo) + 1;
    // Add custom items.
    menu.AddSeparator();
    menu.AddItem("Insert Date", LineEdit.MenuItems.Max + 1);
    // Add event handler.
    menu.IdPressed += OnItemPressed;
}

public void OnItemPressed(int id)
{
    if (id == LineEdit.MenuItems.Max + 1)
    {
        InsertTextAtCaret(Time.GetDateStringFromSystem());
    }
}
```

**Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [Window.visible](class_window.md#class-window-property-visible) property.

---


<a id="class-lineedit-method-get-next-composite-character-column"></a>

[int](class_int.md#class-int) **get_next_composite_character_column**(column: [int](class_int.md#class-int)) const [🔗](class_lineedit.md#class-lineedit-method-get-next-composite-character-column)

Returns the correct column at the end of a composite character like ❤️‍🩹 (mending heart; Unicode: `U+2764 U+FE0F U+200D U+1FA79`) which is comprised of more than one Unicode code point, if the caret is at the start of the composite character. Also returns the correct column with the caret at mid grapheme and for non-composite characters.

**Note:** To check at caret location use `get_next_composite_character_column(get_caret_column())`

---


<a id="class-lineedit-method-get-previous-composite-character-column"></a>

[int](class_int.md#class-int) **get_previous_composite_character_column**(column: [int](class_int.md#class-int)) const [🔗](class_lineedit.md#class-lineedit-method-get-previous-composite-character-column)

Returns the correct column at the start of a composite character like ❤️‍🩹 (mending heart; Unicode: `U+2764 U+FE0F U+200D U+1FA79`) which is comprised of more than one Unicode code point, if the caret is at the end of the composite character. Also returns the correct column with the caret at mid grapheme and for non-composite characters.

**Note:** To check at caret location use `get_previous_composite_character_column(get_caret_column())`

---


<a id="class-lineedit-method-get-scroll-offset"></a>

[float](class_float.md#class-float) **get_scroll_offset**() const [🔗](class_lineedit.md#class-lineedit-method-get-scroll-offset)

Returns the scroll offset due to [caret_column](class_lineedit.md#class-lineedit-property-caret-column), as a number of characters.

---


<a id="class-lineedit-method-get-selected-text"></a>

[String](class_string.md#class-string) **get_selected_text**() [🔗](class_lineedit.md#class-lineedit-method-get-selected-text)

Returns the text inside the selection.

---


<a id="class-lineedit-method-get-selection-from-column"></a>

[int](class_int.md#class-int) **get_selection_from_column**() const [🔗](class_lineedit.md#class-lineedit-method-get-selection-from-column)

Returns the selection begin column.

---


<a id="class-lineedit-method-get-selection-to-column"></a>

[int](class_int.md#class-int) **get_selection_to_column**() const [🔗](class_lineedit.md#class-lineedit-method-get-selection-to-column)

Returns the selection end column.

---


<a id="class-lineedit-method-has-ime-text"></a>

[bool](class_bool.md#class-bool) **has_ime_text**() const [🔗](class_lineedit.md#class-lineedit-method-has-ime-text)

Returns `true` if the user has text in the [Input Method Editor](https://en.wikipedia.org/wiki/Input_method) (IME).

---


<a id="class-lineedit-method-has-redo"></a>

[bool](class_bool.md#class-bool) **has_redo**() const [🔗](class_lineedit.md#class-lineedit-method-has-redo)

Returns `true` if a "redo" action is available.

---


<a id="class-lineedit-method-has-selection"></a>

[bool](class_bool.md#class-bool) **has_selection**() const [🔗](class_lineedit.md#class-lineedit-method-has-selection)

Returns `true` if the user has selected text.

---


<a id="class-lineedit-method-has-undo"></a>

[bool](class_bool.md#class-bool) **has_undo**() const [🔗](class_lineedit.md#class-lineedit-method-has-undo)

Returns `true` if an "undo" action is available.

---


<a id="class-lineedit-method-insert-text-at-caret"></a>

void **insert_text_at_caret**(text: [String](class_string.md#class-string)) [🔗](class_lineedit.md#class-lineedit-method-insert-text-at-caret)

Inserts `text` at the caret. If the resulting value is longer than [max_length](class_lineedit.md#class-lineedit-property-max-length), nothing happens.

---


<a id="class-lineedit-method-is-editing"></a>

[bool](class_bool.md#class-bool) **is_editing**() const [🔗](class_lineedit.md#class-lineedit-method-is-editing)

Returns whether the **LineEdit** is being edited.

---


<a id="class-lineedit-method-is-menu-visible"></a>

[bool](class_bool.md#class-bool) **is_menu_visible**() const [🔗](class_lineedit.md#class-lineedit-method-is-menu-visible)

Returns whether the menu is visible. Use this instead of `get_menu().visible` to improve performance (so the creation of the menu is avoided).

---


<a id="class-lineedit-method-menu-option"></a>

void **menu_option**(option: [int](class_int.md#class-int)) [🔗](class_lineedit.md#class-lineedit-method-menu-option)

Executes a given action as defined in the [MenuItems](class_lineedit.md#enum-lineedit-menuitems) enum.

---


<a id="class-lineedit-method-select"></a>

void **select**(from: [int](class_int.md#class-int) = 0, to: [int](class_int.md#class-int) = -1) [🔗](class_lineedit.md#class-lineedit-method-select)

Selects characters inside **LineEdit** between `from` and `to`. By default, `from` is at the beginning and `to` at the end.

```gdscript
text = "Welcome"
select() # Will select "Welcome".
select(4) # Will select "ome".
select(2, 5) # Will select "lco".
```

```csharp
Text = "Welcome";
Select(); // Will select "Welcome".
Select(4); // Will select "ome".
Select(2, 5); // Will select "lco".
```

---


<a id="class-lineedit-method-select-all"></a>

void **select_all**() [🔗](class_lineedit.md#class-lineedit-method-select-all)

Selects the whole [String](class_string.md#class-string).

---


<a id="class-lineedit-method-unedit"></a>

void **unedit**() [🔗](class_lineedit.md#class-lineedit-method-unedit)

Allows exiting edit mode while preserving focus.

---


<a id="theme-property-descriptions"></a>

## Theme Property Descriptions

<a id="class-lineedit-theme-color-caret-color"></a>

[Color](class_color.md#class-color) **caret_color** = `Color(0.95, 0.95, 0.95, 1)` [🔗](class_lineedit.md#class-lineedit-theme-color-caret-color)

Color of the **LineEdit**'s caret (text cursor). This can be set to a fully transparent color to hide the caret entirely.

---


<a id="class-lineedit-theme-color-clear-button-color"></a>

[Color](class_color.md#class-color) **clear_button_color** = `Color(0.875, 0.875, 0.875, 1)` [🔗](class_lineedit.md#class-lineedit-theme-color-clear-button-color)

Color used as default tint for the clear button.

---


<a id="class-lineedit-theme-color-clear-button-color-pressed"></a>

[Color](class_color.md#class-color) **clear_button_color_pressed** = `Color(1, 1, 1, 1)` [🔗](class_lineedit.md#class-lineedit-theme-color-clear-button-color-pressed)

Color used for the clear button when it's pressed.

---


<a id="class-lineedit-theme-color-font-color"></a>

[Color](class_color.md#class-color) **font_color** = `Color(0.875, 0.875, 0.875, 1)` [🔗](class_lineedit.md#class-lineedit-theme-color-font-color)

Default font color.

---


<a id="class-lineedit-theme-color-font-outline-color"></a>

[Color](class_color.md#class-color) **font_outline_color** = `Color(0, 0, 0, 1)` [🔗](class_lineedit.md#class-lineedit-theme-color-font-outline-color)

The tint of text outline of the **LineEdit**.

---


<a id="class-lineedit-theme-color-font-placeholder-color"></a>

[Color](class_color.md#class-color) **font_placeholder_color** = `Color(0.875, 0.875, 0.875, 0.6)` [🔗](class_lineedit.md#class-lineedit-theme-color-font-placeholder-color)

Font color for [placeholder_text](class_lineedit.md#class-lineedit-property-placeholder-text).

---


<a id="class-lineedit-theme-color-font-selected-color"></a>

[Color](class_color.md#class-color) **font_selected_color** = `Color(1, 1, 1, 1)` [🔗](class_lineedit.md#class-lineedit-theme-color-font-selected-color)

Font color for selected text (inside the selection rectangle).

---


<a id="class-lineedit-theme-color-font-uneditable-color"></a>

[Color](class_color.md#class-color) **font_uneditable_color** = `Color(0.875, 0.875, 0.875, 0.5)` [🔗](class_lineedit.md#class-lineedit-theme-color-font-uneditable-color)

Font color when editing is disabled.

---


<a id="class-lineedit-theme-color-selection-color"></a>

[Color](class_color.md#class-color) **selection_color** = `Color(0.5, 0.5, 0.5, 1)` [🔗](class_lineedit.md#class-lineedit-theme-color-selection-color)

Color of the selection rectangle.

---


<a id="class-lineedit-theme-constant-caret-width"></a>

[int](class_int.md#class-int) **caret_width** = `1` [🔗](class_lineedit.md#class-lineedit-theme-constant-caret-width)

The caret's width in pixels. Greater values can be used to improve accessibility by ensuring the caret is easily visible, or to ensure consistency with a large font size.

---


<a id="class-lineedit-theme-constant-minimum-character-width"></a>

[int](class_int.md#class-int) **minimum_character_width** = `4` [🔗](class_lineedit.md#class-lineedit-theme-constant-minimum-character-width)

Minimum horizontal space for the text (not counting the clear button and content margins). This value is measured in count of 'M' characters (i.e. this number of 'M' characters can be displayed without scrolling).

---


<a id="class-lineedit-theme-constant-outline-size"></a>

[int](class_int.md#class-int) **outline_size** = `0` [🔗](class_lineedit.md#class-lineedit-theme-constant-outline-size)

The size of the text outline.

**Note:** If using a font with [FontFile.multichannel_signed_distance_field](class_fontfile.md#class-fontfile-property-multichannel-signed-distance-field) enabled, its [FontFile.msdf_pixel_range](class_fontfile.md#class-fontfile-property-msdf-pixel-range) must be set to at least *twice* the value of [outline_size](class_lineedit.md#class-lineedit-theme-constant-outline-size) for outline rendering to look correct. Otherwise, the outline may appear to be cut off earlier than intended.

---


<a id="class-lineedit-theme-font-font"></a>

[Font](class_font.md#class-font) **font** [🔗](class_lineedit.md#class-lineedit-theme-font-font)

Font used for the text.

---


<a id="class-lineedit-theme-font-size-font-size"></a>

[int](class_int.md#class-int) **font_size** [🔗](class_lineedit.md#class-lineedit-theme-font-size-font-size)

Font size of the **LineEdit**'s text.

---


<a id="class-lineedit-theme-icon-clear"></a>

[Texture2D](class_texture2d.md#class-texture2d) **clear** [🔗](class_lineedit.md#class-lineedit-theme-icon-clear)

Texture for the clear button. See [clear_button_enabled](class_lineedit.md#class-lineedit-property-clear-button-enabled).

---


<a id="class-lineedit-theme-style-focus"></a>

[StyleBox](class_stylebox.md#class-stylebox) **focus** [🔗](class_lineedit.md#class-lineedit-theme-style-focus)

Background used when **LineEdit** has GUI focus. The [focus](class_lineedit.md#class-lineedit-theme-style-focus) [StyleBox](class_stylebox.md#class-stylebox) is displayed *over* the base [StyleBox](class_stylebox.md#class-stylebox), so a partially transparent [StyleBox](class_stylebox.md#class-stylebox) should be used to ensure the base [StyleBox](class_stylebox.md#class-stylebox) remains visible. A [StyleBox](class_stylebox.md#class-stylebox) that represents an outline or an underline works well for this purpose. To disable the focus visual effect, assign a [StyleBoxEmpty](class_styleboxempty.md#class-styleboxempty) resource. Note that disabling the focus visual effect will harm keyboard/controller navigation usability, so this is not recommended for accessibility reasons.

---


<a id="class-lineedit-theme-style-normal"></a>

[StyleBox](class_stylebox.md#class-stylebox) **normal** [🔗](class_lineedit.md#class-lineedit-theme-style-normal)

Default background for the **LineEdit**.

---


<a id="class-lineedit-theme-style-read-only"></a>

[StyleBox](class_stylebox.md#class-stylebox) **read_only** [🔗](class_lineedit.md#class-lineedit-theme-style-read-only)

Background used when **LineEdit** is in read-only mode ([editable](class_lineedit.md#class-lineedit-property-editable) is set to `false`).
