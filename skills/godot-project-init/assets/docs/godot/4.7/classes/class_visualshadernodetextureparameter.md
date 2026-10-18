> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodetextureparameter.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodetextureparameter"></a>

<a id="class-visualshadernodetextureparameter"></a>

# VisualShaderNodeTextureParameter

**Inherits:** [VisualShaderNodeParameter](class_visualshadernodeparameter.md#class-visualshadernodeparameter) **<** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [VisualShaderNodeCubemapParameter](class_visualshadernodecubemapparameter.md#class-visualshadernodecubemapparameter), [VisualShaderNodeTexture2DArrayParameter](class_visualshadernodetexture2darrayparameter.md#class-visualshadernodetexture2darrayparameter), [VisualShaderNodeTexture2DParameter](class_visualshadernodetexture2dparameter.md#class-visualshadernodetexture2dparameter), [VisualShaderNodeTexture3DParameter](class_visualshadernodetexture3dparameter.md#class-visualshadernodetexture3dparameter), [VisualShaderNodeTextureParameterTriplanar](class_visualshadernodetextureparametertriplanar.md#class-visualshadernodetextureparametertriplanar)

Performs a uniform texture lookup within the visual shader graph.

<a id="description"></a>

## Description

Performs a lookup operation on the texture provided as a uniform for the shader.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [ColorDefault](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-colordefault) | [color_default](class_visualshadernodetextureparameter.md#class-visualshadernodetextureparameter-property-color-default) | `0` |
| [TextureFilter](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturefilter) | [texture_filter](class_visualshadernodetextureparameter.md#class-visualshadernodetextureparameter-property-texture-filter) | `0` |
| [TextureRepeat](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturerepeat) | [texture_repeat](class_visualshadernodetextureparameter.md#class-visualshadernodetextureparameter-property-texture-repeat) | `0` |
| [TextureSource](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturesource) | [texture_source](class_visualshadernodetextureparameter.md#class-visualshadernodetextureparameter-property-texture-source) | `0` |
| [TextureType](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturetype) | [texture_type](class_visualshadernodetextureparameter.md#class-visualshadernodetextureparameter-property-texture-type) | `0` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-visualshadernodetextureparameter-texturetype"></a>

enum **TextureType**: [🔗](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturetype)

<a id="class-visualshadernodetextureparameter-constant-type-data"></a>

[TextureType](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturetype) **TYPE_DATA** = `0`

No hints are added to the uniform declaration.

<a id="class-visualshadernodetextureparameter-constant-type-color"></a>

[TextureType](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturetype) **TYPE_COLOR** = `1`

Adds `source_color` as hint to the uniform declaration for proper conversion from nonlinear sRGB encoding to linear encoding.

<a id="class-visualshadernodetextureparameter-constant-type-normal-map"></a>

[TextureType](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturetype) **TYPE_NORMAL_MAP** = `2`

Adds `hint_normal` as hint to the uniform declaration, which internally converts the texture for proper usage as normal map.

<a id="class-visualshadernodetextureparameter-constant-type-anisotropy"></a>

[TextureType](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturetype) **TYPE_ANISOTROPY** = `3`

Adds `hint_anisotropy` as hint to the uniform declaration to use for a flowmap.

<a id="class-visualshadernodetextureparameter-constant-type-max"></a>

[TextureType](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturetype) **TYPE_MAX** = `4`

Represents the size of the [TextureType](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturetype) enum.

---


<a id="enum-visualshadernodetextureparameter-colordefault"></a>

enum **ColorDefault**: [🔗](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-colordefault)

<a id="class-visualshadernodetextureparameter-constant-color-default-white"></a>

[ColorDefault](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-colordefault) **COLOR_DEFAULT_WHITE** = `0`

Defaults to fully opaque white color.

<a id="class-visualshadernodetextureparameter-constant-color-default-black"></a>

[ColorDefault](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-colordefault) **COLOR_DEFAULT_BLACK** = `1`

Defaults to fully opaque black color.

<a id="class-visualshadernodetextureparameter-constant-color-default-transparent"></a>

[ColorDefault](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-colordefault) **COLOR_DEFAULT_TRANSPARENT** = `2`

Defaults to fully transparent black color.

<a id="class-visualshadernodetextureparameter-constant-color-default-max"></a>

[ColorDefault](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-colordefault) **COLOR_DEFAULT_MAX** = `3`

Represents the size of the [ColorDefault](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-colordefault) enum.

---


<a id="enum-visualshadernodetextureparameter-texturefilter"></a>

enum **TextureFilter**: [🔗](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturefilter)

<a id="class-visualshadernodetextureparameter-constant-filter-default"></a>

[TextureFilter](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturefilter) **FILTER_DEFAULT** = `0`

Sample the texture using the filter determined by the node this shader is attached to.

<a id="class-visualshadernodetextureparameter-constant-filter-nearest"></a>

[TextureFilter](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturefilter) **FILTER_NEAREST** = `1`

The texture filter reads from the nearest pixel only. This makes the texture look pixelated from up close, and grainy from a distance (due to mipmaps not being sampled).

<a id="class-visualshadernodetextureparameter-constant-filter-linear"></a>

[TextureFilter](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturefilter) **FILTER_LINEAR** = `2`

The texture filter blends between the nearest 4 pixels. This makes the texture look smooth from up close, and grainy from a distance (due to mipmaps not being sampled).

<a id="class-visualshadernodetextureparameter-constant-filter-nearest-mipmap"></a>

[TextureFilter](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturefilter) **FILTER_NEAREST_MIPMAP** = `3`

The texture filter reads from the nearest pixel and blends between the nearest 2 mipmaps (or uses the nearest mipmap if [ProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filter](class_projectsettings.md#class-projectsettings-property-rendering-textures-default-filters-use-nearest-mipmap-filter) is `true`). This makes the texture look pixelated from up close, and smooth from a distance.

Use this for non-pixel art textures that may be viewed at a low scale (e.g. due to [Camera2D](class_camera2d.md#class-camera2d) zoom or sprite scaling), as mipmaps are important to smooth out pixels that are smaller than on-screen pixels.

<a id="class-visualshadernodetextureparameter-constant-filter-linear-mipmap"></a>

[TextureFilter](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturefilter) **FILTER_LINEAR_MIPMAP** = `4`

The texture filter blends between the nearest 4 pixels and between the nearest 2 mipmaps (or uses the nearest mipmap if [ProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filter](class_projectsettings.md#class-projectsettings-property-rendering-textures-default-filters-use-nearest-mipmap-filter) is `true`). This makes the texture look smooth from up close, and smooth from a distance.

Use this for non-pixel art textures that may be viewed at a low scale (e.g. due to [Camera2D](class_camera2d.md#class-camera2d) zoom or sprite scaling), as mipmaps are important to smooth out pixels that are smaller than on-screen pixels.

<a id="class-visualshadernodetextureparameter-constant-filter-nearest-mipmap-anisotropic"></a>

[TextureFilter](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturefilter) **FILTER_NEAREST_MIPMAP_ANISOTROPIC** = `5`

The texture filter reads from the nearest pixel and blends between 2 mipmaps (or uses the nearest mipmap if [ProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filter](class_projectsettings.md#class-projectsettings-property-rendering-textures-default-filters-use-nearest-mipmap-filter) is `true`) based on the angle between the surface and the camera view. This makes the texture look pixelated from up close, and smooth from a distance. Anisotropic filtering improves texture quality on surfaces that are almost in line with the camera, but is slightly slower. The anisotropic filtering level can be changed by adjusting [ProjectSettings.rendering/textures/default_filters/anisotropic_filtering_level](class_projectsettings.md#class-projectsettings-property-rendering-textures-default-filters-anisotropic-filtering-level).

**Note:** This texture filter is rarely useful in 2D projects. [FILTER_NEAREST_MIPMAP](class_visualshadernodetextureparameter.md#class-visualshadernodetextureparameter-constant-filter-nearest-mipmap) is usually more appropriate in this case.

<a id="class-visualshadernodetextureparameter-constant-filter-linear-mipmap-anisotropic"></a>

[TextureFilter](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturefilter) **FILTER_LINEAR_MIPMAP_ANISOTROPIC** = `6`

The texture filter blends between the nearest 4 pixels and blends between 2 mipmaps (or uses the nearest mipmap if [ProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filter](class_projectsettings.md#class-projectsettings-property-rendering-textures-default-filters-use-nearest-mipmap-filter) is `true`) based on the angle between the surface and the camera view. This makes the texture look smooth from up close, and smooth from a distance. Anisotropic filtering improves texture quality on surfaces that are almost in line with the camera, but is slightly slower. The anisotropic filtering level can be changed by adjusting [ProjectSettings.rendering/textures/default_filters/anisotropic_filtering_level](class_projectsettings.md#class-projectsettings-property-rendering-textures-default-filters-anisotropic-filtering-level).

**Note:** This texture filter is rarely useful in 2D projects. [FILTER_LINEAR_MIPMAP](class_visualshadernodetextureparameter.md#class-visualshadernodetextureparameter-constant-filter-linear-mipmap) is usually more appropriate in this case.

<a id="class-visualshadernodetextureparameter-constant-filter-max"></a>

[TextureFilter](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturefilter) **FILTER_MAX** = `7`

Represents the size of the [TextureFilter](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturefilter) enum.

---


<a id="enum-visualshadernodetextureparameter-texturerepeat"></a>

enum **TextureRepeat**: [🔗](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturerepeat)

<a id="class-visualshadernodetextureparameter-constant-repeat-default"></a>

[TextureRepeat](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturerepeat) **REPEAT_DEFAULT** = `0`

Sample the texture using the repeat mode determined by the node this shader is attached to.

<a id="class-visualshadernodetextureparameter-constant-repeat-enabled"></a>

[TextureRepeat](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturerepeat) **REPEAT_ENABLED** = `1`

Texture will repeat normally.

<a id="class-visualshadernodetextureparameter-constant-repeat-disabled"></a>

[TextureRepeat](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturerepeat) **REPEAT_DISABLED** = `2`

Texture will not repeat.

<a id="class-visualshadernodetextureparameter-constant-repeat-max"></a>

[TextureRepeat](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturerepeat) **REPEAT_MAX** = `3`

Represents the size of the [TextureRepeat](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturerepeat) enum.

---


<a id="enum-visualshadernodetextureparameter-texturesource"></a>

enum **TextureSource**: [🔗](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturesource)

<a id="class-visualshadernodetextureparameter-constant-source-none"></a>

[TextureSource](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturesource) **SOURCE_NONE** = `0`

The texture source is not specified in the shader.

<a id="class-visualshadernodetextureparameter-constant-source-screen"></a>

[TextureSource](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturesource) **SOURCE_SCREEN** = `1`

The texture source is the screen texture which captures all opaque objects drawn this frame.

<a id="class-visualshadernodetextureparameter-constant-source-depth"></a>

[TextureSource](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturesource) **SOURCE_DEPTH** = `2`

The texture source is the depth texture from the depth prepass.

<a id="class-visualshadernodetextureparameter-constant-source-normal-roughness"></a>

[TextureSource](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturesource) **SOURCE_NORMAL_ROUGHNESS** = `3`

The texture source is the normal-roughness buffer from the depth prepass.

<a id="class-visualshadernodetextureparameter-constant-source-max"></a>

[TextureSource](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturesource) **SOURCE_MAX** = `4`

Represents the size of the [TextureSource](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturesource) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodetextureparameter-property-color-default"></a>

[ColorDefault](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-colordefault) **color_default** = `0` [🔗](class_visualshadernodetextureparameter.md#class-visualshadernodetextureparameter-property-color-default)

- void **set_color_default**(value: [ColorDefault](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-colordefault))
- [ColorDefault](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-colordefault) **get_color_default**()

Sets the default color if no texture is assigned to the uniform.

---


<a id="class-visualshadernodetextureparameter-property-texture-filter"></a>

[TextureFilter](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturefilter) **texture_filter** = `0` [🔗](class_visualshadernodetextureparameter.md#class-visualshadernodetextureparameter-property-texture-filter)

- void **set_texture_filter**(value: [TextureFilter](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturefilter))
- [TextureFilter](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturefilter) **get_texture_filter**()

Sets the texture filtering mode.

---


<a id="class-visualshadernodetextureparameter-property-texture-repeat"></a>

[TextureRepeat](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturerepeat) **texture_repeat** = `0` [🔗](class_visualshadernodetextureparameter.md#class-visualshadernodetextureparameter-property-texture-repeat)

- void **set_texture_repeat**(value: [TextureRepeat](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturerepeat))
- [TextureRepeat](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturerepeat) **get_texture_repeat**()

Sets the texture repeating mode.

---


<a id="class-visualshadernodetextureparameter-property-texture-source"></a>

[TextureSource](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturesource) **texture_source** = `0` [🔗](class_visualshadernodetextureparameter.md#class-visualshadernodetextureparameter-property-texture-source)

- void **set_texture_source**(value: [TextureSource](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturesource))
- [TextureSource](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturesource) **get_texture_source**()

Sets the texture source mode. Used for reading from the screen, depth, or normal_roughness texture.

---


<a id="class-visualshadernodetextureparameter-property-texture-type"></a>

[TextureType](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturetype) **texture_type** = `0` [🔗](class_visualshadernodetextureparameter.md#class-visualshadernodetextureparameter-property-texture-type)

- void **set_texture_type**(value: [TextureType](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturetype))
- [TextureType](class_visualshadernodetextureparameter.md#enum-visualshadernodetextureparameter-texturetype) **get_texture_type**()

Defines the type of data provided by the source texture.
