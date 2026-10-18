> Source: https://docs.godotengine.org/en/4.7/classes/class_gltfspecgloss.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="gltfspecgloss"></a>

<a id="class-gltfspecgloss"></a>

# GLTFSpecGloss

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Archived glTF extension for specular/glossy materials.

<a id="description"></a>

## Description

KHR_materials_pbrSpecularGlossiness is an archived glTF extension. This means that it is deprecated and not recommended for new files. However, it is still supported for loading old files.

<a id="tutorials"></a>

## Tutorials

- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving.md)
- [KHR_materials_pbrSpecularGlossiness glTF extension spec](https://github.com/KhronosGroup/glTF/blob/main/extensions/2.0/Archived/KHR_materials_pbrSpecularGlossiness)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Color](class_color.md#class-color) | [diffuse_factor](class_gltfspecgloss.md#class-gltfspecgloss-property-diffuse-factor) | `Color(1, 1, 1, 1)` |
| [Image](class_image.md#class-image) | [diffuse_img](class_gltfspecgloss.md#class-gltfspecgloss-property-diffuse-img) |  |
| [float](class_float.md#class-float) | [gloss_factor](class_gltfspecgloss.md#class-gltfspecgloss-property-gloss-factor) | `1.0` |
| [Image](class_image.md#class-image) | [spec_gloss_img](class_gltfspecgloss.md#class-gltfspecgloss-property-spec-gloss-img) |  |
| [Color](class_color.md#class-color) | [specular_factor](class_gltfspecgloss.md#class-gltfspecgloss-property-specular-factor) | `Color(1, 1, 1, 1)` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-gltfspecgloss-property-diffuse-factor"></a>

[Color](class_color.md#class-color) **diffuse_factor** = `Color(1, 1, 1, 1)` [🔗](class_gltfspecgloss.md#class-gltfspecgloss-property-diffuse-factor)

- void **set_diffuse_factor**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_diffuse_factor**()

The reflected diffuse factor of the material.

---


<a id="class-gltfspecgloss-property-diffuse-img"></a>

[Image](class_image.md#class-image) **diffuse_img** [🔗](class_gltfspecgloss.md#class-gltfspecgloss-property-diffuse-img)

- void **set_diffuse_img**(value: [Image](class_image.md#class-image))
- [Image](class_image.md#class-image) **get_diffuse_img**()

The diffuse texture.

---


<a id="class-gltfspecgloss-property-gloss-factor"></a>

[float](class_float.md#class-float) **gloss_factor** = `1.0` [🔗](class_gltfspecgloss.md#class-gltfspecgloss-property-gloss-factor)

- void **set_gloss_factor**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_gloss_factor**()

The glossiness or smoothness of the material.

---


<a id="class-gltfspecgloss-property-spec-gloss-img"></a>

[Image](class_image.md#class-image) **spec_gloss_img** [🔗](class_gltfspecgloss.md#class-gltfspecgloss-property-spec-gloss-img)

- void **set_spec_gloss_img**(value: [Image](class_image.md#class-image))
- [Image](class_image.md#class-image) **get_spec_gloss_img**()

The specular-glossiness texture.

---


<a id="class-gltfspecgloss-property-specular-factor"></a>

[Color](class_color.md#class-color) **specular_factor** = `Color(1, 1, 1, 1)` [🔗](class_gltfspecgloss.md#class-gltfspecgloss-property-specular-factor)

- void **set_specular_factor**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_specular_factor**()

The specular RGB color of the material. The alpha channel is unused.
