> Source: https://docs.godotengine.org/en/4.7/classes/class_path2d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="path2d"></a>

<a id="class-path2d"></a>

# Path2D

**Inherits:** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Contains a [Curve2D](class_curve2d.md#class-curve2d) path for [PathFollow2D](class_pathfollow2d.md#class-pathfollow2d) nodes to follow.

<a id="description"></a>

## Description

Can have [PathFollow2D](class_pathfollow2d.md#class-pathfollow2d) child nodes moving along the [Curve2D](class_curve2d.md#class-curve2d). See [PathFollow2D](class_pathfollow2d.md#class-pathfollow2d) for more information on usage.

**Note:** The path is considered as relative to the moved nodes (children of [PathFollow2D](class_pathfollow2d.md#class-pathfollow2d)). As such, the curve should usually start with a zero vector (`(0, 0)`).

<a id="properties"></a>

## Properties

|  |  |
| --- | --- |
| [Curve2D](class_curve2d.md#class-curve2d) | [curve](class_path2d.md#class-path2d-property-curve) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-path2d-property-curve"></a>

[Curve2D](class_curve2d.md#class-curve2d) **curve** [🔗](class_path2d.md#class-path2d-property-curve)

- void **set_curve**(value: [Curve2D](class_curve2d.md#class-curve2d))
- [Curve2D](class_curve2d.md#class-curve2d) **get_curve**()

A [Curve2D](class_curve2d.md#class-curve2d) describing the path.
