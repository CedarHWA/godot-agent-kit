> Source: https://docs.godotengine.org/en/4.7/classes/class_nativemenu.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="nativemenu"></a>

<a id="class-nativemenu"></a>

# NativeMenu

**Inherits:** [Object](class_object.md#class-object)

A server interface for OS native menus.

<a id="description"></a>

## Description

**NativeMenu** handles low-level access to the OS native global menu bar and popup menus.

**Note:** This is low-level API, consider using [MenuBar](class_menubar.md#class-menubar) with [MenuBar.prefer_global_menu](class_menubar.md#class-menubar-property-prefer-global-menu) set to `true`, and [PopupMenu](class_popupmenu.md#class-popupmenu) with [PopupMenu.prefer_native_menu](class_popupmenu.md#class-popupmenu-property-prefer-native-menu) set to `true`.

To create a menu, use [create_menu()](class_nativemenu.md#class-nativemenu-method-create-menu), add menu items using `add_*_item` methods. To remove a menu, use [free_menu()](class_nativemenu.md#class-nativemenu-method-free-menu).

```gdscript
var menu

func _menu_callback(item_id):
    if item_id == "ITEM_CUT":
        cut()
    elif item_id == "ITEM_COPY":
        copy()
    elif item_id == "ITEM_PASTE":
        paste()

func _enter_tree():
    # Create new menu and add items:
    menu = NativeMenu.create_menu()
    NativeMenu.add_item(menu, "Cut", _menu_callback, Callable(), "ITEM_CUT")
    NativeMenu.add_item(menu, "Copy", _menu_callback, Callable(), "ITEM_COPY")
    NativeMenu.add_separator(menu)
    NativeMenu.add_item(menu, "Paste", _menu_callback, Callable(), "ITEM_PASTE")

func _on_button_pressed():
    # Show popup menu at mouse position:
    NativeMenu.popup(menu, DisplayServer.mouse_get_position())

func _exit_tree():
    # Remove menu when it's no longer needed:
    NativeMenu.free_menu(menu)
```

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [int](class_int.md#class-int) | [add_check_item](class_nativemenu.md#class-nativemenu-method-add-check-item)(rid: [RID](class_rid.md#class-rid), label: [String](class_string.md#class-string), callback: [Callable](class_callable.md#class-callable) = Callable(), key_callback: [Callable](class_callable.md#class-callable) = Callable(), tag: [Variant](class_variant.md#class-variant) = null, accelerator: [Key](class_@globalscope.md#enum-globalscope-key) = 0, index: [int](class_int.md#class-int) = -1) |
| [int](class_int.md#class-int) | [add_icon_check_item](class_nativemenu.md#class-nativemenu-method-add-icon-check-item)(rid: [RID](class_rid.md#class-rid), icon: [Texture2D](class_texture2d.md#class-texture2d), label: [String](class_string.md#class-string), callback: [Callable](class_callable.md#class-callable) = Callable(), key_callback: [Callable](class_callable.md#class-callable) = Callable(), tag: [Variant](class_variant.md#class-variant) = null, accelerator: [Key](class_@globalscope.md#enum-globalscope-key) = 0, index: [int](class_int.md#class-int) = -1) |
| [int](class_int.md#class-int) | [add_icon_item](class_nativemenu.md#class-nativemenu-method-add-icon-item)(rid: [RID](class_rid.md#class-rid), icon: [Texture2D](class_texture2d.md#class-texture2d), label: [String](class_string.md#class-string), callback: [Callable](class_callable.md#class-callable) = Callable(), key_callback: [Callable](class_callable.md#class-callable) = Callable(), tag: [Variant](class_variant.md#class-variant) = null, accelerator: [Key](class_@globalscope.md#enum-globalscope-key) = 0, index: [int](class_int.md#class-int) = -1) |
| [int](class_int.md#class-int) | [add_icon_radio_check_item](class_nativemenu.md#class-nativemenu-method-add-icon-radio-check-item)(rid: [RID](class_rid.md#class-rid), icon: [Texture2D](class_texture2d.md#class-texture2d), label: [String](class_string.md#class-string), callback: [Callable](class_callable.md#class-callable) = Callable(), key_callback: [Callable](class_callable.md#class-callable) = Callable(), tag: [Variant](class_variant.md#class-variant) = null, accelerator: [Key](class_@globalscope.md#enum-globalscope-key) = 0, index: [int](class_int.md#class-int) = -1) |
| [int](class_int.md#class-int) | [add_item](class_nativemenu.md#class-nativemenu-method-add-item)(rid: [RID](class_rid.md#class-rid), label: [String](class_string.md#class-string), callback: [Callable](class_callable.md#class-callable) = Callable(), key_callback: [Callable](class_callable.md#class-callable) = Callable(), tag: [Variant](class_variant.md#class-variant) = null, accelerator: [Key](class_@globalscope.md#enum-globalscope-key) = 0, index: [int](class_int.md#class-int) = -1) |
| [int](class_int.md#class-int) | [add_multistate_item](class_nativemenu.md#class-nativemenu-method-add-multistate-item)(rid: [RID](class_rid.md#class-rid), label: [String](class_string.md#class-string), max_states: [int](class_int.md#class-int), default_state: [int](class_int.md#class-int), callback: [Callable](class_callable.md#class-callable) = Callable(), key_callback: [Callable](class_callable.md#class-callable) = Callable(), tag: [Variant](class_variant.md#class-variant) = null, accelerator: [Key](class_@globalscope.md#enum-globalscope-key) = 0, index: [int](class_int.md#class-int) = -1) |
| [int](class_int.md#class-int) | [add_radio_check_item](class_nativemenu.md#class-nativemenu-method-add-radio-check-item)(rid: [RID](class_rid.md#class-rid), label: [String](class_string.md#class-string), callback: [Callable](class_callable.md#class-callable) = Callable(), key_callback: [Callable](class_callable.md#class-callable) = Callable(), tag: [Variant](class_variant.md#class-variant) = null, accelerator: [Key](class_@globalscope.md#enum-globalscope-key) = 0, index: [int](class_int.md#class-int) = -1) |
| [int](class_int.md#class-int) | [add_separator](class_nativemenu.md#class-nativemenu-method-add-separator)(rid: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int) = -1) |
| [int](class_int.md#class-int) | [add_submenu_item](class_nativemenu.md#class-nativemenu-method-add-submenu-item)(rid: [RID](class_rid.md#class-rid), label: [String](class_string.md#class-string), submenu_rid: [RID](class_rid.md#class-rid), tag: [Variant](class_variant.md#class-variant) = null, index: [int](class_int.md#class-int) = -1) |
| void | [clear](class_nativemenu.md#class-nativemenu-method-clear)(rid: [RID](class_rid.md#class-rid)) |
| [RID](class_rid.md#class-rid) | [create_menu](class_nativemenu.md#class-nativemenu-method-create-menu)() |
| [int](class_int.md#class-int) | [find_item_index_with_submenu](class_nativemenu.md#class-nativemenu-method-find-item-index-with-submenu)(rid: [RID](class_rid.md#class-rid), submenu_rid: [RID](class_rid.md#class-rid)) const |
| [int](class_int.md#class-int) | [find_item_index_with_tag](class_nativemenu.md#class-nativemenu-method-find-item-index-with-tag)(rid: [RID](class_rid.md#class-rid), tag: [Variant](class_variant.md#class-variant)) const |
| [int](class_int.md#class-int) | [find_item_index_with_text](class_nativemenu.md#class-nativemenu-method-find-item-index-with-text)(rid: [RID](class_rid.md#class-rid), text: [String](class_string.md#class-string)) const |
| void | [free_menu](class_nativemenu.md#class-nativemenu-method-free-menu)(rid: [RID](class_rid.md#class-rid)) |
| [Key](class_@globalscope.md#enum-globalscope-key) | [get_item_accelerator](class_nativemenu.md#class-nativemenu-method-get-item-accelerator)(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int)) const |
| [Callable](class_callable.md#class-callable) | [get_item_callback](class_nativemenu.md#class-nativemenu-method-get-item-callback)(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_item_count](class_nativemenu.md#class-nativemenu-method-get-item-count)(rid: [RID](class_rid.md#class-rid)) const |
| [Texture2D](class_texture2d.md#class-texture2d) | [get_item_icon](class_nativemenu.md#class-nativemenu-method-get-item-icon)(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_item_indentation_level](class_nativemenu.md#class-nativemenu-method-get-item-indentation-level)(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int)) const |
| [Callable](class_callable.md#class-callable) | [get_item_key_callback](class_nativemenu.md#class-nativemenu-method-get-item-key-callback)(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_item_max_states](class_nativemenu.md#class-nativemenu-method-get-item-max-states)(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_item_state](class_nativemenu.md#class-nativemenu-method-get-item-state)(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int)) const |
| [RID](class_rid.md#class-rid) | [get_item_submenu](class_nativemenu.md#class-nativemenu-method-get-item-submenu)(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int)) const |
| [Variant](class_variant.md#class-variant) | [get_item_tag](class_nativemenu.md#class-nativemenu-method-get-item-tag)(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int)) const |
| [String](class_string.md#class-string) | [get_item_text](class_nativemenu.md#class-nativemenu-method-get-item-text)(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int)) const |
| [String](class_string.md#class-string) | [get_item_tooltip](class_nativemenu.md#class-nativemenu-method-get-item-tooltip)(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int)) const |
| [float](class_float.md#class-float) | [get_minimum_width](class_nativemenu.md#class-nativemenu-method-get-minimum-width)(rid: [RID](class_rid.md#class-rid)) const |
| [Callable](class_callable.md#class-callable) | [get_popup_close_callback](class_nativemenu.md#class-nativemenu-method-get-popup-close-callback)(rid: [RID](class_rid.md#class-rid)) const |
| [Callable](class_callable.md#class-callable) | [get_popup_open_callback](class_nativemenu.md#class-nativemenu-method-get-popup-open-callback)(rid: [RID](class_rid.md#class-rid)) const |
| [Vector2](class_vector2.md#class-vector2) | [get_size](class_nativemenu.md#class-nativemenu-method-get-size)(rid: [RID](class_rid.md#class-rid)) const |
| [RID](class_rid.md#class-rid) | [get_system_menu](class_nativemenu.md#class-nativemenu-method-get-system-menu)(menu_id: [SystemMenus](class_nativemenu.md#enum-nativemenu-systemmenus)) const |
| [String](class_string.md#class-string) | [get_system_menu_name](class_nativemenu.md#class-nativemenu-method-get-system-menu-name)(menu_id: [SystemMenus](class_nativemenu.md#enum-nativemenu-systemmenus)) const |
| [String](class_string.md#class-string) | [get_system_menu_text](class_nativemenu.md#class-nativemenu-method-get-system-menu-text)(menu_id: [SystemMenus](class_nativemenu.md#enum-nativemenu-systemmenus)) const |
| [bool](class_bool.md#class-bool) | [has_feature](class_nativemenu.md#class-nativemenu-method-has-feature)(feature: [Feature](class_nativemenu.md#enum-nativemenu-feature)) const |
| [bool](class_bool.md#class-bool) | [has_menu](class_nativemenu.md#class-nativemenu-method-has-menu)(rid: [RID](class_rid.md#class-rid)) const |
| [bool](class_bool.md#class-bool) | [has_system_menu](class_nativemenu.md#class-nativemenu-method-has-system-menu)(menu_id: [SystemMenus](class_nativemenu.md#enum-nativemenu-systemmenus)) const |
| [bool](class_bool.md#class-bool) | [is_item_checkable](class_nativemenu.md#class-nativemenu-method-is-item-checkable)(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [is_item_checked](class_nativemenu.md#class-nativemenu-method-is-item-checked)(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [is_item_disabled](class_nativemenu.md#class-nativemenu-method-is-item-disabled)(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [is_item_hidden](class_nativemenu.md#class-nativemenu-method-is-item-hidden)(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [is_item_radio_checkable](class_nativemenu.md#class-nativemenu-method-is-item-radio-checkable)(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [is_opened](class_nativemenu.md#class-nativemenu-method-is-opened)(rid: [RID](class_rid.md#class-rid)) const |
| [bool](class_bool.md#class-bool) | [is_system_menu](class_nativemenu.md#class-nativemenu-method-is-system-menu)(rid: [RID](class_rid.md#class-rid)) const |
| void | [popup](class_nativemenu.md#class-nativemenu-method-popup)(rid: [RID](class_rid.md#class-rid), position: [Vector2i](class_vector2i.md#class-vector2i)) |
| void | [remove_item](class_nativemenu.md#class-nativemenu-method-remove-item)(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int)) |
| void | [set_interface_direction](class_nativemenu.md#class-nativemenu-method-set-interface-direction)(rid: [RID](class_rid.md#class-rid), is_rtl: [bool](class_bool.md#class-bool)) |
| void | [set_item_accelerator](class_nativemenu.md#class-nativemenu-method-set-item-accelerator)(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), keycode: [Key](class_@globalscope.md#enum-globalscope-key)) |
| void | [set_item_callback](class_nativemenu.md#class-nativemenu-method-set-item-callback)(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), callback: [Callable](class_callable.md#class-callable)) |
| void | [set_item_checkable](class_nativemenu.md#class-nativemenu-method-set-item-checkable)(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), checkable: [bool](class_bool.md#class-bool)) |
| void | [set_item_checked](class_nativemenu.md#class-nativemenu-method-set-item-checked)(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), checked: [bool](class_bool.md#class-bool)) |
| void | [set_item_disabled](class_nativemenu.md#class-nativemenu-method-set-item-disabled)(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool)) |
| void | [set_item_hidden](class_nativemenu.md#class-nativemenu-method-set-item-hidden)(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), hidden: [bool](class_bool.md#class-bool)) |
| void | [set_item_hover_callbacks](class_nativemenu.md#class-nativemenu-method-set-item-hover-callbacks)(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), callback: [Callable](class_callable.md#class-callable)) |
| void | [set_item_icon](class_nativemenu.md#class-nativemenu-method-set-item-icon)(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), icon: [Texture2D](class_texture2d.md#class-texture2d)) |
| void | [set_item_indentation_level](class_nativemenu.md#class-nativemenu-method-set-item-indentation-level)(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), level: [int](class_int.md#class-int)) |
| [int](class_int.md#class-int) | [set_item_index](class_nativemenu.md#class-nativemenu-method-set-item-index)(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), target_idx: [int](class_int.md#class-int)) |
| void | [set_item_key_callback](class_nativemenu.md#class-nativemenu-method-set-item-key-callback)(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), key_callback: [Callable](class_callable.md#class-callable)) |
| void | [set_item_max_states](class_nativemenu.md#class-nativemenu-method-set-item-max-states)(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), max_states: [int](class_int.md#class-int)) |
| void | [set_item_radio_checkable](class_nativemenu.md#class-nativemenu-method-set-item-radio-checkable)(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), checkable: [bool](class_bool.md#class-bool)) |
| void | [set_item_state](class_nativemenu.md#class-nativemenu-method-set-item-state)(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), state: [int](class_int.md#class-int)) |
| void | [set_item_submenu](class_nativemenu.md#class-nativemenu-method-set-item-submenu)(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), submenu_rid: [RID](class_rid.md#class-rid)) |
| void | [set_item_tag](class_nativemenu.md#class-nativemenu-method-set-item-tag)(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), tag: [Variant](class_variant.md#class-variant)) |
| void | [set_item_text](class_nativemenu.md#class-nativemenu-method-set-item-text)(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), text: [String](class_string.md#class-string)) |
| void | [set_item_tooltip](class_nativemenu.md#class-nativemenu-method-set-item-tooltip)(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), tooltip: [String](class_string.md#class-string)) |
| void | [set_minimum_width](class_nativemenu.md#class-nativemenu-method-set-minimum-width)(rid: [RID](class_rid.md#class-rid), width: [float](class_float.md#class-float)) |
| void | [set_popup_close_callback](class_nativemenu.md#class-nativemenu-method-set-popup-close-callback)(rid: [RID](class_rid.md#class-rid), callback: [Callable](class_callable.md#class-callable)) |
| void | [set_popup_open_callback](class_nativemenu.md#class-nativemenu-method-set-popup-open-callback)(rid: [RID](class_rid.md#class-rid), callback: [Callable](class_callable.md#class-callable)) |
| void | [set_system_menu_text](class_nativemenu.md#class-nativemenu-method-set-system-menu-text)(menu_id: [SystemMenus](class_nativemenu.md#enum-nativemenu-systemmenus), name: [String](class_string.md#class-string)) |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-nativemenu-feature"></a>

enum **Feature**: [🔗](class_nativemenu.md#enum-nativemenu-feature)

<a id="class-nativemenu-constant-feature-global-menu"></a>

[Feature](class_nativemenu.md#enum-nativemenu-feature) **FEATURE_GLOBAL_MENU** = `0`

**NativeMenu** supports native global main menu.

<a id="class-nativemenu-constant-feature-popup-menu"></a>

[Feature](class_nativemenu.md#enum-nativemenu-feature) **FEATURE_POPUP_MENU** = `1`

**NativeMenu** supports native popup menus.

<a id="class-nativemenu-constant-feature-open-close-callback"></a>

[Feature](class_nativemenu.md#enum-nativemenu-feature) **FEATURE_OPEN_CLOSE_CALLBACK** = `2`

**NativeMenu** supports menu open and close callbacks.

<a id="class-nativemenu-constant-feature-hover-callback"></a>

[Feature](class_nativemenu.md#enum-nativemenu-feature) **FEATURE_HOVER_CALLBACK** = `3`

**NativeMenu** supports menu item hover callback.

<a id="class-nativemenu-constant-feature-key-callback"></a>

[Feature](class_nativemenu.md#enum-nativemenu-feature) **FEATURE_KEY_CALLBACK** = `4`

**NativeMenu** supports menu item accelerator/key callback.

---


<a id="enum-nativemenu-systemmenus"></a>

enum **SystemMenus**: [🔗](class_nativemenu.md#enum-nativemenu-systemmenus)

<a id="class-nativemenu-constant-invalid-menu-id"></a>

[SystemMenus](class_nativemenu.md#enum-nativemenu-systemmenus) **INVALID_MENU_ID** = `0`

Invalid special system menu ID.

<a id="class-nativemenu-constant-main-menu-id"></a>

[SystemMenus](class_nativemenu.md#enum-nativemenu-systemmenus) **MAIN_MENU_ID** = `1`

Global main menu ID.

<a id="class-nativemenu-constant-application-menu-id"></a>

[SystemMenus](class_nativemenu.md#enum-nativemenu-systemmenus) **APPLICATION_MENU_ID** = `2`

Application (first menu after "Apple" menu on macOS) menu ID.

<a id="class-nativemenu-constant-window-menu-id"></a>

[SystemMenus](class_nativemenu.md#enum-nativemenu-systemmenus) **WINDOW_MENU_ID** = `3`

"Window" menu ID (on macOS this menu includes standard window control items and a list of open windows).

<a id="class-nativemenu-constant-help-menu-id"></a>

[SystemMenus](class_nativemenu.md#enum-nativemenu-systemmenus) **HELP_MENU_ID** = `4`

"Help" menu ID (on macOS this menu includes help search bar).

<a id="class-nativemenu-constant-dock-menu-id"></a>

[SystemMenus](class_nativemenu.md#enum-nativemenu-systemmenus) **DOCK_MENU_ID** = `5`

Dock icon right-click menu ID (on macOS this menu include standard application control items and a list of open windows).

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-nativemenu-method-add-check-item"></a>

[int](class_int.md#class-int) **add_check_item**(rid: [RID](class_rid.md#class-rid), label: [String](class_string.md#class-string), callback: [Callable](class_callable.md#class-callable) = Callable(), key_callback: [Callable](class_callable.md#class-callable) = Callable(), tag: [Variant](class_variant.md#class-variant) = null, accelerator: [Key](class_@globalscope.md#enum-globalscope-key) = 0, index: [int](class_int.md#class-int) = -1) [🔗](class_nativemenu.md#class-nativemenu-method-add-check-item)

Adds a new checkable item with text `label` to the global menu `rid`.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The `accelerator` is generally a combination of [KeyModifierMask](class_@globalscope.md#enum-globalscope-keymodifiermask)s and [Key](class_@globalscope.md#enum-globalscope-key)s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (`Ctrl + A`).

**Note:** The `callback` and `key_callback` Callables need to accept exactly one Variant parameter, the parameter passed to the Callables will be the value passed to `tag`.

**Note:** This method is implemented on macOS and Windows.

**Note:** On Windows, `accelerator` and `key_callback` are ignored.

---


<a id="class-nativemenu-method-add-icon-check-item"></a>

[int](class_int.md#class-int) **add_icon_check_item**(rid: [RID](class_rid.md#class-rid), icon: [Texture2D](class_texture2d.md#class-texture2d), label: [String](class_string.md#class-string), callback: [Callable](class_callable.md#class-callable) = Callable(), key_callback: [Callable](class_callable.md#class-callable) = Callable(), tag: [Variant](class_variant.md#class-variant) = null, accelerator: [Key](class_@globalscope.md#enum-globalscope-key) = 0, index: [int](class_int.md#class-int) = -1) [🔗](class_nativemenu.md#class-nativemenu-method-add-icon-check-item)

Adds a new checkable item with text `label` and icon `icon` to the global menu `rid`.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The `accelerator` is generally a combination of [KeyModifierMask](class_@globalscope.md#enum-globalscope-keymodifiermask)s and [Key](class_@globalscope.md#enum-globalscope-key)s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (`Ctrl + A`).

**Note:** The `callback` and `key_callback` Callables need to accept exactly one Variant parameter, the parameter passed to the Callables will be the value passed to `tag`.

**Note:** This method is implemented on macOS and Windows.

**Note:** On Windows, `accelerator` and `key_callback` are ignored.

---


<a id="class-nativemenu-method-add-icon-item"></a>

[int](class_int.md#class-int) **add_icon_item**(rid: [RID](class_rid.md#class-rid), icon: [Texture2D](class_texture2d.md#class-texture2d), label: [String](class_string.md#class-string), callback: [Callable](class_callable.md#class-callable) = Callable(), key_callback: [Callable](class_callable.md#class-callable) = Callable(), tag: [Variant](class_variant.md#class-variant) = null, accelerator: [Key](class_@globalscope.md#enum-globalscope-key) = 0, index: [int](class_int.md#class-int) = -1) [🔗](class_nativemenu.md#class-nativemenu-method-add-icon-item)

Adds a new item with text `label` and icon `icon` to the global menu `rid`.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The `accelerator` is generally a combination of [KeyModifierMask](class_@globalscope.md#enum-globalscope-keymodifiermask)s and [Key](class_@globalscope.md#enum-globalscope-key)s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (`Ctrl + A`).

**Note:** The `callback` and `key_callback` Callables need to accept exactly one Variant parameter, the parameter passed to the Callables will be the value passed to `tag`.

**Note:** This method is implemented on macOS and Windows.

**Note:** On Windows, `accelerator` and `key_callback` are ignored.

---


<a id="class-nativemenu-method-add-icon-radio-check-item"></a>

[int](class_int.md#class-int) **add_icon_radio_check_item**(rid: [RID](class_rid.md#class-rid), icon: [Texture2D](class_texture2d.md#class-texture2d), label: [String](class_string.md#class-string), callback: [Callable](class_callable.md#class-callable) = Callable(), key_callback: [Callable](class_callable.md#class-callable) = Callable(), tag: [Variant](class_variant.md#class-variant) = null, accelerator: [Key](class_@globalscope.md#enum-globalscope-key) = 0, index: [int](class_int.md#class-int) = -1) [🔗](class_nativemenu.md#class-nativemenu-method-add-icon-radio-check-item)

Adds a new radio-checkable item with text `label` and icon `icon` to the global menu `rid`.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The `accelerator` is generally a combination of [KeyModifierMask](class_@globalscope.md#enum-globalscope-keymodifiermask)s and [Key](class_@globalscope.md#enum-globalscope-key)s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (`Ctrl + A`).

**Note:** Radio-checkable items just display a checkmark, but don't have any built-in checking behavior and must be checked/unchecked manually. See [set_item_checked()](class_nativemenu.md#class-nativemenu-method-set-item-checked) for more info on how to control it.

**Note:** The `callback` and `key_callback` Callables need to accept exactly one Variant parameter, the parameter passed to the Callables will be the value passed to `tag`.

**Note:** This method is implemented on macOS and Windows.

**Note:** On Windows, `accelerator` and `key_callback` are ignored.

---


<a id="class-nativemenu-method-add-item"></a>

[int](class_int.md#class-int) **add_item**(rid: [RID](class_rid.md#class-rid), label: [String](class_string.md#class-string), callback: [Callable](class_callable.md#class-callable) = Callable(), key_callback: [Callable](class_callable.md#class-callable) = Callable(), tag: [Variant](class_variant.md#class-variant) = null, accelerator: [Key](class_@globalscope.md#enum-globalscope-key) = 0, index: [int](class_int.md#class-int) = -1) [🔗](class_nativemenu.md#class-nativemenu-method-add-item)

Adds a new item with text `label` to the global menu `rid`.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The `accelerator` is generally a combination of [KeyModifierMask](class_@globalscope.md#enum-globalscope-keymodifiermask)s and [Key](class_@globalscope.md#enum-globalscope-key)s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (`Ctrl + A`).

**Note:** The `callback` and `key_callback` Callables need to accept exactly one Variant parameter, the parameter passed to the Callables will be the value passed to `tag`.

**Note:** This method is implemented on macOS and Windows.

**Note:** On Windows, `accelerator` and `key_callback` are ignored.

---


<a id="class-nativemenu-method-add-multistate-item"></a>

[int](class_int.md#class-int) **add_multistate_item**(rid: [RID](class_rid.md#class-rid), label: [String](class_string.md#class-string), max_states: [int](class_int.md#class-int), default_state: [int](class_int.md#class-int), callback: [Callable](class_callable.md#class-callable) = Callable(), key_callback: [Callable](class_callable.md#class-callable) = Callable(), tag: [Variant](class_variant.md#class-variant) = null, accelerator: [Key](class_@globalscope.md#enum-globalscope-key) = 0, index: [int](class_int.md#class-int) = -1) [🔗](class_nativemenu.md#class-nativemenu-method-add-multistate-item)

Adds a new item with text `label` to the global menu `rid`.

Contrarily to normal binary items, multistate items can have more than two states, as defined by `max_states`. Each press or activate of the item will increase the state by one. The default value is defined by `default_state`.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The `accelerator` is generally a combination of [KeyModifierMask](class_@globalscope.md#enum-globalscope-keymodifiermask)s and [Key](class_@globalscope.md#enum-globalscope-key)s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (`Ctrl + A`).

**Note:** By default, there's no indication of the current item state, it should be changed manually.

**Note:** The `callback` and `key_callback` Callables need to accept exactly one Variant parameter, the parameter passed to the Callables will be the value passed to `tag`.

**Note:** This method is implemented on macOS and Windows.

**Note:** On Windows, `accelerator` and `key_callback` are ignored.

---


<a id="class-nativemenu-method-add-radio-check-item"></a>

[int](class_int.md#class-int) **add_radio_check_item**(rid: [RID](class_rid.md#class-rid), label: [String](class_string.md#class-string), callback: [Callable](class_callable.md#class-callable) = Callable(), key_callback: [Callable](class_callable.md#class-callable) = Callable(), tag: [Variant](class_variant.md#class-variant) = null, accelerator: [Key](class_@globalscope.md#enum-globalscope-key) = 0, index: [int](class_int.md#class-int) = -1) [🔗](class_nativemenu.md#class-nativemenu-method-add-radio-check-item)

Adds a new radio-checkable item with text `label` to the global menu `rid`.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The `accelerator` is generally a combination of [KeyModifierMask](class_@globalscope.md#enum-globalscope-keymodifiermask)s and [Key](class_@globalscope.md#enum-globalscope-key)s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (`Ctrl + A`).

**Note:** Radio-checkable items just display a checkmark, but don't have any built-in checking behavior and must be checked/unchecked manually. See [set_item_checked()](class_nativemenu.md#class-nativemenu-method-set-item-checked) for more info on how to control it.

**Note:** The `callback` and `key_callback` Callables need to accept exactly one Variant parameter, the parameter passed to the Callables will be the value passed to `tag`.

**Note:** This method is implemented on macOS and Windows.

**Note:** On Windows, `accelerator` and `key_callback` are ignored.

---


<a id="class-nativemenu-method-add-separator"></a>

[int](class_int.md#class-int) **add_separator**(rid: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int) = -1) [🔗](class_nativemenu.md#class-nativemenu-method-add-separator)

Adds a separator between items to the global menu `rid`. Separators also occupy an index.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

**Note:** This method is implemented on macOS and Windows.

---


<a id="class-nativemenu-method-add-submenu-item"></a>

[int](class_int.md#class-int) **add_submenu_item**(rid: [RID](class_rid.md#class-rid), label: [String](class_string.md#class-string), submenu_rid: [RID](class_rid.md#class-rid), tag: [Variant](class_variant.md#class-variant) = null, index: [int](class_int.md#class-int) = -1) [🔗](class_nativemenu.md#class-nativemenu-method-add-submenu-item)

Adds an item that will act as a submenu of the global menu `rid`. The `submenu_rid` argument is the RID of the global menu that will be shown when the item is clicked.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

**Note:** This method is implemented on macOS and Windows.

---


<a id="class-nativemenu-method-clear"></a>

void **clear**(rid: [RID](class_rid.md#class-rid)) [🔗](class_nativemenu.md#class-nativemenu-method-clear)

Removes all items from the global menu `rid`.

**Note:** This method is implemented on macOS and Windows.

---


<a id="class-nativemenu-method-create-menu"></a>

[RID](class_rid.md#class-rid) **create_menu**() [🔗](class_nativemenu.md#class-nativemenu-method-create-menu)

Creates a new global menu object.

**Note:** This method is implemented on macOS and Windows.

---


<a id="class-nativemenu-method-find-item-index-with-submenu"></a>

[int](class_int.md#class-int) **find_item_index_with_submenu**(rid: [RID](class_rid.md#class-rid), submenu_rid: [RID](class_rid.md#class-rid)) const [🔗](class_nativemenu.md#class-nativemenu-method-find-item-index-with-submenu)

Returns the index of the item with the submenu specified by `submenu_rid`. Indices are automatically assigned to each item by the engine.

**Note:** This method is implemented on macOS and Windows.

---


<a id="class-nativemenu-method-find-item-index-with-tag"></a>

[int](class_int.md#class-int) **find_item_index_with_tag**(rid: [RID](class_rid.md#class-rid), tag: [Variant](class_variant.md#class-variant)) const [🔗](class_nativemenu.md#class-nativemenu-method-find-item-index-with-tag)

Returns the index of the item with the specified `tag`. Indices are automatically assigned to each item by the engine.

**Note:** This method is implemented on macOS and Windows.

---


<a id="class-nativemenu-method-find-item-index-with-text"></a>

[int](class_int.md#class-int) **find_item_index_with_text**(rid: [RID](class_rid.md#class-rid), text: [String](class_string.md#class-string)) const [🔗](class_nativemenu.md#class-nativemenu-method-find-item-index-with-text)

Returns the index of the item with the specified `text`. Indices are automatically assigned to each item by the engine.

**Note:** This method is implemented on macOS and Windows.

---


<a id="class-nativemenu-method-free-menu"></a>

void **free_menu**(rid: [RID](class_rid.md#class-rid)) [🔗](class_nativemenu.md#class-nativemenu-method-free-menu)

Frees a global menu object created by this **NativeMenu**.

**Note:** This method is implemented on macOS and Windows.

---


<a id="class-nativemenu-method-get-item-accelerator"></a>

[Key](class_@globalscope.md#enum-globalscope-key) **get_item_accelerator**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int)) const [🔗](class_nativemenu.md#class-nativemenu-method-get-item-accelerator)

Returns the accelerator of the item at index `idx`. Accelerators are special combinations of keys that activate the item, no matter which control is focused.

**Note:** This method is implemented only on macOS.

---


<a id="class-nativemenu-method-get-item-callback"></a>

[Callable](class_callable.md#class-callable) **get_item_callback**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int)) const [🔗](class_nativemenu.md#class-nativemenu-method-get-item-callback)

Returns the callback of the item at index `idx`.

**Note:** This method is implemented on macOS and Windows.

---


<a id="class-nativemenu-method-get-item-count"></a>

[int](class_int.md#class-int) **get_item_count**(rid: [RID](class_rid.md#class-rid)) const [🔗](class_nativemenu.md#class-nativemenu-method-get-item-count)

Returns number of items in the global menu `rid`.

**Note:** This method is implemented on macOS and Windows.

---


<a id="class-nativemenu-method-get-item-icon"></a>

[Texture2D](class_texture2d.md#class-texture2d) **get_item_icon**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int)) const [🔗](class_nativemenu.md#class-nativemenu-method-get-item-icon)

Returns the icon of the item at index `idx`.

**Note:** This method is implemented on macOS and Windows.

---


<a id="class-nativemenu-method-get-item-indentation-level"></a>

[int](class_int.md#class-int) **get_item_indentation_level**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int)) const [🔗](class_nativemenu.md#class-nativemenu-method-get-item-indentation-level)

Returns the horizontal offset of the item at the given `idx`.

**Note:** This method is implemented only on macOS.

---


<a id="class-nativemenu-method-get-item-key-callback"></a>

[Callable](class_callable.md#class-callable) **get_item_key_callback**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int)) const [🔗](class_nativemenu.md#class-nativemenu-method-get-item-key-callback)

Returns the callback of the item accelerator at index `idx`.

**Note:** This method is implemented only on macOS.

---


<a id="class-nativemenu-method-get-item-max-states"></a>

[int](class_int.md#class-int) **get_item_max_states**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int)) const [🔗](class_nativemenu.md#class-nativemenu-method-get-item-max-states)

Returns number of states of a multistate item. See [add_multistate_item()](class_nativemenu.md#class-nativemenu-method-add-multistate-item) for details.

**Note:** This method is implemented on macOS and Windows.

---


<a id="class-nativemenu-method-get-item-state"></a>

[int](class_int.md#class-int) **get_item_state**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int)) const [🔗](class_nativemenu.md#class-nativemenu-method-get-item-state)

Returns the state of a multistate item. See [add_multistate_item()](class_nativemenu.md#class-nativemenu-method-add-multistate-item) for details.

**Note:** This method is implemented on macOS and Windows.

---


<a id="class-nativemenu-method-get-item-submenu"></a>

[RID](class_rid.md#class-rid) **get_item_submenu**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int)) const [🔗](class_nativemenu.md#class-nativemenu-method-get-item-submenu)

Returns the submenu ID of the item at index `idx`. See [add_submenu_item()](class_nativemenu.md#class-nativemenu-method-add-submenu-item) for more info on how to add a submenu.

**Note:** This method is implemented on macOS and Windows.

---


<a id="class-nativemenu-method-get-item-tag"></a>

[Variant](class_variant.md#class-variant) **get_item_tag**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int)) const [🔗](class_nativemenu.md#class-nativemenu-method-get-item-tag)

Returns the metadata of the specified item, which might be of any type. You can set it with [set_item_tag()](class_nativemenu.md#class-nativemenu-method-set-item-tag), which provides a simple way of assigning context data to items.

**Note:** This method is implemented on macOS and Windows.

---


<a id="class-nativemenu-method-get-item-text"></a>

[String](class_string.md#class-string) **get_item_text**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int)) const [🔗](class_nativemenu.md#class-nativemenu-method-get-item-text)

Returns the text of the item at index `idx`.

**Note:** This method is implemented on macOS and Windows.

---


<a id="class-nativemenu-method-get-item-tooltip"></a>

[String](class_string.md#class-string) **get_item_tooltip**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int)) const [🔗](class_nativemenu.md#class-nativemenu-method-get-item-tooltip)

Returns the tooltip associated with the specified index `idx`.

**Note:** This method is implemented only on macOS.

---


<a id="class-nativemenu-method-get-minimum-width"></a>

[float](class_float.md#class-float) **get_minimum_width**(rid: [RID](class_rid.md#class-rid)) const [🔗](class_nativemenu.md#class-nativemenu-method-get-minimum-width)

Returns global menu minimum width.

**Note:** This method is implemented only on macOS.

---


<a id="class-nativemenu-method-get-popup-close-callback"></a>

[Callable](class_callable.md#class-callable) **get_popup_close_callback**(rid: [RID](class_rid.md#class-rid)) const [🔗](class_nativemenu.md#class-nativemenu-method-get-popup-close-callback)

Returns global menu close callback.

**Note:** This method is implemented on macOS and Windows.

---


<a id="class-nativemenu-method-get-popup-open-callback"></a>

[Callable](class_callable.md#class-callable) **get_popup_open_callback**(rid: [RID](class_rid.md#class-rid)) const [🔗](class_nativemenu.md#class-nativemenu-method-get-popup-open-callback)

Returns global menu open callback.

**Note:** This method is implemented only on macOS.

---


<a id="class-nativemenu-method-get-size"></a>

[Vector2](class_vector2.md#class-vector2) **get_size**(rid: [RID](class_rid.md#class-rid)) const [🔗](class_nativemenu.md#class-nativemenu-method-get-size)

Returns global menu size.

**Note:** This method is implemented on macOS and Windows.

---


<a id="class-nativemenu-method-get-system-menu"></a>

[RID](class_rid.md#class-rid) **get_system_menu**(menu_id: [SystemMenus](class_nativemenu.md#enum-nativemenu-systemmenus)) const [🔗](class_nativemenu.md#class-nativemenu-method-get-system-menu)

Returns RID of a special system menu.

**Note:** This method is implemented only on macOS.

---


<a id="class-nativemenu-method-get-system-menu-name"></a>

[String](class_string.md#class-string) **get_system_menu_name**(menu_id: [SystemMenus](class_nativemenu.md#enum-nativemenu-systemmenus)) const [🔗](class_nativemenu.md#class-nativemenu-method-get-system-menu-name)

Returns readable name of a special system menu.

**Note:** This method is implemented only on macOS.

---


<a id="class-nativemenu-method-get-system-menu-text"></a>

[String](class_string.md#class-string) **get_system_menu_text**(menu_id: [SystemMenus](class_nativemenu.md#enum-nativemenu-systemmenus)) const [🔗](class_nativemenu.md#class-nativemenu-method-get-system-menu-text)

Returns the text of the system menu item.

**Note:** This method is implemented on macOS.

---


<a id="class-nativemenu-method-has-feature"></a>

[bool](class_bool.md#class-bool) **has_feature**(feature: [Feature](class_nativemenu.md#enum-nativemenu-feature)) const [🔗](class_nativemenu.md#class-nativemenu-method-has-feature)

Returns `true` if the specified `feature` is supported by the current **NativeMenu**, `false` otherwise.

**Note:** This method is implemented on macOS and Windows.

---


<a id="class-nativemenu-method-has-menu"></a>

[bool](class_bool.md#class-bool) **has_menu**(rid: [RID](class_rid.md#class-rid)) const [🔗](class_nativemenu.md#class-nativemenu-method-has-menu)

Returns `true` if `rid` is valid global menu.

**Note:** This method is implemented on macOS and Windows.

---


<a id="class-nativemenu-method-has-system-menu"></a>

[bool](class_bool.md#class-bool) **has_system_menu**(menu_id: [SystemMenus](class_nativemenu.md#enum-nativemenu-systemmenus)) const [🔗](class_nativemenu.md#class-nativemenu-method-has-system-menu)

Returns `true` if a special system menu is supported.

**Note:** This method is implemented only on macOS.

---


<a id="class-nativemenu-method-is-item-checkable"></a>

[bool](class_bool.md#class-bool) **is_item_checkable**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int)) const [🔗](class_nativemenu.md#class-nativemenu-method-is-item-checkable)

Returns `true` if the item at index `idx` is checkable in some way, i.e. if it has a checkbox or radio button.

**Note:** This method is implemented on macOS and Windows.

---


<a id="class-nativemenu-method-is-item-checked"></a>

[bool](class_bool.md#class-bool) **is_item_checked**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int)) const [🔗](class_nativemenu.md#class-nativemenu-method-is-item-checked)

Returns `true` if the item at index `idx` is checked.

**Note:** This method is implemented on macOS and Windows.

---


<a id="class-nativemenu-method-is-item-disabled"></a>

[bool](class_bool.md#class-bool) **is_item_disabled**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int)) const [🔗](class_nativemenu.md#class-nativemenu-method-is-item-disabled)

Returns `true` if the item at index `idx` is disabled. When it is disabled it can't be selected, or its action invoked.

See [set_item_disabled()](class_nativemenu.md#class-nativemenu-method-set-item-disabled) for more info on how to disable an item.

**Note:** This method is implemented on macOS and Windows.

---


<a id="class-nativemenu-method-is-item-hidden"></a>

[bool](class_bool.md#class-bool) **is_item_hidden**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int)) const [🔗](class_nativemenu.md#class-nativemenu-method-is-item-hidden)

Returns `true` if the item at index `idx` is hidden.

See [set_item_hidden()](class_nativemenu.md#class-nativemenu-method-set-item-hidden) for more info on how to hide an item.

**Note:** This method is implemented only on macOS.

---


<a id="class-nativemenu-method-is-item-radio-checkable"></a>

[bool](class_bool.md#class-bool) **is_item_radio_checkable**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int)) const [🔗](class_nativemenu.md#class-nativemenu-method-is-item-radio-checkable)

Returns `true` if the item at index `idx` has radio button-style checkability.

**Note:** This is purely cosmetic; you must add the logic for checking/unchecking items in radio groups.

**Note:** This method is implemented on macOS and Windows.

---


<a id="class-nativemenu-method-is-opened"></a>

[bool](class_bool.md#class-bool) **is_opened**(rid: [RID](class_rid.md#class-rid)) const [🔗](class_nativemenu.md#class-nativemenu-method-is-opened)

Returns `true` if the menu is currently opened.

**Note:** This method is implemented only on macOS.

---


<a id="class-nativemenu-method-is-system-menu"></a>

[bool](class_bool.md#class-bool) **is_system_menu**(rid: [RID](class_rid.md#class-rid)) const [🔗](class_nativemenu.md#class-nativemenu-method-is-system-menu)

Return `true` is global menu is a special system menu.

**Note:** This method is implemented only on macOS.

---


<a id="class-nativemenu-method-popup"></a>

void **popup**(rid: [RID](class_rid.md#class-rid), position: [Vector2i](class_vector2i.md#class-vector2i)) [🔗](class_nativemenu.md#class-nativemenu-method-popup)

Shows the global menu at `position` in the screen coordinates.

**Note:** This method is implemented on macOS and Windows.

---


<a id="class-nativemenu-method-remove-item"></a>

void **remove_item**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int)) [🔗](class_nativemenu.md#class-nativemenu-method-remove-item)

Removes the item at index `idx` from the global menu `rid`.

**Note:** The indices of items after the removed item will be shifted by one.

**Note:** This method is implemented on macOS and Windows.

---


<a id="class-nativemenu-method-set-interface-direction"></a>

void **set_interface_direction**(rid: [RID](class_rid.md#class-rid), is_rtl: [bool](class_bool.md#class-bool)) [🔗](class_nativemenu.md#class-nativemenu-method-set-interface-direction)

Sets the menu text layout direction from right-to-left if `is_rtl` is `true`.

**Note:** This method is implemented on macOS and Windows.

---


<a id="class-nativemenu-method-set-item-accelerator"></a>

void **set_item_accelerator**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), keycode: [Key](class_@globalscope.md#enum-globalscope-key)) [🔗](class_nativemenu.md#class-nativemenu-method-set-item-accelerator)

Sets the accelerator of the item at index `idx`. `keycode` can be a single [Key](class_@globalscope.md#enum-globalscope-key), or a combination of [KeyModifierMask](class_@globalscope.md#enum-globalscope-keymodifiermask)s and [Key](class_@globalscope.md#enum-globalscope-key)s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (`Ctrl + A`).

**Note:** This method is implemented only on macOS.

---


<a id="class-nativemenu-method-set-item-callback"></a>

void **set_item_callback**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), callback: [Callable](class_callable.md#class-callable)) [🔗](class_nativemenu.md#class-nativemenu-method-set-item-callback)

Sets the callback of the item at index `idx`. Callback is emitted when an item is pressed.

**Note:** The `callback` Callable needs to accept exactly one Variant parameter, the parameter passed to the Callable will be the value passed to the `tag` parameter when the menu item was created.

**Note:** This method is implemented on macOS and Windows.

---


<a id="class-nativemenu-method-set-item-checkable"></a>

void **set_item_checkable**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), checkable: [bool](class_bool.md#class-bool)) [🔗](class_nativemenu.md#class-nativemenu-method-set-item-checkable)

Sets whether the item at index `idx` has a checkbox. If `false`, sets the type of the item to plain text.

**Note:** This method is implemented on macOS and Windows.

---


<a id="class-nativemenu-method-set-item-checked"></a>

void **set_item_checked**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), checked: [bool](class_bool.md#class-bool)) [🔗](class_nativemenu.md#class-nativemenu-method-set-item-checked)

Sets the checkstate status of the item at index `idx`.

**Note:** This method is implemented on macOS and Windows.

---


<a id="class-nativemenu-method-set-item-disabled"></a>

void **set_item_disabled**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool)) [🔗](class_nativemenu.md#class-nativemenu-method-set-item-disabled)

Enables/disables the item at index `idx`. When it is disabled, it can't be selected and its action can't be invoked.

**Note:** This method is implemented on macOS and Windows.

---


<a id="class-nativemenu-method-set-item-hidden"></a>

void **set_item_hidden**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), hidden: [bool](class_bool.md#class-bool)) [🔗](class_nativemenu.md#class-nativemenu-method-set-item-hidden)

Hides/shows the item at index `idx`. When it is hidden, an item does not appear in a menu and its action cannot be invoked.

**Note:** This method is implemented only on macOS.

---


<a id="class-nativemenu-method-set-item-hover-callbacks"></a>

void **set_item_hover_callbacks**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), callback: [Callable](class_callable.md#class-callable)) [🔗](class_nativemenu.md#class-nativemenu-method-set-item-hover-callbacks)

Sets the callback of the item at index `idx`. The callback is emitted when an item is hovered.

**Note:** The `callback` Callable needs to accept exactly one Variant parameter, the parameter passed to the Callable will be the value passed to the `tag` parameter when the menu item was created.

**Note:** This method is implemented only on macOS.

---


<a id="class-nativemenu-method-set-item-icon"></a>

void **set_item_icon**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), icon: [Texture2D](class_texture2d.md#class-texture2d)) [🔗](class_nativemenu.md#class-nativemenu-method-set-item-icon)

Replaces the [Texture2D](class_texture2d.md#class-texture2d) icon of the specified `idx`.

**Note:** This method is implemented on macOS and Windows.

**Note:** This method is not supported by macOS Dock menu items.

---


<a id="class-nativemenu-method-set-item-indentation-level"></a>

void **set_item_indentation_level**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), level: [int](class_int.md#class-int)) [🔗](class_nativemenu.md#class-nativemenu-method-set-item-indentation-level)

Sets the horizontal offset of the item at the given `idx`.

**Note:** This method is implemented only on macOS.

---


<a id="class-nativemenu-method-set-item-index"></a>

[int](class_int.md#class-int) **set_item_index**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), target_idx: [int](class_int.md#class-int)) [🔗](class_nativemenu.md#class-nativemenu-method-set-item-index)

Changes the index of the item at index `idx` to be at index `target_idx`. This can be used to move an item above other items.

Returns the new index of the moved item, it's not guaranteed to be the same as `target_idx`.

**Note:** The indices of any items between index `idx` and index `target_idx` will be shifted by one.

**Note:** This method is implemented on macOS and Windows.

---


<a id="class-nativemenu-method-set-item-key-callback"></a>

void **set_item_key_callback**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), key_callback: [Callable](class_callable.md#class-callable)) [🔗](class_nativemenu.md#class-nativemenu-method-set-item-key-callback)

Sets the callback of the item at index `idx`. Callback is emitted when its accelerator is activated.

**Note:** The `key_callback` Callable needs to accept exactly one Variant parameter, the parameter passed to the Callable will be the value passed to the `tag` parameter when the menu item was created.

**Note:** This method is implemented only on macOS.

---


<a id="class-nativemenu-method-set-item-max-states"></a>

void **set_item_max_states**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), max_states: [int](class_int.md#class-int)) [🔗](class_nativemenu.md#class-nativemenu-method-set-item-max-states)

Sets number of state of a multistate item. See [add_multistate_item()](class_nativemenu.md#class-nativemenu-method-add-multistate-item) for details.

**Note:** This method is implemented on macOS and Windows.

---


<a id="class-nativemenu-method-set-item-radio-checkable"></a>

void **set_item_radio_checkable**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), checkable: [bool](class_bool.md#class-bool)) [🔗](class_nativemenu.md#class-nativemenu-method-set-item-radio-checkable)

Sets the type of the item at the specified index `idx` to radio button. If `false`, sets the type of the item to plain text.

**Note:** This is purely cosmetic; you must add the logic for checking/unchecking items in radio groups.

**Note:** This method is implemented on macOS and Windows.

---


<a id="class-nativemenu-method-set-item-state"></a>

void **set_item_state**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), state: [int](class_int.md#class-int)) [🔗](class_nativemenu.md#class-nativemenu-method-set-item-state)

Sets the state of a multistate item. See [add_multistate_item()](class_nativemenu.md#class-nativemenu-method-add-multistate-item) for details.

**Note:** This method is implemented on macOS and Windows.

---


<a id="class-nativemenu-method-set-item-submenu"></a>

void **set_item_submenu**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), submenu_rid: [RID](class_rid.md#class-rid)) [🔗](class_nativemenu.md#class-nativemenu-method-set-item-submenu)

Sets the submenu RID of the item at index `idx`. The submenu is a global menu that would be shown when the item is clicked.

**Note:** This method is implemented on macOS and Windows.

---


<a id="class-nativemenu-method-set-item-tag"></a>

void **set_item_tag**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), tag: [Variant](class_variant.md#class-variant)) [🔗](class_nativemenu.md#class-nativemenu-method-set-item-tag)

Sets the metadata of an item, which may be of any type. You can later get it with [get_item_tag()](class_nativemenu.md#class-nativemenu-method-get-item-tag), which provides a simple way of assigning context data to items.

**Note:** This method is implemented on macOS and Windows.

---


<a id="class-nativemenu-method-set-item-text"></a>

void **set_item_text**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), text: [String](class_string.md#class-string)) [🔗](class_nativemenu.md#class-nativemenu-method-set-item-text)

Sets the text of the item at index `idx`.

**Note:** This method is implemented on macOS and Windows.

---


<a id="class-nativemenu-method-set-item-tooltip"></a>

void **set_item_tooltip**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), tooltip: [String](class_string.md#class-string)) [🔗](class_nativemenu.md#class-nativemenu-method-set-item-tooltip)

Sets the [String](class_string.md#class-string) tooltip of the item at the specified index `idx`.

**Note:** This method is implemented only on macOS.

---


<a id="class-nativemenu-method-set-minimum-width"></a>

void **set_minimum_width**(rid: [RID](class_rid.md#class-rid), width: [float](class_float.md#class-float)) [🔗](class_nativemenu.md#class-nativemenu-method-set-minimum-width)

Sets the minimum width of the global menu.

**Note:** This method is implemented only on macOS.

---


<a id="class-nativemenu-method-set-popup-close-callback"></a>

void **set_popup_close_callback**(rid: [RID](class_rid.md#class-rid), callback: [Callable](class_callable.md#class-callable)) [🔗](class_nativemenu.md#class-nativemenu-method-set-popup-close-callback)

Registers callable to emit when the menu is about to show.

**Note:** The OS can simulate menu opening to track menu item changes and global shortcuts, in which case the corresponding close callback is not triggered. Use [is_opened()](class_nativemenu.md#class-nativemenu-method-is-opened) to check if the menu is currently opened.

**Note:** This method is implemented on macOS and Windows.

---


<a id="class-nativemenu-method-set-popup-open-callback"></a>

void **set_popup_open_callback**(rid: [RID](class_rid.md#class-rid), callback: [Callable](class_callable.md#class-callable)) [🔗](class_nativemenu.md#class-nativemenu-method-set-popup-open-callback)

Registers callable to emit after the menu is closed.

**Note:** This method is implemented only on macOS.

---


<a id="class-nativemenu-method-set-system-menu-text"></a>

void **set_system_menu_text**(menu_id: [SystemMenus](class_nativemenu.md#enum-nativemenu-systemmenus), name: [String](class_string.md#class-string)) [🔗](class_nativemenu.md#class-nativemenu-method-set-system-menu-text)

Sets the text of the system menu item.

**Note:** This method is implemented on macOS.
