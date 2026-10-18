> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodetransformfunc.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodetransformfunc"></a>

<a id="class-visualshadernodetransformfunc"></a>

# VisualShaderNodeTransformFunc

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Computes a [Transform3D](class_transform3d.md#class-transform3d) function within the visual shader graph.

<a id="description"></a>

## Description

Computes an inverse or transpose function on the provided [Transform3D](class_transform3d.md#class-transform3d).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Function](class_visualshadernodetransformfunc.md#enum-visualshadernodetransformfunc-function) | [function](class_visualshadernodetransformfunc.md#class-visualshadernodetransformfunc-property-function) | `0` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-visualshadernodetransformfunc-function"></a>

enum **Function**: [🔗](class_visualshadernodetransformfunc.md#enum-visualshadernodetransformfunc-function)

<a id="class-visualshadernodetransformfunc-constant-func-inverse"></a>

[Function](class_visualshadernodetransformfunc.md#enum-visualshadernodetransformfunc-function) **FUNC_INVERSE** = `0`

Perform the inverse operation on the [Transform3D](class_transform3d.md#class-transform3d) matrix.

<a id="class-visualshadernodetransformfunc-constant-func-transpose"></a>

[Function](class_visualshadernodetransformfunc.md#enum-visualshadernodetransformfunc-function) **FUNC_TRANSPOSE** = `1`

Perform the transpose operation on the [Transform3D](class_transform3d.md#class-transform3d) matrix.

<a id="class-visualshadernodetransformfunc-constant-func-max"></a>

[Function](class_visualshadernodetransformfunc.md#enum-visualshadernodetransformfunc-function) **FUNC_MAX** = `2`

Represents the size of the [Function](class_visualshadernodetransformfunc.md#enum-visualshadernodetransformfunc-function) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodetransformfunc-property-function"></a>

[Function](class_visualshadernodetransformfunc.md#enum-visualshadernodetransformfunc-function) **function** = `0` [🔗](class_visualshadernodetransformfunc.md#class-visualshadernodetransformfunc-property-function)

- void **set_function**(value: [Function](class_visualshadernodetransformfunc.md#enum-visualshadernodetransformfunc-function))
- [Function](class_visualshadernodetransformfunc.md#enum-visualshadernodetransformfunc-function) **get_function**()

The function to be computed.
