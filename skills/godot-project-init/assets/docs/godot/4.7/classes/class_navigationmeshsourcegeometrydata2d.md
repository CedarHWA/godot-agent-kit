> Source: https://docs.godotengine.org/en/4.7/classes/class_navigationmeshsourcegeometrydata2d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="navigationmeshsourcegeometrydata2d"></a>

<a id="class-navigationmeshsourcegeometrydata2d"></a>

# NavigationMeshSourceGeometryData2D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Container for parsed source geometry data used in navigation mesh baking.

<a id="description"></a>

## Description

Container for parsed source geometry data used in navigation mesh baking.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_obstruction_outline](class_navigationmeshsourcegeometrydata2d.md#class-navigationmeshsourcegeometrydata2d-method-add-obstruction-outline)(shape_outline: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array)) |
| void | [add_projected_obstruction](class_navigationmeshsourcegeometrydata2d.md#class-navigationmeshsourcegeometrydata2d-method-add-projected-obstruction)(vertices: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), carve: [bool](class_bool.md#class-bool)) |
| void | [add_traversable_outline](class_navigationmeshsourcegeometrydata2d.md#class-navigationmeshsourcegeometrydata2d-method-add-traversable-outline)(shape_outline: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array)) |
| void | [append_obstruction_outlines](class_navigationmeshsourcegeometrydata2d.md#class-navigationmeshsourcegeometrydata2d-method-append-obstruction-outlines)(obstruction_outlines: [Array](class_array.md#class-array)[[PackedVector2Array](class_packedvector2array.md#class-packedvector2array)]) |
| void | [append_traversable_outlines](class_navigationmeshsourcegeometrydata2d.md#class-navigationmeshsourcegeometrydata2d-method-append-traversable-outlines)(traversable_outlines: [Array](class_array.md#class-array)[[PackedVector2Array](class_packedvector2array.md#class-packedvector2array)]) |
| void | [clear](class_navigationmeshsourcegeometrydata2d.md#class-navigationmeshsourcegeometrydata2d-method-clear)() |
| void | [clear_projected_obstructions](class_navigationmeshsourcegeometrydata2d.md#class-navigationmeshsourcegeometrydata2d-method-clear-projected-obstructions)() |
| [Rect2](class_rect2.md#class-rect2) | [get_bounds](class_navigationmeshsourcegeometrydata2d.md#class-navigationmeshsourcegeometrydata2d-method-get-bounds)() |
| [Array](class_array.md#class-array)[[PackedVector2Array](class_packedvector2array.md#class-packedvector2array)] | [get_obstruction_outlines](class_navigationmeshsourcegeometrydata2d.md#class-navigationmeshsourcegeometrydata2d-method-get-obstruction-outlines)() const |
| [Array](class_array.md#class-array) | [get_projected_obstructions](class_navigationmeshsourcegeometrydata2d.md#class-navigationmeshsourcegeometrydata2d-method-get-projected-obstructions)() const |
| [Array](class_array.md#class-array)[[PackedVector2Array](class_packedvector2array.md#class-packedvector2array)] | [get_traversable_outlines](class_navigationmeshsourcegeometrydata2d.md#class-navigationmeshsourcegeometrydata2d-method-get-traversable-outlines)() const |
| [bool](class_bool.md#class-bool) | [has_data](class_navigationmeshsourcegeometrydata2d.md#class-navigationmeshsourcegeometrydata2d-method-has-data)() |
| void | [merge](class_navigationmeshsourcegeometrydata2d.md#class-navigationmeshsourcegeometrydata2d-method-merge)(other_geometry: [NavigationMeshSourceGeometryData2D](class_navigationmeshsourcegeometrydata2d.md#class-navigationmeshsourcegeometrydata2d)) |
| void | [set_obstruction_outlines](class_navigationmeshsourcegeometrydata2d.md#class-navigationmeshsourcegeometrydata2d-method-set-obstruction-outlines)(obstruction_outlines: [Array](class_array.md#class-array)[[PackedVector2Array](class_packedvector2array.md#class-packedvector2array)]) |
| void | [set_projected_obstructions](class_navigationmeshsourcegeometrydata2d.md#class-navigationmeshsourcegeometrydata2d-method-set-projected-obstructions)(projected_obstructions: [Array](class_array.md#class-array)) |
| void | [set_traversable_outlines](class_navigationmeshsourcegeometrydata2d.md#class-navigationmeshsourcegeometrydata2d-method-set-traversable-outlines)(traversable_outlines: [Array](class_array.md#class-array)[[PackedVector2Array](class_packedvector2array.md#class-packedvector2array)]) |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-navigationmeshsourcegeometrydata2d-method-add-obstruction-outline"></a>

void **add_obstruction_outline**(shape_outline: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array)) [🔗](class_navigationmeshsourcegeometrydata2d.md#class-navigationmeshsourcegeometrydata2d-method-add-obstruction-outline)

Adds the outline points of a shape as obstructed area.

---


<a id="class-navigationmeshsourcegeometrydata2d-method-add-projected-obstruction"></a>

void **add_projected_obstruction**(vertices: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), carve: [bool](class_bool.md#class-bool)) [🔗](class_navigationmeshsourcegeometrydata2d.md#class-navigationmeshsourcegeometrydata2d-method-add-projected-obstruction)

Adds a projected obstruction shape to the source geometry. If `carve` is `true` the carved shape will not be affected by additional offsets (e.g. agent radius) of the navigation mesh baking process.

---


<a id="class-navigationmeshsourcegeometrydata2d-method-add-traversable-outline"></a>

void **add_traversable_outline**(shape_outline: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array)) [🔗](class_navigationmeshsourcegeometrydata2d.md#class-navigationmeshsourcegeometrydata2d-method-add-traversable-outline)

Adds the outline points of a shape as traversable area.

---


<a id="class-navigationmeshsourcegeometrydata2d-method-append-obstruction-outlines"></a>

void **append_obstruction_outlines**(obstruction_outlines: [Array](class_array.md#class-array)[[PackedVector2Array](class_packedvector2array.md#class-packedvector2array)]) [🔗](class_navigationmeshsourcegeometrydata2d.md#class-navigationmeshsourcegeometrydata2d-method-append-obstruction-outlines)

Appends another array of `obstruction_outlines` at the end of the existing obstruction outlines array.

---


<a id="class-navigationmeshsourcegeometrydata2d-method-append-traversable-outlines"></a>

void **append_traversable_outlines**(traversable_outlines: [Array](class_array.md#class-array)[[PackedVector2Array](class_packedvector2array.md#class-packedvector2array)]) [🔗](class_navigationmeshsourcegeometrydata2d.md#class-navigationmeshsourcegeometrydata2d-method-append-traversable-outlines)

Appends another array of `traversable_outlines` at the end of the existing traversable outlines array.

---


<a id="class-navigationmeshsourcegeometrydata2d-method-clear"></a>

void **clear**() [🔗](class_navigationmeshsourcegeometrydata2d.md#class-navigationmeshsourcegeometrydata2d-method-clear)

Clears the internal data.

---


<a id="class-navigationmeshsourcegeometrydata2d-method-clear-projected-obstructions"></a>

void **clear_projected_obstructions**() [🔗](class_navigationmeshsourcegeometrydata2d.md#class-navigationmeshsourcegeometrydata2d-method-clear-projected-obstructions)

Clears all projected obstructions.

---


<a id="class-navigationmeshsourcegeometrydata2d-method-get-bounds"></a>

[Rect2](class_rect2.md#class-rect2) **get_bounds**() [🔗](class_navigationmeshsourcegeometrydata2d.md#class-navigationmeshsourcegeometrydata2d-method-get-bounds)

Returns an axis-aligned bounding box that covers all the stored geometry data. The bounds are calculated when calling this function with the result cached until further geometry changes are made.

---


<a id="class-navigationmeshsourcegeometrydata2d-method-get-obstruction-outlines"></a>

[Array](class_array.md#class-array)[[PackedVector2Array](class_packedvector2array.md#class-packedvector2array)] **get_obstruction_outlines**() const [🔗](class_navigationmeshsourcegeometrydata2d.md#class-navigationmeshsourcegeometrydata2d-method-get-obstruction-outlines)

Returns all the obstructed area outlines arrays.

---


<a id="class-navigationmeshsourcegeometrydata2d-method-get-projected-obstructions"></a>

[Array](class_array.md#class-array) **get_projected_obstructions**() const [🔗](class_navigationmeshsourcegeometrydata2d.md#class-navigationmeshsourcegeometrydata2d-method-get-projected-obstructions)

Returns the projected obstructions as an [Array](class_array.md#class-array) of dictionaries. Each [Dictionary](class_dictionary.md#class-dictionary) contains the following entries:

- `vertices` - A [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) that defines the outline points of the projected shape.
- `carve` - A [bool](class_bool.md#class-bool) that defines how the projected shape affects the navigation mesh baking. If `true` the projected shape will not be affected by addition offsets, e.g. agent radius.

---


<a id="class-navigationmeshsourcegeometrydata2d-method-get-traversable-outlines"></a>

[Array](class_array.md#class-array)[[PackedVector2Array](class_packedvector2array.md#class-packedvector2array)] **get_traversable_outlines**() const [🔗](class_navigationmeshsourcegeometrydata2d.md#class-navigationmeshsourcegeometrydata2d-method-get-traversable-outlines)

Returns all the traversable area outlines arrays.

---


<a id="class-navigationmeshsourcegeometrydata2d-method-has-data"></a>

[bool](class_bool.md#class-bool) **has_data**() [🔗](class_navigationmeshsourcegeometrydata2d.md#class-navigationmeshsourcegeometrydata2d-method-has-data)

Returns `true` when parsed source geometry data exists.

---


<a id="class-navigationmeshsourcegeometrydata2d-method-merge"></a>

void **merge**(other_geometry: [NavigationMeshSourceGeometryData2D](class_navigationmeshsourcegeometrydata2d.md#class-navigationmeshsourcegeometrydata2d)) [🔗](class_navigationmeshsourcegeometrydata2d.md#class-navigationmeshsourcegeometrydata2d-method-merge)

Adds the geometry data of another **NavigationMeshSourceGeometryData2D** to the navigation mesh baking data.

---


<a id="class-navigationmeshsourcegeometrydata2d-method-set-obstruction-outlines"></a>

void **set_obstruction_outlines**(obstruction_outlines: [Array](class_array.md#class-array)[[PackedVector2Array](class_packedvector2array.md#class-packedvector2array)]) [🔗](class_navigationmeshsourcegeometrydata2d.md#class-navigationmeshsourcegeometrydata2d-method-set-obstruction-outlines)

Sets all the obstructed area outlines arrays.

---


<a id="class-navigationmeshsourcegeometrydata2d-method-set-projected-obstructions"></a>

void **set_projected_obstructions**(projected_obstructions: [Array](class_array.md#class-array)) [🔗](class_navigationmeshsourcegeometrydata2d.md#class-navigationmeshsourcegeometrydata2d-method-set-projected-obstructions)

Sets the projected obstructions with an Array of Dictionaries with the following key value pairs:

```gdscript
"vertices" : PackedFloat32Array
"carve" : bool
```

---


<a id="class-navigationmeshsourcegeometrydata2d-method-set-traversable-outlines"></a>

void **set_traversable_outlines**(traversable_outlines: [Array](class_array.md#class-array)[[PackedVector2Array](class_packedvector2array.md#class-packedvector2array)]) [🔗](class_navigationmeshsourcegeometrydata2d.md#class-navigationmeshsourcegeometrydata2d-method-set-traversable-outlines)

Sets all the traversable area outlines arrays.
