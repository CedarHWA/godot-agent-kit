> Source: https://docs.godotengine.org/en/4.7/classes/class_editorfilesystemimportformatsupportquery.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="editorfilesystemimportformatsupportquery"></a>

<a id="class-editorfilesystemimportformatsupportquery"></a>

# EditorFileSystemImportFormatSupportQuery

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Used to query and configure import format support.

<a id="description"></a>

## Description

This class is used to query and configure a certain import format. It is used in conjunction with asset format import plugins.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [_get_file_extensions](class_editorfilesystemimportformatsupportquery.md#class-editorfilesystemimportformatsupportquery-private-method-get-file-extensions)() virtual required const |
| [bool](class_bool.md#class-bool) | [_is_active](class_editorfilesystemimportformatsupportquery.md#class-editorfilesystemimportformatsupportquery-private-method-is-active)() virtual required const |
| [bool](class_bool.md#class-bool) | [_query](class_editorfilesystemimportformatsupportquery.md#class-editorfilesystemimportformatsupportquery-private-method-query)() virtual required const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-editorfilesystemimportformatsupportquery-private-method-get-file-extensions"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **_get_file_extensions**() virtual required const [🔗](class_editorfilesystemimportformatsupportquery.md#class-editorfilesystemimportformatsupportquery-private-method-get-file-extensions)

Return the file extensions supported.

---


<a id="class-editorfilesystemimportformatsupportquery-private-method-is-active"></a>

[bool](class_bool.md#class-bool) **_is_active**() virtual required const [🔗](class_editorfilesystemimportformatsupportquery.md#class-editorfilesystemimportformatsupportquery-private-method-is-active)

Return whether this importer is active.

---


<a id="class-editorfilesystemimportformatsupportquery-private-method-query"></a>

[bool](class_bool.md#class-bool) **_query**() virtual required const [🔗](class_editorfilesystemimportformatsupportquery.md#class-editorfilesystemimportformatsupportquery-private-method-query)

Query support. Return `false` if import must not continue.
