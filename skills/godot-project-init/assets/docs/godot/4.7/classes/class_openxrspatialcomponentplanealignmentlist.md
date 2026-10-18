> Source: https://docs.godotengine.org/en/4.7/classes/class_openxrspatialcomponentplanealignmentlist.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxrspatialcomponentplanealignmentlist"></a>

<a id="class-openxrspatialcomponentplanealignmentlist"></a>

# OpenXRSpatialComponentPlaneAlignmentList

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Object for storing the queries plane alignment result data.

<a id="description"></a>

## Description

Object for storing the queries plane alignment result data when calling [OpenXRSpatialEntityExtension.query_snapshot()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-query-snapshot).

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [PlaneAlignment](class_openxrspatialcomponentplanealignmentlist.md#enum-openxrspatialcomponentplanealignmentlist-planealignment) | [get_plane_alignment](class_openxrspatialcomponentplanealignmentlist.md#class-openxrspatialcomponentplanealignmentlist-method-get-plane-alignment)(index: [int](class_int.md#class-int)) const |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-openxrspatialcomponentplanealignmentlist-planealignment"></a>

enum **PlaneAlignment**: [🔗](class_openxrspatialcomponentplanealignmentlist.md#enum-openxrspatialcomponentplanealignmentlist-planealignment)

<a id="class-openxrspatialcomponentplanealignmentlist-constant-plane-alignment-horizontal-upward"></a>

[PlaneAlignment](class_openxrspatialcomponentplanealignmentlist.md#enum-openxrspatialcomponentplanealignmentlist-planealignment) **PLANE_ALIGNMENT_HORIZONTAL_UPWARD** = `0`

Plane is facing upward.

<a id="class-openxrspatialcomponentplanealignmentlist-constant-plane-alignment-horizontal-downward"></a>

[PlaneAlignment](class_openxrspatialcomponentplanealignmentlist.md#enum-openxrspatialcomponentplanealignmentlist-planealignment) **PLANE_ALIGNMENT_HORIZONTAL_DOWNWARD** = `1`

Plane is facing downwards.

<a id="class-openxrspatialcomponentplanealignmentlist-constant-plane-alignment-vertical"></a>

[PlaneAlignment](class_openxrspatialcomponentplanealignmentlist.md#enum-openxrspatialcomponentplanealignmentlist-planealignment) **PLANE_ALIGNMENT_VERTICAL** = `2`

Plane is vertically aligned.

<a id="class-openxrspatialcomponentplanealignmentlist-constant-plane-alignment-arbitrary"></a>

[PlaneAlignment](class_openxrspatialcomponentplanealignmentlist.md#enum-openxrspatialcomponentplanealignmentlist-planealignment) **PLANE_ALIGNMENT_ARBITRARY** = `3`

Plane has an arbitrary alignment.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-openxrspatialcomponentplanealignmentlist-method-get-plane-alignment"></a>

[PlaneAlignment](class_openxrspatialcomponentplanealignmentlist.md#enum-openxrspatialcomponentplanealignmentlist-planealignment) **get_plane_alignment**(index: [int](class_int.md#class-int)) const [🔗](class_openxrspatialcomponentplanealignmentlist.md#class-openxrspatialcomponentplanealignmentlist-method-get-plane-alignment)

Returns the plane alignment for the parent entity at this `index`.
