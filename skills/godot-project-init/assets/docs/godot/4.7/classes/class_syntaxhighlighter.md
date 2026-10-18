> Source: https://docs.godotengine.org/en/4.7/classes/class_syntaxhighlighter.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="syntaxhighlighter"></a>

<a id="class-syntaxhighlighter"></a>

# SyntaxHighlighter

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [CodeHighlighter](class_codehighlighter.md#class-codehighlighter), [EditorSyntaxHighlighter](class_editorsyntaxhighlighter.md#class-editorsyntaxhighlighter)

Base class for syntax highlighters. Provides syntax highlighting data to a [TextEdit](class_textedit.md#class-textedit).

<a id="description"></a>

## Description

Base class for syntax highlighters. Provides syntax highlighting data to a [TextEdit](class_textedit.md#class-textedit). The associated [TextEdit](class_textedit.md#class-textedit) will call into the **SyntaxHighlighter** on an as-needed basis.

**Note:** A **SyntaxHighlighter** instance should not be used across multiple [TextEdit](class_textedit.md#class-textedit) nodes.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [_clear_highlighting_cache](class_syntaxhighlighter.md#class-syntaxhighlighter-private-method-clear-highlighting-cache)() virtual |
| [Dictionary](class_dictionary.md#class-dictionary) | [_get_line_syntax_highlighting](class_syntaxhighlighter.md#class-syntaxhighlighter-private-method-get-line-syntax-highlighting)(line: [int](class_int.md#class-int)) virtual const |
| void | [_update_cache](class_syntaxhighlighter.md#class-syntaxhighlighter-private-method-update-cache)() virtual |
| void | [clear_highlighting_cache](class_syntaxhighlighter.md#class-syntaxhighlighter-method-clear-highlighting-cache)() |
| [Dictionary](class_dictionary.md#class-dictionary) | [get_line_syntax_highlighting](class_syntaxhighlighter.md#class-syntaxhighlighter-method-get-line-syntax-highlighting)(line: [int](class_int.md#class-int)) |
| [TextEdit](class_textedit.md#class-textedit) | [get_text_edit](class_syntaxhighlighter.md#class-syntaxhighlighter-method-get-text-edit)() const |
| void | [update_cache](class_syntaxhighlighter.md#class-syntaxhighlighter-method-update-cache)() |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-syntaxhighlighter-private-method-clear-highlighting-cache"></a>

void **_clear_highlighting_cache**() virtual [🔗](class_syntaxhighlighter.md#class-syntaxhighlighter-private-method-clear-highlighting-cache)

Virtual method which can be overridden to clear any local caches.

---


<a id="class-syntaxhighlighter-private-method-get-line-syntax-highlighting"></a>

[Dictionary](class_dictionary.md#class-dictionary) **_get_line_syntax_highlighting**(line: [int](class_int.md#class-int)) virtual const [🔗](class_syntaxhighlighter.md#class-syntaxhighlighter-private-method-get-line-syntax-highlighting)

Virtual method which can be overridden to return syntax highlighting data.

See [get_line_syntax_highlighting()](class_syntaxhighlighter.md#class-syntaxhighlighter-method-get-line-syntax-highlighting) for more details.

---


<a id="class-syntaxhighlighter-private-method-update-cache"></a>

void **_update_cache**() virtual [🔗](class_syntaxhighlighter.md#class-syntaxhighlighter-private-method-update-cache)

Virtual method which can be overridden to update any local caches.

---


<a id="class-syntaxhighlighter-method-clear-highlighting-cache"></a>

void **clear_highlighting_cache**() [🔗](class_syntaxhighlighter.md#class-syntaxhighlighter-method-clear-highlighting-cache)

Clears all cached syntax highlighting data.

Then calls overridable method [_clear_highlighting_cache()](class_syntaxhighlighter.md#class-syntaxhighlighter-private-method-clear-highlighting-cache).

---


<a id="class-syntaxhighlighter-method-get-line-syntax-highlighting"></a>

[Dictionary](class_dictionary.md#class-dictionary) **get_line_syntax_highlighting**(line: [int](class_int.md#class-int)) [🔗](class_syntaxhighlighter.md#class-syntaxhighlighter-method-get-line-syntax-highlighting)

Returns the syntax highlighting data for the line at index `line`. If the line is not cached, calls [_get_line_syntax_highlighting()](class_syntaxhighlighter.md#class-syntaxhighlighter-private-method-get-line-syntax-highlighting) first to calculate the data.

Each entry is a column number containing a nested [Dictionary](class_dictionary.md#class-dictionary). The column number denotes the start of a region, the region will end if another region is found, or at the end of the line. The nested [Dictionary](class_dictionary.md#class-dictionary) contains the data for that region. Currently only the key `"color"` is supported.

**Example:** Possible return value. This means columns `0` to `4` should be red, and columns `5` to the end of the line should be green:

```gdscript
{
    0: {
        "color": Color(1, 0, 0)
    },
    5: {
        "color": Color(0, 1, 0)
    }
}
```

---


<a id="class-syntaxhighlighter-method-get-text-edit"></a>

[TextEdit](class_textedit.md#class-textedit) **get_text_edit**() const [🔗](class_syntaxhighlighter.md#class-syntaxhighlighter-method-get-text-edit)

Returns the associated [TextEdit](class_textedit.md#class-textedit) node.

---


<a id="class-syntaxhighlighter-method-update-cache"></a>

void **update_cache**() [🔗](class_syntaxhighlighter.md#class-syntaxhighlighter-method-update-cache)

Clears then updates the **SyntaxHighlighter** caches. Override [_update_cache()](class_syntaxhighlighter.md#class-syntaxhighlighter-private-method-update-cache) for a callback.

**Note:** This is called automatically when the associated [TextEdit](class_textedit.md#class-textedit) node, updates its own cache.
