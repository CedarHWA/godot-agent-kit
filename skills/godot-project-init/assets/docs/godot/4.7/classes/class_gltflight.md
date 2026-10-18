> Source: https://docs.godotengine.org/en/4.7/classes/class_gltflight.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="gltflight"></a>

<a id="class-gltflight"></a>

# GLTFLight

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Represents a glTF light.

<a id="description"></a>

## Description

Represents a light as defined by the `KHR_lights_punctual` glTF extension.

<a id="tutorials"></a>

## Tutorials

- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving.md)
- [KHR_lights_punctual glTF extension spec](https://github.com/KhronosGroup/glTF/blob/main/extensions/2.0/Khronos/KHR_lights_punctual)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Color](class_color.md#class-color) | [color](class_gltflight.md#class-gltflight-property-color) | `Color(1, 1, 1, 1)` |
| [float](class_float.md#class-float) | [inner_cone_angle](class_gltflight.md#class-gltflight-property-inner-cone-angle) | `0.0` |
| [float](class_float.md#class-float) | [intensity](class_gltflight.md#class-gltflight-property-intensity) | `1.0` |
| [String](class_string.md#class-string) | [light_type](class_gltflight.md#class-gltflight-property-light-type) | `""` |
| [float](class_float.md#class-float) | [outer_cone_angle](class_gltflight.md#class-gltflight-property-outer-cone-angle) | `0.7853982` |
| [float](class_float.md#class-float) | [range](class_gltflight.md#class-gltflight-property-range) | `inf` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [GLTFLight](class_gltflight.md#class-gltflight) | [from_dictionary](class_gltflight.md#class-gltflight-method-from-dictionary)(dictionary: [Dictionary](class_dictionary.md#class-dictionary)) static |
| [GLTFLight](class_gltflight.md#class-gltflight) | [from_node](class_gltflight.md#class-gltflight-method-from-node)(light_node: [Light3D](class_light3d.md#class-light3d)) static |
| [Variant](class_variant.md#class-variant) | [get_additional_data](class_gltflight.md#class-gltflight-method-get-additional-data)(extension_name: [StringName](class_stringname.md#class-stringname)) |
| void | [set_additional_data](class_gltflight.md#class-gltflight-method-set-additional-data)(extension_name: [StringName](class_stringname.md#class-stringname), additional_data: [Variant](class_variant.md#class-variant)) |
| [Dictionary](class_dictionary.md#class-dictionary) | [to_dictionary](class_gltflight.md#class-gltflight-method-to-dictionary)() const |
| [Light3D](class_light3d.md#class-light3d) | [to_node](class_gltflight.md#class-gltflight-method-to-node)() const |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-gltflight-property-color"></a>

[Color](class_color.md#class-color) **color** = `Color(1, 1, 1, 1)` [🔗](class_gltflight.md#class-gltflight-property-color)

- void **set_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_color**()

The [Color](class_color.md#class-color) of the light in linear space. Defaults to white. A black color causes the light to have no effect.

This value is linear to match glTF, but will be converted to nonlinear sRGB when creating a Godot [Light3D](class_light3d.md#class-light3d) node upon import, or converted to linear when exporting a Godot [Light3D](class_light3d.md#class-light3d) to glTF.

---


<a id="class-gltflight-property-inner-cone-angle"></a>

[float](class_float.md#class-float) **inner_cone_angle** = `0.0` [🔗](class_gltflight.md#class-gltflight-property-inner-cone-angle)

- void **set_inner_cone_angle**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_inner_cone_angle**()

The inner angle of the cone in a spotlight. Must be less than or equal to the outer cone angle.

Within this angle, the light is at full brightness. Between the inner and outer cone angles, there is a transition from full brightness to zero brightness. When creating a Godot [SpotLight3D](class_spotlight3d.md#class-spotlight3d), the ratio between the inner and outer cone angles is used to calculate the attenuation of the light.

---


<a id="class-gltflight-property-intensity"></a>

[float](class_float.md#class-float) **intensity** = `1.0` [🔗](class_gltflight.md#class-gltflight-property-intensity)

- void **set_intensity**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_intensity**()

The intensity of the light. This is expressed in candelas (lumens per steradian) for point and spot lights, and lux (lumens per m²) for directional lights. When creating a Godot light, this value is converted to a unitless multiplier.

---


<a id="class-gltflight-property-light-type"></a>

[String](class_string.md#class-string) **light_type** = `""` [🔗](class_gltflight.md#class-gltflight-property-light-type)

- void **set_light_type**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_light_type**()

The type of the light. The values accepted by Godot are "point", "spot", and "directional", which correspond to Godot's [OmniLight3D](class_omnilight3d.md#class-omnilight3d), [SpotLight3D](class_spotlight3d.md#class-spotlight3d), and [DirectionalLight3D](class_directionallight3d.md#class-directionallight3d) respectively.

---


<a id="class-gltflight-property-outer-cone-angle"></a>

[float](class_float.md#class-float) **outer_cone_angle** = `0.7853982` [🔗](class_gltflight.md#class-gltflight-property-outer-cone-angle)

- void **set_outer_cone_angle**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_outer_cone_angle**()

The outer angle of the cone in a spotlight. Must be greater than or equal to the inner angle.

At this angle, the light drops off to zero brightness. Between the inner and outer cone angles, there is a transition from full brightness to zero brightness. If this angle is a half turn, then the spotlight emits in all directions. When creating a Godot [SpotLight3D](class_spotlight3d.md#class-spotlight3d), the outer cone angle is used as the angle of the spotlight.

---


<a id="class-gltflight-property-range"></a>

[float](class_float.md#class-float) **range** = `inf` [🔗](class_gltflight.md#class-gltflight-property-range)

- void **set_range**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_range**()

The range of the light, beyond which the light has no effect. glTF lights with no range defined behave like physical lights (which have infinite range). When creating a Godot light, the range is clamped to `4096.0`.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-gltflight-method-from-dictionary"></a>

[GLTFLight](class_gltflight.md#class-gltflight) **from_dictionary**(dictionary: [Dictionary](class_dictionary.md#class-dictionary)) static [🔗](class_gltflight.md#class-gltflight-method-from-dictionary)

Creates a new GLTFLight instance by parsing the given [Dictionary](class_dictionary.md#class-dictionary).

---


<a id="class-gltflight-method-from-node"></a>

[GLTFLight](class_gltflight.md#class-gltflight) **from_node**(light_node: [Light3D](class_light3d.md#class-light3d)) static [🔗](class_gltflight.md#class-gltflight-method-from-node)

Create a new GLTFLight instance from the given Godot [Light3D](class_light3d.md#class-light3d) node.

---


<a id="class-gltflight-method-get-additional-data"></a>

[Variant](class_variant.md#class-variant) **get_additional_data**(extension_name: [StringName](class_stringname.md#class-stringname)) [🔗](class_gltflight.md#class-gltflight-method-get-additional-data)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-gltflight-method-set-additional-data"></a>

void **set_additional_data**(extension_name: [StringName](class_stringname.md#class-stringname), additional_data: [Variant](class_variant.md#class-variant)) [🔗](class_gltflight.md#class-gltflight-method-set-additional-data)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-gltflight-method-to-dictionary"></a>

[Dictionary](class_dictionary.md#class-dictionary) **to_dictionary**() const [🔗](class_gltflight.md#class-gltflight-method-to-dictionary)

Serializes this GLTFLight instance into a [Dictionary](class_dictionary.md#class-dictionary).

---


<a id="class-gltflight-method-to-node"></a>

[Light3D](class_light3d.md#class-light3d) **to_node**() const [🔗](class_gltflight.md#class-gltflight-method-to-node)

Converts this GLTFLight instance into a Godot [Light3D](class_light3d.md#class-light3d) node.
