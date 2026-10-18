> Source: https://docs.godotengine.org/en/4.7/classes/class_gdscripttextdocument.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="gdscripttextdocument"></a>

<a id="class-gdscripttextdocument"></a>

# GDScriptTextDocument

**Deprecated:** This class may be changed or removed in future versions.

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Document related language server functionality.

<a id="description"></a>

## Description

Provides language server functionality related to documents.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Array](class_array.md#class-array) | [codeLens](class_gdscripttextdocument.md#class-gdscripttextdocument-method-codelens)(params: [Dictionary](class_dictionary.md#class-dictionary)) |
| [Array](class_array.md#class-array) | [colorPresentation](class_gdscripttextdocument.md#class-gdscripttextdocument-method-colorpresentation)(params: [Dictionary](class_dictionary.md#class-dictionary)) |
| [Array](class_array.md#class-array) | [completion](class_gdscripttextdocument.md#class-gdscripttextdocument-method-completion)(params: [Dictionary](class_dictionary.md#class-dictionary)) |
| [Variant](class_variant.md#class-variant) | [declaration](class_gdscripttextdocument.md#class-gdscripttextdocument-method-declaration)(params: [Dictionary](class_dictionary.md#class-dictionary)) |
| [Array](class_array.md#class-array) | [definition](class_gdscripttextdocument.md#class-gdscripttextdocument-method-definition)(params: [Dictionary](class_dictionary.md#class-dictionary)) |
| void | [didChange](class_gdscripttextdocument.md#class-gdscripttextdocument-method-didchange)(params: [Variant](class_variant.md#class-variant)) |
| void | [didClose](class_gdscripttextdocument.md#class-gdscripttextdocument-method-didclose)(params: [Variant](class_variant.md#class-variant)) |
| void | [didOpen](class_gdscripttextdocument.md#class-gdscripttextdocument-method-didopen)(params: [Variant](class_variant.md#class-variant)) |
| void | [didSave](class_gdscripttextdocument.md#class-gdscripttextdocument-method-didsave)(params: [Variant](class_variant.md#class-variant)) |
| [Array](class_array.md#class-array) | [documentLink](class_gdscripttextdocument.md#class-gdscripttextdocument-method-documentlink)(params: [Dictionary](class_dictionary.md#class-dictionary)) |
| [Array](class_array.md#class-array) | [documentSymbol](class_gdscripttextdocument.md#class-gdscripttextdocument-method-documentsymbol)(params: [Dictionary](class_dictionary.md#class-dictionary)) |
| [Array](class_array.md#class-array) | [foldingRange](class_gdscripttextdocument.md#class-gdscripttextdocument-method-foldingrange)(params: [Dictionary](class_dictionary.md#class-dictionary)) |
| [Variant](class_variant.md#class-variant) | [hover](class_gdscripttextdocument.md#class-gdscripttextdocument-method-hover)(params: [Dictionary](class_dictionary.md#class-dictionary)) |
| [Variant](class_variant.md#class-variant) | [nativeSymbol](class_gdscripttextdocument.md#class-gdscripttextdocument-method-nativesymbol)(params: [Dictionary](class_dictionary.md#class-dictionary)) |
| [Variant](class_variant.md#class-variant) | [prepareRename](class_gdscripttextdocument.md#class-gdscripttextdocument-method-preparerename)(params: [Dictionary](class_dictionary.md#class-dictionary)) |
| [Array](class_array.md#class-array) | [references](class_gdscripttextdocument.md#class-gdscripttextdocument-method-references)(params: [Dictionary](class_dictionary.md#class-dictionary)) |
| [Dictionary](class_dictionary.md#class-dictionary) | [rename](class_gdscripttextdocument.md#class-gdscripttextdocument-method-rename)(params: [Dictionary](class_dictionary.md#class-dictionary)) |
| [Dictionary](class_dictionary.md#class-dictionary) | [resolve](class_gdscripttextdocument.md#class-gdscripttextdocument-method-resolve)(params: [Dictionary](class_dictionary.md#class-dictionary)) |
| void | [show_native_symbol_in_editor](class_gdscripttextdocument.md#class-gdscripttextdocument-method-show-native-symbol-in-editor)(symbol_id: [String](class_string.md#class-string)) |
| [Variant](class_variant.md#class-variant) | [signatureHelp](class_gdscripttextdocument.md#class-gdscripttextdocument-method-signaturehelp)(params: [Dictionary](class_dictionary.md#class-dictionary)) |
| void | [willSaveWaitUntil](class_gdscripttextdocument.md#class-gdscripttextdocument-method-willsavewaituntil)(params: [Variant](class_variant.md#class-variant)) |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-gdscripttextdocument-method-codelens"></a>

[Array](class_array.md#class-array) **codeLens**(params: [Dictionary](class_dictionary.md#class-dictionary)) [🔗](class_gdscripttextdocument.md#class-gdscripttextdocument-method-codelens)

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---


<a id="class-gdscripttextdocument-method-colorpresentation"></a>

[Array](class_array.md#class-array) **colorPresentation**(params: [Dictionary](class_dictionary.md#class-dictionary)) [🔗](class_gdscripttextdocument.md#class-gdscripttextdocument-method-colorpresentation)

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---


<a id="class-gdscripttextdocument-method-completion"></a>

[Array](class_array.md#class-array) **completion**(params: [Dictionary](class_dictionary.md#class-dictionary)) [🔗](class_gdscripttextdocument.md#class-gdscripttextdocument-method-completion)

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---


<a id="class-gdscripttextdocument-method-declaration"></a>

[Variant](class_variant.md#class-variant) **declaration**(params: [Dictionary](class_dictionary.md#class-dictionary)) [🔗](class_gdscripttextdocument.md#class-gdscripttextdocument-method-declaration)

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---


<a id="class-gdscripttextdocument-method-definition"></a>

[Array](class_array.md#class-array) **definition**(params: [Dictionary](class_dictionary.md#class-dictionary)) [🔗](class_gdscripttextdocument.md#class-gdscripttextdocument-method-definition)

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---


<a id="class-gdscripttextdocument-method-didchange"></a>

void **didChange**(params: [Variant](class_variant.md#class-variant)) [🔗](class_gdscripttextdocument.md#class-gdscripttextdocument-method-didchange)

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---


<a id="class-gdscripttextdocument-method-didclose"></a>

void **didClose**(params: [Variant](class_variant.md#class-variant)) [🔗](class_gdscripttextdocument.md#class-gdscripttextdocument-method-didclose)

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---


<a id="class-gdscripttextdocument-method-didopen"></a>

void **didOpen**(params: [Variant](class_variant.md#class-variant)) [🔗](class_gdscripttextdocument.md#class-gdscripttextdocument-method-didopen)

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---


<a id="class-gdscripttextdocument-method-didsave"></a>

void **didSave**(params: [Variant](class_variant.md#class-variant)) [🔗](class_gdscripttextdocument.md#class-gdscripttextdocument-method-didsave)

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---


<a id="class-gdscripttextdocument-method-documentlink"></a>

[Array](class_array.md#class-array) **documentLink**(params: [Dictionary](class_dictionary.md#class-dictionary)) [🔗](class_gdscripttextdocument.md#class-gdscripttextdocument-method-documentlink)

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---


<a id="class-gdscripttextdocument-method-documentsymbol"></a>

[Array](class_array.md#class-array) **documentSymbol**(params: [Dictionary](class_dictionary.md#class-dictionary)) [🔗](class_gdscripttextdocument.md#class-gdscripttextdocument-method-documentsymbol)

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---


<a id="class-gdscripttextdocument-method-foldingrange"></a>

[Array](class_array.md#class-array) **foldingRange**(params: [Dictionary](class_dictionary.md#class-dictionary)) [🔗](class_gdscripttextdocument.md#class-gdscripttextdocument-method-foldingrange)

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---


<a id="class-gdscripttextdocument-method-hover"></a>

[Variant](class_variant.md#class-variant) **hover**(params: [Dictionary](class_dictionary.md#class-dictionary)) [🔗](class_gdscripttextdocument.md#class-gdscripttextdocument-method-hover)

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---


<a id="class-gdscripttextdocument-method-nativesymbol"></a>

[Variant](class_variant.md#class-variant) **nativeSymbol**(params: [Dictionary](class_dictionary.md#class-dictionary)) [🔗](class_gdscripttextdocument.md#class-gdscripttextdocument-method-nativesymbol)

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---


<a id="class-gdscripttextdocument-method-preparerename"></a>

[Variant](class_variant.md#class-variant) **prepareRename**(params: [Dictionary](class_dictionary.md#class-dictionary)) [🔗](class_gdscripttextdocument.md#class-gdscripttextdocument-method-preparerename)

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---


<a id="class-gdscripttextdocument-method-references"></a>

[Array](class_array.md#class-array) **references**(params: [Dictionary](class_dictionary.md#class-dictionary)) [🔗](class_gdscripttextdocument.md#class-gdscripttextdocument-method-references)

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---


<a id="class-gdscripttextdocument-method-rename"></a>

[Dictionary](class_dictionary.md#class-dictionary) **rename**(params: [Dictionary](class_dictionary.md#class-dictionary)) [🔗](class_gdscripttextdocument.md#class-gdscripttextdocument-method-rename)

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---


<a id="class-gdscripttextdocument-method-resolve"></a>

[Dictionary](class_dictionary.md#class-dictionary) **resolve**(params: [Dictionary](class_dictionary.md#class-dictionary)) [🔗](class_gdscripttextdocument.md#class-gdscripttextdocument-method-resolve)

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---


<a id="class-gdscripttextdocument-method-show-native-symbol-in-editor"></a>

void **show_native_symbol_in_editor**(symbol_id: [String](class_string.md#class-string)) [🔗](class_gdscripttextdocument.md#class-gdscripttextdocument-method-show-native-symbol-in-editor)

**Deprecated:** Use [ScriptEditor.goto_help()](class_scripteditor.md#class-scripteditor-method-goto-help) instead.

---


<a id="class-gdscripttextdocument-method-signaturehelp"></a>

[Variant](class_variant.md#class-variant) **signatureHelp**(params: [Dictionary](class_dictionary.md#class-dictionary)) [🔗](class_gdscripttextdocument.md#class-gdscripttextdocument-method-signaturehelp)

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---


<a id="class-gdscripttextdocument-method-willsavewaituntil"></a>

void **willSaveWaitUntil**(params: [Variant](class_variant.md#class-variant)) [🔗](class_gdscripttextdocument.md#class-gdscripttextdocument-method-willsavewaituntil)

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.
