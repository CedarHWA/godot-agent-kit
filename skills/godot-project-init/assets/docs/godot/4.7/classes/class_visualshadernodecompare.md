> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodecompare.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodecompare"></a>

<a id="class-visualshadernodecompare"></a>

# VisualShaderNodeCompare

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A comparison function for common types within the visual shader graph.

<a id="description"></a>

## Description

Compares `a` and `b` of [type](class_visualshadernodecompare.md#class-visualshadernodecompare-property-type) by [function](class_visualshadernodecompare.md#class-visualshadernodecompare-property-function). Returns a boolean scalar. Translates to `if` instruction in shader code.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Condition](class_visualshadernodecompare.md#enum-visualshadernodecompare-condition) | [condition](class_visualshadernodecompare.md#class-visualshadernodecompare-property-condition) | `0` |
| [Function](class_visualshadernodecompare.md#enum-visualshadernodecompare-function) | [function](class_visualshadernodecompare.md#class-visualshadernodecompare-property-function) | `0` |
| [ComparisonType](class_visualshadernodecompare.md#enum-visualshadernodecompare-comparisontype) | [type](class_visualshadernodecompare.md#class-visualshadernodecompare-property-type) | `0` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-visualshadernodecompare-comparisontype"></a>

enum **ComparisonType**: [🔗](class_visualshadernodecompare.md#enum-visualshadernodecompare-comparisontype)

<a id="class-visualshadernodecompare-constant-ctype-scalar"></a>

[ComparisonType](class_visualshadernodecompare.md#enum-visualshadernodecompare-comparisontype) **CTYPE_SCALAR** = `0`

A floating-point scalar.

<a id="class-visualshadernodecompare-constant-ctype-scalar-int"></a>

[ComparisonType](class_visualshadernodecompare.md#enum-visualshadernodecompare-comparisontype) **CTYPE_SCALAR_INT** = `1`

An integer scalar.

<a id="class-visualshadernodecompare-constant-ctype-scalar-uint"></a>

[ComparisonType](class_visualshadernodecompare.md#enum-visualshadernodecompare-comparisontype) **CTYPE_SCALAR_UINT** = `2`

An unsigned integer scalar.

<a id="class-visualshadernodecompare-constant-ctype-vector-2d"></a>

[ComparisonType](class_visualshadernodecompare.md#enum-visualshadernodecompare-comparisontype) **CTYPE_VECTOR_2D** = `3`

A 2D vector type.

<a id="class-visualshadernodecompare-constant-ctype-vector-3d"></a>

[ComparisonType](class_visualshadernodecompare.md#enum-visualshadernodecompare-comparisontype) **CTYPE_VECTOR_3D** = `4`

A 3D vector type.

<a id="class-visualshadernodecompare-constant-ctype-vector-4d"></a>

[ComparisonType](class_visualshadernodecompare.md#enum-visualshadernodecompare-comparisontype) **CTYPE_VECTOR_4D** = `5`

A 4D vector type.

<a id="class-visualshadernodecompare-constant-ctype-boolean"></a>

[ComparisonType](class_visualshadernodecompare.md#enum-visualshadernodecompare-comparisontype) **CTYPE_BOOLEAN** = `6`

A boolean type.

<a id="class-visualshadernodecompare-constant-ctype-transform"></a>

[ComparisonType](class_visualshadernodecompare.md#enum-visualshadernodecompare-comparisontype) **CTYPE_TRANSFORM** = `7`

A transform (`mat4`) type.

<a id="class-visualshadernodecompare-constant-ctype-max"></a>

[ComparisonType](class_visualshadernodecompare.md#enum-visualshadernodecompare-comparisontype) **CTYPE_MAX** = `8`

Represents the size of the [ComparisonType](class_visualshadernodecompare.md#enum-visualshadernodecompare-comparisontype) enum.

---


<a id="enum-visualshadernodecompare-function"></a>

enum **Function**: [🔗](class_visualshadernodecompare.md#enum-visualshadernodecompare-function)

<a id="class-visualshadernodecompare-constant-func-equal"></a>

[Function](class_visualshadernodecompare.md#enum-visualshadernodecompare-function) **FUNC_EQUAL** = `0`

Comparison for equality (`a == b`).

<a id="class-visualshadernodecompare-constant-func-not-equal"></a>

[Function](class_visualshadernodecompare.md#enum-visualshadernodecompare-function) **FUNC_NOT_EQUAL** = `1`

Comparison for inequality (`a != b`).

<a id="class-visualshadernodecompare-constant-func-greater-than"></a>

[Function](class_visualshadernodecompare.md#enum-visualshadernodecompare-function) **FUNC_GREATER_THAN** = `2`

Comparison for greater than (`a > b`). Cannot be used if [type](class_visualshadernodecompare.md#class-visualshadernodecompare-property-type) set to [CTYPE_BOOLEAN](class_visualshadernodecompare.md#class-visualshadernodecompare-constant-ctype-boolean) or [CTYPE_TRANSFORM](class_visualshadernodecompare.md#class-visualshadernodecompare-constant-ctype-transform).

<a id="class-visualshadernodecompare-constant-func-greater-than-equal"></a>

[Function](class_visualshadernodecompare.md#enum-visualshadernodecompare-function) **FUNC_GREATER_THAN_EQUAL** = `3`

Comparison for greater than or equal (`a >= b`). Cannot be used if [type](class_visualshadernodecompare.md#class-visualshadernodecompare-property-type) set to [CTYPE_BOOLEAN](class_visualshadernodecompare.md#class-visualshadernodecompare-constant-ctype-boolean) or [CTYPE_TRANSFORM](class_visualshadernodecompare.md#class-visualshadernodecompare-constant-ctype-transform).

<a id="class-visualshadernodecompare-constant-func-less-than"></a>

[Function](class_visualshadernodecompare.md#enum-visualshadernodecompare-function) **FUNC_LESS_THAN** = `4`

Comparison for less than (`a < b`). Cannot be used if [type](class_visualshadernodecompare.md#class-visualshadernodecompare-property-type) set to [CTYPE_BOOLEAN](class_visualshadernodecompare.md#class-visualshadernodecompare-constant-ctype-boolean) or [CTYPE_TRANSFORM](class_visualshadernodecompare.md#class-visualshadernodecompare-constant-ctype-transform).

<a id="class-visualshadernodecompare-constant-func-less-than-equal"></a>

[Function](class_visualshadernodecompare.md#enum-visualshadernodecompare-function) **FUNC_LESS_THAN_EQUAL** = `5`

Comparison for less than or equal (`a <= b`). Cannot be used if [type](class_visualshadernodecompare.md#class-visualshadernodecompare-property-type) set to [CTYPE_BOOLEAN](class_visualshadernodecompare.md#class-visualshadernodecompare-constant-ctype-boolean) or [CTYPE_TRANSFORM](class_visualshadernodecompare.md#class-visualshadernodecompare-constant-ctype-transform).

<a id="class-visualshadernodecompare-constant-func-max"></a>

[Function](class_visualshadernodecompare.md#enum-visualshadernodecompare-function) **FUNC_MAX** = `6`

Represents the size of the [Function](class_visualshadernodecompare.md#enum-visualshadernodecompare-function) enum.

---


<a id="enum-visualshadernodecompare-condition"></a>

enum **Condition**: [🔗](class_visualshadernodecompare.md#enum-visualshadernodecompare-condition)

<a id="class-visualshadernodecompare-constant-cond-all"></a>

[Condition](class_visualshadernodecompare.md#enum-visualshadernodecompare-condition) **COND_ALL** = `0`

The result will be `true` if all components in the vector satisfy the comparison condition.

<a id="class-visualshadernodecompare-constant-cond-any"></a>

[Condition](class_visualshadernodecompare.md#enum-visualshadernodecompare-condition) **COND_ANY** = `1`

The result will be `true` if any component in the vector satisfies the comparison condition.

<a id="class-visualshadernodecompare-constant-cond-max"></a>

[Condition](class_visualshadernodecompare.md#enum-visualshadernodecompare-condition) **COND_MAX** = `2`

Represents the size of the [Condition](class_visualshadernodecompare.md#enum-visualshadernodecompare-condition) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodecompare-property-condition"></a>

[Condition](class_visualshadernodecompare.md#enum-visualshadernodecompare-condition) **condition** = `0` [🔗](class_visualshadernodecompare.md#class-visualshadernodecompare-property-condition)

- void **set_condition**(value: [Condition](class_visualshadernodecompare.md#enum-visualshadernodecompare-condition))
- [Condition](class_visualshadernodecompare.md#enum-visualshadernodecompare-condition) **get_condition**()

Extra condition which is applied if [type](class_visualshadernodecompare.md#class-visualshadernodecompare-property-type) is set to [CTYPE_VECTOR_3D](class_visualshadernodecompare.md#class-visualshadernodecompare-constant-ctype-vector-3d).

---


<a id="class-visualshadernodecompare-property-function"></a>

[Function](class_visualshadernodecompare.md#enum-visualshadernodecompare-function) **function** = `0` [🔗](class_visualshadernodecompare.md#class-visualshadernodecompare-property-function)

- void **set_function**(value: [Function](class_visualshadernodecompare.md#enum-visualshadernodecompare-function))
- [Function](class_visualshadernodecompare.md#enum-visualshadernodecompare-function) **get_function**()

A comparison function.

---


<a id="class-visualshadernodecompare-property-type"></a>

[ComparisonType](class_visualshadernodecompare.md#enum-visualshadernodecompare-comparisontype) **type** = `0` [🔗](class_visualshadernodecompare.md#class-visualshadernodecompare-property-type)

- void **set_comparison_type**(value: [ComparisonType](class_visualshadernodecompare.md#enum-visualshadernodecompare-comparisontype))
- [ComparisonType](class_visualshadernodecompare.md#enum-visualshadernodecompare-comparisontype) **get_comparison_type**()

The type to be used in the comparison.
