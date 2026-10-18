> Source: https://docs.godotengine.org/en/4.7/classes/class_rdpipelinerasterizationstate.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="rdpipelinerasterizationstate"></a>

<a id="class-rdpipelinerasterizationstate"></a>

# RDPipelineRasterizationState

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Pipeline rasterization state (used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice)).

<a id="description"></a>

## Description

This object is used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [PolygonCullMode](class_renderingdevice.md#enum-renderingdevice-polygoncullmode) | [cull_mode](class_rdpipelinerasterizationstate.md#class-rdpipelinerasterizationstate-property-cull-mode) | `0` |
| [float](class_float.md#class-float) | [depth_bias_clamp](class_rdpipelinerasterizationstate.md#class-rdpipelinerasterizationstate-property-depth-bias-clamp) | `0.0` |
| [float](class_float.md#class-float) | [depth_bias_constant_factor](class_rdpipelinerasterizationstate.md#class-rdpipelinerasterizationstate-property-depth-bias-constant-factor) | `0.0` |
| [bool](class_bool.md#class-bool) | [depth_bias_enabled](class_rdpipelinerasterizationstate.md#class-rdpipelinerasterizationstate-property-depth-bias-enabled) | `false` |
| [float](class_float.md#class-float) | [depth_bias_slope_factor](class_rdpipelinerasterizationstate.md#class-rdpipelinerasterizationstate-property-depth-bias-slope-factor) | `0.0` |
| [bool](class_bool.md#class-bool) | [discard_primitives](class_rdpipelinerasterizationstate.md#class-rdpipelinerasterizationstate-property-discard-primitives) | `false` |
| [bool](class_bool.md#class-bool) | [enable_depth_clamp](class_rdpipelinerasterizationstate.md#class-rdpipelinerasterizationstate-property-enable-depth-clamp) | `false` |
| [PolygonFrontFace](class_renderingdevice.md#enum-renderingdevice-polygonfrontface) | [front_face](class_rdpipelinerasterizationstate.md#class-rdpipelinerasterizationstate-property-front-face) | `0` |
| [float](class_float.md#class-float) | [line_width](class_rdpipelinerasterizationstate.md#class-rdpipelinerasterizationstate-property-line-width) | `1.0` |
| [int](class_int.md#class-int) | [patch_control_points](class_rdpipelinerasterizationstate.md#class-rdpipelinerasterizationstate-property-patch-control-points) | `1` |
| [bool](class_bool.md#class-bool) | [wireframe](class_rdpipelinerasterizationstate.md#class-rdpipelinerasterizationstate-property-wireframe) | `false` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-rdpipelinerasterizationstate-property-cull-mode"></a>

[PolygonCullMode](class_renderingdevice.md#enum-renderingdevice-polygoncullmode) **cull_mode** = `0` [🔗](class_rdpipelinerasterizationstate.md#class-rdpipelinerasterizationstate-property-cull-mode)

- void **set_cull_mode**(value: [PolygonCullMode](class_renderingdevice.md#enum-renderingdevice-polygoncullmode))
- [PolygonCullMode](class_renderingdevice.md#enum-renderingdevice-polygoncullmode) **get_cull_mode**()

The cull mode to use when drawing polygons, which determines whether front faces or backfaces are hidden.

---


<a id="class-rdpipelinerasterizationstate-property-depth-bias-clamp"></a>

[float](class_float.md#class-float) **depth_bias_clamp** = `0.0` [🔗](class_rdpipelinerasterizationstate.md#class-rdpipelinerasterizationstate-property-depth-bias-clamp)

- void **set_depth_bias_clamp**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_depth_bias_clamp**()

A limit for how much each depth value can be offset. If negative, it serves as a minimum value, but if positive, it serves as a maximum value.

---


<a id="class-rdpipelinerasterizationstate-property-depth-bias-constant-factor"></a>

[float](class_float.md#class-float) **depth_bias_constant_factor** = `0.0` [🔗](class_rdpipelinerasterizationstate.md#class-rdpipelinerasterizationstate-property-depth-bias-constant-factor)

- void **set_depth_bias_constant_factor**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_depth_bias_constant_factor**()

A constant offset added to each depth value. Applied after [depth_bias_slope_factor](class_rdpipelinerasterizationstate.md#class-rdpipelinerasterizationstate-property-depth-bias-slope-factor).

---


<a id="class-rdpipelinerasterizationstate-property-depth-bias-enabled"></a>

[bool](class_bool.md#class-bool) **depth_bias_enabled** = `false` [🔗](class_rdpipelinerasterizationstate.md#class-rdpipelinerasterizationstate-property-depth-bias-enabled)

- void **set_depth_bias_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_depth_bias_enabled**()

If `true`, each generated depth value will by offset by some amount. The specific amount is generated per polygon based on the values of [depth_bias_slope_factor](class_rdpipelinerasterizationstate.md#class-rdpipelinerasterizationstate-property-depth-bias-slope-factor) and [depth_bias_constant_factor](class_rdpipelinerasterizationstate.md#class-rdpipelinerasterizationstate-property-depth-bias-constant-factor).

---


<a id="class-rdpipelinerasterizationstate-property-depth-bias-slope-factor"></a>

[float](class_float.md#class-float) **depth_bias_slope_factor** = `0.0` [🔗](class_rdpipelinerasterizationstate.md#class-rdpipelinerasterizationstate-property-depth-bias-slope-factor)

- void **set_depth_bias_slope_factor**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_depth_bias_slope_factor**()

A constant scale applied to the slope of each polygons' depth. Applied before [depth_bias_constant_factor](class_rdpipelinerasterizationstate.md#class-rdpipelinerasterizationstate-property-depth-bias-constant-factor).

---


<a id="class-rdpipelinerasterizationstate-property-discard-primitives"></a>

[bool](class_bool.md#class-bool) **discard_primitives** = `false` [🔗](class_rdpipelinerasterizationstate.md#class-rdpipelinerasterizationstate-property-discard-primitives)

- void **set_discard_primitives**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_discard_primitives**()

If `true`, primitives are discarded immediately before the rasterization stage.

---


<a id="class-rdpipelinerasterizationstate-property-enable-depth-clamp"></a>

[bool](class_bool.md#class-bool) **enable_depth_clamp** = `false` [🔗](class_rdpipelinerasterizationstate.md#class-rdpipelinerasterizationstate-property-enable-depth-clamp)

- void **set_enable_depth_clamp**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_enable_depth_clamp**()

If `true`, clamps depth values according to the minimum and maximum depth of the associated viewport.

---


<a id="class-rdpipelinerasterizationstate-property-front-face"></a>

[PolygonFrontFace](class_renderingdevice.md#enum-renderingdevice-polygonfrontface) **front_face** = `0` [🔗](class_rdpipelinerasterizationstate.md#class-rdpipelinerasterizationstate-property-front-face)

- void **set_front_face**(value: [PolygonFrontFace](class_renderingdevice.md#enum-renderingdevice-polygonfrontface))
- [PolygonFrontFace](class_renderingdevice.md#enum-renderingdevice-polygonfrontface) **get_front_face**()

The winding order to use to determine which face of a triangle is considered its front face.

---


<a id="class-rdpipelinerasterizationstate-property-line-width"></a>

[float](class_float.md#class-float) **line_width** = `1.0` [🔗](class_rdpipelinerasterizationstate.md#class-rdpipelinerasterizationstate-property-line-width)

- void **set_line_width**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_line_width**()

The line width to use when drawing lines (in pixels). Thick lines may not be supported on all hardware.

---


<a id="class-rdpipelinerasterizationstate-property-patch-control-points"></a>

[int](class_int.md#class-int) **patch_control_points** = `1` [🔗](class_rdpipelinerasterizationstate.md#class-rdpipelinerasterizationstate-property-patch-control-points)

- void **set_patch_control_points**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_patch_control_points**()

The number of control points to use when drawing a patch with tessellation enabled. Higher values result in higher quality at the cost of performance.

---


<a id="class-rdpipelinerasterizationstate-property-wireframe"></a>

[bool](class_bool.md#class-bool) **wireframe** = `false` [🔗](class_rdpipelinerasterizationstate.md#class-rdpipelinerasterizationstate-property-wireframe)

- void **set_wireframe**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_wireframe**()

If `true`, performs wireframe rendering for triangles instead of flat or textured rendering.
