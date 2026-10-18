> Source: https://docs.godotengine.org/en/4.7/classes/class_openxrspatialcomponentmarkerlist.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxrspatialcomponentmarkerlist"></a>

<a id="class-openxrspatialcomponentmarkerlist"></a>

# OpenXRSpatialComponentMarkerList

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Object for storing the queries marker result data.

<a id="description"></a>

## Description

Object for storing the queries marker result data when calling [OpenXRSpatialEntityExtension.query_snapshot()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-query-snapshot).

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Variant](class_variant.md#class-variant) | [get_marker_data](class_openxrspatialcomponentmarkerlist.md#class-openxrspatialcomponentmarkerlist-method-get-marker-data)(snapshot: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_marker_id](class_openxrspatialcomponentmarkerlist.md#class-openxrspatialcomponentmarkerlist-method-get-marker-id)(index: [int](class_int.md#class-int)) const |
| [MarkerType](class_openxrspatialcomponentmarkerlist.md#enum-openxrspatialcomponentmarkerlist-markertype) | [get_marker_type](class_openxrspatialcomponentmarkerlist.md#class-openxrspatialcomponentmarkerlist-method-get-marker-type)(index: [int](class_int.md#class-int)) const |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-openxrspatialcomponentmarkerlist-markertype"></a>

enum **MarkerType**: [🔗](class_openxrspatialcomponentmarkerlist.md#enum-openxrspatialcomponentmarkerlist-markertype)

<a id="class-openxrspatialcomponentmarkerlist-constant-marker-type-unknown"></a>

[MarkerType](class_openxrspatialcomponentmarkerlist.md#enum-openxrspatialcomponentmarkerlist-markertype) **MARKER_TYPE_UNKNOWN** = `0`

Unknown or unset marker type.

<a id="class-openxrspatialcomponentmarkerlist-constant-marker-type-qrcode"></a>

[MarkerType](class_openxrspatialcomponentmarkerlist.md#enum-openxrspatialcomponentmarkerlist-markertype) **MARKER_TYPE_QRCODE** = `1`

Marker based on a QR code.

<a id="class-openxrspatialcomponentmarkerlist-constant-marker-type-micro-qrcode"></a>

[MarkerType](class_openxrspatialcomponentmarkerlist.md#enum-openxrspatialcomponentmarkerlist-markertype) **MARKER_TYPE_MICRO_QRCODE** = `2`

Marker based on a micro QR code.

<a id="class-openxrspatialcomponentmarkerlist-constant-marker-type-aruco"></a>

[MarkerType](class_openxrspatialcomponentmarkerlist.md#enum-openxrspatialcomponentmarkerlist-markertype) **MARKER_TYPE_ARUCO** = `3`

Marker based on an Aruco code.

<a id="class-openxrspatialcomponentmarkerlist-constant-marker-type-april-tag"></a>

[MarkerType](class_openxrspatialcomponentmarkerlist.md#enum-openxrspatialcomponentmarkerlist-markertype) **MARKER_TYPE_APRIL_TAG** = `4`

Marker based on an April Tag.

<a id="class-openxrspatialcomponentmarkerlist-constant-marker-type-max"></a>

[MarkerType](class_openxrspatialcomponentmarkerlist.md#enum-openxrspatialcomponentmarkerlist-markertype) **MARKER_TYPE_MAX** = `5`

Maximum value for this enum.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-openxrspatialcomponentmarkerlist-method-get-marker-data"></a>

[Variant](class_variant.md#class-variant) **get_marker_data**(snapshot: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) const [🔗](class_openxrspatialcomponentmarkerlist.md#class-openxrspatialcomponentmarkerlist-method-get-marker-data)

Returns either a [String](class_string.md#class-string) or a [PackedByteArray](class_packedbytearray.md#class-packedbytearray) buffer with data for the marker at this `index`. Only applicable for QR code markers.

---


<a id="class-openxrspatialcomponentmarkerlist-method-get-marker-id"></a>

[int](class_int.md#class-int) **get_marker_id**(index: [int](class_int.md#class-int)) const [🔗](class_openxrspatialcomponentmarkerlist.md#class-openxrspatialcomponentmarkerlist-method-get-marker-id)

Returns the marker ID for the marker at this `index`. Only applicable for Aruco or April Tag markers.

---


<a id="class-openxrspatialcomponentmarkerlist-method-get-marker-type"></a>

[MarkerType](class_openxrspatialcomponentmarkerlist.md#enum-openxrspatialcomponentmarkerlist-markertype) **get_marker_type**(index: [int](class_int.md#class-int)) const [🔗](class_openxrspatialcomponentmarkerlist.md#class-openxrspatialcomponentmarkerlist-method-get-marker-type)

Returns the marker type for the marker at this `index`.
