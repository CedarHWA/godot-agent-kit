> Source: https://docs.godotengine.org/en/4.7/classes/class_skeletonmodification2dlookat.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="skeletonmodification2dlookat"></a>

<a id="class-skeletonmodification2dlookat"></a>

# SkeletonModification2DLookAt

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [SkeletonModification2D](class_skeletonmodification2d.md#class-skeletonmodification2d) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A modification that rotates a [Bone2D](class_bone2d.md#class-bone2d) node to look at a target.

<a id="description"></a>

## Description

This [SkeletonModification2D](class_skeletonmodification2d.md#class-skeletonmodification2d) rotates a bone to look a target. This is extremely helpful for moving character's head to look at the player, rotating a turret to look at a target, or any other case where you want to make a bone rotate towards something quickly and easily.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [NodePath](class_nodepath.md#class-nodepath) | [bone2d_node](class_skeletonmodification2dlookat.md#class-skeletonmodification2dlookat-property-bone2d-node) | `NodePath("")` |
| [int](class_int.md#class-int) | [bone_index](class_skeletonmodification2dlookat.md#class-skeletonmodification2dlookat-property-bone-index) | `-1` |
| [NodePath](class_nodepath.md#class-nodepath) | [target_nodepath](class_skeletonmodification2dlookat.md#class-skeletonmodification2dlookat-property-target-nodepath) | `NodePath("")` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [float](class_float.md#class-float) | [get_additional_rotation](class_skeletonmodification2dlookat.md#class-skeletonmodification2dlookat-method-get-additional-rotation)() const |
| [bool](class_bool.md#class-bool) | [get_constraint_angle_invert](class_skeletonmodification2dlookat.md#class-skeletonmodification2dlookat-method-get-constraint-angle-invert)() const |
| [float](class_float.md#class-float) | [get_constraint_angle_max](class_skeletonmodification2dlookat.md#class-skeletonmodification2dlookat-method-get-constraint-angle-max)() const |
| [float](class_float.md#class-float) | [get_constraint_angle_min](class_skeletonmodification2dlookat.md#class-skeletonmodification2dlookat-method-get-constraint-angle-min)() const |
| [bool](class_bool.md#class-bool) | [get_enable_constraint](class_skeletonmodification2dlookat.md#class-skeletonmodification2dlookat-method-get-enable-constraint)() const |
| void | [set_additional_rotation](class_skeletonmodification2dlookat.md#class-skeletonmodification2dlookat-method-set-additional-rotation)(rotation: [float](class_float.md#class-float)) |
| void | [set_constraint_angle_invert](class_skeletonmodification2dlookat.md#class-skeletonmodification2dlookat-method-set-constraint-angle-invert)(invert: [bool](class_bool.md#class-bool)) |
| void | [set_constraint_angle_max](class_skeletonmodification2dlookat.md#class-skeletonmodification2dlookat-method-set-constraint-angle-max)(angle_max: [float](class_float.md#class-float)) |
| void | [set_constraint_angle_min](class_skeletonmodification2dlookat.md#class-skeletonmodification2dlookat-method-set-constraint-angle-min)(angle_min: [float](class_float.md#class-float)) |
| void | [set_enable_constraint](class_skeletonmodification2dlookat.md#class-skeletonmodification2dlookat-method-set-enable-constraint)(enable_constraint: [bool](class_bool.md#class-bool)) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-skeletonmodification2dlookat-property-bone2d-node"></a>

[NodePath](class_nodepath.md#class-nodepath) **bone2d_node** = `NodePath("")` [🔗](class_skeletonmodification2dlookat.md#class-skeletonmodification2dlookat-property-bone2d-node)

- void **set_bone2d_node**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_bone2d_node**()

The [Bone2D](class_bone2d.md#class-bone2d) node that the modification will operate on.

---


<a id="class-skeletonmodification2dlookat-property-bone-index"></a>

[int](class_int.md#class-int) **bone_index** = `-1` [🔗](class_skeletonmodification2dlookat.md#class-skeletonmodification2dlookat-property-bone-index)

- void **set_bone_index**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_bone_index**()

The index of the [Bone2D](class_bone2d.md#class-bone2d) node that the modification will operate on.

---


<a id="class-skeletonmodification2dlookat-property-target-nodepath"></a>

[NodePath](class_nodepath.md#class-nodepath) **target_nodepath** = `NodePath("")` [🔗](class_skeletonmodification2dlookat.md#class-skeletonmodification2dlookat-property-target-nodepath)

- void **set_target_node**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_target_node**()

The NodePath to the node that is the target for the LookAt modification. This node is what the modification will rotate the [Bone2D](class_bone2d.md#class-bone2d) to.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-skeletonmodification2dlookat-method-get-additional-rotation"></a>

[float](class_float.md#class-float) **get_additional_rotation**() const [🔗](class_skeletonmodification2dlookat.md#class-skeletonmodification2dlookat-method-get-additional-rotation)

Returns the amount of additional rotation that is applied after the LookAt modification executes.

---


<a id="class-skeletonmodification2dlookat-method-get-constraint-angle-invert"></a>

[bool](class_bool.md#class-bool) **get_constraint_angle_invert**() const [🔗](class_skeletonmodification2dlookat.md#class-skeletonmodification2dlookat-method-get-constraint-angle-invert)

Returns whether the constraints to this modification are inverted or not.

---


<a id="class-skeletonmodification2dlookat-method-get-constraint-angle-max"></a>

[float](class_float.md#class-float) **get_constraint_angle_max**() const [🔗](class_skeletonmodification2dlookat.md#class-skeletonmodification2dlookat-method-get-constraint-angle-max)

Returns the constraint's maximum allowed angle.

---


<a id="class-skeletonmodification2dlookat-method-get-constraint-angle-min"></a>

[float](class_float.md#class-float) **get_constraint_angle_min**() const [🔗](class_skeletonmodification2dlookat.md#class-skeletonmodification2dlookat-method-get-constraint-angle-min)

Returns the constraint's minimum allowed angle.

---


<a id="class-skeletonmodification2dlookat-method-get-enable-constraint"></a>

[bool](class_bool.md#class-bool) **get_enable_constraint**() const [🔗](class_skeletonmodification2dlookat.md#class-skeletonmodification2dlookat-method-get-enable-constraint)

Returns `true` if the LookAt modification is using constraints.

---


<a id="class-skeletonmodification2dlookat-method-set-additional-rotation"></a>

void **set_additional_rotation**(rotation: [float](class_float.md#class-float)) [🔗](class_skeletonmodification2dlookat.md#class-skeletonmodification2dlookat-method-set-additional-rotation)

Sets the amount of additional rotation that is to be applied after executing the modification. This allows for offsetting the results by the inputted rotation amount.

---


<a id="class-skeletonmodification2dlookat-method-set-constraint-angle-invert"></a>

void **set_constraint_angle_invert**(invert: [bool](class_bool.md#class-bool)) [🔗](class_skeletonmodification2dlookat.md#class-skeletonmodification2dlookat-method-set-constraint-angle-invert)

When `true`, the modification will use an inverted joint constraint.

An inverted joint constraint only constraints the [Bone2D](class_bone2d.md#class-bone2d) to the angles *outside of* the inputted minimum and maximum angles. For this reason, it is referred to as an inverted joint constraint, as it constraints the joint to the outside of the inputted values.

---


<a id="class-skeletonmodification2dlookat-method-set-constraint-angle-max"></a>

void **set_constraint_angle_max**(angle_max: [float](class_float.md#class-float)) [🔗](class_skeletonmodification2dlookat.md#class-skeletonmodification2dlookat-method-set-constraint-angle-max)

Sets the constraint's maximum allowed angle.

---


<a id="class-skeletonmodification2dlookat-method-set-constraint-angle-min"></a>

void **set_constraint_angle_min**(angle_min: [float](class_float.md#class-float)) [🔗](class_skeletonmodification2dlookat.md#class-skeletonmodification2dlookat-method-set-constraint-angle-min)

Sets the constraint's minimum allowed angle.

---


<a id="class-skeletonmodification2dlookat-method-set-enable-constraint"></a>

void **set_enable_constraint**(enable_constraint: [bool](class_bool.md#class-bool)) [🔗](class_skeletonmodification2dlookat.md#class-skeletonmodification2dlookat-method-set-enable-constraint)

Sets whether this modification will use constraints or not. When `true`, constraints will be applied when solving the LookAt modification.
