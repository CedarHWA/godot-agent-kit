> Source: https://docs.godotengine.org/en/4.7/classes/class_gdscriptlanguageprotocol.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="gdscriptlanguageprotocol"></a>

<a id="class-gdscriptlanguageprotocol"></a>

# GDScriptLanguageProtocol

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [JSONRPC](class_jsonrpc.md#class-jsonrpc) **<** [Object](class_object.md#class-object)

GDScript language server.

<a id="description"></a>

## Description

Provides access to certain features that are implemented in the language server.

**Note:** This class is not a language server client that can be used to access LSP functionality. It only provides access to a limited set of features that is implemented using the same technical foundation as the language server.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [GDScriptTextDocument](class_gdscripttextdocument.md#class-gdscripttextdocument) | [get_text_document](class_gdscriptlanguageprotocol.md#class-gdscriptlanguageprotocol-method-get-text-document)() |
| [GDScriptWorkspace](class_gdscriptworkspace.md#class-gdscriptworkspace) | [get_workspace](class_gdscriptlanguageprotocol.md#class-gdscriptlanguageprotocol-method-get-workspace)() |
| [Variant](class_variant.md#class-variant) | [initialize](class_gdscriptlanguageprotocol.md#class-gdscriptlanguageprotocol-method-initialize)(params: [Dictionary](class_dictionary.md#class-dictionary)) |
| void | [initialized](class_gdscriptlanguageprotocol.md#class-gdscriptlanguageprotocol-method-initialized)(params: [Variant](class_variant.md#class-variant)) |
| [bool](class_bool.md#class-bool) | [is_initialized](class_gdscriptlanguageprotocol.md#class-gdscriptlanguageprotocol-method-is-initialized)() const |
| [bool](class_bool.md#class-bool) | [is_smart_resolve_enabled](class_gdscriptlanguageprotocol.md#class-gdscriptlanguageprotocol-method-is-smart-resolve-enabled)() const |
| void | [notify_client](class_gdscriptlanguageprotocol.md#class-gdscriptlanguageprotocol-method-notify-client)(method: [String](class_string.md#class-string), params: [Variant](class_variant.md#class-variant) = null, client_id: [int](class_int.md#class-int) = -1) |
| [Error](class_@globalscope.md#enum-globalscope-error) | [on_client_connected](class_gdscriptlanguageprotocol.md#class-gdscriptlanguageprotocol-method-on-client-connected)() |
| void | [on_client_disconnected](class_gdscriptlanguageprotocol.md#class-gdscriptlanguageprotocol-method-on-client-disconnected)(client_id: [int](class_int.md#class-int)) |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-gdscriptlanguageprotocol-method-get-text-document"></a>

[GDScriptTextDocument](class_gdscripttextdocument.md#class-gdscripttextdocument) **get_text_document**() [🔗](class_gdscriptlanguageprotocol.md#class-gdscriptlanguageprotocol-method-get-text-document)

**Deprecated:** [GDScriptTextDocument](class_gdscripttextdocument.md#class-gdscripttextdocument) is deprecated.

Returns the language server's [GDScriptTextDocument](class_gdscripttextdocument.md#class-gdscripttextdocument) instance.

---


<a id="class-gdscriptlanguageprotocol-method-get-workspace"></a>

[GDScriptWorkspace](class_gdscriptworkspace.md#class-gdscriptworkspace) **get_workspace**() [🔗](class_gdscriptlanguageprotocol.md#class-gdscriptlanguageprotocol-method-get-workspace)

Returns the language server's [GDScriptWorkspace](class_gdscriptworkspace.md#class-gdscriptworkspace) instance.

---


<a id="class-gdscriptlanguageprotocol-method-initialize"></a>

[Variant](class_variant.md#class-variant) **initialize**(params: [Dictionary](class_dictionary.md#class-dictionary)) [🔗](class_gdscriptlanguageprotocol.md#class-gdscriptlanguageprotocol-method-initialize)

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---


<a id="class-gdscriptlanguageprotocol-method-initialized"></a>

void **initialized**(params: [Variant](class_variant.md#class-variant)) [🔗](class_gdscriptlanguageprotocol.md#class-gdscriptlanguageprotocol-method-initialized)

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---


<a id="class-gdscriptlanguageprotocol-method-is-initialized"></a>

[bool](class_bool.md#class-bool) **is_initialized**() const [🔗](class_gdscriptlanguageprotocol.md#class-gdscriptlanguageprotocol-method-is-initialized)

Returns `true` if the language server was initialized by a language server client, `false` otherwise.

---


<a id="class-gdscriptlanguageprotocol-method-is-smart-resolve-enabled"></a>

[bool](class_bool.md#class-bool) **is_smart_resolve_enabled**() const [🔗](class_gdscriptlanguageprotocol.md#class-gdscriptlanguageprotocol-method-is-smart-resolve-enabled)

Returns `true` if the language server is providing the smart resolve feature, `false` otherwise. The feature can be configured through the editor settings.

---


<a id="class-gdscriptlanguageprotocol-method-notify-client"></a>

void **notify_client**(method: [String](class_string.md#class-string), params: [Variant](class_variant.md#class-variant) = null, client_id: [int](class_int.md#class-int) = -1) [🔗](class_gdscriptlanguageprotocol.md#class-gdscriptlanguageprotocol-method-notify-client)

**Deprecated:** Might result in unwanted side effects for connected clients.

---


<a id="class-gdscriptlanguageprotocol-method-on-client-connected"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **on_client_connected**() [🔗](class_gdscriptlanguageprotocol.md#class-gdscriptlanguageprotocol-method-on-client-connected)

**Deprecated:** Might result in unwanted side effects for connected clients.

---


<a id="class-gdscriptlanguageprotocol-method-on-client-disconnected"></a>

void **on_client_disconnected**(client_id: [int](class_int.md#class-int)) [🔗](class_gdscriptlanguageprotocol.md#class-gdscriptlanguageprotocol-method-on-client-disconnected)

**Deprecated:** Might result in unwanted side effects for connected clients.
