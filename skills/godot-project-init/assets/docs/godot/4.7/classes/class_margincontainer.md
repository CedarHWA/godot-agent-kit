> Source: https://docs.godotengine.org/en/4.7/classes/class_margincontainer.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="margincontainer"></a>

<a id="class-margincontainer"></a>

# MarginContainer

**Inherits:** [Container](class_container.md#class-container) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [EditorDock](class_editordock.md#class-editordock)

A container that keeps a margin around its child controls.

<a id="description"></a>

## Description

**MarginContainer** adds an adjustable margin on each side of its child controls. The margins are added around all children, not around each individual one. To control the **MarginContainer**'s margins, use the `margin_*` theme properties listed below.

**Note:** The margin sizes are theme overrides, not normal properties. This is an example of how to change them in code:

```gdscript
# This code sample assumes the current script is extending MarginContainer.
var margin_value = 100
add_theme_constant_override("margin_top", margin_value)
add_theme_constant_override("margin_left", margin_value)
add_theme_constant_override("margin_bottom", margin_value)
add_theme_constant_override("margin_right", margin_value)
```

```csharp
// This code sample assumes the current script is extending MarginContainer.
int marginValue = 100;
AddThemeConstantOverride("margin_top", marginValue);
AddThemeConstantOverride("margin_left", marginValue);
AddThemeConstantOverride("margin_bottom", marginValue);
AddThemeConstantOverride("margin_right", marginValue);
```

<a id="tutorials"></a>

## Tutorials

- [Using Containers](../tutorials/ui/gui_containers.md)

<a id="theme-properties"></a>

## Theme Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [margin_bottom](class_margincontainer.md#class-margincontainer-theme-constant-margin-bottom) | `0` |
| [int](class_int.md#class-int) | [margin_left](class_margincontainer.md#class-margincontainer-theme-constant-margin-left) | `0` |
| [int](class_int.md#class-int) | [margin_right](class_margincontainer.md#class-margincontainer-theme-constant-margin-right) | `0` |
| [int](class_int.md#class-int) | [margin_top](class_margincontainer.md#class-margincontainer-theme-constant-margin-top) | `0` |

---


<a id="theme-property-descriptions"></a>

## Theme Property Descriptions

<a id="class-margincontainer-theme-constant-margin-bottom"></a>

[int](class_int.md#class-int) **margin_bottom** = `0` [🔗](class_margincontainer.md#class-margincontainer-theme-constant-margin-bottom)

Offsets towards the inside direct children of the container by this amount of pixels from the bottom.

---


<a id="class-margincontainer-theme-constant-margin-left"></a>

[int](class_int.md#class-int) **margin_left** = `0` [🔗](class_margincontainer.md#class-margincontainer-theme-constant-margin-left)

Offsets towards the inside direct children of the container by this amount of pixels from the left.

---


<a id="class-margincontainer-theme-constant-margin-right"></a>

[int](class_int.md#class-int) **margin_right** = `0` [🔗](class_margincontainer.md#class-margincontainer-theme-constant-margin-right)

Offsets towards the inside direct children of the container by this amount of pixels from the right.

---


<a id="class-margincontainer-theme-constant-margin-top"></a>

[int](class_int.md#class-int) **margin_top** = `0` [🔗](class_margincontainer.md#class-margincontainer-theme-constant-margin-top)

Offsets towards the inside direct children of the container by this amount of pixels from the top.
