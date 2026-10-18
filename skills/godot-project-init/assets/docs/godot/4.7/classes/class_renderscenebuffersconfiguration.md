> Source: https://docs.godotengine.org/en/4.7/classes/class_renderscenebuffersconfiguration.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="renderscenebuffersconfiguration"></a>

<a id="class-renderscenebuffersconfiguration"></a>

# RenderSceneBuffersConfiguration

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Configuration object used to setup a [RenderSceneBuffers](class_renderscenebuffers.md#class-renderscenebuffers) object.

<a id="description"></a>

## Description

This configuration object is created and populated by the render engine on a viewport change and used to (re)configure a [RenderSceneBuffers](class_renderscenebuffers.md#class-renderscenebuffers) object.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [ViewportAnisotropicFiltering](class_renderingserver.md#enum-renderingserver-viewportanisotropicfiltering) | [anisotropic_filtering_level](class_renderscenebuffersconfiguration.md#class-renderscenebuffersconfiguration-property-anisotropic-filtering-level) | `2` |
| [float](class_float.md#class-float) | [fsr_sharpness](class_renderscenebuffersconfiguration.md#class-renderscenebuffersconfiguration-property-fsr-sharpness) | `0.0` |
| [Vector2i](class_vector2i.md#class-vector2i) | [internal_size](class_renderscenebuffersconfiguration.md#class-renderscenebuffersconfiguration-property-internal-size) | `Vector2i(0, 0)` |
| [ViewportMSAA](class_renderingserver.md#enum-renderingserver-viewportmsaa) | [msaa_3d](class_renderscenebuffersconfiguration.md#class-renderscenebuffersconfiguration-property-msaa-3d) | `0` |
| [RID](class_rid.md#class-rid) | [render_target](class_renderscenebuffersconfiguration.md#class-renderscenebuffersconfiguration-property-render-target) | `RID()` |
| [ViewportScaling3DMode](class_renderingserver.md#enum-renderingserver-viewportscaling3dmode) | [scaling_3d_mode](class_renderscenebuffersconfiguration.md#class-renderscenebuffersconfiguration-property-scaling-3d-mode) | `255` |
| [ViewportScreenSpaceAA](class_renderingserver.md#enum-renderingserver-viewportscreenspaceaa) | [screen_space_aa](class_renderscenebuffersconfiguration.md#class-renderscenebuffersconfiguration-property-screen-space-aa) | `0` |
| [Vector2i](class_vector2i.md#class-vector2i) | [target_size](class_renderscenebuffersconfiguration.md#class-renderscenebuffersconfiguration-property-target-size) | `Vector2i(0, 0)` |
| [float](class_float.md#class-float) | [texture_mipmap_bias](class_renderscenebuffersconfiguration.md#class-renderscenebuffersconfiguration-property-texture-mipmap-bias) | `0.0` |
| [int](class_int.md#class-int) | [view_count](class_renderscenebuffersconfiguration.md#class-renderscenebuffersconfiguration-property-view-count) | `1` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-renderscenebuffersconfiguration-property-anisotropic-filtering-level"></a>

[ViewportAnisotropicFiltering](class_renderingserver.md#enum-renderingserver-viewportanisotropicfiltering) **anisotropic_filtering_level** = `2` [🔗](class_renderscenebuffersconfiguration.md#class-renderscenebuffersconfiguration-property-anisotropic-filtering-level)

- void **set_anisotropic_filtering_level**(value: [ViewportAnisotropicFiltering](class_renderingserver.md#enum-renderingserver-viewportanisotropicfiltering))
- [ViewportAnisotropicFiltering](class_renderingserver.md#enum-renderingserver-viewportanisotropicfiltering) **get_anisotropic_filtering_level**()

Level of the anisotropic filter.

---


<a id="class-renderscenebuffersconfiguration-property-fsr-sharpness"></a>

[float](class_float.md#class-float) **fsr_sharpness** = `0.0` [🔗](class_renderscenebuffersconfiguration.md#class-renderscenebuffersconfiguration-property-fsr-sharpness)

- void **set_fsr_sharpness**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_fsr_sharpness**()

FSR Sharpness applicable if FSR upscaling is used.

---


<a id="class-renderscenebuffersconfiguration-property-internal-size"></a>

[Vector2i](class_vector2i.md#class-vector2i) **internal_size** = `Vector2i(0, 0)` [🔗](class_renderscenebuffersconfiguration.md#class-renderscenebuffersconfiguration-property-internal-size)

- void **set_internal_size**(value: [Vector2i](class_vector2i.md#class-vector2i))
- [Vector2i](class_vector2i.md#class-vector2i) **get_internal_size**()

The size of the 3D render buffer used for rendering.

---


<a id="class-renderscenebuffersconfiguration-property-msaa-3d"></a>

[ViewportMSAA](class_renderingserver.md#enum-renderingserver-viewportmsaa) **msaa_3d** = `0` [🔗](class_renderscenebuffersconfiguration.md#class-renderscenebuffersconfiguration-property-msaa-3d)

- void **set_msaa_3d**(value: [ViewportMSAA](class_renderingserver.md#enum-renderingserver-viewportmsaa))
- [ViewportMSAA](class_renderingserver.md#enum-renderingserver-viewportmsaa) **get_msaa_3d**()

The MSAA mode we're using for 3D rendering.

---


<a id="class-renderscenebuffersconfiguration-property-render-target"></a>

[RID](class_rid.md#class-rid) **render_target** = `RID()` [🔗](class_renderscenebuffersconfiguration.md#class-renderscenebuffersconfiguration-property-render-target)

- void **set_render_target**(value: [RID](class_rid.md#class-rid))
- [RID](class_rid.md#class-rid) **get_render_target**()

The render target associated with these buffer.

---


<a id="class-renderscenebuffersconfiguration-property-scaling-3d-mode"></a>

[ViewportScaling3DMode](class_renderingserver.md#enum-renderingserver-viewportscaling3dmode) **scaling_3d_mode** = `255` [🔗](class_renderscenebuffersconfiguration.md#class-renderscenebuffersconfiguration-property-scaling-3d-mode)

- void **set_scaling_3d_mode**(value: [ViewportScaling3DMode](class_renderingserver.md#enum-renderingserver-viewportscaling3dmode))
- [ViewportScaling3DMode](class_renderingserver.md#enum-renderingserver-viewportscaling3dmode) **get_scaling_3d_mode**()

The requested scaling mode with which we upscale/downscale if [internal_size](class_renderscenebuffersconfiguration.md#class-renderscenebuffersconfiguration-property-internal-size) and [target_size](class_renderscenebuffersconfiguration.md#class-renderscenebuffersconfiguration-property-target-size) are not equal.

---


<a id="class-renderscenebuffersconfiguration-property-screen-space-aa"></a>

[ViewportScreenSpaceAA](class_renderingserver.md#enum-renderingserver-viewportscreenspaceaa) **screen_space_aa** = `0` [🔗](class_renderscenebuffersconfiguration.md#class-renderscenebuffersconfiguration-property-screen-space-aa)

- void **set_screen_space_aa**(value: [ViewportScreenSpaceAA](class_renderingserver.md#enum-renderingserver-viewportscreenspaceaa))
- [ViewportScreenSpaceAA](class_renderingserver.md#enum-renderingserver-viewportscreenspaceaa) **get_screen_space_aa**()

The requested screen space AA applied in post processing.

---


<a id="class-renderscenebuffersconfiguration-property-target-size"></a>

[Vector2i](class_vector2i.md#class-vector2i) **target_size** = `Vector2i(0, 0)` [🔗](class_renderscenebuffersconfiguration.md#class-renderscenebuffersconfiguration-property-target-size)

- void **set_target_size**(value: [Vector2i](class_vector2i.md#class-vector2i))
- [Vector2i](class_vector2i.md#class-vector2i) **get_target_size**()

The target (upscale) size if scaling is used.

---


<a id="class-renderscenebuffersconfiguration-property-texture-mipmap-bias"></a>

[float](class_float.md#class-float) **texture_mipmap_bias** = `0.0` [🔗](class_renderscenebuffersconfiguration.md#class-renderscenebuffersconfiguration-property-texture-mipmap-bias)

- void **set_texture_mipmap_bias**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_texture_mipmap_bias**()

Bias applied to mipmaps.

**Note:** This property is only supported in the Forward+ and Mobile renderers, not Compatibility. In Compatibility, this property is always treated as if it was set to `0.0`.

---


<a id="class-renderscenebuffersconfiguration-property-view-count"></a>

[int](class_int.md#class-int) **view_count** = `1` [🔗](class_renderscenebuffersconfiguration.md#class-renderscenebuffersconfiguration-property-view-count)

- void **set_view_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_view_count**()

The number of views we're rendering.
