> Source: https://docs.godotengine.org/en/4.7/classes/class_openxrspatialcomponentanchorlist.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxrspatialcomponentanchorlist"></a>

<a id="class-openxrspatialcomponentanchorlist"></a>

# OpenXRSpatialComponentAnchorList

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Object for storing the queries anchor result data.

<a id="description"></a>

## Description

Object for storing the queries anchor result data when calling [OpenXRSpatialEntityExtension.query_snapshot()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-query-snapshot).

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Transform3D](class_transform3d.md#class-transform3d) | [get_entity_pose](class_openxrspatialcomponentanchorlist.md#class-openxrspatialcomponentanchorlist-method-get-entity-pose)(index: [int](class_int.md#class-int)) const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-openxrspatialcomponentanchorlist-method-get-entity-pose"></a>

[Transform3D](class_transform3d.md#class-transform3d) **get_entity_pose**(index: [int](class_int.md#class-int)) const [🔗](class_openxrspatialcomponentanchorlist.md#class-openxrspatialcomponentanchorlist-method-get-entity-pose)

Returns the transform for the entity at this `index`.
