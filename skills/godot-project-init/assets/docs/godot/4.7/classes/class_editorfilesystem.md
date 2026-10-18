> Source: https://docs.godotengine.org/en/4.7/classes/class_editorfilesystem.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="editorfilesystem"></a>

<a id="class-editorfilesystem"></a>

# EditorFileSystem

**Inherits:** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Resource filesystem, as the editor sees it.

<a id="description"></a>

## Description

This object holds information of all resources in the filesystem, their types, etc.

**Note:** This class shouldn't be instantiated directly. Instead, access the singleton using [EditorInterface.get_resource_filesystem()](class_editorinterface.md#class-editorinterface-method-get-resource-filesystem).

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [String](class_string.md#class-string) | [get_file_type](class_editorfilesystem.md#class-editorfilesystem-method-get-file-type)(path: [String](class_string.md#class-string)) const |
| [EditorFileSystemDirectory](class_editorfilesystemdirectory.md#class-editorfilesystemdirectory) | [get_filesystem](class_editorfilesystem.md#class-editorfilesystem-method-get-filesystem)() |
| [EditorFileSystemDirectory](class_editorfilesystemdirectory.md#class-editorfilesystemdirectory) | [get_filesystem_path](class_editorfilesystem.md#class-editorfilesystem-method-get-filesystem-path)(path: [String](class_string.md#class-string)) |
| [float](class_float.md#class-float) | [get_scanning_progress](class_editorfilesystem.md#class-editorfilesystem-method-get-scanning-progress)() const |
| [bool](class_bool.md#class-bool) | [is_importing](class_editorfilesystem.md#class-editorfilesystem-method-is-importing)() const |
| [bool](class_bool.md#class-bool) | [is_scanning](class_editorfilesystem.md#class-editorfilesystem-method-is-scanning)() const |
| void | [reimport_files](class_editorfilesystem.md#class-editorfilesystem-method-reimport-files)(files: [PackedStringArray](class_packedstringarray.md#class-packedstringarray)) |
| void | [scan](class_editorfilesystem.md#class-editorfilesystem-method-scan)() |
| void | [scan_sources](class_editorfilesystem.md#class-editorfilesystem-method-scan-sources)() |
| void | [update_file](class_editorfilesystem.md#class-editorfilesystem-method-update-file)(path: [String](class_string.md#class-string)) |

---


<a id="signals"></a>

## Signals

<a id="class-editorfilesystem-signal-filesystem-changed"></a>

**filesystem_changed**() [🔗](class_editorfilesystem.md#class-editorfilesystem-signal-filesystem-changed)

Emitted if the filesystem changed.

---


<a id="class-editorfilesystem-signal-resources-reimported"></a>

**resources_reimported**(resources: [PackedStringArray](class_packedstringarray.md#class-packedstringarray)) [🔗](class_editorfilesystem.md#class-editorfilesystem-signal-resources-reimported)

Emitted if a resource is reimported.

---


<a id="class-editorfilesystem-signal-resources-reimporting"></a>

**resources_reimporting**(resources: [PackedStringArray](class_packedstringarray.md#class-packedstringarray)) [🔗](class_editorfilesystem.md#class-editorfilesystem-signal-resources-reimporting)

Emitted before a resource is reimported.

---


<a id="class-editorfilesystem-signal-resources-reload"></a>

**resources_reload**(resources: [PackedStringArray](class_packedstringarray.md#class-packedstringarray)) [🔗](class_editorfilesystem.md#class-editorfilesystem-signal-resources-reload)

Emitted if at least one resource is reloaded when the filesystem is scanned.

---


<a id="class-editorfilesystem-signal-script-classes-updated"></a>

**script_classes_updated**() [🔗](class_editorfilesystem.md#class-editorfilesystem-signal-script-classes-updated)

Emitted when the list of global script classes gets updated.

---


<a id="class-editorfilesystem-signal-sources-changed"></a>

**sources_changed**(exist: [bool](class_bool.md#class-bool)) [🔗](class_editorfilesystem.md#class-editorfilesystem-signal-sources-changed)

Emitted if the source of any imported file changed.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-editorfilesystem-method-get-file-type"></a>

[String](class_string.md#class-string) **get_file_type**(path: [String](class_string.md#class-string)) const [🔗](class_editorfilesystem.md#class-editorfilesystem-method-get-file-type)

Returns the resource type of the file, given the full path. This returns a string such as `"Resource"` or `"GDScript"`, *not* a file extension such as `".gd"`.

---


<a id="class-editorfilesystem-method-get-filesystem"></a>

[EditorFileSystemDirectory](class_editorfilesystemdirectory.md#class-editorfilesystemdirectory) **get_filesystem**() [🔗](class_editorfilesystem.md#class-editorfilesystem-method-get-filesystem)

Gets the root directory object.

---


<a id="class-editorfilesystem-method-get-filesystem-path"></a>

[EditorFileSystemDirectory](class_editorfilesystemdirectory.md#class-editorfilesystemdirectory) **get_filesystem_path**(path: [String](class_string.md#class-string)) [🔗](class_editorfilesystem.md#class-editorfilesystem-method-get-filesystem-path)

Returns a view into the filesystem at `path`.

---


<a id="class-editorfilesystem-method-get-scanning-progress"></a>

[float](class_float.md#class-float) **get_scanning_progress**() const [🔗](class_editorfilesystem.md#class-editorfilesystem-method-get-scanning-progress)

Returns the scan progress for 0 to 1 if the FS is being scanned.

---


<a id="class-editorfilesystem-method-is-importing"></a>

[bool](class_bool.md#class-bool) **is_importing**() const [🔗](class_editorfilesystem.md#class-editorfilesystem-method-is-importing)

Returns `true` if resources are currently being imported.

---


<a id="class-editorfilesystem-method-is-scanning"></a>

[bool](class_bool.md#class-bool) **is_scanning**() const [🔗](class_editorfilesystem.md#class-editorfilesystem-method-is-scanning)

Returns `true` if the filesystem is being scanned.

---


<a id="class-editorfilesystem-method-reimport-files"></a>

void **reimport_files**(files: [PackedStringArray](class_packedstringarray.md#class-packedstringarray)) [🔗](class_editorfilesystem.md#class-editorfilesystem-method-reimport-files)

Reimports a set of files. Call this if these files or their `.import` files were directly edited by script or an external program.

If the file type changed or the file was newly created, use [update_file()](class_editorfilesystem.md#class-editorfilesystem-method-update-file) or [scan()](class_editorfilesystem.md#class-editorfilesystem-method-scan).

**Note:** This function blocks until the import is finished. However, the main loop iteration, including timers and [Node._process()](class_node.md#class-node-private-method-process), will occur during the import process due to progress bar updates. Avoid calls to [reimport_files()](class_editorfilesystem.md#class-editorfilesystem-method-reimport-files) or [scan()](class_editorfilesystem.md#class-editorfilesystem-method-scan) while an import is in progress.

---


<a id="class-editorfilesystem-method-scan"></a>

void **scan**() [🔗](class_editorfilesystem.md#class-editorfilesystem-method-scan)

Scan the filesystem for changes.

---


<a id="class-editorfilesystem-method-scan-sources"></a>

void **scan_sources**() [🔗](class_editorfilesystem.md#class-editorfilesystem-method-scan-sources)

Check if the source of any imported resource changed.

---


<a id="class-editorfilesystem-method-update-file"></a>

void **update_file**(path: [String](class_string.md#class-string)) [🔗](class_editorfilesystem.md#class-editorfilesystem-method-update-file)

Add a file in an existing directory, or schedule file information to be updated on editor restart. Can be used to update text files saved by an external program.

This will not import the file. To reimport, call [reimport_files()](class_editorfilesystem.md#class-editorfilesystem-method-reimport-files) or [scan()](class_editorfilesystem.md#class-editorfilesystem-method-scan) methods.
