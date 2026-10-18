> Source: https://docs.godotengine.org/en/4.7/classes/class_segmentshape2d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="segmentshape2d"></a>

<a id="class-segmentshape2d"></a>

# SegmentShape2D

**Inherits:** [Shape2D](class_shape2d.md#class-shape2d) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A 2D line segment shape used for physics collision.

<a id="description"></a>

## Description

A 2D line segment shape, intended for use in physics. Usually used to provide a shape for a [CollisionShape2D](class_collisionshape2d.md#class-collisionshape2d).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Vector2](class_vector2.md#class-vector2) | [a](class_segmentshape2d.md#class-segmentshape2d-property-a) | `Vector2(0, 0)` |
| [Vector2](class_vector2.md#class-vector2) | [b](class_segmentshape2d.md#class-segmentshape2d-property-b) | `Vector2(0, 10)` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-segmentshape2d-property-a"></a>

[Vector2](class_vector2.md#class-vector2) **a** = `Vector2(0, 0)` [🔗](class_segmentshape2d.md#class-segmentshape2d-property-a)

- void **set_a**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_a**()

The segment's first point position.

---


<a id="class-segmentshape2d-property-b"></a>

[Vector2](class_vector2.md#class-vector2) **b** = `Vector2(0, 10)` [🔗](class_segmentshape2d.md#class-segmentshape2d-property-b)

- void **set_b**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_b**()

The segment's second point position.
