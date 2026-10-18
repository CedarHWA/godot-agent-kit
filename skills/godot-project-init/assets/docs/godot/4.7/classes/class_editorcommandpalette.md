> Source: https://docs.godotengine.org/en/4.7/classes/class_editorcommandpalette.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="editorcommandpalette"></a>

<a id="class-editorcommandpalette"></a>

# EditorCommandPalette

**Inherits:** [ConfirmationDialog](class_confirmationdialog.md#class-confirmationdialog) **<** [AcceptDialog](class_acceptdialog.md#class-acceptdialog) **<** [Window](class_window.md#class-window) **<** [Viewport](class_viewport.md#class-viewport) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Godot editor's command palette.

<a id="description"></a>

## Description

Object that holds all the available Commands and their shortcuts text. These Commands can be accessed through **Editor > Command Palette** menu.

Command key names use slash delimiters to distinguish sections, for example: `"example/command1"` then `example` will be the section name.

```gdscript
var command_palette = EditorInterface.get_command_palette()
# external_command is a function that will be called with the command is executed.
var command_callable = Callable(self, "external_command").bind(arguments)
command_palette.add_command("command", "test/command",command_callable)
```

```csharp
EditorCommandPalette commandPalette = EditorInterface.Singleton.GetCommandPalette();
// ExternalCommand is a function that will be called with the command is executed.
Callable commandCallable = new Callable(this, MethodName.ExternalCommand);
commandPalette.AddCommand("command", "test/command", commandCallable)
```

**Note:** This class shouldn't be instantiated directly. Instead, access the singleton using [EditorInterface.get_command_palette()](class_editorinterface.md#class-editorinterface-method-get-command-palette).

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_command](class_editorcommandpalette.md#class-editorcommandpalette-method-add-command)(command_name: [String](class_string.md#class-string), key_name: [String](class_string.md#class-string), binded_callable: [Callable](class_callable.md#class-callable), shortcut_text: [String](class_string.md#class-string) = "None") |
| void | [remove_command](class_editorcommandpalette.md#class-editorcommandpalette-method-remove-command)(key_name: [String](class_string.md#class-string)) |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-editorcommandpalette-method-add-command"></a>

void **add_command**(command_name: [String](class_string.md#class-string), key_name: [String](class_string.md#class-string), binded_callable: [Callable](class_callable.md#class-callable), shortcut_text: [String](class_string.md#class-string) = "None") [🔗](class_editorcommandpalette.md#class-editorcommandpalette-method-add-command)

Adds a custom command to EditorCommandPalette.

- `command_name`: [String](class_string.md#class-string) (Name of the **Command**. This is displayed to the user.)
- `key_name`: [String](class_string.md#class-string) (Name of the key for a particular **Command**. This is used to uniquely identify the **Command**.)
- `binded_callable`: [Callable](class_callable.md#class-callable) (Callable of the **Command**. This will be executed when the **Command** is selected.)
- `shortcut_text`: [String](class_string.md#class-string) (Shortcut text of the **Command** if available.)

---


<a id="class-editorcommandpalette-method-remove-command"></a>

void **remove_command**(key_name: [String](class_string.md#class-string)) [🔗](class_editorcommandpalette.md#class-editorcommandpalette-method-remove-command)

Removes the custom command from EditorCommandPalette.

- `key_name`: [String](class_string.md#class-string) (Name of the key for a particular **Command**.)
