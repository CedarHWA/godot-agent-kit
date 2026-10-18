> Source: https://docs.godotengine.org/en/4.7/classes/class_voxelgi.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="voxelgi"></a>

<a id="class-voxelgi"></a>

# VoxelGI

**Inherits:** [VisualInstance3D](class_visualinstance3d.md#class-visualinstance3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Real-time global illumination (GI) probe.

<a id="description"></a>

## Description

**VoxelGI**s are used to provide high-quality real-time indirect light and reflections to scenes. They precompute the effect of objects that emit light and the effect of static geometry to simulate the behavior of complex light in real-time. **VoxelGI**s need to be baked before having a visible effect. However, once baked, dynamic objects will receive light from them. Furthermore, lights can be fully dynamic or baked.

**Note:** **VoxelGI** is only supported in the Forward+ rendering method, not Mobile or Compatibility.

**Procedural generation:** **VoxelGI** can be baked in an exported project, which makes it suitable for procedurally generated or user-built levels as long as all the geometry is generated in advance. For games where geometry is generated at any time during gameplay, SDFGI is more suitable (see [Environment.sdfgi_enabled](class_environment.md#class-environment-property-sdfgi-enabled)).

**Performance:** **VoxelGI** is relatively demanding on the GPU and is not suited to low-end hardware such as integrated graphics (consider [LightmapGI](class_lightmapgi.md#class-lightmapgi) instead). To improve performance, adjust [ProjectSettings.rendering/global_illumination/voxel_gi/quality](class_projectsettings.md#class-projectsettings-property-rendering-global-illumination-voxel-gi-quality) and enable [ProjectSettings.rendering/global_illumination/gi/use_half_resolution](class_projectsettings.md#class-projectsettings-property-rendering-global-illumination-gi-use-half-resolution) in the Project Settings. To provide a fallback for low-end hardware, consider adding an option to disable **VoxelGI** in your project's options menus. A **VoxelGI** node can be disabled by hiding it.

**Note:** Meshes should have sufficiently thick walls to avoid light leaks (avoid one-sided walls). For interior levels, enclose your level geometry in a sufficiently large box and bridge the loops to close the mesh. To further prevent light leaks, you can also strategically place temporary [MeshInstance3D](class_meshinstance3d.md#class-meshinstance3d) nodes with their [GeometryInstance3D.gi_mode](class_geometryinstance3d.md#class-geometryinstance3d-property-gi-mode) set to [GeometryInstance3D.GI_MODE_STATIC](class_geometryinstance3d.md#class-geometryinstance3d-constant-gi-mode-static). These temporary nodes can then be hidden after baking the **VoxelGI** node.

<a id="tutorials"></a>

## Tutorials

- [Using Voxel global illumination](../tutorials/3d/global_illumination/using_voxel_gi.md)
- [Third Person Shooter (TPS) Demo](https://godotengine.org/asset-library/asset/2710)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [CameraAttributes](class_cameraattributes.md#class-cameraattributes) | [camera_attributes](class_voxelgi.md#class-voxelgi-property-camera-attributes) |  |
| [VoxelGIData](class_voxelgidata.md#class-voxelgidata) | [data](class_voxelgi.md#class-voxelgi-property-data) |  |
| [Vector3](class_vector3.md#class-vector3) | [size](class_voxelgi.md#class-voxelgi-property-size) | `Vector3(20, 20, 20)` |
| [Subdiv](class_voxelgi.md#enum-voxelgi-subdiv) | [subdiv](class_voxelgi.md#class-voxelgi-property-subdiv) | `1` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [bake](class_voxelgi.md#class-voxelgi-method-bake)(from_node: [Node](class_node.md#class-node) = null, create_visual_debug: [bool](class_bool.md#class-bool) = false) |
| void | [debug_bake](class_voxelgi.md#class-voxelgi-method-debug-bake)() |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-voxelgi-subdiv"></a>

enum **Subdiv**: [🔗](class_voxelgi.md#enum-voxelgi-subdiv)

<a id="class-voxelgi-constant-subdiv-64"></a>

[Subdiv](class_voxelgi.md#enum-voxelgi-subdiv) **SUBDIV_64** = `0`

Use 64 subdivisions. This is the lowest quality setting, but the fastest. Use it if you can, but especially use it on lower-end hardware.

<a id="class-voxelgi-constant-subdiv-128"></a>

[Subdiv](class_voxelgi.md#enum-voxelgi-subdiv) **SUBDIV_128** = `1`

Use 128 subdivisions. This is the default quality setting.

<a id="class-voxelgi-constant-subdiv-256"></a>

[Subdiv](class_voxelgi.md#enum-voxelgi-subdiv) **SUBDIV_256** = `2`

Use 256 subdivisions.

<a id="class-voxelgi-constant-subdiv-512"></a>

[Subdiv](class_voxelgi.md#enum-voxelgi-subdiv) **SUBDIV_512** = `3`

Use 512 subdivisions. This is the highest quality setting, but the slowest. On lower-end hardware, this could cause the GPU to stall.

<a id="class-voxelgi-constant-subdiv-max"></a>

[Subdiv](class_voxelgi.md#enum-voxelgi-subdiv) **SUBDIV_MAX** = `4`

Represents the size of the [Subdiv](class_voxelgi.md#enum-voxelgi-subdiv) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-voxelgi-property-camera-attributes"></a>

[CameraAttributes](class_cameraattributes.md#class-cameraattributes) **camera_attributes** [🔗](class_voxelgi.md#class-voxelgi-property-camera-attributes)

- void **set_camera_attributes**(value: [CameraAttributes](class_cameraattributes.md#class-cameraattributes))
- [CameraAttributes](class_cameraattributes.md#class-cameraattributes) **get_camera_attributes**()

The [CameraAttributes](class_cameraattributes.md#class-cameraattributes) resource that specifies exposure levels to bake at. Auto-exposure and non exposure properties will be ignored. Exposure settings should be used to reduce the dynamic range present when baking. If exposure is too high, the **VoxelGI** will have banding artifacts or may have over-exposure artifacts.

---


<a id="class-voxelgi-property-data"></a>

[VoxelGIData](class_voxelgidata.md#class-voxelgidata) **data** [🔗](class_voxelgi.md#class-voxelgi-property-data)

- void **set_probe_data**(value: [VoxelGIData](class_voxelgidata.md#class-voxelgidata))
- [VoxelGIData](class_voxelgidata.md#class-voxelgidata) **get_probe_data**()

The [VoxelGIData](class_voxelgidata.md#class-voxelgidata) resource that holds the data for this **VoxelGI**.

---


<a id="class-voxelgi-property-size"></a>

[Vector3](class_vector3.md#class-vector3) **size** = `Vector3(20, 20, 20)` [🔗](class_voxelgi.md#class-voxelgi-property-size)

- void **set_size**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_size**()

The size of the area covered by the **VoxelGI**. This must be `1.0` or greater on each axis.

**Note:** If you make the size larger without increasing the number of subdivisions with [subdiv](class_voxelgi.md#class-voxelgi-property-subdiv), the size of each cell will increase and result in less detailed lighting.

---


<a id="class-voxelgi-property-subdiv"></a>

[Subdiv](class_voxelgi.md#enum-voxelgi-subdiv) **subdiv** = `1` [🔗](class_voxelgi.md#class-voxelgi-property-subdiv)

- void **set_subdiv**(value: [Subdiv](class_voxelgi.md#enum-voxelgi-subdiv))
- [Subdiv](class_voxelgi.md#enum-voxelgi-subdiv) **get_subdiv**()

Number of times to subdivide the grid that the **VoxelGI** operates on. A higher number results in finer detail and thus higher visual quality, while lower numbers result in better performance.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-voxelgi-method-bake"></a>

void **bake**(from_node: [Node](class_node.md#class-node) = null, create_visual_debug: [bool](class_bool.md#class-bool) = false) [🔗](class_voxelgi.md#class-voxelgi-method-bake)

Bakes the effect from all [GeometryInstance3D](class_geometryinstance3d.md#class-geometryinstance3d)s marked with [GeometryInstance3D.GI_MODE_STATIC](class_geometryinstance3d.md#class-geometryinstance3d-constant-gi-mode-static) and [Light3D](class_light3d.md#class-light3d)s marked with either [Light3D.BAKE_STATIC](class_light3d.md#class-light3d-constant-bake-static) or [Light3D.BAKE_DYNAMIC](class_light3d.md#class-light3d-constant-bake-dynamic). If `create_visual_debug` is `true`, after baking the light, this will generate a [MultiMesh](class_multimesh.md#class-multimesh) that has a cube representing each solid cell with each cube colored to the cell's albedo color. This can be used to visualize the **VoxelGI**'s data and debug any issues that may be occurring.

**Note:** [bake()](class_voxelgi.md#class-voxelgi-method-bake) works from the editor and in exported projects. This makes it suitable for procedurally generated or user-built levels. Baking a **VoxelGI** node generally takes from 5 to 20 seconds in most scenes. Reducing [subdiv](class_voxelgi.md#class-voxelgi-property-subdiv) can speed up baking.

**Note:** [GeometryInstance3D](class_geometryinstance3d.md#class-geometryinstance3d)s and [Light3D](class_light3d.md#class-light3d)s must be fully ready before [bake()](class_voxelgi.md#class-voxelgi-method-bake) is called. If you are procedurally creating those and some meshes or lights are missing from your baked **VoxelGI**, use `call_deferred("bake")` instead of calling [bake()](class_voxelgi.md#class-voxelgi-method-bake) directly.

---


<a id="class-voxelgi-method-debug-bake"></a>

void **debug_bake**() [🔗](class_voxelgi.md#class-voxelgi-method-debug-bake)

Calls [bake()](class_voxelgi.md#class-voxelgi-method-bake) with `create_visual_debug` enabled.
