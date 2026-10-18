> Source: https://docs.godotengine.org/en/4.7/classes/class_xranchor3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="xranchor3d"></a>

<a id="class-xranchor3d"></a>

# XRAnchor3D

**Inherits:** [XRNode3D](class_xrnode3d.md#class-xrnode3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

An anchor point in AR space.

<a id="description"></a>

## Description

The **XRAnchor3D** point is an [XRNode3D](class_xrnode3d.md#class-xrnode3d) that maps a real world location identified by the AR platform to a position within the game world. For example, as long as plane detection in ARKit is on, ARKit will identify and update the position of planes (tables, floors, etc.) and create anchors for them.

This node is mapped to one of the anchors through its unique ID. When you receive a signal that a new anchor is available, you should add this node to your scene for that anchor. You can predefine nodes and set the ID; the nodes will simply remain on `(0, 0, 0)` until a plane is recognized.

Keep in mind that, as long as plane detection is enabled, the size, placing and orientation of an anchor will be updated as the detection logic learns more about the real world out there especially if only part of the surface is in view.

<a id="tutorials"></a>

## Tutorials

- [XR documentation index](../tutorials/xr/index.md)

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Plane](class_plane.md#class-plane) | [get_plane](class_xranchor3d.md#class-xranchor3d-method-get-plane)() const |
| [Vector3](class_vector3.md#class-vector3) | [get_size](class_xranchor3d.md#class-xranchor3d-method-get-size)() const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-xranchor3d-method-get-plane"></a>

[Plane](class_plane.md#class-plane) **get_plane**() const [🔗](class_xranchor3d.md#class-xranchor3d-method-get-plane)

Returns a plane aligned with our anchor; handy for intersection testing.

---


<a id="class-xranchor3d-method-get-size"></a>

[Vector3](class_vector3.md#class-vector3) **get_size**() const [🔗](class_xranchor3d.md#class-xranchor3d-method-get-size)

Returns the estimated size of the plane that was detected. Say when the anchor relates to a table in the real world, this is the estimated size of the surface of that table.
