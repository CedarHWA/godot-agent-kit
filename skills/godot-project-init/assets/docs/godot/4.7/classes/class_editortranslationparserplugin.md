> Source: https://docs.godotengine.org/en/4.7/classes/class_editortranslationparserplugin.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="editortranslationparserplugin"></a>

<a id="class-editortranslationparserplugin"></a>

# EditorTranslationParserPlugin

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Plugin for adding custom parsers to extract strings that are to be translated from custom files (.csv, .json etc.).

<a id="description"></a>

## Description

**EditorTranslationParserPlugin** is invoked when a file is being parsed to extract strings that require translation. To define the parsing and string extraction logic, override the [_parse_file()](class_editortranslationparserplugin.md#class-editortranslationparserplugin-private-method-parse-file) method in script.

The return value should be an [Array](class_array.md#class-array) of [PackedStringArray](class_packedstringarray.md#class-packedstringarray)s, one for each extracted translatable string. Each entry should contain `[msgid, msgctxt, msgid_plural, comment, source_line]`, where all except `msgid` are optional. Empty strings will be ignored.

The extracted strings will be written into a translation template file selected by user under "Template Generation" in "Localization" tab in "Project Settings" menu.

Below shows an example of a custom parser that extracts strings from a CSV file to write into a template.

```gdscript
@tool
extends EditorTranslationParserPlugin

func _parse_file(path):
    var ret: Array[PackedStringArray] = []
    var file = FileAccess.open(path, FileAccess.READ)
    var text = file.get_as_text()
    var split_strs = text.split(",", false)
    for s in split_strs:
        ret.append(PackedStringArray([s]))
        #print("Extracted string: " + s)

    return ret

func _get_recognized_extensions():
    return ["csv"]
```

```csharp
using Godot;

[Tool]
public partial class CustomParser : EditorTranslationParserPlugin
{
    public override Godot.Collections.Array<string[]> _ParseFile(string path)
    {
        Godot.Collections.Array<string[]> ret;
        using var file = FileAccess.Open(path, FileAccess.ModeFlags.Read);
        string text = file.GetAsText();
        string[] splitStrs = text.Split(",", allowEmpty: false);
        foreach (string s in splitStrs)
        {
            ret.Add([s]);
            //GD.Print($"Extracted string: {s}");
        }
        return ret;
    }

    public override string[] _GetRecognizedExtensions()
    {
        return ["csv"];
    }
}
```

To add a translatable string associated with a context, plural, comment, or source line:

```gdscript
# This will add a message with msgid "Test 1", msgctxt "context", msgid_plural "test 1 plurals", comment "test 1 comment", and source line "7".
ret.append(PackedStringArray(["Test 1", "context", "test 1 plurals", "test 1 comment", "7"]))
# This will add a message with msgid "A test without context" and msgid_plural "plurals".
ret.append(PackedStringArray(["A test without context", "", "plurals"]))
# This will add a message with msgid "Only with context" and msgctxt "a friendly context".
ret.append(PackedStringArray(["Only with context", "a friendly context"]))
```

```csharp
// This will add a message with msgid "Test 1", msgctxt "context", msgid_plural "test 1 plurals", comment "test 1 comment", and source line "7".
ret.Add(["Test 1", "context", "test 1 plurals", "test 1 comment", "7"]);
// This will add a message with msgid "A test without context" and msgid_plural "plurals".
ret.Add(["A test without context", "", "plurals"]);
// This will add a message with msgid "Only with context" and msgctxt "a friendly context".
ret.Add(["Only with context", "a friendly context"]);
```

**Note:** If you override parsing logic for standard script types (GDScript, C#, etc.), it would be better to load the `path` argument using [ResourceLoader.load()](class_resourceloader.md#class-resourceloader-method-load). This is because built-in scripts are loaded as [Resource](class_resource.md#class-resource) type, not [FileAccess](class_fileaccess.md#class-fileaccess) type. For example:

```gdscript
func _parse_file(path):
    var res = ResourceLoader.load(path, "Script")
    var text = res.source_code
    # Parsing logic.

func _get_recognized_extensions():
    return ["gd"]
```

```csharp
public override Godot.Collections.Array<string[]> _ParseFile(string path)
{
    var res = ResourceLoader.Load<Script>(path, "Script");
    string text = res.SourceCode;
    // Parsing logic.
}

public override string[] _GetRecognizedExtensions()
{
    return ["gd"];
}
```

Alternatively, the plugin can directly modify the final list of strings, by implementing [_customize_strings()](class_editortranslationparserplugin.md#class-editortranslationparserplugin-private-method-customize-strings).

To use **EditorTranslationParserPlugin**, register it using the [EditorPlugin.add_translation_parser_plugin()](class_editorplugin.md#class-editorplugin-method-add-translation-parser-plugin) method first.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Array](class_array.md#class-array)[[PackedStringArray](class_packedstringarray.md#class-packedstringarray)] | [_customize_strings](class_editortranslationparserplugin.md#class-editortranslationparserplugin-private-method-customize-strings)(strings: [Array](class_array.md#class-array)[[PackedStringArray](class_packedstringarray.md#class-packedstringarray)]) virtual const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [_get_recognized_extensions](class_editortranslationparserplugin.md#class-editortranslationparserplugin-private-method-get-recognized-extensions)() virtual const |
| [Array](class_array.md#class-array)[[PackedStringArray](class_packedstringarray.md#class-packedstringarray)] | [_parse_file](class_editortranslationparserplugin.md#class-editortranslationparserplugin-private-method-parse-file)(path: [String](class_string.md#class-string)) virtual |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-editortranslationparserplugin-private-method-customize-strings"></a>

[Array](class_array.md#class-array)[[PackedStringArray](class_packedstringarray.md#class-packedstringarray)] **_customize_strings**(strings: [Array](class_array.md#class-array)[[PackedStringArray](class_packedstringarray.md#class-packedstringarray)]) virtual const [🔗](class_editortranslationparserplugin.md#class-editortranslationparserplugin-private-method-customize-strings)

Called after parsing all files. You can modify the `strings` array to add or remove entries from the final list of strings, then return it after modifications. Each entry is a [PackedStringArray](class_packedstringarray.md#class-packedstringarray) like explained in the **EditorTranslationParserPlugin**'s description.

```gdscript
@tool
extends EditorTranslationParserPlugin

func _customize_strings(strings):
    # Add new string.
    strings.append(["Test 1", "context", "test 1 plurals", "test 1 comment"])

    # Remove all strings that begin with $.
    strings = strings.filter(func(s): return not s[0].begins_with("$"))

    return strings
```

---


<a id="class-editortranslationparserplugin-private-method-get-recognized-extensions"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **_get_recognized_extensions**() virtual const [🔗](class_editortranslationparserplugin.md#class-editortranslationparserplugin-private-method-get-recognized-extensions)

Gets the list of file extensions to associate with this parser, e.g. `["csv"]`.

---


<a id="class-editortranslationparserplugin-private-method-parse-file"></a>

[Array](class_array.md#class-array)[[PackedStringArray](class_packedstringarray.md#class-packedstringarray)] **_parse_file**(path: [String](class_string.md#class-string)) virtual [🔗](class_editortranslationparserplugin.md#class-editortranslationparserplugin-private-method-parse-file)

Override this method to define a custom parsing logic to extract the translatable strings.
