> Source: https://docs.godotengine.org/en/4.7/classes/class_openxrhand.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxrhand"></a>

<a id="class-openxrhand"></a>

# OpenXRHand

**Deprecated:** Use [XRHandModifier3D](class_xrhandmodifier3d.md#class-xrhandmodifier3d) instead.

**Inherits:** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Node supporting hand and finger tracking in OpenXR.

<a id="description"></a>

## Description

This node enables OpenXR's hand tracking functionality. The node should be a child node of an [XROrigin3D](class_xrorigin3d.md#class-xrorigin3d) node, tracking will update its position to the player's tracked hand Palm joint location (the center of the middle finger's metacarpal bone). This node also updates the skeleton of a properly skinned hand or avatar model.

If the skeleton is a hand (one of the hand bones is the root node of the skeleton), then the skeleton will be placed relative to the hand palm location and the hand mesh and skeleton should be children of the OpenXRHand node.

If the hand bones are part of a full skeleton, then the root of the hand will keep its location with the assumption that IK is used to position the hand and arm.

By default the skeleton hand bones are repositioned to match the size of the tracked hand. To preserve the modeled bone sizes change [bone_update](class_openxrhand.md#class-openxrhand-property-bone-update) to apply rotation only.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [BoneUpdate](class_openxrhand.md#enum-openxrhand-boneupdate) | [bone_update](class_openxrhand.md#class-openxrhand-property-bone-update) | `0` |
| [Hands](class_openxrhand.md#enum-openxrhand-hands) | [hand](class_openxrhand.md#class-openxrhand-property-hand) | `0` |
| [NodePath](class_nodepath.md#class-nodepath) | [hand_skeleton](class_openxrhand.md#class-openxrhand-property-hand-skeleton) | `NodePath("")` |
| [MotionRange](class_openxrhand.md#enum-openxrhand-motionrange) | [motion_range](class_openxrhand.md#class-openxrhand-property-motion-range) | `0` |
| [SkeletonRig](class_openxrhand.md#enum-openxrhand-skeletonrig) | [skeleton_rig](class_openxrhand.md#class-openxrhand-property-skeleton-rig) | `0` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-openxrhand-hands"></a>

enum **Hands**: [🔗](class_openxrhand.md#enum-openxrhand-hands)

<a id="class-openxrhand-constant-hand-left"></a>

[Hands](class_openxrhand.md#enum-openxrhand-hands) **HAND_LEFT** = `0`

Tracking the player's left hand.

<a id="class-openxrhand-constant-hand-right"></a>

[Hands](class_openxrhand.md#enum-openxrhand-hands) **HAND_RIGHT** = `1`

Tracking the player's right hand.

<a id="class-openxrhand-constant-hand-max"></a>

[Hands](class_openxrhand.md#enum-openxrhand-hands) **HAND_MAX** = `2`

Maximum supported hands.

---


<a id="enum-openxrhand-motionrange"></a>

enum **MotionRange**: [🔗](class_openxrhand.md#enum-openxrhand-motionrange)

<a id="class-openxrhand-constant-motion-range-unobstructed"></a>

[MotionRange](class_openxrhand.md#enum-openxrhand-motionrange) **MOTION_RANGE_UNOBSTRUCTED** = `0`

When player grips, hand skeleton will form a full fist.

<a id="class-openxrhand-constant-motion-range-conform-to-controller"></a>

[MotionRange](class_openxrhand.md#enum-openxrhand-motionrange) **MOTION_RANGE_CONFORM_TO_CONTROLLER** = `1`

When player grips, hand skeleton conforms to the controller the player is holding.

<a id="class-openxrhand-constant-motion-range-max"></a>

[MotionRange](class_openxrhand.md#enum-openxrhand-motionrange) **MOTION_RANGE_MAX** = `2`

Maximum supported motion ranges.

---


<a id="enum-openxrhand-skeletonrig"></a>

enum **SkeletonRig**: [🔗](class_openxrhand.md#enum-openxrhand-skeletonrig)

<a id="class-openxrhand-constant-skeleton-rig-openxr"></a>

[SkeletonRig](class_openxrhand.md#enum-openxrhand-skeletonrig) **SKELETON_RIG_OPENXR** = `0`

An OpenXR compliant skeleton.

<a id="class-openxrhand-constant-skeleton-rig-humanoid"></a>

[SkeletonRig](class_openxrhand.md#enum-openxrhand-skeletonrig) **SKELETON_RIG_HUMANOID** = `1`

A [SkeletonProfileHumanoid](class_skeletonprofilehumanoid.md#class-skeletonprofilehumanoid) compliant skeleton.

<a id="class-openxrhand-constant-skeleton-rig-max"></a>

[SkeletonRig](class_openxrhand.md#enum-openxrhand-skeletonrig) **SKELETON_RIG_MAX** = `2`

Maximum supported hands.

---


<a id="enum-openxrhand-boneupdate"></a>

enum **BoneUpdate**: [🔗](class_openxrhand.md#enum-openxrhand-boneupdate)

<a id="class-openxrhand-constant-bone-update-full"></a>

[BoneUpdate](class_openxrhand.md#enum-openxrhand-boneupdate) **BONE_UPDATE_FULL** = `0`

The skeletons bones are fully updated (both position and rotation) to match the tracked bones.

<a id="class-openxrhand-constant-bone-update-rotation-only"></a>

[BoneUpdate](class_openxrhand.md#enum-openxrhand-boneupdate) **BONE_UPDATE_ROTATION_ONLY** = `1`

The skeletons bones are only rotated to align with the tracked bones, preserving bone length.

<a id="class-openxrhand-constant-bone-update-max"></a>

[BoneUpdate](class_openxrhand.md#enum-openxrhand-boneupdate) **BONE_UPDATE_MAX** = `2`

Maximum supported bone update mode.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-openxrhand-property-bone-update"></a>

[BoneUpdate](class_openxrhand.md#enum-openxrhand-boneupdate) **bone_update** = `0` [🔗](class_openxrhand.md#class-openxrhand-property-bone-update)

- void **set_bone_update**(value: [BoneUpdate](class_openxrhand.md#enum-openxrhand-boneupdate))
- [BoneUpdate](class_openxrhand.md#enum-openxrhand-boneupdate) **get_bone_update**()

Specify the type of updates to perform on the bone.

---


<a id="class-openxrhand-property-hand"></a>

[Hands](class_openxrhand.md#enum-openxrhand-hands) **hand** = `0` [🔗](class_openxrhand.md#class-openxrhand-property-hand)

- void **set_hand**(value: [Hands](class_openxrhand.md#enum-openxrhand-hands))
- [Hands](class_openxrhand.md#enum-openxrhand-hands) **get_hand**()

Specifies whether this node tracks the left or right hand of the player.

---


<a id="class-openxrhand-property-hand-skeleton"></a>

[NodePath](class_nodepath.md#class-nodepath) **hand_skeleton** = `NodePath("")` [🔗](class_openxrhand.md#class-openxrhand-property-hand-skeleton)

- void **set_hand_skeleton**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_hand_skeleton**()

Set a [Skeleton3D](class_skeleton3d.md#class-skeleton3d) node for which the pose positions will be updated.

---


<a id="class-openxrhand-property-motion-range"></a>

[MotionRange](class_openxrhand.md#enum-openxrhand-motionrange) **motion_range** = `0` [🔗](class_openxrhand.md#class-openxrhand-property-motion-range)

- void **set_motion_range**(value: [MotionRange](class_openxrhand.md#enum-openxrhand-motionrange))
- [MotionRange](class_openxrhand.md#enum-openxrhand-motionrange) **get_motion_range**()

Set the motion range (if supported) limiting the hand motion.

---


<a id="class-openxrhand-property-skeleton-rig"></a>

[SkeletonRig](class_openxrhand.md#enum-openxrhand-skeletonrig) **skeleton_rig** = `0` [🔗](class_openxrhand.md#class-openxrhand-property-skeleton-rig)

- void **set_skeleton_rig**(value: [SkeletonRig](class_openxrhand.md#enum-openxrhand-skeletonrig))
- [SkeletonRig](class_openxrhand.md#enum-openxrhand-skeletonrig) **get_skeleton_rig**()

Set the type of skeleton rig the [hand_skeleton](class_openxrhand.md#class-openxrhand-property-hand-skeleton) is compliant with.
