> Source: https://docs.godotengine.org/en/4.7/classes/class_cubemaparray.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="cubemaparray"></a>

<a id="class-cubemaparray"></a>

# CubemapArray

**Inherits:** [ImageTextureLayered](class_imagetexturelayered.md#class-imagetexturelayered) **<** [TextureLayered](class_texturelayered.md#class-texturelayered) **<** [Texture](class_texture.md#class-texture) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

An array of [Cubemap](class_cubemap.md#class-cubemap)s, stored together and with a single reference.

<a id="description"></a>

## Description

**CubemapArray**s are made of an array of [Cubemap](class_cubemap.md#class-cubemap)s. Like [Cubemap](class_cubemap.md#class-cubemap)s, they are made of multiple textures, the amount of which must be divisible by 6 (one for each face of the cube).

The primary benefit of **CubemapArray**s is that they can be accessed in shader code using a single texture reference. In other words, you can pass multiple [Cubemap](class_cubemap.md#class-cubemap)s into a shader using a single **CubemapArray**. [Cubemap](class_cubemap.md#class-cubemap)s are allocated in adjacent cache regions on the GPU, which makes **CubemapArray**s the most efficient way to store multiple [Cubemap](class_cubemap.md#class-cubemap)s.

Godot uses **CubemapArray**s internally for many effects, including the [Sky](class_sky.md#class-sky) if you set [ProjectSettings.rendering/reflections/sky_reflections/texture_array_reflections](class_projectsettings.md#class-projectsettings-property-rendering-reflections-sky-reflections-texture-array-reflections) to `true`.

To create such a texture file yourself, reimport your image files using the Godot Editor import presets. To create a CubemapArray from code, use [ImageTextureLayered.create_from_images()](class_imagetexturelayered.md#class-imagetexturelayered-method-create-from-images) on an instance of the CubemapArray class.

The expected image order is X+, X-, Y+, Y-, Z+, Z- (in Godot's coordinate system, so Y+ is "up" and Z- is "forward"). You can use one of the following templates as a base:

- [2×3 cubemap template (default layout option)](https://raw.githubusercontent.com/godotengine/godot-docs/master/tutorials/assets_pipeline/img/cubemap_template_2x3.webp)
- [3×2 cubemap template](https://raw.githubusercontent.com/godotengine/godot-docs/master/tutorials/assets_pipeline/img/cubemap_template_3x2.webp)
- [1×6 cubemap template](https://raw.githubusercontent.com/godotengine/godot-docs/master/tutorials/assets_pipeline/img/cubemap_template_1x6.webp)
- [6×1 cubemap template](https://raw.githubusercontent.com/godotengine/godot-docs/master/tutorials/assets_pipeline/img/cubemap_template_6x1.webp)

Multiple layers are stacked on top of each other when using the default vertical import option (with the first layer at the top). Alternatively, you can choose a horizontal layout in the import options (with the first layer at the left).

**Note:** **CubemapArray** is not supported in the Compatibility renderer due to graphics API limitations.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Resource](class_resource.md#class-resource) | [create_placeholder](class_cubemaparray.md#class-cubemaparray-method-create-placeholder)() const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-cubemaparray-method-create-placeholder"></a>

[Resource](class_resource.md#class-resource) **create_placeholder**() const [🔗](class_cubemaparray.md#class-cubemaparray-method-create-placeholder)

Creates a placeholder version of this resource ([PlaceholderCubemapArray](class_placeholdercubemaparray.md#class-placeholdercubemaparray)).
