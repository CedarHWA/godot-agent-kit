> Source: https://docs.godotengine.org/en/4.7/classes/class_editorplugin.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="editorplugin"></a>

<a id="class-editorplugin"></a>

# EditorPlugin

**Inherits:** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [GridMapEditorPlugin](class_gridmapeditorplugin.md#class-gridmapeditorplugin)

Used by the editor to extend its functionality.

<a id="description"></a>

## Description

Plugins are used by the editor to extend functionality. The most common types of plugins are those which edit a given node or resource type, import plugins and export plugins. See also [EditorScript](class_editorscript.md#class-editorscript) to add functions to the editor.

**Note:** Some names in this class contain "left" or "right" (e.g. [DOCK_SLOT_LEFT_UL](class_editorplugin.md#class-editorplugin-constant-dock-slot-left-ul)). These APIs assume left-to-right layout, and would be backwards when using right-to-left layout. These names are kept for compatibility reasons.

<a id="tutorials"></a>

## Tutorials

- [Editor plugins documentation index](../tutorials/plugins/editor/index.md)

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [_apply_changes](class_editorplugin.md#class-editorplugin-private-method-apply-changes)() virtual |
| [bool](class_bool.md#class-bool) | [_build](class_editorplugin.md#class-editorplugin-private-method-build)() virtual |
| void | [_clear](class_editorplugin.md#class-editorplugin-private-method-clear)() virtual |
| void | [_disable_plugin](class_editorplugin.md#class-editorplugin-private-method-disable-plugin)() virtual |
| void | [_edit](class_editorplugin.md#class-editorplugin-private-method-edit)(object: [Object](class_object.md#class-object)) virtual |
| void | [_enable_plugin](class_editorplugin.md#class-editorplugin-private-method-enable-plugin)() virtual |
| void | [_forward_3d_draw_over_viewport](class_editorplugin.md#class-editorplugin-private-method-forward-3d-draw-over-viewport)(viewport_control: [Control](class_control.md#class-control)) virtual |
| void | [_forward_3d_force_draw_over_viewport](class_editorplugin.md#class-editorplugin-private-method-forward-3d-force-draw-over-viewport)(viewport_control: [Control](class_control.md#class-control)) virtual |
| [int](class_int.md#class-int) | [_forward_3d_gui_input](class_editorplugin.md#class-editorplugin-private-method-forward-3d-gui-input)(viewport_camera: [Camera3D](class_camera3d.md#class-camera3d), event: [InputEvent](class_inputevent.md#class-inputevent)) virtual |
| void | [_forward_canvas_draw_over_viewport](class_editorplugin.md#class-editorplugin-private-method-forward-canvas-draw-over-viewport)(viewport_control: [Control](class_control.md#class-control)) virtual |
| void | [_forward_canvas_force_draw_over_viewport](class_editorplugin.md#class-editorplugin-private-method-forward-canvas-force-draw-over-viewport)(viewport_control: [Control](class_control.md#class-control)) virtual |
| [bool](class_bool.md#class-bool) | [_forward_canvas_gui_input](class_editorplugin.md#class-editorplugin-private-method-forward-canvas-gui-input)(event: [InputEvent](class_inputevent.md#class-inputevent)) virtual |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [_get_breakpoints](class_editorplugin.md#class-editorplugin-private-method-get-breakpoints)() virtual const |
| [Texture2D](class_texture2d.md#class-texture2d) | [_get_plugin_icon](class_editorplugin.md#class-editorplugin-private-method-get-plugin-icon)() virtual const |
| [String](class_string.md#class-string) | [_get_plugin_name](class_editorplugin.md#class-editorplugin-private-method-get-plugin-name)() virtual const |
| [Dictionary](class_dictionary.md#class-dictionary) | [_get_state](class_editorplugin.md#class-editorplugin-private-method-get-state)() virtual const |
| [String](class_string.md#class-string) | [_get_unsaved_status](class_editorplugin.md#class-editorplugin-private-method-get-unsaved-status)(for_scene: [String](class_string.md#class-string)) virtual const |
| void | [_get_window_layout](class_editorplugin.md#class-editorplugin-private-method-get-window-layout)(configuration: [ConfigFile](class_configfile.md#class-configfile)) virtual |
| [bool](class_bool.md#class-bool) | [_handles](class_editorplugin.md#class-editorplugin-private-method-handles)(object: [Object](class_object.md#class-object)) virtual const |
| [bool](class_bool.md#class-bool) | [_has_main_screen](class_editorplugin.md#class-editorplugin-private-method-has-main-screen)() virtual const |
| void | [_make_visible](class_editorplugin.md#class-editorplugin-private-method-make-visible)(visible: [bool](class_bool.md#class-bool)) virtual |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [_run_scene](class_editorplugin.md#class-editorplugin-private-method-run-scene)(scene: [String](class_string.md#class-string), args: [PackedStringArray](class_packedstringarray.md#class-packedstringarray)) virtual const |
| void | [_save_external_data](class_editorplugin.md#class-editorplugin-private-method-save-external-data)() virtual |
| void | [_set_state](class_editorplugin.md#class-editorplugin-private-method-set-state)(state: [Dictionary](class_dictionary.md#class-dictionary)) virtual |
| void | [_set_window_layout](class_editorplugin.md#class-editorplugin-private-method-set-window-layout)(configuration: [ConfigFile](class_configfile.md#class-configfile)) virtual |
| void | [add_autoload_singleton](class_editorplugin.md#class-editorplugin-method-add-autoload-singleton)(name: [String](class_string.md#class-string), path: [String](class_string.md#class-string)) |
| void | [add_context_menu_plugin](class_editorplugin.md#class-editorplugin-method-add-context-menu-plugin)(slot: [ContextMenuSlot](class_editorcontextmenuplugin.md#enum-editorcontextmenuplugin-contextmenuslot), plugin: [EditorContextMenuPlugin](class_editorcontextmenuplugin.md#class-editorcontextmenuplugin)) |
| [Button](class_button.md#class-button) | [add_control_to_bottom_panel](class_editorplugin.md#class-editorplugin-method-add-control-to-bottom-panel)(control: [Control](class_control.md#class-control), title: [String](class_string.md#class-string), shortcut: [Shortcut](class_shortcut.md#class-shortcut) = null) |
| void | [add_control_to_container](class_editorplugin.md#class-editorplugin-method-add-control-to-container)(container: [CustomControlContainer](class_editorplugin.md#enum-editorplugin-customcontrolcontainer), control: [Control](class_control.md#class-control)) |
| void | [add_control_to_dock](class_editorplugin.md#class-editorplugin-method-add-control-to-dock)(slot: [DockSlot](class_editorplugin.md#enum-editorplugin-dockslot), control: [Control](class_control.md#class-control), shortcut: [Shortcut](class_shortcut.md#class-shortcut) = null) |
| void | [add_custom_type](class_editorplugin.md#class-editorplugin-method-add-custom-type)(type: [String](class_string.md#class-string), base: [String](class_string.md#class-string), script: [Script](class_script.md#class-script), icon: [Texture2D](class_texture2d.md#class-texture2d)) |
| void | [add_debugger_plugin](class_editorplugin.md#class-editorplugin-method-add-debugger-plugin)(script: [EditorDebuggerPlugin](class_editordebuggerplugin.md#class-editordebuggerplugin)) |
| void | [add_dock](class_editorplugin.md#class-editorplugin-method-add-dock)(dock: [EditorDock](class_editordock.md#class-editordock)) |
| void | [add_export_platform](class_editorplugin.md#class-editorplugin-method-add-export-platform)(platform: [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform)) |
| void | [add_export_plugin](class_editorplugin.md#class-editorplugin-method-add-export-plugin)(plugin: [EditorExportPlugin](class_editorexportplugin.md#class-editorexportplugin)) |
| void | [add_import_plugin](class_editorplugin.md#class-editorplugin-method-add-import-plugin)(importer: [EditorImportPlugin](class_editorimportplugin.md#class-editorimportplugin), first_priority: [bool](class_bool.md#class-bool) = false) |
| void | [add_inspector_plugin](class_editorplugin.md#class-editorplugin-method-add-inspector-plugin)(plugin: [EditorInspectorPlugin](class_editorinspectorplugin.md#class-editorinspectorplugin)) |
| void | [add_node_3d_gizmo_plugin](class_editorplugin.md#class-editorplugin-method-add-node-3d-gizmo-plugin)(plugin: [EditorNode3DGizmoPlugin](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin)) |
| void | [add_resource_conversion_plugin](class_editorplugin.md#class-editorplugin-method-add-resource-conversion-plugin)(plugin: [EditorResourceConversionPlugin](class_editorresourceconversionplugin.md#class-editorresourceconversionplugin)) |
| void | [add_scene_format_importer_plugin](class_editorplugin.md#class-editorplugin-method-add-scene-format-importer-plugin)(scene_format_importer: [EditorSceneFormatImporter](class_editorsceneformatimporter.md#class-editorsceneformatimporter), first_priority: [bool](class_bool.md#class-bool) = false) |
| void | [add_scene_post_import_plugin](class_editorplugin.md#class-editorplugin-method-add-scene-post-import-plugin)(scene_import_plugin: [EditorScenePostImportPlugin](class_editorscenepostimportplugin.md#class-editorscenepostimportplugin), first_priority: [bool](class_bool.md#class-bool) = false) |
| void | [add_tool_menu_item](class_editorplugin.md#class-editorplugin-method-add-tool-menu-item)(name: [String](class_string.md#class-string), callable: [Callable](class_callable.md#class-callable)) |
| void | [add_tool_submenu_item](class_editorplugin.md#class-editorplugin-method-add-tool-submenu-item)(name: [String](class_string.md#class-string), submenu: [PopupMenu](class_popupmenu.md#class-popupmenu)) |
| void | [add_translation_parser_plugin](class_editorplugin.md#class-editorplugin-method-add-translation-parser-plugin)(parser: [EditorTranslationParserPlugin](class_editortranslationparserplugin.md#class-editortranslationparserplugin)) |
| void | [add_undo_redo_inspector_hook_callback](class_editorplugin.md#class-editorplugin-method-add-undo-redo-inspector-hook-callback)(callable: [Callable](class_callable.md#class-callable)) |
| [EditorInterface](class_editorinterface.md#class-editorinterface) | [get_editor_interface](class_editorplugin.md#class-editorplugin-method-get-editor-interface)() |
| [PopupMenu](class_popupmenu.md#class-popupmenu) | [get_export_as_menu](class_editorplugin.md#class-editorplugin-method-get-export-as-menu)() |
| [String](class_string.md#class-string) | [get_plugin_version](class_editorplugin.md#class-editorplugin-method-get-plugin-version)() const |
| [ScriptCreateDialog](class_scriptcreatedialog.md#class-scriptcreatedialog) | [get_script_create_dialog](class_editorplugin.md#class-editorplugin-method-get-script-create-dialog)() |
| [EditorUndoRedoManager](class_editorundoredomanager.md#class-editorundoredomanager) | [get_undo_redo](class_editorplugin.md#class-editorplugin-method-get-undo-redo)() |
| void | [hide_bottom_panel](class_editorplugin.md#class-editorplugin-method-hide-bottom-panel)() |
| void | [make_bottom_panel_item_visible](class_editorplugin.md#class-editorplugin-method-make-bottom-panel-item-visible)(item: [Control](class_control.md#class-control)) |
| void | [queue_save_layout](class_editorplugin.md#class-editorplugin-method-queue-save-layout)() |
| void | [remove_autoload_singleton](class_editorplugin.md#class-editorplugin-method-remove-autoload-singleton)(name: [String](class_string.md#class-string)) |
| void | [remove_context_menu_plugin](class_editorplugin.md#class-editorplugin-method-remove-context-menu-plugin)(plugin: [EditorContextMenuPlugin](class_editorcontextmenuplugin.md#class-editorcontextmenuplugin)) |
| void | [remove_control_from_bottom_panel](class_editorplugin.md#class-editorplugin-method-remove-control-from-bottom-panel)(control: [Control](class_control.md#class-control)) |
| void | [remove_control_from_container](class_editorplugin.md#class-editorplugin-method-remove-control-from-container)(container: [CustomControlContainer](class_editorplugin.md#enum-editorplugin-customcontrolcontainer), control: [Control](class_control.md#class-control)) |
| void | [remove_control_from_docks](class_editorplugin.md#class-editorplugin-method-remove-control-from-docks)(control: [Control](class_control.md#class-control)) |
| void | [remove_custom_type](class_editorplugin.md#class-editorplugin-method-remove-custom-type)(type: [String](class_string.md#class-string)) |
| void | [remove_debugger_plugin](class_editorplugin.md#class-editorplugin-method-remove-debugger-plugin)(script: [EditorDebuggerPlugin](class_editordebuggerplugin.md#class-editordebuggerplugin)) |
| void | [remove_dock](class_editorplugin.md#class-editorplugin-method-remove-dock)(dock: [EditorDock](class_editordock.md#class-editordock)) |
| void | [remove_export_platform](class_editorplugin.md#class-editorplugin-method-remove-export-platform)(platform: [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform)) |
| void | [remove_export_plugin](class_editorplugin.md#class-editorplugin-method-remove-export-plugin)(plugin: [EditorExportPlugin](class_editorexportplugin.md#class-editorexportplugin)) |
| void | [remove_import_plugin](class_editorplugin.md#class-editorplugin-method-remove-import-plugin)(importer: [EditorImportPlugin](class_editorimportplugin.md#class-editorimportplugin)) |
| void | [remove_inspector_plugin](class_editorplugin.md#class-editorplugin-method-remove-inspector-plugin)(plugin: [EditorInspectorPlugin](class_editorinspectorplugin.md#class-editorinspectorplugin)) |
| void | [remove_node_3d_gizmo_plugin](class_editorplugin.md#class-editorplugin-method-remove-node-3d-gizmo-plugin)(plugin: [EditorNode3DGizmoPlugin](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin)) |
| void | [remove_resource_conversion_plugin](class_editorplugin.md#class-editorplugin-method-remove-resource-conversion-plugin)(plugin: [EditorResourceConversionPlugin](class_editorresourceconversionplugin.md#class-editorresourceconversionplugin)) |
| void | [remove_scene_format_importer_plugin](class_editorplugin.md#class-editorplugin-method-remove-scene-format-importer-plugin)(scene_format_importer: [EditorSceneFormatImporter](class_editorsceneformatimporter.md#class-editorsceneformatimporter)) |
| void | [remove_scene_post_import_plugin](class_editorplugin.md#class-editorplugin-method-remove-scene-post-import-plugin)(scene_import_plugin: [EditorScenePostImportPlugin](class_editorscenepostimportplugin.md#class-editorscenepostimportplugin)) |
| void | [remove_tool_menu_item](class_editorplugin.md#class-editorplugin-method-remove-tool-menu-item)(name: [String](class_string.md#class-string)) |
| void | [remove_translation_parser_plugin](class_editorplugin.md#class-editorplugin-method-remove-translation-parser-plugin)(parser: [EditorTranslationParserPlugin](class_editortranslationparserplugin.md#class-editortranslationparserplugin)) |
| void | [remove_undo_redo_inspector_hook_callback](class_editorplugin.md#class-editorplugin-method-remove-undo-redo-inspector-hook-callback)(callable: [Callable](class_callable.md#class-callable)) |
| void | [set_dock_tab_icon](class_editorplugin.md#class-editorplugin-method-set-dock-tab-icon)(control: [Control](class_control.md#class-control), icon: [Texture2D](class_texture2d.md#class-texture2d)) |
| void | [set_force_draw_over_forwarding_enabled](class_editorplugin.md#class-editorplugin-method-set-force-draw-over-forwarding-enabled)() |
| void | [set_input_event_forwarding_always_enabled](class_editorplugin.md#class-editorplugin-method-set-input-event-forwarding-always-enabled)() |
| [int](class_int.md#class-int) | [update_overlays](class_editorplugin.md#class-editorplugin-method-update-overlays)() const |

---


<a id="signals"></a>

## Signals

<a id="class-editorplugin-signal-main-screen-changed"></a>

**main_screen_changed**(screen_name: [String](class_string.md#class-string)) [🔗](class_editorplugin.md#class-editorplugin-signal-main-screen-changed)

Emitted when user changes the workspace (**2D**, **3D**, **Script**, **Game**, **Asset Store**). Also works with custom screens defined by plugins.

---


<a id="class-editorplugin-signal-project-settings-changed"></a>

**project_settings_changed**() [🔗](class_editorplugin.md#class-editorplugin-signal-project-settings-changed)

**Deprecated:** Use [ProjectSettings.settings_changed](class_projectsettings.md#class-projectsettings-signal-settings-changed) instead.

Emitted when any project setting has changed.

---


<a id="class-editorplugin-signal-resource-saved"></a>

**resource_saved**(resource: [Resource](class_resource.md#class-resource)) [🔗](class_editorplugin.md#class-editorplugin-signal-resource-saved)

Emitted when the given `resource` was saved on disc. See also [scene_saved](class_editorplugin.md#class-editorplugin-signal-scene-saved).

---


<a id="class-editorplugin-signal-scene-changed"></a>

**scene_changed**(scene_root: [Node](class_node.md#class-node)) [🔗](class_editorplugin.md#class-editorplugin-signal-scene-changed)

Emitted when the scene is changed in the editor. The argument will return the root node of the scene that has just become active. If this scene is new and empty, the argument will be `null`.

---


<a id="class-editorplugin-signal-scene-closed"></a>

**scene_closed**(filepath: [String](class_string.md#class-string)) [🔗](class_editorplugin.md#class-editorplugin-signal-scene-closed)

Emitted when user closes a scene. The argument is a file path to the closed scene.

---


<a id="class-editorplugin-signal-scene-saved"></a>

**scene_saved**(filepath: [String](class_string.md#class-string)) [🔗](class_editorplugin.md#class-editorplugin-signal-scene-saved)

Emitted when a scene was saved on disc. The argument is a file path to the saved scene. See also [resource_saved](class_editorplugin.md#class-editorplugin-signal-resource-saved).

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-editorplugin-customcontrolcontainer"></a>

enum **CustomControlContainer**: [🔗](class_editorplugin.md#enum-editorplugin-customcontrolcontainer)

<a id="class-editorplugin-constant-container-toolbar"></a>

[CustomControlContainer](class_editorplugin.md#enum-editorplugin-customcontrolcontainer) **CONTAINER_TOOLBAR** = `0`

Main editor toolbar, next to play buttons.

<a id="class-editorplugin-constant-container-spatial-editor-menu"></a>

[CustomControlContainer](class_editorplugin.md#enum-editorplugin-customcontrolcontainer) **CONTAINER_SPATIAL_EDITOR_MENU** = `1`

The toolbar that appears when 3D editor is active.

<a id="class-editorplugin-constant-container-spatial-editor-side-left"></a>

[CustomControlContainer](class_editorplugin.md#enum-editorplugin-customcontrolcontainer) **CONTAINER_SPATIAL_EDITOR_SIDE_LEFT** = `2`

Left sidebar of the 3D editor.

<a id="class-editorplugin-constant-container-spatial-editor-side-right"></a>

[CustomControlContainer](class_editorplugin.md#enum-editorplugin-customcontrolcontainer) **CONTAINER_SPATIAL_EDITOR_SIDE_RIGHT** = `3`

Right sidebar of the 3D editor.

<a id="class-editorplugin-constant-container-spatial-editor-bottom"></a>

[CustomControlContainer](class_editorplugin.md#enum-editorplugin-customcontrolcontainer) **CONTAINER_SPATIAL_EDITOR_BOTTOM** = `4`

Bottom panel of the 3D editor.

<a id="class-editorplugin-constant-container-canvas-editor-menu"></a>

[CustomControlContainer](class_editorplugin.md#enum-editorplugin-customcontrolcontainer) **CONTAINER_CANVAS_EDITOR_MENU** = `5`

The toolbar that appears when 2D editor is active.

<a id="class-editorplugin-constant-container-canvas-editor-side-left"></a>

[CustomControlContainer](class_editorplugin.md#enum-editorplugin-customcontrolcontainer) **CONTAINER_CANVAS_EDITOR_SIDE_LEFT** = `6`

Left sidebar of the 2D editor.

<a id="class-editorplugin-constant-container-canvas-editor-side-right"></a>

[CustomControlContainer](class_editorplugin.md#enum-editorplugin-customcontrolcontainer) **CONTAINER_CANVAS_EDITOR_SIDE_RIGHT** = `7`

Right sidebar of the 2D editor.

<a id="class-editorplugin-constant-container-canvas-editor-bottom"></a>

[CustomControlContainer](class_editorplugin.md#enum-editorplugin-customcontrolcontainer) **CONTAINER_CANVAS_EDITOR_BOTTOM** = `8`

Bottom panel of the 2D editor.

<a id="class-editorplugin-constant-container-inspector-bottom"></a>

[CustomControlContainer](class_editorplugin.md#enum-editorplugin-customcontrolcontainer) **CONTAINER_INSPECTOR_BOTTOM** = `9`

Bottom section of the inspector.

<a id="class-editorplugin-constant-container-project-setting-tab-left"></a>

[CustomControlContainer](class_editorplugin.md#enum-editorplugin-customcontrolcontainer) **CONTAINER_PROJECT_SETTING_TAB_LEFT** = `10`

Tab of Project Settings dialog, to the left of other tabs.

<a id="class-editorplugin-constant-container-project-setting-tab-right"></a>

[CustomControlContainer](class_editorplugin.md#enum-editorplugin-customcontrolcontainer) **CONTAINER_PROJECT_SETTING_TAB_RIGHT** = `11`

Tab of Project Settings dialog, to the right of other tabs.

---


<a id="enum-editorplugin-dockslot"></a>

enum **DockSlot**: [🔗](class_editorplugin.md#enum-editorplugin-dockslot)

<a id="class-editorplugin-constant-dock-slot-none"></a>

[DockSlot](class_editorplugin.md#enum-editorplugin-dockslot) **DOCK_SLOT_NONE** = `-1`

The dock is closed.

<a id="class-editorplugin-constant-dock-slot-left-ul"></a>

[DockSlot](class_editorplugin.md#enum-editorplugin-dockslot) **DOCK_SLOT_LEFT_UL** = `0`

Dock slot, left side, upper-left (empty in default layout).

<a id="class-editorplugin-constant-dock-slot-left-bl"></a>

[DockSlot](class_editorplugin.md#enum-editorplugin-dockslot) **DOCK_SLOT_LEFT_BL** = `1`

Dock slot, left side, bottom-left (empty in default layout).

<a id="class-editorplugin-constant-dock-slot-left-ur"></a>

[DockSlot](class_editorplugin.md#enum-editorplugin-dockslot) **DOCK_SLOT_LEFT_UR** = `2`

Dock slot, left side, upper-right (in default layout includes Scene and Import docks).

<a id="class-editorplugin-constant-dock-slot-left-br"></a>

[DockSlot](class_editorplugin.md#enum-editorplugin-dockslot) **DOCK_SLOT_LEFT_BR** = `3`

Dock slot, left side, bottom-right (in default layout includes FileSystem dock).

<a id="class-editorplugin-constant-dock-slot-right-ul"></a>

[DockSlot](class_editorplugin.md#enum-editorplugin-dockslot) **DOCK_SLOT_RIGHT_UL** = `4`

Dock slot, right side, upper-left (in default layout includes Inspector, Node, and History docks).

<a id="class-editorplugin-constant-dock-slot-right-bl"></a>

[DockSlot](class_editorplugin.md#enum-editorplugin-dockslot) **DOCK_SLOT_RIGHT_BL** = `5`

Dock slot, right side, bottom-left (empty in default layout).

<a id="class-editorplugin-constant-dock-slot-right-ur"></a>

[DockSlot](class_editorplugin.md#enum-editorplugin-dockslot) **DOCK_SLOT_RIGHT_UR** = `6`

Dock slot, right side, upper-right (empty in default layout).

<a id="class-editorplugin-constant-dock-slot-right-br"></a>

[DockSlot](class_editorplugin.md#enum-editorplugin-dockslot) **DOCK_SLOT_RIGHT_BR** = `7`

Dock slot, right side, bottom-right (empty in default layout).

<a id="class-editorplugin-constant-dock-slot-bottom"></a>

[DockSlot](class_editorplugin.md#enum-editorplugin-dockslot) **DOCK_SLOT_BOTTOM** = `8`

Bottom panel.

<a id="class-editorplugin-constant-dock-slot-max"></a>

[DockSlot](class_editorplugin.md#enum-editorplugin-dockslot) **DOCK_SLOT_MAX** = `9`

Represents the size of the [DockSlot](class_editorplugin.md#enum-editorplugin-dockslot) enum.

---


<a id="enum-editorplugin-afterguiinput"></a>

enum **AfterGUIInput**: [🔗](class_editorplugin.md#enum-editorplugin-afterguiinput)

<a id="class-editorplugin-constant-after-gui-input-pass"></a>

[AfterGUIInput](class_editorplugin.md#enum-editorplugin-afterguiinput) **AFTER_GUI_INPUT_PASS** = `0`

Forwards the [InputEvent](class_inputevent.md#class-inputevent) to other EditorPlugins.

<a id="class-editorplugin-constant-after-gui-input-stop"></a>

[AfterGUIInput](class_editorplugin.md#enum-editorplugin-afterguiinput) **AFTER_GUI_INPUT_STOP** = `1`

Prevents the [InputEvent](class_inputevent.md#class-inputevent) from reaching other Editor classes.

<a id="class-editorplugin-constant-after-gui-input-custom"></a>

[AfterGUIInput](class_editorplugin.md#enum-editorplugin-afterguiinput) **AFTER_GUI_INPUT_CUSTOM** = `2`

Pass the [InputEvent](class_inputevent.md#class-inputevent) to other editor plugins except the main [Node3D](class_node3d.md#class-node3d) one. This can be used to prevent node selection changes and work with sub-gizmos instead.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-editorplugin-private-method-apply-changes"></a>

void **_apply_changes**() virtual [🔗](class_editorplugin.md#class-editorplugin-private-method-apply-changes)

This method is called when the editor is about to save the project, switch to another tab, etc. It asks the plugin to apply any pending state changes to ensure consistency.

This is used, for example, in shader editors to let the plugin know that it must apply the shader code being written by the user to the object.

---


<a id="class-editorplugin-private-method-build"></a>

[bool](class_bool.md#class-bool) **_build**() virtual [🔗](class_editorplugin.md#class-editorplugin-private-method-build)

This method is called when the editor is about to run the project. The plugin can then perform required operations before the project runs.

This method must return a boolean. If this method returns `false`, the project will not run. The run is aborted immediately, so this also prevents all other plugins' [_build()](class_editorplugin.md#class-editorplugin-private-method-build) methods from running.

---


<a id="class-editorplugin-private-method-clear"></a>

void **_clear**() virtual [🔗](class_editorplugin.md#class-editorplugin-private-method-clear)

Clear all the state and reset the object being edited to zero. This ensures your plugin does not keep editing a currently existing node, or a node from the wrong scene.

---


<a id="class-editorplugin-private-method-disable-plugin"></a>

void **_disable_plugin**() virtual [🔗](class_editorplugin.md#class-editorplugin-private-method-disable-plugin)

Called by the engine when the user disables the **EditorPlugin** in the Plugin tab of the project settings window.

---


<a id="class-editorplugin-private-method-edit"></a>

void **_edit**(object: [Object](class_object.md#class-object)) virtual [🔗](class_editorplugin.md#class-editorplugin-private-method-edit)

This function is used for plugins that edit specific object types (nodes or resources). It requests the editor to edit the given object.

`object` can be `null` if the plugin was editing an object, but there is no longer any selected object handled by this plugin. It can be used to cleanup editing state.

---


<a id="class-editorplugin-private-method-enable-plugin"></a>

void **_enable_plugin**() virtual [🔗](class_editorplugin.md#class-editorplugin-private-method-enable-plugin)

Called by the engine when the user enables the **EditorPlugin** in the Plugin tab of the project settings window.

---


<a id="class-editorplugin-private-method-forward-3d-draw-over-viewport"></a>

void **_forward_3d_draw_over_viewport**(viewport_control: [Control](class_control.md#class-control)) virtual [🔗](class_editorplugin.md#class-editorplugin-private-method-forward-3d-draw-over-viewport)

Called by the engine when the 3D editor's viewport is updated. `viewport_control` is an overlay on top of the viewport and it can be used for drawing. You can update the viewport manually by calling [update_overlays()](class_editorplugin.md#class-editorplugin-method-update-overlays).

```gdscript
func _forward_3d_draw_over_viewport(overlay):
    # Draw a circle at the cursor's position.
    overlay.draw_circle(overlay.get_local_mouse_position(), 64, Color.WHITE)

func _forward_3d_gui_input(camera, event):
    if event is InputEventMouseMotion:
        # Redraw the viewport when the cursor is moved.
        update_overlays()
        return EditorPlugin.AFTER_GUI_INPUT_STOP
    return EditorPlugin.AFTER_GUI_INPUT_PASS
```

```csharp
public override void _Forward3DDrawOverViewport(Control viewportControl)
{
    // Draw a circle at the cursor's position.
    viewportControl.DrawCircle(viewportControl.GetLocalMousePosition(), 64, Colors.White);
}

public override EditorPlugin.AfterGuiInput _Forward3DGuiInput(Camera3D viewportCamera, InputEvent @event)
{
    if (@event is InputEventMouseMotion)
    {
        // Redraw the viewport when the cursor is moved.
        UpdateOverlays();
        return EditorPlugin.AfterGuiInput.Stop;
    }
    return EditorPlugin.AfterGuiInput.Pass;
}
```

---


<a id="class-editorplugin-private-method-forward-3d-force-draw-over-viewport"></a>

void **_forward_3d_force_draw_over_viewport**(viewport_control: [Control](class_control.md#class-control)) virtual [🔗](class_editorplugin.md#class-editorplugin-private-method-forward-3d-force-draw-over-viewport)

This method is the same as [_forward_3d_draw_over_viewport()](class_editorplugin.md#class-editorplugin-private-method-forward-3d-draw-over-viewport), except it draws on top of everything. Useful when you need an extra layer that shows over anything else.

You need to enable calling of this method by using [set_force_draw_over_forwarding_enabled()](class_editorplugin.md#class-editorplugin-method-set-force-draw-over-forwarding-enabled).

---


<a id="class-editorplugin-private-method-forward-3d-gui-input"></a>

[int](class_int.md#class-int) **_forward_3d_gui_input**(viewport_camera: [Camera3D](class_camera3d.md#class-camera3d), event: [InputEvent](class_inputevent.md#class-inputevent)) virtual [🔗](class_editorplugin.md#class-editorplugin-private-method-forward-3d-gui-input)

Called when there is a root node in the current edited scene, [_handles()](class_editorplugin.md#class-editorplugin-private-method-handles) is implemented, and an [InputEvent](class_inputevent.md#class-inputevent) happens in the 3D viewport. The return value decides whether the [InputEvent](class_inputevent.md#class-inputevent) is consumed or forwarded to other **EditorPlugin**s. See [AfterGUIInput](class_editorplugin.md#enum-editorplugin-afterguiinput) for options.

```gdscript
# Prevents the InputEvent from reaching other Editor classes.
func _forward_3d_gui_input(camera, event):
    return EditorPlugin.AFTER_GUI_INPUT_STOP
```

```csharp
// Prevents the InputEvent from reaching other Editor classes.
public override EditorPlugin.AfterGuiInput _Forward3DGuiInput(Camera3D camera, InputEvent @event)
{
    return EditorPlugin.AfterGuiInput.Stop;
}
```

This method must return [AFTER_GUI_INPUT_PASS](class_editorplugin.md#class-editorplugin-constant-after-gui-input-pass) in order to forward the [InputEvent](class_inputevent.md#class-inputevent) to other Editor classes.

```gdscript
# Consumes InputEventMouseMotion and forwards other InputEvent types.
func _forward_3d_gui_input(camera, event):
    return EditorPlugin.AFTER_GUI_INPUT_STOP if event is InputEventMouseMotion else EditorPlugin.AFTER_GUI_INPUT_PASS
```

```csharp
// Consumes InputEventMouseMotion and forwards other InputEvent types.
public override EditorPlugin.AfterGuiInput _Forward3DGuiInput(Camera3D camera, InputEvent @event)
{
    return @event is InputEventMouseMotion ? EditorPlugin.AfterGuiInput.Stop : EditorPlugin.AfterGuiInput.Pass;
}
```

---


<a id="class-editorplugin-private-method-forward-canvas-draw-over-viewport"></a>

void **_forward_canvas_draw_over_viewport**(viewport_control: [Control](class_control.md#class-control)) virtual [🔗](class_editorplugin.md#class-editorplugin-private-method-forward-canvas-draw-over-viewport)

Called by the engine when the 2D editor's viewport is updated. `viewport_control` is an overlay on top of the viewport and it can be used for drawing. You can update the viewport manually by calling [update_overlays()](class_editorplugin.md#class-editorplugin-method-update-overlays).

```gdscript
func _forward_canvas_draw_over_viewport(overlay):
    # Draw a circle at the cursor's position.
    overlay.draw_circle(overlay.get_local_mouse_position(), 64, Color.WHITE)

func _forward_canvas_gui_input(event):
    if event is InputEventMouseMotion:
        # Redraw the viewport when the cursor is moved.
        update_overlays()
        return true
    return false
```

```csharp
public override void _ForwardCanvasDrawOverViewport(Control viewportControl)
{
    // Draw a circle at the cursor's position.
    viewportControl.DrawCircle(viewportControl.GetLocalMousePosition(), 64, Colors.White);
}

public override bool _ForwardCanvasGuiInput(InputEvent @event)
{
    if (@event is InputEventMouseMotion)
    {
        // Redraw the viewport when the cursor is moved.
        UpdateOverlays();
        return true;
    }
    return false;
}
```

---


<a id="class-editorplugin-private-method-forward-canvas-force-draw-over-viewport"></a>

void **_forward_canvas_force_draw_over_viewport**(viewport_control: [Control](class_control.md#class-control)) virtual [🔗](class_editorplugin.md#class-editorplugin-private-method-forward-canvas-force-draw-over-viewport)

This method is the same as [_forward_canvas_draw_over_viewport()](class_editorplugin.md#class-editorplugin-private-method-forward-canvas-draw-over-viewport), except it draws on top of everything. Useful when you need an extra layer that shows over anything else.

You need to enable calling of this method by using [set_force_draw_over_forwarding_enabled()](class_editorplugin.md#class-editorplugin-method-set-force-draw-over-forwarding-enabled).

---


<a id="class-editorplugin-private-method-forward-canvas-gui-input"></a>

[bool](class_bool.md#class-bool) **_forward_canvas_gui_input**(event: [InputEvent](class_inputevent.md#class-inputevent)) virtual [🔗](class_editorplugin.md#class-editorplugin-private-method-forward-canvas-gui-input)

Called when there is a root node in the current edited scene, [_handles()](class_editorplugin.md#class-editorplugin-private-method-handles) is implemented, and an [InputEvent](class_inputevent.md#class-inputevent) happens in the 2D viewport. If this method returns `true`, `event` is intercepted by this **EditorPlugin**, otherwise `event` is forwarded to other Editor classes.

```gdscript
# Prevents the InputEvent from reaching other Editor classes.
func _forward_canvas_gui_input(event):
    return true
```

```csharp
// Prevents the InputEvent from reaching other Editor classes.
public override bool ForwardCanvasGuiInput(InputEvent @event)
{
    return true;
}
```

This method must return `false` in order to forward the [InputEvent](class_inputevent.md#class-inputevent) to other Editor classes.

```gdscript
# Consumes InputEventMouseMotion and forwards other InputEvent types.
func _forward_canvas_gui_input(event):
    if (event is InputEventMouseMotion):
        return true
    return false
```

```csharp
// Consumes InputEventMouseMotion and forwards other InputEvent types.
public override bool _ForwardCanvasGuiInput(InputEvent @event)
{
    if (@event is InputEventMouseMotion)
    {
        return true;
    }
    return false;
}
```

---


<a id="class-editorplugin-private-method-get-breakpoints"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **_get_breakpoints**() virtual const [🔗](class_editorplugin.md#class-editorplugin-private-method-get-breakpoints)

This is for editors that edit script-based objects. You can return a list of breakpoints in the format (`script:line`), for example: `res://path_to_script.gd:25`.

---


<a id="class-editorplugin-private-method-get-plugin-icon"></a>

[Texture2D](class_texture2d.md#class-texture2d) **_get_plugin_icon**() virtual const [🔗](class_editorplugin.md#class-editorplugin-private-method-get-plugin-icon)

Override this method in your plugin to return a [Texture2D](class_texture2d.md#class-texture2d) in order to give it an icon.

For main screen plugins, this appears at the top of the screen, to the right of the "2D", "3D", "Script", "Game", and "Asset Store" buttons.

Ideally, the plugin icon should be white with a transparent background and 16×16 pixels in size.

```gdscript
func _get_plugin_icon():
    # You can use a custom icon:
    return preload("res://addons/my_plugin/my_plugin_icon.svg")
    # Or use a built-in icon:
    return EditorInterface.get_editor_theme().get_icon("Node", "EditorIcons")
```

```csharp
public override Texture2D _GetPluginIcon()
{
    // You can use a custom icon:
    return ResourceLoader.Load<Texture2D>("res://addons/my_plugin/my_plugin_icon.svg");
    // Or use a built-in icon:
    return EditorInterface.Singleton.GetEditorTheme().GetIcon("Node", "EditorIcons");
}
```

---


<a id="class-editorplugin-private-method-get-plugin-name"></a>

[String](class_string.md#class-string) **_get_plugin_name**() virtual const [🔗](class_editorplugin.md#class-editorplugin-private-method-get-plugin-name)

Override this method in your plugin to provide the name of the plugin when displayed in the Godot editor.

For main screen plugins, this appears at the top of the screen, to the right of the "2D", "3D", "Script", "Game", and "Asset Store" buttons.

---


<a id="class-editorplugin-private-method-get-state"></a>

[Dictionary](class_dictionary.md#class-dictionary) **_get_state**() virtual const [🔗](class_editorplugin.md#class-editorplugin-private-method-get-state)

Override this method to provide a state data you want to be saved, like view position, grid settings, folding, etc. This is used when saving the scene (so state is kept when opening it again) and for switching tabs (so state can be restored when the tab returns). This data is automatically saved for each scene in an `editstate` file in the editor metadata folder. If you want to store global (scene-independent) editor data for your plugin, you can use [_get_window_layout()](class_editorplugin.md#class-editorplugin-private-method-get-window-layout) instead.

Use [_set_state()](class_editorplugin.md#class-editorplugin-private-method-set-state) to restore your saved state.

**Note:** This method should not be used to save important settings that should persist with the project.

**Note:** You must implement [_get_plugin_name()](class_editorplugin.md#class-editorplugin-private-method-get-plugin-name) for the state to be stored and restored correctly.

```gdscript
func _get_state():
    var state = { "zoom": zoom, "preferred_color": my_color }
    return state
```

---


<a id="class-editorplugin-private-method-get-unsaved-status"></a>

[String](class_string.md#class-string) **_get_unsaved_status**(for_scene: [String](class_string.md#class-string)) virtual const [🔗](class_editorplugin.md#class-editorplugin-private-method-get-unsaved-status)

Override this method to provide a custom message that lists unsaved changes. The editor will call this method when exiting or when closing a scene, and display the returned string in a confirmation dialog. Return empty string if the plugin has no unsaved changes.

When closing a scene, `for_scene` is the path to the scene being closed. You can use it to handle built-in resources in that scene.

If the user confirms saving, [_save_external_data()](class_editorplugin.md#class-editorplugin-private-method-save-external-data) will be called, before closing the editor.

```gdscript
func _get_unsaved_status(for_scene):
    if not unsaved:
        return ""

    if for_scene.is_empty():
        return "Save changes in MyCustomPlugin before closing?"
    else:
        return "Scene %s has changes from MyCustomPlugin. Save before closing?" % for_scene.get_file()

func _save_external_data():
    unsaved = false
```

If the plugin has no scene-specific changes, you can ignore the calls when closing scenes:

```gdscript
func _get_unsaved_status(for_scene):
    if not for_scene.is_empty():
        return ""
```

---


<a id="class-editorplugin-private-method-get-window-layout"></a>

void **_get_window_layout**(configuration: [ConfigFile](class_configfile.md#class-configfile)) virtual [🔗](class_editorplugin.md#class-editorplugin-private-method-get-window-layout)

Override this method to provide the GUI layout of the plugin or any other data you want to be stored. This is used to save the project's editor layout when [queue_save_layout()](class_editorplugin.md#class-editorplugin-method-queue-save-layout) is called or the editor layout was changed (for example changing the position of a dock). The data is stored in the `editor_layout.cfg` file in the editor metadata directory.

Use [_set_window_layout()](class_editorplugin.md#class-editorplugin-private-method-set-window-layout) to restore your saved layout.

```gdscript
func _get_window_layout(configuration):
    configuration.set_value("MyPlugin", "window_position", $Window.position)
    configuration.set_value("MyPlugin", "icon_color", $Icon.modulate)
```

---


<a id="class-editorplugin-private-method-handles"></a>

[bool](class_bool.md#class-bool) **_handles**(object: [Object](class_object.md#class-object)) virtual const [🔗](class_editorplugin.md#class-editorplugin-private-method-handles)

Implement this function if your plugin edits a specific type of object (Resource or Node). If you return `true`, then you will get the functions [_edit()](class_editorplugin.md#class-editorplugin-private-method-edit) and [_make_visible()](class_editorplugin.md#class-editorplugin-private-method-make-visible) called when the editor requests them. If you have declared the methods [_forward_canvas_gui_input()](class_editorplugin.md#class-editorplugin-private-method-forward-canvas-gui-input) and [_forward_3d_gui_input()](class_editorplugin.md#class-editorplugin-private-method-forward-3d-gui-input) these will be called too.

**Note:** Each plugin should handle only one type of objects at a time. If a plugin handles more types of objects and they are edited at the same time, it will result in errors.

---


<a id="class-editorplugin-private-method-has-main-screen"></a>

[bool](class_bool.md#class-bool) **_has_main_screen**() virtual const [🔗](class_editorplugin.md#class-editorplugin-private-method-has-main-screen)

Returns `true` if this is a main screen editor plugin (it goes in the workspace selector together with **2D**, **3D**, **Script**, **Game**, and **Asset Store**).

When the plugin's workspace is selected, other main screen plugins will be hidden, but your plugin will not appear automatically. It needs to be added as a child of [EditorInterface.get_editor_main_screen()](class_editorinterface.md#class-editorinterface-method-get-editor-main-screen) and made visible inside [_make_visible()](class_editorplugin.md#class-editorplugin-private-method-make-visible).

Use [_get_plugin_name()](class_editorplugin.md#class-editorplugin-private-method-get-plugin-name) and [_get_plugin_icon()](class_editorplugin.md#class-editorplugin-private-method-get-plugin-icon) to customize the plugin button's appearance.

```gdscript
var plugin_control

func _enter_tree():
    plugin_control = preload("my_plugin_control.tscn").instantiate()
    EditorInterface.get_editor_main_screen().add_child(plugin_control)
    plugin_control.hide()

func _has_main_screen():
    return true

func _make_visible(visible):
    plugin_control.visible = visible

func _get_plugin_name():
    return "My Super Cool Plugin 3000"

func _get_plugin_icon():
    return EditorInterface.get_editor_theme().get_icon("Node", "EditorIcons")
```

---


<a id="class-editorplugin-private-method-make-visible"></a>

void **_make_visible**(visible: [bool](class_bool.md#class-bool)) virtual [🔗](class_editorplugin.md#class-editorplugin-private-method-make-visible)

This function will be called when the editor is requested to become visible. It is used for plugins that edit a specific object type.

Remember that you have to manage the visibility of all your editor controls manually.

---


<a id="class-editorplugin-private-method-run-scene"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **_run_scene**(scene: [String](class_string.md#class-string), args: [PackedStringArray](class_packedstringarray.md#class-packedstringarray)) virtual const [🔗](class_editorplugin.md#class-editorplugin-private-method-run-scene)

This function is called when an individual scene is about to be played in the editor. `args` is a list of command line arguments that will be passed to the new Godot instance, which will be replaced by the list returned by this function.

```gdscript
func _run_scene(scene, args):
    args.append("--an-extra-argument")
    return args
```

**Note:** Text that is printed in this method will not be visible in the editor's Output panel unless [EditorSettings.run/output/always_clear_output_on_play](class_editorsettings.md#class-editorsettings-property-run-output-always-clear-output-on-play) is `false`.

---


<a id="class-editorplugin-private-method-save-external-data"></a>

void **_save_external_data**() virtual [🔗](class_editorplugin.md#class-editorplugin-private-method-save-external-data)

This method is called after the editor saves the project or when it's closed. It asks the plugin to save edited external scenes/resources.

---


<a id="class-editorplugin-private-method-set-state"></a>

void **_set_state**(state: [Dictionary](class_dictionary.md#class-dictionary)) virtual [🔗](class_editorplugin.md#class-editorplugin-private-method-set-state)

Restore the state saved by [_get_state()](class_editorplugin.md#class-editorplugin-private-method-get-state). This method is called when the current scene tab is changed in the editor.

**Note:** Your plugin must implement [_get_plugin_name()](class_editorplugin.md#class-editorplugin-private-method-get-plugin-name), otherwise it will not be recognized and this method will not be called.

```gdscript
func _set_state(data):
    zoom = data.get("zoom", 1.0)
    preferred_color = data.get("my_color", Color.WHITE)
```

---


<a id="class-editorplugin-private-method-set-window-layout"></a>

void **_set_window_layout**(configuration: [ConfigFile](class_configfile.md#class-configfile)) virtual [🔗](class_editorplugin.md#class-editorplugin-private-method-set-window-layout)

Restore the plugin GUI layout and data saved by [_get_window_layout()](class_editorplugin.md#class-editorplugin-private-method-get-window-layout). This method is called for every plugin on editor startup. Use the provided `configuration` file to read your saved data.

```gdscript
func _set_window_layout(configuration):
    $Window.position = configuration.get_value("MyPlugin", "window_position", Vector2())
    $Icon.modulate = configuration.get_value("MyPlugin", "icon_color", Color.WHITE)
```

---


<a id="class-editorplugin-method-add-autoload-singleton"></a>

void **add_autoload_singleton**(name: [String](class_string.md#class-string), path: [String](class_string.md#class-string)) [🔗](class_editorplugin.md#class-editorplugin-method-add-autoload-singleton)

Adds a script at `path` to the Autoload list as `name`.

---


<a id="class-editorplugin-method-add-context-menu-plugin"></a>

void **add_context_menu_plugin**(slot: [ContextMenuSlot](class_editorcontextmenuplugin.md#enum-editorcontextmenuplugin-contextmenuslot), plugin: [EditorContextMenuPlugin](class_editorcontextmenuplugin.md#class-editorcontextmenuplugin)) [🔗](class_editorplugin.md#class-editorplugin-method-add-context-menu-plugin)

Adds a plugin to the context menu. `slot` is the context menu where the plugin will be added.

**Note:** A plugin instance can belong only to a single context menu slot.

---


<a id="class-editorplugin-method-add-control-to-bottom-panel"></a>

[Button](class_button.md#class-button) **add_control_to_bottom_panel**(control: [Control](class_control.md#class-control), title: [String](class_string.md#class-string), shortcut: [Shortcut](class_shortcut.md#class-shortcut) = null) [🔗](class_editorplugin.md#class-editorplugin-method-add-control-to-bottom-panel)

**Deprecated:** Use [add_dock()](class_editorplugin.md#class-editorplugin-method-add-dock) instead, with [EditorDock.default_slot](class_editordock.md#class-editordock-property-default-slot) set to [DOCK_SLOT_BOTTOM](class_editorplugin.md#class-editorplugin-constant-dock-slot-bottom).

Adds a control to the bottom panel (together with Output, Debug, Animation, etc.). Returns a reference to a button that is outside the scene tree. It's up to you to hide/show the button when needed. When your plugin is deactivated, make sure to remove your custom control with [remove_control_from_bottom_panel()](class_editorplugin.md#class-editorplugin-method-remove-control-from-bottom-panel) and free it with [Node.queue_free()](class_node.md#class-node-method-queue-free).

`shortcut` is a shortcut that, when activated, will toggle the bottom panel's visibility. The shortcut object is only set when this control is added to the bottom panel.

**Note** See the default editor bottom panel shortcuts in the Editor Settings for inspiration. By convention, they all use `Alt` modifier.

---


<a id="class-editorplugin-method-add-control-to-container"></a>

void **add_control_to_container**(container: [CustomControlContainer](class_editorplugin.md#enum-editorplugin-customcontrolcontainer), control: [Control](class_control.md#class-control)) [🔗](class_editorplugin.md#class-editorplugin-method-add-control-to-container)

Adds a custom control to a container in the editor UI.

Please remember that you have to manage the visibility of your custom controls yourself (and likely hide it after adding it).

When your plugin is deactivated, make sure to remove your custom control with [remove_control_from_container()](class_editorplugin.md#class-editorplugin-method-remove-control-from-container) and free it with [Node.queue_free()](class_node.md#class-node-method-queue-free).

---


<a id="class-editorplugin-method-add-control-to-dock"></a>

void **add_control_to_dock**(slot: [DockSlot](class_editorplugin.md#enum-editorplugin-dockslot), control: [Control](class_control.md#class-control), shortcut: [Shortcut](class_shortcut.md#class-shortcut) = null) [🔗](class_editorplugin.md#class-editorplugin-method-add-control-to-dock)

**Deprecated:** Use [add_dock()](class_editorplugin.md#class-editorplugin-method-add-dock) instead.

Adds the control to a specific dock slot.

If the dock is repositioned and as long as the plugin is active, the editor will save the dock position on further sessions.

When your plugin is deactivated, make sure to remove your custom control with [remove_control_from_docks()](class_editorplugin.md#class-editorplugin-method-remove-control-from-docks) and free it with [Node.queue_free()](class_node.md#class-node-method-queue-free).

Optionally, you can specify a shortcut parameter. When pressed, this shortcut will open and focus the dock.

---


<a id="class-editorplugin-method-add-custom-type"></a>

void **add_custom_type**(type: [String](class_string.md#class-string), base: [String](class_string.md#class-string), script: [Script](class_script.md#class-script), icon: [Texture2D](class_texture2d.md#class-texture2d)) [🔗](class_editorplugin.md#class-editorplugin-method-add-custom-type)

Adds a custom type, which will appear in the list of nodes or resources.

When a given node or resource is selected, the base type will be instantiated (e.g. "Node3D", "Control", "Resource"), then the script will be loaded and set to this object.

**Note:** The base type is the base engine class which this type's class hierarchy inherits, not any custom type parent classes.

You can use the virtual method [_handles()](class_editorplugin.md#class-editorplugin-private-method-handles) to check if your custom object is being edited by checking the script or using the `is` keyword.

During run-time, this will be a simple object with a script so this function does not need to be called then.

**Note:** Custom types added this way are not true classes. They are just a helper to create a node with specific script.

---


<a id="class-editorplugin-method-add-debugger-plugin"></a>

void **add_debugger_plugin**(script: [EditorDebuggerPlugin](class_editordebuggerplugin.md#class-editordebuggerplugin)) [🔗](class_editorplugin.md#class-editorplugin-method-add-debugger-plugin)

Adds a [Script](class_script.md#class-script) as debugger plugin to the Debugger. The script must extend [EditorDebuggerPlugin](class_editordebuggerplugin.md#class-editordebuggerplugin).

---


<a id="class-editorplugin-method-add-dock"></a>

void **add_dock**(dock: [EditorDock](class_editordock.md#class-editordock)) [🔗](class_editorplugin.md#class-editorplugin-method-add-dock)

Adds a new dock.

When your plugin is deactivated, make sure to remove your custom dock with [remove_dock()](class_editorplugin.md#class-editorplugin-method-remove-dock) and free it with [Node.queue_free()](class_node.md#class-node-method-queue-free).

---


<a id="class-editorplugin-method-add-export-platform"></a>

void **add_export_platform**(platform: [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform)) [🔗](class_editorplugin.md#class-editorplugin-method-add-export-platform)

Registers a new [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform). Export platforms provides functionality of exporting to the specific platform.

---


<a id="class-editorplugin-method-add-export-plugin"></a>

void **add_export_plugin**(plugin: [EditorExportPlugin](class_editorexportplugin.md#class-editorexportplugin)) [🔗](class_editorplugin.md#class-editorplugin-method-add-export-plugin)

Registers a new [EditorExportPlugin](class_editorexportplugin.md#class-editorexportplugin). Export plugins are used to perform tasks when the project is being exported.

See [add_inspector_plugin()](class_editorplugin.md#class-editorplugin-method-add-inspector-plugin) for an example of how to register a plugin.

---


<a id="class-editorplugin-method-add-import-plugin"></a>

void **add_import_plugin**(importer: [EditorImportPlugin](class_editorimportplugin.md#class-editorimportplugin), first_priority: [bool](class_bool.md#class-bool) = false) [🔗](class_editorplugin.md#class-editorplugin-method-add-import-plugin)

Registers a new [EditorImportPlugin](class_editorimportplugin.md#class-editorimportplugin). Import plugins are used to import custom and unsupported assets as a custom [Resource](class_resource.md#class-resource) type.

If `first_priority` is `true`, the new import plugin is inserted first in the list and takes precedence over pre-existing plugins.

**Note:** If you want to import custom 3D asset formats use [add_scene_format_importer_plugin()](class_editorplugin.md#class-editorplugin-method-add-scene-format-importer-plugin) instead.

See [add_inspector_plugin()](class_editorplugin.md#class-editorplugin-method-add-inspector-plugin) for an example of how to register a plugin.

---


<a id="class-editorplugin-method-add-inspector-plugin"></a>

void **add_inspector_plugin**(plugin: [EditorInspectorPlugin](class_editorinspectorplugin.md#class-editorinspectorplugin)) [🔗](class_editorplugin.md#class-editorplugin-method-add-inspector-plugin)

Registers a new [EditorInspectorPlugin](class_editorinspectorplugin.md#class-editorinspectorplugin). Inspector plugins are used to extend [EditorInspector](class_editorinspector.md#class-editorinspector) and provide custom configuration tools for your object's properties.

**Note:** Always use [remove_inspector_plugin()](class_editorplugin.md#class-editorplugin-method-remove-inspector-plugin) to remove the registered [EditorInspectorPlugin](class_editorinspectorplugin.md#class-editorinspectorplugin) when your **EditorPlugin** is disabled to prevent leaks and an unexpected behavior.

```gdscript
const MyInspectorPlugin = preload("res://addons/your_addon/path/to/your/script.gd")
var inspector_plugin = MyInspectorPlugin.new()

func _enter_tree():
    add_inspector_plugin(inspector_plugin)

func _exit_tree():
    remove_inspector_plugin(inspector_plugin)
```

---


<a id="class-editorplugin-method-add-node-3d-gizmo-plugin"></a>

void **add_node_3d_gizmo_plugin**(plugin: [EditorNode3DGizmoPlugin](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin)) [🔗](class_editorplugin.md#class-editorplugin-method-add-node-3d-gizmo-plugin)

Registers a new [EditorNode3DGizmoPlugin](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin). Gizmo plugins are used to add custom gizmos to the 3D preview viewport for a [Node3D](class_node3d.md#class-node3d).

See [add_inspector_plugin()](class_editorplugin.md#class-editorplugin-method-add-inspector-plugin) for an example of how to register a plugin.

---


<a id="class-editorplugin-method-add-resource-conversion-plugin"></a>

void **add_resource_conversion_plugin**(plugin: [EditorResourceConversionPlugin](class_editorresourceconversionplugin.md#class-editorresourceconversionplugin)) [🔗](class_editorplugin.md#class-editorplugin-method-add-resource-conversion-plugin)

Registers a new [EditorResourceConversionPlugin](class_editorresourceconversionplugin.md#class-editorresourceconversionplugin). Resource conversion plugins are used to add custom resource converters to the editor inspector.

See [EditorResourceConversionPlugin](class_editorresourceconversionplugin.md#class-editorresourceconversionplugin) for an example of how to create a resource conversion plugin.

---


<a id="class-editorplugin-method-add-scene-format-importer-plugin"></a>

void **add_scene_format_importer_plugin**(scene_format_importer: [EditorSceneFormatImporter](class_editorsceneformatimporter.md#class-editorsceneformatimporter), first_priority: [bool](class_bool.md#class-bool) = false) [🔗](class_editorplugin.md#class-editorplugin-method-add-scene-format-importer-plugin)

Registers a new [EditorSceneFormatImporter](class_editorsceneformatimporter.md#class-editorsceneformatimporter). Scene importers are used to import custom 3D asset formats as scenes.

If `first_priority` is `true`, the new import plugin is inserted first in the list and takes precedence over pre-existing plugins.

---


<a id="class-editorplugin-method-add-scene-post-import-plugin"></a>

void **add_scene_post_import_plugin**(scene_import_plugin: [EditorScenePostImportPlugin](class_editorscenepostimportplugin.md#class-editorscenepostimportplugin), first_priority: [bool](class_bool.md#class-bool) = false) [🔗](class_editorplugin.md#class-editorplugin-method-add-scene-post-import-plugin)

Add an [EditorScenePostImportPlugin](class_editorscenepostimportplugin.md#class-editorscenepostimportplugin). These plugins allow customizing the import process of 3D assets by adding new options to the import dialogs.

If `first_priority` is `true`, the new import plugin is inserted first in the list and takes precedence over pre-existing plugins.

---


<a id="class-editorplugin-method-add-tool-menu-item"></a>

void **add_tool_menu_item**(name: [String](class_string.md#class-string), callable: [Callable](class_callable.md#class-callable)) [🔗](class_editorplugin.md#class-editorplugin-method-add-tool-menu-item)

Adds a custom menu item to **Project > Tools** named `name`. When clicked, the provided `callable` will be called.

---


<a id="class-editorplugin-method-add-tool-submenu-item"></a>

void **add_tool_submenu_item**(name: [String](class_string.md#class-string), submenu: [PopupMenu](class_popupmenu.md#class-popupmenu)) [🔗](class_editorplugin.md#class-editorplugin-method-add-tool-submenu-item)

Adds a custom [PopupMenu](class_popupmenu.md#class-popupmenu) submenu under **Project > Tools >** `name`. Use [remove_tool_menu_item()](class_editorplugin.md#class-editorplugin-method-remove-tool-menu-item) on plugin clean up to remove the menu.

---


<a id="class-editorplugin-method-add-translation-parser-plugin"></a>

void **add_translation_parser_plugin**(parser: [EditorTranslationParserPlugin](class_editortranslationparserplugin.md#class-editortranslationparserplugin)) [🔗](class_editorplugin.md#class-editorplugin-method-add-translation-parser-plugin)

Registers a custom translation parser plugin for extracting translatable strings from custom files.

---


<a id="class-editorplugin-method-add-undo-redo-inspector-hook-callback"></a>

void **add_undo_redo_inspector_hook_callback**(callable: [Callable](class_callable.md#class-callable)) [🔗](class_editorplugin.md#class-editorplugin-method-add-undo-redo-inspector-hook-callback)

Hooks a callback into the undo/redo action creation when a property is modified in the inspector. This allows, for example, to save other properties that may be lost when a given property is modified.

The callback should have 4 arguments: [Object](class_object.md#class-object) `undo_redo`, [Object](class_object.md#class-object) `modified_object`, [String](class_string.md#class-string) `property` and [Variant](class_variant.md#class-variant) `new_value`. They are, respectively, the [UndoRedo](class_undoredo.md#class-undoredo) object used by the inspector, the currently modified object, the name of the modified property and the new value the property is about to take.

---


<a id="class-editorplugin-method-get-editor-interface"></a>

[EditorInterface](class_editorinterface.md#class-editorinterface) **get_editor_interface**() [🔗](class_editorplugin.md#class-editorplugin-method-get-editor-interface)

**Deprecated:** [EditorInterface](class_editorinterface.md#class-editorinterface) is a global singleton and can be accessed directly by its name.

Returns the [EditorInterface](class_editorinterface.md#class-editorinterface) singleton instance.

---


<a id="class-editorplugin-method-get-export-as-menu"></a>

[PopupMenu](class_popupmenu.md#class-popupmenu) **get_export_as_menu**() [🔗](class_editorplugin.md#class-editorplugin-method-get-export-as-menu)

Returns the [PopupMenu](class_popupmenu.md#class-popupmenu) under **Scene > Export As...**.

---


<a id="class-editorplugin-method-get-plugin-version"></a>

[String](class_string.md#class-string) **get_plugin_version**() const [🔗](class_editorplugin.md#class-editorplugin-method-get-plugin-version)

Provide the version of the plugin declared in the `plugin.cfg` config file.

---


<a id="class-editorplugin-method-get-script-create-dialog"></a>

[ScriptCreateDialog](class_scriptcreatedialog.md#class-scriptcreatedialog) **get_script_create_dialog**() [🔗](class_editorplugin.md#class-editorplugin-method-get-script-create-dialog)

Gets the Editor's dialog used for making scripts.

**Note:** Users can configure it before use.

**Warning:** Removing and freeing this node will render a part of the editor useless and may cause a crash.

---


<a id="class-editorplugin-method-get-undo-redo"></a>

[EditorUndoRedoManager](class_editorundoredomanager.md#class-editorundoredomanager) **get_undo_redo**() [🔗](class_editorplugin.md#class-editorplugin-method-get-undo-redo)

Gets the undo/redo object. Most actions in the editor can be undoable, so use this object to make sure this happens when it's worth it.

---


<a id="class-editorplugin-method-hide-bottom-panel"></a>

void **hide_bottom_panel**() [🔗](class_editorplugin.md#class-editorplugin-method-hide-bottom-panel)

Minimizes the bottom panel.

---


<a id="class-editorplugin-method-make-bottom-panel-item-visible"></a>

void **make_bottom_panel_item_visible**(item: [Control](class_control.md#class-control)) [🔗](class_editorplugin.md#class-editorplugin-method-make-bottom-panel-item-visible)

Makes a specific item in the bottom panel visible.

---


<a id="class-editorplugin-method-queue-save-layout"></a>

void **queue_save_layout**() [🔗](class_editorplugin.md#class-editorplugin-method-queue-save-layout)

Queue save the project's editor layout.

---


<a id="class-editorplugin-method-remove-autoload-singleton"></a>

void **remove_autoload_singleton**(name: [String](class_string.md#class-string)) [🔗](class_editorplugin.md#class-editorplugin-method-remove-autoload-singleton)

Removes an Autoload `name` from the list.

---


<a id="class-editorplugin-method-remove-context-menu-plugin"></a>

void **remove_context_menu_plugin**(plugin: [EditorContextMenuPlugin](class_editorcontextmenuplugin.md#class-editorcontextmenuplugin)) [🔗](class_editorplugin.md#class-editorplugin-method-remove-context-menu-plugin)

Removes the specified context menu plugin.

---


<a id="class-editorplugin-method-remove-control-from-bottom-panel"></a>

void **remove_control_from_bottom_panel**(control: [Control](class_control.md#class-control)) [🔗](class_editorplugin.md#class-editorplugin-method-remove-control-from-bottom-panel)

**Deprecated:** Use [remove_dock()](class_editorplugin.md#class-editorplugin-method-remove-dock) instead.

Removes the control from the bottom panel. You have to manually [Node.queue_free()](class_node.md#class-node-method-queue-free) the control.

---


<a id="class-editorplugin-method-remove-control-from-container"></a>

void **remove_control_from_container**(container: [CustomControlContainer](class_editorplugin.md#enum-editorplugin-customcontrolcontainer), control: [Control](class_control.md#class-control)) [🔗](class_editorplugin.md#class-editorplugin-method-remove-control-from-container)

Removes the control from the specified container. You have to manually [Node.queue_free()](class_node.md#class-node-method-queue-free) the control.

---


<a id="class-editorplugin-method-remove-control-from-docks"></a>

void **remove_control_from_docks**(control: [Control](class_control.md#class-control)) [🔗](class_editorplugin.md#class-editorplugin-method-remove-control-from-docks)

**Deprecated:** Use [remove_dock()](class_editorplugin.md#class-editorplugin-method-remove-dock) instead.

Removes the control from the dock. You have to manually [Node.queue_free()](class_node.md#class-node-method-queue-free) the control.

---


<a id="class-editorplugin-method-remove-custom-type"></a>

void **remove_custom_type**(type: [String](class_string.md#class-string)) [🔗](class_editorplugin.md#class-editorplugin-method-remove-custom-type)

Removes a custom type added by [add_custom_type()](class_editorplugin.md#class-editorplugin-method-add-custom-type).

---


<a id="class-editorplugin-method-remove-debugger-plugin"></a>

void **remove_debugger_plugin**(script: [EditorDebuggerPlugin](class_editordebuggerplugin.md#class-editordebuggerplugin)) [🔗](class_editorplugin.md#class-editorplugin-method-remove-debugger-plugin)

Removes the debugger plugin with given script from the Debugger.

---


<a id="class-editorplugin-method-remove-dock"></a>

void **remove_dock**(dock: [EditorDock](class_editordock.md#class-editordock)) [🔗](class_editorplugin.md#class-editorplugin-method-remove-dock)

Removes `dock` from the available docks. You should manually call [Node.queue_free()](class_node.md#class-node-method-queue-free) to free it.

---


<a id="class-editorplugin-method-remove-export-platform"></a>

void **remove_export_platform**(platform: [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform)) [🔗](class_editorplugin.md#class-editorplugin-method-remove-export-platform)

Removes an export platform registered by [add_export_platform()](class_editorplugin.md#class-editorplugin-method-add-export-platform).

---


<a id="class-editorplugin-method-remove-export-plugin"></a>

void **remove_export_plugin**(plugin: [EditorExportPlugin](class_editorexportplugin.md#class-editorexportplugin)) [🔗](class_editorplugin.md#class-editorplugin-method-remove-export-plugin)

Removes an export plugin registered by [add_export_plugin()](class_editorplugin.md#class-editorplugin-method-add-export-plugin).

---


<a id="class-editorplugin-method-remove-import-plugin"></a>

void **remove_import_plugin**(importer: [EditorImportPlugin](class_editorimportplugin.md#class-editorimportplugin)) [🔗](class_editorplugin.md#class-editorplugin-method-remove-import-plugin)

Removes an import plugin registered by [add_import_plugin()](class_editorplugin.md#class-editorplugin-method-add-import-plugin).

---


<a id="class-editorplugin-method-remove-inspector-plugin"></a>

void **remove_inspector_plugin**(plugin: [EditorInspectorPlugin](class_editorinspectorplugin.md#class-editorinspectorplugin)) [🔗](class_editorplugin.md#class-editorplugin-method-remove-inspector-plugin)

Removes an inspector plugin registered by [add_inspector_plugin()](class_editorplugin.md#class-editorplugin-method-add-inspector-plugin).

---


<a id="class-editorplugin-method-remove-node-3d-gizmo-plugin"></a>

void **remove_node_3d_gizmo_plugin**(plugin: [EditorNode3DGizmoPlugin](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin)) [🔗](class_editorplugin.md#class-editorplugin-method-remove-node-3d-gizmo-plugin)

Removes a gizmo plugin registered by [add_node_3d_gizmo_plugin()](class_editorplugin.md#class-editorplugin-method-add-node-3d-gizmo-plugin).

---


<a id="class-editorplugin-method-remove-resource-conversion-plugin"></a>

void **remove_resource_conversion_plugin**(plugin: [EditorResourceConversionPlugin](class_editorresourceconversionplugin.md#class-editorresourceconversionplugin)) [🔗](class_editorplugin.md#class-editorplugin-method-remove-resource-conversion-plugin)

Removes a resource conversion plugin registered by [add_resource_conversion_plugin()](class_editorplugin.md#class-editorplugin-method-add-resource-conversion-plugin).

---


<a id="class-editorplugin-method-remove-scene-format-importer-plugin"></a>

void **remove_scene_format_importer_plugin**(scene_format_importer: [EditorSceneFormatImporter](class_editorsceneformatimporter.md#class-editorsceneformatimporter)) [🔗](class_editorplugin.md#class-editorplugin-method-remove-scene-format-importer-plugin)

Removes a scene format importer registered by [add_scene_format_importer_plugin()](class_editorplugin.md#class-editorplugin-method-add-scene-format-importer-plugin).

---


<a id="class-editorplugin-method-remove-scene-post-import-plugin"></a>

void **remove_scene_post_import_plugin**(scene_import_plugin: [EditorScenePostImportPlugin](class_editorscenepostimportplugin.md#class-editorscenepostimportplugin)) [🔗](class_editorplugin.md#class-editorplugin-method-remove-scene-post-import-plugin)

Remove the [EditorScenePostImportPlugin](class_editorscenepostimportplugin.md#class-editorscenepostimportplugin), added with [add_scene_post_import_plugin()](class_editorplugin.md#class-editorplugin-method-add-scene-post-import-plugin).

---


<a id="class-editorplugin-method-remove-tool-menu-item"></a>

void **remove_tool_menu_item**(name: [String](class_string.md#class-string)) [🔗](class_editorplugin.md#class-editorplugin-method-remove-tool-menu-item)

Removes a menu `name` from **Project > Tools**.

---


<a id="class-editorplugin-method-remove-translation-parser-plugin"></a>

void **remove_translation_parser_plugin**(parser: [EditorTranslationParserPlugin](class_editortranslationparserplugin.md#class-editortranslationparserplugin)) [🔗](class_editorplugin.md#class-editorplugin-method-remove-translation-parser-plugin)

Removes a custom translation parser plugin registered by [add_translation_parser_plugin()](class_editorplugin.md#class-editorplugin-method-add-translation-parser-plugin).

---


<a id="class-editorplugin-method-remove-undo-redo-inspector-hook-callback"></a>

void **remove_undo_redo_inspector_hook_callback**(callable: [Callable](class_callable.md#class-callable)) [🔗](class_editorplugin.md#class-editorplugin-method-remove-undo-redo-inspector-hook-callback)

Removes a callback previously added by [add_undo_redo_inspector_hook_callback()](class_editorplugin.md#class-editorplugin-method-add-undo-redo-inspector-hook-callback).

---


<a id="class-editorplugin-method-set-dock-tab-icon"></a>

void **set_dock_tab_icon**(control: [Control](class_control.md#class-control), icon: [Texture2D](class_texture2d.md#class-texture2d)) [🔗](class_editorplugin.md#class-editorplugin-method-set-dock-tab-icon)

**Deprecated:** Use [EditorDock.dock_icon](class_editordock.md#class-editordock-property-dock-icon) instead.

Sets the tab icon for the given control in a dock slot. Setting to `null` removes the icon.

---


<a id="class-editorplugin-method-set-force-draw-over-forwarding-enabled"></a>

void **set_force_draw_over_forwarding_enabled**() [🔗](class_editorplugin.md#class-editorplugin-method-set-force-draw-over-forwarding-enabled)

Enables calling of [_forward_canvas_force_draw_over_viewport()](class_editorplugin.md#class-editorplugin-private-method-forward-canvas-force-draw-over-viewport) for the 2D editor and [_forward_3d_force_draw_over_viewport()](class_editorplugin.md#class-editorplugin-private-method-forward-3d-force-draw-over-viewport) for the 3D editor when their viewports are updated. You need to call this method only once and it will work permanently for this plugin.

---


<a id="class-editorplugin-method-set-input-event-forwarding-always-enabled"></a>

void **set_input_event_forwarding_always_enabled**() [🔗](class_editorplugin.md#class-editorplugin-method-set-input-event-forwarding-always-enabled)

Use this method if you always want to receive inputs from 3D view screen inside [_forward_3d_gui_input()](class_editorplugin.md#class-editorplugin-private-method-forward-3d-gui-input). It might be especially usable if your plugin will want to use raycast in the scene.

---


<a id="class-editorplugin-method-update-overlays"></a>

[int](class_int.md#class-int) **update_overlays**() const [🔗](class_editorplugin.md#class-editorplugin-method-update-overlays)

Updates the overlays of the 2D and 3D editor viewport. Causes methods [_forward_canvas_draw_over_viewport()](class_editorplugin.md#class-editorplugin-private-method-forward-canvas-draw-over-viewport), [_forward_canvas_force_draw_over_viewport()](class_editorplugin.md#class-editorplugin-private-method-forward-canvas-force-draw-over-viewport), [_forward_3d_draw_over_viewport()](class_editorplugin.md#class-editorplugin-private-method-forward-3d-draw-over-viewport) and [_forward_3d_force_draw_over_viewport()](class_editorplugin.md#class-editorplugin-private-method-forward-3d-force-draw-over-viewport) to be called.
