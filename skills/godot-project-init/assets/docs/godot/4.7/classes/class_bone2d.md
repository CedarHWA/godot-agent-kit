> Source: https://docs.godotengine.org/en/4.7/classes/class_bone2d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="bone2d"></a>

<a id="class-bone2d"></a>

# Bone2D

**Inherits:** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A joint used with [Skeleton2D](class_skeleton2d.md#class-skeleton2d) to control and animate other nodes.

<a id="description"></a>

## Description

A hierarchy of **Bone2D**s can be bound to a [Skeleton2D](class_skeleton2d.md#class-skeleton2d) to control and animate other [Node2D](class_node2d.md#class-node2d) nodes.

You can use **Bone2D** and [Skeleton2D](class_skeleton2d.md#class-skeleton2d) nodes to animate 2D meshes created with the [Polygon2D](class_polygon2d.md#class-polygon2d) UV editor.

Each bone has a [rest](class_bone2d.md#class-bone2d-property-rest) transform that you can reset to with [apply_rest()](class_bone2d.md#class-bone2d-method-apply-rest). These rest poses are relative to the bone's parent.

If in the editor, you can set the rest pose of an entire skeleton using a menu option, from the code, you need to iterate over the bones to set their individual rest poses.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Transform2D](class_transform2d.md#class-transform2d) | [rest](class_bone2d.md#class-bone2d-property-rest) | `Transform2D(0, 0, 0, 0, 0, 0)` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [apply_rest](class_bone2d.md#class-bone2d-method-apply-rest)() |
| [bool](class_bool.md#class-bool) | [get_autocalculate_length_and_angle](class_bone2d.md#class-bone2d-method-get-autocalculate-length-and-angle)() const |
| [float](class_float.md#class-float) | [get_bone_angle](class_bone2d.md#class-bone2d-method-get-bone-angle)() const |
| [int](class_int.md#class-int) | [get_index_in_skeleton](class_bone2d.md#class-bone2d-method-get-index-in-skeleton)() const |
| [float](class_float.md#class-float) | [get_length](class_bone2d.md#class-bone2d-method-get-length)() const |
| [Transform2D](class_transform2d.md#class-transform2d) | [get_skeleton_rest](class_bone2d.md#class-bone2d-method-get-skeleton-rest)() const |
| void | [set_autocalculate_length_and_angle](class_bone2d.md#class-bone2d-method-set-autocalculate-length-and-angle)(auto_calculate: [bool](class_bool.md#class-bool)) |
| void | [set_bone_angle](class_bone2d.md#class-bone2d-method-set-bone-angle)(angle: [float](class_float.md#class-float)) |
| void | [set_length](class_bone2d.md#class-bone2d-method-set-length)(length: [float](class_float.md#class-float)) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-bone2d-property-rest"></a>

[Transform2D](class_transform2d.md#class-transform2d) **rest** = `Transform2D(0, 0, 0, 0, 0, 0)` [🔗](class_bone2d.md#class-bone2d-property-rest)

- void **set_rest**(value: [Transform2D](class_transform2d.md#class-transform2d))
- [Transform2D](class_transform2d.md#class-transform2d) **get_rest**()

Rest transform of the bone. You can reset the node's transforms to this value using [apply_rest()](class_bone2d.md#class-bone2d-method-apply-rest).

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-bone2d-method-apply-rest"></a>

void **apply_rest**() [🔗](class_bone2d.md#class-bone2d-method-apply-rest)

Resets the bone to the rest pose. This is equivalent to setting [Node2D.transform](class_node2d.md#class-node2d-property-transform) to [rest](class_bone2d.md#class-bone2d-property-rest).

---


<a id="class-bone2d-method-get-autocalculate-length-and-angle"></a>

[bool](class_bool.md#class-bool) **get_autocalculate_length_and_angle**() const [🔗](class_bone2d.md#class-bone2d-method-get-autocalculate-length-and-angle)

Returns whether this **Bone2D** is going to autocalculate its length and bone angle using its first **Bone2D** child node, if one exists. If there are no **Bone2D** children, then it cannot autocalculate these values and will print a warning.

---


<a id="class-bone2d-method-get-bone-angle"></a>

[float](class_float.md#class-float) **get_bone_angle**() const [🔗](class_bone2d.md#class-bone2d-method-get-bone-angle)

Returns the angle of the bone in the **Bone2D**.

**Note:** This is different from the **Bone2D**'s rotation. The bone's angle is the rotation of the bone shown by the gizmo, which is unaffected by the **Bone2D**'s [Node2D.transform](class_node2d.md#class-node2d-property-transform).

---


<a id="class-bone2d-method-get-index-in-skeleton"></a>

[int](class_int.md#class-int) **get_index_in_skeleton**() const [🔗](class_bone2d.md#class-bone2d-method-get-index-in-skeleton)

Returns the node's index as part of the entire skeleton. See [Skeleton2D](class_skeleton2d.md#class-skeleton2d).

---


<a id="class-bone2d-method-get-length"></a>

[float](class_float.md#class-float) **get_length**() const [🔗](class_bone2d.md#class-bone2d-method-get-length)

Returns the length of the bone in the **Bone2D** node.

---


<a id="class-bone2d-method-get-skeleton-rest"></a>

[Transform2D](class_transform2d.md#class-transform2d) **get_skeleton_rest**() const [🔗](class_bone2d.md#class-bone2d-method-get-skeleton-rest)

Returns the node's [rest](class_bone2d.md#class-bone2d-property-rest) [Transform2D](class_transform2d.md#class-transform2d) if it doesn't have a parent, or its rest pose relative to its parent.

---


<a id="class-bone2d-method-set-autocalculate-length-and-angle"></a>

void **set_autocalculate_length_and_angle**(auto_calculate: [bool](class_bool.md#class-bool)) [🔗](class_bone2d.md#class-bone2d-method-set-autocalculate-length-and-angle)

When set to `true`, the **Bone2D** node will attempt to automatically calculate the bone angle and length using the first child **Bone2D** node, if one exists. If none exist, the **Bone2D** cannot automatically calculate these values and will print a warning.

---


<a id="class-bone2d-method-set-bone-angle"></a>

void **set_bone_angle**(angle: [float](class_float.md#class-float)) [🔗](class_bone2d.md#class-bone2d-method-set-bone-angle)

Sets the bone angle for the **Bone2D**. This is typically set to the rotation from the **Bone2D** to a child **Bone2D** node.

**Note:** This is different from the **Bone2D**'s rotation. The bone's angle is the rotation of the bone shown by the gizmo, which is unaffected by the **Bone2D**'s [Node2D.transform](class_node2d.md#class-node2d-property-transform).

---


<a id="class-bone2d-method-set-length"></a>

void **set_length**(length: [float](class_float.md#class-float)) [🔗](class_bone2d.md#class-bone2d-method-set-length)

Sets the length of the bone in the **Bone2D**.
