> Source: https://docs.godotengine.org/en/4.7/classes/class_meshinstance2d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="meshinstance2d"></a>

<a id="class-meshinstance2d"></a>

# MeshInstance2D

**Inherits:** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Node used for displaying a [Mesh](class_mesh.md#class-mesh) in 2D.

<a id="description"></a>

## Description

Node used for displaying a [Mesh](class_mesh.md#class-mesh) in 2D. This can be faster to render compared to displaying a [Sprite2D](class_sprite2d.md#class-sprite2d) node with large transparent areas, especially if the node takes up a lot of space on screen at high viewport resolutions. This is because using a mesh designed to fit the sprite's opaque areas will reduce GPU fill rate utilization (at the cost of increased vertex processing utilization).

When a [Mesh](class_mesh.md#class-mesh) has to be instantiated more than thousands of times close to each other, consider using a [MultiMesh](class_multimesh.md#class-multimesh) in a [MultiMeshInstance2D](class_multimeshinstance2d.md#class-multimeshinstance2d) instead.

A **MeshInstance2D** can be created from an existing [Sprite2D](class_sprite2d.md#class-sprite2d) via a tool in the editor toolbar. Select the [Sprite2D](class_sprite2d.md#class-sprite2d) node, then choose **Sprite2D > Convert to MeshInstance2D** at the top of the 2D editor viewport.

<a id="tutorials"></a>

## Tutorials

- [2D meshes](../tutorials/2d/2d_meshes.md)

<a id="properties"></a>

## Properties

|  |  |
| --- | --- |
| [Mesh](class_mesh.md#class-mesh) | [mesh](class_meshinstance2d.md#class-meshinstance2d-property-mesh) |
| [Texture2D](class_texture2d.md#class-texture2d) | [texture](class_meshinstance2d.md#class-meshinstance2d-property-texture) |

---


<a id="signals"></a>

## Signals

<a id="class-meshinstance2d-signal-texture-changed"></a>

**texture_changed**() [🔗](class_meshinstance2d.md#class-meshinstance2d-signal-texture-changed)

Emitted when the [texture](class_meshinstance2d.md#class-meshinstance2d-property-texture) is changed.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-meshinstance2d-property-mesh"></a>

[Mesh](class_mesh.md#class-mesh) **mesh** [🔗](class_meshinstance2d.md#class-meshinstance2d-property-mesh)

- void **set_mesh**(value: [Mesh](class_mesh.md#class-mesh))
- [Mesh](class_mesh.md#class-mesh) **get_mesh**()

The [Mesh](class_mesh.md#class-mesh) that will be drawn by the **MeshInstance2D**.

---


<a id="class-meshinstance2d-property-texture"></a>

[Texture2D](class_texture2d.md#class-texture2d) **texture** [🔗](class_meshinstance2d.md#class-meshinstance2d-property-texture)

- void **set_texture**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_texture**()

The [Texture2D](class_texture2d.md#class-texture2d) that will be used if using the default [CanvasItemMaterial](class_canvasitemmaterial.md#class-canvasitemmaterial). Can be accessed as `TEXTURE` in CanvasItem shader.
