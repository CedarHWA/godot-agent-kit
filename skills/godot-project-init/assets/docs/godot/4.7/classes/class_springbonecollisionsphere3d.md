> Source: https://docs.godotengine.org/en/4.7/classes/class_springbonecollisionsphere3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="springbonecollisionsphere3d"></a>

<a id="class-springbonecollisionsphere3d"></a>

# SpringBoneCollisionSphere3D

**Inherits:** [SpringBoneCollision3D](class_springbonecollision3d.md#class-springbonecollision3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A sphere shape collision that interacts with [SpringBoneSimulator3D](class_springbonesimulator3d.md#class-springbonesimulator3d).

<a id="description"></a>

## Description

A sphere shape collision that interacts with [SpringBoneSimulator3D](class_springbonesimulator3d.md#class-springbonesimulator3d).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [inside](class_springbonecollisionsphere3d.md#class-springbonecollisionsphere3d-property-inside) | `false` |
| [float](class_float.md#class-float) | [radius](class_springbonecollisionsphere3d.md#class-springbonecollisionsphere3d-property-radius) | `0.1` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-springbonecollisionsphere3d-property-inside"></a>

[bool](class_bool.md#class-bool) **inside** = `false` [🔗](class_springbonecollisionsphere3d.md#class-springbonecollisionsphere3d-property-inside)

- void **set_inside**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_inside**()

If `true`, the collision acts to trap the joint within the collision.

---


<a id="class-springbonecollisionsphere3d-property-radius"></a>

[float](class_float.md#class-float) **radius** = `0.1` [🔗](class_springbonecollisionsphere3d.md#class-springbonecollisionsphere3d-property-radius)

- void **set_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_radius**()

The sphere's radius.
