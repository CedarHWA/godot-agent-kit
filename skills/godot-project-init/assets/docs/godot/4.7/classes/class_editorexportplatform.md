> Source: https://docs.godotengine.org/en/4.7/classes/class_editorexportplatform.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="editorexportplatform"></a>

<a id="class-editorexportplatform"></a>

# EditorExportPlatform

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [EditorExportPlatformAndroid](class_editorexportplatformandroid.md#class-editorexportplatformandroid), [EditorExportPlatformAppleEmbedded](class_editorexportplatformappleembedded.md#class-editorexportplatformappleembedded), [EditorExportPlatformExtension](class_editorexportplatformextension.md#class-editorexportplatformextension), [EditorExportPlatformMacOS](class_editorexportplatformmacos.md#class-editorexportplatformmacos), [EditorExportPlatformPC](class_editorexportplatformpc.md#class-editorexportplatformpc), [EditorExportPlatformWeb](class_editorexportplatformweb.md#class-editorexportplatformweb)

Identifies a supported export platform, and internally provides the functionality of exporting to that platform.

<a id="description"></a>

## Description

Base resource that provides the functionality of exporting a release build of a project to a platform, from the editor. Stores platform-specific metadata such as the name and supported features of the platform, and performs the exporting of projects, PCK files, and ZIP files. Uses an export template for the platform provided at the time of project exporting.

Used in scripting by [EditorExportPlugin](class_editorexportplugin.md#class-editorexportplugin) to configure platform-specific customization of scenes and resources. See [EditorExportPlugin._begin_customize_scenes()](class_editorexportplugin.md#class-editorexportplugin-private-method-begin-customize-scenes) and [EditorExportPlugin._begin_customize_resources()](class_editorexportplugin.md#class-editorexportplugin-private-method-begin-customize-resources) for more details.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_message](class_editorexportplatform.md#class-editorexportplatform-method-add-message)(type: [ExportMessageType](class_editorexportplatform.md#enum-editorexportplatform-exportmessagetype), category: [String](class_string.md#class-string), message: [String](class_string.md#class-string)) |
| void | [clear_messages](class_editorexportplatform.md#class-editorexportplatform-method-clear-messages)() |
| [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset) | [create_preset](class_editorexportplatform.md#class-editorexportplatform-method-create-preset)() |
| [Error](class_@globalscope.md#enum-globalscope-error) | [export_pack](class_editorexportplatform.md#class-editorexportplatform-method-export-pack)(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool), path: [String](class_string.md#class-string), flags: BitField[[DebugFlags](class_editorexportplatform.md#enum-editorexportplatform-debugflags)] = 0) |
| [Error](class_@globalscope.md#enum-globalscope-error) | [export_pack_patch](class_editorexportplatform.md#class-editorexportplatform-method-export-pack-patch)(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool), path: [String](class_string.md#class-string), patches: [PackedStringArray](class_packedstringarray.md#class-packedstringarray) = PackedStringArray(), flags: BitField[[DebugFlags](class_editorexportplatform.md#enum-editorexportplatform-debugflags)] = 0) |
| [Error](class_@globalscope.md#enum-globalscope-error) | [export_project](class_editorexportplatform.md#class-editorexportplatform-method-export-project)(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool), path: [String](class_string.md#class-string), flags: BitField[[DebugFlags](class_editorexportplatform.md#enum-editorexportplatform-debugflags)] = 0, notify: [bool](class_bool.md#class-bool) = true) |
| [Error](class_@globalscope.md#enum-globalscope-error) | [export_project_files](class_editorexportplatform.md#class-editorexportplatform-method-export-project-files)(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool), save_cb: [Callable](class_callable.md#class-callable), shared_cb: [Callable](class_callable.md#class-callable) = Callable()) |
| [Error](class_@globalscope.md#enum-globalscope-error) | [export_zip](class_editorexportplatform.md#class-editorexportplatform-method-export-zip)(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool), path: [String](class_string.md#class-string), flags: BitField[[DebugFlags](class_editorexportplatform.md#enum-editorexportplatform-debugflags)] = 0) |
| [Error](class_@globalscope.md#enum-globalscope-error) | [export_zip_patch](class_editorexportplatform.md#class-editorexportplatform-method-export-zip-patch)(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool), path: [String](class_string.md#class-string), patches: [PackedStringArray](class_packedstringarray.md#class-packedstringarray) = PackedStringArray(), flags: BitField[[DebugFlags](class_editorexportplatform.md#enum-editorexportplatform-debugflags)] = 0) |
| [Dictionary](class_dictionary.md#class-dictionary) | [find_export_template](class_editorexportplatform.md#class-editorexportplatform-method-find-export-template)(template_file_name: [String](class_string.md#class-string)) const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [gen_export_flags](class_editorexportplatform.md#class-editorexportplatform-method-gen-export-flags)(flags: BitField[[DebugFlags](class_editorexportplatform.md#enum-editorexportplatform-debugflags)]) |
| [Array](class_array.md#class-array) | [get_current_presets](class_editorexportplatform.md#class-editorexportplatform-method-get-current-presets)() const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [get_forced_export_files](class_editorexportplatform.md#class-editorexportplatform-method-get-forced-export-files)(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset) = null) static |
| [Dictionary](class_dictionary.md#class-dictionary) | [get_internal_export_files](class_editorexportplatform.md#class-editorexportplatform-method-get-internal-export-files)(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool)) |
| [String](class_string.md#class-string) | [get_message_category](class_editorexportplatform.md#class-editorexportplatform-method-get-message-category)(index: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_message_count](class_editorexportplatform.md#class-editorexportplatform-method-get-message-count)() const |
| [String](class_string.md#class-string) | [get_message_text](class_editorexportplatform.md#class-editorexportplatform-method-get-message-text)(index: [int](class_int.md#class-int)) const |
| [ExportMessageType](class_editorexportplatform.md#enum-editorexportplatform-exportmessagetype) | [get_message_type](class_editorexportplatform.md#class-editorexportplatform-method-get-message-type)(index: [int](class_int.md#class-int)) const |
| [String](class_string.md#class-string) | [get_os_name](class_editorexportplatform.md#class-editorexportplatform-method-get-os-name)() const |
| [ExportMessageType](class_editorexportplatform.md#enum-editorexportplatform-exportmessagetype) | [get_worst_message_type](class_editorexportplatform.md#class-editorexportplatform-method-get-worst-message-type)() const |
| [Dictionary](class_dictionary.md#class-dictionary) | [save_pack](class_editorexportplatform.md#class-editorexportplatform-method-save-pack)(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool), path: [String](class_string.md#class-string), embed: [bool](class_bool.md#class-bool) = false) |
| [Dictionary](class_dictionary.md#class-dictionary) | [save_pack_patch](class_editorexportplatform.md#class-editorexportplatform-method-save-pack-patch)(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool), path: [String](class_string.md#class-string)) |
| [Dictionary](class_dictionary.md#class-dictionary) | [save_zip](class_editorexportplatform.md#class-editorexportplatform-method-save-zip)(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool), path: [String](class_string.md#class-string)) |
| [Dictionary](class_dictionary.md#class-dictionary) | [save_zip_patch](class_editorexportplatform.md#class-editorexportplatform-method-save-zip-patch)(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool), path: [String](class_string.md#class-string)) |
| [Error](class_@globalscope.md#enum-globalscope-error) | [ssh_push_to_remote](class_editorexportplatform.md#class-editorexportplatform-method-ssh-push-to-remote)(host: [String](class_string.md#class-string), port: [String](class_string.md#class-string), scp_args: [PackedStringArray](class_packedstringarray.md#class-packedstringarray), src_file: [String](class_string.md#class-string), dst_file: [String](class_string.md#class-string)) const |
| [Error](class_@globalscope.md#enum-globalscope-error) | [ssh_run_on_remote](class_editorexportplatform.md#class-editorexportplatform-method-ssh-run-on-remote)(host: [String](class_string.md#class-string), port: [String](class_string.md#class-string), ssh_arg: [PackedStringArray](class_packedstringarray.md#class-packedstringarray), cmd_args: [String](class_string.md#class-string), output: [Array](class_array.md#class-array) = [], port_fwd: [int](class_int.md#class-int) = -1) const |
| [int](class_int.md#class-int) | [ssh_run_on_remote_no_wait](class_editorexportplatform.md#class-editorexportplatform-method-ssh-run-on-remote-no-wait)(host: [String](class_string.md#class-string), port: [String](class_string.md#class-string), ssh_args: [PackedStringArray](class_packedstringarray.md#class-packedstringarray), cmd_args: [String](class_string.md#class-string), port_fwd: [int](class_int.md#class-int) = -1) const |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-editorexportplatform-exportmessagetype"></a>

enum **ExportMessageType**: [🔗](class_editorexportplatform.md#enum-editorexportplatform-exportmessagetype)

<a id="class-editorexportplatform-constant-export-message-none"></a>

[ExportMessageType](class_editorexportplatform.md#enum-editorexportplatform-exportmessagetype) **EXPORT_MESSAGE_NONE** = `0`

Invalid message type used as the default value when no type is specified.

<a id="class-editorexportplatform-constant-export-message-info"></a>

[ExportMessageType](class_editorexportplatform.md#enum-editorexportplatform-exportmessagetype) **EXPORT_MESSAGE_INFO** = `1`

Message type for informational messages that have no effect on the export.

<a id="class-editorexportplatform-constant-export-message-warning"></a>

[ExportMessageType](class_editorexportplatform.md#enum-editorexportplatform-exportmessagetype) **EXPORT_MESSAGE_WARNING** = `2`

Message type for warning messages that should be addressed but still allow to complete the export.

<a id="class-editorexportplatform-constant-export-message-error"></a>

[ExportMessageType](class_editorexportplatform.md#enum-editorexportplatform-exportmessagetype) **EXPORT_MESSAGE_ERROR** = `3`

Message type for error messages that must be addressed and fail the export.

---


<a id="enum-editorexportplatform-debugflags"></a>

flags **DebugFlags**: [🔗](class_editorexportplatform.md#enum-editorexportplatform-debugflags)

<a id="class-editorexportplatform-constant-debug-flag-dumb-client"></a>

[DebugFlags](class_editorexportplatform.md#enum-editorexportplatform-debugflags) **DEBUG_FLAG_DUMB_CLIENT** = `1`

Flag is set if the remotely debugged project is expected to use the remote file system. If set, [gen_export_flags()](class_editorexportplatform.md#class-editorexportplatform-method-gen-export-flags) will append `--remote-fs` and `--remote-fs-password` (if [EditorSettings.filesystem/file_server/password](class_editorsettings.md#class-editorsettings-property-filesystem-file-server-password) is defined) command line arguments to the returned list.

<a id="class-editorexportplatform-constant-debug-flag-remote-debug"></a>

[DebugFlags](class_editorexportplatform.md#enum-editorexportplatform-debugflags) **DEBUG_FLAG_REMOTE_DEBUG** = `2`

Flag is set if remote debug is enabled. If set, [gen_export_flags()](class_editorexportplatform.md#class-editorexportplatform-method-gen-export-flags) will append `--remote-debug` and `--breakpoints` (if breakpoints are selected in the script editor or added by the plugin) command line arguments to the returned list.

<a id="class-editorexportplatform-constant-debug-flag-remote-debug-localhost"></a>

[DebugFlags](class_editorexportplatform.md#enum-editorexportplatform-debugflags) **DEBUG_FLAG_REMOTE_DEBUG_LOCALHOST** = `4`

Flag is set if remotely debugged project is running on the localhost. If set, [gen_export_flags()](class_editorexportplatform.md#class-editorexportplatform-method-gen-export-flags) will use `localhost` instead of [EditorSettings.network/debug/remote_host](class_editorsettings.md#class-editorsettings-property-network-debug-remote-host) as remote debugger host.

<a id="class-editorexportplatform-constant-debug-flag-view-collisions"></a>

[DebugFlags](class_editorexportplatform.md#enum-editorexportplatform-debugflags) **DEBUG_FLAG_VIEW_COLLISIONS** = `8`

Flag is set if the "Visible Collision Shapes" remote debug option is enabled. If set, [gen_export_flags()](class_editorexportplatform.md#class-editorexportplatform-method-gen-export-flags) will append the `--debug-collisions` command line argument to the returned list.

<a id="class-editorexportplatform-constant-debug-flag-view-navigation"></a>

[DebugFlags](class_editorexportplatform.md#enum-editorexportplatform-debugflags) **DEBUG_FLAG_VIEW_NAVIGATION** = `16`

Flag is set if the "Visible Navigation" remote debug option is enabled. If set, [gen_export_flags()](class_editorexportplatform.md#class-editorexportplatform-method-gen-export-flags) will append the `--debug-navigation` command line argument to the returned list.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-editorexportplatform-method-add-message"></a>

void **add_message**(type: [ExportMessageType](class_editorexportplatform.md#enum-editorexportplatform-exportmessagetype), category: [String](class_string.md#class-string), message: [String](class_string.md#class-string)) [🔗](class_editorexportplatform.md#class-editorexportplatform-method-add-message)

Adds a message to the export log that will be displayed when exporting ends.

---


<a id="class-editorexportplatform-method-clear-messages"></a>

void **clear_messages**() [🔗](class_editorexportplatform.md#class-editorexportplatform-method-clear-messages)

Clears the export log.

---


<a id="class-editorexportplatform-method-create-preset"></a>

[EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset) **create_preset**() [🔗](class_editorexportplatform.md#class-editorexportplatform-method-create-preset)

Create a new preset for this platform.

---


<a id="class-editorexportplatform-method-export-pack"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **export_pack**(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool), path: [String](class_string.md#class-string), flags: BitField[[DebugFlags](class_editorexportplatform.md#enum-editorexportplatform-debugflags)] = 0) [🔗](class_editorexportplatform.md#class-editorexportplatform-method-export-pack)

Creates a PCK archive at `path` for the specified `preset`.

---


<a id="class-editorexportplatform-method-export-pack-patch"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **export_pack_patch**(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool), path: [String](class_string.md#class-string), patches: [PackedStringArray](class_packedstringarray.md#class-packedstringarray) = PackedStringArray(), flags: BitField[[DebugFlags](class_editorexportplatform.md#enum-editorexportplatform-debugflags)] = 0) [🔗](class_editorexportplatform.md#class-editorexportplatform-method-export-pack-patch)

Creates a patch PCK archive at `path` for the specified `preset`, containing only the files that have changed since the last patch.

**Note:** `patches` is an optional override of the set of patches defined in the export preset. When empty the patches defined in the export preset will be used instead.

---


<a id="class-editorexportplatform-method-export-project"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **export_project**(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool), path: [String](class_string.md#class-string), flags: BitField[[DebugFlags](class_editorexportplatform.md#enum-editorexportplatform-debugflags)] = 0, notify: [bool](class_bool.md#class-bool) = true) [🔗](class_editorexportplatform.md#class-editorexportplatform-method-export-project)

Creates a full project at `path` for the specified `preset`. If `notify` is `true`, plugins using [EditorExportPlugin._export_begin()](class_editorexportplugin.md#class-editorexportplugin-private-method-export-begin) will be called during the process.

---


<a id="class-editorexportplatform-method-export-project-files"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **export_project_files**(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool), save_cb: [Callable](class_callable.md#class-callable), shared_cb: [Callable](class_callable.md#class-callable) = Callable()) [🔗](class_editorexportplatform.md#class-editorexportplatform-method-export-project-files)

Exports project files for the specified preset. This method can be used to implement custom export format, other than PCK and ZIP. One of the callbacks is called for each exported file.

`save_cb` is called for all exported files and have the following arguments: `file_path: String`, `file_data: PackedByteArray`, `file_index: int`, `file_count: int`, `encryption_include_filters: PackedStringArray`, `encryption_exclude_filters: PackedStringArray`, `encryption_key: PackedByteArray`.

`shared_cb` is called for exported native shared/static libraries and have the following arguments: `file_path: String`, `tags: PackedStringArray`, `target_folder: String`.

**Note:** `file_index` and `file_count` are intended for progress tracking only and aren't necessarily unique and precise.

---


<a id="class-editorexportplatform-method-export-zip"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **export_zip**(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool), path: [String](class_string.md#class-string), flags: BitField[[DebugFlags](class_editorexportplatform.md#enum-editorexportplatform-debugflags)] = 0) [🔗](class_editorexportplatform.md#class-editorexportplatform-method-export-zip)

Create a ZIP archive at `path` for the specified `preset`.

---


<a id="class-editorexportplatform-method-export-zip-patch"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **export_zip_patch**(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool), path: [String](class_string.md#class-string), patches: [PackedStringArray](class_packedstringarray.md#class-packedstringarray) = PackedStringArray(), flags: BitField[[DebugFlags](class_editorexportplatform.md#enum-editorexportplatform-debugflags)] = 0) [🔗](class_editorexportplatform.md#class-editorexportplatform-method-export-zip-patch)

Create a patch ZIP archive at `path` for the specified `preset`, containing only the files that have changed since the last patch.

**Note:** `patches` is an optional override of the set of patches defined in the export preset. When empty the patches defined in the export preset will be used instead.

---


<a id="class-editorexportplatform-method-find-export-template"></a>

[Dictionary](class_dictionary.md#class-dictionary) **find_export_template**(template_file_name: [String](class_string.md#class-string)) const [🔗](class_editorexportplatform.md#class-editorexportplatform-method-find-export-template)

Locates export template for the platform, and returns [Dictionary](class_dictionary.md#class-dictionary) with the following keys: `path: String` and `error: String`. This method is provided for convenience and custom export platforms aren't required to use it or keep export templates stored in the same way official templates are.

---


<a id="class-editorexportplatform-method-gen-export-flags"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **gen_export_flags**(flags: BitField[[DebugFlags](class_editorexportplatform.md#enum-editorexportplatform-debugflags)]) [🔗](class_editorexportplatform.md#class-editorexportplatform-method-gen-export-flags)

Generates array of command line arguments for the default export templates for the debug flags and editor settings.

---


<a id="class-editorexportplatform-method-get-current-presets"></a>

[Array](class_array.md#class-array) **get_current_presets**() const [🔗](class_editorexportplatform.md#class-editorexportplatform-method-get-current-presets)

Returns array of [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset)s for this platform.

---


<a id="class-editorexportplatform-method-get-forced-export-files"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_forced_export_files**(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset) = null) static [🔗](class_editorexportplatform.md#class-editorexportplatform-method-get-forced-export-files)

Returns array of core file names that always should be exported regardless of preset config.

---


<a id="class-editorexportplatform-method-get-internal-export-files"></a>

[Dictionary](class_dictionary.md#class-dictionary) **get_internal_export_files**(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool)) [🔗](class_editorexportplatform.md#class-editorexportplatform-method-get-internal-export-files)

Returns additional files that should always be exported regardless of preset configuration, and are not part of the project source. The returned [Dictionary](class_dictionary.md#class-dictionary) contains filename keys ([String](class_string.md#class-string)) and their corresponding raw data ([PackedByteArray](class_packedbytearray.md#class-packedbytearray)).

---


<a id="class-editorexportplatform-method-get-message-category"></a>

[String](class_string.md#class-string) **get_message_category**(index: [int](class_int.md#class-int)) const [🔗](class_editorexportplatform.md#class-editorexportplatform-method-get-message-category)

Returns the message category for the message with the given `index`.

---


<a id="class-editorexportplatform-method-get-message-count"></a>

[int](class_int.md#class-int) **get_message_count**() const [🔗](class_editorexportplatform.md#class-editorexportplatform-method-get-message-count)

Returns the number of messages in the export log.

---


<a id="class-editorexportplatform-method-get-message-text"></a>

[String](class_string.md#class-string) **get_message_text**(index: [int](class_int.md#class-int)) const [🔗](class_editorexportplatform.md#class-editorexportplatform-method-get-message-text)

Returns the text for the message with the given `index`.

---


<a id="class-editorexportplatform-method-get-message-type"></a>

[ExportMessageType](class_editorexportplatform.md#enum-editorexportplatform-exportmessagetype) **get_message_type**(index: [int](class_int.md#class-int)) const [🔗](class_editorexportplatform.md#class-editorexportplatform-method-get-message-type)

Returns the type for the message with the given `index`.

---


<a id="class-editorexportplatform-method-get-os-name"></a>

[String](class_string.md#class-string) **get_os_name**() const [🔗](class_editorexportplatform.md#class-editorexportplatform-method-get-os-name)

Returns the name of the export operating system handled by this **EditorExportPlatform** class, as a friendly string. Possible return values are `Windows`, `Linux`, `macOS`, `Android`, `iOS`, and `Web`.

---


<a id="class-editorexportplatform-method-get-worst-message-type"></a>

[ExportMessageType](class_editorexportplatform.md#enum-editorexportplatform-exportmessagetype) **get_worst_message_type**() const [🔗](class_editorexportplatform.md#class-editorexportplatform-method-get-worst-message-type)

Returns most severe message type currently present in the export log.

---


<a id="class-editorexportplatform-method-save-pack"></a>

[Dictionary](class_dictionary.md#class-dictionary) **save_pack**(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool), path: [String](class_string.md#class-string), embed: [bool](class_bool.md#class-bool) = false) [🔗](class_editorexportplatform.md#class-editorexportplatform-method-save-pack)

Saves PCK archive and returns [Dictionary](class_dictionary.md#class-dictionary) with the following keys: `result: Error`, `so_files: Array` (array of the shared/static objects which contains dictionaries with the following keys: `path: String`, `tags: PackedStringArray`, and `target_folder: String`).

If `embed` is `true`, PCK content is appended to the end of `path` file and return [Dictionary](class_dictionary.md#class-dictionary) additionally include following keys: `embedded_start: int` (embedded PCK offset) and `embedded_size: int` (embedded PCK size).

---


<a id="class-editorexportplatform-method-save-pack-patch"></a>

[Dictionary](class_dictionary.md#class-dictionary) **save_pack_patch**(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool), path: [String](class_string.md#class-string)) [🔗](class_editorexportplatform.md#class-editorexportplatform-method-save-pack-patch)

Saves patch PCK archive and returns [Dictionary](class_dictionary.md#class-dictionary) with the following keys: `result: Error`, `so_files: Array` (array of the shared/static objects which contains dictionaries with the following keys: `path: String`, `tags: PackedStringArray`, and `target_folder: String`).

---


<a id="class-editorexportplatform-method-save-zip"></a>

[Dictionary](class_dictionary.md#class-dictionary) **save_zip**(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool), path: [String](class_string.md#class-string)) [🔗](class_editorexportplatform.md#class-editorexportplatform-method-save-zip)

Saves ZIP archive and returns [Dictionary](class_dictionary.md#class-dictionary) with the following keys: `result: Error`, `so_files: Array` (array of the shared/static objects which contains dictionaries with the following keys: `path: String`, `tags: PackedStringArray`, and `target_folder: String`).

---


<a id="class-editorexportplatform-method-save-zip-patch"></a>

[Dictionary](class_dictionary.md#class-dictionary) **save_zip_patch**(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool), path: [String](class_string.md#class-string)) [🔗](class_editorexportplatform.md#class-editorexportplatform-method-save-zip-patch)

Saves patch ZIP archive and returns [Dictionary](class_dictionary.md#class-dictionary) with the following keys: `result: Error`, `so_files: Array` (array of the shared/static objects which contains dictionaries with the following keys: `path: String`, `tags: PackedStringArray`, and `target_folder: String`).

---


<a id="class-editorexportplatform-method-ssh-push-to-remote"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **ssh_push_to_remote**(host: [String](class_string.md#class-string), port: [String](class_string.md#class-string), scp_args: [PackedStringArray](class_packedstringarray.md#class-packedstringarray), src_file: [String](class_string.md#class-string), dst_file: [String](class_string.md#class-string)) const [🔗](class_editorexportplatform.md#class-editorexportplatform-method-ssh-push-to-remote)

Uploads specified file over SCP protocol to the remote host.

---


<a id="class-editorexportplatform-method-ssh-run-on-remote"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **ssh_run_on_remote**(host: [String](class_string.md#class-string), port: [String](class_string.md#class-string), ssh_arg: [PackedStringArray](class_packedstringarray.md#class-packedstringarray), cmd_args: [String](class_string.md#class-string), output: [Array](class_array.md#class-array) = [], port_fwd: [int](class_int.md#class-int) = -1) const [🔗](class_editorexportplatform.md#class-editorexportplatform-method-ssh-run-on-remote)

Executes specified command on the remote host via SSH protocol and returns command output in the `output`.

---


<a id="class-editorexportplatform-method-ssh-run-on-remote-no-wait"></a>

[int](class_int.md#class-int) **ssh_run_on_remote_no_wait**(host: [String](class_string.md#class-string), port: [String](class_string.md#class-string), ssh_args: [PackedStringArray](class_packedstringarray.md#class-packedstringarray), cmd_args: [String](class_string.md#class-string), port_fwd: [int](class_int.md#class-int) = -1) const [🔗](class_editorexportplatform.md#class-editorexportplatform-method-ssh-run-on-remote-no-wait)

Executes specified command on the remote host via SSH protocol and returns process ID (on the remote host) without waiting for command to finish.
