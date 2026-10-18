> Source: https://docs.godotengine.org/en/4.7/classes/class_sprite3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="sprite3d"></a>

<a id="class-sprite3d"></a>

# Sprite3D

**Inherits:** [SpriteBase3D](class_spritebase3d.md#class-spritebase3d) **<** [GeometryInstance3D](class_geometryinstance3d.md#class-geometryinstance3d) **<** [VisualInstance3D](class_visualinstance3d.md#class-visualinstance3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

2D sprite node in a 3D world.

<a id="description"></a>

## Description

A node that displays a 2D texture in a 3D environment. The texture displayed can be a region from a larger atlas texture, or a frame from a sprite sheet animation. See also [SpriteBase3D](class_spritebase3d.md#class-spritebase3d) where properties such as the billboard mode are defined.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [frame](class_sprite3d.md#class-sprite3d-property-frame) | `0` |
| [Vector2i](class_vector2i.md#class-vector2i) | [frame_coords](class_sprite3d.md#class-sprite3d-property-frame-coords) | `Vector2i(0, 0)` |
| [int](class_int.md#class-int) | [hframes](class_sprite3d.md#class-sprite3d-property-hframes) | `1` |
| [bool](class_bool.md#class-bool) | [region_enabled](class_sprite3d.md#class-sprite3d-property-region-enabled) | `false` |
| [Rect2](class_rect2.md#class-rect2) | [region_rect](class_sprite3d.md#class-sprite3d-property-region-rect) | `Rect2(0, 0, 0, 0)` |
| [Texture2D](class_texture2d.md#class-texture2d) | [texture](class_sprite3d.md#class-sprite3d-property-texture) |  |
| [int](class_int.md#class-int) | [vframes](class_sprite3d.md#class-sprite3d-property-vframes) | `1` |

---


<a id="signals"></a>

## Signals

<a id="class-sprite3d-signal-frame-changed"></a>

**frame_changed**() [🔗](class_sprite3d.md#class-sprite3d-signal-frame-changed)

Emitted when the [frame](class_sprite3d.md#class-sprite3d-property-frame) changes.

---


<a id="class-sprite3d-signal-texture-changed"></a>

**texture_changed**() [🔗](class_sprite3d.md#class-sprite3d-signal-texture-changed)

Emitted when the [texture](class_sprite3d.md#class-sprite3d-property-texture) changes.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-sprite3d-property-frame"></a>

[int](class_int.md#class-int) **frame** = `0` [🔗](class_sprite3d.md#class-sprite3d-property-frame)

- void **set_frame**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_frame**()

Current frame to display from sprite sheet. [hframes](class_sprite3d.md#class-sprite3d-property-hframes) or [vframes](class_sprite3d.md#class-sprite3d-property-vframes) must be greater than 1. This property is automatically adjusted when [hframes](class_sprite3d.md#class-sprite3d-property-hframes) or [vframes](class_sprite3d.md#class-sprite3d-property-vframes) are changed to keep pointing to the same visual frame (same column and row). If that's impossible, this value is reset to `0`.

---


<a id="class-sprite3d-property-frame-coords"></a>

[Vector2i](class_vector2i.md#class-vector2i) **frame_coords** = `Vector2i(0, 0)` [🔗](class_sprite3d.md#class-sprite3d-property-frame-coords)

- void **set_frame_coords**(value: [Vector2i](class_vector2i.md#class-vector2i))
- [Vector2i](class_vector2i.md#class-vector2i) **get_frame_coords**()

Coordinates of the frame to display from sprite sheet. This is as an alias for the [frame](class_sprite3d.md#class-sprite3d-property-frame) property. [hframes](class_sprite3d.md#class-sprite3d-property-hframes) or [vframes](class_sprite3d.md#class-sprite3d-property-vframes) must be greater than 1.

---


<a id="class-sprite3d-property-hframes"></a>

[int](class_int.md#class-int) **hframes** = `1` [🔗](class_sprite3d.md#class-sprite3d-property-hframes)

- void **set_hframes**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_hframes**()

The number of columns in the sprite sheet. When this property is changed, [frame](class_sprite3d.md#class-sprite3d-property-frame) is adjusted so that the same visual frame is maintained (same row and column). If that's impossible, [frame](class_sprite3d.md#class-sprite3d-property-frame) is reset to `0`.

---


<a id="class-sprite3d-property-region-enabled"></a>

[bool](class_bool.md#class-bool) **region_enabled** = `false` [🔗](class_sprite3d.md#class-sprite3d-property-region-enabled)

- void **set_region_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_region_enabled**()

If `true`, the sprite will use [region_rect](class_sprite3d.md#class-sprite3d-property-region-rect) and display only the specified part of its texture.

---


<a id="class-sprite3d-property-region-rect"></a>

[Rect2](class_rect2.md#class-rect2) **region_rect** = `Rect2(0, 0, 0, 0)` [🔗](class_sprite3d.md#class-sprite3d-property-region-rect)

- void **set_region_rect**(value: [Rect2](class_rect2.md#class-rect2))
- [Rect2](class_rect2.md#class-rect2) **get_region_rect**()

The region of the atlas texture to display. [region_enabled](class_sprite3d.md#class-sprite3d-property-region-enabled) must be `true`.

---


<a id="class-sprite3d-property-texture"></a>

[Texture2D](class_texture2d.md#class-texture2d) **texture** [🔗](class_sprite3d.md#class-sprite3d-property-texture)

- void **set_texture**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_texture**()

[Texture2D](class_texture2d.md#class-texture2d) object to draw. If [GeometryInstance3D.material_override](class_geometryinstance3d.md#class-geometryinstance3d-property-material-override) is used, this will be overridden. The size information is still used.

---


<a id="class-sprite3d-property-vframes"></a>

[int](class_int.md#class-int) **vframes** = `1` [🔗](class_sprite3d.md#class-sprite3d-property-vframes)

- void **set_vframes**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_vframes**()

The number of rows in the sprite sheet. When this property is changed, [frame](class_sprite3d.md#class-sprite3d-property-frame) is adjusted so that the same visual frame is maintained (same row and column). If that's impossible, [frame](class_sprite3d.md#class-sprite3d-property-frame) is reset to `0`.
