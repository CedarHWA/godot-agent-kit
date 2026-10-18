> Source: https://docs.godotengine.org/en/4.7/classes/class_joint2d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="joint2d"></a>

<a id="class-joint2d"></a>

# Joint2D

**Inherits:** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [DampedSpringJoint2D](class_dampedspringjoint2d.md#class-dampedspringjoint2d), [GrooveJoint2D](class_groovejoint2d.md#class-groovejoint2d), [PinJoint2D](class_pinjoint2d.md#class-pinjoint2d)

Abstract base class for all 2D physics joints.

<a id="description"></a>

## Description

Abstract base class for all joints in 2D physics. 2D joints bind together two physics bodies ([node_a](class_joint2d.md#class-joint2d-property-node-a) and [node_b](class_joint2d.md#class-joint2d-property-node-b)) and apply a constraint.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [bias](class_joint2d.md#class-joint2d-property-bias) | `0.0` |
| [bool](class_bool.md#class-bool) | [disable_collision](class_joint2d.md#class-joint2d-property-disable-collision) | `true` |
| [NodePath](class_nodepath.md#class-nodepath) | [node_a](class_joint2d.md#class-joint2d-property-node-a) | `NodePath("")` |
| [NodePath](class_nodepath.md#class-nodepath) | [node_b](class_joint2d.md#class-joint2d-property-node-b) | `NodePath("")` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [RID](class_rid.md#class-rid) | [get_rid](class_joint2d.md#class-joint2d-method-get-rid)() const |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-joint2d-property-bias"></a>

[float](class_float.md#class-float) **bias** = `0.0` [🔗](class_joint2d.md#class-joint2d-property-bias)

- void **set_bias**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_bias**()

When [node_a](class_joint2d.md#class-joint2d-property-node-a) and [node_b](class_joint2d.md#class-joint2d-property-node-b) move in different directions the [bias](class_joint2d.md#class-joint2d-property-bias) controls how fast the joint pulls them back to their original position. The lower the [bias](class_joint2d.md#class-joint2d-property-bias) the more the two bodies can pull on the joint.

When set to `0`, the default value from [ProjectSettings.physics/2d/solver/default_constraint_bias](class_projectsettings.md#class-projectsettings-property-physics-2d-solver-default-constraint-bias) is used.

---


<a id="class-joint2d-property-disable-collision"></a>

[bool](class_bool.md#class-bool) **disable_collision** = `true` [🔗](class_joint2d.md#class-joint2d-property-disable-collision)

- void **set_exclude_nodes_from_collision**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_exclude_nodes_from_collision**()

If `true`, the two bodies bound together do not collide with each other.

---


<a id="class-joint2d-property-node-a"></a>

[NodePath](class_nodepath.md#class-nodepath) **node_a** = `NodePath("")` [🔗](class_joint2d.md#class-joint2d-property-node-a)

- void **set_node_a**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_node_a**()

Path to the first body (A) attached to the joint. The node must inherit [PhysicsBody2D](class_physicsbody2d.md#class-physicsbody2d).

---


<a id="class-joint2d-property-node-b"></a>

[NodePath](class_nodepath.md#class-nodepath) **node_b** = `NodePath("")` [🔗](class_joint2d.md#class-joint2d-property-node-b)

- void **set_node_b**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_node_b**()

Path to the second body (B) attached to the joint. The node must inherit [PhysicsBody2D](class_physicsbody2d.md#class-physicsbody2d).

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-joint2d-method-get-rid"></a>

[RID](class_rid.md#class-rid) **get_rid**() const [🔗](class_joint2d.md#class-joint2d-method-get-rid)

Returns the joint's internal [RID](class_rid.md#class-rid) from the [PhysicsServer2D](class_physicsserver2d.md#class-physicsserver2d).
