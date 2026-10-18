> Source: https://docs.godotengine.org/en/4.7/classes/class_editorscenepostimport.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="editorscenepostimport"></a>

<a id="class-editorscenepostimport"></a>

# EditorScenePostImport

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Post-processes scenes after import.

<a id="description"></a>

## Description

Imported scenes can be automatically modified right after import by setting their **Custom Script** Import property to a `tool` script that inherits from this class.

The [_post_import()](class_editorscenepostimport.md#class-editorscenepostimport-private-method-post-import) callback receives the imported scene's root node and returns the modified version of the scene:

```gdscript
@tool # Needed so it runs in editor.
extends EditorScenePostImport

# This sample changes all node names.
# Called right after the scene is imported and gets the root node.
func _post_import(scene):
    # Change all node names to "modified_[oldnodename]"
    iterate(scene)
    return scene # Remember to return the imported scene

func iterate(node):
    if node != null:
        node.name = "modified_" + node.name
        for child in node.get_children():
            iterate(child)
```

```csharp
using Godot;

// This sample changes all node names.
// Called right after the scene is imported and gets the root node.
[Tool]
public partial class NodeRenamer : EditorScenePostImport
{
    public override GodotObject _PostImport(Node scene)
    {
        // Change all node names to "modified_[oldnodename]"
        Iterate(scene);
        return scene; // Remember to return the imported scene
    }

    public void Iterate(Node node)
    {
        if (node != null)
        {
            node.Name = $"modified_{node.Name}";
            foreach (Node child in node.GetChildren())
            {
                Iterate(child);
            }
        }
    }
}
```

<a id="tutorials"></a>

## Tutorials

- [Importing 3D scenes: Configuration: Using import scripts for automation](../tutorials/assets_pipeline/importing_3d_scenes/import_configuration.md#using-import-scripts-for-automation)

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Object](class_object.md#class-object) | [_post_import](class_editorscenepostimport.md#class-editorscenepostimport-private-method-post-import)(scene: [Node](class_node.md#class-node)) virtual |
| [String](class_string.md#class-string) | [get_source_file](class_editorscenepostimport.md#class-editorscenepostimport-method-get-source-file)() const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-editorscenepostimport-private-method-post-import"></a>

[Object](class_object.md#class-object) **_post_import**(scene: [Node](class_node.md#class-node)) virtual [🔗](class_editorscenepostimport.md#class-editorscenepostimport-private-method-post-import)

Called after the scene was imported. This method must return the modified version of the scene.

---


<a id="class-editorscenepostimport-method-get-source-file"></a>

[String](class_string.md#class-string) **get_source_file**() const [🔗](class_editorscenepostimport.md#class-editorscenepostimport-method-get-source-file)

Returns the source file path which got imported (e.g. `res://scene.dae`).
