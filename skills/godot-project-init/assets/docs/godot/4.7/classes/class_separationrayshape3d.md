> Source: https://docs.godotengine.org/en/4.7/classes/class_separationrayshape3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="separationrayshape3d"></a>

<a id="class-separationrayshape3d"></a>

# SeparationRayShape3D

**Inherits:** [Shape3D](class_shape3d.md#class-shape3d) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A 3D ray shape used for physics collision that tries to separate itself from any collider.

<a id="description"></a>

## Description

A 3D ray shape, intended for use in physics. Usually used to provide a shape for a [CollisionShape3D](class_collisionshape3d.md#class-collisionshape3d). When a **SeparationRayShape3D** collides with an object, it tries to separate itself from it by moving its endpoint to the collision point. For example, a **SeparationRayShape3D** next to a character can allow it to instantly move up when touching stairs.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [length](class_separationrayshape3d.md#class-separationrayshape3d-property-length) | `1.0` |
| [bool](class_bool.md#class-bool) | [slide_on_slope](class_separationrayshape3d.md#class-separationrayshape3d-property-slide-on-slope) | `false` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-separationrayshape3d-property-length"></a>

[float](class_float.md#class-float) **length** = `1.0` [🔗](class_separationrayshape3d.md#class-separationrayshape3d-property-length)

- void **set_length**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_length**()

The ray's length.

---


<a id="class-separationrayshape3d-property-slide-on-slope"></a>

[bool](class_bool.md#class-bool) **slide_on_slope** = `false` [🔗](class_separationrayshape3d.md#class-separationrayshape3d-property-slide-on-slope)

- void **set_slide_on_slope**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_slide_on_slope**()

If `false` (default), the shape always separates and returns a normal along its own direction.

If `true`, the shape can return the correct normal and separate in any direction, allowing sliding motion on slopes.
