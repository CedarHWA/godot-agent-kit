> Source: https://docs.godotengine.org/en/4.7/classes/class_tilemappattern.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="tilemappattern"></a>

<a id="class-tilemappattern"></a>

# TileMapPattern

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Holds a pattern to be copied from or pasted into [TileMap](class_tilemap.md#class-tilemap)s.

<a id="description"></a>

## Description

This resource holds a set of cells to help bulk manipulations of [TileMap](class_tilemap.md#class-tilemap).

A pattern always starts at the `(0, 0)` coordinates and cannot have cells with negative coordinates.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [int](class_int.md#class-int) | [get_cell_alternative_tile](class_tilemappattern.md#class-tilemappattern-method-get-cell-alternative-tile)(coords: [Vector2i](class_vector2i.md#class-vector2i)) const |
| [Vector2i](class_vector2i.md#class-vector2i) | [get_cell_atlas_coords](class_tilemappattern.md#class-tilemappattern-method-get-cell-atlas-coords)(coords: [Vector2i](class_vector2i.md#class-vector2i)) const |
| [int](class_int.md#class-int) | [get_cell_source_id](class_tilemappattern.md#class-tilemappattern-method-get-cell-source-id)(coords: [Vector2i](class_vector2i.md#class-vector2i)) const |
| [Vector2i](class_vector2i.md#class-vector2i) | [get_size](class_tilemappattern.md#class-tilemappattern-method-get-size)() const |
| [Array](class_array.md#class-array)[[Vector2i](class_vector2i.md#class-vector2i)] | [get_used_cells](class_tilemappattern.md#class-tilemappattern-method-get-used-cells)() const |
| [bool](class_bool.md#class-bool) | [has_cell](class_tilemappattern.md#class-tilemappattern-method-has-cell)(coords: [Vector2i](class_vector2i.md#class-vector2i)) const |
| [bool](class_bool.md#class-bool) | [is_empty](class_tilemappattern.md#class-tilemappattern-method-is-empty)() const |
| void | [remove_cell](class_tilemappattern.md#class-tilemappattern-method-remove-cell)(coords: [Vector2i](class_vector2i.md#class-vector2i), update_size: [bool](class_bool.md#class-bool)) |
| void | [set_cell](class_tilemappattern.md#class-tilemappattern-method-set-cell)(coords: [Vector2i](class_vector2i.md#class-vector2i), source_id: [int](class_int.md#class-int) = -1, atlas_coords: [Vector2i](class_vector2i.md#class-vector2i) = Vector2i(-1, -1), alternative_tile: [int](class_int.md#class-int) = -1) |
| void | [set_size](class_tilemappattern.md#class-tilemappattern-method-set-size)(size: [Vector2i](class_vector2i.md#class-vector2i)) |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-tilemappattern-method-get-cell-alternative-tile"></a>

[int](class_int.md#class-int) **get_cell_alternative_tile**(coords: [Vector2i](class_vector2i.md#class-vector2i)) const [🔗](class_tilemappattern.md#class-tilemappattern-method-get-cell-alternative-tile)

Returns the tile alternative ID of the cell at `coords`.

---


<a id="class-tilemappattern-method-get-cell-atlas-coords"></a>

[Vector2i](class_vector2i.md#class-vector2i) **get_cell_atlas_coords**(coords: [Vector2i](class_vector2i.md#class-vector2i)) const [🔗](class_tilemappattern.md#class-tilemappattern-method-get-cell-atlas-coords)

Returns the tile atlas coordinates ID of the cell at `coords`.

---


<a id="class-tilemappattern-method-get-cell-source-id"></a>

[int](class_int.md#class-int) **get_cell_source_id**(coords: [Vector2i](class_vector2i.md#class-vector2i)) const [🔗](class_tilemappattern.md#class-tilemappattern-method-get-cell-source-id)

Returns the tile source ID of the cell at `coords`.

---


<a id="class-tilemappattern-method-get-size"></a>

[Vector2i](class_vector2i.md#class-vector2i) **get_size**() const [🔗](class_tilemappattern.md#class-tilemappattern-method-get-size)

Returns the size, in cells, of the pattern.

---


<a id="class-tilemappattern-method-get-used-cells"></a>

[Array](class_array.md#class-array)[[Vector2i](class_vector2i.md#class-vector2i)] **get_used_cells**() const [🔗](class_tilemappattern.md#class-tilemappattern-method-get-used-cells)

Returns the list of used cell coordinates in the pattern.

---


<a id="class-tilemappattern-method-has-cell"></a>

[bool](class_bool.md#class-bool) **has_cell**(coords: [Vector2i](class_vector2i.md#class-vector2i)) const [🔗](class_tilemappattern.md#class-tilemappattern-method-has-cell)

Returns whether the pattern has a tile at the given coordinates.

---


<a id="class-tilemappattern-method-is-empty"></a>

[bool](class_bool.md#class-bool) **is_empty**() const [🔗](class_tilemappattern.md#class-tilemappattern-method-is-empty)

Returns whether the pattern is empty or not.

---


<a id="class-tilemappattern-method-remove-cell"></a>

void **remove_cell**(coords: [Vector2i](class_vector2i.md#class-vector2i), update_size: [bool](class_bool.md#class-bool)) [🔗](class_tilemappattern.md#class-tilemappattern-method-remove-cell)

Remove the cell at the given coordinates.

---


<a id="class-tilemappattern-method-set-cell"></a>

void **set_cell**(coords: [Vector2i](class_vector2i.md#class-vector2i), source_id: [int](class_int.md#class-int) = -1, atlas_coords: [Vector2i](class_vector2i.md#class-vector2i) = Vector2i(-1, -1), alternative_tile: [int](class_int.md#class-int) = -1) [🔗](class_tilemappattern.md#class-tilemappattern-method-set-cell)

Sets the tile identifiers for the cell at coordinates `coords`. See [TileMap.set_cell()](class_tilemap.md#class-tilemap-method-set-cell).

---


<a id="class-tilemappattern-method-set-size"></a>

void **set_size**(size: [Vector2i](class_vector2i.md#class-vector2i)) [🔗](class_tilemappattern.md#class-tilemappattern-method-set-size)

Sets the size of the pattern.
