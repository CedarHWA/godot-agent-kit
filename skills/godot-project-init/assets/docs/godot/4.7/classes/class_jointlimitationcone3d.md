> Source: https://docs.godotengine.org/en/4.7/classes/class_jointlimitationcone3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="jointlimitationcone3d"></a>

<a id="class-jointlimitationcone3d"></a>

# JointLimitationCone3D

**Inherits:** [JointLimitation3D](class_jointlimitation3d.md#class-jointlimitation3d) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A cone shape limitation that interacts with [ChainIK3D](class_chainik3d.md#class-chainik3d).

<a id="description"></a>

## Description

A cone shape limitation that interacts with [ChainIK3D](class_chainik3d.md#class-chainik3d).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [angle](class_jointlimitationcone3d.md#class-jointlimitationcone3d-property-angle) | `1.5707964` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-jointlimitationcone3d-property-angle"></a>

[float](class_float.md#class-float) **angle** = `1.5707964` [🔗](class_jointlimitationcone3d.md#class-jointlimitationcone3d-property-angle)

- void **set_angle**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_angle**()

The radius range of the hole made by the cone.

`0` degrees makes a sphere without hole, `180` degrees makes a hemisphere, and `360` degrees become empty (no limitation).
