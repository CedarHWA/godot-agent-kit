> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodefloatfunc.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodefloatfunc"></a>

<a id="class-visualshadernodefloatfunc"></a>

# VisualShaderNodeFloatFunc

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A scalar floating-point function to be used within the visual shader graph.

<a id="description"></a>

## Description

Accept a floating-point scalar (`x`) to the input port and transform it according to [function](class_visualshadernodefloatfunc.md#class-visualshadernodefloatfunc-property-function).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Function](class_visualshadernodefloatfunc.md#enum-visualshadernodefloatfunc-function) | [function](class_visualshadernodefloatfunc.md#class-visualshadernodefloatfunc-property-function) | `13` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-visualshadernodefloatfunc-function"></a>

enum **Function**: [🔗](class_visualshadernodefloatfunc.md#enum-visualshadernodefloatfunc-function)

<a id="class-visualshadernodefloatfunc-constant-func-sin"></a>

[Function](class_visualshadernodefloatfunc.md#enum-visualshadernodefloatfunc-function) **FUNC_SIN** = `0`

Returns the sine of the parameter. Translates to `sin(x)` in the Godot Shader Language.

<a id="class-visualshadernodefloatfunc-constant-func-cos"></a>

[Function](class_visualshadernodefloatfunc.md#enum-visualshadernodefloatfunc-function) **FUNC_COS** = `1`

Returns the cosine of the parameter. Translates to `cos(x)` in the Godot Shader Language.

<a id="class-visualshadernodefloatfunc-constant-func-tan"></a>

[Function](class_visualshadernodefloatfunc.md#enum-visualshadernodefloatfunc-function) **FUNC_TAN** = `2`

Returns the tangent of the parameter. Translates to `tan(x)` in the Godot Shader Language.

<a id="class-visualshadernodefloatfunc-constant-func-asin"></a>

[Function](class_visualshadernodefloatfunc.md#enum-visualshadernodefloatfunc-function) **FUNC_ASIN** = `3`

Returns the arc-sine of the parameter. Translates to `asin(x)` in the Godot Shader Language.

<a id="class-visualshadernodefloatfunc-constant-func-acos"></a>

[Function](class_visualshadernodefloatfunc.md#enum-visualshadernodefloatfunc-function) **FUNC_ACOS** = `4`

Returns the arc-cosine of the parameter. Translates to `acos(x)` in the Godot Shader Language.

<a id="class-visualshadernodefloatfunc-constant-func-atan"></a>

[Function](class_visualshadernodefloatfunc.md#enum-visualshadernodefloatfunc-function) **FUNC_ATAN** = `5`

Returns the arc-tangent of the parameter. Translates to `atan(x)` in the Godot Shader Language.

<a id="class-visualshadernodefloatfunc-constant-func-sinh"></a>

[Function](class_visualshadernodefloatfunc.md#enum-visualshadernodefloatfunc-function) **FUNC_SINH** = `6`

Returns the hyperbolic sine of the parameter. Translates to `sinh(x)` in the Godot Shader Language.

<a id="class-visualshadernodefloatfunc-constant-func-cosh"></a>

[Function](class_visualshadernodefloatfunc.md#enum-visualshadernodefloatfunc-function) **FUNC_COSH** = `7`

Returns the hyperbolic cosine of the parameter. Translates to `cosh(x)` in the Godot Shader Language.

<a id="class-visualshadernodefloatfunc-constant-func-tanh"></a>

[Function](class_visualshadernodefloatfunc.md#enum-visualshadernodefloatfunc-function) **FUNC_TANH** = `8`

Returns the hyperbolic tangent of the parameter. Translates to `tanh(x)` in the Godot Shader Language.

<a id="class-visualshadernodefloatfunc-constant-func-log"></a>

[Function](class_visualshadernodefloatfunc.md#enum-visualshadernodefloatfunc-function) **FUNC_LOG** = `9`

Returns the natural logarithm of the parameter. Translates to `log(x)` in the Godot Shader Language.

<a id="class-visualshadernodefloatfunc-constant-func-exp"></a>

[Function](class_visualshadernodefloatfunc.md#enum-visualshadernodefloatfunc-function) **FUNC_EXP** = `10`

Returns the natural exponentiation of the parameter. Translates to `exp(x)` in the Godot Shader Language.

<a id="class-visualshadernodefloatfunc-constant-func-sqrt"></a>

[Function](class_visualshadernodefloatfunc.md#enum-visualshadernodefloatfunc-function) **FUNC_SQRT** = `11`

Returns the square root of the parameter. Translates to `sqrt(x)` in the Godot Shader Language.

<a id="class-visualshadernodefloatfunc-constant-func-abs"></a>

[Function](class_visualshadernodefloatfunc.md#enum-visualshadernodefloatfunc-function) **FUNC_ABS** = `12`

Returns the absolute value of the parameter. Translates to `abs(x)` in the Godot Shader Language.

<a id="class-visualshadernodefloatfunc-constant-func-sign"></a>

[Function](class_visualshadernodefloatfunc.md#enum-visualshadernodefloatfunc-function) **FUNC_SIGN** = `13`

Extracts the sign of the parameter. Translates to `sign(x)` in the Godot Shader Language.

<a id="class-visualshadernodefloatfunc-constant-func-floor"></a>

[Function](class_visualshadernodefloatfunc.md#enum-visualshadernodefloatfunc-function) **FUNC_FLOOR** = `14`

Finds the nearest integer less than or equal to the parameter. Translates to `floor(x)` in the Godot Shader Language.

<a id="class-visualshadernodefloatfunc-constant-func-round"></a>

[Function](class_visualshadernodefloatfunc.md#enum-visualshadernodefloatfunc-function) **FUNC_ROUND** = `15`

Finds the nearest integer to the parameter. Translates to `round(x)` in the Godot Shader Language.

<a id="class-visualshadernodefloatfunc-constant-func-ceil"></a>

[Function](class_visualshadernodefloatfunc.md#enum-visualshadernodefloatfunc-function) **FUNC_CEIL** = `16`

Finds the nearest integer that is greater than or equal to the parameter. Translates to `ceil(x)` in the Godot Shader Language.

<a id="class-visualshadernodefloatfunc-constant-func-fract"></a>

[Function](class_visualshadernodefloatfunc.md#enum-visualshadernodefloatfunc-function) **FUNC_FRACT** = `17`

Computes the fractional part of the argument. Translates to `fract(x)` in the Godot Shader Language.

<a id="class-visualshadernodefloatfunc-constant-func-saturate"></a>

[Function](class_visualshadernodefloatfunc.md#enum-visualshadernodefloatfunc-function) **FUNC_SATURATE** = `18`

Clamps the value between `0.0` and `1.0` using `min(max(x, 0.0), 1.0)`.

<a id="class-visualshadernodefloatfunc-constant-func-negate"></a>

[Function](class_visualshadernodefloatfunc.md#enum-visualshadernodefloatfunc-function) **FUNC_NEGATE** = `19`

Negates the `x` using `-(x)`.

<a id="class-visualshadernodefloatfunc-constant-func-acosh"></a>

[Function](class_visualshadernodefloatfunc.md#enum-visualshadernodefloatfunc-function) **FUNC_ACOSH** = `20`

Returns the arc-hyperbolic-cosine of the parameter. Translates to `acosh(x)` in the Godot Shader Language.

<a id="class-visualshadernodefloatfunc-constant-func-asinh"></a>

[Function](class_visualshadernodefloatfunc.md#enum-visualshadernodefloatfunc-function) **FUNC_ASINH** = `21`

Returns the arc-hyperbolic-sine of the parameter. Translates to `asinh(x)` in the Godot Shader Language.

<a id="class-visualshadernodefloatfunc-constant-func-atanh"></a>

[Function](class_visualshadernodefloatfunc.md#enum-visualshadernodefloatfunc-function) **FUNC_ATANH** = `22`

Returns the arc-hyperbolic-tangent of the parameter. Translates to `atanh(x)` in the Godot Shader Language.

<a id="class-visualshadernodefloatfunc-constant-func-degrees"></a>

[Function](class_visualshadernodefloatfunc.md#enum-visualshadernodefloatfunc-function) **FUNC_DEGREES** = `23`

Convert a quantity in radians to degrees. Translates to `degrees(x)` in the Godot Shader Language.

<a id="class-visualshadernodefloatfunc-constant-func-exp2"></a>

[Function](class_visualshadernodefloatfunc.md#enum-visualshadernodefloatfunc-function) **FUNC_EXP2** = `24`

Returns 2 raised by the power of the parameter. Translates to `exp2(x)` in the Godot Shader Language.

<a id="class-visualshadernodefloatfunc-constant-func-inverse-sqrt"></a>

[Function](class_visualshadernodefloatfunc.md#enum-visualshadernodefloatfunc-function) **FUNC_INVERSE_SQRT** = `25`

Returns the inverse of the square root of the parameter. Translates to `inversesqrt(x)` in the Godot Shader Language.

<a id="class-visualshadernodefloatfunc-constant-func-log2"></a>

[Function](class_visualshadernodefloatfunc.md#enum-visualshadernodefloatfunc-function) **FUNC_LOG2** = `26`

Returns the base 2 logarithm of the parameter. Translates to `log2(x)` in the Godot Shader Language.

<a id="class-visualshadernodefloatfunc-constant-func-radians"></a>

[Function](class_visualshadernodefloatfunc.md#enum-visualshadernodefloatfunc-function) **FUNC_RADIANS** = `27`

Convert a quantity in degrees to radians. Translates to `radians(x)` in the Godot Shader Language.

<a id="class-visualshadernodefloatfunc-constant-func-reciprocal"></a>

[Function](class_visualshadernodefloatfunc.md#enum-visualshadernodefloatfunc-function) **FUNC_RECIPROCAL** = `28`

Finds reciprocal value of dividing 1 by `x` (i.e. `1 / x`).

<a id="class-visualshadernodefloatfunc-constant-func-roundeven"></a>

[Function](class_visualshadernodefloatfunc.md#enum-visualshadernodefloatfunc-function) **FUNC_ROUNDEVEN** = `29`

Finds the nearest even integer to the parameter. Translates to `roundEven(x)` in the Godot Shader Language.

<a id="class-visualshadernodefloatfunc-constant-func-trunc"></a>

[Function](class_visualshadernodefloatfunc.md#enum-visualshadernodefloatfunc-function) **FUNC_TRUNC** = `30`

Returns a value equal to the nearest integer to `x` whose absolute value is not larger than the absolute value of `x`. Translates to `trunc(x)` in the Godot Shader Language.

<a id="class-visualshadernodefloatfunc-constant-func-oneminus"></a>

[Function](class_visualshadernodefloatfunc.md#enum-visualshadernodefloatfunc-function) **FUNC_ONEMINUS** = `31`

Subtracts scalar `x` from 1 (i.e. `1 - x`).

<a id="class-visualshadernodefloatfunc-constant-func-max"></a>

[Function](class_visualshadernodefloatfunc.md#enum-visualshadernodefloatfunc-function) **FUNC_MAX** = `32`

Represents the size of the [Function](class_visualshadernodefloatfunc.md#enum-visualshadernodefloatfunc-function) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodefloatfunc-property-function"></a>

[Function](class_visualshadernodefloatfunc.md#enum-visualshadernodefloatfunc-function) **function** = `13` [🔗](class_visualshadernodefloatfunc.md#class-visualshadernodefloatfunc-property-function)

- void **set_function**(value: [Function](class_visualshadernodefloatfunc.md#enum-visualshadernodefloatfunc-function))
- [Function](class_visualshadernodefloatfunc.md#enum-visualshadernodefloatfunc-function) **get_function**()

A function to be applied to the scalar.
