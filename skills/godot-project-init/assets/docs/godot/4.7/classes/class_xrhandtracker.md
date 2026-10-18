> Source: https://docs.godotengine.org/en/4.7/classes/class_xrhandtracker.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="xrhandtracker"></a>

<a id="class-xrhandtracker"></a>

# XRHandTracker

**Inherits:** [XRPositionalTracker](class_xrpositionaltracker.md#class-xrpositionaltracker) **<** [XRTracker](class_xrtracker.md#class-xrtracker) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A tracked hand in XR.

<a id="description"></a>

## Description

A hand tracking system will create an instance of this object and add it to the [XRServer](class_xrserver.md#class-xrserver). This tracking system will then obtain skeleton data, convert it to the Godot Humanoid hand skeleton and store this data on the **XRHandTracker** object.

Use [XRHandModifier3D](class_xrhandmodifier3d.md#class-xrhandmodifier3d) to animate a hand mesh using hand tracking data.

<a id="tutorials"></a>

## Tutorials

- [XR documentation index](../tutorials/xr/index.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [TrackerHand](class_xrpositionaltracker.md#enum-xrpositionaltracker-trackerhand) | hand | `1` (overrides [XRPositionalTracker](class_xrpositionaltracker.md#class-xrpositionaltracker-property-hand)) |
| [HandTrackingSource](class_xrhandtracker.md#enum-xrhandtracker-handtrackingsource) | [hand_tracking_source](class_xrhandtracker.md#class-xrhandtracker-property-hand-tracking-source) | `0` |
| [bool](class_bool.md#class-bool) | [has_tracking_data](class_xrhandtracker.md#class-xrhandtracker-property-has-tracking-data) | `false` |
| [TrackerType](class_xrserver.md#enum-xrserver-trackertype) | type | `16` (overrides [XRTracker](class_xrtracker.md#class-xrtracker-property-type)) |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Vector3](class_vector3.md#class-vector3) | [get_hand_joint_angular_velocity](class_xrhandtracker.md#class-xrhandtracker-method-get-hand-joint-angular-velocity)(joint: [HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint)) const |
| BitField[[HandJointFlags](class_xrhandtracker.md#enum-xrhandtracker-handjointflags)] | [get_hand_joint_flags](class_xrhandtracker.md#class-xrhandtracker-method-get-hand-joint-flags)(joint: [HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint)) const |
| [Vector3](class_vector3.md#class-vector3) | [get_hand_joint_linear_velocity](class_xrhandtracker.md#class-xrhandtracker-method-get-hand-joint-linear-velocity)(joint: [HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint)) const |
| [float](class_float.md#class-float) | [get_hand_joint_radius](class_xrhandtracker.md#class-xrhandtracker-method-get-hand-joint-radius)(joint: [HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint)) const |
| [Transform3D](class_transform3d.md#class-transform3d) | [get_hand_joint_transform](class_xrhandtracker.md#class-xrhandtracker-method-get-hand-joint-transform)(joint: [HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint)) const |
| void | [set_hand_joint_angular_velocity](class_xrhandtracker.md#class-xrhandtracker-method-set-hand-joint-angular-velocity)(joint: [HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint), angular_velocity: [Vector3](class_vector3.md#class-vector3)) |
| void | [set_hand_joint_flags](class_xrhandtracker.md#class-xrhandtracker-method-set-hand-joint-flags)(joint: [HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint), flags: BitField[[HandJointFlags](class_xrhandtracker.md#enum-xrhandtracker-handjointflags)]) |
| void | [set_hand_joint_linear_velocity](class_xrhandtracker.md#class-xrhandtracker-method-set-hand-joint-linear-velocity)(joint: [HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint), linear_velocity: [Vector3](class_vector3.md#class-vector3)) |
| void | [set_hand_joint_radius](class_xrhandtracker.md#class-xrhandtracker-method-set-hand-joint-radius)(joint: [HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint), radius: [float](class_float.md#class-float)) |
| void | [set_hand_joint_transform](class_xrhandtracker.md#class-xrhandtracker-method-set-hand-joint-transform)(joint: [HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint), transform: [Transform3D](class_transform3d.md#class-transform3d)) |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-xrhandtracker-handtrackingsource"></a>

enum **HandTrackingSource**: [🔗](class_xrhandtracker.md#enum-xrhandtracker-handtrackingsource)

<a id="class-xrhandtracker-constant-hand-tracking-source-unknown"></a>

[HandTrackingSource](class_xrhandtracker.md#enum-xrhandtracker-handtrackingsource) **HAND_TRACKING_SOURCE_UNKNOWN** = `0`

The source of hand tracking data is unknown.

<a id="class-xrhandtracker-constant-hand-tracking-source-unobstructed"></a>

[HandTrackingSource](class_xrhandtracker.md#enum-xrhandtracker-handtrackingsource) **HAND_TRACKING_SOURCE_UNOBSTRUCTED** = `1`

The source of hand tracking data is unobstructed, meaning that an accurate method of hand tracking is used. These include optical hand tracking, data gloves, etc.

<a id="class-xrhandtracker-constant-hand-tracking-source-controller"></a>

[HandTrackingSource](class_xrhandtracker.md#enum-xrhandtracker-handtrackingsource) **HAND_TRACKING_SOURCE_CONTROLLER** = `2`

The source of hand tracking data is a controller, meaning that joint positions are inferred from controller inputs.

<a id="class-xrhandtracker-constant-hand-tracking-source-not-tracked"></a>

[HandTrackingSource](class_xrhandtracker.md#enum-xrhandtracker-handtrackingsource) **HAND_TRACKING_SOURCE_NOT_TRACKED** = `3`

No hand tracking data is tracked, this either means the hand is obscured, the controller is turned off, or tracking is not supported for the current input type.

<a id="class-xrhandtracker-constant-hand-tracking-source-max"></a>

[HandTrackingSource](class_xrhandtracker.md#enum-xrhandtracker-handtrackingsource) **HAND_TRACKING_SOURCE_MAX** = `4`

Represents the size of the [HandTrackingSource](class_xrhandtracker.md#enum-xrhandtracker-handtrackingsource) enum.

---


<a id="enum-xrhandtracker-handjoint"></a>

enum **HandJoint**: [🔗](class_xrhandtracker.md#enum-xrhandtracker-handjoint)

<a id="class-xrhandtracker-constant-hand-joint-palm"></a>

[HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint) **HAND_JOINT_PALM** = `0`

Palm joint.

<a id="class-xrhandtracker-constant-hand-joint-wrist"></a>

[HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint) **HAND_JOINT_WRIST** = `1`

Wrist joint.

<a id="class-xrhandtracker-constant-hand-joint-thumb-metacarpal"></a>

[HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint) **HAND_JOINT_THUMB_METACARPAL** = `2`

Thumb metacarpal joint.

<a id="class-xrhandtracker-constant-hand-joint-thumb-phalanx-proximal"></a>

[HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint) **HAND_JOINT_THUMB_PHALANX_PROXIMAL** = `3`

Thumb phalanx proximal joint.

<a id="class-xrhandtracker-constant-hand-joint-thumb-phalanx-distal"></a>

[HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint) **HAND_JOINT_THUMB_PHALANX_DISTAL** = `4`

Thumb phalanx distal joint.

<a id="class-xrhandtracker-constant-hand-joint-thumb-tip"></a>

[HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint) **HAND_JOINT_THUMB_TIP** = `5`

Thumb tip joint.

<a id="class-xrhandtracker-constant-hand-joint-index-finger-metacarpal"></a>

[HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint) **HAND_JOINT_INDEX_FINGER_METACARPAL** = `6`

Index finger metacarpal joint.

<a id="class-xrhandtracker-constant-hand-joint-index-finger-phalanx-proximal"></a>

[HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint) **HAND_JOINT_INDEX_FINGER_PHALANX_PROXIMAL** = `7`

Index finger phalanx proximal joint.

<a id="class-xrhandtracker-constant-hand-joint-index-finger-phalanx-intermediate"></a>

[HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint) **HAND_JOINT_INDEX_FINGER_PHALANX_INTERMEDIATE** = `8`

Index finger phalanx intermediate joint.

<a id="class-xrhandtracker-constant-hand-joint-index-finger-phalanx-distal"></a>

[HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint) **HAND_JOINT_INDEX_FINGER_PHALANX_DISTAL** = `9`

Index finger phalanx distal joint.

<a id="class-xrhandtracker-constant-hand-joint-index-finger-tip"></a>

[HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint) **HAND_JOINT_INDEX_FINGER_TIP** = `10`

Index finger tip joint.

<a id="class-xrhandtracker-constant-hand-joint-middle-finger-metacarpal"></a>

[HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint) **HAND_JOINT_MIDDLE_FINGER_METACARPAL** = `11`

Middle finger metacarpal joint.

<a id="class-xrhandtracker-constant-hand-joint-middle-finger-phalanx-proximal"></a>

[HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint) **HAND_JOINT_MIDDLE_FINGER_PHALANX_PROXIMAL** = `12`

Middle finger phalanx proximal joint.

<a id="class-xrhandtracker-constant-hand-joint-middle-finger-phalanx-intermediate"></a>

[HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint) **HAND_JOINT_MIDDLE_FINGER_PHALANX_INTERMEDIATE** = `13`

Middle finger phalanx intermediate joint.

<a id="class-xrhandtracker-constant-hand-joint-middle-finger-phalanx-distal"></a>

[HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint) **HAND_JOINT_MIDDLE_FINGER_PHALANX_DISTAL** = `14`

Middle finger phalanx distal joint.

<a id="class-xrhandtracker-constant-hand-joint-middle-finger-tip"></a>

[HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint) **HAND_JOINT_MIDDLE_FINGER_TIP** = `15`

Middle finger tip joint.

<a id="class-xrhandtracker-constant-hand-joint-ring-finger-metacarpal"></a>

[HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint) **HAND_JOINT_RING_FINGER_METACARPAL** = `16`

Ring finger metacarpal joint.

<a id="class-xrhandtracker-constant-hand-joint-ring-finger-phalanx-proximal"></a>

[HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint) **HAND_JOINT_RING_FINGER_PHALANX_PROXIMAL** = `17`

Ring finger phalanx proximal joint.

<a id="class-xrhandtracker-constant-hand-joint-ring-finger-phalanx-intermediate"></a>

[HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint) **HAND_JOINT_RING_FINGER_PHALANX_INTERMEDIATE** = `18`

Ring finger phalanx intermediate joint.

<a id="class-xrhandtracker-constant-hand-joint-ring-finger-phalanx-distal"></a>

[HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint) **HAND_JOINT_RING_FINGER_PHALANX_DISTAL** = `19`

Ring finger phalanx distal joint.

<a id="class-xrhandtracker-constant-hand-joint-ring-finger-tip"></a>

[HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint) **HAND_JOINT_RING_FINGER_TIP** = `20`

Ring finger tip joint.

<a id="class-xrhandtracker-constant-hand-joint-pinky-finger-metacarpal"></a>

[HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint) **HAND_JOINT_PINKY_FINGER_METACARPAL** = `21`

Pinky finger metacarpal joint.

<a id="class-xrhandtracker-constant-hand-joint-pinky-finger-phalanx-proximal"></a>

[HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint) **HAND_JOINT_PINKY_FINGER_PHALANX_PROXIMAL** = `22`

Pinky finger phalanx proximal joint.

<a id="class-xrhandtracker-constant-hand-joint-pinky-finger-phalanx-intermediate"></a>

[HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint) **HAND_JOINT_PINKY_FINGER_PHALANX_INTERMEDIATE** = `23`

Pinky finger phalanx intermediate joint.

<a id="class-xrhandtracker-constant-hand-joint-pinky-finger-phalanx-distal"></a>

[HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint) **HAND_JOINT_PINKY_FINGER_PHALANX_DISTAL** = `24`

Pinky finger phalanx distal joint.

<a id="class-xrhandtracker-constant-hand-joint-pinky-finger-tip"></a>

[HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint) **HAND_JOINT_PINKY_FINGER_TIP** = `25`

Pinky finger tip joint.

<a id="class-xrhandtracker-constant-hand-joint-max"></a>

[HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint) **HAND_JOINT_MAX** = `26`

Represents the size of the [HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint) enum.

---


<a id="enum-xrhandtracker-handjointflags"></a>

flags **HandJointFlags**: [🔗](class_xrhandtracker.md#enum-xrhandtracker-handjointflags)

<a id="class-xrhandtracker-constant-hand-joint-flag-orientation-valid"></a>

[HandJointFlags](class_xrhandtracker.md#enum-xrhandtracker-handjointflags) **HAND_JOINT_FLAG_ORIENTATION_VALID** = `1`

The hand joint's orientation data is valid.

<a id="class-xrhandtracker-constant-hand-joint-flag-orientation-tracked"></a>

[HandJointFlags](class_xrhandtracker.md#enum-xrhandtracker-handjointflags) **HAND_JOINT_FLAG_ORIENTATION_TRACKED** = `2`

The hand joint's orientation is actively tracked. May not be set if tracking has been temporarily lost.

<a id="class-xrhandtracker-constant-hand-joint-flag-position-valid"></a>

[HandJointFlags](class_xrhandtracker.md#enum-xrhandtracker-handjointflags) **HAND_JOINT_FLAG_POSITION_VALID** = `4`

The hand joint's position data is valid.

<a id="class-xrhandtracker-constant-hand-joint-flag-position-tracked"></a>

[HandJointFlags](class_xrhandtracker.md#enum-xrhandtracker-handjointflags) **HAND_JOINT_FLAG_POSITION_TRACKED** = `8`

The hand joint's position is actively tracked. May not be set if tracking has been temporarily lost.

<a id="class-xrhandtracker-constant-hand-joint-flag-linear-velocity-valid"></a>

[HandJointFlags](class_xrhandtracker.md#enum-xrhandtracker-handjointflags) **HAND_JOINT_FLAG_LINEAR_VELOCITY_VALID** = `16`

The hand joint's linear velocity data is valid.

<a id="class-xrhandtracker-constant-hand-joint-flag-angular-velocity-valid"></a>

[HandJointFlags](class_xrhandtracker.md#enum-xrhandtracker-handjointflags) **HAND_JOINT_FLAG_ANGULAR_VELOCITY_VALID** = `32`

The hand joint's angular velocity data is valid.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-xrhandtracker-property-hand-tracking-source"></a>

[HandTrackingSource](class_xrhandtracker.md#enum-xrhandtracker-handtrackingsource) **hand_tracking_source** = `0` [🔗](class_xrhandtracker.md#class-xrhandtracker-property-hand-tracking-source)

- void **set_hand_tracking_source**(value: [HandTrackingSource](class_xrhandtracker.md#enum-xrhandtracker-handtrackingsource))
- [HandTrackingSource](class_xrhandtracker.md#enum-xrhandtracker-handtrackingsource) **get_hand_tracking_source**()

The source of the hand tracking data.

---


<a id="class-xrhandtracker-property-has-tracking-data"></a>

[bool](class_bool.md#class-bool) **has_tracking_data** = `false` [🔗](class_xrhandtracker.md#class-xrhandtracker-property-has-tracking-data)

- void **set_has_tracking_data**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_has_tracking_data**()

If `true`, the hand tracking data is valid.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-xrhandtracker-method-get-hand-joint-angular-velocity"></a>

[Vector3](class_vector3.md#class-vector3) **get_hand_joint_angular_velocity**(joint: [HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint)) const [🔗](class_xrhandtracker.md#class-xrhandtracker-method-get-hand-joint-angular-velocity)

Returns the angular velocity for the given hand joint.

---


<a id="class-xrhandtracker-method-get-hand-joint-flags"></a>

BitField[[HandJointFlags](class_xrhandtracker.md#enum-xrhandtracker-handjointflags)] **get_hand_joint_flags**(joint: [HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint)) const [🔗](class_xrhandtracker.md#class-xrhandtracker-method-get-hand-joint-flags)

Returns flags about the validity of the tracking data for the given hand joint.

---


<a id="class-xrhandtracker-method-get-hand-joint-linear-velocity"></a>

[Vector3](class_vector3.md#class-vector3) **get_hand_joint_linear_velocity**(joint: [HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint)) const [🔗](class_xrhandtracker.md#class-xrhandtracker-method-get-hand-joint-linear-velocity)

Returns the linear velocity for the given hand joint.

---


<a id="class-xrhandtracker-method-get-hand-joint-radius"></a>

[float](class_float.md#class-float) **get_hand_joint_radius**(joint: [HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint)) const [🔗](class_xrhandtracker.md#class-xrhandtracker-method-get-hand-joint-radius)

Returns the radius of the given hand joint.

---


<a id="class-xrhandtracker-method-get-hand-joint-transform"></a>

[Transform3D](class_transform3d.md#class-transform3d) **get_hand_joint_transform**(joint: [HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint)) const [🔗](class_xrhandtracker.md#class-xrhandtracker-method-get-hand-joint-transform)

Returns the transform for the given hand joint.

---


<a id="class-xrhandtracker-method-set-hand-joint-angular-velocity"></a>

void **set_hand_joint_angular_velocity**(joint: [HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint), angular_velocity: [Vector3](class_vector3.md#class-vector3)) [🔗](class_xrhandtracker.md#class-xrhandtracker-method-set-hand-joint-angular-velocity)

Sets the angular velocity for the given hand joint.

---


<a id="class-xrhandtracker-method-set-hand-joint-flags"></a>

void **set_hand_joint_flags**(joint: [HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint), flags: BitField[[HandJointFlags](class_xrhandtracker.md#enum-xrhandtracker-handjointflags)]) [🔗](class_xrhandtracker.md#class-xrhandtracker-method-set-hand-joint-flags)

Sets flags about the validity of the tracking data for the given hand joint.

---


<a id="class-xrhandtracker-method-set-hand-joint-linear-velocity"></a>

void **set_hand_joint_linear_velocity**(joint: [HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint), linear_velocity: [Vector3](class_vector3.md#class-vector3)) [🔗](class_xrhandtracker.md#class-xrhandtracker-method-set-hand-joint-linear-velocity)

Sets the linear velocity for the given hand joint.

---


<a id="class-xrhandtracker-method-set-hand-joint-radius"></a>

void **set_hand_joint_radius**(joint: [HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint), radius: [float](class_float.md#class-float)) [🔗](class_xrhandtracker.md#class-xrhandtracker-method-set-hand-joint-radius)

Sets the radius of the given hand joint.

---


<a id="class-xrhandtracker-method-set-hand-joint-transform"></a>

void **set_hand_joint_transform**(joint: [HandJoint](class_xrhandtracker.md#enum-xrhandtracker-handjoint), transform: [Transform3D](class_transform3d.md#class-transform3d)) [🔗](class_xrhandtracker.md#class-xrhandtracker-method-set-hand-joint-transform)

Sets the transform for the given hand joint.
