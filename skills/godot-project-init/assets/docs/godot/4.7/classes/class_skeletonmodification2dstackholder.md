> Source: https://docs.godotengine.org/en/4.7/classes/class_skeletonmodification2dstackholder.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="skeletonmodification2dstackholder"></a>

<a id="class-skeletonmodification2dstackholder"></a>

# SkeletonModification2DStackHolder

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [SkeletonModification2D](class_skeletonmodification2d.md#class-skeletonmodification2d) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A modification that holds and executes a [SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d).

<a id="description"></a>

## Description

This [SkeletonModification2D](class_skeletonmodification2d.md#class-skeletonmodification2d) holds a reference to a [SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d), allowing you to use multiple modification stacks on a single [Skeleton2D](class_skeleton2d.md#class-skeleton2d).

**Note:** The modifications in the held [SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d) will only be executed if their execution mode matches the execution mode of the SkeletonModification2DStackHolder.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d) | [get_held_modification_stack](class_skeletonmodification2dstackholder.md#class-skeletonmodification2dstackholder-method-get-held-modification-stack)() const |
| void | [set_held_modification_stack](class_skeletonmodification2dstackholder.md#class-skeletonmodification2dstackholder-method-set-held-modification-stack)(held_modification_stack: [SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d)) |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-skeletonmodification2dstackholder-method-get-held-modification-stack"></a>

[SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d) **get_held_modification_stack**() const [🔗](class_skeletonmodification2dstackholder.md#class-skeletonmodification2dstackholder-method-get-held-modification-stack)

Returns the [SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d) that this modification is holding.

---


<a id="class-skeletonmodification2dstackholder-method-set-held-modification-stack"></a>

void **set_held_modification_stack**(held_modification_stack: [SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d)) [🔗](class_skeletonmodification2dstackholder.md#class-skeletonmodification2dstackholder-method-set-held-modification-stack)

Sets the [SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d) that this modification is holding. This modification stack will then be executed when this modification is executed.
