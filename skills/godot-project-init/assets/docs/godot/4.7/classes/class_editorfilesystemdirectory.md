> Source: https://docs.godotengine.org/en/4.7/classes/class_editorfilesystemdirectory.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="editorfilesystemdirectory"></a>

<a id="class-editorfilesystemdirectory"></a>

# EditorFileSystemDirectory

**Inherits:** [Object](class_object.md#class-object)

A directory for the resource filesystem.

<a id="description"></a>

## Description

A more generalized, low-level variation of the directory concept.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [int](class_int.md#class-int) | [find_dir_index](class_editorfilesystemdirectory.md#class-editorfilesystemdirectory-method-find-dir-index)(name: [String](class_string.md#class-string)) const |
| [int](class_int.md#class-int) | [find_file_index](class_editorfilesystemdirectory.md#class-editorfilesystemdirectory-method-find-file-index)(name: [String](class_string.md#class-string)) const |
| [String](class_string.md#class-string) | [get_file](class_editorfilesystemdirectory.md#class-editorfilesystemdirectory-method-get-file)(idx: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_file_count](class_editorfilesystemdirectory.md#class-editorfilesystemdirectory-method-get-file-count)() const |
| [bool](class_bool.md#class-bool) | [get_file_import_is_valid](class_editorfilesystemdirectory.md#class-editorfilesystemdirectory-method-get-file-import-is-valid)(idx: [int](class_int.md#class-int)) const |
| [String](class_string.md#class-string) | [get_file_path](class_editorfilesystemdirectory.md#class-editorfilesystemdirectory-method-get-file-path)(idx: [int](class_int.md#class-int)) const |
| [String](class_string.md#class-string) | [get_file_script_class_extends](class_editorfilesystemdirectory.md#class-editorfilesystemdirectory-method-get-file-script-class-extends)(idx: [int](class_int.md#class-int)) const |
| [String](class_string.md#class-string) | [get_file_script_class_name](class_editorfilesystemdirectory.md#class-editorfilesystemdirectory-method-get-file-script-class-name)(idx: [int](class_int.md#class-int)) const |
| [StringName](class_stringname.md#class-stringname) | [get_file_type](class_editorfilesystemdirectory.md#class-editorfilesystemdirectory-method-get-file-type)(idx: [int](class_int.md#class-int)) const |
| [String](class_string.md#class-string) | [get_name](class_editorfilesystemdirectory.md#class-editorfilesystemdirectory-method-get-name)() |
| [EditorFileSystemDirectory](class_editorfilesystemdirectory.md#class-editorfilesystemdirectory) | [get_parent](class_editorfilesystemdirectory.md#class-editorfilesystemdirectory-method-get-parent)() |
| [String](class_string.md#class-string) | [get_path](class_editorfilesystemdirectory.md#class-editorfilesystemdirectory-method-get-path)() const |
| [EditorFileSystemDirectory](class_editorfilesystemdirectory.md#class-editorfilesystemdirectory) | [get_subdir](class_editorfilesystemdirectory.md#class-editorfilesystemdirectory-method-get-subdir)(idx: [int](class_int.md#class-int)) |
| [int](class_int.md#class-int) | [get_subdir_count](class_editorfilesystemdirectory.md#class-editorfilesystemdirectory-method-get-subdir-count)() const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-editorfilesystemdirectory-method-find-dir-index"></a>

[int](class_int.md#class-int) **find_dir_index**(name: [String](class_string.md#class-string)) const [🔗](class_editorfilesystemdirectory.md#class-editorfilesystemdirectory-method-find-dir-index)

Returns the index of the directory with name `name` or `-1` if not found.

---


<a id="class-editorfilesystemdirectory-method-find-file-index"></a>

[int](class_int.md#class-int) **find_file_index**(name: [String](class_string.md#class-string)) const [🔗](class_editorfilesystemdirectory.md#class-editorfilesystemdirectory-method-find-file-index)

Returns the index of the file with name `name` or `-1` if not found.

---


<a id="class-editorfilesystemdirectory-method-get-file"></a>

[String](class_string.md#class-string) **get_file**(idx: [int](class_int.md#class-int)) const [🔗](class_editorfilesystemdirectory.md#class-editorfilesystemdirectory-method-get-file)

Returns the name of the file at index `idx`.

---


<a id="class-editorfilesystemdirectory-method-get-file-count"></a>

[int](class_int.md#class-int) **get_file_count**() const [🔗](class_editorfilesystemdirectory.md#class-editorfilesystemdirectory-method-get-file-count)

Returns the number of files in this directory.

---


<a id="class-editorfilesystemdirectory-method-get-file-import-is-valid"></a>

[bool](class_bool.md#class-bool) **get_file_import_is_valid**(idx: [int](class_int.md#class-int)) const [🔗](class_editorfilesystemdirectory.md#class-editorfilesystemdirectory-method-get-file-import-is-valid)

Returns `true` if the file at index `idx` imported properly.

---


<a id="class-editorfilesystemdirectory-method-get-file-path"></a>

[String](class_string.md#class-string) **get_file_path**(idx: [int](class_int.md#class-int)) const [🔗](class_editorfilesystemdirectory.md#class-editorfilesystemdirectory-method-get-file-path)

Returns the path to the file at index `idx`.

---


<a id="class-editorfilesystemdirectory-method-get-file-script-class-extends"></a>

[String](class_string.md#class-string) **get_file_script_class_extends**(idx: [int](class_int.md#class-int)) const [🔗](class_editorfilesystemdirectory.md#class-editorfilesystemdirectory-method-get-file-script-class-extends)

Returns the base class of the script class defined in the file at index `idx`. If the file doesn't define a script class using the `class_name` syntax, this will return an empty string.

---


<a id="class-editorfilesystemdirectory-method-get-file-script-class-name"></a>

[String](class_string.md#class-string) **get_file_script_class_name**(idx: [int](class_int.md#class-int)) const [🔗](class_editorfilesystemdirectory.md#class-editorfilesystemdirectory-method-get-file-script-class-name)

Returns the name of the script class defined in the file at index `idx`. If the file doesn't define a script class using the `class_name` syntax, this will return an empty string.

---


<a id="class-editorfilesystemdirectory-method-get-file-type"></a>

[StringName](class_stringname.md#class-stringname) **get_file_type**(idx: [int](class_int.md#class-int)) const [🔗](class_editorfilesystemdirectory.md#class-editorfilesystemdirectory-method-get-file-type)

Returns the resource type of the file at index `idx`. This returns a string such as `"Resource"` or `"GDScript"`, *not* a file extension such as `".gd"`.

---


<a id="class-editorfilesystemdirectory-method-get-name"></a>

[String](class_string.md#class-string) **get_name**() [🔗](class_editorfilesystemdirectory.md#class-editorfilesystemdirectory-method-get-name)

Returns the name of this directory.

---


<a id="class-editorfilesystemdirectory-method-get-parent"></a>

[EditorFileSystemDirectory](class_editorfilesystemdirectory.md#class-editorfilesystemdirectory) **get_parent**() [🔗](class_editorfilesystemdirectory.md#class-editorfilesystemdirectory-method-get-parent)

Returns the parent directory for this directory or `null` if called on a directory at `res://` or `user://`.

---


<a id="class-editorfilesystemdirectory-method-get-path"></a>

[String](class_string.md#class-string) **get_path**() const [🔗](class_editorfilesystemdirectory.md#class-editorfilesystemdirectory-method-get-path)

Returns the path to this directory.

---


<a id="class-editorfilesystemdirectory-method-get-subdir"></a>

[EditorFileSystemDirectory](class_editorfilesystemdirectory.md#class-editorfilesystemdirectory) **get_subdir**(idx: [int](class_int.md#class-int)) [🔗](class_editorfilesystemdirectory.md#class-editorfilesystemdirectory-method-get-subdir)

Returns the subdirectory at index `idx`.

---


<a id="class-editorfilesystemdirectory-method-get-subdir-count"></a>

[int](class_int.md#class-int) **get_subdir_count**() const [🔗](class_editorfilesystemdirectory.md#class-editorfilesystemdirectory-method-get-subdir-count)

Returns the number of subdirectories in this directory.
