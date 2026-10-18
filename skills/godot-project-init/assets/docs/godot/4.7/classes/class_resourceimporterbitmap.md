> Source: https://docs.godotengine.org/en/4.7/classes/class_resourceimporterbitmap.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="resourceimporterbitmap"></a>

<a id="class-resourceimporterbitmap"></a>

# ResourceImporterBitMap

**Inherits:** [ResourceImporter](class_resourceimporter.md#class-resourceimporter) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Imports a [BitMap](class_bitmap.md#class-bitmap) resource (2D array of boolean values).

<a id="description"></a>

## Description

[BitMap](class_bitmap.md#class-bitmap) resources are typically used as click masks in [TextureButton](class_texturebutton.md#class-texturebutton) and [TouchScreenButton](class_touchscreenbutton.md#class-touchscreenbutton).

<a id="tutorials"></a>

## Tutorials

- [Importing images](../tutorials/assets_pipeline/importing_images.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [create_from](class_resourceimporterbitmap.md#class-resourceimporterbitmap-property-create-from) | `0` |
| [float](class_float.md#class-float) | [threshold](class_resourceimporterbitmap.md#class-resourceimporterbitmap-property-threshold) | `0.5` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-resourceimporterbitmap-property-create-from"></a>

[int](class_int.md#class-int) **create_from** = `0` [🔗](class_resourceimporterbitmap.md#class-resourceimporterbitmap-property-create-from)

The data source to use for generating the bitmap.

**Black & White:** Pixels whose HSV value is greater than the [threshold](class_resourceimporterbitmap.md#class-resourceimporterbitmap-property-threshold) will be considered as "enabled" (bit is `true`). If the pixel is lower than or equal to the threshold, it will be considered as "disabled" (bit is `false`).

**Alpha:** Pixels whose alpha value is greater than the [threshold](class_resourceimporterbitmap.md#class-resourceimporterbitmap-property-threshold) will be considered as "enabled" (bit is `true`). If the pixel is lower than or equal to the threshold, it will be considered as "disabled" (bit is `false`).

---


<a id="class-resourceimporterbitmap-property-threshold"></a>

[float](class_float.md#class-float) **threshold** = `0.5` [🔗](class_resourceimporterbitmap.md#class-resourceimporterbitmap-property-threshold)

The threshold to use to determine which bits should be considered enabled or disabled. See also [create_from](class_resourceimporterbitmap.md#class-resourceimporterbitmap-property-create-from).
