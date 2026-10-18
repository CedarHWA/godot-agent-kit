> Source: https://docs.godotengine.org/en/4.7/classes/class_openxrspatialplanetrackingcapability.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxrspatialplanetrackingcapability"></a>

<a id="class-openxrspatialplanetrackingcapability"></a>

# OpenXRSpatialPlaneTrackingCapability

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class-openxrextensionwrapper) **<** [Object](class_object.md#class-object)

Implementation for handling spatial entity plane tracking logic.

<a id="description"></a>

## Description

This class handles the OpenXR plane tracking spatial entity extension.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [is_supported](class_openxrspatialplanetrackingcapability.md#class-openxrspatialplanetrackingcapability-method-is-supported)() |
| [OpenXRFutureResult](class_openxrfutureresult.md#class-openxrfutureresult) | [start_entity_discovery](class_openxrspatialplanetrackingcapability.md#class-openxrspatialplanetrackingcapability-method-start-entity-discovery)(spatial_context: [RID](class_rid.md#class-rid), component_data: [Array](class_array.md#class-array)[[OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata)], next_snapshot_create: [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) = null, next_snapshot_query: [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) = null, user_callback: [Callable](class_callable.md#class-callable) = Callable()) |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-openxrspatialplanetrackingcapability-method-is-supported"></a>

[bool](class_bool.md#class-bool) **is_supported**() [🔗](class_openxrspatialplanetrackingcapability.md#class-openxrspatialplanetrackingcapability-method-is-supported)

Returns `true` if plane tracking is supported by the current device.

---


<a id="class-openxrspatialplanetrackingcapability-method-start-entity-discovery"></a>

[OpenXRFutureResult](class_openxrfutureresult.md#class-openxrfutureresult) **start_entity_discovery**(spatial_context: [RID](class_rid.md#class-rid), component_data: [Array](class_array.md#class-array)[[OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata)], next_snapshot_create: [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) = null, next_snapshot_query: [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) = null, user_callback: [Callable](class_callable.md#class-callable) = Callable()) [🔗](class_openxrspatialplanetrackingcapability.md#class-openxrspatialplanetrackingcapability-method-start-entity-discovery)

Calls [OpenXRSpatialEntityExtension.discover_spatial_entities()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-discover-spatial-entities) and [OpenXRSpatialEntityExtension.query_snapshot()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-query-snapshot) with the plane entities associated with `spatial_context`.

`component_data` are the [OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata)s to discover for this plane capability.

If `next_snapshot_create` is non-null, then pass this to the `next` parameter in [OpenXRSpatialEntityExtension.discover_spatial_entities()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-discover-spatial-entities).

If `next_snapshot_query` is non-null, then pass this to the `next` parameter in [OpenXRSpatialEntityExtension.query_snapshot()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-query-snapshot).

`user_callback`, when non-null, is called with two parameters usually twice. The first parameter is the [RID](class_rid.md#class-rid) of the discovery snapshot and the second parameter is a boolean where `false` indicates the discovery snapshot is about to be processed, and `true` indicates the discovery snapshot has been processed and `component_data` has valid data. The second call is skipped if an error was encountered.

The returned [OpenXRFutureResult](class_openxrfutureresult.md#class-openxrfutureresult) is identical to the return from [OpenXRSpatialEntityExtension.discover_spatial_entities()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-discover-spatial-entities).
