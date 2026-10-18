> Source: https://docs.godotengine.org/en/4.7/classes/class_colorpalette.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="colorpalette"></a>

<a id="class-colorpalette"></a>

# ColorPalette

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A resource class for managing a palette of colors, which can be loaded and saved using [ColorPicker](class_colorpicker.md#class-colorpicker).

<a id="description"></a>

## Description

The **ColorPalette** resource is designed to store and manage a collection of colors. This resource is useful in scenarios where a predefined set of colors is required, such as for creating themes, designing user interfaces, or managing game assets. The built-in [ColorPicker](class_colorpicker.md#class-colorpicker) control can also make use of **ColorPalette** without additional code.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) | [colors](class_colorpalette.md#class-colorpalette-property-colors) | `PackedColorArray()` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-colorpalette-property-colors"></a>

[PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) **colors** = `PackedColorArray()` [🔗](class_colorpalette.md#class-colorpalette-property-colors)

- void **set_colors**(value: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray))
- [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) **get_colors**()

A [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) containing the colors in the palette.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) for more details.
