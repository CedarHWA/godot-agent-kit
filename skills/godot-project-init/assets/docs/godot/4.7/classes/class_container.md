> Source: https://docs.godotengine.org/en/4.7/classes/class_container.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="container"></a>

<a id="class-container"></a>

# Container

**Inherits:** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [AspectRatioContainer](class_aspectratiocontainer.md#class-aspectratiocontainer), [BoxContainer](class_boxcontainer.md#class-boxcontainer), [CenterContainer](class_centercontainer.md#class-centercontainer), [EditorProperty](class_editorproperty.md#class-editorproperty), [FlowContainer](class_flowcontainer.md#class-flowcontainer), [FoldableContainer](class_foldablecontainer.md#class-foldablecontainer), [GraphElement](class_graphelement.md#class-graphelement), [GridContainer](class_gridcontainer.md#class-gridcontainer), [MarginContainer](class_margincontainer.md#class-margincontainer), [PanelContainer](class_panelcontainer.md#class-panelcontainer), [ScrollContainer](class_scrollcontainer.md#class-scrollcontainer), [SplitContainer](class_splitcontainer.md#class-splitcontainer), [SubViewportContainer](class_subviewportcontainer.md#class-subviewportcontainer), [TabContainer](class_tabcontainer.md#class-tabcontainer)

Base class for all GUI containers.

<a id="description"></a>

## Description

Base class for all GUI containers. A **Container** automatically arranges its child controls in a certain way. This class can be inherited to make custom container types.

<a id="tutorials"></a>

## Tutorials

- [Using Containers](../tutorials/ui/gui_containers.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [accessibility_region](class_container.md#class-container-property-accessibility-region) | `false` |
| [MouseFilter](class_control.md#enum-control-mousefilter) | mouse_filter | `1` (overrides [Control](class_control.md#class-control-property-mouse-filter)) |
| [bool](class_bool.md#class-bool) | propagate_maximum_size | `true` (overrides [Control](class_control.md#class-control-property-propagate-maximum-size)) |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array) | [_get_allowed_size_flags_horizontal](class_container.md#class-container-private-method-get-allowed-size-flags-horizontal)() virtual const |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array) | [_get_allowed_size_flags_vertical](class_container.md#class-container-private-method-get-allowed-size-flags-vertical)() virtual const |
| void | [fit_child_in_rect](class_container.md#class-container-method-fit-child-in-rect)(child: [Control](class_control.md#class-control), rect: [Rect2](class_rect2.md#class-rect2)) |
| void | [queue_sort](class_container.md#class-container-method-queue-sort)() |

---


<a id="signals"></a>

## Signals

<a id="class-container-signal-pre-sort-children"></a>

**pre_sort_children**() [🔗](class_container.md#class-container-signal-pre-sort-children)

Emitted when children are going to be sorted.

---


<a id="class-container-signal-sort-children"></a>

**sort_children**() [🔗](class_container.md#class-container-signal-sort-children)

Emitted when sorting the children is needed.

---


<a id="constants"></a>

## Constants

<a id="class-container-constant-notification-pre-sort-children"></a>

**NOTIFICATION_PRE_SORT_CHILDREN** = `50` [🔗](class_container.md#class-container-constant-notification-pre-sort-children)

Notification just before children are going to be sorted, in case there's something to process beforehand.

<a id="class-container-constant-notification-sort-children"></a>

**NOTIFICATION_SORT_CHILDREN** = `51` [🔗](class_container.md#class-container-constant-notification-sort-children)

Notification for when sorting the children, it must be obeyed immediately.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-container-property-accessibility-region"></a>

[bool](class_bool.md#class-bool) **accessibility_region** = `false` [🔗](class_container.md#class-container-property-accessibility-region)

- void **set_accessibility_region**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_accessibility_region**()

If `true`, this container is marked as a region for accessibility. Use [Control.accessibility_name](class_control.md#class-control-property-accessibility-name) to give the region a descriptive name. Screen readers can navigate between regions using landmark navigation.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-container-private-method-get-allowed-size-flags-horizontal"></a>

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **_get_allowed_size_flags_horizontal**() virtual const [🔗](class_container.md#class-container-private-method-get-allowed-size-flags-horizontal)

Implement to return a list of allowed horizontal [SizeFlags](class_control.md#enum-control-sizeflags) for child nodes. This doesn't technically prevent the usages of any other size flags, if your implementation requires that. This only limits the options available to the user in the Inspector dock.

**Note:** Having no size flags is equal to having [Control.SIZE_SHRINK_BEGIN](class_control.md#class-control-constant-size-shrink-begin). As such, this value is always implicitly allowed.

---


<a id="class-container-private-method-get-allowed-size-flags-vertical"></a>

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **_get_allowed_size_flags_vertical**() virtual const [🔗](class_container.md#class-container-private-method-get-allowed-size-flags-vertical)

Implement to return a list of allowed vertical [SizeFlags](class_control.md#enum-control-sizeflags) for child nodes. This doesn't technically prevent the usages of any other size flags, if your implementation requires that. This only limits the options available to the user in the Inspector dock.

**Note:** Having no size flags is equal to having [Control.SIZE_SHRINK_BEGIN](class_control.md#class-control-constant-size-shrink-begin). As such, this value is always implicitly allowed.

---


<a id="class-container-method-fit-child-in-rect"></a>

void **fit_child_in_rect**(child: [Control](class_control.md#class-control), rect: [Rect2](class_rect2.md#class-rect2)) [🔗](class_container.md#class-container-method-fit-child-in-rect)

Fit a child control in a given rect. This is mainly a helper for creating custom container classes.

---


<a id="class-container-method-queue-sort"></a>

void **queue_sort**() [🔗](class_container.md#class-container-method-queue-sort)

Queue resort of the contained children. This is called automatically anyway, but can be called upon request.
