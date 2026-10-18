> Source: https://docs.godotengine.org/en/4.7/classes/class_groovejoint2d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="groovejoint2d"></a>

<a id="class-groovejoint2d"></a>

# GrooveJoint2D

**Inherits:** [Joint2D](class_joint2d.md#class-joint2d) **<** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A physics joint that restricts the movement of two 2D physics bodies to a fixed axis.

<a id="description"></a>

## Description

A physics joint that restricts the movement of two 2D physics bodies to a fixed axis. For example, a [StaticBody2D](class_staticbody2d.md#class-staticbody2d) representing a piston base can be attached to a [RigidBody2D](class_rigidbody2d.md#class-rigidbody2d) representing the piston head, moving up and down.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [initial_offset](class_groovejoint2d.md#class-groovejoint2d-property-initial-offset) | `25.0` |
| [float](class_float.md#class-float) | [length](class_groovejoint2d.md#class-groovejoint2d-property-length) | `50.0` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-groovejoint2d-property-initial-offset"></a>

[float](class_float.md#class-float) **initial_offset** = `25.0` [🔗](class_groovejoint2d.md#class-groovejoint2d-property-initial-offset)

- void **set_initial_offset**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_initial_offset**()

The body B's initial anchor position defined by the joint's origin and a local offset [initial_offset](class_groovejoint2d.md#class-groovejoint2d-property-initial-offset) along the joint's Y axis (along the groove).

---


<a id="class-groovejoint2d-property-length"></a>

[float](class_float.md#class-float) **length** = `50.0` [🔗](class_groovejoint2d.md#class-groovejoint2d-property-length)

- void **set_length**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_length**()

The groove's length. The groove is from the joint's origin towards [length](class_groovejoint2d.md#class-groovejoint2d-property-length) along the joint's local Y axis.
