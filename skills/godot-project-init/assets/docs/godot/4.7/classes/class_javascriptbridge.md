> Source: https://docs.godotengine.org/en/4.7/classes/class_javascriptbridge.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="javascriptbridge"></a>

<a id="class-javascriptbridge"></a>

# JavaScriptBridge

**Inherits:** [Object](class_object.md#class-object)

Singleton that connects the engine with the browser's JavaScript context in Web export.

<a id="description"></a>

## Description

The JavaScriptBridge singleton is implemented only in the Web export. It's used to access the browser's JavaScript context. This allows interaction with embedding pages or calling third-party JavaScript APIs.

**Note:** This singleton can be disabled at build-time to improve security. By default, the JavaScriptBridge singleton is enabled. Official export templates also have the JavaScriptBridge singleton enabled. See [Compiling for the Web](../engine_details/development/compiling/compiling_for_web.md) in the documentation for more information.

<a id="tutorials"></a>

## Tutorials

- [The JavaScriptBridge singleton](../tutorials/platform/web/javascript_bridge.md)

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [JavaScriptObject](class_javascriptobject.md#class-javascriptobject) | [create_callback](class_javascriptbridge.md#class-javascriptbridge-method-create-callback)(callable: [Callable](class_callable.md#class-callable)) |
| [Variant](class_variant.md#class-variant) | [create_object](class_javascriptbridge.md#class-javascriptbridge-method-create-object)(object: [String](class_string.md#class-string), ...) vararg |
| void | [download_buffer](class_javascriptbridge.md#class-javascriptbridge-method-download-buffer)(buffer: [PackedByteArray](class_packedbytearray.md#class-packedbytearray), name: [String](class_string.md#class-string), mime: [String](class_string.md#class-string) = "application/octet-stream") |
| [Variant](class_variant.md#class-variant) | [eval](class_javascriptbridge.md#class-javascriptbridge-method-eval)(code: [String](class_string.md#class-string), use_global_execution_context: [bool](class_bool.md#class-bool) = false) |
| void | [force_fs_sync](class_javascriptbridge.md#class-javascriptbridge-method-force-fs-sync)() |
| [JavaScriptObject](class_javascriptobject.md#class-javascriptobject) | [get_interface](class_javascriptbridge.md#class-javascriptbridge-method-get-interface)(interface: [String](class_string.md#class-string)) |
| [bool](class_bool.md#class-bool) | [is_js_buffer](class_javascriptbridge.md#class-javascriptbridge-method-is-js-buffer)(javascript_object: [JavaScriptObject](class_javascriptobject.md#class-javascriptobject)) |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray) | [js_buffer_to_packed_byte_array](class_javascriptbridge.md#class-javascriptbridge-method-js-buffer-to-packed-byte-array)(javascript_buffer: [JavaScriptObject](class_javascriptobject.md#class-javascriptobject)) |
| [bool](class_bool.md#class-bool) | [pwa_needs_update](class_javascriptbridge.md#class-javascriptbridge-method-pwa-needs-update)() const |
| [Error](class_@globalscope.md#enum-globalscope-error) | [pwa_update](class_javascriptbridge.md#class-javascriptbridge-method-pwa-update)() |

---


<a id="signals"></a>

## Signals

<a id="class-javascriptbridge-signal-pwa-update-available"></a>

**pwa_update_available**() [🔗](class_javascriptbridge.md#class-javascriptbridge-signal-pwa-update-available)

Emitted when an update for this progressive web app has been detected but is waiting to be activated because a previous version is active. See [pwa_update()](class_javascriptbridge.md#class-javascriptbridge-method-pwa-update) to force the update to take place immediately.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-javascriptbridge-method-create-callback"></a>

[JavaScriptObject](class_javascriptobject.md#class-javascriptobject) **create_callback**(callable: [Callable](class_callable.md#class-callable)) [🔗](class_javascriptbridge.md#class-javascriptbridge-method-create-callback)

Creates a reference to a [Callable](class_callable.md#class-callable) that can be used as a callback by JavaScript. The reference must be kept until the callback happens, or it won't be called at all. See [JavaScriptObject](class_javascriptobject.md#class-javascriptobject) for usage.

**Note:** The callback function must take exactly one [Array](class_array.md#class-array) argument, which is going to be the JavaScript [arguments object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments) converted to an array.

---


<a id="class-javascriptbridge-method-create-object"></a>

[Variant](class_variant.md#class-variant) **create_object**(object: [String](class_string.md#class-string), ...) vararg [🔗](class_javascriptbridge.md#class-javascriptbridge-method-create-object)

Creates a new JavaScript object using the `new` constructor. The `object` must a valid property of the JavaScript `window`. See [JavaScriptObject](class_javascriptobject.md#class-javascriptobject) for usage.

---


<a id="class-javascriptbridge-method-download-buffer"></a>

void **download_buffer**(buffer: [PackedByteArray](class_packedbytearray.md#class-packedbytearray), name: [String](class_string.md#class-string), mime: [String](class_string.md#class-string) = "application/octet-stream") [🔗](class_javascriptbridge.md#class-javascriptbridge-method-download-buffer)

Prompts the user to download a file containing the specified `buffer`. The file will have the given `name` and `mime` type.

**Note:** The browser may override the [MIME type](https://en.wikipedia.org/wiki/Media_type) provided based on the file `name`'s extension.

**Note:** Browsers might block the download if [download_buffer()](class_javascriptbridge.md#class-javascriptbridge-method-download-buffer) is not being called from a user interaction (e.g. button click).

**Note:** Browsers might ask the user for permission or block the download if multiple download requests are made in a quick succession.

---


<a id="class-javascriptbridge-method-eval"></a>

[Variant](class_variant.md#class-variant) **eval**(code: [String](class_string.md#class-string), use_global_execution_context: [bool](class_bool.md#class-bool) = false) [🔗](class_javascriptbridge.md#class-javascriptbridge-method-eval)

Execute the string `code` as JavaScript code within the browser window. This is a call to the actual global JavaScript function `eval()`.

If `use_global_execution_context` is `true`, the code will be evaluated in the global execution context. Otherwise, it is evaluated in the execution context of a function within the engine's runtime environment.

---


<a id="class-javascriptbridge-method-force-fs-sync"></a>

void **force_fs_sync**() [🔗](class_javascriptbridge.md#class-javascriptbridge-method-force-fs-sync)

Force synchronization of the persistent file system (when enabled).

**Note:** This is only useful for modules or extensions that can't use [FileAccess](class_fileaccess.md#class-fileaccess) to write files.

---


<a id="class-javascriptbridge-method-get-interface"></a>

[JavaScriptObject](class_javascriptobject.md#class-javascriptobject) **get_interface**(interface: [String](class_string.md#class-string)) [🔗](class_javascriptbridge.md#class-javascriptbridge-method-get-interface)

Returns an interface to a JavaScript object that can be used by scripts. The `interface` must be a valid property of the JavaScript `window`. The callback must accept a single [Array](class_array.md#class-array) argument, which will contain the JavaScript `arguments`. See [JavaScriptObject](class_javascriptobject.md#class-javascriptobject) for usage.

---


<a id="class-javascriptbridge-method-is-js-buffer"></a>

[bool](class_bool.md#class-bool) **is_js_buffer**(javascript_object: [JavaScriptObject](class_javascriptobject.md#class-javascriptobject)) [🔗](class_javascriptbridge.md#class-javascriptbridge-method-is-js-buffer)

Returns `true` if the given `javascript_object` is of type [ArrayBuffer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer), [DataView](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView), or one of the many [typed array objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray).

---


<a id="class-javascriptbridge-method-js-buffer-to-packed-byte-array"></a>

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **js_buffer_to_packed_byte_array**(javascript_buffer: [JavaScriptObject](class_javascriptobject.md#class-javascriptobject)) [🔗](class_javascriptbridge.md#class-javascriptbridge-method-js-buffer-to-packed-byte-array)

Returns a copy of `javascript_buffer`'s contents as a [PackedByteArray](class_packedbytearray.md#class-packedbytearray). See also [is_js_buffer()](class_javascriptbridge.md#class-javascriptbridge-method-is-js-buffer).

---


<a id="class-javascriptbridge-method-pwa-needs-update"></a>

[bool](class_bool.md#class-bool) **pwa_needs_update**() const [🔗](class_javascriptbridge.md#class-javascriptbridge-method-pwa-needs-update)

Returns `true` if a new version of the progressive web app is waiting to be activated.

**Note:** Only relevant when exported as a Progressive Web App.

---


<a id="class-javascriptbridge-method-pwa-update"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **pwa_update**() [🔗](class_javascriptbridge.md#class-javascriptbridge-method-pwa-update)

Performs the live update of the progressive web app. Forcing the new version to be installed and the page to be reloaded.

**Note:** Your application will be **reloaded in all browser tabs**.

**Note:** Only relevant when exported as a Progressive Web App and [pwa_needs_update()](class_javascriptbridge.md#class-javascriptbridge-method-pwa-needs-update) returns `true`.
