> Source: https://docs.godotengine.org/en/4.7/classes/class_physicalbonesimulator3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="physicalbonesimulator3d"></a>

<a id="class-physicalbonesimulator3d"></a>

# PhysicalBoneSimulator3D

**Inherits:** [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Node that can be the parent of [PhysicalBone3D](class_physicalbone3d.md#class-physicalbone3d) and can apply the simulation results to [Skeleton3D](class_skeleton3d.md#class-skeleton3d).

<a id="description"></a>

## Description

Node that can be the parent of [PhysicalBone3D](class_physicalbone3d.md#class-physicalbone3d) and can apply the simulation results to [Skeleton3D](class_skeleton3d.md#class-skeleton3d).

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [is_simulating_physics](class_physicalbonesimulator3d.md#class-physicalbonesimulator3d-method-is-simulating-physics)() const |
| void | [physical_bones_add_collision_exception](class_physicalbonesimulator3d.md#class-physicalbonesimulator3d-method-physical-bones-add-collision-exception)(exception: [RID](class_rid.md#class-rid)) |
| void | [physical_bones_remove_collision_exception](class_physicalbonesimulator3d.md#class-physicalbonesimulator3d-method-physical-bones-remove-collision-exception)(exception: [RID](class_rid.md#class-rid)) |
| void | [physical_bones_start_simulation](class_physicalbonesimulator3d.md#class-physicalbonesimulator3d-method-physical-bones-start-simulation)(bones: [Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] = []) |
| void | [physical_bones_stop_simulation](class_physicalbonesimulator3d.md#class-physicalbonesimulator3d-method-physical-bones-stop-simulation)() |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-physicalbonesimulator3d-method-is-simulating-physics"></a>

[bool](class_bool.md#class-bool) **is_simulating_physics**() const [🔗](class_physicalbonesimulator3d.md#class-physicalbonesimulator3d-method-is-simulating-physics)

Returns a boolean that indicates whether the **PhysicalBoneSimulator3D** is running and simulating.

---


<a id="class-physicalbonesimulator3d-method-physical-bones-add-collision-exception"></a>

void **physical_bones_add_collision_exception**(exception: [RID](class_rid.md#class-rid)) [🔗](class_physicalbonesimulator3d.md#class-physicalbonesimulator3d-method-physical-bones-add-collision-exception)

Adds a collision exception to the physical bone.

Works just like the [RigidBody3D](class_rigidbody3d.md#class-rigidbody3d) node.

---


<a id="class-physicalbonesimulator3d-method-physical-bones-remove-collision-exception"></a>

void **physical_bones_remove_collision_exception**(exception: [RID](class_rid.md#class-rid)) [🔗](class_physicalbonesimulator3d.md#class-physicalbonesimulator3d-method-physical-bones-remove-collision-exception)

Removes a collision exception to the physical bone.

Works just like the [RigidBody3D](class_rigidbody3d.md#class-rigidbody3d) node.

---


<a id="class-physicalbonesimulator3d-method-physical-bones-start-simulation"></a>

void **physical_bones_start_simulation**(bones: [Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] = []) [🔗](class_physicalbonesimulator3d.md#class-physicalbonesimulator3d-method-physical-bones-start-simulation)

Tells the [PhysicalBone3D](class_physicalbone3d.md#class-physicalbone3d) nodes in the Skeleton to start simulating and reacting to the physics world.

Optionally, a list of bone names can be passed-in, allowing only the passed-in bones to be simulated.

---


<a id="class-physicalbonesimulator3d-method-physical-bones-stop-simulation"></a>

void **physical_bones_stop_simulation**() [🔗](class_physicalbonesimulator3d.md#class-physicalbonesimulator3d-method-physical-bones-stop-simulation)

Tells the [PhysicalBone3D](class_physicalbone3d.md#class-physicalbone3d) nodes in the Skeleton to stop simulating.
