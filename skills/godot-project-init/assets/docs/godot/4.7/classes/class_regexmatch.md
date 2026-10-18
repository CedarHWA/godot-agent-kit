> Source: https://docs.godotengine.org/en/4.7/classes/class_regexmatch.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="regexmatch"></a>

<a id="class-regexmatch"></a>

# RegExMatch

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Contains the results of a [RegEx](class_regex.md#class-regex) search.

<a id="description"></a>

## Description

Contains the results of a single [RegEx](class_regex.md#class-regex) match returned by [RegEx.search()](class_regex.md#class-regex-method-search) and [RegEx.search_all()](class_regex.md#class-regex-method-search-all). It can be used to find the position and range of the match and its capturing groups, and it can extract its substring for you.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Dictionary](class_dictionary.md#class-dictionary) | [names](class_regexmatch.md#class-regexmatch-property-names) | `{}` |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [strings](class_regexmatch.md#class-regexmatch-property-strings) | `PackedStringArray()` |
| [String](class_string.md#class-string) | [subject](class_regexmatch.md#class-regexmatch-property-subject) | `""` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [int](class_int.md#class-int) | [get_end](class_regexmatch.md#class-regexmatch-method-get-end)(name: [Variant](class_variant.md#class-variant) = 0) const |
| [int](class_int.md#class-int) | [get_group_count](class_regexmatch.md#class-regexmatch-method-get-group-count)() const |
| [int](class_int.md#class-int) | [get_start](class_regexmatch.md#class-regexmatch-method-get-start)(name: [Variant](class_variant.md#class-variant) = 0) const |
| [String](class_string.md#class-string) | [get_string](class_regexmatch.md#class-regexmatch-method-get-string)(name: [Variant](class_variant.md#class-variant) = 0) const |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-regexmatch-property-names"></a>

[Dictionary](class_dictionary.md#class-dictionary) **names** = `{}` [🔗](class_regexmatch.md#class-regexmatch-property-names)

- [Dictionary](class_dictionary.md#class-dictionary) **get_names**()

A dictionary of named groups and its corresponding group number. Only groups that were matched are included. If multiple groups have the same name, that name would refer to the first matching one.

---


<a id="class-regexmatch-property-strings"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **strings** = `PackedStringArray()` [🔗](class_regexmatch.md#class-regexmatch-property-strings)

- [PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_strings**()

An [Array](class_array.md#class-array) of the match and its capturing groups.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedStringArray](class_packedstringarray.md#class-packedstringarray) for more details.

---


<a id="class-regexmatch-property-subject"></a>

[String](class_string.md#class-string) **subject** = `""` [🔗](class_regexmatch.md#class-regexmatch-property-subject)

- [String](class_string.md#class-string) **get_subject**()

The source string used with the search pattern to find this matching result.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-regexmatch-method-get-end"></a>

[int](class_int.md#class-int) **get_end**(name: [Variant](class_variant.md#class-variant) = 0) const [🔗](class_regexmatch.md#class-regexmatch-method-get-end)

Returns the end position of the match within the source string. The end position of capturing groups can be retrieved by providing its group number as an integer or its string name (if it's a named group). The default value of 0 refers to the whole pattern.

Returns -1 if the group did not match or doesn't exist.

---


<a id="class-regexmatch-method-get-group-count"></a>

[int](class_int.md#class-int) **get_group_count**() const [🔗](class_regexmatch.md#class-regexmatch-method-get-group-count)

Returns the number of capturing groups.

---


<a id="class-regexmatch-method-get-start"></a>

[int](class_int.md#class-int) **get_start**(name: [Variant](class_variant.md#class-variant) = 0) const [🔗](class_regexmatch.md#class-regexmatch-method-get-start)

Returns the starting position of the match within the source string. The starting position of capturing groups can be retrieved by providing its group number as an integer or its string name (if it's a named group). The default value of 0 refers to the whole pattern.

Returns -1 if the group did not match or doesn't exist.

---


<a id="class-regexmatch-method-get-string"></a>

[String](class_string.md#class-string) **get_string**(name: [Variant](class_variant.md#class-variant) = 0) const [🔗](class_regexmatch.md#class-regexmatch-method-get-string)

Returns the substring of the match from the source string. Capturing groups can be retrieved by providing its group number as an integer or its string name (if it's a named group). The default value of 0 refers to the whole pattern.

Returns an empty string if the group did not match or doesn't exist.
