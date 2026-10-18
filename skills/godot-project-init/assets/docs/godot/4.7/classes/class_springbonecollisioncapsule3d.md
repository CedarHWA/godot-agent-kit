> Source: https://docs.godotengine.org/en/4.7/classes/class_springbonecollisioncapsule3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="springbonecollisioncapsule3d"></a>

<a id="class-springbonecollisioncapsule3d"></a>

# SpringBoneCollisionCapsule3D

**Inherits:** [SpringBoneCollision3D](class_springbonecollision3d.md#class-springbonecollision3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A capsule shape collision that interacts with [SpringBoneSimulator3D](class_springbonesimulator3d.md#class-springbonesimulator3d).

<a id="description"></a>

## Description

A capsule shape collision that interacts with [SpringBoneSimulator3D](class_springbonesimulator3d.md#class-springbonesimulator3d).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [height](class_springbonecollisioncapsule3d.md#class-springbonecollisioncapsule3d-property-height) | `0.5` |
| [bool](class_bool.md#class-bool) | [inside](class_springbonecollisioncapsule3d.md#class-springbonecollisioncapsule3d-property-inside) | `false` |
| [float](class_float.md#class-float) | [mid_height](class_springbonecollisioncapsule3d.md#class-springbonecollisioncapsule3d-property-mid-height) |  |
| [float](class_float.md#class-float) | [radius](class_springbonecollisioncapsule3d.md#class-springbonecollisioncapsule3d-property-radius) | `0.1` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-springbonecollisioncapsule3d-property-height"></a>

[float](class_float.md#class-float) **height** = `0.5` [🔗](class_springbonecollisioncapsule3d.md#class-springbonecollisioncapsule3d-property-height)

- void **set_height**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_height**()

The capsule's full height, including the hemispheres.

**Note:** The [height](class_springbonecollisioncapsule3d.md#class-springbonecollisioncapsule3d-property-height) of a capsule must be at least twice its [radius](class_springbonecollisioncapsule3d.md#class-springbonecollisioncapsule3d-property-radius). Otherwise, the capsule becomes a sphere. If the [height](class_springbonecollisioncapsule3d.md#class-springbonecollisioncapsule3d-property-height) is less than twice the [radius](class_springbonecollisioncapsule3d.md#class-springbonecollisioncapsule3d-property-radius), the properties adjust to a valid value.

---


<a id="class-springbonecollisioncapsule3d-property-inside"></a>

[bool](class_bool.md#class-bool) **inside** = `false` [🔗](class_springbonecollisioncapsule3d.md#class-springbonecollisioncapsule3d-property-inside)

- void **set_inside**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_inside**()

If `true`, the collision acts to trap the joint within the collision.

---


<a id="class-springbonecollisioncapsule3d-property-mid-height"></a>

[float](class_float.md#class-float) **mid_height** [🔗](class_springbonecollisioncapsule3d.md#class-springbonecollisioncapsule3d-property-mid-height)

- void **set_mid_height**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_mid_height**()

The capsule's height, excluding the hemispheres. This is the height of the central cylindrical part in the middle of the capsule, and is the distance between the centers of the two hemispheres. This is a wrapper for [height](class_springbonecollisioncapsule3d.md#class-springbonecollisioncapsule3d-property-height).

---


<a id="class-springbonecollisioncapsule3d-property-radius"></a>

[float](class_float.md#class-float) **radius** = `0.1` [🔗](class_springbonecollisioncapsule3d.md#class-springbonecollisioncapsule3d-property-radius)

- void **set_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_radius**()

The capsule's radius.

**Note:** The [radius](class_springbonecollisioncapsule3d.md#class-springbonecollisioncapsule3d-property-radius) of a capsule cannot be greater than half of its [height](class_springbonecollisioncapsule3d.md#class-springbonecollisioncapsule3d-property-height). Otherwise, the capsule becomes a sphere. If the [radius](class_springbonecollisioncapsule3d.md#class-springbonecollisioncapsule3d-property-radius) is greater than half of the [height](class_springbonecollisioncapsule3d.md#class-springbonecollisioncapsule3d-property-height), the properties adjust to a valid value.
