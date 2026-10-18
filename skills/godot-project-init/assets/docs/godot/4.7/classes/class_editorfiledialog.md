> Source: https://docs.godotengine.org/en/4.7/classes/class_editorfiledialog.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="editorfiledialog"></a>

<a id="class-editorfiledialog"></a>

# EditorFileDialog

**Inherits:** [FileDialog](class_filedialog.md#class-filedialog) **<** [ConfirmationDialog](class_confirmationdialog.md#class-confirmationdialog) **<** [AcceptDialog](class_acceptdialog.md#class-acceptdialog) **<** [Window](class_window.md#class-window) **<** [Viewport](class_viewport.md#class-viewport) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A modified version of [FileDialog](class_filedialog.md#class-filedialog) used by the editor.

<a id="description"></a>

## Description

**EditorFileDialog** is a [FileDialog](class_filedialog.md#class-filedialog) tweaked to work in the editor. It automatically handles favorite and recent directory lists, and synchronizes some properties with their corresponding editor settings.

**EditorFileDialog** will automatically show a native dialog based on the [EditorSettings.interface/editor/appearance/use_native_file_dialogs](class_editorsettings.md#class-editorsettings-property-interface-editor-appearance-use-native-file-dialogs) editor setting and ignores [FileDialog.use_native_dialog](class_filedialog.md#class-filedialog-property-use-native-dialog).

**Note:** **EditorFileDialog** is invisible by default. To make it visible, call one of the `popup_*` methods from [Window](class_window.md#class-window) on the node, such as [Window.popup_centered_clamped()](class_window.md#class-window-method-popup-centered-clamped).

**Note:** On Linux and macOS, sandboxed apps always use native dialogs to access the host file system.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [disable_overwrite_warning](class_editorfiledialog.md#class-editorfiledialog-property-disable-overwrite-warning) | `false` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_side_menu](class_editorfiledialog.md#class-editorfiledialog-method-add-side-menu)(menu: [Control](class_control.md#class-control), title: [String](class_string.md#class-string) = "") |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-editorfiledialog-property-disable-overwrite-warning"></a>

[bool](class_bool.md#class-bool) **disable_overwrite_warning** = `false` [🔗](class_editorfiledialog.md#class-editorfiledialog-property-disable-overwrite-warning)

- void **set_disable_overwrite_warning**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_overwrite_warning_disabled**()

**Deprecated:** Use [FileDialog.overwrite_warning_enabled](class_filedialog.md#class-filedialog-property-overwrite-warning-enabled) instead.

If `true`, the **EditorFileDialog** will not warn the user before overwriting files.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-editorfiledialog-method-add-side-menu"></a>

void **add_side_menu**(menu: [Control](class_control.md#class-control), title: [String](class_string.md#class-string) = "") [🔗](class_editorfiledialog.md#class-editorfiledialog-method-add-side-menu)

**Deprecated:** This feature is no longer supported.

This method is kept for compatibility and does nothing. As an alternative, you can display another dialog after showing the file dialog.
