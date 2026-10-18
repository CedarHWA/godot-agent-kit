> Source: https://docs.godotengine.org/en/4.7/classes/class_lightoccluder2d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="lightoccluder2d"></a>

<a id="class-lightoccluder2d"></a>

# LightOccluder2D

**Inherits:** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Occludes light cast by a Light2D, casting shadows.

<a id="description"></a>

## Description

Occludes light cast by a Light2D, casting shadows. The LightOccluder2D must be provided with an [OccluderPolygon2D](class_occluderpolygon2d.md#class-occluderpolygon2d) in order for the shadow to be computed.

<a id="tutorials"></a>

## Tutorials

- [2D lights and shadows](../tutorials/2d/2d_lights_and_shadows.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [OccluderPolygon2D](class_occluderpolygon2d.md#class-occluderpolygon2d) | [occluder](class_lightoccluder2d.md#class-lightoccluder2d-property-occluder) |  |
| [int](class_int.md#class-int) | [occluder_light_mask](class_lightoccluder2d.md#class-lightoccluder2d-property-occluder-light-mask) | `1` |
| [bool](class_bool.md#class-bool) | [sdf_collision](class_lightoccluder2d.md#class-lightoccluder2d-property-sdf-collision) | `true` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-lightoccluder2d-property-occluder"></a>

[OccluderPolygon2D](class_occluderpolygon2d.md#class-occluderpolygon2d) **occluder** [🔗](class_lightoccluder2d.md#class-lightoccluder2d-property-occluder)

- void **set_occluder_polygon**(value: [OccluderPolygon2D](class_occluderpolygon2d.md#class-occluderpolygon2d))
- [OccluderPolygon2D](class_occluderpolygon2d.md#class-occluderpolygon2d) **get_occluder_polygon**()

The [OccluderPolygon2D](class_occluderpolygon2d.md#class-occluderpolygon2d) used to compute the shadow.

---


<a id="class-lightoccluder2d-property-occluder-light-mask"></a>

[int](class_int.md#class-int) **occluder_light_mask** = `1` [🔗](class_lightoccluder2d.md#class-lightoccluder2d-property-occluder-light-mask)

- void **set_occluder_light_mask**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_occluder_light_mask**()

The LightOccluder2D's occluder light mask. The LightOccluder2D will cast shadows only from Light2D(s) that have the same light mask(s).

---


<a id="class-lightoccluder2d-property-sdf-collision"></a>

[bool](class_bool.md#class-bool) **sdf_collision** = `true` [🔗](class_lightoccluder2d.md#class-lightoccluder2d-property-sdf-collision)

- void **set_as_sdf_collision**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_set_as_sdf_collision**()

If enabled, the occluder will be part of a real-time generated signed distance field that can be used in custom shaders.
