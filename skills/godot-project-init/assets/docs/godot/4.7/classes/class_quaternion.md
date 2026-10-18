> Source: https://docs.godotengine.org/en/4.7/classes/class_quaternion.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="quaternion"></a>

<a id="class-quaternion"></a>

# Quaternion

A unit quaternion used for representing 3D rotations.

<a id="description"></a>

## Description

The **Quaternion** built-in [Variant](class_variant.md#class-variant) type is a 4D data structure that represents rotation in the form of a [Hamilton convention quaternion](https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation). Compared to the [Basis](class_basis.md#class-basis) type which can store both rotation and scale, quaternions can *only* store rotation.

A **Quaternion** is composed by 4 floating-point components: [w](class_quaternion.md#class-quaternion-property-w), [x](class_quaternion.md#class-quaternion-property-x), [y](class_quaternion.md#class-quaternion-property-y), and [z](class_quaternion.md#class-quaternion-property-z). These components are very compact in memory, and because of this some operations are more efficient and less likely to cause floating-point errors. Methods such as [get_angle()](class_quaternion.md#class-quaternion-method-get-angle), [get_axis()](class_quaternion.md#class-quaternion-method-get-axis), and [slerp()](class_quaternion.md#class-quaternion-method-slerp) are faster than their [Basis](class_basis.md#class-basis) counterparts.

For a great introduction to quaternions, see [this video by 3Blue1Brown](https://www.youtube.com/watch?v=d4EgbgTm0Bg). You do not need to know the math behind quaternions, as Godot provides several helper methods that handle it for you. These include [slerp()](class_quaternion.md#class-quaternion-method-slerp) and [spherical_cubic_interpolate()](class_quaternion.md#class-quaternion-method-spherical-cubic-interpolate), as well as the `*` operator.

**Note:** Quaternions must be normalized before being used for rotation (see [normalized()](class_quaternion.md#class-quaternion-method-normalized)).

**Note:** Similarly to [Vector2](class_vector2.md#class-vector2) and [Vector3](class_vector3.md#class-vector3), the components of a quaternion use 32-bit precision by default, unlike [float](class_float.md#class-float) which is always 64-bit. If double precision is needed, compile the engine with the option `precision=double`.

**Note:** In a boolean context, a quaternion will evaluate to `false` if it's equal to [IDENTITY](class_quaternion.md#class-quaternion-constant-identity). Otherwise, a quaternion will always evaluate to `true`.

Note

There are notable differences when using this API with C#. See [C# API differences to GDScript](../tutorials/scripting/c_sharp/c_sharp_differences.md#doc-c-sharp-differences) for more information.

<a id="tutorials"></a>

## Tutorials

- [3Blue1Brown's video on Quaternions](https://www.youtube.com/watch?v=d4EgbgTm0Bg)
- [Online Quaternion Visualization](https://quaternions.online/)
- [Using 3D transforms](../tutorials/3d/using_transforms.md#interpolating-with-quaternions)
- [Third Person Shooter (TPS) Demo](https://godotengine.org/asset-library/asset/2710)
- [Advanced Quaternion Visualization](https://iwatake2222.github.io/rotation_master/rotation_master.html)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [w](class_quaternion.md#class-quaternion-property-w) | `1.0` |
| [float](class_float.md#class-float) | [x](class_quaternion.md#class-quaternion-property-x) | `0.0` |
| [float](class_float.md#class-float) | [y](class_quaternion.md#class-quaternion-property-y) | `0.0` |
| [float](class_float.md#class-float) | [z](class_quaternion.md#class-quaternion-property-z) | `0.0` |

<a id="constructors"></a>

## Constructors

|  |  |
| --- | --- |
| [Quaternion](class_quaternion.md#class-quaternion) | [Quaternion](class_quaternion.md#class-quaternion-constructor-quaternion)() |
| [Quaternion](class_quaternion.md#class-quaternion) | [Quaternion](class_quaternion.md#class-quaternion-constructor-quaternion)(from: [Quaternion](class_quaternion.md#class-quaternion)) |
| [Quaternion](class_quaternion.md#class-quaternion) | [Quaternion](class_quaternion.md#class-quaternion-constructor-quaternion)(arc_from: [Vector3](class_vector3.md#class-vector3), arc_to: [Vector3](class_vector3.md#class-vector3)) |
| [Quaternion](class_quaternion.md#class-quaternion) | [Quaternion](class_quaternion.md#class-quaternion-constructor-quaternion)(axis: [Vector3](class_vector3.md#class-vector3), angle: [float](class_float.md#class-float)) |
| [Quaternion](class_quaternion.md#class-quaternion) | [Quaternion](class_quaternion.md#class-quaternion-constructor-quaternion)(from: [Basis](class_basis.md#class-basis)) |
| [Quaternion](class_quaternion.md#class-quaternion) | [Quaternion](class_quaternion.md#class-quaternion-constructor-quaternion)(x: [float](class_float.md#class-float), y: [float](class_float.md#class-float), z: [float](class_float.md#class-float), w: [float](class_float.md#class-float)) |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [float](class_float.md#class-float) | [angle_to](class_quaternion.md#class-quaternion-method-angle-to)(to: [Quaternion](class_quaternion.md#class-quaternion)) const |
| [float](class_float.md#class-float) | [dot](class_quaternion.md#class-quaternion-method-dot)(with: [Quaternion](class_quaternion.md#class-quaternion)) const |
| [Quaternion](class_quaternion.md#class-quaternion) | [exp](class_quaternion.md#class-quaternion-method-exp)() const |
| [Quaternion](class_quaternion.md#class-quaternion) | [from_euler](class_quaternion.md#class-quaternion-method-from-euler)(euler: [Vector3](class_vector3.md#class-vector3)) static |
| [float](class_float.md#class-float) | [get_angle](class_quaternion.md#class-quaternion-method-get-angle)() const |
| [Vector3](class_vector3.md#class-vector3) | [get_axis](class_quaternion.md#class-quaternion-method-get-axis)() const |
| [Vector3](class_vector3.md#class-vector3) | [get_euler](class_quaternion.md#class-quaternion-method-get-euler)(order: [int](class_int.md#class-int) = 2) const |
| [Quaternion](class_quaternion.md#class-quaternion) | [inverse](class_quaternion.md#class-quaternion-method-inverse)() const |
| [bool](class_bool.md#class-bool) | [is_equal_approx](class_quaternion.md#class-quaternion-method-is-equal-approx)(to: [Quaternion](class_quaternion.md#class-quaternion)) const |
| [bool](class_bool.md#class-bool) | [is_finite](class_quaternion.md#class-quaternion-method-is-finite)() const |
| [bool](class_bool.md#class-bool) | [is_normalized](class_quaternion.md#class-quaternion-method-is-normalized)() const |
| [float](class_float.md#class-float) | [length](class_quaternion.md#class-quaternion-method-length)() const |
| [float](class_float.md#class-float) | [length_squared](class_quaternion.md#class-quaternion-method-length-squared)() const |
| [Quaternion](class_quaternion.md#class-quaternion) | [log](class_quaternion.md#class-quaternion-method-log)() const |
| [Quaternion](class_quaternion.md#class-quaternion) | [normalized](class_quaternion.md#class-quaternion-method-normalized)() const |
| [Quaternion](class_quaternion.md#class-quaternion) | [slerp](class_quaternion.md#class-quaternion-method-slerp)(to: [Quaternion](class_quaternion.md#class-quaternion), weight: [float](class_float.md#class-float)) const |
| [Quaternion](class_quaternion.md#class-quaternion) | [slerpni](class_quaternion.md#class-quaternion-method-slerpni)(to: [Quaternion](class_quaternion.md#class-quaternion), weight: [float](class_float.md#class-float)) const |
| [Quaternion](class_quaternion.md#class-quaternion) | [spherical_cubic_interpolate](class_quaternion.md#class-quaternion-method-spherical-cubic-interpolate)(b: [Quaternion](class_quaternion.md#class-quaternion), pre_a: [Quaternion](class_quaternion.md#class-quaternion), post_b: [Quaternion](class_quaternion.md#class-quaternion), weight: [float](class_float.md#class-float)) const |
| [Quaternion](class_quaternion.md#class-quaternion) | [spherical_cubic_interpolate_in_time](class_quaternion.md#class-quaternion-method-spherical-cubic-interpolate-in-time)(b: [Quaternion](class_quaternion.md#class-quaternion), pre_a: [Quaternion](class_quaternion.md#class-quaternion), post_b: [Quaternion](class_quaternion.md#class-quaternion), weight: [float](class_float.md#class-float), b_t: [float](class_float.md#class-float), pre_a_t: [float](class_float.md#class-float), post_b_t: [float](class_float.md#class-float)) const |

<a id="operators"></a>

## Operators

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [operator !=](class_quaternion.md#class-quaternion-operator-neq-quaternion)(right: [Quaternion](class_quaternion.md#class-quaternion)) |
| [Quaternion](class_quaternion.md#class-quaternion) | [operator \*](class_quaternion.md#class-quaternion-operator-mul-quaternion)(right: [Quaternion](class_quaternion.md#class-quaternion)) |
| [Vector3](class_vector3.md#class-vector3) | [operator \*](class_quaternion.md#class-quaternion-operator-mul-vector3)(right: [Vector3](class_vector3.md#class-vector3)) |
| [Quaternion](class_quaternion.md#class-quaternion) | [operator \*](class_quaternion.md#class-quaternion-operator-mul-float)(right: [float](class_float.md#class-float)) |
| [Quaternion](class_quaternion.md#class-quaternion) | [operator \*](class_quaternion.md#class-quaternion-operator-mul-int)(right: [int](class_int.md#class-int)) |
| [Quaternion](class_quaternion.md#class-quaternion) | [operator +](class_quaternion.md#class-quaternion-operator-sum-quaternion)(right: [Quaternion](class_quaternion.md#class-quaternion)) |
| [Quaternion](class_quaternion.md#class-quaternion) | [operator -](class_quaternion.md#class-quaternion-operator-dif-quaternion)(right: [Quaternion](class_quaternion.md#class-quaternion)) |
| [Quaternion](class_quaternion.md#class-quaternion) | [operator /](class_quaternion.md#class-quaternion-operator-div-float)(right: [float](class_float.md#class-float)) |
| [Quaternion](class_quaternion.md#class-quaternion) | [operator /](class_quaternion.md#class-quaternion-operator-div-int)(right: [int](class_int.md#class-int)) |
| [bool](class_bool.md#class-bool) | [operator ==](class_quaternion.md#class-quaternion-operator-eq-quaternion)(right: [Quaternion](class_quaternion.md#class-quaternion)) |
| [float](class_float.md#class-float) | [operator []](class_quaternion.md#class-quaternion-operator-idx-int)(index: [int](class_int.md#class-int)) |
| [Quaternion](class_quaternion.md#class-quaternion) | [operator unary+](class_quaternion.md#class-quaternion-operator-unplus)() |
| [Quaternion](class_quaternion.md#class-quaternion) | [operator unary-](class_quaternion.md#class-quaternion-operator-unminus)() |

---


<a id="constants"></a>

## Constants

<a id="class-quaternion-constant-identity"></a>

**IDENTITY** = `Quaternion(0, 0, 0, 1)` [🔗](class_quaternion.md#class-quaternion-constant-identity)

The identity quaternion, representing no rotation. This has the same rotation as [Basis.IDENTITY](class_basis.md#class-basis-constant-identity).

If a [Vector3](class_vector3.md#class-vector3) is rotated (multiplied) by this quaternion, it does not change.

**Note:** In GDScript, this constant is equivalent to creating a [Quaternion](class_quaternion.md#class-quaternion-constructor-quaternion) without any arguments. It can be used to make your code clearer, and for consistency with C#.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-quaternion-property-w"></a>

[float](class_float.md#class-float) **w** = `1.0` [🔗](class_quaternion.md#class-quaternion-property-w)

W component of the quaternion. This is the "real" part.

**Note:** Quaternion components should usually not be manipulated directly.

---


<a id="class-quaternion-property-x"></a>

[float](class_float.md#class-float) **x** = `0.0` [🔗](class_quaternion.md#class-quaternion-property-x)

X component of the quaternion. This is the value along the "imaginary" `i` axis.

**Note:** Quaternion components should usually not be manipulated directly.

---


<a id="class-quaternion-property-y"></a>

[float](class_float.md#class-float) **y** = `0.0` [🔗](class_quaternion.md#class-quaternion-property-y)

Y component of the quaternion. This is the value along the "imaginary" `j` axis.

**Note:** Quaternion components should usually not be manipulated directly.

---


<a id="class-quaternion-property-z"></a>

[float](class_float.md#class-float) **z** = `0.0` [🔗](class_quaternion.md#class-quaternion-property-z)

Z component of the quaternion. This is the value along the "imaginary" `k` axis.

**Note:** Quaternion components should usually not be manipulated directly.

---


<a id="constructor-descriptions"></a>

## Constructor Descriptions

<a id="class-quaternion-constructor-quaternion"></a>

[Quaternion](class_quaternion.md#class-quaternion) **Quaternion**() [🔗](class_quaternion.md#class-quaternion-constructor-quaternion)

Constructs a **Quaternion** identical to [IDENTITY](class_quaternion.md#class-quaternion-constant-identity).

**Note:** In C#, this constructs a **Quaternion** with all of its components set to `0.0`.

---

[Quaternion](class_quaternion.md#class-quaternion) **Quaternion**(from: [Quaternion](class_quaternion.md#class-quaternion))

Constructs a **Quaternion** as a copy of the given **Quaternion**.

---

[Quaternion](class_quaternion.md#class-quaternion) **Quaternion**(arc_from: [Vector3](class_vector3.md#class-vector3), arc_to: [Vector3](class_vector3.md#class-vector3))

Constructs a **Quaternion** representing the shortest arc between `arc_from` and `arc_to`. These can be imagined as two points intersecting a sphere's surface, with a radius of `1.0`.

---

[Quaternion](class_quaternion.md#class-quaternion) **Quaternion**(axis: [Vector3](class_vector3.md#class-vector3), angle: [float](class_float.md#class-float))

Constructs a **Quaternion** representing rotation around the `axis` by the given `angle`, in radians. The axis must be a normalized vector.

---

[Quaternion](class_quaternion.md#class-quaternion) **Quaternion**(from: [Basis](class_basis.md#class-basis))

Constructs a **Quaternion** from the given rotation [Basis](class_basis.md#class-basis).

This constructor is faster than [Basis.get_rotation_quaternion()](class_basis.md#class-basis-method-get-rotation-quaternion), but the given basis must be *orthonormalized* (see [Basis.orthonormalized()](class_basis.md#class-basis-method-orthonormalized)). Otherwise, the constructor fails and returns [IDENTITY](class_quaternion.md#class-quaternion-constant-identity).

---

[Quaternion](class_quaternion.md#class-quaternion) **Quaternion**(x: [float](class_float.md#class-float), y: [float](class_float.md#class-float), z: [float](class_float.md#class-float), w: [float](class_float.md#class-float))

Constructs a **Quaternion** defined by the given values.

**Note:** Only normalized quaternions represent rotation; if these values are not normalized, the new **Quaternion** will not be a valid rotation.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-quaternion-method-angle-to"></a>

[float](class_float.md#class-float) **angle_to**(to: [Quaternion](class_quaternion.md#class-quaternion)) const [🔗](class_quaternion.md#class-quaternion-method-angle-to)

Returns the angle between this quaternion and `to`. This is the magnitude of the angle you would need to rotate by to get from one to the other.

**Note:** The magnitude of the floating-point error for this method is abnormally high, so methods such as `is_zero_approx` will not work reliably.

---


<a id="class-quaternion-method-dot"></a>

[float](class_float.md#class-float) **dot**(with: [Quaternion](class_quaternion.md#class-quaternion)) const [🔗](class_quaternion.md#class-quaternion-method-dot)

Returns the dot product between this quaternion and `with`.

This is equivalent to `(quat.x * with.x) + (quat.y * with.y) + (quat.z * with.z) + (quat.w * with.w)`.

---


<a id="class-quaternion-method-exp"></a>

[Quaternion](class_quaternion.md#class-quaternion) **exp**() const [🔗](class_quaternion.md#class-quaternion-method-exp)

Returns the exponential of this quaternion. The rotation axis of the result is the normalized rotation axis of this quaternion, the angle of the result is the length of the vector part of this quaternion.

---


<a id="class-quaternion-method-from-euler"></a>

[Quaternion](class_quaternion.md#class-quaternion) **from_euler**(euler: [Vector3](class_vector3.md#class-vector3)) static [🔗](class_quaternion.md#class-quaternion-method-from-euler)

Constructs a new **Quaternion** from the given [Vector3](class_vector3.md#class-vector3) of [Euler angles](https://en.wikipedia.org/wiki/Euler_angles), in radians. In Godot, Euler angles always use intrinsic order. This method always uses the intrinsic YXZ convention ([@GlobalScope.EULER_ORDER_YXZ](class_@globalscope.md#class-globalscope-constant-euler-order-yxz)).

---


<a id="class-quaternion-method-get-angle"></a>

[float](class_float.md#class-float) **get_angle**() const [🔗](class_quaternion.md#class-quaternion-method-get-angle)

Returns the angle of the rotation represented by this quaternion.

**Note:** The quaternion must be normalized.

---


<a id="class-quaternion-method-get-axis"></a>

[Vector3](class_vector3.md#class-vector3) **get_axis**() const [🔗](class_quaternion.md#class-quaternion-method-get-axis)

Returns the rotation axis of the rotation represented by this quaternion.

---


<a id="class-quaternion-method-get-euler"></a>

[Vector3](class_vector3.md#class-vector3) **get_euler**(order: [int](class_int.md#class-int) = 2) const [🔗](class_quaternion.md#class-quaternion-method-get-euler)

Returns this quaternion's rotation as a [Vector3](class_vector3.md#class-vector3) of [Euler angles](https://en.wikipedia.org/wiki/Euler_angles), in radians.

The order of each consecutive rotation can be changed with `order` (see [EulerOrder](class_@globalscope.md#enum-globalscope-eulerorder) constants). In Godot, Euler angles always use intrinsic order. By default, the intrinsic YXZ convention is used ([@GlobalScope.EULER_ORDER_YXZ](class_@globalscope.md#class-globalscope-constant-euler-order-yxz)): since we are decomposing, local Z (roll) is calculated first, then local X (pitch), and lastly local Y (yaw). When using the opposite method [from_euler()](class_quaternion.md#class-quaternion-method-from-euler) to compose a rotation, this order is reversed.

---


<a id="class-quaternion-method-inverse"></a>

[Quaternion](class_quaternion.md#class-quaternion) **inverse**() const [🔗](class_quaternion.md#class-quaternion-method-inverse)

Returns the inverse version of this quaternion, inverting the sign of every component except [w](class_quaternion.md#class-quaternion-property-w).

---


<a id="class-quaternion-method-is-equal-approx"></a>

[bool](class_bool.md#class-bool) **is_equal_approx**(to: [Quaternion](class_quaternion.md#class-quaternion)) const [🔗](class_quaternion.md#class-quaternion-method-is-equal-approx)

Returns `true` if this quaternion and `to` are approximately equal, by calling [@GlobalScope.is_equal_approx()](class_@globalscope.md#class-globalscope-method-is-equal-approx) on each component.

---


<a id="class-quaternion-method-is-finite"></a>

[bool](class_bool.md#class-bool) **is_finite**() const [🔗](class_quaternion.md#class-quaternion-method-is-finite)

Returns `true` if this quaternion is finite, by calling [@GlobalScope.is_finite()](class_@globalscope.md#class-globalscope-method-is-finite) on each component.

---


<a id="class-quaternion-method-is-normalized"></a>

[bool](class_bool.md#class-bool) **is_normalized**() const [🔗](class_quaternion.md#class-quaternion-method-is-normalized)

Returns `true` if this quaternion is normalized. See also [normalized()](class_quaternion.md#class-quaternion-method-normalized).

---


<a id="class-quaternion-method-length"></a>

[float](class_float.md#class-float) **length**() const [🔗](class_quaternion.md#class-quaternion-method-length)

Returns this quaternion's length, also called magnitude.

---


<a id="class-quaternion-method-length-squared"></a>

[float](class_float.md#class-float) **length_squared**() const [🔗](class_quaternion.md#class-quaternion-method-length-squared)

Returns this quaternion's length, squared.

**Note:** This method is faster than [length()](class_quaternion.md#class-quaternion-method-length), so prefer it if you only need to compare quaternion lengths.

---


<a id="class-quaternion-method-log"></a>

[Quaternion](class_quaternion.md#class-quaternion) **log**() const [🔗](class_quaternion.md#class-quaternion-method-log)

Returns the logarithm of this quaternion. Multiplies this quaternion's rotation axis by its rotation angle, and stores the result in the returned quaternion's vector part ([x](class_quaternion.md#class-quaternion-property-x), [y](class_quaternion.md#class-quaternion-property-y), and [z](class_quaternion.md#class-quaternion-property-z)). The returned quaternion's real part ([w](class_quaternion.md#class-quaternion-property-w)) is always `0.0`.

---


<a id="class-quaternion-method-normalized"></a>

[Quaternion](class_quaternion.md#class-quaternion) **normalized**() const [🔗](class_quaternion.md#class-quaternion-method-normalized)

Returns a copy of this quaternion, normalized so that its length is `1.0`. See also [is_normalized()](class_quaternion.md#class-quaternion-method-is-normalized).

---


<a id="class-quaternion-method-slerp"></a>

[Quaternion](class_quaternion.md#class-quaternion) **slerp**(to: [Quaternion](class_quaternion.md#class-quaternion), weight: [float](class_float.md#class-float)) const [🔗](class_quaternion.md#class-quaternion-method-slerp)

Performs a spherical-linear interpolation with the `to` quaternion, given a `weight` and returns the result. Both this quaternion and `to` must be normalized.

---


<a id="class-quaternion-method-slerpni"></a>

[Quaternion](class_quaternion.md#class-quaternion) **slerpni**(to: [Quaternion](class_quaternion.md#class-quaternion), weight: [float](class_float.md#class-float)) const [🔗](class_quaternion.md#class-quaternion-method-slerpni)

Performs a spherical-linear interpolation with the `to` quaternion, given a `weight` and returns the result. Unlike [slerp()](class_quaternion.md#class-quaternion-method-slerp), this method does not check if the rotation path is smaller than 90 degrees. Both this quaternion and `to` must be normalized.

---


<a id="class-quaternion-method-spherical-cubic-interpolate"></a>

[Quaternion](class_quaternion.md#class-quaternion) **spherical_cubic_interpolate**(b: [Quaternion](class_quaternion.md#class-quaternion), pre_a: [Quaternion](class_quaternion.md#class-quaternion), post_b: [Quaternion](class_quaternion.md#class-quaternion), weight: [float](class_float.md#class-float)) const [🔗](class_quaternion.md#class-quaternion-method-spherical-cubic-interpolate)

Performs a spherical cubic interpolation between quaternions `pre_a`, this vector, `b`, and `post_b`, by the given amount `weight`.

---


<a id="class-quaternion-method-spherical-cubic-interpolate-in-time"></a>

[Quaternion](class_quaternion.md#class-quaternion) **spherical_cubic_interpolate_in_time**(b: [Quaternion](class_quaternion.md#class-quaternion), pre_a: [Quaternion](class_quaternion.md#class-quaternion), post_b: [Quaternion](class_quaternion.md#class-quaternion), weight: [float](class_float.md#class-float), b_t: [float](class_float.md#class-float), pre_a_t: [float](class_float.md#class-float), post_b_t: [float](class_float.md#class-float)) const [🔗](class_quaternion.md#class-quaternion-method-spherical-cubic-interpolate-in-time)

Performs a spherical cubic interpolation between quaternions `pre_a`, this vector, `b`, and `post_b`, by the given amount `weight`.

It can perform smoother interpolation than [spherical_cubic_interpolate()](class_quaternion.md#class-quaternion-method-spherical-cubic-interpolate) by the time values.

---


<a id="operator-descriptions"></a>

## Operator Descriptions

<a id="class-quaternion-operator-neq-quaternion"></a>

[bool](class_bool.md#class-bool) **operator !=**(right: [Quaternion](class_quaternion.md#class-quaternion)) [🔗](class_quaternion.md#class-quaternion-operator-neq-quaternion)

Returns `true` if the components of both quaternions are not exactly equal.

**Note:** Due to floating-point precision errors, consider using [is_equal_approx()](class_quaternion.md#class-quaternion-method-is-equal-approx) instead, which is more reliable.

---


<a id="class-quaternion-operator-mul-quaternion"></a>

[Quaternion](class_quaternion.md#class-quaternion) **operator \***(right: [Quaternion](class_quaternion.md#class-quaternion)) [🔗](class_quaternion.md#class-quaternion-operator-mul-quaternion)

Composes (multiplies) two quaternions. This rotates the `right` quaternion (the child) by this quaternion (the parent).

---


<a id="class-quaternion-operator-mul-vector3"></a>

[Vector3](class_vector3.md#class-vector3) **operator \***(right: [Vector3](class_vector3.md#class-vector3)) [🔗](class_quaternion.md#class-quaternion-operator-mul-vector3)

Rotates (multiplies) the `right` vector by this quaternion, returning a [Vector3](class_vector3.md#class-vector3).

---


<a id="class-quaternion-operator-mul-float"></a>

[Quaternion](class_quaternion.md#class-quaternion) **operator \***(right: [float](class_float.md#class-float)) [🔗](class_quaternion.md#class-quaternion-operator-mul-float)

Multiplies each component of the **Quaternion** by the right [float](class_float.md#class-float) value.

This operation is not meaningful on its own, but it can be used as a part of a larger expression.

---


<a id="class-quaternion-operator-mul-int"></a>

[Quaternion](class_quaternion.md#class-quaternion) **operator \***(right: [int](class_int.md#class-int)) [🔗](class_quaternion.md#class-quaternion-operator-mul-int)

Multiplies each component of the **Quaternion** by the right [int](class_int.md#class-int) value.

This operation is not meaningful on its own, but it can be used as a part of a larger expression.

---


<a id="class-quaternion-operator-sum-quaternion"></a>

[Quaternion](class_quaternion.md#class-quaternion) **operator +**(right: [Quaternion](class_quaternion.md#class-quaternion)) [🔗](class_quaternion.md#class-quaternion-operator-sum-quaternion)

Adds each component of the left **Quaternion** to the right **Quaternion**.

This operation is not meaningful on its own, but it can be used as a part of a larger expression, such as approximating an intermediate rotation between two nearby rotations.

---


<a id="class-quaternion-operator-dif-quaternion"></a>

[Quaternion](class_quaternion.md#class-quaternion) **operator -**(right: [Quaternion](class_quaternion.md#class-quaternion)) [🔗](class_quaternion.md#class-quaternion-operator-dif-quaternion)

Subtracts each component of the left **Quaternion** by the right **Quaternion**.

This operation is not meaningful on its own, but it can be used as a part of a larger expression.

---


<a id="class-quaternion-operator-div-float"></a>

[Quaternion](class_quaternion.md#class-quaternion) **operator /**(right: [float](class_float.md#class-float)) [🔗](class_quaternion.md#class-quaternion-operator-div-float)

Divides each component of the **Quaternion** by the right [float](class_float.md#class-float) value.

This operation is not meaningful on its own, but it can be used as a part of a larger expression.

---


<a id="class-quaternion-operator-div-int"></a>

[Quaternion](class_quaternion.md#class-quaternion) **operator /**(right: [int](class_int.md#class-int)) [🔗](class_quaternion.md#class-quaternion-operator-div-int)

Divides each component of the **Quaternion** by the right [int](class_int.md#class-int) value.

This operation is not meaningful on its own, but it can be used as a part of a larger expression.

---


<a id="class-quaternion-operator-eq-quaternion"></a>

[bool](class_bool.md#class-bool) **operator ==**(right: [Quaternion](class_quaternion.md#class-quaternion)) [🔗](class_quaternion.md#class-quaternion-operator-eq-quaternion)

Returns `true` if the components of both quaternions are exactly equal.

**Note:** Due to floating-point precision errors, consider using [is_equal_approx()](class_quaternion.md#class-quaternion-method-is-equal-approx) instead, which is more reliable.

---


<a id="class-quaternion-operator-idx-int"></a>

[float](class_float.md#class-float) **operator []**(index: [int](class_int.md#class-int)) [🔗](class_quaternion.md#class-quaternion-operator-idx-int)

Accesses each component of this quaternion by their index.

Index `0` is the same as [x](class_quaternion.md#class-quaternion-property-x), index `1` is the same as [y](class_quaternion.md#class-quaternion-property-y), index `2` is the same as [z](class_quaternion.md#class-quaternion-property-z), and index `3` is the same as [w](class_quaternion.md#class-quaternion-property-w).

---


<a id="class-quaternion-operator-unplus"></a>

[Quaternion](class_quaternion.md#class-quaternion) **operator unary+**() [🔗](class_quaternion.md#class-quaternion-operator-unplus)

Returns the same value as if the `+` was not there. Unary `+` does nothing, but sometimes it can make your code more readable.

---


<a id="class-quaternion-operator-unminus"></a>

[Quaternion](class_quaternion.md#class-quaternion) **operator unary-**() [🔗](class_quaternion.md#class-quaternion-operator-unminus)

Returns the negative value of the **Quaternion**. This is the same as multiplying all components by `-1`. This operation results in a quaternion that represents the same rotation.
