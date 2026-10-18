> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodeintfunc.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodeintfunc"></a>

<a id="class-visualshadernodeintfunc"></a>

# VisualShaderNodeIntFunc

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A scalar integer function to be used within the visual shader graph.

<a id="description"></a>

## Description

Accept an integer scalar (`x`) to the input port and transform it according to [function](class_visualshadernodeintfunc.md#class-visualshadernodeintfunc-property-function).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Function](class_visualshadernodeintfunc.md#enum-visualshadernodeintfunc-function) | [function](class_visualshadernodeintfunc.md#class-visualshadernodeintfunc-property-function) | `2` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-visualshadernodeintfunc-function"></a>

enum **Function**: [🔗](class_visualshadernodeintfunc.md#enum-visualshadernodeintfunc-function)

<a id="class-visualshadernodeintfunc-constant-func-abs"></a>

[Function](class_visualshadernodeintfunc.md#enum-visualshadernodeintfunc-function) **FUNC_ABS** = `0`

Returns the absolute value of the parameter. Translates to `abs(x)` in the Godot Shader Language.

<a id="class-visualshadernodeintfunc-constant-func-negate"></a>

[Function](class_visualshadernodeintfunc.md#enum-visualshadernodeintfunc-function) **FUNC_NEGATE** = `1`

Negates the `x` using `-(x)`.

<a id="class-visualshadernodeintfunc-constant-func-sign"></a>

[Function](class_visualshadernodeintfunc.md#enum-visualshadernodeintfunc-function) **FUNC_SIGN** = `2`

Extracts the sign of the parameter. Translates to `sign(x)` in the Godot Shader Language.

<a id="class-visualshadernodeintfunc-constant-func-bitwise-not"></a>

[Function](class_visualshadernodeintfunc.md#enum-visualshadernodeintfunc-function) **FUNC_BITWISE_NOT** = `3`

Returns the result of bitwise `NOT` operation on the integer. Translates to `~a` in the Godot Shader Language.

<a id="class-visualshadernodeintfunc-constant-func-max"></a>

[Function](class_visualshadernodeintfunc.md#enum-visualshadernodeintfunc-function) **FUNC_MAX** = `4`

Represents the size of the [Function](class_visualshadernodeintfunc.md#enum-visualshadernodeintfunc-function) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodeintfunc-property-function"></a>

[Function](class_visualshadernodeintfunc.md#enum-visualshadernodeintfunc-function) **function** = `2` [🔗](class_visualshadernodeintfunc.md#class-visualshadernodeintfunc-property-function)

- void **set_function**(value: [Function](class_visualshadernodeintfunc.md#enum-visualshadernodeintfunc-function))
- [Function](class_visualshadernodeintfunc.md#enum-visualshadernodeintfunc-function) **get_function**()

A function to be applied to the scalar.
