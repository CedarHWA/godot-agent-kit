> Source: https://docs.godotengine.org/en/4.7/classes/class_boxcontainer.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="boxcontainer"></a>

<a id="class-boxcontainer"></a>

# BoxContainer

**Inherits:** [Container](class_container.md#class-container) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [HBoxContainer](class_hboxcontainer.md#class-hboxcontainer), [VBoxContainer](class_vboxcontainer.md#class-vboxcontainer)

A container that arranges its child controls horizontally or vertically.

<a id="description"></a>

## Description

A container that arranges its child controls horizontally or vertically, rearranging them automatically when their minimum size changes.

<a id="tutorials"></a>

## Tutorials

- [Using Containers](../tutorials/ui/gui_containers.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [AlignmentMode](class_boxcontainer.md#enum-boxcontainer-alignmentmode) | [alignment](class_boxcontainer.md#class-boxcontainer-property-alignment) | `0` |
| [bool](class_bool.md#class-bool) | [vertical](class_boxcontainer.md#class-boxcontainer-property-vertical) | `false` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Control](class_control.md#class-control) | [add_spacer](class_boxcontainer.md#class-boxcontainer-method-add-spacer)(begin: [bool](class_bool.md#class-bool)) |

<a id="theme-properties"></a>

## Theme Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [separation](class_boxcontainer.md#class-boxcontainer-theme-constant-separation) | `4` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-boxcontainer-alignmentmode"></a>

enum **AlignmentMode**: [🔗](class_boxcontainer.md#enum-boxcontainer-alignmentmode)

<a id="class-boxcontainer-constant-alignment-begin"></a>

[AlignmentMode](class_boxcontainer.md#enum-boxcontainer-alignmentmode) **ALIGNMENT_BEGIN** = `0`

The child controls will be arranged at the beginning of the container, i.e. top if orientation is vertical, left if orientation is horizontal (right for RTL layout).

<a id="class-boxcontainer-constant-alignment-center"></a>

[AlignmentMode](class_boxcontainer.md#enum-boxcontainer-alignmentmode) **ALIGNMENT_CENTER** = `1`

The child controls will be centered in the container.

<a id="class-boxcontainer-constant-alignment-end"></a>

[AlignmentMode](class_boxcontainer.md#enum-boxcontainer-alignmentmode) **ALIGNMENT_END** = `2`

The child controls will be arranged at the end of the container, i.e. bottom if orientation is vertical, right if orientation is horizontal (left for RTL layout).

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-boxcontainer-property-alignment"></a>

[AlignmentMode](class_boxcontainer.md#enum-boxcontainer-alignmentmode) **alignment** = `0` [🔗](class_boxcontainer.md#class-boxcontainer-property-alignment)

- void **set_alignment**(value: [AlignmentMode](class_boxcontainer.md#enum-boxcontainer-alignmentmode))
- [AlignmentMode](class_boxcontainer.md#enum-boxcontainer-alignmentmode) **get_alignment**()

The alignment of the container's children (must be one of [ALIGNMENT_BEGIN](class_boxcontainer.md#class-boxcontainer-constant-alignment-begin), [ALIGNMENT_CENTER](class_boxcontainer.md#class-boxcontainer-constant-alignment-center), or [ALIGNMENT_END](class_boxcontainer.md#class-boxcontainer-constant-alignment-end)).

---


<a id="class-boxcontainer-property-vertical"></a>

[bool](class_bool.md#class-bool) **vertical** = `false` [🔗](class_boxcontainer.md#class-boxcontainer-property-vertical)

- void **set_vertical**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_vertical**()

If `true`, the **BoxContainer** will arrange its children vertically, rather than horizontally.

Can't be changed when using [HBoxContainer](class_hboxcontainer.md#class-hboxcontainer) and [VBoxContainer](class_vboxcontainer.md#class-vboxcontainer).

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-boxcontainer-method-add-spacer"></a>

[Control](class_control.md#class-control) **add_spacer**(begin: [bool](class_bool.md#class-bool)) [🔗](class_boxcontainer.md#class-boxcontainer-method-add-spacer)

Adds a [Control](class_control.md#class-control) node to the box as a spacer. If `begin` is `true`, it will insert the [Control](class_control.md#class-control) node in front of all other children.

---


<a id="theme-property-descriptions"></a>

## Theme Property Descriptions

<a id="class-boxcontainer-theme-constant-separation"></a>

[int](class_int.md#class-int) **separation** = `4` [🔗](class_boxcontainer.md#class-boxcontainer-theme-constant-separation)

The space between the **BoxContainer**'s elements, in pixels.
