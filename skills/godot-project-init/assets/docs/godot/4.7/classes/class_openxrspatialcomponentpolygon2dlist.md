> Source: https://docs.godotengine.org/en/4.7/classes/class_openxrspatialcomponentpolygon2dlist.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxrspatialcomponentpolygon2dlist"></a>

<a id="class-openxrspatialcomponentpolygon2dlist"></a>

# OpenXRSpatialComponentPolygon2DList

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Object for storing the queries polygon2d result data.

<a id="description"></a>

## Description

Object for storing the queries 2D polygon result data when calling [OpenXRSpatialEntityExtension.query_snapshot()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-query-snapshot).

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Transform3D](class_transform3d.md#class-transform3d) | [get_transform](class_openxrspatialcomponentpolygon2dlist.md#class-openxrspatialcomponentpolygon2dlist-method-get-transform)(index: [int](class_int.md#class-int)) const |
| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) | [get_vertices](class_openxrspatialcomponentpolygon2dlist.md#class-openxrspatialcomponentpolygon2dlist-method-get-vertices)(snapshot: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-openxrspatialcomponentpolygon2dlist-method-get-transform"></a>

[Transform3D](class_transform3d.md#class-transform3d) **get_transform**(index: [int](class_int.md#class-int)) const [🔗](class_openxrspatialcomponentpolygon2dlist.md#class-openxrspatialcomponentpolygon2dlist-method-get-transform)

Returns the transform for positioning our polygon for the entity at this `index`.

---


<a id="class-openxrspatialcomponentpolygon2dlist-method-get-vertices"></a>

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **get_vertices**(snapshot: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) const [🔗](class_openxrspatialcomponentpolygon2dlist.md#class-openxrspatialcomponentpolygon2dlist-method-get-vertices)

Returns the polygon vertices for the entity at this `index`.
