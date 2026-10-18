> Source: https://docs.godotengine.org/en/4.7/classes/class_openxrcompositionlayer.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxrcompositionlayer"></a>

<a id="class-openxrcompositionlayer"></a>

# OpenXRCompositionLayer

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [OpenXRCompositionLayerCylinder](class_openxrcompositionlayercylinder.md#class-openxrcompositionlayercylinder), [OpenXRCompositionLayerEquirect](class_openxrcompositionlayerequirect.md#class-openxrcompositionlayerequirect), [OpenXRCompositionLayerQuad](class_openxrcompositionlayerquad.md#class-openxrcompositionlayerquad)

The parent class of all OpenXR composition layer nodes.

<a id="description"></a>

## Description

Composition layers allow 2D viewports to be displayed inside of the headset by the XR compositor through special projections that retain their quality. This allows for rendering clear text while keeping the layer at a native resolution.

**Note:** If the OpenXR runtime doesn't support the given composition layer type, a fallback mesh can be generated with a [ViewportTexture](class_viewporttexture.md#class-viewporttexture), in order to emulate the composition layer.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [alpha_blend](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-alpha-blend) | `false` |
| [Vector2i](class_vector2i.md#class-vector2i) | [android_surface_size](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-android-surface-size) | `Vector2i(1024, 1024)` |
| [bool](class_bool.md#class-bool) | [enable_hole_punch](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-enable-hole-punch) | `false` |
| [EyeVisibility](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-eyevisibility) | [eye_visibility](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-eye-visibility) | `0` |
| [SubViewport](class_subviewport.md#class-subviewport) | [layer_viewport](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-layer-viewport) |  |
| [bool](class_bool.md#class-bool) | [protected_content](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-protected-content) | `false` |
| [int](class_int.md#class-int) | [sort_order](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-sort-order) | `1` |
| [Swizzle](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-swizzle) | [swapchain_state_alpha_swizzle](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-swapchain-state-alpha-swizzle) | `3` |
| [Swizzle](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-swizzle) | [swapchain_state_blue_swizzle](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-swapchain-state-blue-swizzle) | `2` |
| [Color](class_color.md#class-color) | [swapchain_state_border_color](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-swapchain-state-border-color) | `Color(0, 0, 0, 0)` |
| [Swizzle](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-swizzle) | [swapchain_state_green_swizzle](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-swapchain-state-green-swizzle) | `1` |
| [Wrap](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-wrap) | [swapchain_state_horizontal_wrap](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-swapchain-state-horizontal-wrap) | `0` |
| [Filter](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-filter) | [swapchain_state_mag_filter](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-swapchain-state-mag-filter) | `1` |
| [float](class_float.md#class-float) | [swapchain_state_max_anisotropy](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-swapchain-state-max-anisotropy) | `1.0` |
| [Filter](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-filter) | [swapchain_state_min_filter](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-swapchain-state-min-filter) | `1` |
| [MipmapMode](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-mipmapmode) | [swapchain_state_mipmap_mode](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-swapchain-state-mipmap-mode) | `2` |
| [Swizzle](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-swizzle) | [swapchain_state_red_swizzle](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-swapchain-state-red-swizzle) | `0` |
| [Wrap](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-wrap) | [swapchain_state_vertical_wrap](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-swapchain-state-vertical-wrap) | `0` |
| [bool](class_bool.md#class-bool) | [use_android_surface](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-use-android-surface) | `false` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [JavaObject](class_javaobject.md#class-javaobject) | [get_android_surface](class_openxrcompositionlayer.md#class-openxrcompositionlayer-method-get-android-surface)() |
| [Vector2](class_vector2.md#class-vector2) | [intersects_ray](class_openxrcompositionlayer.md#class-openxrcompositionlayer-method-intersects-ray)(origin: [Vector3](class_vector3.md#class-vector3), direction: [Vector3](class_vector3.md#class-vector3)) const |
| [bool](class_bool.md#class-bool) | [is_natively_supported](class_openxrcompositionlayer.md#class-openxrcompositionlayer-method-is-natively-supported)() const |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-openxrcompositionlayer-filter"></a>

enum **Filter**: [🔗](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-filter)

<a id="class-openxrcompositionlayer-constant-filter-nearest"></a>

[Filter](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-filter) **FILTER_NEAREST** = `0`

Perform nearest-neighbor filtering when sampling the texture.

<a id="class-openxrcompositionlayer-constant-filter-linear"></a>

[Filter](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-filter) **FILTER_LINEAR** = `1`

Perform linear filtering when sampling the texture.

<a id="class-openxrcompositionlayer-constant-filter-cubic"></a>

[Filter](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-filter) **FILTER_CUBIC** = `2`

Perform cubic filtering when sampling the texture.

---


<a id="enum-openxrcompositionlayer-mipmapmode"></a>

enum **MipmapMode**: [🔗](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-mipmapmode)

<a id="class-openxrcompositionlayer-constant-mipmap-mode-disabled"></a>

[MipmapMode](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-mipmapmode) **MIPMAP_MODE_DISABLED** = `0`

Disable mipmapping.

**Note:** Mipmapping can only be disabled in the Compatibility renderer.

<a id="class-openxrcompositionlayer-constant-mipmap-mode-nearest"></a>

[MipmapMode](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-mipmapmode) **MIPMAP_MODE_NEAREST** = `1`

Use the mipmap of the nearest resolution.

<a id="class-openxrcompositionlayer-constant-mipmap-mode-linear"></a>

[MipmapMode](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-mipmapmode) **MIPMAP_MODE_LINEAR** = `2`

Use linear interpolation of the two mipmaps of the nearest resolution.

---


<a id="enum-openxrcompositionlayer-wrap"></a>

enum **Wrap**: [🔗](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-wrap)

<a id="class-openxrcompositionlayer-constant-wrap-clamp-to-border"></a>

[Wrap](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-wrap) **WRAP_CLAMP_TO_BORDER** = `0`

Clamp the texture to its specified border color.

<a id="class-openxrcompositionlayer-constant-wrap-clamp-to-edge"></a>

[Wrap](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-wrap) **WRAP_CLAMP_TO_EDGE** = `1`

Clamp the texture to its edge color.

<a id="class-openxrcompositionlayer-constant-wrap-repeat"></a>

[Wrap](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-wrap) **WRAP_REPEAT** = `2`

Repeat the texture infinitely.

<a id="class-openxrcompositionlayer-constant-wrap-mirrored-repeat"></a>

[Wrap](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-wrap) **WRAP_MIRRORED_REPEAT** = `3`

Repeat the texture infinitely, mirroring it on each repeat.

<a id="class-openxrcompositionlayer-constant-wrap-mirror-clamp-to-edge"></a>

[Wrap](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-wrap) **WRAP_MIRROR_CLAMP_TO_EDGE** = `4`

Mirror the texture once and then clamp the texture to its edge color.

**Note:** This wrap mode is not available in the Compatibility renderer.

---


<a id="enum-openxrcompositionlayer-swizzle"></a>

enum **Swizzle**: [🔗](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-swizzle)

<a id="class-openxrcompositionlayer-constant-swizzle-red"></a>

[Swizzle](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-swizzle) **SWIZZLE_RED** = `0`

Maps a color channel to the value of the red channel.

<a id="class-openxrcompositionlayer-constant-swizzle-green"></a>

[Swizzle](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-swizzle) **SWIZZLE_GREEN** = `1`

Maps a color channel to the value of the green channel.

<a id="class-openxrcompositionlayer-constant-swizzle-blue"></a>

[Swizzle](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-swizzle) **SWIZZLE_BLUE** = `2`

Maps a color channel to the value of the blue channel.

<a id="class-openxrcompositionlayer-constant-swizzle-alpha"></a>

[Swizzle](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-swizzle) **SWIZZLE_ALPHA** = `3`

Maps a color channel to the value of the alpha channel.

<a id="class-openxrcompositionlayer-constant-swizzle-zero"></a>

[Swizzle](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-swizzle) **SWIZZLE_ZERO** = `4`

Maps a color channel to the value of zero.

<a id="class-openxrcompositionlayer-constant-swizzle-one"></a>

[Swizzle](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-swizzle) **SWIZZLE_ONE** = `5`

Maps a color channel to the value of one.

---


<a id="enum-openxrcompositionlayer-eyevisibility"></a>

enum **EyeVisibility**: [🔗](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-eyevisibility)

<a id="class-openxrcompositionlayer-constant-eye-visibility-both"></a>

[EyeVisibility](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-eyevisibility) **EYE_VISIBILITY_BOTH** = `0`

The layer is visible to both the left and right eyes.

<a id="class-openxrcompositionlayer-constant-eye-visibility-left"></a>

[EyeVisibility](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-eyevisibility) **EYE_VISIBILITY_LEFT** = `1`

The layer is visible only to the left eye.

<a id="class-openxrcompositionlayer-constant-eye-visibility-right"></a>

[EyeVisibility](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-eyevisibility) **EYE_VISIBILITY_RIGHT** = `2`

The layer is visible only to the right eye.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-openxrcompositionlayer-property-alpha-blend"></a>

[bool](class_bool.md#class-bool) **alpha_blend** = `false` [🔗](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-alpha-blend)

- void **set_alpha_blend**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_alpha_blend**()

Enables the blending the layer using its alpha channel.

Can be combined with [Viewport.transparent_bg](class_viewport.md#class-viewport-property-transparent-bg) to give the layer a transparent background.

---


<a id="class-openxrcompositionlayer-property-android-surface-size"></a>

[Vector2i](class_vector2i.md#class-vector2i) **android_surface_size** = `Vector2i(1024, 1024)` [🔗](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-android-surface-size)

- void **set_android_surface_size**(value: [Vector2i](class_vector2i.md#class-vector2i))
- [Vector2i](class_vector2i.md#class-vector2i) **get_android_surface_size**()

The size of the Android surface to create if [use_android_surface](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-use-android-surface) is enabled.

---


<a id="class-openxrcompositionlayer-property-enable-hole-punch"></a>

[bool](class_bool.md#class-bool) **enable_hole_punch** = `false` [🔗](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-enable-hole-punch)

- void **set_enable_hole_punch**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_enable_hole_punch**()

Enables a technique called "hole punching", which allows putting the composition layer behind the main projection layer (i.e. setting [sort_order](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-sort-order) to a negative value) while "punching a hole" through everything rendered by Godot so that the layer is still visible.

This can be used to create the illusion that the composition layer exists in the same 3D space as everything rendered by Godot, allowing objects to appear to pass both behind or in front of the composition layer.

---


<a id="class-openxrcompositionlayer-property-eye-visibility"></a>

[EyeVisibility](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-eyevisibility) **eye_visibility** = `0` [🔗](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-eye-visibility)

- void **set_eye_visibility**(value: [EyeVisibility](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-eyevisibility))
- [EyeVisibility](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-eyevisibility) **get_eye_visibility**()

The eye(s) the composition layer is visible to.

**Note:** Not all composition layer types or runtimes support restricting visibility to a single eye.

---


<a id="class-openxrcompositionlayer-property-layer-viewport"></a>

[SubViewport](class_subviewport.md#class-subviewport) **layer_viewport** [🔗](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-layer-viewport)

- void **set_layer_viewport**(value: [SubViewport](class_subviewport.md#class-subviewport))
- [SubViewport](class_subviewport.md#class-subviewport) **get_layer_viewport**()

The [SubViewport](class_subviewport.md#class-subviewport) to render on the composition layer.

---


<a id="class-openxrcompositionlayer-property-protected-content"></a>

[bool](class_bool.md#class-bool) **protected_content** = `false` [🔗](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-protected-content)

- void **set_protected_content**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_protected_content**()

If enabled, the OpenXR swapchain will be created with the `XR_SWAPCHAIN_CREATE_PROTECTED_CONTENT_BIT` flag, which will protect its contents from CPU access.

When used with an Android Surface, this may allow DRM content to be presented, and will only take effect when the Surface is first created; later changes to this property will have no effect.

---


<a id="class-openxrcompositionlayer-property-sort-order"></a>

[int](class_int.md#class-int) **sort_order** = `1` [🔗](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-sort-order)

- void **set_sort_order**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_sort_order**()

The sort order for this composition layer. Higher numbers will be shown in front of lower numbers.

**Note:** This will have no effect if a fallback mesh is being used.

---


<a id="class-openxrcompositionlayer-property-swapchain-state-alpha-swizzle"></a>

[Swizzle](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-swizzle) **swapchain_state_alpha_swizzle** = `3` [🔗](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-swapchain-state-alpha-swizzle)

- void **set_alpha_swizzle**(value: [Swizzle](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-swizzle))
- [Swizzle](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-swizzle) **get_alpha_swizzle**()

The swizzle value for the alpha channel of the swapchain state.

**Note:** This property only has an effect on devices that support the OpenXR XR_FB_swapchain_update_state OpenGLES/Vulkan extensions.

---


<a id="class-openxrcompositionlayer-property-swapchain-state-blue-swizzle"></a>

[Swizzle](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-swizzle) **swapchain_state_blue_swizzle** = `2` [🔗](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-swapchain-state-blue-swizzle)

- void **set_blue_swizzle**(value: [Swizzle](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-swizzle))
- [Swizzle](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-swizzle) **get_blue_swizzle**()

The swizzle value for the blue channel of the swapchain state.

**Note:** This property only has an effect on devices that support the OpenXR XR_FB_swapchain_update_state OpenGLES/Vulkan extensions.

---


<a id="class-openxrcompositionlayer-property-swapchain-state-border-color"></a>

[Color](class_color.md#class-color) **swapchain_state_border_color** = `Color(0, 0, 0, 0)` [🔗](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-swapchain-state-border-color)

- void **set_border_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_border_color**()

The border color of the swapchain state that is used when the wrap mode clamps to the border.

**Note:** This property only has an effect on devices that support the OpenXR XR_FB_swapchain_update_state OpenGLES/Vulkan extensions.

---


<a id="class-openxrcompositionlayer-property-swapchain-state-green-swizzle"></a>

[Swizzle](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-swizzle) **swapchain_state_green_swizzle** = `1` [🔗](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-swapchain-state-green-swizzle)

- void **set_green_swizzle**(value: [Swizzle](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-swizzle))
- [Swizzle](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-swizzle) **get_green_swizzle**()

The swizzle value for the green channel of the swapchain state.

**Note:** This property only has an effect on devices that support the OpenXR XR_FB_swapchain_update_state OpenGLES/Vulkan extensions.

---


<a id="class-openxrcompositionlayer-property-swapchain-state-horizontal-wrap"></a>

[Wrap](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-wrap) **swapchain_state_horizontal_wrap** = `0` [🔗](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-swapchain-state-horizontal-wrap)

- void **set_horizontal_wrap**(value: [Wrap](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-wrap))
- [Wrap](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-wrap) **get_horizontal_wrap**()

The horizontal wrap mode of the swapchain state.

**Note:** This property only has an effect on devices that support the OpenXR XR_FB_swapchain_update_state OpenGLES/Vulkan extensions.

---


<a id="class-openxrcompositionlayer-property-swapchain-state-mag-filter"></a>

[Filter](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-filter) **swapchain_state_mag_filter** = `1` [🔗](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-swapchain-state-mag-filter)

- void **set_mag_filter**(value: [Filter](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-filter))
- [Filter](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-filter) **get_mag_filter**()

The magnification filter of the swapchain state.

**Note:** This property only has an effect on devices that support the OpenXR XR_FB_swapchain_update_state OpenGLES/Vulkan extensions.

---


<a id="class-openxrcompositionlayer-property-swapchain-state-max-anisotropy"></a>

[float](class_float.md#class-float) **swapchain_state_max_anisotropy** = `1.0` [🔗](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-swapchain-state-max-anisotropy)

- void **set_max_anisotropy**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_max_anisotropy**()

The max anisotropy of the swapchain state.

**Note:** This property only has an effect on devices that support the OpenXR XR_FB_swapchain_update_state OpenGLES/Vulkan extensions.

---


<a id="class-openxrcompositionlayer-property-swapchain-state-min-filter"></a>

[Filter](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-filter) **swapchain_state_min_filter** = `1` [🔗](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-swapchain-state-min-filter)

- void **set_min_filter**(value: [Filter](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-filter))
- [Filter](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-filter) **get_min_filter**()

The minification filter of the swapchain state.

**Note:** This property only has an effect on devices that support the OpenXR XR_FB_swapchain_update_state OpenGLES/Vulkan extensions.

---


<a id="class-openxrcompositionlayer-property-swapchain-state-mipmap-mode"></a>

[MipmapMode](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-mipmapmode) **swapchain_state_mipmap_mode** = `2` [🔗](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-swapchain-state-mipmap-mode)

- void **set_mipmap_mode**(value: [MipmapMode](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-mipmapmode))
- [MipmapMode](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-mipmapmode) **get_mipmap_mode**()

The mipmap mode of the swapchain state.

**Note:** This property only has an effect on devices that support the OpenXR XR_FB_swapchain_update_state OpenGLES/Vulkan extensions.

---


<a id="class-openxrcompositionlayer-property-swapchain-state-red-swizzle"></a>

[Swizzle](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-swizzle) **swapchain_state_red_swizzle** = `0` [🔗](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-swapchain-state-red-swizzle)

- void **set_red_swizzle**(value: [Swizzle](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-swizzle))
- [Swizzle](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-swizzle) **get_red_swizzle**()

The swizzle value for the red channel of the swapchain state.

**Note:** This property only has an effect on devices that support the OpenXR XR_FB_swapchain_update_state OpenGLES/Vulkan extensions.

---


<a id="class-openxrcompositionlayer-property-swapchain-state-vertical-wrap"></a>

[Wrap](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-wrap) **swapchain_state_vertical_wrap** = `0` [🔗](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-swapchain-state-vertical-wrap)

- void **set_vertical_wrap**(value: [Wrap](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-wrap))
- [Wrap](class_openxrcompositionlayer.md#enum-openxrcompositionlayer-wrap) **get_vertical_wrap**()

The vertical wrap mode of the swapchain state.

**Note:** This property only has an effect on devices that support the OpenXR XR_FB_swapchain_update_state OpenGLES/Vulkan extensions.

---


<a id="class-openxrcompositionlayer-property-use-android-surface"></a>

[bool](class_bool.md#class-bool) **use_android_surface** = `false` [🔗](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-use-android-surface)

- void **set_use_android_surface**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_use_android_surface**()

If enabled, an Android surface will be created (with the dimensions from [android_surface_size](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-android-surface-size)) which will provide the 2D content for the composition layer, rather than using [layer_viewport](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-layer-viewport).

See [get_android_surface()](class_openxrcompositionlayer.md#class-openxrcompositionlayer-method-get-android-surface) for information about how to get the surface so that your application can draw to it.

**Note:** This will only work in Android builds.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-openxrcompositionlayer-method-get-android-surface"></a>

[JavaObject](class_javaobject.md#class-javaobject) **get_android_surface**() [🔗](class_openxrcompositionlayer.md#class-openxrcompositionlayer-method-get-android-surface)

Returns a [JavaObject](class_javaobject.md#class-javaobject) representing an `android.view.Surface` if [use_android_surface](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-use-android-surface) is enabled and OpenXR has created the surface. Otherwise, this will return `null`.

**Note:** The surface can only be created during an active OpenXR session. So, if [use_android_surface](class_openxrcompositionlayer.md#class-openxrcompositionlayer-property-use-android-surface) is enabled outside of an OpenXR session, it won't be created until a new session fully starts.

---


<a id="class-openxrcompositionlayer-method-intersects-ray"></a>

[Vector2](class_vector2.md#class-vector2) **intersects_ray**(origin: [Vector3](class_vector3.md#class-vector3), direction: [Vector3](class_vector3.md#class-vector3)) const [🔗](class_openxrcompositionlayer.md#class-openxrcompositionlayer-method-intersects-ray)

Returns UV coordinates where the given ray intersects with the composition layer. `origin` and `direction` must be in global space.

Returns `Vector2(-1.0, -1.0)` if the ray doesn't intersect.

---


<a id="class-openxrcompositionlayer-method-is-natively-supported"></a>

[bool](class_bool.md#class-bool) **is_natively_supported**() const [🔗](class_openxrcompositionlayer.md#class-openxrcompositionlayer-method-is-natively-supported)

Returns `true` if the OpenXR runtime natively supports this composition layer type.

**Note:** This will only return an accurate result after the OpenXR session has started.
