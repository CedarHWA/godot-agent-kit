> Source: https://docs.godotengine.org/en/4.7/classes/class_ribbontrailmesh.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="ribbontrailmesh"></a>

<a id="class-ribbontrailmesh"></a>

# RibbonTrailMesh

**Inherits:** [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh) **<** [Mesh](class_mesh.md#class-mesh) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Represents a straight ribbon-shaped [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh) with variable width.

<a id="description"></a>

## Description

**RibbonTrailMesh** represents a straight ribbon-shaped mesh with variable width. The ribbon is composed of a number of flat or cross-shaped sections, each with the same [section_length](class_ribbontrailmesh.md#class-ribbontrailmesh-property-section-length) and number of [section_segments](class_ribbontrailmesh.md#class-ribbontrailmesh-property-section-segments). A [curve](class_ribbontrailmesh.md#class-ribbontrailmesh-property-curve) is sampled along the total length of the ribbon, meaning that the curve determines the size of the ribbon along its length.

This primitive mesh is usually used for particle trails.

<a id="tutorials"></a>

## Tutorials

- [3D Particle trails](../tutorials/3d/particles/trails.md)
- [Particle systems (3D)](../tutorials/3d/particles/index.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Curve](class_curve.md#class-curve) | [curve](class_ribbontrailmesh.md#class-ribbontrailmesh-property-curve) |  |
| [float](class_float.md#class-float) | [section_length](class_ribbontrailmesh.md#class-ribbontrailmesh-property-section-length) | `0.2` |
| [int](class_int.md#class-int) | [section_segments](class_ribbontrailmesh.md#class-ribbontrailmesh-property-section-segments) | `3` |
| [int](class_int.md#class-int) | [sections](class_ribbontrailmesh.md#class-ribbontrailmesh-property-sections) | `5` |
| [Shape](class_ribbontrailmesh.md#enum-ribbontrailmesh-shape) | [shape](class_ribbontrailmesh.md#class-ribbontrailmesh-property-shape) | `1` |
| [float](class_float.md#class-float) | [size](class_ribbontrailmesh.md#class-ribbontrailmesh-property-size) | `1.0` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-ribbontrailmesh-shape"></a>

enum **Shape**: [🔗](class_ribbontrailmesh.md#enum-ribbontrailmesh-shape)

<a id="class-ribbontrailmesh-constant-shape-flat"></a>

[Shape](class_ribbontrailmesh.md#enum-ribbontrailmesh-shape) **SHAPE_FLAT** = `0`

Gives the mesh a single flat face.

<a id="class-ribbontrailmesh-constant-shape-cross"></a>

[Shape](class_ribbontrailmesh.md#enum-ribbontrailmesh-shape) **SHAPE_CROSS** = `1`

Gives the mesh two perpendicular flat faces, making a cross shape.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-ribbontrailmesh-property-curve"></a>

[Curve](class_curve.md#class-curve) **curve** [🔗](class_ribbontrailmesh.md#class-ribbontrailmesh-property-curve)

- void **set_curve**(value: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_curve**()

Determines the size of the ribbon along its length. The size of a particular section segment is obtained by multiplying the baseline [size](class_ribbontrailmesh.md#class-ribbontrailmesh-property-size) by the value of this curve at the given distance. For values smaller than `0`, the faces will be inverted. Should be a unit [Curve](class_curve.md#class-curve).

---


<a id="class-ribbontrailmesh-property-section-length"></a>

[float](class_float.md#class-float) **section_length** = `0.2` [🔗](class_ribbontrailmesh.md#class-ribbontrailmesh-property-section-length)

- void **set_section_length**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_section_length**()

The length of a section of the ribbon.

---


<a id="class-ribbontrailmesh-property-section-segments"></a>

[int](class_int.md#class-int) **section_segments** = `3` [🔗](class_ribbontrailmesh.md#class-ribbontrailmesh-property-section-segments)

- void **set_section_segments**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_section_segments**()

The number of segments in a section. The [curve](class_ribbontrailmesh.md#class-ribbontrailmesh-property-curve) is sampled on each segment to determine its size. Higher values result in a more detailed ribbon at the cost of performance.

---


<a id="class-ribbontrailmesh-property-sections"></a>

[int](class_int.md#class-int) **sections** = `5` [🔗](class_ribbontrailmesh.md#class-ribbontrailmesh-property-sections)

- void **set_sections**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_sections**()

The total number of sections on the ribbon.

---


<a id="class-ribbontrailmesh-property-shape"></a>

[Shape](class_ribbontrailmesh.md#enum-ribbontrailmesh-shape) **shape** = `1` [🔗](class_ribbontrailmesh.md#class-ribbontrailmesh-property-shape)

- void **set_shape**(value: [Shape](class_ribbontrailmesh.md#enum-ribbontrailmesh-shape))
- [Shape](class_ribbontrailmesh.md#enum-ribbontrailmesh-shape) **get_shape**()

Determines the shape of the ribbon.

---


<a id="class-ribbontrailmesh-property-size"></a>

[float](class_float.md#class-float) **size** = `1.0` [🔗](class_ribbontrailmesh.md#class-ribbontrailmesh-property-size)

- void **set_size**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_size**()

The baseline size of the ribbon. The size of a particular section segment is obtained by multiplying this size by the value of the [curve](class_ribbontrailmesh.md#class-ribbontrailmesh-property-curve) at the given distance.
