> Source: https://docs.godotengine.org/en/4.7/classes/class_bonemap.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="bonemap"></a>

<a id="class-bonemap"></a>

# BoneMap

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Describes a mapping of bone names for retargeting [Skeleton3D](class_skeleton3d.md#class-skeleton3d) into common names defined by a [SkeletonProfile](class_skeletonprofile.md#class-skeletonprofile).

<a id="description"></a>

## Description

This class contains a dictionary that uses a list of bone names in [SkeletonProfile](class_skeletonprofile.md#class-skeletonprofile) as key names.

By assigning the actual [Skeleton3D](class_skeleton3d.md#class-skeleton3d) bone name as the key value, it maps the [Skeleton3D](class_skeleton3d.md#class-skeleton3d) to the [SkeletonProfile](class_skeletonprofile.md#class-skeletonprofile).

<a id="tutorials"></a>

## Tutorials

- [Retargeting 3D Skeletons](../tutorials/assets_pipeline/retargeting_3d_skeletons.md)

<a id="properties"></a>

## Properties

|  |  |
| --- | --- |
| [SkeletonProfile](class_skeletonprofile.md#class-skeletonprofile) | [profile](class_bonemap.md#class-bonemap-property-profile) |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [StringName](class_stringname.md#class-stringname) | [find_profile_bone_name](class_bonemap.md#class-bonemap-method-find-profile-bone-name)(skeleton_bone_name: [StringName](class_stringname.md#class-stringname)) const |
| [StringName](class_stringname.md#class-stringname) | [get_skeleton_bone_name](class_bonemap.md#class-bonemap-method-get-skeleton-bone-name)(profile_bone_name: [StringName](class_stringname.md#class-stringname)) const |
| void | [set_skeleton_bone_name](class_bonemap.md#class-bonemap-method-set-skeleton-bone-name)(profile_bone_name: [StringName](class_stringname.md#class-stringname), skeleton_bone_name: [StringName](class_stringname.md#class-stringname)) |

---


<a id="signals"></a>

## Signals

<a id="class-bonemap-signal-bone-map-updated"></a>

**bone_map_updated**() [🔗](class_bonemap.md#class-bonemap-signal-bone-map-updated)

This signal is emitted when change the key value in the **BoneMap**. This is used to validate mapping and to update **BoneMap** editor.

---


<a id="class-bonemap-signal-profile-updated"></a>

**profile_updated**() [🔗](class_bonemap.md#class-bonemap-signal-profile-updated)

This signal is emitted when change the value in profile or change the reference of profile. This is used to update key names in the **BoneMap** and to redraw the **BoneMap** editor.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-bonemap-property-profile"></a>

[SkeletonProfile](class_skeletonprofile.md#class-skeletonprofile) **profile** [🔗](class_bonemap.md#class-bonemap-property-profile)

- void **set_profile**(value: [SkeletonProfile](class_skeletonprofile.md#class-skeletonprofile))
- [SkeletonProfile](class_skeletonprofile.md#class-skeletonprofile) **get_profile**()

A [SkeletonProfile](class_skeletonprofile.md#class-skeletonprofile) of the mapping target. Key names in the **BoneMap** are synchronized with it.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-bonemap-method-find-profile-bone-name"></a>

[StringName](class_stringname.md#class-stringname) **find_profile_bone_name**(skeleton_bone_name: [StringName](class_stringname.md#class-stringname)) const [🔗](class_bonemap.md#class-bonemap-method-find-profile-bone-name)

Returns a profile bone name having `skeleton_bone_name`. If not found, an empty [StringName](class_stringname.md#class-stringname) will be returned.

In the retargeting process, the returned bone name is the bone name of the target skeleton.

---


<a id="class-bonemap-method-get-skeleton-bone-name"></a>

[StringName](class_stringname.md#class-stringname) **get_skeleton_bone_name**(profile_bone_name: [StringName](class_stringname.md#class-stringname)) const [🔗](class_bonemap.md#class-bonemap-method-get-skeleton-bone-name)

Returns a skeleton bone name is mapped to `profile_bone_name`.

In the retargeting process, the returned bone name is the bone name of the source skeleton.

---


<a id="class-bonemap-method-set-skeleton-bone-name"></a>

void **set_skeleton_bone_name**(profile_bone_name: [StringName](class_stringname.md#class-stringname), skeleton_bone_name: [StringName](class_stringname.md#class-stringname)) [🔗](class_bonemap.md#class-bonemap-method-set-skeleton-bone-name)

Maps a skeleton bone name to `profile_bone_name`.

In the retargeting process, the setting bone name is the bone name of the source skeleton.
