> Source: https://docs.godotengine.org/en/4.7/classes/class_gdscriptworkspace.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="gdscriptworkspace"></a>

<a id="class-gdscriptworkspace"></a>

# GDScriptWorkspace

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Workspace related language server functionality.

<a id="description"></a>

## Description

Provides language server functionality related to the workspace.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [apply_new_signal](class_gdscriptworkspace.md#class-gdscriptworkspace-method-apply-new-signal)(obj: [Object](class_object.md#class-object), function: [String](class_string.md#class-string), args: [PackedStringArray](class_packedstringarray.md#class-packedstringarray)) |
| void | [didDeleteFiles](class_gdscriptworkspace.md#class-gdscriptworkspace-method-diddeletefiles)(params: [Dictionary](class_dictionary.md#class-dictionary)) |
| [Dictionary](class_dictionary.md#class-dictionary) | [generate_script_api](class_gdscriptworkspace.md#class-gdscriptworkspace-method-generate-script-api)(path: [String](class_string.md#class-string)) |
| [String](class_string.md#class-string) | [get_file_path](class_gdscriptworkspace.md#class-gdscriptworkspace-method-get-file-path)(uri: [String](class_string.md#class-string)) |
| [String](class_string.md#class-string) | [get_file_uri](class_gdscriptworkspace.md#class-gdscriptworkspace-method-get-file-uri)(path: [String](class_string.md#class-string)) const |
| [Error](class_@globalscope.md#enum-globalscope-error) | [parse_local_script](class_gdscriptworkspace.md#class-gdscriptworkspace-method-parse-local-script)(path: [String](class_string.md#class-string)) |
| [Error](class_@globalscope.md#enum-globalscope-error) | [parse_script](class_gdscriptworkspace.md#class-gdscriptworkspace-method-parse-script)(path: [String](class_string.md#class-string), content: [String](class_string.md#class-string)) |
| void | [publish_diagnostics](class_gdscriptworkspace.md#class-gdscriptworkspace-method-publish-diagnostics)(path: [String](class_string.md#class-string)) |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-gdscriptworkspace-method-apply-new-signal"></a>

void **apply_new_signal**(obj: [Object](class_object.md#class-object), function: [String](class_string.md#class-string), args: [PackedStringArray](class_packedstringarray.md#class-packedstringarray)) [🔗](class_gdscriptworkspace.md#class-gdscriptworkspace-method-apply-new-signal)

**Deprecated:** Might result in unwanted side effects for connected clients.

---


<a id="class-gdscriptworkspace-method-diddeletefiles"></a>

void **didDeleteFiles**(params: [Dictionary](class_dictionary.md#class-dictionary)) [🔗](class_gdscriptworkspace.md#class-gdscriptworkspace-method-diddeletefiles)

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---


<a id="class-gdscriptworkspace-method-generate-script-api"></a>

[Dictionary](class_dictionary.md#class-dictionary) **generate_script_api**(path: [String](class_string.md#class-string)) [🔗](class_gdscriptworkspace.md#class-gdscriptworkspace-method-generate-script-api)

Returns the interface of the script in a machine-readable format.

---


<a id="class-gdscriptworkspace-method-get-file-path"></a>

[String](class_string.md#class-string) **get_file_path**(uri: [String](class_string.md#class-string)) [🔗](class_gdscriptworkspace.md#class-gdscriptworkspace-method-get-file-path)

Converts a URI to a file path.

---


<a id="class-gdscriptworkspace-method-get-file-uri"></a>

[String](class_string.md#class-string) **get_file_uri**(path: [String](class_string.md#class-string)) const [🔗](class_gdscriptworkspace.md#class-gdscriptworkspace-method-get-file-uri)

Converts a file path to a URI.

---


<a id="class-gdscriptworkspace-method-parse-local-script"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **parse_local_script**(path: [String](class_string.md#class-string)) [🔗](class_gdscriptworkspace.md#class-gdscriptworkspace-method-parse-local-script)

**Deprecated:** Might result in unwanted side effects for connected clients.

---


<a id="class-gdscriptworkspace-method-parse-script"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **parse_script**(path: [String](class_string.md#class-string), content: [String](class_string.md#class-string)) [🔗](class_gdscriptworkspace.md#class-gdscriptworkspace-method-parse-script)

**Deprecated:** Might result in unwanted side effects for connected clients.

---


<a id="class-gdscriptworkspace-method-publish-diagnostics"></a>

void **publish_diagnostics**(path: [String](class_string.md#class-string)) [🔗](class_gdscriptworkspace.md#class-gdscriptworkspace-method-publish-diagnostics)

**Deprecated:** Might result in unwanted side effects for connected clients.
