> Source: https://docs.godotengine.org/en/4.7/classes/class_pointlight2d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="pointlight2d"></a>

<a id="class-pointlight2d"></a>

# PointLight2D

**Inherits:** [Light2D](class_light2d.md#class-light2d) **<** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Positional 2D light source.

<a id="description"></a>

## Description

Casts light in a 2D environment. This light's shape is defined by a (usually grayscale) texture.

<a id="tutorials"></a>

## Tutorials

- [2D lights and shadows](../tutorials/2d/2d_lights_and_shadows.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [height](class_pointlight2d.md#class-pointlight2d-property-height) | `0.0` |
| [Vector2](class_vector2.md#class-vector2) | [offset](class_pointlight2d.md#class-pointlight2d-property-offset) | `Vector2(0, 0)` |
| [Texture2D](class_texture2d.md#class-texture2d) | [texture](class_pointlight2d.md#class-pointlight2d-property-texture) |  |
| [float](class_float.md#class-float) | [texture_scale](class_pointlight2d.md#class-pointlight2d-property-texture-scale) | `1.0` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-pointlight2d-property-height"></a>

[float](class_float.md#class-float) **height** = `0.0` [🔗](class_pointlight2d.md#class-pointlight2d-property-height)

- void **set_height**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_height**()

The height of the light. Used with 2D normal mapping. The units are in pixels, e.g. if the height is 100, then it will illuminate an object 100 pixels away at a 45° angle to the plane.

---


<a id="class-pointlight2d-property-offset"></a>

[Vector2](class_vector2.md#class-vector2) **offset** = `Vector2(0, 0)` [🔗](class_pointlight2d.md#class-pointlight2d-property-offset)

- void **set_texture_offset**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_texture_offset**()

The offset of the light's [texture](class_pointlight2d.md#class-pointlight2d-property-texture).

---


<a id="class-pointlight2d-property-texture"></a>

[Texture2D](class_texture2d.md#class-texture2d) **texture** [🔗](class_pointlight2d.md#class-pointlight2d-property-texture)

- void **set_texture**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_texture**()

[Texture2D](class_texture2d.md#class-texture2d) used for the light's appearance.

---


<a id="class-pointlight2d-property-texture-scale"></a>

[float](class_float.md#class-float) **texture_scale** = `1.0` [🔗](class_pointlight2d.md#class-pointlight2d-property-texture-scale)

- void **set_texture_scale**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_texture_scale**()

The [texture](class_pointlight2d.md#class-pointlight2d-property-texture)'s scale factor.
