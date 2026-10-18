> Source: https://docs.godotengine.org/en/4.7/classes/class_shaderincludedb.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="shaderincludedb"></a>

<a id="class-shaderincludedb"></a>

# ShaderIncludeDB

**Inherits:** [Object](class_object.md#class-object)

Internal database of built in shader include files.

<a id="description"></a>

## Description

This object contains shader fragments from Godot's internal shaders. These can be used when access to internal uniform buffers and/or internal functions is required for instance when composing compositor effects or compute shaders. Only fragments for the current rendering device are loaded.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [String](class_string.md#class-string) | [get_built_in_include_file](class_shaderincludedb.md#class-shaderincludedb-method-get-built-in-include-file)(filename: [String](class_string.md#class-string)) static |
| [bool](class_bool.md#class-bool) | [has_built_in_include_file](class_shaderincludedb.md#class-shaderincludedb-method-has-built-in-include-file)(filename: [String](class_string.md#class-string)) static |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [list_built_in_include_files](class_shaderincludedb.md#class-shaderincludedb-method-list-built-in-include-files)() static |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-shaderincludedb-method-get-built-in-include-file"></a>

[String](class_string.md#class-string) **get_built_in_include_file**(filename: [String](class_string.md#class-string)) static [🔗](class_shaderincludedb.md#class-shaderincludedb-method-get-built-in-include-file)

Returns the code for the built-in shader fragment. You can also access this in your shader code through `#include "filename"`.

---


<a id="class-shaderincludedb-method-has-built-in-include-file"></a>

[bool](class_bool.md#class-bool) **has_built_in_include_file**(filename: [String](class_string.md#class-string)) static [🔗](class_shaderincludedb.md#class-shaderincludedb-method-has-built-in-include-file)

Returns `true` if an include file with this name exists.

---


<a id="class-shaderincludedb-method-list-built-in-include-files"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **list_built_in_include_files**() static [🔗](class_shaderincludedb.md#class-shaderincludedb-method-list-built-in-include-files)

Returns a list of built-in include files that are currently registered.
