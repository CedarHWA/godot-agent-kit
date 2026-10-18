> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodeparticlemultiplybyaxisangle.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodeparticlemultiplybyaxisangle"></a>

<a id="class-visualshadernodeparticlemultiplybyaxisangle"></a>

# VisualShaderNodeParticleMultiplyByAxisAngle

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A visual shader helper node for multiplying position and rotation of particles.

<a id="description"></a>

## Description

This node helps to multiply a position input vector by rotation using specific axis. Intended to work with emitters.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [degrees_mode](class_visualshadernodeparticlemultiplybyaxisangle.md#class-visualshadernodeparticlemultiplybyaxisangle-property-degrees-mode) | `true` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodeparticlemultiplybyaxisangle-property-degrees-mode"></a>

[bool](class_bool.md#class-bool) **degrees_mode** = `true` [🔗](class_visualshadernodeparticlemultiplybyaxisangle.md#class-visualshadernodeparticlemultiplybyaxisangle-property-degrees-mode)

- void **set_degrees_mode**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_degrees_mode**()

If `true`, the angle will be interpreted in degrees instead of radians.
