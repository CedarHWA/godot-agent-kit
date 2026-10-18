> Source: https://docs.godotengine.org/en/4.7/classes/class_twoboneik3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="twoboneik3d"></a>

<a id="class-twoboneik3d"></a>

# TwoBoneIK3D

**Inherits:** [IKModifier3D](class_ikmodifier3d.md#class-ikmodifier3d) **<** [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Rotation based intersection of two circles inverse kinematics solver.

<a id="description"></a>

## Description

This [IKModifier3D](class_ikmodifier3d.md#class-ikmodifier3d) requires a pole target. It provides deterministic results by constructing a plane from each joint and pole target and finding the intersection of two circles (disks in 3D).

This IK can handle twist by setting the pole direction. If there are more than one bone between each set bone, their rotations are ignored, and the straight line connecting the root-middle and middle-end joints are treated as virtual bones.

**Note:** All the methods in this class take an `index` parameter. This parameter specifies which setting list entry to return if the IK has multiple entries (e.g. `settings/<index>/root_bone_name`).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [setting_count](class_twoboneik3d.md#class-twoboneik3d-property-setting-count) | `0` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [int](class_int.md#class-int) | [get_end_bone](class_twoboneik3d.md#class-twoboneik3d-method-get-end-bone)(index: [int](class_int.md#class-int)) const |
| [BoneDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-bonedirection) | [get_end_bone_direction](class_twoboneik3d.md#class-twoboneik3d-method-get-end-bone-direction)(index: [int](class_int.md#class-int)) const |
| [float](class_float.md#class-float) | [get_end_bone_length](class_twoboneik3d.md#class-twoboneik3d-method-get-end-bone-length)(index: [int](class_int.md#class-int)) const |
| [String](class_string.md#class-string) | [get_end_bone_name](class_twoboneik3d.md#class-twoboneik3d-method-get-end-bone-name)(index: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_middle_bone](class_twoboneik3d.md#class-twoboneik3d-method-get-middle-bone)(index: [int](class_int.md#class-int)) const |
| [String](class_string.md#class-string) | [get_middle_bone_name](class_twoboneik3d.md#class-twoboneik3d-method-get-middle-bone-name)(index: [int](class_int.md#class-int)) const |
| [SecondaryDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-secondarydirection) | [get_pole_direction](class_twoboneik3d.md#class-twoboneik3d-method-get-pole-direction)(index: [int](class_int.md#class-int)) const |
| [Vector3](class_vector3.md#class-vector3) | [get_pole_direction_vector](class_twoboneik3d.md#class-twoboneik3d-method-get-pole-direction-vector)(index: [int](class_int.md#class-int)) const |
| [NodePath](class_nodepath.md#class-nodepath) | [get_pole_node](class_twoboneik3d.md#class-twoboneik3d-method-get-pole-node)(index: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_root_bone](class_twoboneik3d.md#class-twoboneik3d-method-get-root-bone)(index: [int](class_int.md#class-int)) const |
| [String](class_string.md#class-string) | [get_root_bone_name](class_twoboneik3d.md#class-twoboneik3d-method-get-root-bone-name)(index: [int](class_int.md#class-int)) const |
| [NodePath](class_nodepath.md#class-nodepath) | [get_target_node](class_twoboneik3d.md#class-twoboneik3d-method-get-target-node)(index: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [is_end_bone_extended](class_twoboneik3d.md#class-twoboneik3d-method-is-end-bone-extended)(index: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [is_using_virtual_end](class_twoboneik3d.md#class-twoboneik3d-method-is-using-virtual-end)(index: [int](class_int.md#class-int)) const |
| void | [set_end_bone](class_twoboneik3d.md#class-twoboneik3d-method-set-end-bone)(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int)) |
| void | [set_end_bone_direction](class_twoboneik3d.md#class-twoboneik3d-method-set-end-bone-direction)(index: [int](class_int.md#class-int), bone_direction: [BoneDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-bonedirection)) |
| void | [set_end_bone_length](class_twoboneik3d.md#class-twoboneik3d-method-set-end-bone-length)(index: [int](class_int.md#class-int), length: [float](class_float.md#class-float)) |
| void | [set_end_bone_name](class_twoboneik3d.md#class-twoboneik3d-method-set-end-bone-name)(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string)) |
| void | [set_extend_end_bone](class_twoboneik3d.md#class-twoboneik3d-method-set-extend-end-bone)(index: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool)) |
| void | [set_middle_bone](class_twoboneik3d.md#class-twoboneik3d-method-set-middle-bone)(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int)) |
| void | [set_middle_bone_name](class_twoboneik3d.md#class-twoboneik3d-method-set-middle-bone-name)(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string)) |
| void | [set_pole_direction](class_twoboneik3d.md#class-twoboneik3d-method-set-pole-direction)(index: [int](class_int.md#class-int), direction: [SecondaryDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-secondarydirection)) |
| void | [set_pole_direction_vector](class_twoboneik3d.md#class-twoboneik3d-method-set-pole-direction-vector)(index: [int](class_int.md#class-int), vector: [Vector3](class_vector3.md#class-vector3)) |
| void | [set_pole_node](class_twoboneik3d.md#class-twoboneik3d-method-set-pole-node)(index: [int](class_int.md#class-int), pole_node: [NodePath](class_nodepath.md#class-nodepath)) |
| void | [set_root_bone](class_twoboneik3d.md#class-twoboneik3d-method-set-root-bone)(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int)) |
| void | [set_root_bone_name](class_twoboneik3d.md#class-twoboneik3d-method-set-root-bone-name)(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string)) |
| void | [set_target_node](class_twoboneik3d.md#class-twoboneik3d-method-set-target-node)(index: [int](class_int.md#class-int), target_node: [NodePath](class_nodepath.md#class-nodepath)) |
| void | [set_use_virtual_end](class_twoboneik3d.md#class-twoboneik3d-method-set-use-virtual-end)(index: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool)) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-twoboneik3d-property-setting-count"></a>

[int](class_int.md#class-int) **setting_count** = `0` [🔗](class_twoboneik3d.md#class-twoboneik3d-property-setting-count)

- void **set_setting_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_setting_count**()

The number of settings.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-twoboneik3d-method-get-end-bone"></a>

[int](class_int.md#class-int) **get_end_bone**(index: [int](class_int.md#class-int)) const [🔗](class_twoboneik3d.md#class-twoboneik3d-method-get-end-bone)

Returns the end bone index.

---


<a id="class-twoboneik3d-method-get-end-bone-direction"></a>

[BoneDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-bonedirection) **get_end_bone_direction**(index: [int](class_int.md#class-int)) const [🔗](class_twoboneik3d.md#class-twoboneik3d-method-get-end-bone-direction)

Returns the end bone's tail direction when [is_end_bone_extended()](class_twoboneik3d.md#class-twoboneik3d-method-is-end-bone-extended) is `true`.

---


<a id="class-twoboneik3d-method-get-end-bone-length"></a>

[float](class_float.md#class-float) **get_end_bone_length**(index: [int](class_int.md#class-int)) const [🔗](class_twoboneik3d.md#class-twoboneik3d-method-get-end-bone-length)

Returns the end bone tail length of the bone chain when [is_end_bone_extended()](class_twoboneik3d.md#class-twoboneik3d-method-is-end-bone-extended) is `true`.

---


<a id="class-twoboneik3d-method-get-end-bone-name"></a>

[String](class_string.md#class-string) **get_end_bone_name**(index: [int](class_int.md#class-int)) const [🔗](class_twoboneik3d.md#class-twoboneik3d-method-get-end-bone-name)

Returns the end bone name.

---


<a id="class-twoboneik3d-method-get-middle-bone"></a>

[int](class_int.md#class-int) **get_middle_bone**(index: [int](class_int.md#class-int)) const [🔗](class_twoboneik3d.md#class-twoboneik3d-method-get-middle-bone)

Returns the middle bone index.

---


<a id="class-twoboneik3d-method-get-middle-bone-name"></a>

[String](class_string.md#class-string) **get_middle_bone_name**(index: [int](class_int.md#class-int)) const [🔗](class_twoboneik3d.md#class-twoboneik3d-method-get-middle-bone-name)

Returns the middle bone name.

---


<a id="class-twoboneik3d-method-get-pole-direction"></a>

[SecondaryDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-secondarydirection) **get_pole_direction**(index: [int](class_int.md#class-int)) const [🔗](class_twoboneik3d.md#class-twoboneik3d-method-get-pole-direction)

Returns the pole direction.

---


<a id="class-twoboneik3d-method-get-pole-direction-vector"></a>

[Vector3](class_vector3.md#class-vector3) **get_pole_direction_vector**(index: [int](class_int.md#class-int)) const [🔗](class_twoboneik3d.md#class-twoboneik3d-method-get-pole-direction-vector)

Returns the pole direction vector.

If [get_pole_direction()](class_twoboneik3d.md#class-twoboneik3d-method-get-pole-direction) is [SkeletonModifier3D.SECONDARY_DIRECTION_NONE](class_skeletonmodifier3d.md#class-skeletonmodifier3d-constant-secondary-direction-none), this method returns `Vector3(0, 0, 0)`.

---


<a id="class-twoboneik3d-method-get-pole-node"></a>

[NodePath](class_nodepath.md#class-nodepath) **get_pole_node**(index: [int](class_int.md#class-int)) const [🔗](class_twoboneik3d.md#class-twoboneik3d-method-get-pole-node)

Returns the pole target node that constructs a plane which the joints are all on and the pole is trying to direct.

---


<a id="class-twoboneik3d-method-get-root-bone"></a>

[int](class_int.md#class-int) **get_root_bone**(index: [int](class_int.md#class-int)) const [🔗](class_twoboneik3d.md#class-twoboneik3d-method-get-root-bone)

Returns the root bone index.

---


<a id="class-twoboneik3d-method-get-root-bone-name"></a>

[String](class_string.md#class-string) **get_root_bone_name**(index: [int](class_int.md#class-int)) const [🔗](class_twoboneik3d.md#class-twoboneik3d-method-get-root-bone-name)

Returns the root bone name.

---


<a id="class-twoboneik3d-method-get-target-node"></a>

[NodePath](class_nodepath.md#class-nodepath) **get_target_node**(index: [int](class_int.md#class-int)) const [🔗](class_twoboneik3d.md#class-twoboneik3d-method-get-target-node)

Returns the target node that the end bone is trying to reach.

---


<a id="class-twoboneik3d-method-is-end-bone-extended"></a>

[bool](class_bool.md#class-bool) **is_end_bone_extended**(index: [int](class_int.md#class-int)) const [🔗](class_twoboneik3d.md#class-twoboneik3d-method-is-end-bone-extended)

Returns `true` if the end bone is extended to have a tail.

---


<a id="class-twoboneik3d-method-is-using-virtual-end"></a>

[bool](class_bool.md#class-bool) **is_using_virtual_end**(index: [int](class_int.md#class-int)) const [🔗](class_twoboneik3d.md#class-twoboneik3d-method-is-using-virtual-end)

Returns `true` if the end bone is extended from the middle bone as a virtual bone.

---


<a id="class-twoboneik3d-method-set-end-bone"></a>

void **set_end_bone**(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int)) [🔗](class_twoboneik3d.md#class-twoboneik3d-method-set-end-bone)

Sets the end bone index.

---


<a id="class-twoboneik3d-method-set-end-bone-direction"></a>

void **set_end_bone_direction**(index: [int](class_int.md#class-int), bone_direction: [BoneDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-bonedirection)) [🔗](class_twoboneik3d.md#class-twoboneik3d-method-set-end-bone-direction)

Sets the end bone tail direction when [is_end_bone_extended()](class_twoboneik3d.md#class-twoboneik3d-method-is-end-bone-extended) is `true`.

---


<a id="class-twoboneik3d-method-set-end-bone-length"></a>

void **set_end_bone_length**(index: [int](class_int.md#class-int), length: [float](class_float.md#class-float)) [🔗](class_twoboneik3d.md#class-twoboneik3d-method-set-end-bone-length)

Sets the end bone tail length when [is_end_bone_extended()](class_twoboneik3d.md#class-twoboneik3d-method-is-end-bone-extended) is `true`.

---


<a id="class-twoboneik3d-method-set-end-bone-name"></a>

void **set_end_bone_name**(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string)) [🔗](class_twoboneik3d.md#class-twoboneik3d-method-set-end-bone-name)

Sets the end bone name.

**Note:** The end bone must be a child of the middle bone.

---


<a id="class-twoboneik3d-method-set-extend-end-bone"></a>

void **set_extend_end_bone**(index: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool)) [🔗](class_twoboneik3d.md#class-twoboneik3d-method-set-extend-end-bone)

If `enabled` is `true`, the end bone is extended to have a tail.

---


<a id="class-twoboneik3d-method-set-middle-bone"></a>

void **set_middle_bone**(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int)) [🔗](class_twoboneik3d.md#class-twoboneik3d-method-set-middle-bone)

Sets the middle bone index.

---


<a id="class-twoboneik3d-method-set-middle-bone-name"></a>

void **set_middle_bone_name**(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string)) [🔗](class_twoboneik3d.md#class-twoboneik3d-method-set-middle-bone-name)

Sets the middle bone name.

**Note:** The middle bone must be a child of the root bone.

---


<a id="class-twoboneik3d-method-set-pole-direction"></a>

void **set_pole_direction**(index: [int](class_int.md#class-int), direction: [SecondaryDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-secondarydirection)) [🔗](class_twoboneik3d.md#class-twoboneik3d-method-set-pole-direction)

Sets the pole direction.

The pole is on the middle bone and will direct to the pole target.

The rotation axis is a vector that is orthogonal to this and the forward vector.

**Note:** The pole direction and the forward vector shouldn't be colinear to avoid unintended rotation.

---


<a id="class-twoboneik3d-method-set-pole-direction-vector"></a>

void **set_pole_direction_vector**(index: [int](class_int.md#class-int), vector: [Vector3](class_vector3.md#class-vector3)) [🔗](class_twoboneik3d.md#class-twoboneik3d-method-set-pole-direction-vector)

Sets the pole direction vector.

This vector is normalized by an internal process.

If the vector length is `0`, it is considered synonymous with [SkeletonModifier3D.SECONDARY_DIRECTION_NONE](class_skeletonmodifier3d.md#class-skeletonmodifier3d-constant-secondary-direction-none).

---


<a id="class-twoboneik3d-method-set-pole-node"></a>

void **set_pole_node**(index: [int](class_int.md#class-int), pole_node: [NodePath](class_nodepath.md#class-nodepath)) [🔗](class_twoboneik3d.md#class-twoboneik3d-method-set-pole-node)

Sets the pole target node that constructs a plane which the joints are all on and the pole is trying to direct.

---


<a id="class-twoboneik3d-method-set-root-bone"></a>

void **set_root_bone**(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int)) [🔗](class_twoboneik3d.md#class-twoboneik3d-method-set-root-bone)

Sets the root bone index.

---


<a id="class-twoboneik3d-method-set-root-bone-name"></a>

void **set_root_bone_name**(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string)) [🔗](class_twoboneik3d.md#class-twoboneik3d-method-set-root-bone-name)

Sets the root bone name.

---


<a id="class-twoboneik3d-method-set-target-node"></a>

void **set_target_node**(index: [int](class_int.md#class-int), target_node: [NodePath](class_nodepath.md#class-nodepath)) [🔗](class_twoboneik3d.md#class-twoboneik3d-method-set-target-node)

Sets the target node that the end bone is trying to reach.

---


<a id="class-twoboneik3d-method-set-use-virtual-end"></a>

void **set_use_virtual_end**(index: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool)) [🔗](class_twoboneik3d.md#class-twoboneik3d-method-set-use-virtual-end)

If `enabled` is `true`, the end bone is extended from the middle bone as a virtual bone.
