> Source: https://docs.godotengine.org/en/4.7/classes/class_openxrspatialcomponentplanesemanticlabellist.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxrspatialcomponentplanesemanticlabellist"></a>

<a id="class-openxrspatialcomponentplanesemanticlabellist"></a>

# OpenXRSpatialComponentPlaneSemanticLabelList

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Object for storing the queries plane semantic label result data.

<a id="description"></a>

## Description

Object for storing the queries plane semantic label result data when calling [OpenXRSpatialEntityExtension.query_snapshot()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-query-snapshot).

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [PlaneSemanticLabel](class_openxrspatialcomponentplanesemanticlabellist.md#enum-openxrspatialcomponentplanesemanticlabellist-planesemanticlabel) | [get_plane_semantic_label](class_openxrspatialcomponentplanesemanticlabellist.md#class-openxrspatialcomponentplanesemanticlabellist-method-get-plane-semantic-label)(index: [int](class_int.md#class-int)) const |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-openxrspatialcomponentplanesemanticlabellist-planesemanticlabel"></a>

enum **PlaneSemanticLabel**: [🔗](class_openxrspatialcomponentplanesemanticlabellist.md#enum-openxrspatialcomponentplanesemanticlabellist-planesemanticlabel)

<a id="class-openxrspatialcomponentplanesemanticlabellist-constant-plane-semantic-label-uncategorized"></a>

[PlaneSemanticLabel](class_openxrspatialcomponentplanesemanticlabellist.md#enum-openxrspatialcomponentplanesemanticlabellist-planesemanticlabel) **PLANE_SEMANTIC_LABEL_UNCATEGORIZED** = `1`

Uncategorized plane.

<a id="class-openxrspatialcomponentplanesemanticlabellist-constant-plane-semantic-label-floor"></a>

[PlaneSemanticLabel](class_openxrspatialcomponentplanesemanticlabellist.md#enum-openxrspatialcomponentplanesemanticlabellist-planesemanticlabel) **PLANE_SEMANTIC_LABEL_FLOOR** = `2`

Plane represents a floor.

<a id="class-openxrspatialcomponentplanesemanticlabellist-constant-plane-semantic-label-wall"></a>

[PlaneSemanticLabel](class_openxrspatialcomponentplanesemanticlabellist.md#enum-openxrspatialcomponentplanesemanticlabellist-planesemanticlabel) **PLANE_SEMANTIC_LABEL_WALL** = `3`

Plane represents a wall.

<a id="class-openxrspatialcomponentplanesemanticlabellist-constant-plane-semantic-label-ceiling"></a>

[PlaneSemanticLabel](class_openxrspatialcomponentplanesemanticlabellist.md#enum-openxrspatialcomponentplanesemanticlabellist-planesemanticlabel) **PLANE_SEMANTIC_LABEL_CEILING** = `4`

Plane represents a ceiling.

<a id="class-openxrspatialcomponentplanesemanticlabellist-constant-plane-semantic-label-table"></a>

[PlaneSemanticLabel](class_openxrspatialcomponentplanesemanticlabellist.md#enum-openxrspatialcomponentplanesemanticlabellist-planesemanticlabel) **PLANE_SEMANTIC_LABEL_TABLE** = `5`

Plane represents the surface of a table.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-openxrspatialcomponentplanesemanticlabellist-method-get-plane-semantic-label"></a>

[PlaneSemanticLabel](class_openxrspatialcomponentplanesemanticlabellist.md#enum-openxrspatialcomponentplanesemanticlabellist-planesemanticlabel) **get_plane_semantic_label**(index: [int](class_int.md#class-int)) const [🔗](class_openxrspatialcomponentplanesemanticlabellist.md#class-openxrspatialcomponentplanesemanticlabellist-method-get-plane-semantic-label)

Returns the plane semantic label for the parent entity at this `index`.
