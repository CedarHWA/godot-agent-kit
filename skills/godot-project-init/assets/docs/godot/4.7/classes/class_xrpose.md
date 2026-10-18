> Source: https://docs.godotengine.org/en/4.7/classes/class_xrpose.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="xrpose"></a>

<a id="class-xrpose"></a>

# XRPose

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

This object contains all data related to a pose on a tracked object.

<a id="description"></a>

## Description

XR runtimes often identify multiple locations on devices such as controllers that are spatially tracked.

Orientation, location, linear velocity and angular velocity are all provided for each pose by the XR runtime. This object contains this state of a pose.

<a id="tutorials"></a>

## Tutorials

- [XR documentation index](../tutorials/xr/index.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Vector3](class_vector3.md#class-vector3) | [angular_velocity](class_xrpose.md#class-xrpose-property-angular-velocity) | `Vector3(0, 0, 0)` |
| [bool](class_bool.md#class-bool) | [has_tracking_data](class_xrpose.md#class-xrpose-property-has-tracking-data) | `false` |
| [Vector3](class_vector3.md#class-vector3) | [linear_velocity](class_xrpose.md#class-xrpose-property-linear-velocity) | `Vector3(0, 0, 0)` |
| [StringName](class_stringname.md#class-stringname) | [name](class_xrpose.md#class-xrpose-property-name) | `&""` |
| [TrackingConfidence](class_xrpose.md#enum-xrpose-trackingconfidence) | [tracking_confidence](class_xrpose.md#class-xrpose-property-tracking-confidence) | `0` |
| [Transform3D](class_transform3d.md#class-transform3d) | [transform](class_xrpose.md#class-xrpose-property-transform) | `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Transform3D](class_transform3d.md#class-transform3d) | [get_adjusted_transform](class_xrpose.md#class-xrpose-method-get-adjusted-transform)() const |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-xrpose-trackingconfidence"></a>

enum **TrackingConfidence**: [🔗](class_xrpose.md#enum-xrpose-trackingconfidence)

<a id="class-xrpose-constant-xr-tracking-confidence-none"></a>

[TrackingConfidence](class_xrpose.md#enum-xrpose-trackingconfidence) **XR_TRACKING_CONFIDENCE_NONE** = `0`

No tracking information is available for this pose.

<a id="class-xrpose-constant-xr-tracking-confidence-low"></a>

[TrackingConfidence](class_xrpose.md#enum-xrpose-trackingconfidence) **XR_TRACKING_CONFIDENCE_LOW** = `1`

Tracking information may be inaccurate or estimated. For example, with inside out tracking this would indicate a controller may be (partially) obscured.

<a id="class-xrpose-constant-xr-tracking-confidence-high"></a>

[TrackingConfidence](class_xrpose.md#enum-xrpose-trackingconfidence) **XR_TRACKING_CONFIDENCE_HIGH** = `2`

Tracking information is considered accurate and up to date.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-xrpose-property-angular-velocity"></a>

[Vector3](class_vector3.md#class-vector3) **angular_velocity** = `Vector3(0, 0, 0)` [🔗](class_xrpose.md#class-xrpose-property-angular-velocity)

- void **set_angular_velocity**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_angular_velocity**()

The angular velocity for this pose.

---


<a id="class-xrpose-property-has-tracking-data"></a>

[bool](class_bool.md#class-bool) **has_tracking_data** = `false` [🔗](class_xrpose.md#class-xrpose-property-has-tracking-data)

- void **set_has_tracking_data**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_has_tracking_data**()

If `true` our tracking data is up to date. If `false` we're no longer receiving new tracking data and our state is whatever that last valid state was.

---


<a id="class-xrpose-property-linear-velocity"></a>

[Vector3](class_vector3.md#class-vector3) **linear_velocity** = `Vector3(0, 0, 0)` [🔗](class_xrpose.md#class-xrpose-property-linear-velocity)

- void **set_linear_velocity**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_linear_velocity**()

The linear velocity of this pose.

---


<a id="class-xrpose-property-name"></a>

[StringName](class_stringname.md#class-stringname) **name** = `&""` [🔗](class_xrpose.md#class-xrpose-property-name)

- void **set_name**(value: [StringName](class_stringname.md#class-stringname))
- [StringName](class_stringname.md#class-stringname) **get_name**()

The name of this pose. Usually, this name is derived from an action map set up by the user. Godot also suggests some pose names that [XRInterface](class_xrinterface.md#class-xrinterface) objects are expected to implement:

- `root` is the root location, often used for tracked objects that do not have further nodes.
- `aim` is the tip of a controller with its orientation pointing outwards, often used for raycasts.
- `grip` is the location where the user grips the controller.
- `skeleton` is the root location for a hand mesh, when using hand tracking and an animated skeleton is supplied by the XR runtime.

---


<a id="class-xrpose-property-tracking-confidence"></a>

[TrackingConfidence](class_xrpose.md#enum-xrpose-trackingconfidence) **tracking_confidence** = `0` [🔗](class_xrpose.md#class-xrpose-property-tracking-confidence)

- void **set_tracking_confidence**(value: [TrackingConfidence](class_xrpose.md#enum-xrpose-trackingconfidence))
- [TrackingConfidence](class_xrpose.md#enum-xrpose-trackingconfidence) **get_tracking_confidence**()

The tracking confidence for this pose, provides insight on how accurate the spatial positioning of this record is.

---


<a id="class-xrpose-property-transform"></a>

[Transform3D](class_transform3d.md#class-transform3d) **transform** = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)` [🔗](class_xrpose.md#class-xrpose-property-transform)

- void **set_transform**(value: [Transform3D](class_transform3d.md#class-transform3d))
- [Transform3D](class_transform3d.md#class-transform3d) **get_transform**()

The transform containing the original and transform as reported by the XR runtime.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-xrpose-method-get-adjusted-transform"></a>

[Transform3D](class_transform3d.md#class-transform3d) **get_adjusted_transform**() const [🔗](class_xrpose.md#class-xrpose-method-get-adjusted-transform)

Returns the [transform](class_xrpose.md#class-xrpose-property-transform) with world scale and our reference frame applied. This is the transform used to position [XRNode3D](class_xrnode3d.md#class-xrnode3d) objects.
