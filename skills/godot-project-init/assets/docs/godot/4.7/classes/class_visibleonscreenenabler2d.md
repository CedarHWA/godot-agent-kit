> Source: https://docs.godotengine.org/en/4.7/classes/class_visibleonscreenenabler2d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visibleonscreenenabler2d"></a>

<a id="class-visibleonscreenenabler2d"></a>

# VisibleOnScreenEnabler2D

**Inherits:** [VisibleOnScreenNotifier2D](class_visibleonscreennotifier2d.md#class-visibleonscreennotifier2d) **<** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A rectangular region of 2D space that, when visible on screen, enables a target node.

<a id="description"></a>

## Description

**VisibleOnScreenEnabler2D** contains a rectangular region of 2D space and a target node. The target node will be automatically enabled (via its [Node.process_mode](class_node.md#class-node-property-process-mode) property) when any part of this region becomes visible on the screen, and automatically disabled otherwise. This can for example be used to activate enemies only when the player approaches them.

See [VisibleOnScreenNotifier2D](class_visibleonscreennotifier2d.md#class-visibleonscreennotifier2d) if you only want to be notified when the region is visible on screen.

**Note:** **VisibleOnScreenEnabler2D** uses the render culling code to determine whether it's visible on screen, so it won't function unless [CanvasItem.visible](class_canvasitem.md#class-canvasitem-property-visible) is set to `true`.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [EnableMode](class_visibleonscreenenabler2d.md#enum-visibleonscreenenabler2d-enablemode) | [enable_mode](class_visibleonscreenenabler2d.md#class-visibleonscreenenabler2d-property-enable-mode) | `0` |
| [NodePath](class_nodepath.md#class-nodepath) | [enable_node_path](class_visibleonscreenenabler2d.md#class-visibleonscreenenabler2d-property-enable-node-path) | `NodePath("..")` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-visibleonscreenenabler2d-enablemode"></a>

enum **EnableMode**: [🔗](class_visibleonscreenenabler2d.md#enum-visibleonscreenenabler2d-enablemode)

<a id="class-visibleonscreenenabler2d-constant-enable-mode-inherit"></a>

[EnableMode](class_visibleonscreenenabler2d.md#enum-visibleonscreenenabler2d-enablemode) **ENABLE_MODE_INHERIT** = `0`

Corresponds to [Node.PROCESS_MODE_INHERIT](class_node.md#class-node-constant-process-mode-inherit).

<a id="class-visibleonscreenenabler2d-constant-enable-mode-always"></a>

[EnableMode](class_visibleonscreenenabler2d.md#enum-visibleonscreenenabler2d-enablemode) **ENABLE_MODE_ALWAYS** = `1`

Corresponds to [Node.PROCESS_MODE_ALWAYS](class_node.md#class-node-constant-process-mode-always).

<a id="class-visibleonscreenenabler2d-constant-enable-mode-when-paused"></a>

[EnableMode](class_visibleonscreenenabler2d.md#enum-visibleonscreenenabler2d-enablemode) **ENABLE_MODE_WHEN_PAUSED** = `2`

Corresponds to [Node.PROCESS_MODE_WHEN_PAUSED](class_node.md#class-node-constant-process-mode-when-paused).

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visibleonscreenenabler2d-property-enable-mode"></a>

[EnableMode](class_visibleonscreenenabler2d.md#enum-visibleonscreenenabler2d-enablemode) **enable_mode** = `0` [🔗](class_visibleonscreenenabler2d.md#class-visibleonscreenenabler2d-property-enable-mode)

- void **set_enable_mode**(value: [EnableMode](class_visibleonscreenenabler2d.md#enum-visibleonscreenenabler2d-enablemode))
- [EnableMode](class_visibleonscreenenabler2d.md#enum-visibleonscreenenabler2d-enablemode) **get_enable_mode**()

Determines how the target node is enabled. Corresponds to [ProcessMode](class_node.md#enum-node-processmode). When the node is disabled, it always uses [Node.PROCESS_MODE_DISABLED](class_node.md#class-node-constant-process-mode-disabled).

---


<a id="class-visibleonscreenenabler2d-property-enable-node-path"></a>

[NodePath](class_nodepath.md#class-nodepath) **enable_node_path** = `NodePath("..")` [🔗](class_visibleonscreenenabler2d.md#class-visibleonscreenenabler2d-property-enable-node-path)

- void **set_enable_node_path**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_enable_node_path**()

The path to the target node, relative to the **VisibleOnScreenEnabler2D**. The target node is cached; it's only assigned when setting this property (if the **VisibleOnScreenEnabler2D** is inside the scene tree) and every time the **VisibleOnScreenEnabler2D** enters the scene tree. If the path is empty, no node will be affected. If the path is invalid, an error is also generated.
