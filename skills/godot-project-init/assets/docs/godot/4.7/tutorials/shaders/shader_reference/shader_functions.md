> Source: https://docs.godotengine.org/en/4.7/tutorials/shaders/shader_reference/shader_functions.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="built-in-shader-functions"></a>

<a id="doc-shader-functions"></a>

# Built-in shader functions

Godot supports a large number of built-in shader functions, conforming roughly to the
GLSL ES 3.0 specification.

Note

The following type aliases only used in documentation to reduce repetitive function declarations.
They can each refer to any of several actual types.

| alias | actual types | glsl documentation alias |
| --- | --- | --- |
| vec_type | float, vec2, vec3, or vec4 | genType |
| vec_int_type | int, ivec2, ivec3, or ivec4 | genIType |
| vec_uint_type | uint, uvec2, uvec3, or uvec4 | genUType |
| vec_bool_type | bool, bvec2, bvec3, or bvec4 | genBType |
| mat_type | mat2, mat3, or mat4 | mat |
| gvec4_type | vec4, ivec4, or uvec4 | gvec4 |
| gsampler2D | sampler2D, isampler2D, or uSampler2D | gsampler2D |
| gsampler2DArray | sampler2DArray, isampler2DArray, or uSampler2DArray | gsampler2DArray |
| gsampler3D | sampler3D, isampler3D, or uSampler3D | gsampler3D |

If any of these are specified for multiple parameters, they must all be the same type unless otherwise noted.

<a id="shading-componentwise"></a>

Note

Many functions that accept one or more vectors or matrices perform the described function on each component of the vector/matrix.
Some examples:

| Operation | Equivalent Scalar Operation |
| --- | --- |
| `sqrt(vec2(4, 64))` | `vec2(sqrt(4), sqrt(64))` |
| `min(vec2(3, 4), 1)` | `vec2(min(3, 1), min(4, 1))` |
| `min(vec3(1, 2, 3),vec3(5, 1, 3))` | `vec3(min(1, 5), min(2, 1), min(3, 3))` |
| `pow(vec3(3, 8, 5 ), 2)` | `vec3(pow(3, 2), pow(8, 2), pow(5, 2))` |
| `pow(vec3(3, 8, 5), vec3(1, 2, 4))` | `vec3(pow(3, 1), pow(8, 2), pow(5, 4))` |

The [GLSL Language Specification](http://www.opengl.org/registry/doc/GLSLangSpec.4.30.6.pdf) says under section 5.10 Vector and Matrix Operations:

> With a few exceptions, operations are component-wise. Usually, when an operator operates on a
> vector or matrix, it is operating independently on each component of the vector or matrix,
> in a component-wise fashion. [...] The exceptions are matrix multiplied by vector,
> vector multiplied by matrix, and matrix multiplied by matrix. These do not operate component-wise,
> but rather perform the correct linear algebraic multiply.

These function descriptions are adapted and modified from
[official OpenGL documentation](https://registry.khronos.org/OpenGL-Refpages/gl4/)
originally published by Khronos Group under the
[Open Publication License](https://opencontent.org/openpub).
Each function description links to the corresponding official OpenGL
documentation. Modification history for this page can be found on
[GitHub](https://github.com/godotengine/godot-docs/blob/master/tutorials/shaders/shader_reference/shader_functions.rst).

---


<a id="trigonometric-functions"></a>

## Trigonometric functions

| Return Type | Function | Description / Return value |
| --- | --- | --- |
| vec_type | [radians](shader_functions.md#shader-func-radians)(vec_type degrees) | Convert degrees to radians. |
| vec_type | [degrees](shader_functions.md#shader-func-degrees)(vec_type radians) | Convert radians to degrees. |
| vec_type | [sin](shader_functions.md#shader-func-sin)(vec_type x) | Sine. |
| vec_type | [cos](shader_functions.md#shader-func-cos)(vec_type x) | Cosine. |
| vec_type | [tan](shader_functions.md#shader-func-tan)(vec_type x) | Tangent. |
| vec_type | [asin](shader_functions.md#shader-func-asin)(vec_type x) | Arc sine. |
| vec_type | [acos](shader_functions.md#shader-func-acos)(vec_type x) | Arc cosine. |
| vec_type  vec_type | [atan](shader_functions.md#shader-func-atan)(vec_type y_over_x)  [atan](shader_functions.md#shader-func-atan2)(vec_type y, vec_type x) | Arc tangent. |
| vec_type | [sinh](shader_functions.md#shader-func-sinh)(vec_type x) | Hyperbolic sine. |
| vec_type | [cosh](shader_functions.md#shader-func-cosh)(vec_type x) | Hyperbolic cosine. |
| vec_type | [tanh](shader_functions.md#shader-func-tanh)(vec_type x) | Hyperbolic tangent. |
| vec_type | [asinh](shader_functions.md#shader-func-asinh)(vec_type x) | Arc hyperbolic sine. |
| vec_type | [acosh](shader_functions.md#shader-func-acosh)(vec_type x) | Arc hyperbolic cosine. |
| vec_type | [atanh](shader_functions.md#shader-func-atanh)(vec_type x) | Arc hyperbolic tangent. |

<a id="trigonometric-function-descriptions"></a>

### Trigonometric function descriptions

<a id="shader-func-radians"></a>

vec_type **radians**(vec_type degrees) [🔗](shader_functions.md#shader-func-radians)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Converts a quantity specified in degrees into radians, with the formula
> `degrees * (PI / 180)`.
>
> param degrees:
> :   The quantity, in degrees, to be converted to radians.
>
> return:
> :   The input `degrees` converted to radians.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/radians.xhtml>

---


<a id="shader-func-degrees"></a>

vec_type **degrees**(vec_type radians) [🔗](shader_functions.md#shader-func-degrees)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Converts a quantity specified in radians into degrees, with the formula
> `radians * (180 / PI)`
>
> param radians:
> :   The quantity, in radians, to be converted to degrees.
>
> return:
> :   The input `radians` converted to degrees.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/degrees.xhtml>

---


<a id="shader-func-sin"></a>

vec_type **sin**(vec_type angle) [🔗](shader_functions.md#shader-func-sin)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Returns the trigonometric sine of `angle`.
>
> param angle:
> :   The quantity, in radians, of which to return the sine.
>
> return:
> :   The sine of `angle`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/sin.xhtml>

---


<a id="shader-func-cos"></a>

vec_type **cos**(vec_type angle) [🔗](shader_functions.md#shader-func-cos)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Returns the trigonometric cosine of `angle`.
>
> param angle:
> :   The quantity, in radians, of which to return the cosine.
>
> return:
> :   The cosine of `angle`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/cos.xhtml>

---


<a id="shader-func-tan"></a>

vec_type **tan**(vec_type angle) [🔗](shader_functions.md#shader-func-tan)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Returns the trigonometric tangent of `angle`.
>
> param angle:
> :   The quantity, in radians, of which to return the tangent.
>
> return:
> :   The tangent of `angle`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/tan.xhtml>

---


<a id="shader-func-asin"></a>

vec_type **asin**(vec_type x) [🔗](shader_functions.md#shader-func-asin)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Arc sine, or inverse sine.
> Calculates the angle whose sine is `x` and is in the range `[-PI/2, PI/2]`.
> The result is undefined if `x < -1` or `x > 1`.
>
> param x:
> :   The value whose arc sine to return.
>
> return:
> :   The angle whose trigonometric sine is `x`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/asin.xhtml>

---


<a id="shader-func-acos"></a>

vec_type **acos**(vec_type x) [🔗](shader_functions.md#shader-func-acos)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Arc cosine, or inverse cosine.
> Calculates the angle whose cosine is `x` and is in the range `[0, PI]`.
>
> The result is undefined if `x < -1` or `x > 1`.
>
> param x:
> :   The value whose arc cosine to return.
>
> return:
> :   The angle whose trigonometric cosine is `x`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/acos.xhtml>

---


<a id="shader-func-atan"></a>

vec_type **atan**(vec_type y_over_x) [🔗](shader_functions.md#shader-func-atan)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Calculates the arc tangent given a tangent value of `y/x`.
>
> Note
>
> Because of the sign ambiguity, the function cannot determine with certainty in
> which quadrant the angle falls only by its tangent value. If you need to know the
> quadrant, use [atan(vec_type y, vec_type x)](shader_functions.md#shader-func-atan2).
>
> param y_over_x:
> :   The fraction whose arc tangent to return.
>
> return:
> :   The trigonometric arc-tangent of `y_over_x` and is
>     in the range `[-PI/2, PI/2]`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/atan.xhtml>

---


<a id="shader-func-atan2"></a>

vec_type **atan**(vec_type y, vec_type x) [🔗](shader_functions.md#shader-func-atan2)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Calculates the arc tangent given a numerator and denominator. The signs of
> `y` and `x` are used to determine the quadrant that the angle lies in.
> The result is undefined if `x == 0`.
>
> Equivalent to [atan2()](../../../classes/class_@globalscope.md#class-globalscope-method-atan2) in GDScript.
>
> param y:
> :   The numerator of the fraction whose arc tangent to return.
>
> param x:
> :   The denominator of the fraction whose arc tangent to return.
>
> return:
> :   The trigonometric arc tangent of `y/x` and is in
>     the range `[-PI, PI]`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/atan.xhtml>

---


<a id="shader-func-sinh"></a>

vec_type **sinh**(vec_type x) [🔗](shader_functions.md#shader-func-sinh)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Calculates the hyperbolic sine using `(e^x - e^-x)/2`.
>
> param x:
> :   The value whose hyperbolic sine to return.
>
> return:
> :   The hyperbolic sine of `x`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/sinh.xhtml>

---


<a id="shader-func-cosh"></a>

vec_type **cosh**(vec_type x) [🔗](shader_functions.md#shader-func-cosh)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Calculates the hyperbolic cosine using `(e^x + e^-x)/2`.
>
> param x:
> :   The value whose hyperbolic cosine to return.
>
> return:
> :   The hyperbolic cosine of `x`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/cosh.xhtml>

---


<a id="shader-func-tanh"></a>

vec_type **tanh**(vec_type x) [🔗](shader_functions.md#shader-func-tanh)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Calculates the hyperbolic tangent using `sinh(x)/cosh(x)`.
>
> param x:
> :   The value whose hyperbolic tangent to return.
>
> return:
> :   The hyperbolic tangent of `x`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/tanh.xhtml>

---


<a id="shader-func-asinh"></a>

vec_type **asinh**(vec_type x) [🔗](shader_functions.md#shader-func-asinh)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Calculates the arc hyperbolic sine of `x`, or the inverse of `sinh`.
>
> param x:
> :   The value whose arc hyperbolic sine to return.
>
> return:
> :   The arc hyperbolic sine of `x`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/asinh.xhtml>

---


<a id="shader-func-acosh"></a>

vec_type **acosh**(vec_type x) [🔗](shader_functions.md#shader-func-acosh)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Calculates the arc hyperbolic cosine of `x`, or the non-negative inverse of `cosh`.
> The result is undefined if `x < 1`.
>
> param x:
> :   The value whose arc hyperbolic cosine to return.
>
> return:
> :   The arc hyperbolic cosine of `x`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/acosh.xhtml>

---


<a id="shader-func-atanh"></a>

vec_type **atanh**(vec_type x) [🔗](shader_functions.md#shader-func-atanh)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Calculates the arc hyperbolic tangent of `x`, or the inverse of `tanh`.
> The result is undefined if `abs(x) > 1`.
>
> param x:
> :   The value whose arc hyperbolic tangent to return.
>
> return:
> :   The arc hyperbolic tangent of `x`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/atanh.xhtml>

---


<a id="exponential-and-math-functions"></a>

## Exponential and math functions

| Return Type | Function | Description / Return value |
| --- | --- | --- |
| vec_type | [pow](shader_functions.md#shader-func-pow)(vec_type x, vec_type y) | Power (undefined if `x < 0` or if `x == 0` and `y <= 0`). |
| vec_type | [exp](shader_functions.md#shader-func-exp)(vec_type x) | Base-e exponential. |
| vec_type | [exp2](shader_functions.md#shader-func-exp2)(vec_type x) | Base-2 exponential. |
| vec_type | [log](shader_functions.md#shader-func-log)(vec_type x) | Natural (base-e) logarithm. |
| vec_type | [log2](shader_functions.md#shader-func-log2)(vec_type x) | Base-2 logarithm. |
| vec_type | [sqrt](shader_functions.md#shader-func-sqrt)(vec_type x) | Square root. |
| vec_type | [inversesqrt](shader_functions.md#shader-func-inversesqrt)(vec_type x) | Inverse square root. |
| vec_type  vec_int_type | [abs](shader_functions.md#shader-func-abs)(vec_type x)  [abs](shader_functions.md#shader-func-abs)(vec_int_type x) | Absolute value (returns positive value if negative). |
| vec_type | [sign](shader_functions.md#shader-func-sign)(vec_type x) | Returns `1.0` if positive, `-1.0` if negative, `0.0` otherwise. |
| vec_int_type | [sign](shader_functions.md#shader-func-sign)(vec_int_type x) | Returns `1` if positive, `-1` if negative, `0` otherwise. |
| vec_type | [floor](shader_functions.md#shader-func-floor)(vec_type x) | Rounds to the integer below. |
| vec_type | [round](shader_functions.md#shader-func-round)(vec_type x) | Rounds to the nearest integer. |
| vec_type | [roundEven](shader_functions.md#shader-func-roundeven)(vec_type x) | Rounds to the nearest even integer. |
| vec_type | [trunc](shader_functions.md#shader-func-trunc)(vec_type x) | Truncation. |
| vec_type | [ceil](shader_functions.md#shader-func-ceil)(vec_type x) | Rounds to the integer above. |
| vec_type | [fract](shader_functions.md#shader-func-fract)(vec_type x) | Fractional (returns `x - floor(x)`). |
| vec_type  vec_type | [mod](shader_functions.md#shader-func-mod)(vec_type x, vec_type y)  [mod](shader_functions.md#shader-func-mod)(vec_type x, float y) | Modulo (division remainder). |
| vec_type | [modf](shader_functions.md#shader-func-modf)(vec_type x, out vec_type i) | Fractional of `x`, with `i` as integer part. |
| vec_type  vec_type  vec_int_type  vec_int_type  vec_uint_type  vec_uint_type | [min](shader_functions.md#shader-func-min)(vec_type a, vec_type b)  [min](shader_functions.md#shader-func-min)(vec_type a, float b)  [min](shader_functions.md#shader-func-min)(vec_int_type a, vec_int_type b)  [min](shader_functions.md#shader-func-min)(vec_int_type a, int b)  [min](shader_functions.md#shader-func-min)(vec_uint_type a, vec_uint_type b)  [min](shader_functions.md#shader-func-min)(vec_uint_type a, uint b) | Lowest value between `a` and `b`. |
| vec_type  vec_type  vec_int_type  vec_int_type  vec_uint_type  vec_uint_type | [max](shader_functions.md#shader-func-max)(vec_type a, vec_type b)  [max](shader_functions.md#shader-func-max)(vec_type a, float b)  [max](shader_functions.md#shader-func-max)(vec_int_type a, vec_int_type b)  [max](shader_functions.md#shader-func-max)(vec_int_type a, int b)  [max](shader_functions.md#shader-func-max)(vec_uint_type a, vec_uint_type b)  [max](shader_functions.md#shader-func-max)(vec_uint_type a, uint b) | Highest value between `a` and `b`. |
| vec_type  vec_type  vec_int_type  vec_int_type  vec_uint_type  vec_uint_type | [clamp](shader_functions.md#shader-func-clamp)(vec_type x, vec_type min, vec_type max)  [clamp](shader_functions.md#shader-func-clamp)(vec_type x, float min, float max)  [clamp](shader_functions.md#shader-func-clamp)(vec_int_type x, vec_int_type min, vec_int_type max)  [clamp](shader_functions.md#shader-func-clamp)(vec_int_type x, int min, int max)  [clamp](shader_functions.md#shader-func-clamp)(vec_uint_type x, vec_uint_type min, vec_uint_type max)  [clamp](shader_functions.md#shader-func-clamp)(vec_uint_type x, uint min, uint max) | Clamps `x` between `min` and `max` (inclusive). |
| vec_type  vec_type  vec_type | [mix](shader_functions.md#shader-func-mix)(vec_type a, vec_type b, vec_type c)  [mix](shader_functions.md#shader-func-mix)(vec_type a, vec_type b, float c)  [mix](shader_functions.md#shader-func-mix)(vec_type a, vec_type b, vec_bool_type c) | Linear interpolate between `a` and `b` by `c`. |
| vec_type | [fma](shader_functions.md#shader-func-fma)(vec_type a, vec_type b, vec_type c) | Fused multiply-add operation: `(a * b + c)` |
| vec_type  vec_type | [step](shader_functions.md#shader-func-step)(vec_type a, vec_type b)  [step](shader_functions.md#shader-func-step)(float a, vec_type b) | `b < a ? 0.0 : 1.0` |
| vec_type  vec_type | [smoothstep](shader_functions.md#shader-func-smoothstep)(vec_type a, vec_type b, vec_type c)  [smoothstep](shader_functions.md#shader-func-smoothstep)(float a, float b, vec_type c) | Hermite interpolate between `a` and `b` by `c`. |
| vec_bool_type | [isnan](shader_functions.md#shader-func-isnan)(vec_type x) | Returns `true` if scalar or vector component is `NaN`. |
| vec_bool_type | [isinf](shader_functions.md#shader-func-isinf)(vec_type x) | Returns `true` if scalar or vector component is `INF`. |
| vec_int_type | [floatBitsToInt](shader_functions.md#shader-func-floatbitstoint)(vec_type x) | `float` to `int` bit copying, no conversion. |
| vec_uint_type | [floatBitsToUint](shader_functions.md#shader-func-floatbitstouint)(vec_type x) | `float` to `uint` bit copying, no conversion. |
| vec_type | [intBitsToFloat](shader_functions.md#shader-func-intbitstofloat)(vec_int_type x) | `int` to `float` bit copying, no conversion. |
| vec_type | [uintBitsToFloat](shader_functions.md#shader-func-uintbitstofloat)(vec_uint_type x) | `uint` to `float` bit copying, no conversion. |

<a id="exponential-and-math-function-descriptions"></a>

### Exponential and math function descriptions

<a id="shader-func-pow"></a>

vec_type **pow**(vec_type x, vec_type y) [🔗](shader_functions.md#shader-func-pow)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Raises `x` to the power of `y`.
>
> The result is undefined if `x < 0` or if `x == 0` and `y <= 0`.
>
> param x:
> :   The value to be raised to the power `y`.
>
> param y:
> :   The power to which `x` will be raised.
>
> return:
> :   The value of `x` raised to the `y` power.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/pow.xhtml>

---


<a id="shader-func-exp"></a>

vec_type **exp**(vec_type x) [🔗](shader_functions.md#shader-func-exp)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Raises `e` to the power of `x`, or the the natural exponentiation.
>
> Equivalent to `pow(e, x)`.
>
> param x:
> :   The value to exponentiate.
>
> return:
> :   The natural exponentiation of `x`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/exp.xhtml>

---


<a id="shader-func-exp2"></a>

vec_type **exp2**(vec_type x) [🔗](shader_functions.md#shader-func-exp2)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Raises `2` to the power of `x`.
>
> Equivalent to `pow(2.0, x)`.
>
> param x:
> :   The value of the power to which `2` will be raised.
>
> return:
> :   `2` raised to the power of `x`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/exp2.xhtml>

---


<a id="shader-func-log"></a>

vec_type **log**(vec_type x) [🔗](shader_functions.md#shader-func-log)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Returns the natural logarithm of `x`, i.e. the value `y` which satisfies `x == pow(e, y)`.
> The result is undefined if `x <= 0`.
>
> param x:
> :   The value of which to take the natural logarithm.
>
> return:
> :   The natural logarithm of `x`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/log.xhtml>

---


<a id="shader-func-log2"></a>

vec_type **log2**(vec_type x) [🔗](shader_functions.md#shader-func-log2)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Returns the base-2 logarithm of `x`, i.e. the value `y` which satisfies `x == pow(2, y)`.
> The result is undefined if `x <= 0`.
>
> param x:
> :   The value of which to take the base-2 logarithm.
>
> return:
> :   The base-2 logarithm of `x`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/log2.xhtml>

---


<a id="shader-func-sqrt"></a>

vec_type **sqrt**(vec_type x) [🔗](shader_functions.md#shader-func-sqrt)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Returns the square root of `x`.
> The result is undefined if `x < 0`.
>
> param x:
> :   The value of which to take the square root.
>
> return:
> :   The square root of `x`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/sqrt.xhtml>

---


<a id="shader-func-inversesqrt"></a>

vec_type **inversesqrt**(vec_type x) [🔗](shader_functions.md#shader-func-inversesqrt)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Returns the inverse of the square root of `x`, or `1.0 / sqrt(x)`.
> The result is undefined if `x <= 0`.
>
> param x:
> :   The value of which to take the inverse of the square root.
>
> return:
> :   The inverse of the square root of `x`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/inversesqrt.xhtml>

---


<a id="shader-func-abs"></a>

vec_type **abs**(vec_type x) [🔗](shader_functions.md#shader-func-abs)

vec_int_type **abs**(vec_int_type x) [🔗](shader_functions.md#shader-func-abs)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Returns the absolute value of `x`. Returns `x` if `x` is positive, otherwise returns `-1 * x`.
>
> param x:
> :   The value of which to return the absolute.
>
> return:
> :   The absolute value of `x`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/abs.xhtml>

---


<a id="shader-func-sign"></a>

vec_type **sign**(vec_type x) [🔗](shader_functions.md#shader-func-sign)

vec_int_type **sign**(vec_int_type x) [🔗](shader_functions.md#shader-func-sign)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Returns `-1` if `x < 0`, `0` if `x == 0`, and `1` if `x > 0`.
>
> param x:
> :   The value from which to extract the sign.
>
> return:
> :   The sign of `x`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/sign.xhtml>

---


<a id="shader-func-floor"></a>

vec_type **floor**(vec_type x) [🔗](shader_functions.md#shader-func-floor)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Returns a value equal to the nearest integer that is less than or equal to `x`.
>
> param x:
> :   The value to floor.
>
> return:
> :   The nearest integer that is less than or equal to `x`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/floor.xhtml>

---


<a id="shader-func-round"></a>

vec_type **round**(vec_type x) [🔗](shader_functions.md#shader-func-round)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Rounds `x` to the nearest integer.
>
> Note
>
> Rounding of values with a fractional part of `0.5` is implementation-dependent.
> This includes the possibility that `round(x)` returns the same value as
> `roundEven(x)` for all values of `x`.
>
> param x:
> :   The value to round.
>
> return:
> :   The rounded value.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/round.xhtml>

---


<a id="shader-func-roundeven"></a>

vec_type **roundEven**(vec_type x) [🔗](shader_functions.md#shader-func-roundeven)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Rounds `x` to the nearest integer. A value with a fractional part of `0.5`
> will always round toward the nearest even integer.
> For example, both `3.5` and `4.5` will round to `4.0`.
>
> param x:
> :   The value to round.
>
> return:
> :   The rounded value.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/roundEven.xhtml>

---


<a id="shader-func-trunc"></a>

vec_type **trunc**(vec_type x) [🔗](shader_functions.md#shader-func-trunc)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Truncates `x`. Returns a value equal to the nearest integer to `x` whose
> absolute value is not larger than the absolute value of `x`.
>
> param x:
> :   The value to evaluate.
>
> return:
> :   The truncated value.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/trunc.xhtml>

---


<a id="shader-func-ceil"></a>

vec_type **ceil**(vec_type x) [🔗](shader_functions.md#shader-func-ceil)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Returns a value equal to the nearest integer that is greater than or equal to `x`.
>
> param x:
> :   The value to evaluate.
>
> return:
> :   The ceiling-ed value.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/ceil.xhtml>

---


<a id="shader-func-fract"></a>

vec_type **fract**(vec_type x) [🔗](shader_functions.md#shader-func-fract)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Returns the fractional part of `x`.
>
> This is calculated as `x - floor(x)`.
>
> param x:
> :   The value to evaluate.
>
> return:
> :   The fractional part of `x`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/fract.xhtml>

---


<a id="shader-func-mod"></a>

vec_type **mod**(vec_type x, vec_type y) [🔗](shader_functions.md#shader-func-mod)

vec_type **mod**(vec_type x, float y) [🔗](shader_functions.md#shader-func-mod)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Returns the value of `x modulo y`.
> This is also sometimes called the remainder.
>
> This is computed as `x - y * floor(x/y)`.
>
> param x:
> :   The value to evaluate.
>
> return:
> :   The value of `x modulo y`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/mod.xhtml>

---


<a id="shader-func-modf"></a>

vec_type **modf**(vec_type x, out vec_type i) [🔗](shader_functions.md#shader-func-modf)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Separates a floating-point value `x` into its integer and fractional parts.
>
> The fractional part of the number is returned from the function.
> The integer part (as a floating-point quantity) is returned in the output parameter `i`.
>
> param x:
> :   The value to separate.
>
> param out i:
> :   A variable that receives the integer part of `x`.
>
> return:
> :   The fractional part of the number.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/modf.xhtml>

---


<a id="shader-func-min"></a>

vec_type **min**(vec_type a, vec_type b) [🔗](shader_functions.md#shader-func-min)

vec_type **min**(vec_type a, float b) [🔗](shader_functions.md#shader-func-min)

vec_int_type **min**(vec_int_type a, vec_int_type b) [🔗](shader_functions.md#shader-func-min)

vec_int_type **min**(vec_int_type a, int b) [🔗](shader_functions.md#shader-func-min)

vec_uint_type **min**(vec_uint_type a, vec_uint_type b) [🔗](shader_functions.md#shader-func-min)

vec_uint_type **min**(vec_uint_type a, uint b) [🔗](shader_functions.md#shader-func-min)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Returns the minimum of two values `a` and `b`.
>
> Returns `b` if `b < a`, otherwise returns `a`.
>
> param a:
> :   The first value to compare.
>
> param b:
> :   The second value to compare.
>
> return:
> :   The minimum value.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/min.xhtml>

---


<a id="shader-func-max"></a>

vec_type **max**(vec_type a, vec_type b) [🔗](shader_functions.md#shader-func-max)

vec_type **max**(vec_type a, float b) [🔗](shader_functions.md#shader-func-max)

vec_uint_type **max**(vec_uint_type a, vec_uint_type b) [🔗](shader_functions.md#shader-func-max)

vec_uint_type **max**(vec_uint_type a, uint b) [🔗](shader_functions.md#shader-func-max)

vec_int_type **max**(vec_int_type a, vec_int_type b) [🔗](shader_functions.md#shader-func-max)

vec_int_type **max**(vec_int_type a, int b) [🔗](shader_functions.md#shader-func-max)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Returns the maximum of two values `a` and `b`.
>
> It returns `b` if `b > a`, otherwise it returns `a`.
>
> param a:
> :   The first value to compare.
>
> param b:
> :   The second value to compare.
>
> return:
> :   The maximum value.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/max.xhtml>

---


<a id="shader-func-clamp"></a>

vec_type **clamp**(vec_type x, vec_type minVal, vec_type maxVal) [🔗](shader_functions.md#shader-func-clamp)

vec_type **clamp**(vec_type x, float minVal, float maxVal) [🔗](shader_functions.md#shader-func-clamp)

vec_int_type **clamp**(vec_int_type x, vec_int_type minVal, vec_int_type maxVal) [🔗](shader_functions.md#shader-func-clamp)

vec_int_type **clamp**(vec_int_type x, int minVal, int maxVal) [🔗](shader_functions.md#shader-func-clamp)

vec_uint_type **clamp**(vec_uint_type x, vec_uint_type minVal, vec_uint_type maxVal) [🔗](shader_functions.md#shader-func-clamp)

vec_uint_type **clamp**(vec_uint_type x, uint minVal, uint maxVal) [🔗](shader_functions.md#shader-func-clamp)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Returns the value of `x` constrained to the range `minVal` to `maxVal`.
>
> The returned value is computed as `min(max(x, minVal), maxVal)`.
>
> param x:
> :   The value to constrain.
>
> param minVal:
> :   The lower end of the range into which to constrain `x`.
>
> param maxVal:
> :   The upper end of the range into which to constrain `x`.
>
> return:
> :   The clamped value.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/clamp.xhtml>

---


<a id="shader-func-mix"></a>

vec_type **mix**(vec_type a, vec_type b, vec_type c) [🔗](shader_functions.md#shader-func-mix)

vec_type **mix**(vec_type a, vec_type b, float c) [🔗](shader_functions.md#shader-func-mix)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Performs a linear interpolation between `a` and `b` using `c` to weight between them.
>
> Computed as `a * (1 - c) + b * c`.
>
> Equivalent to [lerp()](../../../classes/class_@globalscope.md#class-globalscope-method-lerp) in GDScript.
>
> param a:
> :   The start of the range in which to interpolate.
>
> param b:
> :   The end of the range in which to interpolate.
>
> param c:
> :   The value to use to interpolate between `a` and `b`.
>
> return:
> :   The interpolated value.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/mix.xhtml>

---

vec_type **mix**(vec_type a, vec_type b, vec_bool_type c) [🔗](shader_functions.md#shader-func-mix)

> Selects either value `a` or value `b` based on the value of `c`.
> For a component of `c` that is false, the corresponding component of `a` is returned.
> For a component of `c` that is true, the corresponding component of `b` is returned.
> Components of `a` and `b` that are not selected are allowed to be invalid floating-point values and will have no effect on the results.
>
> If `a`, `b`, and `c` are vector types the operation is performed [component-wise](shader_functions.md#shading-componentwise).
> For example, `mix(vec2(42, 314), vec2(9.8, 6e23), bvec2(true, false)))` will return `vec2(9.8, 314)`.
>
> param a:
> :   Value returned when `c` is false.
>
> param b:
> :   Value returned when `c` is true.
>
> param c:
> :   The value used to select between `a` and `b`.
>
> return:
> :   The interpolated value.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/mix.xhtml>

---


<a id="shader-func-fma"></a>

vec_type **fma**(vec_type a, vec_type b, vec_type c) [🔗](shader_functions.md#shader-func-fma)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Performs, where possible, a fused multiply-add operation, returning `a * b + c`. In use cases where the
> return value is eventually consumed by a variable declared as precise:
>
> > - `fma()` is considered a single operation, whereas the expression `a * b + c` consumed by a variable declared as precise is considered two operations.
> > - The precision of `fma()` can differ from the precision of the expression `a * b + c`.
> > - `fma()` will be computed with the same precision as any other `fma()` consumed by a precise variable,
> >   giving invariant results for the same input values of a, b and c.
>
> Otherwise, in the absence of precise consumption, there are no special constraints on the number of operations
> or difference in precision between `fma()` and the expression `a * b + c`.
>
> param a:
> :   The first value to be multiplied.
>
> param b:
> :   The second value to be multiplied.
>
> param c:
> :   The value to be added to the result.
>
> return:
> :   The value of `a * b + c`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/fma.xhtml>

---


<a id="shader-func-step"></a>

vec_type **step**(vec_type a, vec_type b) [🔗](shader_functions.md#shader-func-step)

vec_type **step**(float a, vec_type b) [🔗](shader_functions.md#shader-func-step)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Generates a step function by comparing b to a.
>
> Equivalent to `if (b < a) { return 0.0; } else { return 1.0; }`.
> For element i of the return value, 0.0 is returned if b[i] < a[i], and 1.0 is returned otherwise.
>
> param a:
> :   The location of the edge of the step function.
>
> param b:
> :   The value to be used to generate the step function.
>
> return:
> :   `0.0` or `1.0`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/step.xhtml>

---


<a id="shader-func-smoothstep"></a>

vec_type **smoothstep**(vec_type a, vec_type b, vec_type c) [🔗](shader_functions.md#shader-func-smoothstep)

vec_type **smoothstep**(float a, float b, vec_type c) [🔗](shader_functions.md#shader-func-smoothstep)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Performs smooth Hermite interpolation between `0` and `1` when a < c < b.
> This is useful in cases where a threshold function with a smooth transition is desired.
>
> Smoothstep is equivalent to:
>
> ```gdscript
> vec_type t;
> t = clamp((c - a) / (b - a), 0.0, 1.0);
> return t * t * (3.0 - 2.0 * t);
> ```
>
> Results are undefined if `a >= b`.
>
> param a:
> :   The value of the lower edge of the Hermite function.
>
> param b:
> :   The value of the upper edge of the Hermite function.
>
> param c:
> :   The source value for interpolation.
>
> return:
> :   The interpolated value.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/smoothstep.xhtml>

---


<a id="shader-func-isnan"></a>

vec_bool_type **isnan**(vec_type x) [🔗](shader_functions.md#shader-func-isnan)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> For each element i of the result, returns `true` if x[i] is positive
> or negative floating-point NaN (Not a Number) and false otherwise.
>
> param x:
> :   The value to test for NaN.
>
> return:
> :   `true` or `false`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/isnan.xhtml>

---


<a id="shader-func-isinf"></a>

vec_bool_type **isinf**(vec_type x) [🔗](shader_functions.md#shader-func-isinf)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> For each element i of the result, returns `true` if x[i] is positive or negative
> floating-point infinity and false otherwise.
>
> param x:
> :   The value to test for infinity.
>
> return:
> :   `true` or `false`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/isinf.xhtml>

---


<a id="shader-func-floatbitstoint"></a>

vec_int_type **floatBitsToInt**(vec_type x) [🔗](shader_functions.md#shader-func-floatbitstoint)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Returns the encoding of the floating-point parameters as `int`.
>
> The floating-point bit-level representation is preserved.
>
> param x:
> :   The value whose floating-point encoding to return.
>
> return:
> :   The floating-point encoding of `x`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/floatBitsToInt.xhtml>

---


<a id="shader-func-floatbitstouint"></a>

vec_uint_type **floatBitsToUint**(vec_type x) [🔗](shader_functions.md#shader-func-floatbitstouint)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Returns the encoding of the floating-point parameters as `uint`.
>
> The floating-point bit-level representation is preserved.
>
> param x:
> :   The value whose floating-point encoding to return.
>
> return:
> :   The floating-point encoding of `x`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/floatBitsToInt.xhtml>

---


<a id="shader-func-intbitstofloat"></a>

vec_type **intBitsToFloat**(vec_int_type x) [🔗](shader_functions.md#shader-func-intbitstofloat)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Converts a bit encoding to a floating-point value. Opposite of floatBitsToInt<shader_func_floatBitsToInt>
>
> If the encoding of a `NaN` is passed in `x`, it will not signal and the resulting value will be undefined.
>
> If the encoding of a floating-point infinity is passed in parameter `x`, the resulting floating-point value is
> the corresponding (positive or negative) floating-point infinity.
>
> param x:
> :   The bit encoding to return as a floating-point value.
>
> return:
> :   A floating-point value.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/intBitsToFloat.xhtml>

---


<a id="shader-func-uintbitstofloat"></a>

vec_type **uintBitsToFloat**(vec_uint_type x) [🔗](shader_functions.md#shader-func-uintbitstofloat)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Converts a bit encoding to a floating-point value. Opposite of floatBitsToUint<shader_func_floatBitsToUint>
>
> If the encoding of a `NaN` is passed in `x`, it will not signal and the resulting value will be undefined.
>
> If the encoding of a floating-point infinity is passed in parameter `x`, the resulting floating-point value is
> the corresponding (positive or negative) floating-point infinity.
>
> param x:
> :   The bit encoding to return as a floating-point value.
>
> return:
> :   A floating-point value.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/intBitsToFloat.xhtml>

---


<a id="geometric-functions"></a>

## Geometric functions

|  |  |  |
| --- | --- | --- |
| float | [length](shader_functions.md#shader-func-length)(vec_type x) | Vector length. |
| float | [distance](shader_functions.md#shader-func-distance)(vec_type a, vec_type b) | Distance between vectors i.e `length(a - b)`. |
| float | [dot](shader_functions.md#shader-func-dot)(vec_type a, vec_type b) | Dot product. |
| vec3 | [cross](shader_functions.md#shader-func-cross)(vec3 a, vec3 b) | Cross product. |
| vec_type | [normalize](shader_functions.md#shader-func-normalize)(vec_type x) | Normalize to unit length. |
| vec3 | [reflect](shader_functions.md#shader-func-reflect)(vec3 I, vec3 N) | Reflect. |
| vec3 | [refract](shader_functions.md#shader-func-refract)(vec3 I, vec3 N, float eta) | Refract. |
| vec_type | [faceforward](shader_functions.md#shader-func-faceforward)(vec_type N, vec_type I, vec_type Nref) | If `dot(Nref, I) < 0`, returns `N`, otherwise `-N`. |
| mat_type | [matrixCompMult](shader_functions.md#shader-func-matrixcompmult)(mat_type x, mat_type y) | Matrix component multiplication. |
| mat_type | [outerProduct](shader_functions.md#shader-func-outerproduct)(vec_type column, vec_type row) | Matrix outer product. |
| mat_type | [transpose](shader_functions.md#shader-func-transpose)(mat_type m) | Transpose matrix. |
| float | [determinant](shader_functions.md#shader-func-determinant)(mat_type m) | Matrix determinant. |
| mat_type | [inverse](shader_functions.md#shader-func-inverse)(mat_type m) | Inverse matrix. |

<a id="geometric-function-descriptions"></a>

### Geometric function descriptions

<a id="shader-func-length"></a>

float **length**(vec_type x) [🔗](shader_functions.md#shader-func-length)

> Returns the length of the vector, i.e.,
> `sqrt(x[0] * x[0] + x[1] * x[1] + ... + x[n] * x[n])`
>
> param x:
> :   The vector
>
> return:
> :   The length of the vector.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/length.xhtml>

---


<a id="shader-func-distance"></a>

float **distance**(vec_type a, vec_type b) [🔗](shader_functions.md#shader-func-distance)

> Returns the distance between the two points `a` and `b`, i.e.,
> `length(b - a);`
>
> param a:
> :   The first point.
>
> param b:
> :   The second point.
>
> return:
> :   The scalar distance between the points
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/distance.xhtml>

---


<a id="shader-func-dot"></a>

float **dot**(vec_type a, vec_type b) [🔗](shader_functions.md#shader-func-dot)

> Returns the dot product of two vectors, `a` and `b`, i.e.,
> `a.x * b.x + a.y * b.y + ...`
>
> param a:
> :   The first vector.
>
> param b:
> :   The second vector.
>
> return:
> :   The dot product.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/dot.xhtml>

---


<a id="shader-func-cross"></a>

vec3 **cross**(vec3 a, vec3 b) [🔗](shader_functions.md#shader-func-cross)

> Returns the cross product of two vectors, i.e.:
>
> ```glsl
> vec3( a.y * b.z - b.y * a.z,
>       a.z * b.x - b.z * a.x,
>       a.x * b.y - b.x * a.y)
> ```
>
> param a:
> :   The first vector.
>
> param b:
> :   The second vector.
>
> return:
> :   The cross product of `a` and `b`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/cross.xhtml>

---


<a id="shader-func-normalize"></a>

vec_type **normalize**(vec_type x) [🔗](shader_functions.md#shader-func-normalize)

> Returns a vector with the same direction as `x` but with length `1.0`.
>
> param x:
> :   The vector to normalize.
>
> return:
> :   The normalized vector.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/normalize.xhtml>

---


<a id="shader-func-reflect"></a>

vec3 **reflect**(vec3 I, vec3 N) [🔗](shader_functions.md#shader-func-reflect)

> Calculate the reflection direction for an incident vector.
>
> For a given incident vector `I` and surface normal `N` reflect returns the reflection direction calculated as `I - 2.0 * dot(N, I) * N`.
>
> Note
>
> `N` should be normalized in order to achieve the desired result.
>
> param I:
> :   The incident vector.
>
> param N:
> :   The normal vector.
>
> return:
> :   The reflection vector.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/reflect.xhtml>

---


<a id="shader-func-refract"></a>

vec3 **refract**(vec3 I, vec3 N, float eta) [🔗](shader_functions.md#shader-func-refract)

> Calculate the refraction direction for an incident vector.
>
> For a given incident vector `I`, surface normal `N` and ratio of indices of refraction, `eta`, refract returns the refraction vector, `R`.
>
> `R` is calculated as:
>
> ```glsl
> k = 1.0 - eta * eta * (1.0 - dot(N, I) * dot(N, I));
> if (k < 0.0)
>     R = genType(0.0);       // or genDType(0.0)
> else
>     R = eta * I - (eta * dot(N, I) + sqrt(k)) * N;
> ```
>
> Note
>
> The input parameters I and N should be normalized in order to achieve the desired result.
>
> param I:
> :   The incident vector.
>
> param N:
> :   The normal vector.
>
> param eta:
> :   The ratio of indices of refraction.
>
> return:
> :   The refraction vector.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/refract.xhtml>

---


<a id="shader-func-faceforward"></a>

vec_type **faceforward**(vec_type N, vec_type I, vec_type Nref) [🔗](shader_functions.md#shader-func-faceforward)

> Returns a vector pointing in the same direction as another.
>
> Orients a vector to point away from a surface as defined by its normal.
> If `dot(Nref, I) < 0` faceforward returns `N`, otherwise it returns `-N`.
>
> param N:
> :   The vector to orient.
>
> param I:
> :   The incident vector.
>
> param Nref:
> :   The reference vector.
>
> return:
> :   The oriented vector.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/faceforward.xhtml>

---


<a id="shader-func-matrixcompmult"></a>

mat_type **matrixCompMult**(mat_type x, mat_type y) [🔗](shader_functions.md#shader-func-matrixcompmult)

> Perform a [component-wise](shader_functions.md#shading-componentwise) multiplication of two matrices.
>
> Performs a component-wise multiplication of two matrices, yielding a result
> matrix where each component, `result[i][j]` is computed as the scalar
> product of `x[i][j]` and `y[i][j]`.
>
> param x:
> :   The first matrix multiplicand.
>
> param y:
> :   The second matrix multiplicand.
>
> return:
> :   The resultant matrix.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/matrixCompMult.xhtml>

---


<a id="shader-func-outerproduct"></a>

mat_type **outerProduct**(vec_type column, vec_type row) [🔗](shader_functions.md#shader-func-outerproduct)

> Calculate the outer product of a pair of vectors.
>
> Does a linear algebraic matrix multiply `column * row`, yielding a matrix whose number of
> rows is the number of components in `column` and whose number of columns is the number of
> components in `row`.
>
> param column:
> :   The column vector for multiplication.
>
> param row:
> :   The row vector for multiplication.
>
> return:
> :   The outer product matrix.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/outerProduct.xhtml>

---


<a id="shader-func-transpose"></a>

mat_type **transpose**(mat_type m) [🔗](shader_functions.md#shader-func-transpose)

> Calculate the transpose of a matrix.
>
> param m:
> :   The matrix to transpose.
>
> return:
> :   A new matrix that is the transpose of the input matrix `m`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/transpose.xhtml>

---


<a id="shader-func-determinant"></a>

float **determinant**(mat_type m) [🔗](shader_functions.md#shader-func-determinant)

> Calculate the determinant of a matrix.
>
> param m:
> :   The matrix.
>
> return:
> :   The determinant of the input matrix `m`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/determinant.xhtml>

---


<a id="shader-func-inverse"></a>

mat_type **inverse**(mat_type m) [🔗](shader_functions.md#shader-func-inverse)

> Calculate the inverse of a matrix.
>
> The values in the returned matrix are undefined if `m` is singular or poorly-conditioned (nearly singular).
>
> param m:
> :   The matrix of which to take the inverse.
>
> return:
> :   A new matrix which is the inverse of the input matrix `m`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/inverse.xhtml>

---


<a id="comparison-functions"></a>

## Comparison functions

|  |  |  |
| --- | --- | --- |
| vec_bool_type | [lessThan](shader_functions.md#shader-func-lessthan)(vec_type x, vec_type y) | Bool vector comparison on < int/uint/float vectors. |
| vec_bool_type | [greaterThan](shader_functions.md#shader-func-greaterthan)(vec_type x, vec_type y) | Bool vector comparison on > int/uint/float vectors. |
| vec_bool_type | [lessThanEqual](shader_functions.md#shader-func-lessthanequal)(vec_type x, vec_type y) | Bool vector comparison on <= int/uint/float vectors. |
| vec_bool_type | [greaterThanEqual](shader_functions.md#shader-func-greaterthanequal)( vec_type x, vec_type y) | Bool vector comparison on >= int/uint/float vectors. |
| vec_bool_type | [equal](shader_functions.md#shader-func-equal)(vec_type x, vec_type y) | Bool vector comparison on == int/uint/float vectors. |
| vec_bool_type | [notEqual](shader_functions.md#shader-func-notequal)(vec_type x, vec_type y) | Bool vector comparison on != int/uint/float vectors. |
| bool | [any](shader_functions.md#shader-func-any)(vec_bool_type x) | `true` if any component is `true`, `false` otherwise. |
| bool | [all](shader_functions.md#shader-func-all)(vec_bool_type x) | `true` if all components are `true`, `false` otherwise. |
| vec_bool_type | [not](shader_functions.md#shader-func-not)(vec_bool_type x) | Invert boolean vector. |

<a id="comparison-function-descriptions"></a>

### Comparison function descriptions

<a id="shader-func-lessthan"></a>

vec_bool_type **lessThan**(vec_type x, vec_type y) [🔗](shader_functions.md#shader-func-lessthan)

> Performs a [component-wise](shader_functions.md#shading-componentwise) less-than comparison of two vectors.
>
> param x:
> :   The first vector to compare.
>
> param y:
> :   The second vector to compare.
>
> return:
> :   A boolean vector in which each element `i` is computed as `x[i] < y[i]`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/lessThan.xhtml>

---


<a id="shader-func-greaterthan"></a>

vec_bool_type **greaterThan**(vec_type x, vec_type y) [🔗](shader_functions.md#shader-func-greaterthan)

> Performs a [component-wise](shader_functions.md#shading-componentwise) greater-than comparison of two vectors.
>
> param x:
> :   The first vector to compare.
>
> param y:
> :   The second vector to compare.
>
> return:
> :   A boolean vector in which each element `i` is computed as `x[i] > y[i]`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/greaterThan.xhtml>

---


<a id="shader-func-lessthanequal"></a>

vec_bool_type **lessThanEqual**(vec_type x, vec_type y) [🔗](shader_functions.md#shader-func-lessthanequal)

> Performs a [component-wise](shader_functions.md#shading-componentwise) less-than-or-equal comparison of two vectors.
>
> param x:
> :   The first vector to compare.
>
> param y:
> :   The second vector to compare.
>
> return:
> :   A boolean vector in which each element `i` is computed as `x[i] <= y[i]`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/lessThanEqual.xhtml>

---


<a id="shader-func-greaterthanequal"></a>

vec_bool_type **greaterThanEqual**(vec_type x, vec_type y) [🔗](shader_functions.md#shader-func-greaterthanequal)

> Performs a [component-wise](shader_functions.md#shading-componentwise) greater-than-or-equal comparison of two vectors.
>
> param x:
> :   The first vector to compare.
>
> param y:
> :   The second vector to compare.
>
> return:
> :   A boolean vector in which each element `i` is computed as `x[i] >= y[i]`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/greaterThanEqual.xhtml>

---


<a id="shader-func-equal"></a>

vec_bool_type **equal**(vec_type x, vec_type y) [🔗](shader_functions.md#shader-func-equal)

> Performs a [component-wise](shader_functions.md#shading-componentwise) equal-to comparison of two vectors.
>
> param x:
> :   The first vector to compare.
>
> param y:
> :   The second vector to compare.
>
> return:
> :   A boolean vector in which each element `i` is computed as `x[i] == y[i]`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/equal.xhtml>

---


<a id="shader-func-notequal"></a>

vec_bool_type **notEqual**(vec_type x, vec_type y) [🔗](shader_functions.md#shader-func-notequal)

> Performs a [component-wise](shader_functions.md#shading-componentwise) not-equal-to comparison of two vectors.
>
> param x:
> :   The first vector for comparison.
>
> param y:
> :   The second vector for comparison.
>
> return:
> :   A boolean vector in which each element `i` is computed as `x[i] != y[i]`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/notEqual.xhtml>

---


<a id="shader-func-any"></a>

bool **any**(vec_bool_type x) [🔗](shader_functions.md#shader-func-any)

> Returns `true` if any element of a boolean vector is `true`, `false` otherwise.
>
> Functionally equivalent to:
>
> ```gdscript
> bool any(bvec x) {     // bvec can be bvec2, bvec3 or bvec4
>     bool result = false;
>     int i;
>     for (i = 0; i < x.length(); ++i) {
>         result |= x[i];
>     }
>     return result;
> }
> ```
>
> param x:
> :   The vector to be tested for truth.
>
> return:
> :   `true` if any element of `x` is `true` and `false` otherwise.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/any.xhtml>

---


<a id="shader-func-all"></a>

bool **all**(vec_bool_type x) [🔗](shader_functions.md#shader-func-all)

> Returns `true` if all elements of a boolean vector are `true`, `false` otherwise.
>
> Functionally equivalent to:
>
> ```gdscript
> bool all(bvec x)       // bvec can be bvec2, bvec3 or bvec4
> {
>     bool result = true;
>     int i;
>     for (i = 0; i < x.length(); ++i)
>     {
>         result &= x[i];
>     }
>     return result;
> }
> ```
>
> param x:
> :   The vector to be tested for truth.
>
> return:
> :   `true` if all elements of `x` are `true` and `false` otherwise.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/all.xhtml>

---


<a id="shader-func-not"></a>

vec_bool_type **not**(vec_bool_type x) [🔗](shader_functions.md#shader-func-not)

> Logically invert a boolean vector.
>
> param x:
> :   The vector to be inverted.
>
> return:
> :   A new boolean vector for which each element i is computed as !x[i].
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/not.xhtml>

---


<a id="texture-functions"></a>

## Texture functions

|  |  |  |
| --- | --- | --- |
| ivec2  ivec2  ivec2  ivec3  ivec3 | [textureSize](shader_functions.md#shader-func-texturesize)(gsampler2D s, int lod)  [textureSize](shader_functions.md#shader-func-texturesize)(samplerCube s, int lod)  [textureSize](shader_functions.md#shader-func-texturesize)(samplerCubeArray s, int lod)  [textureSize](shader_functions.md#shader-func-texturesize)(gsampler2DArray s, int lod)  [textureSize](shader_functions.md#shader-func-texturesize)(gsampler3D s, int lod) | Get the size of a texture.  For performance reasons, this function should be avoided as it always performs a full texture read. When possible, you should pass the texture size as a uniform instead. |
| vec2  vec3  vec2  vec2 | [textureQueryLod](shader_functions.md#shader-func-texturequerylod)(gsampler2D s, vec2 p)  [textureQueryLod](shader_functions.md#shader-func-texturequerylod)(gsampler2DArray s, vec2 p)  [textureQueryLod](shader_functions.md#shader-func-texturequerylod)(gsampler3D s, vec3 p)  [textureQueryLod](shader_functions.md#shader-func-texturequerylod)(samplerCube s, vec3 p) | Compute the level-of-detail that would be used to sample from a texture. |
| int  int  int  int | [textureQueryLevels](shader_functions.md#shader-func-texturequerylevels)(gsampler2D s)  [textureQueryLevels](shader_functions.md#shader-func-texturequerylevels)(gsampler2DArray s)  [textureQueryLevels](shader_functions.md#shader-func-texturequerylevels)(gsampler3D s)  [textureQueryLevels](shader_functions.md#shader-func-texturequerylevels)(samplerCube s) | Get the number of accessible mipmap levels of a texture. |
| gvec4_type  gvec4_type  gvec4_type  vec4  vec4  vec4 | [texture](shader_functions.md#shader-func-texture)(gsampler2D s, vec2 p [, float bias] )  [texture](shader_functions.md#shader-func-texture)(gsampler2DArray s, vec3 p [, float bias] )  [texture](shader_functions.md#shader-func-texture)(gsampler3D s, vec3 p [, float bias] )  [texture](shader_functions.md#shader-func-texture)(samplerCube s, vec3 p [, float bias] )  [texture](shader_functions.md#shader-func-texture)(samplerCubeArray s, vec4 p [, float bias] )  [texture](shader_functions.md#shader-func-texture)(samplerExternalOES s, vec2 p [, float bias] ) | Performs a texture read. |
| gvec4_type  gvec4_type  gvec4_type | [textureProj](shader_functions.md#shader-func-textureproj)(gsampler2D s, vec3 p [, float bias] )  [textureProj](shader_functions.md#shader-func-textureproj)(gsampler2D s, vec4 p [, float bias] )  [textureProj](shader_functions.md#shader-func-textureproj)(gsampler3D s, vec4 p [, float bias] ) | Performs a texture read with projection. |
| gvec4_type  gvec4_type  gvec4_type  vec4  vec4 | [textureLod](shader_functions.md#shader-func-texturelod)(gsampler2D s, vec2 p, float lod)  [textureLod](shader_functions.md#shader-func-texturelod)(gsampler2DArray s, vec3 p, float lod)  [textureLod](shader_functions.md#shader-func-texturelod)(gsampler3D s, vec3 p, float lod)  [textureLod](shader_functions.md#shader-func-texturelod)(samplerCube s, vec3 p, float lod)  [textureLod](shader_functions.md#shader-func-texturelod)(samplerCubeArray s, vec4 p, float lod) | Performs a texture read at custom mipmap. |
| gvec4_type  gvec4_type  gvec4_type | [textureProjLod](shader_functions.md#shader-func-textureprojlod)(gsampler2D s, vec3 p, float lod)  [textureProjLod](shader_functions.md#shader-func-textureprojlod)(gsampler2D s, vec4 p, float lod)  [textureProjLod](shader_functions.md#shader-func-textureprojlod)(gsampler3D s, vec4 p, float lod) | Performs a texture read with projection/LOD. |
| gvec4_type  gvec4_type  gvec4_type  vec4  vec4 | [textureGrad](shader_functions.md#shader-func-texturegrad)(gsampler2D s, vec2 p, vec2 dPdx, vec2 dPdy)  [textureGrad](shader_functions.md#shader-func-texturegrad)(gsampler2DArray s, vec3 p, vec2 dPdx, vec2 dPdy)  [textureGrad](shader_functions.md#shader-func-texturegrad)(gsampler3D s, vec3 p, vec2 dPdx, vec2 dPdy)  [textureGrad](shader_functions.md#shader-func-texturegrad)(samplerCube s, vec3 p, vec3 dPdx, vec3 dPdy)  [textureGrad](shader_functions.md#shader-func-texturegrad)(samplerCubeArray s, vec3 p, vec3 dPdx, vec3 dPdy) | Performs a texture read with explicit gradients. |
| gvec4_type  gvec4_type  gvec4_type | [textureProjGrad](shader_functions.md#shader-func-textureprojgrad)(gsampler2D s, vec3 p, vec2 dPdx, vec2 dPdy)  [textureProjGrad](shader_functions.md#shader-func-textureprojgrad)(gsampler2D s, vec4 p, vec2 dPdx, vec2 dPdy)  [textureProjGrad](shader_functions.md#shader-func-textureprojgrad)(gsampler3D s, vec4 p, vec3 dPdx, vec3 dPdy) | Performs a texture read with projection/LOD and with explicit |
| gvec4_type  gvec4_type  gvec4_type | [texelFetch](shader_functions.md#shader-func-texelfetch)(gsampler2D s, ivec2 p, int lod)  [texelFetch](shader_functions.md#shader-func-texelfetch)(gsampler2DArray s, ivec3 p, int lod)  [texelFetch](shader_functions.md#shader-func-texelfetch)(gsampler3D s, ivec3 p, int lod) | Fetches a single texel using integer coordinates. |
| gvec4_type  gvec4_type  vec4 | [textureGather](shader_functions.md#shader-func-texturegather)(gsampler2D s, vec2 p [, int comps] )  [textureGather](shader_functions.md#shader-func-texturegather)(gsampler2DArray s, vec3 p [, int comps] )  [textureGather](shader_functions.md#shader-func-texturegather)(samplerCube s, vec3 p [, int comps] ) | Gathers four texels from a texture. |
| vec_type | [dFdx](shader_functions.md#shader-func-dfdx)(vec_type p) | Derivative with respect to `x` window coordinate, automatic granularity. |
| vec_type | [dFdxCoarse](shader_functions.md#shader-func-dfdxcoarse)(vec_type p) | Derivative with respect to `x` window coordinate, course granularity.  Not available when using the Compatibility renderer. |
| vec_type | [dFdxFine](shader_functions.md#shader-func-dfdxfine)(vec_type p) | Derivative with respect to `x` window coordinate, fine granularity.  Not available when using the Compatibility renderer. |
| vec_type | [dFdy](shader_functions.md#shader-func-dfdy)(vec_type p) | Derivative with respect to `y` window coordinate, automatic granularity. |
| vec_type | [dFdyCoarse](shader_functions.md#shader-func-dfdycoarse)(vec_type p) | Derivative with respect to `y` window coordinate, course granularity.  Not available when using the Compatibility renderer. |
| vec_type | [dFdyFine](shader_functions.md#shader-func-dfdyfine)(vec_type p) | Derivative with respect to `y` window coordinate, fine granularity.  Not available when using the Compatibility renderer. |
| vec_type | [fwidth](shader_functions.md#shader-func-fwidth)(vec_type p) | Sum of absolute derivative in `x` and `y`. |
| vec_type | [fwidthCoarse](shader_functions.md#shader-func-fwidthcoarse)(vec_type p) | Sum of absolute derivative in `x` and `y`.  Not available when using the Compatibility renderer. |
| vec_type | [fwidthFine](shader_functions.md#shader-func-fwidthfine)(vec_type p) | Sum of absolute derivative in `x` and `y`.  Not available when using the Compatibility renderer. |

<a id="texture-function-descriptions"></a>

### Texture function descriptions

<a id="shader-func-texturesize"></a>

ivec2 **textureSize**(gsampler2D s, int lod) [🔗](shader_functions.md#shader-func-texturesize)

ivec2 **textureSize**(samplerCube s, int lod) [🔗](shader_functions.md#shader-func-texturesize)

ivec2 **textureSize**(samplerCubeArray s, int lod) [🔗](shader_functions.md#shader-func-texturesize)

ivec3 **textureSize**(gsampler2DArray s, int lod) [🔗](shader_functions.md#shader-func-texturesize)

ivec3 **textureSize**(gsampler3D s, int lod) [🔗](shader_functions.md#shader-func-texturesize)

> Retrieves the dimensions of a level of a texture.
>
> Returns the dimensions of level `lod` (if present) of the texture bound to sampler.
>
> The components in the return value are filled in, in order, with the width, height and depth
> of the texture. For the array forms, the last component of the return value is
> the number of layers in the texture array.
>
> param s:
> :   The sampler to which the texture whose dimensions to retrieve is bound.
>
> param lod:
> :   The level of the texture for which to retrieve the dimensions.
>
> return:
> :   The dimensions of level `lod` (if present) of the texture bound to sampler.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureSize.xhtml>

---


<a id="shader-func-texturequerylod"></a>

vec2 **textureQueryLod**(gsampler2D s, vec2 p) [🔗](shader_functions.md#shader-func-texturequerylod)

vec2 **textureQueryLod**(gsampler2DArray s, vec2 p) [🔗](shader_functions.md#shader-func-texturequerylod)

vec2 **textureQueryLod**(gsampler3D s, vec3 p) [🔗](shader_functions.md#shader-func-texturequerylod)

vec2 **textureQueryLod**(samplerCube s, vec3 p) [🔗](shader_functions.md#shader-func-texturequerylod)

> Note
>
> Available only in the fragment shader.
>
> Compute the level-of-detail that would be used to sample from a texture.
>
> The mipmap array(s) that would be accessed is returned in the x component of
> the return value. The computed level-of-detail relative to the base level is
> returned in the y component of the return value.
>
> If called on an incomplete texture, the result of the operation is undefined.
>
> param s:
> :   The sampler to which the texture whose level-of-detail will be queried is bound.
>
> param p:
> :   The texture coordinates at which the level-of-detail will be queried.
>
> return:
> :   See description.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureQueryLod.xhtml>

---


<a id="shader-func-texturequerylevels"></a>

int **textureQueryLevels**(gsampler2D s) [🔗](shader_functions.md#shader-func-texturequerylevels)

int **textureQueryLevels**(gsampler2DArray s) [🔗](shader_functions.md#shader-func-texturequerylevels)

int **textureQueryLevels**(gsampler3D s) [🔗](shader_functions.md#shader-func-texturequerylevels)

int **textureQueryLevels**(samplerCube s) [🔗](shader_functions.md#shader-func-texturequerylevels)

> Compute the number of accessible mipmap levels of a texture.
>
> If called on an incomplete texture, or if no texture is associated with sampler, `0` is returned.
>
> param s:
> :   The sampler to which the texture whose mipmap level count will be queried is bound.
>
> return:
> :   The number of accessible mipmap levels in the texture, or `0`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureQueryLevels.xhtml>

---


<a id="shader-func-texture"></a>

gvec4_type **texture**(gsampler2D s, vec2 p [, float bias] ) [🔗](shader_functions.md#shader-func-texture)

gvec4_type **texture**(gsampler2DArray s, vec3 p [, float bias] ) [🔗](shader_functions.md#shader-func-texture)

gvec4_type **texture**(gsampler3D s, vec3 p [, float bias] ) [🔗](shader_functions.md#shader-func-texture)

vec4 **texture**(samplerCube s, vec3 p [, float bias] ) [🔗](shader_functions.md#shader-func-texture)

vec4 **texture**(samplerCubeArray s, vec4 p [, float bias] ) [🔗](shader_functions.md#shader-func-texture)

vec4 **texture**(samplerExternalOES s, vec2 p [, float bias] ) [🔗](shader_functions.md#shader-func-texture)

> Retrieves texels from a texture.
>
> Samples texels from the texture bound to `s` at texture coordinate `p`. An optional bias, specified in `bias` is
> included in the level-of-detail computation that is used to choose mipmap(s) from which to sample.
>
> For shadow forms, the last component of `p` is used as Dsub and the array layer is specified in the second to last
> component of `p`. (The second component of `p` is unused for 1D shadow lookups.)
>
> For non-shadow variants, the array layer comes from the last component of P.
>
> param s:
> :   The sampler to which the texture from which texels will be retrieved is bound.
>
> param p:
> :   The texture coordinates at which texture will be sampled.
>
> param bias:
> :   An optional bias to be applied during level-of-detail computation.
>
> return:
> :   A texel.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/texture.xhtml>

---


<a id="shader-func-textureproj"></a>

gvec4_type **textureProj**(gsampler2D s, vec3 p [, float bias] ) [🔗](shader_functions.md#shader-func-textureproj)

gvec4_type **textureProj**(gsampler2D s, vec4 p [, float bias] ) [🔗](shader_functions.md#shader-func-textureproj)

gvec4_type **textureProj**(gsampler3D s, vec4 p [, float bias] ) [🔗](shader_functions.md#shader-func-textureproj)

> Perform a texture lookup with projection.
>
> The texture coordinates consumed from `p`, not including the last component of `p`, are
> divided by the last component of `p`. The resulting 3rd component of `p` in the shadow
> forms is used as Dref. After these values are computed, the texture lookup proceeds as in texture.
>
> param s:
> :   The sampler to which the texture from which texels will be retrieved is bound.
>
> param p:
> :   The texture coordinates at which texture will be sampled.
>
> param bias:
> :   Optional bias to be applied during level-of-detail computation.
>
> return:
> :   A texel.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureProj.xhtml>

---


<a id="shader-func-texturelod"></a>

gvec4_type **textureLod**(gsampler2D s, vec2 p, float lod) [🔗](shader_functions.md#shader-func-texturelod)

gvec4_type **textureLod**(gsampler2DArray s, vec3 p, float lod) [🔗](shader_functions.md#shader-func-texturelod)

gvec4_type **textureLod**(gsampler3D s, vec3 p, float lod) [🔗](shader_functions.md#shader-func-texturelod)

vec4 **textureLod**(samplerCube s, vec3 p, float lod) [🔗](shader_functions.md#shader-func-texturelod)

vec4 **textureLod**(samplerCubeArray s, vec4 p, float lod) [🔗](shader_functions.md#shader-func-texturelod)

> Performs a texture lookup at coordinate `p` from the texture bound to sampler with
> an explicit level-of-detail as specified in `lod`. `lod` specifies λbase and sets the
> partial derivatives as follows:
>
> ```gdscript
> δu/δx=0, δv/δx=0, δw/δx=0
> δu/δy=0, δv/δy=0, δw/δy=0
> ```
>
> param s:
> :   The sampler to which the texture from which texels will be retrieved is bound.
>
> param p:
> :   The texture coordinates at which texture will be sampled.
>
> param lod:
> :   The explicit level-of-detail.
>
> return:
> :   A texel.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureLod.xhtml>

---


<a id="shader-func-textureprojlod"></a>

gvec4_type **textureProjLod**(gsampler2D s, vec3 p, float lod) [🔗](shader_functions.md#shader-func-textureprojlod)

gvec4_type **textureProjLod**(gsampler2D s, vec4 p, float lod) [🔗](shader_functions.md#shader-func-textureprojlod)

gvec4_type **textureProjLod**(gsampler3D s, vec4 p, float lod) [🔗](shader_functions.md#shader-func-textureprojlod)

> Performs a texture lookup with projection from an explicitly specified level-of-detail.
>
> The texture coordinates consumed from P, not including the last component of `p`, are
> divided by the last component of `p`. The resulting 3rd component of `p` in the shadow
> forms is used as Dref. After these values are computed, the texture lookup proceeds as in
> textureLod<shader_func_textureLod>, with `lod` used to specify the level-of-detail from
> which the texture will be sampled.
>
> param s:
> :   The sampler to which the texture from which texels will be retrieved is bound.
>
> param p:
> :   The texture coordinates at which texture will be sampled.
>
> param lod:
> :   The explicit level-of-detail from which to fetch texels.
>
> return:
> :   a texel
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureProjLod.xhtml>

---


<a id="shader-func-texturegrad"></a>

gvec4_type **textureGrad**(gsampler2D s, vec2 p, vec2 dPdx, vec2 dPdy) [🔗](shader_functions.md#shader-func-texturegrad)

gvec4_type **textureGrad**(gsampler2DArray s, vec3 p, vec2 dPdx, vec2 dPdy) [🔗](shader_functions.md#shader-func-texturegrad)

gvec4_type **textureGrad**(gsampler3D s, vec3 p, vec2 dPdx, vec2 dPdy) [🔗](shader_functions.md#shader-func-texturegrad)

vec4 **textureGrad**(samplerCube s, vec3 p, vec3 dPdx, vec3 dPdy) [🔗](shader_functions.md#shader-func-texturegrad)

vec4 **textureGrad**(samplerCubeArray s, vec3 p, vec3 dPdx, vec3 dPdy) [🔗](shader_functions.md#shader-func-texturegrad)

> Performs a texture lookup at coordinate `p` from the texture bound to sampler with explicit texture coordinate gradients as specified in `dPdx` and `dPdy`. Set:
> :   - `δs/δx=δp/δx` for a 1D texture, `δp.s/δx` otherwise
>     - `δs/δy=δp/δy` for a 1D texture, `δp.s/δy` otherwise
>     - `δt/δx=0.0` for a 1D texture, `δp.t/δx` otherwise
>     - `δt/δy=0.0` for a 1D texture, `δp.t/δy` otherwise
>     - `δr/δx=0.0` for a 1D or 2D texture, `δp.p/δx` otherwise
>     - `δr/δy=0.0` for a 1D or 2D texture, `δp.p/δy` otherwise
>
> For the cube version, the partial derivatives of `p` are assumed to be in the coordinate system used before texture coordinates are projected onto the appropriate cube face.
>
> param s:
> :   The sampler to which the texture from which texels will be retrieved is bound.
>
> param p:
> :   The texture coordinates at which texture will be sampled.
>
> param dPdx:
> :   The partial derivative of P with respect to window x.
>
> param dPdy:
> :   The partial derivative of P with respect to window y.
>
> return:
> :   A texel.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureGrad.xhtml>

---


<a id="shader-func-textureprojgrad"></a>

gvec4_type **textureProjGrad**(gsampler2D s, vec3 p, vec2 dPdx, vec2 dPdy) [🔗](shader_functions.md#shader-func-textureprojgrad)

gvec4_type **textureProjGrad**(gsampler2D s, vec4 p, vec2 dPdx, vec2 dPdy) [🔗](shader_functions.md#shader-func-textureprojgrad)

gvec4_type **textureProjGrad**(gsampler3D s, vec4 p, vec3 dPdx, vec3 dPdy) [🔗](shader_functions.md#shader-func-textureprojgrad)

> Perform a texture lookup with projection and explicit gradients.
>
> The texture coordinates consumed from `p`, not including the last component of `p`, are divided by the last component of `p`.
> After these values are computed, the texture lookup proceeds as in textureGrad<shader_func_textureGrad>, passing `dPdx` and `dPdy` as gradients.
>
> param s:
> :   The sampler to which the texture from which texels will be retrieved is bound.
>
> param p:
> :   The texture coordinates at which texture will be sampled.
>
> param dPdx:
> :   The partial derivative of `p` with respect to window x.
>
> param dPdy:
> :   The partial derivative of `p` with respect to window y.
>
> return:
> :   A texel.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureProjGrad.xhtml>

---


<a id="shader-func-texelfetch"></a>

gvec4_type **texelFetch**(gsampler2D s, ivec2 p, int lod) [🔗](shader_functions.md#shader-func-texelfetch)

gvec4_type **texelFetch**(gsampler2DArray s, ivec3 p, int lod) [🔗](shader_functions.md#shader-func-texelfetch)

gvec4_type **texelFetch**(gsampler3D s, ivec3 p, int lod) [🔗](shader_functions.md#shader-func-texelfetch)

> Performs a lookup of a single texel from texture coordinate `p` in the texture bound to sampler.
>
> param s:
> :   The sampler to which the texture from which texels will be retrieved is bound.
>
> param p:
> :   The texture coordinates at which texture will be sampled.
>
> param lod:
> :   Specifies the level-of-detail within the texture from which the texel will be fetched.
>
> return:
> :   A texel.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/texelFetch.xhtml>

---


<a id="shader-func-texturegather"></a>

gvec4_type **textureGather**(gsampler2D s, vec2 p [, int comps] ) [🔗](shader_functions.md#shader-func-texturegather)

gvec4_type **textureGather**(gsampler2DArray s, vec3 p [, int comps] ) [🔗](shader_functions.md#shader-func-texturegather)

vec4 **textureGather**(samplerCube s, vec3 p [, int comps] ) [🔗](shader_functions.md#shader-func-texturegather)

> Gathers four texels from a texture.
>
> Returns the value:
>
> ```gdscript
> vec4(Sample_i0_j1(p, base).comps,
>      Sample_i1_j1(p, base).comps,
>      Sample_i1_j0(p, base).comps,
>      Sample_i0_j0(p, base).comps);
> ```
>
> param s:
> :   The sampler to which the texture from which texels will be retrieved is bound.
>
> param p:
> :   The texture coordinates at which texture will be sampled.
>
> param comps:
> :   *optional* the component of the source texture (0 -> x, 1 -> y, 2 -> z, 3 -> w) that will be used to generate the resulting vector. Zero if not specified.
>
> return:
> :   The gathered texel.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureGather.xhtml>

---


<a id="shader-func-dfdx"></a>

vec_type **dFdx**(vec_type p) [🔗](shader_functions.md#shader-func-dfdx)

> Note
>
> Available only in the fragment shader.
>
> Returns the partial derivative of `p` with respect to the window x coordinate using local differencing.
>
> Returns either [dFdxCoarse](shader_functions.md#shader-func-dfdxcoarse) or [dFdxFine](shader_functions.md#shader-func-dfdxfine).
> The implementation may choose which calculation to perform based upon factors
> such as performance or the value of the API `GL_FRAGMENT_SHADER_DERIVATIVE_HINT` hint.
>
> Warning
>
> Expressions that imply higher order derivatives such as `dFdx(dFdx(n))`
> have undefined results, as do mixed-order derivatives such as `dFdx(dFdy(n))`.
>
> param p:
> :   The expression of which to take the partial derivative.
>
>     Note
>
>     It is assumed that the expression `p` is continuous and therefore expressions evaluated via non-uniform control flow may be undefined.
>
> return:
> :   The partial derivative of `p`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/dFdx.xhtml>

---


<a id="shader-func-dfdxcoarse"></a>

vec_type **dFdxCoarse**(vec_type p) [🔗](shader_functions.md#shader-func-dfdxcoarse)

> Note
>
> Available only in the fragment shader.
> Not available when using the Compatibility renderer.
>
> Returns the partial derivative of `p` with respect to the window x coordinate.
>
> Calculates derivatives using local differencing based on the value of `p`
> for the current fragment's neighbors, and will possibly, but not necessarily,
> include the value for the current fragment. That is, over a given area, the
> implementation can compute derivatives in fewer unique locations than would
> be allowed for the corresponding [dFdxFine](shader_functions.md#shader-func-dfdxfine) function.
>
> Warning
>
> Expressions that imply higher order derivatives such as `dFdx(dFdx(n))`
> have undefined results, as do mixed-order derivatives such as `dFdx(dFdy(n))`.
>
> param p:
> :   The expression of which to take the partial derivative.
>
>     Note
>
>     It is assumed that the expression `p` is continuous and therefore
>     expressions evaluated via non-uniform control flow may be undefined.
>
> return:
> :   The partial derivative of `p`.
>
> <https://registry.khronos.org/OpenGL-Refpages/gl4/html/dFdx.xhtml>

---


<a id="shader-func-dfdxfine"></a>

vec_type **dFdxFine**(vec_type p) [🔗](shader_functions.md#shader-func-dfdxfine)

> Note
>
> Available only in the fragment shader.
> Not available when using the Compatibility renderer.
>
> Returns the partial derivative of `p` with respect to the window x coordinate.
>
> Calculates derivatives using local differencing based on the value of `p` for the current fragment and its immediate neighbor(s).
>
> Warning
>
> Expressions that imply higher order derivatives such as `dFdx(dFdx(n))`
> have undefined results, as do mixed-order derivatives such as `dFdx(dFdy(n))`.
>
> param p:
> :   The expression of which to take the partial derivative.
>
>     Note
>
>     It is assumed that the expression `p` is continuous and therefore expressions evaluated via non-uniform control flow may be undefined.
>
> return:
> :   The partial derivative of `p`.
>
> <https://registry.khronos.org/OpenGL-Refpages/gl4/html/dFdx.xhtml>

---


<a id="shader-func-dfdy"></a>

vec_type **dFdy**(vec_type p) [🔗](shader_functions.md#shader-func-dfdy)

> Note
>
> Available only in the fragment shader.
>
> Returns the partial derivative of `p` with respect to the window y coordinate using local differencing.
>
> Returns either [dFdyCoarse](shader_functions.md#shader-func-dfdycoarse) or [dFdyFine](shader_functions.md#shader-func-dfdyfine).
> The implementation may choose which calculation to perform based upon factors
> such as performance or the value of the API `GL_FRAGMENT_SHADER_DERIVATIVE_HINT` hint.
>
> Warning
>
> Expressions that imply higher order derivatives such as `dFdx(dFdx(n))`
> have undefined results, as do mixed-order derivatives such as `dFdx(dFdy(n))`.
>
> param p:
> :   The expression of which to take the partial derivative.
>
>     Note
>
>     It is assumed that the expression `p` is continuous and therefore expressions evaluated via non-uniform control flow may be undefined.
>
> return:
> :   The partial derivative of `p`.
>
> <https://registry.khronos.org/OpenGL-Refpages/gl4/html/dFdx.xhtml>

---


<a id="shader-func-dfdycoarse"></a>

vec_type **dFdyCoarse**(vec_type p) [🔗](shader_functions.md#shader-func-dfdycoarse)

> Note
>
> Available only in the fragment shader.
> Not available when using the Compatibility renderer.
>
> Returns the partial derivative of `p` with respect to the window y coordinate.
>
> Calculates derivatives using local differencing based on the value of `p` for the current fragment's neighbors, and will possibly,
> but not necessarily, include the value for the current fragment. That is, over a given area, the implementation can compute derivatives in fewer unique locations than
> would be allowed for the corresponding dFdyFine and dFdyFine functions.
>
> Warning
>
> Expressions that imply higher order derivatives such as `dFdx(dFdx(n))` have undefined results, as do mixed-order derivatives such as `dFdx(dFdy(n))`.
>
> param p:
> :   The expression of which to take the partial derivative.
>
>     Note
>
>     It is assumed that the expression `p` is continuous and therefore expressions evaluated via non-uniform control flow may be undefined.
>
> return:
> :   The partial derivative of `p`.
>
> <https://registry.khronos.org/OpenGL-Refpages/gl4/html/dFdx.xhtml>

---


<a id="shader-func-dfdyfine"></a>

vec_type **dFdyFine**(vec_type p) [🔗](shader_functions.md#shader-func-dfdyfine)

> Note
>
> Available only in the fragment shader.
> Not available when using the Compatibility renderer.
>
> Returns the partial derivative of `p` with respect to the window y coordinate.
>
> Calculates derivatives using local differencing based on the value of `p` for the current fragment and its immediate neighbor(s).
>
> Warning
>
> Expressions that imply higher order derivatives such as `dFdx(dFdx(n))` have undefined results, as do mixed-order derivatives such as `dFdx(dFdy(n))`.
>
> param p:
> :   The expression of which to take the partial derivative.
>
>     Note
>
>     It is assumed that the expression `p` is continuous and therefore expressions evaluated via non-uniform control flow may be undefined.
>
> return:
> :   The partial derivative of `p`.
>
> <https://registry.khronos.org/OpenGL-Refpages/gl4/html/dFdx.xhtml>

---


<a id="shader-func-fwidth"></a>

vec_type **fwidth**(vec_type p) [🔗](shader_functions.md#shader-func-fwidth)

> Returns the sum of the absolute value of derivatives in x and y.
>
> Uses local differencing for the input argument `p`.
>
> Equivalent to `abs(dFdx(p)) + abs(dFdy(p))`.
>
> param p:
> :   The expression of which to take the partial derivative.
>
> return:
> :   The partial derivative.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/fwidth.xhtml>

---


<a id="shader-func-fwidthcoarse"></a>

vec_type **fwidthCoarse**(vec_type p) [🔗](shader_functions.md#shader-func-fwidthcoarse)

> Note
>
> Available only in the fragment shader.
> Not available when using the Compatibility renderer.
>
> Returns the sum of the absolute value of derivatives in x and y.
>
> Uses local differencing for the input argument p.
>
> Equivalent to `abs(dFdxCoarse(p)) + abs(dFdyCoarse(p))`.
>
> param p:
> :   The expression of which to take the partial derivative.
>
> return:
> :   The partial derivative.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/fwidth.xhtml>

---


<a id="shader-func-fwidthfine"></a>

vec_type **fwidthFine**(vec_type p) [🔗](shader_functions.md#shader-func-fwidthfine)

> Note
>
> Available only in the fragment shader.
> Not available when using the Compatibility renderer.
>
> Returns the sum of the absolute value of derivatives in x and y.
>
> Uses local differencing for the input argument p.
>
> Equivalent to `abs(dFdxFine(p)) + abs(dFdyFine(p))`.
>
> param p:
> :   The expression of which to take the partial derivative.
>
> return:
> :   The partial derivative.
>
> <https://registry.khronos.org/OpenGL-Refpages/gl4/html/fwidth.xhtml>

---


<a id="packing-and-unpacking-functions"></a>

## Packing and unpacking functions

These functions convert floating-point numbers into various sized integers and
then pack those integers into a single 32bit unsigned integer. The 'unpack'
functions perform the opposite operation, returning the original
floating-point numbers.

|  |  |  |
| --- | --- | --- |
| uint  vec2 | [packHalf2x16](shader_functions.md#shader-func-packhalf2x16)(vec2 v)  [unpackHalf2x16](shader_functions.md#shader-func-unpackhalf2x16)(uint v) | Convert two 32-bit floats to 16 bit floats and pack them. |
| uint  vec2 | [packUnorm2x16](shader_functions.md#shader-func-packunorm2x16)(vec2 v)  [unpackUnorm2x16](shader_functions.md#shader-func-unpackunorm2x16)(uint v) | Convert two normalized (range 0..1) 32-bit floats to 16-bit unsigned ints and pack them. |
| uint  vec2 | [packSnorm2x16](shader_functions.md#shader-func-packsnorm2x16)(vec2 v)  [unpackSnorm2x16](shader_functions.md#shader-func-unpacksnorm2x16)(uint v) | Convert two signed normalized (range -1..1) 32-bit floats to 16-bit signed ints and pack them. |
| uint  vec4 | [packUnorm4x8](shader_functions.md#shader-func-packunorm4x8)(vec4 v)  [unpackUnorm4x8](shader_functions.md#shader-func-unpackunorm4x8)(uint v) | Convert four normalized (range 0..1) 32-bit floats into 8-bit unsigned ints and pack them. |
| uint  vec4 | [packSnorm4x8](shader_functions.md#shader-func-packsnorm4x8)(vec4 v)  [unpackSnorm4x8](shader_functions.md#shader-func-unpacksnorm4x8)(uint v) | Convert four signed normalized (range -1..1) 32-bit floats into 8-bit signed ints and pack them. |

<a id="packing-and-unpacking-function-descriptions"></a>

### Packing and unpacking function descriptions

<a id="shader-func-packhalf2x16"></a>

uint **packHalf2x16**(vec2 v) [🔗](shader_functions.md#shader-func-packhalf2x16)

> Converts two 32-bit floating-point quantities to 16-bit floating-point
> quantities and packs them into a single 32-bit integer.
>
> Returns an unsigned integer obtained by converting the components of a two-component floating-point vector to
> the 16-bit floating-point representation found in the OpenGL Specification, and then packing these two
> 16-bit integers into a 32-bit unsigned integer. The first vector component specifies the 16 least-significant
> bits of the result; the second component specifies the 16 most-significant bits.
>
> param v:
> :   A vector of two 32-bit floating-point values that are to be converted to 16-bit representation and packed into the result.
>
> return:
> :   The packed value.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/packHalf2x16.xhtml>

---


<a id="shader-func-unpackhalf2x16"></a>

vec2 **unpackHalf2x16**(uint v) [🔗](shader_functions.md#shader-func-unpackhalf2x16)

> Inverse of [packHalf2x16](shader_functions.md#shader-func-packhalf2x16).
>
> Unpacks a 32-bit integer into two 16-bit floating-point values, converts them to 32-bit floating-point values, and puts them into a vector.
> The first component of the vector is obtained from the 16 least-significant bits of `v`; the second component is obtained from the
> 16 most-significant bits of `v`.
>
> param v:
> :   A single 32-bit unsigned integer containing 2 packed 16-bit floating-point values.
>
> return:
> :   Two unpacked floating-point values.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/unpackHalf2x16.xhtml>

---


<a id="shader-func-packunorm2x16"></a>

uint **packUnorm2x16**(vec2 v) [🔗](shader_functions.md#shader-func-packunorm2x16)

> Pack floating-point values into an unsigned integer.
>
> Converts each component of the normalized floating-point value v into 16-bit integer values and then packs the results into a 32-bit unsigned integer.
>
> The conversion for component c of `v` to fixed-point is performed as follows:
>
> ```gdscript
> round(clamp(c, 0.0, 1.0) * 65535.0)
> ```
>
> The first component of the vector will be written to the least significant bits of the output; the last component will be written to the most significant bits.
>
> param v:
> :   A vector of values to be packed into an unsigned integer.
>
> return:
> :   Unsigned 32 bit integer containing the packed encoding of the vector.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/packUnorm.xhtml>

---


<a id="shader-func-unpackunorm2x16"></a>

vec2 **unpackUnorm2x16**(uint v) [🔗](shader_functions.md#shader-func-unpackunorm2x16)

> Unpack floating-point values from an unsigned integer.
>
> Unpack single 32-bit unsigned integers into a pair of 16-bit unsigned integers.
> Then, each component is converted to a normalized floating-point value to generate the returned two-component vector.
>
> The conversion for unpacked fixed point value f to floating-point is performed as follows:
>
> > f / 65535.0
>
> The first component of the returned vector will be extracted from the least significant bits of the input; the last component will be extracted from the most significant bits.
>
> param v:
> :   An unsigned integer containing packed floating-point values.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/unpackUnorm.xhtml>

---


<a id="shader-func-packsnorm2x16"></a>

uint **packSnorm2x16**(vec2 v) [🔗](shader_functions.md#shader-func-packsnorm2x16)

> Packs floating-point values into an unsigned integer.
>
> Convert each component of the normalized floating-point value `v` into 16-bit integer values and then packs the results into a 32-bit unsigned integer.
>
> The conversion for component c of `v` to fixed-point is performed as follows:
>
> ```gdscript
> round(clamp(c, -1.0, 1.0) * 32767.0)
> ```
>
> The first component of the vector will be written to the least significant bits of the output; the last component will be written to the most significant bits.
>
> param v:
> :   A vector of values to be packed into an unsigned integer.
>
> return:
> :   Unsigned 32 bit integer containing the packed encoding of the vector.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/packUnorm.xhtml>

---


<a id="shader-func-unpacksnorm2x16"></a>

vec2 **unpackSnorm2x16**(uint v) [🔗](shader_functions.md#shader-func-unpacksnorm2x16)

> Unpacks floating-point values from an unsigned integer.
>
> Unpacks single 32-bit unsigned integers into a pair of 16-bit signed integers.
> Then, each component is converted to a normalized floating-point value to generate the returned two-component vector.
>
> The conversion for unpacked fixed point value f to floating-point is performed as follows:
>
> > clamp(f / 32727.0, -1.0, 1.0)
>
> The first component of the returned vector will be extracted from the least significant bits of the input; the last component will be extracted from the most significant bits.
>
> param v:
> :   An unsigned integer containing packed floating-point values.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/unpackUnorm.xhtml>

---


<a id="shader-func-packunorm4x8"></a>

uint **packUnorm4x8**(vec4 v) [🔗](shader_functions.md#shader-func-packunorm4x8)

> Packs floating-point values into an unsigned integer.
>
> Converts each component of the normalized floating-point value `v` into 16-bit integer values and then packs the results into a 32-bit unsigned integer.
>
> The conversion for component c of `v` to fixed-point is performed as follows:
>
> ```gdscript
> round(clamp(c, 0.0, 1.0) * 255.0)
> ```
>
> The first component of the vector will be written to the least significant bits of the output; the last component will be written to the most significant bits.
>
> param v:
> :   A vector of values to be packed into an unsigned integer.
>
> return:
> :   Unsigned 32 bit integer containing the packed encoding of the vector.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/packUnorm.xhtml>

---


<a id="shader-func-unpackunorm4x8"></a>

vec4 **unpackUnorm4x8**(uint v) [🔗](shader_functions.md#shader-func-unpackunorm4x8)

> Unpacks floating-point values from an unsigned integer.
>
> Unpacks single 32-bit unsigned integers into four 8-bit unsigned integers.
> Then, each component is converted to a normalized floating-point value to generate the returned four-component vector.
>
> The conversion for unpacked fixed point value f to floating-point is performed as follows:
>
> > f / 255.0
>
> The first component of the returned vector will be extracted from the least significant bits of the input; the last component will be extracted from the most significant bits.
>
> param v:
> :   An unsigned integer containing packed floating-point values.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/unpackUnorm.xhtml>

---


<a id="shader-func-packsnorm4x8"></a>

uint **packSnorm4x8**(vec4 v) [🔗](shader_functions.md#shader-func-packsnorm4x8)

> Packs floating-point values into an unsigned integer.
>
> Convert each component of the normalized floating-point value `v` into 16-bit integer values and then packs the results into a 32-bit unsigned integer.
>
> The conversion for component c of `v` to fixed-point is performed as follows:
>
> ```gdscript
> round(clamp(c, -1.0, 1.0) * 127.0)
> ```
>
> The first component of the vector will be written to the least significant bits of the output; the last component will be written to the most significant bits.
>
> param v:
> :   A vector of values to be packed into an unsigned integer.
>
> return:
> :   Unsigned 32 bit integer containing the packed encoding of the vector.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/packUnorm.xhtml>

---


<a id="shader-func-unpacksnorm4x8"></a>

vec4 **unpackSnorm4x8**(uint v) [🔗](shader_functions.md#shader-func-unpacksnorm4x8)

> Unpack floating-point values from an unsigned integer.
>
> Unpack single 32-bit unsigned integers into four 8-bit signed integers.
> Then, each component is converted to a normalized floating-point value to generate the returned four-component vector.
>
> The conversion for unpacked fixed point value f to floating-point is performed as follows:
>
> > clamp(f / 127.0, -1.0, 1.0)
>
> The first component of the returned vector will be extracted from the least significant bits of the input; the last component will be extracted from the most significant bits.
>
> param v:
> :   An unsigned integer containing packed floating-point values.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/unpackUnorm.xhtml>

---


<a id="bitwise-functions"></a>

## Bitwise functions

|  |  |  |
| --- | --- | --- |
| vec_int_type  vec_uint_type | [bitfieldExtract](shader_functions.md#shader-func-bitfieldextract)(vec_int_type value, int offset, int bits)  [bitfieldExtract](shader_functions.md#shader-func-bitfieldextract)(vec_uint_type value, int offset, int bits) | Extracts a range of bits from an integer. |
| vec_int_type  vec_uint_type | [bitfieldInsert](shader_functions.md#shader-func-bitfieldinsert)(vec_int_type base, vec_int_type insert, int offset, int bits)  [bitfieldInsert](shader_functions.md#shader-func-bitfieldinsert)(vec_uint_type base, vec_uint_type insert, int offset, int bits) | Insert a range of bits into an integer. |
| vec_int_type  vec_uint_type | [bitfieldReverse](shader_functions.md#shader-func-bitfieldreverse)(vec_int_type value)  [bitfieldReverse](shader_functions.md#shader-func-bitfieldreverse)(vec_uint_type value) | Reverse the order of bits in an integer. |
| vec_int_type  vec_uint_type | [bitCount](shader_functions.md#shader-func-bitcount)(vec_int_type value)  [bitCount](shader_functions.md#shader-func-bitcount)(vec_uint_type value) | Counts the number of 1 bits in an integer. |
| vec_int_type  vec_uint_type | [findLSB](shader_functions.md#shader-func-findlsb)(vec_int_type value)  [findLSB](shader_functions.md#shader-func-findlsb)(vec_uint_type value) | Find the index of the least significant bit set to 1 in an integer. |
| vec_int_type  vec_uint_type | [findMSB](shader_functions.md#shader-func-findmsb)(vec_int_type value)  [findMSB](shader_functions.md#shader-func-findmsb)(vec_uint_type value) | Find the index of the most significant bit set to 1 in an integer. |
| void  void | [imulExtended](shader_functions.md#shader-func-imulextended)(vec_int_type x, vec_int_type y, out vec_int_type msb, out vec_int_type lsb)  [umulExtended](shader_functions.md#shader-func-umulextended)(vec_uint_type x, vec_uint_type y, out vec_uint_type msb, out vec_uint_type lsb) | Multiplies two 32-bit numbers and produce a 64-bit result. |
| vec_uint_type | [uaddCarry](shader_functions.md#shader-func-uaddcarry)(vec_uint_type x, vec_uint_type y, out vec_uint_type carry) | Adds two unsigned integers and generates carry. |
| vec_uint_type | [usubBorrow](shader_functions.md#shader-func-usubborrow)(vec_uint_type x, vec_uint_type y, out vec_uint_type borrow) | Subtracts two unsigned integers and generates borrow. |
| vec_type | [ldexp](shader_functions.md#shader-func-ldexp)(vec_type x, out vec_int_type exp) | Assemble a floating-point number from a value and exponent. |
| vec_type | [frexp](shader_functions.md#shader-func-frexp)(vec_type x, out vec_int_type exp) | Splits a floating-point number (`x`) into significand integral components |

<a id="bitwise-function-descriptions"></a>

### Bitwise function descriptions

<a id="shader-func-bitfieldextract"></a>

vec_int_type **bitfieldExtract**(vec_int_type value, int offset, int bits) [🔗](shader_functions.md#shader-func-bitfieldextract)

> Extracts a subset of the bits of `value` and returns it in the least significant bits of the result.
> The range of bits extracted is `[offset, offset + bits - 1]`.
>
> The most significant bits of the result will be set to zero.
>
> Note
>
> If bits is zero, the result will be zero.
>
> Warning
>
> The result will be undefined if:
>
> - offset or bits is negative.
> - if the sum of offset and bits is greater than the number of bits used to store the operand.
>
> param value:
> :   The integer from which to extract bits.
>
> param offset:
> :   The index of the first bit to extract.
>
> param bits:
> :   The number of bits to extract.
>
> return:
> :   Integer with the requested bits.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/bitfieldExtract.xhtml>

---

vec_uint_type **bitfieldExtract**(vec_uint_type value, int offset, int bits) [🔗](shader_functions.md#shader-func-bitfieldextract)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Extracts a subset of the bits of `value` and returns it in the least significant bits of the result.
> The range of bits extracted is `[offset, offset + bits - 1]`.
>
> The most significant bits will be set to the value of `offset + base - 1` (i.e., it is sign extended to the width of the return type).
>
> Note
>
> If bits is zero, the result will be zero.
>
> Warning
>
> The result will be undefined if:
>
> - offset or bits is negative.
> - if the sum of offset and bits is greater than the number of bits used to store the operand.
>
> param value:
> :   The integer from which to extract bits.
>
> param offset:
> :   The index of the first bit to extract.
>
> param bits:
> :   The number of bits to extract.
>
> return:
> :   Integer with the requested bits.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/bitfieldExtract.xhtml>

---


<a id="shader-func-bitfieldinsert"></a>

vec_uint_type **bitfieldExtract**(vec_uint_type value, int offset, int bits) [🔗](shader_functions.md#shader-func-bitfieldinsert)

vec_uint_type **bitfieldInsert**(vec_uint_type base, vec_uint_type insert, int offset, int bits) [🔗](shader_functions.md#shader-func-bitfieldinsert)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Inserts the `bits` least significant bits of `insert` into `base` at offset `offset`.
>
> The returned value will have bits [offset, offset + bits + 1] taken from [0, bits - 1] of `insert` and
> all other bits taken directly from the corresponding bits of base.
>
> Note
>
> If bits is zero, the result will be the original value of base.
>
> Warning
>
> The result will be undefined if:
>
> - offset or bits is negative.
> - if the sum of offset and bits is greater than the number of bits used to store the operand.
>
> param base:
> :   The integer into which to insert `insert`.
>
> param insert:
> :   The value of the bits to insert.
>
> param offset:
> :   The index of the first bit to insert.
>
> param bits:
> :   The number of bits to insert.
>
> return:
> :   `base` with inserted bits.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/bitfieldInsert.xhtml>

---


<a id="shader-func-bitfieldreverse"></a>

vec_int_type **bitfieldReverse**(vec_int_type value) [🔗](shader_functions.md#shader-func-bitfieldreverse)

vec_uint_type **bitfieldReverse**(vec_uint_type value) [🔗](shader_functions.md#shader-func-bitfieldreverse)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Reverse the order of bits in an integer.
>
> The bit numbered `n` will be taken from bit `(bits - 1) - n` of `value`, where bits is the total number of bits used to represent `value`.
>
> param value:
> :   The value whose bits to reverse.
>
> return:
> :   `value` but with its bits reversed.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/bitfieldReverse.xhtml>

---


<a id="shader-func-bitcount"></a>

vec_int_type **bitCount**(vec_int_type value) [🔗](shader_functions.md#shader-func-bitcount)

vec_uint_type **bitCount**(vec_uint_type value) [🔗](shader_functions.md#shader-func-bitcount)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Counts the number of 1 bits in an integer.
>
> param value:
> :   The value whose bits to count.
>
> return:
> :   The number of bits that are set to 1 in the binary representation of `value`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/bitCount.xhtml>

---


<a id="shader-func-findlsb"></a>

vec_int_type **findLSB**(vec_int_type value) [🔗](shader_functions.md#shader-func-findlsb)

vec_uint_type **findLSB**(vec_uint_type value) [🔗](shader_functions.md#shader-func-findlsb)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Find the index of the least significant bit set to `1`.
>
> Note
>
> If `value` is zero, `-1` will be returned.
>
> param value:
> :   The value whose bits to scan.
>
> return:
> :   The bit number of the least significant bit that is set to 1 in the binary representation of value.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/findLSB.xhtml>

---


<a id="shader-func-findmsb"></a>

vec_int_type **findMSB**(vec_int_type value) [🔗](shader_functions.md#shader-func-findmsb)

vec_uint_type **findMSB**(vec_uint_type value) [🔗](shader_functions.md#shader-func-findmsb)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Find the index of the most significant bit set to 1.
>
> Note
>
> For signed integer types, the sign bit is checked first and then:
> :   - For positive integers, the result will be the bit number of the most significant bit that is set to 1.
>     - For negative integers, the result will be the bit number of the most significant bit set to 0.
>
> Note
>
> For a value of zero or negative 1, -1 will be returned.
>
> param value:
> :   The value whose bits to scan.
>
> return:
> :   The bit number of the most significant bit that is set to 1 in the binary representation of value.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/findMSB.xhtml>

---


<a id="shader-func-imulextended"></a>

void **imulExtended**(vec_int_type x, vec_int_type y, out vec_int_type msb, out vec_int_type lsb) [🔗](shader_functions.md#shader-func-imulextended)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Perform 32-bit by 32-bit signed multiplication to produce a 64-bit result.
>
> The 32 least significant bits of this product are returned in `lsb` and the 32 most significant bits are returned in `msb`.
>
> param x:
> :   The first multiplicand.
>
> param y:
> :   The second multiplicand.
>
> param msb:
> :   The variable to receive the most significant word of the product.
>
> param lsb:
> :   The variable to receive the least significant word of the product.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/umulExtended.xhtml>

---


<a id="shader-func-umulextended"></a>

void **umulExtended**(vec_uint_type x, vec_uint_type y, out vec_uint_type msb, out vec_uint_type lsb) [🔗](shader_functions.md#shader-func-umulextended)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Perform 32-bit by 32-bit unsigned multiplication to produce a 64-bit result.
>
> The 32 least significant bits of this product are returned in `lsb` and the 32 most significant bits are returned in `msb`.
>
> param x:
> :   The first multiplicand.
>
> param y:
> :   The second multiplicand.
>
> param msb:
> :   The variable to receive the most significant word of the product.
>
> param lsb:
> :   The variable to receive the least significant word of the product.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/umulExtended.xhtml>

---


<a id="shader-func-uaddcarry"></a>

vec_uint_type **uaddCarry**(vec_uint_type x, vec_uint_type y, out vec_uint_type carry) [🔗](shader_functions.md#shader-func-uaddcarry)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Add unsigned integers and generate carry.
>
> adds two 32-bit unsigned integer variables (scalars or vectors) and generates a 32-bit unsigned integer result, along with a carry output.
> The value carry is .
>
> param x:
> :   The first operand.
>
> param y:
> :   The second operand.
>
> param carry:
> :   0 if the sum is less than 232, otherwise 1.
>
> return:
> :   `(x + y) % 2^32`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/uaddCarry.xhtml>

---


<a id="shader-func-usubborrow"></a>

vec_uint_type **usubBorrow**(vec_uint_type x, vec_uint_type y, out vec_uint_type borrow) [🔗](shader_functions.md#shader-func-usubborrow)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Subtract unsigned integers and generate borrow.
>
> param x:
> :   The first operand.
>
> param y:
> :   The second operand.
>
> param borrow:
> :   `0` if `x >= y`, otherwise `1`.
>
> return:
> :   The difference of `x` and `y` if non-negative, or 232 plus that difference otherwise.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/usubBorrow.xhtml>

---


<a id="shader-func-ldexp"></a>

vec_type **ldexp**(vec_type x, out vec_int_type exp) [🔗](shader_functions.md#shader-func-ldexp)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Assembles a floating-point number from a value and exponent.
>
> Warning
>
> If this product is too large to be represented in the floating-point
> type, the result is undefined.
>
> param x:
> :   The value to be used as a source of significand.
>
> param exp:
> :   The value to be used as a source of exponent.
>
> return:
> :   `x * 2^exp`
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/ldexp.xhtml>

---


<a id="shader-func-frexp"></a>

vec_type **frexp**(vec_type x, out vec_int_type exp) [🔗](shader_functions.md#shader-func-frexp)

> [Component-wise Function](shader_functions.md#shading-componentwise).
>
> Extracts `x` into a floating-point significand in the range `[0.5, 1.0)` and in integral exponent of two, such that:
>
> ```gdscript
> x = significand * 2 ^ exponent
> ```
>
> For a floating-point value of zero, the significand and exponent are both zero.
>
> Warning
>
> For a floating-point value that is an infinity or a floating-point NaN, the results are undefined.
>
> param x:
> :   The value from which significand and exponent are to be extracted.
>
> param exp:
> :   The variable into which to place the exponent of `x`.
>
> return:
> :   The significand of `x`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/frexp.xhtml>

---
