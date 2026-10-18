> Source: https://docs.godotengine.org/en/4.7/classes/class_ikmodifier3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="ikmodifier3d"></a>

<a id="class-ikmodifier3d"></a>

# IKModifier3D

**Inherits:** [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [ChainIK3D](class_chainik3d.md#class-chainik3d), [TwoBoneIK3D](class_twoboneik3d.md#class-twoboneik3d)

A node for inverse kinematics which may modify more than one bone.

<a id="description"></a>

## Description

Base class of [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d)s that has some joint lists and applies inverse kinematics. This class has some structs, enums, and helper methods which are useful to solve inverse kinematics.

<a id="tutorials"></a>

## Tutorials

- [Inverse Kinematics Returns to Godot 4.6 - IKModifier3D](https://godotengine.org/article/inverse-kinematics-returns-to-godot-4-6/#ikmodifier3d-and-7-child-classes)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [mutable_bone_axes](class_ikmodifier3d.md#class-ikmodifier3d-property-mutable-bone-axes) | `true` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [clear_settings](class_ikmodifier3d.md#class-ikmodifier3d-method-clear-settings)() |
| [int](class_int.md#class-int) | [get_setting_count](class_ikmodifier3d.md#class-ikmodifier3d-method-get-setting-count)() const |
| void | [reset](class_ikmodifier3d.md#class-ikmodifier3d-method-reset)() |
| void | [set_setting_count](class_ikmodifier3d.md#class-ikmodifier3d-method-set-setting-count)(count: [int](class_int.md#class-int)) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-ikmodifier3d-property-mutable-bone-axes"></a>

[bool](class_bool.md#class-bool) **mutable_bone_axes** = `true` [🔗](class_ikmodifier3d.md#class-ikmodifier3d-property-mutable-bone-axes)

- void **set_mutable_bone_axes**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **are_bone_axes_mutable**()

If `true`, the solver retrieves the bone axis from the bone pose every frame.

If `false`, the solver retrieves the bone axis from the bone rest and caches it, which increases performance slightly, but position changes in the bone pose made before processing this **IKModifier3D** are ignored.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-ikmodifier3d-method-clear-settings"></a>

void **clear_settings**() [🔗](class_ikmodifier3d.md#class-ikmodifier3d-method-clear-settings)

Clears all settings.

---


<a id="class-ikmodifier3d-method-get-setting-count"></a>

[int](class_int.md#class-int) **get_setting_count**() const [🔗](class_ikmodifier3d.md#class-ikmodifier3d-method-get-setting-count)

Returns the number of settings.

---


<a id="class-ikmodifier3d-method-reset"></a>

void **reset**() [🔗](class_ikmodifier3d.md#class-ikmodifier3d-method-reset)

Resets a state with respect to the current bone pose.

---


<a id="class-ikmodifier3d-method-set-setting-count"></a>

void **set_setting_count**(count: [int](class_int.md#class-int)) [🔗](class_ikmodifier3d.md#class-ikmodifier3d-method-set-setting-count)

Sets the number of settings.
