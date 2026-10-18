> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodeuvfunc.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodeuvfunc"></a>

<a id="class-visualshadernodeuvfunc"></a>

# VisualShaderNodeUVFunc

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Contains functions to modify texture coordinates (`uv`) to be used within the visual shader graph.

<a id="description"></a>

## Description

UV functions are similar to [Vector2](class_vector2.md#class-vector2) functions, but the input port of this node uses the shader's UV value by default.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Function](class_visualshadernodeuvfunc.md#enum-visualshadernodeuvfunc-function) | [function](class_visualshadernodeuvfunc.md#class-visualshadernodeuvfunc-property-function) | `0` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-visualshadernodeuvfunc-function"></a>

enum **Function**: [🔗](class_visualshadernodeuvfunc.md#enum-visualshadernodeuvfunc-function)

<a id="class-visualshadernodeuvfunc-constant-func-panning"></a>

[Function](class_visualshadernodeuvfunc.md#enum-visualshadernodeuvfunc-function) **FUNC_PANNING** = `0`

Translates `uv` by using `scale` and `offset` values using the following formula: `uv = uv + offset * scale`. `uv` port is connected to `UV` built-in by default.

<a id="class-visualshadernodeuvfunc-constant-func-scaling"></a>

[Function](class_visualshadernodeuvfunc.md#enum-visualshadernodeuvfunc-function) **FUNC_SCALING** = `1`

Scales `uv` by using `scale` and `pivot` values using the following formula: `uv = (uv - pivot) * scale + pivot`. `uv` port is connected to `UV` built-in by default.

<a id="class-visualshadernodeuvfunc-constant-func-max"></a>

[Function](class_visualshadernodeuvfunc.md#enum-visualshadernodeuvfunc-function) **FUNC_MAX** = `2`

Represents the size of the [Function](class_visualshadernodeuvfunc.md#enum-visualshadernodeuvfunc-function) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodeuvfunc-property-function"></a>

[Function](class_visualshadernodeuvfunc.md#enum-visualshadernodeuvfunc-function) **function** = `0` [🔗](class_visualshadernodeuvfunc.md#class-visualshadernodeuvfunc-property-function)

- void **set_function**(value: [Function](class_visualshadernodeuvfunc.md#enum-visualshadernodeuvfunc-function))
- [Function](class_visualshadernodeuvfunc.md#enum-visualshadernodeuvfunc-function) **get_function**()

A function to be applied to the texture coordinates.
