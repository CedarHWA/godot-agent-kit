> Source: https://docs.godotengine.org/en/4.7/classes/class_polygon2d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="polygon2d"></a>

<a id="class-polygon2d"></a>

# Polygon2D

**Inherits:** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A 2D polygon.

<a id="description"></a>

## Description

A Polygon2D is defined by a set of points. Each point is connected to the next, with the final point being connected to the first, resulting in a closed polygon. Polygon2Ds can be filled with color (solid or gradient) or filled with a given texture.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [antialiased](class_polygon2d.md#class-polygon2d-property-antialiased) | `false` |
| [Color](class_color.md#class-color) | [color](class_polygon2d.md#class-polygon2d-property-color) | `Color(1, 1, 1, 1)` |
| [int](class_int.md#class-int) | [internal_vertex_count](class_polygon2d.md#class-polygon2d-property-internal-vertex-count) | `0` |
| [float](class_float.md#class-float) | [invert_border](class_polygon2d.md#class-polygon2d-property-invert-border) | `100.0` |
| [bool](class_bool.md#class-bool) | [invert_enabled](class_polygon2d.md#class-polygon2d-property-invert-enabled) | `false` |
| [Vector2](class_vector2.md#class-vector2) | [offset](class_polygon2d.md#class-polygon2d-property-offset) | `Vector2(0, 0)` |
| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) | [polygon](class_polygon2d.md#class-polygon2d-property-polygon) | `PackedVector2Array()` |
| [Array](class_array.md#class-array) | [polygons](class_polygon2d.md#class-polygon2d-property-polygons) | `[]` |
| [NodePath](class_nodepath.md#class-nodepath) | [skeleton](class_polygon2d.md#class-polygon2d-property-skeleton) | `NodePath("")` |
| [Texture2D](class_texture2d.md#class-texture2d) | [texture](class_polygon2d.md#class-polygon2d-property-texture) |  |
| [Vector2](class_vector2.md#class-vector2) | [texture_offset](class_polygon2d.md#class-polygon2d-property-texture-offset) | `Vector2(0, 0)` |
| [float](class_float.md#class-float) | [texture_rotation](class_polygon2d.md#class-polygon2d-property-texture-rotation) | `0.0` |
| [Vector2](class_vector2.md#class-vector2) | [texture_scale](class_polygon2d.md#class-polygon2d-property-texture-scale) | `Vector2(1, 1)` |
| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) | [uv](class_polygon2d.md#class-polygon2d-property-uv) | `PackedVector2Array()` |
| [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) | [vertex_colors](class_polygon2d.md#class-polygon2d-property-vertex-colors) | `PackedColorArray()` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_bone](class_polygon2d.md#class-polygon2d-method-add-bone)(path: [NodePath](class_nodepath.md#class-nodepath), weights: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array)) |
| void | [clear_bones](class_polygon2d.md#class-polygon2d-method-clear-bones)() |
| void | [erase_bone](class_polygon2d.md#class-polygon2d-method-erase-bone)(index: [int](class_int.md#class-int)) |
| [int](class_int.md#class-int) | [get_bone_count](class_polygon2d.md#class-polygon2d-method-get-bone-count)() const |
| [NodePath](class_nodepath.md#class-nodepath) | [get_bone_path](class_polygon2d.md#class-polygon2d-method-get-bone-path)(index: [int](class_int.md#class-int)) const |
| [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) | [get_bone_weights](class_polygon2d.md#class-polygon2d-method-get-bone-weights)(index: [int](class_int.md#class-int)) const |
| void | [set_bone_path](class_polygon2d.md#class-polygon2d-method-set-bone-path)(index: [int](class_int.md#class-int), path: [NodePath](class_nodepath.md#class-nodepath)) |
| void | [set_bone_weights](class_polygon2d.md#class-polygon2d-method-set-bone-weights)(index: [int](class_int.md#class-int), weights: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array)) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-polygon2d-property-antialiased"></a>

[bool](class_bool.md#class-bool) **antialiased** = `false` [🔗](class_polygon2d.md#class-polygon2d-property-antialiased)

- void **set_antialiased**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_antialiased**()

If `true`, polygon edges will be anti-aliased.

---


<a id="class-polygon2d-property-color"></a>

[Color](class_color.md#class-color) **color** = `Color(1, 1, 1, 1)` [🔗](class_polygon2d.md#class-polygon2d-property-color)

- void **set_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_color**()

The polygon's fill color. If [texture](class_polygon2d.md#class-polygon2d-property-texture) is set, it will be multiplied by this color. It will also be the default color for vertices not set in [vertex_colors](class_polygon2d.md#class-polygon2d-property-vertex-colors).

---


<a id="class-polygon2d-property-internal-vertex-count"></a>

[int](class_int.md#class-int) **internal_vertex_count** = `0` [🔗](class_polygon2d.md#class-polygon2d-property-internal-vertex-count)

- void **set_internal_vertex_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_internal_vertex_count**()

Number of internal vertices, used for UV mapping.

---


<a id="class-polygon2d-property-invert-border"></a>

[float](class_float.md#class-float) **invert_border** = `100.0` [🔗](class_polygon2d.md#class-polygon2d-property-invert-border)

- void **set_invert_border**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_invert_border**()

Added padding applied to the bounding box when [invert_enabled](class_polygon2d.md#class-polygon2d-property-invert-enabled) is set to `true`. Setting this value too small may result in a "Bad Polygon" error.

---


<a id="class-polygon2d-property-invert-enabled"></a>

[bool](class_bool.md#class-bool) **invert_enabled** = `false` [🔗](class_polygon2d.md#class-polygon2d-property-invert-enabled)

- void **set_invert_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_invert_enabled**()

If `true`, the polygon will be inverted, containing the area outside the defined points and extending to the [invert_border](class_polygon2d.md#class-polygon2d-property-invert-border).

---


<a id="class-polygon2d-property-offset"></a>

[Vector2](class_vector2.md#class-vector2) **offset** = `Vector2(0, 0)` [🔗](class_polygon2d.md#class-polygon2d-property-offset)

- void **set_offset**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_offset**()

The offset applied to each vertex.

---


<a id="class-polygon2d-property-polygon"></a>

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **polygon** = `PackedVector2Array()` [🔗](class_polygon2d.md#class-polygon2d-property-polygon)

- void **set_polygon**(value: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array))
- [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **get_polygon**()

The polygon's list of vertices. The final point will be connected to the first.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) for more details.

---


<a id="class-polygon2d-property-polygons"></a>

[Array](class_array.md#class-array) **polygons** = `[]` [🔗](class_polygon2d.md#class-polygon2d-property-polygons)

- void **set_polygons**(value: [Array](class_array.md#class-array))
- [Array](class_array.md#class-array) **get_polygons**()

The list of polygons, in case more than one is being represented. Every individual polygon is stored as a [PackedInt32Array](class_packedint32array.md#class-packedint32array) where each [int](class_int.md#class-int) is an index to a point in [polygon](class_polygon2d.md#class-polygon2d-property-polygon). If empty, this property will be ignored, and the resulting single polygon will be composed of all points in [polygon](class_polygon2d.md#class-polygon2d-property-polygon), using the order they are stored in.

---


<a id="class-polygon2d-property-skeleton"></a>

[NodePath](class_nodepath.md#class-nodepath) **skeleton** = `NodePath("")` [🔗](class_polygon2d.md#class-polygon2d-property-skeleton)

- void **set_skeleton**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_skeleton**()

Path to a [Skeleton2D](class_skeleton2d.md#class-skeleton2d) node used for skeleton-based deformations of this polygon. If empty or invalid, skeletal deformations will not be used.

---


<a id="class-polygon2d-property-texture"></a>

[Texture2D](class_texture2d.md#class-texture2d) **texture** [🔗](class_polygon2d.md#class-polygon2d-property-texture)

- void **set_texture**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_texture**()

The polygon's fill texture. Use [uv](class_polygon2d.md#class-polygon2d-property-uv) to set texture coordinates.

---


<a id="class-polygon2d-property-texture-offset"></a>

[Vector2](class_vector2.md#class-vector2) **texture_offset** = `Vector2(0, 0)` [🔗](class_polygon2d.md#class-polygon2d-property-texture-offset)

- void **set_texture_offset**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_texture_offset**()

Amount to offset the polygon's [texture](class_polygon2d.md#class-polygon2d-property-texture). If set to `Vector2(0, 0)`, the texture's origin (its top-left corner) will be placed at the polygon's position.

---


<a id="class-polygon2d-property-texture-rotation"></a>

[float](class_float.md#class-float) **texture_rotation** = `0.0` [🔗](class_polygon2d.md#class-polygon2d-property-texture-rotation)

- void **set_texture_rotation**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_texture_rotation**()

The texture's rotation in radians.

---


<a id="class-polygon2d-property-texture-scale"></a>

[Vector2](class_vector2.md#class-vector2) **texture_scale** = `Vector2(1, 1)` [🔗](class_polygon2d.md#class-polygon2d-property-texture-scale)

- void **set_texture_scale**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_texture_scale**()

Amount to multiply the [uv](class_polygon2d.md#class-polygon2d-property-uv) coordinates when using [texture](class_polygon2d.md#class-polygon2d-property-texture). Larger values make the texture smaller, and vice versa.

---


<a id="class-polygon2d-property-uv"></a>

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **uv** = `PackedVector2Array()` [🔗](class_polygon2d.md#class-polygon2d-property-uv)

- void **set_uv**(value: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array))
- [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **get_uv**()

Texture coordinates for each vertex of the polygon. There should be one UV value per polygon vertex. If there are fewer, undefined vertices will use `Vector2(0, 0)`.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) for more details.

---


<a id="class-polygon2d-property-vertex-colors"></a>

[PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) **vertex_colors** = `PackedColorArray()` [🔗](class_polygon2d.md#class-polygon2d-property-vertex-colors)

- void **set_vertex_colors**(value: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray))
- [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) **get_vertex_colors**()

Color for each vertex. Colors are interpolated between vertices, resulting in smooth gradients. There should be one per polygon vertex. If there are fewer, undefined vertices will use [color](class_polygon2d.md#class-polygon2d-property-color).

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) for more details.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-polygon2d-method-add-bone"></a>

void **add_bone**(path: [NodePath](class_nodepath.md#class-nodepath), weights: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array)) [🔗](class_polygon2d.md#class-polygon2d-method-add-bone)

Adds a bone with the specified `path` and `weights`.

---


<a id="class-polygon2d-method-clear-bones"></a>

void **clear_bones**() [🔗](class_polygon2d.md#class-polygon2d-method-clear-bones)

Removes all bones from this **Polygon2D**.

---


<a id="class-polygon2d-method-erase-bone"></a>

void **erase_bone**(index: [int](class_int.md#class-int)) [🔗](class_polygon2d.md#class-polygon2d-method-erase-bone)

Removes the specified bone from this **Polygon2D**.

---


<a id="class-polygon2d-method-get-bone-count"></a>

[int](class_int.md#class-int) **get_bone_count**() const [🔗](class_polygon2d.md#class-polygon2d-method-get-bone-count)

Returns the number of bones in this **Polygon2D**.

---


<a id="class-polygon2d-method-get-bone-path"></a>

[NodePath](class_nodepath.md#class-nodepath) **get_bone_path**(index: [int](class_int.md#class-int)) const [🔗](class_polygon2d.md#class-polygon2d-method-get-bone-path)

Returns the path to the node associated with the specified bone.

---


<a id="class-polygon2d-method-get-bone-weights"></a>

[PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) **get_bone_weights**(index: [int](class_int.md#class-int)) const [🔗](class_polygon2d.md#class-polygon2d-method-get-bone-weights)

Returns the weight values of the specified bone.

---


<a id="class-polygon2d-method-set-bone-path"></a>

void **set_bone_path**(index: [int](class_int.md#class-int), path: [NodePath](class_nodepath.md#class-nodepath)) [🔗](class_polygon2d.md#class-polygon2d-method-set-bone-path)

Sets the path to the node associated with the specified bone.

---


<a id="class-polygon2d-method-set-bone-weights"></a>

void **set_bone_weights**(index: [int](class_int.md#class-int), weights: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array)) [🔗](class_polygon2d.md#class-polygon2d-method-set-bone-weights)

Sets the weight values for the specified bone.
