> Source: https://docs.godotengine.org/en/4.7/classes/class_flowcontainer.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="flowcontainer"></a>

<a id="class-flowcontainer"></a>

# FlowContainer

**Inherits:** [Container](class_container.md#class-container) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [HFlowContainer](class_hflowcontainer.md#class-hflowcontainer), [VFlowContainer](class_vflowcontainer.md#class-vflowcontainer)

A container that arranges its child controls horizontally or vertically and wraps them around at the borders.

<a id="description"></a>

## Description

A container that arranges its child controls horizontally or vertically and wraps them around at the borders. This is similar to how text in a book wraps around when no more words can fit on a line.

<a id="tutorials"></a>

## Tutorials

- [Using Containers](../tutorials/ui/gui_containers.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [AlignmentMode](class_flowcontainer.md#enum-flowcontainer-alignmentmode) | [alignment](class_flowcontainer.md#class-flowcontainer-property-alignment) | `0` |
| [LastWrapAlignmentMode](class_flowcontainer.md#enum-flowcontainer-lastwrapalignmentmode) | [last_wrap_alignment](class_flowcontainer.md#class-flowcontainer-property-last-wrap-alignment) | `0` |
| [bool](class_bool.md#class-bool) | [reverse_fill](class_flowcontainer.md#class-flowcontainer-property-reverse-fill) | `false` |
| [bool](class_bool.md#class-bool) | [vertical](class_flowcontainer.md#class-flowcontainer-property-vertical) | `false` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [int](class_int.md#class-int) | [get_line_count](class_flowcontainer.md#class-flowcontainer-method-get-line-count)() const |

<a id="theme-properties"></a>

## Theme Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [h_separation](class_flowcontainer.md#class-flowcontainer-theme-constant-h-separation) | `4` |
| [int](class_int.md#class-int) | [v_separation](class_flowcontainer.md#class-flowcontainer-theme-constant-v-separation) | `4` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-flowcontainer-alignmentmode"></a>

enum **AlignmentMode**: [🔗](class_flowcontainer.md#enum-flowcontainer-alignmentmode)

<a id="class-flowcontainer-constant-alignment-begin"></a>

[AlignmentMode](class_flowcontainer.md#enum-flowcontainer-alignmentmode) **ALIGNMENT_BEGIN** = `0`

The child controls will be arranged at the beginning of the container, i.e. top if orientation is vertical, left if orientation is horizontal (right for RTL layout).

<a id="class-flowcontainer-constant-alignment-center"></a>

[AlignmentMode](class_flowcontainer.md#enum-flowcontainer-alignmentmode) **ALIGNMENT_CENTER** = `1`

The child controls will be centered in the container.

<a id="class-flowcontainer-constant-alignment-end"></a>

[AlignmentMode](class_flowcontainer.md#enum-flowcontainer-alignmentmode) **ALIGNMENT_END** = `2`

The child controls will be arranged at the end of the container, i.e. bottom if orientation is vertical, right if orientation is horizontal (left for RTL layout).

---


<a id="enum-flowcontainer-lastwrapalignmentmode"></a>

enum **LastWrapAlignmentMode**: [🔗](class_flowcontainer.md#enum-flowcontainer-lastwrapalignmentmode)

<a id="class-flowcontainer-constant-last-wrap-alignment-inherit"></a>

[LastWrapAlignmentMode](class_flowcontainer.md#enum-flowcontainer-lastwrapalignmentmode) **LAST_WRAP_ALIGNMENT_INHERIT** = `0`

The last partially filled row or column will wrap aligned to the previous row or column in accordance with [alignment](class_flowcontainer.md#class-flowcontainer-property-alignment).

<a id="class-flowcontainer-constant-last-wrap-alignment-begin"></a>

[LastWrapAlignmentMode](class_flowcontainer.md#enum-flowcontainer-lastwrapalignmentmode) **LAST_WRAP_ALIGNMENT_BEGIN** = `1`

The last partially filled row or column will wrap aligned to the beginning of the previous row or column.

<a id="class-flowcontainer-constant-last-wrap-alignment-center"></a>

[LastWrapAlignmentMode](class_flowcontainer.md#enum-flowcontainer-lastwrapalignmentmode) **LAST_WRAP_ALIGNMENT_CENTER** = `2`

The last partially filled row or column will wrap aligned to the center of the previous row or column.

<a id="class-flowcontainer-constant-last-wrap-alignment-end"></a>

[LastWrapAlignmentMode](class_flowcontainer.md#enum-flowcontainer-lastwrapalignmentmode) **LAST_WRAP_ALIGNMENT_END** = `3`

The last partially filled row or column will wrap aligned to the end of the previous row or column.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-flowcontainer-property-alignment"></a>

[AlignmentMode](class_flowcontainer.md#enum-flowcontainer-alignmentmode) **alignment** = `0` [🔗](class_flowcontainer.md#class-flowcontainer-property-alignment)

- void **set_alignment**(value: [AlignmentMode](class_flowcontainer.md#enum-flowcontainer-alignmentmode))
- [AlignmentMode](class_flowcontainer.md#enum-flowcontainer-alignmentmode) **get_alignment**()

The alignment of the container's children (must be one of [ALIGNMENT_BEGIN](class_flowcontainer.md#class-flowcontainer-constant-alignment-begin), [ALIGNMENT_CENTER](class_flowcontainer.md#class-flowcontainer-constant-alignment-center), or [ALIGNMENT_END](class_flowcontainer.md#class-flowcontainer-constant-alignment-end)).

---


<a id="class-flowcontainer-property-last-wrap-alignment"></a>

[LastWrapAlignmentMode](class_flowcontainer.md#enum-flowcontainer-lastwrapalignmentmode) **last_wrap_alignment** = `0` [🔗](class_flowcontainer.md#class-flowcontainer-property-last-wrap-alignment)

- void **set_last_wrap_alignment**(value: [LastWrapAlignmentMode](class_flowcontainer.md#enum-flowcontainer-lastwrapalignmentmode))
- [LastWrapAlignmentMode](class_flowcontainer.md#enum-flowcontainer-lastwrapalignmentmode) **get_last_wrap_alignment**()

The wrap behavior of the last, partially filled row or column (must be one of [LAST_WRAP_ALIGNMENT_INHERIT](class_flowcontainer.md#class-flowcontainer-constant-last-wrap-alignment-inherit), [LAST_WRAP_ALIGNMENT_BEGIN](class_flowcontainer.md#class-flowcontainer-constant-last-wrap-alignment-begin), [LAST_WRAP_ALIGNMENT_CENTER](class_flowcontainer.md#class-flowcontainer-constant-last-wrap-alignment-center), or [LAST_WRAP_ALIGNMENT_END](class_flowcontainer.md#class-flowcontainer-constant-last-wrap-alignment-end)).

---


<a id="class-flowcontainer-property-reverse-fill"></a>

[bool](class_bool.md#class-bool) **reverse_fill** = `false` [🔗](class_flowcontainer.md#class-flowcontainer-property-reverse-fill)

- void **set_reverse_fill**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_reverse_fill**()

If `true`, reverses fill direction. Horizontal **FlowContainer**s will fill rows bottom to top, vertical **FlowContainer**s will fill columns right to left.

When using a vertical **FlowContainer** with a right to left [Control.layout_direction](class_control.md#class-control-property-layout-direction), columns will fill left to right instead.

---


<a id="class-flowcontainer-property-vertical"></a>

[bool](class_bool.md#class-bool) **vertical** = `false` [🔗](class_flowcontainer.md#class-flowcontainer-property-vertical)

- void **set_vertical**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_vertical**()

If `true`, the **FlowContainer** will arrange its children vertically, rather than horizontally.

Can't be changed when using [HFlowContainer](class_hflowcontainer.md#class-hflowcontainer) and [VFlowContainer](class_vflowcontainer.md#class-vflowcontainer).

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-flowcontainer-method-get-line-count"></a>

[int](class_int.md#class-int) **get_line_count**() const [🔗](class_flowcontainer.md#class-flowcontainer-method-get-line-count)

Returns the current line count.

---


<a id="theme-property-descriptions"></a>

## Theme Property Descriptions

<a id="class-flowcontainer-theme-constant-h-separation"></a>

[int](class_int.md#class-int) **h_separation** = `4` [🔗](class_flowcontainer.md#class-flowcontainer-theme-constant-h-separation)

The horizontal separation of child nodes.

---


<a id="class-flowcontainer-theme-constant-v-separation"></a>

[int](class_int.md#class-int) **v_separation** = `4` [🔗](class_flowcontainer.md#class-flowcontainer-theme-constant-v-separation)

The vertical separation of child nodes.
