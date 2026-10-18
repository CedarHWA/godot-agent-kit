> Source: https://docs.godotengine.org/en/4.7/classes/class_gridmapeditorplugin.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="gridmapeditorplugin"></a>

<a id="class-gridmapeditorplugin"></a>

# GridMapEditorPlugin

**Inherits:** [EditorPlugin](class_editorplugin.md#class-editorplugin) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Editor for [GridMap](class_gridmap.md#class-gridmap) nodes.

<a id="description"></a>

## Description

GridMapEditorPlugin provides access to the [GridMap](class_gridmap.md#class-gridmap) editor functionality.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [clear_selection](class_gridmapeditorplugin.md#class-gridmapeditorplugin-method-clear-selection)() |
| [GridMap](class_gridmap.md#class-gridmap) | [get_current_grid_map](class_gridmapeditorplugin.md#class-gridmapeditorplugin-method-get-current-grid-map)() const |
| [Array](class_array.md#class-array) | [get_selected_cells](class_gridmapeditorplugin.md#class-gridmapeditorplugin-method-get-selected-cells)() const |
| [int](class_int.md#class-int) | [get_selected_palette_item](class_gridmapeditorplugin.md#class-gridmapeditorplugin-method-get-selected-palette-item)() const |
| [AABB](class_aabb.md#class-aabb) | [get_selection](class_gridmapeditorplugin.md#class-gridmapeditorplugin-method-get-selection)() const |
| [bool](class_bool.md#class-bool) | [has_selection](class_gridmapeditorplugin.md#class-gridmapeditorplugin-method-has-selection)() const |
| void | [set_selected_palette_item](class_gridmapeditorplugin.md#class-gridmapeditorplugin-method-set-selected-palette-item)(item: [int](class_int.md#class-int)) const |
| void | [set_selection](class_gridmapeditorplugin.md#class-gridmapeditorplugin-method-set-selection)(begin: [Vector3i](class_vector3i.md#class-vector3i), end: [Vector3i](class_vector3i.md#class-vector3i)) |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-gridmapeditorplugin-method-clear-selection"></a>

void **clear_selection**() [🔗](class_gridmapeditorplugin.md#class-gridmapeditorplugin-method-clear-selection)

Deselects any currently selected cells.

---


<a id="class-gridmapeditorplugin-method-get-current-grid-map"></a>

[GridMap](class_gridmap.md#class-gridmap) **get_current_grid_map**() const [🔗](class_gridmapeditorplugin.md#class-gridmapeditorplugin-method-get-current-grid-map)

Returns the [GridMap](class_gridmap.md#class-gridmap) node currently edited by the grid map editor.

---


<a id="class-gridmapeditorplugin-method-get-selected-cells"></a>

[Array](class_array.md#class-array) **get_selected_cells**() const [🔗](class_gridmapeditorplugin.md#class-gridmapeditorplugin-method-get-selected-cells)

Returns an array of [Vector3i](class_vector3i.md#class-vector3i)s with the selected cells' coordinates.

---


<a id="class-gridmapeditorplugin-method-get-selected-palette-item"></a>

[int](class_int.md#class-int) **get_selected_palette_item**() const [🔗](class_gridmapeditorplugin.md#class-gridmapeditorplugin-method-get-selected-palette-item)

Returns the index of the selected [MeshLibrary](class_meshlibrary.md#class-meshlibrary) item in the grid map editor's palette or `-1` if no item is selected.

**Note:** The indices might not be in the same order as they appear in the editor's interface.

---


<a id="class-gridmapeditorplugin-method-get-selection"></a>

[AABB](class_aabb.md#class-aabb) **get_selection**() const [🔗](class_gridmapeditorplugin.md#class-gridmapeditorplugin-method-get-selection)

Returns the cell coordinate bounds of the current selection. Use [has_selection()](class_gridmapeditorplugin.md#class-gridmapeditorplugin-method-has-selection) to check if there is an active selection.

---


<a id="class-gridmapeditorplugin-method-has-selection"></a>

[bool](class_bool.md#class-bool) **has_selection**() const [🔗](class_gridmapeditorplugin.md#class-gridmapeditorplugin-method-has-selection)

Returns `true` if there are selected cells.

---


<a id="class-gridmapeditorplugin-method-set-selected-palette-item"></a>

void **set_selected_palette_item**(item: [int](class_int.md#class-int)) const [🔗](class_gridmapeditorplugin.md#class-gridmapeditorplugin-method-set-selected-palette-item)

Selects the [MeshLibrary](class_meshlibrary.md#class-meshlibrary) item with the given index in the grid map editor's palette. If a negative index is given, no item will be selected. If a value greater than the last index is given, the last item will be selected.

**Note:** The indices might not be in the same order as they appear in the editor's interface.

---


<a id="class-gridmapeditorplugin-method-set-selection"></a>

void **set_selection**(begin: [Vector3i](class_vector3i.md#class-vector3i), end: [Vector3i](class_vector3i.md#class-vector3i)) [🔗](class_gridmapeditorplugin.md#class-gridmapeditorplugin-method-set-selection)

Selects the cells inside the given bounds from `begin` to `end`.
