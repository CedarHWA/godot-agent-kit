> Source: https://docs.godotengine.org/en/4.7/classes/class_skeletonmodifier3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="skeletonmodifier3d"></a>

<a id="class-skeletonmodifier3d"></a>

# SkeletonModifier3D

**Inherits:** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [BoneConstraint3D](class_boneconstraint3d.md#class-boneconstraint3d), [BoneTwistDisperser3D](class_bonetwistdisperser3d.md#class-bonetwistdisperser3d), [IKModifier3D](class_ikmodifier3d.md#class-ikmodifier3d), [LimitAngularVelocityModifier3D](class_limitangularvelocitymodifier3d.md#class-limitangularvelocitymodifier3d), [LookAtModifier3D](class_lookatmodifier3d.md#class-lookatmodifier3d), [ModifierBoneTarget3D](class_modifierbonetarget3d.md#class-modifierbonetarget3d), [PhysicalBoneSimulator3D](class_physicalbonesimulator3d.md#class-physicalbonesimulator3d), [RetargetModifier3D](class_retargetmodifier3d.md#class-retargetmodifier3d), [SkeletonIK3D](class_skeletonik3d.md#class-skeletonik3d), [SpringBoneSimulator3D](class_springbonesimulator3d.md#class-springbonesimulator3d), [XRBodyModifier3D](class_xrbodymodifier3d.md#class-xrbodymodifier3d), [XRHandModifier3D](class_xrhandmodifier3d.md#class-xrhandmodifier3d)

A node that may modify a Skeleton3D's bones.

<a id="description"></a>

## Description

**SkeletonModifier3D** retrieves a target [Skeleton3D](class_skeleton3d.md#class-skeleton3d) by having a [Skeleton3D](class_skeleton3d.md#class-skeleton3d) parent.

If there is an [AnimationMixer](class_animationmixer.md#class-animationmixer), a modification always performs after playback process of the [AnimationMixer](class_animationmixer.md#class-animationmixer).

This node should be used to implement custom IK solvers, constraints, or skeleton physics.

<a id="tutorials"></a>

## Tutorials

- [Design of the Skeleton Modifier 3D](https://godotengine.org/article/design-of-the-skeleton-modifier-3d/)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [active](class_skeletonmodifier3d.md#class-skeletonmodifier3d-property-active) | `true` |
| [float](class_float.md#class-float) | [influence](class_skeletonmodifier3d.md#class-skeletonmodifier3d-property-influence) | `1.0` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [_process_modification](class_skeletonmodifier3d.md#class-skeletonmodifier3d-private-method-process-modification)() virtual |
| void | [_process_modification_with_delta](class_skeletonmodifier3d.md#class-skeletonmodifier3d-private-method-process-modification-with-delta)(delta: [float](class_float.md#class-float)) virtual |
| void | [_skeleton_changed](class_skeletonmodifier3d.md#class-skeletonmodifier3d-private-method-skeleton-changed)(old_skeleton: [Skeleton3D](class_skeleton3d.md#class-skeleton3d), new_skeleton: [Skeleton3D](class_skeleton3d.md#class-skeleton3d)) virtual |
| void | [_validate_bone_names](class_skeletonmodifier3d.md#class-skeletonmodifier3d-private-method-validate-bone-names)() virtual |
| [Skeleton3D](class_skeleton3d.md#class-skeleton3d) | [get_skeleton](class_skeletonmodifier3d.md#class-skeletonmodifier3d-method-get-skeleton)() const |

---


<a id="signals"></a>

## Signals

<a id="class-skeletonmodifier3d-signal-modification-processed"></a>

**modification_processed**() [🔗](class_skeletonmodifier3d.md#class-skeletonmodifier3d-signal-modification-processed)

Notifies when the modification have been finished.

**Note:** If you want to get the modified bone pose by the modifier, you must use [Skeleton3D.get_bone_pose()](class_skeleton3d.md#class-skeleton3d-method-get-bone-pose) or [Skeleton3D.get_bone_global_pose()](class_skeleton3d.md#class-skeleton3d-method-get-bone-global-pose) at the moment this signal is fired.

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-skeletonmodifier3d-boneaxis"></a>

enum **BoneAxis**: [🔗](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-boneaxis)

<a id="class-skeletonmodifier3d-constant-bone-axis-plus-x"></a>

[BoneAxis](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-boneaxis) **BONE_AXIS_PLUS_X** = `0`

Enumerated value for the +X axis.

<a id="class-skeletonmodifier3d-constant-bone-axis-minus-x"></a>

[BoneAxis](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-boneaxis) **BONE_AXIS_MINUS_X** = `1`

Enumerated value for the -X axis.

<a id="class-skeletonmodifier3d-constant-bone-axis-plus-y"></a>

[BoneAxis](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-boneaxis) **BONE_AXIS_PLUS_Y** = `2`

Enumerated value for the +Y axis.

<a id="class-skeletonmodifier3d-constant-bone-axis-minus-y"></a>

[BoneAxis](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-boneaxis) **BONE_AXIS_MINUS_Y** = `3`

Enumerated value for the -Y axis.

<a id="class-skeletonmodifier3d-constant-bone-axis-plus-z"></a>

[BoneAxis](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-boneaxis) **BONE_AXIS_PLUS_Z** = `4`

Enumerated value for the +Z axis.

<a id="class-skeletonmodifier3d-constant-bone-axis-minus-z"></a>

[BoneAxis](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-boneaxis) **BONE_AXIS_MINUS_Z** = `5`

Enumerated value for the -Z axis.

---


<a id="enum-skeletonmodifier3d-bonedirection"></a>

enum **BoneDirection**: [🔗](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-bonedirection)

<a id="class-skeletonmodifier3d-constant-bone-direction-plus-x"></a>

[BoneDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-bonedirection) **BONE_DIRECTION_PLUS_X** = `0`

Enumerated value for the +X axis.

<a id="class-skeletonmodifier3d-constant-bone-direction-minus-x"></a>

[BoneDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-bonedirection) **BONE_DIRECTION_MINUS_X** = `1`

Enumerated value for the -X axis.

<a id="class-skeletonmodifier3d-constant-bone-direction-plus-y"></a>

[BoneDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-bonedirection) **BONE_DIRECTION_PLUS_Y** = `2`

Enumerated value for the +Y axis.

<a id="class-skeletonmodifier3d-constant-bone-direction-minus-y"></a>

[BoneDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-bonedirection) **BONE_DIRECTION_MINUS_Y** = `3`

Enumerated value for the -Y axis.

<a id="class-skeletonmodifier3d-constant-bone-direction-plus-z"></a>

[BoneDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-bonedirection) **BONE_DIRECTION_PLUS_Z** = `4`

Enumerated value for the +Z axis.

<a id="class-skeletonmodifier3d-constant-bone-direction-minus-z"></a>

[BoneDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-bonedirection) **BONE_DIRECTION_MINUS_Z** = `5`

Enumerated value for the -Z axis.

<a id="class-skeletonmodifier3d-constant-bone-direction-from-parent"></a>

[BoneDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-bonedirection) **BONE_DIRECTION_FROM_PARENT** = `6`

Enumerated value for the axis from a parent bone to the child bone.

---


<a id="enum-skeletonmodifier3d-secondarydirection"></a>

enum **SecondaryDirection**: [🔗](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-secondarydirection)

<a id="class-skeletonmodifier3d-constant-secondary-direction-none"></a>

[SecondaryDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-secondarydirection) **SECONDARY_DIRECTION_NONE** = `0`

Enumerated value for the case when the axis is undefined.

<a id="class-skeletonmodifier3d-constant-secondary-direction-plus-x"></a>

[SecondaryDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-secondarydirection) **SECONDARY_DIRECTION_PLUS_X** = `1`

Enumerated value for the +X axis.

<a id="class-skeletonmodifier3d-constant-secondary-direction-minus-x"></a>

[SecondaryDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-secondarydirection) **SECONDARY_DIRECTION_MINUS_X** = `2`

Enumerated value for the -X axis.

<a id="class-skeletonmodifier3d-constant-secondary-direction-plus-y"></a>

[SecondaryDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-secondarydirection) **SECONDARY_DIRECTION_PLUS_Y** = `3`

Enumerated value for the +Y axis.

<a id="class-skeletonmodifier3d-constant-secondary-direction-minus-y"></a>

[SecondaryDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-secondarydirection) **SECONDARY_DIRECTION_MINUS_Y** = `4`

Enumerated value for the -Y axis.

<a id="class-skeletonmodifier3d-constant-secondary-direction-plus-z"></a>

[SecondaryDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-secondarydirection) **SECONDARY_DIRECTION_PLUS_Z** = `5`

Enumerated value for the +Z axis.

<a id="class-skeletonmodifier3d-constant-secondary-direction-minus-z"></a>

[SecondaryDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-secondarydirection) **SECONDARY_DIRECTION_MINUS_Z** = `6`

Enumerated value for the -Z axis.

<a id="class-skeletonmodifier3d-constant-secondary-direction-custom"></a>

[SecondaryDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-secondarydirection) **SECONDARY_DIRECTION_CUSTOM** = `7`

Enumerated value for an optional axis.

---


<a id="enum-skeletonmodifier3d-rotationaxis"></a>

enum **RotationAxis**: [🔗](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-rotationaxis)

<a id="class-skeletonmodifier3d-constant-rotation-axis-x"></a>

[RotationAxis](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-rotationaxis) **ROTATION_AXIS_X** = `0`

Enumerated value for the rotation of the X axis.

<a id="class-skeletonmodifier3d-constant-rotation-axis-y"></a>

[RotationAxis](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-rotationaxis) **ROTATION_AXIS_Y** = `1`

Enumerated value for the rotation of the Y axis.

<a id="class-skeletonmodifier3d-constant-rotation-axis-z"></a>

[RotationAxis](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-rotationaxis) **ROTATION_AXIS_Z** = `2`

Enumerated value for the rotation of the Z axis.

<a id="class-skeletonmodifier3d-constant-rotation-axis-all"></a>

[RotationAxis](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-rotationaxis) **ROTATION_AXIS_ALL** = `3`

Enumerated value for the unconstrained rotation.

<a id="class-skeletonmodifier3d-constant-rotation-axis-custom"></a>

[RotationAxis](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-rotationaxis) **ROTATION_AXIS_CUSTOM** = `4`

Enumerated value for an optional rotation axis.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-skeletonmodifier3d-property-active"></a>

[bool](class_bool.md#class-bool) **active** = `true` [🔗](class_skeletonmodifier3d.md#class-skeletonmodifier3d-property-active)

- void **set_active**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_active**()

If `true`, the **SkeletonModifier3D** will be processing.

---


<a id="class-skeletonmodifier3d-property-influence"></a>

[float](class_float.md#class-float) **influence** = `1.0` [🔗](class_skeletonmodifier3d.md#class-skeletonmodifier3d-property-influence)

- void **set_influence**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_influence**()

Sets the influence of the modification.

**Note:** This value is used by [Skeleton3D](class_skeleton3d.md#class-skeleton3d) to blend, so the **SkeletonModifier3D** should always apply only 100% of the result without interpolation.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-skeletonmodifier3d-private-method-process-modification"></a>

void **_process_modification**() virtual [🔗](class_skeletonmodifier3d.md#class-skeletonmodifier3d-private-method-process-modification)

**Deprecated:** Use [_process_modification_with_delta()](class_skeletonmodifier3d.md#class-skeletonmodifier3d-private-method-process-modification-with-delta) instead.

Override this virtual method to implement a custom skeleton modifier. You should do things like get the [Skeleton3D](class_skeleton3d.md#class-skeleton3d)'s current pose and apply the pose here.

[_process_modification()](class_skeletonmodifier3d.md#class-skeletonmodifier3d-private-method-process-modification) must not apply [influence](class_skeletonmodifier3d.md#class-skeletonmodifier3d-property-influence) to bone poses because the [Skeleton3D](class_skeleton3d.md#class-skeleton3d) automatically applies influence to all bone poses set by the modifier.

---


<a id="class-skeletonmodifier3d-private-method-process-modification-with-delta"></a>

void **_process_modification_with_delta**(delta: [float](class_float.md#class-float)) virtual [🔗](class_skeletonmodifier3d.md#class-skeletonmodifier3d-private-method-process-modification-with-delta)

Override this virtual method to implement a custom skeleton modifier. You should do things like get the [Skeleton3D](class_skeleton3d.md#class-skeleton3d)'s current pose and apply the pose here.

[_process_modification_with_delta()](class_skeletonmodifier3d.md#class-skeletonmodifier3d-private-method-process-modification-with-delta) must not apply [influence](class_skeletonmodifier3d.md#class-skeletonmodifier3d-property-influence) to bone poses because the [Skeleton3D](class_skeleton3d.md#class-skeleton3d) automatically applies influence to all bone poses set by the modifier.

`delta` is passed from parent [Skeleton3D](class_skeleton3d.md#class-skeleton3d). See also [Skeleton3D.advance()](class_skeleton3d.md#class-skeleton3d-method-advance).

**Note:** This method may be called outside [Node._process()](class_node.md#class-node-private-method-process) and [Node._physics_process()](class_node.md#class-node-private-method-physics-process) with `delta` is `0.0`, since the modification should be processed immediately after initialization of the [Skeleton3D](class_skeleton3d.md#class-skeleton3d).

---


<a id="class-skeletonmodifier3d-private-method-skeleton-changed"></a>

void **_skeleton_changed**(old_skeleton: [Skeleton3D](class_skeleton3d.md#class-skeleton3d), new_skeleton: [Skeleton3D](class_skeleton3d.md#class-skeleton3d)) virtual [🔗](class_skeletonmodifier3d.md#class-skeletonmodifier3d-private-method-skeleton-changed)

Called when the skeleton is changed.

---


<a id="class-skeletonmodifier3d-private-method-validate-bone-names"></a>

void **_validate_bone_names**() virtual [🔗](class_skeletonmodifier3d.md#class-skeletonmodifier3d-private-method-validate-bone-names)

Called when bone names and indices need to be validated, such as when entering the scene tree or changing skeleton.

---


<a id="class-skeletonmodifier3d-method-get-skeleton"></a>

[Skeleton3D](class_skeleton3d.md#class-skeleton3d) **get_skeleton**() const [🔗](class_skeletonmodifier3d.md#class-skeletonmodifier3d-method-get-skeleton)

Returns the parent [Skeleton3D](class_skeleton3d.md#class-skeleton3d) node if it exists. Otherwise, returns `null`.
