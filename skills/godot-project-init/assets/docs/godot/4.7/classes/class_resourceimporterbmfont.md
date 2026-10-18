> Source: https://docs.godotengine.org/en/4.7/classes/class_resourceimporterbmfont.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="resourceimporterbmfont"></a>

<a id="class-resourceimporterbmfont"></a>

# ResourceImporterBMFont

**Inherits:** [ResourceImporter](class_resourceimporter.md#class-resourceimporter) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Imports a bitmap font in the BMFont (`.fnt`) format.

<a id="description"></a>

## Description

The BMFont format is a format created by the [BMFont](https://www.angelcode.com/products/bmfont/) program. Many BMFont-compatible programs also exist, like [BMGlyph](https://www.bmglyph.com/).

Compared to [ResourceImporterImageFont](class_resourceimporterimagefont.md#class-resourceimporterimagefont), **ResourceImporterBMFont** supports bitmap fonts with varying glyph widths/heights.

See also [ResourceImporterDynamicFont](class_resourceimporterdynamicfont.md#class-resourceimporterdynamicfont).

<a id="tutorials"></a>

## Tutorials

- [Bitmap fonts - Using fonts](../tutorials/ui/gui_using_fonts.md#bitmap-fonts)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [compress](class_resourceimporterbmfont.md#class-resourceimporterbmfont-property-compress) | `true` |
| [Array](class_array.md#class-array) | [fallbacks](class_resourceimporterbmfont.md#class-resourceimporterbmfont-property-fallbacks) | `[]` |
| [int](class_int.md#class-int) | [scaling_mode](class_resourceimporterbmfont.md#class-resourceimporterbmfont-property-scaling-mode) | `2` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-resourceimporterbmfont-property-compress"></a>

[bool](class_bool.md#class-bool) **compress** = `true` [🔗](class_resourceimporterbmfont.md#class-resourceimporterbmfont-property-compress)

If `true`, uses lossless compression for the resulting font.

---


<a id="class-resourceimporterbmfont-property-fallbacks"></a>

[Array](class_array.md#class-array) **fallbacks** = `[]` [🔗](class_resourceimporterbmfont.md#class-resourceimporterbmfont-property-fallbacks)

List of font fallbacks to use if a glyph isn't found in this bitmap font. Fonts at the beginning of the array are attempted first.

---


<a id="class-resourceimporterbmfont-property-scaling-mode"></a>

[int](class_int.md#class-int) **scaling_mode** = `2` [🔗](class_resourceimporterbmfont.md#class-resourceimporterbmfont-property-scaling-mode)

Font scaling mode.
