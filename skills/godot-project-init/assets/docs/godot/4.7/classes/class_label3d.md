> Source: https://docs.godotengine.org/en/4.7/classes/class_label3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="label3d"></a>

<a id="class-label3d"></a>

# Label3D

**Inherits:** [GeometryInstance3D](class_geometryinstance3d.md#class-geometryinstance3d) **<** [VisualInstance3D](class_visualinstance3d.md#class-visualinstance3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A node for displaying plain text in 3D space.

<a id="description"></a>

## Description

A node for displaying plain text in 3D space. By adjusting various properties of this node, you can configure things such as the text's appearance and whether it always faces the camera.

<a id="tutorials"></a>

## Tutorials

- [3D text](../tutorials/3d/3d_text.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [alpha_antialiasing_edge](class_label3d.md#class-label3d-property-alpha-antialiasing-edge) | `0.0` |
| [AlphaAntiAliasing](class_basematerial3d.md#enum-basematerial3d-alphaantialiasing) | [alpha_antialiasing_mode](class_label3d.md#class-label3d-property-alpha-antialiasing-mode) | `0` |
| [AlphaCutMode](class_label3d.md#enum-label3d-alphacutmode) | [alpha_cut](class_label3d.md#class-label3d-property-alpha-cut) | `0` |
| [float](class_float.md#class-float) | [alpha_hash_scale](class_label3d.md#class-label3d-property-alpha-hash-scale) | `1.0` |
| [float](class_float.md#class-float) | [alpha_scissor_threshold](class_label3d.md#class-label3d-property-alpha-scissor-threshold) | `0.5` |
| [AutowrapMode](class_textserver.md#enum-textserver-autowrapmode) | [autowrap_mode](class_label3d.md#class-label3d-property-autowrap-mode) | `0` |
| BitField[[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)] | [autowrap_trim_flags](class_label3d.md#class-label3d-property-autowrap-trim-flags) | `192` |
| [BillboardMode](class_basematerial3d.md#enum-basematerial3d-billboardmode) | [billboard](class_label3d.md#class-label3d-property-billboard) | `0` |
| [ShadowCastingSetting](class_geometryinstance3d.md#enum-geometryinstance3d-shadowcastingsetting) | cast_shadow | `0` (overrides [GeometryInstance3D](class_geometryinstance3d.md#class-geometryinstance3d-property-cast-shadow)) |
| [bool](class_bool.md#class-bool) | [double_sided](class_label3d.md#class-label3d-property-double-sided) | `true` |
| [bool](class_bool.md#class-bool) | [fixed_size](class_label3d.md#class-label3d-property-fixed-size) | `false` |
| [Font](class_font.md#class-font) | [font](class_label3d.md#class-label3d-property-font) |  |
| [int](class_int.md#class-int) | [font_size](class_label3d.md#class-label3d-property-font-size) | `32` |
| [GIMode](class_geometryinstance3d.md#enum-geometryinstance3d-gimode) | gi_mode | `0` (overrides [GeometryInstance3D](class_geometryinstance3d.md#class-geometryinstance3d-property-gi-mode)) |
| [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) | [horizontal_alignment](class_label3d.md#class-label3d-property-horizontal-alignment) | `1` |
| BitField[[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] | [justification_flags](class_label3d.md#class-label3d-property-justification-flags) | `163` |
| [String](class_string.md#class-string) | [language](class_label3d.md#class-label3d-property-language) | `""` |
| [float](class_float.md#class-float) | [line_spacing](class_label3d.md#class-label3d-property-line-spacing) | `0.0` |
| [Color](class_color.md#class-color) | [modulate](class_label3d.md#class-label3d-property-modulate) | `Color(1, 1, 1, 1)` |
| [bool](class_bool.md#class-bool) | [no_depth_test](class_label3d.md#class-label3d-property-no-depth-test) | `false` |
| [Vector2](class_vector2.md#class-vector2) | [offset](class_label3d.md#class-label3d-property-offset) | `Vector2(0, 0)` |
| [Color](class_color.md#class-color) | [outline_modulate](class_label3d.md#class-label3d-property-outline-modulate) | `Color(0, 0, 0, 1)` |
| [int](class_int.md#class-int) | [outline_render_priority](class_label3d.md#class-label3d-property-outline-render-priority) | `-1` |
| [int](class_int.md#class-int) | [outline_size](class_label3d.md#class-label3d-property-outline-size) | `12` |
| [float](class_float.md#class-float) | [pixel_size](class_label3d.md#class-label3d-property-pixel-size) | `0.005` |
| [int](class_int.md#class-int) | [render_priority](class_label3d.md#class-label3d-property-render-priority) | `0` |
| [bool](class_bool.md#class-bool) | [shaded](class_label3d.md#class-label3d-property-shaded) | `false` |
| [StructuredTextParser](class_textserver.md#enum-textserver-structuredtextparser) | [structured_text_bidi_override](class_label3d.md#class-label3d-property-structured-text-bidi-override) | `0` |
| [Array](class_array.md#class-array) | [structured_text_bidi_override_options](class_label3d.md#class-label3d-property-structured-text-bidi-override-options) | `[]` |
| [String](class_string.md#class-string) | [text](class_label3d.md#class-label3d-property-text) | `""` |
| [Direction](class_textserver.md#enum-textserver-direction) | [text_direction](class_label3d.md#class-label3d-property-text-direction) | `0` |
| [TextureFilter](class_basematerial3d.md#enum-basematerial3d-texturefilter) | [texture_filter](class_label3d.md#class-label3d-property-texture-filter) | `3` |
| [bool](class_bool.md#class-bool) | [uppercase](class_label3d.md#class-label3d-property-uppercase) | `false` |
| [VerticalAlignment](class_@globalscope.md#enum-globalscope-verticalalignment) | [vertical_alignment](class_label3d.md#class-label3d-property-vertical-alignment) | `1` |
| [float](class_float.md#class-float) | [width](class_label3d.md#class-label3d-property-width) | `500.0` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [TriangleMesh](class_trianglemesh.md#class-trianglemesh) | [generate_triangle_mesh](class_label3d.md#class-label3d-method-generate-triangle-mesh)() const |
| [bool](class_bool.md#class-bool) | [get_draw_flag](class_label3d.md#class-label3d-method-get-draw-flag)(flag: [DrawFlags](class_label3d.md#enum-label3d-drawflags)) const |
| void | [set_draw_flag](class_label3d.md#class-label3d-method-set-draw-flag)(flag: [DrawFlags](class_label3d.md#enum-label3d-drawflags), enabled: [bool](class_bool.md#class-bool)) |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-label3d-drawflags"></a>

enum **DrawFlags**: [🔗](class_label3d.md#enum-label3d-drawflags)

<a id="class-label3d-constant-flag-shaded"></a>

[DrawFlags](class_label3d.md#enum-label3d-drawflags) **FLAG_SHADED** = `0`

If set, lights in the environment affect the label.

<a id="class-label3d-constant-flag-double-sided"></a>

[DrawFlags](class_label3d.md#enum-label3d-drawflags) **FLAG_DOUBLE_SIDED** = `1`

If set, text can be seen from the back as well. If not, the text is invisible when looking at it from behind.

<a id="class-label3d-constant-flag-disable-depth-test"></a>

[DrawFlags](class_label3d.md#enum-label3d-drawflags) **FLAG_DISABLE_DEPTH_TEST** = `2`

Disables the depth test, so this object is drawn on top of all others. However, objects drawn after it in the draw order may cover it.

<a id="class-label3d-constant-flag-fixed-size"></a>

[DrawFlags](class_label3d.md#enum-label3d-drawflags) **FLAG_FIXED_SIZE** = `3`

Label is scaled by depth so that it always appears the same size on screen.

<a id="class-label3d-constant-flag-max"></a>

[DrawFlags](class_label3d.md#enum-label3d-drawflags) **FLAG_MAX** = `4`

Represents the size of the [DrawFlags](class_label3d.md#enum-label3d-drawflags) enum.

---


<a id="enum-label3d-alphacutmode"></a>

enum **AlphaCutMode**: [🔗](class_label3d.md#enum-label3d-alphacutmode)

<a id="class-label3d-constant-alpha-cut-disabled"></a>

[AlphaCutMode](class_label3d.md#enum-label3d-alphacutmode) **ALPHA_CUT_DISABLED** = `0`

This mode performs standard alpha blending. It can display translucent areas, but transparency sorting issues may be visible when multiple transparent materials are overlapping. [GeometryInstance3D.cast_shadow](class_geometryinstance3d.md#class-geometryinstance3d-property-cast-shadow) has no effect when this transparency mode is used; the **Label3D** will never cast shadows.

<a id="class-label3d-constant-alpha-cut-discard"></a>

[AlphaCutMode](class_label3d.md#enum-label3d-alphacutmode) **ALPHA_CUT_DISCARD** = `1`

This mode only allows fully transparent or fully opaque pixels. Harsh edges will be visible unless some form of screen-space antialiasing is enabled (see [ProjectSettings.rendering/anti_aliasing/quality/screen_space_aa](class_projectsettings.md#class-projectsettings-property-rendering-anti-aliasing-quality-screen-space-aa)). This mode is also known as *alpha testing* or *1-bit transparency*.

**Note:** This mode might have issues with anti-aliased fonts and outlines, try adjusting [alpha_scissor_threshold](class_label3d.md#class-label3d-property-alpha-scissor-threshold) or using MSDF font.

**Note:** When using text with overlapping glyphs (e.g., cursive scripts), this mode might have transparency sorting issues between the main text and the outline.

<a id="class-label3d-constant-alpha-cut-opaque-prepass"></a>

[AlphaCutMode](class_label3d.md#enum-label3d-alphacutmode) **ALPHA_CUT_OPAQUE_PREPASS** = `2`

This mode draws fully opaque pixels in the depth prepass. This is slower than [ALPHA_CUT_DISABLED](class_label3d.md#class-label3d-constant-alpha-cut-disabled) or [ALPHA_CUT_DISCARD](class_label3d.md#class-label3d-constant-alpha-cut-discard), but it allows displaying translucent areas and smooth edges while using proper sorting.

**Note:** When using text with overlapping glyphs (e.g., cursive scripts), this mode might have transparency sorting issues between the main text and the outline.

<a id="class-label3d-constant-alpha-cut-hash"></a>

[AlphaCutMode](class_label3d.md#enum-label3d-alphacutmode) **ALPHA_CUT_HASH** = `3`

This mode draws cuts off all values below a spatially-deterministic threshold, the rest will remain opaque.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-label3d-property-alpha-antialiasing-edge"></a>

[float](class_float.md#class-float) **alpha_antialiasing_edge** = `0.0` [🔗](class_label3d.md#class-label3d-property-alpha-antialiasing-edge)

- void **set_alpha_antialiasing_edge**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_alpha_antialiasing_edge**()

Threshold at which antialiasing will be applied on the alpha channel.

---


<a id="class-label3d-property-alpha-antialiasing-mode"></a>

[AlphaAntiAliasing](class_basematerial3d.md#enum-basematerial3d-alphaantialiasing) **alpha_antialiasing_mode** = `0` [🔗](class_label3d.md#class-label3d-property-alpha-antialiasing-mode)

- void **set_alpha_antialiasing**(value: [AlphaAntiAliasing](class_basematerial3d.md#enum-basematerial3d-alphaantialiasing))
- [AlphaAntiAliasing](class_basematerial3d.md#enum-basematerial3d-alphaantialiasing) **get_alpha_antialiasing**()

The type of alpha antialiasing to apply.

---


<a id="class-label3d-property-alpha-cut"></a>

[AlphaCutMode](class_label3d.md#enum-label3d-alphacutmode) **alpha_cut** = `0` [🔗](class_label3d.md#class-label3d-property-alpha-cut)

- void **set_alpha_cut_mode**(value: [AlphaCutMode](class_label3d.md#enum-label3d-alphacutmode))
- [AlphaCutMode](class_label3d.md#enum-label3d-alphacutmode) **get_alpha_cut_mode**()

The alpha cutting mode to use for the sprite.

---


<a id="class-label3d-property-alpha-hash-scale"></a>

[float](class_float.md#class-float) **alpha_hash_scale** = `1.0` [🔗](class_label3d.md#class-label3d-property-alpha-hash-scale)

- void **set_alpha_hash_scale**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_alpha_hash_scale**()

The hashing scale for Alpha Hash. Recommended values between `0` and `2`.

---


<a id="class-label3d-property-alpha-scissor-threshold"></a>

[float](class_float.md#class-float) **alpha_scissor_threshold** = `0.5` [🔗](class_label3d.md#class-label3d-property-alpha-scissor-threshold)

- void **set_alpha_scissor_threshold**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_alpha_scissor_threshold**()

Threshold at which the alpha scissor will discard values.

---


<a id="class-label3d-property-autowrap-mode"></a>

[AutowrapMode](class_textserver.md#enum-textserver-autowrapmode) **autowrap_mode** = `0` [🔗](class_label3d.md#class-label3d-property-autowrap-mode)

- void **set_autowrap_mode**(value: [AutowrapMode](class_textserver.md#enum-textserver-autowrapmode))
- [AutowrapMode](class_textserver.md#enum-textserver-autowrapmode) **get_autowrap_mode**()

If set to something other than [TextServer.AUTOWRAP_OFF](class_textserver.md#class-textserver-constant-autowrap-off), the text gets wrapped inside the node's bounding rectangle. If you resize the node, it will change its height automatically to show all the text.

---


<a id="class-label3d-property-autowrap-trim-flags"></a>

BitField[[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)] **autowrap_trim_flags** = `192` [🔗](class_label3d.md#class-label3d-property-autowrap-trim-flags)

- void **set_autowrap_trim_flags**(value: BitField[[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)])
- BitField[[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)] **get_autowrap_trim_flags**()

Autowrap space trimming flags. See [TextServer.BREAK_TRIM_START_EDGE_SPACES](class_textserver.md#class-textserver-constant-break-trim-start-edge-spaces) and [TextServer.BREAK_TRIM_END_EDGE_SPACES](class_textserver.md#class-textserver-constant-break-trim-end-edge-spaces) for more info.

---


<a id="class-label3d-property-billboard"></a>

[BillboardMode](class_basematerial3d.md#enum-basematerial3d-billboardmode) **billboard** = `0` [🔗](class_label3d.md#class-label3d-property-billboard)

- void **set_billboard_mode**(value: [BillboardMode](class_basematerial3d.md#enum-basematerial3d-billboardmode))
- [BillboardMode](class_basematerial3d.md#enum-basematerial3d-billboardmode) **get_billboard_mode**()

The billboard mode to use for the label.

---


<a id="class-label3d-property-double-sided"></a>

[bool](class_bool.md#class-bool) **double_sided** = `true` [🔗](class_label3d.md#class-label3d-property-double-sided)

- void **set_draw_flag**(flag: [DrawFlags](class_label3d.md#enum-label3d-drawflags), enabled: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_draw_flag**(flag: [DrawFlags](class_label3d.md#enum-label3d-drawflags)) const

If `true`, text can be seen from the back as well, if `false`, it is invisible when looking at it from behind.

---


<a id="class-label3d-property-fixed-size"></a>

[bool](class_bool.md#class-bool) **fixed_size** = `false` [🔗](class_label3d.md#class-label3d-property-fixed-size)

- void **set_draw_flag**(flag: [DrawFlags](class_label3d.md#enum-label3d-drawflags), enabled: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_draw_flag**(flag: [DrawFlags](class_label3d.md#enum-label3d-drawflags)) const

If `true`, the label is rendered at the same size regardless of distance. The label's size on screen is the same as if the camera was `1.0` units away from the label's origin, regardless of the actual distance from the camera. The [Camera3D](class_camera3d.md#class-camera3d)'s field of view (or [Camera3D.size](class_camera3d.md#class-camera3d-property-size) when in orthogonal/frustum mode) still affects the size the label is drawn at.

---


<a id="class-label3d-property-font"></a>

[Font](class_font.md#class-font) **font** [🔗](class_label3d.md#class-label3d-property-font)

- void **set_font**(value: [Font](class_font.md#class-font))
- [Font](class_font.md#class-font) **get_font**()

Font configuration used to display text.

---


<a id="class-label3d-property-font-size"></a>

[int](class_int.md#class-int) **font_size** = `32` [🔗](class_label3d.md#class-label3d-property-font-size)

- void **set_font_size**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_font_size**()

Font size of the **Label3D**'s text. To make the font look more detailed when up close, increase [font_size](class_label3d.md#class-label3d-property-font-size) while decreasing [pixel_size](class_label3d.md#class-label3d-property-pixel-size) at the same time.

Higher font sizes require more time to render new characters, which can cause stuttering during gameplay.

---


<a id="class-label3d-property-horizontal-alignment"></a>

[HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) **horizontal_alignment** = `1` [🔗](class_label3d.md#class-label3d-property-horizontal-alignment)

- void **set_horizontal_alignment**(value: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment))
- [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) **get_horizontal_alignment**()

Controls the text's horizontal alignment. Supports left, center, right, and fill (also known as justify).

---


<a id="class-label3d-property-justification-flags"></a>

BitField[[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] **justification_flags** = `163` [🔗](class_label3d.md#class-label3d-property-justification-flags)

- void **set_justification_flags**(value: BitField[[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)])
- BitField[[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] **get_justification_flags**()

Line fill alignment rules.

---


<a id="class-label3d-property-language"></a>

[String](class_string.md#class-string) **language** = `""` [🔗](class_label3d.md#class-label3d-property-language)

- void **set_language**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_language**()

Language code used for line-breaking and text shaping algorithms. If left empty, the current locale is used instead.

---


<a id="class-label3d-property-line-spacing"></a>

[float](class_float.md#class-float) **line_spacing** = `0.0` [🔗](class_label3d.md#class-label3d-property-line-spacing)

- void **set_line_spacing**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_line_spacing**()

Additional vertical spacing between lines (in pixels), spacing is added to line descent. This value can be negative.

---


<a id="class-label3d-property-modulate"></a>

[Color](class_color.md#class-color) **modulate** = `Color(1, 1, 1, 1)` [🔗](class_label3d.md#class-label3d-property-modulate)

- void **set_modulate**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_modulate**()

Text [Color](class_color.md#class-color) of the **Label3D**.

---


<a id="class-label3d-property-no-depth-test"></a>

[bool](class_bool.md#class-bool) **no_depth_test** = `false` [🔗](class_label3d.md#class-label3d-property-no-depth-test)

- void **set_draw_flag**(flag: [DrawFlags](class_label3d.md#enum-label3d-drawflags), enabled: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_draw_flag**(flag: [DrawFlags](class_label3d.md#enum-label3d-drawflags)) const

If `true`, depth testing is disabled and the object will be drawn in render order.

---


<a id="class-label3d-property-offset"></a>

[Vector2](class_vector2.md#class-vector2) **offset** = `Vector2(0, 0)` [🔗](class_label3d.md#class-label3d-property-offset)

- void **set_offset**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_offset**()

The text drawing offset (in pixels).

---


<a id="class-label3d-property-outline-modulate"></a>

[Color](class_color.md#class-color) **outline_modulate** = `Color(0, 0, 0, 1)` [🔗](class_label3d.md#class-label3d-property-outline-modulate)

- void **set_outline_modulate**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_outline_modulate**()

The tint of text outline.

---


<a id="class-label3d-property-outline-render-priority"></a>

[int](class_int.md#class-int) **outline_render_priority** = `-1` [🔗](class_label3d.md#class-label3d-property-outline-render-priority)

- void **set_outline_render_priority**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_outline_render_priority**()

Sets the render priority for the text outline. Higher priority objects will be sorted in front of lower priority objects.

**Note:** This only applies if [alpha_cut](class_label3d.md#class-label3d-property-alpha-cut) is set to [ALPHA_CUT_DISABLED](class_label3d.md#class-label3d-constant-alpha-cut-disabled) (default value).

**Note:** This only applies to sorting of transparent objects. This will not impact how transparent objects are sorted relative to opaque objects. This is because opaque objects are not sorted, while transparent objects are sorted from back to front (subject to priority).

---


<a id="class-label3d-property-outline-size"></a>

[int](class_int.md#class-int) **outline_size** = `12` [🔗](class_label3d.md#class-label3d-property-outline-size)

- void **set_outline_size**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_outline_size**()

Text outline size.

---


<a id="class-label3d-property-pixel-size"></a>

[float](class_float.md#class-float) **pixel_size** = `0.005` [🔗](class_label3d.md#class-label3d-property-pixel-size)

- void **set_pixel_size**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_pixel_size**()

The size of one pixel's width on the label to scale it in 3D. To make the font look more detailed when up close, increase [font_size](class_label3d.md#class-label3d-property-font-size) while decreasing [pixel_size](class_label3d.md#class-label3d-property-pixel-size) at the same time.

---


<a id="class-label3d-property-render-priority"></a>

[int](class_int.md#class-int) **render_priority** = `0` [🔗](class_label3d.md#class-label3d-property-render-priority)

- void **set_render_priority**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_render_priority**()

Sets the render priority for the text. Higher priority objects will be sorted in front of lower priority objects.

**Note:** This only applies if [alpha_cut](class_label3d.md#class-label3d-property-alpha-cut) is set to [ALPHA_CUT_DISABLED](class_label3d.md#class-label3d-constant-alpha-cut-disabled) (default value).

**Note:** This only applies to sorting of transparent objects. This will not impact how transparent objects are sorted relative to opaque objects. This is because opaque objects are not sorted, while transparent objects are sorted from back to front (subject to priority).

---


<a id="class-label3d-property-shaded"></a>

[bool](class_bool.md#class-bool) **shaded** = `false` [🔗](class_label3d.md#class-label3d-property-shaded)

- void **set_draw_flag**(flag: [DrawFlags](class_label3d.md#enum-label3d-drawflags), enabled: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_draw_flag**(flag: [DrawFlags](class_label3d.md#enum-label3d-drawflags)) const

If `true`, the [Light3D](class_light3d.md#class-light3d) in the [Environment](class_environment.md#class-environment) has effects on the label.

---


<a id="class-label3d-property-structured-text-bidi-override"></a>

[StructuredTextParser](class_textserver.md#enum-textserver-structuredtextparser) **structured_text_bidi_override** = `0` [🔗](class_label3d.md#class-label3d-property-structured-text-bidi-override)

- void **set_structured_text_bidi_override**(value: [StructuredTextParser](class_textserver.md#enum-textserver-structuredtextparser))
- [StructuredTextParser](class_textserver.md#enum-textserver-structuredtextparser) **get_structured_text_bidi_override**()

Set BiDi algorithm override for the structured text.

---


<a id="class-label3d-property-structured-text-bidi-override-options"></a>

[Array](class_array.md#class-array) **structured_text_bidi_override_options** = `[]` [🔗](class_label3d.md#class-label3d-property-structured-text-bidi-override-options)

- void **set_structured_text_bidi_override_options**(value: [Array](class_array.md#class-array))
- [Array](class_array.md#class-array) **get_structured_text_bidi_override_options**()

Set additional options for BiDi override.

---


<a id="class-label3d-property-text"></a>

[String](class_string.md#class-string) **text** = `""` [🔗](class_label3d.md#class-label3d-property-text)

- void **set_text**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_text**()

The text to display on screen.

---


<a id="class-label3d-property-text-direction"></a>

[Direction](class_textserver.md#enum-textserver-direction) **text_direction** = `0` [🔗](class_label3d.md#class-label3d-property-text-direction)

- void **set_text_direction**(value: [Direction](class_textserver.md#enum-textserver-direction))
- [Direction](class_textserver.md#enum-textserver-direction) **get_text_direction**()

Base text writing direction.

---


<a id="class-label3d-property-texture-filter"></a>

[TextureFilter](class_basematerial3d.md#enum-basematerial3d-texturefilter) **texture_filter** = `3` [🔗](class_label3d.md#class-label3d-property-texture-filter)

- void **set_texture_filter**(value: [TextureFilter](class_basematerial3d.md#enum-basematerial3d-texturefilter))
- [TextureFilter](class_basematerial3d.md#enum-basematerial3d-texturefilter) **get_texture_filter**()

Filter flags for the texture.

---


<a id="class-label3d-property-uppercase"></a>

[bool](class_bool.md#class-bool) **uppercase** = `false` [🔗](class_label3d.md#class-label3d-property-uppercase)

- void **set_uppercase**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_uppercase**()

If `true`, all the text displays as UPPERCASE.

---


<a id="class-label3d-property-vertical-alignment"></a>

[VerticalAlignment](class_@globalscope.md#enum-globalscope-verticalalignment) **vertical_alignment** = `1` [🔗](class_label3d.md#class-label3d-property-vertical-alignment)

- void **set_vertical_alignment**(value: [VerticalAlignment](class_@globalscope.md#enum-globalscope-verticalalignment))
- [VerticalAlignment](class_@globalscope.md#enum-globalscope-verticalalignment) **get_vertical_alignment**()

Controls the text's vertical alignment. Supports top, center, and bottom.

---


<a id="class-label3d-property-width"></a>

[float](class_float.md#class-float) **width** = `500.0` [🔗](class_label3d.md#class-label3d-property-width)

- void **set_width**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_width**()

Text width (in pixels), used for autowrap and fill alignment.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-label3d-method-generate-triangle-mesh"></a>

[TriangleMesh](class_trianglemesh.md#class-trianglemesh) **generate_triangle_mesh**() const [🔗](class_label3d.md#class-label3d-method-generate-triangle-mesh)

Returns a [TriangleMesh](class_trianglemesh.md#class-trianglemesh) with the label's vertices following its current configuration (such as its [pixel_size](class_label3d.md#class-label3d-property-pixel-size)).

---


<a id="class-label3d-method-get-draw-flag"></a>

[bool](class_bool.md#class-bool) **get_draw_flag**(flag: [DrawFlags](class_label3d.md#enum-label3d-drawflags)) const [🔗](class_label3d.md#class-label3d-method-get-draw-flag)

Returns the value of the specified flag.

---


<a id="class-label3d-method-set-draw-flag"></a>

void **set_draw_flag**(flag: [DrawFlags](class_label3d.md#enum-label3d-drawflags), enabled: [bool](class_bool.md#class-bool)) [🔗](class_label3d.md#class-label3d-method-set-draw-flag)

If `true`, the specified `flag` will be enabled.
