> Source: https://docs.godotengine.org/en/4.7/classes/class_rdpipelinespecializationconstant.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="rdpipelinespecializationconstant"></a>

<a id="class-rdpipelinespecializationconstant"></a>

# RDPipelineSpecializationConstant

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Pipeline specialization constant (used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice)).

<a id="description"></a>

## Description

A *specialization constant* is a way to create additional variants of shaders without actually increasing the number of shader versions that are compiled. This allows improving performance by reducing the number of shader versions and reducing `if` branching, while still allowing shaders to be flexible for different use cases.

This object is used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [constant_id](class_rdpipelinespecializationconstant.md#class-rdpipelinespecializationconstant-property-constant-id) | `0` |
| [Variant](class_variant.md#class-variant) | [value](class_rdpipelinespecializationconstant.md#class-rdpipelinespecializationconstant-property-value) |  |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-rdpipelinespecializationconstant-property-constant-id"></a>

[int](class_int.md#class-int) **constant_id** = `0` [🔗](class_rdpipelinespecializationconstant.md#class-rdpipelinespecializationconstant-property-constant-id)

- void **set_constant_id**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_constant_id**()

The identifier of the specialization constant. This is a value starting from `0` and that increments for every different specialization constant for a given shader.

---


<a id="class-rdpipelinespecializationconstant-property-value"></a>

[Variant](class_variant.md#class-variant) **value** [🔗](class_rdpipelinespecializationconstant.md#class-rdpipelinespecializationconstant-property-value)

- void **set_value**(value: [Variant](class_variant.md#class-variant))
- [Variant](class_variant.md#class-variant) **get_value**()

The specialization constant's value. Only [bool](class_bool.md#class-bool), [int](class_int.md#class-int) and [float](class_float.md#class-float) types are valid for specialization constants.
