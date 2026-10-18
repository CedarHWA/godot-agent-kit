> Source: https://docs.godotengine.org/en/4.7/classes/class_shadermaterial.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="shadermaterial"></a>

<a id="class-shadermaterial"></a>

# ShaderMaterial

**Inherits:** [Material](class_material.md#class-material) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A material defined by a custom [Shader](class_shader.md#class-shader) program and the values of its shader parameters.

<a id="description"></a>

## Description

A material that uses a custom [Shader](class_shader.md#class-shader) program to render visual items (canvas items, meshes, skies, fog), or to process particles. Compared to other materials, **ShaderMaterial** gives deeper control over the generated shader code. For more information, see the shaders documentation index below.

Multiple **ShaderMaterial**s can use the same shader and configure different values for the shader uniforms.

**Note:** For performance reasons, the [Resource.changed](class_resource.md#class-resource-signal-changed) signal is only emitted when the [Resource.resource_name](class_resource.md#class-resource-property-resource-name) changes. Only in editor, it is also emitted for [shader](class_shadermaterial.md#class-shadermaterial-property-shader) changes.

<a id="tutorials"></a>

## Tutorials

- [Shaders documentation index](../tutorials/shaders/index.md)

<a id="properties"></a>

## Properties

|  |  |
| --- | --- |
| [Shader](class_shader.md#class-shader) | [shader](class_shadermaterial.md#class-shadermaterial-property-shader) |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Variant](class_variant.md#class-variant) | [get_shader_parameter](class_shadermaterial.md#class-shadermaterial-method-get-shader-parameter)(param: [StringName](class_stringname.md#class-stringname)) const |
| void | [set_shader_parameter](class_shadermaterial.md#class-shadermaterial-method-set-shader-parameter)(param: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant)) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-shadermaterial-property-shader"></a>

[Shader](class_shader.md#class-shader) **shader** [🔗](class_shadermaterial.md#class-shadermaterial-property-shader)

- void **set_shader**(value: [Shader](class_shader.md#class-shader))
- [Shader](class_shader.md#class-shader) **get_shader**()

The [Shader](class_shader.md#class-shader) program used to render this material.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-shadermaterial-method-get-shader-parameter"></a>

[Variant](class_variant.md#class-variant) **get_shader_parameter**(param: [StringName](class_stringname.md#class-stringname)) const [🔗](class_shadermaterial.md#class-shadermaterial-method-get-shader-parameter)

Returns the current value set for this material of a uniform in the shader.

---


<a id="class-shadermaterial-method-set-shader-parameter"></a>

void **set_shader_parameter**(param: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant)) [🔗](class_shadermaterial.md#class-shadermaterial-method-set-shader-parameter)

Changes the value set for this material of a uniform in the shader.

**Note:** `param` is case-sensitive and must match the name of the uniform in the code exactly (not the capitalized name in the inspector).

**Note:** Changes to the shader uniform will be effective on all instances using this **ShaderMaterial**. To prevent this, use per-instance uniforms with [CanvasItem.set_instance_shader_parameter()](class_canvasitem.md#class-canvasitem-method-set-instance-shader-parameter), [GeometryInstance3D.set_instance_shader_parameter()](class_geometryinstance3d.md#class-geometryinstance3d-method-set-instance-shader-parameter) or duplicate the **ShaderMaterial** resource using [Resource.duplicate()](class_resource.md#class-resource-method-duplicate). Per-instance uniforms allow for better shader reuse and are therefore faster, so they should be preferred over duplicating the **ShaderMaterial** when possible.
