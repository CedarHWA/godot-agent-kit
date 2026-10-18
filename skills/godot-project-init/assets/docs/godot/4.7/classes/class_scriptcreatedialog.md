> Source: https://docs.godotengine.org/en/4.7/classes/class_scriptcreatedialog.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="scriptcreatedialog"></a>

<a id="class-scriptcreatedialog"></a>

# ScriptCreateDialog

**Inherits:** [ConfirmationDialog](class_confirmationdialog.md#class-confirmationdialog) **<** [AcceptDialog](class_acceptdialog.md#class-acceptdialog) **<** [Window](class_window.md#class-window) **<** [Viewport](class_viewport.md#class-viewport) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Godot editor's popup dialog for creating new [Script](class_script.md#class-script) files.

<a id="description"></a>

## Description

The **ScriptCreateDialog** creates script files according to a given template for a given scripting language. The standard use is to configure its fields prior to calling one of the [Window.popup()](class_window.md#class-window-method-popup) methods.

```gdscript
func _ready():
    var dialog = ScriptCreateDialog.new();
    dialog.config("Node", "res://new_node.gd") # For in-engine types.
    dialog.config("\"res://base_node.gd\"", "res://derived_node.gd") # For script types.
    dialog.popup_centered()
```

```csharp
public override void _Ready()
{
    var dialog = new ScriptCreateDialog();
    dialog.Config("Node", "res://NewNode.cs"); // For in-engine types.
    dialog.Config("\"res://BaseNode.cs\"", "res://DerivedNode.cs"); // For script types.
    dialog.PopupCentered();
}
```

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | dialog_hide_on_ok | `false` (overrides [AcceptDialog](class_acceptdialog.md#class-acceptdialog-property-dialog-hide-on-ok)) |
| [String](class_string.md#class-string) | ok_button_text | `"Create"` (overrides [AcceptDialog](class_acceptdialog.md#class-acceptdialog-property-ok-button-text)) |
| [String](class_string.md#class-string) | title | `"Attach Node Script"` (overrides [Window](class_window.md#class-window-property-title)) |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [config](class_scriptcreatedialog.md#class-scriptcreatedialog-method-config)(inherits: [String](class_string.md#class-string), path: [String](class_string.md#class-string), built_in_enabled: [bool](class_bool.md#class-bool) = true, load_enabled: [bool](class_bool.md#class-bool) = true) |

---


<a id="signals"></a>

## Signals

<a id="class-scriptcreatedialog-signal-script-created"></a>

**script_created**(script: [Script](class_script.md#class-script)) [🔗](class_scriptcreatedialog.md#class-scriptcreatedialog-signal-script-created)

Emitted when the user clicks the OK button.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-scriptcreatedialog-method-config"></a>

void **config**(inherits: [String](class_string.md#class-string), path: [String](class_string.md#class-string), built_in_enabled: [bool](class_bool.md#class-bool) = true, load_enabled: [bool](class_bool.md#class-bool) = true) [🔗](class_scriptcreatedialog.md#class-scriptcreatedialog-method-config)

Prefills required fields to configure the ScriptCreateDialog for use.
