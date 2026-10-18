> Source: https://docs.godotengine.org/en/4.7/classes/class_openxrspatialcomponentmesh3dlist.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxrspatialcomponentmesh3dlist"></a>

<a id="class-openxrspatialcomponentmesh3dlist"></a>

# OpenXRSpatialComponentMesh3DList

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Object for storing the queries mesh3d result data.

<a id="description"></a>

## Description

Object for storing the queries 3d mesh result data when calling [OpenXRSpatialEntityExtension.query_snapshot()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-query-snapshot).

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Mesh](class_mesh.md#class-mesh) | [get_mesh](class_openxrspatialcomponentmesh3dlist.md#class-openxrspatialcomponentmesh3dlist-method-get-mesh)(index: [int](class_int.md#class-int)) const |
| [Transform3D](class_transform3d.md#class-transform3d) | [get_transform](class_openxrspatialcomponentmesh3dlist.md#class-openxrspatialcomponentmesh3dlist-method-get-transform)(index: [int](class_int.md#class-int)) const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-openxrspatialcomponentmesh3dlist-method-get-mesh"></a>

[Mesh](class_mesh.md#class-mesh) **get_mesh**(index: [int](class_int.md#class-int)) const [🔗](class_openxrspatialcomponentmesh3dlist.md#class-openxrspatialcomponentmesh3dlist-method-get-mesh)

Returns the mesh for the entity at this `index`.

---


<a id="class-openxrspatialcomponentmesh3dlist-method-get-transform"></a>

[Transform3D](class_transform3d.md#class-transform3d) **get_transform**(index: [int](class_int.md#class-int)) const [🔗](class_openxrspatialcomponentmesh3dlist.md#class-openxrspatialcomponentmesh3dlist-method-get-transform)

Returns the transform for positioning our mesh for the entity at this `index`.
