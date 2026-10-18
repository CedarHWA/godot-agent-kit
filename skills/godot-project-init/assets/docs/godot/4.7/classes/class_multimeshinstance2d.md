> Source: https://docs.godotengine.org/en/4.7/classes/class_multimeshinstance2d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="multimeshinstance2d"></a>

<a id="class-multimeshinstance2d"></a>

# MultiMeshInstance2D

**Inherits:** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Node that instances a [MultiMesh](class_multimesh.md#class-multimesh) in 2D.

<a id="description"></a>

## Description

**MultiMeshInstance2D** is a specialized node to instance a [MultiMesh](class_multimesh.md#class-multimesh) resource in 2D. This can be faster to render compared to displaying many [Sprite2D](class_sprite2d.md#class-sprite2d) nodes with large transparent areas, especially if the nodes take up a lot of space on screen at high viewport resolutions. This is because using a mesh designed to fit the sprites' opaque areas will reduce GPU fill rate utilization (at the cost of increased vertex processing utilization).

Usage is the same as [MultiMeshInstance3D](class_multimeshinstance3d.md#class-multimeshinstance3d).

<a id="properties"></a>

## Properties

|  |  |
| --- | --- |
| [MultiMesh](class_multimesh.md#class-multimesh) | [multimesh](class_multimeshinstance2d.md#class-multimeshinstance2d-property-multimesh) |
| [Texture2D](class_texture2d.md#class-texture2d) | [texture](class_multimeshinstance2d.md#class-multimeshinstance2d-property-texture) |

---


<a id="signals"></a>

## Signals

<a id="class-multimeshinstance2d-signal-texture-changed"></a>

**texture_changed**() [🔗](class_multimeshinstance2d.md#class-multimeshinstance2d-signal-texture-changed)

Emitted when the [texture](class_multimeshinstance2d.md#class-multimeshinstance2d-property-texture) is changed.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-multimeshinstance2d-property-multimesh"></a>

[MultiMesh](class_multimesh.md#class-multimesh) **multimesh** [🔗](class_multimeshinstance2d.md#class-multimeshinstance2d-property-multimesh)

- void **set_multimesh**(value: [MultiMesh](class_multimesh.md#class-multimesh))
- [MultiMesh](class_multimesh.md#class-multimesh) **get_multimesh**()

The [MultiMesh](class_multimesh.md#class-multimesh) that will be drawn by the **MultiMeshInstance2D**.

---


<a id="class-multimeshinstance2d-property-texture"></a>

[Texture2D](class_texture2d.md#class-texture2d) **texture** [🔗](class_multimeshinstance2d.md#class-multimeshinstance2d-property-texture)

- void **set_texture**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_texture**()

The [Texture2D](class_texture2d.md#class-texture2d) that will be used if using the default [CanvasItemMaterial](class_canvasitemmaterial.md#class-canvasitemmaterial). Can be accessed as `TEXTURE` in CanvasItem shader.
