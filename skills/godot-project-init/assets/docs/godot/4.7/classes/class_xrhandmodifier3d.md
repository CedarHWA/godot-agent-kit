> Source: https://docs.godotengine.org/en/4.7/classes/class_xrhandmodifier3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="xrhandmodifier3d"></a>

<a id="class-xrhandmodifier3d"></a>

# XRHandModifier3D

**Inherits:** [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A node for driving hand meshes from [XRHandTracker](class_xrhandtracker.md#class-xrhandtracker) data.

<a id="description"></a>

## Description

This node uses hand tracking data from an [XRHandTracker](class_xrhandtracker.md#class-xrhandtracker) to pose the skeleton of a hand mesh.

Positioning of hands is performed by creating an [XRNode3D](class_xrnode3d.md#class-xrnode3d) ancestor of the hand mesh driven by the same [XRHandTracker](class_xrhandtracker.md#class-xrhandtracker).

The hand tracking position-data is scaled by [Skeleton3D.motion_scale](class_skeleton3d.md#class-skeleton3d-property-motion-scale) when applied to the skeleton, which can be used to adjust the tracked hand to match the scale of the hand model.

<a id="tutorials"></a>

## Tutorials

- [XR documentation index](../tutorials/xr/index.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [BoneUpdate](class_xrhandmodifier3d.md#enum-xrhandmodifier3d-boneupdate) | [bone_update](class_xrhandmodifier3d.md#class-xrhandmodifier3d-property-bone-update) | `0` |
| [StringName](class_stringname.md#class-stringname) | [hand_tracker](class_xrhandmodifier3d.md#class-xrhandmodifier3d-property-hand-tracker) | `&"/user/hand_tracker/left"` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-xrhandmodifier3d-boneupdate"></a>

enum **BoneUpdate**: [🔗](class_xrhandmodifier3d.md#enum-xrhandmodifier3d-boneupdate)

<a id="class-xrhandmodifier3d-constant-bone-update-full"></a>

[BoneUpdate](class_xrhandmodifier3d.md#enum-xrhandmodifier3d-boneupdate) **BONE_UPDATE_FULL** = `0`

The skeleton's bones are fully updated (both position and rotation) to match the tracked bones.

<a id="class-xrhandmodifier3d-constant-bone-update-rotation-only"></a>

[BoneUpdate](class_xrhandmodifier3d.md#enum-xrhandmodifier3d-boneupdate) **BONE_UPDATE_ROTATION_ONLY** = `1`

The skeleton's bones are only rotated to align with the tracked bones, preserving bone length.

<a id="class-xrhandmodifier3d-constant-bone-update-max"></a>

[BoneUpdate](class_xrhandmodifier3d.md#enum-xrhandmodifier3d-boneupdate) **BONE_UPDATE_MAX** = `2`

Represents the size of the [BoneUpdate](class_xrhandmodifier3d.md#enum-xrhandmodifier3d-boneupdate) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-xrhandmodifier3d-property-bone-update"></a>

[BoneUpdate](class_xrhandmodifier3d.md#enum-xrhandmodifier3d-boneupdate) **bone_update** = `0` [🔗](class_xrhandmodifier3d.md#class-xrhandmodifier3d-property-bone-update)

- void **set_bone_update**(value: [BoneUpdate](class_xrhandmodifier3d.md#enum-xrhandmodifier3d-boneupdate))
- [BoneUpdate](class_xrhandmodifier3d.md#enum-xrhandmodifier3d-boneupdate) **get_bone_update**()

Specifies the type of updates to perform on the bones.

---


<a id="class-xrhandmodifier3d-property-hand-tracker"></a>

[StringName](class_stringname.md#class-stringname) **hand_tracker** = `&"/user/hand_tracker/left"` [🔗](class_xrhandmodifier3d.md#class-xrhandmodifier3d-property-hand-tracker)

- void **set_hand_tracker**(value: [StringName](class_stringname.md#class-stringname))
- [StringName](class_stringname.md#class-stringname) **get_hand_tracker**()

The name of the [XRHandTracker](class_xrhandtracker.md#class-xrhandtracker) registered with [XRServer](class_xrserver.md#class-xrserver) to obtain the hand tracking data from.
