> Source: https://docs.godotengine.org/en/4.7/classes/class_openxrplanetracker.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxrplanetracker"></a>

<a id="class-openxrplanetracker"></a>

# OpenXRPlaneTracker

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialEntityTracker](class_openxrspatialentitytracker.md#class-openxrspatialentitytracker) **<** [XRPositionalTracker](class_xrpositionaltracker.md#class-xrpositionaltracker) **<** [XRTracker](class_xrtracker.md#class-xrtracker) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Spatial entity tracker for our spatial entity plane tracking extension.

<a id="description"></a>

## Description

Spatial entity tracker for our OpenXR spatial entity plane tracking extension. These trackers identify entities in our real space such as walls, floors, tables, etc. and map their location to our virtual space.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Vector2](class_vector2.md#class-vector2) | [bounds_size](class_openxrplanetracker.md#class-openxrplanetracker-property-bounds-size) | `Vector2(0, 0)` |
| [PlaneAlignment](class_openxrspatialcomponentplanealignmentlist.md#enum-openxrspatialcomponentplanealignmentlist-planealignment) | [plane_alignment](class_openxrplanetracker.md#class-openxrplanetracker-property-plane-alignment) | `0` |
| [String](class_string.md#class-string) | [plane_label](class_openxrplanetracker.md#class-openxrplanetracker-property-plane-label) | `""` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [clear_mesh_data](class_openxrplanetracker.md#class-openxrplanetracker-method-clear-mesh-data)() |
| [Mesh](class_mesh.md#class-mesh) | [get_mesh](class_openxrplanetracker.md#class-openxrplanetracker-method-get-mesh)() |
| [Transform3D](class_transform3d.md#class-transform3d) | [get_mesh_offset](class_openxrplanetracker.md#class-openxrplanetracker-method-get-mesh-offset)() const |
| [Shape3D](class_shape3d.md#class-shape3d) | [get_shape](class_openxrplanetracker.md#class-openxrplanetracker-method-get-shape)(thickness: [float](class_float.md#class-float) = 0.01) |
| void | [set_mesh_data](class_openxrplanetracker.md#class-openxrplanetracker-method-set-mesh-data)(origin: [Transform3D](class_transform3d.md#class-transform3d), vertices: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), indices: [PackedInt32Array](class_packedint32array.md#class-packedint32array) = PackedInt32Array()) |

---


<a id="signals"></a>

## Signals

<a id="class-openxrplanetracker-signal-mesh-changed"></a>

**mesh_changed**() [🔗](class_openxrplanetracker.md#class-openxrplanetracker-signal-mesh-changed)

Emitted when our mesh data has changed the mesh instance and collision needs to be updated.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-openxrplanetracker-property-bounds-size"></a>

[Vector2](class_vector2.md#class-vector2) **bounds_size** = `Vector2(0, 0)` [🔗](class_openxrplanetracker.md#class-openxrplanetracker-property-bounds-size)

- void **set_bounds_size**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_bounds_size**()

The bounding size of the plane. This is a 2D size.

---


<a id="class-openxrplanetracker-property-plane-alignment"></a>

[PlaneAlignment](class_openxrspatialcomponentplanealignmentlist.md#enum-openxrspatialcomponentplanealignmentlist-planealignment) **plane_alignment** = `0` [🔗](class_openxrplanetracker.md#class-openxrplanetracker-property-plane-alignment)

- void **set_plane_alignment**(value: [PlaneAlignment](class_openxrspatialcomponentplanealignmentlist.md#enum-openxrspatialcomponentplanealignmentlist-planealignment))
- [PlaneAlignment](class_openxrspatialcomponentplanealignmentlist.md#enum-openxrspatialcomponentplanealignmentlist-planealignment) **get_plane_alignment**()

The main alignment in space of this plane.

---


<a id="class-openxrplanetracker-property-plane-label"></a>

[String](class_string.md#class-string) **plane_label** = `""` [🔗](class_openxrplanetracker.md#class-openxrplanetracker-property-plane-label)

- void **set_plane_label**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_plane_label**()

The semantic label for this plane.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-openxrplanetracker-method-clear-mesh-data"></a>

void **clear_mesh_data**() [🔗](class_openxrplanetracker.md#class-openxrplanetracker-method-clear-mesh-data)

Clears the mesh data for this tracker. You should only call this if you are handling your own discovery logic.

---


<a id="class-openxrplanetracker-method-get-mesh"></a>

[Mesh](class_mesh.md#class-mesh) **get_mesh**() [🔗](class_openxrplanetracker.md#class-openxrplanetracker-method-get-mesh)

Gets a mesh created from either the mesh data or from our bounding size for this plane.

---


<a id="class-openxrplanetracker-method-get-mesh-offset"></a>

[Transform3D](class_transform3d.md#class-transform3d) **get_mesh_offset**() const [🔗](class_openxrplanetracker.md#class-openxrplanetracker-method-get-mesh-offset)

Gets the transform by which to offset the mesh and collision shape from our pose to display these correctly.

---


<a id="class-openxrplanetracker-method-get-shape"></a>

[Shape3D](class_shape3d.md#class-shape3d) **get_shape**(thickness: [float](class_float.md#class-float) = 0.01) [🔗](class_openxrplanetracker.md#class-openxrplanetracker-method-get-shape)

Gets a collision shape built either from the mesh data or from our bounding size for this plane.

---


<a id="class-openxrplanetracker-method-set-mesh-data"></a>

void **set_mesh_data**(origin: [Transform3D](class_transform3d.md#class-transform3d), vertices: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), indices: [PackedInt32Array](class_packedint32array.md#class-packedint32array) = PackedInt32Array()) [🔗](class_openxrplanetracker.md#class-openxrplanetracker-method-set-mesh-data)

Sets the mesh data for this plane. You should only call this if you are handling your own discovery logic.
