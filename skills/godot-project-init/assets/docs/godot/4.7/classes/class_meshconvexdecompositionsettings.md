> Source: https://docs.godotengine.org/en/4.7/classes/class_meshconvexdecompositionsettings.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="meshconvexdecompositionsettings"></a>

<a id="class-meshconvexdecompositionsettings"></a>

# MeshConvexDecompositionSettings

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Parameters to be used with a [Mesh](class_mesh.md#class-mesh) convex decomposition operation.

<a id="description"></a>

## Description

Parameters to be used with a [Mesh](class_mesh.md#class-mesh) convex decomposition operation.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [convex_hull_approximation](class_meshconvexdecompositionsettings.md#class-meshconvexdecompositionsettings-property-convex-hull-approximation) | `true` |
| [int](class_int.md#class-int) | [convex_hull_downsampling](class_meshconvexdecompositionsettings.md#class-meshconvexdecompositionsettings-property-convex-hull-downsampling) | `4` |
| [float](class_float.md#class-float) | [max_concavity](class_meshconvexdecompositionsettings.md#class-meshconvexdecompositionsettings-property-max-concavity) | `1.0` |
| [int](class_int.md#class-int) | [max_convex_hulls](class_meshconvexdecompositionsettings.md#class-meshconvexdecompositionsettings-property-max-convex-hulls) | `1` |
| [int](class_int.md#class-int) | [max_num_vertices_per_convex_hull](class_meshconvexdecompositionsettings.md#class-meshconvexdecompositionsettings-property-max-num-vertices-per-convex-hull) | `32` |
| [float](class_float.md#class-float) | [min_volume_per_convex_hull](class_meshconvexdecompositionsettings.md#class-meshconvexdecompositionsettings-property-min-volume-per-convex-hull) | `0.0001` |
| [Mode](class_meshconvexdecompositionsettings.md#enum-meshconvexdecompositionsettings-mode) | [mode](class_meshconvexdecompositionsettings.md#class-meshconvexdecompositionsettings-property-mode) | `0` |
| [bool](class_bool.md#class-bool) | [normalize_mesh](class_meshconvexdecompositionsettings.md#class-meshconvexdecompositionsettings-property-normalize-mesh) | `false` |
| [int](class_int.md#class-int) | [plane_downsampling](class_meshconvexdecompositionsettings.md#class-meshconvexdecompositionsettings-property-plane-downsampling) | `4` |
| [bool](class_bool.md#class-bool) | [project_hull_vertices](class_meshconvexdecompositionsettings.md#class-meshconvexdecompositionsettings-property-project-hull-vertices) | `true` |
| [int](class_int.md#class-int) | [resolution](class_meshconvexdecompositionsettings.md#class-meshconvexdecompositionsettings-property-resolution) | `10000` |
| [float](class_float.md#class-float) | [revolution_axes_clipping_bias](class_meshconvexdecompositionsettings.md#class-meshconvexdecompositionsettings-property-revolution-axes-clipping-bias) | `0.05` |
| [float](class_float.md#class-float) | [symmetry_planes_clipping_bias](class_meshconvexdecompositionsettings.md#class-meshconvexdecompositionsettings-property-symmetry-planes-clipping-bias) | `0.05` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-meshconvexdecompositionsettings-mode"></a>

enum **Mode**: [🔗](class_meshconvexdecompositionsettings.md#enum-meshconvexdecompositionsettings-mode)

<a id="class-meshconvexdecompositionsettings-constant-convex-decomposition-mode-voxel"></a>

[Mode](class_meshconvexdecompositionsettings.md#enum-meshconvexdecompositionsettings-mode) **CONVEX_DECOMPOSITION_MODE_VOXEL** = `0`

Constant for voxel-based approximate convex decomposition.

<a id="class-meshconvexdecompositionsettings-constant-convex-decomposition-mode-tetrahedron"></a>

[Mode](class_meshconvexdecompositionsettings.md#enum-meshconvexdecompositionsettings-mode) **CONVEX_DECOMPOSITION_MODE_TETRAHEDRON** = `1`

Constant for tetrahedron-based approximate convex decomposition.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-meshconvexdecompositionsettings-property-convex-hull-approximation"></a>

[bool](class_bool.md#class-bool) **convex_hull_approximation** = `true` [🔗](class_meshconvexdecompositionsettings.md#class-meshconvexdecompositionsettings-property-convex-hull-approximation)

- void **set_convex_hull_approximation**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_convex_hull_approximation**()

If `true`, uses approximation for computing convex hulls.

---


<a id="class-meshconvexdecompositionsettings-property-convex-hull-downsampling"></a>

[int](class_int.md#class-int) **convex_hull_downsampling** = `4` [🔗](class_meshconvexdecompositionsettings.md#class-meshconvexdecompositionsettings-property-convex-hull-downsampling)

- void **set_convex_hull_downsampling**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_convex_hull_downsampling**()

Controls the precision of the convex-hull generation process during the clipping plane selection stage. Ranges from `1` to `16`.

---


<a id="class-meshconvexdecompositionsettings-property-max-concavity"></a>

[float](class_float.md#class-float) **max_concavity** = `1.0` [🔗](class_meshconvexdecompositionsettings.md#class-meshconvexdecompositionsettings-property-max-concavity)

- void **set_max_concavity**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_max_concavity**()

Maximum concavity. Ranges from `0.0` to `1.0`.

---


<a id="class-meshconvexdecompositionsettings-property-max-convex-hulls"></a>

[int](class_int.md#class-int) **max_convex_hulls** = `1` [🔗](class_meshconvexdecompositionsettings.md#class-meshconvexdecompositionsettings-property-max-convex-hulls)

- void **set_max_convex_hulls**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_max_convex_hulls**()

The maximum number of convex hulls to produce from the merge operation.

---


<a id="class-meshconvexdecompositionsettings-property-max-num-vertices-per-convex-hull"></a>

[int](class_int.md#class-int) **max_num_vertices_per_convex_hull** = `32` [🔗](class_meshconvexdecompositionsettings.md#class-meshconvexdecompositionsettings-property-max-num-vertices-per-convex-hull)

- void **set_max_num_vertices_per_convex_hull**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_max_num_vertices_per_convex_hull**()

Controls the maximum number of triangles per convex-hull. Ranges from `4` to `1024`.

---


<a id="class-meshconvexdecompositionsettings-property-min-volume-per-convex-hull"></a>

[float](class_float.md#class-float) **min_volume_per_convex_hull** = `0.0001` [🔗](class_meshconvexdecompositionsettings.md#class-meshconvexdecompositionsettings-property-min-volume-per-convex-hull)

- void **set_min_volume_per_convex_hull**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_min_volume_per_convex_hull**()

Controls the adaptive sampling of the generated convex-hulls. Ranges from `0.0` to `0.01`.

---


<a id="class-meshconvexdecompositionsettings-property-mode"></a>

[Mode](class_meshconvexdecompositionsettings.md#enum-meshconvexdecompositionsettings-mode) **mode** = `0` [🔗](class_meshconvexdecompositionsettings.md#class-meshconvexdecompositionsettings-property-mode)

- void **set_mode**(value: [Mode](class_meshconvexdecompositionsettings.md#enum-meshconvexdecompositionsettings-mode))
- [Mode](class_meshconvexdecompositionsettings.md#enum-meshconvexdecompositionsettings-mode) **get_mode**()

Mode for the approximate convex decomposition.

---


<a id="class-meshconvexdecompositionsettings-property-normalize-mesh"></a>

[bool](class_bool.md#class-bool) **normalize_mesh** = `false` [🔗](class_meshconvexdecompositionsettings.md#class-meshconvexdecompositionsettings-property-normalize-mesh)

- void **set_normalize_mesh**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_normalize_mesh**()

If `true`, normalizes the mesh before applying the convex decomposition.

---


<a id="class-meshconvexdecompositionsettings-property-plane-downsampling"></a>

[int](class_int.md#class-int) **plane_downsampling** = `4` [🔗](class_meshconvexdecompositionsettings.md#class-meshconvexdecompositionsettings-property-plane-downsampling)

- void **set_plane_downsampling**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_plane_downsampling**()

Controls the granularity of the search for the "best" clipping plane. Ranges from `1` to `16`.

---


<a id="class-meshconvexdecompositionsettings-property-project-hull-vertices"></a>

[bool](class_bool.md#class-bool) **project_hull_vertices** = `true` [🔗](class_meshconvexdecompositionsettings.md#class-meshconvexdecompositionsettings-property-project-hull-vertices)

- void **set_project_hull_vertices**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_project_hull_vertices**()

If `true`, projects output convex hull vertices onto the original source mesh to increase floating-point accuracy of the results.

---


<a id="class-meshconvexdecompositionsettings-property-resolution"></a>

[int](class_int.md#class-int) **resolution** = `10000` [🔗](class_meshconvexdecompositionsettings.md#class-meshconvexdecompositionsettings-property-resolution)

- void **set_resolution**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_resolution**()

Maximum number of voxels generated during the voxelization stage.

---


<a id="class-meshconvexdecompositionsettings-property-revolution-axes-clipping-bias"></a>

[float](class_float.md#class-float) **revolution_axes_clipping_bias** = `0.05` [🔗](class_meshconvexdecompositionsettings.md#class-meshconvexdecompositionsettings-property-revolution-axes-clipping-bias)

- void **set_revolution_axes_clipping_bias**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_revolution_axes_clipping_bias**()

Controls the bias toward clipping along revolution axes. Ranges from `0.0` to `1.0`.

---


<a id="class-meshconvexdecompositionsettings-property-symmetry-planes-clipping-bias"></a>

[float](class_float.md#class-float) **symmetry_planes_clipping_bias** = `0.05` [🔗](class_meshconvexdecompositionsettings.md#class-meshconvexdecompositionsettings-property-symmetry-planes-clipping-bias)

- void **set_symmetry_planes_clipping_bias**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_symmetry_planes_clipping_bias**()

Controls the bias toward clipping along symmetry planes. Ranges from `0.0` to `1.0`.
