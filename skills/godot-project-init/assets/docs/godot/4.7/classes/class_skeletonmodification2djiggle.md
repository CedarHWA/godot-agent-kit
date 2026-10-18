> Source: https://docs.godotengine.org/en/4.7/classes/class_skeletonmodification2djiggle.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="skeletonmodification2djiggle"></a>

<a id="class-skeletonmodification2djiggle"></a>

# SkeletonModification2DJiggle

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [SkeletonModification2D](class_skeletonmodification2d.md#class-skeletonmodification2d) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A modification that jiggles [Bone2D](class_bone2d.md#class-bone2d) nodes as they move towards a target.

<a id="description"></a>

## Description

This modification moves a series of bones, typically called a bone chain, towards a target. What makes this modification special is that it calculates the velocity and acceleration for each bone in the bone chain, and runs a very light physics-like calculation using the inputted values. This allows the bones to overshoot the target and "jiggle" around. It can be configured to act more like a spring, or sway around like cloth might.

This modification is useful for adding additional motion to things like hair, the edges of clothing, and more. It has several settings to that allow control over how the joint moves when the target moves.

**Note:** The Jiggle modifier has `jiggle_joints`, which are the data objects that hold the data for each joint in the Jiggle chain. This is different from than [Bone2D](class_bone2d.md#class-bone2d) nodes! Jiggle joints hold the data needed for each [Bone2D](class_bone2d.md#class-bone2d) in the bone chain used by the Jiggle modification.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [damping](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-property-damping) | `0.75` |
| [Vector2](class_vector2.md#class-vector2) | [gravity](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-property-gravity) | `Vector2(0, 6)` |
| [int](class_int.md#class-int) | [jiggle_data_chain_length](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-property-jiggle-data-chain-length) | `0` |
| [float](class_float.md#class-float) | [mass](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-property-mass) | `0.75` |
| [float](class_float.md#class-float) | [stiffness](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-property-stiffness) | `3.0` |
| [NodePath](class_nodepath.md#class-nodepath) | [target_nodepath](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-property-target-nodepath) | `NodePath("")` |
| [bool](class_bool.md#class-bool) | [use_gravity](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-property-use-gravity) | `false` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [int](class_int.md#class-int) | [get_collision_mask](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-method-get-collision-mask)() const |
| [NodePath](class_nodepath.md#class-nodepath) | [get_jiggle_joint_bone2d_node](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-method-get-jiggle-joint-bone2d-node)(joint_idx: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_jiggle_joint_bone_index](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-method-get-jiggle-joint-bone-index)(joint_idx: [int](class_int.md#class-int)) const |
| [float](class_float.md#class-float) | [get_jiggle_joint_damping](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-method-get-jiggle-joint-damping)(joint_idx: [int](class_int.md#class-int)) const |
| [Vector2](class_vector2.md#class-vector2) | [get_jiggle_joint_gravity](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-method-get-jiggle-joint-gravity)(joint_idx: [int](class_int.md#class-int)) const |
| [float](class_float.md#class-float) | [get_jiggle_joint_mass](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-method-get-jiggle-joint-mass)(joint_idx: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [get_jiggle_joint_override](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-method-get-jiggle-joint-override)(joint_idx: [int](class_int.md#class-int)) const |
| [float](class_float.md#class-float) | [get_jiggle_joint_stiffness](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-method-get-jiggle-joint-stiffness)(joint_idx: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [get_jiggle_joint_use_gravity](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-method-get-jiggle-joint-use-gravity)(joint_idx: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [get_use_colliders](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-method-get-use-colliders)() const |
| void | [reset](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-method-reset)() |
| void | [set_collision_mask](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-method-set-collision-mask)(collision_mask: [int](class_int.md#class-int)) |
| void | [set_jiggle_joint_bone2d_node](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-method-set-jiggle-joint-bone2d-node)(joint_idx: [int](class_int.md#class-int), bone2d_node: [NodePath](class_nodepath.md#class-nodepath)) |
| void | [set_jiggle_joint_bone_index](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-method-set-jiggle-joint-bone-index)(joint_idx: [int](class_int.md#class-int), bone_idx: [int](class_int.md#class-int)) |
| void | [set_jiggle_joint_damping](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-method-set-jiggle-joint-damping)(joint_idx: [int](class_int.md#class-int), damping: [float](class_float.md#class-float)) |
| void | [set_jiggle_joint_gravity](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-method-set-jiggle-joint-gravity)(joint_idx: [int](class_int.md#class-int), gravity: [Vector2](class_vector2.md#class-vector2)) |
| void | [set_jiggle_joint_mass](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-method-set-jiggle-joint-mass)(joint_idx: [int](class_int.md#class-int), mass: [float](class_float.md#class-float)) |
| void | [set_jiggle_joint_override](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-method-set-jiggle-joint-override)(joint_idx: [int](class_int.md#class-int), override: [bool](class_bool.md#class-bool)) |
| void | [set_jiggle_joint_stiffness](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-method-set-jiggle-joint-stiffness)(joint_idx: [int](class_int.md#class-int), stiffness: [float](class_float.md#class-float)) |
| void | [set_jiggle_joint_use_gravity](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-method-set-jiggle-joint-use-gravity)(joint_idx: [int](class_int.md#class-int), use_gravity: [bool](class_bool.md#class-bool)) |
| void | [set_use_colliders](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-method-set-use-colliders)(use_colliders: [bool](class_bool.md#class-bool)) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-skeletonmodification2djiggle-property-damping"></a>

[float](class_float.md#class-float) **damping** = `0.75` [🔗](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-property-damping)

- void **set_damping**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_damping**()

The default amount of damping applied to the Jiggle joints, if they are not overridden. Higher values lead to more of the calculated velocity being applied.

---


<a id="class-skeletonmodification2djiggle-property-gravity"></a>

[Vector2](class_vector2.md#class-vector2) **gravity** = `Vector2(0, 6)` [🔗](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-property-gravity)

- void **set_gravity**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_gravity**()

The default amount of gravity applied to the Jiggle joints, if they are not overridden.

---


<a id="class-skeletonmodification2djiggle-property-jiggle-data-chain-length"></a>

[int](class_int.md#class-int) **jiggle_data_chain_length** = `0` [🔗](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-property-jiggle-data-chain-length)

- void **set_jiggle_data_chain_length**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_jiggle_data_chain_length**()

The amount of Jiggle joints in the Jiggle modification.

---


<a id="class-skeletonmodification2djiggle-property-mass"></a>

[float](class_float.md#class-float) **mass** = `0.75` [🔗](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-property-mass)

- void **set_mass**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_mass**()

The default amount of mass assigned to the Jiggle joints, if they are not overridden. Higher values lead to faster movements and more overshooting.

---


<a id="class-skeletonmodification2djiggle-property-stiffness"></a>

[float](class_float.md#class-float) **stiffness** = `3.0` [🔗](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-property-stiffness)

- void **set_stiffness**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_stiffness**()

The default amount of stiffness assigned to the Jiggle joints, if they are not overridden. Higher values act more like springs, quickly moving into the correct position.

---


<a id="class-skeletonmodification2djiggle-property-target-nodepath"></a>

[NodePath](class_nodepath.md#class-nodepath) **target_nodepath** = `NodePath("")` [🔗](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-property-target-nodepath)

- void **set_target_node**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_target_node**()

The NodePath to the node that is the target for the Jiggle modification. This node is what the Jiggle chain will attempt to rotate the bone chain to.

---


<a id="class-skeletonmodification2djiggle-property-use-gravity"></a>

[bool](class_bool.md#class-bool) **use_gravity** = `false` [🔗](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-property-use-gravity)

- void **set_use_gravity**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_use_gravity**()

Whether the gravity vector, [gravity](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-property-gravity), should be applied to the Jiggle joints, assuming they are not overriding the default settings.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-skeletonmodification2djiggle-method-get-collision-mask"></a>

[int](class_int.md#class-int) **get_collision_mask**() const [🔗](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-method-get-collision-mask)

Returns the collision mask used by the Jiggle modifier when collisions are enabled.

---


<a id="class-skeletonmodification2djiggle-method-get-jiggle-joint-bone2d-node"></a>

[NodePath](class_nodepath.md#class-nodepath) **get_jiggle_joint_bone2d_node**(joint_idx: [int](class_int.md#class-int)) const [🔗](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-method-get-jiggle-joint-bone2d-node)

Returns the [Bone2D](class_bone2d.md#class-bone2d) node assigned to the Jiggle joint at `joint_idx`.

---


<a id="class-skeletonmodification2djiggle-method-get-jiggle-joint-bone-index"></a>

[int](class_int.md#class-int) **get_jiggle_joint_bone_index**(joint_idx: [int](class_int.md#class-int)) const [🔗](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-method-get-jiggle-joint-bone-index)

Returns the index of the [Bone2D](class_bone2d.md#class-bone2d) node assigned to the Jiggle joint at `joint_idx`.

---


<a id="class-skeletonmodification2djiggle-method-get-jiggle-joint-damping"></a>

[float](class_float.md#class-float) **get_jiggle_joint_damping**(joint_idx: [int](class_int.md#class-int)) const [🔗](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-method-get-jiggle-joint-damping)

Returns the amount of damping of the Jiggle joint at `joint_idx`.

---


<a id="class-skeletonmodification2djiggle-method-get-jiggle-joint-gravity"></a>

[Vector2](class_vector2.md#class-vector2) **get_jiggle_joint_gravity**(joint_idx: [int](class_int.md#class-int)) const [🔗](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-method-get-jiggle-joint-gravity)

Returns a [Vector2](class_vector2.md#class-vector2) representing the amount of gravity the Jiggle joint at `joint_idx` is influenced by.

---


<a id="class-skeletonmodification2djiggle-method-get-jiggle-joint-mass"></a>

[float](class_float.md#class-float) **get_jiggle_joint_mass**(joint_idx: [int](class_int.md#class-int)) const [🔗](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-method-get-jiggle-joint-mass)

Returns the amount of mass of the jiggle joint at `joint_idx`.

---


<a id="class-skeletonmodification2djiggle-method-get-jiggle-joint-override"></a>

[bool](class_bool.md#class-bool) **get_jiggle_joint_override**(joint_idx: [int](class_int.md#class-int)) const [🔗](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-method-get-jiggle-joint-override)

Returns a boolean that indicates whether the joint at `joint_idx` is overriding the default Jiggle joint data defined in the modification.

---


<a id="class-skeletonmodification2djiggle-method-get-jiggle-joint-stiffness"></a>

[float](class_float.md#class-float) **get_jiggle_joint_stiffness**(joint_idx: [int](class_int.md#class-int)) const [🔗](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-method-get-jiggle-joint-stiffness)

Returns the stiffness of the Jiggle joint at `joint_idx`.

---


<a id="class-skeletonmodification2djiggle-method-get-jiggle-joint-use-gravity"></a>

[bool](class_bool.md#class-bool) **get_jiggle_joint_use_gravity**(joint_idx: [int](class_int.md#class-int)) const [🔗](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-method-get-jiggle-joint-use-gravity)

Returns a boolean that indicates whether the joint at `joint_idx` is using gravity or not.

---


<a id="class-skeletonmodification2djiggle-method-get-use-colliders"></a>

[bool](class_bool.md#class-bool) **get_use_colliders**() const [🔗](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-method-get-use-colliders)

Returns whether the jiggle modifier is taking physics colliders into account when solving.

---


<a id="class-skeletonmodification2djiggle-method-reset"></a>

void **reset**() [🔗](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-method-reset)

Resets the internal jiggle simulation state to the current bone positions, clearing velocity, acceleration, and accumulated forces.

---


<a id="class-skeletonmodification2djiggle-method-set-collision-mask"></a>

void **set_collision_mask**(collision_mask: [int](class_int.md#class-int)) [🔗](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-method-set-collision-mask)

Sets the collision mask that the Jiggle modifier will use when reacting to colliders, if the Jiggle modifier is set to take colliders into account.

---


<a id="class-skeletonmodification2djiggle-method-set-jiggle-joint-bone2d-node"></a>

void **set_jiggle_joint_bone2d_node**(joint_idx: [int](class_int.md#class-int), bone2d_node: [NodePath](class_nodepath.md#class-nodepath)) [🔗](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-method-set-jiggle-joint-bone2d-node)

Sets the [Bone2D](class_bone2d.md#class-bone2d) node assigned to the Jiggle joint at `joint_idx`.

---


<a id="class-skeletonmodification2djiggle-method-set-jiggle-joint-bone-index"></a>

void **set_jiggle_joint_bone_index**(joint_idx: [int](class_int.md#class-int), bone_idx: [int](class_int.md#class-int)) [🔗](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-method-set-jiggle-joint-bone-index)

Sets the bone index, `bone_idx`, of the Jiggle joint at `joint_idx`. When possible, this will also update the `bone2d_node` of the Jiggle joint based on data provided by the linked skeleton.

---


<a id="class-skeletonmodification2djiggle-method-set-jiggle-joint-damping"></a>

void **set_jiggle_joint_damping**(joint_idx: [int](class_int.md#class-int), damping: [float](class_float.md#class-float)) [🔗](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-method-set-jiggle-joint-damping)

Sets the amount of damping of the Jiggle joint at `joint_idx`.

---


<a id="class-skeletonmodification2djiggle-method-set-jiggle-joint-gravity"></a>

void **set_jiggle_joint_gravity**(joint_idx: [int](class_int.md#class-int), gravity: [Vector2](class_vector2.md#class-vector2)) [🔗](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-method-set-jiggle-joint-gravity)

Sets the gravity vector of the Jiggle joint at `joint_idx`.

---


<a id="class-skeletonmodification2djiggle-method-set-jiggle-joint-mass"></a>

void **set_jiggle_joint_mass**(joint_idx: [int](class_int.md#class-int), mass: [float](class_float.md#class-float)) [🔗](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-method-set-jiggle-joint-mass)

Sets the of mass of the Jiggle joint at `joint_idx`.

---


<a id="class-skeletonmodification2djiggle-method-set-jiggle-joint-override"></a>

void **set_jiggle_joint_override**(joint_idx: [int](class_int.md#class-int), override: [bool](class_bool.md#class-bool)) [🔗](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-method-set-jiggle-joint-override)

Sets whether the Jiggle joint at `joint_idx` should override the default Jiggle joint settings. Setting this to `true` will make the joint use its own settings rather than the default ones attached to the modification.

---


<a id="class-skeletonmodification2djiggle-method-set-jiggle-joint-stiffness"></a>

void **set_jiggle_joint_stiffness**(joint_idx: [int](class_int.md#class-int), stiffness: [float](class_float.md#class-float)) [🔗](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-method-set-jiggle-joint-stiffness)

Sets the of stiffness of the Jiggle joint at `joint_idx`.

---


<a id="class-skeletonmodification2djiggle-method-set-jiggle-joint-use-gravity"></a>

void **set_jiggle_joint_use_gravity**(joint_idx: [int](class_int.md#class-int), use_gravity: [bool](class_bool.md#class-bool)) [🔗](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-method-set-jiggle-joint-use-gravity)

Sets whether the Jiggle joint at `joint_idx` should use gravity.

---


<a id="class-skeletonmodification2djiggle-method-set-use-colliders"></a>

void **set_use_colliders**(use_colliders: [bool](class_bool.md#class-bool)) [🔗](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle-method-set-use-colliders)

If `true`, the Jiggle modifier will take colliders into account, keeping them from entering into these collision objects.
