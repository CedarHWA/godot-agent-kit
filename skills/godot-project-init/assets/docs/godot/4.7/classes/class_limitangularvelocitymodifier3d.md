> Source: https://docs.godotengine.org/en/4.7/classes/class_limitangularvelocitymodifier3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="limitangularvelocitymodifier3d"></a>

<a id="class-limitangularvelocitymodifier3d"></a>

# LimitAngularVelocityModifier3D

**Inherits:** [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Limit bone rotation angular velocity.

<a id="description"></a>

## Description

This modifier limits bone rotation angular velocity by comparing poses between previous and current frame.

You can add bone chains by specifying their root and end bones, then add the bones between them to a list. Modifier processes either that list or the bones excluding those in the list depending on the option [exclude](class_limitangularvelocitymodifier3d.md#class-limitangularvelocitymodifier3d-property-exclude).

**Note:** Most methods in this class take an `index` parameter. This parameter specifies which setting list entry to return if the IK has multiple entries (e.g. `settings/<index>/root_bone_name`).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [chain_count](class_limitangularvelocitymodifier3d.md#class-limitangularvelocitymodifier3d-property-chain-count) | `0` |
| [bool](class_bool.md#class-bool) | [exclude](class_limitangularvelocitymodifier3d.md#class-limitangularvelocitymodifier3d-property-exclude) | `false` |
| [int](class_int.md#class-int) | [joint_count](class_limitangularvelocitymodifier3d.md#class-limitangularvelocitymodifier3d-property-joint-count) | `0` |
| [float](class_float.md#class-float) | [max_angular_velocity](class_limitangularvelocitymodifier3d.md#class-limitangularvelocitymodifier3d-property-max-angular-velocity) | `6.2831855` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [clear_chains](class_limitangularvelocitymodifier3d.md#class-limitangularvelocitymodifier3d-method-clear-chains)() |
| [int](class_int.md#class-int) | [get_end_bone](class_limitangularvelocitymodifier3d.md#class-limitangularvelocitymodifier3d-method-get-end-bone)(index: [int](class_int.md#class-int)) const |
| [String](class_string.md#class-string) | [get_end_bone_name](class_limitangularvelocitymodifier3d.md#class-limitangularvelocitymodifier3d-method-get-end-bone-name)(index: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_root_bone](class_limitangularvelocitymodifier3d.md#class-limitangularvelocitymodifier3d-method-get-root-bone)(index: [int](class_int.md#class-int)) const |
| [String](class_string.md#class-string) | [get_root_bone_name](class_limitangularvelocitymodifier3d.md#class-limitangularvelocitymodifier3d-method-get-root-bone-name)(index: [int](class_int.md#class-int)) const |
| void | [reset](class_limitangularvelocitymodifier3d.md#class-limitangularvelocitymodifier3d-method-reset)() |
| void | [set_end_bone](class_limitangularvelocitymodifier3d.md#class-limitangularvelocitymodifier3d-method-set-end-bone)(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int)) |
| void | [set_end_bone_name](class_limitangularvelocitymodifier3d.md#class-limitangularvelocitymodifier3d-method-set-end-bone-name)(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string)) |
| void | [set_root_bone](class_limitangularvelocitymodifier3d.md#class-limitangularvelocitymodifier3d-method-set-root-bone)(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int)) |
| void | [set_root_bone_name](class_limitangularvelocitymodifier3d.md#class-limitangularvelocitymodifier3d-method-set-root-bone-name)(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string)) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-limitangularvelocitymodifier3d-property-chain-count"></a>

[int](class_int.md#class-int) **chain_count** = `0` [🔗](class_limitangularvelocitymodifier3d.md#class-limitangularvelocitymodifier3d-property-chain-count)

- void **set_chain_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_chain_count**()

The number of chains.

---


<a id="class-limitangularvelocitymodifier3d-property-exclude"></a>

[bool](class_bool.md#class-bool) **exclude** = `false` [🔗](class_limitangularvelocitymodifier3d.md#class-limitangularvelocitymodifier3d-property-exclude)

- void **set_exclude**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_exclude**()

If `true`, the modifier processes bones not included in the bone list.

If `false`, the bones processed by the modifier are equal to the bone list.

---


<a id="class-limitangularvelocitymodifier3d-property-joint-count"></a>

[int](class_int.md#class-int) **joint_count** = `0` [🔗](class_limitangularvelocitymodifier3d.md#class-limitangularvelocitymodifier3d-property-joint-count)

The number of joints in the list which created by chains dynamically.

---


<a id="class-limitangularvelocitymodifier3d-property-max-angular-velocity"></a>

[float](class_float.md#class-float) **max_angular_velocity** = `6.2831855` [🔗](class_limitangularvelocitymodifier3d.md#class-limitangularvelocitymodifier3d-property-max-angular-velocity)

- void **set_max_angular_velocity**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_max_angular_velocity**()

The maximum angular velocity per second.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-limitangularvelocitymodifier3d-method-clear-chains"></a>

void **clear_chains**() [🔗](class_limitangularvelocitymodifier3d.md#class-limitangularvelocitymodifier3d-method-clear-chains)

Clear all chains.

---


<a id="class-limitangularvelocitymodifier3d-method-get-end-bone"></a>

[int](class_int.md#class-int) **get_end_bone**(index: [int](class_int.md#class-int)) const [🔗](class_limitangularvelocitymodifier3d.md#class-limitangularvelocitymodifier3d-method-get-end-bone)

Returns the end bone index of the bone chain.

---


<a id="class-limitangularvelocitymodifier3d-method-get-end-bone-name"></a>

[String](class_string.md#class-string) **get_end_bone_name**(index: [int](class_int.md#class-int)) const [🔗](class_limitangularvelocitymodifier3d.md#class-limitangularvelocitymodifier3d-method-get-end-bone-name)

Returns the end bone name of the bone chain.

---


<a id="class-limitangularvelocitymodifier3d-method-get-root-bone"></a>

[int](class_int.md#class-int) **get_root_bone**(index: [int](class_int.md#class-int)) const [🔗](class_limitangularvelocitymodifier3d.md#class-limitangularvelocitymodifier3d-method-get-root-bone)

Returns the root bone index of the bone chain.

---


<a id="class-limitangularvelocitymodifier3d-method-get-root-bone-name"></a>

[String](class_string.md#class-string) **get_root_bone_name**(index: [int](class_int.md#class-int)) const [🔗](class_limitangularvelocitymodifier3d.md#class-limitangularvelocitymodifier3d-method-get-root-bone-name)

Returns the root bone name of the bone chain.

---


<a id="class-limitangularvelocitymodifier3d-method-reset"></a>

void **reset**() [🔗](class_limitangularvelocitymodifier3d.md#class-limitangularvelocitymodifier3d-method-reset)

Sets the reference pose for angle comparison to the current pose with the influence of constraints removed. This function is automatically triggered when joints change or upon activation.

---


<a id="class-limitangularvelocitymodifier3d-method-set-end-bone"></a>

void **set_end_bone**(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int)) [🔗](class_limitangularvelocitymodifier3d.md#class-limitangularvelocitymodifier3d-method-set-end-bone)

Sets the end bone index of the bone chain.

---


<a id="class-limitangularvelocitymodifier3d-method-set-end-bone-name"></a>

void **set_end_bone_name**(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string)) [🔗](class_limitangularvelocitymodifier3d.md#class-limitangularvelocitymodifier3d-method-set-end-bone-name)

Sets the end bone name of the bone chain.

**Note:** End bone must be the root bone or a child of the root bone.

---


<a id="class-limitangularvelocitymodifier3d-method-set-root-bone"></a>

void **set_root_bone**(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int)) [🔗](class_limitangularvelocitymodifier3d.md#class-limitangularvelocitymodifier3d-method-set-root-bone)

Sets the root bone index of the bone chain.

---


<a id="class-limitangularvelocitymodifier3d-method-set-root-bone-name"></a>

void **set_root_bone_name**(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string)) [🔗](class_limitangularvelocitymodifier3d.md#class-limitangularvelocitymodifier3d-method-set-root-bone-name)

Sets the root bone name of the bone chain.
