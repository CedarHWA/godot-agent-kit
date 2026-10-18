> Source: https://docs.godotengine.org/en/4.7/classes/class_circleshape2d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="circleshape2d"></a>

<a id="class-circleshape2d"></a>

# CircleShape2D

**Inherits:** [Shape2D](class_shape2d.md#class-shape2d) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A 2D circle shape used for physics collision.

<a id="description"></a>

## Description

A 2D circle shape, intended for use in physics. Usually used to provide a shape for a [CollisionShape2D](class_collisionshape2d.md#class-collisionshape2d).

**Performance:** **CircleShape2D** is fast to check collisions against. It is faster than [RectangleShape2D](class_rectangleshape2d.md#class-rectangleshape2d) and [CapsuleShape2D](class_capsuleshape2d.md#class-capsuleshape2d).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [radius](class_circleshape2d.md#class-circleshape2d-property-radius) | `10.0` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-circleshape2d-property-radius"></a>

[float](class_float.md#class-float) **radius** = `10.0` [🔗](class_circleshape2d.md#class-circleshape2d-property-radius)

- void **set_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_radius**()

The circle's radius.
