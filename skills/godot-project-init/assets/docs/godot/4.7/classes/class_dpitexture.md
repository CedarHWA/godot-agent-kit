> Source: https://docs.godotengine.org/en/4.7/classes/class_dpitexture.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="dpitexture"></a>

<a id="class-dpitexture"></a>

# DPITexture

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [Texture2D](class_texture2d.md#class-texture2d) **<** [Texture](class_texture.md#class-texture) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

An automatically scalable [Texture2D](class_texture2d.md#class-texture2d) based on an SVG image.

<a id="description"></a>

## Description

An automatically scalable [Texture2D](class_texture2d.md#class-texture2d) based on an SVG image. **DPITexture**s are used to automatically re-rasterize icons and other texture based UI theme elements to match viewport scale and font oversampling. See also [ProjectSettings.display/window/stretch/mode](class_projectsettings.md#class-projectsettings-property-display-window-stretch-mode) ("canvas_items" mode) and [Viewport.oversampling_override](class_viewport.md#class-viewport-property-oversampling-override).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [base_scale](class_dpitexture.md#class-dpitexture-property-base-scale) | `1.0` |
| [Dictionary](class_dictionary.md#class-dictionary) | [color_map](class_dpitexture.md#class-dpitexture-property-color-map) | `{}` |
| [bool](class_bool.md#class-bool) | [fix_alpha_border](class_dpitexture.md#class-dpitexture-property-fix-alpha-border) | `false` |
| [bool](class_bool.md#class-bool) | [premult_alpha](class_dpitexture.md#class-dpitexture-property-premult-alpha) | `false` |
| [bool](class_bool.md#class-bool) | resource_local_to_scene | `false` (overrides [Resource](class_resource.md#class-resource-property-resource-local-to-scene)) |
| [float](class_float.md#class-float) | [saturation](class_dpitexture.md#class-dpitexture-property-saturation) | `1.0` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [DPITexture](class_dpitexture.md#class-dpitexture) | [create_from_string](class_dpitexture.md#class-dpitexture-method-create-from-string)(source: [String](class_string.md#class-string), scale: [float](class_float.md#class-float) = 1.0, saturation: [float](class_float.md#class-float) = 1.0, color_map: [Dictionary](class_dictionary.md#class-dictionary) = {}) static |
| [RID](class_rid.md#class-rid) | [get_scaled_rid](class_dpitexture.md#class-dpitexture-method-get-scaled-rid)() const |
| [String](class_string.md#class-string) | [get_source](class_dpitexture.md#class-dpitexture-method-get-source)() const |
| void | [set_size_override](class_dpitexture.md#class-dpitexture-method-set-size-override)(size: [Vector2i](class_vector2i.md#class-vector2i)) |
| void | [set_source](class_dpitexture.md#class-dpitexture-method-set-source)(source: [String](class_string.md#class-string)) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-dpitexture-property-base-scale"></a>

[float](class_float.md#class-float) **base_scale** = `1.0` [🔗](class_dpitexture.md#class-dpitexture-property-base-scale)

- void **set_base_scale**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_base_scale**()

Texture scale. `1.0` is the original SVG size. Higher values result in a larger image.

---


<a id="class-dpitexture-property-color-map"></a>

[Dictionary](class_dictionary.md#class-dictionary) **color_map** = `{}` [🔗](class_dpitexture.md#class-dpitexture-property-color-map)

- void **set_color_map**(value: [Dictionary](class_dictionary.md#class-dictionary))
- [Dictionary](class_dictionary.md#class-dictionary) **get_color_map**()

If set, remaps texture colors according to [Color](class_color.md#class-color)-[Color](class_color.md#class-color) map.

---


<a id="class-dpitexture-property-fix-alpha-border"></a>

[bool](class_bool.md#class-bool) **fix_alpha_border** = `false` [🔗](class_dpitexture.md#class-dpitexture-property-fix-alpha-border)

- void **set_fix_alpha_border**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_fix_alpha_border**()

If `true`, puts pixels of the same surrounding color in transition from transparent to opaque areas. For textures displayed with bilinear filtering, this helps to reduce the outline effect when exporting images from an image editor.

---


<a id="class-dpitexture-property-premult-alpha"></a>

[bool](class_bool.md#class-bool) **premult_alpha** = `false` [🔗](class_dpitexture.md#class-dpitexture-property-premult-alpha)

- void **set_premult_alpha**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_premult_alpha**()

An alternative to fixing darkened borders with [fix_alpha_border](class_dpitexture.md#class-dpitexture-property-fix-alpha-border) is to use premultiplied alpha. By enabling this option, the texture will be converted to this format. A premultiplied alpha texture requires specific materials to be displayed correctly:

- In 2D, a [CanvasItemMaterial](class_canvasitemmaterial.md#class-canvasitemmaterial) will need to be created and configured to use the [CanvasItemMaterial.BLEND_MODE_PREMULT_ALPHA](class_canvasitemmaterial.md#class-canvasitemmaterial-constant-blend-mode-premult-alpha) blend mode on [CanvasItem](class_canvasitem.md#class-canvasitem)s that use this texture. In custom `canvas_item` shaders, `render_mode blend_premul_alpha;` should be used.
- In 3D, a [BaseMaterial3D](class_basematerial3d.md#class-basematerial3d) will need to be created and configured to use the [BaseMaterial3D.BLEND_MODE_PREMULT_ALPHA](class_basematerial3d.md#class-basematerial3d-constant-blend-mode-premult-alpha) blend mode on materials that use this texture. In custom `spatial` shaders, `render_mode blend_premul_alpha;` should be used.

---


<a id="class-dpitexture-property-saturation"></a>

[float](class_float.md#class-float) **saturation** = `1.0` [🔗](class_dpitexture.md#class-dpitexture-property-saturation)

- void **set_saturation**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_saturation**()

Overrides texture saturation.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-dpitexture-method-create-from-string"></a>

[DPITexture](class_dpitexture.md#class-dpitexture) **create_from_string**(source: [String](class_string.md#class-string), scale: [float](class_float.md#class-float) = 1.0, saturation: [float](class_float.md#class-float) = 1.0, color_map: [Dictionary](class_dictionary.md#class-dictionary) = {}) static [🔗](class_dpitexture.md#class-dpitexture-method-create-from-string)

Creates a new **DPITexture** and initializes it by allocating and setting the SVG data to `source`.

---


<a id="class-dpitexture-method-get-scaled-rid"></a>

[RID](class_rid.md#class-rid) **get_scaled_rid**() const [🔗](class_dpitexture.md#class-dpitexture-method-get-scaled-rid)

Returns the [RID](class_rid.md#class-rid) of the texture rasterized to match the oversampling of the currently drawn canvas item.

---


<a id="class-dpitexture-method-get-source"></a>

[String](class_string.md#class-string) **get_source**() const [🔗](class_dpitexture.md#class-dpitexture-method-get-source)

Returns this SVG texture's source code.

---


<a id="class-dpitexture-method-set-size-override"></a>

void **set_size_override**(size: [Vector2i](class_vector2i.md#class-vector2i)) [🔗](class_dpitexture.md#class-dpitexture-method-set-size-override)

Resizes the texture to the specified dimensions.

---


<a id="class-dpitexture-method-set-source"></a>

void **set_source**(source: [String](class_string.md#class-string)) [🔗](class_dpitexture.md#class-dpitexture-method-set-source)

Sets this SVG texture's source code.
