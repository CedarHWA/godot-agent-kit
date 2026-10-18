> Source: https://docs.godotengine.org/en/4.7/classes/class_shader.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="shader"></a>

<a id="class-shader"></a>

# Shader

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [VisualShader](class_visualshader.md#class-visualshader)

A shader implemented in the Godot shading language.

<a id="description"></a>

## Description

A custom shader program implemented in the Godot shading language, saved with the `.gdshader` extension.

This class is used by a [ShaderMaterial](class_shadermaterial.md#class-shadermaterial) and allows you to write your own custom behavior for rendering visual items or updating particle information. For a detailed explanation and usage, please see the tutorials linked below.

<a id="tutorials"></a>

## Tutorials

- [Shaders documentation index](../tutorials/shaders/index.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [String](class_string.md#class-string) | [code](class_shader.md#class-shader-property-code) | `""` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Texture](class_texture.md#class-texture) | [get_default_texture_parameter](class_shader.md#class-shader-method-get-default-texture-parameter)(name: [StringName](class_stringname.md#class-stringname), index: [int](class_int.md#class-int) = 0) const |
| [Mode](class_shader.md#enum-shader-mode) | [get_mode](class_shader.md#class-shader-method-get-mode)() const |
| [Array](class_array.md#class-array) | [get_shader_uniform_list](class_shader.md#class-shader-method-get-shader-uniform-list)(get_groups: [bool](class_bool.md#class-bool) = false) |
| void | [inspect_native_shader_code](class_shader.md#class-shader-method-inspect-native-shader-code)() |
| void | [set_default_texture_parameter](class_shader.md#class-shader-method-set-default-texture-parameter)(name: [StringName](class_stringname.md#class-stringname), texture: [Texture](class_texture.md#class-texture), index: [int](class_int.md#class-int) = 0) |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-shader-mode"></a>

enum **Mode**: [🔗](class_shader.md#enum-shader-mode)

<a id="class-shader-constant-mode-spatial"></a>

[Mode](class_shader.md#enum-shader-mode) **MODE_SPATIAL** = `0`

Mode used to draw all 3D objects.

<a id="class-shader-constant-mode-canvas-item"></a>

[Mode](class_shader.md#enum-shader-mode) **MODE_CANVAS_ITEM** = `1`

Mode used to draw all 2D objects.

<a id="class-shader-constant-mode-particles"></a>

[Mode](class_shader.md#enum-shader-mode) **MODE_PARTICLES** = `2`

Mode used to calculate particle information on a per-particle basis. Not used for drawing.

<a id="class-shader-constant-mode-sky"></a>

[Mode](class_shader.md#enum-shader-mode) **MODE_SKY** = `3`

Mode used for drawing skies. Only works with shaders attached to [Sky](class_sky.md#class-sky) objects.

<a id="class-shader-constant-mode-fog"></a>

[Mode](class_shader.md#enum-shader-mode) **MODE_FOG** = `4`

Mode used for setting the color and density of volumetric fog effect.

<a id="class-shader-constant-mode-texture-blit"></a>

[Mode](class_shader.md#enum-shader-mode) **MODE_TEXTURE_BLIT** = `5`

Mode used for drawing to DrawableTexture resources via blit calls.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-shader-property-code"></a>

[String](class_string.md#class-string) **code** = `""` [🔗](class_shader.md#class-shader-property-code)

- void **set_code**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_code**()

Returns the shader's code as the user has written it, not the full generated code used internally.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-shader-method-get-default-texture-parameter"></a>

[Texture](class_texture.md#class-texture) **get_default_texture_parameter**(name: [StringName](class_stringname.md#class-stringname), index: [int](class_int.md#class-int) = 0) const [🔗](class_shader.md#class-shader-method-get-default-texture-parameter)

Returns the texture that is set as default for the specified parameter.

**Note:** `name` must match the name of the uniform in the code exactly.

**Note:** If the sampler array is used use `index` to access the specified texture.

---


<a id="class-shader-method-get-mode"></a>

[Mode](class_shader.md#enum-shader-mode) **get_mode**() const [🔗](class_shader.md#class-shader-method-get-mode)

Returns the shader mode for the shader.

---


<a id="class-shader-method-get-shader-uniform-list"></a>

[Array](class_array.md#class-array) **get_shader_uniform_list**(get_groups: [bool](class_bool.md#class-bool) = false) [🔗](class_shader.md#class-shader-method-get-shader-uniform-list)

Returns the list of shader uniforms that can be assigned to a [ShaderMaterial](class_shadermaterial.md#class-shadermaterial), for use with [ShaderMaterial.set_shader_parameter()](class_shadermaterial.md#class-shadermaterial-method-set-shader-parameter) and [ShaderMaterial.get_shader_parameter()](class_shadermaterial.md#class-shadermaterial-method-get-shader-parameter). The parameters returned are contained in dictionaries in a similar format to the ones returned by [Object.get_property_list()](class_object.md#class-object-method-get-property-list).

If argument `get_groups` is `true`, parameter grouping hints are also included in the list.

---


<a id="class-shader-method-inspect-native-shader-code"></a>

void **inspect_native_shader_code**() [🔗](class_shader.md#class-shader-method-inspect-native-shader-code)

Only available when running in the editor. Opens a popup that visualizes the generated shader code, including all variants and internal shader code. See also [Material.inspect_native_shader_code()](class_material.md#class-material-method-inspect-native-shader-code).

---


<a id="class-shader-method-set-default-texture-parameter"></a>

void **set_default_texture_parameter**(name: [StringName](class_stringname.md#class-stringname), texture: [Texture](class_texture.md#class-texture), index: [int](class_int.md#class-int) = 0) [🔗](class_shader.md#class-shader-method-set-default-texture-parameter)

Sets the default texture to be used with a texture uniform. The default is used if a texture is not set in the [ShaderMaterial](class_shadermaterial.md#class-shadermaterial).

**Note:** `name` must match the name of the uniform in the code exactly.

**Note:** If the sampler array is used use `index` to access the specified texture.
