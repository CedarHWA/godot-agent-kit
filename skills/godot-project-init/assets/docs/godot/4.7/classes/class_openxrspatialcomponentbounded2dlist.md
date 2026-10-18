> Source: https://docs.godotengine.org/en/4.7/classes/class_openxrspatialcomponentbounded2dlist.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxrspatialcomponentbounded2dlist"></a>

<a id="class-openxrspatialcomponentbounded2dlist"></a>

# OpenXRSpatialComponentBounded2DList

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Object for storing the queries bounded2d result data.

<a id="description"></a>

## Description

Object for storing the queries 2D bounding rectangle result data when calling [OpenXRSpatialEntityExtension.query_snapshot()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-query-snapshot).

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Transform3D](class_transform3d.md#class-transform3d) | [get_center_pose](class_openxrspatialcomponentbounded2dlist.md#class-openxrspatialcomponentbounded2dlist-method-get-center-pose)(index: [int](class_int.md#class-int)) const |
| [Vector2](class_vector2.md#class-vector2) | [get_size](class_openxrspatialcomponentbounded2dlist.md#class-openxrspatialcomponentbounded2dlist-method-get-size)(index: [int](class_int.md#class-int)) const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-openxrspatialcomponentbounded2dlist-method-get-center-pose"></a>

[Transform3D](class_transform3d.md#class-transform3d) **get_center_pose**(index: [int](class_int.md#class-int)) const [🔗](class_openxrspatialcomponentbounded2dlist.md#class-openxrspatialcomponentbounded2dlist-method-get-center-pose)

Returns the center of our bounding rectangle for the entity at this `index`.

---


<a id="class-openxrspatialcomponentbounded2dlist-method-get-size"></a>

[Vector2](class_vector2.md#class-vector2) **get_size**(index: [int](class_int.md#class-int)) const [🔗](class_openxrspatialcomponentbounded2dlist.md#class-openxrspatialcomponentbounded2dlist-method-get-size)

Returns the size of our bounding rectangle for the entity at this `index`.
