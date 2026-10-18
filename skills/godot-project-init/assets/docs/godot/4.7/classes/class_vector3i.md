> Source: https://docs.godotengine.org/en/4.7/classes/class_vector3i.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="vector3i"></a>

<a id="class-vector3i"></a>

# Vector3i

A 3D vector using integer coordinates.

<a id="description"></a>

## Description

A 3-element structure that can be used to represent 3D grid coordinates or any other triplet of integers.

It uses integer coordinates and is therefore preferable to [Vector3](class_vector3.md#class-vector3) when exact precision is required. Note that the values are limited to 32 bits, and unlike [Vector3](class_vector3.md#class-vector3) this cannot be configured with an engine build option. Use [int](class_int.md#class-int) or [PackedInt64Array](class_packedint64array.md#class-packedint64array) if 64-bit values are needed.

**Note:** In a boolean context, a Vector3i will evaluate to `false` if it's equal to `Vector3i(0, 0, 0)`. Otherwise, a Vector3i will always evaluate to `true`.

<a id="tutorials"></a>

## Tutorials

- [Math documentation index](../tutorials/math/index.md)
- [Vector math](../tutorials/math/vector_math.md)
- [3Blue1Brown Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [x](class_vector3i.md#class-vector3i-property-x) | `0` |
| [int](class_int.md#class-int) | [y](class_vector3i.md#class-vector3i-property-y) | `0` |
| [int](class_int.md#class-int) | [z](class_vector3i.md#class-vector3i-property-z) | `0` |

<a id="constructors"></a>

## Constructors

|  |  |
| --- | --- |
| [Vector3i](class_vector3i.md#class-vector3i) | [Vector3i](class_vector3i.md#class-vector3i-constructor-vector3i)() |
| [Vector3i](class_vector3i.md#class-vector3i) | [Vector3i](class_vector3i.md#class-vector3i-constructor-vector3i)(from: [Vector3i](class_vector3i.md#class-vector3i)) |
| [Vector3i](class_vector3i.md#class-vector3i) | [Vector3i](class_vector3i.md#class-vector3i-constructor-vector3i)(from: [Vector3](class_vector3.md#class-vector3)) |
| [Vector3i](class_vector3i.md#class-vector3i) | [Vector3i](class_vector3i.md#class-vector3i-constructor-vector3i)(x: [int](class_int.md#class-int), y: [int](class_int.md#class-int), z: [int](class_int.md#class-int)) |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Vector3i](class_vector3i.md#class-vector3i) | [abs](class_vector3i.md#class-vector3i-method-abs)() const |
| [Vector3i](class_vector3i.md#class-vector3i) | [clamp](class_vector3i.md#class-vector3i-method-clamp)(min: [Vector3i](class_vector3i.md#class-vector3i), max: [Vector3i](class_vector3i.md#class-vector3i)) const |
| [Vector3i](class_vector3i.md#class-vector3i) | [clampi](class_vector3i.md#class-vector3i-method-clampi)(min: [int](class_int.md#class-int), max: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [distance_squared_to](class_vector3i.md#class-vector3i-method-distance-squared-to)(to: [Vector3i](class_vector3i.md#class-vector3i)) const |
| [float](class_float.md#class-float) | [distance_to](class_vector3i.md#class-vector3i-method-distance-to)(to: [Vector3i](class_vector3i.md#class-vector3i)) const |
| [float](class_float.md#class-float) | [length](class_vector3i.md#class-vector3i-method-length)() const |
| [int](class_int.md#class-int) | [length_squared](class_vector3i.md#class-vector3i-method-length-squared)() const |
| [Vector3i](class_vector3i.md#class-vector3i) | [max](class_vector3i.md#class-vector3i-method-max)(with: [Vector3i](class_vector3i.md#class-vector3i)) const |
| [int](class_int.md#class-int) | [max_axis_index](class_vector3i.md#class-vector3i-method-max-axis-index)() const |
| [Vector3i](class_vector3i.md#class-vector3i) | [maxi](class_vector3i.md#class-vector3i-method-maxi)(with: [int](class_int.md#class-int)) const |
| [Vector3i](class_vector3i.md#class-vector3i) | [min](class_vector3i.md#class-vector3i-method-min)(with: [Vector3i](class_vector3i.md#class-vector3i)) const |
| [int](class_int.md#class-int) | [min_axis_index](class_vector3i.md#class-vector3i-method-min-axis-index)() const |
| [Vector3i](class_vector3i.md#class-vector3i) | [mini](class_vector3i.md#class-vector3i-method-mini)(with: [int](class_int.md#class-int)) const |
| [Vector3i](class_vector3i.md#class-vector3i) | [sign](class_vector3i.md#class-vector3i-method-sign)() const |
| [Vector3i](class_vector3i.md#class-vector3i) | [snapped](class_vector3i.md#class-vector3i-method-snapped)(step: [Vector3i](class_vector3i.md#class-vector3i)) const |
| [Vector3i](class_vector3i.md#class-vector3i) | [snappedi](class_vector3i.md#class-vector3i-method-snappedi)(step: [int](class_int.md#class-int)) const |

<a id="operators"></a>

## Operators

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [operator !=](class_vector3i.md#class-vector3i-operator-neq-vector3i)(right: [Vector3i](class_vector3i.md#class-vector3i)) |
| [Vector3i](class_vector3i.md#class-vector3i) | [operator %](class_vector3i.md#class-vector3i-operator-mod-vector3i)(right: [Vector3i](class_vector3i.md#class-vector3i)) |
| [Vector3i](class_vector3i.md#class-vector3i) | [operator %](class_vector3i.md#class-vector3i-operator-mod-int)(right: [int](class_int.md#class-int)) |
| [Vector3i](class_vector3i.md#class-vector3i) | [operator \*](class_vector3i.md#class-vector3i-operator-mul-vector3i)(right: [Vector3i](class_vector3i.md#class-vector3i)) |
| [Vector3](class_vector3.md#class-vector3) | [operator \*](class_vector3i.md#class-vector3i-operator-mul-float)(right: [float](class_float.md#class-float)) |
| [Vector3i](class_vector3i.md#class-vector3i) | [operator \*](class_vector3i.md#class-vector3i-operator-mul-int)(right: [int](class_int.md#class-int)) |
| [Vector3i](class_vector3i.md#class-vector3i) | [operator +](class_vector3i.md#class-vector3i-operator-sum-vector3i)(right: [Vector3i](class_vector3i.md#class-vector3i)) |
| [Vector3i](class_vector3i.md#class-vector3i) | [operator -](class_vector3i.md#class-vector3i-operator-dif-vector3i)(right: [Vector3i](class_vector3i.md#class-vector3i)) |
| [Vector3i](class_vector3i.md#class-vector3i) | [operator /](class_vector3i.md#class-vector3i-operator-div-vector3i)(right: [Vector3i](class_vector3i.md#class-vector3i)) |
| [Vector3](class_vector3.md#class-vector3) | [operator /](class_vector3i.md#class-vector3i-operator-div-float)(right: [float](class_float.md#class-float)) |
| [Vector3i](class_vector3i.md#class-vector3i) | [operator /](class_vector3i.md#class-vector3i-operator-div-int)(right: [int](class_int.md#class-int)) |
| [bool](class_bool.md#class-bool) | [operator <](class_vector3i.md#class-vector3i-operator-lt-vector3i)(right: [Vector3i](class_vector3i.md#class-vector3i)) |
| [bool](class_bool.md#class-bool) | [operator <=](class_vector3i.md#class-vector3i-operator-lte-vector3i)(right: [Vector3i](class_vector3i.md#class-vector3i)) |
| [bool](class_bool.md#class-bool) | [operator ==](class_vector3i.md#class-vector3i-operator-eq-vector3i)(right: [Vector3i](class_vector3i.md#class-vector3i)) |
| [bool](class_bool.md#class-bool) | [operator >](class_vector3i.md#class-vector3i-operator-gt-vector3i)(right: [Vector3i](class_vector3i.md#class-vector3i)) |
| [bool](class_bool.md#class-bool) | [operator >=](class_vector3i.md#class-vector3i-operator-gte-vector3i)(right: [Vector3i](class_vector3i.md#class-vector3i)) |
| [int](class_int.md#class-int) | [operator []](class_vector3i.md#class-vector3i-operator-idx-int)(index: [int](class_int.md#class-int)) |
| [Vector3i](class_vector3i.md#class-vector3i) | [operator unary+](class_vector3i.md#class-vector3i-operator-unplus)() |
| [Vector3i](class_vector3i.md#class-vector3i) | [operator unary-](class_vector3i.md#class-vector3i-operator-unminus)() |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-vector3i-axis"></a>

enum **Axis**: [🔗](class_vector3i.md#enum-vector3i-axis)

<a id="class-vector3i-constant-axis-x"></a>

[Axis](class_vector3i.md#enum-vector3i-axis) **AXIS_X** = `0`

Enumerated value for the X axis. Returned by [max_axis_index()](class_vector3i.md#class-vector3i-method-max-axis-index) and [min_axis_index()](class_vector3i.md#class-vector3i-method-min-axis-index).

<a id="class-vector3i-constant-axis-y"></a>

[Axis](class_vector3i.md#enum-vector3i-axis) **AXIS_Y** = `1`

Enumerated value for the Y axis. Returned by [max_axis_index()](class_vector3i.md#class-vector3i-method-max-axis-index) and [min_axis_index()](class_vector3i.md#class-vector3i-method-min-axis-index).

<a id="class-vector3i-constant-axis-z"></a>

[Axis](class_vector3i.md#enum-vector3i-axis) **AXIS_Z** = `2`

Enumerated value for the Z axis. Returned by [max_axis_index()](class_vector3i.md#class-vector3i-method-max-axis-index) and [min_axis_index()](class_vector3i.md#class-vector3i-method-min-axis-index).

---


<a id="constants"></a>

## Constants

<a id="class-vector3i-constant-zero"></a>

**ZERO** = `Vector3i(0, 0, 0)` [🔗](class_vector3i.md#class-vector3i-constant-zero)

Zero vector, a vector with all components set to `0`.

<a id="class-vector3i-constant-one"></a>

**ONE** = `Vector3i(1, 1, 1)` [🔗](class_vector3i.md#class-vector3i-constant-one)

One vector, a vector with all components set to `1`.

<a id="class-vector3i-constant-min"></a>

**MIN** = `Vector3i(-2147483648, -2147483648, -2147483648)` [🔗](class_vector3i.md#class-vector3i-constant-min)

Min vector, a vector with all components equal to `INT32_MIN`. Can be used as a negative integer equivalent of [Vector3.INF](class_vector3.md#class-vector3-constant-inf).

<a id="class-vector3i-constant-max"></a>

**MAX** = `Vector3i(2147483647, 2147483647, 2147483647)` [🔗](class_vector3i.md#class-vector3i-constant-max)

Max vector, a vector with all components equal to `INT32_MAX`. Can be used as an integer equivalent of [Vector3.INF](class_vector3.md#class-vector3-constant-inf).

<a id="class-vector3i-constant-left"></a>

**LEFT** = `Vector3i(-1, 0, 0)` [🔗](class_vector3i.md#class-vector3i-constant-left)

Left unit vector. Represents the local direction of left, and the global direction of west.

<a id="class-vector3i-constant-right"></a>

**RIGHT** = `Vector3i(1, 0, 0)` [🔗](class_vector3i.md#class-vector3i-constant-right)

Right unit vector. Represents the local direction of right, and the global direction of east.

<a id="class-vector3i-constant-up"></a>

**UP** = `Vector3i(0, 1, 0)` [🔗](class_vector3i.md#class-vector3i-constant-up)

Up unit vector.

<a id="class-vector3i-constant-down"></a>

**DOWN** = `Vector3i(0, -1, 0)` [🔗](class_vector3i.md#class-vector3i-constant-down)

Down unit vector.

<a id="class-vector3i-constant-forward"></a>

**FORWARD** = `Vector3i(0, 0, -1)` [🔗](class_vector3i.md#class-vector3i-constant-forward)

Forward unit vector. Represents the local direction of forward, and the global direction of north.

<a id="class-vector3i-constant-back"></a>

**BACK** = `Vector3i(0, 0, 1)` [🔗](class_vector3i.md#class-vector3i-constant-back)

Back unit vector. Represents the local direction of back, and the global direction of south.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-vector3i-property-x"></a>

[int](class_int.md#class-int) **x** = `0` [🔗](class_vector3i.md#class-vector3i-property-x)

The vector's X component. Also accessible by using the index position `[0]`.

---


<a id="class-vector3i-property-y"></a>

[int](class_int.md#class-int) **y** = `0` [🔗](class_vector3i.md#class-vector3i-property-y)

The vector's Y component. Also accessible by using the index position `[1]`.

---


<a id="class-vector3i-property-z"></a>

[int](class_int.md#class-int) **z** = `0` [🔗](class_vector3i.md#class-vector3i-property-z)

The vector's Z component. Also accessible by using the index position `[2]`.

---


<a id="constructor-descriptions"></a>

## Constructor Descriptions

<a id="class-vector3i-constructor-vector3i"></a>

[Vector3i](class_vector3i.md#class-vector3i) **Vector3i**() [🔗](class_vector3i.md#class-vector3i-constructor-vector3i)

Constructs a default-initialized **Vector3i** with all components set to `0`.

---

[Vector3i](class_vector3i.md#class-vector3i) **Vector3i**(from: [Vector3i](class_vector3i.md#class-vector3i))

Constructs a **Vector3i** as a copy of the given **Vector3i**.

---

[Vector3i](class_vector3i.md#class-vector3i) **Vector3i**(from: [Vector3](class_vector3.md#class-vector3))

Constructs a new **Vector3i** from the given [Vector3](class_vector3.md#class-vector3) by truncating components' fractional parts (rounding towards zero). For a different behavior consider passing the result of [Vector3.ceil()](class_vector3.md#class-vector3-method-ceil), [Vector3.floor()](class_vector3.md#class-vector3-method-floor) or [Vector3.round()](class_vector3.md#class-vector3-method-round) to this constructor instead.

---

[Vector3i](class_vector3i.md#class-vector3i) **Vector3i**(x: [int](class_int.md#class-int), y: [int](class_int.md#class-int), z: [int](class_int.md#class-int))

Returns a **Vector3i** with the given components.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-vector3i-method-abs"></a>

[Vector3i](class_vector3i.md#class-vector3i) **abs**() const [🔗](class_vector3i.md#class-vector3i-method-abs)

Returns a new vector with all components in absolute values (i.e. positive).

---


<a id="class-vector3i-method-clamp"></a>

[Vector3i](class_vector3i.md#class-vector3i) **clamp**(min: [Vector3i](class_vector3i.md#class-vector3i), max: [Vector3i](class_vector3i.md#class-vector3i)) const [🔗](class_vector3i.md#class-vector3i-method-clamp)

Returns a new vector with all components clamped between the components of `min` and `max`, by running [@GlobalScope.clamp()](class_@globalscope.md#class-globalscope-method-clamp) on each component.

---


<a id="class-vector3i-method-clampi"></a>

[Vector3i](class_vector3i.md#class-vector3i) **clampi**(min: [int](class_int.md#class-int), max: [int](class_int.md#class-int)) const [🔗](class_vector3i.md#class-vector3i-method-clampi)

Returns a new vector with all components clamped between `min` and `max`, by running [@GlobalScope.clamp()](class_@globalscope.md#class-globalscope-method-clamp) on each component.

---


<a id="class-vector3i-method-distance-squared-to"></a>

[int](class_int.md#class-int) **distance_squared_to**(to: [Vector3i](class_vector3i.md#class-vector3i)) const [🔗](class_vector3i.md#class-vector3i-method-distance-squared-to)

Returns the squared [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance) between this vector and `to`.

This method runs faster than [distance_to()](class_vector3i.md#class-vector3i-method-distance-to), so prefer it if you need to compare vectors or need the squared distance for some formula.

---


<a id="class-vector3i-method-distance-to"></a>

[float](class_float.md#class-float) **distance_to**(to: [Vector3i](class_vector3i.md#class-vector3i)) const [🔗](class_vector3i.md#class-vector3i-method-distance-to)

Returns the [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance) between this vector and `to`.

---


<a id="class-vector3i-method-length"></a>

[float](class_float.md#class-float) **length**() const [🔗](class_vector3i.md#class-vector3i-method-length)

Returns the length (magnitude) of this vector.

---


<a id="class-vector3i-method-length-squared"></a>

[int](class_int.md#class-int) **length_squared**() const [🔗](class_vector3i.md#class-vector3i-method-length-squared)

Returns the squared length (squared magnitude) of this vector.

This method runs faster than [length()](class_vector3i.md#class-vector3i-method-length), so prefer it if you need to compare vectors or need the squared distance for some formula.

---


<a id="class-vector3i-method-max"></a>

[Vector3i](class_vector3i.md#class-vector3i) **max**(with: [Vector3i](class_vector3i.md#class-vector3i)) const [🔗](class_vector3i.md#class-vector3i-method-max)

Returns the component-wise maximum of this and `with`, equivalent to `Vector3i(maxi(x, with.x), maxi(y, with.y), maxi(z, with.z))`.

---


<a id="class-vector3i-method-max-axis-index"></a>

[int](class_int.md#class-int) **max_axis_index**() const [🔗](class_vector3i.md#class-vector3i-method-max-axis-index)

Returns the axis of the vector's highest value. See `AXIS_*` constants. If all components are equal, this method returns [AXIS_X](class_vector3i.md#class-vector3i-constant-axis-x).

---


<a id="class-vector3i-method-maxi"></a>

[Vector3i](class_vector3i.md#class-vector3i) **maxi**(with: [int](class_int.md#class-int)) const [🔗](class_vector3i.md#class-vector3i-method-maxi)

Returns the component-wise maximum of this and `with`, equivalent to `Vector3i(maxi(x, with), maxi(y, with), maxi(z, with))`.

---


<a id="class-vector3i-method-min"></a>

[Vector3i](class_vector3i.md#class-vector3i) **min**(with: [Vector3i](class_vector3i.md#class-vector3i)) const [🔗](class_vector3i.md#class-vector3i-method-min)

Returns the component-wise minimum of this and `with`, equivalent to `Vector3i(mini(x, with.x), mini(y, with.y), mini(z, with.z))`.

---


<a id="class-vector3i-method-min-axis-index"></a>

[int](class_int.md#class-int) **min_axis_index**() const [🔗](class_vector3i.md#class-vector3i-method-min-axis-index)

Returns the axis of the vector's lowest value. See `AXIS_*` constants. If all components are equal, this method returns [AXIS_Z](class_vector3i.md#class-vector3i-constant-axis-z).

---


<a id="class-vector3i-method-mini"></a>

[Vector3i](class_vector3i.md#class-vector3i) **mini**(with: [int](class_int.md#class-int)) const [🔗](class_vector3i.md#class-vector3i-method-mini)

Returns the component-wise minimum of this and `with`, equivalent to `Vector3i(mini(x, with), mini(y, with), mini(z, with))`.

---


<a id="class-vector3i-method-sign"></a>

[Vector3i](class_vector3i.md#class-vector3i) **sign**() const [🔗](class_vector3i.md#class-vector3i-method-sign)

Returns a new vector with each component set to `1` if it's positive, `-1` if it's negative, and `0` if it's zero. The result is identical to calling [@GlobalScope.sign()](class_@globalscope.md#class-globalscope-method-sign) on each component.

---


<a id="class-vector3i-method-snapped"></a>

[Vector3i](class_vector3i.md#class-vector3i) **snapped**(step: [Vector3i](class_vector3i.md#class-vector3i)) const [🔗](class_vector3i.md#class-vector3i-method-snapped)

Returns a new vector with each component snapped to the closest multiple of the corresponding component in `step`.

---


<a id="class-vector3i-method-snappedi"></a>

[Vector3i](class_vector3i.md#class-vector3i) **snappedi**(step: [int](class_int.md#class-int)) const [🔗](class_vector3i.md#class-vector3i-method-snappedi)

Returns a new vector with each component snapped to the closest multiple of `step`.

---


<a id="operator-descriptions"></a>

## Operator Descriptions

<a id="class-vector3i-operator-neq-vector3i"></a>

[bool](class_bool.md#class-bool) **operator !=**(right: [Vector3i](class_vector3i.md#class-vector3i)) [🔗](class_vector3i.md#class-vector3i-operator-neq-vector3i)

Returns `true` if the vectors are not equal.

---


<a id="class-vector3i-operator-mod-vector3i"></a>

[Vector3i](class_vector3i.md#class-vector3i) **operator %**(right: [Vector3i](class_vector3i.md#class-vector3i)) [🔗](class_vector3i.md#class-vector3i-operator-mod-vector3i)

Gets the remainder of each component of the **Vector3i** with the components of the given **Vector3i**. This operation uses truncated division, which is often not desired as it does not work well with negative numbers. Consider using [@GlobalScope.posmod()](class_@globalscope.md#class-globalscope-method-posmod) instead if you want to handle negative numbers.

```gdscript
print(Vector3i(10, -20, 30) % Vector3i(7, 8, 9)) # Prints (3, -4, 3)
```

---


<a id="class-vector3i-operator-mod-int"></a>

[Vector3i](class_vector3i.md#class-vector3i) **operator %**(right: [int](class_int.md#class-int)) [🔗](class_vector3i.md#class-vector3i-operator-mod-int)

Gets the remainder of each component of the **Vector3i** with the given [int](class_int.md#class-int). This operation uses truncated division, which is often not desired as it does not work well with negative numbers. Consider using [@GlobalScope.posmod()](class_@globalscope.md#class-globalscope-method-posmod) instead if you want to handle negative numbers.

```gdscript
print(Vector3i(10, -20, 30) % 7) # Prints (3, -6, 2)
```

---


<a id="class-vector3i-operator-mul-vector3i"></a>

[Vector3i](class_vector3i.md#class-vector3i) **operator \***(right: [Vector3i](class_vector3i.md#class-vector3i)) [🔗](class_vector3i.md#class-vector3i-operator-mul-vector3i)

Multiplies each component of the **Vector3i** by the components of the given **Vector3i**.

```gdscript
print(Vector3i(10, 20, 30) * Vector3i(3, 4, 5)) # Prints (30, 80, 150)
```

---


<a id="class-vector3i-operator-mul-float"></a>

[Vector3](class_vector3.md#class-vector3) **operator \***(right: [float](class_float.md#class-float)) [🔗](class_vector3i.md#class-vector3i-operator-mul-float)

Multiplies each component of the **Vector3i** by the given [float](class_float.md#class-float). Returns a [Vector3](class_vector3.md#class-vector3).

```gdscript
print(Vector3i(10, 15, 20) * 0.9) # Prints (9.0, 13.5, 18.0)
```

---


<a id="class-vector3i-operator-mul-int"></a>

[Vector3i](class_vector3i.md#class-vector3i) **operator \***(right: [int](class_int.md#class-int)) [🔗](class_vector3i.md#class-vector3i-operator-mul-int)

Multiplies each component of the **Vector3i** by the given [int](class_int.md#class-int).

---


<a id="class-vector3i-operator-sum-vector3i"></a>

[Vector3i](class_vector3i.md#class-vector3i) **operator +**(right: [Vector3i](class_vector3i.md#class-vector3i)) [🔗](class_vector3i.md#class-vector3i-operator-sum-vector3i)

Adds each component of the **Vector3i** by the components of the given **Vector3i**.

```gdscript
print(Vector3i(10, 20, 30) + Vector3i(3, 4, 5)) # Prints (13, 24, 35)
```

---


<a id="class-vector3i-operator-dif-vector3i"></a>

[Vector3i](class_vector3i.md#class-vector3i) **operator -**(right: [Vector3i](class_vector3i.md#class-vector3i)) [🔗](class_vector3i.md#class-vector3i-operator-dif-vector3i)

Subtracts each component of the **Vector3i** by the components of the given **Vector3i**.

```gdscript
print(Vector3i(10, 20, 30) - Vector3i(3, 4, 5)) # Prints (7, 16, 25)
```

---


<a id="class-vector3i-operator-div-vector3i"></a>

[Vector3i](class_vector3i.md#class-vector3i) **operator /**(right: [Vector3i](class_vector3i.md#class-vector3i)) [🔗](class_vector3i.md#class-vector3i-operator-div-vector3i)

Divides each component of the **Vector3i** by the components of the given **Vector3i**.

```gdscript
print(Vector3i(10, 20, 30) / Vector3i(2, 5, 3)) # Prints (5, 4, 10)
```

---


<a id="class-vector3i-operator-div-float"></a>

[Vector3](class_vector3.md#class-vector3) **operator /**(right: [float](class_float.md#class-float)) [🔗](class_vector3i.md#class-vector3i-operator-div-float)

Divides each component of the **Vector3i** by the given [float](class_float.md#class-float). Returns a [Vector3](class_vector3.md#class-vector3).

```gdscript
print(Vector3i(1, 2, 3) / 2.5) # Prints (0.4, 0.8, 1.2)
```

---


<a id="class-vector3i-operator-div-int"></a>

[Vector3i](class_vector3i.md#class-vector3i) **operator /**(right: [int](class_int.md#class-int)) [🔗](class_vector3i.md#class-vector3i-operator-div-int)

Divides each component of the **Vector3i** by the given [int](class_int.md#class-int).

---


<a id="class-vector3i-operator-lt-vector3i"></a>

[bool](class_bool.md#class-bool) **operator <**(right: [Vector3i](class_vector3i.md#class-vector3i)) [🔗](class_vector3i.md#class-vector3i-operator-lt-vector3i)

Compares two **Vector3i** vectors by first checking if the X value of the left vector is less than the X value of the `right` vector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors, and then with the Z values. This operator is useful for sorting vectors.

---


<a id="class-vector3i-operator-lte-vector3i"></a>

[bool](class_bool.md#class-bool) **operator <=**(right: [Vector3i](class_vector3i.md#class-vector3i)) [🔗](class_vector3i.md#class-vector3i-operator-lte-vector3i)

Compares two **Vector3i** vectors by first checking if the X value of the left vector is less than or equal to the X value of the `right` vector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors, and then with the Z values. This operator is useful for sorting vectors.

---


<a id="class-vector3i-operator-eq-vector3i"></a>

[bool](class_bool.md#class-bool) **operator ==**(right: [Vector3i](class_vector3i.md#class-vector3i)) [🔗](class_vector3i.md#class-vector3i-operator-eq-vector3i)

Returns `true` if the vectors are equal.

---


<a id="class-vector3i-operator-gt-vector3i"></a>

[bool](class_bool.md#class-bool) **operator >**(right: [Vector3i](class_vector3i.md#class-vector3i)) [🔗](class_vector3i.md#class-vector3i-operator-gt-vector3i)

Compares two **Vector3i** vectors by first checking if the X value of the left vector is greater than the X value of the `right` vector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors, and then with the Z values. This operator is useful for sorting vectors.

---


<a id="class-vector3i-operator-gte-vector3i"></a>

[bool](class_bool.md#class-bool) **operator >=**(right: [Vector3i](class_vector3i.md#class-vector3i)) [🔗](class_vector3i.md#class-vector3i-operator-gte-vector3i)

Compares two **Vector3i** vectors by first checking if the X value of the left vector is greater than or equal to the X value of the `right` vector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors, and then with the Z values. This operator is useful for sorting vectors.

---


<a id="class-vector3i-operator-idx-int"></a>

[int](class_int.md#class-int) **operator []**(index: [int](class_int.md#class-int)) [🔗](class_vector3i.md#class-vector3i-operator-idx-int)

Access vector components using their `index`. `v[0]` is equivalent to `v.x`, `v[1]` is equivalent to `v.y`, and `v[2]` is equivalent to `v.z`.

---


<a id="class-vector3i-operator-unplus"></a>

[Vector3i](class_vector3i.md#class-vector3i) **operator unary+**() [🔗](class_vector3i.md#class-vector3i-operator-unplus)

Returns the same value as if the `+` was not there. Unary `+` does nothing, but sometimes it can make your code more readable.

---


<a id="class-vector3i-operator-unminus"></a>

[Vector3i](class_vector3i.md#class-vector3i) **operator unary-**() [🔗](class_vector3i.md#class-vector3i-operator-unminus)

Returns the negative value of the **Vector3i**. This is the same as writing `Vector3i(-v.x, -v.y, -v.z)`. This operation flips the direction of the vector while keeping the same magnitude.
