> Source: https://docs.godotengine.org/en/4.7/classes/class_modifierbonetarget3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="modifierbonetarget3d"></a>

<a id="class-modifierbonetarget3d"></a>

# ModifierBoneTarget3D

**Inherits:** [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

А node that dynamically copies the 3D transform of a bone in its parent [Skeleton3D](class_skeleton3d.md#class-skeleton3d).

<a id="description"></a>

## Description

This node selects a bone in a [Skeleton3D](class_skeleton3d.md#class-skeleton3d) and attaches to it. This means that the **ModifierBoneTarget3D** node will dynamically copy the 3D transform of the selected bone.

The functionality is similar to [BoneAttachment3D](class_boneattachment3d.md#class-boneattachment3d), but this node adopts the [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) cycle and is intended to be used as another [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d)'s target.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [bone](class_modifierbonetarget3d.md#class-modifierbonetarget3d-property-bone) | `-1` |
| [String](class_string.md#class-string) | [bone_name](class_modifierbonetarget3d.md#class-modifierbonetarget3d-property-bone-name) | `""` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-modifierbonetarget3d-property-bone"></a>

[int](class_int.md#class-int) **bone** = `-1` [🔗](class_modifierbonetarget3d.md#class-modifierbonetarget3d-property-bone)

- void **set_bone**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_bone**()

The index of the attached bone.

---


<a id="class-modifierbonetarget3d-property-bone-name"></a>

[String](class_string.md#class-string) **bone_name** = `""` [🔗](class_modifierbonetarget3d.md#class-modifierbonetarget3d-property-bone-name)

- void **set_bone_name**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_bone_name**()

The name of the attached bone.
