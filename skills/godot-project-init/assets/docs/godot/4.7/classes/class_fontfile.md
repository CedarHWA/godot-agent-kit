> Source: https://docs.godotengine.org/en/4.7/classes/class_fontfile.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="fontfile"></a>

<a id="class-fontfile"></a>

# FontFile

**Inherits:** [Font](class_font.md#class-font) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Holds font source data and prerendered glyph cache, imported from a dynamic or a bitmap font.

<a id="description"></a>

## Description

**FontFile** contains a set of glyphs to represent Unicode characters imported from a font file, as well as a cache of rasterized glyphs, and a set of fallback [Font](class_font.md#class-font)s to use.

Use [FontVariation](class_fontvariation.md#class-fontvariation) to access specific OpenType variation of the font, create simulated bold / slanted version, and draw lines of text.

For more complex text processing, use [FontVariation](class_fontvariation.md#class-fontvariation) in conjunction with [TextLine](class_textline.md#class-textline) or [TextParagraph](class_textparagraph.md#class-textparagraph).

Supported font formats:

- Dynamic font importer: TrueType (.ttf), TrueType collection (.ttc), OpenType (.otf), OpenType collection (.otc), WOFF (.woff), WOFF2 (.woff2), Type 1 (.pfb, .pfm).
- Bitmap font importer: AngelCode BMFont (.fnt, .font), text and binary (version 3) format variants.
- Monospace image font importer: All supported image formats.

**Note:** A character is a symbol that represents an item (letter, digit etc.) in an abstract way.

**Note:** A glyph is a bitmap or a shape used to draw one or more characters in a context-dependent manner. Glyph indices are bound to the specific font data source.

**Note:** If none of the font data sources contain glyphs for a character used in a string, the character in question will be replaced with a box displaying its hexadecimal code.

```gdscript
var f = load("res://BarlowCondensed-Bold.ttf")
$Label.add_theme_font_override("font", f)
$Label.add_theme_font_size_override("font_size", 64)
```

```csharp
var f = ResourceLoader.Load<FontFile>("res://BarlowCondensed-Bold.ttf");
GetNode("Label").AddThemeFontOverride("font", f);
GetNode("Label").AddThemeFontSizeOverride("font_size", 64);
```

<a id="tutorials"></a>

## Tutorials

- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [allow_system_fallback](class_fontfile.md#class-fontfile-property-allow-system-fallback) | `true` |
| [FontAntialiasing](class_textserver.md#enum-textserver-fontantialiasing) | [antialiasing](class_fontfile.md#class-fontfile-property-antialiasing) | `1` |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray) | [data](class_fontfile.md#class-fontfile-property-data) | `PackedByteArray()` |
| [bool](class_bool.md#class-bool) | [disable_embedded_bitmaps](class_fontfile.md#class-fontfile-property-disable-embedded-bitmaps) | `true` |
| [int](class_int.md#class-int) | [fixed_size](class_fontfile.md#class-fontfile-property-fixed-size) | `0` |
| [FixedSizeScaleMode](class_textserver.md#enum-textserver-fixedsizescalemode) | [fixed_size_scale_mode](class_fontfile.md#class-fontfile-property-fixed-size-scale-mode) | `0` |
| [String](class_string.md#class-string) | [font_name](class_fontfile.md#class-fontfile-property-font-name) | `""` |
| [int](class_int.md#class-int) | [font_stretch](class_fontfile.md#class-fontfile-property-font-stretch) | `100` |
| BitField[[FontStyle](class_textserver.md#enum-textserver-fontstyle)] | [font_style](class_fontfile.md#class-fontfile-property-font-style) | `0` |
| [int](class_int.md#class-int) | [font_weight](class_fontfile.md#class-fontfile-property-font-weight) | `400` |
| [bool](class_bool.md#class-bool) | [force_autohinter](class_fontfile.md#class-fontfile-property-force-autohinter) | `false` |
| [bool](class_bool.md#class-bool) | [generate_mipmaps](class_fontfile.md#class-fontfile-property-generate-mipmaps) | `false` |
| [Hinting](class_textserver.md#enum-textserver-hinting) | [hinting](class_fontfile.md#class-fontfile-property-hinting) | `1` |
| [bool](class_bool.md#class-bool) | [keep_rounding_remainders](class_fontfile.md#class-fontfile-property-keep-rounding-remainders) | `true` |
| [bool](class_bool.md#class-bool) | [modulate_color_glyphs](class_fontfile.md#class-fontfile-property-modulate-color-glyphs) | `false` |
| [int](class_int.md#class-int) | [msdf_pixel_range](class_fontfile.md#class-fontfile-property-msdf-pixel-range) | `16` |
| [int](class_int.md#class-int) | [msdf_size](class_fontfile.md#class-fontfile-property-msdf-size) | `48` |
| [bool](class_bool.md#class-bool) | [multichannel_signed_distance_field](class_fontfile.md#class-fontfile-property-multichannel-signed-distance-field) | `false` |
| [Dictionary](class_dictionary.md#class-dictionary) | [opentype_feature_overrides](class_fontfile.md#class-fontfile-property-opentype-feature-overrides) | `{}` |
| [float](class_float.md#class-float) | [oversampling](class_fontfile.md#class-fontfile-property-oversampling) | `0.0` |
| [String](class_string.md#class-string) | [style_name](class_fontfile.md#class-fontfile-property-style-name) | `""` |
| [SubpixelPositioning](class_textserver.md#enum-textserver-subpixelpositioning) | [subpixel_positioning](class_fontfile.md#class-fontfile-property-subpixel-positioning) | `1` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [clear_cache](class_fontfile.md#class-fontfile-method-clear-cache)() |
| void | [clear_glyphs](class_fontfile.md#class-fontfile-method-clear-glyphs)(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i)) |
| void | [clear_kerning_map](class_fontfile.md#class-fontfile-method-clear-kerning-map)(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int)) |
| void | [clear_size_cache](class_fontfile.md#class-fontfile-method-clear-size-cache)(cache_index: [int](class_int.md#class-int)) |
| void | [clear_textures](class_fontfile.md#class-fontfile-method-clear-textures)(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i)) |
| [float](class_float.md#class-float) | [get_cache_ascent](class_fontfile.md#class-fontfile-method-get-cache-ascent)(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_cache_count](class_fontfile.md#class-fontfile-method-get-cache-count)() const |
| [float](class_float.md#class-float) | [get_cache_descent](class_fontfile.md#class-fontfile-method-get-cache-descent)(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int)) const |
| [float](class_float.md#class-float) | [get_cache_scale](class_fontfile.md#class-fontfile-method-get-cache-scale)(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int)) const |
| [float](class_float.md#class-float) | [get_cache_underline_position](class_fontfile.md#class-fontfile-method-get-cache-underline-position)(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int)) const |
| [float](class_float.md#class-float) | [get_cache_underline_thickness](class_fontfile.md#class-fontfile-method-get-cache-underline-thickness)(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_char_from_glyph_index](class_fontfile.md#class-fontfile-method-get-char-from-glyph-index)(size: [int](class_int.md#class-int), glyph_index: [int](class_int.md#class-int)) const |
| [float](class_float.md#class-float) | [get_embolden](class_fontfile.md#class-fontfile-method-get-embolden)(cache_index: [int](class_int.md#class-int)) const |
| [float](class_float.md#class-float) | [get_extra_baseline_offset](class_fontfile.md#class-fontfile-method-get-extra-baseline-offset)(cache_index: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_extra_spacing](class_fontfile.md#class-fontfile-method-get-extra-spacing)(cache_index: [int](class_int.md#class-int), spacing: [SpacingType](class_textserver.md#enum-textserver-spacingtype)) const |
| [int](class_int.md#class-int) | [get_face_index](class_fontfile.md#class-fontfile-method-get-face-index)(cache_index: [int](class_int.md#class-int)) const |
| [Vector2](class_vector2.md#class-vector2) | [get_glyph_advance](class_fontfile.md#class-fontfile-method-get-glyph-advance)(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int), glyph: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_glyph_index](class_fontfile.md#class-fontfile-method-get-glyph-index)(size: [int](class_int.md#class-int), char: [int](class_int.md#class-int), variation_selector: [int](class_int.md#class-int)) const |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array) | [get_glyph_list](class_fontfile.md#class-fontfile-method-get-glyph-list)(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i)) const |
| [Vector2](class_vector2.md#class-vector2) | [get_glyph_offset](class_fontfile.md#class-fontfile-method-get-glyph-offset)(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int)) const |
| [Vector2](class_vector2.md#class-vector2) | [get_glyph_size](class_fontfile.md#class-fontfile-method-get-glyph-size)(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_glyph_texture_idx](class_fontfile.md#class-fontfile-method-get-glyph-texture-idx)(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int)) const |
| [Rect2](class_rect2.md#class-rect2) | [get_glyph_uv_rect](class_fontfile.md#class-fontfile-method-get-glyph-uv-rect)(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int)) const |
| [Vector2](class_vector2.md#class-vector2) | [get_kerning](class_fontfile.md#class-fontfile-method-get-kerning)(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int), glyph_pair: [Vector2i](class_vector2i.md#class-vector2i)) const |
| [Array](class_array.md#class-array)[[Vector2i](class_vector2i.md#class-vector2i)] | [get_kerning_list](class_fontfile.md#class-fontfile-method-get-kerning-list)(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [get_language_support_override](class_fontfile.md#class-fontfile-method-get-language-support-override)(language: [String](class_string.md#class-string)) const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [get_language_support_overrides](class_fontfile.md#class-fontfile-method-get-language-support-overrides)() const |
| [bool](class_bool.md#class-bool) | [get_script_support_override](class_fontfile.md#class-fontfile-method-get-script-support-override)(script: [String](class_string.md#class-string)) const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [get_script_support_overrides](class_fontfile.md#class-fontfile-method-get-script-support-overrides)() const |
| [Array](class_array.md#class-array)[[Vector2i](class_vector2i.md#class-vector2i)] | [get_size_cache_list](class_fontfile.md#class-fontfile-method-get-size-cache-list)(cache_index: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_texture_count](class_fontfile.md#class-fontfile-method-get-texture-count)(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i)) const |
| [Image](class_image.md#class-image) | [get_texture_image](class_fontfile.md#class-fontfile-method-get-texture-image)(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int)) const |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array) | [get_texture_offsets](class_fontfile.md#class-fontfile-method-get-texture-offsets)(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int)) const |
| [Transform2D](class_transform2d.md#class-transform2d) | [get_transform](class_fontfile.md#class-fontfile-method-get-transform)(cache_index: [int](class_int.md#class-int)) const |
| [Dictionary](class_dictionary.md#class-dictionary) | [get_variation_coordinates](class_fontfile.md#class-fontfile-method-get-variation-coordinates)(cache_index: [int](class_int.md#class-int)) const |
| [Error](class_@globalscope.md#enum-globalscope-error) | [load_bitmap_font](class_fontfile.md#class-fontfile-method-load-bitmap-font)(path: [String](class_string.md#class-string)) |
| [Error](class_@globalscope.md#enum-globalscope-error) | [load_dynamic_font](class_fontfile.md#class-fontfile-method-load-dynamic-font)(path: [String](class_string.md#class-string)) |
| void | [remove_cache](class_fontfile.md#class-fontfile-method-remove-cache)(cache_index: [int](class_int.md#class-int)) |
| void | [remove_glyph](class_fontfile.md#class-fontfile-method-remove-glyph)(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int)) |
| void | [remove_kerning](class_fontfile.md#class-fontfile-method-remove-kerning)(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int), glyph_pair: [Vector2i](class_vector2i.md#class-vector2i)) |
| void | [remove_language_support_override](class_fontfile.md#class-fontfile-method-remove-language-support-override)(language: [String](class_string.md#class-string)) |
| void | [remove_script_support_override](class_fontfile.md#class-fontfile-method-remove-script-support-override)(script: [String](class_string.md#class-string)) |
| void | [remove_size_cache](class_fontfile.md#class-fontfile-method-remove-size-cache)(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i)) |
| void | [remove_texture](class_fontfile.md#class-fontfile-method-remove-texture)(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int)) |
| void | [render_glyph](class_fontfile.md#class-fontfile-method-render-glyph)(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), index: [int](class_int.md#class-int)) |
| void | [render_range](class_fontfile.md#class-fontfile-method-render-range)(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), start: [int](class_int.md#class-int), end: [int](class_int.md#class-int)) |
| void | [set_cache_ascent](class_fontfile.md#class-fontfile-method-set-cache-ascent)(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int), ascent: [float](class_float.md#class-float)) |
| void | [set_cache_descent](class_fontfile.md#class-fontfile-method-set-cache-descent)(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int), descent: [float](class_float.md#class-float)) |
| void | [set_cache_scale](class_fontfile.md#class-fontfile-method-set-cache-scale)(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int), scale: [float](class_float.md#class-float)) |
| void | [set_cache_underline_position](class_fontfile.md#class-fontfile-method-set-cache-underline-position)(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int), underline_position: [float](class_float.md#class-float)) |
| void | [set_cache_underline_thickness](class_fontfile.md#class-fontfile-method-set-cache-underline-thickness)(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int), underline_thickness: [float](class_float.md#class-float)) |
| void | [set_embolden](class_fontfile.md#class-fontfile-method-set-embolden)(cache_index: [int](class_int.md#class-int), strength: [float](class_float.md#class-float)) |
| void | [set_extra_baseline_offset](class_fontfile.md#class-fontfile-method-set-extra-baseline-offset)(cache_index: [int](class_int.md#class-int), baseline_offset: [float](class_float.md#class-float)) |
| void | [set_extra_spacing](class_fontfile.md#class-fontfile-method-set-extra-spacing)(cache_index: [int](class_int.md#class-int), spacing: [SpacingType](class_textserver.md#enum-textserver-spacingtype), value: [int](class_int.md#class-int)) |
| void | [set_face_index](class_fontfile.md#class-fontfile-method-set-face-index)(cache_index: [int](class_int.md#class-int), face_index: [int](class_int.md#class-int)) |
| void | [set_glyph_advance](class_fontfile.md#class-fontfile-method-set-glyph-advance)(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int), glyph: [int](class_int.md#class-int), advance: [Vector2](class_vector2.md#class-vector2)) |
| void | [set_glyph_offset](class_fontfile.md#class-fontfile-method-set-glyph-offset)(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int), offset: [Vector2](class_vector2.md#class-vector2)) |
| void | [set_glyph_size](class_fontfile.md#class-fontfile-method-set-glyph-size)(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int), gl_size: [Vector2](class_vector2.md#class-vector2)) |
| void | [set_glyph_texture_idx](class_fontfile.md#class-fontfile-method-set-glyph-texture-idx)(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int), texture_idx: [int](class_int.md#class-int)) |
| void | [set_glyph_uv_rect](class_fontfile.md#class-fontfile-method-set-glyph-uv-rect)(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int), uv_rect: [Rect2](class_rect2.md#class-rect2)) |
| void | [set_kerning](class_fontfile.md#class-fontfile-method-set-kerning)(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int), glyph_pair: [Vector2i](class_vector2i.md#class-vector2i), kerning: [Vector2](class_vector2.md#class-vector2)) |
| void | [set_language_support_override](class_fontfile.md#class-fontfile-method-set-language-support-override)(language: [String](class_string.md#class-string), supported: [bool](class_bool.md#class-bool)) |
| void | [set_script_support_override](class_fontfile.md#class-fontfile-method-set-script-support-override)(script: [String](class_string.md#class-string), supported: [bool](class_bool.md#class-bool)) |
| void | [set_texture_image](class_fontfile.md#class-fontfile-method-set-texture-image)(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int), image: [Image](class_image.md#class-image)) |
| void | [set_texture_offsets](class_fontfile.md#class-fontfile-method-set-texture-offsets)(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int), offset: [PackedInt32Array](class_packedint32array.md#class-packedint32array)) |
| void | [set_transform](class_fontfile.md#class-fontfile-method-set-transform)(cache_index: [int](class_int.md#class-int), transform: [Transform2D](class_transform2d.md#class-transform2d)) |
| void | [set_variation_coordinates](class_fontfile.md#class-fontfile-method-set-variation-coordinates)(cache_index: [int](class_int.md#class-int), variation_coordinates: [Dictionary](class_dictionary.md#class-dictionary)) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-fontfile-property-allow-system-fallback"></a>

[bool](class_bool.md#class-bool) **allow_system_fallback** = `true` [🔗](class_fontfile.md#class-fontfile-property-allow-system-fallback)

- void **set_allow_system_fallback**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_allow_system_fallback**()

If set to `true`, system fonts can be automatically used as fallbacks.

---


<a id="class-fontfile-property-antialiasing"></a>

[FontAntialiasing](class_textserver.md#enum-textserver-fontantialiasing) **antialiasing** = `1` [🔗](class_fontfile.md#class-fontfile-property-antialiasing)

- void **set_antialiasing**(value: [FontAntialiasing](class_textserver.md#enum-textserver-fontantialiasing))
- [FontAntialiasing](class_textserver.md#enum-textserver-fontantialiasing) **get_antialiasing**()

Font anti-aliasing mode.

---


<a id="class-fontfile-property-data"></a>

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **data** = `PackedByteArray()` [🔗](class_fontfile.md#class-fontfile-property-data)

- void **set_data**(value: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))
- [PackedByteArray](class_packedbytearray.md#class-packedbytearray) **get_data**()

Contents of the dynamic font source file.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray](class_packedbytearray.md#class-packedbytearray) for more details.

---


<a id="class-fontfile-property-disable-embedded-bitmaps"></a>

[bool](class_bool.md#class-bool) **disable_embedded_bitmaps** = `true` [🔗](class_fontfile.md#class-fontfile-property-disable-embedded-bitmaps)

- void **set_disable_embedded_bitmaps**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_disable_embedded_bitmaps**()

If set to `true`, embedded font bitmap loading is disabled (bitmap-only and color fonts ignore this property).

---


<a id="class-fontfile-property-fixed-size"></a>

[int](class_int.md#class-int) **fixed_size** = `0` [🔗](class_fontfile.md#class-fontfile-property-fixed-size)

- void **set_fixed_size**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_fixed_size**()

Font size, used only for the bitmap fonts.

---


<a id="class-fontfile-property-fixed-size-scale-mode"></a>

[FixedSizeScaleMode](class_textserver.md#enum-textserver-fixedsizescalemode) **fixed_size_scale_mode** = `0` [🔗](class_fontfile.md#class-fontfile-property-fixed-size-scale-mode)

- void **set_fixed_size_scale_mode**(value: [FixedSizeScaleMode](class_textserver.md#enum-textserver-fixedsizescalemode))
- [FixedSizeScaleMode](class_textserver.md#enum-textserver-fixedsizescalemode) **get_fixed_size_scale_mode**()

Scaling mode, used only for the bitmap fonts with [fixed_size](class_fontfile.md#class-fontfile-property-fixed-size) greater than zero.

---


<a id="class-fontfile-property-font-name"></a>

[String](class_string.md#class-string) **font_name** = `""` [🔗](class_fontfile.md#class-fontfile-property-font-name)

- void **set_font_name**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_font_name**()

Font family name.

---


<a id="class-fontfile-property-font-stretch"></a>

[int](class_int.md#class-int) **font_stretch** = `100` [🔗](class_fontfile.md#class-fontfile-property-font-stretch)

- void **set_font_stretch**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_font_stretch**()

Font stretch amount, compared to a normal width. A percentage value between `50%` and `200%`.

---


<a id="class-fontfile-property-font-style"></a>

BitField[[FontStyle](class_textserver.md#enum-textserver-fontstyle)] **font_style** = `0` [🔗](class_fontfile.md#class-fontfile-property-font-style)

- void **set_font_style**(value: BitField[[FontStyle](class_textserver.md#enum-textserver-fontstyle)])
- BitField[[FontStyle](class_textserver.md#enum-textserver-fontstyle)] **get_font_style**()

Font style flags.

---


<a id="class-fontfile-property-font-weight"></a>

[int](class_int.md#class-int) **font_weight** = `400` [🔗](class_fontfile.md#class-fontfile-property-font-weight)

- void **set_font_weight**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_font_weight**()

Weight (boldness) of the font. A value in the `100...999` range, normal font weight is `400`, bold font weight is `700`.

---


<a id="class-fontfile-property-force-autohinter"></a>

[bool](class_bool.md#class-bool) **force_autohinter** = `false` [🔗](class_fontfile.md#class-fontfile-property-force-autohinter)

- void **set_force_autohinter**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_force_autohinter**()

If set to `true`, auto-hinting is supported and preferred over font built-in hinting. Used by dynamic fonts only (MSDF fonts don't support hinting).

---


<a id="class-fontfile-property-generate-mipmaps"></a>

[bool](class_bool.md#class-bool) **generate_mipmaps** = `false` [🔗](class_fontfile.md#class-fontfile-property-generate-mipmaps)

- void **set_generate_mipmaps**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_generate_mipmaps**()

If set to `true`, generate mipmaps for the font textures.

---


<a id="class-fontfile-property-hinting"></a>

[Hinting](class_textserver.md#enum-textserver-hinting) **hinting** = `1` [🔗](class_fontfile.md#class-fontfile-property-hinting)

- void **set_hinting**(value: [Hinting](class_textserver.md#enum-textserver-hinting))
- [Hinting](class_textserver.md#enum-textserver-hinting) **get_hinting**()

Font hinting mode. Used by dynamic fonts only.

---


<a id="class-fontfile-property-keep-rounding-remainders"></a>

[bool](class_bool.md#class-bool) **keep_rounding_remainders** = `true` [🔗](class_fontfile.md#class-fontfile-property-keep-rounding-remainders)

- void **set_keep_rounding_remainders**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_keep_rounding_remainders**()

If set to `true`, when aligning glyphs to the pixel boundaries rounding remainders are accumulated to ensure more uniform glyph distribution. This setting has no effect if subpixel positioning is enabled.

---


<a id="class-fontfile-property-modulate-color-glyphs"></a>

[bool](class_bool.md#class-bool) **modulate_color_glyphs** = `false` [🔗](class_fontfile.md#class-fontfile-property-modulate-color-glyphs)

- void **set_modulate_color_glyphs**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_modulate_color_glyphs**()

If set to `true`, color modulation is applied when drawing colored glyphs, otherwise it's applied to the monochrome glyphs only.

---


<a id="class-fontfile-property-msdf-pixel-range"></a>

[int](class_int.md#class-int) **msdf_pixel_range** = `16` [🔗](class_fontfile.md#class-fontfile-property-msdf-pixel-range)

- void **set_msdf_pixel_range**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_msdf_pixel_range**()

The width of the range around the shape between the minimum and maximum representable signed distance. If using font outlines, [msdf_pixel_range](class_fontfile.md#class-fontfile-property-msdf-pixel-range) must be set to at least *twice* the size of the largest font outline. The default [msdf_pixel_range](class_fontfile.md#class-fontfile-property-msdf-pixel-range) value of `16` allows outline sizes up to `8` to look correct.

---


<a id="class-fontfile-property-msdf-size"></a>

[int](class_int.md#class-int) **msdf_size** = `48` [🔗](class_fontfile.md#class-fontfile-property-msdf-size)

- void **set_msdf_size**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_msdf_size**()

Source font size used to generate MSDF textures. Higher values allow for more precision, but are slower to render and require more memory. Only increase this value if you notice a visible lack of precision in glyph rendering.

---


<a id="class-fontfile-property-multichannel-signed-distance-field"></a>

[bool](class_bool.md#class-bool) **multichannel_signed_distance_field** = `false` [🔗](class_fontfile.md#class-fontfile-property-multichannel-signed-distance-field)

- void **set_multichannel_signed_distance_field**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_multichannel_signed_distance_field**()

If set to `true`, glyphs of all sizes are rendered using single multichannel signed distance field (MSDF) generated from the dynamic font vector data. Since this approach does not rely on rasterizing the font every time its size changes, this allows for resizing the font in real-time without any performance penalty. Text will also not look grainy for [Control](class_control.md#class-control)s that are scaled down (or for [Label3D](class_label3d.md#class-label3d)s viewed from a long distance). As a downside, font hinting is not available with MSDF. The lack of font hinting may result in less crisp and less readable fonts at small sizes.

**Note:** If using font outlines, [msdf_pixel_range](class_fontfile.md#class-fontfile-property-msdf-pixel-range) must be set to at least *twice* the size of the largest font outline.

**Note:** MSDF font rendering does not render glyphs with overlapping shapes correctly. Overlapping shapes are not valid per the OpenType standard, but are still commonly found in many font files, especially those converted by Google Fonts. To avoid issues with overlapping glyphs, consider downloading the font file directly from the type foundry instead of relying on Google Fonts.

---


<a id="class-fontfile-property-opentype-feature-overrides"></a>

[Dictionary](class_dictionary.md#class-dictionary) **opentype_feature_overrides** = `{}` [🔗](class_fontfile.md#class-fontfile-property-opentype-feature-overrides)

- void **set_opentype_feature_overrides**(value: [Dictionary](class_dictionary.md#class-dictionary))
- [Dictionary](class_dictionary.md#class-dictionary) **get_opentype_feature_overrides**()

Font OpenType feature set override.

---


<a id="class-fontfile-property-oversampling"></a>

[float](class_float.md#class-float) **oversampling** = `0.0` [🔗](class_fontfile.md#class-fontfile-property-oversampling)

- void **set_oversampling**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_oversampling**()

If set to a positive value, overrides the oversampling factor of the viewport this font is used in. See [Viewport.oversampling](class_viewport.md#class-viewport-property-oversampling). This value doesn't override the `oversampling` parameter of `draw_*` methods.

---


<a id="class-fontfile-property-style-name"></a>

[String](class_string.md#class-string) **style_name** = `""` [🔗](class_fontfile.md#class-fontfile-property-style-name)

- void **set_font_style_name**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_font_style_name**()

Font style name.

---


<a id="class-fontfile-property-subpixel-positioning"></a>

[SubpixelPositioning](class_textserver.md#enum-textserver-subpixelpositioning) **subpixel_positioning** = `1` [🔗](class_fontfile.md#class-fontfile-property-subpixel-positioning)

- void **set_subpixel_positioning**(value: [SubpixelPositioning](class_textserver.md#enum-textserver-subpixelpositioning))
- [SubpixelPositioning](class_textserver.md#enum-textserver-subpixelpositioning) **get_subpixel_positioning**()

Font glyph subpixel positioning mode. Subpixel positioning provides shaper text and better kerning for smaller font sizes, at the cost of higher memory usage and lower font rasterization speed. Use [TextServer.SUBPIXEL_POSITIONING_AUTO](class_textserver.md#class-textserver-constant-subpixel-positioning-auto) to automatically enable it based on the font size.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-fontfile-method-clear-cache"></a>

void **clear_cache**() [🔗](class_fontfile.md#class-fontfile-method-clear-cache)

Removes all font cache entries.

---


<a id="class-fontfile-method-clear-glyphs"></a>

void **clear_glyphs**(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i)) [🔗](class_fontfile.md#class-fontfile-method-clear-glyphs)

Removes all rendered glyph information from the cache entry.

**Note:** This function will not remove textures associated with the glyphs, use [remove_texture()](class_fontfile.md#class-fontfile-method-remove-texture) to remove them manually.

---


<a id="class-fontfile-method-clear-kerning-map"></a>

void **clear_kerning_map**(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int)) [🔗](class_fontfile.md#class-fontfile-method-clear-kerning-map)

Removes all kerning overrides.

---


<a id="class-fontfile-method-clear-size-cache"></a>

void **clear_size_cache**(cache_index: [int](class_int.md#class-int)) [🔗](class_fontfile.md#class-fontfile-method-clear-size-cache)

Removes all font sizes from the cache entry.

---


<a id="class-fontfile-method-clear-textures"></a>

void **clear_textures**(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i)) [🔗](class_fontfile.md#class-fontfile-method-clear-textures)

Removes all textures from font cache entry.

**Note:** This function will not remove glyphs associated with the texture, use [remove_glyph()](class_fontfile.md#class-fontfile-method-remove-glyph) to remove them manually.

---


<a id="class-fontfile-method-get-cache-ascent"></a>

[float](class_float.md#class-float) **get_cache_ascent**(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int)) const [🔗](class_fontfile.md#class-fontfile-method-get-cache-ascent)

Returns the font ascent (number of pixels above the baseline).

---


<a id="class-fontfile-method-get-cache-count"></a>

[int](class_int.md#class-int) **get_cache_count**() const [🔗](class_fontfile.md#class-fontfile-method-get-cache-count)

Returns number of the font cache entries.

---


<a id="class-fontfile-method-get-cache-descent"></a>

[float](class_float.md#class-float) **get_cache_descent**(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int)) const [🔗](class_fontfile.md#class-fontfile-method-get-cache-descent)

Returns the font descent (number of pixels below the baseline).

---


<a id="class-fontfile-method-get-cache-scale"></a>

[float](class_float.md#class-float) **get_cache_scale**(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int)) const [🔗](class_fontfile.md#class-fontfile-method-get-cache-scale)

Returns scaling factor of the color bitmap font.

---


<a id="class-fontfile-method-get-cache-underline-position"></a>

[float](class_float.md#class-float) **get_cache_underline_position**(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int)) const [🔗](class_fontfile.md#class-fontfile-method-get-cache-underline-position)

Returns pixel offset of the underline below the baseline.

---


<a id="class-fontfile-method-get-cache-underline-thickness"></a>

[float](class_float.md#class-float) **get_cache_underline_thickness**(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int)) const [🔗](class_fontfile.md#class-fontfile-method-get-cache-underline-thickness)

Returns thickness of the underline in pixels.

---


<a id="class-fontfile-method-get-char-from-glyph-index"></a>

[int](class_int.md#class-int) **get_char_from_glyph_index**(size: [int](class_int.md#class-int), glyph_index: [int](class_int.md#class-int)) const [🔗](class_fontfile.md#class-fontfile-method-get-char-from-glyph-index)

Returns character code associated with `glyph_index`, or `0` if `glyph_index` is invalid. See [get_glyph_index()](class_fontfile.md#class-fontfile-method-get-glyph-index).

---


<a id="class-fontfile-method-get-embolden"></a>

[float](class_float.md#class-float) **get_embolden**(cache_index: [int](class_int.md#class-int)) const [🔗](class_fontfile.md#class-fontfile-method-get-embolden)

Returns embolden strength, if is not equal to zero, emboldens the font outlines. Negative values reduce the outline thickness.

---


<a id="class-fontfile-method-get-extra-baseline-offset"></a>

[float](class_float.md#class-float) **get_extra_baseline_offset**(cache_index: [int](class_int.md#class-int)) const [🔗](class_fontfile.md#class-fontfile-method-get-extra-baseline-offset)

Returns extra baseline offset (as a fraction of font height).

---


<a id="class-fontfile-method-get-extra-spacing"></a>

[int](class_int.md#class-int) **get_extra_spacing**(cache_index: [int](class_int.md#class-int), spacing: [SpacingType](class_textserver.md#enum-textserver-spacingtype)) const [🔗](class_fontfile.md#class-fontfile-method-get-extra-spacing)

Returns spacing for `spacing` in pixels (not relative to the font size).

---


<a id="class-fontfile-method-get-face-index"></a>

[int](class_int.md#class-int) **get_face_index**(cache_index: [int](class_int.md#class-int)) const [🔗](class_fontfile.md#class-fontfile-method-get-face-index)

Returns an active face index in the TrueType / OpenType collection.

---


<a id="class-fontfile-method-get-glyph-advance"></a>

[Vector2](class_vector2.md#class-vector2) **get_glyph_advance**(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int), glyph: [int](class_int.md#class-int)) const [🔗](class_fontfile.md#class-fontfile-method-get-glyph-advance)

Returns glyph advance (offset of the next glyph).

**Note:** Advance for glyphs outlines is the same as the base glyph advance and is not saved.

---


<a id="class-fontfile-method-get-glyph-index"></a>

[int](class_int.md#class-int) **get_glyph_index**(size: [int](class_int.md#class-int), char: [int](class_int.md#class-int), variation_selector: [int](class_int.md#class-int)) const [🔗](class_fontfile.md#class-fontfile-method-get-glyph-index)

Returns the glyph index of a `char`, optionally modified by the `variation_selector`.

---


<a id="class-fontfile-method-get-glyph-list"></a>

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_glyph_list**(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i)) const [🔗](class_fontfile.md#class-fontfile-method-get-glyph-list)

Returns list of rendered glyphs in the cache entry.

---


<a id="class-fontfile-method-get-glyph-offset"></a>

[Vector2](class_vector2.md#class-vector2) **get_glyph_offset**(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int)) const [🔗](class_fontfile.md#class-fontfile-method-get-glyph-offset)

Returns glyph offset from the baseline.

---


<a id="class-fontfile-method-get-glyph-size"></a>

[Vector2](class_vector2.md#class-vector2) **get_glyph_size**(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int)) const [🔗](class_fontfile.md#class-fontfile-method-get-glyph-size)

Returns glyph size.

---


<a id="class-fontfile-method-get-glyph-texture-idx"></a>

[int](class_int.md#class-int) **get_glyph_texture_idx**(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int)) const [🔗](class_fontfile.md#class-fontfile-method-get-glyph-texture-idx)

Returns index of the cache texture containing the glyph.

---


<a id="class-fontfile-method-get-glyph-uv-rect"></a>

[Rect2](class_rect2.md#class-rect2) **get_glyph_uv_rect**(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int)) const [🔗](class_fontfile.md#class-fontfile-method-get-glyph-uv-rect)

Returns rectangle in the cache texture containing the glyph.

---


<a id="class-fontfile-method-get-kerning"></a>

[Vector2](class_vector2.md#class-vector2) **get_kerning**(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int), glyph_pair: [Vector2i](class_vector2i.md#class-vector2i)) const [🔗](class_fontfile.md#class-fontfile-method-get-kerning)

Returns kerning for the pair of glyphs.

---


<a id="class-fontfile-method-get-kerning-list"></a>

[Array](class_array.md#class-array)[[Vector2i](class_vector2i.md#class-vector2i)] **get_kerning_list**(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int)) const [🔗](class_fontfile.md#class-fontfile-method-get-kerning-list)

Returns list of the kerning overrides.

---


<a id="class-fontfile-method-get-language-support-override"></a>

[bool](class_bool.md#class-bool) **get_language_support_override**(language: [String](class_string.md#class-string)) const [🔗](class_fontfile.md#class-fontfile-method-get-language-support-override)

Returns `true` if support override is enabled for the `language`.

---


<a id="class-fontfile-method-get-language-support-overrides"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_language_support_overrides**() const [🔗](class_fontfile.md#class-fontfile-method-get-language-support-overrides)

Returns list of language support overrides.

---


<a id="class-fontfile-method-get-script-support-override"></a>

[bool](class_bool.md#class-bool) **get_script_support_override**(script: [String](class_string.md#class-string)) const [🔗](class_fontfile.md#class-fontfile-method-get-script-support-override)

Returns `true` if support override is enabled for the `script`.

---


<a id="class-fontfile-method-get-script-support-overrides"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_script_support_overrides**() const [🔗](class_fontfile.md#class-fontfile-method-get-script-support-overrides)

Returns list of script support overrides.

---


<a id="class-fontfile-method-get-size-cache-list"></a>

[Array](class_array.md#class-array)[[Vector2i](class_vector2i.md#class-vector2i)] **get_size_cache_list**(cache_index: [int](class_int.md#class-int)) const [🔗](class_fontfile.md#class-fontfile-method-get-size-cache-list)

Returns list of the font sizes in the cache. Each size is [Vector2i](class_vector2i.md#class-vector2i) with font size and outline size.

---


<a id="class-fontfile-method-get-texture-count"></a>

[int](class_int.md#class-int) **get_texture_count**(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i)) const [🔗](class_fontfile.md#class-fontfile-method-get-texture-count)

Returns number of textures used by font cache entry.

---


<a id="class-fontfile-method-get-texture-image"></a>

[Image](class_image.md#class-image) **get_texture_image**(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int)) const [🔗](class_fontfile.md#class-fontfile-method-get-texture-image)

Returns a copy of the font cache texture image.

---


<a id="class-fontfile-method-get-texture-offsets"></a>

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_texture_offsets**(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int)) const [🔗](class_fontfile.md#class-fontfile-method-get-texture-offsets)

Returns a copy of the array containing glyph packing data.

---


<a id="class-fontfile-method-get-transform"></a>

[Transform2D](class_transform2d.md#class-transform2d) **get_transform**(cache_index: [int](class_int.md#class-int)) const [🔗](class_fontfile.md#class-fontfile-method-get-transform)

Returns 2D transform, applied to the font outlines, can be used for slanting, flipping and rotating glyphs.

---


<a id="class-fontfile-method-get-variation-coordinates"></a>

[Dictionary](class_dictionary.md#class-dictionary) **get_variation_coordinates**(cache_index: [int](class_int.md#class-int)) const [🔗](class_fontfile.md#class-fontfile-method-get-variation-coordinates)

Returns variation coordinates for the specified font cache entry. See [Font.get_supported_variation_list()](class_font.md#class-font-method-get-supported-variation-list) for more info.

---


<a id="class-fontfile-method-load-bitmap-font"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **load_bitmap_font**(path: [String](class_string.md#class-string)) [🔗](class_fontfile.md#class-fontfile-method-load-bitmap-font)

Loads an AngelCode BMFont (.fnt, .font) bitmap font from file `path`.

**Warning:** This method should only be used in the editor or in cases when you need to load external fonts at run-time, such as fonts located at the `user://` directory.

---


<a id="class-fontfile-method-load-dynamic-font"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **load_dynamic_font**(path: [String](class_string.md#class-string)) [🔗](class_fontfile.md#class-fontfile-method-load-dynamic-font)

Loads a TrueType (.ttf), OpenType (.otf), WOFF (.woff), WOFF2 (.woff2) or Type 1 (.pfb, .pfm) dynamic font from file `path`.

**Warning:** This method should only be used in the editor or in cases when you need to load external fonts at run-time, such as fonts located at the `user://` directory.

---


<a id="class-fontfile-method-remove-cache"></a>

void **remove_cache**(cache_index: [int](class_int.md#class-int)) [🔗](class_fontfile.md#class-fontfile-method-remove-cache)

Removes specified font cache entry.

---


<a id="class-fontfile-method-remove-glyph"></a>

void **remove_glyph**(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int)) [🔗](class_fontfile.md#class-fontfile-method-remove-glyph)

Removes specified rendered glyph information from the cache entry.

**Note:** This function will not remove textures associated with the glyphs, use [remove_texture()](class_fontfile.md#class-fontfile-method-remove-texture) to remove them manually.

---


<a id="class-fontfile-method-remove-kerning"></a>

void **remove_kerning**(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int), glyph_pair: [Vector2i](class_vector2i.md#class-vector2i)) [🔗](class_fontfile.md#class-fontfile-method-remove-kerning)

Removes kerning override for the pair of glyphs.

---


<a id="class-fontfile-method-remove-language-support-override"></a>

void **remove_language_support_override**(language: [String](class_string.md#class-string)) [🔗](class_fontfile.md#class-fontfile-method-remove-language-support-override)

Remove language support override.

---


<a id="class-fontfile-method-remove-script-support-override"></a>

void **remove_script_support_override**(script: [String](class_string.md#class-string)) [🔗](class_fontfile.md#class-fontfile-method-remove-script-support-override)

Removes script support override.

---


<a id="class-fontfile-method-remove-size-cache"></a>

void **remove_size_cache**(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i)) [🔗](class_fontfile.md#class-fontfile-method-remove-size-cache)

Removes specified font size from the cache entry.

---


<a id="class-fontfile-method-remove-texture"></a>

void **remove_texture**(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int)) [🔗](class_fontfile.md#class-fontfile-method-remove-texture)

Removes specified texture from the cache entry.

**Note:** This function will not remove glyphs associated with the texture. Remove them manually using [remove_glyph()](class_fontfile.md#class-fontfile-method-remove-glyph).

---


<a id="class-fontfile-method-render-glyph"></a>

void **render_glyph**(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), index: [int](class_int.md#class-int)) [🔗](class_fontfile.md#class-fontfile-method-render-glyph)

Renders specified glyph to the font cache texture.

---


<a id="class-fontfile-method-render-range"></a>

void **render_range**(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), start: [int](class_int.md#class-int), end: [int](class_int.md#class-int)) [🔗](class_fontfile.md#class-fontfile-method-render-range)

Renders the range of characters to the font cache texture.

---


<a id="class-fontfile-method-set-cache-ascent"></a>

void **set_cache_ascent**(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int), ascent: [float](class_float.md#class-float)) [🔗](class_fontfile.md#class-fontfile-method-set-cache-ascent)

Sets the font ascent (number of pixels above the baseline).

---


<a id="class-fontfile-method-set-cache-descent"></a>

void **set_cache_descent**(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int), descent: [float](class_float.md#class-float)) [🔗](class_fontfile.md#class-fontfile-method-set-cache-descent)

Sets the font descent (number of pixels below the baseline).

---


<a id="class-fontfile-method-set-cache-scale"></a>

void **set_cache_scale**(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int), scale: [float](class_float.md#class-float)) [🔗](class_fontfile.md#class-fontfile-method-set-cache-scale)

Sets scaling factor of the color bitmap font.

---


<a id="class-fontfile-method-set-cache-underline-position"></a>

void **set_cache_underline_position**(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int), underline_position: [float](class_float.md#class-float)) [🔗](class_fontfile.md#class-fontfile-method-set-cache-underline-position)

Sets pixel offset of the underline below the baseline.

---


<a id="class-fontfile-method-set-cache-underline-thickness"></a>

void **set_cache_underline_thickness**(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int), underline_thickness: [float](class_float.md#class-float)) [🔗](class_fontfile.md#class-fontfile-method-set-cache-underline-thickness)

Sets thickness of the underline in pixels.

---


<a id="class-fontfile-method-set-embolden"></a>

void **set_embolden**(cache_index: [int](class_int.md#class-int), strength: [float](class_float.md#class-float)) [🔗](class_fontfile.md#class-fontfile-method-set-embolden)

Sets embolden strength, if is not equal to zero, emboldens the font outlines. Negative values reduce the outline thickness.

---


<a id="class-fontfile-method-set-extra-baseline-offset"></a>

void **set_extra_baseline_offset**(cache_index: [int](class_int.md#class-int), baseline_offset: [float](class_float.md#class-float)) [🔗](class_fontfile.md#class-fontfile-method-set-extra-baseline-offset)

Sets extra baseline offset (as a fraction of font height).

---


<a id="class-fontfile-method-set-extra-spacing"></a>

void **set_extra_spacing**(cache_index: [int](class_int.md#class-int), spacing: [SpacingType](class_textserver.md#enum-textserver-spacingtype), value: [int](class_int.md#class-int)) [🔗](class_fontfile.md#class-fontfile-method-set-extra-spacing)

Sets the spacing for `spacing` to `value` in pixels (not relative to the font size).

---


<a id="class-fontfile-method-set-face-index"></a>

void **set_face_index**(cache_index: [int](class_int.md#class-int), face_index: [int](class_int.md#class-int)) [🔗](class_fontfile.md#class-fontfile-method-set-face-index)

Sets an active face index in the TrueType / OpenType collection.

---


<a id="class-fontfile-method-set-glyph-advance"></a>

void **set_glyph_advance**(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int), glyph: [int](class_int.md#class-int), advance: [Vector2](class_vector2.md#class-vector2)) [🔗](class_fontfile.md#class-fontfile-method-set-glyph-advance)

Sets glyph advance (offset of the next glyph).

**Note:** Advance for glyphs outlines is the same as the base glyph advance and is not saved.

---


<a id="class-fontfile-method-set-glyph-offset"></a>

void **set_glyph_offset**(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int), offset: [Vector2](class_vector2.md#class-vector2)) [🔗](class_fontfile.md#class-fontfile-method-set-glyph-offset)

Sets glyph offset from the baseline.

---


<a id="class-fontfile-method-set-glyph-size"></a>

void **set_glyph_size**(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int), gl_size: [Vector2](class_vector2.md#class-vector2)) [🔗](class_fontfile.md#class-fontfile-method-set-glyph-size)

Sets glyph size.

---


<a id="class-fontfile-method-set-glyph-texture-idx"></a>

void **set_glyph_texture_idx**(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int), texture_idx: [int](class_int.md#class-int)) [🔗](class_fontfile.md#class-fontfile-method-set-glyph-texture-idx)

Sets index of the cache texture containing the glyph.

---


<a id="class-fontfile-method-set-glyph-uv-rect"></a>

void **set_glyph_uv_rect**(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int), uv_rect: [Rect2](class_rect2.md#class-rect2)) [🔗](class_fontfile.md#class-fontfile-method-set-glyph-uv-rect)

Sets rectangle in the cache texture containing the glyph.

---


<a id="class-fontfile-method-set-kerning"></a>

void **set_kerning**(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int), glyph_pair: [Vector2i](class_vector2i.md#class-vector2i), kerning: [Vector2](class_vector2.md#class-vector2)) [🔗](class_fontfile.md#class-fontfile-method-set-kerning)

Sets kerning for the pair of glyphs.

---


<a id="class-fontfile-method-set-language-support-override"></a>

void **set_language_support_override**(language: [String](class_string.md#class-string), supported: [bool](class_bool.md#class-bool)) [🔗](class_fontfile.md#class-fontfile-method-set-language-support-override)

Adds override for [Font.is_language_supported()](class_font.md#class-font-method-is-language-supported).

---


<a id="class-fontfile-method-set-script-support-override"></a>

void **set_script_support_override**(script: [String](class_string.md#class-string), supported: [bool](class_bool.md#class-bool)) [🔗](class_fontfile.md#class-fontfile-method-set-script-support-override)

Adds override for [Font.is_script_supported()](class_font.md#class-font-method-is-script-supported).

---


<a id="class-fontfile-method-set-texture-image"></a>

void **set_texture_image**(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int), image: [Image](class_image.md#class-image)) [🔗](class_fontfile.md#class-fontfile-method-set-texture-image)

Sets font cache texture image.

---


<a id="class-fontfile-method-set-texture-offsets"></a>

void **set_texture_offsets**(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int), offset: [PackedInt32Array](class_packedint32array.md#class-packedint32array)) [🔗](class_fontfile.md#class-fontfile-method-set-texture-offsets)

Sets array containing glyph packing data.

---


<a id="class-fontfile-method-set-transform"></a>

void **set_transform**(cache_index: [int](class_int.md#class-int), transform: [Transform2D](class_transform2d.md#class-transform2d)) [🔗](class_fontfile.md#class-fontfile-method-set-transform)

Sets 2D transform, applied to the font outlines, can be used for slanting, flipping, and rotating glyphs.

---


<a id="class-fontfile-method-set-variation-coordinates"></a>

void **set_variation_coordinates**(cache_index: [int](class_int.md#class-int), variation_coordinates: [Dictionary](class_dictionary.md#class-dictionary)) [🔗](class_fontfile.md#class-fontfile-method-set-variation-coordinates)

Sets variation coordinates for the specified font cache entry. See [Font.get_supported_variation_list()](class_font.md#class-font-method-get-supported-variation-list) for more info.
