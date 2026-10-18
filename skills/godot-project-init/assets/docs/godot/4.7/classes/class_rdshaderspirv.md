> Source: https://docs.godotengine.org/en/4.7/classes/class_rdshaderspirv.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="rdshaderspirv"></a>

<a id="class-rdshaderspirv"></a>

# RDShaderSPIRV

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

SPIR-V intermediate representation as part of an [RDShaderFile](class_rdshaderfile.md#class-rdshaderfile) (used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice)).

<a id="description"></a>

## Description

**RDShaderSPIRV** represents an [RDShaderFile](class_rdshaderfile.md#class-rdshaderfile)'s [SPIR-V](https://www.khronos.org/spir/) code for various shader stages, as well as possible compilation error messages. SPIR-V is a low-level intermediate shader representation. This intermediate representation is not used directly by GPUs for rendering, but it can be compiled into binary shaders that GPUs can understand. Unlike compiled shaders, SPIR-V is portable across GPU models and driver versions.

This object is used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray) | [bytecode_any_hit](class_rdshaderspirv.md#class-rdshaderspirv-property-bytecode-any-hit) | `PackedByteArray()` |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray) | [bytecode_closest_hit](class_rdshaderspirv.md#class-rdshaderspirv-property-bytecode-closest-hit) | `PackedByteArray()` |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray) | [bytecode_compute](class_rdshaderspirv.md#class-rdshaderspirv-property-bytecode-compute) | `PackedByteArray()` |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray) | [bytecode_fragment](class_rdshaderspirv.md#class-rdshaderspirv-property-bytecode-fragment) | `PackedByteArray()` |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray) | [bytecode_intersection](class_rdshaderspirv.md#class-rdshaderspirv-property-bytecode-intersection) | `PackedByteArray()` |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray) | [bytecode_miss](class_rdshaderspirv.md#class-rdshaderspirv-property-bytecode-miss) | `PackedByteArray()` |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray) | [bytecode_raygen](class_rdshaderspirv.md#class-rdshaderspirv-property-bytecode-raygen) | `PackedByteArray()` |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray) | [bytecode_tesselation_control](class_rdshaderspirv.md#class-rdshaderspirv-property-bytecode-tesselation-control) | `PackedByteArray()` |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray) | [bytecode_tesselation_evaluation](class_rdshaderspirv.md#class-rdshaderspirv-property-bytecode-tesselation-evaluation) | `PackedByteArray()` |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray) | [bytecode_vertex](class_rdshaderspirv.md#class-rdshaderspirv-property-bytecode-vertex) | `PackedByteArray()` |
| [String](class_string.md#class-string) | [compile_error_any_hit](class_rdshaderspirv.md#class-rdshaderspirv-property-compile-error-any-hit) | `""` |
| [String](class_string.md#class-string) | [compile_error_closest_hit](class_rdshaderspirv.md#class-rdshaderspirv-property-compile-error-closest-hit) | `""` |
| [String](class_string.md#class-string) | [compile_error_compute](class_rdshaderspirv.md#class-rdshaderspirv-property-compile-error-compute) | `""` |
| [String](class_string.md#class-string) | [compile_error_fragment](class_rdshaderspirv.md#class-rdshaderspirv-property-compile-error-fragment) | `""` |
| [String](class_string.md#class-string) | [compile_error_intersection](class_rdshaderspirv.md#class-rdshaderspirv-property-compile-error-intersection) | `""` |
| [String](class_string.md#class-string) | [compile_error_miss](class_rdshaderspirv.md#class-rdshaderspirv-property-compile-error-miss) | `""` |
| [String](class_string.md#class-string) | [compile_error_raygen](class_rdshaderspirv.md#class-rdshaderspirv-property-compile-error-raygen) | `""` |
| [String](class_string.md#class-string) | [compile_error_tesselation_control](class_rdshaderspirv.md#class-rdshaderspirv-property-compile-error-tesselation-control) | `""` |
| [String](class_string.md#class-string) | [compile_error_tesselation_evaluation](class_rdshaderspirv.md#class-rdshaderspirv-property-compile-error-tesselation-evaluation) | `""` |
| [String](class_string.md#class-string) | [compile_error_vertex](class_rdshaderspirv.md#class-rdshaderspirv-property-compile-error-vertex) | `""` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray) | [get_stage_bytecode](class_rdshaderspirv.md#class-rdshaderspirv-method-get-stage-bytecode)(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) const |
| [String](class_string.md#class-string) | [get_stage_compile_error](class_rdshaderspirv.md#class-rdshaderspirv-method-get-stage-compile-error)(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) const |
| void | [set_stage_bytecode](class_rdshaderspirv.md#class-rdshaderspirv-method-set-stage-bytecode)(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), bytecode: [PackedByteArray](class_packedbytearray.md#class-packedbytearray)) |
| void | [set_stage_compile_error](class_rdshaderspirv.md#class-rdshaderspirv-method-set-stage-compile-error)(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), compile_error: [String](class_string.md#class-string)) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-rdshaderspirv-property-bytecode-any-hit"></a>

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **bytecode_any_hit** = `PackedByteArray()` [🔗](class_rdshaderspirv.md#class-rdshaderspirv-property-bytecode-any-hit)

- void **set_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), bytecode: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))
- [PackedByteArray](class_packedbytearray.md#class-packedbytearray) **get_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) const

The SPIR-V bytecode for the any hit shader stage.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray](class_packedbytearray.md#class-packedbytearray) for more details.

---


<a id="class-rdshaderspirv-property-bytecode-closest-hit"></a>

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **bytecode_closest_hit** = `PackedByteArray()` [🔗](class_rdshaderspirv.md#class-rdshaderspirv-property-bytecode-closest-hit)

- void **set_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), bytecode: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))
- [PackedByteArray](class_packedbytearray.md#class-packedbytearray) **get_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) const

The SPIR-V bytecode for the closest hit shader stage.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray](class_packedbytearray.md#class-packedbytearray) for more details.

---


<a id="class-rdshaderspirv-property-bytecode-compute"></a>

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **bytecode_compute** = `PackedByteArray()` [🔗](class_rdshaderspirv.md#class-rdshaderspirv-property-bytecode-compute)

- void **set_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), bytecode: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))
- [PackedByteArray](class_packedbytearray.md#class-packedbytearray) **get_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) const

The SPIR-V bytecode for the compute shader stage.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray](class_packedbytearray.md#class-packedbytearray) for more details.

---


<a id="class-rdshaderspirv-property-bytecode-fragment"></a>

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **bytecode_fragment** = `PackedByteArray()` [🔗](class_rdshaderspirv.md#class-rdshaderspirv-property-bytecode-fragment)

- void **set_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), bytecode: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))
- [PackedByteArray](class_packedbytearray.md#class-packedbytearray) **get_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) const

The SPIR-V bytecode for the fragment shader stage.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray](class_packedbytearray.md#class-packedbytearray) for more details.

---


<a id="class-rdshaderspirv-property-bytecode-intersection"></a>

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **bytecode_intersection** = `PackedByteArray()` [🔗](class_rdshaderspirv.md#class-rdshaderspirv-property-bytecode-intersection)

- void **set_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), bytecode: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))
- [PackedByteArray](class_packedbytearray.md#class-packedbytearray) **get_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) const

The SPIR-V bytecode for the intersection shader stage.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray](class_packedbytearray.md#class-packedbytearray) for more details.

---


<a id="class-rdshaderspirv-property-bytecode-miss"></a>

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **bytecode_miss** = `PackedByteArray()` [🔗](class_rdshaderspirv.md#class-rdshaderspirv-property-bytecode-miss)

- void **set_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), bytecode: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))
- [PackedByteArray](class_packedbytearray.md#class-packedbytearray) **get_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) const

The SPIR-V bytecode for the miss shader stage.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray](class_packedbytearray.md#class-packedbytearray) for more details.

---


<a id="class-rdshaderspirv-property-bytecode-raygen"></a>

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **bytecode_raygen** = `PackedByteArray()` [🔗](class_rdshaderspirv.md#class-rdshaderspirv-property-bytecode-raygen)

- void **set_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), bytecode: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))
- [PackedByteArray](class_packedbytearray.md#class-packedbytearray) **get_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) const

The SPIR-V bytecode for the ray generation shader stage.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray](class_packedbytearray.md#class-packedbytearray) for more details.

---


<a id="class-rdshaderspirv-property-bytecode-tesselation-control"></a>

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **bytecode_tesselation_control** = `PackedByteArray()` [🔗](class_rdshaderspirv.md#class-rdshaderspirv-property-bytecode-tesselation-control)

- void **set_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), bytecode: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))
- [PackedByteArray](class_packedbytearray.md#class-packedbytearray) **get_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) const

The SPIR-V bytecode for the tessellation control shader stage.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray](class_packedbytearray.md#class-packedbytearray) for more details.

---


<a id="class-rdshaderspirv-property-bytecode-tesselation-evaluation"></a>

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **bytecode_tesselation_evaluation** = `PackedByteArray()` [🔗](class_rdshaderspirv.md#class-rdshaderspirv-property-bytecode-tesselation-evaluation)

- void **set_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), bytecode: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))
- [PackedByteArray](class_packedbytearray.md#class-packedbytearray) **get_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) const

The SPIR-V bytecode for the tessellation evaluation shader stage.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray](class_packedbytearray.md#class-packedbytearray) for more details.

---


<a id="class-rdshaderspirv-property-bytecode-vertex"></a>

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **bytecode_vertex** = `PackedByteArray()` [🔗](class_rdshaderspirv.md#class-rdshaderspirv-property-bytecode-vertex)

- void **set_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), bytecode: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))
- [PackedByteArray](class_packedbytearray.md#class-packedbytearray) **get_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) const

The SPIR-V bytecode for the vertex shader stage.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray](class_packedbytearray.md#class-packedbytearray) for more details.

---


<a id="class-rdshaderspirv-property-compile-error-any-hit"></a>

[String](class_string.md#class-string) **compile_error_any_hit** = `""` [🔗](class_rdshaderspirv.md#class-rdshaderspirv-property-compile-error-any-hit)

- void **set_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), compile_error: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) const

The compilation error message for the any hit shader stage (set by the SPIR-V compiler and Godot). If empty, shader compilation was successful.

---


<a id="class-rdshaderspirv-property-compile-error-closest-hit"></a>

[String](class_string.md#class-string) **compile_error_closest_hit** = `""` [🔗](class_rdshaderspirv.md#class-rdshaderspirv-property-compile-error-closest-hit)

- void **set_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), compile_error: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) const

The compilation error message for the closest hit shader stage (set by the SPIR-V compiler and Godot). If empty, shader compilation was successful.

---


<a id="class-rdshaderspirv-property-compile-error-compute"></a>

[String](class_string.md#class-string) **compile_error_compute** = `""` [🔗](class_rdshaderspirv.md#class-rdshaderspirv-property-compile-error-compute)

- void **set_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), compile_error: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) const

The compilation error message for the compute shader stage (set by the SPIR-V compiler and Godot). If empty, shader compilation was successful.

---


<a id="class-rdshaderspirv-property-compile-error-fragment"></a>

[String](class_string.md#class-string) **compile_error_fragment** = `""` [🔗](class_rdshaderspirv.md#class-rdshaderspirv-property-compile-error-fragment)

- void **set_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), compile_error: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) const

The compilation error message for the fragment shader stage (set by the SPIR-V compiler and Godot). If empty, shader compilation was successful.

---


<a id="class-rdshaderspirv-property-compile-error-intersection"></a>

[String](class_string.md#class-string) **compile_error_intersection** = `""` [🔗](class_rdshaderspirv.md#class-rdshaderspirv-property-compile-error-intersection)

- void **set_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), compile_error: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) const

The compilation error message for the intersection shader stage (set by the SPIR-V compiler and Godot). If empty, shader compilation was successful.

---


<a id="class-rdshaderspirv-property-compile-error-miss"></a>

[String](class_string.md#class-string) **compile_error_miss** = `""` [🔗](class_rdshaderspirv.md#class-rdshaderspirv-property-compile-error-miss)

- void **set_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), compile_error: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) const

The compilation error message for the miss shader stage (set by the SPIR-V compiler and Godot). If empty, shader compilation was successful.

---


<a id="class-rdshaderspirv-property-compile-error-raygen"></a>

[String](class_string.md#class-string) **compile_error_raygen** = `""` [🔗](class_rdshaderspirv.md#class-rdshaderspirv-property-compile-error-raygen)

- void **set_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), compile_error: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) const

The compilation error message for the ray generation shader stage (set by the SPIR-V compiler and Godot). If empty, shader compilation was successful.

---


<a id="class-rdshaderspirv-property-compile-error-tesselation-control"></a>

[String](class_string.md#class-string) **compile_error_tesselation_control** = `""` [🔗](class_rdshaderspirv.md#class-rdshaderspirv-property-compile-error-tesselation-control)

- void **set_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), compile_error: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) const

The compilation error message for the tessellation control shader stage (set by the SPIR-V compiler and Godot). If empty, shader compilation was successful.

---


<a id="class-rdshaderspirv-property-compile-error-tesselation-evaluation"></a>

[String](class_string.md#class-string) **compile_error_tesselation_evaluation** = `""` [🔗](class_rdshaderspirv.md#class-rdshaderspirv-property-compile-error-tesselation-evaluation)

- void **set_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), compile_error: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) const

The compilation error message for the tessellation evaluation shader stage (set by the SPIR-V compiler and Godot). If empty, shader compilation was successful.

---


<a id="class-rdshaderspirv-property-compile-error-vertex"></a>

[String](class_string.md#class-string) **compile_error_vertex** = `""` [🔗](class_rdshaderspirv.md#class-rdshaderspirv-property-compile-error-vertex)

- void **set_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), compile_error: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) const

The compilation error message for the vertex shader stage (set by the SPIR-V compiler and Godot). If empty, shader compilation was successful.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-rdshaderspirv-method-get-stage-bytecode"></a>

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **get_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) const [🔗](class_rdshaderspirv.md#class-rdshaderspirv-method-get-stage-bytecode)

Equivalent to getting one of [bytecode_compute](class_rdshaderspirv.md#class-rdshaderspirv-property-bytecode-compute), [bytecode_fragment](class_rdshaderspirv.md#class-rdshaderspirv-property-bytecode-fragment), [bytecode_tesselation_control](class_rdshaderspirv.md#class-rdshaderspirv-property-bytecode-tesselation-control), [bytecode_tesselation_evaluation](class_rdshaderspirv.md#class-rdshaderspirv-property-bytecode-tesselation-evaluation), [bytecode_vertex](class_rdshaderspirv.md#class-rdshaderspirv-property-bytecode-vertex).

---


<a id="class-rdshaderspirv-method-get-stage-compile-error"></a>

[String](class_string.md#class-string) **get_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) const [🔗](class_rdshaderspirv.md#class-rdshaderspirv-method-get-stage-compile-error)

Returns the compilation error message for the given shader `stage`. Equivalent to getting one of [compile_error_compute](class_rdshaderspirv.md#class-rdshaderspirv-property-compile-error-compute), [compile_error_fragment](class_rdshaderspirv.md#class-rdshaderspirv-property-compile-error-fragment), [compile_error_tesselation_control](class_rdshaderspirv.md#class-rdshaderspirv-property-compile-error-tesselation-control), [compile_error_tesselation_evaluation](class_rdshaderspirv.md#class-rdshaderspirv-property-compile-error-tesselation-evaluation), [compile_error_vertex](class_rdshaderspirv.md#class-rdshaderspirv-property-compile-error-vertex).

---


<a id="class-rdshaderspirv-method-set-stage-bytecode"></a>

void **set_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), bytecode: [PackedByteArray](class_packedbytearray.md#class-packedbytearray)) [🔗](class_rdshaderspirv.md#class-rdshaderspirv-method-set-stage-bytecode)

Sets the SPIR-V `bytecode` for the given shader `stage`. Equivalent to setting one of [bytecode_compute](class_rdshaderspirv.md#class-rdshaderspirv-property-bytecode-compute), [bytecode_fragment](class_rdshaderspirv.md#class-rdshaderspirv-property-bytecode-fragment), [bytecode_tesselation_control](class_rdshaderspirv.md#class-rdshaderspirv-property-bytecode-tesselation-control), [bytecode_tesselation_evaluation](class_rdshaderspirv.md#class-rdshaderspirv-property-bytecode-tesselation-evaluation), [bytecode_vertex](class_rdshaderspirv.md#class-rdshaderspirv-property-bytecode-vertex).

---


<a id="class-rdshaderspirv-method-set-stage-compile-error"></a>

void **set_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), compile_error: [String](class_string.md#class-string)) [🔗](class_rdshaderspirv.md#class-rdshaderspirv-method-set-stage-compile-error)

Sets the compilation error message for the given shader `stage` to `compile_error`. Equivalent to setting one of [compile_error_compute](class_rdshaderspirv.md#class-rdshaderspirv-property-compile-error-compute), [compile_error_fragment](class_rdshaderspirv.md#class-rdshaderspirv-property-compile-error-fragment), [compile_error_tesselation_control](class_rdshaderspirv.md#class-rdshaderspirv-property-compile-error-tesselation-control), [compile_error_tesselation_evaluation](class_rdshaderspirv.md#class-rdshaderspirv-property-compile-error-tesselation-evaluation), [compile_error_vertex](class_rdshaderspirv.md#class-rdshaderspirv-property-compile-error-vertex).
