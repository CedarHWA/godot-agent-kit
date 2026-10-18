> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodeis.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodeis"></a>

<a id="class-visualshadernodeis"></a>

# VisualShaderNodeIs

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A boolean comparison operator to be used within the visual shader graph.

<a id="description"></a>

## Description

Returns the boolean result of the comparison between `INF` or `NaN` and a scalar parameter.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Function](class_visualshadernodeis.md#enum-visualshadernodeis-function) | [function](class_visualshadernodeis.md#class-visualshadernodeis-property-function) | `0` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-visualshadernodeis-function"></a>

enum **Function**: [🔗](class_visualshadernodeis.md#enum-visualshadernodeis-function)

<a id="class-visualshadernodeis-constant-func-is-inf"></a>

[Function](class_visualshadernodeis.md#enum-visualshadernodeis-function) **FUNC_IS_INF** = `0`

Comparison with `INF` (Infinity).

<a id="class-visualshadernodeis-constant-func-is-nan"></a>

[Function](class_visualshadernodeis.md#enum-visualshadernodeis-function) **FUNC_IS_NAN** = `1`

Comparison with `NaN` (Not a Number; indicates invalid numeric results, such as division by zero).

<a id="class-visualshadernodeis-constant-func-max"></a>

[Function](class_visualshadernodeis.md#enum-visualshadernodeis-function) **FUNC_MAX** = `2`

Represents the size of the [Function](class_visualshadernodeis.md#enum-visualshadernodeis-function) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodeis-property-function"></a>

[Function](class_visualshadernodeis.md#enum-visualshadernodeis-function) **function** = `0` [🔗](class_visualshadernodeis.md#class-visualshadernodeis-property-function)

- void **set_function**(value: [Function](class_visualshadernodeis.md#enum-visualshadernodeis-function))
- [Function](class_visualshadernodeis.md#enum-visualshadernodeis-function) **get_function**()

The comparison function.
