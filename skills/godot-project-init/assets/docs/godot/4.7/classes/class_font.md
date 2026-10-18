> Source: https://docs.godotengine.org/en/4.7/classes/class_font.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="font"></a>

<a id="class-font"></a>

# Font

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [FontFile](class_fontfile.md#class-fontfile), [FontVariation](class_fontvariation.md#class-fontvariation), [SystemFont](class_systemfont.md#class-systemfont)

Abstract base class for fonts and font variations.

<a id="description"></a>

## Description

Abstract base class for different font types. It has methods for drawing text and font character introspection.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Array](class_array.md#class-array)[[Font](class_font.md#class-font)] | [fallbacks](class_font.md#class-font-property-fallbacks) | `[]` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [float](class_float.md#class-float) | [draw_char](class_font.md#class-font-method-draw-char)(canvas_item: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), char: [int](class_int.md#class-int), font_size: [int](class_int.md#class-int), modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0) const |
| [float](class_float.md#class-float) | [draw_char_outline](class_font.md#class-font-method-draw-char-outline)(canvas_item: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), char: [int](class_int.md#class-int), font_size: [int](class_int.md#class-int), size: [int](class_int.md#class-int) = -1, modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0) const |
| void | [draw_multiline_string](class_font.md#class-font-method-draw-multiline-string)(canvas_item: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), text: [String](class_string.md#class-string), alignment: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) = 0, width: [float](class_float.md#class-float) = -1, font_size: [int](class_int.md#class-int) = 16, max_lines: [int](class_int.md#class-int) = -1, modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), brk_flags: BitField[[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)] = 3, justification_flags: BitField[[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] = 3, direction: [Direction](class_textserver.md#enum-textserver-direction) = 0, orientation: [Orientation](class_textserver.md#enum-textserver-orientation) = 0, oversampling: [float](class_float.md#class-float) = 0.0) const |
| void | [draw_multiline_string_outline](class_font.md#class-font-method-draw-multiline-string-outline)(canvas_item: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), text: [String](class_string.md#class-string), alignment: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) = 0, width: [float](class_float.md#class-float) = -1, font_size: [int](class_int.md#class-int) = 16, max_lines: [int](class_int.md#class-int) = -1, size: [int](class_int.md#class-int) = 1, modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), brk_flags: BitField[[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)] = 3, justification_flags: BitField[[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] = 3, direction: [Direction](class_textserver.md#enum-textserver-direction) = 0, orientation: [Orientation](class_textserver.md#enum-textserver-orientation) = 0, oversampling: [float](class_float.md#class-float) = 0.0) const |
| void | [draw_string](class_font.md#class-font-method-draw-string)(canvas_item: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), text: [String](class_string.md#class-string), alignment: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) = 0, width: [float](class_float.md#class-float) = -1, font_size: [int](class_int.md#class-int) = 16, modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), justification_flags: BitField[[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] = 3, direction: [Direction](class_textserver.md#enum-textserver-direction) = 0, orientation: [Orientation](class_textserver.md#enum-textserver-orientation) = 0, oversampling: [float](class_float.md#class-float) = 0.0) const |
| void | [draw_string_outline](class_font.md#class-font-method-draw-string-outline)(canvas_item: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), text: [String](class_string.md#class-string), alignment: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) = 0, width: [float](class_float.md#class-float) = -1, font_size: [int](class_int.md#class-int) = 16, size: [int](class_int.md#class-int) = 1, modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), justification_flags: BitField[[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] = 3, direction: [Direction](class_textserver.md#enum-textserver-direction) = 0, orientation: [Orientation](class_textserver.md#enum-textserver-orientation) = 0, oversampling: [float](class_float.md#class-float) = 0.0) const |
| [RID](class_rid.md#class-rid) | [find_variation](class_font.md#class-font-method-find-variation)(variation_coordinates: [Dictionary](class_dictionary.md#class-dictionary), face_index: [int](class_int.md#class-int) = 0, strength: [float](class_float.md#class-float) = 0.0, transform: [Transform2D](class_transform2d.md#class-transform2d) = Transform2D(1, 0, 0, 1, 0, 0), spacing_top: [int](class_int.md#class-int) = 0, spacing_bottom: [int](class_int.md#class-int) = 0, spacing_space: [int](class_int.md#class-int) = 0, spacing_glyph: [int](class_int.md#class-int) = 0, baseline_offset: [float](class_float.md#class-float) = 0.0, palette_index: [int](class_int.md#class-int) = 0, custom_colors: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) = PackedColorArray()) const |
| [float](class_float.md#class-float) | [get_ascent](class_font.md#class-font-method-get-ascent)(font_size: [int](class_int.md#class-int) = 16) const |
| [Vector2](class_vector2.md#class-vector2) | [get_char_size](class_font.md#class-font-method-get-char-size)(char: [int](class_int.md#class-int), font_size: [int](class_int.md#class-int)) const |
| [float](class_float.md#class-float) | [get_descent](class_font.md#class-font-method-get-descent)(font_size: [int](class_int.md#class-int) = 16) const |
| [int](class_int.md#class-int) | [get_face_count](class_font.md#class-font-method-get-face-count)() const |
| [String](class_string.md#class-string) | [get_font_name](class_font.md#class-font-method-get-font-name)() const |
| [int](class_int.md#class-int) | [get_font_stretch](class_font.md#class-font-method-get-font-stretch)() const |
| BitField[[FontStyle](class_textserver.md#enum-textserver-fontstyle)] | [get_font_style](class_font.md#class-font-method-get-font-style)() const |
| [String](class_string.md#class-string) | [get_font_style_name](class_font.md#class-font-method-get-font-style-name)() const |
| [int](class_int.md#class-int) | [get_font_weight](class_font.md#class-font-method-get-font-weight)() const |
| [float](class_float.md#class-float) | [get_height](class_font.md#class-font-method-get-height)(font_size: [int](class_int.md#class-int) = 16) const |
| [Vector2](class_vector2.md#class-vector2) | [get_multiline_string_size](class_font.md#class-font-method-get-multiline-string-size)(text: [String](class_string.md#class-string), alignment: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) = 0, width: [float](class_float.md#class-float) = -1, font_size: [int](class_int.md#class-int) = 16, max_lines: [int](class_int.md#class-int) = -1, brk_flags: BitField[[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)] = 3, justification_flags: BitField[[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] = 3, direction: [Direction](class_textserver.md#enum-textserver-direction) = 0, orientation: [Orientation](class_textserver.md#enum-textserver-orientation) = 0) const |
| [Dictionary](class_dictionary.md#class-dictionary) | [get_opentype_features](class_font.md#class-font-method-get-opentype-features)() const |
| [Dictionary](class_dictionary.md#class-dictionary) | [get_ot_name_strings](class_font.md#class-font-method-get-ot-name-strings)() const |
| [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) | [get_palette_colors](class_font.md#class-font-method-get-palette-colors)(index: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_palette_count](class_font.md#class-font-method-get-palette-count)() const |
| [String](class_string.md#class-string) | [get_palette_name](class_font.md#class-font-method-get-palette-name)(index: [int](class_int.md#class-int)) const |
| [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] | [get_rids](class_font.md#class-font-method-get-rids)() const |
| [int](class_int.md#class-int) | [get_spacing](class_font.md#class-font-method-get-spacing)(spacing: [SpacingType](class_textserver.md#enum-textserver-spacingtype)) const |
| [Vector2](class_vector2.md#class-vector2) | [get_string_size](class_font.md#class-font-method-get-string-size)(text: [String](class_string.md#class-string), alignment: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) = 0, width: [float](class_float.md#class-float) = -1, font_size: [int](class_int.md#class-int) = 16, justification_flags: BitField[[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] = 3, direction: [Direction](class_textserver.md#enum-textserver-direction) = 0, orientation: [Orientation](class_textserver.md#enum-textserver-orientation) = 0) const |
| [String](class_string.md#class-string) | [get_supported_chars](class_font.md#class-font-method-get-supported-chars)() const |
| [Dictionary](class_dictionary.md#class-dictionary) | [get_supported_feature_list](class_font.md#class-font-method-get-supported-feature-list)() const |
| [Dictionary](class_dictionary.md#class-dictionary) | [get_supported_variation_list](class_font.md#class-font-method-get-supported-variation-list)() const |
| [float](class_float.md#class-float) | [get_underline_position](class_font.md#class-font-method-get-underline-position)(font_size: [int](class_int.md#class-int) = 16) const |
| [float](class_float.md#class-float) | [get_underline_thickness](class_font.md#class-font-method-get-underline-thickness)(font_size: [int](class_int.md#class-int) = 16) const |
| [bool](class_bool.md#class-bool) | [has_char](class_font.md#class-font-method-has-char)(char: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [is_language_supported](class_font.md#class-font-method-is-language-supported)(language: [String](class_string.md#class-string)) const |
| [bool](class_bool.md#class-bool) | [is_script_supported](class_font.md#class-font-method-is-script-supported)(script: [String](class_string.md#class-string)) const |
| void | [set_cache_capacity](class_font.md#class-font-method-set-cache-capacity)(single_line: [int](class_int.md#class-int), multi_line: [int](class_int.md#class-int)) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-font-property-fallbacks"></a>

[Array](class_array.md#class-array)[[Font](class_font.md#class-font)] **fallbacks** = `[]` [🔗](class_font.md#class-font-property-fallbacks)

- void **set_fallbacks**(value: [Array](class_array.md#class-array)[[Font](class_font.md#class-font)])
- [Array](class_array.md#class-array)[[Font](class_font.md#class-font)] **get_fallbacks**()

Array of fallback **Font**s to use as a substitute if a glyph is not found in this current **Font**.

If this array is empty in a [FontVariation](class_fontvariation.md#class-fontvariation), the [FontVariation.base_font](class_fontvariation.md#class-fontvariation-property-base-font)'s fallbacks are used instead.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-font-method-draw-char"></a>

[float](class_float.md#class-float) **draw_char**(canvas_item: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), char: [int](class_int.md#class-int), font_size: [int](class_int.md#class-int), modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0) const [🔗](class_font.md#class-font-method-draw-char)

Draw a single Unicode character `char` into a canvas item using the font, at a given position, with `modulate` color. `pos` specifies the baseline, not the top. To draw from the top, *ascent* must be added to the Y axis. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

**Note:** Do not use this function to draw strings character by character, use [draw_string()](class_font.md#class-font-method-draw-string) or [TextLine](class_textline.md#class-textline) instead.

---


<a id="class-font-method-draw-char-outline"></a>

[float](class_float.md#class-float) **draw_char_outline**(canvas_item: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), char: [int](class_int.md#class-int), font_size: [int](class_int.md#class-int), size: [int](class_int.md#class-int) = -1, modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0) const [🔗](class_font.md#class-font-method-draw-char-outline)

Draw a single Unicode character `char` outline into a canvas item using the font, at a given position, with `modulate` color and `size` outline size. `pos` specifies the baseline, not the top. To draw from the top, *ascent* must be added to the Y axis. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

**Note:** Do not use this function to draw strings character by character, use [draw_string()](class_font.md#class-font-method-draw-string) or [TextLine](class_textline.md#class-textline) instead.

---


<a id="class-font-method-draw-multiline-string"></a>

void **draw_multiline_string**(canvas_item: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), text: [String](class_string.md#class-string), alignment: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) = 0, width: [float](class_float.md#class-float) = -1, font_size: [int](class_int.md#class-int) = 16, max_lines: [int](class_int.md#class-int) = -1, modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), brk_flags: BitField[[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)] = 3, justification_flags: BitField[[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] = 3, direction: [Direction](class_textserver.md#enum-textserver-direction) = 0, orientation: [Orientation](class_textserver.md#enum-textserver-orientation) = 0, oversampling: [float](class_float.md#class-float) = 0.0) const [🔗](class_font.md#class-font-method-draw-multiline-string)

Breaks `text` into lines using rules specified by `brk_flags` and draws it into a canvas item using the font, at a given position, with `modulate` color, optionally clipping the width and aligning horizontally. `pos` specifies the baseline of the first line, not the top. To draw from the top, *ascent* must be added to the Y axis. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

See also [CanvasItem.draw_multiline_string()](class_canvasitem.md#class-canvasitem-method-draw-multiline-string).

---


<a id="class-font-method-draw-multiline-string-outline"></a>

void **draw_multiline_string_outline**(canvas_item: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), text: [String](class_string.md#class-string), alignment: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) = 0, width: [float](class_float.md#class-float) = -1, font_size: [int](class_int.md#class-int) = 16, max_lines: [int](class_int.md#class-int) = -1, size: [int](class_int.md#class-int) = 1, modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), brk_flags: BitField[[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)] = 3, justification_flags: BitField[[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] = 3, direction: [Direction](class_textserver.md#enum-textserver-direction) = 0, orientation: [Orientation](class_textserver.md#enum-textserver-orientation) = 0, oversampling: [float](class_float.md#class-float) = 0.0) const [🔗](class_font.md#class-font-method-draw-multiline-string-outline)

Breaks `text` to the lines using rules specified by `brk_flags` and draws text outline into a canvas item using the font, at a given position, with `modulate` color and `size` outline size, optionally clipping the width and aligning horizontally. `pos` specifies the baseline of the first line, not the top. To draw from the top, *ascent* must be added to the Y axis. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

See also [CanvasItem.draw_multiline_string_outline()](class_canvasitem.md#class-canvasitem-method-draw-multiline-string-outline).

---


<a id="class-font-method-draw-string"></a>

void **draw_string**(canvas_item: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), text: [String](class_string.md#class-string), alignment: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) = 0, width: [float](class_float.md#class-float) = -1, font_size: [int](class_int.md#class-int) = 16, modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), justification_flags: BitField[[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] = 3, direction: [Direction](class_textserver.md#enum-textserver-direction) = 0, orientation: [Orientation](class_textserver.md#enum-textserver-orientation) = 0, oversampling: [float](class_float.md#class-float) = 0.0) const [🔗](class_font.md#class-font-method-draw-string)

Draw `text` into a canvas item using the font, at a given position, with `modulate` color, optionally clipping the width and aligning horizontally. `pos` specifies the baseline, not the top. To draw from the top, *ascent* must be added to the Y axis. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

See also [CanvasItem.draw_string()](class_canvasitem.md#class-canvasitem-method-draw-string).

---


<a id="class-font-method-draw-string-outline"></a>

void **draw_string_outline**(canvas_item: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), text: [String](class_string.md#class-string), alignment: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) = 0, width: [float](class_float.md#class-float) = -1, font_size: [int](class_int.md#class-int) = 16, size: [int](class_int.md#class-int) = 1, modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), justification_flags: BitField[[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] = 3, direction: [Direction](class_textserver.md#enum-textserver-direction) = 0, orientation: [Orientation](class_textserver.md#enum-textserver-orientation) = 0, oversampling: [float](class_float.md#class-float) = 0.0) const [🔗](class_font.md#class-font-method-draw-string-outline)

Draw `text` outline into a canvas item using the font, at a given position, with `modulate` color and `size` outline size, optionally clipping the width and aligning horizontally. `pos` specifies the baseline, not the top. To draw from the top, *ascent* must be added to the Y axis. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

See also [CanvasItem.draw_string_outline()](class_canvasitem.md#class-canvasitem-method-draw-string-outline).

---


<a id="class-font-method-find-variation"></a>

[RID](class_rid.md#class-rid) **find_variation**(variation_coordinates: [Dictionary](class_dictionary.md#class-dictionary), face_index: [int](class_int.md#class-int) = 0, strength: [float](class_float.md#class-float) = 0.0, transform: [Transform2D](class_transform2d.md#class-transform2d) = Transform2D(1, 0, 0, 1, 0, 0), spacing_top: [int](class_int.md#class-int) = 0, spacing_bottom: [int](class_int.md#class-int) = 0, spacing_space: [int](class_int.md#class-int) = 0, spacing_glyph: [int](class_int.md#class-int) = 0, baseline_offset: [float](class_float.md#class-float) = 0.0, palette_index: [int](class_int.md#class-int) = 0, custom_colors: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) = PackedColorArray()) const [🔗](class_font.md#class-font-method-find-variation)

Returns [TextServer](class_textserver.md#class-textserver) RID of the font cache for specific variation.

---


<a id="class-font-method-get-ascent"></a>

[float](class_float.md#class-float) **get_ascent**(font_size: [int](class_int.md#class-int) = 16) const [🔗](class_font.md#class-font-method-get-ascent)

Returns the maximum font ascent (number of pixels above the baseline) of this font and all fallback fonts.

**Note:** Real ascent of the string is context-dependent and can be significantly different from the value returned by this function. Use it only as rough estimate (e.g. as the ascent of empty line).

---


<a id="class-font-method-get-char-size"></a>

[Vector2](class_vector2.md#class-vector2) **get_char_size**(char: [int](class_int.md#class-int), font_size: [int](class_int.md#class-int)) const [🔗](class_font.md#class-font-method-get-char-size)

Returns the size of a character. Does not take kerning into account.

**Note:** Do not use this function to calculate width of the string character by character, use [get_string_size()](class_font.md#class-font-method-get-string-size) or [TextLine](class_textline.md#class-textline) instead. The height returned is the font height (see also [get_height()](class_font.md#class-font-method-get-height)) and has no relation to the glyph height.

---


<a id="class-font-method-get-descent"></a>

[float](class_float.md#class-float) **get_descent**(font_size: [int](class_int.md#class-int) = 16) const [🔗](class_font.md#class-font-method-get-descent)

Returns the maximum font descent (number of pixels below the baseline) of this font and all fallback fonts.

**Note:** Real descent of the string is context-dependent and can be significantly different from the value returned by this function. Use it only as rough estimate (e.g. as the descent of empty line).

---


<a id="class-font-method-get-face-count"></a>

[int](class_int.md#class-int) **get_face_count**() const [🔗](class_font.md#class-font-method-get-face-count)

Returns number of faces in the TrueType / OpenType collection.

---


<a id="class-font-method-get-font-name"></a>

[String](class_string.md#class-string) **get_font_name**() const [🔗](class_font.md#class-font-method-get-font-name)

Returns font family name.

---


<a id="class-font-method-get-font-stretch"></a>

[int](class_int.md#class-int) **get_font_stretch**() const [🔗](class_font.md#class-font-method-get-font-stretch)

Returns font stretch amount, compared to a normal width. A percentage value between `50%` and `200%`.

---


<a id="class-font-method-get-font-style"></a>

BitField[[FontStyle](class_textserver.md#enum-textserver-fontstyle)] **get_font_style**() const [🔗](class_font.md#class-font-method-get-font-style)

Returns font style flags.

---


<a id="class-font-method-get-font-style-name"></a>

[String](class_string.md#class-string) **get_font_style_name**() const [🔗](class_font.md#class-font-method-get-font-style-name)

Returns font style name.

---


<a id="class-font-method-get-font-weight"></a>

[int](class_int.md#class-int) **get_font_weight**() const [🔗](class_font.md#class-font-method-get-font-weight)

Returns weight (boldness) of the font. A value in the `100...999` range, normal font weight is `400`, bold font weight is `700`.

---


<a id="class-font-method-get-height"></a>

[float](class_float.md#class-float) **get_height**(font_size: [int](class_int.md#class-int) = 16) const [🔗](class_font.md#class-font-method-get-height)

Returns the total average font height (ascent plus descent) in pixels.

**Note:** Real height of the string is context-dependent and can be significantly different from the value returned by this function. Use it only as rough estimate (e.g. as the height of empty line).

---


<a id="class-font-method-get-multiline-string-size"></a>

[Vector2](class_vector2.md#class-vector2) **get_multiline_string_size**(text: [String](class_string.md#class-string), alignment: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) = 0, width: [float](class_float.md#class-float) = -1, font_size: [int](class_int.md#class-int) = 16, max_lines: [int](class_int.md#class-int) = -1, brk_flags: BitField[[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)] = 3, justification_flags: BitField[[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] = 3, direction: [Direction](class_textserver.md#enum-textserver-direction) = 0, orientation: [Orientation](class_textserver.md#enum-textserver-orientation) = 0) const [🔗](class_font.md#class-font-method-get-multiline-string-size)

Returns the size of a bounding box of a string broken into the lines, taking kerning and advance into account.

See also [draw_multiline_string()](class_font.md#class-font-method-draw-multiline-string).

---


<a id="class-font-method-get-opentype-features"></a>

[Dictionary](class_dictionary.md#class-dictionary) **get_opentype_features**() const [🔗](class_font.md#class-font-method-get-opentype-features)

Returns a set of OpenType feature tags. More info: [OpenType feature tags](https://docs.microsoft.com/en-us/typography/opentype/spec/featuretags).

---


<a id="class-font-method-get-ot-name-strings"></a>

[Dictionary](class_dictionary.md#class-dictionary) **get_ot_name_strings**() const [🔗](class_font.md#class-font-method-get-ot-name-strings)

Returns [Dictionary](class_dictionary.md#class-dictionary) with OpenType font name strings (localized font names, version, description, license information, sample text, etc.).

---


<a id="class-font-method-get-palette-colors"></a>

[PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) **get_palette_colors**(index: [int](class_int.md#class-int)) const [🔗](class_font.md#class-font-method-get-palette-colors)

Returns the array in the predefined color palette at `index`. Palette contains all colors used to render font glyphs. Each palette has the same number of colors. Colors can be overridden using [FontVariation](class_fontvariation.md#class-fontvariation).

---


<a id="class-font-method-get-palette-count"></a>

[int](class_int.md#class-int) **get_palette_count**() const [🔗](class_font.md#class-font-method-get-palette-count)

Returns the number of predefined color palettes. Palette contains all colors used to render font glyphs. Each palette has the same number of colors.

---


<a id="class-font-method-get-palette-name"></a>

[String](class_string.md#class-string) **get_palette_name**(index: [int](class_int.md#class-int)) const [🔗](class_font.md#class-font-method-get-palette-name)

Returns the name of the predefined color palette at `index`. Palette contains all colors used to render font glyphs. Each palette has the same number of colors.

---


<a id="class-font-method-get-rids"></a>

[Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] **get_rids**() const [🔗](class_font.md#class-font-method-get-rids)

Returns [Array](class_array.md#class-array) of valid **Font** [RID](class_rid.md#class-rid)s, which can be passed to the [TextServer](class_textserver.md#class-textserver) methods.

---


<a id="class-font-method-get-spacing"></a>

[int](class_int.md#class-int) **get_spacing**(spacing: [SpacingType](class_textserver.md#enum-textserver-spacingtype)) const [🔗](class_font.md#class-font-method-get-spacing)

Returns the amount of spacing for the given `spacing` type.

---


<a id="class-font-method-get-string-size"></a>

[Vector2](class_vector2.md#class-vector2) **get_string_size**(text: [String](class_string.md#class-string), alignment: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) = 0, width: [float](class_float.md#class-float) = -1, font_size: [int](class_int.md#class-int) = 16, justification_flags: BitField[[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] = 3, direction: [Direction](class_textserver.md#enum-textserver-direction) = 0, orientation: [Orientation](class_textserver.md#enum-textserver-orientation) = 0) const [🔗](class_font.md#class-font-method-get-string-size)

Returns the size of a bounding box of a single-line string, taking kerning, advance and subpixel positioning into account. See also [get_multiline_string_size()](class_font.md#class-font-method-get-multiline-string-size) and [draw_string()](class_font.md#class-font-method-draw-string).

For example, to get the string size as displayed by a single-line Label, use:

```gdscript
var string_size = $Label.get_theme_font("font").get_string_size($Label.text, HORIZONTAL_ALIGNMENT_LEFT, -1, $Label.get_theme_font_size("font_size"))
```

```csharp
Label label = GetNode<Label>("Label");
Vector2 stringSize = label.GetThemeFont("font").GetStringSize(label.Text, HorizontalAlignment.Left, -1, label.GetThemeFontSize("font_size"));
```

**Note:** Since kerning, advance and subpixel positioning are taken into account by [get_string_size()](class_font.md#class-font-method-get-string-size), using separate [get_string_size()](class_font.md#class-font-method-get-string-size) calls on substrings of a string then adding the results together will return a different result compared to using a single [get_string_size()](class_font.md#class-font-method-get-string-size) call on the full string.

**Note:** Real height of the string is context-dependent and can be significantly different from the value returned by [get_height()](class_font.md#class-font-method-get-height).

---


<a id="class-font-method-get-supported-chars"></a>

[String](class_string.md#class-string) **get_supported_chars**() const [🔗](class_font.md#class-font-method-get-supported-chars)

Returns a string containing all the characters available in the font.

If a given character is included in more than one font data source, it appears only once in the returned string.

---


<a id="class-font-method-get-supported-feature-list"></a>

[Dictionary](class_dictionary.md#class-dictionary) **get_supported_feature_list**() const [🔗](class_font.md#class-font-method-get-supported-feature-list)

Returns list of OpenType features supported by font.

---


<a id="class-font-method-get-supported-variation-list"></a>

[Dictionary](class_dictionary.md#class-dictionary) **get_supported_variation_list**() const [🔗](class_font.md#class-font-method-get-supported-variation-list)

Returns list of supported [variation coordinates](https://docs.microsoft.com/en-us/typography/opentype/spec/dvaraxisreg), each coordinate is returned as `tag: Vector3i(min_value,max_value,default_value)`.

Font variations allow for continuous change of glyph characteristics along some given design axis, such as weight, width or slant.

To print available variation axes of a variable font:

```gdscript
var fv = FontVariation.new()
fv.base_font = load("res://RobotoFlex.ttf")
var variation_list = fv.get_supported_variation_list()
for tag in variation_list:
    var name = TextServerManager.get_primary_interface().tag_to_name(tag)
    var values = variation_list[tag]
    print("variation axis: %s (%d)\n\tmin, max, default: %s" % [name, tag, values])
```

**Note:** To set and get variation coordinates of a [FontVariation](class_fontvariation.md#class-fontvariation), use [FontVariation.variation_opentype](class_fontvariation.md#class-fontvariation-property-variation-opentype).

---


<a id="class-font-method-get-underline-position"></a>

[float](class_float.md#class-float) **get_underline_position**(font_size: [int](class_int.md#class-int) = 16) const [🔗](class_font.md#class-font-method-get-underline-position)

Returns average pixel offset of the underline below the baseline.

**Note:** Real underline position of the string is context-dependent and can be significantly different from the value returned by this function. Use it only as rough estimate.

---


<a id="class-font-method-get-underline-thickness"></a>

[float](class_float.md#class-float) **get_underline_thickness**(font_size: [int](class_int.md#class-int) = 16) const [🔗](class_font.md#class-font-method-get-underline-thickness)

Returns average thickness of the underline.

**Note:** Real underline thickness of the string is context-dependent and can be significantly different from the value returned by this function. Use it only as rough estimate.

---


<a id="class-font-method-has-char"></a>

[bool](class_bool.md#class-bool) **has_char**(char: [int](class_int.md#class-int)) const [🔗](class_font.md#class-font-method-has-char)

Returns `true` if a Unicode `char` is available in the font.

---


<a id="class-font-method-is-language-supported"></a>

[bool](class_bool.md#class-bool) **is_language_supported**(language: [String](class_string.md#class-string)) const [🔗](class_font.md#class-font-method-is-language-supported)

Returns `true` if the font supports the given language (as a [ISO 639](https://en.wikipedia.org/wiki/ISO_639-1) code).

---


<a id="class-font-method-is-script-supported"></a>

[bool](class_bool.md#class-bool) **is_script_supported**(script: [String](class_string.md#class-string)) const [🔗](class_font.md#class-font-method-is-script-supported)

Returns `true` if the font supports the given script (as a [ISO 15924](https://en.wikipedia.org/wiki/ISO_15924) code).

---


<a id="class-font-method-set-cache-capacity"></a>

void **set_cache_capacity**(single_line: [int](class_int.md#class-int), multi_line: [int](class_int.md#class-int)) [🔗](class_font.md#class-font-method-set-cache-capacity)

Sets LRU cache capacity for `draw_*` methods.
