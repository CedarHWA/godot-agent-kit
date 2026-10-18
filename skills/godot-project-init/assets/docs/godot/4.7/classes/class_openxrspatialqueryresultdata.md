> Source: https://docs.godotengine.org/en/4.7/classes/class_openxrspatialqueryresultdata.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxrspatialqueryresultdata"></a>

<a id="class-openxrspatialqueryresultdata"></a>

# OpenXRSpatialQueryResultData

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Object for storing the main query result data.

<a id="description"></a>

## Description

Object for storing the main query result data when calling [OpenXRSpatialEntityExtension.query_snapshot()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-query-snapshot). This must always be the first component requested.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [int](class_int.md#class-int) | [get_capacity](class_openxrspatialqueryresultdata.md#class-openxrspatialqueryresultdata-method-get-capacity)() const |
| [int](class_int.md#class-int) | [get_entity_id](class_openxrspatialqueryresultdata.md#class-openxrspatialqueryresultdata-method-get-entity-id)(index: [int](class_int.md#class-int)) const |
| [EntityTrackingState](class_openxrspatialentitytracker.md#enum-openxrspatialentitytracker-entitytrackingstate) | [get_entity_state](class_openxrspatialqueryresultdata.md#class-openxrspatialqueryresultdata-method-get-entity-state)(index: [int](class_int.md#class-int)) const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-openxrspatialqueryresultdata-method-get-capacity"></a>

[int](class_int.md#class-int) **get_capacity**() const [🔗](class_openxrspatialqueryresultdata.md#class-openxrspatialqueryresultdata-method-get-capacity)

Returns the number of entities that were retrieved.

---


<a id="class-openxrspatialqueryresultdata-method-get-entity-id"></a>

[int](class_int.md#class-int) **get_entity_id**(index: [int](class_int.md#class-int)) const [🔗](class_openxrspatialqueryresultdata.md#class-openxrspatialqueryresultdata-method-get-entity-id)

Returns the entity id (`XrSpatialEntityIdEXT`) for the entity at this `index`.

---


<a id="class-openxrspatialqueryresultdata-method-get-entity-state"></a>

[EntityTrackingState](class_openxrspatialentitytracker.md#enum-openxrspatialentitytracker-entitytrackingstate) **get_entity_state**(index: [int](class_int.md#class-int)) const [🔗](class_openxrspatialqueryresultdata.md#class-openxrspatialqueryresultdata-method-get-entity-state)

Returns the entity state for the entity at this `index`.
