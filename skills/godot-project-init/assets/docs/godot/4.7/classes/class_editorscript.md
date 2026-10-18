> Source: https://docs.godotengine.org/en/4.7/classes/class_editorscript.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="editorscript"></a>

<a id="class-editorscript"></a>

# EditorScript

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Base script that can be used to add extension functions to the editor.

<a id="description"></a>

## Description

Scripts extending this class and implementing its [_run()](class_editorscript.md#class-editorscript-private-method-run) method can be executed from the Script Editor's **File > Run** menu option (or by pressing `Ctrl + Shift + X`) while the editor is running. This is useful for adding custom in-editor functionality to Godot. For more complex additions, consider using [EditorPlugin](class_editorplugin.md#class-editorplugin)s instead.

If a script extending this class also has a global class name, it will be included in the editor's command palette.

**Note:** Extending scripts need to have `tool` mode enabled.

**Example:** Running the following script prints "Hello from the Godot Editor!":

```gdscript
@tool
extends EditorScript

func _run():
    print("Hello from the Godot Editor!")
```

```csharp
using Godot;

[Tool]
public partial class HelloEditor : EditorScript
{
    public override void _Run()
    {
        GD.Print("Hello from the Godot Editor!");
    }
}
```

**Note:** EditorScript is [RefCounted](class_refcounted.md#class-refcounted), meaning it is destroyed when nothing references it. This can cause errors during asynchronous operations if there are no references to the script.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [_run](class_editorscript.md#class-editorscript-private-method-run)() virtual required |
| void | [add_root_node](class_editorscript.md#class-editorscript-method-add-root-node)(node: [Node](class_node.md#class-node)) |
| [EditorInterface](class_editorinterface.md#class-editorinterface) | [get_editor_interface](class_editorscript.md#class-editorscript-method-get-editor-interface)() const |
| [Node](class_node.md#class-node) | [get_scene](class_editorscript.md#class-editorscript-method-get-scene)() const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-editorscript-private-method-run"></a>

void **_run**() virtual required [🔗](class_editorscript.md#class-editorscript-private-method-run)

This method is executed by the Editor when **File > Run** is used.

---


<a id="class-editorscript-method-add-root-node"></a>

void **add_root_node**(node: [Node](class_node.md#class-node)) [🔗](class_editorscript.md#class-editorscript-method-add-root-node)

**Deprecated:** Use [EditorInterface.add_root_node()](class_editorinterface.md#class-editorinterface-method-add-root-node) instead.

Makes `node` root of the currently opened scene. Only works if the scene is empty. If the `node` is a scene instance, an inheriting scene will be created.

---


<a id="class-editorscript-method-get-editor-interface"></a>

[EditorInterface](class_editorinterface.md#class-editorinterface) **get_editor_interface**() const [🔗](class_editorscript.md#class-editorscript-method-get-editor-interface)

**Deprecated:** [EditorInterface](class_editorinterface.md#class-editorinterface) is a global singleton and can be accessed directly by its name.

Returns the [EditorInterface](class_editorinterface.md#class-editorinterface) singleton instance.

---


<a id="class-editorscript-method-get-scene"></a>

[Node](class_node.md#class-node) **get_scene**() const [🔗](class_editorscript.md#class-editorscript-method-get-scene)

**Deprecated:** Use [EditorInterface.get_edited_scene_root()](class_editorinterface.md#class-editorinterface-method-get-edited-scene-root) instead.

Returns the edited (current) scene's root [Node](class_node.md#class-node). Equivalent of [EditorInterface.get_edited_scene_root()](class_editorinterface.md#class-editorinterface-method-get-edited-scene-root).
