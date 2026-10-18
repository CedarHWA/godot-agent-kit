> Source: https://docs.godotengine.org/en/4.7/classes/class_rdshadersource.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="rdshadersource"></a>

<a id="class-rdshadersource"></a>

# RDShaderSource

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Shader source code (used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice)).

<a id="description"></a>

## Description

Shader source code in text form.

See also [RDShaderFile](class_rdshaderfile.md#class-rdshaderfile). **RDShaderSource** is only meant to be used with the [RenderingDevice](class_renderingdevice.md#class-renderingdevice) API. It should not be confused with Godot's own [Shader](class_shader.md#class-shader) resource, which is what Godot's various nodes use for high-level shader programming.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [ShaderLanguage](class_renderingdevice.md#enum-renderingdevice-shaderlanguage) | [language](class_rdshadersource.md#class-rdshadersource-property-language) | `0` |
| [String](class_string.md#class-string) | [source_any_hit](class_rdshadersource.md#class-rdshadersource-property-source-any-hit) | `""` |
| [String](class_string.md#class-string) | [source_closest_hit](class_rdshadersource.md#class-rdshadersource-property-source-closest-hit) | `""` |
| [String](class_string.md#class-string) | [source_compute](class_rdshadersource.md#class-rdshadersource-property-source-compute) | `""` |
| [String](class_string.md#class-string) | [source_fragment](class_rdshadersource.md#class-rdshadersource-property-source-fragment) | `""` |
| [String](class_string.md#class-string) | [source_intersection](class_rdshadersource.md#class-rdshadersource-property-source-intersection) | `""` |
| [String](class_string.md#class-string) | [source_miss](class_rdshadersource.md#class-rdshadersource-property-source-miss) | `""` |
| [String](class_string.md#class-string) | [source_raygen](class_rdshadersource.md#class-rdshadersource-property-source-raygen) | `""` |
| [String](class_string.md#class-string) | [source_tesselation_control](class_rdshadersource.md#class-rdshadersource-property-source-tesselation-control) | `""` |
| [String](class_string.md#class-string) | [source_tesselation_evaluation](class_rdshadersource.md#class-rdshadersource-property-source-tesselation-evaluation) | `""` |
| [String](class_string.md#class-string) | [source_vertex](class_rdshadersource.md#class-rdshadersource-property-source-vertex) | `""` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [String](class_string.md#class-string) | [get_stage_source](class_rdshadersource.md#class-rdshadersource-method-get-stage-source)(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) const |
| void | [set_stage_source](class_rdshadersource.md#class-rdshadersource-method-set-stage-source)(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), source: [String](class_string.md#class-string)) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-rdshadersource-property-language"></a>

[ShaderLanguage](class_renderingdevice.md#enum-renderingdevice-shaderlanguage) **language** = `0` [🔗](class_rdshadersource.md#class-rdshadersource-property-language)

- void **set_language**(value: [ShaderLanguage](class_renderingdevice.md#enum-renderingdevice-shaderlanguage))
- [ShaderLanguage](class_renderingdevice.md#enum-renderingdevice-shaderlanguage) **get_language**()

The language the shader is written in.

---


<a id="class-rdshadersource-property-source-any-hit"></a>

[String](class_string.md#class-string) **source_any_hit** = `""` [🔗](class_rdshadersource.md#class-rdshadersource-property-source-any-hit)

- void **set_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), source: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) const

Source code for the shader's any hit stage.

---


<a id="class-rdshadersource-property-source-closest-hit"></a>

[String](class_string.md#class-string) **source_closest_hit** = `""` [🔗](class_rdshadersource.md#class-rdshadersource-property-source-closest-hit)

- void **set_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), source: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) const

Source code for the shader's closest hit stage.

---


<a id="class-rdshadersource-property-source-compute"></a>

[String](class_string.md#class-string) **source_compute** = `""` [🔗](class_rdshadersource.md#class-rdshadersource-property-source-compute)

- void **set_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), source: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) const

Source code for the shader's compute stage.

---


<a id="class-rdshadersource-property-source-fragment"></a>

[String](class_string.md#class-string) **source_fragment** = `""` [🔗](class_rdshadersource.md#class-rdshadersource-property-source-fragment)

- void **set_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), source: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) const

Source code for the shader's fragment stage.

---


<a id="class-rdshadersource-property-source-intersection"></a>

[String](class_string.md#class-string) **source_intersection** = `""` [🔗](class_rdshadersource.md#class-rdshadersource-property-source-intersection)

- void **set_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), source: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) const

Source code for the shader's intersection stage.

---


<a id="class-rdshadersource-property-source-miss"></a>

[String](class_string.md#class-string) **source_miss** = `""` [🔗](class_rdshadersource.md#class-rdshadersource-property-source-miss)

- void **set_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), source: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) const

Source code for the shader's miss stage.

---


<a id="class-rdshadersource-property-source-raygen"></a>

[String](class_string.md#class-string) **source_raygen** = `""` [🔗](class_rdshadersource.md#class-rdshadersource-property-source-raygen)

- void **set_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), source: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) const

Source code for the shader's ray generation stage.

---


<a id="class-rdshadersource-property-source-tesselation-control"></a>

[String](class_string.md#class-string) **source_tesselation_control** = `""` [🔗](class_rdshadersource.md#class-rdshadersource-property-source-tesselation-control)

- void **set_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), source: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) const

Source code for the shader's tessellation control stage.

---


<a id="class-rdshadersource-property-source-tesselation-evaluation"></a>

[String](class_string.md#class-string) **source_tesselation_evaluation** = `""` [🔗](class_rdshadersource.md#class-rdshadersource-property-source-tesselation-evaluation)

- void **set_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), source: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) const

Source code for the shader's tessellation evaluation stage.

---


<a id="class-rdshadersource-property-source-vertex"></a>

[String](class_string.md#class-string) **source_vertex** = `""` [🔗](class_rdshadersource.md#class-rdshadersource-property-source-vertex)

- void **set_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), source: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) const

Source code for the shader's vertex stage.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-rdshadersource-method-get-stage-source"></a>

[String](class_string.md#class-string) **get_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) const [🔗](class_rdshadersource.md#class-rdshadersource-method-get-stage-source)

Returns source code for the specified shader `stage`. Equivalent to getting one of [source_compute](class_rdshadersource.md#class-rdshadersource-property-source-compute), [source_fragment](class_rdshadersource.md#class-rdshadersource-property-source-fragment), [source_tesselation_control](class_rdshadersource.md#class-rdshadersource-property-source-tesselation-control), [source_tesselation_evaluation](class_rdshadersource.md#class-rdshadersource-property-source-tesselation-evaluation) or [source_vertex](class_rdshadersource.md#class-rdshadersource-property-source-vertex).

---


<a id="class-rdshadersource-method-set-stage-source"></a>

void **set_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), source: [String](class_string.md#class-string)) [🔗](class_rdshadersource.md#class-rdshadersource-method-set-stage-source)

Sets `source` code for the specified shader `stage`. Equivalent to setting one of [source_compute](class_rdshadersource.md#class-rdshadersource-property-source-compute), [source_fragment](class_rdshadersource.md#class-rdshadersource-property-source-fragment), [source_tesselation_control](class_rdshadersource.md#class-rdshadersource-property-source-tesselation-control), [source_tesselation_evaluation](class_rdshadersource.md#class-rdshadersource-property-source-tesselation-evaluation) or [source_vertex](class_rdshadersource.md#class-rdshadersource-property-source-vertex).

**Note:** If you set the compute shader source code using this method directly, remember to remove the Godot-specific hint `#[compute]`.
