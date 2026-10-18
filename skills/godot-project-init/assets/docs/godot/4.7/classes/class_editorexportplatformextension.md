> Source: https://docs.godotengine.org/en/4.7/classes/class_editorexportplatformextension.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="editorexportplatformextension"></a>

<a id="class-editorexportplatformextension"></a>

# EditorExportPlatformExtension

**Inherits:** [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Base class for custom [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform) implementations (plugins).

<a id="description"></a>

## Description

External [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform) implementations should inherit from this class.

To use [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform), register it using the [EditorPlugin.add_export_platform()](class_editorplugin.md#class-editorplugin-method-add-export-platform) method first.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [_can_export](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-can-export)(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool)) virtual const |
| void | [_cleanup](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-cleanup)() virtual |
| [Error](class_@globalscope.md#enum-globalscope-error) | [_export_pack](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-export-pack)(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool), path: [String](class_string.md#class-string), flags: BitField[[DebugFlags](class_editorexportplatform.md#enum-editorexportplatform-debugflags)]) virtual |
| [Error](class_@globalscope.md#enum-globalscope-error) | [_export_pack_patch](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-export-pack-patch)(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool), path: [String](class_string.md#class-string), patches: [PackedStringArray](class_packedstringarray.md#class-packedstringarray), flags: BitField[[DebugFlags](class_editorexportplatform.md#enum-editorexportplatform-debugflags)]) virtual |
| [Error](class_@globalscope.md#enum-globalscope-error) | [_export_project](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-export-project)(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool), path: [String](class_string.md#class-string), flags: BitField[[DebugFlags](class_editorexportplatform.md#enum-editorexportplatform-debugflags)]) virtual required |
| [Error](class_@globalscope.md#enum-globalscope-error) | [_export_zip](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-export-zip)(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool), path: [String](class_string.md#class-string), flags: BitField[[DebugFlags](class_editorexportplatform.md#enum-editorexportplatform-debugflags)]) virtual |
| [Error](class_@globalscope.md#enum-globalscope-error) | [_export_zip_patch](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-export-zip-patch)(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool), path: [String](class_string.md#class-string), patches: [PackedStringArray](class_packedstringarray.md#class-packedstringarray), flags: BitField[[DebugFlags](class_editorexportplatform.md#enum-editorexportplatform-debugflags)]) virtual |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [_get_binary_extensions](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-get-binary-extensions)(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset)) virtual required const |
| [String](class_string.md#class-string) | [_get_debug_protocol](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-get-debug-protocol)() virtual const |
| [String](class_string.md#class-string) | [_get_device_architecture](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-get-device-architecture)(device: [int](class_int.md#class-int)) virtual const |
| [bool](class_bool.md#class-bool) | [_get_export_option_visibility](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-get-export-option-visibility)(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), option: [String](class_string.md#class-string)) virtual const |
| [String](class_string.md#class-string) | [_get_export_option_warning](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-get-export-option-warning)(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), option: [StringName](class_stringname.md#class-stringname)) virtual const |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | [_get_export_options](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-get-export-options)() virtual const |
| [Texture2D](class_texture2d.md#class-texture2d) | [_get_logo](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-get-logo)() virtual required const |
| [String](class_string.md#class-string) | [_get_name](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-get-name)() virtual required const |
| [Texture2D](class_texture2d.md#class-texture2d) | [_get_option_icon](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-get-option-icon)(device: [int](class_int.md#class-int)) virtual const |
| [String](class_string.md#class-string) | [_get_option_label](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-get-option-label)(device: [int](class_int.md#class-int)) virtual const |
| [String](class_string.md#class-string) | [_get_option_tooltip](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-get-option-tooltip)(device: [int](class_int.md#class-int)) virtual const |
| [int](class_int.md#class-int) | [_get_options_count](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-get-options-count)() virtual const |
| [String](class_string.md#class-string) | [_get_options_tooltip](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-get-options-tooltip)() virtual const |
| [String](class_string.md#class-string) | [_get_os_name](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-get-os-name)() virtual required const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [_get_platform_features](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-get-platform-features)() virtual required const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [_get_preset_features](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-get-preset-features)(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset)) virtual required const |
| [Texture2D](class_texture2d.md#class-texture2d) | [_get_run_icon](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-get-run-icon)() virtual const |
| [bool](class_bool.md#class-bool) | [_has_valid_export_configuration](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-has-valid-export-configuration)(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool)) virtual required const |
| [bool](class_bool.md#class-bool) | [_has_valid_project_configuration](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-has-valid-project-configuration)(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset)) virtual required const |
| void | [_initialize](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-initialize)() virtual |
| [bool](class_bool.md#class-bool) | [_is_executable](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-is-executable)(path: [String](class_string.md#class-string)) virtual const |
| [bool](class_bool.md#class-bool) | [_poll_export](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-poll-export)() virtual |
| [Error](class_@globalscope.md#enum-globalscope-error) | [_run](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-run)(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), device: [int](class_int.md#class-int), debug_flags: BitField[[DebugFlags](class_editorexportplatform.md#enum-editorexportplatform-debugflags)]) virtual |
| [bool](class_bool.md#class-bool) | [_should_update_export_options](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-should-update-export-options)() virtual |
| [String](class_string.md#class-string) | [get_config_error](class_editorexportplatformextension.md#class-editorexportplatformextension-method-get-config-error)() const |
| [bool](class_bool.md#class-bool) | [get_config_missing_templates](class_editorexportplatformextension.md#class-editorexportplatformextension-method-get-config-missing-templates)() const |
| void | [set_config_error](class_editorexportplatformextension.md#class-editorexportplatformextension-method-set-config-error)(error_text: [String](class_string.md#class-string)) const |
| void | [set_config_missing_templates](class_editorexportplatformextension.md#class-editorexportplatformextension-method-set-config-missing-templates)(missing_templates: [bool](class_bool.md#class-bool)) const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-editorexportplatformextension-private-method-can-export"></a>

[bool](class_bool.md#class-bool) **_can_export**(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool)) virtual const [🔗](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-can-export)

Returns `true` if the specified `preset` is valid and can be exported. Use [set_config_error()](class_editorexportplatformextension.md#class-editorexportplatformextension-method-set-config-error) and [set_config_missing_templates()](class_editorexportplatformextension.md#class-editorexportplatformextension-method-set-config-missing-templates) to set error details.

Usual implementations call [_has_valid_export_configuration()](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-has-valid-export-configuration) and [_has_valid_project_configuration()](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-has-valid-project-configuration) to determine if exporting is possible.

---


<a id="class-editorexportplatformextension-private-method-cleanup"></a>

void **_cleanup**() virtual [🔗](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-cleanup)

Called by the editor before platform is unregistered.

---


<a id="class-editorexportplatformextension-private-method-export-pack"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **_export_pack**(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool), path: [String](class_string.md#class-string), flags: BitField[[DebugFlags](class_editorexportplatform.md#enum-editorexportplatform-debugflags)]) virtual [🔗](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-export-pack)

Creates a PCK archive at `path` for the specified `preset`.

This method is called when "Export PCK/ZIP" button is pressed in the export dialog, with "Export as Patch" disabled, and PCK is selected as a file type.

---


<a id="class-editorexportplatformextension-private-method-export-pack-patch"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **_export_pack_patch**(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool), path: [String](class_string.md#class-string), patches: [PackedStringArray](class_packedstringarray.md#class-packedstringarray), flags: BitField[[DebugFlags](class_editorexportplatform.md#enum-editorexportplatform-debugflags)]) virtual [🔗](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-export-pack-patch)

Creates a patch PCK archive at `path` for the specified `preset`, containing only the files that have changed since the last patch.

This method is called when "Export PCK/ZIP" button is pressed in the export dialog, with "Export as Patch" enabled, and PCK is selected as a file type.

**Note:** The patches provided in `patches` have already been loaded when this method is called and are merely provided as context. When empty the patches defined in the export preset have been loaded instead.

---


<a id="class-editorexportplatformextension-private-method-export-project"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **_export_project**(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool), path: [String](class_string.md#class-string), flags: BitField[[DebugFlags](class_editorexportplatform.md#enum-editorexportplatform-debugflags)]) virtual required [🔗](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-export-project)

Creates a full project at `path` for the specified `preset`.

This method is called when "Export" button is pressed in the export dialog.

This method implementation can call [EditorExportPlatform.save_pack()](class_editorexportplatform.md#class-editorexportplatform-method-save-pack) or [EditorExportPlatform.save_zip()](class_editorexportplatform.md#class-editorexportplatform-method-save-zip) to use default PCK/ZIP export process, or calls [EditorExportPlatform.export_project_files()](class_editorexportplatform.md#class-editorexportplatform-method-export-project-files) and implement custom callback for processing each exported file.

---


<a id="class-editorexportplatformextension-private-method-export-zip"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **_export_zip**(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool), path: [String](class_string.md#class-string), flags: BitField[[DebugFlags](class_editorexportplatform.md#enum-editorexportplatform-debugflags)]) virtual [🔗](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-export-zip)

Create a ZIP archive at `path` for the specified `preset`.

This method is called when "Export PCK/ZIP" button is pressed in the export dialog, with "Export as Patch" disabled, and ZIP is selected as a file type.

---


<a id="class-editorexportplatformextension-private-method-export-zip-patch"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **_export_zip_patch**(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool), path: [String](class_string.md#class-string), patches: [PackedStringArray](class_packedstringarray.md#class-packedstringarray), flags: BitField[[DebugFlags](class_editorexportplatform.md#enum-editorexportplatform-debugflags)]) virtual [🔗](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-export-zip-patch)

Create a ZIP archive at `path` for the specified `preset`, containing only the files that have changed since the last patch.

This method is called when "Export PCK/ZIP" button is pressed in the export dialog, with "Export as Patch" enabled, and ZIP is selected as a file type.

**Note:** The patches provided in `patches` have already been loaded when this method is called and are merely provided as context. When empty the patches defined in the export preset have been loaded instead.

---


<a id="class-editorexportplatformextension-private-method-get-binary-extensions"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **_get_binary_extensions**(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset)) virtual required const [🔗](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-get-binary-extensions)

Returns array of supported binary extensions for the full project export.

---


<a id="class-editorexportplatformextension-private-method-get-debug-protocol"></a>

[String](class_string.md#class-string) **_get_debug_protocol**() virtual const [🔗](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-get-debug-protocol)

Returns protocol used for remote debugging. Default implementation return `tcp://`.

---


<a id="class-editorexportplatformextension-private-method-get-device-architecture"></a>

[String](class_string.md#class-string) **_get_device_architecture**(device: [int](class_int.md#class-int)) virtual const [🔗](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-get-device-architecture)

Returns device architecture for one-click deploy.

---


<a id="class-editorexportplatformextension-private-method-get-export-option-visibility"></a>

[bool](class_bool.md#class-bool) **_get_export_option_visibility**(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), option: [String](class_string.md#class-string)) virtual const [🔗](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-get-export-option-visibility)

Validates `option` and returns visibility for the specified `preset`. Default implementation return `true` for all options.

---


<a id="class-editorexportplatformextension-private-method-get-export-option-warning"></a>

[String](class_string.md#class-string) **_get_export_option_warning**(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), option: [StringName](class_stringname.md#class-stringname)) virtual const [🔗](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-get-export-option-warning)

Validates `option` and returns warning message for the specified `preset`. Default implementation return empty string for all options.

---


<a id="class-editorexportplatformextension-private-method-get-export-options"></a>

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **_get_export_options**() virtual const [🔗](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-get-export-options)

Returns a property list, as an [Array](class_array.md#class-array) of dictionaries. Each [Dictionary](class_dictionary.md#class-dictionary) must at least contain the `name: StringName` and `type: Variant.Type` entries.

Additionally, the following keys are supported:

- `hint: PropertyHint`
- `hint_string: String`
- `usage: PropertyUsageFlags`
- `class_name: StringName`
- `default_value: Variant`, default value of the property.
- `update_visibility: bool`, if set to `true`, [_get_export_option_visibility()](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-get-export-option-visibility) is called for each property when this property is changed.
- `required: bool`, if set to `true`, this property warnings are critical, and should be resolved to make export possible. This value is a hint for the [_has_valid_export_configuration()](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-has-valid-export-configuration) implementation, and not used by the engine directly.

See also [Object._get_property_list()](class_object.md#class-object-private-method-get-property-list).

---


<a id="class-editorexportplatformextension-private-method-get-logo"></a>

[Texture2D](class_texture2d.md#class-texture2d) **_get_logo**() virtual required const [🔗](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-get-logo)

Returns the platform logo displayed in the export dialog. The logo should be 32×32 pixels, adjusted for the current editor scale (see [EditorInterface.get_editor_scale()](class_editorinterface.md#class-editorinterface-method-get-editor-scale)).

---


<a id="class-editorexportplatformextension-private-method-get-name"></a>

[String](class_string.md#class-string) **_get_name**() virtual required const [🔗](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-get-name)

Returns export platform name.

---


<a id="class-editorexportplatformextension-private-method-get-option-icon"></a>

[Texture2D](class_texture2d.md#class-texture2d) **_get_option_icon**(device: [int](class_int.md#class-int)) virtual const [🔗](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-get-option-icon)

Returns the item icon for the specified `device` in the one-click deploy menu. The icon should be 16×16 pixels, adjusted for the current editor scale (see [EditorInterface.get_editor_scale()](class_editorinterface.md#class-editorinterface-method-get-editor-scale)).

---


<a id="class-editorexportplatformextension-private-method-get-option-label"></a>

[String](class_string.md#class-string) **_get_option_label**(device: [int](class_int.md#class-int)) virtual const [🔗](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-get-option-label)

Returns one-click deploy menu item label for the specified `device`.

---


<a id="class-editorexportplatformextension-private-method-get-option-tooltip"></a>

[String](class_string.md#class-string) **_get_option_tooltip**(device: [int](class_int.md#class-int)) virtual const [🔗](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-get-option-tooltip)

Returns one-click deploy menu item tooltip for the specified `device`.

---


<a id="class-editorexportplatformextension-private-method-get-options-count"></a>

[int](class_int.md#class-int) **_get_options_count**() virtual const [🔗](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-get-options-count)

Returns the number of devices (or other options) available in the one-click deploy menu.

---


<a id="class-editorexportplatformextension-private-method-get-options-tooltip"></a>

[String](class_string.md#class-string) **_get_options_tooltip**() virtual const [🔗](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-get-options-tooltip)

Returns tooltip of the one-click deploy menu button.

---


<a id="class-editorexportplatformextension-private-method-get-os-name"></a>

[String](class_string.md#class-string) **_get_os_name**() virtual required const [🔗](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-get-os-name)

Returns target OS name.

---


<a id="class-editorexportplatformextension-private-method-get-platform-features"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **_get_platform_features**() virtual required const [🔗](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-get-platform-features)

Returns array of platform specific features.

---


<a id="class-editorexportplatformextension-private-method-get-preset-features"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **_get_preset_features**(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset)) virtual required const [🔗](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-get-preset-features)

Returns array of platform specific features for the specified `preset`.

---


<a id="class-editorexportplatformextension-private-method-get-run-icon"></a>

[Texture2D](class_texture2d.md#class-texture2d) **_get_run_icon**() virtual const [🔗](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-get-run-icon)

Returns the icon of the one-click deploy menu button. The icon should be 16×16 pixels, adjusted for the current editor scale (see [EditorInterface.get_editor_scale()](class_editorinterface.md#class-editorinterface-method-get-editor-scale)).

---


<a id="class-editorexportplatformextension-private-method-has-valid-export-configuration"></a>

[bool](class_bool.md#class-bool) **_has_valid_export_configuration**(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool)) virtual required const [🔗](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-has-valid-export-configuration)

Returns `true` if export configuration is valid.

---


<a id="class-editorexportplatformextension-private-method-has-valid-project-configuration"></a>

[bool](class_bool.md#class-bool) **_has_valid_project_configuration**(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset)) virtual required const [🔗](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-has-valid-project-configuration)

Returns `true` if project configuration is valid.

---


<a id="class-editorexportplatformextension-private-method-initialize"></a>

void **_initialize**() virtual [🔗](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-initialize)

Initializes the plugin. Called by the editor when platform is registered.

---


<a id="class-editorexportplatformextension-private-method-is-executable"></a>

[bool](class_bool.md#class-bool) **_is_executable**(path: [String](class_string.md#class-string)) virtual const [🔗](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-is-executable)

Returns `true` if specified file is a valid executable (native executable or script) for the target platform.

---


<a id="class-editorexportplatformextension-private-method-poll-export"></a>

[bool](class_bool.md#class-bool) **_poll_export**() virtual [🔗](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-poll-export)

Returns `true` if one-click deploy options are changed and editor interface should be updated.

---


<a id="class-editorexportplatformextension-private-method-run"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **_run**(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), device: [int](class_int.md#class-int), debug_flags: BitField[[DebugFlags](class_editorexportplatform.md#enum-editorexportplatform-debugflags)]) virtual [🔗](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-run)

This method is called when `device` one-click deploy menu option is selected.

Implementation should export project to a temporary location, upload and run it on the specific `device`, or perform another action associated with the menu item.

---


<a id="class-editorexportplatformextension-private-method-should-update-export-options"></a>

[bool](class_bool.md#class-bool) **_should_update_export_options**() virtual [🔗](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-should-update-export-options)

Returns `true` if export options list is changed and presets should be updated.

---


<a id="class-editorexportplatformextension-method-get-config-error"></a>

[String](class_string.md#class-string) **get_config_error**() const [🔗](class_editorexportplatformextension.md#class-editorexportplatformextension-method-get-config-error)

Returns current configuration error message text. This method should be called only from the [_can_export()](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-can-export), [_has_valid_export_configuration()](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-has-valid-export-configuration), or [_has_valid_project_configuration()](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-has-valid-project-configuration) implementations.

---


<a id="class-editorexportplatformextension-method-get-config-missing-templates"></a>

[bool](class_bool.md#class-bool) **get_config_missing_templates**() const [🔗](class_editorexportplatformextension.md#class-editorexportplatformextension-method-get-config-missing-templates)

Returns `true` is export templates are missing from the current configuration. This method should be called only from the [_can_export()](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-can-export), [_has_valid_export_configuration()](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-has-valid-export-configuration), or [_has_valid_project_configuration()](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-has-valid-project-configuration) implementations.

---


<a id="class-editorexportplatformextension-method-set-config-error"></a>

void **set_config_error**(error_text: [String](class_string.md#class-string)) const [🔗](class_editorexportplatformextension.md#class-editorexportplatformextension-method-set-config-error)

Sets current configuration error message text. This method should be called only from the [_can_export()](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-can-export), [_has_valid_export_configuration()](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-has-valid-export-configuration), or [_has_valid_project_configuration()](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-has-valid-project-configuration) implementations.

---


<a id="class-editorexportplatformextension-method-set-config-missing-templates"></a>

void **set_config_missing_templates**(missing_templates: [bool](class_bool.md#class-bool)) const [🔗](class_editorexportplatformextension.md#class-editorexportplatformextension-method-set-config-missing-templates)

Set to `true` is export templates are missing from the current configuration. This method should be called only from the [_can_export()](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-can-export), [_has_valid_export_configuration()](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-has-valid-export-configuration), or [_has_valid_project_configuration()](class_editorexportplatformextension.md#class-editorexportplatformextension-private-method-has-valid-project-configuration) implementations.
