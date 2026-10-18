> Source: https://docs.godotengine.org/en/4.7/classes/class_skeletonmodification2dphysicalbones.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="skeletonmodification2dphysicalbones"></a>

<a id="class-skeletonmodification2dphysicalbones"></a>

# SkeletonModification2DPhysicalBones

**Experimental:** Physical bones may be changed in the future to perform the position update of [Bone2D](class_bone2d.md#class-bone2d) on their own, without needing this resource.

**Inherits:** [SkeletonModification2D](class_skeletonmodification2d.md#class-skeletonmodification2d) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A modification that applies the transforms of [PhysicalBone2D](class_physicalbone2d.md#class-physicalbone2d) nodes to [Bone2D](class_bone2d.md#class-bone2d) nodes.

<a id="description"></a>

## Description

This modification takes the transforms of [PhysicalBone2D](class_physicalbone2d.md#class-physicalbone2d) nodes and applies them to [Bone2D](class_bone2d.md#class-bone2d) nodes. This allows the [Bone2D](class_bone2d.md#class-bone2d) nodes to react to physics thanks to the linked [PhysicalBone2D](class_physicalbone2d.md#class-physicalbone2d) nodes.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [physical_bone_chain_length](class_skeletonmodification2dphysicalbones.md#class-skeletonmodification2dphysicalbones-property-physical-bone-chain-length) | `0` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [fetch_physical_bones](class_skeletonmodification2dphysicalbones.md#class-skeletonmodification2dphysicalbones-method-fetch-physical-bones)() |
| [NodePath](class_nodepath.md#class-nodepath) | [get_physical_bone_node](class_skeletonmodification2dphysicalbones.md#class-skeletonmodification2dphysicalbones-method-get-physical-bone-node)(joint_idx: [int](class_int.md#class-int)) const |
| void | [set_physical_bone_node](class_skeletonmodification2dphysicalbones.md#class-skeletonmodification2dphysicalbones-method-set-physical-bone-node)(joint_idx: [int](class_int.md#class-int), physicalbone2d_node: [NodePath](class_nodepath.md#class-nodepath)) |
| void | [start_simulation](class_skeletonmodification2dphysicalbones.md#class-skeletonmodification2dphysicalbones-method-start-simulation)(bones: [Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] = []) |
| void | [stop_simulation](class_skeletonmodification2dphysicalbones.md#class-skeletonmodification2dphysicalbones-method-stop-simulation)(bones: [Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] = []) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-skeletonmodification2dphysicalbones-property-physical-bone-chain-length"></a>

[int](class_int.md#class-int) **physical_bone_chain_length** = `0` [🔗](class_skeletonmodification2dphysicalbones.md#class-skeletonmodification2dphysicalbones-property-physical-bone-chain-length)

- void **set_physical_bone_chain_length**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_physical_bone_chain_length**()

The number of [PhysicalBone2D](class_physicalbone2d.md#class-physicalbone2d) nodes linked in this modification.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-skeletonmodification2dphysicalbones-method-fetch-physical-bones"></a>

void **fetch_physical_bones**() [🔗](class_skeletonmodification2dphysicalbones.md#class-skeletonmodification2dphysicalbones-method-fetch-physical-bones)

Empties the list of [PhysicalBone2D](class_physicalbone2d.md#class-physicalbone2d) nodes and populates it with all [PhysicalBone2D](class_physicalbone2d.md#class-physicalbone2d) nodes that are children of the [Skeleton2D](class_skeleton2d.md#class-skeleton2d).

---


<a id="class-skeletonmodification2dphysicalbones-method-get-physical-bone-node"></a>

[NodePath](class_nodepath.md#class-nodepath) **get_physical_bone_node**(joint_idx: [int](class_int.md#class-int)) const [🔗](class_skeletonmodification2dphysicalbones.md#class-skeletonmodification2dphysicalbones-method-get-physical-bone-node)

Returns the [PhysicalBone2D](class_physicalbone2d.md#class-physicalbone2d) node at `joint_idx`.

---


<a id="class-skeletonmodification2dphysicalbones-method-set-physical-bone-node"></a>

void **set_physical_bone_node**(joint_idx: [int](class_int.md#class-int), physicalbone2d_node: [NodePath](class_nodepath.md#class-nodepath)) [🔗](class_skeletonmodification2dphysicalbones.md#class-skeletonmodification2dphysicalbones-method-set-physical-bone-node)

Sets the [PhysicalBone2D](class_physicalbone2d.md#class-physicalbone2d) node at `joint_idx`.

**Note:** This is just the index used for this modification, not the bone index used in the [Skeleton2D](class_skeleton2d.md#class-skeleton2d).

---


<a id="class-skeletonmodification2dphysicalbones-method-start-simulation"></a>

void **start_simulation**(bones: [Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] = []) [🔗](class_skeletonmodification2dphysicalbones.md#class-skeletonmodification2dphysicalbones-method-start-simulation)

Tell the [PhysicalBone2D](class_physicalbone2d.md#class-physicalbone2d) nodes to start simulating and interacting with the physics world.

Optionally, an array of bone names can be passed to this function, and that will cause only [PhysicalBone2D](class_physicalbone2d.md#class-physicalbone2d) nodes with those names to start simulating.

---


<a id="class-skeletonmodification2dphysicalbones-method-stop-simulation"></a>

void **stop_simulation**(bones: [Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] = []) [🔗](class_skeletonmodification2dphysicalbones.md#class-skeletonmodification2dphysicalbones-method-stop-simulation)

Tell the [PhysicalBone2D](class_physicalbone2d.md#class-physicalbone2d) nodes to stop simulating and interacting with the physics world.

Optionally, an array of bone names can be passed to this function, and that will cause only [PhysicalBone2D](class_physicalbone2d.md#class-physicalbone2d) nodes with those names to stop simulating.
