> Source: https://docs.godotengine.org/en/4.7/classes/class_visibleonscreennotifier2d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visibleonscreennotifier2d"></a>

<a id="class-visibleonscreennotifier2d"></a>

# VisibleOnScreenNotifier2D

**Inherits:** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [VisibleOnScreenEnabler2D](class_visibleonscreenenabler2d.md#class-visibleonscreenenabler2d)

A rectangular region of 2D space that detects whether it is visible on screen.

<a id="description"></a>

## Description

**VisibleOnScreenNotifier2D** represents a rectangular region of 2D space. When any part of this region becomes visible on screen or in a viewport, it will emit a [screen_entered](class_visibleonscreennotifier2d.md#class-visibleonscreennotifier2d-signal-screen-entered) signal, and likewise it will emit a [screen_exited](class_visibleonscreennotifier2d.md#class-visibleonscreennotifier2d-signal-screen-exited) signal when no part of it remains visible.

If you want a node to be enabled automatically when this region is visible on screen, use [VisibleOnScreenEnabler2D](class_visibleonscreenenabler2d.md#class-visibleonscreenenabler2d).

**Note:** **VisibleOnScreenNotifier2D** uses the render culling code to determine whether it's visible on screen, so it won't function unless [CanvasItem.visible](class_canvasitem.md#class-canvasitem-property-visible) is set to `true`.

<a id="tutorials"></a>

## Tutorials

- [2D Dodge The Creeps Demo](https://godotengine.org/asset-library/asset/2712)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Rect2](class_rect2.md#class-rect2) | [rect](class_visibleonscreennotifier2d.md#class-visibleonscreennotifier2d-property-rect) | `Rect2(-10, -10, 20, 20)` |
| [bool](class_bool.md#class-bool) | [show_rect](class_visibleonscreennotifier2d.md#class-visibleonscreennotifier2d-property-show-rect) | `true` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [is_on_screen](class_visibleonscreennotifier2d.md#class-visibleonscreennotifier2d-method-is-on-screen)() const |

---


<a id="signals"></a>

## Signals

<a id="class-visibleonscreennotifier2d-signal-screen-entered"></a>

**screen_entered**() [🔗](class_visibleonscreennotifier2d.md#class-visibleonscreennotifier2d-signal-screen-entered)

Emitted when the VisibleOnScreenNotifier2D enters the screen.

---


<a id="class-visibleonscreennotifier2d-signal-screen-exited"></a>

**screen_exited**() [🔗](class_visibleonscreennotifier2d.md#class-visibleonscreennotifier2d-signal-screen-exited)

Emitted when the VisibleOnScreenNotifier2D exits the screen.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visibleonscreennotifier2d-property-rect"></a>

[Rect2](class_rect2.md#class-rect2) **rect** = `Rect2(-10, -10, 20, 20)` [🔗](class_visibleonscreennotifier2d.md#class-visibleonscreennotifier2d-property-rect)

- void **set_rect**(value: [Rect2](class_rect2.md#class-rect2))
- [Rect2](class_rect2.md#class-rect2) **get_rect**()

The VisibleOnScreenNotifier2D's bounding rectangle.

---


<a id="class-visibleonscreennotifier2d-property-show-rect"></a>

[bool](class_bool.md#class-bool) **show_rect** = `true` [🔗](class_visibleonscreennotifier2d.md#class-visibleonscreennotifier2d-property-show-rect)

- void **set_show_rect**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_showing_rect**()

If `true`, shows the rectangle area of [rect](class_visibleonscreennotifier2d.md#class-visibleonscreennotifier2d-property-rect) in the editor with a translucent magenta fill. Unlike changing the visibility of the VisibleOnScreenNotifier2D, this does not affect the screen culling detection.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-visibleonscreennotifier2d-method-is-on-screen"></a>

[bool](class_bool.md#class-bool) **is_on_screen**() const [🔗](class_visibleonscreennotifier2d.md#class-visibleonscreennotifier2d-method-is-on-screen)

If `true`, the bounding rectangle is on the screen.

**Note:** It takes one frame for the **VisibleOnScreenNotifier2D**'s visibility to be determined once added to the scene tree, so this method will always return `false` right after it is instantiated, before the draw pass.
