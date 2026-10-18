> Source: https://docs.godotengine.org/en/4.7/classes/class_gdextensionmanager.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="gdextensionmanager"></a>

<a id="class-gdextensionmanager"></a>

# GDExtensionManager

**Inherits:** [Object](class_object.md#class-object)

Provides access to GDExtension functionality.

<a id="description"></a>

## Description

The GDExtensionManager loads, initializes, and keeps track of all available [GDExtension](class_gdextension.md#class-gdextension) libraries in the project.

**Note:** Do not worry about GDExtension unless you know what you are doing.

<a id="tutorials"></a>

## Tutorials

- [GDExtension overview](../engine_details/engine_api/gdextension/what_is_gdextension.md)
- [GDExtension example in C++](../tutorials/scripting/cpp/gdextension_cpp_example.md)

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [GDExtension](class_gdextension.md#class-gdextension) | [get_extension](class_gdextensionmanager.md#class-gdextensionmanager-method-get-extension)(path: [String](class_string.md#class-string)) |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [get_loaded_extensions](class_gdextensionmanager.md#class-gdextensionmanager-method-get-loaded-extensions)() const |
| [bool](class_bool.md#class-bool) | [is_extension_loaded](class_gdextensionmanager.md#class-gdextensionmanager-method-is-extension-loaded)(path: [String](class_string.md#class-string)) const |
| [LoadStatus](class_gdextensionmanager.md#enum-gdextensionmanager-loadstatus) | [load_extension](class_gdextensionmanager.md#class-gdextensionmanager-method-load-extension)(path: [String](class_string.md#class-string)) |
| [LoadStatus](class_gdextensionmanager.md#enum-gdextensionmanager-loadstatus) | [load_extension_from_function](class_gdextensionmanager.md#class-gdextensionmanager-method-load-extension-from-function)(path: [String](class_string.md#class-string), init_func: `const GDExtensionInitializationFunction*`) |
| [LoadStatus](class_gdextensionmanager.md#enum-gdextensionmanager-loadstatus) | [reload_extension](class_gdextensionmanager.md#class-gdextensionmanager-method-reload-extension)(path: [String](class_string.md#class-string)) |
| [LoadStatus](class_gdextensionmanager.md#enum-gdextensionmanager-loadstatus) | [unload_extension](class_gdextensionmanager.md#class-gdextensionmanager-method-unload-extension)(path: [String](class_string.md#class-string)) |

---


<a id="signals"></a>

## Signals

<a id="class-gdextensionmanager-signal-extension-loaded"></a>

**extension_loaded**(extension: [GDExtension](class_gdextension.md#class-gdextension)) [🔗](class_gdextensionmanager.md#class-gdextensionmanager-signal-extension-loaded)

Emitted after the editor has finished loading a new extension.

**Note:** This signal is only emitted in editor builds.

---


<a id="class-gdextensionmanager-signal-extension-unloading"></a>

**extension_unloading**(extension: [GDExtension](class_gdextension.md#class-gdextension)) [🔗](class_gdextensionmanager.md#class-gdextensionmanager-signal-extension-unloading)

Emitted before the editor starts unloading an extension.

**Note:** This signal is only emitted in editor builds.

---


<a id="class-gdextensionmanager-signal-extensions-reloaded"></a>

**extensions_reloaded**() [🔗](class_gdextensionmanager.md#class-gdextensionmanager-signal-extensions-reloaded)

Emitted after the editor has finished reloading one or more extensions.

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-gdextensionmanager-loadstatus"></a>

enum **LoadStatus**: [🔗](class_gdextensionmanager.md#enum-gdextensionmanager-loadstatus)

<a id="class-gdextensionmanager-constant-load-status-ok"></a>

[LoadStatus](class_gdextensionmanager.md#enum-gdextensionmanager-loadstatus) **LOAD_STATUS_OK** = `0`

The extension has loaded successfully.

<a id="class-gdextensionmanager-constant-load-status-failed"></a>

[LoadStatus](class_gdextensionmanager.md#enum-gdextensionmanager-loadstatus) **LOAD_STATUS_FAILED** = `1`

The extension has failed to load, possibly because it does not exist or has missing dependencies.

<a id="class-gdextensionmanager-constant-load-status-already-loaded"></a>

[LoadStatus](class_gdextensionmanager.md#enum-gdextensionmanager-loadstatus) **LOAD_STATUS_ALREADY_LOADED** = `2`

The extension has already been loaded.

<a id="class-gdextensionmanager-constant-load-status-not-loaded"></a>

[LoadStatus](class_gdextensionmanager.md#enum-gdextensionmanager-loadstatus) **LOAD_STATUS_NOT_LOADED** = `3`

The extension has not been loaded.

<a id="class-gdextensionmanager-constant-load-status-needs-restart"></a>

[LoadStatus](class_gdextensionmanager.md#enum-gdextensionmanager-loadstatus) **LOAD_STATUS_NEEDS_RESTART** = `4`

The extension requires the application to restart to fully load.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-gdextensionmanager-method-get-extension"></a>

[GDExtension](class_gdextension.md#class-gdextension) **get_extension**(path: [String](class_string.md#class-string)) [🔗](class_gdextensionmanager.md#class-gdextensionmanager-method-get-extension)

Returns the [GDExtension](class_gdextension.md#class-gdextension) at the given file `path`, or `null` if it has not been loaded or does not exist.

---


<a id="class-gdextensionmanager-method-get-loaded-extensions"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_loaded_extensions**() const [🔗](class_gdextensionmanager.md#class-gdextensionmanager-method-get-loaded-extensions)

Returns the file paths of all currently loaded extensions.

---


<a id="class-gdextensionmanager-method-is-extension-loaded"></a>

[bool](class_bool.md#class-bool) **is_extension_loaded**(path: [String](class_string.md#class-string)) const [🔗](class_gdextensionmanager.md#class-gdextensionmanager-method-is-extension-loaded)

Returns `true` if the extension at the given file `path` has already been loaded successfully. See also [get_loaded_extensions()](class_gdextensionmanager.md#class-gdextensionmanager-method-get-loaded-extensions).

---


<a id="class-gdextensionmanager-method-load-extension"></a>

[LoadStatus](class_gdextensionmanager.md#enum-gdextensionmanager-loadstatus) **load_extension**(path: [String](class_string.md#class-string)) [🔗](class_gdextensionmanager.md#class-gdextensionmanager-method-load-extension)

Loads an extension by absolute file path. The `path` needs to point to a valid [GDExtension](class_gdextension.md#class-gdextension). Returns [LOAD_STATUS_OK](class_gdextensionmanager.md#class-gdextensionmanager-constant-load-status-ok) if successful.

---


<a id="class-gdextensionmanager-method-load-extension-from-function"></a>

[LoadStatus](class_gdextensionmanager.md#enum-gdextensionmanager-loadstatus) **load_extension_from_function**(path: [String](class_string.md#class-string), init_func: `const GDExtensionInitializationFunction*`) [🔗](class_gdextensionmanager.md#class-gdextensionmanager-method-load-extension-from-function)

Loads the extension already in address space via the given path and initialization function. The `path` needs to be unique and start with `"libgodot://"`. Returns [LOAD_STATUS_OK](class_gdextensionmanager.md#class-gdextensionmanager-constant-load-status-ok) if successful.

---


<a id="class-gdextensionmanager-method-reload-extension"></a>

[LoadStatus](class_gdextensionmanager.md#enum-gdextensionmanager-loadstatus) **reload_extension**(path: [String](class_string.md#class-string)) [🔗](class_gdextensionmanager.md#class-gdextensionmanager-method-reload-extension)

Reloads the extension at the given file path. The `path` needs to point to a valid [GDExtension](class_gdextension.md#class-gdextension), otherwise this method may return either [LOAD_STATUS_NOT_LOADED](class_gdextensionmanager.md#class-gdextensionmanager-constant-load-status-not-loaded) or [LOAD_STATUS_FAILED](class_gdextensionmanager.md#class-gdextensionmanager-constant-load-status-failed).

**Note:** You can only reload extensions in the editor. In release builds, this method always fails and returns [LOAD_STATUS_FAILED](class_gdextensionmanager.md#class-gdextensionmanager-constant-load-status-failed).

---


<a id="class-gdextensionmanager-method-unload-extension"></a>

[LoadStatus](class_gdextensionmanager.md#enum-gdextensionmanager-loadstatus) **unload_extension**(path: [String](class_string.md#class-string)) [🔗](class_gdextensionmanager.md#class-gdextensionmanager-method-unload-extension)

Unloads an extension by file path. The `path` needs to point to an already loaded [GDExtension](class_gdextension.md#class-gdextension), otherwise this method returns [LOAD_STATUS_NOT_LOADED](class_gdextensionmanager.md#class-gdextensionmanager-constant-load-status-not-loaded).
