> Source: https://docs.godotengine.org/en/4.7/classes/class_skeletonprofile.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="skeletonprofile"></a>

<a id="class-skeletonprofile"></a>

# SkeletonProfile

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [SkeletonProfileHumanoid](class_skeletonprofilehumanoid.md#class-skeletonprofilehumanoid)

Base class for a profile of a virtual skeleton used as a target for retargeting.

<a id="description"></a>

## Description

This resource is used in [EditorScenePostImport](class_editorscenepostimport.md#class-editorscenepostimport). Some parameters are referring to bones in [Skeleton3D](class_skeleton3d.md#class-skeleton3d), [Skin](class_skin.md#class-skin), [Animation](class_animation.md#class-animation), and some other nodes are rewritten based on the parameters of **SkeletonProfile**.

**Note:** These parameters need to be set only when creating a custom profile. In [SkeletonProfileHumanoid](class_skeletonprofilehumanoid.md#class-skeletonprofilehumanoid), they are defined internally as read-only values.

<a id="tutorials"></a>

## Tutorials

- [Retargeting 3D Skeletons](../tutorials/assets_pipeline/retargeting_3d_skeletons.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [bone_size](class_skeletonprofile.md#class-skeletonprofile-property-bone-size) | `0` |
| [int](class_int.md#class-int) | [group_size](class_skeletonprofile.md#class-skeletonprofile-property-group-size) | `0` |
| [StringName](class_stringname.md#class-stringname) | [root_bone](class_skeletonprofile.md#class-skeletonprofile-property-root-bone) | `&""` |
| [StringName](class_stringname.md#class-stringname) | [scale_base_bone](class_skeletonprofile.md#class-skeletonprofile-property-scale-base-bone) | `&""` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [int](class_int.md#class-int) | [find_bone](class_skeletonprofile.md#class-skeletonprofile-method-find-bone)(bone_name: [StringName](class_stringname.md#class-stringname)) const |
| [StringName](class_stringname.md#class-stringname) | [get_bone_name](class_skeletonprofile.md#class-skeletonprofile-method-get-bone-name)(bone_idx: [int](class_int.md#class-int)) const |
| [StringName](class_stringname.md#class-stringname) | [get_bone_parent](class_skeletonprofile.md#class-skeletonprofile-method-get-bone-parent)(bone_idx: [int](class_int.md#class-int)) const |
| [StringName](class_stringname.md#class-stringname) | [get_bone_tail](class_skeletonprofile.md#class-skeletonprofile-method-get-bone-tail)(bone_idx: [int](class_int.md#class-int)) const |
| [StringName](class_stringname.md#class-stringname) | [get_group](class_skeletonprofile.md#class-skeletonprofile-method-get-group)(bone_idx: [int](class_int.md#class-int)) const |
| [StringName](class_stringname.md#class-stringname) | [get_group_name](class_skeletonprofile.md#class-skeletonprofile-method-get-group-name)(group_idx: [int](class_int.md#class-int)) const |
| [Vector2](class_vector2.md#class-vector2) | [get_handle_offset](class_skeletonprofile.md#class-skeletonprofile-method-get-handle-offset)(bone_idx: [int](class_int.md#class-int)) const |
| [Transform3D](class_transform3d.md#class-transform3d) | [get_reference_pose](class_skeletonprofile.md#class-skeletonprofile-method-get-reference-pose)(bone_idx: [int](class_int.md#class-int)) const |
| [TailDirection](class_skeletonprofile.md#enum-skeletonprofile-taildirection) | [get_tail_direction](class_skeletonprofile.md#class-skeletonprofile-method-get-tail-direction)(bone_idx: [int](class_int.md#class-int)) const |
| [Texture2D](class_texture2d.md#class-texture2d) | [get_texture](class_skeletonprofile.md#class-skeletonprofile-method-get-texture)(group_idx: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [is_required](class_skeletonprofile.md#class-skeletonprofile-method-is-required)(bone_idx: [int](class_int.md#class-int)) const |
| void | [set_bone_name](class_skeletonprofile.md#class-skeletonprofile-method-set-bone-name)(bone_idx: [int](class_int.md#class-int), bone_name: [StringName](class_stringname.md#class-stringname)) |
| void | [set_bone_parent](class_skeletonprofile.md#class-skeletonprofile-method-set-bone-parent)(bone_idx: [int](class_int.md#class-int), bone_parent: [StringName](class_stringname.md#class-stringname)) |
| void | [set_bone_tail](class_skeletonprofile.md#class-skeletonprofile-method-set-bone-tail)(bone_idx: [int](class_int.md#class-int), bone_tail: [StringName](class_stringname.md#class-stringname)) |
| void | [set_group](class_skeletonprofile.md#class-skeletonprofile-method-set-group)(bone_idx: [int](class_int.md#class-int), group: [StringName](class_stringname.md#class-stringname)) |
| void | [set_group_name](class_skeletonprofile.md#class-skeletonprofile-method-set-group-name)(group_idx: [int](class_int.md#class-int), group_name: [StringName](class_stringname.md#class-stringname)) |
| void | [set_handle_offset](class_skeletonprofile.md#class-skeletonprofile-method-set-handle-offset)(bone_idx: [int](class_int.md#class-int), handle_offset: [Vector2](class_vector2.md#class-vector2)) |
| void | [set_reference_pose](class_skeletonprofile.md#class-skeletonprofile-method-set-reference-pose)(bone_idx: [int](class_int.md#class-int), bone_name: [Transform3D](class_transform3d.md#class-transform3d)) |
| void | [set_required](class_skeletonprofile.md#class-skeletonprofile-method-set-required)(bone_idx: [int](class_int.md#class-int), required: [bool](class_bool.md#class-bool)) |
| void | [set_tail_direction](class_skeletonprofile.md#class-skeletonprofile-method-set-tail-direction)(bone_idx: [int](class_int.md#class-int), tail_direction: [TailDirection](class_skeletonprofile.md#enum-skeletonprofile-taildirection)) |
| void | [set_texture](class_skeletonprofile.md#class-skeletonprofile-method-set-texture)(group_idx: [int](class_int.md#class-int), texture: [Texture2D](class_texture2d.md#class-texture2d)) |

---


<a id="signals"></a>

## Signals

<a id="class-skeletonprofile-signal-profile-updated"></a>

**profile_updated**() [🔗](class_skeletonprofile.md#class-skeletonprofile-signal-profile-updated)

This signal is emitted when change the value in profile. This is used to update key name in the [BoneMap](class_bonemap.md#class-bonemap) and to redraw the [BoneMap](class_bonemap.md#class-bonemap) editor.

**Note:** This signal is not connected directly to editor to simplify the reference, instead it is passed on to editor through the [BoneMap](class_bonemap.md#class-bonemap).

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-skeletonprofile-taildirection"></a>

enum **TailDirection**: [🔗](class_skeletonprofile.md#enum-skeletonprofile-taildirection)

<a id="class-skeletonprofile-constant-tail-direction-average-children"></a>

[TailDirection](class_skeletonprofile.md#enum-skeletonprofile-taildirection) **TAIL_DIRECTION_AVERAGE_CHILDREN** = `0`

Direction to the average coordinates of bone children.

<a id="class-skeletonprofile-constant-tail-direction-specific-child"></a>

[TailDirection](class_skeletonprofile.md#enum-skeletonprofile-taildirection) **TAIL_DIRECTION_SPECIFIC_CHILD** = `1`

Direction to the coordinates of specified bone child.

<a id="class-skeletonprofile-constant-tail-direction-end"></a>

[TailDirection](class_skeletonprofile.md#enum-skeletonprofile-taildirection) **TAIL_DIRECTION_END** = `2`

Direction is not calculated.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-skeletonprofile-property-bone-size"></a>

[int](class_int.md#class-int) **bone_size** = `0` [🔗](class_skeletonprofile.md#class-skeletonprofile-property-bone-size)

- void **set_bone_size**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_bone_size**()

The amount of bones in retargeting section's [BoneMap](class_bonemap.md#class-bonemap) editor. For example, [SkeletonProfileHumanoid](class_skeletonprofilehumanoid.md#class-skeletonprofilehumanoid) has 56 bones.

The size of elements in [BoneMap](class_bonemap.md#class-bonemap) updates when changing this property in it's assigned **SkeletonProfile**.

---


<a id="class-skeletonprofile-property-group-size"></a>

[int](class_int.md#class-int) **group_size** = `0` [🔗](class_skeletonprofile.md#class-skeletonprofile-property-group-size)

- void **set_group_size**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_group_size**()

The amount of groups of bones in retargeting section's [BoneMap](class_bonemap.md#class-bonemap) editor. For example, [SkeletonProfileHumanoid](class_skeletonprofilehumanoid.md#class-skeletonprofilehumanoid) has 4 groups.

This property exists to separate the bone list into several sections in the editor.

---


<a id="class-skeletonprofile-property-root-bone"></a>

[StringName](class_stringname.md#class-stringname) **root_bone** = `&""` [🔗](class_skeletonprofile.md#class-skeletonprofile-property-root-bone)

- void **set_root_bone**(value: [StringName](class_stringname.md#class-stringname))
- [StringName](class_stringname.md#class-stringname) **get_root_bone**()

A bone name that will be used as the root bone in [AnimationTree](class_animationtree.md#class-animationtree). This should be the bone of the parent of hips that exists at the world origin.

---


<a id="class-skeletonprofile-property-scale-base-bone"></a>

[StringName](class_stringname.md#class-stringname) **scale_base_bone** = `&""` [🔗](class_skeletonprofile.md#class-skeletonprofile-property-scale-base-bone)

- void **set_scale_base_bone**(value: [StringName](class_stringname.md#class-stringname))
- [StringName](class_stringname.md#class-stringname) **get_scale_base_bone**()

A bone name which will use model's height as the coefficient for normalization. For example, [SkeletonProfileHumanoid](class_skeletonprofilehumanoid.md#class-skeletonprofilehumanoid) defines it as `Hips`.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-skeletonprofile-method-find-bone"></a>

[int](class_int.md#class-int) **find_bone**(bone_name: [StringName](class_stringname.md#class-stringname)) const [🔗](class_skeletonprofile.md#class-skeletonprofile-method-find-bone)

Returns the bone index that matches `bone_name` as its name.

---


<a id="class-skeletonprofile-method-get-bone-name"></a>

[StringName](class_stringname.md#class-stringname) **get_bone_name**(bone_idx: [int](class_int.md#class-int)) const [🔗](class_skeletonprofile.md#class-skeletonprofile-method-get-bone-name)

Returns the name of the bone at `bone_idx` that will be the key name in the [BoneMap](class_bonemap.md#class-bonemap).

In the retargeting process, the returned bone name is the bone name of the target skeleton.

---


<a id="class-skeletonprofile-method-get-bone-parent"></a>

[StringName](class_stringname.md#class-stringname) **get_bone_parent**(bone_idx: [int](class_int.md#class-int)) const [🔗](class_skeletonprofile.md#class-skeletonprofile-method-get-bone-parent)

Returns the name of the bone which is the parent to the bone at `bone_idx`. The result is empty if the bone has no parent.

---


<a id="class-skeletonprofile-method-get-bone-tail"></a>

[StringName](class_stringname.md#class-stringname) **get_bone_tail**(bone_idx: [int](class_int.md#class-int)) const [🔗](class_skeletonprofile.md#class-skeletonprofile-method-get-bone-tail)

Returns the name of the bone which is the tail of the bone at `bone_idx`.

---


<a id="class-skeletonprofile-method-get-group"></a>

[StringName](class_stringname.md#class-stringname) **get_group**(bone_idx: [int](class_int.md#class-int)) const [🔗](class_skeletonprofile.md#class-skeletonprofile-method-get-group)

Returns the group of the bone at `bone_idx`.

---


<a id="class-skeletonprofile-method-get-group-name"></a>

[StringName](class_stringname.md#class-stringname) **get_group_name**(group_idx: [int](class_int.md#class-int)) const [🔗](class_skeletonprofile.md#class-skeletonprofile-method-get-group-name)

Returns the name of the group at `group_idx` that will be the drawing group in the [BoneMap](class_bonemap.md#class-bonemap) editor.

---


<a id="class-skeletonprofile-method-get-handle-offset"></a>

[Vector2](class_vector2.md#class-vector2) **get_handle_offset**(bone_idx: [int](class_int.md#class-int)) const [🔗](class_skeletonprofile.md#class-skeletonprofile-method-get-handle-offset)

Returns the offset of the bone at `bone_idx` that will be the button position in the [BoneMap](class_bonemap.md#class-bonemap) editor.

This is the offset with origin at the top left corner of the square.

---


<a id="class-skeletonprofile-method-get-reference-pose"></a>

[Transform3D](class_transform3d.md#class-transform3d) **get_reference_pose**(bone_idx: [int](class_int.md#class-int)) const [🔗](class_skeletonprofile.md#class-skeletonprofile-method-get-reference-pose)

Returns the reference pose transform for bone `bone_idx`.

---


<a id="class-skeletonprofile-method-get-tail-direction"></a>

[TailDirection](class_skeletonprofile.md#enum-skeletonprofile-taildirection) **get_tail_direction**(bone_idx: [int](class_int.md#class-int)) const [🔗](class_skeletonprofile.md#class-skeletonprofile-method-get-tail-direction)

Returns the tail direction of the bone at `bone_idx`.

---


<a id="class-skeletonprofile-method-get-texture"></a>

[Texture2D](class_texture2d.md#class-texture2d) **get_texture**(group_idx: [int](class_int.md#class-int)) const [🔗](class_skeletonprofile.md#class-skeletonprofile-method-get-texture)

Returns the texture of the group at `group_idx` that will be the drawing group background image in the [BoneMap](class_bonemap.md#class-bonemap) editor.

---


<a id="class-skeletonprofile-method-is-required"></a>

[bool](class_bool.md#class-bool) **is_required**(bone_idx: [int](class_int.md#class-int)) const [🔗](class_skeletonprofile.md#class-skeletonprofile-method-is-required)

Returns whether the bone at `bone_idx` is required for retargeting.

This value is used by the bone map editor. If this method returns `true`, and no bone is assigned, the handle color will be red on the bone map editor.

---


<a id="class-skeletonprofile-method-set-bone-name"></a>

void **set_bone_name**(bone_idx: [int](class_int.md#class-int), bone_name: [StringName](class_stringname.md#class-stringname)) [🔗](class_skeletonprofile.md#class-skeletonprofile-method-set-bone-name)

Sets the name of the bone at `bone_idx` that will be the key name in the [BoneMap](class_bonemap.md#class-bonemap).

In the retargeting process, the setting bone name is the bone name of the target skeleton.

---


<a id="class-skeletonprofile-method-set-bone-parent"></a>

void **set_bone_parent**(bone_idx: [int](class_int.md#class-int), bone_parent: [StringName](class_stringname.md#class-stringname)) [🔗](class_skeletonprofile.md#class-skeletonprofile-method-set-bone-parent)

Sets the bone with name `bone_parent` as the parent of the bone at `bone_idx`. If an empty string is passed, then the bone has no parent.

---


<a id="class-skeletonprofile-method-set-bone-tail"></a>

void **set_bone_tail**(bone_idx: [int](class_int.md#class-int), bone_tail: [StringName](class_stringname.md#class-stringname)) [🔗](class_skeletonprofile.md#class-skeletonprofile-method-set-bone-tail)

Sets the bone with name `bone_tail` as the tail of the bone at `bone_idx`.

---


<a id="class-skeletonprofile-method-set-group"></a>

void **set_group**(bone_idx: [int](class_int.md#class-int), group: [StringName](class_stringname.md#class-stringname)) [🔗](class_skeletonprofile.md#class-skeletonprofile-method-set-group)

Sets the group of the bone at `bone_idx`.

---


<a id="class-skeletonprofile-method-set-group-name"></a>

void **set_group_name**(group_idx: [int](class_int.md#class-int), group_name: [StringName](class_stringname.md#class-stringname)) [🔗](class_skeletonprofile.md#class-skeletonprofile-method-set-group-name)

Sets the name of the group at `group_idx` that will be the drawing group in the [BoneMap](class_bonemap.md#class-bonemap) editor.

---


<a id="class-skeletonprofile-method-set-handle-offset"></a>

void **set_handle_offset**(bone_idx: [int](class_int.md#class-int), handle_offset: [Vector2](class_vector2.md#class-vector2)) [🔗](class_skeletonprofile.md#class-skeletonprofile-method-set-handle-offset)

Sets the offset of the bone at `bone_idx` that will be the button position in the [BoneMap](class_bonemap.md#class-bonemap) editor.

This is the offset with origin at the top left corner of the square.

---


<a id="class-skeletonprofile-method-set-reference-pose"></a>

void **set_reference_pose**(bone_idx: [int](class_int.md#class-int), bone_name: [Transform3D](class_transform3d.md#class-transform3d)) [🔗](class_skeletonprofile.md#class-skeletonprofile-method-set-reference-pose)

Sets the reference pose transform for bone `bone_idx`.

---


<a id="class-skeletonprofile-method-set-required"></a>

void **set_required**(bone_idx: [int](class_int.md#class-int), required: [bool](class_bool.md#class-bool)) [🔗](class_skeletonprofile.md#class-skeletonprofile-method-set-required)

Sets the required status for bone `bone_idx` to `required`.

---


<a id="class-skeletonprofile-method-set-tail-direction"></a>

void **set_tail_direction**(bone_idx: [int](class_int.md#class-int), tail_direction: [TailDirection](class_skeletonprofile.md#enum-skeletonprofile-taildirection)) [🔗](class_skeletonprofile.md#class-skeletonprofile-method-set-tail-direction)

Sets the tail direction of the bone at `bone_idx`.

**Note:** This only specifies the method of calculation. The actual coordinates required should be stored in an external skeleton, so the calculation itself needs to be done externally.

---


<a id="class-skeletonprofile-method-set-texture"></a>

void **set_texture**(group_idx: [int](class_int.md#class-int), texture: [Texture2D](class_texture2d.md#class-texture2d)) [🔗](class_skeletonprofile.md#class-skeletonprofile-method-set-texture)

Sets the texture of the group at `group_idx` that will be the drawing group background image in the [BoneMap](class_bonemap.md#class-bonemap) editor.
