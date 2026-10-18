> Source: https://docs.godotengine.org/en/4.7/classes/class_rdshaderfile.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="rdshaderfile"></a>

<a id="class-rdshaderfile"></a>

# RDShaderFile

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Compiled shader file in SPIR-V form (used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice)). Not to be confused with Godot's own [Shader](class_shader.md#class-shader).

<a id="description"></a>

## Description

Compiled shader file in SPIR-V form.

See also [RDShaderSource](class_rdshadersource.md#class-rdshadersource). **RDShaderFile** is only meant to be used with the [RenderingDevice](class_renderingdevice.md#class-renderingdevice) API. It should not be confused with Godot's own [Shader](class_shader.md#class-shader) resource, which is what Godot's various nodes use for high-level shader programming.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [String](class_string.md#class-string) | [base_error](class_rdshaderfile.md#class-rdshaderfile-property-base-error) | `""` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [RDShaderSPIRV](class_rdshaderspirv.md#class-rdshaderspirv) | [get_spirv](class_rdshaderfile.md#class-rdshaderfile-method-get-spirv)(version: [StringName](class_stringname.md#class-stringname) = &"") const |
| [Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] | [get_version_list](class_rdshaderfile.md#class-rdshaderfile-method-get-version-list)() const |
| void | [set_bytecode](class_rdshaderfile.md#class-rdshaderfile-method-set-bytecode)(bytecode: [RDShaderSPIRV](class_rdshaderspirv.md#class-rdshaderspirv), version: [StringName](class_stringname.md#class-stringname) = &"") |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-rdshaderfile-property-base-error"></a>

[String](class_string.md#class-string) **base_error** = `""` [🔗](class_rdshaderfile.md#class-rdshaderfile-property-base-error)

- void **set_base_error**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_base_error**()

The base compilation error message, which indicates errors not related to a specific shader stage if non-empty. If empty, shader compilation is not necessarily successful (check [RDShaderSPIRV](class_rdshaderspirv.md#class-rdshaderspirv)'s error message members).

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-rdshaderfile-method-get-spirv"></a>

[RDShaderSPIRV](class_rdshaderspirv.md#class-rdshaderspirv) **get_spirv**(version: [StringName](class_stringname.md#class-stringname) = &"") const [🔗](class_rdshaderfile.md#class-rdshaderfile-method-get-spirv)

Returns the SPIR-V intermediate representation for the specified shader `version`.

---


<a id="class-rdshaderfile-method-get-version-list"></a>

[Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] **get_version_list**() const [🔗](class_rdshaderfile.md#class-rdshaderfile-method-get-version-list)

Returns the list of compiled versions for this shader.

---


<a id="class-rdshaderfile-method-set-bytecode"></a>

void **set_bytecode**(bytecode: [RDShaderSPIRV](class_rdshaderspirv.md#class-rdshaderspirv), version: [StringName](class_stringname.md#class-stringname) = &"") [🔗](class_rdshaderfile.md#class-rdshaderfile-method-set-bytecode)

Sets the SPIR-V `bytecode` that will be compiled for the specified `version`.
