> Source: https://docs.godotengine.org/en/4.7/classes/class_openxrspatialcomponentdata.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxrspatialcomponentdata"></a>

<a id="class-openxrspatialcomponentdata"></a>

# OpenXRSpatialComponentData

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [OpenXRSpatialComponentAnchorList](class_openxrspatialcomponentanchorlist.md#class-openxrspatialcomponentanchorlist), [OpenXRSpatialComponentBounded2DList](class_openxrspatialcomponentbounded2dlist.md#class-openxrspatialcomponentbounded2dlist), [OpenXRSpatialComponentBounded3DList](class_openxrspatialcomponentbounded3dlist.md#class-openxrspatialcomponentbounded3dlist), [OpenXRSpatialComponentMarkerList](class_openxrspatialcomponentmarkerlist.md#class-openxrspatialcomponentmarkerlist), [OpenXRSpatialComponentMesh2DList](class_openxrspatialcomponentmesh2dlist.md#class-openxrspatialcomponentmesh2dlist), [OpenXRSpatialComponentMesh3DList](class_openxrspatialcomponentmesh3dlist.md#class-openxrspatialcomponentmesh3dlist), [OpenXRSpatialComponentParentList](class_openxrspatialcomponentparentlist.md#class-openxrspatialcomponentparentlist), [OpenXRSpatialComponentPersistenceList](class_openxrspatialcomponentpersistencelist.md#class-openxrspatialcomponentpersistencelist), [OpenXRSpatialComponentPlaneAlignmentList](class_openxrspatialcomponentplanealignmentlist.md#class-openxrspatialcomponentplanealignmentlist), [OpenXRSpatialComponentPlaneSemanticLabelList](class_openxrspatialcomponentplanesemanticlabellist.md#class-openxrspatialcomponentplanesemanticlabellist), [OpenXRSpatialComponentPolygon2DList](class_openxrspatialcomponentpolygon2dlist.md#class-openxrspatialcomponentpolygon2dlist), [OpenXRSpatialQueryResultData](class_openxrspatialqueryresultdata.md#class-openxrspatialqueryresultdata)

Object for storing OpenXR spatial entity component data.

<a id="description"></a>

## Description

Object for storing OpenXR spatial entity component data.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [int](class_int.md#class-int) | [_get_component_type](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata-private-method-get-component-type)() virtual const |
| [int](class_int.md#class-int) | [_get_structure_data](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata-private-method-get-structure-data)(next: [int](class_int.md#class-int)) virtual |
| void | [_set_capacity](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata-private-method-set-capacity)(capacity: [int](class_int.md#class-int)) virtual |
| [int](class_int.md#class-int) | [get_component_type](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata-method-get-component-type)() const |
| void | [set_capacity](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata-method-set-capacity)(capacity: [int](class_int.md#class-int)) |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-openxrspatialcomponentdata-private-method-get-component-type"></a>

[int](class_int.md#class-int) **_get_component_type**() virtual const [🔗](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata-private-method-get-component-type)

Return the component type for the component we store data for.

---


<a id="class-openxrspatialcomponentdata-private-method-get-structure-data"></a>

[int](class_int.md#class-int) **_get_structure_data**(next: [int](class_int.md#class-int)) virtual [🔗](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata-private-method-get-structure-data)

Return a pointer to the structure data that will be submitted along with the snapshot query. This pointer must remain valid as long as this object is instantiated.

---


<a id="class-openxrspatialcomponentdata-private-method-set-capacity"></a>

void **_set_capacity**(capacity: [int](class_int.md#class-int)) virtual [🔗](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata-private-method-set-capacity)

Sets the expected capacity as provided by the spatial entities query system. Buffers should be initialized with the correct storage.

---


<a id="class-openxrspatialcomponentdata-method-get-component-type"></a>

[int](class_int.md#class-int) **get_component_type**() const [🔗](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata-method-get-component-type)

Gets this **OpenXRSpatialComponentData**'s `XrSpatialComponentTypeEXT`.

---


<a id="class-openxrspatialcomponentdata-method-set-capacity"></a>

void **set_capacity**(capacity: [int](class_int.md#class-int)) [🔗](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata-method-set-capacity)

Sets the expected capacity as provided by the spatial entities query system. Buffers should be initialized with the correct storage.
