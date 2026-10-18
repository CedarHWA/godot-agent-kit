> Source: https://docs.godotengine.org/en/4.7/classes/class_spheremesh.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="spheremesh"></a>

<a id="class-spheremesh"></a>

# SphereMesh

**Inherits:** [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh) **<** [Mesh](class_mesh.md#class-mesh) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Class representing a spherical [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh).

<a id="description"></a>

## Description

Class representing a spherical [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [height](class_spheremesh.md#class-spheremesh-property-height) | `1.0` |
| [bool](class_bool.md#class-bool) | [is_hemisphere](class_spheremesh.md#class-spheremesh-property-is-hemisphere) | `false` |
| [int](class_int.md#class-int) | [radial_segments](class_spheremesh.md#class-spheremesh-property-radial-segments) | `64` |
| [float](class_float.md#class-float) | [radius](class_spheremesh.md#class-spheremesh-property-radius) | `0.5` |
| [int](class_int.md#class-int) | [rings](class_spheremesh.md#class-spheremesh-property-rings) | `32` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-spheremesh-property-height"></a>

[float](class_float.md#class-float) **height** = `1.0` [🔗](class_spheremesh.md#class-spheremesh-property-height)

- void **set_height**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_height**()

Full height of the sphere.

---


<a id="class-spheremesh-property-is-hemisphere"></a>

[bool](class_bool.md#class-bool) **is_hemisphere** = `false` [🔗](class_spheremesh.md#class-spheremesh-property-is-hemisphere)

- void **set_is_hemisphere**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_is_hemisphere**()

If `true`, a hemisphere is created rather than a full sphere.

**Note:** To get a regular hemisphere, the height and radius of the sphere must be equal.

---


<a id="class-spheremesh-property-radial-segments"></a>

[int](class_int.md#class-int) **radial_segments** = `64` [🔗](class_spheremesh.md#class-spheremesh-property-radial-segments)

- void **set_radial_segments**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_radial_segments**()

Number of radial segments on the sphere.

---


<a id="class-spheremesh-property-radius"></a>

[float](class_float.md#class-float) **radius** = `0.5` [🔗](class_spheremesh.md#class-spheremesh-property-radius)

- void **set_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_radius**()

Radius of sphere.

---


<a id="class-spheremesh-property-rings"></a>

[int](class_int.md#class-int) **rings** = `32` [🔗](class_spheremesh.md#class-spheremesh-property-rings)

- void **set_rings**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_rings**()

Number of segments along the height of the sphere.
