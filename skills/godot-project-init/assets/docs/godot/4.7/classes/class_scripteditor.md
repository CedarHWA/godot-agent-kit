> Source: https://docs.godotengine.org/en/4.7/classes/class_scripteditor.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="scripteditor"></a>

<a id="class-scripteditor"></a>

# ScriptEditor

**Inherits:** [PanelContainer](class_panelcontainer.md#class-panelcontainer) **<** [Container](class_container.md#class-container) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Godot editor's script editor.

<a id="description"></a>

## Description

Godot editor's script editor.

**Note:** This class shouldn't be instantiated directly. Instead, access the singleton using [EditorInterface.get_script_editor()](class_editorinterface.md#class-editorinterface-method-get-script-editor).

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [clear_docs_from_script](class_scripteditor.md#class-scripteditor-method-clear-docs-from-script)(script: [Script](class_script.md#class-script)) |
| [Error](class_@globalscope.md#enum-globalscope-error) | [close_file](class_scripteditor.md#class-scripteditor-method-close-file)(path: [String](class_string.md#class-string)) |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [get_breakpoints](class_scripteditor.md#class-scripteditor-method-get-breakpoints)() |
| [ScriptEditorBase](class_scripteditorbase.md#class-scripteditorbase) | [get_current_editor](class_scripteditor.md#class-scripteditor-method-get-current-editor)() const |
| [Script](class_script.md#class-script) | [get_current_script](class_scripteditor.md#class-scripteditor-method-get-current-script)() |
| [Array](class_array.md#class-array)[[ScriptEditorBase](class_scripteditorbase.md#class-scripteditorbase)] | [get_open_script_editors](class_scripteditor.md#class-scripteditor-method-get-open-script-editors)() const |
| [Array](class_array.md#class-array)[[Script](class_script.md#class-script)] | [get_open_scripts](class_scripteditor.md#class-scripteditor-method-get-open-scripts)() const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [get_unsaved_files](class_scripteditor.md#class-scripteditor-method-get-unsaved-files)() const |
| void | [goto_help](class_scripteditor.md#class-scripteditor-method-goto-help)(topic: [String](class_string.md#class-string)) |
| void | [goto_line](class_scripteditor.md#class-scripteditor-method-goto-line)(line_number: [int](class_int.md#class-int)) |
| void | [open_script_create_dialog](class_scripteditor.md#class-scripteditor-method-open-script-create-dialog)(base_name: [String](class_string.md#class-string), base_path: [String](class_string.md#class-string)) |
| void | [register_syntax_highlighter](class_scripteditor.md#class-scripteditor-method-register-syntax-highlighter)(syntax_highlighter: [EditorSyntaxHighlighter](class_editorsyntaxhighlighter.md#class-editorsyntaxhighlighter)) |
| void | [reload_open_files](class_scripteditor.md#class-scripteditor-method-reload-open-files)() |
| void | [save_all_scripts](class_scripteditor.md#class-scripteditor-method-save-all-scripts)() |
| void | [unregister_syntax_highlighter](class_scripteditor.md#class-scripteditor-method-unregister-syntax-highlighter)(syntax_highlighter: [EditorSyntaxHighlighter](class_editorsyntaxhighlighter.md#class-editorsyntaxhighlighter)) |
| void | [update_docs_from_script](class_scripteditor.md#class-scripteditor-method-update-docs-from-script)(script: [Script](class_script.md#class-script)) |

---


<a id="signals"></a>

## Signals

<a id="class-scripteditor-signal-editor-script-changed"></a>

**editor_script_changed**(script: [Script](class_script.md#class-script)) [🔗](class_scripteditor.md#class-scripteditor-signal-editor-script-changed)

Emitted when user changed active script. Argument is a freshly activated [Script](class_script.md#class-script).

---


<a id="class-scripteditor-signal-script-close"></a>

**script_close**(script: [Script](class_script.md#class-script)) [🔗](class_scripteditor.md#class-scripteditor-signal-script-close)

Emitted when editor is about to close the active script. Argument is a [Script](class_script.md#class-script) that is going to be closed.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-scripteditor-method-clear-docs-from-script"></a>

void **clear_docs_from_script**(script: [Script](class_script.md#class-script)) [🔗](class_scripteditor.md#class-scripteditor-method-clear-docs-from-script)

Removes the documentation for the given `script`.

**Note:** This should be called whenever the script is changed to keep the open documentation state up to date.

---


<a id="class-scripteditor-method-close-file"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **close_file**(path: [String](class_string.md#class-string)) [🔗](class_scripteditor.md#class-scripteditor-method-close-file)

Closes the file at the given `path`, discarding any unsaved changes.

Returns [@GlobalScope.OK](class_@globalscope.md#class-globalscope-constant-ok) on success or [@GlobalScope.ERR_FILE_NOT_FOUND](class_@globalscope.md#class-globalscope-constant-err-file-not-found) if the file is not found.

---


<a id="class-scripteditor-method-get-breakpoints"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_breakpoints**() [🔗](class_scripteditor.md#class-scripteditor-method-get-breakpoints)

Returns array of breakpoints.

---


<a id="class-scripteditor-method-get-current-editor"></a>

[ScriptEditorBase](class_scripteditorbase.md#class-scripteditorbase) **get_current_editor**() const [🔗](class_scripteditor.md#class-scripteditor-method-get-current-editor)

Returns the [ScriptEditorBase](class_scripteditorbase.md#class-scripteditorbase) object that the user is currently editing.

---


<a id="class-scripteditor-method-get-current-script"></a>

[Script](class_script.md#class-script) **get_current_script**() [🔗](class_scripteditor.md#class-scripteditor-method-get-current-script)

Returns a [Script](class_script.md#class-script) that is currently active in editor.

---


<a id="class-scripteditor-method-get-open-script-editors"></a>

[Array](class_array.md#class-array)[[ScriptEditorBase](class_scripteditorbase.md#class-scripteditorbase)] **get_open_script_editors**() const [🔗](class_scripteditor.md#class-scripteditor-method-get-open-script-editors)

Returns an array with all [ScriptEditorBase](class_scripteditorbase.md#class-scripteditorbase) objects which are currently open in editor.

---


<a id="class-scripteditor-method-get-open-scripts"></a>

[Array](class_array.md#class-array)[[Script](class_script.md#class-script)] **get_open_scripts**() const [🔗](class_scripteditor.md#class-scripteditor-method-get-open-scripts)

Returns an array with all [Script](class_script.md#class-script) objects which are currently open in editor.

---


<a id="class-scripteditor-method-get-unsaved-files"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_unsaved_files**() const [🔗](class_scripteditor.md#class-scripteditor-method-get-unsaved-files)

Returns an array of file paths of scripts with unsaved changes open in the editor.

---


<a id="class-scripteditor-method-goto-help"></a>

void **goto_help**(topic: [String](class_string.md#class-string)) [🔗](class_scripteditor.md#class-scripteditor-method-goto-help)

Opens help for the given topic. The `topic` is an encoded string that controls which class, method, constant, signal, annotation, property, or theme item should be focused.

The supported `topic` formats include `class_name:class`, `class_method:class:method`, `class_constant:class:constant`, `class_signal:class:signal`, `class_annotation:class:@annotation`, `class_property:class:property`, and `class_theme_item:class:item`, where `class` is the class name, `method` is the method name, `constant` is the constant name, `signal` is the signal name, `annotation` is the annotation name, `property` is the property name, and `item` is the theme item.

```gdscript
# Shows help for the Node class.
class_name:Node
# Shows help for the global min function.
# Global objects are accessible in the `@GlobalScope` namespace, shown here.
class_method:@GlobalScope:min
# Shows help for get_viewport in the Node class.
class_method:Node:get_viewport
# Shows help for the Input constant MOUSE_BUTTON_MIDDLE.
class_constant:Input:MOUSE_BUTTON_MIDDLE
# Shows help for the BaseButton signal pressed.
class_signal:BaseButton:pressed
# Shows help for the CanvasItem property visible.
class_property:CanvasItem:visible
# Shows help for the GDScript annotation export.
# Annotations should be prefixed with the `@` symbol in the descriptor, as shown here.
class_annotation:@GDScript:@export
# Shows help for the GraphNode theme item named panel_selected.
class_theme_item:GraphNode:panel_selected
```

---


<a id="class-scripteditor-method-goto-line"></a>

void **goto_line**(line_number: [int](class_int.md#class-int)) [🔗](class_scripteditor.md#class-scripteditor-method-goto-line)

Goes to the specified line in the current script.

---


<a id="class-scripteditor-method-open-script-create-dialog"></a>

void **open_script_create_dialog**(base_name: [String](class_string.md#class-string), base_path: [String](class_string.md#class-string)) [🔗](class_scripteditor.md#class-scripteditor-method-open-script-create-dialog)

Opens the script create dialog. The script will extend `base_name`. The file extension can be omitted from `base_path`. It will be added based on the selected scripting language.

---


<a id="class-scripteditor-method-register-syntax-highlighter"></a>

void **register_syntax_highlighter**(syntax_highlighter: [EditorSyntaxHighlighter](class_editorsyntaxhighlighter.md#class-editorsyntaxhighlighter)) [🔗](class_scripteditor.md#class-scripteditor-method-register-syntax-highlighter)

Registers the [EditorSyntaxHighlighter](class_editorsyntaxhighlighter.md#class-editorsyntaxhighlighter) to the editor, the [EditorSyntaxHighlighter](class_editorsyntaxhighlighter.md#class-editorsyntaxhighlighter) will be available on all open scripts.

**Note:** Does not apply to scripts that are already opened.

---


<a id="class-scripteditor-method-reload-open-files"></a>

void **reload_open_files**() [🔗](class_scripteditor.md#class-scripteditor-method-reload-open-files)

Reloads all currently opened files. This should be used when opened files are changed outside of the script editor. The user may be prompted to resolve file conflicts, see [EditorSettings.text_editor/behavior/files/auto_reload_scripts_on_external_change](class_editorsettings.md#class-editorsettings-property-text-editor-behavior-files-auto-reload-scripts-on-external-change).

---


<a id="class-scripteditor-method-save-all-scripts"></a>

void **save_all_scripts**() [🔗](class_scripteditor.md#class-scripteditor-method-save-all-scripts)

Saves all open scripts.

---


<a id="class-scripteditor-method-unregister-syntax-highlighter"></a>

void **unregister_syntax_highlighter**(syntax_highlighter: [EditorSyntaxHighlighter](class_editorsyntaxhighlighter.md#class-editorsyntaxhighlighter)) [🔗](class_scripteditor.md#class-scripteditor-method-unregister-syntax-highlighter)

Unregisters the [EditorSyntaxHighlighter](class_editorsyntaxhighlighter.md#class-editorsyntaxhighlighter) from the editor.

**Note:** The [EditorSyntaxHighlighter](class_editorsyntaxhighlighter.md#class-editorsyntaxhighlighter) will still be applied to scripts that are already opened.

---


<a id="class-scripteditor-method-update-docs-from-script"></a>

void **update_docs_from_script**(script: [Script](class_script.md#class-script)) [🔗](class_scripteditor.md#class-scripteditor-method-update-docs-from-script)

Updates the documentation for the given `script`.

**Note:** This should be called whenever the script is changed to keep the open documentation state up to date.
