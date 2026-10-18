> Source: https://docs.godotengine.org/en/4.7/classes/class_plane.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="plane"></a>

<a id="class-plane"></a>

# Plane

A plane in Hessian normal form.

<a id="description"></a>

## Description

Represents a normalized plane equation. [normal](class_plane.md#class-plane-property-normal) is the normal of the plane (a, b, c normalized), and [d](class_plane.md#class-plane-property-d) is the distance from the origin to the plane (in the direction of "normal"). "Over" or "Above" the plane is considered the side of the plane towards where the normal is pointing.

**Note:** In a boolean context, a plane will evaluate to `false` if all its components equal `0`. Otherwise, a plane will always evaluate to `true`.

<a id="tutorials"></a>

## Tutorials

- [Math documentation index](../tutorials/math/index.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [d](class_plane.md#class-plane-property-d) | `0.0` |
| [Vector3](class_vector3.md#class-vector3) | [normal](class_plane.md#class-plane-property-normal) | `Vector3(0, 0, 0)` |
| [float](class_float.md#class-float) | [x](class_plane.md#class-plane-property-x) | `0.0` |
| [float](class_float.md#class-float) | [y](class_plane.md#class-plane-property-y) | `0.0` |
| [float](class_float.md#class-float) | [z](class_plane.md#class-plane-property-z) | `0.0` |

<a id="constructors"></a>

## Constructors

|  |  |
| --- | --- |
| [Plane](class_plane.md#class-plane) | [Plane](class_plane.md#class-plane-constructor-plane)() |
| [Plane](class_plane.md#class-plane) | [Plane](class_plane.md#class-plane-constructor-plane)(from: [Plane](class_plane.md#class-plane)) |
| [Plane](class_plane.md#class-plane) | [Plane](class_plane.md#class-plane-constructor-plane)(a: [float](class_float.md#class-float), b: [float](class_float.md#class-float), c: [float](class_float.md#class-float), d: [float](class_float.md#class-float)) |
| [Plane](class_plane.md#class-plane) | [Plane](class_plane.md#class-plane-constructor-plane)(normal: [Vector3](class_vector3.md#class-vector3)) |
| [Plane](class_plane.md#class-plane) | [Plane](class_plane.md#class-plane-constructor-plane)(normal: [Vector3](class_vector3.md#class-vector3), d: [float](class_float.md#class-float)) |
| [Plane](class_plane.md#class-plane) | [Plane](class_plane.md#class-plane-constructor-plane)(normal: [Vector3](class_vector3.md#class-vector3), point: [Vector3](class_vector3.md#class-vector3)) |
| [Plane](class_plane.md#class-plane) | [Plane](class_plane.md#class-plane-constructor-plane)(point1: [Vector3](class_vector3.md#class-vector3), point2: [Vector3](class_vector3.md#class-vector3), point3: [Vector3](class_vector3.md#class-vector3)) |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [float](class_float.md#class-float) | [distance_to](class_plane.md#class-plane-method-distance-to)(point: [Vector3](class_vector3.md#class-vector3)) const |
| [Vector3](class_vector3.md#class-vector3) | [get_center](class_plane.md#class-plane-method-get-center)() const |
| [bool](class_bool.md#class-bool) | [has_point](class_plane.md#class-plane-method-has-point)(point: [Vector3](class_vector3.md#class-vector3), tolerance: [float](class_float.md#class-float) = 1e-05) const |
| [Variant](class_variant.md#class-variant) | [intersect_3](class_plane.md#class-plane-method-intersect-3)(b: [Plane](class_plane.md#class-plane), c: [Plane](class_plane.md#class-plane)) const |
| [Variant](class_variant.md#class-variant) | [intersects_ray](class_plane.md#class-plane-method-intersects-ray)(from: [Vector3](class_vector3.md#class-vector3), dir: [Vector3](class_vector3.md#class-vector3)) const |
| [Variant](class_variant.md#class-variant) | [intersects_segment](class_plane.md#class-plane-method-intersects-segment)(from: [Vector3](class_vector3.md#class-vector3), to: [Vector3](class_vector3.md#class-vector3)) const |
| [bool](class_bool.md#class-bool) | [is_equal_approx](class_plane.md#class-plane-method-is-equal-approx)(to_plane: [Plane](class_plane.md#class-plane)) const |
| [bool](class_bool.md#class-bool) | [is_finite](class_plane.md#class-plane-method-is-finite)() const |
| [bool](class_bool.md#class-bool) | [is_point_over](class_plane.md#class-plane-method-is-point-over)(point: [Vector3](class_vector3.md#class-vector3)) const |
| [Plane](class_plane.md#class-plane) | [normalized](class_plane.md#class-plane-method-normalized)() const |
| [Vector3](class_vector3.md#class-vector3) | [project](class_plane.md#class-plane-method-project)(point: [Vector3](class_vector3.md#class-vector3)) const |

<a id="operators"></a>

## Operators

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [operator !=](class_plane.md#class-plane-operator-neq-plane)(right: [Plane](class_plane.md#class-plane)) |
| [Plane](class_plane.md#class-plane) | [operator \*](class_plane.md#class-plane-operator-mul-transform3d)(right: [Transform3D](class_transform3d.md#class-transform3d)) |
| [bool](class_bool.md#class-bool) | [operator ==](class_plane.md#class-plane-operator-eq-plane)(right: [Plane](class_plane.md#class-plane)) |
| [Plane](class_plane.md#class-plane) | [operator unary+](class_plane.md#class-plane-operator-unplus)() |
| [Plane](class_plane.md#class-plane) | [operator unary-](class_plane.md#class-plane-operator-unminus)() |

---


<a id="constants"></a>

## Constants

<a id="class-plane-constant-plane-yz"></a>

**PLANE_YZ** = `Plane(1, 0, 0, 0)` [🔗](class_plane.md#class-plane-constant-plane-yz)

A plane that extends in the Y and Z axes (normal vector points +X).

<a id="class-plane-constant-plane-xz"></a>

**PLANE_XZ** = `Plane(0, 1, 0, 0)` [🔗](class_plane.md#class-plane-constant-plane-xz)

A plane that extends in the X and Z axes (normal vector points +Y).

<a id="class-plane-constant-plane-xy"></a>

**PLANE_XY** = `Plane(0, 0, 1, 0)` [🔗](class_plane.md#class-plane-constant-plane-xy)

A plane that extends in the X and Y axes (normal vector points +Z).

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-plane-property-d"></a>

[float](class_float.md#class-float) **d** = `0.0` [🔗](class_plane.md#class-plane-property-d)

The distance from the origin to the plane, expressed in terms of [normal](class_plane.md#class-plane-property-normal) (according to its direction and magnitude). Actual absolute distance from the origin to the plane can be calculated as `abs(d) / normal.length()` (if [normal](class_plane.md#class-plane-property-normal) has zero length then this **Plane** does not represent a valid plane).

In the scalar equation of the plane `ax + by + cz = d`, this is `d`, while the `(a, b, c)` coordinates are represented by the [normal](class_plane.md#class-plane-property-normal) property.

---


<a id="class-plane-property-normal"></a>

[Vector3](class_vector3.md#class-vector3) **normal** = `Vector3(0, 0, 0)` [🔗](class_plane.md#class-plane-property-normal)

The normal of the plane, typically a unit vector. Shouldn't be a zero vector as **Plane** with such [normal](class_plane.md#class-plane-property-normal) does not represent a valid plane.

In the scalar equation of the plane `ax + by + cz = d`, this is the vector `(a, b, c)`, where `d` is the [d](class_plane.md#class-plane-property-d) property.

---


<a id="class-plane-property-x"></a>

[float](class_float.md#class-float) **x** = `0.0` [🔗](class_plane.md#class-plane-property-x)

The X component of the plane's [normal](class_plane.md#class-plane-property-normal) vector.

---


<a id="class-plane-property-y"></a>

[float](class_float.md#class-float) **y** = `0.0` [🔗](class_plane.md#class-plane-property-y)

The Y component of the plane's [normal](class_plane.md#class-plane-property-normal) vector.

---


<a id="class-plane-property-z"></a>

[float](class_float.md#class-float) **z** = `0.0` [🔗](class_plane.md#class-plane-property-z)

The Z component of the plane's [normal](class_plane.md#class-plane-property-normal) vector.

---


<a id="constructor-descriptions"></a>

## Constructor Descriptions

<a id="class-plane-constructor-plane"></a>

[Plane](class_plane.md#class-plane) **Plane**() [🔗](class_plane.md#class-plane-constructor-plane)

Constructs a default-initialized **Plane** with all components set to `0`.

---

[Plane](class_plane.md#class-plane) **Plane**(from: [Plane](class_plane.md#class-plane))

Constructs a **Plane** as a copy of the given **Plane**.

---

[Plane](class_plane.md#class-plane) **Plane**(a: [float](class_float.md#class-float), b: [float](class_float.md#class-float), c: [float](class_float.md#class-float), d: [float](class_float.md#class-float))

Creates a plane from the four parameters. The three components of the resulting plane's [normal](class_plane.md#class-plane-property-normal) are `a`, `b` and `c`, and the plane has a distance of `d` from the origin.

---

[Plane](class_plane.md#class-plane) **Plane**(normal: [Vector3](class_vector3.md#class-vector3))

Creates a plane from the normal vector. The plane will intersect the origin.

The `normal` of the plane must be a unit vector.

---

[Plane](class_plane.md#class-plane) **Plane**(normal: [Vector3](class_vector3.md#class-vector3), d: [float](class_float.md#class-float))

Creates a plane from the normal vector and the plane's distance from the origin.

The `normal` of the plane must be a unit vector.

---

[Plane](class_plane.md#class-plane) **Plane**(normal: [Vector3](class_vector3.md#class-vector3), point: [Vector3](class_vector3.md#class-vector3))

Creates a plane from the normal vector and a point on the plane.

The `normal` of the plane must be a unit vector.

---

[Plane](class_plane.md#class-plane) **Plane**(point1: [Vector3](class_vector3.md#class-vector3), point2: [Vector3](class_vector3.md#class-vector3), point3: [Vector3](class_vector3.md#class-vector3))

Creates a plane from the three points, given in clockwise order.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-plane-method-distance-to"></a>

[float](class_float.md#class-float) **distance_to**(point: [Vector3](class_vector3.md#class-vector3)) const [🔗](class_plane.md#class-plane-method-distance-to)

Returns the shortest distance from the plane to the position `point`. If the point is above the plane, the distance will be positive. If below, the distance will be negative.

---


<a id="class-plane-method-get-center"></a>

[Vector3](class_vector3.md#class-vector3) **get_center**() const [🔗](class_plane.md#class-plane-method-get-center)

Returns the center of the plane.

---


<a id="class-plane-method-has-point"></a>

[bool](class_bool.md#class-bool) **has_point**(point: [Vector3](class_vector3.md#class-vector3), tolerance: [float](class_float.md#class-float) = 1e-05) const [🔗](class_plane.md#class-plane-method-has-point)

Returns `true` if `point` is inside the plane. Comparison uses a custom minimum `tolerance` threshold.

---


<a id="class-plane-method-intersect-3"></a>

[Variant](class_variant.md#class-variant) **intersect_3**(b: [Plane](class_plane.md#class-plane), c: [Plane](class_plane.md#class-plane)) const [🔗](class_plane.md#class-plane-method-intersect-3)

Returns the intersection point of the three planes `b`, `c` and this plane. If no intersection is found, `null` is returned.

---


<a id="class-plane-method-intersects-ray"></a>

[Variant](class_variant.md#class-variant) **intersects_ray**(from: [Vector3](class_vector3.md#class-vector3), dir: [Vector3](class_vector3.md#class-vector3)) const [🔗](class_plane.md#class-plane-method-intersects-ray)

Returns the intersection point of a ray consisting of the position `from` and the direction normal `dir` with this plane. If no intersection is found, `null` is returned.

---


<a id="class-plane-method-intersects-segment"></a>

[Variant](class_variant.md#class-variant) **intersects_segment**(from: [Vector3](class_vector3.md#class-vector3), to: [Vector3](class_vector3.md#class-vector3)) const [🔗](class_plane.md#class-plane-method-intersects-segment)

Returns the intersection point of a segment from position `from` to position `to` with this plane. If no intersection is found, `null` is returned.

---


<a id="class-plane-method-is-equal-approx"></a>

[bool](class_bool.md#class-bool) **is_equal_approx**(to_plane: [Plane](class_plane.md#class-plane)) const [🔗](class_plane.md#class-plane-method-is-equal-approx)

Returns `true` if this plane and `to_plane` are approximately equal, by running [@GlobalScope.is_equal_approx()](class_@globalscope.md#class-globalscope-method-is-equal-approx) on each component.

---


<a id="class-plane-method-is-finite"></a>

[bool](class_bool.md#class-bool) **is_finite**() const [🔗](class_plane.md#class-plane-method-is-finite)

Returns `true` if this plane is finite, by calling [@GlobalScope.is_finite()](class_@globalscope.md#class-globalscope-method-is-finite) on each component.

---


<a id="class-plane-method-is-point-over"></a>

[bool](class_bool.md#class-bool) **is_point_over**(point: [Vector3](class_vector3.md#class-vector3)) const [🔗](class_plane.md#class-plane-method-is-point-over)

Returns `true` if `point` is located above the plane.

---


<a id="class-plane-method-normalized"></a>

[Plane](class_plane.md#class-plane) **normalized**() const [🔗](class_plane.md#class-plane-method-normalized)

Returns a copy of the plane, with normalized [normal](class_plane.md#class-plane-property-normal) (so it's a unit vector). Returns `Plane(0, 0, 0, 0)` if [normal](class_plane.md#class-plane-property-normal) can't be normalized (it has zero length).

---


<a id="class-plane-method-project"></a>

[Vector3](class_vector3.md#class-vector3) **project**(point: [Vector3](class_vector3.md#class-vector3)) const [🔗](class_plane.md#class-plane-method-project)

Returns the orthogonal projection of `point` into a point in the plane.

---


<a id="operator-descriptions"></a>

## Operator Descriptions

<a id="class-plane-operator-neq-plane"></a>

[bool](class_bool.md#class-bool) **operator !=**(right: [Plane](class_plane.md#class-plane)) [🔗](class_plane.md#class-plane-operator-neq-plane)

Returns `true` if the planes are not equal.

**Note:** Due to floating-point precision errors, consider using [is_equal_approx()](class_plane.md#class-plane-method-is-equal-approx) instead, which is more reliable.

---


<a id="class-plane-operator-mul-transform3d"></a>

[Plane](class_plane.md#class-plane) **operator \***(right: [Transform3D](class_transform3d.md#class-transform3d)) [🔗](class_plane.md#class-plane-operator-mul-transform3d)

Inversely transforms (multiplies) the **Plane** by the given [Transform3D](class_transform3d.md#class-transform3d) transformation matrix.

`plane * transform` is equivalent to `transform.affine_inverse() * plane`. See [Transform3D.affine_inverse()](class_transform3d.md#class-transform3d-method-affine-inverse).

---


<a id="class-plane-operator-eq-plane"></a>

[bool](class_bool.md#class-bool) **operator ==**(right: [Plane](class_plane.md#class-plane)) [🔗](class_plane.md#class-plane-operator-eq-plane)

Returns `true` if the planes are exactly equal.

**Note:** Due to floating-point precision errors, consider using [is_equal_approx()](class_plane.md#class-plane-method-is-equal-approx) instead, which is more reliable.

---


<a id="class-plane-operator-unplus"></a>

[Plane](class_plane.md#class-plane) **operator unary+**() [🔗](class_plane.md#class-plane-operator-unplus)

Returns the same value as if the `+` was not there. Unary `+` does nothing, but sometimes it can make your code more readable.

---


<a id="class-plane-operator-unminus"></a>

[Plane](class_plane.md#class-plane) **operator unary-**() [🔗](class_plane.md#class-plane-operator-unminus)

Returns the negative value of the **Plane**. This is the same as writing `Plane(-p.normal, -p.d)`. This operation flips the direction of the normal vector and also flips the distance value, resulting in a Plane that is in the same place, but facing the opposite direction.
