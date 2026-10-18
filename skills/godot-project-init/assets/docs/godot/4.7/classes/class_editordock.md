> Source: https://docs.godotengine.org/en/4.7/classes/class_editordock.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="editordock"></a>

<a id="class-editordock"></a>

# EditorDock

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [MarginContainer](class_margincontainer.md#class-margincontainer) **<** [Container](class_container.md#class-container) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [FileSystemDock](class_filesystemdock.md#class-filesystemdock)

Dockable container for the editor.

<a id="description"></a>

## Description

EditorDock is a [Container](class_container.md#class-container) node that can be docked in one of the editor's dock slots. Docks are added by plugins to provide space for controls related to an [EditorPlugin](class_editorplugin.md#class-editorplugin). The editor comes with a few built-in docks, such as the Scene dock, FileSystem dock, etc.

You can add a dock by using [EditorPlugin.add_dock()](class_editorplugin.md#class-editorplugin-method-add-dock). The dock can be customized by changing its properties.

```gdscript
@tool
extends EditorPlugin

# Dock reference.
var dock

# Plugin initialization.
func _enter_tree():
    dock = EditorDock.new()
    dock.title = "My Dock"
    dock.dock_icon = preload("./dock_icon.png")
    dock.default_slot = EditorDock.DOCK_SLOT_RIGHT_UL
    var dock_content = preload("./dock_content.tscn").instantiate()
    dock.add_child(dock_content)
    add_dock(dock)

# Plugin clean-up.
func _exit_tree():
    remove_dock(dock)
    dock.queue_free()
    dock = null
```

<a id="tutorials"></a>

## Tutorials

- [Making plugins](../tutorials/plugins/editor/making_plugins.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | accessibility_region | `true` (overrides [Container](class_container.md#class-container-property-accessibility-region)) |
| BitField[[DockLayout](class_editordock.md#enum-editordock-docklayout)] | [available_layouts](class_editordock.md#class-editordock-property-available-layouts) | `5` |
| [bool](class_bool.md#class-bool) | [closable](class_editordock.md#class-editordock-property-closable) | `false` |
| [DockSlot](class_editordock.md#enum-editordock-dockslot) | [default_slot](class_editordock.md#class-editordock-property-default-slot) | `-1` |
| [Texture2D](class_texture2d.md#class-texture2d) | [dock_icon](class_editordock.md#class-editordock-property-dock-icon) |  |
| [Shortcut](class_shortcut.md#class-shortcut) | [dock_shortcut](class_editordock.md#class-editordock-property-dock-shortcut) |  |
| [bool](class_bool.md#class-bool) | [force_show_icon](class_editordock.md#class-editordock-property-force-show-icon) | `false` |
| [bool](class_bool.md#class-bool) | [global](class_editordock.md#class-editordock-property-global) | `true` |
| [StringName](class_stringname.md#class-stringname) | [icon_name](class_editordock.md#class-editordock-property-icon-name) | `&""` |
| [String](class_string.md#class-string) | [layout_key](class_editordock.md#class-editordock-property-layout-key) | `""` |
| [String](class_string.md#class-string) | [title](class_editordock.md#class-editordock-property-title) | `""` |
| [Color](class_color.md#class-color) | [title_color](class_editordock.md#class-editordock-property-title-color) | `Color(0, 0, 0, 0)` |
| [bool](class_bool.md#class-bool) | [transient](class_editordock.md#class-editordock-property-transient) | `false` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [_load_layout_from_config](class_editordock.md#class-editordock-private-method-load-layout-from-config)(config: [ConfigFile](class_configfile.md#class-configfile), section: [String](class_string.md#class-string)) virtual |
| void | [_save_layout_to_config](class_editordock.md#class-editordock-private-method-save-layout-to-config)(config: [ConfigFile](class_configfile.md#class-configfile), section: [String](class_string.md#class-string)) virtual const |
| void | [_update_layout](class_editordock.md#class-editordock-private-method-update-layout)(layout: [int](class_int.md#class-int)) virtual |
| void | [close](class_editordock.md#class-editordock-method-close)() |
| void | [make_visible](class_editordock.md#class-editordock-method-make-visible)() |
| void | [open](class_editordock.md#class-editordock-method-open)() |

---


<a id="signals"></a>

## Signals

<a id="class-editordock-signal-closed"></a>

**closed**() [🔗](class_editordock.md#class-editordock-signal-closed)

Emitted when the dock is closed with the Close button in the context popup, before it's removed from its parent. See [closable](class_editordock.md#class-editordock-property-closable).

---


<a id="class-editordock-signal-opened"></a>

**opened**() [🔗](class_editordock.md#class-editordock-signal-opened)

Emitted when the dock is opened via the Editor > Editor Docks menu, before it's made visible.

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-editordock-docklayout"></a>

flags **DockLayout**: [🔗](class_editordock.md#enum-editordock-docklayout)

<a id="class-editordock-constant-dock-layout-vertical"></a>

[DockLayout](class_editordock.md#enum-editordock-docklayout) **DOCK_LAYOUT_VERTICAL** = `1`

Allows placing the dock in the vertical dock slots on either side of the editor.

<a id="class-editordock-constant-dock-layout-horizontal"></a>

[DockLayout](class_editordock.md#enum-editordock-docklayout) **DOCK_LAYOUT_HORIZONTAL** = `2`

Allows placing the dock in the horizontal dock slots at the bottom.

<a id="class-editordock-constant-dock-layout-floating"></a>

[DockLayout](class_editordock.md#enum-editordock-docklayout) **DOCK_LAYOUT_FLOATING** = `4`

Allows making the dock floating (opened as a separate window).

<a id="class-editordock-constant-dock-layout-all"></a>

[DockLayout](class_editordock.md#enum-editordock-docklayout) **DOCK_LAYOUT_ALL** = `7`

Allows placing the dock in all available slots.

---


<a id="enum-editordock-dockslot"></a>

enum **DockSlot**: [🔗](class_editordock.md#enum-editordock-dockslot)

<a id="class-editordock-constant-dock-slot-none"></a>

[DockSlot](class_editordock.md#enum-editordock-dockslot) **DOCK_SLOT_NONE** = `-1`

The dock is closed.

<a id="class-editordock-constant-dock-slot-left-ul"></a>

[DockSlot](class_editordock.md#enum-editordock-dockslot) **DOCK_SLOT_LEFT_UL** = `0`

Dock slot, left side, upper-left (empty in default layout).

<a id="class-editordock-constant-dock-slot-left-bl"></a>

[DockSlot](class_editordock.md#enum-editordock-dockslot) **DOCK_SLOT_LEFT_BL** = `1`

Dock slot, left side, bottom-left (empty in default layout).

<a id="class-editordock-constant-dock-slot-left-ur"></a>

[DockSlot](class_editordock.md#enum-editordock-dockslot) **DOCK_SLOT_LEFT_UR** = `2`

Dock slot, left side, upper-right (in default layout includes Scene and Import docks).

<a id="class-editordock-constant-dock-slot-left-br"></a>

[DockSlot](class_editordock.md#enum-editordock-dockslot) **DOCK_SLOT_LEFT_BR** = `3`

Dock slot, left side, bottom-right (in default layout includes FileSystem and History docks).

<a id="class-editordock-constant-dock-slot-right-ul"></a>

[DockSlot](class_editordock.md#enum-editordock-dockslot) **DOCK_SLOT_RIGHT_UL** = `4`

Dock slot, right side, upper-left (in default layout includes Inspector, Signal, and Group docks).

<a id="class-editordock-constant-dock-slot-right-bl"></a>

[DockSlot](class_editordock.md#enum-editordock-dockslot) **DOCK_SLOT_RIGHT_BL** = `5`

Dock slot, right side, bottom-left (empty in default layout).

<a id="class-editordock-constant-dock-slot-right-ur"></a>

[DockSlot](class_editordock.md#enum-editordock-dockslot) **DOCK_SLOT_RIGHT_UR** = `6`

Dock slot, right side, upper-right (empty in default layout).

<a id="class-editordock-constant-dock-slot-right-br"></a>

[DockSlot](class_editordock.md#enum-editordock-dockslot) **DOCK_SLOT_RIGHT_BR** = `7`

Dock slot, right side, bottom-right (empty in default layout).

<a id="class-editordock-constant-dock-slot-bottom"></a>

[DockSlot](class_editordock.md#enum-editordock-dockslot) **DOCK_SLOT_BOTTOM** = `8`

Bottom panel.

<a id="class-editordock-constant-dock-slot-bottom-l"></a>

[DockSlot](class_editordock.md#enum-editordock-dockslot) **DOCK_SLOT_BOTTOM_L** = `9`

Dock slot at the bottom, below bottom panel, on the left side.

<a id="class-editordock-constant-dock-slot-bottom-r"></a>

[DockSlot](class_editordock.md#enum-editordock-dockslot) **DOCK_SLOT_BOTTOM_R** = `10`

Dock slot at the bottom, below bottom panel, on the right side.

<a id="class-editordock-constant-dock-slot-max"></a>

[DockSlot](class_editordock.md#enum-editordock-dockslot) **DOCK_SLOT_MAX** = `11`

Represents the size of the [DockSlot](class_editordock.md#enum-editordock-dockslot) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-editordock-property-available-layouts"></a>

BitField[[DockLayout](class_editordock.md#enum-editordock-docklayout)] **available_layouts** = `5` [🔗](class_editordock.md#class-editordock-property-available-layouts)

- void **set_available_layouts**(value: BitField[[DockLayout](class_editordock.md#enum-editordock-docklayout)])
- BitField[[DockLayout](class_editordock.md#enum-editordock-docklayout)] **get_available_layouts**()

The available layouts for this dock, as a bitmask. By default, the dock allows vertical and floating layouts.

---


<a id="class-editordock-property-closable"></a>

[bool](class_bool.md#class-bool) **closable** = `false` [🔗](class_editordock.md#class-editordock-property-closable)

- void **set_closable**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_closable**()

If `true`, the dock can be closed with the Close button in the context popup. Docks with [global](class_editordock.md#class-editordock-property-global) enabled are always closable.

---


<a id="class-editordock-property-default-slot"></a>

[DockSlot](class_editordock.md#enum-editordock-dockslot) **default_slot** = `-1` [🔗](class_editordock.md#class-editordock-property-default-slot)

- void **set_default_slot**(value: [DockSlot](class_editordock.md#enum-editordock-dockslot))
- [DockSlot](class_editordock.md#enum-editordock-dockslot) **get_default_slot**()

The default dock slot used when adding the dock with [EditorPlugin.add_dock()](class_editorplugin.md#class-editorplugin-method-add-dock).

After the dock is added, it can be moved to a different slot and the editor will automatically remember its position between sessions. If you remove and re-add the dock, it will be reset to default.

---


<a id="class-editordock-property-dock-icon"></a>

[Texture2D](class_texture2d.md#class-texture2d) **dock_icon** [🔗](class_editordock.md#class-editordock-property-dock-icon)

- void **set_dock_icon**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_dock_icon**()

The icon for the dock, as a texture. If specified, it will override [icon_name](class_editordock.md#class-editordock-property-icon-name).

---


<a id="class-editordock-property-dock-shortcut"></a>

[Shortcut](class_shortcut.md#class-shortcut) **dock_shortcut** [🔗](class_editordock.md#class-editordock-property-dock-shortcut)

- void **set_dock_shortcut**(value: [Shortcut](class_shortcut.md#class-shortcut))
- [Shortcut](class_shortcut.md#class-shortcut) **get_dock_shortcut**()

The shortcut used to open the dock.

---


<a id="class-editordock-property-force-show-icon"></a>

[bool](class_bool.md#class-bool) **force_show_icon** = `false` [🔗](class_editordock.md#class-editordock-property-force-show-icon)

- void **set_force_show_icon**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_force_show_icon**()

If `true`, the dock will always display an icon, regardless of [EditorSettings.interface/editor/docks/dock_tab_style](class_editorsettings.md#class-editorsettings-property-interface-editor-docks-dock-tab-style) or [EditorSettings.interface/editor/docks/bottom_dock_tab_style](class_editorsettings.md#class-editorsettings-property-interface-editor-docks-bottom-dock-tab-style).

---


<a id="class-editordock-property-global"></a>

[bool](class_bool.md#class-bool) **global** = `true` [🔗](class_editordock.md#class-editordock-property-global)

- void **set_global**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_global**()

If `true`, the dock appears in the **Editor > Editor Docks** menu and can be closed. Non-global docks can still be closed using [close()](class_editordock.md#class-editordock-method-close) or when [closable](class_editordock.md#class-editordock-property-closable) is `true`.

---


<a id="class-editordock-property-icon-name"></a>

[StringName](class_stringname.md#class-stringname) **icon_name** = `&""` [🔗](class_editordock.md#class-editordock-property-icon-name)

- void **set_icon_name**(value: [StringName](class_stringname.md#class-stringname))
- [StringName](class_stringname.md#class-stringname) **get_icon_name**()

The icon for the dock, as a name from the `EditorIcons` theme type in the editor theme. You can find the list of available icons [here](https://godot-editor-icons.github.io/).

---


<a id="class-editordock-property-layout-key"></a>

[String](class_string.md#class-string) **layout_key** = `""` [🔗](class_editordock.md#class-editordock-property-layout-key)

- void **set_layout_key**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_layout_key**()

The key representing this dock in the editor's layout file. If empty, the dock's displayed name will be used instead.

---


<a id="class-editordock-property-title"></a>

[String](class_string.md#class-string) **title** = `""` [🔗](class_editordock.md#class-editordock-property-title)

- void **set_title**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_title**()

The title of the dock's tab. If empty, the dock's [Node.name](class_node.md#class-node-property-name) will be used. If the name is auto-generated (contains `@`), the first child's name will be used instead.

---


<a id="class-editordock-property-title-color"></a>

[Color](class_color.md#class-color) **title_color** = `Color(0, 0, 0, 0)` [🔗](class_editordock.md#class-editordock-property-title-color)

- void **set_title_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_title_color**()

The color of the dock tab's title. If its alpha is `0.0`, the default font color will be used.

---


<a id="class-editordock-property-transient"></a>

[bool](class_bool.md#class-bool) **transient** = `false` [🔗](class_editordock.md#class-editordock-property-transient)

- void **set_transient**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_transient**()

If `true`, the dock is not automatically opened or closed when loading an editor layout, only moved. It also can't be opened using a shortcut. This is meant for docks that are opened and closed in specific cases, such as when selecting a [TileMap](class_tilemap.md#class-tilemap) or [AnimationTree](class_animationtree.md#class-animationtree) node.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-editordock-private-method-load-layout-from-config"></a>

void **_load_layout_from_config**(config: [ConfigFile](class_configfile.md#class-configfile), section: [String](class_string.md#class-string)) virtual [🔗](class_editordock.md#class-editordock-private-method-load-layout-from-config)

Implement this method to handle loading this dock's layout. It's equivalent to [EditorPlugin._set_window_layout()](class_editorplugin.md#class-editorplugin-private-method-set-window-layout). `section` is a unique section based on [layout_key](class_editordock.md#class-editordock-property-layout-key).

---


<a id="class-editordock-private-method-save-layout-to-config"></a>

void **_save_layout_to_config**(config: [ConfigFile](class_configfile.md#class-configfile), section: [String](class_string.md#class-string)) virtual const [🔗](class_editordock.md#class-editordock-private-method-save-layout-to-config)

Implement this method to handle saving this dock's layout. It's equivalent to [EditorPlugin._get_window_layout()](class_editorplugin.md#class-editorplugin-private-method-get-window-layout). `section` is a unique section based on [layout_key](class_editordock.md#class-editordock-property-layout-key).

---


<a id="class-editordock-private-method-update-layout"></a>

void **_update_layout**(layout: [int](class_int.md#class-int)) virtual [🔗](class_editordock.md#class-editordock-private-method-update-layout)

Implement this method to handle the layout switching for this dock. `layout` is one of the [DockLayout](class_editordock.md#enum-editordock-docklayout) constants.

```gdscript
func _update_layout(layout):
    box_container.vertical = (layout == DOCK_LAYOUT_VERTICAL)
```

---


<a id="class-editordock-method-close"></a>

void **close**() [🔗](class_editordock.md#class-editordock-method-close)

Closes the dock, making its tab hidden.

---


<a id="class-editordock-method-make-visible"></a>

void **make_visible**() [🔗](class_editordock.md#class-editordock-method-make-visible)

Focuses the dock's tab (or window if it's floating). If the dock was closed, it will be opened. If it's a bottom dock, makes the bottom panel visible.

---


<a id="class-editordock-method-open"></a>

void **open**() [🔗](class_editordock.md#class-editordock-method-open)

Opens the dock. It will appear in the last used dock slot. If the dock has no default slot, it will be opened floating.

**Note:** This does not focus the dock. If you want to open and focus the dock, use [make_visible()](class_editordock.md#class-editordock-method-make-visible).
