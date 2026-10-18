> Source: https://docs.godotengine.org/en/4.7/classes/class_sphereshape3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="sphereshape3d"></a>

<a id="class-sphereshape3d"></a>

# SphereShape3D

**Inherits:** [Shape3D](class_shape3d.md#class-shape3d) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A 3D sphere shape used for physics collision.

<a id="description"></a>

## Description

A 3D sphere shape, intended for use in physics. Usually used to provide a shape for a [CollisionShape3D](class_collisionshape3d.md#class-collisionshape3d).

**Performance:** **SphereShape3D** is fast to check collisions against. It is faster than [BoxShape3D](class_boxshape3d.md#class-boxshape3d), [CapsuleShape3D](class_capsuleshape3d.md#class-capsuleshape3d), and [CylinderShape3D](class_cylindershape3d.md#class-cylindershape3d).

<a id="tutorials"></a>

## Tutorials

- [3D Physics Tests Demo](https://godotengine.org/asset-library/asset/2747)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [radius](class_sphereshape3d.md#class-sphereshape3d-property-radius) | `0.5` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-sphereshape3d-property-radius"></a>

[float](class_float.md#class-float) **radius** = `0.5` [🔗](class_sphereshape3d.md#class-sphereshape3d-property-radius)

- void **set_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_radius**()

The sphere's radius. The shape's diameter is double the radius.
