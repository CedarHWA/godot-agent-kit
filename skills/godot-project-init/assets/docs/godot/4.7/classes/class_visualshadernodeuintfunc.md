> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodeuintfunc.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodeuintfunc"></a>

<a id="class-visualshadernodeuintfunc"></a>

# VisualShaderNodeUIntFunc

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

An unsigned scalar integer function to be used within the visual shader graph.

<a id="description"></a>

## Description

Accept an unsigned integer scalar (`x`) to the input port and transform it according to [function](class_visualshadernodeuintfunc.md#class-visualshadernodeuintfunc-property-function).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Function](class_visualshadernodeuintfunc.md#enum-visualshadernodeuintfunc-function) | [function](class_visualshadernodeuintfunc.md#class-visualshadernodeuintfunc-property-function) | `0` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-visualshadernodeuintfunc-function"></a>

enum **Function**: [🔗](class_visualshadernodeuintfunc.md#enum-visualshadernodeuintfunc-function)

<a id="class-visualshadernodeuintfunc-constant-func-negate"></a>

[Function](class_visualshadernodeuintfunc.md#enum-visualshadernodeuintfunc-function) **FUNC_NEGATE** = `0`

Negates the `x` using `-(x)`.

<a id="class-visualshadernodeuintfunc-constant-func-bitwise-not"></a>

[Function](class_visualshadernodeuintfunc.md#enum-visualshadernodeuintfunc-function) **FUNC_BITWISE_NOT** = `1`

Returns the result of bitwise `NOT` operation on the integer. Translates to `~a` in the Godot Shader Language.

<a id="class-visualshadernodeuintfunc-constant-func-max"></a>

[Function](class_visualshadernodeuintfunc.md#enum-visualshadernodeuintfunc-function) **FUNC_MAX** = `2`

Represents the size of the [Function](class_visualshadernodeuintfunc.md#enum-visualshadernodeuintfunc-function) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodeuintfunc-property-function"></a>

[Function](class_visualshadernodeuintfunc.md#enum-visualshadernodeuintfunc-function) **function** = `0` [🔗](class_visualshadernodeuintfunc.md#class-visualshadernodeuintfunc-property-function)

- void **set_function**(value: [Function](class_visualshadernodeuintfunc.md#enum-visualshadernodeuintfunc-function))
- [Function](class_visualshadernodeuintfunc.md#enum-visualshadernodeuintfunc-function) **get_function**()

A function to be applied to the scalar.
