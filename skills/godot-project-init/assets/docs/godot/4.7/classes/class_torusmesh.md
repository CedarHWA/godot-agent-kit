> Source: https://docs.godotengine.org/en/4.7/classes/class_torusmesh.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="torusmesh"></a>

<a id="class-torusmesh"></a>

# TorusMesh

**Inherits:** [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh) **<** [Mesh](class_mesh.md#class-mesh) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Class representing a torus [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh).

<a id="description"></a>

## Description

Class representing a torus [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [inner_radius](class_torusmesh.md#class-torusmesh-property-inner-radius) | `0.5` |
| [float](class_float.md#class-float) | [outer_radius](class_torusmesh.md#class-torusmesh-property-outer-radius) | `1.0` |
| [int](class_int.md#class-int) | [ring_segments](class_torusmesh.md#class-torusmesh-property-ring-segments) | `32` |
| [int](class_int.md#class-int) | [rings](class_torusmesh.md#class-torusmesh-property-rings) | `64` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-torusmesh-property-inner-radius"></a>

[float](class_float.md#class-float) **inner_radius** = `0.5` [🔗](class_torusmesh.md#class-torusmesh-property-inner-radius)

- void **set_inner_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_inner_radius**()

The inner radius of the torus.

---


<a id="class-torusmesh-property-outer-radius"></a>

[float](class_float.md#class-float) **outer_radius** = `1.0` [🔗](class_torusmesh.md#class-torusmesh-property-outer-radius)

- void **set_outer_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_outer_radius**()

The outer radius of the torus.

---


<a id="class-torusmesh-property-ring-segments"></a>

[int](class_int.md#class-int) **ring_segments** = `32` [🔗](class_torusmesh.md#class-torusmesh-property-ring-segments)

- void **set_ring_segments**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_ring_segments**()

The number of edges each ring of the torus is constructed of.

---


<a id="class-torusmesh-property-rings"></a>

[int](class_int.md#class-int) **rings** = `64` [🔗](class_torusmesh.md#class-torusmesh-property-rings)

- void **set_rings**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_rings**()

The number of slices the torus is constructed of.
