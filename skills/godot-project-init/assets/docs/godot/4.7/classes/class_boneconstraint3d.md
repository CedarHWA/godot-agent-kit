> Source: https://docs.godotengine.org/en/4.7/classes/class_boneconstraint3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="boneconstraint3d"></a>

<a id="class-boneconstraint3d"></a>

# BoneConstraint3D

**Inherits:** [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [AimModifier3D](class_aimmodifier3d.md#class-aimmodifier3d), [ConvertTransformModifier3D](class_converttransformmodifier3d.md#class-converttransformmodifier3d), [CopyTransformModifier3D](class_copytransformmodifier3d.md#class-copytransformmodifier3d)

A node that may modify Skeleton3D's bone with associating the two bones.

<a id="description"></a>

## Description

Base class of [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) that modifies the bone set in [set_apply_bone()](class_boneconstraint3d.md#class-boneconstraint3d-method-set-apply-bone) based on the transform of the bone retrieved by [get_reference_bone()](class_boneconstraint3d.md#class-boneconstraint3d-method-get-reference-bone).

**Note:** Most methods in this class take an `index` parameter. This parameter specifies which setting list entry to return if the IK has multiple entries (e.g. `settings/<index>/amount`).

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [clear_setting](class_boneconstraint3d.md#class-boneconstraint3d-method-clear-setting)() |
| [float](class_float.md#class-float) | [get_amount](class_boneconstraint3d.md#class-boneconstraint3d-method-get-amount)(index: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_apply_bone](class_boneconstraint3d.md#class-boneconstraint3d-method-get-apply-bone)(index: [int](class_int.md#class-int)) const |
| [String](class_string.md#class-string) | [get_apply_bone_name](class_boneconstraint3d.md#class-boneconstraint3d-method-get-apply-bone-name)(index: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_reference_bone](class_boneconstraint3d.md#class-boneconstraint3d-method-get-reference-bone)(index: [int](class_int.md#class-int)) const |
| [String](class_string.md#class-string) | [get_reference_bone_name](class_boneconstraint3d.md#class-boneconstraint3d-method-get-reference-bone-name)(index: [int](class_int.md#class-int)) const |
| [NodePath](class_nodepath.md#class-nodepath) | [get_reference_node](class_boneconstraint3d.md#class-boneconstraint3d-method-get-reference-node)(index: [int](class_int.md#class-int)) const |
| [ReferenceType](class_boneconstraint3d.md#enum-boneconstraint3d-referencetype) | [get_reference_type](class_boneconstraint3d.md#class-boneconstraint3d-method-get-reference-type)(index: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_setting_count](class_boneconstraint3d.md#class-boneconstraint3d-method-get-setting-count)() const |
| void | [set_amount](class_boneconstraint3d.md#class-boneconstraint3d-method-set-amount)(index: [int](class_int.md#class-int), amount: [float](class_float.md#class-float)) |
| void | [set_apply_bone](class_boneconstraint3d.md#class-boneconstraint3d-method-set-apply-bone)(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int)) |
| void | [set_apply_bone_name](class_boneconstraint3d.md#class-boneconstraint3d-method-set-apply-bone-name)(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string)) |
| void | [set_reference_bone](class_boneconstraint3d.md#class-boneconstraint3d-method-set-reference-bone)(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int)) |
| void | [set_reference_bone_name](class_boneconstraint3d.md#class-boneconstraint3d-method-set-reference-bone-name)(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string)) |
| void | [set_reference_node](class_boneconstraint3d.md#class-boneconstraint3d-method-set-reference-node)(index: [int](class_int.md#class-int), node: [NodePath](class_nodepath.md#class-nodepath)) |
| void | [set_reference_type](class_boneconstraint3d.md#class-boneconstraint3d-method-set-reference-type)(index: [int](class_int.md#class-int), type: [ReferenceType](class_boneconstraint3d.md#enum-boneconstraint3d-referencetype)) |
| void | [set_setting_count](class_boneconstraint3d.md#class-boneconstraint3d-method-set-setting-count)(count: [int](class_int.md#class-int)) |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-boneconstraint3d-referencetype"></a>

enum **ReferenceType**: [🔗](class_boneconstraint3d.md#enum-boneconstraint3d-referencetype)

<a id="class-boneconstraint3d-constant-reference-type-bone"></a>

[ReferenceType](class_boneconstraint3d.md#enum-boneconstraint3d-referencetype) **REFERENCE_TYPE_BONE** = `0`

The reference target is a bone. In this case, the reference target spaces is local space.

<a id="class-boneconstraint3d-constant-reference-type-node"></a>

[ReferenceType](class_boneconstraint3d.md#enum-boneconstraint3d-referencetype) **REFERENCE_TYPE_NODE** = `1`

The reference target is a [Node3D](class_node3d.md#class-node3d). In this case, the reference target spaces is model space.

In other words, the reference target's coordinates are treated as if it were placed directly under [Skeleton3D](class_skeleton3d.md#class-skeleton3d) which parent of the **BoneConstraint3D**.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-boneconstraint3d-method-clear-setting"></a>

void **clear_setting**() [🔗](class_boneconstraint3d.md#class-boneconstraint3d-method-clear-setting)

Clear all settings.

---


<a id="class-boneconstraint3d-method-get-amount"></a>

[float](class_float.md#class-float) **get_amount**(index: [int](class_int.md#class-int)) const [🔗](class_boneconstraint3d.md#class-boneconstraint3d-method-get-amount)

Returns the apply amount of the setting at `index`.

---


<a id="class-boneconstraint3d-method-get-apply-bone"></a>

[int](class_int.md#class-int) **get_apply_bone**(index: [int](class_int.md#class-int)) const [🔗](class_boneconstraint3d.md#class-boneconstraint3d-method-get-apply-bone)

Returns the apply bone of the setting at `index`. This bone will be modified.

---


<a id="class-boneconstraint3d-method-get-apply-bone-name"></a>

[String](class_string.md#class-string) **get_apply_bone_name**(index: [int](class_int.md#class-int)) const [🔗](class_boneconstraint3d.md#class-boneconstraint3d-method-get-apply-bone-name)

Returns the apply bone name of the setting at `index`. This bone will be modified.

---


<a id="class-boneconstraint3d-method-get-reference-bone"></a>

[int](class_int.md#class-int) **get_reference_bone**(index: [int](class_int.md#class-int)) const [🔗](class_boneconstraint3d.md#class-boneconstraint3d-method-get-reference-bone)

Returns the reference bone of the setting at `index`.

This bone will be only referenced and not modified by this modifier.

---


<a id="class-boneconstraint3d-method-get-reference-bone-name"></a>

[String](class_string.md#class-string) **get_reference_bone_name**(index: [int](class_int.md#class-int)) const [🔗](class_boneconstraint3d.md#class-boneconstraint3d-method-get-reference-bone-name)

Returns the reference bone name of the setting at `index`.

This bone will be only referenced and not modified by this modifier.

---


<a id="class-boneconstraint3d-method-get-reference-node"></a>

[NodePath](class_nodepath.md#class-nodepath) **get_reference_node**(index: [int](class_int.md#class-int)) const [🔗](class_boneconstraint3d.md#class-boneconstraint3d-method-get-reference-node)

Returns the reference node path of the setting at `index`.

This node will be only referenced and not modified by this modifier.

---


<a id="class-boneconstraint3d-method-get-reference-type"></a>

[ReferenceType](class_boneconstraint3d.md#enum-boneconstraint3d-referencetype) **get_reference_type**(index: [int](class_int.md#class-int)) const [🔗](class_boneconstraint3d.md#class-boneconstraint3d-method-get-reference-type)

Returns the reference target type of the setting at `index`. See also [ReferenceType](class_boneconstraint3d.md#enum-boneconstraint3d-referencetype).

---


<a id="class-boneconstraint3d-method-get-setting-count"></a>

[int](class_int.md#class-int) **get_setting_count**() const [🔗](class_boneconstraint3d.md#class-boneconstraint3d-method-get-setting-count)

Returns the number of settings in the modifier.

---


<a id="class-boneconstraint3d-method-set-amount"></a>

void **set_amount**(index: [int](class_int.md#class-int), amount: [float](class_float.md#class-float)) [🔗](class_boneconstraint3d.md#class-boneconstraint3d-method-set-amount)

Sets the apply amount of the setting at `index` to `amount`.

---


<a id="class-boneconstraint3d-method-set-apply-bone"></a>

void **set_apply_bone**(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int)) [🔗](class_boneconstraint3d.md#class-boneconstraint3d-method-set-apply-bone)

Sets the apply bone of the setting at `index` to `bone`. This bone will be modified.

---


<a id="class-boneconstraint3d-method-set-apply-bone-name"></a>

void **set_apply_bone_name**(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string)) [🔗](class_boneconstraint3d.md#class-boneconstraint3d-method-set-apply-bone-name)

Sets the apply bone of the setting at `index` to `bone_name`. This bone will be modified.

---


<a id="class-boneconstraint3d-method-set-reference-bone"></a>

void **set_reference_bone**(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int)) [🔗](class_boneconstraint3d.md#class-boneconstraint3d-method-set-reference-bone)

Sets the reference bone of the setting at `index` to `bone`.

This bone will be only referenced and not modified by this modifier.

---


<a id="class-boneconstraint3d-method-set-reference-bone-name"></a>

void **set_reference_bone_name**(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string)) [🔗](class_boneconstraint3d.md#class-boneconstraint3d-method-set-reference-bone-name)

Sets the reference bone of the setting at `index` to `bone_name`.

This bone will be only referenced and not modified by this modifier.

---


<a id="class-boneconstraint3d-method-set-reference-node"></a>

void **set_reference_node**(index: [int](class_int.md#class-int), node: [NodePath](class_nodepath.md#class-nodepath)) [🔗](class_boneconstraint3d.md#class-boneconstraint3d-method-set-reference-node)

Sets the reference node path of the setting at `index` to `node`.

This node will be only referenced and not modified by this modifier.

---


<a id="class-boneconstraint3d-method-set-reference-type"></a>

void **set_reference_type**(index: [int](class_int.md#class-int), type: [ReferenceType](class_boneconstraint3d.md#enum-boneconstraint3d-referencetype)) [🔗](class_boneconstraint3d.md#class-boneconstraint3d-method-set-reference-type)

Sets the reference target type of the setting at `index` to `type`. See also [ReferenceType](class_boneconstraint3d.md#enum-boneconstraint3d-referencetype).

---


<a id="class-boneconstraint3d-method-set-setting-count"></a>

void **set_setting_count**(count: [int](class_int.md#class-int)) [🔗](class_boneconstraint3d.md#class-boneconstraint3d-method-set-setting-count)

Sets the number of settings in the modifier.
