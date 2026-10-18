> Source: https://docs.godotengine.org/en/4.7/classes/class_shaderinclude.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="shaderinclude"></a>

<a id="class-shaderinclude"></a>

# ShaderInclude

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A snippet of shader code to be included in a [Shader](class_shader.md#class-shader) with `#include`.

<a id="description"></a>

## Description

A shader include file, saved with the `.gdshaderinc` extension. This class allows you to define a custom shader snippet that can be included in a [Shader](class_shader.md#class-shader) by using the preprocessor directive `#include`, followed by the file path (e.g. `#include "res://shader_lib.gdshaderinc"`). The snippet doesn't have to be a valid shader on its own.

<a id="tutorials"></a>

## Tutorials

- [Shader preprocessor](../tutorials/shaders/shader_reference/shader_preprocessor.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [String](class_string.md#class-string) | [code](class_shaderinclude.md#class-shaderinclude-property-code) | `""` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-shaderinclude-property-code"></a>

[String](class_string.md#class-string) **code** = `""` [🔗](class_shaderinclude.md#class-shaderinclude-property-code)

- void **set_code**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_code**()

Returns the code of the shader include file. The returned text is what the user has written, not the full generated code used internally.
