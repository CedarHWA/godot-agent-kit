> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodeinput.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodeinput"></a>

<a id="class-visualshadernodeinput"></a>

# VisualShaderNodeInput

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Represents the input shader parameter within the visual shader graph.

<a id="description"></a>

## Description

Gives access to input variables (built-ins) available for the shader. See the shading reference for the list of available built-ins for each shader type (check `Tutorials` section for link).

<a id="tutorials"></a>

## Tutorials

- [Shading reference index](../tutorials/shaders/shader_reference/index.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [String](class_string.md#class-string) | [input_name](class_visualshadernodeinput.md#class-visualshadernodeinput-property-input-name) | `"[None]"` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [String](class_string.md#class-string) | [get_input_real_name](class_visualshadernodeinput.md#class-visualshadernodeinput-method-get-input-real-name)() const |

---


<a id="signals"></a>

## Signals

<a id="class-visualshadernodeinput-signal-input-type-changed"></a>

**input_type_changed**() [🔗](class_visualshadernodeinput.md#class-visualshadernodeinput-signal-input-type-changed)

Emitted when input is changed via [input_name](class_visualshadernodeinput.md#class-visualshadernodeinput-property-input-name).

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodeinput-property-input-name"></a>

[String](class_string.md#class-string) **input_name** = `"[None]"` [🔗](class_visualshadernodeinput.md#class-visualshadernodeinput-property-input-name)

- void **set_input_name**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_input_name**()

One of the several input constants in lower-case style like: "vertex" (`VERTEX`) or "point_size" (`POINT_SIZE`).

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-visualshadernodeinput-method-get-input-real-name"></a>

[String](class_string.md#class-string) **get_input_real_name**() const [🔗](class_visualshadernodeinput.md#class-visualshadernodeinput-method-get-input-real-name)

Returns a translated name of the current constant in the Godot Shader Language. E.g. `"ALBEDO"` if the [input_name](class_visualshadernodeinput.md#class-visualshadernodeinput-property-input-name) equal to `"albedo"`.
