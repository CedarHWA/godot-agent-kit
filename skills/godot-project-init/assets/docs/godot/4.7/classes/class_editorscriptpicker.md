> Source: https://docs.godotengine.org/en/4.7/classes/class_editorscriptpicker.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="editorscriptpicker"></a>

<a id="class-editorscriptpicker"></a>

# EditorScriptPicker

**Inherits:** [EditorResourcePicker](class_editorresourcepicker.md#class-editorresourcepicker) **<** [HBoxContainer](class_hboxcontainer.md#class-hboxcontainer) **<** [BoxContainer](class_boxcontainer.md#class-boxcontainer) **<** [Container](class_container.md#class-container) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Godot editor's control for selecting the `script` property of a [Node](class_node.md#class-node).

<a id="description"></a>

## Description

Similar to [EditorResourcePicker](class_editorresourcepicker.md#class-editorresourcepicker) this [Control](class_control.md#class-control) node is used in the editor's Inspector dock, but only to edit the `script` property of a [Node](class_node.md#class-node). Default options for creating new resources of all possible subtypes are replaced with dedicated buttons that open the "Attach Node Script" dialog. Can be used with [EditorInspectorPlugin](class_editorinspectorplugin.md#class-editorinspectorplugin) to recreate the same behavior.

**Note:** You must set the [script_owner](class_editorscriptpicker.md#class-editorscriptpicker-property-script-owner) for the custom context menu items to work.

<a id="properties"></a>

## Properties

|  |  |
| --- | --- |
| [Node](class_node.md#class-node) | [script_owner](class_editorscriptpicker.md#class-editorscriptpicker-property-script-owner) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-editorscriptpicker-property-script-owner"></a>

[Node](class_node.md#class-node) **script_owner** [🔗](class_editorscriptpicker.md#class-editorscriptpicker-property-script-owner)

- void **set_script_owner**(value: [Node](class_node.md#class-node))
- [Node](class_node.md#class-node) **get_script_owner**()

The owner [Node](class_node.md#class-node) of the script property that holds the edited resource.
