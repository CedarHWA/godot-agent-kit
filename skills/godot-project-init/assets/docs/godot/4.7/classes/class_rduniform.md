> Source: https://docs.godotengine.org/en/4.7/classes/class_rduniform.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="rduniform"></a>

<a id="class-rduniform"></a>

# RDUniform

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Shader uniform (used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice)).

<a id="description"></a>

## Description

This object is used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [binding](class_rduniform.md#class-rduniform-property-binding) | `0` |
| [UniformType](class_renderingdevice.md#enum-renderingdevice-uniformtype) | [uniform_type](class_rduniform.md#class-rduniform-property-uniform-type) | `3` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_id](class_rduniform.md#class-rduniform-method-add-id)(id: [RID](class_rid.md#class-rid)) |
| void | [clear_ids](class_rduniform.md#class-rduniform-method-clear-ids)() |
| [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] | [get_ids](class_rduniform.md#class-rduniform-method-get-ids)() const |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-rduniform-property-binding"></a>

[int](class_int.md#class-int) **binding** = `0` [🔗](class_rduniform.md#class-rduniform-property-binding)

- void **set_binding**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_binding**()

The uniform's binding.

---


<a id="class-rduniform-property-uniform-type"></a>

[UniformType](class_renderingdevice.md#enum-renderingdevice-uniformtype) **uniform_type** = `3` [🔗](class_rduniform.md#class-rduniform-property-uniform-type)

- void **set_uniform_type**(value: [UniformType](class_renderingdevice.md#enum-renderingdevice-uniformtype))
- [UniformType](class_renderingdevice.md#enum-renderingdevice-uniformtype) **get_uniform_type**()

The uniform's data type.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-rduniform-method-add-id"></a>

void **add_id**(id: [RID](class_rid.md#class-rid)) [🔗](class_rduniform.md#class-rduniform-method-add-id)

Binds the given id to the uniform. The data associated with the id is then used when the uniform is passed to a shader.

---


<a id="class-rduniform-method-clear-ids"></a>

void **clear_ids**() [🔗](class_rduniform.md#class-rduniform-method-clear-ids)

Unbinds all ids currently bound to the uniform.

---


<a id="class-rduniform-method-get-ids"></a>

[Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] **get_ids**() const [🔗](class_rduniform.md#class-rduniform-method-get-ids)

Returns an array of all ids currently bound to the uniform.
