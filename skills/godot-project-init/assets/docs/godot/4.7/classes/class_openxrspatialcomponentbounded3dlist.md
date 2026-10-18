> Source: https://docs.godotengine.org/en/4.7/classes/class_openxrspatialcomponentbounded3dlist.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxrspatialcomponentbounded3dlist"></a>

<a id="class-openxrspatialcomponentbounded3dlist"></a>

# OpenXRSpatialComponentBounded3DList

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Object for storing the queries bounded3d result data.

<a id="description"></a>

## Description

Object for storing the queries 3d bounding box result data when calling [OpenXRSpatialEntityExtension.query_snapshot()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-query-snapshot).

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Transform3D](class_transform3d.md#class-transform3d) | [get_center_pose](class_openxrspatialcomponentbounded3dlist.md#class-openxrspatialcomponentbounded3dlist-method-get-center-pose)(index: [int](class_int.md#class-int)) const |
| [Vector3](class_vector3.md#class-vector3) | [get_size](class_openxrspatialcomponentbounded3dlist.md#class-openxrspatialcomponentbounded3dlist-method-get-size)(index: [int](class_int.md#class-int)) const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-openxrspatialcomponentbounded3dlist-method-get-center-pose"></a>

[Transform3D](class_transform3d.md#class-transform3d) **get_center_pose**(index: [int](class_int.md#class-int)) const [🔗](class_openxrspatialcomponentbounded3dlist.md#class-openxrspatialcomponentbounded3dlist-method-get-center-pose)

Returns the center of our bounding box for the entity at this `index`.

---


<a id="class-openxrspatialcomponentbounded3dlist-method-get-size"></a>

[Vector3](class_vector3.md#class-vector3) **get_size**(index: [int](class_int.md#class-int)) const [🔗](class_openxrspatialcomponentbounded3dlist.md#class-openxrspatialcomponentbounded3dlist-method-get-size)

Returns the size of our bounding box for the entity at this `index`.
