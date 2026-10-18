> Source: https://docs.godotengine.org/en/4.7/classes/class_openxrmarkertracker.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxrmarkertracker"></a>

<a id="class-openxrmarkertracker"></a>

# OpenXRMarkerTracker

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialEntityTracker](class_openxrspatialentitytracker.md#class-openxrspatialentitytracker) **<** [XRPositionalTracker](class_xrpositionaltracker.md#class-xrpositionaltracker) **<** [XRTracker](class_xrtracker.md#class-xrtracker) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Spatial entity tracker for our spatial entity marker tracking extension.

<a id="description"></a>

## Description

Spatial entity tracker for our OpenXR spatial entity marker tracking extension. These trackers identify entities in our real space detected by a visual marker such as a QRCode or Aruco code, and map their location to our virtual space.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Vector2](class_vector2.md#class-vector2) | [bounds_size](class_openxrmarkertracker.md#class-openxrmarkertracker-property-bounds-size) | `Vector2(0, 0)` |
| [int](class_int.md#class-int) | [marker_id](class_openxrmarkertracker.md#class-openxrmarkertracker-property-marker-id) | `0` |
| [MarkerType](class_openxrspatialcomponentmarkerlist.md#enum-openxrspatialcomponentmarkerlist-markertype) | [marker_type](class_openxrmarkertracker.md#class-openxrmarkertracker-property-marker-type) | `0` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Variant](class_variant.md#class-variant) | [get_marker_data](class_openxrmarkertracker.md#class-openxrmarkertracker-method-get-marker-data)() const |
| void | [set_marker_data](class_openxrmarkertracker.md#class-openxrmarkertracker-method-set-marker-data)(marker_data: [Variant](class_variant.md#class-variant)) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-openxrmarkertracker-property-bounds-size"></a>

[Vector2](class_vector2.md#class-vector2) **bounds_size** = `Vector2(0, 0)` [🔗](class_openxrmarkertracker.md#class-openxrmarkertracker-property-bounds-size)

- void **set_bounds_size**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_bounds_size**()

The bounds size for this marker.

---


<a id="class-openxrmarkertracker-property-marker-id"></a>

[int](class_int.md#class-int) **marker_id** = `0` [🔗](class_openxrmarkertracker.md#class-openxrmarkertracker-property-marker-id)

- void **set_marker_id**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_marker_id**()

The marker ID for this marker, this is only returned for Aruco and April Tag markers. Call [get_marker_data()](class_openxrmarkertracker.md#class-openxrmarkertracker-method-get-marker-data) for QRCode markers.

---


<a id="class-openxrmarkertracker-property-marker-type"></a>

[MarkerType](class_openxrspatialcomponentmarkerlist.md#enum-openxrspatialcomponentmarkerlist-markertype) **marker_type** = `0` [🔗](class_openxrmarkertracker.md#class-openxrmarkertracker-property-marker-type)

- void **set_marker_type**(value: [MarkerType](class_openxrspatialcomponentmarkerlist.md#enum-openxrspatialcomponentmarkerlist-markertype))
- [MarkerType](class_openxrspatialcomponentmarkerlist.md#enum-openxrspatialcomponentmarkerlist-markertype) **get_marker_type**()

The type of marker.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-openxrmarkertracker-method-get-marker-data"></a>

[Variant](class_variant.md#class-variant) **get_marker_data**() const [🔗](class_openxrmarkertracker.md#class-openxrmarkertracker-method-get-marker-data)

Returns the marker data for this marker. This can return a [String](class_string.md#class-string) or [PackedByteArray](class_packedbytearray.md#class-packedbytearray). Only applicable to QR Code based markers.

---


<a id="class-openxrmarkertracker-method-set-marker-data"></a>

void **set_marker_data**(marker_data: [Variant](class_variant.md#class-variant)) [🔗](class_openxrmarkertracker.md#class-openxrmarkertracker-method-set-marker-data)

Sets the marker data for this marker.

**Note:** This should only be set by marker discovery logic.
