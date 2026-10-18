> Source: https://docs.godotengine.org/en/4.7/classes/class_chainik3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="chainik3d"></a>

<a id="class-chainik3d"></a>

# ChainIK3D

**Inherits:** [IKModifier3D](class_ikmodifier3d.md#class-ikmodifier3d) **<** [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [IterateIK3D](class_iterateik3d.md#class-iterateik3d), [SplineIK3D](class_splineik3d.md#class-splineik3d)

A [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) to apply inverse kinematics to bone chains containing an arbitrary number of bones.

<a id="description"></a>

## Description

Base class of [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) that automatically generates a joint list from the bones between the root bone and the end bone.

**Note:** All the methods in this class take an `index` parameter. This parameter specifies which setting list entry to return if the IK has multiple entries (e.g. `settings/<index>/root_bone_name`).

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [int](class_int.md#class-int) | [get_end_bone](class_chainik3d.md#class-chainik3d-method-get-end-bone)(index: [int](class_int.md#class-int)) const |
| [BoneDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-bonedirection) | [get_end_bone_direction](class_chainik3d.md#class-chainik3d-method-get-end-bone-direction)(index: [int](class_int.md#class-int)) const |
| [float](class_float.md#class-float) | [get_end_bone_length](class_chainik3d.md#class-chainik3d-method-get-end-bone-length)(index: [int](class_int.md#class-int)) const |
| [String](class_string.md#class-string) | [get_end_bone_name](class_chainik3d.md#class-chainik3d-method-get-end-bone-name)(index: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_joint_bone](class_chainik3d.md#class-chainik3d-method-get-joint-bone)(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int)) const |
| [String](class_string.md#class-string) | [get_joint_bone_name](class_chainik3d.md#class-chainik3d-method-get-joint-bone-name)(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_joint_count](class_chainik3d.md#class-chainik3d-method-get-joint-count)(index: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_root_bone](class_chainik3d.md#class-chainik3d-method-get-root-bone)(index: [int](class_int.md#class-int)) const |
| [String](class_string.md#class-string) | [get_root_bone_name](class_chainik3d.md#class-chainik3d-method-get-root-bone-name)(index: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [is_end_bone_extended](class_chainik3d.md#class-chainik3d-method-is-end-bone-extended)(index: [int](class_int.md#class-int)) const |
| void | [set_end_bone](class_chainik3d.md#class-chainik3d-method-set-end-bone)(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int)) |
| void | [set_end_bone_direction](class_chainik3d.md#class-chainik3d-method-set-end-bone-direction)(index: [int](class_int.md#class-int), bone_direction: [BoneDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-bonedirection)) |
| void | [set_end_bone_length](class_chainik3d.md#class-chainik3d-method-set-end-bone-length)(index: [int](class_int.md#class-int), length: [float](class_float.md#class-float)) |
| void | [set_end_bone_name](class_chainik3d.md#class-chainik3d-method-set-end-bone-name)(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string)) |
| void | [set_extend_end_bone](class_chainik3d.md#class-chainik3d-method-set-extend-end-bone)(index: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool)) |
| void | [set_root_bone](class_chainik3d.md#class-chainik3d-method-set-root-bone)(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int)) |
| void | [set_root_bone_name](class_chainik3d.md#class-chainik3d-method-set-root-bone-name)(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string)) |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-chainik3d-method-get-end-bone"></a>

[int](class_int.md#class-int) **get_end_bone**(index: [int](class_int.md#class-int)) const [🔗](class_chainik3d.md#class-chainik3d-method-get-end-bone)

Returns the end bone index of the bone chain.

---


<a id="class-chainik3d-method-get-end-bone-direction"></a>

[BoneDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-bonedirection) **get_end_bone_direction**(index: [int](class_int.md#class-int)) const [🔗](class_chainik3d.md#class-chainik3d-method-get-end-bone-direction)

Returns the tail direction of the end bone of the bone chain when [is_end_bone_extended()](class_chainik3d.md#class-chainik3d-method-is-end-bone-extended) is `true`.

---


<a id="class-chainik3d-method-get-end-bone-length"></a>

[float](class_float.md#class-float) **get_end_bone_length**(index: [int](class_int.md#class-int)) const [🔗](class_chainik3d.md#class-chainik3d-method-get-end-bone-length)

Returns the end bone tail length of the bone chain when [is_end_bone_extended()](class_chainik3d.md#class-chainik3d-method-is-end-bone-extended) is `true`.

---


<a id="class-chainik3d-method-get-end-bone-name"></a>

[String](class_string.md#class-string) **get_end_bone_name**(index: [int](class_int.md#class-int)) const [🔗](class_chainik3d.md#class-chainik3d-method-get-end-bone-name)

Returns the end bone name of the bone chain.

---


<a id="class-chainik3d-method-get-joint-bone"></a>

[int](class_int.md#class-int) **get_joint_bone**(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int)) const [🔗](class_chainik3d.md#class-chainik3d-method-get-joint-bone)

Returns the bone index at `joint` in the bone chain's joint list.

---


<a id="class-chainik3d-method-get-joint-bone-name"></a>

[String](class_string.md#class-string) **get_joint_bone_name**(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int)) const [🔗](class_chainik3d.md#class-chainik3d-method-get-joint-bone-name)

Returns the bone name at `joint` in the bone chain's joint list.

---


<a id="class-chainik3d-method-get-joint-count"></a>

[int](class_int.md#class-int) **get_joint_count**(index: [int](class_int.md#class-int)) const [🔗](class_chainik3d.md#class-chainik3d-method-get-joint-count)

Returns the joint count of the bone chain's joint list.

---


<a id="class-chainik3d-method-get-root-bone"></a>

[int](class_int.md#class-int) **get_root_bone**(index: [int](class_int.md#class-int)) const [🔗](class_chainik3d.md#class-chainik3d-method-get-root-bone)

Returns the root bone index of the bone chain.

---


<a id="class-chainik3d-method-get-root-bone-name"></a>

[String](class_string.md#class-string) **get_root_bone_name**(index: [int](class_int.md#class-int)) const [🔗](class_chainik3d.md#class-chainik3d-method-get-root-bone-name)

Returns the root bone name of the bone chain.

---


<a id="class-chainik3d-method-is-end-bone-extended"></a>

[bool](class_bool.md#class-bool) **is_end_bone_extended**(index: [int](class_int.md#class-int)) const [🔗](class_chainik3d.md#class-chainik3d-method-is-end-bone-extended)

Returns `true` if the end bone is extended to have a tail.

---


<a id="class-chainik3d-method-set-end-bone"></a>

void **set_end_bone**(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int)) [🔗](class_chainik3d.md#class-chainik3d-method-set-end-bone)

Sets the end bone index of the bone chain.

---


<a id="class-chainik3d-method-set-end-bone-direction"></a>

void **set_end_bone_direction**(index: [int](class_int.md#class-int), bone_direction: [BoneDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-bonedirection)) [🔗](class_chainik3d.md#class-chainik3d-method-set-end-bone-direction)

Sets the end bone tail direction of the bone chain when [is_end_bone_extended()](class_chainik3d.md#class-chainik3d-method-is-end-bone-extended) is `true`.

---


<a id="class-chainik3d-method-set-end-bone-length"></a>

void **set_end_bone_length**(index: [int](class_int.md#class-int), length: [float](class_float.md#class-float)) [🔗](class_chainik3d.md#class-chainik3d-method-set-end-bone-length)

Sets the end bone tail length of the bone chain when [is_end_bone_extended()](class_chainik3d.md#class-chainik3d-method-is-end-bone-extended) is `true`.

---


<a id="class-chainik3d-method-set-end-bone-name"></a>

void **set_end_bone_name**(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string)) [🔗](class_chainik3d.md#class-chainik3d-method-set-end-bone-name)

Sets the end bone name of the bone chain.

**Note:** The end bone must be the root bone or a child of the root bone. If they are the same, the tail must be extended by [set_extend_end_bone()](class_chainik3d.md#class-chainik3d-method-set-extend-end-bone) to modify the bone.

---


<a id="class-chainik3d-method-set-extend-end-bone"></a>

void **set_extend_end_bone**(index: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool)) [🔗](class_chainik3d.md#class-chainik3d-method-set-extend-end-bone)

If `enabled` is `true`, the end bone is extended to have a tail.

The extended tail config is allocated to the last element in the joint list. In other words, if you set `enabled` to `false`, the config of the last element in the joint list has no effect in the simulated result.

---


<a id="class-chainik3d-method-set-root-bone"></a>

void **set_root_bone**(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int)) [🔗](class_chainik3d.md#class-chainik3d-method-set-root-bone)

Sets the root bone index of the bone chain.

---


<a id="class-chainik3d-method-set-root-bone-name"></a>

void **set_root_bone_name**(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string)) [🔗](class_chainik3d.md#class-chainik3d-method-set-root-bone-name)

Sets the root bone name of the bone chain.
