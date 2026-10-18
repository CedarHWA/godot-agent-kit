> Source: https://docs.godotengine.org/en/4.7/classes/class_skeletonmodificationstack2d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="skeletonmodificationstack2d"></a>

<a id="class-skeletonmodificationstack2d"></a>

# SkeletonModificationStack2D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A resource that holds a stack of [SkeletonModification2D](class_skeletonmodification2d.md#class-skeletonmodification2d)s.

<a id="description"></a>

## Description

This resource is used by the Skeleton and holds a stack of [SkeletonModification2D](class_skeletonmodification2d.md#class-skeletonmodification2d)s.

This controls the order of the modifications and how they are applied. Modification order is especially important for full-body IK setups, as you need to execute the modifications in the correct order to get the desired results. For example, you want to execute a modification on the spine *before* the arms on a humanoid skeleton.

This resource also controls how strongly all of the modifications are applied to the [Skeleton2D](class_skeleton2d.md#class-skeleton2d).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [enabled](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d-property-enabled) | `false` |
| [int](class_int.md#class-int) | [modification_count](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d-property-modification-count) | `0` |
| [float](class_float.md#class-float) | [strength](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d-property-strength) | `1.0` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_modification](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d-method-add-modification)(modification: [SkeletonModification2D](class_skeletonmodification2d.md#class-skeletonmodification2d)) |
| void | [delete_modification](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d-method-delete-modification)(mod_idx: [int](class_int.md#class-int)) |
| void | [enable_all_modifications](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d-method-enable-all-modifications)(enabled: [bool](class_bool.md#class-bool)) |
| void | [execute](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d-method-execute)(delta: [float](class_float.md#class-float), execution_mode: [int](class_int.md#class-int)) |
| [bool](class_bool.md#class-bool) | [get_is_setup](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d-method-get-is-setup)() const |
| [SkeletonModification2D](class_skeletonmodification2d.md#class-skeletonmodification2d) | [get_modification](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d-method-get-modification)(mod_idx: [int](class_int.md#class-int)) const |
| [Skeleton2D](class_skeleton2d.md#class-skeleton2d) | [get_skeleton](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d-method-get-skeleton)() const |
| void | [set_modification](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d-method-set-modification)(mod_idx: [int](class_int.md#class-int), modification: [SkeletonModification2D](class_skeletonmodification2d.md#class-skeletonmodification2d)) |
| void | [setup](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d-method-setup)() |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-skeletonmodificationstack2d-property-enabled"></a>

[bool](class_bool.md#class-bool) **enabled** = `false` [🔗](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d-property-enabled)

- void **set_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_enabled**()

If `true`, the modification's in the stack will be called. This is handled automatically through the [Skeleton2D](class_skeleton2d.md#class-skeleton2d) node.

---


<a id="class-skeletonmodificationstack2d-property-modification-count"></a>

[int](class_int.md#class-int) **modification_count** = `0` [🔗](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d-property-modification-count)

- void **set_modification_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_modification_count**()

The number of modifications in the stack.

---


<a id="class-skeletonmodificationstack2d-property-strength"></a>

[float](class_float.md#class-float) **strength** = `1.0` [🔗](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d-property-strength)

- void **set_strength**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_strength**()

The interpolation strength of the modifications in stack. A value of `0` will make it where the modifications are not applied, a strength of `0.5` will be half applied, and a strength of `1` will allow the modifications to be fully applied and override the [Skeleton2D](class_skeleton2d.md#class-skeleton2d) [Bone2D](class_bone2d.md#class-bone2d) poses.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-skeletonmodificationstack2d-method-add-modification"></a>

void **add_modification**(modification: [SkeletonModification2D](class_skeletonmodification2d.md#class-skeletonmodification2d)) [🔗](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d-method-add-modification)

Adds the passed-in [SkeletonModification2D](class_skeletonmodification2d.md#class-skeletonmodification2d) to the stack.

---


<a id="class-skeletonmodificationstack2d-method-delete-modification"></a>

void **delete_modification**(mod_idx: [int](class_int.md#class-int)) [🔗](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d-method-delete-modification)

Deletes the [SkeletonModification2D](class_skeletonmodification2d.md#class-skeletonmodification2d) at the index position `mod_idx`, if it exists.

---


<a id="class-skeletonmodificationstack2d-method-enable-all-modifications"></a>

void **enable_all_modifications**(enabled: [bool](class_bool.md#class-bool)) [🔗](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d-method-enable-all-modifications)

Enables all [SkeletonModification2D](class_skeletonmodification2d.md#class-skeletonmodification2d)s in the stack.

---


<a id="class-skeletonmodificationstack2d-method-execute"></a>

void **execute**(delta: [float](class_float.md#class-float), execution_mode: [int](class_int.md#class-int)) [🔗](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d-method-execute)

Executes all of the [SkeletonModification2D](class_skeletonmodification2d.md#class-skeletonmodification2d)s in the stack that use the same execution mode as the passed-in `execution_mode`, starting from index `0` to [modification_count](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d-property-modification-count).

**Note:** The order of the modifications can matter depending on the modifications. For example, modifications on a spine should operate before modifications on the arms in order to get proper results.

---


<a id="class-skeletonmodificationstack2d-method-get-is-setup"></a>

[bool](class_bool.md#class-bool) **get_is_setup**() const [🔗](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d-method-get-is-setup)

Returns a boolean that indicates whether the modification stack is setup and can execute.

---


<a id="class-skeletonmodificationstack2d-method-get-modification"></a>

[SkeletonModification2D](class_skeletonmodification2d.md#class-skeletonmodification2d) **get_modification**(mod_idx: [int](class_int.md#class-int)) const [🔗](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d-method-get-modification)

Returns the [SkeletonModification2D](class_skeletonmodification2d.md#class-skeletonmodification2d) at the passed-in index, `mod_idx`.

---


<a id="class-skeletonmodificationstack2d-method-get-skeleton"></a>

[Skeleton2D](class_skeleton2d.md#class-skeleton2d) **get_skeleton**() const [🔗](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d-method-get-skeleton)

Returns the [Skeleton2D](class_skeleton2d.md#class-skeleton2d) node that the SkeletonModificationStack2D is bound to.

---


<a id="class-skeletonmodificationstack2d-method-set-modification"></a>

void **set_modification**(mod_idx: [int](class_int.md#class-int), modification: [SkeletonModification2D](class_skeletonmodification2d.md#class-skeletonmodification2d)) [🔗](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d-method-set-modification)

Sets the modification at `mod_idx` to the passed-in modification, `modification`.

---


<a id="class-skeletonmodificationstack2d-method-setup"></a>

void **setup**() [🔗](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d-method-setup)

Sets up the modification stack so it can execute. This function should be called by [Skeleton2D](class_skeleton2d.md#class-skeleton2d) and shouldn't be manually called unless you know what you are doing.
