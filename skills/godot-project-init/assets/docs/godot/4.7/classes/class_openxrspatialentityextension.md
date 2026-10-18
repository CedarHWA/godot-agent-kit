> Source: https://docs.godotengine.org/en/4.7/classes/class_openxrspatialentityextension.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxrspatialentityextension"></a>

<a id="class-openxrspatialentityextension"></a>

# OpenXRSpatialEntityExtension

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class-openxrextensionwrapper) **<** [Object](class_object.md#class-object)

OpenXR extension that handles spatial entities.

<a id="description"></a>

## Description

OpenXR extension that handles spatial entities and, when enabled, allows querying those spatial entities. This extension will also automatically manage [XRTracker](class_xrtracker.md#class-xrtracker) objects for static entities.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [RID](class_rid.md#class-rid) | [add_spatial_entity](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-add-spatial-entity)(spatial_context: [RID](class_rid.md#class-rid), entity_id: [int](class_int.md#class-int), entity: [int](class_int.md#class-int)) |
| [OpenXRFutureResult](class_openxrfutureresult.md#class-openxrfutureresult) | [create_spatial_context](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-create-spatial-context)(capability_configurations: [Array](class_array.md#class-array)[[OpenXRSpatialCapabilityConfigurationBaseHeader](class_openxrspatialcapabilityconfigurationbaseheader.md#class-openxrspatialcapabilityconfigurationbaseheader)], next: [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) = null, user_callback: [Callable](class_callable.md#class-callable) = Callable()) |
| [OpenXRFutureResult](class_openxrfutureresult.md#class-openxrfutureresult) | [discover_spatial_entities](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-discover-spatial-entities)(spatial_context: [RID](class_rid.md#class-rid), component_types: [PackedInt64Array](class_packedint64array.md#class-packedint64array), next: [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) = null, user_callback: [Callable](class_callable.md#class-callable) = Callable()) |
| [OpenXRFutureResult](class_openxrfutureresult.md#class-openxrfutureresult) | [discover_spatial_entities_with_component_data](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-discover-spatial-entities-with-component-data)(spatial_context: [RID](class_rid.md#class-rid), component_data: [Array](class_array.md#class-array)[[OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata)], next: [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) = null, user_callback: [Callable](class_callable.md#class-callable) = Callable()) |
| [RID](class_rid.md#class-rid) | [find_spatial_entity](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-find-spatial-entity)(entity_id: [int](class_int.md#class-int)) |
| void | [free_spatial_context](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-free-spatial-context)(spatial_context: [RID](class_rid.md#class-rid)) |
| void | [free_spatial_entity](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-free-spatial-entity)(entity: [RID](class_rid.md#class-rid)) |
| void | [free_spatial_snapshot](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-free-spatial-snapshot)(spatial_snapshot: [RID](class_rid.md#class-rid)) |
| [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) | [get_float_buffer](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-get-float-buffer)(spatial_snapshot: [RID](class_rid.md#class-rid), buffer_id: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_spatial_context_handle](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-get-spatial-context-handle)(spatial_context: [RID](class_rid.md#class-rid)) const |
| [bool](class_bool.md#class-bool) | [get_spatial_context_ready](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-get-spatial-context-ready)(spatial_context: [RID](class_rid.md#class-rid)) const |
| [RID](class_rid.md#class-rid) | [get_spatial_entity_context](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-get-spatial-entity-context)(entity: [RID](class_rid.md#class-rid)) const |
| [int](class_int.md#class-int) | [get_spatial_entity_id](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-get-spatial-entity-id)(entity: [RID](class_rid.md#class-rid)) const |
| [RID](class_rid.md#class-rid) | [get_spatial_snapshot_context](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-get-spatial-snapshot-context)(spatial_snapshot: [RID](class_rid.md#class-rid)) const |
| [int](class_int.md#class-int) | [get_spatial_snapshot_handle](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-get-spatial-snapshot-handle)(spatial_snapshot: [RID](class_rid.md#class-rid)) const |
| [String](class_string.md#class-string) | [get_string](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-get-string)(spatial_snapshot: [RID](class_rid.md#class-rid), buffer_id: [int](class_int.md#class-int)) const |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray) | [get_uint8_buffer](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-get-uint8-buffer)(spatial_snapshot: [RID](class_rid.md#class-rid), buffer_id: [int](class_int.md#class-int)) const |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array) | [get_uint16_buffer](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-get-uint16-buffer)(spatial_snapshot: [RID](class_rid.md#class-rid), buffer_id: [int](class_int.md#class-int)) const |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array) | [get_uint32_buffer](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-get-uint32-buffer)(spatial_snapshot: [RID](class_rid.md#class-rid), buffer_id: [int](class_int.md#class-int)) const |
| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) | [get_vector2_buffer](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-get-vector2-buffer)(spatial_snapshot: [RID](class_rid.md#class-rid), buffer_id: [int](class_int.md#class-int)) const |
| [PackedVector3Array](class_packedvector3array.md#class-packedvector3array) | [get_vector3_buffer](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-get-vector3-buffer)(spatial_snapshot: [RID](class_rid.md#class-rid), buffer_id: [int](class_int.md#class-int)) const |
| [RID](class_rid.md#class-rid) | [make_spatial_entity](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-make-spatial-entity)(spatial_context: [RID](class_rid.md#class-rid), entity_id: [int](class_int.md#class-int)) |
| [bool](class_bool.md#class-bool) | [query_snapshot](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-query-snapshot)(spatial_snapshot: [RID](class_rid.md#class-rid), component_data: [Array](class_array.md#class-array)[[OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata)], next: [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) = null) |
| [bool](class_bool.md#class-bool) | [supports_capability](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-supports-capability)(capability: [Capability](class_openxrspatialentityextension.md#enum-openxrspatialentityextension-capability)) |
| [bool](class_bool.md#class-bool) | [supports_component_type](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-supports-component-type)(capability: [Capability](class_openxrspatialentityextension.md#enum-openxrspatialentityextension-capability), component_type: [ComponentType](class_openxrspatialentityextension.md#enum-openxrspatialentityextension-componenttype)) |
| [RID](class_rid.md#class-rid) | [update_spatial_entities](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-update-spatial-entities)(spatial_context: [RID](class_rid.md#class-rid), entities: [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)], component_types: [PackedInt64Array](class_packedint64array.md#class-packedint64array), next: [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) = null) |

---


<a id="signals"></a>

## Signals

<a id="class-openxrspatialentityextension-signal-spatial-discovery-recommended"></a>

**spatial_discovery_recommended**(spatial_context: [RID](class_rid.md#class-rid)) [🔗](class_openxrspatialentityextension.md#class-openxrspatialentityextension-signal-spatial-discovery-recommended)

Emitted when OpenXR recommends running a discovery query because entities managed by this spatial context have (likely) changed.

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-openxrspatialentityextension-capability"></a>

enum **Capability**: [🔗](class_openxrspatialentityextension.md#enum-openxrspatialentityextension-capability)

<a id="class-openxrspatialentityextension-constant-capability-plane-tracking"></a>

[Capability](class_openxrspatialentityextension.md#enum-openxrspatialentityextension-capability) **CAPABILITY_PLANE_TRACKING** = `1000741000`

Plane tracking capability.

<a id="class-openxrspatialentityextension-constant-capability-marker-tracking-qr-code"></a>

[Capability](class_openxrspatialentityextension.md#enum-openxrspatialentityextension-capability) **CAPABILITY_MARKER_TRACKING_QR_CODE** = `1000743000`

QR code based marker tracking capability.

<a id="class-openxrspatialentityextension-constant-capability-marker-tracking-micro-qr-code"></a>

[Capability](class_openxrspatialentityextension.md#enum-openxrspatialentityextension-capability) **CAPABILITY_MARKER_TRACKING_MICRO_QR_CODE** = `1000743001`

Micro QR code based marker tracking capability.

<a id="class-openxrspatialentityextension-constant-capability-marker-tracking-aruco-marker"></a>

[Capability](class_openxrspatialentityextension.md#enum-openxrspatialentityextension-capability) **CAPABILITY_MARKER_TRACKING_ARUCO_MARKER** = `1000743002`

Aruco marker based marker tracking capability.

<a id="class-openxrspatialentityextension-constant-capability-marker-tracking-april-tag"></a>

[Capability](class_openxrspatialentityextension.md#enum-openxrspatialentityextension-capability) **CAPABILITY_MARKER_TRACKING_APRIL_TAG** = `1000743003`

April tag based marker tracking capability.

<a id="class-openxrspatialentityextension-constant-capability-anchor"></a>

[Capability](class_openxrspatialentityextension.md#enum-openxrspatialentityextension-capability) **CAPABILITY_ANCHOR** = `1000762000`

Anchor capability.

---


<a id="enum-openxrspatialentityextension-componenttype"></a>

enum **ComponentType**: [🔗](class_openxrspatialentityextension.md#enum-openxrspatialentityextension-componenttype)

<a id="class-openxrspatialentityextension-constant-component-type-bounded-2d"></a>

[ComponentType](class_openxrspatialentityextension.md#enum-openxrspatialentityextension-componenttype) **COMPONENT_TYPE_BOUNDED_2D** = `1`

Component that provides the 2D bounds for a spatial entity. The corresponding list structure is `XrSpatialComponentBounded2DListEXT`; the corresponding data structure is `XrSpatialBounded2DDataEXT`.

<a id="class-openxrspatialentityextension-constant-component-type-bounded-3d"></a>

[ComponentType](class_openxrspatialentityextension.md#enum-openxrspatialentityextension-componenttype) **COMPONENT_TYPE_BOUNDED_3D** = `2`

Component that provides the 3D bounds for a spatial entity. The corresponding list structure is `XrSpatialComponentBounded3DListEXT`; the corresponding data structure is `XrBoxf`.

<a id="class-openxrspatialentityextension-constant-component-type-parent"></a>

[ComponentType](class_openxrspatialentityextension.md#enum-openxrspatialentityextension-componenttype) **COMPONENT_TYPE_PARENT** = `3`

Component that provides the XrSpatialEntityIdEXT of the parent for a spatial entity. The corresponding list structure is `XrSpatialComponentParentListEXT`; the corresponding data structure is `XrSpatialEntityIdEXT`.

<a id="class-openxrspatialentityextension-constant-component-type-mesh-3d"></a>

[ComponentType](class_openxrspatialentityextension.md#enum-openxrspatialentityextension-componenttype) **COMPONENT_TYPE_MESH_3D** = `4`

Component that provides a 3D mesh for a spatial entity. The corresponding list structure is `XrSpatialComponentMesh3DListEXT`; the corresponding data structure is `XrSpatialMeshDataEXT`.

<a id="class-openxrspatialentityextension-constant-component-type-plane-alignment"></a>

[ComponentType](class_openxrspatialentityextension.md#enum-openxrspatialentityextension-componenttype) **COMPONENT_TYPE_PLANE_ALIGNMENT** = `1000741000`

Component that provides the plane alignment enum for a spatial entity. The corresponding list structure is `XrSpatialComponentPlaneAlignmentListEXT`; the corresponding data structure is `XrSpatialPlaneAlignmentEXT` (Added by the `XR_EXT_spatial_plane_tracking` extension).

<a id="class-openxrspatialentityextension-constant-component-type-mesh-2d"></a>

[ComponentType](class_openxrspatialentityextension.md#enum-openxrspatialentityextension-componenttype) **COMPONENT_TYPE_MESH_2D** = `1000741001`

Component that provides a 2D mesh for a spatial entity. The corresponding list structure is `XrSpatialComponentMesh2DListEXT`; the corresponding data structure is `XrSpatialMeshDataEXT` (Added by the `XR_EXT_spatial_plane_tracking` extension).

<a id="class-openxrspatialentityextension-constant-component-type-polygon-2d"></a>

[ComponentType](class_openxrspatialentityextension.md#enum-openxrspatialentityextension-componenttype) **COMPONENT_TYPE_POLYGON_2D** = `1000741002`

Component that provides a 2D boundary polygon for a spatial entity. The corresponding list structure is `XrSpatialComponentPolygon2DListEXT`; the corresponding data structure is `XrSpatialPolygon2DDataEXT` (Added by the `XR_EXT_spatial_plane_tracking` extension).

<a id="class-openxrspatialentityextension-constant-component-type-plane-semantic-label"></a>

[ComponentType](class_openxrspatialentityextension.md#enum-openxrspatialentityextension-componenttype) **COMPONENT_TYPE_PLANE_SEMANTIC_LABEL** = `1000741003`

Component that provides a semantic label for a plane. The corresponding list structure is `XrSpatialComponentPlaneSemanticLabelListEXT`; the corresponding data structure is `XrSpatialPlaneSemanticLabelEXT` (Added by the `XR_EXT_spatial_plane_tracking` extension).

<a id="class-openxrspatialentityextension-constant-component-type-marker"></a>

[ComponentType](class_openxrspatialentityextension.md#enum-openxrspatialentityextension-componenttype) **COMPONENT_TYPE_MARKER** = `1000743000`

A component describing the marker type, ID and location. The corresponding list structure is `XrSpatialComponentMarkerListEXT`; the corresponding data structure is `XrSpatialMarkerDataEXT` (Added by the `XR_EXT_spatial_marker_tracking` extension).

<a id="class-openxrspatialentityextension-constant-component-type-anchor"></a>

[ComponentType](class_openxrspatialentityextension.md#enum-openxrspatialentityextension-componenttype) **COMPONENT_TYPE_ANCHOR** = `1000762000`

Component that provides the location for an anchor. The corresponding list structure is `XrSpatialComponentAnchorListEXT`; the corresponding data structure is `XrPosef` (Added by the `XR_EXT_spatial_anchor` extension).

<a id="class-openxrspatialentityextension-constant-component-type-persistence"></a>

[ComponentType](class_openxrspatialentityextension.md#enum-openxrspatialentityextension-componenttype) **COMPONENT_TYPE_PERSISTENCE** = `1000763000`

Component that provides the persisted UUID for a spatial entity. The corresponding list structure is `XrSpatialComponentPersistenceListEXT; the corresponding data structure is [code]XrSpatialPersistenceDataEXT` (Added by the `XR_EXT_spatial_persistence` extension).

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-openxrspatialentityextension-method-add-spatial-entity"></a>

[RID](class_rid.md#class-rid) **add_spatial_entity**(spatial_context: [RID](class_rid.md#class-rid), entity_id: [int](class_int.md#class-int), entity: [int](class_int.md#class-int)) [🔗](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-add-spatial-entity)

Registers an entity that was created directly on the OpenXR runtime.

---


<a id="class-openxrspatialentityextension-method-create-spatial-context"></a>

[OpenXRFutureResult](class_openxrfutureresult.md#class-openxrfutureresult) **create_spatial_context**(capability_configurations: [Array](class_array.md#class-array)[[OpenXRSpatialCapabilityConfigurationBaseHeader](class_openxrspatialcapabilityconfigurationbaseheader.md#class-openxrspatialcapabilityconfigurationbaseheader)], next: [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) = null, user_callback: [Callable](class_callable.md#class-callable) = Callable()) [🔗](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-create-spatial-context)

Creates a new spatial context that handles entities for the provided capability configurations. `capability_configurations` is an array of [OpenXRSpatialCapabilityConfigurationBaseHeader](class_openxrspatialcapabilityconfigurationbaseheader.md#class-openxrspatialcapabilityconfigurationbaseheader) with the needed capability configuration data.

`next` is an optional parameter that can contain additional information for creating our spatial context.

**Note:** This is an asynchronous method and returns an [OpenXRFutureResult](class_openxrfutureresult.md#class-openxrfutureresult) object with which to track the status, discarding this object will not cancel the creation process. On success `user_callback` will be called if specified. The result data for this function is the [RID](class_rid.md#class-rid) for our spatial context.

---


<a id="class-openxrspatialentityextension-method-discover-spatial-entities"></a>

[OpenXRFutureResult](class_openxrfutureresult.md#class-openxrfutureresult) **discover_spatial_entities**(spatial_context: [RID](class_rid.md#class-rid), component_types: [PackedInt64Array](class_packedint64array.md#class-packedint64array), next: [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) = null, user_callback: [Callable](class_callable.md#class-callable) = Callable()) [🔗](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-discover-spatial-entities)

Starts a new discovery query, this will gather all objects tracked by the `spatial_context` that have at least one of the component types specified in `component_types`.

`next` is an optional parameter that can contain additional information for executing the discovery query.

**Note:** This is an asynchronous method and returns an [OpenXRFutureResult](class_openxrfutureresult.md#class-openxrfutureresult) object with which to track the status, discarding this object will not cancel the discovery process. On success `user_callback` will be called if specified. The result data for this function is the [RID](class_rid.md#class-rid) for our snapshot.

---


<a id="class-openxrspatialentityextension-method-discover-spatial-entities-with-component-data"></a>

[OpenXRFutureResult](class_openxrfutureresult.md#class-openxrfutureresult) **discover_spatial_entities_with_component_data**(spatial_context: [RID](class_rid.md#class-rid), component_data: [Array](class_array.md#class-array)[[OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata)], next: [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) = null, user_callback: [Callable](class_callable.md#class-callable) = Callable()) [🔗](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-discover-spatial-entities-with-component-data)

Convenience method when the caller only has an [Array](class_array.md#class-array) of [OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata) and needs to discover spatial entities.

---


<a id="class-openxrspatialentityextension-method-find-spatial-entity"></a>

[RID](class_rid.md#class-rid) **find_spatial_entity**(entity_id: [int](class_int.md#class-int)) [🔗](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-find-spatial-entity)

Returns the [RID](class_rid.md#class-rid) for the specified spatial entity ID.

---


<a id="class-openxrspatialentityextension-method-free-spatial-context"></a>

void **free_spatial_context**(spatial_context: [RID](class_rid.md#class-rid)) [🔗](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-free-spatial-context)

Frees a spatial context previously created when calling [create_spatial_context()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-create-spatial-context). If the spatial context creation is still ongoing, the asynchronous process is cancelled.

---


<a id="class-openxrspatialentityextension-method-free-spatial-entity"></a>

void **free_spatial_entity**(entity: [RID](class_rid.md#class-rid)) [🔗](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-free-spatial-entity)

Frees an entity previously created when calling [add_spatial_entity()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-add-spatial-entity) or [make_spatial_entity()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-make-spatial-entity).

---


<a id="class-openxrspatialentityextension-method-free-spatial-snapshot"></a>

void **free_spatial_snapshot**(spatial_snapshot: [RID](class_rid.md#class-rid)) [🔗](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-free-spatial-snapshot)

Frees a spatial snapshot previously created when calling [discover_spatial_entities()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-discover-spatial-entities). If the spatial snapshot creation is still ongoing, the asynchronous process is cancelled.

---


<a id="class-openxrspatialentityextension-method-get-float-buffer"></a>

[PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) **get_float_buffer**(spatial_snapshot: [RID](class_rid.md#class-rid), buffer_id: [int](class_int.md#class-int)) const [🔗](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-get-float-buffer)

Returns a buffer with floats from a buffer that was retrieved when taking a snapshot.

---


<a id="class-openxrspatialentityextension-method-get-spatial-context-handle"></a>

[int](class_int.md#class-int) **get_spatial_context_handle**(spatial_context: [RID](class_rid.md#class-rid)) const [🔗](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-get-spatial-context-handle)

Returns the OpenXR spatial context handle for this snapshot.

**Note:** This method is intended to be used from GDExtensions that implement spatial entity capability handlers.

---


<a id="class-openxrspatialentityextension-method-get-spatial-context-ready"></a>

[bool](class_bool.md#class-bool) **get_spatial_context_ready**(spatial_context: [RID](class_rid.md#class-rid)) const [🔗](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-get-spatial-context-ready)

Returns `true` if the spatial context finished its creation and is ready to be used.

---


<a id="class-openxrspatialentityextension-method-get-spatial-entity-context"></a>

[RID](class_rid.md#class-rid) **get_spatial_entity_context**(entity: [RID](class_rid.md#class-rid)) const [🔗](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-get-spatial-entity-context)

Returns the spatial context for this entity.

---


<a id="class-openxrspatialentityextension-method-get-spatial-entity-id"></a>

[int](class_int.md#class-int) **get_spatial_entity_id**(entity: [RID](class_rid.md#class-rid)) const [🔗](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-get-spatial-entity-id)

Returns the internal `XrSpatialEntityIdEXT` associated with the entity.

---


<a id="class-openxrspatialentityextension-method-get-spatial-snapshot-context"></a>

[RID](class_rid.md#class-rid) **get_spatial_snapshot_context**(spatial_snapshot: [RID](class_rid.md#class-rid)) const [🔗](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-get-spatial-snapshot-context)

Returns the spatial context related to this spatial snapshot.

---


<a id="class-openxrspatialentityextension-method-get-spatial-snapshot-handle"></a>

[int](class_int.md#class-int) **get_spatial_snapshot_handle**(spatial_snapshot: [RID](class_rid.md#class-rid)) const [🔗](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-get-spatial-snapshot-handle)

Returns the OpenXR spatial snapshot handle for this snapshot.

**Note:** This method is intended to be used from GDExtensions that implement spatial entity capability handlers.

---


<a id="class-openxrspatialentityextension-method-get-string"></a>

[String](class_string.md#class-string) **get_string**(spatial_snapshot: [RID](class_rid.md#class-rid), buffer_id: [int](class_int.md#class-int)) const [🔗](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-get-string)

Returns a string from a buffer that was retrieved when taking a snapshot.

---


<a id="class-openxrspatialentityextension-method-get-uint8-buffer"></a>

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **get_uint8_buffer**(spatial_snapshot: [RID](class_rid.md#class-rid), buffer_id: [int](class_int.md#class-int)) const [🔗](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-get-uint8-buffer)

Returns a buffer with 8 bit ints from a buffer that was retrieved when taking a snapshot.

---


<a id="class-openxrspatialentityextension-method-get-uint16-buffer"></a>

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_uint16_buffer**(spatial_snapshot: [RID](class_rid.md#class-rid), buffer_id: [int](class_int.md#class-int)) const [🔗](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-get-uint16-buffer)

Returns a buffer with 16 bit ints from a buffer that was retrieved when taking a snapshot.

---


<a id="class-openxrspatialentityextension-method-get-uint32-buffer"></a>

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_uint32_buffer**(spatial_snapshot: [RID](class_rid.md#class-rid), buffer_id: [int](class_int.md#class-int)) const [🔗](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-get-uint32-buffer)

Returns a buffer with 32 bit ints from a buffer that was retrieved when taking a snapshot.

---


<a id="class-openxrspatialentityextension-method-get-vector2-buffer"></a>

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **get_vector2_buffer**(spatial_snapshot: [RID](class_rid.md#class-rid), buffer_id: [int](class_int.md#class-int)) const [🔗](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-get-vector2-buffer)

Returns a buffer with [Vector2](class_vector2.md#class-vector2) entries from a buffer that was retrieved when taking a snapshot.

---


<a id="class-openxrspatialentityextension-method-get-vector3-buffer"></a>

[PackedVector3Array](class_packedvector3array.md#class-packedvector3array) **get_vector3_buffer**(spatial_snapshot: [RID](class_rid.md#class-rid), buffer_id: [int](class_int.md#class-int)) const [🔗](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-get-vector3-buffer)

Returns a buffer with [Vector3](class_vector3.md#class-vector3) entries from a buffer that was retrieved when taking a snapshot.

---


<a id="class-openxrspatialentityextension-method-make-spatial-entity"></a>

[RID](class_rid.md#class-rid) **make_spatial_entity**(spatial_context: [RID](class_rid.md#class-rid), entity_id: [int](class_int.md#class-int)) [🔗](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-make-spatial-entity)

Creates a new entity for this `entity_id`. The `spatial_context` should match the context that discovered the entity.

---


<a id="class-openxrspatialentityextension-method-query-snapshot"></a>

[bool](class_bool.md#class-bool) **query_snapshot**(spatial_snapshot: [RID](class_rid.md#class-rid), component_data: [Array](class_array.md#class-array)[[OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata)], next: [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) = null) [🔗](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-query-snapshot)

Queries the snapshot data. This will find all entities in the snapshot that contain all requested components in `component_data`. The objects held within `component_data` will then be populated with the queried data. `component_data` must always have an object of [OpenXRSpatialQueryResultData](class_openxrspatialqueryresultdata.md#class-openxrspatialqueryresultdata) as the first entry.

`next` is an optional parameter that can contain additional information passed when setting our query conditions.

---


<a id="class-openxrspatialentityextension-method-supports-capability"></a>

[bool](class_bool.md#class-bool) **supports_capability**(capability: [Capability](class_openxrspatialentityextension.md#enum-openxrspatialentityextension-capability)) [🔗](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-supports-capability)

Returns `true` if this spatial entity `capability` is supported by the hardware used.

---


<a id="class-openxrspatialentityextension-method-supports-component-type"></a>

[bool](class_bool.md#class-bool) **supports_component_type**(capability: [Capability](class_openxrspatialentityextension.md#enum-openxrspatialentityextension-capability), component_type: [ComponentType](class_openxrspatialentityextension.md#enum-openxrspatialentityextension-componenttype)) [🔗](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-supports-component-type)

Returns `true` if this `capability` supports the `component_type`.

---


<a id="class-openxrspatialentityextension-method-update-spatial-entities"></a>

[RID](class_rid.md#class-rid) **update_spatial_entities**(spatial_context: [RID](class_rid.md#class-rid), entities: [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)], component_types: [PackedInt64Array](class_packedint64array.md#class-packedint64array), next: [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) = null) [🔗](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-update-spatial-entities)

Performs a snapshot for a limited number of entities. This is NOT an asynchronous method and will return the snapshot immediately.
