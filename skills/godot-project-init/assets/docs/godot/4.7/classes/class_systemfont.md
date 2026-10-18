> Source: https://docs.godotengine.org/en/4.7/classes/class_systemfont.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="systemfont"></a>

<a id="class-systemfont"></a>

# SystemFont

**Inherits:** [Font](class_font.md#class-font) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A font loaded from a system font. Falls back to a default theme font if not implemented on the host OS.

<a id="description"></a>

## Description

**SystemFont** loads a font from a system font with the first matching name from [font_names](class_systemfont.md#class-systemfont-property-font-names).

It will attempt to match font style, but it's not guaranteed.

The returned font might be part of a font collection or be a variable font with OpenType "weight", "width" and/or "italic" features set.

You can create [FontVariation](class_fontvariation.md#class-fontvariation) of the system font for precise control over its features.

**Note:** This class is implemented on iOS, Linux, macOS and Windows, on other platforms it will fallback to default theme font.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [allow_system_fallback](class_systemfont.md#class-systemfont-property-allow-system-fallback) | `true` |
| [FontAntialiasing](class_textserver.md#enum-textserver-fontantialiasing) | [antialiasing](class_systemfont.md#class-systemfont-property-antialiasing) | `1` |
| [bool](class_bool.md#class-bool) | [disable_embedded_bitmaps](class_systemfont.md#class-systemfont-property-disable-embedded-bitmaps) | `true` |
| [bool](class_bool.md#class-bool) | [font_italic](class_systemfont.md#class-systemfont-property-font-italic) | `false` |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [font_names](class_systemfont.md#class-systemfont-property-font-names) | `PackedStringArray()` |
| [int](class_int.md#class-int) | [font_stretch](class_systemfont.md#class-systemfont-property-font-stretch) | `100` |
| [int](class_int.md#class-int) | [font_weight](class_systemfont.md#class-systemfont-property-font-weight) | `400` |
| [bool](class_bool.md#class-bool) | [force_autohinter](class_systemfont.md#class-systemfont-property-force-autohinter) | `false` |
| [bool](class_bool.md#class-bool) | [generate_mipmaps](class_systemfont.md#class-systemfont-property-generate-mipmaps) | `false` |
| [Hinting](class_textserver.md#enum-textserver-hinting) | [hinting](class_systemfont.md#class-systemfont-property-hinting) | `1` |
| [bool](class_bool.md#class-bool) | [keep_rounding_remainders](class_systemfont.md#class-systemfont-property-keep-rounding-remainders) | `true` |
| [bool](class_bool.md#class-bool) | [modulate_color_glyphs](class_systemfont.md#class-systemfont-property-modulate-color-glyphs) | `false` |
| [int](class_int.md#class-int) | [msdf_pixel_range](class_systemfont.md#class-systemfont-property-msdf-pixel-range) | `16` |
| [int](class_int.md#class-int) | [msdf_size](class_systemfont.md#class-systemfont-property-msdf-size) | `48` |
| [bool](class_bool.md#class-bool) | [multichannel_signed_distance_field](class_systemfont.md#class-systemfont-property-multichannel-signed-distance-field) | `false` |
| [float](class_float.md#class-float) | [oversampling](class_systemfont.md#class-systemfont-property-oversampling) | `0.0` |
| [SubpixelPositioning](class_textserver.md#enum-textserver-subpixelpositioning) | [subpixel_positioning](class_systemfont.md#class-systemfont-property-subpixel-positioning) | `1` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-systemfont-property-allow-system-fallback"></a>

[bool](class_bool.md#class-bool) **allow_system_fallback** = `true` [🔗](class_systemfont.md#class-systemfont-property-allow-system-fallback)

- void **set_allow_system_fallback**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_allow_system_fallback**()

If set to `true`, system fonts can be automatically used as fallbacks.

---


<a id="class-systemfont-property-antialiasing"></a>

[FontAntialiasing](class_textserver.md#enum-textserver-fontantialiasing) **antialiasing** = `1` [🔗](class_systemfont.md#class-systemfont-property-antialiasing)

- void **set_antialiasing**(value: [FontAntialiasing](class_textserver.md#enum-textserver-fontantialiasing))
- [FontAntialiasing](class_textserver.md#enum-textserver-fontantialiasing) **get_antialiasing**()

Font anti-aliasing mode.

---


<a id="class-systemfont-property-disable-embedded-bitmaps"></a>

[bool](class_bool.md#class-bool) **disable_embedded_bitmaps** = `true` [🔗](class_systemfont.md#class-systemfont-property-disable-embedded-bitmaps)

- void **set_disable_embedded_bitmaps**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_disable_embedded_bitmaps**()

If set to `true`, embedded font bitmap loading is disabled (bitmap-only and color fonts ignore this property).

---


<a id="class-systemfont-property-font-italic"></a>

[bool](class_bool.md#class-bool) **font_italic** = `false` [🔗](class_systemfont.md#class-systemfont-property-font-italic)

- void **set_font_italic**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_font_italic**()

If set to `true`, italic or oblique font is preferred.

---


<a id="class-systemfont-property-font-names"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **font_names** = `PackedStringArray()` [🔗](class_systemfont.md#class-systemfont-property-font-names)

- void **set_font_names**(value: [PackedStringArray](class_packedstringarray.md#class-packedstringarray))
- [PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_font_names**()

Array of font family names to search, first matching font found is used.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedStringArray](class_packedstringarray.md#class-packedstringarray) for more details.

---


<a id="class-systemfont-property-font-stretch"></a>

[int](class_int.md#class-int) **font_stretch** = `100` [🔗](class_systemfont.md#class-systemfont-property-font-stretch)

- void **set_font_stretch**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_font_stretch**()

Preferred font stretch amount, compared to a normal width. A percentage value between `50%` and `200%`.

---


<a id="class-systemfont-property-font-weight"></a>

[int](class_int.md#class-int) **font_weight** = `400` [🔗](class_systemfont.md#class-systemfont-property-font-weight)

- void **set_font_weight**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_font_weight**()

Preferred weight (boldness) of the font. A value in the `100...999` range, normal font weight is `400`, bold font weight is `700`.

---


<a id="class-systemfont-property-force-autohinter"></a>

[bool](class_bool.md#class-bool) **force_autohinter** = `false` [🔗](class_systemfont.md#class-systemfont-property-force-autohinter)

- void **set_force_autohinter**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_force_autohinter**()

If set to `true`, auto-hinting is supported and preferred over font built-in hinting.

---


<a id="class-systemfont-property-generate-mipmaps"></a>

[bool](class_bool.md#class-bool) **generate_mipmaps** = `false` [🔗](class_systemfont.md#class-systemfont-property-generate-mipmaps)

- void **set_generate_mipmaps**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_generate_mipmaps**()

If set to `true`, generate mipmaps for the font textures.

---


<a id="class-systemfont-property-hinting"></a>

[Hinting](class_textserver.md#enum-textserver-hinting) **hinting** = `1` [🔗](class_systemfont.md#class-systemfont-property-hinting)

- void **set_hinting**(value: [Hinting](class_textserver.md#enum-textserver-hinting))
- [Hinting](class_textserver.md#enum-textserver-hinting) **get_hinting**()

Font hinting mode.

---


<a id="class-systemfont-property-keep-rounding-remainders"></a>

[bool](class_bool.md#class-bool) **keep_rounding_remainders** = `true` [🔗](class_systemfont.md#class-systemfont-property-keep-rounding-remainders)

- void **set_keep_rounding_remainders**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_keep_rounding_remainders**()

If set to `true`, when aligning glyphs to the pixel boundaries rounding remainders are accumulated to ensure more uniform glyph distribution. This setting has no effect if subpixel positioning is enabled.

---


<a id="class-systemfont-property-modulate-color-glyphs"></a>

[bool](class_bool.md#class-bool) **modulate_color_glyphs** = `false` [🔗](class_systemfont.md#class-systemfont-property-modulate-color-glyphs)

- void **set_modulate_color_glyphs**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_modulate_color_glyphs**()

If set to `true`, color modulation is applied when drawing colored glyphs, otherwise it's applied to the monochrome glyphs only.

---


<a id="class-systemfont-property-msdf-pixel-range"></a>

[int](class_int.md#class-int) **msdf_pixel_range** = `16` [🔗](class_systemfont.md#class-systemfont-property-msdf-pixel-range)

- void **set_msdf_pixel_range**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_msdf_pixel_range**()

The width of the range around the shape between the minimum and maximum representable signed distance. If using font outlines, [msdf_pixel_range](class_systemfont.md#class-systemfont-property-msdf-pixel-range) must be set to at least *twice* the size of the largest font outline. The default [msdf_pixel_range](class_systemfont.md#class-systemfont-property-msdf-pixel-range) value of `16` allows outline sizes up to `8` to look correct.

---


<a id="class-systemfont-property-msdf-size"></a>

[int](class_int.md#class-int) **msdf_size** = `48` [🔗](class_systemfont.md#class-systemfont-property-msdf-size)

- void **set_msdf_size**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_msdf_size**()

Source font size used to generate MSDF textures. Higher values allow for more precision, but are slower to render and require more memory. Only increase this value if you notice a visible lack of precision in glyph rendering.

---


<a id="class-systemfont-property-multichannel-signed-distance-field"></a>

[bool](class_bool.md#class-bool) **multichannel_signed_distance_field** = `false` [🔗](class_systemfont.md#class-systemfont-property-multichannel-signed-distance-field)

- void **set_multichannel_signed_distance_field**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_multichannel_signed_distance_field**()

If set to `true`, glyphs of all sizes are rendered using single multichannel signed distance field generated from the dynamic font vector data.

---


<a id="class-systemfont-property-oversampling"></a>

[float](class_float.md#class-float) **oversampling** = `0.0` [🔗](class_systemfont.md#class-systemfont-property-oversampling)

- void **set_oversampling**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_oversampling**()

If set to a positive value, overrides the oversampling factor of the viewport this font is used in. See [Viewport.oversampling](class_viewport.md#class-viewport-property-oversampling). This value doesn't override the `oversampling` parameter of `draw_*` methods.

---


<a id="class-systemfont-property-subpixel-positioning"></a>

[SubpixelPositioning](class_textserver.md#enum-textserver-subpixelpositioning) **subpixel_positioning** = `1` [🔗](class_systemfont.md#class-systemfont-property-subpixel-positioning)

- void **set_subpixel_positioning**(value: [SubpixelPositioning](class_textserver.md#enum-textserver-subpixelpositioning))
- [SubpixelPositioning](class_textserver.md#enum-textserver-subpixelpositioning) **get_subpixel_positioning**()

Font glyph subpixel positioning mode. Subpixel positioning provides shaper text and better kerning for smaller font sizes, at the cost of memory usage and font rasterization speed. Use [TextServer.SUBPIXEL_POSITIONING_AUTO](class_textserver.md#class-textserver-constant-subpixel-positioning-auto) to automatically enable it based on the font size.
