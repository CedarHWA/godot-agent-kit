> Source: https://docs.godotengine.org/en/4.7/classes/class_float.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="float"></a>

<a id="class-float"></a>

# float

A built-in type for floating-point numbers.

<a id="description"></a>

## Description

The **float** built-in type is a 64-bit double-precision floating-point number, equivalent to `double` in C++. This type has 14 reliable decimal digits of precision. The maximum value of **float** is approximately `1.79769e308`, and the minimum is approximately `-1.79769e308`.

Many methods and properties in the engine use 32-bit single-precision floating-point numbers instead, equivalent to `float` in C++, which have 6 reliable decimal digits of precision. For data structures such as [Vector2](class_vector2.md#class-vector2) and [Vector3](class_vector3.md#class-vector3), Godot uses 32-bit floating-point numbers by default, but it can be changed to use 64-bit doubles if Godot is compiled with the `precision=double` option.

Math done using the **float** type is not guaranteed to be exact and will often result in small errors. You should usually use the [@GlobalScope.is_equal_approx()](class_@globalscope.md#class-globalscope-method-is-equal-approx) and [@GlobalScope.is_zero_approx()](class_@globalscope.md#class-globalscope-method-is-zero-approx) methods instead of `==` to compare **float** values for equality.

**Note:** In a boolean context, a **float** will evaluate to `false` if it's exactly equal to `0.0`, and to `true` otherwise.

<a id="tutorials"></a>

## Tutorials

- [Wikipedia: Double-precision floating-point format](https://en.wikipedia.org/wiki/Double-precision_floating-point_format)
- [Wikipedia: Single-precision floating-point format](https://en.wikipedia.org/wiki/Single-precision_floating-point_format)

<a id="constructors"></a>

## Constructors

|  |  |
| --- | --- |
| [float](class_float.md#class-float) | [float](class_float.md#class-float-constructor-float)() |
| [float](class_float.md#class-float) | [float](class_float.md#class-float-constructor-float)(from: [float](class_float.md#class-float)) |
| [float](class_float.md#class-float) | [float](class_float.md#class-float-constructor-float)(from: [String](class_string.md#class-string)) |
| [float](class_float.md#class-float) | [float](class_float.md#class-float-constructor-float)(from: [bool](class_bool.md#class-bool)) |
| [float](class_float.md#class-float) | [float](class_float.md#class-float-constructor-float)(from: [int](class_int.md#class-int)) |

<a id="operators"></a>

## Operators

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [operator !=](class_float.md#class-float-operator-neq-float)(right: [float](class_float.md#class-float)) |
| [bool](class_bool.md#class-bool) | [operator !=](class_float.md#class-float-operator-neq-int)(right: [int](class_int.md#class-int)) |
| [Color](class_color.md#class-color) | [operator \*](class_float.md#class-float-operator-mul-color)(right: [Color](class_color.md#class-color)) |
| [Quaternion](class_quaternion.md#class-quaternion) | [operator \*](class_float.md#class-float-operator-mul-quaternion)(right: [Quaternion](class_quaternion.md#class-quaternion)) |
| [Vector2](class_vector2.md#class-vector2) | [operator \*](class_float.md#class-float-operator-mul-vector2)(right: [Vector2](class_vector2.md#class-vector2)) |
| [Vector2](class_vector2.md#class-vector2) | [operator \*](class_float.md#class-float-operator-mul-vector2i)(right: [Vector2i](class_vector2i.md#class-vector2i)) |
| [Vector3](class_vector3.md#class-vector3) | [operator \*](class_float.md#class-float-operator-mul-vector3)(right: [Vector3](class_vector3.md#class-vector3)) |
| [Vector3](class_vector3.md#class-vector3) | [operator \*](class_float.md#class-float-operator-mul-vector3i)(right: [Vector3i](class_vector3i.md#class-vector3i)) |
| [Vector4](class_vector4.md#class-vector4) | [operator \*](class_float.md#class-float-operator-mul-vector4)(right: [Vector4](class_vector4.md#class-vector4)) |
| [Vector4](class_vector4.md#class-vector4) | [operator \*](class_float.md#class-float-operator-mul-vector4i)(right: [Vector4i](class_vector4i.md#class-vector4i)) |
| [float](class_float.md#class-float) | [operator \*](class_float.md#class-float-operator-mul-float)(right: [float](class_float.md#class-float)) |
| [float](class_float.md#class-float) | [operator \*](class_float.md#class-float-operator-mul-int)(right: [int](class_int.md#class-int)) |
| [float](class_float.md#class-float) | [operator \*\*](class_float.md#class-float-operator-pow-float)(right: [float](class_float.md#class-float)) |
| [float](class_float.md#class-float) | [operator \*\*](class_float.md#class-float-operator-pow-int)(right: [int](class_int.md#class-int)) |
| [float](class_float.md#class-float) | [operator +](class_float.md#class-float-operator-sum-float)(right: [float](class_float.md#class-float)) |
| [float](class_float.md#class-float) | [operator +](class_float.md#class-float-operator-sum-int)(right: [int](class_int.md#class-int)) |
| [float](class_float.md#class-float) | [operator -](class_float.md#class-float-operator-dif-float)(right: [float](class_float.md#class-float)) |
| [float](class_float.md#class-float) | [operator -](class_float.md#class-float-operator-dif-int)(right: [int](class_int.md#class-int)) |
| [float](class_float.md#class-float) | [operator /](class_float.md#class-float-operator-div-float)(right: [float](class_float.md#class-float)) |
| [float](class_float.md#class-float) | [operator /](class_float.md#class-float-operator-div-int)(right: [int](class_int.md#class-int)) |
| [bool](class_bool.md#class-bool) | [operator <](class_float.md#class-float-operator-lt-float)(right: [float](class_float.md#class-float)) |
| [bool](class_bool.md#class-bool) | [operator <](class_float.md#class-float-operator-lt-int)(right: [int](class_int.md#class-int)) |
| [bool](class_bool.md#class-bool) | [operator <=](class_float.md#class-float-operator-lte-float)(right: [float](class_float.md#class-float)) |
| [bool](class_bool.md#class-bool) | [operator <=](class_float.md#class-float-operator-lte-int)(right: [int](class_int.md#class-int)) |
| [bool](class_bool.md#class-bool) | [operator ==](class_float.md#class-float-operator-eq-float)(right: [float](class_float.md#class-float)) |
| [bool](class_bool.md#class-bool) | [operator ==](class_float.md#class-float-operator-eq-int)(right: [int](class_int.md#class-int)) |
| [bool](class_bool.md#class-bool) | [operator >](class_float.md#class-float-operator-gt-float)(right: [float](class_float.md#class-float)) |
| [bool](class_bool.md#class-bool) | [operator >](class_float.md#class-float-operator-gt-int)(right: [int](class_int.md#class-int)) |
| [bool](class_bool.md#class-bool) | [operator >=](class_float.md#class-float-operator-gte-float)(right: [float](class_float.md#class-float)) |
| [bool](class_bool.md#class-bool) | [operator >=](class_float.md#class-float-operator-gte-int)(right: [int](class_int.md#class-int)) |
| [float](class_float.md#class-float) | [operator unary+](class_float.md#class-float-operator-unplus)() |
| [float](class_float.md#class-float) | [operator unary-](class_float.md#class-float-operator-unminus)() |

---


<a id="constructor-descriptions"></a>

## Constructor Descriptions

<a id="class-float-constructor-float"></a>

[float](class_float.md#class-float) **float**() [🔗](class_float.md#class-float-constructor-float)

Constructs a default-initialized **float** set to `0.0`.

---

[float](class_float.md#class-float) **float**(from: [float](class_float.md#class-float))

Constructs a **float** as a copy of the given **float**.

---

[float](class_float.md#class-float) **float**(from: [String](class_string.md#class-string))

Converts a [String](class_string.md#class-string) to a **float**, following the same rules as [String.to_float()](class_string.md#class-string-method-to-float).

---

[float](class_float.md#class-float) **float**(from: [bool](class_bool.md#class-bool))

Cast a [bool](class_bool.md#class-bool) value to a floating-point value, `float(true)` will be equal to 1.0 and `float(false)` will be equal to 0.0.

---

[float](class_float.md#class-float) **float**(from: [int](class_int.md#class-int))

Cast an [int](class_int.md#class-int) value to a floating-point value, `float(1)` will be equal to `1.0`.

---


<a id="operator-descriptions"></a>

## Operator Descriptions

<a id="class-float-operator-neq-float"></a>

[bool](class_bool.md#class-bool) **operator !=**(right: [float](class_float.md#class-float)) [🔗](class_float.md#class-float-operator-neq-float)

Returns `true` if two floats are different from each other.

**Note:** [@GDScript.NAN](class_@gdscript.md#class-gdscript-constant-nan) doesn't behave the same as other numbers. Therefore, the results from this operator may not be accurate if NaNs are included.

---


<a id="class-float-operator-neq-int"></a>

[bool](class_bool.md#class-bool) **operator !=**(right: [int](class_int.md#class-int)) [🔗](class_float.md#class-float-operator-neq-int)

Returns `true` if the integer has different value than the float.

---


<a id="class-float-operator-mul-color"></a>

[Color](class_color.md#class-color) **operator \***(right: [Color](class_color.md#class-color)) [🔗](class_float.md#class-float-operator-mul-color)

Multiplies each component of the [Color](class_color.md#class-color), including the alpha, by the given **float**.

```gdscript
print(1.5 * Color(0.5, 0.5, 0.5)) # Prints (0.75, 0.75, 0.75, 1.5)
```

---


<a id="class-float-operator-mul-quaternion"></a>

[Quaternion](class_quaternion.md#class-quaternion) **operator \***(right: [Quaternion](class_quaternion.md#class-quaternion)) [🔗](class_float.md#class-float-operator-mul-quaternion)

Multiplies each component of the [Quaternion](class_quaternion.md#class-quaternion) by the given **float**. This operation is not meaningful on its own, but it can be used as a part of a larger expression.

---


<a id="class-float-operator-mul-vector2"></a>

[Vector2](class_vector2.md#class-vector2) **operator \***(right: [Vector2](class_vector2.md#class-vector2)) [🔗](class_float.md#class-float-operator-mul-vector2)

Multiplies each component of the [Vector2](class_vector2.md#class-vector2) by the given **float**.

```gdscript
print(2.5 * Vector2(1, 3)) # Prints (2.5, 7.5)
```

---


<a id="class-float-operator-mul-vector2i"></a>

[Vector2](class_vector2.md#class-vector2) **operator \***(right: [Vector2i](class_vector2i.md#class-vector2i)) [🔗](class_float.md#class-float-operator-mul-vector2i)

Multiplies each component of the [Vector2i](class_vector2i.md#class-vector2i) by the given **float**. Returns a [Vector2](class_vector2.md#class-vector2).

```gdscript
print(0.9 * Vector2i(10, 15)) # Prints (9.0, 13.5)
```

---


<a id="class-float-operator-mul-vector3"></a>

[Vector3](class_vector3.md#class-vector3) **operator \***(right: [Vector3](class_vector3.md#class-vector3)) [🔗](class_float.md#class-float-operator-mul-vector3)

Multiplies each component of the [Vector3](class_vector3.md#class-vector3) by the given **float**.

---


<a id="class-float-operator-mul-vector3i"></a>

[Vector3](class_vector3.md#class-vector3) **operator \***(right: [Vector3i](class_vector3i.md#class-vector3i)) [🔗](class_float.md#class-float-operator-mul-vector3i)

Multiplies each component of the [Vector3i](class_vector3i.md#class-vector3i) by the given **float**. Returns a [Vector3](class_vector3.md#class-vector3).

```gdscript
print(0.9 * Vector3i(10, 15, 20)) # Prints (9.0, 13.5, 18.0)
```

---


<a id="class-float-operator-mul-vector4"></a>

[Vector4](class_vector4.md#class-vector4) **operator \***(right: [Vector4](class_vector4.md#class-vector4)) [🔗](class_float.md#class-float-operator-mul-vector4)

Multiplies each component of the [Vector4](class_vector4.md#class-vector4) by the given **float**.

---


<a id="class-float-operator-mul-vector4i"></a>

[Vector4](class_vector4.md#class-vector4) **operator \***(right: [Vector4i](class_vector4i.md#class-vector4i)) [🔗](class_float.md#class-float-operator-mul-vector4i)

Multiplies each component of the [Vector4i](class_vector4i.md#class-vector4i) by the given **float**. Returns a [Vector4](class_vector4.md#class-vector4).

```gdscript
print(0.9 * Vector4i(10, 15, 20, -10)) # Prints (9.0, 13.5, 18.0, -9.0)
```

---


<a id="class-float-operator-mul-float"></a>

[float](class_float.md#class-float) **operator \***(right: [float](class_float.md#class-float)) [🔗](class_float.md#class-float-operator-mul-float)

Multiplies two **float**s.

---


<a id="class-float-operator-mul-int"></a>

[float](class_float.md#class-float) **operator \***(right: [int](class_int.md#class-int)) [🔗](class_float.md#class-float-operator-mul-int)

Multiplies a **float** and an [int](class_int.md#class-int). The result is a **float**.

---


<a id="class-float-operator-pow-float"></a>

[float](class_float.md#class-float) **operator \*\***(right: [float](class_float.md#class-float)) [🔗](class_float.md#class-float-operator-pow-float)

Raises a **float** to a power of a **float**.

```gdscript
print(39.0625**0.25) # 2.5
```

---


<a id="class-float-operator-pow-int"></a>

[float](class_float.md#class-float) **operator \*\***(right: [int](class_int.md#class-int)) [🔗](class_float.md#class-float-operator-pow-int)

Raises a **float** to a power of an [int](class_int.md#class-int). The result is a **float**.

```gdscript
print(0.9**3) # 0.729
```

---


<a id="class-float-operator-sum-float"></a>

[float](class_float.md#class-float) **operator +**(right: [float](class_float.md#class-float)) [🔗](class_float.md#class-float-operator-sum-float)

Adds two floats.

---


<a id="class-float-operator-sum-int"></a>

[float](class_float.md#class-float) **operator +**(right: [int](class_int.md#class-int)) [🔗](class_float.md#class-float-operator-sum-int)

Adds a **float** and an [int](class_int.md#class-int). The result is a **float**.

---


<a id="class-float-operator-dif-float"></a>

[float](class_float.md#class-float) **operator -**(right: [float](class_float.md#class-float)) [🔗](class_float.md#class-float-operator-dif-float)

Subtracts a float from a float.

---


<a id="class-float-operator-dif-int"></a>

[float](class_float.md#class-float) **operator -**(right: [int](class_int.md#class-int)) [🔗](class_float.md#class-float-operator-dif-int)

Subtracts an [int](class_int.md#class-int) from a **float**. The result is a **float**.

---


<a id="class-float-operator-div-float"></a>

[float](class_float.md#class-float) **operator /**(right: [float](class_float.md#class-float)) [🔗](class_float.md#class-float-operator-div-float)

Divides two floats.

---


<a id="class-float-operator-div-int"></a>

[float](class_float.md#class-float) **operator /**(right: [int](class_int.md#class-int)) [🔗](class_float.md#class-float-operator-div-int)

Divides a **float** by an [int](class_int.md#class-int). The result is a **float**.

---


<a id="class-float-operator-lt-float"></a>

[bool](class_bool.md#class-bool) **operator <**(right: [float](class_float.md#class-float)) [🔗](class_float.md#class-float-operator-lt-float)

Returns `true` if the left float is less than the right one.

**Note:** [@GDScript.NAN](class_@gdscript.md#class-gdscript-constant-nan) doesn't behave the same as other numbers. Therefore, the results from this operator may not be accurate if NaNs are included.

---


<a id="class-float-operator-lt-int"></a>

[bool](class_bool.md#class-bool) **operator <**(right: [int](class_int.md#class-int)) [🔗](class_float.md#class-float-operator-lt-int)

Returns `true` if this **float** is less than the given [int](class_int.md#class-int).

---


<a id="class-float-operator-lte-float"></a>

[bool](class_bool.md#class-bool) **operator <=**(right: [float](class_float.md#class-float)) [🔗](class_float.md#class-float-operator-lte-float)

Returns `true` if the left float is less than or equal to the right one.

**Note:** [@GDScript.NAN](class_@gdscript.md#class-gdscript-constant-nan) doesn't behave the same as other numbers. Therefore, the results from this operator may not be accurate if NaNs are included.

---


<a id="class-float-operator-lte-int"></a>

[bool](class_bool.md#class-bool) **operator <=**(right: [int](class_int.md#class-int)) [🔗](class_float.md#class-float-operator-lte-int)

Returns `true` if this **float** is less than or equal to the given [int](class_int.md#class-int).

---


<a id="class-float-operator-eq-float"></a>

[bool](class_bool.md#class-bool) **operator ==**(right: [float](class_float.md#class-float)) [🔗](class_float.md#class-float-operator-eq-float)

Returns `true` if both floats are exactly equal.

**Note:** Due to floating-point precision errors, consider using [@GlobalScope.is_equal_approx()](class_@globalscope.md#class-globalscope-method-is-equal-approx) or [@GlobalScope.is_zero_approx()](class_@globalscope.md#class-globalscope-method-is-zero-approx) instead, which are more reliable.

**Note:** [@GDScript.NAN](class_@gdscript.md#class-gdscript-constant-nan) doesn't behave the same as other numbers. Therefore, the results from this operator may not be accurate if NaNs are included.

---


<a id="class-float-operator-eq-int"></a>

[bool](class_bool.md#class-bool) **operator ==**(right: [int](class_int.md#class-int)) [🔗](class_float.md#class-float-operator-eq-int)

Returns `true` if the **float** and the given [int](class_int.md#class-int) are equal.

---


<a id="class-float-operator-gt-float"></a>

[bool](class_bool.md#class-bool) **operator >**(right: [float](class_float.md#class-float)) [🔗](class_float.md#class-float-operator-gt-float)

Returns `true` if the left float is greater than the right one.

**Note:** [@GDScript.NAN](class_@gdscript.md#class-gdscript-constant-nan) doesn't behave the same as other numbers. Therefore, the results from this operator may not be accurate if NaNs are included.

---


<a id="class-float-operator-gt-int"></a>

[bool](class_bool.md#class-bool) **operator >**(right: [int](class_int.md#class-int)) [🔗](class_float.md#class-float-operator-gt-int)

Returns `true` if this **float** is greater than the given [int](class_int.md#class-int).

---


<a id="class-float-operator-gte-float"></a>

[bool](class_bool.md#class-bool) **operator >=**(right: [float](class_float.md#class-float)) [🔗](class_float.md#class-float-operator-gte-float)

Returns `true` if the left float is greater than or equal to the right one.

**Note:** [@GDScript.NAN](class_@gdscript.md#class-gdscript-constant-nan) doesn't behave the same as other numbers. Therefore, the results from this operator may not be accurate if NaNs are included.

---


<a id="class-float-operator-gte-int"></a>

[bool](class_bool.md#class-bool) **operator >=**(right: [int](class_int.md#class-int)) [🔗](class_float.md#class-float-operator-gte-int)

Returns `true` if this **float** is greater than or equal to the given [int](class_int.md#class-int).

---


<a id="class-float-operator-unplus"></a>

[float](class_float.md#class-float) **operator unary+**() [🔗](class_float.md#class-float-operator-unplus)

Returns the same value as if the `+` was not there. Unary `+` does nothing, but sometimes it can make your code more readable.

---


<a id="class-float-operator-unminus"></a>

[float](class_float.md#class-float) **operator unary-**() [🔗](class_float.md#class-float-operator-unminus)

Returns the negative value of the **float**. If positive, turns the number negative. If negative, turns the number positive. With floats, the number zero can be either positive or negative.
