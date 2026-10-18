> Source: https://docs.godotengine.org/en/4.7/classes/class_textserverextension.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="textserverextension"></a>

<a id="class-textserverextension"></a>

# TextServerExtension

**Inherits:** [TextServer](class_textserver.md#class-textserver) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [TextServerAdvanced](class_textserveradvanced.md#class-textserveradvanced), [TextServerDummy](class_textserverdummy.md#class-textserverdummy), [TextServerFallback](class_textserverfallback.md#class-textserverfallback)

Base class for custom [TextServer](class_textserver.md#class-textserver) implementations (plugins).

<a id="description"></a>

## Description

External [TextServer](class_textserver.md#class-textserver) implementations should inherit from this class.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [_cleanup](class_textserverextension.md#class-textserverextension-private-method-cleanup)() virtual |
| [RID](class_rid.md#class-rid) | [_create_font](class_textserverextension.md#class-textserverextension-private-method-create-font)() virtual required |
| [RID](class_rid.md#class-rid) | [_create_font_linked_variation](class_textserverextension.md#class-textserverextension-private-method-create-font-linked-variation)(font_rid: [RID](class_rid.md#class-rid)) virtual |
| [RID](class_rid.md#class-rid) | [_create_shaped_text](class_textserverextension.md#class-textserverextension-private-method-create-shaped-text)(direction: [Direction](class_textserver.md#enum-textserver-direction), orientation: [Orientation](class_textserver.md#enum-textserver-orientation)) virtual required |
| void | [_draw_hex_code_box](class_textserverextension.md#class-textserverextension-private-method-draw-hex-code-box)(canvas: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), pos: [Vector2](class_vector2.md#class-vector2), index: [int](class_int.md#class-int), color: [Color](class_color.md#class-color)) virtual const |
| void | [_font_clear_glyphs](class_textserverextension.md#class-textserverextension-private-method-font-clear-glyphs)(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i)) virtual required |
| void | [_font_clear_kerning_map](class_textserverextension.md#class-textserverextension-private-method-font-clear-kerning-map)(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int)) virtual |
| void | [_font_clear_size_cache](class_textserverextension.md#class-textserverextension-private-method-font-clear-size-cache)(font_rid: [RID](class_rid.md#class-rid)) virtual required |
| void | [_font_clear_system_fallback_cache](class_textserverextension.md#class-textserverextension-private-method-font-clear-system-fallback-cache)() virtual |
| void | [_font_clear_textures](class_textserverextension.md#class-textserverextension-private-method-font-clear-textures)(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i)) virtual required |
| void | [_font_draw_glyph](class_textserverextension.md#class-textserverextension-private-method-font-draw-glyph)(font_rid: [RID](class_rid.md#class-rid), canvas: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), pos: [Vector2](class_vector2.md#class-vector2), index: [int](class_int.md#class-int), color: [Color](class_color.md#class-color), oversampling: [float](class_float.md#class-float)) virtual required const |
| void | [_font_draw_glyph_outline](class_textserverextension.md#class-textserverextension-private-method-font-draw-glyph-outline)(font_rid: [RID](class_rid.md#class-rid), canvas: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), outline_size: [int](class_int.md#class-int), pos: [Vector2](class_vector2.md#class-vector2), index: [int](class_int.md#class-int), color: [Color](class_color.md#class-color), oversampling: [float](class_float.md#class-float)) virtual required const |
| [FontAntialiasing](class_textserver.md#enum-textserver-fontantialiasing) | [_font_get_antialiasing](class_textserverextension.md#class-textserverextension-private-method-font-get-antialiasing)(font_rid: [RID](class_rid.md#class-rid)) virtual const |
| [float](class_float.md#class-float) | [_font_get_ascent](class_textserverextension.md#class-textserverextension-private-method-font-get-ascent)(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int)) virtual required const |
| [float](class_float.md#class-float) | [_font_get_baseline_offset](class_textserverextension.md#class-textserverextension-private-method-font-get-baseline-offset)(font_rid: [RID](class_rid.md#class-rid)) virtual const |
| [int](class_int.md#class-int) | [_font_get_char_from_glyph_index](class_textserverextension.md#class-textserverextension-private-method-font-get-char-from-glyph-index)(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), glyph_index: [int](class_int.md#class-int)) virtual required const |
| [float](class_float.md#class-float) | [_font_get_descent](class_textserverextension.md#class-textserverextension-private-method-font-get-descent)(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int)) virtual required const |
| [bool](class_bool.md#class-bool) | [_font_get_disable_embedded_bitmaps](class_textserverextension.md#class-textserverextension-private-method-font-get-disable-embedded-bitmaps)(font_rid: [RID](class_rid.md#class-rid)) virtual const |
| [float](class_float.md#class-float) | [_font_get_embolden](class_textserverextension.md#class-textserverextension-private-method-font-get-embolden)(font_rid: [RID](class_rid.md#class-rid)) virtual const |
| [int](class_int.md#class-int) | [_font_get_face_count](class_textserverextension.md#class-textserverextension-private-method-font-get-face-count)(font_rid: [RID](class_rid.md#class-rid)) virtual const |
| [int](class_int.md#class-int) | [_font_get_face_index](class_textserverextension.md#class-textserverextension-private-method-font-get-face-index)(font_rid: [RID](class_rid.md#class-rid)) virtual const |
| [int](class_int.md#class-int) | [_font_get_fixed_size](class_textserverextension.md#class-textserverextension-private-method-font-get-fixed-size)(font_rid: [RID](class_rid.md#class-rid)) virtual required const |
| [FixedSizeScaleMode](class_textserver.md#enum-textserver-fixedsizescalemode) | [_font_get_fixed_size_scale_mode](class_textserverextension.md#class-textserverextension-private-method-font-get-fixed-size-scale-mode)(font_rid: [RID](class_rid.md#class-rid)) virtual required const |
| [bool](class_bool.md#class-bool) | [_font_get_generate_mipmaps](class_textserverextension.md#class-textserverextension-private-method-font-get-generate-mipmaps)(font_rid: [RID](class_rid.md#class-rid)) virtual const |
| [float](class_float.md#class-float) | [_font_get_global_oversampling](class_textserverextension.md#class-textserverextension-private-method-font-get-global-oversampling)() virtual const |
| [Vector2](class_vector2.md#class-vector2) | [_font_get_glyph_advance](class_textserverextension.md#class-textserverextension-private-method-font-get-glyph-advance)(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), glyph: [int](class_int.md#class-int)) virtual required const |
| [Dictionary](class_dictionary.md#class-dictionary) | [_font_get_glyph_contours](class_textserverextension.md#class-textserverextension-private-method-font-get-glyph-contours)(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), index: [int](class_int.md#class-int)) virtual const |
| [int](class_int.md#class-int) | [_font_get_glyph_index](class_textserverextension.md#class-textserverextension-private-method-font-get-glyph-index)(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), char: [int](class_int.md#class-int), variation_selector: [int](class_int.md#class-int)) virtual required const |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array) | [_font_get_glyph_list](class_textserverextension.md#class-textserverextension-private-method-font-get-glyph-list)(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i)) virtual required const |
| [Vector2](class_vector2.md#class-vector2) | [_font_get_glyph_offset](class_textserverextension.md#class-textserverextension-private-method-font-get-glyph-offset)(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int)) virtual required const |
| [Vector2](class_vector2.md#class-vector2) | [_font_get_glyph_size](class_textserverextension.md#class-textserverextension-private-method-font-get-glyph-size)(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int)) virtual required const |
| [int](class_int.md#class-int) | [_font_get_glyph_texture_idx](class_textserverextension.md#class-textserverextension-private-method-font-get-glyph-texture-idx)(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int)) virtual required const |
| [RID](class_rid.md#class-rid) | [_font_get_glyph_texture_rid](class_textserverextension.md#class-textserverextension-private-method-font-get-glyph-texture-rid)(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int)) virtual required const |
| [Vector2](class_vector2.md#class-vector2) | [_font_get_glyph_texture_size](class_textserverextension.md#class-textserverextension-private-method-font-get-glyph-texture-size)(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int)) virtual required const |
| [Rect2](class_rect2.md#class-rect2) | [_font_get_glyph_uv_rect](class_textserverextension.md#class-textserverextension-private-method-font-get-glyph-uv-rect)(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int)) virtual required const |
| [Hinting](class_textserver.md#enum-textserver-hinting) | [_font_get_hinting](class_textserverextension.md#class-textserverextension-private-method-font-get-hinting)(font_rid: [RID](class_rid.md#class-rid)) virtual const |
| [bool](class_bool.md#class-bool) | [_font_get_keep_rounding_remainders](class_textserverextension.md#class-textserverextension-private-method-font-get-keep-rounding-remainders)(font_rid: [RID](class_rid.md#class-rid)) virtual const |
| [Vector2](class_vector2.md#class-vector2) | [_font_get_kerning](class_textserverextension.md#class-textserverextension-private-method-font-get-kerning)(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), glyph_pair: [Vector2i](class_vector2i.md#class-vector2i)) virtual const |
| [Array](class_array.md#class-array)[[Vector2i](class_vector2i.md#class-vector2i)] | [_font_get_kerning_list](class_textserverextension.md#class-textserverextension-private-method-font-get-kerning-list)(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int)) virtual const |
| [bool](class_bool.md#class-bool) | [_font_get_language_support_override](class_textserverextension.md#class-textserverextension-private-method-font-get-language-support-override)(font_rid: [RID](class_rid.md#class-rid), language: [String](class_string.md#class-string)) virtual |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [_font_get_language_support_overrides](class_textserverextension.md#class-textserverextension-private-method-font-get-language-support-overrides)(font_rid: [RID](class_rid.md#class-rid)) virtual |
| [int](class_int.md#class-int) | [_font_get_msdf_pixel_range](class_textserverextension.md#class-textserverextension-private-method-font-get-msdf-pixel-range)(font_rid: [RID](class_rid.md#class-rid)) virtual const |
| [int](class_int.md#class-int) | [_font_get_msdf_size](class_textserverextension.md#class-textserverextension-private-method-font-get-msdf-size)(font_rid: [RID](class_rid.md#class-rid)) virtual const |
| [String](class_string.md#class-string) | [_font_get_name](class_textserverextension.md#class-textserverextension-private-method-font-get-name)(font_rid: [RID](class_rid.md#class-rid)) virtual const |
| [Dictionary](class_dictionary.md#class-dictionary) | [_font_get_opentype_feature_overrides](class_textserverextension.md#class-textserverextension-private-method-font-get-opentype-feature-overrides)(font_rid: [RID](class_rid.md#class-rid)) virtual const |
| [Dictionary](class_dictionary.md#class-dictionary) | [_font_get_ot_name_strings](class_textserverextension.md#class-textserverextension-private-method-font-get-ot-name-strings)(font_rid: [RID](class_rid.md#class-rid)) virtual const |
| [float](class_float.md#class-float) | [_font_get_oversampling](class_textserverextension.md#class-textserverextension-private-method-font-get-oversampling)(font_rid: [RID](class_rid.md#class-rid)) virtual const |
| [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) | [_font_get_palette_colors](class_textserverextension.md#class-textserverextension-private-method-font-get-palette-colors)(font_rid: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) virtual const |
| [int](class_int.md#class-int) | [_font_get_palette_count](class_textserverextension.md#class-textserverextension-private-method-font-get-palette-count)(font_rid: [RID](class_rid.md#class-rid)) virtual const |
| [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) | [_font_get_palette_custom_colors](class_textserverextension.md#class-textserverextension-private-method-font-get-palette-custom-colors)(font_rid: [RID](class_rid.md#class-rid)) virtual const |
| [String](class_string.md#class-string) | [_font_get_palette_name](class_textserverextension.md#class-textserverextension-private-method-font-get-palette-name)(font_rid: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) virtual const |
| [float](class_float.md#class-float) | [_font_get_scale](class_textserverextension.md#class-textserverextension-private-method-font-get-scale)(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int)) virtual required const |
| [bool](class_bool.md#class-bool) | [_font_get_script_support_override](class_textserverextension.md#class-textserverextension-private-method-font-get-script-support-override)(font_rid: [RID](class_rid.md#class-rid), script: [String](class_string.md#class-string)) virtual |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [_font_get_script_support_overrides](class_textserverextension.md#class-textserverextension-private-method-font-get-script-support-overrides)(font_rid: [RID](class_rid.md#class-rid)) virtual |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | [_font_get_size_cache_info](class_textserverextension.md#class-textserverextension-private-method-font-get-size-cache-info)(font_rid: [RID](class_rid.md#class-rid)) virtual const |
| [Array](class_array.md#class-array)[[Vector2i](class_vector2i.md#class-vector2i)] | [_font_get_size_cache_list](class_textserverextension.md#class-textserverextension-private-method-font-get-size-cache-list)(font_rid: [RID](class_rid.md#class-rid)) virtual required const |
| [int](class_int.md#class-int) | [_font_get_spacing](class_textserverextension.md#class-textserverextension-private-method-font-get-spacing)(font_rid: [RID](class_rid.md#class-rid), spacing: [SpacingType](class_textserver.md#enum-textserver-spacingtype)) virtual const |
| [int](class_int.md#class-int) | [_font_get_stretch](class_textserverextension.md#class-textserverextension-private-method-font-get-stretch)(font_rid: [RID](class_rid.md#class-rid)) virtual const |
| BitField[[FontStyle](class_textserver.md#enum-textserver-fontstyle)] | [_font_get_style](class_textserverextension.md#class-textserverextension-private-method-font-get-style)(font_rid: [RID](class_rid.md#class-rid)) virtual const |
| [String](class_string.md#class-string) | [_font_get_style_name](class_textserverextension.md#class-textserverextension-private-method-font-get-style-name)(font_rid: [RID](class_rid.md#class-rid)) virtual const |
| [SubpixelPositioning](class_textserver.md#enum-textserver-subpixelpositioning) | [_font_get_subpixel_positioning](class_textserverextension.md#class-textserverextension-private-method-font-get-subpixel-positioning)(font_rid: [RID](class_rid.md#class-rid)) virtual const |
| [String](class_string.md#class-string) | [_font_get_supported_chars](class_textserverextension.md#class-textserverextension-private-method-font-get-supported-chars)(font_rid: [RID](class_rid.md#class-rid)) virtual required const |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array) | [_font_get_supported_glyphs](class_textserverextension.md#class-textserverextension-private-method-font-get-supported-glyphs)(font_rid: [RID](class_rid.md#class-rid)) virtual required const |
| [int](class_int.md#class-int) | [_font_get_texture_count](class_textserverextension.md#class-textserverextension-private-method-font-get-texture-count)(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i)) virtual required const |
| [Image](class_image.md#class-image) | [_font_get_texture_image](class_textserverextension.md#class-textserverextension-private-method-font-get-texture-image)(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int)) virtual required const |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array) | [_font_get_texture_offsets](class_textserverextension.md#class-textserverextension-private-method-font-get-texture-offsets)(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int)) virtual const |
| [Transform2D](class_transform2d.md#class-transform2d) | [_font_get_transform](class_textserverextension.md#class-textserverextension-private-method-font-get-transform)(font_rid: [RID](class_rid.md#class-rid)) virtual const |
| [float](class_float.md#class-float) | [_font_get_underline_position](class_textserverextension.md#class-textserverextension-private-method-font-get-underline-position)(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int)) virtual required const |
| [float](class_float.md#class-float) | [_font_get_underline_thickness](class_textserverextension.md#class-textserverextension-private-method-font-get-underline-thickness)(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int)) virtual required const |
| [int](class_int.md#class-int) | [_font_get_used_palette](class_textserverextension.md#class-textserverextension-private-method-font-get-used-palette)(font_rid: [RID](class_rid.md#class-rid)) virtual const |
| [Dictionary](class_dictionary.md#class-dictionary) | [_font_get_variation_coordinates](class_textserverextension.md#class-textserverextension-private-method-font-get-variation-coordinates)(font_rid: [RID](class_rid.md#class-rid)) virtual const |
| [int](class_int.md#class-int) | [_font_get_weight](class_textserverextension.md#class-textserverextension-private-method-font-get-weight)(font_rid: [RID](class_rid.md#class-rid)) virtual const |
| [bool](class_bool.md#class-bool) | [_font_has_char](class_textserverextension.md#class-textserverextension-private-method-font-has-char)(font_rid: [RID](class_rid.md#class-rid), char: [int](class_int.md#class-int)) virtual required const |
| [bool](class_bool.md#class-bool) | [_font_is_allow_system_fallback](class_textserverextension.md#class-textserverextension-private-method-font-is-allow-system-fallback)(font_rid: [RID](class_rid.md#class-rid)) virtual const |
| [bool](class_bool.md#class-bool) | [_font_is_force_autohinter](class_textserverextension.md#class-textserverextension-private-method-font-is-force-autohinter)(font_rid: [RID](class_rid.md#class-rid)) virtual const |
| [bool](class_bool.md#class-bool) | [_font_is_language_supported](class_textserverextension.md#class-textserverextension-private-method-font-is-language-supported)(font_rid: [RID](class_rid.md#class-rid), language: [String](class_string.md#class-string)) virtual const |
| [bool](class_bool.md#class-bool) | [_font_is_modulate_color_glyphs](class_textserverextension.md#class-textserverextension-private-method-font-is-modulate-color-glyphs)(font_rid: [RID](class_rid.md#class-rid)) virtual const |
| [bool](class_bool.md#class-bool) | [_font_is_multichannel_signed_distance_field](class_textserverextension.md#class-textserverextension-private-method-font-is-multichannel-signed-distance-field)(font_rid: [RID](class_rid.md#class-rid)) virtual const |
| [bool](class_bool.md#class-bool) | [_font_is_script_supported](class_textserverextension.md#class-textserverextension-private-method-font-is-script-supported)(font_rid: [RID](class_rid.md#class-rid), script: [String](class_string.md#class-string)) virtual const |
| void | [_font_remove_glyph](class_textserverextension.md#class-textserverextension-private-method-font-remove-glyph)(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int)) virtual required |
| void | [_font_remove_kerning](class_textserverextension.md#class-textserverextension-private-method-font-remove-kerning)(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), glyph_pair: [Vector2i](class_vector2i.md#class-vector2i)) virtual |
| void | [_font_remove_language_support_override](class_textserverextension.md#class-textserverextension-private-method-font-remove-language-support-override)(font_rid: [RID](class_rid.md#class-rid), language: [String](class_string.md#class-string)) virtual |
| void | [_font_remove_script_support_override](class_textserverextension.md#class-textserverextension-private-method-font-remove-script-support-override)(font_rid: [RID](class_rid.md#class-rid), script: [String](class_string.md#class-string)) virtual |
| void | [_font_remove_size_cache](class_textserverextension.md#class-textserverextension-private-method-font-remove-size-cache)(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i)) virtual required |
| void | [_font_remove_texture](class_textserverextension.md#class-textserverextension-private-method-font-remove-texture)(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int)) virtual required |
| void | [_font_render_glyph](class_textserverextension.md#class-textserverextension-private-method-font-render-glyph)(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), index: [int](class_int.md#class-int)) virtual |
| void | [_font_render_range](class_textserverextension.md#class-textserverextension-private-method-font-render-range)(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), start: [int](class_int.md#class-int), end: [int](class_int.md#class-int)) virtual |
| void | [_font_set_allow_system_fallback](class_textserverextension.md#class-textserverextension-private-method-font-set-allow-system-fallback)(font_rid: [RID](class_rid.md#class-rid), allow_system_fallback: [bool](class_bool.md#class-bool)) virtual |
| void | [_font_set_antialiasing](class_textserverextension.md#class-textserverextension-private-method-font-set-antialiasing)(font_rid: [RID](class_rid.md#class-rid), antialiasing: [FontAntialiasing](class_textserver.md#enum-textserver-fontantialiasing)) virtual |
| void | [_font_set_ascent](class_textserverextension.md#class-textserverextension-private-method-font-set-ascent)(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), ascent: [float](class_float.md#class-float)) virtual required |
| void | [_font_set_baseline_offset](class_textserverextension.md#class-textserverextension-private-method-font-set-baseline-offset)(font_rid: [RID](class_rid.md#class-rid), baseline_offset: [float](class_float.md#class-float)) virtual |
| void | [_font_set_data](class_textserverextension.md#class-textserverextension-private-method-font-set-data)(font_rid: [RID](class_rid.md#class-rid), data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray)) virtual |
| void | [_font_set_data_ptr](class_textserverextension.md#class-textserverextension-private-method-font-set-data-ptr)(font_rid: [RID](class_rid.md#class-rid), data_ptr: `const uint8_t*`, data_size: [int](class_int.md#class-int)) virtual |
| void | [_font_set_descent](class_textserverextension.md#class-textserverextension-private-method-font-set-descent)(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), descent: [float](class_float.md#class-float)) virtual required |
| void | [_font_set_disable_embedded_bitmaps](class_textserverextension.md#class-textserverextension-private-method-font-set-disable-embedded-bitmaps)(font_rid: [RID](class_rid.md#class-rid), disable_embedded_bitmaps: [bool](class_bool.md#class-bool)) virtual |
| void | [_font_set_embolden](class_textserverextension.md#class-textserverextension-private-method-font-set-embolden)(font_rid: [RID](class_rid.md#class-rid), strength: [float](class_float.md#class-float)) virtual |
| void | [_font_set_face_index](class_textserverextension.md#class-textserverextension-private-method-font-set-face-index)(font_rid: [RID](class_rid.md#class-rid), face_index: [int](class_int.md#class-int)) virtual |
| void | [_font_set_fixed_size](class_textserverextension.md#class-textserverextension-private-method-font-set-fixed-size)(font_rid: [RID](class_rid.md#class-rid), fixed_size: [int](class_int.md#class-int)) virtual required |
| void | [_font_set_fixed_size_scale_mode](class_textserverextension.md#class-textserverextension-private-method-font-set-fixed-size-scale-mode)(font_rid: [RID](class_rid.md#class-rid), fixed_size_scale_mode: [FixedSizeScaleMode](class_textserver.md#enum-textserver-fixedsizescalemode)) virtual required |
| void | [_font_set_force_autohinter](class_textserverextension.md#class-textserverextension-private-method-font-set-force-autohinter)(font_rid: [RID](class_rid.md#class-rid), force_autohinter: [bool](class_bool.md#class-bool)) virtual |
| void | [_font_set_generate_mipmaps](class_textserverextension.md#class-textserverextension-private-method-font-set-generate-mipmaps)(font_rid: [RID](class_rid.md#class-rid), generate_mipmaps: [bool](class_bool.md#class-bool)) virtual |
| void | [_font_set_global_oversampling](class_textserverextension.md#class-textserverextension-private-method-font-set-global-oversampling)(oversampling: [float](class_float.md#class-float)) virtual |
| void | [_font_set_glyph_advance](class_textserverextension.md#class-textserverextension-private-method-font-set-glyph-advance)(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), glyph: [int](class_int.md#class-int), advance: [Vector2](class_vector2.md#class-vector2)) virtual required |
| void | [_font_set_glyph_offset](class_textserverextension.md#class-textserverextension-private-method-font-set-glyph-offset)(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int), offset: [Vector2](class_vector2.md#class-vector2)) virtual required |
| void | [_font_set_glyph_size](class_textserverextension.md#class-textserverextension-private-method-font-set-glyph-size)(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int), gl_size: [Vector2](class_vector2.md#class-vector2)) virtual required |
| void | [_font_set_glyph_texture_idx](class_textserverextension.md#class-textserverextension-private-method-font-set-glyph-texture-idx)(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int), texture_idx: [int](class_int.md#class-int)) virtual required |
| void | [_font_set_glyph_uv_rect](class_textserverextension.md#class-textserverextension-private-method-font-set-glyph-uv-rect)(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int), uv_rect: [Rect2](class_rect2.md#class-rect2)) virtual required |
| void | [_font_set_hinting](class_textserverextension.md#class-textserverextension-private-method-font-set-hinting)(font_rid: [RID](class_rid.md#class-rid), hinting: [Hinting](class_textserver.md#enum-textserver-hinting)) virtual |
| void | [_font_set_keep_rounding_remainders](class_textserverextension.md#class-textserverextension-private-method-font-set-keep-rounding-remainders)(font_rid: [RID](class_rid.md#class-rid), keep_rounding_remainders: [bool](class_bool.md#class-bool)) virtual |
| void | [_font_set_kerning](class_textserverextension.md#class-textserverextension-private-method-font-set-kerning)(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), glyph_pair: [Vector2i](class_vector2i.md#class-vector2i), kerning: [Vector2](class_vector2.md#class-vector2)) virtual |
| void | [_font_set_language_support_override](class_textserverextension.md#class-textserverextension-private-method-font-set-language-support-override)(font_rid: [RID](class_rid.md#class-rid), language: [String](class_string.md#class-string), supported: [bool](class_bool.md#class-bool)) virtual |
| void | [_font_set_modulate_color_glyphs](class_textserverextension.md#class-textserverextension-private-method-font-set-modulate-color-glyphs)(font_rid: [RID](class_rid.md#class-rid), modulate: [bool](class_bool.md#class-bool)) virtual |
| void | [_font_set_msdf_pixel_range](class_textserverextension.md#class-textserverextension-private-method-font-set-msdf-pixel-range)(font_rid: [RID](class_rid.md#class-rid), msdf_pixel_range: [int](class_int.md#class-int)) virtual |
| void | [_font_set_msdf_size](class_textserverextension.md#class-textserverextension-private-method-font-set-msdf-size)(font_rid: [RID](class_rid.md#class-rid), msdf_size: [int](class_int.md#class-int)) virtual |
| void | [_font_set_multichannel_signed_distance_field](class_textserverextension.md#class-textserverextension-private-method-font-set-multichannel-signed-distance-field)(font_rid: [RID](class_rid.md#class-rid), msdf: [bool](class_bool.md#class-bool)) virtual |
| void | [_font_set_name](class_textserverextension.md#class-textserverextension-private-method-font-set-name)(font_rid: [RID](class_rid.md#class-rid), name: [String](class_string.md#class-string)) virtual |
| void | [_font_set_opentype_feature_overrides](class_textserverextension.md#class-textserverextension-private-method-font-set-opentype-feature-overrides)(font_rid: [RID](class_rid.md#class-rid), overrides: [Dictionary](class_dictionary.md#class-dictionary)) virtual |
| void | [_font_set_oversampling](class_textserverextension.md#class-textserverextension-private-method-font-set-oversampling)(font_rid: [RID](class_rid.md#class-rid), oversampling: [float](class_float.md#class-float)) virtual |
| void | [_font_set_palette_custom_colors](class_textserverextension.md#class-textserverextension-private-method-font-set-palette-custom-colors)(font_rid: [RID](class_rid.md#class-rid), colors: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray)) virtual |
| void | [_font_set_scale](class_textserverextension.md#class-textserverextension-private-method-font-set-scale)(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), scale: [float](class_float.md#class-float)) virtual required |
| void | [_font_set_script_support_override](class_textserverextension.md#class-textserverextension-private-method-font-set-script-support-override)(font_rid: [RID](class_rid.md#class-rid), script: [String](class_string.md#class-string), supported: [bool](class_bool.md#class-bool)) virtual |
| void | [_font_set_spacing](class_textserverextension.md#class-textserverextension-private-method-font-set-spacing)(font_rid: [RID](class_rid.md#class-rid), spacing: [SpacingType](class_textserver.md#enum-textserver-spacingtype), value: [int](class_int.md#class-int)) virtual |
| void | [_font_set_stretch](class_textserverextension.md#class-textserverextension-private-method-font-set-stretch)(font_rid: [RID](class_rid.md#class-rid), stretch: [int](class_int.md#class-int)) virtual |
| void | [_font_set_style](class_textserverextension.md#class-textserverextension-private-method-font-set-style)(font_rid: [RID](class_rid.md#class-rid), style: BitField[[FontStyle](class_textserver.md#enum-textserver-fontstyle)]) virtual |
| void | [_font_set_style_name](class_textserverextension.md#class-textserverextension-private-method-font-set-style-name)(font_rid: [RID](class_rid.md#class-rid), name_style: [String](class_string.md#class-string)) virtual |
| void | [_font_set_subpixel_positioning](class_textserverextension.md#class-textserverextension-private-method-font-set-subpixel-positioning)(font_rid: [RID](class_rid.md#class-rid), subpixel_positioning: [SubpixelPositioning](class_textserver.md#enum-textserver-subpixelpositioning)) virtual |
| void | [_font_set_texture_image](class_textserverextension.md#class-textserverextension-private-method-font-set-texture-image)(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int), image: [Image](class_image.md#class-image)) virtual required |
| void | [_font_set_texture_offsets](class_textserverextension.md#class-textserverextension-private-method-font-set-texture-offsets)(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int), offset: [PackedInt32Array](class_packedint32array.md#class-packedint32array)) virtual |
| void | [_font_set_transform](class_textserverextension.md#class-textserverextension-private-method-font-set-transform)(font_rid: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d)) virtual |
| void | [_font_set_underline_position](class_textserverextension.md#class-textserverextension-private-method-font-set-underline-position)(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), underline_position: [float](class_float.md#class-float)) virtual required |
| void | [_font_set_underline_thickness](class_textserverextension.md#class-textserverextension-private-method-font-set-underline-thickness)(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), underline_thickness: [float](class_float.md#class-float)) virtual required |
| void | [_font_set_used_palette](class_textserverextension.md#class-textserverextension-private-method-font-set-used-palette)(font_rid: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) virtual |
| void | [_font_set_variation_coordinates](class_textserverextension.md#class-textserverextension-private-method-font-set-variation-coordinates)(font_rid: [RID](class_rid.md#class-rid), variation_coordinates: [Dictionary](class_dictionary.md#class-dictionary)) virtual |
| void | [_font_set_weight](class_textserverextension.md#class-textserverextension-private-method-font-set-weight)(font_rid: [RID](class_rid.md#class-rid), weight: [int](class_int.md#class-int)) virtual |
| [Dictionary](class_dictionary.md#class-dictionary) | [_font_supported_feature_list](class_textserverextension.md#class-textserverextension-private-method-font-supported-feature-list)(font_rid: [RID](class_rid.md#class-rid)) virtual const |
| [Dictionary](class_dictionary.md#class-dictionary) | [_font_supported_variation_list](class_textserverextension.md#class-textserverextension-private-method-font-supported-variation-list)(font_rid: [RID](class_rid.md#class-rid)) virtual const |
| [String](class_string.md#class-string) | [_format_number](class_textserverextension.md#class-textserverextension-private-method-format-number)(number: [String](class_string.md#class-string), language: [String](class_string.md#class-string)) virtual const |
| void | [_free_rid](class_textserverextension.md#class-textserverextension-private-method-free-rid)(rid: [RID](class_rid.md#class-rid)) virtual required |
| [int](class_int.md#class-int) | [_get_features](class_textserverextension.md#class-textserverextension-private-method-get-features)() virtual required const |
| [Vector2](class_vector2.md#class-vector2) | [_get_hex_code_box_size](class_textserverextension.md#class-textserverextension-private-method-get-hex-code-box-size)(size: [int](class_int.md#class-int), index: [int](class_int.md#class-int)) virtual const |
| [String](class_string.md#class-string) | [_get_name](class_textserverextension.md#class-textserverextension-private-method-get-name)() virtual required const |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray) | [_get_support_data](class_textserverextension.md#class-textserverextension-private-method-get-support-data)() virtual const |
| [String](class_string.md#class-string) | [_get_support_data_filename](class_textserverextension.md#class-textserverextension-private-method-get-support-data-filename)() virtual const |
| [String](class_string.md#class-string) | [_get_support_data_info](class_textserverextension.md#class-textserverextension-private-method-get-support-data-info)() virtual const |
| [bool](class_bool.md#class-bool) | [_has](class_textserverextension.md#class-textserverextension-private-method-has)(rid: [RID](class_rid.md#class-rid)) virtual required |
| [bool](class_bool.md#class-bool) | [_has_feature](class_textserverextension.md#class-textserverextension-private-method-has-feature)(feature: [Feature](class_textserver.md#enum-textserver-feature)) virtual required const |
| [int](class_int.md#class-int) | [_is_confusable](class_textserverextension.md#class-textserverextension-private-method-is-confusable)(string: [String](class_string.md#class-string), dict: [PackedStringArray](class_packedstringarray.md#class-packedstringarray)) virtual const |
| [bool](class_bool.md#class-bool) | [_is_locale_right_to_left](class_textserverextension.md#class-textserverextension-private-method-is-locale-right-to-left)(locale: [String](class_string.md#class-string)) virtual const |
| [bool](class_bool.md#class-bool) | [_is_locale_using_support_data](class_textserverextension.md#class-textserverextension-private-method-is-locale-using-support-data)(locale: [String](class_string.md#class-string)) virtual const |
| [bool](class_bool.md#class-bool) | [_is_valid_identifier](class_textserverextension.md#class-textserverextension-private-method-is-valid-identifier)(string: [String](class_string.md#class-string)) virtual const |
| [bool](class_bool.md#class-bool) | [_is_valid_letter](class_textserverextension.md#class-textserverextension-private-method-is-valid-letter)(unicode: [int](class_int.md#class-int)) virtual const |
| [bool](class_bool.md#class-bool) | [_load_support_data](class_textserverextension.md#class-textserverextension-private-method-load-support-data)(filename: [String](class_string.md#class-string)) virtual |
| [int](class_int.md#class-int) | [_name_to_tag](class_textserverextension.md#class-textserverextension-private-method-name-to-tag)(name: [String](class_string.md#class-string)) virtual const |
| [String](class_string.md#class-string) | [_parse_number](class_textserverextension.md#class-textserverextension-private-method-parse-number)(number: [String](class_string.md#class-string), language: [String](class_string.md#class-string)) virtual const |
| [Array](class_array.md#class-array)[[Vector3i](class_vector3i.md#class-vector3i)] | [_parse_structured_text](class_textserverextension.md#class-textserverextension-private-method-parse-structured-text)(parser_type: [StructuredTextParser](class_textserver.md#enum-textserver-structuredtextparser), args: [Array](class_array.md#class-array), text: [String](class_string.md#class-string)) virtual const |
| [String](class_string.md#class-string) | [_percent_sign](class_textserverextension.md#class-textserverextension-private-method-percent-sign)(language: [String](class_string.md#class-string)) virtual const |
| void | [_reference_oversampling_level](class_textserverextension.md#class-textserverextension-private-method-reference-oversampling-level)(oversampling: [float](class_float.md#class-float)) virtual |
| [bool](class_bool.md#class-bool) | [_save_support_data](class_textserverextension.md#class-textserverextension-private-method-save-support-data)(filename: [String](class_string.md#class-string)) virtual const |
| [int](class_int.md#class-int) | [_shaped_get_run_count](class_textserverextension.md#class-textserverextension-private-method-shaped-get-run-count)(shaped: [RID](class_rid.md#class-rid)) virtual const |
| [Direction](class_textserver.md#enum-textserver-direction) | [_shaped_get_run_direction](class_textserverextension.md#class-textserverextension-private-method-shaped-get-run-direction)(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) virtual const |
| [RID](class_rid.md#class-rid) | [_shaped_get_run_font_rid](class_textserverextension.md#class-textserverextension-private-method-shaped-get-run-font-rid)(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) virtual const |
| [int](class_int.md#class-int) | [_shaped_get_run_font_size](class_textserverextension.md#class-textserverextension-private-method-shaped-get-run-font-size)(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) virtual const |
| [Vector2i](class_vector2i.md#class-vector2i) | [_shaped_get_run_glyph_range](class_textserverextension.md#class-textserverextension-private-method-shaped-get-run-glyph-range)(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) virtual const |
| [String](class_string.md#class-string) | [_shaped_get_run_language](class_textserverextension.md#class-textserverextension-private-method-shaped-get-run-language)(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) virtual const |
| [Variant](class_variant.md#class-variant) | [_shaped_get_run_object](class_textserverextension.md#class-textserverextension-private-method-shaped-get-run-object)(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) virtual const |
| [Vector2i](class_vector2i.md#class-vector2i) | [_shaped_get_run_range](class_textserverextension.md#class-textserverextension-private-method-shaped-get-run-range)(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) virtual const |
| [String](class_string.md#class-string) | [_shaped_get_run_text](class_textserverextension.md#class-textserverextension-private-method-shaped-get-run-text)(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) virtual const |
| [int](class_int.md#class-int) | [_shaped_get_span_count](class_textserverextension.md#class-textserverextension-private-method-shaped-get-span-count)(shaped: [RID](class_rid.md#class-rid)) virtual required const |
| [Variant](class_variant.md#class-variant) | [_shaped_get_span_embedded_object](class_textserverextension.md#class-textserverextension-private-method-shaped-get-span-embedded-object)(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) virtual required const |
| [Variant](class_variant.md#class-variant) | [_shaped_get_span_meta](class_textserverextension.md#class-textserverextension-private-method-shaped-get-span-meta)(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) virtual required const |
| [Variant](class_variant.md#class-variant) | [_shaped_get_span_object](class_textserverextension.md#class-textserverextension-private-method-shaped-get-span-object)(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) virtual required const |
| [String](class_string.md#class-string) | [_shaped_get_span_text](class_textserverextension.md#class-textserverextension-private-method-shaped-get-span-text)(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) virtual required const |
| [String](class_string.md#class-string) | [_shaped_get_text](class_textserverextension.md#class-textserverextension-private-method-shaped-get-text)(shaped: [RID](class_rid.md#class-rid)) virtual required const |
| void | [_shaped_set_span_update_font](class_textserverextension.md#class-textserverextension-private-method-shaped-set-span-update-font)(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int), fonts: [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)], size: [int](class_int.md#class-int), opentype_features: [Dictionary](class_dictionary.md#class-dictionary)) virtual required |
| [bool](class_bool.md#class-bool) | [_shaped_text_add_object](class_textserverextension.md#class-textserverextension-private-method-shaped-text-add-object)(shaped: [RID](class_rid.md#class-rid), key: [Variant](class_variant.md#class-variant), size: [Vector2](class_vector2.md#class-vector2), inline_align: [InlineAlignment](class_@globalscope.md#enum-globalscope-inlinealignment), length: [int](class_int.md#class-int), baseline: [float](class_float.md#class-float)) virtual required |
| [bool](class_bool.md#class-bool) | [_shaped_text_add_string](class_textserverextension.md#class-textserverextension-private-method-shaped-text-add-string)(shaped: [RID](class_rid.md#class-rid), text: [String](class_string.md#class-string), fonts: [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)], size: [int](class_int.md#class-int), opentype_features: [Dictionary](class_dictionary.md#class-dictionary), language: [String](class_string.md#class-string), meta: [Variant](class_variant.md#class-variant)) virtual required |
| void | [_shaped_text_clear](class_textserverextension.md#class-textserverextension-private-method-shaped-text-clear)(shaped: [RID](class_rid.md#class-rid)) virtual required |
| [int](class_int.md#class-int) | [_shaped_text_closest_character_pos](class_textserverextension.md#class-textserverextension-private-method-shaped-text-closest-character-pos)(shaped: [RID](class_rid.md#class-rid), pos: [int](class_int.md#class-int)) virtual const |
| void | [_shaped_text_draw](class_textserverextension.md#class-textserverextension-private-method-shaped-text-draw)(shaped: [RID](class_rid.md#class-rid), canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), clip_l: [float](class_float.md#class-float), clip_r: [float](class_float.md#class-float), color: [Color](class_color.md#class-color), oversampling: [float](class_float.md#class-float)) virtual const |
| void | [_shaped_text_draw_outline](class_textserverextension.md#class-textserverextension-private-method-shaped-text-draw-outline)(shaped: [RID](class_rid.md#class-rid), canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), clip_l: [float](class_float.md#class-float), clip_r: [float](class_float.md#class-float), outline_size: [int](class_int.md#class-int), color: [Color](class_color.md#class-color), oversampling: [float](class_float.md#class-float)) virtual const |
| [RID](class_rid.md#class-rid) | [_shaped_text_duplicate](class_textserverextension.md#class-textserverextension-private-method-shaped-text-duplicate)(shaped: [RID](class_rid.md#class-rid)) virtual required |
| [float](class_float.md#class-float) | [_shaped_text_fit_to_width](class_textserverextension.md#class-textserverextension-private-method-shaped-text-fit-to-width)(shaped: [RID](class_rid.md#class-rid), width: [float](class_float.md#class-float), justification_flags: BitField[[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)]) virtual |
| [float](class_float.md#class-float) | [_shaped_text_get_ascent](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-ascent)(shaped: [RID](class_rid.md#class-rid)) virtual required const |
| void | [_shaped_text_get_carets](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-carets)(shaped: [RID](class_rid.md#class-rid), position: [int](class_int.md#class-int), r_caret: `CaretInfo*`) virtual const |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array) | [_shaped_text_get_character_breaks](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-character-breaks)(shaped: [RID](class_rid.md#class-rid)) virtual const |
| [int](class_int.md#class-int) | [_shaped_text_get_custom_ellipsis](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-custom-ellipsis)(shaped: [RID](class_rid.md#class-rid)) virtual const |
| [String](class_string.md#class-string) | [_shaped_text_get_custom_punctuation](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-custom-punctuation)(shaped: [RID](class_rid.md#class-rid)) virtual const |
| [float](class_float.md#class-float) | [_shaped_text_get_descent](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-descent)(shaped: [RID](class_rid.md#class-rid)) virtual required const |
| [Direction](class_textserver.md#enum-textserver-direction) | [_shaped_text_get_direction](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-direction)(shaped: [RID](class_rid.md#class-rid)) virtual const |
| [int](class_int.md#class-int) | [_shaped_text_get_dominant_direction_in_range](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-dominant-direction-in-range)(shaped: [RID](class_rid.md#class-rid), start: [int](class_int.md#class-int), end: [int](class_int.md#class-int)) virtual const |
| [int](class_int.md#class-int) | [_shaped_text_get_ellipsis_glyph_count](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-ellipsis-glyph-count)(shaped: [RID](class_rid.md#class-rid)) virtual required const |
| `const Glyph*` | [_shaped_text_get_ellipsis_glyphs](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-ellipsis-glyphs)(shaped: [RID](class_rid.md#class-rid)) virtual required const |
| [int](class_int.md#class-int) | [_shaped_text_get_ellipsis_pos](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-ellipsis-pos)(shaped: [RID](class_rid.md#class-rid)) virtual required const |
| [int](class_int.md#class-int) | [_shaped_text_get_glyph_count](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-glyph-count)(shaped: [RID](class_rid.md#class-rid)) virtual required const |
| `const Glyph*` | [_shaped_text_get_glyphs](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-glyphs)(shaped: [RID](class_rid.md#class-rid)) virtual required const |
| [Vector2](class_vector2.md#class-vector2) | [_shaped_text_get_grapheme_bounds](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-grapheme-bounds)(shaped: [RID](class_rid.md#class-rid), pos: [int](class_int.md#class-int)) virtual const |
| [Direction](class_textserver.md#enum-textserver-direction) | [_shaped_text_get_inferred_direction](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-inferred-direction)(shaped: [RID](class_rid.md#class-rid)) virtual const |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array) | [_shaped_text_get_line_breaks](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-line-breaks)(shaped: [RID](class_rid.md#class-rid), width: [float](class_float.md#class-float), start: [int](class_int.md#class-int), break_flags: BitField[[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)]) virtual const |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array) | [_shaped_text_get_line_breaks_adv](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-line-breaks-adv)(shaped: [RID](class_rid.md#class-rid), width: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array), start: [int](class_int.md#class-int), once: [bool](class_bool.md#class-bool), break_flags: BitField[[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)]) virtual const |
| [int](class_int.md#class-int) | [_shaped_text_get_object_glyph](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-object-glyph)(shaped: [RID](class_rid.md#class-rid), key: [Variant](class_variant.md#class-variant)) virtual required const |
| [Vector2i](class_vector2i.md#class-vector2i) | [_shaped_text_get_object_range](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-object-range)(shaped: [RID](class_rid.md#class-rid), key: [Variant](class_variant.md#class-variant)) virtual required const |
| [Rect2](class_rect2.md#class-rect2) | [_shaped_text_get_object_rect](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-object-rect)(shaped: [RID](class_rid.md#class-rid), key: [Variant](class_variant.md#class-variant)) virtual required const |
| [Array](class_array.md#class-array) | [_shaped_text_get_objects](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-objects)(shaped: [RID](class_rid.md#class-rid)) virtual required const |
| [Orientation](class_textserver.md#enum-textserver-orientation) | [_shaped_text_get_orientation](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-orientation)(shaped: [RID](class_rid.md#class-rid)) virtual const |
| [RID](class_rid.md#class-rid) | [_shaped_text_get_parent](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-parent)(shaped: [RID](class_rid.md#class-rid)) virtual required const |
| [bool](class_bool.md#class-bool) | [_shaped_text_get_preserve_control](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-preserve-control)(shaped: [RID](class_rid.md#class-rid)) virtual const |
| [bool](class_bool.md#class-bool) | [_shaped_text_get_preserve_invalid](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-preserve-invalid)(shaped: [RID](class_rid.md#class-rid)) virtual const |
| [Vector2i](class_vector2i.md#class-vector2i) | [_shaped_text_get_range](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-range)(shaped: [RID](class_rid.md#class-rid)) virtual required const |
| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) | [_shaped_text_get_selection](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-selection)(shaped: [RID](class_rid.md#class-rid), start: [int](class_int.md#class-int), end: [int](class_int.md#class-int)) virtual const |
| [Vector2](class_vector2.md#class-vector2) | [_shaped_text_get_size](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-size)(shaped: [RID](class_rid.md#class-rid)) virtual required const |
| [int](class_int.md#class-int) | [_shaped_text_get_spacing](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-spacing)(shaped: [RID](class_rid.md#class-rid), spacing: [SpacingType](class_textserver.md#enum-textserver-spacingtype)) virtual const |
| [int](class_int.md#class-int) | [_shaped_text_get_trim_pos](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-trim-pos)(shaped: [RID](class_rid.md#class-rid)) virtual required const |
| [float](class_float.md#class-float) | [_shaped_text_get_underline_position](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-underline-position)(shaped: [RID](class_rid.md#class-rid)) virtual required const |
| [float](class_float.md#class-float) | [_shaped_text_get_underline_thickness](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-underline-thickness)(shaped: [RID](class_rid.md#class-rid)) virtual required const |
| [float](class_float.md#class-float) | [_shaped_text_get_width](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-width)(shaped: [RID](class_rid.md#class-rid)) virtual required const |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array) | [_shaped_text_get_word_breaks](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-word-breaks)(shaped: [RID](class_rid.md#class-rid), grapheme_flags: BitField[[GraphemeFlag](class_textserver.md#enum-textserver-graphemeflag)], skip_grapheme_flags: BitField[[GraphemeFlag](class_textserver.md#enum-textserver-graphemeflag)]) virtual const |
| [bool](class_bool.md#class-bool) | [_shaped_text_has_object](class_textserverextension.md#class-textserverextension-private-method-shaped-text-has-object)(shaped: [RID](class_rid.md#class-rid), key: [Variant](class_variant.md#class-variant)) virtual required const |
| [int](class_int.md#class-int) | [_shaped_text_hit_test_grapheme](class_textserverextension.md#class-textserverextension-private-method-shaped-text-hit-test-grapheme)(shaped: [RID](class_rid.md#class-rid), coord: [float](class_float.md#class-float)) virtual const |
| [int](class_int.md#class-int) | [_shaped_text_hit_test_position](class_textserverextension.md#class-textserverextension-private-method-shaped-text-hit-test-position)(shaped: [RID](class_rid.md#class-rid), coord: [float](class_float.md#class-float)) virtual const |
| [bool](class_bool.md#class-bool) | [_shaped_text_is_ready](class_textserverextension.md#class-textserverextension-private-method-shaped-text-is-ready)(shaped: [RID](class_rid.md#class-rid)) virtual required const |
| [int](class_int.md#class-int) | [_shaped_text_next_character_pos](class_textserverextension.md#class-textserverextension-private-method-shaped-text-next-character-pos)(shaped: [RID](class_rid.md#class-rid), pos: [int](class_int.md#class-int)) virtual const |
| [int](class_int.md#class-int) | [_shaped_text_next_grapheme_pos](class_textserverextension.md#class-textserverextension-private-method-shaped-text-next-grapheme-pos)(shaped: [RID](class_rid.md#class-rid), pos: [int](class_int.md#class-int)) virtual const |
| void | [_shaped_text_overrun_trim_to_width](class_textserverextension.md#class-textserverextension-private-method-shaped-text-overrun-trim-to-width)(shaped: [RID](class_rid.md#class-rid), width: [float](class_float.md#class-float), trim_flags: BitField[[TextOverrunFlag](class_textserver.md#enum-textserver-textoverrunflag)]) virtual |
| [int](class_int.md#class-int) | [_shaped_text_prev_character_pos](class_textserverextension.md#class-textserverextension-private-method-shaped-text-prev-character-pos)(shaped: [RID](class_rid.md#class-rid), pos: [int](class_int.md#class-int)) virtual const |
| [int](class_int.md#class-int) | [_shaped_text_prev_grapheme_pos](class_textserverextension.md#class-textserverextension-private-method-shaped-text-prev-grapheme-pos)(shaped: [RID](class_rid.md#class-rid), pos: [int](class_int.md#class-int)) virtual const |
| [bool](class_bool.md#class-bool) | [_shaped_text_resize_object](class_textserverextension.md#class-textserverextension-private-method-shaped-text-resize-object)(shaped: [RID](class_rid.md#class-rid), key: [Variant](class_variant.md#class-variant), size: [Vector2](class_vector2.md#class-vector2), inline_align: [InlineAlignment](class_@globalscope.md#enum-globalscope-inlinealignment), baseline: [float](class_float.md#class-float)) virtual required |
| void | [_shaped_text_set_bidi_override](class_textserverextension.md#class-textserverextension-private-method-shaped-text-set-bidi-override)(shaped: [RID](class_rid.md#class-rid), override: [Array](class_array.md#class-array)) virtual |
| void | [_shaped_text_set_custom_ellipsis](class_textserverextension.md#class-textserverextension-private-method-shaped-text-set-custom-ellipsis)(shaped: [RID](class_rid.md#class-rid), char: [int](class_int.md#class-int)) virtual |
| void | [_shaped_text_set_custom_punctuation](class_textserverextension.md#class-textserverextension-private-method-shaped-text-set-custom-punctuation)(shaped: [RID](class_rid.md#class-rid), punct: [String](class_string.md#class-string)) virtual |
| void | [_shaped_text_set_direction](class_textserverextension.md#class-textserverextension-private-method-shaped-text-set-direction)(shaped: [RID](class_rid.md#class-rid), direction: [Direction](class_textserver.md#enum-textserver-direction)) virtual |
| void | [_shaped_text_set_orientation](class_textserverextension.md#class-textserverextension-private-method-shaped-text-set-orientation)(shaped: [RID](class_rid.md#class-rid), orientation: [Orientation](class_textserver.md#enum-textserver-orientation)) virtual |
| void | [_shaped_text_set_preserve_control](class_textserverextension.md#class-textserverextension-private-method-shaped-text-set-preserve-control)(shaped: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool)) virtual |
| void | [_shaped_text_set_preserve_invalid](class_textserverextension.md#class-textserverextension-private-method-shaped-text-set-preserve-invalid)(shaped: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool)) virtual |
| void | [_shaped_text_set_spacing](class_textserverextension.md#class-textserverextension-private-method-shaped-text-set-spacing)(shaped: [RID](class_rid.md#class-rid), spacing: [SpacingType](class_textserver.md#enum-textserver-spacingtype), value: [int](class_int.md#class-int)) virtual |
| [bool](class_bool.md#class-bool) | [_shaped_text_shape](class_textserverextension.md#class-textserverextension-private-method-shaped-text-shape)(shaped: [RID](class_rid.md#class-rid)) virtual required |
| `const Glyph*` | [_shaped_text_sort_logical](class_textserverextension.md#class-textserverextension-private-method-shaped-text-sort-logical)(shaped: [RID](class_rid.md#class-rid)) virtual required |
| [RID](class_rid.md#class-rid) | [_shaped_text_substr](class_textserverextension.md#class-textserverextension-private-method-shaped-text-substr)(shaped: [RID](class_rid.md#class-rid), start: [int](class_int.md#class-int), length: [int](class_int.md#class-int)) virtual required const |
| [float](class_float.md#class-float) | [_shaped_text_tab_align](class_textserverextension.md#class-textserverextension-private-method-shaped-text-tab-align)(shaped: [RID](class_rid.md#class-rid), tab_stops: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array)) virtual |
| [bool](class_bool.md#class-bool) | [_shaped_text_update_breaks](class_textserverextension.md#class-textserverextension-private-method-shaped-text-update-breaks)(shaped: [RID](class_rid.md#class-rid)) virtual |
| [bool](class_bool.md#class-bool) | [_shaped_text_update_justification_ops](class_textserverextension.md#class-textserverextension-private-method-shaped-text-update-justification-ops)(shaped: [RID](class_rid.md#class-rid)) virtual |
| [bool](class_bool.md#class-bool) | [_spoof_check](class_textserverextension.md#class-textserverextension-private-method-spoof-check)(string: [String](class_string.md#class-string)) virtual const |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array) | [_string_get_character_breaks](class_textserverextension.md#class-textserverextension-private-method-string-get-character-breaks)(string: [String](class_string.md#class-string), language: [String](class_string.md#class-string)) virtual const |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array) | [_string_get_word_breaks](class_textserverextension.md#class-textserverextension-private-method-string-get-word-breaks)(string: [String](class_string.md#class-string), language: [String](class_string.md#class-string), chars_per_line: [int](class_int.md#class-int)) virtual const |
| [String](class_string.md#class-string) | [_string_to_lower](class_textserverextension.md#class-textserverextension-private-method-string-to-lower)(string: [String](class_string.md#class-string), language: [String](class_string.md#class-string)) virtual const |
| [String](class_string.md#class-string) | [_string_to_title](class_textserverextension.md#class-textserverextension-private-method-string-to-title)(string: [String](class_string.md#class-string), language: [String](class_string.md#class-string)) virtual const |
| [String](class_string.md#class-string) | [_string_to_upper](class_textserverextension.md#class-textserverextension-private-method-string-to-upper)(string: [String](class_string.md#class-string), language: [String](class_string.md#class-string)) virtual const |
| [String](class_string.md#class-string) | [_strip_diacritics](class_textserverextension.md#class-textserverextension-private-method-strip-diacritics)(string: [String](class_string.md#class-string)) virtual const |
| [String](class_string.md#class-string) | [_tag_to_name](class_textserverextension.md#class-textserverextension-private-method-tag-to-name)(tag: [int](class_int.md#class-int)) virtual const |
| void | [_unreference_oversampling_level](class_textserverextension.md#class-textserverextension-private-method-unreference-oversampling-level)(oversampling: [float](class_float.md#class-float)) virtual |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-textserverextension-private-method-cleanup"></a>

void **_cleanup**() virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-cleanup)

This method is called before text server is unregistered.

---


<a id="class-textserverextension-private-method-create-font"></a>

[RID](class_rid.md#class-rid) **_create_font**() virtual required [🔗](class_textserverextension.md#class-textserverextension-private-method-create-font)

Creates a new, empty font cache entry resource.

---


<a id="class-textserverextension-private-method-create-font-linked-variation"></a>

[RID](class_rid.md#class-rid) **_create_font_linked_variation**(font_rid: [RID](class_rid.md#class-rid)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-create-font-linked-variation)

Optional, implement if font supports extra spacing or baseline offset.

Creates a new variation existing font which is reusing the same glyph cache and font data.

---


<a id="class-textserverextension-private-method-create-shaped-text"></a>

[RID](class_rid.md#class-rid) **_create_shaped_text**(direction: [Direction](class_textserver.md#enum-textserver-direction), orientation: [Orientation](class_textserver.md#enum-textserver-orientation)) virtual required [🔗](class_textserverextension.md#class-textserverextension-private-method-create-shaped-text)

Creates a new buffer for complex text layout, with the given `direction` and `orientation`.

---


<a id="class-textserverextension-private-method-draw-hex-code-box"></a>

void **_draw_hex_code_box**(canvas: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), pos: [Vector2](class_vector2.md#class-vector2), index: [int](class_int.md#class-int), color: [Color](class_color.md#class-color)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-draw-hex-code-box)

Draws box displaying character hexadecimal code.

---


<a id="class-textserverextension-private-method-font-clear-glyphs"></a>

void **_font_clear_glyphs**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i)) virtual required [🔗](class_textserverextension.md#class-textserverextension-private-method-font-clear-glyphs)

Removes all rendered glyph information from the cache entry.

---


<a id="class-textserverextension-private-method-font-clear-kerning-map"></a>

void **_font_clear_kerning_map**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-clear-kerning-map)

Removes all kerning overrides.

---


<a id="class-textserverextension-private-method-font-clear-size-cache"></a>

void **_font_clear_size_cache**(font_rid: [RID](class_rid.md#class-rid)) virtual required [🔗](class_textserverextension.md#class-textserverextension-private-method-font-clear-size-cache)

Removes all font sizes from the cache entry.

---


<a id="class-textserverextension-private-method-font-clear-system-fallback-cache"></a>

void **_font_clear_system_fallback_cache**() virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-clear-system-fallback-cache)

Frees all automatically loaded system fonts.

---


<a id="class-textserverextension-private-method-font-clear-textures"></a>

void **_font_clear_textures**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i)) virtual required [🔗](class_textserverextension.md#class-textserverextension-private-method-font-clear-textures)

Removes all textures from font cache entry.

---


<a id="class-textserverextension-private-method-font-draw-glyph"></a>

void **_font_draw_glyph**(font_rid: [RID](class_rid.md#class-rid), canvas: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), pos: [Vector2](class_vector2.md#class-vector2), index: [int](class_int.md#class-int), color: [Color](class_color.md#class-color), oversampling: [float](class_float.md#class-float)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-draw-glyph)

Draws single glyph into a canvas item at the position, using `font_rid` at the size `size`. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

---


<a id="class-textserverextension-private-method-font-draw-glyph-outline"></a>

void **_font_draw_glyph_outline**(font_rid: [RID](class_rid.md#class-rid), canvas: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), outline_size: [int](class_int.md#class-int), pos: [Vector2](class_vector2.md#class-vector2), index: [int](class_int.md#class-int), color: [Color](class_color.md#class-color), oversampling: [float](class_float.md#class-float)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-draw-glyph-outline)

Draws single glyph outline of size `outline_size` into a canvas item at the position, using `font_rid` at the size `size`. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

---


<a id="class-textserverextension-private-method-font-get-antialiasing"></a>

[FontAntialiasing](class_textserver.md#enum-textserver-fontantialiasing) **_font_get_antialiasing**(font_rid: [RID](class_rid.md#class-rid)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-antialiasing)

Returns font anti-aliasing mode.

---


<a id="class-textserverextension-private-method-font-get-ascent"></a>

[float](class_float.md#class-float) **_font_get_ascent**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-ascent)

Returns the font ascent (number of pixels above the baseline).

---


<a id="class-textserverextension-private-method-font-get-baseline-offset"></a>

[float](class_float.md#class-float) **_font_get_baseline_offset**(font_rid: [RID](class_rid.md#class-rid)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-baseline-offset)

Returns extra baseline offset (as a fraction of font height).

---


<a id="class-textserverextension-private-method-font-get-char-from-glyph-index"></a>

[int](class_int.md#class-int) **_font_get_char_from_glyph_index**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), glyph_index: [int](class_int.md#class-int)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-char-from-glyph-index)

Returns character code associated with `glyph_index`, or `0` if `glyph_index` is invalid.

---


<a id="class-textserverextension-private-method-font-get-descent"></a>

[float](class_float.md#class-float) **_font_get_descent**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-descent)

Returns the font descent (number of pixels below the baseline).

---


<a id="class-textserverextension-private-method-font-get-disable-embedded-bitmaps"></a>

[bool](class_bool.md#class-bool) **_font_get_disable_embedded_bitmaps**(font_rid: [RID](class_rid.md#class-rid)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-disable-embedded-bitmaps)

Returns whether the font's embedded bitmap loading is disabled.

---


<a id="class-textserverextension-private-method-font-get-embolden"></a>

[float](class_float.md#class-float) **_font_get_embolden**(font_rid: [RID](class_rid.md#class-rid)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-embolden)

Returns font embolden strength.

---


<a id="class-textserverextension-private-method-font-get-face-count"></a>

[int](class_int.md#class-int) **_font_get_face_count**(font_rid: [RID](class_rid.md#class-rid)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-face-count)

Returns number of faces in the TrueType / OpenType collection.

---


<a id="class-textserverextension-private-method-font-get-face-index"></a>

[int](class_int.md#class-int) **_font_get_face_index**(font_rid: [RID](class_rid.md#class-rid)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-face-index)

Returns an active face index in the TrueType / OpenType collection.

---


<a id="class-textserverextension-private-method-font-get-fixed-size"></a>

[int](class_int.md#class-int) **_font_get_fixed_size**(font_rid: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-fixed-size)

Returns bitmap font fixed size.

---


<a id="class-textserverextension-private-method-font-get-fixed-size-scale-mode"></a>

[FixedSizeScaleMode](class_textserver.md#enum-textserver-fixedsizescalemode) **_font_get_fixed_size_scale_mode**(font_rid: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-fixed-size-scale-mode)

Returns bitmap font scaling mode.

---


<a id="class-textserverextension-private-method-font-get-generate-mipmaps"></a>

[bool](class_bool.md#class-bool) **_font_get_generate_mipmaps**(font_rid: [RID](class_rid.md#class-rid)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-generate-mipmaps)

Returns `true` if font texture mipmap generation is enabled.

---


<a id="class-textserverextension-private-method-font-get-global-oversampling"></a>

[float](class_float.md#class-float) **_font_get_global_oversampling**() virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-global-oversampling)

Returns the font oversampling factor, shared by all fonts in the TextServer.

---


<a id="class-textserverextension-private-method-font-get-glyph-advance"></a>

[Vector2](class_vector2.md#class-vector2) **_font_get_glyph_advance**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), glyph: [int](class_int.md#class-int)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-glyph-advance)

Returns glyph advance (offset of the next glyph).

---


<a id="class-textserverextension-private-method-font-get-glyph-contours"></a>

[Dictionary](class_dictionary.md#class-dictionary) **_font_get_glyph_contours**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), index: [int](class_int.md#class-int)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-glyph-contours)

Returns outline contours of the glyph.

---


<a id="class-textserverextension-private-method-font-get-glyph-index"></a>

[int](class_int.md#class-int) **_font_get_glyph_index**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), char: [int](class_int.md#class-int), variation_selector: [int](class_int.md#class-int)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-glyph-index)

Returns the glyph index of a `char`, optionally modified by the `variation_selector`.

---


<a id="class-textserverextension-private-method-font-get-glyph-list"></a>

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **_font_get_glyph_list**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-glyph-list)

Returns list of rendered glyphs in the cache entry.

---


<a id="class-textserverextension-private-method-font-get-glyph-offset"></a>

[Vector2](class_vector2.md#class-vector2) **_font_get_glyph_offset**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-glyph-offset)

Returns glyph offset from the baseline.

---


<a id="class-textserverextension-private-method-font-get-glyph-size"></a>

[Vector2](class_vector2.md#class-vector2) **_font_get_glyph_size**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-glyph-size)

Returns size of the glyph.

---


<a id="class-textserverextension-private-method-font-get-glyph-texture-idx"></a>

[int](class_int.md#class-int) **_font_get_glyph_texture_idx**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-glyph-texture-idx)

Returns index of the cache texture containing the glyph.

---


<a id="class-textserverextension-private-method-font-get-glyph-texture-rid"></a>

[RID](class_rid.md#class-rid) **_font_get_glyph_texture_rid**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-glyph-texture-rid)

Returns resource ID of the cache texture containing the glyph.

---


<a id="class-textserverextension-private-method-font-get-glyph-texture-size"></a>

[Vector2](class_vector2.md#class-vector2) **_font_get_glyph_texture_size**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-glyph-texture-size)

Returns size of the cache texture containing the glyph.

---


<a id="class-textserverextension-private-method-font-get-glyph-uv-rect"></a>

[Rect2](class_rect2.md#class-rect2) **_font_get_glyph_uv_rect**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-glyph-uv-rect)

Returns rectangle in the cache texture containing the glyph.

---


<a id="class-textserverextension-private-method-font-get-hinting"></a>

[Hinting](class_textserver.md#enum-textserver-hinting) **_font_get_hinting**(font_rid: [RID](class_rid.md#class-rid)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-hinting)

Returns the font hinting mode. Used by dynamic fonts only.

---


<a id="class-textserverextension-private-method-font-get-keep-rounding-remainders"></a>

[bool](class_bool.md#class-bool) **_font_get_keep_rounding_remainders**(font_rid: [RID](class_rid.md#class-rid)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-keep-rounding-remainders)

Returns glyph position rounding behavior. If set to `true`, when aligning glyphs to the pixel boundaries rounding remainders are accumulated to ensure more uniform glyph distribution. This setting has no effect if subpixel positioning is enabled.

---


<a id="class-textserverextension-private-method-font-get-kerning"></a>

[Vector2](class_vector2.md#class-vector2) **_font_get_kerning**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), glyph_pair: [Vector2i](class_vector2i.md#class-vector2i)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-kerning)

Returns kerning for the pair of glyphs.

---


<a id="class-textserverextension-private-method-font-get-kerning-list"></a>

[Array](class_array.md#class-array)[[Vector2i](class_vector2i.md#class-vector2i)] **_font_get_kerning_list**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-kerning-list)

Returns list of the kerning overrides.

---


<a id="class-textserverextension-private-method-font-get-language-support-override"></a>

[bool](class_bool.md#class-bool) **_font_get_language_support_override**(font_rid: [RID](class_rid.md#class-rid), language: [String](class_string.md#class-string)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-language-support-override)

Returns `true` if support override is enabled for the `language`.

---


<a id="class-textserverextension-private-method-font-get-language-support-overrides"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **_font_get_language_support_overrides**(font_rid: [RID](class_rid.md#class-rid)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-language-support-overrides)

Returns list of language support overrides.

---


<a id="class-textserverextension-private-method-font-get-msdf-pixel-range"></a>

[int](class_int.md#class-int) **_font_get_msdf_pixel_range**(font_rid: [RID](class_rid.md#class-rid)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-msdf-pixel-range)

Returns the width of the range around the shape between the minimum and maximum representable signed distance.

---


<a id="class-textserverextension-private-method-font-get-msdf-size"></a>

[int](class_int.md#class-int) **_font_get_msdf_size**(font_rid: [RID](class_rid.md#class-rid)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-msdf-size)

Returns source font size used to generate MSDF textures.

---


<a id="class-textserverextension-private-method-font-get-name"></a>

[String](class_string.md#class-string) **_font_get_name**(font_rid: [RID](class_rid.md#class-rid)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-name)

Returns font family name.

---


<a id="class-textserverextension-private-method-font-get-opentype-feature-overrides"></a>

[Dictionary](class_dictionary.md#class-dictionary) **_font_get_opentype_feature_overrides**(font_rid: [RID](class_rid.md#class-rid)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-opentype-feature-overrides)

Returns font OpenType feature set override.

---


<a id="class-textserverextension-private-method-font-get-ot-name-strings"></a>

[Dictionary](class_dictionary.md#class-dictionary) **_font_get_ot_name_strings**(font_rid: [RID](class_rid.md#class-rid)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-ot-name-strings)

Returns [Dictionary](class_dictionary.md#class-dictionary) with OpenType font name strings (localized font names, version, description, license information, sample text, etc.).

---


<a id="class-textserverextension-private-method-font-get-oversampling"></a>

[float](class_float.md#class-float) **_font_get_oversampling**(font_rid: [RID](class_rid.md#class-rid)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-oversampling)

Returns oversampling factor override. If set to a positive value, overrides the oversampling factor of the viewport this font is used in. See [Viewport.oversampling](class_viewport.md#class-viewport-property-oversampling). This value doesn't override the `oversampling` parameter of `draw_*` methods. Used by dynamic fonts only.

---


<a id="class-textserverextension-private-method-font-get-palette-colors"></a>

[PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) **_font_get_palette_colors**(font_rid: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-palette-colors)

Returns the array in the predefined color palette at `index`. Palette contains all colors used to render font glyphs. Each palette has the same number of colors. Colors can be overridden using [_font_set_palette_custom_colors()](class_textserverextension.md#class-textserverextension-private-method-font-set-palette-custom-colors).

---


<a id="class-textserverextension-private-method-font-get-palette-count"></a>

[int](class_int.md#class-int) **_font_get_palette_count**(font_rid: [RID](class_rid.md#class-rid)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-palette-count)

Returns the number of predefined color palettes. Palette contains all colors used to render font glyphs. Each palette has the same number of colors.

---


<a id="class-textserverextension-private-method-font-get-palette-custom-colors"></a>

[PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) **_font_get_palette_custom_colors**(font_rid: [RID](class_rid.md#class-rid)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-palette-custom-colors)

Returns array of custom colors to override predefined palette.

---


<a id="class-textserverextension-private-method-font-get-palette-name"></a>

[String](class_string.md#class-string) **_font_get_palette_name**(font_rid: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-palette-name)

Returns the name of the predefined color palette at `index`. Palette contains all colors used to render font glyphs. Each palette has the same number of colors.

---


<a id="class-textserverextension-private-method-font-get-scale"></a>

[float](class_float.md#class-float) **_font_get_scale**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-scale)

Returns scaling factor of the color bitmap font.

---


<a id="class-textserverextension-private-method-font-get-script-support-override"></a>

[bool](class_bool.md#class-bool) **_font_get_script_support_override**(font_rid: [RID](class_rid.md#class-rid), script: [String](class_string.md#class-string)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-script-support-override)

Returns `true` if support override is enabled for the `script`.

---


<a id="class-textserverextension-private-method-font-get-script-support-overrides"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **_font_get_script_support_overrides**(font_rid: [RID](class_rid.md#class-rid)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-script-support-overrides)

Returns list of script support overrides.

---


<a id="class-textserverextension-private-method-font-get-size-cache-info"></a>

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **_font_get_size_cache_info**(font_rid: [RID](class_rid.md#class-rid)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-size-cache-info)

Returns font cache information, each entry contains the following fields: `Vector2i size_px` - font size in pixels, `float viewport_oversampling` - viewport oversampling factor, `int glyphs` - number of rendered glyphs, `int textures` - number of used textures, `int textures_size` - size of texture data in bytes.

---


<a id="class-textserverextension-private-method-font-get-size-cache-list"></a>

[Array](class_array.md#class-array)[[Vector2i](class_vector2i.md#class-vector2i)] **_font_get_size_cache_list**(font_rid: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-size-cache-list)

Returns list of the font sizes in the cache. Each size is [Vector2i](class_vector2i.md#class-vector2i) with font size and outline size.

---


<a id="class-textserverextension-private-method-font-get-spacing"></a>

[int](class_int.md#class-int) **_font_get_spacing**(font_rid: [RID](class_rid.md#class-rid), spacing: [SpacingType](class_textserver.md#enum-textserver-spacingtype)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-spacing)

Returns the spacing for `spacing` in pixels (not relative to the font size).

---


<a id="class-textserverextension-private-method-font-get-stretch"></a>

[int](class_int.md#class-int) **_font_get_stretch**(font_rid: [RID](class_rid.md#class-rid)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-stretch)

Returns font stretch amount, compared to a normal width. A percentage value between `50%` and `200%`.

---


<a id="class-textserverextension-private-method-font-get-style"></a>

BitField[[FontStyle](class_textserver.md#enum-textserver-fontstyle)] **_font_get_style**(font_rid: [RID](class_rid.md#class-rid)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-style)

Returns font style flags.

---


<a id="class-textserverextension-private-method-font-get-style-name"></a>

[String](class_string.md#class-string) **_font_get_style_name**(font_rid: [RID](class_rid.md#class-rid)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-style-name)

Returns font style name.

---


<a id="class-textserverextension-private-method-font-get-subpixel-positioning"></a>

[SubpixelPositioning](class_textserver.md#enum-textserver-subpixelpositioning) **_font_get_subpixel_positioning**(font_rid: [RID](class_rid.md#class-rid)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-subpixel-positioning)

Returns font subpixel glyph positioning mode.

---


<a id="class-textserverextension-private-method-font-get-supported-chars"></a>

[String](class_string.md#class-string) **_font_get_supported_chars**(font_rid: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-supported-chars)

Returns a string containing all the characters available in the font.

---


<a id="class-textserverextension-private-method-font-get-supported-glyphs"></a>

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **_font_get_supported_glyphs**(font_rid: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-supported-glyphs)

Returns an array containing all glyph indices in the font.

---


<a id="class-textserverextension-private-method-font-get-texture-count"></a>

[int](class_int.md#class-int) **_font_get_texture_count**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-texture-count)

Returns number of textures used by font cache entry.

---


<a id="class-textserverextension-private-method-font-get-texture-image"></a>

[Image](class_image.md#class-image) **_font_get_texture_image**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-texture-image)

Returns font cache texture image data.

---


<a id="class-textserverextension-private-method-font-get-texture-offsets"></a>

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **_font_get_texture_offsets**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-texture-offsets)

Returns array containing glyph packing data.

---


<a id="class-textserverextension-private-method-font-get-transform"></a>

[Transform2D](class_transform2d.md#class-transform2d) **_font_get_transform**(font_rid: [RID](class_rid.md#class-rid)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-transform)

Returns 2D transform applied to the font outlines.

---


<a id="class-textserverextension-private-method-font-get-underline-position"></a>

[float](class_float.md#class-float) **_font_get_underline_position**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-underline-position)

Returns pixel offset of the underline below the baseline.

---


<a id="class-textserverextension-private-method-font-get-underline-thickness"></a>

[float](class_float.md#class-float) **_font_get_underline_thickness**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-underline-thickness)

Returns thickness of the underline in pixels.

---


<a id="class-textserverextension-private-method-font-get-used-palette"></a>

[int](class_int.md#class-int) **_font_get_used_palette**(font_rid: [RID](class_rid.md#class-rid)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-used-palette)

Returns used palette index.

---


<a id="class-textserverextension-private-method-font-get-variation-coordinates"></a>

[Dictionary](class_dictionary.md#class-dictionary) **_font_get_variation_coordinates**(font_rid: [RID](class_rid.md#class-rid)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-variation-coordinates)

Returns variation coordinates for the specified font cache entry.

---


<a id="class-textserverextension-private-method-font-get-weight"></a>

[int](class_int.md#class-int) **_font_get_weight**(font_rid: [RID](class_rid.md#class-rid)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-get-weight)

Returns weight (boldness) of the font. A value in the `100...999` range, normal font weight is `400`, bold font weight is `700`.

---


<a id="class-textserverextension-private-method-font-has-char"></a>

[bool](class_bool.md#class-bool) **_font_has_char**(font_rid: [RID](class_rid.md#class-rid), char: [int](class_int.md#class-int)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-has-char)

Returns `true` if a Unicode `char` is available in the font.

---


<a id="class-textserverextension-private-method-font-is-allow-system-fallback"></a>

[bool](class_bool.md#class-bool) **_font_is_allow_system_fallback**(font_rid: [RID](class_rid.md#class-rid)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-is-allow-system-fallback)

Returns `true` if system fonts can be automatically used as fallbacks.

---


<a id="class-textserverextension-private-method-font-is-force-autohinter"></a>

[bool](class_bool.md#class-bool) **_font_is_force_autohinter**(font_rid: [RID](class_rid.md#class-rid)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-is-force-autohinter)

Returns `true` if auto-hinting is supported and preferred over font built-in hinting.

---


<a id="class-textserverextension-private-method-font-is-language-supported"></a>

[bool](class_bool.md#class-bool) **_font_is_language_supported**(font_rid: [RID](class_rid.md#class-rid), language: [String](class_string.md#class-string)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-is-language-supported)

Returns `true` if the font supports the given language (as a [ISO 639](https://en.wikipedia.org/wiki/ISO_639-1) code).

---


<a id="class-textserverextension-private-method-font-is-modulate-color-glyphs"></a>

[bool](class_bool.md#class-bool) **_font_is_modulate_color_glyphs**(font_rid: [RID](class_rid.md#class-rid)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-is-modulate-color-glyphs)

Returns `true` if color modulation is applied when drawing the font's colored glyphs.

---


<a id="class-textserverextension-private-method-font-is-multichannel-signed-distance-field"></a>

[bool](class_bool.md#class-bool) **_font_is_multichannel_signed_distance_field**(font_rid: [RID](class_rid.md#class-rid)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-is-multichannel-signed-distance-field)

Returns `true` if glyphs of all sizes are rendered using single multichannel signed distance field generated from the dynamic font vector data.

---


<a id="class-textserverextension-private-method-font-is-script-supported"></a>

[bool](class_bool.md#class-bool) **_font_is_script_supported**(font_rid: [RID](class_rid.md#class-rid), script: [String](class_string.md#class-string)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-is-script-supported)

Returns `true` if the font supports the given script (as a [ISO 15924](https://en.wikipedia.org/wiki/ISO_15924) code).

---


<a id="class-textserverextension-private-method-font-remove-glyph"></a>

void **_font_remove_glyph**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int)) virtual required [🔗](class_textserverextension.md#class-textserverextension-private-method-font-remove-glyph)

Removes specified rendered glyph information from the cache entry.

---


<a id="class-textserverextension-private-method-font-remove-kerning"></a>

void **_font_remove_kerning**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), glyph_pair: [Vector2i](class_vector2i.md#class-vector2i)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-remove-kerning)

Removes kerning override for the pair of glyphs.

---


<a id="class-textserverextension-private-method-font-remove-language-support-override"></a>

void **_font_remove_language_support_override**(font_rid: [RID](class_rid.md#class-rid), language: [String](class_string.md#class-string)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-remove-language-support-override)

Remove language support override.

---


<a id="class-textserverextension-private-method-font-remove-script-support-override"></a>

void **_font_remove_script_support_override**(font_rid: [RID](class_rid.md#class-rid), script: [String](class_string.md#class-string)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-remove-script-support-override)

Removes script support override.

---


<a id="class-textserverextension-private-method-font-remove-size-cache"></a>

void **_font_remove_size_cache**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i)) virtual required [🔗](class_textserverextension.md#class-textserverextension-private-method-font-remove-size-cache)

Removes specified font size from the cache entry.

---


<a id="class-textserverextension-private-method-font-remove-texture"></a>

void **_font_remove_texture**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int)) virtual required [🔗](class_textserverextension.md#class-textserverextension-private-method-font-remove-texture)

Removes specified texture from the cache entry.

---


<a id="class-textserverextension-private-method-font-render-glyph"></a>

void **_font_render_glyph**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), index: [int](class_int.md#class-int)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-render-glyph)

Renders specified glyph to the font cache texture.

---


<a id="class-textserverextension-private-method-font-render-range"></a>

void **_font_render_range**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), start: [int](class_int.md#class-int), end: [int](class_int.md#class-int)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-render-range)

Renders the range of characters to the font cache texture.

---


<a id="class-textserverextension-private-method-font-set-allow-system-fallback"></a>

void **_font_set_allow_system_fallback**(font_rid: [RID](class_rid.md#class-rid), allow_system_fallback: [bool](class_bool.md#class-bool)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-allow-system-fallback)

If set to `true`, system fonts can be automatically used as fallbacks.

---


<a id="class-textserverextension-private-method-font-set-antialiasing"></a>

void **_font_set_antialiasing**(font_rid: [RID](class_rid.md#class-rid), antialiasing: [FontAntialiasing](class_textserver.md#enum-textserver-fontantialiasing)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-antialiasing)

Sets font anti-aliasing mode.

---


<a id="class-textserverextension-private-method-font-set-ascent"></a>

void **_font_set_ascent**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), ascent: [float](class_float.md#class-float)) virtual required [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-ascent)

Sets the font ascent (number of pixels above the baseline).

---


<a id="class-textserverextension-private-method-font-set-baseline-offset"></a>

void **_font_set_baseline_offset**(font_rid: [RID](class_rid.md#class-rid), baseline_offset: [float](class_float.md#class-float)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-baseline-offset)

Sets extra baseline offset (as a fraction of font height).

---


<a id="class-textserverextension-private-method-font-set-data"></a>

void **_font_set_data**(font_rid: [RID](class_rid.md#class-rid), data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-data)

Sets font source data, e.g contents of the dynamic font source file.

---


<a id="class-textserverextension-private-method-font-set-data-ptr"></a>

void **_font_set_data_ptr**(font_rid: [RID](class_rid.md#class-rid), data_ptr: `const uint8_t*`, data_size: [int](class_int.md#class-int)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-data-ptr)

Sets pointer to the font source data, e.g contents of the dynamic font source file.

---


<a id="class-textserverextension-private-method-font-set-descent"></a>

void **_font_set_descent**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), descent: [float](class_float.md#class-float)) virtual required [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-descent)

Sets the font descent (number of pixels below the baseline).

---


<a id="class-textserverextension-private-method-font-set-disable-embedded-bitmaps"></a>

void **_font_set_disable_embedded_bitmaps**(font_rid: [RID](class_rid.md#class-rid), disable_embedded_bitmaps: [bool](class_bool.md#class-bool)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-disable-embedded-bitmaps)

If set to `true`, embedded font bitmap loading is disabled.

---


<a id="class-textserverextension-private-method-font-set-embolden"></a>

void **_font_set_embolden**(font_rid: [RID](class_rid.md#class-rid), strength: [float](class_float.md#class-float)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-embolden)

Sets font embolden strength. If `strength` is not equal to zero, emboldens the font outlines. Negative values reduce the outline thickness.

---


<a id="class-textserverextension-private-method-font-set-face-index"></a>

void **_font_set_face_index**(font_rid: [RID](class_rid.md#class-rid), face_index: [int](class_int.md#class-int)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-face-index)

Sets an active face index in the TrueType / OpenType collection.

---


<a id="class-textserverextension-private-method-font-set-fixed-size"></a>

void **_font_set_fixed_size**(font_rid: [RID](class_rid.md#class-rid), fixed_size: [int](class_int.md#class-int)) virtual required [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-fixed-size)

Sets bitmap font fixed size. If set to value greater than zero, same cache entry will be used for all font sizes.

---


<a id="class-textserverextension-private-method-font-set-fixed-size-scale-mode"></a>

void **_font_set_fixed_size_scale_mode**(font_rid: [RID](class_rid.md#class-rid), fixed_size_scale_mode: [FixedSizeScaleMode](class_textserver.md#enum-textserver-fixedsizescalemode)) virtual required [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-fixed-size-scale-mode)

Sets bitmap font scaling mode. This property is used only if `fixed_size` is greater than zero.

---


<a id="class-textserverextension-private-method-font-set-force-autohinter"></a>

void **_font_set_force_autohinter**(font_rid: [RID](class_rid.md#class-rid), force_autohinter: [bool](class_bool.md#class-bool)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-force-autohinter)

If set to `true` auto-hinting is preferred over font built-in hinting.

---


<a id="class-textserverextension-private-method-font-set-generate-mipmaps"></a>

void **_font_set_generate_mipmaps**(font_rid: [RID](class_rid.md#class-rid), generate_mipmaps: [bool](class_bool.md#class-bool)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-generate-mipmaps)

If set to `true` font texture mipmap generation is enabled.

---


<a id="class-textserverextension-private-method-font-set-global-oversampling"></a>

void **_font_set_global_oversampling**(oversampling: [float](class_float.md#class-float)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-global-oversampling)

Sets oversampling factor, shared by all font in the TextServer.

---


<a id="class-textserverextension-private-method-font-set-glyph-advance"></a>

void **_font_set_glyph_advance**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), glyph: [int](class_int.md#class-int), advance: [Vector2](class_vector2.md#class-vector2)) virtual required [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-glyph-advance)

Sets glyph advance (offset of the next glyph).

---


<a id="class-textserverextension-private-method-font-set-glyph-offset"></a>

void **_font_set_glyph_offset**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int), offset: [Vector2](class_vector2.md#class-vector2)) virtual required [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-glyph-offset)

Sets glyph offset from the baseline.

---


<a id="class-textserverextension-private-method-font-set-glyph-size"></a>

void **_font_set_glyph_size**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int), gl_size: [Vector2](class_vector2.md#class-vector2)) virtual required [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-glyph-size)

Sets size of the glyph.

---


<a id="class-textserverextension-private-method-font-set-glyph-texture-idx"></a>

void **_font_set_glyph_texture_idx**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int), texture_idx: [int](class_int.md#class-int)) virtual required [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-glyph-texture-idx)

Sets index of the cache texture containing the glyph.

---


<a id="class-textserverextension-private-method-font-set-glyph-uv-rect"></a>

void **_font_set_glyph_uv_rect**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int), uv_rect: [Rect2](class_rect2.md#class-rect2)) virtual required [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-glyph-uv-rect)

Sets rectangle in the cache texture containing the glyph.

---


<a id="class-textserverextension-private-method-font-set-hinting"></a>

void **_font_set_hinting**(font_rid: [RID](class_rid.md#class-rid), hinting: [Hinting](class_textserver.md#enum-textserver-hinting)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-hinting)

Sets font hinting mode. Used by dynamic fonts only.

---


<a id="class-textserverextension-private-method-font-set-keep-rounding-remainders"></a>

void **_font_set_keep_rounding_remainders**(font_rid: [RID](class_rid.md#class-rid), keep_rounding_remainders: [bool](class_bool.md#class-bool)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-keep-rounding-remainders)

Sets glyph position rounding behavior. If set to `true`, when aligning glyphs to the pixel boundaries rounding remainders are accumulated to ensure more uniform glyph distribution. This setting has no effect if subpixel positioning is enabled.

---


<a id="class-textserverextension-private-method-font-set-kerning"></a>

void **_font_set_kerning**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), glyph_pair: [Vector2i](class_vector2i.md#class-vector2i), kerning: [Vector2](class_vector2.md#class-vector2)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-kerning)

Sets kerning for the pair of glyphs.

---


<a id="class-textserverextension-private-method-font-set-language-support-override"></a>

void **_font_set_language_support_override**(font_rid: [RID](class_rid.md#class-rid), language: [String](class_string.md#class-string), supported: [bool](class_bool.md#class-bool)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-language-support-override)

Adds override for [_font_is_language_supported()](class_textserverextension.md#class-textserverextension-private-method-font-is-language-supported).

---


<a id="class-textserverextension-private-method-font-set-modulate-color-glyphs"></a>

void **_font_set_modulate_color_glyphs**(font_rid: [RID](class_rid.md#class-rid), modulate: [bool](class_bool.md#class-bool)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-modulate-color-glyphs)

If set to `true`, color modulation is applied when drawing colored glyphs, otherwise it's applied to the monochrome glyphs only.

---


<a id="class-textserverextension-private-method-font-set-msdf-pixel-range"></a>

void **_font_set_msdf_pixel_range**(font_rid: [RID](class_rid.md#class-rid), msdf_pixel_range: [int](class_int.md#class-int)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-msdf-pixel-range)

Sets the width of the range around the shape between the minimum and maximum representable signed distance.

---


<a id="class-textserverextension-private-method-font-set-msdf-size"></a>

void **_font_set_msdf_size**(font_rid: [RID](class_rid.md#class-rid), msdf_size: [int](class_int.md#class-int)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-msdf-size)

Sets source font size used to generate MSDF textures.

---


<a id="class-textserverextension-private-method-font-set-multichannel-signed-distance-field"></a>

void **_font_set_multichannel_signed_distance_field**(font_rid: [RID](class_rid.md#class-rid), msdf: [bool](class_bool.md#class-bool)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-multichannel-signed-distance-field)

If set to `true`, glyphs of all sizes are rendered using single multichannel signed distance field generated from the dynamic font vector data. MSDF rendering allows displaying the font at any scaling factor without blurriness, and without incurring a CPU cost when the font size changes (since the font no longer needs to be rasterized on the CPU). As a downside, font hinting is not available with MSDF. The lack of font hinting may result in less crisp and less readable fonts at small sizes.

---


<a id="class-textserverextension-private-method-font-set-name"></a>

void **_font_set_name**(font_rid: [RID](class_rid.md#class-rid), name: [String](class_string.md#class-string)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-name)

Sets the font family name.

---


<a id="class-textserverextension-private-method-font-set-opentype-feature-overrides"></a>

void **_font_set_opentype_feature_overrides**(font_rid: [RID](class_rid.md#class-rid), overrides: [Dictionary](class_dictionary.md#class-dictionary)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-opentype-feature-overrides)

Sets font OpenType feature set override.

---


<a id="class-textserverextension-private-method-font-set-oversampling"></a>

void **_font_set_oversampling**(font_rid: [RID](class_rid.md#class-rid), oversampling: [float](class_float.md#class-float)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-oversampling)

If set to a positive value, overrides the oversampling factor of the viewport this font is used in. See [Viewport.oversampling](class_viewport.md#class-viewport-property-oversampling). This value doesn't override the `oversampling` parameter of `draw_*` methods. Used by dynamic fonts only.

---


<a id="class-textserverextension-private-method-font-set-palette-custom-colors"></a>

void **_font_set_palette_custom_colors**(font_rid: [RID](class_rid.md#class-rid), colors: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-palette-custom-colors)

Sets array of custom colors to override predefined palette. Set to empty array to reset overrides. Use `Color(0, 0, 0, 0)`, to keep predefined palette color at specific position.

---


<a id="class-textserverextension-private-method-font-set-scale"></a>

void **_font_set_scale**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), scale: [float](class_float.md#class-float)) virtual required [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-scale)

Sets scaling factor of the color bitmap font.

---


<a id="class-textserverextension-private-method-font-set-script-support-override"></a>

void **_font_set_script_support_override**(font_rid: [RID](class_rid.md#class-rid), script: [String](class_string.md#class-string), supported: [bool](class_bool.md#class-bool)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-script-support-override)

Adds override for [_font_is_script_supported()](class_textserverextension.md#class-textserverextension-private-method-font-is-script-supported).

---


<a id="class-textserverextension-private-method-font-set-spacing"></a>

void **_font_set_spacing**(font_rid: [RID](class_rid.md#class-rid), spacing: [SpacingType](class_textserver.md#enum-textserver-spacingtype), value: [int](class_int.md#class-int)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-spacing)

Sets the spacing for `spacing` to `value` in pixels (not relative to the font size).

---


<a id="class-textserverextension-private-method-font-set-stretch"></a>

void **_font_set_stretch**(font_rid: [RID](class_rid.md#class-rid), stretch: [int](class_int.md#class-int)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-stretch)

Sets font stretch amount, compared to a normal width. A percentage value between `50%` and `200%`.

---


<a id="class-textserverextension-private-method-font-set-style"></a>

void **_font_set_style**(font_rid: [RID](class_rid.md#class-rid), style: BitField[[FontStyle](class_textserver.md#enum-textserver-fontstyle)]) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-style)

Sets the font style flags.

---


<a id="class-textserverextension-private-method-font-set-style-name"></a>

void **_font_set_style_name**(font_rid: [RID](class_rid.md#class-rid), name_style: [String](class_string.md#class-string)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-style-name)

Sets the font style name.

---


<a id="class-textserverextension-private-method-font-set-subpixel-positioning"></a>

void **_font_set_subpixel_positioning**(font_rid: [RID](class_rid.md#class-rid), subpixel_positioning: [SubpixelPositioning](class_textserver.md#enum-textserver-subpixelpositioning)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-subpixel-positioning)

Sets font subpixel glyph positioning mode.

---


<a id="class-textserverextension-private-method-font-set-texture-image"></a>

void **_font_set_texture_image**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int), image: [Image](class_image.md#class-image)) virtual required [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-texture-image)

Sets font cache texture image data.

---


<a id="class-textserverextension-private-method-font-set-texture-offsets"></a>

void **_font_set_texture_offsets**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int), offset: [PackedInt32Array](class_packedint32array.md#class-packedint32array)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-texture-offsets)

Sets array containing glyph packing data.

---


<a id="class-textserverextension-private-method-font-set-transform"></a>

void **_font_set_transform**(font_rid: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-transform)

Sets 2D transform, applied to the font outlines, can be used for slanting, flipping, and rotating glyphs.

---


<a id="class-textserverextension-private-method-font-set-underline-position"></a>

void **_font_set_underline_position**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), underline_position: [float](class_float.md#class-float)) virtual required [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-underline-position)

Sets pixel offset of the underline below the baseline.

---


<a id="class-textserverextension-private-method-font-set-underline-thickness"></a>

void **_font_set_underline_thickness**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), underline_thickness: [float](class_float.md#class-float)) virtual required [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-underline-thickness)

Sets thickness of the underline in pixels.

---


<a id="class-textserverextension-private-method-font-set-used-palette"></a>

void **_font_set_used_palette**(font_rid: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-used-palette)

Sets used palette index.

---


<a id="class-textserverextension-private-method-font-set-variation-coordinates"></a>

void **_font_set_variation_coordinates**(font_rid: [RID](class_rid.md#class-rid), variation_coordinates: [Dictionary](class_dictionary.md#class-dictionary)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-variation-coordinates)

Sets variation coordinates for the specified font cache entry.

---


<a id="class-textserverextension-private-method-font-set-weight"></a>

void **_font_set_weight**(font_rid: [RID](class_rid.md#class-rid), weight: [int](class_int.md#class-int)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-font-set-weight)

Sets weight (boldness) of the font. A value in the `100...999` range, normal font weight is `400`, bold font weight is `700`.

---


<a id="class-textserverextension-private-method-font-supported-feature-list"></a>

[Dictionary](class_dictionary.md#class-dictionary) **_font_supported_feature_list**(font_rid: [RID](class_rid.md#class-rid)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-supported-feature-list)

Returns the dictionary of the supported OpenType features.

---


<a id="class-textserverextension-private-method-font-supported-variation-list"></a>

[Dictionary](class_dictionary.md#class-dictionary) **_font_supported_variation_list**(font_rid: [RID](class_rid.md#class-rid)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-font-supported-variation-list)

Returns the dictionary of the supported OpenType variation coordinates.

---


<a id="class-textserverextension-private-method-format-number"></a>

[String](class_string.md#class-string) **_format_number**(number: [String](class_string.md#class-string), language: [String](class_string.md#class-string)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-format-number)

**Deprecated:** Use [TranslationServer.format_number()](class_translationserver.md#class-translationserver-method-format-number) instead.

Converts a number from Western Arabic (0..9) to the numeral system used in the given `language`.

If `language` is an empty string, the active locale will be used.

---


<a id="class-textserverextension-private-method-free-rid"></a>

void **_free_rid**(rid: [RID](class_rid.md#class-rid)) virtual required [🔗](class_textserverextension.md#class-textserverextension-private-method-free-rid)

Frees an object created by this [TextServer](class_textserver.md#class-textserver).

---


<a id="class-textserverextension-private-method-get-features"></a>

[int](class_int.md#class-int) **_get_features**() virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-get-features)

Returns text server features, see [Feature](class_textserver.md#enum-textserver-feature).

---


<a id="class-textserverextension-private-method-get-hex-code-box-size"></a>

[Vector2](class_vector2.md#class-vector2) **_get_hex_code_box_size**(size: [int](class_int.md#class-int), index: [int](class_int.md#class-int)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-get-hex-code-box-size)

Returns size of the replacement character (box with character hexadecimal code that is drawn in place of invalid characters).

---


<a id="class-textserverextension-private-method-get-name"></a>

[String](class_string.md#class-string) **_get_name**() virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-get-name)

Returns the name of the server interface.

---


<a id="class-textserverextension-private-method-get-support-data"></a>

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **_get_support_data**() virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-get-support-data)

Returns default TextServer database (e.g. ICU break iterators and dictionaries).

---


<a id="class-textserverextension-private-method-get-support-data-filename"></a>

[String](class_string.md#class-string) **_get_support_data_filename**() virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-get-support-data-filename)

Returns default TextServer database (e.g. ICU break iterators and dictionaries) filename.

---


<a id="class-textserverextension-private-method-get-support-data-info"></a>

[String](class_string.md#class-string) **_get_support_data_info**() virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-get-support-data-info)

Returns TextServer database (e.g. ICU break iterators and dictionaries) description.

---


<a id="class-textserverextension-private-method-has"></a>

[bool](class_bool.md#class-bool) **_has**(rid: [RID](class_rid.md#class-rid)) virtual required [🔗](class_textserverextension.md#class-textserverextension-private-method-has)

Returns `true` if `rid` is valid resource owned by this text server.

---


<a id="class-textserverextension-private-method-has-feature"></a>

[bool](class_bool.md#class-bool) **_has_feature**(feature: [Feature](class_textserver.md#enum-textserver-feature)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-has-feature)

Returns `true` if the server supports a feature.

---


<a id="class-textserverextension-private-method-is-confusable"></a>

[int](class_int.md#class-int) **_is_confusable**(string: [String](class_string.md#class-string), dict: [PackedStringArray](class_packedstringarray.md#class-packedstringarray)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-is-confusable)

Returns index of the first string in `dict` which is visually confusable with the `string`, or `-1` if none is found.

---


<a id="class-textserverextension-private-method-is-locale-right-to-left"></a>

[bool](class_bool.md#class-bool) **_is_locale_right_to_left**(locale: [String](class_string.md#class-string)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-is-locale-right-to-left)

Returns `true` if locale is right-to-left.

---


<a id="class-textserverextension-private-method-is-locale-using-support-data"></a>

[bool](class_bool.md#class-bool) **_is_locale_using_support_data**(locale: [String](class_string.md#class-string)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-is-locale-using-support-data)

Returns `true` if the locale requires text server support data for line/word breaking.

---


<a id="class-textserverextension-private-method-is-valid-identifier"></a>

[bool](class_bool.md#class-bool) **_is_valid_identifier**(string: [String](class_string.md#class-string)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-is-valid-identifier)

Returns `true` if `string` is a valid identifier.

---


<a id="class-textserverextension-private-method-is-valid-letter"></a>

[bool](class_bool.md#class-bool) **_is_valid_letter**(unicode: [int](class_int.md#class-int)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-is-valid-letter)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-textserverextension-private-method-load-support-data"></a>

[bool](class_bool.md#class-bool) **_load_support_data**(filename: [String](class_string.md#class-string)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-load-support-data)

Loads optional TextServer database (e.g. ICU break iterators and dictionaries).

---


<a id="class-textserverextension-private-method-name-to-tag"></a>

[int](class_int.md#class-int) **_name_to_tag**(name: [String](class_string.md#class-string)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-name-to-tag)

Converts the given readable name of a feature, variation, script, or language to an OpenType tag.

---


<a id="class-textserverextension-private-method-parse-number"></a>

[String](class_string.md#class-string) **_parse_number**(number: [String](class_string.md#class-string), language: [String](class_string.md#class-string)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-parse-number)

**Deprecated:** Use [TranslationServer.parse_number()](class_translationserver.md#class-translationserver-method-parse-number) instead.

Converts `number` from the numeral system used in the given `language` to Western Arabic (0..9).

If `language` is an empty string, the active locale will be used.

---


<a id="class-textserverextension-private-method-parse-structured-text"></a>

[Array](class_array.md#class-array)[[Vector3i](class_vector3i.md#class-vector3i)] **_parse_structured_text**(parser_type: [StructuredTextParser](class_textserver.md#enum-textserver-structuredtextparser), args: [Array](class_array.md#class-array), text: [String](class_string.md#class-string)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-parse-structured-text)

Default implementation of the BiDi algorithm override function.

---


<a id="class-textserverextension-private-method-percent-sign"></a>

[String](class_string.md#class-string) **_percent_sign**(language: [String](class_string.md#class-string)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-percent-sign)

**Deprecated:** Use [TranslationServer.get_percent_sign()](class_translationserver.md#class-translationserver-method-get-percent-sign) instead.

Returns percent sign used in the given `language`.

---


<a id="class-textserverextension-private-method-reference-oversampling-level"></a>

void **_reference_oversampling_level**(oversampling: [float](class_float.md#class-float)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-reference-oversampling-level)

Increases the reference count of the specified oversampling level. This method is called by [Viewport](class_viewport.md#class-viewport), and should not be used directly.

---


<a id="class-textserverextension-private-method-save-support-data"></a>

[bool](class_bool.md#class-bool) **_save_support_data**(filename: [String](class_string.md#class-string)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-save-support-data)

Saves optional TextServer database (e.g. ICU break iterators and dictionaries) to the file.

---


<a id="class-textserverextension-private-method-shaped-get-run-count"></a>

[int](class_int.md#class-int) **_shaped_get_run_count**(shaped: [RID](class_rid.md#class-rid)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-get-run-count)

Returns the number of uniform text runs in the buffer.

---


<a id="class-textserverextension-private-method-shaped-get-run-direction"></a>

[Direction](class_textserver.md#enum-textserver-direction) **_shaped_get_run_direction**(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-get-run-direction)

Returns the direction of the `index` text run (in visual order).

---


<a id="class-textserverextension-private-method-shaped-get-run-font-rid"></a>

[RID](class_rid.md#class-rid) **_shaped_get_run_font_rid**(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-get-run-font-rid)

Returns the font RID of the `index` text run (in visual order).

---


<a id="class-textserverextension-private-method-shaped-get-run-font-size"></a>

[int](class_int.md#class-int) **_shaped_get_run_font_size**(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-get-run-font-size)

Returns the font size of the `index` text run (in visual order).

---


<a id="class-textserverextension-private-method-shaped-get-run-glyph-range"></a>

[Vector2i](class_vector2i.md#class-vector2i) **_shaped_get_run_glyph_range**(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-get-run-glyph-range)

Returns the glyph range of the `index` text run (in visual order).

---


<a id="class-textserverextension-private-method-shaped-get-run-language"></a>

[String](class_string.md#class-string) **_shaped_get_run_language**(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-get-run-language)

Returns the language of the `index` text run (in visual order).

---


<a id="class-textserverextension-private-method-shaped-get-run-object"></a>

[Variant](class_variant.md#class-variant) **_shaped_get_run_object**(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-get-run-object)

Returns the embedded object of the `index` text run (in visual order).

---


<a id="class-textserverextension-private-method-shaped-get-run-range"></a>

[Vector2i](class_vector2i.md#class-vector2i) **_shaped_get_run_range**(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-get-run-range)

Returns the source text range of the `index` text run (in visual order).

---


<a id="class-textserverextension-private-method-shaped-get-run-text"></a>

[String](class_string.md#class-string) **_shaped_get_run_text**(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-get-run-text)

Returns the source text of the `index` text run (in visual order).

---


<a id="class-textserverextension-private-method-shaped-get-span-count"></a>

[int](class_int.md#class-int) **_shaped_get_span_count**(shaped: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-get-span-count)

Returns number of text spans added using [_shaped_text_add_string()](class_textserverextension.md#class-textserverextension-private-method-shaped-text-add-string) or [_shaped_text_add_object()](class_textserverextension.md#class-textserverextension-private-method-shaped-text-add-object).

---


<a id="class-textserverextension-private-method-shaped-get-span-embedded-object"></a>

[Variant](class_variant.md#class-variant) **_shaped_get_span_embedded_object**(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-get-span-embedded-object)

Returns text embedded object key.

---


<a id="class-textserverextension-private-method-shaped-get-span-meta"></a>

[Variant](class_variant.md#class-variant) **_shaped_get_span_meta**(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-get-span-meta)

Returns text span metadata.

---


<a id="class-textserverextension-private-method-shaped-get-span-object"></a>

[Variant](class_variant.md#class-variant) **_shaped_get_span_object**(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-get-span-object)

Returns the text span embedded object key.

---


<a id="class-textserverextension-private-method-shaped-get-span-text"></a>

[String](class_string.md#class-string) **_shaped_get_span_text**(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-get-span-text)

Returns the text span source text.

---


<a id="class-textserverextension-private-method-shaped-get-text"></a>

[String](class_string.md#class-string) **_shaped_get_text**(shaped: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-get-text)

Returns the text buffer source text, including object replacement characters.

---


<a id="class-textserverextension-private-method-shaped-set-span-update-font"></a>

void **_shaped_set_span_update_font**(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int), fonts: [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)], size: [int](class_int.md#class-int), opentype_features: [Dictionary](class_dictionary.md#class-dictionary)) virtual required [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-set-span-update-font)

Changes text span font, font size, and OpenType features, without changing the text.

---


<a id="class-textserverextension-private-method-shaped-text-add-object"></a>

[bool](class_bool.md#class-bool) **_shaped_text_add_object**(shaped: [RID](class_rid.md#class-rid), key: [Variant](class_variant.md#class-variant), size: [Vector2](class_vector2.md#class-vector2), inline_align: [InlineAlignment](class_@globalscope.md#enum-globalscope-inlinealignment), length: [int](class_int.md#class-int), baseline: [float](class_float.md#class-float)) virtual required [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-add-object)

Adds inline object to the text buffer, `key` must be unique. In the text, object is represented as `length` object replacement characters.

---


<a id="class-textserverextension-private-method-shaped-text-add-string"></a>

[bool](class_bool.md#class-bool) **_shaped_text_add_string**(shaped: [RID](class_rid.md#class-rid), text: [String](class_string.md#class-string), fonts: [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)], size: [int](class_int.md#class-int), opentype_features: [Dictionary](class_dictionary.md#class-dictionary), language: [String](class_string.md#class-string), meta: [Variant](class_variant.md#class-variant)) virtual required [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-add-string)

Adds text span and font to draw it to the text buffer.

---


<a id="class-textserverextension-private-method-shaped-text-clear"></a>

void **_shaped_text_clear**(shaped: [RID](class_rid.md#class-rid)) virtual required [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-clear)

Clears text buffer (removes text and inline objects).

---


<a id="class-textserverextension-private-method-shaped-text-closest-character-pos"></a>

[int](class_int.md#class-int) **_shaped_text_closest_character_pos**(shaped: [RID](class_rid.md#class-rid), pos: [int](class_int.md#class-int)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-closest-character-pos)

Returns composite character position closest to the `pos`.

---


<a id="class-textserverextension-private-method-shaped-text-draw"></a>

void **_shaped_text_draw**(shaped: [RID](class_rid.md#class-rid), canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), clip_l: [float](class_float.md#class-float), clip_r: [float](class_float.md#class-float), color: [Color](class_color.md#class-color), oversampling: [float](class_float.md#class-float)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-draw)

Draw shaped text into a canvas item at a given position, with `color`. `pos` specifies the leftmost point of the baseline (for horizontal layout) or topmost point of the baseline (for vertical layout). If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

---


<a id="class-textserverextension-private-method-shaped-text-draw-outline"></a>

void **_shaped_text_draw_outline**(shaped: [RID](class_rid.md#class-rid), canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), clip_l: [float](class_float.md#class-float), clip_r: [float](class_float.md#class-float), outline_size: [int](class_int.md#class-int), color: [Color](class_color.md#class-color), oversampling: [float](class_float.md#class-float)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-draw-outline)

Draw the outline of the shaped text into a canvas item at a given position, with `color`. `pos` specifies the leftmost point of the baseline (for horizontal layout) or topmost point of the baseline (for vertical layout). If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

---


<a id="class-textserverextension-private-method-shaped-text-duplicate"></a>

[RID](class_rid.md#class-rid) **_shaped_text_duplicate**(shaped: [RID](class_rid.md#class-rid)) virtual required [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-duplicate)

Duplicates shaped text buffer.

---


<a id="class-textserverextension-private-method-shaped-text-fit-to-width"></a>

[float](class_float.md#class-float) **_shaped_text_fit_to_width**(shaped: [RID](class_rid.md#class-rid), width: [float](class_float.md#class-float), justification_flags: BitField[[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)]) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-fit-to-width)

Adjusts text width to fit to specified width, returns new text width.

---


<a id="class-textserverextension-private-method-shaped-text-get-ascent"></a>

[float](class_float.md#class-float) **_shaped_text_get_ascent**(shaped: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-ascent)

Returns the text ascent (number of pixels above the baseline for horizontal layout or to the left of baseline for vertical).

---


<a id="class-textserverextension-private-method-shaped-text-get-carets"></a>

void **_shaped_text_get_carets**(shaped: [RID](class_rid.md#class-rid), position: [int](class_int.md#class-int), r_caret: `CaretInfo*`) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-carets)

Returns shapes of the carets corresponding to the character offset `position` in the text. Returned caret shape is 1 pixel wide rectangle.

---


<a id="class-textserverextension-private-method-shaped-text-get-character-breaks"></a>

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **_shaped_text_get_character_breaks**(shaped: [RID](class_rid.md#class-rid)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-character-breaks)

Returns array of the composite character boundaries.

---


<a id="class-textserverextension-private-method-shaped-text-get-custom-ellipsis"></a>

[int](class_int.md#class-int) **_shaped_text_get_custom_ellipsis**(shaped: [RID](class_rid.md#class-rid)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-custom-ellipsis)

Returns ellipsis character used for text clipping.

---


<a id="class-textserverextension-private-method-shaped-text-get-custom-punctuation"></a>

[String](class_string.md#class-string) **_shaped_text_get_custom_punctuation**(shaped: [RID](class_rid.md#class-rid)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-custom-punctuation)

Returns custom punctuation character list, used for word breaking. If set to empty string, server defaults are used.

---


<a id="class-textserverextension-private-method-shaped-text-get-descent"></a>

[float](class_float.md#class-float) **_shaped_text_get_descent**(shaped: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-descent)

Returns the text descent (number of pixels below the baseline for horizontal layout or to the right of baseline for vertical).

---


<a id="class-textserverextension-private-method-shaped-text-get-direction"></a>

[Direction](class_textserver.md#enum-textserver-direction) **_shaped_text_get_direction**(shaped: [RID](class_rid.md#class-rid)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-direction)

Returns direction of the text.

---


<a id="class-textserverextension-private-method-shaped-text-get-dominant-direction-in-range"></a>

[int](class_int.md#class-int) **_shaped_text_get_dominant_direction_in_range**(shaped: [RID](class_rid.md#class-rid), start: [int](class_int.md#class-int), end: [int](class_int.md#class-int)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-dominant-direction-in-range)

Returns dominant direction of in the range of text.

---


<a id="class-textserverextension-private-method-shaped-text-get-ellipsis-glyph-count"></a>

[int](class_int.md#class-int) **_shaped_text_get_ellipsis_glyph_count**(shaped: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-ellipsis-glyph-count)

Returns number of glyphs in the ellipsis.

---


<a id="class-textserverextension-private-method-shaped-text-get-ellipsis-glyphs"></a>

`const Glyph*` **_shaped_text_get_ellipsis_glyphs**(shaped: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-ellipsis-glyphs)

Returns array of the glyphs in the ellipsis.

---


<a id="class-textserverextension-private-method-shaped-text-get-ellipsis-pos"></a>

[int](class_int.md#class-int) **_shaped_text_get_ellipsis_pos**(shaped: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-ellipsis-pos)

Returns position of the ellipsis.

---


<a id="class-textserverextension-private-method-shaped-text-get-glyph-count"></a>

[int](class_int.md#class-int) **_shaped_text_get_glyph_count**(shaped: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-glyph-count)

Returns number of glyphs in the buffer.

---


<a id="class-textserverextension-private-method-shaped-text-get-glyphs"></a>

`const Glyph*` **_shaped_text_get_glyphs**(shaped: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-glyphs)

Returns an array of glyphs in the visual order.

---


<a id="class-textserverextension-private-method-shaped-text-get-grapheme-bounds"></a>

[Vector2](class_vector2.md#class-vector2) **_shaped_text_get_grapheme_bounds**(shaped: [RID](class_rid.md#class-rid), pos: [int](class_int.md#class-int)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-grapheme-bounds)

Returns composite character's bounds as offsets from the start of the line.

---


<a id="class-textserverextension-private-method-shaped-text-get-inferred-direction"></a>

[Direction](class_textserver.md#enum-textserver-direction) **_shaped_text_get_inferred_direction**(shaped: [RID](class_rid.md#class-rid)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-inferred-direction)

Returns direction of the text, inferred by the BiDi algorithm.

---


<a id="class-textserverextension-private-method-shaped-text-get-line-breaks"></a>

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **_shaped_text_get_line_breaks**(shaped: [RID](class_rid.md#class-rid), width: [float](class_float.md#class-float), start: [int](class_int.md#class-int), break_flags: BitField[[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)]) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-line-breaks)

Breaks text to the lines and returns character ranges for each line.

---


<a id="class-textserverextension-private-method-shaped-text-get-line-breaks-adv"></a>

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **_shaped_text_get_line_breaks_adv**(shaped: [RID](class_rid.md#class-rid), width: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array), start: [int](class_int.md#class-int), once: [bool](class_bool.md#class-bool), break_flags: BitField[[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)]) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-line-breaks-adv)

Breaks text to the lines and columns. Returns character ranges for each segment.

---


<a id="class-textserverextension-private-method-shaped-text-get-object-glyph"></a>

[int](class_int.md#class-int) **_shaped_text_get_object_glyph**(shaped: [RID](class_rid.md#class-rid), key: [Variant](class_variant.md#class-variant)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-object-glyph)

Returns the glyph index of the inline object.

---


<a id="class-textserverextension-private-method-shaped-text-get-object-range"></a>

[Vector2i](class_vector2i.md#class-vector2i) **_shaped_text_get_object_range**(shaped: [RID](class_rid.md#class-rid), key: [Variant](class_variant.md#class-variant)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-object-range)

Returns the character range of the inline object.

---


<a id="class-textserverextension-private-method-shaped-text-get-object-rect"></a>

[Rect2](class_rect2.md#class-rect2) **_shaped_text_get_object_rect**(shaped: [RID](class_rid.md#class-rid), key: [Variant](class_variant.md#class-variant)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-object-rect)

Returns bounding rectangle of the inline object.

---


<a id="class-textserverextension-private-method-shaped-text-get-objects"></a>

[Array](class_array.md#class-array) **_shaped_text_get_objects**(shaped: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-objects)

Returns array of inline objects.

---


<a id="class-textserverextension-private-method-shaped-text-get-orientation"></a>

[Orientation](class_textserver.md#enum-textserver-orientation) **_shaped_text_get_orientation**(shaped: [RID](class_rid.md#class-rid)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-orientation)

Returns text orientation.

---


<a id="class-textserverextension-private-method-shaped-text-get-parent"></a>

[RID](class_rid.md#class-rid) **_shaped_text_get_parent**(shaped: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-parent)

Returns the parent buffer from which the substring originates.

---


<a id="class-textserverextension-private-method-shaped-text-get-preserve-control"></a>

[bool](class_bool.md#class-bool) **_shaped_text_get_preserve_control**(shaped: [RID](class_rid.md#class-rid)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-preserve-control)

Returns `true` if text buffer is configured to display control characters.

---


<a id="class-textserverextension-private-method-shaped-text-get-preserve-invalid"></a>

[bool](class_bool.md#class-bool) **_shaped_text_get_preserve_invalid**(shaped: [RID](class_rid.md#class-rid)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-preserve-invalid)

Returns `true` if text buffer is configured to display hexadecimal codes in place of invalid characters.

---


<a id="class-textserverextension-private-method-shaped-text-get-range"></a>

[Vector2i](class_vector2i.md#class-vector2i) **_shaped_text_get_range**(shaped: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-range)

Returns substring buffer character range in the parent buffer.

---


<a id="class-textserverextension-private-method-shaped-text-get-selection"></a>

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **_shaped_text_get_selection**(shaped: [RID](class_rid.md#class-rid), start: [int](class_int.md#class-int), end: [int](class_int.md#class-int)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-selection)

Returns selection rectangles for the specified character range.

---


<a id="class-textserverextension-private-method-shaped-text-get-size"></a>

[Vector2](class_vector2.md#class-vector2) **_shaped_text_get_size**(shaped: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-size)

Returns size of the text.

---


<a id="class-textserverextension-private-method-shaped-text-get-spacing"></a>

[int](class_int.md#class-int) **_shaped_text_get_spacing**(shaped: [RID](class_rid.md#class-rid), spacing: [SpacingType](class_textserver.md#enum-textserver-spacingtype)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-spacing)

Returns extra spacing added between glyphs or lines in pixels.

---


<a id="class-textserverextension-private-method-shaped-text-get-trim-pos"></a>

[int](class_int.md#class-int) **_shaped_text_get_trim_pos**(shaped: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-trim-pos)

Returns the position of the overrun trim.

---


<a id="class-textserverextension-private-method-shaped-text-get-underline-position"></a>

[float](class_float.md#class-float) **_shaped_text_get_underline_position**(shaped: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-underline-position)

Returns pixel offset of the underline below the baseline.

---


<a id="class-textserverextension-private-method-shaped-text-get-underline-thickness"></a>

[float](class_float.md#class-float) **_shaped_text_get_underline_thickness**(shaped: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-underline-thickness)

Returns thickness of the underline.

---


<a id="class-textserverextension-private-method-shaped-text-get-width"></a>

[float](class_float.md#class-float) **_shaped_text_get_width**(shaped: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-width)

Returns width (for horizontal layout) or height (for vertical) of the text.

---


<a id="class-textserverextension-private-method-shaped-text-get-word-breaks"></a>

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **_shaped_text_get_word_breaks**(shaped: [RID](class_rid.md#class-rid), grapheme_flags: BitField[[GraphemeFlag](class_textserver.md#enum-textserver-graphemeflag)], skip_grapheme_flags: BitField[[GraphemeFlag](class_textserver.md#enum-textserver-graphemeflag)]) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-get-word-breaks)

Breaks text into words and returns array of character ranges. Use `grapheme_flags` to set what characters are used for breaking.

---


<a id="class-textserverextension-private-method-shaped-text-has-object"></a>

[bool](class_bool.md#class-bool) **_shaped_text_has_object**(shaped: [RID](class_rid.md#class-rid), key: [Variant](class_variant.md#class-variant)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-has-object)

Returns `true` if an object with `key` is embedded in this shaped text buffer.

---


<a id="class-textserverextension-private-method-shaped-text-hit-test-grapheme"></a>

[int](class_int.md#class-int) **_shaped_text_hit_test_grapheme**(shaped: [RID](class_rid.md#class-rid), coord: [float](class_float.md#class-float)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-hit-test-grapheme)

Returns grapheme index at the specified pixel offset at the baseline, or `-1` if none is found.

---


<a id="class-textserverextension-private-method-shaped-text-hit-test-position"></a>

[int](class_int.md#class-int) **_shaped_text_hit_test_position**(shaped: [RID](class_rid.md#class-rid), coord: [float](class_float.md#class-float)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-hit-test-position)

Returns caret character offset at the specified pixel offset at the baseline. This function always returns a valid position.

---


<a id="class-textserverextension-private-method-shaped-text-is-ready"></a>

[bool](class_bool.md#class-bool) **_shaped_text_is_ready**(shaped: [RID](class_rid.md#class-rid)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-is-ready)

Returns `true` if buffer is successfully shaped.

---


<a id="class-textserverextension-private-method-shaped-text-next-character-pos"></a>

[int](class_int.md#class-int) **_shaped_text_next_character_pos**(shaped: [RID](class_rid.md#class-rid), pos: [int](class_int.md#class-int)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-next-character-pos)

Returns composite character end position closest to the `pos`.

---


<a id="class-textserverextension-private-method-shaped-text-next-grapheme-pos"></a>

[int](class_int.md#class-int) **_shaped_text_next_grapheme_pos**(shaped: [RID](class_rid.md#class-rid), pos: [int](class_int.md#class-int)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-next-grapheme-pos)

Returns grapheme end position closest to the `pos`.

---


<a id="class-textserverextension-private-method-shaped-text-overrun-trim-to-width"></a>

void **_shaped_text_overrun_trim_to_width**(shaped: [RID](class_rid.md#class-rid), width: [float](class_float.md#class-float), trim_flags: BitField[[TextOverrunFlag](class_textserver.md#enum-textserver-textoverrunflag)]) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-overrun-trim-to-width)

Trims text if it exceeds the given width.

---


<a id="class-textserverextension-private-method-shaped-text-prev-character-pos"></a>

[int](class_int.md#class-int) **_shaped_text_prev_character_pos**(shaped: [RID](class_rid.md#class-rid), pos: [int](class_int.md#class-int)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-prev-character-pos)

Returns composite character start position closest to the `pos`.

---


<a id="class-textserverextension-private-method-shaped-text-prev-grapheme-pos"></a>

[int](class_int.md#class-int) **_shaped_text_prev_grapheme_pos**(shaped: [RID](class_rid.md#class-rid), pos: [int](class_int.md#class-int)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-prev-grapheme-pos)

Returns grapheme start position closest to the `pos`.

---


<a id="class-textserverextension-private-method-shaped-text-resize-object"></a>

[bool](class_bool.md#class-bool) **_shaped_text_resize_object**(shaped: [RID](class_rid.md#class-rid), key: [Variant](class_variant.md#class-variant), size: [Vector2](class_vector2.md#class-vector2), inline_align: [InlineAlignment](class_@globalscope.md#enum-globalscope-inlinealignment), baseline: [float](class_float.md#class-float)) virtual required [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-resize-object)

Sets new size and alignment of embedded object.

---


<a id="class-textserverextension-private-method-shaped-text-set-bidi-override"></a>

void **_shaped_text_set_bidi_override**(shaped: [RID](class_rid.md#class-rid), override: [Array](class_array.md#class-array)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-set-bidi-override)

Overrides BiDi for the structured text.

---


<a id="class-textserverextension-private-method-shaped-text-set-custom-ellipsis"></a>

void **_shaped_text_set_custom_ellipsis**(shaped: [RID](class_rid.md#class-rid), char: [int](class_int.md#class-int)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-set-custom-ellipsis)

Sets ellipsis character used for text clipping.

---


<a id="class-textserverextension-private-method-shaped-text-set-custom-punctuation"></a>

void **_shaped_text_set_custom_punctuation**(shaped: [RID](class_rid.md#class-rid), punct: [String](class_string.md#class-string)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-set-custom-punctuation)

Sets custom punctuation character list, used for word breaking. If set to empty string, server defaults are used.

---


<a id="class-textserverextension-private-method-shaped-text-set-direction"></a>

void **_shaped_text_set_direction**(shaped: [RID](class_rid.md#class-rid), direction: [Direction](class_textserver.md#enum-textserver-direction)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-set-direction)

Sets desired text direction. If set to [TextServer.DIRECTION_AUTO](class_textserver.md#class-textserver-constant-direction-auto), direction will be detected based on the buffer contents and current locale.

---


<a id="class-textserverextension-private-method-shaped-text-set-orientation"></a>

void **_shaped_text_set_orientation**(shaped: [RID](class_rid.md#class-rid), orientation: [Orientation](class_textserver.md#enum-textserver-orientation)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-set-orientation)

Sets desired text orientation.

---


<a id="class-textserverextension-private-method-shaped-text-set-preserve-control"></a>

void **_shaped_text_set_preserve_control**(shaped: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-set-preserve-control)

If set to `true` text buffer will display control characters.

---


<a id="class-textserverextension-private-method-shaped-text-set-preserve-invalid"></a>

void **_shaped_text_set_preserve_invalid**(shaped: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-set-preserve-invalid)

If set to `true` text buffer will display invalid characters as hexadecimal codes, otherwise nothing is displayed.

---


<a id="class-textserverextension-private-method-shaped-text-set-spacing"></a>

void **_shaped_text_set_spacing**(shaped: [RID](class_rid.md#class-rid), spacing: [SpacingType](class_textserver.md#enum-textserver-spacingtype), value: [int](class_int.md#class-int)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-set-spacing)

Sets extra spacing added between glyphs or lines in pixels.

---


<a id="class-textserverextension-private-method-shaped-text-shape"></a>

[bool](class_bool.md#class-bool) **_shaped_text_shape**(shaped: [RID](class_rid.md#class-rid)) virtual required [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-shape)

Shapes buffer if it's not shaped. Returns `true` if the string is shaped successfully.

---


<a id="class-textserverextension-private-method-shaped-text-sort-logical"></a>

`const Glyph*` **_shaped_text_sort_logical**(shaped: [RID](class_rid.md#class-rid)) virtual required [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-sort-logical)

Returns text glyphs in the logical order.

---


<a id="class-textserverextension-private-method-shaped-text-substr"></a>

[RID](class_rid.md#class-rid) **_shaped_text_substr**(shaped: [RID](class_rid.md#class-rid), start: [int](class_int.md#class-int), length: [int](class_int.md#class-int)) virtual required const [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-substr)

Returns text buffer for the substring of the text in the `shaped` text buffer (including inline objects).

---


<a id="class-textserverextension-private-method-shaped-text-tab-align"></a>

[float](class_float.md#class-float) **_shaped_text_tab_align**(shaped: [RID](class_rid.md#class-rid), tab_stops: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-tab-align)

Aligns shaped text to the given tab-stops.

---


<a id="class-textserverextension-private-method-shaped-text-update-breaks"></a>

[bool](class_bool.md#class-bool) **_shaped_text_update_breaks**(shaped: [RID](class_rid.md#class-rid)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-update-breaks)

Updates break points in the shaped text. This method is called by default implementation of text breaking functions.

---


<a id="class-textserverextension-private-method-shaped-text-update-justification-ops"></a>

[bool](class_bool.md#class-bool) **_shaped_text_update_justification_ops**(shaped: [RID](class_rid.md#class-rid)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-shaped-text-update-justification-ops)

Updates justification points in the shaped text. This method is called by default implementation of text justification functions.

---


<a id="class-textserverextension-private-method-spoof-check"></a>

[bool](class_bool.md#class-bool) **_spoof_check**(string: [String](class_string.md#class-string)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-spoof-check)

Returns `true` if `string` is likely to be an attempt at confusing the reader.

---


<a id="class-textserverextension-private-method-string-get-character-breaks"></a>

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **_string_get_character_breaks**(string: [String](class_string.md#class-string), language: [String](class_string.md#class-string)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-string-get-character-breaks)

Returns array of the composite character boundaries.

---


<a id="class-textserverextension-private-method-string-get-word-breaks"></a>

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **_string_get_word_breaks**(string: [String](class_string.md#class-string), language: [String](class_string.md#class-string), chars_per_line: [int](class_int.md#class-int)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-string-get-word-breaks)

Returns an array of the word break boundaries. Elements in the returned array are the offsets of the start and end of words. Therefore the length of the array is always even.

---


<a id="class-textserverextension-private-method-string-to-lower"></a>

[String](class_string.md#class-string) **_string_to_lower**(string: [String](class_string.md#class-string), language: [String](class_string.md#class-string)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-string-to-lower)

Returns the string converted to `lowercase`.

---


<a id="class-textserverextension-private-method-string-to-title"></a>

[String](class_string.md#class-string) **_string_to_title**(string: [String](class_string.md#class-string), language: [String](class_string.md#class-string)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-string-to-title)

Returns the string converted to `Title Case`.

---


<a id="class-textserverextension-private-method-string-to-upper"></a>

[String](class_string.md#class-string) **_string_to_upper**(string: [String](class_string.md#class-string), language: [String](class_string.md#class-string)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-string-to-upper)

Returns the string converted to `UPPERCASE`.

---


<a id="class-textserverextension-private-method-strip-diacritics"></a>

[String](class_string.md#class-string) **_strip_diacritics**(string: [String](class_string.md#class-string)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-strip-diacritics)

Strips diacritics from the string.

---


<a id="class-textserverextension-private-method-tag-to-name"></a>

[String](class_string.md#class-string) **_tag_to_name**(tag: [int](class_int.md#class-int)) virtual const [🔗](class_textserverextension.md#class-textserverextension-private-method-tag-to-name)

Converts the given OpenType tag to the readable name of a feature, variation, script, or language.

---


<a id="class-textserverextension-private-method-unreference-oversampling-level"></a>

void **_unreference_oversampling_level**(oversampling: [float](class_float.md#class-float)) virtual [🔗](class_textserverextension.md#class-textserverextension-private-method-unreference-oversampling-level)

Decreases the reference count of the specified oversampling level, and frees the font cache for oversampling level when the reference count reaches zero. This method is called by [Viewport](class_viewport.md#class-viewport), and should not be used directly.
