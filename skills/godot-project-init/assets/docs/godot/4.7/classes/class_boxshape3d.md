> Source: https://docs.godotengine.org/en/4.7/classes/class_boxshape3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="boxshape3d"></a>

<a id="class-boxshape3d"></a>

# BoxShape3D

**Inherits:** [Shape3D](class_shape3d.md#class-shape3d) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A 3D box shape used for physics collision.

<a id="description"></a>

## Description

A 3D box shape, intended for use in physics. Usually used to provide a shape for a [CollisionShape3D](class_collisionshape3d.md#class-collisionshape3d).

**Performance:** **BoxShape3D** is fast to check collisions against. It is faster than [CapsuleShape3D](class_capsuleshape3d.md#class-capsuleshape3d) and [CylinderShape3D](class_cylindershape3d.md#class-cylindershape3d), but slower than [SphereShape3D](class_sphereshape3d.md#class-sphereshape3d).

<a id="tutorials"></a>

## Tutorials

- [3D Physics Tests Demo](https://godotengine.org/asset-library/asset/2747)
- [3D Kinematic Character Demo](https://godotengine.org/asset-library/asset/2739)
- [3D Platformer Demo](https://godotengine.org/asset-library/asset/2748)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Vector3](class_vector3.md#class-vector3) | [size](class_boxshape3d.md#class-boxshape3d-property-size) | `Vector3(1, 1, 1)` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-boxshape3d-property-size"></a>

[Vector3](class_vector3.md#class-vector3) **size** = `Vector3(1, 1, 1)` [🔗](class_boxshape3d.md#class-boxshape3d-property-size)

- void **set_size**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_size**()

The box's width, height and depth.
