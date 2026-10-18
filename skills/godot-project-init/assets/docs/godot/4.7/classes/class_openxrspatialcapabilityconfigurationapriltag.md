> Source: https://docs.godotengine.org/en/4.7/classes/class_openxrspatialcapabilityconfigurationapriltag.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxrspatialcapabilityconfigurationapriltag"></a>

<a id="class-openxrspatialcapabilityconfigurationapriltag"></a>

# OpenXRSpatialCapabilityConfigurationAprilTag

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialCapabilityConfigurationBaseHeader](class_openxrspatialcapabilityconfigurationbaseheader.md#class-openxrspatialcapabilityconfigurationbaseheader) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Configuration header for April tag markers.

<a id="description"></a>

## Description

Configuration header for April tag markers. Pass this to [OpenXRSpatialEntityExtension.create_spatial_context()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-create-spatial-context) to create a spatial context that can detect April tags.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [AprilTagDict](class_openxrspatialcapabilityconfigurationapriltag.md#enum-openxrspatialcapabilityconfigurationapriltag-apriltagdict) | [april_dict](class_openxrspatialcapabilityconfigurationapriltag.md#class-openxrspatialcapabilityconfigurationapriltag-property-april-dict) | `4` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [PackedInt64Array](class_packedint64array.md#class-packedint64array) | [get_enabled_components](class_openxrspatialcapabilityconfigurationapriltag.md#class-openxrspatialcapabilityconfigurationapriltag-method-get-enabled-components)() const |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-openxrspatialcapabilityconfigurationapriltag-apriltagdict"></a>

enum **AprilTagDict**: [🔗](class_openxrspatialcapabilityconfigurationapriltag.md#enum-openxrspatialcapabilityconfigurationapriltag-apriltagdict)

<a id="class-openxrspatialcapabilityconfigurationapriltag-constant-april-tag-dict-16h5"></a>

[AprilTagDict](class_openxrspatialcapabilityconfigurationapriltag.md#enum-openxrspatialcapabilityconfigurationapriltag-apriltagdict) **APRIL_TAG_DICT_16H5** = `1`

4 by 4 bits, minimum Hamming distance between any two codes = 5, 30 codes.

<a id="class-openxrspatialcapabilityconfigurationapriltag-constant-april-tag-dict-25h9"></a>

[AprilTagDict](class_openxrspatialcapabilityconfigurationapriltag.md#enum-openxrspatialcapabilityconfigurationapriltag-apriltagdict) **APRIL_TAG_DICT_25H9** = `2`

5 by 5 bits, minimum Hamming distance between any two codes = 9, 35 codes.

<a id="class-openxrspatialcapabilityconfigurationapriltag-constant-april-tag-dict-36h10"></a>

[AprilTagDict](class_openxrspatialcapabilityconfigurationapriltag.md#enum-openxrspatialcapabilityconfigurationapriltag-apriltagdict) **APRIL_TAG_DICT_36H10** = `3`

6 by 6 bits, minimum Hamming distance between any two codes = 10, 2320 codes.

<a id="class-openxrspatialcapabilityconfigurationapriltag-constant-april-tag-dict-36h11"></a>

[AprilTagDict](class_openxrspatialcapabilityconfigurationapriltag.md#enum-openxrspatialcapabilityconfigurationapriltag-apriltagdict) **APRIL_TAG_DICT_36H11** = `4`

6 by 6 bits, minimum Hamming distance between any two codes = 11, 587 codes.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-openxrspatialcapabilityconfigurationapriltag-property-april-dict"></a>

[AprilTagDict](class_openxrspatialcapabilityconfigurationapriltag.md#enum-openxrspatialcapabilityconfigurationapriltag-apriltagdict) **april_dict** = `4` [🔗](class_openxrspatialcapabilityconfigurationapriltag.md#class-openxrspatialcapabilityconfigurationapriltag-property-april-dict)

- void **set_april_dict**(value: [AprilTagDict](class_openxrspatialcapabilityconfigurationapriltag.md#enum-openxrspatialcapabilityconfigurationapriltag-apriltagdict))
- [AprilTagDict](class_openxrspatialcapabilityconfigurationapriltag.md#enum-openxrspatialcapabilityconfigurationapriltag-apriltagdict) **get_april_dict**()

Dictionary to use to decode April tags.

**Note:** Must be set before using this configuration to create a spatial context.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-openxrspatialcapabilityconfigurationapriltag-method-get-enabled-components"></a>

[PackedInt64Array](class_packedint64array.md#class-packedint64array) **get_enabled_components**() const [🔗](class_openxrspatialcapabilityconfigurationapriltag.md#class-openxrspatialcapabilityconfigurationapriltag-method-get-enabled-components)

Returns the components enabled by this configuration.

**Note:** Only valid after this configuration was used to create a spatial context.
