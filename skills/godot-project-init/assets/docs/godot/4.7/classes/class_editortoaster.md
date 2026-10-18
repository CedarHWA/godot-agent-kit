> Source: https://docs.godotengine.org/en/4.7/classes/class_editortoaster.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="editortoaster"></a>

<a id="class-editortoaster"></a>

# EditorToaster

**Inherits:** [HBoxContainer](class_hboxcontainer.md#class-hboxcontainer) **<** [BoxContainer](class_boxcontainer.md#class-boxcontainer) **<** [Container](class_container.md#class-container) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Manages toast notifications within the editor.

<a id="description"></a>

## Description

This object manages the functionality and display of toast notifications within the editor, ensuring immediate and informative alerts are presented to the user.

**Note:** This class shouldn't be instantiated directly. Instead, access the singleton using [EditorInterface.get_editor_toaster()](class_editorinterface.md#class-editorinterface-method-get-editor-toaster).

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [push_toast](class_editortoaster.md#class-editortoaster-method-push-toast)(message: [String](class_string.md#class-string), severity: [Severity](class_editortoaster.md#enum-editortoaster-severity) = 0, tooltip: [String](class_string.md#class-string) = "") |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-editortoaster-severity"></a>

enum **Severity**: [🔗](class_editortoaster.md#enum-editortoaster-severity)

<a id="class-editortoaster-constant-severity-info"></a>

[Severity](class_editortoaster.md#enum-editortoaster-severity) **SEVERITY_INFO** = `0`

Toast will display with an INFO severity.

<a id="class-editortoaster-constant-severity-warning"></a>

[Severity](class_editortoaster.md#enum-editortoaster-severity) **SEVERITY_WARNING** = `1`

Toast will display with a WARNING severity and have a corresponding color.

<a id="class-editortoaster-constant-severity-error"></a>

[Severity](class_editortoaster.md#enum-editortoaster-severity) **SEVERITY_ERROR** = `2`

Toast will display with an ERROR severity and have a corresponding color.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-editortoaster-method-push-toast"></a>

void **push_toast**(message: [String](class_string.md#class-string), severity: [Severity](class_editortoaster.md#enum-editortoaster-severity) = 0, tooltip: [String](class_string.md#class-string) = "") [🔗](class_editortoaster.md#class-editortoaster-method-push-toast)

Pushes a toast notification to the editor for display.
