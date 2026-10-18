> Source: https://docs.godotengine.org/en/4.7/classes/class_gdscriptsyntaxhighlighter.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="gdscriptsyntaxhighlighter"></a>

<a id="class-gdscriptsyntaxhighlighter"></a>

# GDScriptSyntaxHighlighter

**Inherits:** [EditorSyntaxHighlighter](class_editorsyntaxhighlighter.md#class-editorsyntaxhighlighter) **<** [SyntaxHighlighter](class_syntaxhighlighter.md#class-syntaxhighlighter) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A GDScript syntax highlighter that can be used with [TextEdit](class_textedit.md#class-textedit) and [CodeEdit](class_codeedit.md#class-codeedit) nodes.

<a id="description"></a>

## Description

**Note:** This class can only be used for editor plugins because it relies on editor settings.

```gdscript
var code_preview = TextEdit.new()
var highlighter = GDScriptSyntaxHighlighter.new()
code_preview.syntax_highlighter = highlighter
```

```csharp
var codePreview = new TextEdit();
var highlighter = new GDScriptSyntaxHighlighter();
codePreview.SyntaxHighlighter = highlighter;
```
