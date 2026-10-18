> Source: https://docs.godotengine.org/en/4.7/classes/class_panoramaskymaterial.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="panoramaskymaterial"></a>

<a id="class-panoramaskymaterial"></a>

# PanoramaSkyMaterial

**Inherits:** [Material](class_material.md#class-material) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A material that provides a special texture to a [Sky](class_sky.md#class-sky), usually an HDR panorama.

<a id="description"></a>

## Description

A resource referenced in a [Sky](class_sky.md#class-sky) that is used to draw a background. **PanoramaSkyMaterial** functions similar to skyboxes in other engines, except it uses an equirectangular sky map instead of a [Cubemap](class_cubemap.md#class-cubemap).

Using an HDR panorama is strongly recommended for accurate, high-quality reflections. Godot supports the Radiance HDR (`.hdr`) and OpenEXR (`.exr`) image formats for this purpose.

You can use [this tool](https://danilw.github.io/GLSL-howto/cubemap_to_panorama_js/cubemap_to_panorama.html) to convert a cubemap to an equirectangular sky map.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [energy_multiplier](class_panoramaskymaterial.md#class-panoramaskymaterial-property-energy-multiplier) | `1.0` |
| [bool](class_bool.md#class-bool) | [filter](class_panoramaskymaterial.md#class-panoramaskymaterial-property-filter) | `true` |
| [Texture2D](class_texture2d.md#class-texture2d) | [panorama](class_panoramaskymaterial.md#class-panoramaskymaterial-property-panorama) |  |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-panoramaskymaterial-property-energy-multiplier"></a>

[float](class_float.md#class-float) **energy_multiplier** = `1.0` [🔗](class_panoramaskymaterial.md#class-panoramaskymaterial-property-energy-multiplier)

- void **set_energy_multiplier**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_energy_multiplier**()

The sky's overall brightness multiplier. Higher values result in a brighter sky.

---


<a id="class-panoramaskymaterial-property-filter"></a>

[bool](class_bool.md#class-bool) **filter** = `true` [🔗](class_panoramaskymaterial.md#class-panoramaskymaterial-property-filter)

- void **set_filtering_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_filtering_enabled**()

A boolean value to determine if the background texture should be filtered or not.

---


<a id="class-panoramaskymaterial-property-panorama"></a>

[Texture2D](class_texture2d.md#class-texture2d) **panorama** [🔗](class_panoramaskymaterial.md#class-panoramaskymaterial-property-panorama)

- void **set_panorama**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_panorama**()

[Texture2D](class_texture2d.md#class-texture2d) to be applied to the **PanoramaSkyMaterial**.
