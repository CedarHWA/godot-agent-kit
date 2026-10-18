> Source: https://docs.godotengine.org/en/4.7/classes/class_openxrspatialmarkertrackingcapability.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxrspatialmarkertrackingcapability"></a>

<a id="class-openxrspatialmarkertrackingcapability"></a>

# OpenXRSpatialMarkerTrackingCapability

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class-openxrextensionwrapper) **<** [Object](class_object.md#class-object)

Implementation for handling spatial entity marker tracking logic.

<a id="description"></a>

## Description

This class handles the OpenXR marker tracking spatial entity extension.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [do_entity_update](class_openxrspatialmarkertrackingcapability.md#class-openxrspatialmarkertrackingcapability-method-do-entity-update)(spatial_context: [RID](class_rid.md#class-rid), component_data: [Array](class_array.md#class-array)[[OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata)], next_snapshot_create: [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) = null, next_snapshot_query: [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) = null) |
| [bool](class_bool.md#class-bool) | [is_april_tag_supported](class_openxrspatialmarkertrackingcapability.md#class-openxrspatialmarkertrackingcapability-method-is-april-tag-supported)() |
| [bool](class_bool.md#class-bool) | [is_aruco_supported](class_openxrspatialmarkertrackingcapability.md#class-openxrspatialmarkertrackingcapability-method-is-aruco-supported)() |
| [bool](class_bool.md#class-bool) | [is_micro_qrcode_supported](class_openxrspatialmarkertrackingcapability.md#class-openxrspatialmarkertrackingcapability-method-is-micro-qrcode-supported)() |
| [bool](class_bool.md#class-bool) | [is_qrcode_supported](class_openxrspatialmarkertrackingcapability.md#class-openxrspatialmarkertrackingcapability-method-is-qrcode-supported)() |
| [OpenXRFutureResult](class_openxrfutureresult.md#class-openxrfutureresult) | [start_entity_discovery](class_openxrspatialmarkertrackingcapability.md#class-openxrspatialmarkertrackingcapability-method-start-entity-discovery)(spatial_context: [RID](class_rid.md#class-rid), component_data: [Array](class_array.md#class-array)[[OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata)], next_snapshot_create: [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) = null, next_snapshot_query: [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) = null, user_callback: [Callable](class_callable.md#class-callable) = Callable()) |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-openxrspatialmarkertrackingcapability-method-do-entity-update"></a>

void **do_entity_update**(spatial_context: [RID](class_rid.md#class-rid), component_data: [Array](class_array.md#class-array)[[OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata)], next_snapshot_create: [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) = null, next_snapshot_query: [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) = null) [🔗](class_openxrspatialmarkertrackingcapability.md#class-openxrspatialmarkertrackingcapability-method-do-entity-update)

Calls [OpenXRSpatialEntityExtension.update_spatial_entities()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-update-spatial-entities) and [OpenXRSpatialEntityExtension.query_snapshot()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-query-snapshot) with the marker entities associated with `spatial_context`.

`component_data` are the [OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata)s to update for this marker capability.

If `next_snapshot_create` is non-null, then pass this to the `next` parameter in [OpenXRSpatialEntityExtension.update_spatial_entities()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-update-spatial-entities).

If `next_snapshot_query` is non-null, then pass this to the `next` parameter in [OpenXRSpatialEntityExtension.query_snapshot()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-query-snapshot).

---


<a id="class-openxrspatialmarkertrackingcapability-method-is-april-tag-supported"></a>

[bool](class_bool.md#class-bool) **is_april_tag_supported**() [🔗](class_openxrspatialmarkertrackingcapability.md#class-openxrspatialmarkertrackingcapability-method-is-april-tag-supported)

Returns `true` if April tag marker tracking is supported by the current device.

---


<a id="class-openxrspatialmarkertrackingcapability-method-is-aruco-supported"></a>

[bool](class_bool.md#class-bool) **is_aruco_supported**() [🔗](class_openxrspatialmarkertrackingcapability.md#class-openxrspatialmarkertrackingcapability-method-is-aruco-supported)

Returns `true` if Aruco marker tracking is supported by the current device.

---


<a id="class-openxrspatialmarkertrackingcapability-method-is-micro-qrcode-supported"></a>

[bool](class_bool.md#class-bool) **is_micro_qrcode_supported**() [🔗](class_openxrspatialmarkertrackingcapability.md#class-openxrspatialmarkertrackingcapability-method-is-micro-qrcode-supported)

Returns `true` if micro QR code marker tracking is supported by the current device.

---


<a id="class-openxrspatialmarkertrackingcapability-method-is-qrcode-supported"></a>

[bool](class_bool.md#class-bool) **is_qrcode_supported**() [🔗](class_openxrspatialmarkertrackingcapability.md#class-openxrspatialmarkertrackingcapability-method-is-qrcode-supported)

Returns `true` if QR code marker tracking is supported by the current device.

---


<a id="class-openxrspatialmarkertrackingcapability-method-start-entity-discovery"></a>

[OpenXRFutureResult](class_openxrfutureresult.md#class-openxrfutureresult) **start_entity_discovery**(spatial_context: [RID](class_rid.md#class-rid), component_data: [Array](class_array.md#class-array)[[OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata)], next_snapshot_create: [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) = null, next_snapshot_query: [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) = null, user_callback: [Callable](class_callable.md#class-callable) = Callable()) [🔗](class_openxrspatialmarkertrackingcapability.md#class-openxrspatialmarkertrackingcapability-method-start-entity-discovery)

Calls [OpenXRSpatialEntityExtension.discover_spatial_entities()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-discover-spatial-entities) and [OpenXRSpatialEntityExtension.query_snapshot()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-query-snapshot) with the marker entities associated with `spatial_context`.

`component_data` are the [OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata)s to discover for this marker capability.

If `next_snapshot_create` is non-null, then pass this to the `next` parameter in [OpenXRSpatialEntityExtension.discover_spatial_entities()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-discover-spatial-entities).

If `next_snapshot_query` is non-null, then pass this to the `next` parameter in [OpenXRSpatialEntityExtension.query_snapshot()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-query-snapshot).

`user_callback`, when non-null, is called with two parameters usually twice. The first parameter is the [RID](class_rid.md#class-rid) of the discovery snapshot and the second parameter is a boolean where `false` indicates the discovery snapshot is about to be processed, and `true` indicates the discovery snapshot has been processed and `component_data` has valid data. The second call is skipped if an error was encountered.

The returned [OpenXRFutureResult](class_openxrfutureresult.md#class-openxrfutureresult) is identical to the return from [OpenXRSpatialEntityExtension.discover_spatial_entities()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-discover-spatial-entities).
