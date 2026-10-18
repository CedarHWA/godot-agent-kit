> Source: https://docs.godotengine.org/en/4.7/classes/class_editorselection.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="editorselection"></a>

<a id="class-editorselection"></a>

# EditorSelection

**Inherits:** [Object](class_object.md#class-object)

Manages the SceneTree selection in the editor.

<a id="description"></a>

## Description

This object manages the SceneTree selection in the editor.

**Note:** This class shouldn't be instantiated directly. Instead, access the singleton using [EditorInterface.get_selection()](class_editorinterface.md#class-editorinterface-method-get-selection).

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_node](class_editorselection.md#class-editorselection-method-add-node)(node: [Node](class_node.md#class-node)) |
| void | [clear](class_editorselection.md#class-editorselection-method-clear)() |
| [Array](class_array.md#class-array)[[Node](class_node.md#class-node)] | [get_selected_nodes](class_editorselection.md#class-editorselection-method-get-selected-nodes)() |
| [Array](class_array.md#class-array)[[Node](class_node.md#class-node)] | [get_top_selected_nodes](class_editorselection.md#class-editorselection-method-get-top-selected-nodes)() |
| [Array](class_array.md#class-array)[[Node](class_node.md#class-node)] | [get_transformable_selected_nodes](class_editorselection.md#class-editorselection-method-get-transformable-selected-nodes)() |
| void | [remove_node](class_editorselection.md#class-editorselection-method-remove-node)(node: [Node](class_node.md#class-node)) |

---


<a id="signals"></a>

## Signals

<a id="class-editorselection-signal-selection-changed"></a>

**selection_changed**() [🔗](class_editorselection.md#class-editorselection-signal-selection-changed)

Emitted when the selection changes.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-editorselection-method-add-node"></a>

void **add_node**(node: [Node](class_node.md#class-node)) [🔗](class_editorselection.md#class-editorselection-method-add-node)

Adds a node to the selection.

**Note:** The newly selected node will not be automatically edited in the inspector. If you want to edit a node, use [EditorInterface.edit_node()](class_editorinterface.md#class-editorinterface-method-edit-node).

---


<a id="class-editorselection-method-clear"></a>

void **clear**() [🔗](class_editorselection.md#class-editorselection-method-clear)

Clear the selection.

---


<a id="class-editorselection-method-get-selected-nodes"></a>

[Array](class_array.md#class-array)[[Node](class_node.md#class-node)] **get_selected_nodes**() [🔗](class_editorselection.md#class-editorselection-method-get-selected-nodes)

Returns the list of selected nodes.

---


<a id="class-editorselection-method-get-top-selected-nodes"></a>

[Array](class_array.md#class-array)[[Node](class_node.md#class-node)] **get_top_selected_nodes**() [🔗](class_editorselection.md#class-editorselection-method-get-top-selected-nodes)

Returns the list of top selected nodes only, excluding any children. This is useful for performing transform operations (moving them, rotating, etc.).

For example, if there is a node A with a child B and a sibling C, then selecting all three will cause this method to return only A and C. Changing the global transform of A will affect the global transform of B, so there is no need to change B separately.

---


<a id="class-editorselection-method-get-transformable-selected-nodes"></a>

[Array](class_array.md#class-array)[[Node](class_node.md#class-node)] **get_transformable_selected_nodes**() [🔗](class_editorselection.md#class-editorselection-method-get-transformable-selected-nodes)

**Deprecated:** Use [get_top_selected_nodes()](class_editorselection.md#class-editorselection-method-get-top-selected-nodes) instead.

Returns the list of top selected nodes only, excluding any children. This is useful for performing transform operations (moving them, rotating, etc.). See [get_top_selected_nodes()](class_editorselection.md#class-editorselection-method-get-top-selected-nodes).

---


<a id="class-editorselection-method-remove-node"></a>

void **remove_node**(node: [Node](class_node.md#class-node)) [🔗](class_editorselection.md#class-editorselection-method-remove-node)

Removes a node from the selection.
