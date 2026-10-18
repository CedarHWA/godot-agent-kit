> Source: https://docs.godotengine.org/en/4.7/classes/class_separator.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="separator"></a>

<a id="class-separator"></a>

# Separator

**Inherits:** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [HSeparator](class_hseparator.md#class-hseparator), [VSeparator](class_vseparator.md#class-vseparator)

Abstract base class for separators.

<a id="description"></a>

## Description

Abstract base class for separators, used for separating other controls. **Separator**s are purely visual and normally drawn as a [StyleBoxLine](class_styleboxline.md#class-styleboxline).

<a id="theme-properties"></a>

## Theme Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [separation](class_separator.md#class-separator-theme-constant-separation) | `0` |
| [StyleBox](class_stylebox.md#class-stylebox) | [separator](class_separator.md#class-separator-theme-style-separator) |  |

---


<a id="theme-property-descriptions"></a>

## Theme Property Descriptions

<a id="class-separator-theme-constant-separation"></a>

[int](class_int.md#class-int) **separation** = `0` [🔗](class_separator.md#class-separator-theme-constant-separation)

The size of the area covered by the separator. Effectively works like a minimum width/height.

---


<a id="class-separator-theme-style-separator"></a>

[StyleBox](class_stylebox.md#class-stylebox) **separator** [🔗](class_separator.md#class-separator-theme-style-separator)

The style for the separator line. Works best with [StyleBoxLine](class_styleboxline.md#class-styleboxline) (remember to enable [StyleBoxLine.vertical](class_styleboxline.md#class-styleboxline-property-vertical) for [VSeparator](class_vseparator.md#class-vseparator)).
