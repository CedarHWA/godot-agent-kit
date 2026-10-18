> Source: https://docs.godotengine.org/en/4.7/classes/class_openxrspatialcomponentmesh2dlist.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxrspatialcomponentmesh2dlist"></a>

<a id="class-openxrspatialcomponentmesh2dlist"></a>

# OpenXRSpatialComponentMesh2DList

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Object for storing the queries mesh2d result data.

<a id="description"></a>

## Description

Object for storing the queries 2D mesh result data when calling [OpenXRSpatialEntityExtension.query_snapshot()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-query-snapshot).

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array) | [get_indices](class_openxrspatialcomponentmesh2dlist.md#class-openxrspatialcomponentmesh2dlist-method-get-indices)(snapshot: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) const |
| [Transform3D](class_transform3d.md#class-transform3d) | [get_transform](class_openxrspatialcomponentmesh2dlist.md#class-openxrspatialcomponentmesh2dlist-method-get-transform)(index: [int](class_int.md#class-int)) const |
| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) | [get_vertices](class_openxrspatialcomponentmesh2dlist.md#class-openxrspatialcomponentmesh2dlist-method-get-vertices)(snapshot: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-openxrspatialcomponentmesh2dlist-method-get-indices"></a>

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_indices**(snapshot: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) const [🔗](class_openxrspatialcomponentmesh2dlist.md#class-openxrspatialcomponentmesh2dlist-method-get-indices)

Returns the mesh indices for the entity at this `index`.

---


<a id="class-openxrspatialcomponentmesh2dlist-method-get-transform"></a>

[Transform3D](class_transform3d.md#class-transform3d) **get_transform**(index: [int](class_int.md#class-int)) const [🔗](class_openxrspatialcomponentmesh2dlist.md#class-openxrspatialcomponentmesh2dlist-method-get-transform)

Returns the transform for positioning our mesh for the entity at this `index`.

---


<a id="class-openxrspatialcomponentmesh2dlist-method-get-vertices"></a>

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **get_vertices**(snapshot: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) const [🔗](class_openxrspatialcomponentmesh2dlist.md#class-openxrspatialcomponentmesh2dlist-method-get-vertices)

Returns the mesh vertices for the entity at this `index`.
