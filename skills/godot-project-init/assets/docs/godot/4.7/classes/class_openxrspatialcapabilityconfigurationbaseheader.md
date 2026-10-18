> Source: https://docs.godotengine.org/en/4.7/classes/class_openxrspatialcapabilityconfigurationbaseheader.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxrspatialcapabilityconfigurationbaseheader"></a>

<a id="class-openxrspatialcapabilityconfigurationbaseheader"></a>

# OpenXRSpatialCapabilityConfigurationBaseHeader

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [OpenXRSpatialCapabilityConfigurationAnchor](class_openxrspatialcapabilityconfigurationanchor.md#class-openxrspatialcapabilityconfigurationanchor), [OpenXRSpatialCapabilityConfigurationAprilTag](class_openxrspatialcapabilityconfigurationapriltag.md#class-openxrspatialcapabilityconfigurationapriltag), [OpenXRSpatialCapabilityConfigurationAruco](class_openxrspatialcapabilityconfigurationaruco.md#class-openxrspatialcapabilityconfigurationaruco), [OpenXRSpatialCapabilityConfigurationMicroQrCode](class_openxrspatialcapabilityconfigurationmicroqrcode.md#class-openxrspatialcapabilityconfigurationmicroqrcode), [OpenXRSpatialCapabilityConfigurationPlaneTracking](class_openxrspatialcapabilityconfigurationplanetracking.md#class-openxrspatialcapabilityconfigurationplanetracking), [OpenXRSpatialCapabilityConfigurationQrCode](class_openxrspatialcapabilityconfigurationqrcode.md#class-openxrspatialcapabilityconfigurationqrcode)

Wrapper base class for OpenXR Spatial Capability Configuration headers.

<a id="description"></a>

## Description

Wrapper base class for OpenXR Spatial Capability Configuration headers. This class needs to be implemented for each capability configuration structure usable within OpenXR's spatial entities system.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [int](class_int.md#class-int) | [_get_configuration](class_openxrspatialcapabilityconfigurationbaseheader.md#class-openxrspatialcapabilityconfigurationbaseheader-private-method-get-configuration)() virtual |
| [bool](class_bool.md#class-bool) | [_has_valid_configuration](class_openxrspatialcapabilityconfigurationbaseheader.md#class-openxrspatialcapabilityconfigurationbaseheader-private-method-has-valid-configuration)() virtual const |
| [int](class_int.md#class-int) | [get_configuration](class_openxrspatialcapabilityconfigurationbaseheader.md#class-openxrspatialcapabilityconfigurationbaseheader-method-get-configuration)() |
| [bool](class_bool.md#class-bool) | [has_valid_configuration](class_openxrspatialcapabilityconfigurationbaseheader.md#class-openxrspatialcapabilityconfigurationbaseheader-method-has-valid-configuration)() const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-openxrspatialcapabilityconfigurationbaseheader-private-method-get-configuration"></a>

[int](class_int.md#class-int) **_get_configuration**() virtual [🔗](class_openxrspatialcapabilityconfigurationbaseheader.md#class-openxrspatialcapabilityconfigurationbaseheader-private-method-get-configuration)

Return a pointer (encoded as an `int64_t`) to a struct holding the spatial capability configuration data. The memory for this struct should remain accessible as long as this object remains instantiated.

---


<a id="class-openxrspatialcapabilityconfigurationbaseheader-private-method-has-valid-configuration"></a>

[bool](class_bool.md#class-bool) **_has_valid_configuration**() virtual const [🔗](class_openxrspatialcapabilityconfigurationbaseheader.md#class-openxrspatialcapabilityconfigurationbaseheader-private-method-has-valid-configuration)

Return `true` if this object contains a valid configuration that can be retrieved when calling [_get_configuration()](class_openxrspatialcapabilityconfigurationbaseheader.md#class-openxrspatialcapabilityconfigurationbaseheader-private-method-get-configuration).

---


<a id="class-openxrspatialcapabilityconfigurationbaseheader-method-get-configuration"></a>

[int](class_int.md#class-int) **get_configuration**() [🔗](class_openxrspatialcapabilityconfigurationbaseheader.md#class-openxrspatialcapabilityconfigurationbaseheader-method-get-configuration)

Gets a pointer to the `XrSpatialCapabilityConfigurationBaseHeaderEXT` struct.

**Note:** This method is intended to be used from GDExtensions.

---


<a id="class-openxrspatialcapabilityconfigurationbaseheader-method-has-valid-configuration"></a>

[bool](class_bool.md#class-bool) **has_valid_configuration**() const [🔗](class_openxrspatialcapabilityconfigurationbaseheader.md#class-openxrspatialcapabilityconfigurationbaseheader-method-has-valid-configuration)

Returns `true` if this object contains a valid configuration that can be used when calling [OpenXRSpatialEntityExtension.create_spatial_context()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-create-spatial-context).
