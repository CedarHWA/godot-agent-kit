> Source: https://docs.godotengine.org/en/4.7/classes/class_marker2d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="marker2d"></a>

<a id="class-marker2d"></a>

# Marker2D

**Inherits:** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Generic 2D position hint for editing.

<a id="description"></a>

## Description

Generic 2D position hint for editing. It's just like a plain [Node2D](class_node2d.md#class-node2d), but it displays as a cross in the 2D editor at all times. You can set the cross' visual size by using the gizmo in the 2D editor while the node is selected.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [gizmo_extents](class_marker2d.md#class-marker2d-property-gizmo-extents) | `10.0` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-marker2d-property-gizmo-extents"></a>

[float](class_float.md#class-float) **gizmo_extents** = `10.0` [🔗](class_marker2d.md#class-marker2d-property-gizmo-extents)

- void **set_gizmo_extents**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_gizmo_extents**()

Size of the gizmo cross that appears in the editor.
