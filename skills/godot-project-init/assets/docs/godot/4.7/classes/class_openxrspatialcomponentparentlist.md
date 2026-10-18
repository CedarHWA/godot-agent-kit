> Source: https://docs.godotengine.org/en/4.7/classes/class_openxrspatialcomponentparentlist.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxrspatialcomponentparentlist"></a>

<a id="class-openxrspatialcomponentparentlist"></a>

# OpenXRSpatialComponentParentList

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Object for storing the queries parent result data.

<a id="description"></a>

## Description

Object for storing the queries parent result data when calling [OpenXRSpatialEntityExtension.query_snapshot()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-query-snapshot).

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [RID](class_rid.md#class-rid) | [get_parent](class_openxrspatialcomponentparentlist.md#class-openxrspatialcomponentparentlist-method-get-parent)(index: [int](class_int.md#class-int)) const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-openxrspatialcomponentparentlist-method-get-parent"></a>

[RID](class_rid.md#class-rid) **get_parent**(index: [int](class_int.md#class-int)) const [🔗](class_openxrspatialcomponentparentlist.md#class-openxrspatialcomponentparentlist-method-get-parent)

Returns the RID for the parent entity at this `index`.
