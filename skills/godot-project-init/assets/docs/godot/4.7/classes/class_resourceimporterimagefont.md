> Source: https://docs.godotengine.org/en/4.7/classes/class_resourceimporterimagefont.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="resourceimporterimagefont"></a>

<a id="class-resourceimporterimagefont"></a>

# ResourceImporterImageFont

**Inherits:** [ResourceImporter](class_resourceimporter.md#class-resourceimporter) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Imports a bitmap font where all glyphs have the same width and height.

<a id="description"></a>

## Description

This image-based workflow can be easier to use than [ResourceImporterBMFont](class_resourceimporterbmfont.md#class-resourceimporterbmfont), but it requires all glyphs to have the same width and height, glyph advances and drawing offsets can be customized. This makes **ResourceImporterImageFont** most suited to fixed-width fonts.

See also [ResourceImporterDynamicFont](class_resourceimporterdynamicfont.md#class-resourceimporterdynamicfont).

<a id="tutorials"></a>

## Tutorials

- [Bitmap fonts - Using fonts](../tutorials/ui/gui_using_fonts.md#bitmap-fonts)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [ascent](class_resourceimporterimagefont.md#class-resourceimporterimagefont-property-ascent) | `0` |
| [Rect2i](class_rect2i.md#class-rect2i) | [character_margin](class_resourceimporterimagefont.md#class-resourceimporterimagefont-property-character-margin) | `Rect2i(0, 0, 0, 0)` |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [character_ranges](class_resourceimporterimagefont.md#class-resourceimporterimagefont-property-character-ranges) | `PackedStringArray()` |
| [int](class_int.md#class-int) | [columns](class_resourceimporterimagefont.md#class-resourceimporterimagefont-property-columns) | `1` |
| [bool](class_bool.md#class-bool) | [compress](class_resourceimporterimagefont.md#class-resourceimporterimagefont-property-compress) | `true` |
| [int](class_int.md#class-int) | [descent](class_resourceimporterimagefont.md#class-resourceimporterimagefont-property-descent) | `0` |
| [Array](class_array.md#class-array) | [fallbacks](class_resourceimporterimagefont.md#class-resourceimporterimagefont-property-fallbacks) | `[]` |
| [Rect2i](class_rect2i.md#class-rect2i) | [image_margin](class_resourceimporterimagefont.md#class-resourceimporterimagefont-property-image-margin) | `Rect2i(0, 0, 0, 0)` |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [kerning_pairs](class_resourceimporterimagefont.md#class-resourceimporterimagefont-property-kerning-pairs) | `PackedStringArray()` |
| [int](class_int.md#class-int) | [rows](class_resourceimporterimagefont.md#class-resourceimporterimagefont-property-rows) | `1` |
| [int](class_int.md#class-int) | [scaling_mode](class_resourceimporterimagefont.md#class-resourceimporterimagefont-property-scaling-mode) | `2` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-resourceimporterimagefont-property-ascent"></a>

[int](class_int.md#class-int) **ascent** = `0` [🔗](class_resourceimporterimagefont.md#class-resourceimporterimagefont-property-ascent)

Font ascent (number of pixels above the baseline). If set to `0`, half of the character height is used.

---


<a id="class-resourceimporterimagefont-property-character-margin"></a>

[Rect2i](class_rect2i.md#class-rect2i) **character_margin** = `Rect2i(0, 0, 0, 0)` [🔗](class_resourceimporterimagefont.md#class-resourceimporterimagefont-property-character-margin)

Margin applied around every imported glyph. If your font image contains guides (in the form of lines between glyphs) or if spacing between characters appears incorrect, try adjusting [character_margin](class_resourceimporterimagefont.md#class-resourceimporterimagefont-property-character-margin).

---


<a id="class-resourceimporterimagefont-property-character-ranges"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **character_ranges** = `PackedStringArray()` [🔗](class_resourceimporterimagefont.md#class-resourceimporterimagefont-property-character-ranges)

The character ranges to import from the font image. This is an array that maps each position on the image (in tile coordinates, not pixels). The font atlas is traversed from left to right and top to bottom. Characters can be specified with decimal numbers (126), hexadecimal numbers (`0x007e` or `U+007e`), or between single quotes (`'~'`). Ranges can be specified with a hyphen between characters.

For example, `0-127` represents the full ASCII range. It can also be written as `0x0000-0x007f` (or `U+0000-U+007f`). As another example, `' '-'~'` is equivalent to `32-126` and represents the range of printable (visible) ASCII characters.

For any range, the character advance and offset can be customized by appending three space-separated integer values (additional advance, x offset, y offset) to the end. For example `'a'-'b' 4 5 2` sets the advance to `char_width + 4` and offset to `Vector2(5, 2)` for both a and b characters.

**Note:** The overall number of characters must not exceed the number of [columns](class_resourceimporterimagefont.md#class-resourceimporterimagefont-property-columns) multiplied by [rows](class_resourceimporterimagefont.md#class-resourceimporterimagefont-property-rows). Otherwise, the font will fail to import.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedStringArray](class_packedstringarray.md#class-packedstringarray) for more details.

---


<a id="class-resourceimporterimagefont-property-columns"></a>

[int](class_int.md#class-int) **columns** = `1` [🔗](class_resourceimporterimagefont.md#class-resourceimporterimagefont-property-columns)

Number of columns in the font image. See also [rows](class_resourceimporterimagefont.md#class-resourceimporterimagefont-property-rows).

---


<a id="class-resourceimporterimagefont-property-compress"></a>

[bool](class_bool.md#class-bool) **compress** = `true` [🔗](class_resourceimporterimagefont.md#class-resourceimporterimagefont-property-compress)

If `true`, uses lossless compression for the resulting font.

---


<a id="class-resourceimporterimagefont-property-descent"></a>

[int](class_int.md#class-int) **descent** = `0` [🔗](class_resourceimporterimagefont.md#class-resourceimporterimagefont-property-descent)

Font descent (number of pixels below the baseline). If set to `0`, half of the character height is used.

---


<a id="class-resourceimporterimagefont-property-fallbacks"></a>

[Array](class_array.md#class-array) **fallbacks** = `[]` [🔗](class_resourceimporterimagefont.md#class-resourceimporterimagefont-property-fallbacks)

List of font fallbacks to use if a glyph isn't found in this bitmap font. Fonts at the beginning of the array are attempted first.

---


<a id="class-resourceimporterimagefont-property-image-margin"></a>

[Rect2i](class_rect2i.md#class-rect2i) **image_margin** = `Rect2i(0, 0, 0, 0)` [🔗](class_resourceimporterimagefont.md#class-resourceimporterimagefont-property-image-margin)

Margin to cut on the sides of the entire image. This can be used to cut parts of the image that contain attribution information or similar.

---


<a id="class-resourceimporterimagefont-property-kerning-pairs"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **kerning_pairs** = `PackedStringArray()` [🔗](class_resourceimporterimagefont.md#class-resourceimporterimagefont-property-kerning-pairs)

Kerning pairs for the font. Kerning pair adjust the spacing between two characters.

Each string consist of three space separated values: "from" string, "to" string and integer offset. Each combination form the two string for a kerning pair, e.g, `ab cd -3` will create kerning pairs `ac`, `ad`, `bc`, and `bd` with offset `-3`. `\uXXXX` escape sequences can be used to add Unicode characters.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedStringArray](class_packedstringarray.md#class-packedstringarray) for more details.

---


<a id="class-resourceimporterimagefont-property-rows"></a>

[int](class_int.md#class-int) **rows** = `1` [🔗](class_resourceimporterimagefont.md#class-resourceimporterimagefont-property-rows)

Number of rows in the font image. See also [columns](class_resourceimporterimagefont.md#class-resourceimporterimagefont-property-columns).

---


<a id="class-resourceimporterimagefont-property-scaling-mode"></a>

[int](class_int.md#class-int) **scaling_mode** = `2` [🔗](class_resourceimporterimagefont.md#class-resourceimporterimagefont-property-scaling-mode)

Font scaling mode.
