> Source: https://docs.godotengine.org/en/4.7/classes/class_openxrspatialcomponentpersistencelist.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxrspatialcomponentpersistencelist"></a>

<a id="class-openxrspatialcomponentpersistencelist"></a>

# OpenXRSpatialComponentPersistenceList

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Object for storing the query persistence result data.

<a id="description"></a>

## Description

Object for storing the query persistence result data when calling [OpenXRSpatialEntityExtension.query_snapshot()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-query-snapshot).

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [int](class_int.md#class-int) | [get_persistent_state](class_openxrspatialcomponentpersistencelist.md#class-openxrspatialcomponentpersistencelist-method-get-persistent-state)(index: [int](class_int.md#class-int)) const |
| [String](class_string.md#class-string) | [get_persistent_uuid](class_openxrspatialcomponentpersistencelist.md#class-openxrspatialcomponentpersistencelist-method-get-persistent-uuid)(index: [int](class_int.md#class-int)) const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-openxrspatialcomponentpersistencelist-method-get-persistent-state"></a>

[int](class_int.md#class-int) **get_persistent_state**(index: [int](class_int.md#class-int)) const [🔗](class_openxrspatialcomponentpersistencelist.md#class-openxrspatialcomponentpersistencelist-method-get-persistent-state)

Returns the persistent state (`XrSpatialPersistenceStateEXT`) for the entity at this `index`.

---


<a id="class-openxrspatialcomponentpersistencelist-method-get-persistent-uuid"></a>

[String](class_string.md#class-string) **get_persistent_uuid**(index: [int](class_int.md#class-int)) const [🔗](class_openxrspatialcomponentpersistencelist.md#class-openxrspatialcomponentpersistencelist-method-get-persistent-uuid)

Returns the persistent uuid for the entity at this `index`.
