> Source: https://docs.godotengine.org/en/4.7/classes/class_packedcolorarray.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="packedcolorarray"></a>

<a id="class-packedcolorarray"></a>

# PackedColorArray

A packed array of [Color](class_color.md#class-color)s.

<a id="description"></a>

## Description

An array specifically designed to hold [Color](class_color.md#class-color). Packs data tightly, so it saves memory for large array sizes.

**Differences between packed arrays, typed arrays, and untyped arrays:** Packed arrays are generally faster to iterate on and modify compared to a typed array of the same type (e.g. **PackedColorArray** versus `Array[Color]`). Also, packed arrays consume less memory. As a downside, packed arrays are less flexible as they don't offer as many convenience methods such as [Array.map()](class_array.md#class-array-method-map). Typed arrays are in turn faster to iterate on and modify than untyped arrays.

**Note:** Packed arrays are always passed by reference. To get a copy of an array that can be modified independently of the original array, use [duplicate()](class_packedcolorarray.md#class-packedcolorarray-method-duplicate). This is *not* the case for built-in properties and methods. In these cases the returned packed array is a copy, and changing it will *not* affect the original value. To update a built-in property of this type, modify the returned array and then assign it to the property again.

**Note:** In a boolean context, a packed array will evaluate to `false` if it's empty. Otherwise, a packed array will always evaluate to `true`.

Note

There are notable differences when using this API with C#. See [C# API differences to GDScript](../tutorials/scripting/c_sharp/c_sharp_differences.md#doc-c-sharp-differences) for more information.

<a id="constructors"></a>

## Constructors

|  |  |
| --- | --- |
| [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) | [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray-constructor-packedcolorarray)() |
| [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) | [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray-constructor-packedcolorarray)(from: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray)) |
| [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) | [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray-constructor-packedcolorarray)(from: [Array](class_array.md#class-array)) |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [append](class_packedcolorarray.md#class-packedcolorarray-method-append)(value: [Color](class_color.md#class-color)) |
| void | [append_array](class_packedcolorarray.md#class-packedcolorarray-method-append-array)(array: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray)) |
| [int](class_int.md#class-int) | [bsearch](class_packedcolorarray.md#class-packedcolorarray-method-bsearch)(value: [Color](class_color.md#class-color), before: [bool](class_bool.md#class-bool) = true) const |
| void | [clear](class_packedcolorarray.md#class-packedcolorarray-method-clear)() |
| [int](class_int.md#class-int) | [count](class_packedcolorarray.md#class-packedcolorarray-method-count)(value: [Color](class_color.md#class-color)) const |
| [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) | [duplicate](class_packedcolorarray.md#class-packedcolorarray-method-duplicate)() const |
| [bool](class_bool.md#class-bool) | [erase](class_packedcolorarray.md#class-packedcolorarray-method-erase)(value: [Color](class_color.md#class-color)) |
| void | [fill](class_packedcolorarray.md#class-packedcolorarray-method-fill)(value: [Color](class_color.md#class-color)) |
| [int](class_int.md#class-int) | [find](class_packedcolorarray.md#class-packedcolorarray-method-find)(value: [Color](class_color.md#class-color), from: [int](class_int.md#class-int) = 0) const |
| [Color](class_color.md#class-color) | [get](class_packedcolorarray.md#class-packedcolorarray-method-get)(index: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [has](class_packedcolorarray.md#class-packedcolorarray-method-has)(value: [Color](class_color.md#class-color)) const |
| [int](class_int.md#class-int) | [insert](class_packedcolorarray.md#class-packedcolorarray-method-insert)(at_index: [int](class_int.md#class-int), value: [Color](class_color.md#class-color)) |
| [bool](class_bool.md#class-bool) | [is_empty](class_packedcolorarray.md#class-packedcolorarray-method-is-empty)() const |
| [bool](class_bool.md#class-bool) | [push_back](class_packedcolorarray.md#class-packedcolorarray-method-push-back)(value: [Color](class_color.md#class-color)) |
| void | [remove_at](class_packedcolorarray.md#class-packedcolorarray-method-remove-at)(index: [int](class_int.md#class-int)) |
| [int](class_int.md#class-int) | [resize](class_packedcolorarray.md#class-packedcolorarray-method-resize)(new_size: [int](class_int.md#class-int)) |
| void | [reverse](class_packedcolorarray.md#class-packedcolorarray-method-reverse)() |
| [int](class_int.md#class-int) | [rfind](class_packedcolorarray.md#class-packedcolorarray-method-rfind)(value: [Color](class_color.md#class-color), from: [int](class_int.md#class-int) = -1) const |
| void | [set](class_packedcolorarray.md#class-packedcolorarray-method-set)(index: [int](class_int.md#class-int), value: [Color](class_color.md#class-color)) |
| [int](class_int.md#class-int) | [size](class_packedcolorarray.md#class-packedcolorarray-method-size)() const |
| [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) | [slice](class_packedcolorarray.md#class-packedcolorarray-method-slice)(begin: [int](class_int.md#class-int), end: [int](class_int.md#class-int) = 2147483647) const |
| void | [sort](class_packedcolorarray.md#class-packedcolorarray-method-sort)() |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray) | [to_byte_array](class_packedcolorarray.md#class-packedcolorarray-method-to-byte-array)() const |

<a id="operators"></a>

## Operators

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [operator !=](class_packedcolorarray.md#class-packedcolorarray-operator-neq-packedcolorarray)(right: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray)) |
| [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) | [operator +](class_packedcolorarray.md#class-packedcolorarray-operator-sum-packedcolorarray)(right: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray)) |
| [bool](class_bool.md#class-bool) | [operator ==](class_packedcolorarray.md#class-packedcolorarray-operator-eq-packedcolorarray)(right: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray)) |
| [Color](class_color.md#class-color) | [operator []](class_packedcolorarray.md#class-packedcolorarray-operator-idx-int)(index: [int](class_int.md#class-int)) |

---


<a id="constructor-descriptions"></a>

## Constructor Descriptions

<a id="class-packedcolorarray-constructor-packedcolorarray"></a>

[PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) **PackedColorArray**() [🔗](class_packedcolorarray.md#class-packedcolorarray-constructor-packedcolorarray)

Constructs an empty **PackedColorArray**.

---

[PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) **PackedColorArray**(from: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray))

Constructs a **PackedColorArray** as a copy of the given **PackedColorArray**.

---

[PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) **PackedColorArray**(from: [Array](class_array.md#class-array))

Constructs a new **PackedColorArray**. Optionally, you can pass in a generic [Array](class_array.md#class-array) that will be converted.

**Note:** When initializing a **PackedColorArray** with elements, it must be initialized with an [Array](class_array.md#class-array) of [Color](class_color.md#class-color) values:

```gdscript
var array = PackedColorArray([Color(0.1, 0.2, 0.3), Color(0.4, 0.5, 0.6)])
```

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-packedcolorarray-method-append"></a>

[bool](class_bool.md#class-bool) **append**(value: [Color](class_color.md#class-color)) [🔗](class_packedcolorarray.md#class-packedcolorarray-method-append)

Appends an element at the end of the array (alias of [push_back()](class_packedcolorarray.md#class-packedcolorarray-method-push-back)).

---


<a id="class-packedcolorarray-method-append-array"></a>

void **append_array**(array: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray)) [🔗](class_packedcolorarray.md#class-packedcolorarray-method-append-array)

Appends a **PackedColorArray** at the end of this array.

---


<a id="class-packedcolorarray-method-bsearch"></a>

[int](class_int.md#class-int) **bsearch**(value: [Color](class_color.md#class-color), before: [bool](class_bool.md#class-bool) = true) const [🔗](class_packedcolorarray.md#class-packedcolorarray-method-bsearch)

Finds the index of an existing value (or the insertion index that maintains sorting order, if the value is not yet present in the array) using binary search. Optionally, a `before` specifier can be passed. If `false`, the returned index comes after all existing entries of the value in the array.

**Note:** Calling [bsearch()](class_packedcolorarray.md#class-packedcolorarray-method-bsearch) on an unsorted array results in unexpected behavior.

---


<a id="class-packedcolorarray-method-clear"></a>

void **clear**() [🔗](class_packedcolorarray.md#class-packedcolorarray-method-clear)

Clears the array. This is equivalent to using [resize()](class_packedcolorarray.md#class-packedcolorarray-method-resize) with a size of `0`.

---


<a id="class-packedcolorarray-method-count"></a>

[int](class_int.md#class-int) **count**(value: [Color](class_color.md#class-color)) const [🔗](class_packedcolorarray.md#class-packedcolorarray-method-count)

Returns the number of times an element is in the array.

---


<a id="class-packedcolorarray-method-duplicate"></a>

[PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) **duplicate**() const [🔗](class_packedcolorarray.md#class-packedcolorarray-method-duplicate)

Creates a copy of the array, and returns it.

---


<a id="class-packedcolorarray-method-erase"></a>

[bool](class_bool.md#class-bool) **erase**(value: [Color](class_color.md#class-color)) [🔗](class_packedcolorarray.md#class-packedcolorarray-method-erase)

Removes the first occurrence of a value from the array and returns `true`. If the value does not exist in the array, nothing happens and `false` is returned. To remove an element by index, use [remove_at()](class_packedcolorarray.md#class-packedcolorarray-method-remove-at) instead.

---


<a id="class-packedcolorarray-method-fill"></a>

void **fill**(value: [Color](class_color.md#class-color)) [🔗](class_packedcolorarray.md#class-packedcolorarray-method-fill)

Assigns the given value to all elements in the array. This can typically be used together with [resize()](class_packedcolorarray.md#class-packedcolorarray-method-resize) to create an array with a given size and initialized elements.

---


<a id="class-packedcolorarray-method-find"></a>

[int](class_int.md#class-int) **find**(value: [Color](class_color.md#class-color), from: [int](class_int.md#class-int) = 0) const [🔗](class_packedcolorarray.md#class-packedcolorarray-method-find)

Searches the array for a value and returns its index or `-1` if not found. Optionally, the initial search index can be passed.

---


<a id="class-packedcolorarray-method-get"></a>

[Color](class_color.md#class-color) **get**(index: [int](class_int.md#class-int)) const [🔗](class_packedcolorarray.md#class-packedcolorarray-method-get)

Returns the [Color](class_color.md#class-color) at the given `index` in the array. If `index` is out-of-bounds or negative, this method fails and returns `Color(0, 0, 0, 1)`.

This method is similar (but not identical) to the `[]` operator. Most notably, when this method fails, it doesn't pause project execution if run from the editor.

---


<a id="class-packedcolorarray-method-has"></a>

[bool](class_bool.md#class-bool) **has**(value: [Color](class_color.md#class-color)) const [🔗](class_packedcolorarray.md#class-packedcolorarray-method-has)

Returns `true` if the array contains `value`.

---


<a id="class-packedcolorarray-method-insert"></a>

[int](class_int.md#class-int) **insert**(at_index: [int](class_int.md#class-int), value: [Color](class_color.md#class-color)) [🔗](class_packedcolorarray.md#class-packedcolorarray-method-insert)

Inserts a new element at a given position in the array. The position must be valid, or at the end of the array (`idx == size()`).

---


<a id="class-packedcolorarray-method-is-empty"></a>

[bool](class_bool.md#class-bool) **is_empty**() const [🔗](class_packedcolorarray.md#class-packedcolorarray-method-is-empty)

Returns `true` if the array is empty.

---


<a id="class-packedcolorarray-method-push-back"></a>

[bool](class_bool.md#class-bool) **push_back**(value: [Color](class_color.md#class-color)) [🔗](class_packedcolorarray.md#class-packedcolorarray-method-push-back)

Appends a value to the array.

---


<a id="class-packedcolorarray-method-remove-at"></a>

void **remove_at**(index: [int](class_int.md#class-int)) [🔗](class_packedcolorarray.md#class-packedcolorarray-method-remove-at)

Removes an element from the array by index.

---


<a id="class-packedcolorarray-method-resize"></a>

[int](class_int.md#class-int) **resize**(new_size: [int](class_int.md#class-int)) [🔗](class_packedcolorarray.md#class-packedcolorarray-method-resize)

Sets the size of the array. If the array is grown, reserves elements at the end of the array. If the array is shrunk, truncates the array to the new size. Calling [resize()](class_packedcolorarray.md#class-packedcolorarray-method-resize) once and assigning the new values is faster than adding new elements one by one.

Returns [@GlobalScope.OK](class_@globalscope.md#class-globalscope-constant-ok) on success, or one of the following [Error](class_@globalscope.md#enum-globalscope-error) constants if this method fails: [@GlobalScope.ERR_INVALID_PARAMETER](class_@globalscope.md#class-globalscope-constant-err-invalid-parameter) if the size is negative, or [@GlobalScope.ERR_OUT_OF_MEMORY](class_@globalscope.md#class-globalscope-constant-err-out-of-memory) if allocations fail. Use [size()](class_packedcolorarray.md#class-packedcolorarray-method-size) to find the actual size of the array after resize.

---


<a id="class-packedcolorarray-method-reverse"></a>

void **reverse**() [🔗](class_packedcolorarray.md#class-packedcolorarray-method-reverse)

Reverses the order of the elements in the array.

---


<a id="class-packedcolorarray-method-rfind"></a>

[int](class_int.md#class-int) **rfind**(value: [Color](class_color.md#class-color), from: [int](class_int.md#class-int) = -1) const [🔗](class_packedcolorarray.md#class-packedcolorarray-method-rfind)

Searches the array in reverse order. Optionally, a start search index can be passed. If negative, the start index is considered relative to the end of the array.

---


<a id="class-packedcolorarray-method-set"></a>

void **set**(index: [int](class_int.md#class-int), value: [Color](class_color.md#class-color)) [🔗](class_packedcolorarray.md#class-packedcolorarray-method-set)

Changes the [Color](class_color.md#class-color) at the given index.

---


<a id="class-packedcolorarray-method-size"></a>

[int](class_int.md#class-int) **size**() const [🔗](class_packedcolorarray.md#class-packedcolorarray-method-size)

Returns the number of elements in the array.

---


<a id="class-packedcolorarray-method-slice"></a>

[PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) **slice**(begin: [int](class_int.md#class-int), end: [int](class_int.md#class-int) = 2147483647) const [🔗](class_packedcolorarray.md#class-packedcolorarray-method-slice)

Returns the slice of the **PackedColorArray**, from `begin` (inclusive) to `end` (exclusive), as a new **PackedColorArray**.

The absolute value of `begin` and `end` will be clamped to the array size, so the default value for `end` makes it slice to the size of the array by default (i.e. `arr.slice(1)` is a shorthand for `arr.slice(1, arr.size())`).

If either `begin` or `end` are negative, they will be relative to the end of the array (i.e. `arr.slice(0, -2)` is a shorthand for `arr.slice(0, arr.size() - 2)`).

---


<a id="class-packedcolorarray-method-sort"></a>

void **sort**() [🔗](class_packedcolorarray.md#class-packedcolorarray-method-sort)

Sorts the elements of the array in ascending order.

---


<a id="class-packedcolorarray-method-to-byte-array"></a>

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **to_byte_array**() const [🔗](class_packedcolorarray.md#class-packedcolorarray-method-to-byte-array)

Returns a [PackedByteArray](class_packedbytearray.md#class-packedbytearray) with each color encoded as bytes.

---


<a id="operator-descriptions"></a>

## Operator Descriptions

<a id="class-packedcolorarray-operator-neq-packedcolorarray"></a>

[bool](class_bool.md#class-bool) **operator !=**(right: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray)) [🔗](class_packedcolorarray.md#class-packedcolorarray-operator-neq-packedcolorarray)

Returns `true` if contents of the arrays differ.

---


<a id="class-packedcolorarray-operator-sum-packedcolorarray"></a>

[PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) **operator +**(right: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray)) [🔗](class_packedcolorarray.md#class-packedcolorarray-operator-sum-packedcolorarray)

Returns a new **PackedColorArray** with contents of `right` added at the end of this array. For better performance, consider using [append_array()](class_packedcolorarray.md#class-packedcolorarray-method-append-array) instead.

---


<a id="class-packedcolorarray-operator-eq-packedcolorarray"></a>

[bool](class_bool.md#class-bool) **operator ==**(right: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray)) [🔗](class_packedcolorarray.md#class-packedcolorarray-operator-eq-packedcolorarray)

Returns `true` if contents of both arrays are the same, i.e. they have all equal [Color](class_color.md#class-color)s at the corresponding indices.

---


<a id="class-packedcolorarray-operator-idx-int"></a>

[Color](class_color.md#class-color) **operator []**(index: [int](class_int.md#class-int)) [🔗](class_packedcolorarray.md#class-packedcolorarray-operator-idx-int)

Returns the [Color](class_color.md#class-color) at index `index`. Negative indices can be used to access the elements starting from the end. Using index out of array's bounds will result in an error.
