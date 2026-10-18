> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodederivativefunc.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodederivativefunc"></a>

<a id="class-visualshadernodederivativefunc"></a>

# VisualShaderNodeDerivativeFunc

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Calculates a derivative within the visual shader graph.

<a id="description"></a>

## Description

This node is only available in `Fragment` and `Light` visual shaders.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Function](class_visualshadernodederivativefunc.md#enum-visualshadernodederivativefunc-function) | [function](class_visualshadernodederivativefunc.md#class-visualshadernodederivativefunc-property-function) | `0` |
| [OpType](class_visualshadernodederivativefunc.md#enum-visualshadernodederivativefunc-optype) | [op_type](class_visualshadernodederivativefunc.md#class-visualshadernodederivativefunc-property-op-type) | `0` |
| [Precision](class_visualshadernodederivativefunc.md#enum-visualshadernodederivativefunc-precision) | [precision](class_visualshadernodederivativefunc.md#class-visualshadernodederivativefunc-property-precision) | `0` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-visualshadernodederivativefunc-optype"></a>

enum **OpType**: [🔗](class_visualshadernodederivativefunc.md#enum-visualshadernodederivativefunc-optype)

<a id="class-visualshadernodederivativefunc-constant-op-type-scalar"></a>

[OpType](class_visualshadernodederivativefunc.md#enum-visualshadernodederivativefunc-optype) **OP_TYPE_SCALAR** = `0`

A floating-point scalar.

<a id="class-visualshadernodederivativefunc-constant-op-type-vector-2d"></a>

[OpType](class_visualshadernodederivativefunc.md#enum-visualshadernodederivativefunc-optype) **OP_TYPE_VECTOR_2D** = `1`

A 2D vector type.

<a id="class-visualshadernodederivativefunc-constant-op-type-vector-3d"></a>

[OpType](class_visualshadernodederivativefunc.md#enum-visualshadernodederivativefunc-optype) **OP_TYPE_VECTOR_3D** = `2`

A 3D vector type.

<a id="class-visualshadernodederivativefunc-constant-op-type-vector-4d"></a>

[OpType](class_visualshadernodederivativefunc.md#enum-visualshadernodederivativefunc-optype) **OP_TYPE_VECTOR_4D** = `3`

A 4D vector type.

<a id="class-visualshadernodederivativefunc-constant-op-type-max"></a>

[OpType](class_visualshadernodederivativefunc.md#enum-visualshadernodederivativefunc-optype) **OP_TYPE_MAX** = `4`

Represents the size of the [OpType](class_visualshadernodederivativefunc.md#enum-visualshadernodederivativefunc-optype) enum.

---


<a id="enum-visualshadernodederivativefunc-function"></a>

enum **Function**: [🔗](class_visualshadernodederivativefunc.md#enum-visualshadernodederivativefunc-function)

<a id="class-visualshadernodederivativefunc-constant-func-sum"></a>

[Function](class_visualshadernodederivativefunc.md#enum-visualshadernodederivativefunc-function) **FUNC_SUM** = `0`

Sum of absolute derivative in `x` and `y`.

<a id="class-visualshadernodederivativefunc-constant-func-x"></a>

[Function](class_visualshadernodederivativefunc.md#enum-visualshadernodederivativefunc-function) **FUNC_X** = `1`

Derivative in `x` using local differencing.

<a id="class-visualshadernodederivativefunc-constant-func-y"></a>

[Function](class_visualshadernodederivativefunc.md#enum-visualshadernodederivativefunc-function) **FUNC_Y** = `2`

Derivative in `y` using local differencing.

<a id="class-visualshadernodederivativefunc-constant-func-max"></a>

[Function](class_visualshadernodederivativefunc.md#enum-visualshadernodederivativefunc-function) **FUNC_MAX** = `3`

Represents the size of the [Function](class_visualshadernodederivativefunc.md#enum-visualshadernodederivativefunc-function) enum.

---


<a id="enum-visualshadernodederivativefunc-precision"></a>

enum **Precision**: [🔗](class_visualshadernodederivativefunc.md#enum-visualshadernodederivativefunc-precision)

<a id="class-visualshadernodederivativefunc-constant-precision-none"></a>

[Precision](class_visualshadernodederivativefunc.md#enum-visualshadernodederivativefunc-precision) **PRECISION_NONE** = `0`

No precision is specified, the GPU driver is allowed to use whatever level of precision it chooses. This is the default option and is equivalent to using `dFdx()` or `dFdy()` in text shaders.

<a id="class-visualshadernodederivativefunc-constant-precision-coarse"></a>

[Precision](class_visualshadernodederivativefunc.md#enum-visualshadernodederivativefunc-precision) **PRECISION_COARSE** = `1`

The derivative will be calculated using the current fragment's neighbors (which may not include the current fragment). This tends to be faster than using [PRECISION_FINE](class_visualshadernodederivativefunc.md#class-visualshadernodederivativefunc-constant-precision-fine), but may not be suitable when more precision is needed. This is equivalent to using `dFdxCoarse()` or `dFdyCoarse()` in text shaders.

<a id="class-visualshadernodederivativefunc-constant-precision-fine"></a>

[Precision](class_visualshadernodederivativefunc.md#enum-visualshadernodederivativefunc-precision) **PRECISION_FINE** = `2`

The derivative will be calculated using the current fragment and its immediate neighbors. This tends to be slower than using [PRECISION_COARSE](class_visualshadernodederivativefunc.md#class-visualshadernodederivativefunc-constant-precision-coarse), but may be necessary when more precision is needed. This is equivalent to using `dFdxFine()` or `dFdyFine()` in text shaders.

<a id="class-visualshadernodederivativefunc-constant-precision-max"></a>

[Precision](class_visualshadernodederivativefunc.md#enum-visualshadernodederivativefunc-precision) **PRECISION_MAX** = `3`

Represents the size of the [Precision](class_visualshadernodederivativefunc.md#enum-visualshadernodederivativefunc-precision) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodederivativefunc-property-function"></a>

[Function](class_visualshadernodederivativefunc.md#enum-visualshadernodederivativefunc-function) **function** = `0` [🔗](class_visualshadernodederivativefunc.md#class-visualshadernodederivativefunc-property-function)

- void **set_function**(value: [Function](class_visualshadernodederivativefunc.md#enum-visualshadernodederivativefunc-function))
- [Function](class_visualshadernodederivativefunc.md#enum-visualshadernodederivativefunc-function) **get_function**()

A derivative function type.

---


<a id="class-visualshadernodederivativefunc-property-op-type"></a>

[OpType](class_visualshadernodederivativefunc.md#enum-visualshadernodederivativefunc-optype) **op_type** = `0` [🔗](class_visualshadernodederivativefunc.md#class-visualshadernodederivativefunc-property-op-type)

- void **set_op_type**(value: [OpType](class_visualshadernodederivativefunc.md#enum-visualshadernodederivativefunc-optype))
- [OpType](class_visualshadernodederivativefunc.md#enum-visualshadernodederivativefunc-optype) **get_op_type**()

A type of operands and returned value.

---


<a id="class-visualshadernodederivativefunc-property-precision"></a>

[Precision](class_visualshadernodederivativefunc.md#enum-visualshadernodederivativefunc-precision) **precision** = `0` [🔗](class_visualshadernodederivativefunc.md#class-visualshadernodederivativefunc-property-precision)

- void **set_precision**(value: [Precision](class_visualshadernodederivativefunc.md#enum-visualshadernodederivativefunc-precision))
- [Precision](class_visualshadernodederivativefunc.md#enum-visualshadernodederivativefunc-precision) **get_precision**()

Sets the level of precision to use for the derivative function. When using the Compatibility renderer, this setting has no effect.
