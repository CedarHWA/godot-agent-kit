> Source: https://docs.godotengine.org/en/4.7/classes/class_visibleonscreennotifier3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visibleonscreennotifier3d"></a>

<a id="class-visibleonscreennotifier3d"></a>

# VisibleOnScreenNotifier3D

**Inherits:** [VisualInstance3D](class_visualinstance3d.md#class-visualinstance3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [VisibleOnScreenEnabler3D](class_visibleonscreenenabler3d.md#class-visibleonscreenenabler3d)

A box-shaped region of 3D space that detects whether it is visible on screen.

<a id="description"></a>

## Description

**VisibleOnScreenNotifier3D** represents a box-shaped region of 3D space. When any part of this region becomes visible on screen or in a [Camera3D](class_camera3d.md#class-camera3d)'s view, it will emit a [screen_entered](class_visibleonscreennotifier3d.md#class-visibleonscreennotifier3d-signal-screen-entered) signal, and likewise it will emit a [screen_exited](class_visibleonscreennotifier3d.md#class-visibleonscreennotifier3d-signal-screen-exited) signal when no part of it remains visible.

If you want a node to be enabled automatically when this region is visible on screen, use [VisibleOnScreenEnabler3D](class_visibleonscreenenabler3d.md#class-visibleonscreenenabler3d).

**Note:** **VisibleOnScreenNotifier3D** uses an approximate heuristic that doesn't take walls and other occlusion into account, unless occlusion culling is used. It also won't function unless [Node3D.visible](class_node3d.md#class-node3d-property-visible) is set to `true`.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [AABB](class_aabb.md#class-aabb) | [aabb](class_visibleonscreennotifier3d.md#class-visibleonscreennotifier3d-property-aabb) | `AABB(-1, -1, -1, 2, 2, 2)` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [is_on_screen](class_visibleonscreennotifier3d.md#class-visibleonscreennotifier3d-method-is-on-screen)() const |

---


<a id="signals"></a>

## Signals

<a id="class-visibleonscreennotifier3d-signal-screen-entered"></a>

**screen_entered**() [🔗](class_visibleonscreennotifier3d.md#class-visibleonscreennotifier3d-signal-screen-entered)

Emitted when the **VisibleOnScreenNotifier3D** enters the screen.

---


<a id="class-visibleonscreennotifier3d-signal-screen-exited"></a>

**screen_exited**() [🔗](class_visibleonscreennotifier3d.md#class-visibleonscreennotifier3d-signal-screen-exited)

Emitted when the **VisibleOnScreenNotifier3D** exits the screen.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visibleonscreennotifier3d-property-aabb"></a>

[AABB](class_aabb.md#class-aabb) **aabb** = `AABB(-1, -1, -1, 2, 2, 2)` [🔗](class_visibleonscreennotifier3d.md#class-visibleonscreennotifier3d-property-aabb)

- void **set_aabb**(value: [AABB](class_aabb.md#class-aabb))
- [AABB](class_aabb.md#class-aabb) **get_aabb**()

The **VisibleOnScreenNotifier3D**'s bounding box.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-visibleonscreennotifier3d-method-is-on-screen"></a>

[bool](class_bool.md#class-bool) **is_on_screen**() const [🔗](class_visibleonscreennotifier3d.md#class-visibleonscreennotifier3d-method-is-on-screen)

Returns `true` if the bounding box is on the screen.

**Note:** It takes one frame for the **VisibleOnScreenNotifier3D**'s visibility to be assessed once added to the scene tree, so this method will always return `false` right after it is instantiated.
