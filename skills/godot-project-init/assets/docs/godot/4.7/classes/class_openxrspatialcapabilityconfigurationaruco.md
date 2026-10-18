> Source: https://docs.godotengine.org/en/4.7/classes/class_openxrspatialcapabilityconfigurationaruco.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxrspatialcapabilityconfigurationaruco"></a>

<a id="class-openxrspatialcapabilityconfigurationaruco"></a>

# OpenXRSpatialCapabilityConfigurationAruco

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialCapabilityConfigurationBaseHeader](class_openxrspatialcapabilityconfigurationbaseheader.md#class-openxrspatialcapabilityconfigurationbaseheader) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Configuration header for Aruco markers.

<a id="description"></a>

## Description

Configuration header for Aruco markers. Pass this to [OpenXRSpatialEntityExtension.create_spatial_context()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-create-spatial-context) to create a spatial context that can detect Aruco markers.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [ArucoDict](class_openxrspatialcapabilityconfigurationaruco.md#enum-openxrspatialcapabilityconfigurationaruco-arucodict) | [aruco_dict](class_openxrspatialcapabilityconfigurationaruco.md#class-openxrspatialcapabilityconfigurationaruco-property-aruco-dict) | `16` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [PackedInt64Array](class_packedint64array.md#class-packedint64array) | [get_enabled_components](class_openxrspatialcapabilityconfigurationaruco.md#class-openxrspatialcapabilityconfigurationaruco-method-get-enabled-components)() const |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-openxrspatialcapabilityconfigurationaruco-arucodict"></a>

enum **ArucoDict**: [🔗](class_openxrspatialcapabilityconfigurationaruco.md#enum-openxrspatialcapabilityconfigurationaruco-arucodict)

<a id="class-openxrspatialcapabilityconfigurationaruco-constant-aruco-dict-4x4-50"></a>

[ArucoDict](class_openxrspatialcapabilityconfigurationaruco.md#enum-openxrspatialcapabilityconfigurationaruco-arucodict) **ARUCO_DICT_4X4_50** = `1`

4 by 4 pixel Aruco marker dictionary with 50 IDs.

<a id="class-openxrspatialcapabilityconfigurationaruco-constant-aruco-dict-4x4-100"></a>

[ArucoDict](class_openxrspatialcapabilityconfigurationaruco.md#enum-openxrspatialcapabilityconfigurationaruco-arucodict) **ARUCO_DICT_4X4_100** = `2`

4 by 4 pixel Aruco marker dictionary with 100 IDs.

<a id="class-openxrspatialcapabilityconfigurationaruco-constant-aruco-dict-4x4-250"></a>

[ArucoDict](class_openxrspatialcapabilityconfigurationaruco.md#enum-openxrspatialcapabilityconfigurationaruco-arucodict) **ARUCO_DICT_4X4_250** = `3`

4 by 4 pixel Aruco marker dictionary with 250 IDs.

<a id="class-openxrspatialcapabilityconfigurationaruco-constant-aruco-dict-4x4-1000"></a>

[ArucoDict](class_openxrspatialcapabilityconfigurationaruco.md#enum-openxrspatialcapabilityconfigurationaruco-arucodict) **ARUCO_DICT_4X4_1000** = `4`

4 by 4 pixel Aruco marker dictionary with 1000 IDs.

<a id="class-openxrspatialcapabilityconfigurationaruco-constant-aruco-dict-5x5-50"></a>

[ArucoDict](class_openxrspatialcapabilityconfigurationaruco.md#enum-openxrspatialcapabilityconfigurationaruco-arucodict) **ARUCO_DICT_5X5_50** = `5`

5 by 5 pixel Aruco marker dictionary with 50 IDs.

<a id="class-openxrspatialcapabilityconfigurationaruco-constant-aruco-dict-5x5-100"></a>

[ArucoDict](class_openxrspatialcapabilityconfigurationaruco.md#enum-openxrspatialcapabilityconfigurationaruco-arucodict) **ARUCO_DICT_5X5_100** = `6`

5 by 5 pixel Aruco marker dictionary with 100 IDs.

<a id="class-openxrspatialcapabilityconfigurationaruco-constant-aruco-dict-5x5-250"></a>

[ArucoDict](class_openxrspatialcapabilityconfigurationaruco.md#enum-openxrspatialcapabilityconfigurationaruco-arucodict) **ARUCO_DICT_5X5_250** = `7`

5 by 5 pixel Aruco marker dictionary with 250 IDs.

<a id="class-openxrspatialcapabilityconfigurationaruco-constant-aruco-dict-5x5-1000"></a>

[ArucoDict](class_openxrspatialcapabilityconfigurationaruco.md#enum-openxrspatialcapabilityconfigurationaruco-arucodict) **ARUCO_DICT_5X5_1000** = `8`

5 by 5 pixel Aruco marker dictionary with 1000 IDs.

<a id="class-openxrspatialcapabilityconfigurationaruco-constant-aruco-dict-6x6-50"></a>

[ArucoDict](class_openxrspatialcapabilityconfigurationaruco.md#enum-openxrspatialcapabilityconfigurationaruco-arucodict) **ARUCO_DICT_6X6_50** = `9`

6 by 6 pixel Aruco marker dictionary with 50 IDs.

<a id="class-openxrspatialcapabilityconfigurationaruco-constant-aruco-dict-6x6-100"></a>

[ArucoDict](class_openxrspatialcapabilityconfigurationaruco.md#enum-openxrspatialcapabilityconfigurationaruco-arucodict) **ARUCO_DICT_6X6_100** = `10`

6 by 6 pixel Aruco marker dictionary with 100 IDs.

<a id="class-openxrspatialcapabilityconfigurationaruco-constant-aruco-dict-6x6-250"></a>

[ArucoDict](class_openxrspatialcapabilityconfigurationaruco.md#enum-openxrspatialcapabilityconfigurationaruco-arucodict) **ARUCO_DICT_6X6_250** = `11`

6 by 6 pixel Aruco marker dictionary with 250 IDs.

<a id="class-openxrspatialcapabilityconfigurationaruco-constant-aruco-dict-6x6-1000"></a>

[ArucoDict](class_openxrspatialcapabilityconfigurationaruco.md#enum-openxrspatialcapabilityconfigurationaruco-arucodict) **ARUCO_DICT_6X6_1000** = `12`

6 by 6 pixel Aruco marker dictionary with 1000 IDs.

<a id="class-openxrspatialcapabilityconfigurationaruco-constant-aruco-dict-7x7-50"></a>

[ArucoDict](class_openxrspatialcapabilityconfigurationaruco.md#enum-openxrspatialcapabilityconfigurationaruco-arucodict) **ARUCO_DICT_7X7_50** = `13`

7 by 7 pixel Aruco marker dictionary with 50 IDs.

<a id="class-openxrspatialcapabilityconfigurationaruco-constant-aruco-dict-7x7-100"></a>

[ArucoDict](class_openxrspatialcapabilityconfigurationaruco.md#enum-openxrspatialcapabilityconfigurationaruco-arucodict) **ARUCO_DICT_7X7_100** = `14`

7 by 7 pixel Aruco marker dictionary with 100 IDs.

<a id="class-openxrspatialcapabilityconfigurationaruco-constant-aruco-dict-7x7-250"></a>

[ArucoDict](class_openxrspatialcapabilityconfigurationaruco.md#enum-openxrspatialcapabilityconfigurationaruco-arucodict) **ARUCO_DICT_7X7_250** = `15`

7 by 7 pixel Aruco marker dictionary with 250 IDs.

<a id="class-openxrspatialcapabilityconfigurationaruco-constant-aruco-dict-7x7-1000"></a>

[ArucoDict](class_openxrspatialcapabilityconfigurationaruco.md#enum-openxrspatialcapabilityconfigurationaruco-arucodict) **ARUCO_DICT_7X7_1000** = `16`

7 by 7 pixel Aruco marker dictionary with 1000 IDs.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-openxrspatialcapabilityconfigurationaruco-property-aruco-dict"></a>

[ArucoDict](class_openxrspatialcapabilityconfigurationaruco.md#enum-openxrspatialcapabilityconfigurationaruco-arucodict) **aruco_dict** = `16` [🔗](class_openxrspatialcapabilityconfigurationaruco.md#class-openxrspatialcapabilityconfigurationaruco-property-aruco-dict)

- void **set_aruco_dict**(value: [ArucoDict](class_openxrspatialcapabilityconfigurationaruco.md#enum-openxrspatialcapabilityconfigurationaruco-arucodict))
- [ArucoDict](class_openxrspatialcapabilityconfigurationaruco.md#enum-openxrspatialcapabilityconfigurationaruco-arucodict) **get_aruco_dict**()

Dictionary to use to decode Aruco markers.

**Note:** Must be set before using this configuration to create a spatial context.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-openxrspatialcapabilityconfigurationaruco-method-get-enabled-components"></a>

[PackedInt64Array](class_packedint64array.md#class-packedint64array) **get_enabled_components**() const [🔗](class_openxrspatialcapabilityconfigurationaruco.md#class-openxrspatialcapabilityconfigurationaruco-method-get-enabled-components)

Returns the components enabled by this configuration.

**Note:** Only valid after this configuration was used to create a spatial context.
