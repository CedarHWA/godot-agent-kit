> Source: https://docs.godotengine.org/en/4.7/classes/class_canvasmodulate.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="canvasmodulate"></a>

<a id="class-canvasmodulate"></a>

# CanvasModulate

**Inherits:** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A node that applies a color tint to a canvas.

<a id="description"></a>

## Description

**CanvasModulate** applies a color tint to all nodes on a canvas. Only one can be used to tint a canvas, but [CanvasLayer](class_canvaslayer.md#class-canvaslayer)s can be used to render things independently.

<a id="tutorials"></a>

## Tutorials

- [2D lights and shadows](../tutorials/2d/2d_lights_and_shadows.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Color](class_color.md#class-color) | [color](class_canvasmodulate.md#class-canvasmodulate-property-color) | `Color(1, 1, 1, 1)` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-canvasmodulate-property-color"></a>

[Color](class_color.md#class-color) **color** = `Color(1, 1, 1, 1)` [🔗](class_canvasmodulate.md#class-canvasmodulate-property-color)

- void **set_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_color**()

The tint color to apply.
