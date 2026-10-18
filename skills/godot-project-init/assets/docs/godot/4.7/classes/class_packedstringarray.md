> Source: https://docs.godotengine.org/en/4.7/classes/class_packedstringarray.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="packedstringarray"></a>

<a id="class-packedstringarray"></a>

# PackedStringArray

A packed array of [String](class_string.md#class-string)s.

<a id="description"></a>

## Description

An array specifically designed to hold [String](class_string.md#class-string)s. Packs data tightly, so it saves memory for large array sizes.

If you want to join the strings in the array, use [String.join()](class_string.md#class-string-method-join).

```gdscript
var string_array = PackedStringArray(["hello", "world"])
var string = " ".join(string_array)
print(string) # "hello world"
```

**Differences between packed arrays, typed arrays, and untyped arrays:** Packed arrays are generally faster to iterate on and modify compared to a typed array of the same type (e.g. **PackedStringArray** versus `Array[String]`). Also, packed arrays consume less memory. As a downside, packed arrays are less flexible as they don't offer as many convenience methods such as [Array.map()](class_array.md#class-array-method-map). Typed arrays are in turn faster to iterate on and modify than untyped arrays.

**Note:** Packed arrays are always passed by reference. To get a copy of an array that can be modified independently of the original array, use [duplicate()](class_packedstringarray.md#class-packedstringarray-method-duplicate). This is *not* the case for built-in properties and methods. In these cases the returned packed array is a copy, and changing it will *not* affect the original value. To update a built-in property of this type, modify the returned array and then assign it to the property again.

**Note:** In a boolean context, a packed array will evaluate to `false` if it's empty. Otherwise, a packed array will always evaluate to `true`.

Note

There are notable differences when using this API with C#. See [C# API differences to GDScript](../tutorials/scripting/c_sharp/c_sharp_differences.md#doc-c-sharp-differences) for more information.

<a id="tutorials"></a>

## Tutorials

- [Operating System Testing Demo](https://godotengine.org/asset-library/asset/2789)

<a id="constructors"></a>

## Constructors

|  |  |
| --- | --- |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [PackedStringArray](class_packedstringarray.md#class-packedstringarray-constructor-packedstringarray)() |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [PackedStringArray](class_packedstringarray.md#class-packedstringarray-constructor-packedstringarray)(from: [PackedStringArray](class_packedstringarray.md#class-packedstringarray)) |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [PackedStringArray](class_packedstringarray.md#class-packedstringarray-constructor-packedstringarray)(from: [Array](class_array.md#class-array)) |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [append](class_packedstringarray.md#class-packedstringarray-method-append)(value: [String](class_string.md#class-string)) |
| void | [append_array](class_packedstringarray.md#class-packedstringarray-method-append-array)(array: [PackedStringArray](class_packedstringarray.md#class-packedstringarray)) |
| [int](class_int.md#class-int) | [bsearch](class_packedstringarray.md#class-packedstringarray-method-bsearch)(value: [String](class_string.md#class-string), before: [bool](class_bool.md#class-bool) = true) const |
| void | [clear](class_packedstringarray.md#class-packedstringarray-method-clear)() |
| [int](class_int.md#class-int) | [count](class_packedstringarray.md#class-packedstringarray-method-count)(value: [String](class_string.md#class-string)) const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [duplicate](class_packedstringarray.md#class-packedstringarray-method-duplicate)() const |
| [bool](class_bool.md#class-bool) | [erase](class_packedstringarray.md#class-packedstringarray-method-erase)(value: [String](class_string.md#class-string)) |
| void | [fill](class_packedstringarray.md#class-packedstringarray-method-fill)(value: [String](class_string.md#class-string)) |
| [int](class_int.md#class-int) | [find](class_packedstringarray.md#class-packedstringarray-method-find)(value: [String](class_string.md#class-string), from: [int](class_int.md#class-int) = 0) const |
| [String](class_string.md#class-string) | [get](class_packedstringarray.md#class-packedstringarray-method-get)(index: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [has](class_packedstringarray.md#class-packedstringarray-method-has)(value: [String](class_string.md#class-string)) const |
| [int](class_int.md#class-int) | [insert](class_packedstringarray.md#class-packedstringarray-method-insert)(at_index: [int](class_int.md#class-int), value: [String](class_string.md#class-string)) |
| [bool](class_bool.md#class-bool) | [is_empty](class_packedstringarray.md#class-packedstringarray-method-is-empty)() const |
| [bool](class_bool.md#class-bool) | [push_back](class_packedstringarray.md#class-packedstringarray-method-push-back)(value: [String](class_string.md#class-string)) |
| void | [remove_at](class_packedstringarray.md#class-packedstringarray-method-remove-at)(index: [int](class_int.md#class-int)) |
| [int](class_int.md#class-int) | [resize](class_packedstringarray.md#class-packedstringarray-method-resize)(new_size: [int](class_int.md#class-int)) |
| void | [reverse](class_packedstringarray.md#class-packedstringarray-method-reverse)() |
| [int](class_int.md#class-int) | [rfind](class_packedstringarray.md#class-packedstringarray-method-rfind)(value: [String](class_string.md#class-string), from: [int](class_int.md#class-int) = -1) const |
| void | [set](class_packedstringarray.md#class-packedstringarray-method-set)(index: [int](class_int.md#class-int), value: [String](class_string.md#class-string)) |
| [int](class_int.md#class-int) | [size](class_packedstringarray.md#class-packedstringarray-method-size)() const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [slice](class_packedstringarray.md#class-packedstringarray-method-slice)(begin: [int](class_int.md#class-int), end: [int](class_int.md#class-int) = 2147483647) const |
| void | [sort](class_packedstringarray.md#class-packedstringarray-method-sort)() |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray) | [to_byte_array](class_packedstringarray.md#class-packedstringarray-method-to-byte-array)() const |

<a id="operators"></a>

## Operators

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [operator !=](class_packedstringarray.md#class-packedstringarray-operator-neq-packedstringarray)(right: [PackedStringArray](class_packedstringarray.md#class-packedstringarray)) |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [operator +](class_packedstringarray.md#class-packedstringarray-operator-sum-packedstringarray)(right: [PackedStringArray](class_packedstringarray.md#class-packedstringarray)) |
| [bool](class_bool.md#class-bool) | [operator ==](class_packedstringarray.md#class-packedstringarray-operator-eq-packedstringarray)(right: [PackedStringArray](class_packedstringarray.md#class-packedstringarray)) |
| [String](class_string.md#class-string) | [operator []](class_packedstringarray.md#class-packedstringarray-operator-idx-int)(index: [int](class_int.md#class-int)) |

---


<a id="constructor-descriptions"></a>

## Constructor Descriptions

<a id="class-packedstringarray-constructor-packedstringarray"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **PackedStringArray**() [🔗](class_packedstringarray.md#class-packedstringarray-constructor-packedstringarray)

Constructs an empty **PackedStringArray**.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **PackedStringArray**(from: [PackedStringArray](class_packedstringarray.md#class-packedstringarray))

Constructs a **PackedStringArray** as a copy of the given **PackedStringArray**.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **PackedStringArray**(from: [Array](class_array.md#class-array))

Constructs a new **PackedStringArray**. Optionally, you can pass in a generic [Array](class_array.md#class-array) that will be converted.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-packedstringarray-method-append"></a>

[bool](class_bool.md#class-bool) **append**(value: [String](class_string.md#class-string)) [🔗](class_packedstringarray.md#class-packedstringarray-method-append)

Appends an element at the end of the array (alias of [push_back()](class_packedstringarray.md#class-packedstringarray-method-push-back)).

---


<a id="class-packedstringarray-method-append-array"></a>

void **append_array**(array: [PackedStringArray](class_packedstringarray.md#class-packedstringarray)) [🔗](class_packedstringarray.md#class-packedstringarray-method-append-array)

Appends a **PackedStringArray** at the end of this array.

---


<a id="class-packedstringarray-method-bsearch"></a>

[int](class_int.md#class-int) **bsearch**(value: [String](class_string.md#class-string), before: [bool](class_bool.md#class-bool) = true) const [🔗](class_packedstringarray.md#class-packedstringarray-method-bsearch)

Finds the index of an existing value (or the insertion index that maintains sorting order, if the value is not yet present in the array) using binary search. Optionally, a `before` specifier can be passed. If `false`, the returned index comes after all existing entries of the value in the array.

**Note:** Calling [bsearch()](class_packedstringarray.md#class-packedstringarray-method-bsearch) on an unsorted array results in unexpected behavior.

---


<a id="class-packedstringarray-method-clear"></a>

void **clear**() [🔗](class_packedstringarray.md#class-packedstringarray-method-clear)

Clears the array. This is equivalent to using [resize()](class_packedstringarray.md#class-packedstringarray-method-resize) with a size of `0`.

---


<a id="class-packedstringarray-method-count"></a>

[int](class_int.md#class-int) **count**(value: [String](class_string.md#class-string)) const [🔗](class_packedstringarray.md#class-packedstringarray-method-count)

Returns the number of times an element is in the array.

---


<a id="class-packedstringarray-method-duplicate"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **duplicate**() const [🔗](class_packedstringarray.md#class-packedstringarray-method-duplicate)

Creates a copy of the array, and returns it.

---


<a id="class-packedstringarray-method-erase"></a>

[bool](class_bool.md#class-bool) **erase**(value: [String](class_string.md#class-string)) [🔗](class_packedstringarray.md#class-packedstringarray-method-erase)

Removes the first occurrence of a value from the array and returns `true`. If the value does not exist in the array, nothing happens and `false` is returned. To remove an element by index, use [remove_at()](class_packedstringarray.md#class-packedstringarray-method-remove-at) instead.

---


<a id="class-packedstringarray-method-fill"></a>

void **fill**(value: [String](class_string.md#class-string)) [🔗](class_packedstringarray.md#class-packedstringarray-method-fill)

Assigns the given value to all elements in the array. This can typically be used together with [resize()](class_packedstringarray.md#class-packedstringarray-method-resize) to create an array with a given size and initialized elements.

---


<a id="class-packedstringarray-method-find"></a>

[int](class_int.md#class-int) **find**(value: [String](class_string.md#class-string), from: [int](class_int.md#class-int) = 0) const [🔗](class_packedstringarray.md#class-packedstringarray-method-find)

Searches the array for a value and returns its index or `-1` if not found. Optionally, the initial search index can be passed.

---


<a id="class-packedstringarray-method-get"></a>

[String](class_string.md#class-string) **get**(index: [int](class_int.md#class-int)) const [🔗](class_packedstringarray.md#class-packedstringarray-method-get)

Returns the [String](class_string.md#class-string) at the given `index` in the array. If `index` is out-of-bounds or negative, this method fails and returns an empty string.

This method is similar (but not identical) to the `[]` operator. Most notably, when this method fails, it doesn't pause project execution if run from the editor.

---


<a id="class-packedstringarray-method-has"></a>

[bool](class_bool.md#class-bool) **has**(value: [String](class_string.md#class-string)) const [🔗](class_packedstringarray.md#class-packedstringarray-method-has)

Returns `true` if the array contains `value`.

---


<a id="class-packedstringarray-method-insert"></a>

[int](class_int.md#class-int) **insert**(at_index: [int](class_int.md#class-int), value: [String](class_string.md#class-string)) [🔗](class_packedstringarray.md#class-packedstringarray-method-insert)

Inserts a new element at a given position in the array. The position must be valid, or at the end of the array (`idx == size()`).

---


<a id="class-packedstringarray-method-is-empty"></a>

[bool](class_bool.md#class-bool) **is_empty**() const [🔗](class_packedstringarray.md#class-packedstringarray-method-is-empty)

Returns `true` if the array is empty.

---


<a id="class-packedstringarray-method-push-back"></a>

[bool](class_bool.md#class-bool) **push_back**(value: [String](class_string.md#class-string)) [🔗](class_packedstringarray.md#class-packedstringarray-method-push-back)

Appends a string element at end of the array.

---


<a id="class-packedstringarray-method-remove-at"></a>

void **remove_at**(index: [int](class_int.md#class-int)) [🔗](class_packedstringarray.md#class-packedstringarray-method-remove-at)

Removes an element from the array by index.

---


<a id="class-packedstringarray-method-resize"></a>

[int](class_int.md#class-int) **resize**(new_size: [int](class_int.md#class-int)) [🔗](class_packedstringarray.md#class-packedstringarray-method-resize)

Sets the size of the array. If the array is grown, reserves elements at the end of the array. If the array is shrunk, truncates the array to the new size. Calling [resize()](class_packedstringarray.md#class-packedstringarray-method-resize) once and assigning the new values is faster than adding new elements one by one.

Returns [@GlobalScope.OK](class_@globalscope.md#class-globalscope-constant-ok) on success, or one of the following [Error](class_@globalscope.md#enum-globalscope-error) constants if this method fails: [@GlobalScope.ERR_INVALID_PARAMETER](class_@globalscope.md#class-globalscope-constant-err-invalid-parameter) if the size is negative, or [@GlobalScope.ERR_OUT_OF_MEMORY](class_@globalscope.md#class-globalscope-constant-err-out-of-memory) if allocations fail. Use [size()](class_packedstringarray.md#class-packedstringarray-method-size) to find the actual size of the array after resize.

---


<a id="class-packedstringarray-method-reverse"></a>

void **reverse**() [🔗](class_packedstringarray.md#class-packedstringarray-method-reverse)

Reverses the order of the elements in the array.

---


<a id="class-packedstringarray-method-rfind"></a>

[int](class_int.md#class-int) **rfind**(value: [String](class_string.md#class-string), from: [int](class_int.md#class-int) = -1) const [🔗](class_packedstringarray.md#class-packedstringarray-method-rfind)

Searches the array in reverse order. Optionally, a start search index can be passed. If negative, the start index is considered relative to the end of the array.

---


<a id="class-packedstringarray-method-set"></a>

void **set**(index: [int](class_int.md#class-int), value: [String](class_string.md#class-string)) [🔗](class_packedstringarray.md#class-packedstringarray-method-set)

Changes the [String](class_string.md#class-string) at the given index.

---


<a id="class-packedstringarray-method-size"></a>

[int](class_int.md#class-int) **size**() const [🔗](class_packedstringarray.md#class-packedstringarray-method-size)

Returns the number of elements in the array.

---


<a id="class-packedstringarray-method-slice"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **slice**(begin: [int](class_int.md#class-int), end: [int](class_int.md#class-int) = 2147483647) const [🔗](class_packedstringarray.md#class-packedstringarray-method-slice)

Returns the slice of the **PackedStringArray**, from `begin` (inclusive) to `end` (exclusive), as a new **PackedStringArray**.

The absolute value of `begin` and `end` will be clamped to the array size, so the default value for `end` makes it slice to the size of the array by default (i.e. `arr.slice(1)` is a shorthand for `arr.slice(1, arr.size())`).

If either `begin` or `end` are negative, they will be relative to the end of the array (i.e. `arr.slice(0, -2)` is a shorthand for `arr.slice(0, arr.size() - 2)`).

---


<a id="class-packedstringarray-method-sort"></a>

void **sort**() [🔗](class_packedstringarray.md#class-packedstringarray-method-sort)

Sorts the elements of the array in ascending order.

---


<a id="class-packedstringarray-method-to-byte-array"></a>

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **to_byte_array**() const [🔗](class_packedstringarray.md#class-packedstringarray-method-to-byte-array)

Returns a [PackedByteArray](class_packedbytearray.md#class-packedbytearray) with each string encoded as UTF-8. Strings are `null` terminated.

---


<a id="operator-descriptions"></a>

## Operator Descriptions

<a id="class-packedstringarray-operator-neq-packedstringarray"></a>

[bool](class_bool.md#class-bool) **operator !=**(right: [PackedStringArray](class_packedstringarray.md#class-packedstringarray)) [🔗](class_packedstringarray.md#class-packedstringarray-operator-neq-packedstringarray)

Returns `true` if contents of the arrays differ.

---


<a id="class-packedstringarray-operator-sum-packedstringarray"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **operator +**(right: [PackedStringArray](class_packedstringarray.md#class-packedstringarray)) [🔗](class_packedstringarray.md#class-packedstringarray-operator-sum-packedstringarray)

Returns a new **PackedStringArray** with contents of `right` added at the end of this array. For better performance, consider using [append_array()](class_packedstringarray.md#class-packedstringarray-method-append-array) instead.

---


<a id="class-packedstringarray-operator-eq-packedstringarray"></a>

[bool](class_bool.md#class-bool) **operator ==**(right: [PackedStringArray](class_packedstringarray.md#class-packedstringarray)) [🔗](class_packedstringarray.md#class-packedstringarray-operator-eq-packedstringarray)

Returns `true` if contents of both arrays are the same, i.e. they have all equal [String](class_string.md#class-string)s at the corresponding indices.

---


<a id="class-packedstringarray-operator-idx-int"></a>

[String](class_string.md#class-string) **operator []**(index: [int](class_int.md#class-int)) [🔗](class_packedstringarray.md#class-packedstringarray-operator-idx-int)

Returns the [String](class_string.md#class-string) at index `index`. Negative indices can be used to access the elements starting from the end. Using index out of array's bounds will result in an error.
