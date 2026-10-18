> Source: https://docs.godotengine.org/en/4.7/classes/class_xrbodymodifier3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="xrbodymodifier3d"></a>

<a id="class-xrbodymodifier3d"></a>

# XRBodyModifier3D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A node for driving body meshes from [XRBodyTracker](class_xrbodytracker.md#class-xrbodytracker) data.

<a id="description"></a>

## Description

This node uses body tracking data from an [XRBodyTracker](class_xrbodytracker.md#class-xrbodytracker) to pose the skeleton of a body mesh.

Positioning of the body is performed by creating an [XRNode3D](class_xrnode3d.md#class-xrnode3d) ancestor of the body mesh driven by the same [XRBodyTracker](class_xrbodytracker.md#class-xrbodytracker).

The body tracking position-data is scaled by [Skeleton3D.motion_scale](class_skeleton3d.md#class-skeleton3d-property-motion-scale) when applied to the skeleton, which can be used to adjust the tracked body to match the scale of the body model.

<a id="tutorials"></a>

## Tutorials

- [XR documentation index](../tutorials/xr/index.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [StringName](class_stringname.md#class-stringname) | [body_tracker](class_xrbodymodifier3d.md#class-xrbodymodifier3d-property-body-tracker) | `&"/user/body_tracker"` |
| BitField[[BodyUpdate](class_xrbodymodifier3d.md#enum-xrbodymodifier3d-bodyupdate)] | [body_update](class_xrbodymodifier3d.md#class-xrbodymodifier3d-property-body-update) | `7` |
| [BoneUpdate](class_xrbodymodifier3d.md#enum-xrbodymodifier3d-boneupdate) | [bone_update](class_xrbodymodifier3d.md#class-xrbodymodifier3d-property-bone-update) | `0` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-xrbodymodifier3d-bodyupdate"></a>

flags **BodyUpdate**: [🔗](class_xrbodymodifier3d.md#enum-xrbodymodifier3d-bodyupdate)

<a id="class-xrbodymodifier3d-constant-body-update-upper-body"></a>

[BodyUpdate](class_xrbodymodifier3d.md#enum-xrbodymodifier3d-bodyupdate) **BODY_UPDATE_UPPER_BODY** = `1`

The skeleton's upper body joints are updated.

<a id="class-xrbodymodifier3d-constant-body-update-lower-body"></a>

[BodyUpdate](class_xrbodymodifier3d.md#enum-xrbodymodifier3d-bodyupdate) **BODY_UPDATE_LOWER_BODY** = `2`

The skeleton's lower body joints are updated.

<a id="class-xrbodymodifier3d-constant-body-update-hands"></a>

[BodyUpdate](class_xrbodymodifier3d.md#enum-xrbodymodifier3d-bodyupdate) **BODY_UPDATE_HANDS** = `4`

The skeleton's hand joints are updated.

---


<a id="enum-xrbodymodifier3d-boneupdate"></a>

enum **BoneUpdate**: [🔗](class_xrbodymodifier3d.md#enum-xrbodymodifier3d-boneupdate)

<a id="class-xrbodymodifier3d-constant-bone-update-full"></a>

[BoneUpdate](class_xrbodymodifier3d.md#enum-xrbodymodifier3d-boneupdate) **BONE_UPDATE_FULL** = `0`

The skeleton's bones are fully updated (both position and rotation) to match the tracked bones.

<a id="class-xrbodymodifier3d-constant-bone-update-rotation-only"></a>

[BoneUpdate](class_xrbodymodifier3d.md#enum-xrbodymodifier3d-boneupdate) **BONE_UPDATE_ROTATION_ONLY** = `1`

The skeleton's bones are only rotated to align with the tracked bones, preserving bone length.

<a id="class-xrbodymodifier3d-constant-bone-update-max"></a>

[BoneUpdate](class_xrbodymodifier3d.md#enum-xrbodymodifier3d-boneupdate) **BONE_UPDATE_MAX** = `2`

Represents the size of the [BoneUpdate](class_xrbodymodifier3d.md#enum-xrbodymodifier3d-boneupdate) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-xrbodymodifier3d-property-body-tracker"></a>

[StringName](class_stringname.md#class-stringname) **body_tracker** = `&"/user/body_tracker"` [🔗](class_xrbodymodifier3d.md#class-xrbodymodifier3d-property-body-tracker)

- void **set_body_tracker**(value: [StringName](class_stringname.md#class-stringname))
- [StringName](class_stringname.md#class-stringname) **get_body_tracker**()

The name of the [XRBodyTracker](class_xrbodytracker.md#class-xrbodytracker) registered with [XRServer](class_xrserver.md#class-xrserver) to obtain the body tracking data from.

---


<a id="class-xrbodymodifier3d-property-body-update"></a>

BitField[[BodyUpdate](class_xrbodymodifier3d.md#enum-xrbodymodifier3d-bodyupdate)] **body_update** = `7` [🔗](class_xrbodymodifier3d.md#class-xrbodymodifier3d-property-body-update)

- void **set_body_update**(value: BitField[[BodyUpdate](class_xrbodymodifier3d.md#enum-xrbodymodifier3d-bodyupdate)])
- BitField[[BodyUpdate](class_xrbodymodifier3d.md#enum-xrbodymodifier3d-bodyupdate)] **get_body_update**()

Specifies the body parts to update.

---


<a id="class-xrbodymodifier3d-property-bone-update"></a>

[BoneUpdate](class_xrbodymodifier3d.md#enum-xrbodymodifier3d-boneupdate) **bone_update** = `0` [🔗](class_xrbodymodifier3d.md#class-xrbodymodifier3d-property-bone-update)

- void **set_bone_update**(value: [BoneUpdate](class_xrbodymodifier3d.md#enum-xrbodymodifier3d-boneupdate))
- [BoneUpdate](class_xrbodymodifier3d.md#enum-xrbodymodifier3d-boneupdate) **get_bone_update**()

Specifies the type of updates to perform on the bones.
