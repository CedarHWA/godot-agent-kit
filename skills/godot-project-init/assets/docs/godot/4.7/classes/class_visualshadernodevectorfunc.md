> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodevectorfunc.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodevectorfunc"></a>

<a id="class-visualshadernodevectorfunc"></a>

# VisualShaderNodeVectorFunc

**Inherits:** [VisualShaderNodeVectorBase](class_visualshadernodevectorbase.md#class-visualshadernodevectorbase) **<** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A vector function to be used within the visual shader graph.

<a id="description"></a>

## Description

A visual shader node able to perform different functions using vectors.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Function](class_visualshadernodevectorfunc.md#enum-visualshadernodevectorfunc-function) | [function](class_visualshadernodevectorfunc.md#class-visualshadernodevectorfunc-property-function) | `0` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-visualshadernodevectorfunc-function"></a>

enum **Function**: [🔗](class_visualshadernodevectorfunc.md#enum-visualshadernodevectorfunc-function)

<a id="class-visualshadernodevectorfunc-constant-func-normalize"></a>

[Function](class_visualshadernodevectorfunc.md#enum-visualshadernodevectorfunc-function) **FUNC_NORMALIZE** = `0`

Normalizes the vector so that it has a length of `1` but points in the same direction.

<a id="class-visualshadernodevectorfunc-constant-func-saturate"></a>

[Function](class_visualshadernodevectorfunc.md#enum-visualshadernodevectorfunc-function) **FUNC_SATURATE** = `1`

Clamps the value between `0.0` and `1.0`.

<a id="class-visualshadernodevectorfunc-constant-func-negate"></a>

[Function](class_visualshadernodevectorfunc.md#enum-visualshadernodevectorfunc-function) **FUNC_NEGATE** = `2`

Returns the opposite value of the parameter.

<a id="class-visualshadernodevectorfunc-constant-func-reciprocal"></a>

[Function](class_visualshadernodevectorfunc.md#enum-visualshadernodevectorfunc-function) **FUNC_RECIPROCAL** = `3`

Returns `1/vector`.

<a id="class-visualshadernodevectorfunc-constant-func-abs"></a>

[Function](class_visualshadernodevectorfunc.md#enum-visualshadernodevectorfunc-function) **FUNC_ABS** = `4`

Returns the absolute value of the parameter.

<a id="class-visualshadernodevectorfunc-constant-func-acos"></a>

[Function](class_visualshadernodevectorfunc.md#enum-visualshadernodevectorfunc-function) **FUNC_ACOS** = `5`

Returns the arc-cosine of the parameter.

<a id="class-visualshadernodevectorfunc-constant-func-acosh"></a>

[Function](class_visualshadernodevectorfunc.md#enum-visualshadernodevectorfunc-function) **FUNC_ACOSH** = `6`

Returns the inverse hyperbolic cosine of the parameter.

<a id="class-visualshadernodevectorfunc-constant-func-asin"></a>

[Function](class_visualshadernodevectorfunc.md#enum-visualshadernodevectorfunc-function) **FUNC_ASIN** = `7`

Returns the arc-sine of the parameter.

<a id="class-visualshadernodevectorfunc-constant-func-asinh"></a>

[Function](class_visualshadernodevectorfunc.md#enum-visualshadernodevectorfunc-function) **FUNC_ASINH** = `8`

Returns the inverse hyperbolic sine of the parameter.

<a id="class-visualshadernodevectorfunc-constant-func-atan"></a>

[Function](class_visualshadernodevectorfunc.md#enum-visualshadernodevectorfunc-function) **FUNC_ATAN** = `9`

Returns the arc-tangent of the parameter.

<a id="class-visualshadernodevectorfunc-constant-func-atanh"></a>

[Function](class_visualshadernodevectorfunc.md#enum-visualshadernodevectorfunc-function) **FUNC_ATANH** = `10`

Returns the inverse hyperbolic tangent of the parameter.

<a id="class-visualshadernodevectorfunc-constant-func-ceil"></a>

[Function](class_visualshadernodevectorfunc.md#enum-visualshadernodevectorfunc-function) **FUNC_CEIL** = `11`

Finds the nearest integer that is greater than or equal to the parameter.

<a id="class-visualshadernodevectorfunc-constant-func-cos"></a>

[Function](class_visualshadernodevectorfunc.md#enum-visualshadernodevectorfunc-function) **FUNC_COS** = `12`

Returns the cosine of the parameter.

<a id="class-visualshadernodevectorfunc-constant-func-cosh"></a>

[Function](class_visualshadernodevectorfunc.md#enum-visualshadernodevectorfunc-function) **FUNC_COSH** = `13`

Returns the hyperbolic cosine of the parameter.

<a id="class-visualshadernodevectorfunc-constant-func-degrees"></a>

[Function](class_visualshadernodevectorfunc.md#enum-visualshadernodevectorfunc-function) **FUNC_DEGREES** = `14`

Converts a quantity in radians to degrees.

<a id="class-visualshadernodevectorfunc-constant-func-exp"></a>

[Function](class_visualshadernodevectorfunc.md#enum-visualshadernodevectorfunc-function) **FUNC_EXP** = `15`

Base-e Exponential.

<a id="class-visualshadernodevectorfunc-constant-func-exp2"></a>

[Function](class_visualshadernodevectorfunc.md#enum-visualshadernodevectorfunc-function) **FUNC_EXP2** = `16`

Base-2 Exponential.

<a id="class-visualshadernodevectorfunc-constant-func-floor"></a>

[Function](class_visualshadernodevectorfunc.md#enum-visualshadernodevectorfunc-function) **FUNC_FLOOR** = `17`

Finds the nearest integer less than or equal to the parameter.

<a id="class-visualshadernodevectorfunc-constant-func-fract"></a>

[Function](class_visualshadernodevectorfunc.md#enum-visualshadernodevectorfunc-function) **FUNC_FRACT** = `18`

Computes the fractional part of the argument.

<a id="class-visualshadernodevectorfunc-constant-func-inverse-sqrt"></a>

[Function](class_visualshadernodevectorfunc.md#enum-visualshadernodevectorfunc-function) **FUNC_INVERSE_SQRT** = `19`

Returns the inverse of the square root of the parameter.

<a id="class-visualshadernodevectorfunc-constant-func-log"></a>

[Function](class_visualshadernodevectorfunc.md#enum-visualshadernodevectorfunc-function) **FUNC_LOG** = `20`

Natural logarithm.

<a id="class-visualshadernodevectorfunc-constant-func-log2"></a>

[Function](class_visualshadernodevectorfunc.md#enum-visualshadernodevectorfunc-function) **FUNC_LOG2** = `21`

Base-2 logarithm.

<a id="class-visualshadernodevectorfunc-constant-func-radians"></a>

[Function](class_visualshadernodevectorfunc.md#enum-visualshadernodevectorfunc-function) **FUNC_RADIANS** = `22`

Converts a quantity in degrees to radians.

<a id="class-visualshadernodevectorfunc-constant-func-round"></a>

[Function](class_visualshadernodevectorfunc.md#enum-visualshadernodevectorfunc-function) **FUNC_ROUND** = `23`

Finds the nearest integer to the parameter.

<a id="class-visualshadernodevectorfunc-constant-func-roundeven"></a>

[Function](class_visualshadernodevectorfunc.md#enum-visualshadernodevectorfunc-function) **FUNC_ROUNDEVEN** = `24`

Finds the nearest even integer to the parameter.

<a id="class-visualshadernodevectorfunc-constant-func-sign"></a>

[Function](class_visualshadernodevectorfunc.md#enum-visualshadernodevectorfunc-function) **FUNC_SIGN** = `25`

Extracts the sign of the parameter, i.e. returns `-1` if the parameter is negative, `1` if it's positive and `0` otherwise.

<a id="class-visualshadernodevectorfunc-constant-func-sin"></a>

[Function](class_visualshadernodevectorfunc.md#enum-visualshadernodevectorfunc-function) **FUNC_SIN** = `26`

Returns the sine of the parameter.

<a id="class-visualshadernodevectorfunc-constant-func-sinh"></a>

[Function](class_visualshadernodevectorfunc.md#enum-visualshadernodevectorfunc-function) **FUNC_SINH** = `27`

Returns the hyperbolic sine of the parameter.

<a id="class-visualshadernodevectorfunc-constant-func-sqrt"></a>

[Function](class_visualshadernodevectorfunc.md#enum-visualshadernodevectorfunc-function) **FUNC_SQRT** = `28`

Returns the square root of the parameter.

<a id="class-visualshadernodevectorfunc-constant-func-tan"></a>

[Function](class_visualshadernodevectorfunc.md#enum-visualshadernodevectorfunc-function) **FUNC_TAN** = `29`

Returns the tangent of the parameter.

<a id="class-visualshadernodevectorfunc-constant-func-tanh"></a>

[Function](class_visualshadernodevectorfunc.md#enum-visualshadernodevectorfunc-function) **FUNC_TANH** = `30`

Returns the hyperbolic tangent of the parameter.

<a id="class-visualshadernodevectorfunc-constant-func-trunc"></a>

[Function](class_visualshadernodevectorfunc.md#enum-visualshadernodevectorfunc-function) **FUNC_TRUNC** = `31`

Returns a value equal to the nearest integer to the parameter whose absolute value is not larger than the absolute value of the parameter.

<a id="class-visualshadernodevectorfunc-constant-func-oneminus"></a>

[Function](class_visualshadernodevectorfunc.md#enum-visualshadernodevectorfunc-function) **FUNC_ONEMINUS** = `32`

Returns `1.0 - vector`.

<a id="class-visualshadernodevectorfunc-constant-func-max"></a>

[Function](class_visualshadernodevectorfunc.md#enum-visualshadernodevectorfunc-function) **FUNC_MAX** = `33`

Represents the size of the [Function](class_visualshadernodevectorfunc.md#enum-visualshadernodevectorfunc-function) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodevectorfunc-property-function"></a>

[Function](class_visualshadernodevectorfunc.md#enum-visualshadernodevectorfunc-function) **function** = `0` [🔗](class_visualshadernodevectorfunc.md#class-visualshadernodevectorfunc-property-function)

- void **set_function**(value: [Function](class_visualshadernodevectorfunc.md#enum-visualshadernodevectorfunc-function))
- [Function](class_visualshadernodevectorfunc.md#enum-visualshadernodevectorfunc-function) **get_function**()

The function to be performed.
