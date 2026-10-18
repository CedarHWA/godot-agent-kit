> Source: https://docs.godotengine.org/en/4.7/classes/class_subviewportcontainer.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="subviewportcontainer"></a>

<a id="class-subviewportcontainer"></a>

# SubViewportContainer

**Inherits:** [Container](class_container.md#class-container) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A container used for displaying the contents of a [SubViewport](class_subviewport.md#class-subviewport).

<a id="description"></a>

## Description

A container that displays the contents of underlying [SubViewport](class_subviewport.md#class-subviewport) child nodes. It uses the combined size of the [SubViewport](class_subviewport.md#class-subviewport)s as minimum size, unless [stretch](class_subviewportcontainer.md#class-subviewportcontainer-property-stretch) is enabled.

**Note:** Changing a **SubViewportContainer**'s [Control.scale](class_control.md#class-control-property-scale) will cause its contents to appear distorted. To change its visual size without causing distortion, adjust the node's margins instead (if it's not already in a container).

**Note:** The **SubViewportContainer** forwards mouse-enter and mouse-exit notifications to its sub-viewports.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [FocusMode](class_control.md#enum-control-focusmode) | focus_mode | `1` (overrides [Control](class_control.md#class-control-property-focus-mode)) |
| [bool](class_bool.md#class-bool) | [mouse_target](class_subviewportcontainer.md#class-subviewportcontainer-property-mouse-target) | `false` |
| [bool](class_bool.md#class-bool) | [stretch](class_subviewportcontainer.md#class-subviewportcontainer-property-stretch) | `false` |
| [int](class_int.md#class-int) | [stretch_shrink](class_subviewportcontainer.md#class-subviewportcontainer-property-stretch-shrink) | `1` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [_propagate_input_event](class_subviewportcontainer.md#class-subviewportcontainer-private-method-propagate-input-event)(event: [InputEvent](class_inputevent.md#class-inputevent)) virtual const |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-subviewportcontainer-property-mouse-target"></a>

[bool](class_bool.md#class-bool) **mouse_target** = `false` [🔗](class_subviewportcontainer.md#class-subviewportcontainer-property-mouse-target)

- void **set_mouse_target**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_mouse_target_enabled**()

Configure, if either the **SubViewportContainer** or alternatively the [Control](class_control.md#class-control) nodes of its [SubViewport](class_subviewport.md#class-subviewport) children should be available as targets of mouse-related functionalities, like identifying the drop target in drag-and-drop operations or cursor shape of hovered [Control](class_control.md#class-control) node.

If `false`, the [Control](class_control.md#class-control) nodes inside its [SubViewport](class_subviewport.md#class-subviewport) children are considered as targets.

If `true`, the **SubViewportContainer** itself will be considered as a target.

---


<a id="class-subviewportcontainer-property-stretch"></a>

[bool](class_bool.md#class-bool) **stretch** = `false` [🔗](class_subviewportcontainer.md#class-subviewportcontainer-property-stretch)

- void **set_stretch**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_stretch_enabled**()

If `true`, the sub-viewport will be automatically resized to the control's size.

**Note:** If `true`, this will prohibit changing [SubViewport.size](class_subviewport.md#class-subviewport-property-size) of its children manually.

---


<a id="class-subviewportcontainer-property-stretch-shrink"></a>

[int](class_int.md#class-int) **stretch_shrink** = `1` [🔗](class_subviewportcontainer.md#class-subviewportcontainer-property-stretch-shrink)

- void **set_stretch_shrink**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_stretch_shrink**()

Divides the sub-viewport's effective resolution by this value while preserving its scale. This can be used to speed up rendering.

For example, a 1280×720 sub-viewport with [stretch_shrink](class_subviewportcontainer.md#class-subviewportcontainer-property-stretch-shrink) set to `2` will be rendered at 640×360 while occupying the same size in the container.

**Note:** [stretch](class_subviewportcontainer.md#class-subviewportcontainer-property-stretch) must be `true` for this property to work.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-subviewportcontainer-private-method-propagate-input-event"></a>

[bool](class_bool.md#class-bool) **_propagate_input_event**(event: [InputEvent](class_inputevent.md#class-inputevent)) virtual const [🔗](class_subviewportcontainer.md#class-subviewportcontainer-private-method-propagate-input-event)

**Experimental:** This method may be changed or removed in future versions.

Virtual method to be implemented by the user. If it returns `true`, the `event` is propagated to [SubViewport](class_subviewport.md#class-subviewport) children. Propagation doesn't happen if it returns `false`. If the function is not implemented, all events are propagated to SubViewports.
