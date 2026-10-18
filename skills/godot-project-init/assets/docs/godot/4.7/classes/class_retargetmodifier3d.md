> Source: https://docs.godotengine.org/en/4.7/classes/class_retargetmodifier3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="retargetmodifier3d"></a>

<a id="class-retargetmodifier3d"></a>

# RetargetModifier3D

**Inherits:** [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A modifier to transfer parent skeleton poses (or global poses) to child skeletons in model space with different rests.

<a id="description"></a>

## Description

Retrieves the pose (or global pose) relative to the parent Skeleton's rest in model space and transfers it to the child Skeleton.

This modifier rewrites the pose of the child skeleton directly in the parent skeleton's update process. This means that it overwrites the mapped bone pose set in the normal process on the target skeleton. If you want to set the target skeleton bone pose after retargeting, you will need to add a [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) child to the target skeleton and thereby modify the pose.

**Note:** When the [use_global_pose](class_retargetmodifier3d.md#class-retargetmodifier3d-property-use-global-pose) is enabled, even if it is an unmapped bone, it can cause visual problems because the global pose is applied ignoring the parent bone's pose **if it has mapped bone children**. See also [use_global_pose](class_retargetmodifier3d.md#class-retargetmodifier3d-property-use-global-pose).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| BitField[[TransformFlag](class_retargetmodifier3d.md#enum-retargetmodifier3d-transformflag)] | [enable](class_retargetmodifier3d.md#class-retargetmodifier3d-property-enable) | `7` |
| [SkeletonProfile](class_skeletonprofile.md#class-skeletonprofile) | [profile](class_retargetmodifier3d.md#class-retargetmodifier3d-property-profile) |  |
| [bool](class_bool.md#class-bool) | [use_global_pose](class_retargetmodifier3d.md#class-retargetmodifier3d-property-use-global-pose) | `false` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [is_position_enabled](class_retargetmodifier3d.md#class-retargetmodifier3d-method-is-position-enabled)() const |
| [bool](class_bool.md#class-bool) | [is_rotation_enabled](class_retargetmodifier3d.md#class-retargetmodifier3d-method-is-rotation-enabled)() const |
| [bool](class_bool.md#class-bool) | [is_scale_enabled](class_retargetmodifier3d.md#class-retargetmodifier3d-method-is-scale-enabled)() const |
| void | [set_position_enabled](class_retargetmodifier3d.md#class-retargetmodifier3d-method-set-position-enabled)(enabled: [bool](class_bool.md#class-bool)) |
| void | [set_rotation_enabled](class_retargetmodifier3d.md#class-retargetmodifier3d-method-set-rotation-enabled)(enabled: [bool](class_bool.md#class-bool)) |
| void | [set_scale_enabled](class_retargetmodifier3d.md#class-retargetmodifier3d-method-set-scale-enabled)(enabled: [bool](class_bool.md#class-bool)) |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-retargetmodifier3d-transformflag"></a>

flags **TransformFlag**: [🔗](class_retargetmodifier3d.md#enum-retargetmodifier3d-transformflag)

<a id="class-retargetmodifier3d-constant-transform-flag-position"></a>

[TransformFlag](class_retargetmodifier3d.md#enum-retargetmodifier3d-transformflag) **TRANSFORM_FLAG_POSITION** = `1`

If set, allows to retarget the position.

<a id="class-retargetmodifier3d-constant-transform-flag-rotation"></a>

[TransformFlag](class_retargetmodifier3d.md#enum-retargetmodifier3d-transformflag) **TRANSFORM_FLAG_ROTATION** = `2`

If set, allows to retarget the rotation.

<a id="class-retargetmodifier3d-constant-transform-flag-scale"></a>

[TransformFlag](class_retargetmodifier3d.md#enum-retargetmodifier3d-transformflag) **TRANSFORM_FLAG_SCALE** = `4`

If set, allows to retarget the scale.

<a id="class-retargetmodifier3d-constant-transform-flag-all"></a>

[TransformFlag](class_retargetmodifier3d.md#enum-retargetmodifier3d-transformflag) **TRANSFORM_FLAG_ALL** = `7`

If set, allows to retarget the position/rotation/scale.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-retargetmodifier3d-property-enable"></a>

BitField[[TransformFlag](class_retargetmodifier3d.md#enum-retargetmodifier3d-transformflag)] **enable** = `7` [🔗](class_retargetmodifier3d.md#class-retargetmodifier3d-property-enable)

- void **set_enable_flags**(value: BitField[[TransformFlag](class_retargetmodifier3d.md#enum-retargetmodifier3d-transformflag)])
- BitField[[TransformFlag](class_retargetmodifier3d.md#enum-retargetmodifier3d-transformflag)] **get_enable_flags**()

Flags to control the process of the transform elements individually when [use_global_pose](class_retargetmodifier3d.md#class-retargetmodifier3d-property-use-global-pose) is disabled.

---


<a id="class-retargetmodifier3d-property-profile"></a>

[SkeletonProfile](class_skeletonprofile.md#class-skeletonprofile) **profile** [🔗](class_retargetmodifier3d.md#class-retargetmodifier3d-property-profile)

- void **set_profile**(value: [SkeletonProfile](class_skeletonprofile.md#class-skeletonprofile))
- [SkeletonProfile](class_skeletonprofile.md#class-skeletonprofile) **get_profile**()

[SkeletonProfile](class_skeletonprofile.md#class-skeletonprofile) for retargeting bones with names matching the bone list.

---


<a id="class-retargetmodifier3d-property-use-global-pose"></a>

[bool](class_bool.md#class-bool) **use_global_pose** = `false` [🔗](class_retargetmodifier3d.md#class-retargetmodifier3d-property-use-global-pose)

- void **set_use_global_pose**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_using_global_pose**()

If `false`, in case the target skeleton has fewer bones than the source skeleton, the source bone parent's transform will be ignored.

Instead, it is possible to retarget between models with different body shapes, and position, rotation, and scale can be retargeted separately.

If `true`, retargeting is performed taking into account global pose.

In case the target skeleton has fewer bones than the source skeleton, the source bone parent's transform is taken into account. However, bone length between skeletons must match exactly, if not, the bones will be forced to expand or shrink.

This is useful for using dummy bone with length `0` to match postures when retargeting between models with different number of bones.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-retargetmodifier3d-method-is-position-enabled"></a>

[bool](class_bool.md#class-bool) **is_position_enabled**() const [🔗](class_retargetmodifier3d.md#class-retargetmodifier3d-method-is-position-enabled)

Returns `true` if [enable](class_retargetmodifier3d.md#class-retargetmodifier3d-property-enable) has [TRANSFORM_FLAG_POSITION](class_retargetmodifier3d.md#class-retargetmodifier3d-constant-transform-flag-position).

---


<a id="class-retargetmodifier3d-method-is-rotation-enabled"></a>

[bool](class_bool.md#class-bool) **is_rotation_enabled**() const [🔗](class_retargetmodifier3d.md#class-retargetmodifier3d-method-is-rotation-enabled)

Returns `true` if [enable](class_retargetmodifier3d.md#class-retargetmodifier3d-property-enable) has [TRANSFORM_FLAG_ROTATION](class_retargetmodifier3d.md#class-retargetmodifier3d-constant-transform-flag-rotation).

---


<a id="class-retargetmodifier3d-method-is-scale-enabled"></a>

[bool](class_bool.md#class-bool) **is_scale_enabled**() const [🔗](class_retargetmodifier3d.md#class-retargetmodifier3d-method-is-scale-enabled)

Returns `true` if [enable](class_retargetmodifier3d.md#class-retargetmodifier3d-property-enable) has [TRANSFORM_FLAG_SCALE](class_retargetmodifier3d.md#class-retargetmodifier3d-constant-transform-flag-scale).

---


<a id="class-retargetmodifier3d-method-set-position-enabled"></a>

void **set_position_enabled**(enabled: [bool](class_bool.md#class-bool)) [🔗](class_retargetmodifier3d.md#class-retargetmodifier3d-method-set-position-enabled)

Sets [TRANSFORM_FLAG_POSITION](class_retargetmodifier3d.md#class-retargetmodifier3d-constant-transform-flag-position) into [enable](class_retargetmodifier3d.md#class-retargetmodifier3d-property-enable).

---


<a id="class-retargetmodifier3d-method-set-rotation-enabled"></a>

void **set_rotation_enabled**(enabled: [bool](class_bool.md#class-bool)) [🔗](class_retargetmodifier3d.md#class-retargetmodifier3d-method-set-rotation-enabled)

Sets [TRANSFORM_FLAG_ROTATION](class_retargetmodifier3d.md#class-retargetmodifier3d-constant-transform-flag-rotation) into [enable](class_retargetmodifier3d.md#class-retargetmodifier3d-property-enable).

---


<a id="class-retargetmodifier3d-method-set-scale-enabled"></a>

void **set_scale_enabled**(enabled: [bool](class_bool.md#class-bool)) [🔗](class_retargetmodifier3d.md#class-retargetmodifier3d-method-set-scale-enabled)

Sets [TRANSFORM_FLAG_SCALE](class_retargetmodifier3d.md#class-retargetmodifier3d-constant-transform-flag-scale) into [enable](class_retargetmodifier3d.md#class-retargetmodifier3d-property-enable).
