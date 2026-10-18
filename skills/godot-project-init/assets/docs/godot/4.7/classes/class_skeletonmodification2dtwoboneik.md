> Source: https://docs.godotengine.org/en/4.7/classes/class_skeletonmodification2dtwoboneik.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="skeletonmodification2dtwoboneik"></a>

<a id="class-skeletonmodification2dtwoboneik"></a>

# SkeletonModification2DTwoBoneIK

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [SkeletonModification2D](class_skeletonmodification2d.md#class-skeletonmodification2d) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A modification that rotates two bones using the law of cosines to reach the target.

<a id="description"></a>

## Description

This [SkeletonModification2D](class_skeletonmodification2d.md#class-skeletonmodification2d) uses an algorithm typically called TwoBoneIK. This algorithm works by leveraging the law of cosines and the lengths of the bones to figure out what rotation the bones currently have, and what rotation they need to make a complete triangle, where the first bone, the second bone, and the target form the three vertices of the triangle. Because the algorithm works by making a triangle, it can only operate on two bones.

TwoBoneIK is great for arms, legs, and really any joints that can be represented by just two bones that bend to reach a target. This solver is more lightweight than [SkeletonModification2DFABRIK](class_skeletonmodification2dfabrik.md#class-skeletonmodification2dfabrik), but gives similar, natural looking results.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [flip_bend_direction](class_skeletonmodification2dtwoboneik.md#class-skeletonmodification2dtwoboneik-property-flip-bend-direction) | `false` |
| [float](class_float.md#class-float) | [target_maximum_distance](class_skeletonmodification2dtwoboneik.md#class-skeletonmodification2dtwoboneik-property-target-maximum-distance) | `0.0` |
| [float](class_float.md#class-float) | [target_minimum_distance](class_skeletonmodification2dtwoboneik.md#class-skeletonmodification2dtwoboneik-property-target-minimum-distance) | `0.0` |
| [NodePath](class_nodepath.md#class-nodepath) | [target_nodepath](class_skeletonmodification2dtwoboneik.md#class-skeletonmodification2dtwoboneik-property-target-nodepath) | `NodePath("")` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [NodePath](class_nodepath.md#class-nodepath) | [get_joint_one_bone2d_node](class_skeletonmodification2dtwoboneik.md#class-skeletonmodification2dtwoboneik-method-get-joint-one-bone2d-node)() const |
| [int](class_int.md#class-int) | [get_joint_one_bone_idx](class_skeletonmodification2dtwoboneik.md#class-skeletonmodification2dtwoboneik-method-get-joint-one-bone-idx)() const |
| [NodePath](class_nodepath.md#class-nodepath) | [get_joint_two_bone2d_node](class_skeletonmodification2dtwoboneik.md#class-skeletonmodification2dtwoboneik-method-get-joint-two-bone2d-node)() const |
| [int](class_int.md#class-int) | [get_joint_two_bone_idx](class_skeletonmodification2dtwoboneik.md#class-skeletonmodification2dtwoboneik-method-get-joint-two-bone-idx)() const |
| void | [set_joint_one_bone2d_node](class_skeletonmodification2dtwoboneik.md#class-skeletonmodification2dtwoboneik-method-set-joint-one-bone2d-node)(bone2d_node: [NodePath](class_nodepath.md#class-nodepath)) |
| void | [set_joint_one_bone_idx](class_skeletonmodification2dtwoboneik.md#class-skeletonmodification2dtwoboneik-method-set-joint-one-bone-idx)(bone_idx: [int](class_int.md#class-int)) |
| void | [set_joint_two_bone2d_node](class_skeletonmodification2dtwoboneik.md#class-skeletonmodification2dtwoboneik-method-set-joint-two-bone2d-node)(bone2d_node: [NodePath](class_nodepath.md#class-nodepath)) |
| void | [set_joint_two_bone_idx](class_skeletonmodification2dtwoboneik.md#class-skeletonmodification2dtwoboneik-method-set-joint-two-bone-idx)(bone_idx: [int](class_int.md#class-int)) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-skeletonmodification2dtwoboneik-property-flip-bend-direction"></a>

[bool](class_bool.md#class-bool) **flip_bend_direction** = `false` [🔗](class_skeletonmodification2dtwoboneik.md#class-skeletonmodification2dtwoboneik-property-flip-bend-direction)

- void **set_flip_bend_direction**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flip_bend_direction**()

If `true`, the bones in the modification will bend outward as opposed to inwards when contracting. If `false`, the bones will bend inwards when contracting.

---


<a id="class-skeletonmodification2dtwoboneik-property-target-maximum-distance"></a>

[float](class_float.md#class-float) **target_maximum_distance** = `0.0` [🔗](class_skeletonmodification2dtwoboneik.md#class-skeletonmodification2dtwoboneik-property-target-maximum-distance)

- void **set_target_maximum_distance**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_target_maximum_distance**()

The maximum distance the target can be at. If the target is farther than this distance, the modification will solve as if it's at this maximum distance. When set to `0`, the modification will solve without distance constraints.

---


<a id="class-skeletonmodification2dtwoboneik-property-target-minimum-distance"></a>

[float](class_float.md#class-float) **target_minimum_distance** = `0.0` [🔗](class_skeletonmodification2dtwoboneik.md#class-skeletonmodification2dtwoboneik-property-target-minimum-distance)

- void **set_target_minimum_distance**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_target_minimum_distance**()

The minimum distance the target can be at. If the target is closer than this distance, the modification will solve as if it's at this minimum distance. When set to `0`, the modification will solve without distance constraints.

---


<a id="class-skeletonmodification2dtwoboneik-property-target-nodepath"></a>

[NodePath](class_nodepath.md#class-nodepath) **target_nodepath** = `NodePath("")` [🔗](class_skeletonmodification2dtwoboneik.md#class-skeletonmodification2dtwoboneik-property-target-nodepath)

- void **set_target_node**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_target_node**()

The NodePath to the node that is the target for the TwoBoneIK modification. This node is what the modification will use when bending the [Bone2D](class_bone2d.md#class-bone2d) nodes.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-skeletonmodification2dtwoboneik-method-get-joint-one-bone2d-node"></a>

[NodePath](class_nodepath.md#class-nodepath) **get_joint_one_bone2d_node**() const [🔗](class_skeletonmodification2dtwoboneik.md#class-skeletonmodification2dtwoboneik-method-get-joint-one-bone2d-node)

Returns the [Bone2D](class_bone2d.md#class-bone2d) node that is being used as the first bone in the TwoBoneIK modification.

---


<a id="class-skeletonmodification2dtwoboneik-method-get-joint-one-bone-idx"></a>

[int](class_int.md#class-int) **get_joint_one_bone_idx**() const [🔗](class_skeletonmodification2dtwoboneik.md#class-skeletonmodification2dtwoboneik-method-get-joint-one-bone-idx)

Returns the index of the [Bone2D](class_bone2d.md#class-bone2d) node that is being used as the first bone in the TwoBoneIK modification.

---


<a id="class-skeletonmodification2dtwoboneik-method-get-joint-two-bone2d-node"></a>

[NodePath](class_nodepath.md#class-nodepath) **get_joint_two_bone2d_node**() const [🔗](class_skeletonmodification2dtwoboneik.md#class-skeletonmodification2dtwoboneik-method-get-joint-two-bone2d-node)

Returns the [Bone2D](class_bone2d.md#class-bone2d) node that is being used as the second bone in the TwoBoneIK modification.

---


<a id="class-skeletonmodification2dtwoboneik-method-get-joint-two-bone-idx"></a>

[int](class_int.md#class-int) **get_joint_two_bone_idx**() const [🔗](class_skeletonmodification2dtwoboneik.md#class-skeletonmodification2dtwoboneik-method-get-joint-two-bone-idx)

Returns the index of the [Bone2D](class_bone2d.md#class-bone2d) node that is being used as the second bone in the TwoBoneIK modification.

---


<a id="class-skeletonmodification2dtwoboneik-method-set-joint-one-bone2d-node"></a>

void **set_joint_one_bone2d_node**(bone2d_node: [NodePath](class_nodepath.md#class-nodepath)) [🔗](class_skeletonmodification2dtwoboneik.md#class-skeletonmodification2dtwoboneik-method-set-joint-one-bone2d-node)

Sets the [Bone2D](class_bone2d.md#class-bone2d) node that is being used as the first bone in the TwoBoneIK modification.

---


<a id="class-skeletonmodification2dtwoboneik-method-set-joint-one-bone-idx"></a>

void **set_joint_one_bone_idx**(bone_idx: [int](class_int.md#class-int)) [🔗](class_skeletonmodification2dtwoboneik.md#class-skeletonmodification2dtwoboneik-method-set-joint-one-bone-idx)

Sets the index of the [Bone2D](class_bone2d.md#class-bone2d) node that is being used as the first bone in the TwoBoneIK modification.

---


<a id="class-skeletonmodification2dtwoboneik-method-set-joint-two-bone2d-node"></a>

void **set_joint_two_bone2d_node**(bone2d_node: [NodePath](class_nodepath.md#class-nodepath)) [🔗](class_skeletonmodification2dtwoboneik.md#class-skeletonmodification2dtwoboneik-method-set-joint-two-bone2d-node)

Sets the [Bone2D](class_bone2d.md#class-bone2d) node that is being used as the second bone in the TwoBoneIK modification.

---


<a id="class-skeletonmodification2dtwoboneik-method-set-joint-two-bone-idx"></a>

void **set_joint_two_bone_idx**(bone_idx: [int](class_int.md#class-int)) [🔗](class_skeletonmodification2dtwoboneik.md#class-skeletonmodification2dtwoboneik-method-set-joint-two-bone-idx)

Sets the index of the [Bone2D](class_bone2d.md#class-bone2d) node that is being used as the second bone in the TwoBoneIK modification.
