> Source: https://docs.godotengine.org/en/4.7/classes/class_capsulemesh.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="capsulemesh"></a>

<a id="class-capsulemesh"></a>

# CapsuleMesh

**Inherits:** [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh) **<** [Mesh](class_mesh.md#class-mesh) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Class representing a capsule-shaped [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh).

<a id="description"></a>

## Description

Class representing a capsule-shaped [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [height](class_capsulemesh.md#class-capsulemesh-property-height) | `2.0` |
| [int](class_int.md#class-int) | [radial_segments](class_capsulemesh.md#class-capsulemesh-property-radial-segments) | `64` |
| [float](class_float.md#class-float) | [radius](class_capsulemesh.md#class-capsulemesh-property-radius) | `0.5` |
| [int](class_int.md#class-int) | [rings](class_capsulemesh.md#class-capsulemesh-property-rings) | `8` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-capsulemesh-property-height"></a>

[float](class_float.md#class-float) **height** = `2.0` [🔗](class_capsulemesh.md#class-capsulemesh-property-height)

- void **set_height**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_height**()

Total height of the capsule mesh (including the hemispherical ends).

**Note:** The [height](class_capsulemesh.md#class-capsulemesh-property-height) of a capsule must be at least twice its [radius](class_capsulemesh.md#class-capsulemesh-property-radius). Otherwise, the capsule becomes a circle. If the [height](class_capsulemesh.md#class-capsulemesh-property-height) is less than twice the [radius](class_capsulemesh.md#class-capsulemesh-property-radius), the properties adjust to a valid value.

---


<a id="class-capsulemesh-property-radial-segments"></a>

[int](class_int.md#class-int) **radial_segments** = `64` [🔗](class_capsulemesh.md#class-capsulemesh-property-radial-segments)

- void **set_radial_segments**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_radial_segments**()

Number of radial segments on the capsule mesh.

---


<a id="class-capsulemesh-property-radius"></a>

[float](class_float.md#class-float) **radius** = `0.5` [🔗](class_capsulemesh.md#class-capsulemesh-property-radius)

- void **set_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_radius**()

Radius of the capsule mesh.

**Note:** The [radius](class_capsulemesh.md#class-capsulemesh-property-radius) of a capsule cannot be greater than half of its [height](class_capsulemesh.md#class-capsulemesh-property-height). Otherwise, the capsule becomes a circle. If the [radius](class_capsulemesh.md#class-capsulemesh-property-radius) is greater than half of the [height](class_capsulemesh.md#class-capsulemesh-property-height), the properties adjust to a valid value.

---


<a id="class-capsulemesh-property-rings"></a>

[int](class_int.md#class-int) **rings** = `8` [🔗](class_capsulemesh.md#class-capsulemesh-property-rings)

- void **set_rings**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_rings**()

Number of rings along the height of the capsule.
