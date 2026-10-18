> Source: https://docs.godotengine.org/en/4.7/classes/class_openxrspatialcapabilityconfigurationanchor.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxrspatialcapabilityconfigurationanchor"></a>

<a id="class-openxrspatialcapabilityconfigurationanchor"></a>

# OpenXRSpatialCapabilityConfigurationAnchor

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialCapabilityConfigurationBaseHeader](class_openxrspatialcapabilityconfigurationbaseheader.md#class-openxrspatialcapabilityconfigurationbaseheader) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Configuration header for spatial anchors.

<a id="description"></a>

## Description

Configuration header for spatial anchors. Pass this to [OpenXRSpatialEntityExtension.create_spatial_context()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-create-spatial-context) to create a spatial context with spatial anchor capabilities.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [PackedInt64Array](class_packedint64array.md#class-packedint64array) | [get_enabled_components](class_openxrspatialcapabilityconfigurationanchor.md#class-openxrspatialcapabilityconfigurationanchor-method-get-enabled-components)() const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-openxrspatialcapabilityconfigurationanchor-method-get-enabled-components"></a>

[PackedInt64Array](class_packedint64array.md#class-packedint64array) **get_enabled_components**() const [🔗](class_openxrspatialcapabilityconfigurationanchor.md#class-openxrspatialcapabilityconfigurationanchor-method-get-enabled-components)

Returns the components enabled by this configuration.

**Note:** Only valid after this configuration was used to create a spatial context.
