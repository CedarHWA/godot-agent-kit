> Source: https://docs.godotengine.org/en/4.7/classes/class_aspectratiocontainer.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="aspectratiocontainer"></a>

<a id="class-aspectratiocontainer"></a>

# AspectRatioContainer

**Inherits:** [Container](class_container.md#class-container) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A container that preserves the proportions of its child controls.

<a id="description"></a>

## Description

A container type that arranges its child controls in a way that preserves their proportions automatically when the container is resized. Useful when a container has a dynamic size and the child nodes must adjust their sizes accordingly without losing their aspect ratios.

<a id="tutorials"></a>

## Tutorials

- [Using Containers](../tutorials/ui/gui_containers.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [AlignmentMode](class_aspectratiocontainer.md#enum-aspectratiocontainer-alignmentmode) | [alignment_horizontal](class_aspectratiocontainer.md#class-aspectratiocontainer-property-alignment-horizontal) | `1` |
| [AlignmentMode](class_aspectratiocontainer.md#enum-aspectratiocontainer-alignmentmode) | [alignment_vertical](class_aspectratiocontainer.md#class-aspectratiocontainer-property-alignment-vertical) | `1` |
| [float](class_float.md#class-float) | [ratio](class_aspectratiocontainer.md#class-aspectratiocontainer-property-ratio) | `1.0` |
| [StretchMode](class_aspectratiocontainer.md#enum-aspectratiocontainer-stretchmode) | [stretch_mode](class_aspectratiocontainer.md#class-aspectratiocontainer-property-stretch-mode) | `2` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-aspectratiocontainer-stretchmode"></a>

enum **StretchMode**: [🔗](class_aspectratiocontainer.md#enum-aspectratiocontainer-stretchmode)

<a id="class-aspectratiocontainer-constant-stretch-width-controls-height"></a>

[StretchMode](class_aspectratiocontainer.md#enum-aspectratiocontainer-stretchmode) **STRETCH_WIDTH_CONTROLS_HEIGHT** = `0`

The height of child controls is automatically adjusted based on the width of the container.

<a id="class-aspectratiocontainer-constant-stretch-height-controls-width"></a>

[StretchMode](class_aspectratiocontainer.md#enum-aspectratiocontainer-stretchmode) **STRETCH_HEIGHT_CONTROLS_WIDTH** = `1`

The width of child controls is automatically adjusted based on the height of the container.

<a id="class-aspectratiocontainer-constant-stretch-fit"></a>

[StretchMode](class_aspectratiocontainer.md#enum-aspectratiocontainer-stretchmode) **STRETCH_FIT** = `2`

The bounding rectangle of child controls is automatically adjusted to fit inside the container while keeping the aspect ratio.

<a id="class-aspectratiocontainer-constant-stretch-cover"></a>

[StretchMode](class_aspectratiocontainer.md#enum-aspectratiocontainer-stretchmode) **STRETCH_COVER** = `3`

The width and height of child controls is automatically adjusted to make their bounding rectangle cover the entire area of the container while keeping the aspect ratio.

When the bounding rectangle of child controls exceed the container's size and [Control.clip_contents](class_control.md#class-control-property-clip-contents) is enabled, this allows to show only the container's area restricted by its own bounding rectangle.

---


<a id="enum-aspectratiocontainer-alignmentmode"></a>

enum **AlignmentMode**: [🔗](class_aspectratiocontainer.md#enum-aspectratiocontainer-alignmentmode)

<a id="class-aspectratiocontainer-constant-alignment-begin"></a>

[AlignmentMode](class_aspectratiocontainer.md#enum-aspectratiocontainer-alignmentmode) **ALIGNMENT_BEGIN** = `0`

Aligns child controls with the beginning (left or top) of the container.

<a id="class-aspectratiocontainer-constant-alignment-center"></a>

[AlignmentMode](class_aspectratiocontainer.md#enum-aspectratiocontainer-alignmentmode) **ALIGNMENT_CENTER** = `1`

Aligns child controls with the center of the container.

<a id="class-aspectratiocontainer-constant-alignment-end"></a>

[AlignmentMode](class_aspectratiocontainer.md#enum-aspectratiocontainer-alignmentmode) **ALIGNMENT_END** = `2`

Aligns child controls with the end (right or bottom) of the container.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-aspectratiocontainer-property-alignment-horizontal"></a>

[AlignmentMode](class_aspectratiocontainer.md#enum-aspectratiocontainer-alignmentmode) **alignment_horizontal** = `1` [🔗](class_aspectratiocontainer.md#class-aspectratiocontainer-property-alignment-horizontal)

- void **set_alignment_horizontal**(value: [AlignmentMode](class_aspectratiocontainer.md#enum-aspectratiocontainer-alignmentmode))
- [AlignmentMode](class_aspectratiocontainer.md#enum-aspectratiocontainer-alignmentmode) **get_alignment_horizontal**()

Specifies the horizontal relative position of child controls.

---


<a id="class-aspectratiocontainer-property-alignment-vertical"></a>

[AlignmentMode](class_aspectratiocontainer.md#enum-aspectratiocontainer-alignmentmode) **alignment_vertical** = `1` [🔗](class_aspectratiocontainer.md#class-aspectratiocontainer-property-alignment-vertical)

- void **set_alignment_vertical**(value: [AlignmentMode](class_aspectratiocontainer.md#enum-aspectratiocontainer-alignmentmode))
- [AlignmentMode](class_aspectratiocontainer.md#enum-aspectratiocontainer-alignmentmode) **get_alignment_vertical**()

Specifies the vertical relative position of child controls.

---


<a id="class-aspectratiocontainer-property-ratio"></a>

[float](class_float.md#class-float) **ratio** = `1.0` [🔗](class_aspectratiocontainer.md#class-aspectratiocontainer-property-ratio)

- void **set_ratio**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_ratio**()

The aspect ratio to enforce on child controls. This is the width divided by the height. The ratio depends on the [stretch_mode](class_aspectratiocontainer.md#class-aspectratiocontainer-property-stretch-mode).

---


<a id="class-aspectratiocontainer-property-stretch-mode"></a>

[StretchMode](class_aspectratiocontainer.md#enum-aspectratiocontainer-stretchmode) **stretch_mode** = `2` [🔗](class_aspectratiocontainer.md#class-aspectratiocontainer-property-stretch-mode)

- void **set_stretch_mode**(value: [StretchMode](class_aspectratiocontainer.md#enum-aspectratiocontainer-stretchmode))
- [StretchMode](class_aspectratiocontainer.md#enum-aspectratiocontainer-stretchmode) **get_stretch_mode**()

The stretch mode used to align child controls.
