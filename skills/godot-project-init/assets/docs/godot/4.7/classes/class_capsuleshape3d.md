> Source: https://docs.godotengine.org/en/4.7/classes/class_capsuleshape3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="capsuleshape3d"></a>

<a id="class-capsuleshape3d"></a>

# CapsuleShape3D

**Inherits:** [Shape3D](class_shape3d.md#class-shape3d) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A 3D capsule shape used for physics collision.

<a id="description"></a>

## Description

A 3D capsule shape, intended for use in physics. Usually used to provide a shape for a [CollisionShape3D](class_collisionshape3d.md#class-collisionshape3d).

**Performance:** **CapsuleShape3D** is fast to check collisions against. It is faster than [CylinderShape3D](class_cylindershape3d.md#class-cylindershape3d), but slower than [SphereShape3D](class_sphereshape3d.md#class-sphereshape3d) and [BoxShape3D](class_boxshape3d.md#class-boxshape3d).

<a id="tutorials"></a>

## Tutorials

- [3D Physics Tests Demo](https://godotengine.org/asset-library/asset/2747)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [height](class_capsuleshape3d.md#class-capsuleshape3d-property-height) | `2.0` |
| [float](class_float.md#class-float) | [mid_height](class_capsuleshape3d.md#class-capsuleshape3d-property-mid-height) |  |
| [float](class_float.md#class-float) | [radius](class_capsuleshape3d.md#class-capsuleshape3d-property-radius) | `0.5` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-capsuleshape3d-property-height"></a>

[float](class_float.md#class-float) **height** = `2.0` [🔗](class_capsuleshape3d.md#class-capsuleshape3d-property-height)

- void **set_height**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_height**()

The capsule's full height, including the hemispheres.

**Note:** The [height](class_capsuleshape3d.md#class-capsuleshape3d-property-height) of a capsule must be at least twice its [radius](class_capsuleshape3d.md#class-capsuleshape3d-property-radius). Otherwise, the capsule becomes a sphere. If the [height](class_capsuleshape3d.md#class-capsuleshape3d-property-height) is less than twice the [radius](class_capsuleshape3d.md#class-capsuleshape3d-property-radius), the properties adjust to a valid value.

---


<a id="class-capsuleshape3d-property-mid-height"></a>

[float](class_float.md#class-float) **mid_height** [🔗](class_capsuleshape3d.md#class-capsuleshape3d-property-mid-height)

- void **set_mid_height**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_mid_height**()

The capsule's height, excluding the hemispheres. This is the height of the central cylindrical part in the middle of the capsule, and is the distance between the centers of the two hemispheres. This is a wrapper for [height](class_capsuleshape3d.md#class-capsuleshape3d-property-height).

---


<a id="class-capsuleshape3d-property-radius"></a>

[float](class_float.md#class-float) **radius** = `0.5` [🔗](class_capsuleshape3d.md#class-capsuleshape3d-property-radius)

- void **set_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_radius**()

The capsule's radius.

**Note:** The [radius](class_capsuleshape3d.md#class-capsuleshape3d-property-radius) of a capsule cannot be greater than half of its [height](class_capsuleshape3d.md#class-capsuleshape3d-property-height). Otherwise, the capsule becomes a sphere. If the [radius](class_capsuleshape3d.md#class-capsuleshape3d-property-radius) is greater than half of the [height](class_capsuleshape3d.md#class-capsuleshape3d-property-height), the properties adjust to a valid value.
