> Source: https://docs.godotengine.org/en/4.7/classes/class_codehighlighter.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="codehighlighter"></a>

<a id="class-codehighlighter"></a>

# CodeHighlighter

**Inherits:** [SyntaxHighlighter](class_syntaxhighlighter.md#class-syntaxhighlighter) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A syntax highlighter intended for code.

<a id="description"></a>

## Description

By adjusting various properties of this resource, you can change the colors of strings, comments, numbers, and other text patterns inside a [TextEdit](class_textedit.md#class-textedit) control.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Dictionary](class_dictionary.md#class-dictionary) | [color_regions](class_codehighlighter.md#class-codehighlighter-property-color-regions) | `{}` |
| [Color](class_color.md#class-color) | [function_color](class_codehighlighter.md#class-codehighlighter-property-function-color) | `Color(0, 0, 0, 1)` |
| [Dictionary](class_dictionary.md#class-dictionary) | [keyword_colors](class_codehighlighter.md#class-codehighlighter-property-keyword-colors) | `{}` |
| [Dictionary](class_dictionary.md#class-dictionary) | [member_keyword_colors](class_codehighlighter.md#class-codehighlighter-property-member-keyword-colors) | `{}` |
| [Color](class_color.md#class-color) | [member_variable_color](class_codehighlighter.md#class-codehighlighter-property-member-variable-color) | `Color(0, 0, 0, 1)` |
| [Color](class_color.md#class-color) | [number_color](class_codehighlighter.md#class-codehighlighter-property-number-color) | `Color(0, 0, 0, 1)` |
| [Color](class_color.md#class-color) | [symbol_color](class_codehighlighter.md#class-codehighlighter-property-symbol-color) | `Color(0, 0, 0, 1)` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_color_region](class_codehighlighter.md#class-codehighlighter-method-add-color-region)(start_key: [String](class_string.md#class-string), end_key: [String](class_string.md#class-string), color: [Color](class_color.md#class-color), line_only: [bool](class_bool.md#class-bool) = false) |
| void | [add_keyword_color](class_codehighlighter.md#class-codehighlighter-method-add-keyword-color)(keyword: [String](class_string.md#class-string), color: [Color](class_color.md#class-color)) |
| void | [add_member_keyword_color](class_codehighlighter.md#class-codehighlighter-method-add-member-keyword-color)(member_keyword: [String](class_string.md#class-string), color: [Color](class_color.md#class-color)) |
| void | [clear_color_regions](class_codehighlighter.md#class-codehighlighter-method-clear-color-regions)() |
| void | [clear_keyword_colors](class_codehighlighter.md#class-codehighlighter-method-clear-keyword-colors)() |
| void | [clear_member_keyword_colors](class_codehighlighter.md#class-codehighlighter-method-clear-member-keyword-colors)() |
| [Color](class_color.md#class-color) | [get_keyword_color](class_codehighlighter.md#class-codehighlighter-method-get-keyword-color)(keyword: [String](class_string.md#class-string)) const |
| [Color](class_color.md#class-color) | [get_member_keyword_color](class_codehighlighter.md#class-codehighlighter-method-get-member-keyword-color)(member_keyword: [String](class_string.md#class-string)) const |
| [bool](class_bool.md#class-bool) | [has_color_region](class_codehighlighter.md#class-codehighlighter-method-has-color-region)(start_key: [String](class_string.md#class-string)) const |
| [bool](class_bool.md#class-bool) | [has_keyword_color](class_codehighlighter.md#class-codehighlighter-method-has-keyword-color)(keyword: [String](class_string.md#class-string)) const |
| [bool](class_bool.md#class-bool) | [has_member_keyword_color](class_codehighlighter.md#class-codehighlighter-method-has-member-keyword-color)(member_keyword: [String](class_string.md#class-string)) const |
| void | [remove_color_region](class_codehighlighter.md#class-codehighlighter-method-remove-color-region)(start_key: [String](class_string.md#class-string)) |
| void | [remove_keyword_color](class_codehighlighter.md#class-codehighlighter-method-remove-keyword-color)(keyword: [String](class_string.md#class-string)) |
| void | [remove_member_keyword_color](class_codehighlighter.md#class-codehighlighter-method-remove-member-keyword-color)(member_keyword: [String](class_string.md#class-string)) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-codehighlighter-property-color-regions"></a>

[Dictionary](class_dictionary.md#class-dictionary) **color_regions** = `{}` [🔗](class_codehighlighter.md#class-codehighlighter-property-color-regions)

- void **set_color_regions**(value: [Dictionary](class_dictionary.md#class-dictionary))
- [Dictionary](class_dictionary.md#class-dictionary) **get_color_regions**()

Sets the color regions. All existing regions will be removed. The [Dictionary](class_dictionary.md#class-dictionary) key is the region start and end key, separated by a space. The value is the region color.

---


<a id="class-codehighlighter-property-function-color"></a>

[Color](class_color.md#class-color) **function_color** = `Color(0, 0, 0, 1)` [🔗](class_codehighlighter.md#class-codehighlighter-property-function-color)

- void **set_function_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_function_color**()

Sets color for functions. A function is a non-keyword string followed by a '('.

---


<a id="class-codehighlighter-property-keyword-colors"></a>

[Dictionary](class_dictionary.md#class-dictionary) **keyword_colors** = `{}` [🔗](class_codehighlighter.md#class-codehighlighter-property-keyword-colors)

- void **set_keyword_colors**(value: [Dictionary](class_dictionary.md#class-dictionary))
- [Dictionary](class_dictionary.md#class-dictionary) **get_keyword_colors**()

Sets the keyword colors. All existing keywords will be removed. The [Dictionary](class_dictionary.md#class-dictionary) key is the keyword. The value is the keyword color.

---


<a id="class-codehighlighter-property-member-keyword-colors"></a>

[Dictionary](class_dictionary.md#class-dictionary) **member_keyword_colors** = `{}` [🔗](class_codehighlighter.md#class-codehighlighter-property-member-keyword-colors)

- void **set_member_keyword_colors**(value: [Dictionary](class_dictionary.md#class-dictionary))
- [Dictionary](class_dictionary.md#class-dictionary) **get_member_keyword_colors**()

Sets the member keyword colors. All existing member keyword will be removed. The [Dictionary](class_dictionary.md#class-dictionary) key is the member keyword. The value is the member keyword color.

---


<a id="class-codehighlighter-property-member-variable-color"></a>

[Color](class_color.md#class-color) **member_variable_color** = `Color(0, 0, 0, 1)` [🔗](class_codehighlighter.md#class-codehighlighter-property-member-variable-color)

- void **set_member_variable_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_member_variable_color**()

Sets color for member variables. A member variable is non-keyword, non-function string proceeded with a '.'.

---


<a id="class-codehighlighter-property-number-color"></a>

[Color](class_color.md#class-color) **number_color** = `Color(0, 0, 0, 1)` [🔗](class_codehighlighter.md#class-codehighlighter-property-number-color)

- void **set_number_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_number_color**()

Sets the color for numbers.

---


<a id="class-codehighlighter-property-symbol-color"></a>

[Color](class_color.md#class-color) **symbol_color** = `Color(0, 0, 0, 1)` [🔗](class_codehighlighter.md#class-codehighlighter-property-symbol-color)

- void **set_symbol_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_symbol_color**()

Sets the color for symbols.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-codehighlighter-method-add-color-region"></a>

void **add_color_region**(start_key: [String](class_string.md#class-string), end_key: [String](class_string.md#class-string), color: [Color](class_color.md#class-color), line_only: [bool](class_bool.md#class-bool) = false) [🔗](class_codehighlighter.md#class-codehighlighter-method-add-color-region)

Adds a color region (such as for comments or strings) from `start_key` to `end_key`. Both keys should be symbols, and `start_key` must not be shared with other delimiters.

If `line_only` is `true` or `end_key` is an empty [String](class_string.md#class-string), the region does not carry over to the next line.

---


<a id="class-codehighlighter-method-add-keyword-color"></a>

void **add_keyword_color**(keyword: [String](class_string.md#class-string), color: [Color](class_color.md#class-color)) [🔗](class_codehighlighter.md#class-codehighlighter-method-add-keyword-color)

Sets the color for a keyword.

The keyword cannot contain any symbols except '_'.

---


<a id="class-codehighlighter-method-add-member-keyword-color"></a>

void **add_member_keyword_color**(member_keyword: [String](class_string.md#class-string), color: [Color](class_color.md#class-color)) [🔗](class_codehighlighter.md#class-codehighlighter-method-add-member-keyword-color)

Sets the color for a member keyword.

The member keyword cannot contain any symbols except '_'.

It will not be highlighted if preceded by a '.'.

---


<a id="class-codehighlighter-method-clear-color-regions"></a>

void **clear_color_regions**() [🔗](class_codehighlighter.md#class-codehighlighter-method-clear-color-regions)

Removes all color regions.

---


<a id="class-codehighlighter-method-clear-keyword-colors"></a>

void **clear_keyword_colors**() [🔗](class_codehighlighter.md#class-codehighlighter-method-clear-keyword-colors)

Removes all keywords.

---


<a id="class-codehighlighter-method-clear-member-keyword-colors"></a>

void **clear_member_keyword_colors**() [🔗](class_codehighlighter.md#class-codehighlighter-method-clear-member-keyword-colors)

Removes all member keywords.

---


<a id="class-codehighlighter-method-get-keyword-color"></a>

[Color](class_color.md#class-color) **get_keyword_color**(keyword: [String](class_string.md#class-string)) const [🔗](class_codehighlighter.md#class-codehighlighter-method-get-keyword-color)

Returns the color for a keyword.

---


<a id="class-codehighlighter-method-get-member-keyword-color"></a>

[Color](class_color.md#class-color) **get_member_keyword_color**(member_keyword: [String](class_string.md#class-string)) const [🔗](class_codehighlighter.md#class-codehighlighter-method-get-member-keyword-color)

Returns the color for a member keyword.

---


<a id="class-codehighlighter-method-has-color-region"></a>

[bool](class_bool.md#class-bool) **has_color_region**(start_key: [String](class_string.md#class-string)) const [🔗](class_codehighlighter.md#class-codehighlighter-method-has-color-region)

Returns `true` if the start key exists, else `false`.

---


<a id="class-codehighlighter-method-has-keyword-color"></a>

[bool](class_bool.md#class-bool) **has_keyword_color**(keyword: [String](class_string.md#class-string)) const [🔗](class_codehighlighter.md#class-codehighlighter-method-has-keyword-color)

Returns `true` if the keyword exists, else `false`.

---


<a id="class-codehighlighter-method-has-member-keyword-color"></a>

[bool](class_bool.md#class-bool) **has_member_keyword_color**(member_keyword: [String](class_string.md#class-string)) const [🔗](class_codehighlighter.md#class-codehighlighter-method-has-member-keyword-color)

Returns `true` if the member keyword exists, else `false`.

---


<a id="class-codehighlighter-method-remove-color-region"></a>

void **remove_color_region**(start_key: [String](class_string.md#class-string)) [🔗](class_codehighlighter.md#class-codehighlighter-method-remove-color-region)

Removes the color region that uses that start key.

---


<a id="class-codehighlighter-method-remove-keyword-color"></a>

void **remove_keyword_color**(keyword: [String](class_string.md#class-string)) [🔗](class_codehighlighter.md#class-codehighlighter-method-remove-keyword-color)

Removes the keyword.

---


<a id="class-codehighlighter-method-remove-member-keyword-color"></a>

void **remove_member_keyword_color**(member_keyword: [String](class_string.md#class-string)) [🔗](class_codehighlighter.md#class-codehighlighter-method-remove-member-keyword-color)

Removes the member keyword.
