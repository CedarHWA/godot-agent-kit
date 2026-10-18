> Source: https://docs.godotengine.org/en/4.7/classes/class_resourceimportersvg.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="resourceimportersvg"></a>

<a id="class-resourceimportersvg"></a>

# ResourceImporterSVG

**Inherits:** [ResourceImporter](class_resourceimporter.md#class-resourceimporter) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Imports an SVG file as an automatically scalable texture for use in UI elements and 2D rendering.

<a id="description"></a>

## Description

This importer imports [DPITexture](class_dpitexture.md#class-dpitexture) resources. See also [ResourceImporterTexture](class_resourceimportertexture.md#class-resourceimportertexture) and [ResourceImporterImage](class_resourceimporterimage.md#class-resourceimporterimage).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [base_scale](class_resourceimportersvg.md#class-resourceimportersvg-property-base-scale) | `1.0` |
| [Dictionary](class_dictionary.md#class-dictionary) | [color_map](class_resourceimportersvg.md#class-resourceimportersvg-property-color-map) | `{}` |
| [bool](class_bool.md#class-bool) | [compress](class_resourceimportersvg.md#class-resourceimportersvg-property-compress) | `true` |
| [bool](class_bool.md#class-bool) | [fix_alpha_border](class_resourceimportersvg.md#class-resourceimportersvg-property-fix-alpha-border) | `false` |
| [bool](class_bool.md#class-bool) | [premult_alpha](class_resourceimportersvg.md#class-resourceimportersvg-property-premult-alpha) | `false` |
| [float](class_float.md#class-float) | [saturation](class_resourceimportersvg.md#class-resourceimportersvg-property-saturation) | `1.0` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-resourceimportersvg-property-base-scale"></a>

[float](class_float.md#class-float) **base_scale** = `1.0` [🔗](class_resourceimportersvg.md#class-resourceimportersvg-property-base-scale)

Texture scale. `1.0` is the original SVG size. Higher values result in a larger image.

---


<a id="class-resourceimportersvg-property-color-map"></a>

[Dictionary](class_dictionary.md#class-dictionary) **color_map** = `{}` [🔗](class_resourceimportersvg.md#class-resourceimportersvg-property-color-map)

If set, remaps texture colors according to [Color](class_color.md#class-color)-[Color](class_color.md#class-color) map.

---


<a id="class-resourceimportersvg-property-compress"></a>

[bool](class_bool.md#class-bool) **compress** = `true` [🔗](class_resourceimportersvg.md#class-resourceimportersvg-property-compress)

If `true`, uses lossless compression for the SVG source.

---


<a id="class-resourceimportersvg-property-fix-alpha-border"></a>

[bool](class_bool.md#class-bool) **fix_alpha_border** = `false` [🔗](class_resourceimportersvg.md#class-resourceimportersvg-property-fix-alpha-border)

If `true`, puts pixels of the same surrounding color in transition from transparent to opaque areas. For textures displayed with bilinear filtering, this helps to reduce the outline effect when exporting images from an image editor.

---


<a id="class-resourceimportersvg-property-premult-alpha"></a>

[bool](class_bool.md#class-bool) **premult_alpha** = `false` [🔗](class_resourceimportersvg.md#class-resourceimportersvg-property-premult-alpha)

An alternative to fixing darkened borders with [fix_alpha_border](class_resourceimportersvg.md#class-resourceimportersvg-property-fix-alpha-border) is to use premultiplied alpha. By enabling this option, the texture will be converted to this format. A premultiplied alpha texture requires specific materials to be displayed correctly:

- In 2D, a [CanvasItemMaterial](class_canvasitemmaterial.md#class-canvasitemmaterial) will need to be created and configured to use the [CanvasItemMaterial.BLEND_MODE_PREMULT_ALPHA](class_canvasitemmaterial.md#class-canvasitemmaterial-constant-blend-mode-premult-alpha) blend mode on [CanvasItem](class_canvasitem.md#class-canvasitem)s that use this texture. In custom `canvas_item` shaders, `render_mode blend_premul_alpha;` should be used.
- In 3D, a [BaseMaterial3D](class_basematerial3d.md#class-basematerial3d) will need to be created and configured to use the [BaseMaterial3D.BLEND_MODE_PREMULT_ALPHA](class_basematerial3d.md#class-basematerial3d-constant-blend-mode-premult-alpha) blend mode on materials that use this texture. In custom `spatial` shaders, `render_mode blend_premul_alpha;` should be used.

---


<a id="class-resourceimportersvg-property-saturation"></a>

[float](class_float.md#class-float) **saturation** = `1.0` [🔗](class_resourceimportersvg.md#class-resourceimportersvg-property-saturation)

Overrides texture saturation.
