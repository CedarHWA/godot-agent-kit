> Source: https://docs.godotengine.org/en/4.7/classes/class_openxrspatialcapabilityconfigurationplanetracking.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxrspatialcapabilityconfigurationplanetracking"></a>

<a id="class-openxrspatialcapabilityconfigurationplanetracking"></a>

# OpenXRSpatialCapabilityConfigurationPlaneTracking

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialCapabilityConfigurationBaseHeader](class_openxrspatialcapabilityconfigurationbaseheader.md#class-openxrspatialcapabilityconfigurationbaseheader) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Configuration header for plane tracking.

<a id="description"></a>

## Description

Configuration header for plane tracking. Pass this to [OpenXRSpatialEntityExtension.create_spatial_context()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-create-spatial-context) to create a spatial context with plane tracking capabilities.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [PackedInt64Array](class_packedint64array.md#class-packedint64array) | [get_enabled_components](class_openxrspatialcapabilityconfigurationplanetracking.md#class-openxrspatialcapabilityconfigurationplanetracking-method-get-enabled-components)() const |
| [bool](class_bool.md#class-bool) | [supports_labels](class_openxrspatialcapabilityconfigurationplanetracking.md#class-openxrspatialcapabilityconfigurationplanetracking-method-supports-labels)() |
| [bool](class_bool.md#class-bool) | [supports_mesh_2d](class_openxrspatialcapabilityconfigurationplanetracking.md#class-openxrspatialcapabilityconfigurationplanetracking-method-supports-mesh-2d)() |
| [bool](class_bool.md#class-bool) | [supports_polygons](class_openxrspatialcapabilityconfigurationplanetracking.md#class-openxrspatialcapabilityconfigurationplanetracking-method-supports-polygons)() |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-openxrspatialcapabilityconfigurationplanetracking-method-get-enabled-components"></a>

[PackedInt64Array](class_packedint64array.md#class-packedint64array) **get_enabled_components**() const [🔗](class_openxrspatialcapabilityconfigurationplanetracking.md#class-openxrspatialcapabilityconfigurationplanetracking-method-get-enabled-components)

Returns the components enabled by this configuration.

**Note:** Only valid after this configuration was used to create a spatial context.

---


<a id="class-openxrspatialcapabilityconfigurationplanetracking-method-supports-labels"></a>

[bool](class_bool.md#class-bool) **supports_labels**() [🔗](class_openxrspatialcapabilityconfigurationplanetracking.md#class-openxrspatialcapabilityconfigurationplanetracking-method-supports-labels)

Returns `true` if we support the plane semantic label component (only valid after the OpenXR session has started). You can query these using the [OpenXRSpatialComponentPlaneSemanticLabelList](class_openxrspatialcomponentplanesemanticlabellist.md#class-openxrspatialcomponentplanesemanticlabellist) data object.

---


<a id="class-openxrspatialcapabilityconfigurationplanetracking-method-supports-mesh-2d"></a>

[bool](class_bool.md#class-bool) **supports_mesh_2d**() [🔗](class_openxrspatialcapabilityconfigurationplanetracking.md#class-openxrspatialcapabilityconfigurationplanetracking-method-supports-mesh-2d)

Returns `true` if we support the mesh 2D component (only valid after the OpenXR session has started). You can query these using the [OpenXRSpatialComponentMesh2DList](class_openxrspatialcomponentmesh2dlist.md#class-openxrspatialcomponentmesh2dlist) data object.

---


<a id="class-openxrspatialcapabilityconfigurationplanetracking-method-supports-polygons"></a>

[bool](class_bool.md#class-bool) **supports_polygons**() [🔗](class_openxrspatialcapabilityconfigurationplanetracking.md#class-openxrspatialcapabilityconfigurationplanetracking-method-supports-polygons)

Returns `true` if we support the polygon 2D component (only valid after the OpenXR session has started). You can query these using the [OpenXRSpatialComponentPolygon2DList](class_openxrspatialcomponentpolygon2dlist.md#class-openxrspatialcomponentpolygon2dlist) data object.
