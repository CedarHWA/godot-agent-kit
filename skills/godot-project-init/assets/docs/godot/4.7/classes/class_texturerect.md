> Source: https://docs.godotengine.org/en/4.7/classes/class_texturerect.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="texturerect"></a>

<a id="class-texturerect"></a>

# TextureRect

**Inherits:** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A control that displays a texture.

<a id="description"></a>

## Description

A control that displays a texture, for example an icon inside a GUI. The texture's placement can be controlled with the [stretch_mode](class_texturerect.md#class-texturerect-property-stretch-mode) property. It can scale, tile, or stay centered inside its bounding rectangle.

<a id="tutorials"></a>

## Tutorials

- [3D Voxel Demo](https://godotengine.org/asset-library/asset/2755)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [ExpandMode](class_texturerect.md#enum-texturerect-expandmode) | [expand_mode](class_texturerect.md#class-texturerect-property-expand-mode) | `0` |
| [bool](class_bool.md#class-bool) | [flip_h](class_texturerect.md#class-texturerect-property-flip-h) | `false` |
| [bool](class_bool.md#class-bool) | [flip_v](class_texturerect.md#class-texturerect-property-flip-v) | `false` |
| [MouseFilter](class_control.md#enum-control-mousefilter) | mouse_filter | `1` (overrides [Control](class_control.md#class-control-property-mouse-filter)) |
| [StretchMode](class_texturerect.md#enum-texturerect-stretchmode) | [stretch_mode](class_texturerect.md#class-texturerect-property-stretch-mode) | `0` |
| [Texture2D](class_texture2d.md#class-texture2d) | [texture](class_texturerect.md#class-texturerect-property-texture) |  |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-texturerect-expandmode"></a>

enum **ExpandMode**: [🔗](class_texturerect.md#enum-texturerect-expandmode)

<a id="class-texturerect-constant-expand-keep-size"></a>

[ExpandMode](class_texturerect.md#enum-texturerect-expandmode) **EXPAND_KEEP_SIZE** = `0`

The minimum size will be equal to texture size, i.e. **TextureRect** can't be smaller than the texture.

<a id="class-texturerect-constant-expand-ignore-size"></a>

[ExpandMode](class_texturerect.md#enum-texturerect-expandmode) **EXPAND_IGNORE_SIZE** = `1`

The size of the texture won't be considered for minimum size calculation, so the **TextureRect** can be shrunk down past the texture size.

<a id="class-texturerect-constant-expand-fit-width"></a>

[ExpandMode](class_texturerect.md#enum-texturerect-expandmode) **EXPAND_FIT_WIDTH** = `2`

The height of the texture will be ignored. Minimum width will be equal to the current height. Useful for horizontal layouts, e.g. inside [HBoxContainer](class_hboxcontainer.md#class-hboxcontainer).

<a id="class-texturerect-constant-expand-fit-width-proportional"></a>

[ExpandMode](class_texturerect.md#enum-texturerect-expandmode) **EXPAND_FIT_WIDTH_PROPORTIONAL** = `3`

Same as [EXPAND_FIT_WIDTH](class_texturerect.md#class-texturerect-constant-expand-fit-width), but keeps texture's aspect ratio.

<a id="class-texturerect-constant-expand-fit-height"></a>

[ExpandMode](class_texturerect.md#enum-texturerect-expandmode) **EXPAND_FIT_HEIGHT** = `4`

The width of the texture will be ignored. Minimum height will be equal to the current width. Useful for vertical layouts, e.g. inside [VBoxContainer](class_vboxcontainer.md#class-vboxcontainer).

<a id="class-texturerect-constant-expand-fit-height-proportional"></a>

[ExpandMode](class_texturerect.md#enum-texturerect-expandmode) **EXPAND_FIT_HEIGHT_PROPORTIONAL** = `5`

Same as [EXPAND_FIT_HEIGHT](class_texturerect.md#class-texturerect-constant-expand-fit-height), but keeps texture's aspect ratio.

---


<a id="enum-texturerect-stretchmode"></a>

enum **StretchMode**: [🔗](class_texturerect.md#enum-texturerect-stretchmode)

<a id="class-texturerect-constant-stretch-scale"></a>

[StretchMode](class_texturerect.md#enum-texturerect-stretchmode) **STRETCH_SCALE** = `0`

Scale to fit the node's bounding rectangle.

<a id="class-texturerect-constant-stretch-tile"></a>

[StretchMode](class_texturerect.md#enum-texturerect-stretchmode) **STRETCH_TILE** = `1`

Tile inside the node's bounding rectangle.

**Note:** [STRETCH_TILE](class_texturerect.md#class-texturerect-constant-stretch-tile) mode is not supported for [texture](class_texturerect.md#class-texturerect-property-texture) set to an [AtlasTexture](class_atlastexture.md#class-atlastexture) with non-zero [AtlasTexture.margin](class_atlastexture.md#class-atlastexture-property-margin).

<a id="class-texturerect-constant-stretch-keep"></a>

[StretchMode](class_texturerect.md#enum-texturerect-stretchmode) **STRETCH_KEEP** = `2`

The texture keeps its original size and stays in the bounding rectangle's top-left corner.

<a id="class-texturerect-constant-stretch-keep-centered"></a>

[StretchMode](class_texturerect.md#enum-texturerect-stretchmode) **STRETCH_KEEP_CENTERED** = `3`

The texture keeps its original size and stays centered in the node's bounding rectangle.

<a id="class-texturerect-constant-stretch-keep-aspect"></a>

[StretchMode](class_texturerect.md#enum-texturerect-stretchmode) **STRETCH_KEEP_ASPECT** = `4`

Scale the texture to fit the node's bounding rectangle, but maintain the texture's aspect ratio.

<a id="class-texturerect-constant-stretch-keep-aspect-centered"></a>

[StretchMode](class_texturerect.md#enum-texturerect-stretchmode) **STRETCH_KEEP_ASPECT_CENTERED** = `5`

Scale the texture to fit the node's bounding rectangle, center it and maintain its aspect ratio.

<a id="class-texturerect-constant-stretch-keep-aspect-covered"></a>

[StretchMode](class_texturerect.md#enum-texturerect-stretchmode) **STRETCH_KEEP_ASPECT_COVERED** = `6`

Scale the texture so that the shorter side fits the bounding rectangle. The other side clips to the node's limits.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-texturerect-property-expand-mode"></a>

[ExpandMode](class_texturerect.md#enum-texturerect-expandmode) **expand_mode** = `0` [🔗](class_texturerect.md#class-texturerect-property-expand-mode)

- void **set_expand_mode**(value: [ExpandMode](class_texturerect.md#enum-texturerect-expandmode))
- [ExpandMode](class_texturerect.md#enum-texturerect-expandmode) **get_expand_mode**()

**Experimental:** Using [EXPAND_FIT_WIDTH](class_texturerect.md#class-texturerect-constant-expand-fit-width), [EXPAND_FIT_WIDTH_PROPORTIONAL](class_texturerect.md#class-texturerect-constant-expand-fit-width-proportional), [EXPAND_FIT_HEIGHT](class_texturerect.md#class-texturerect-constant-expand-fit-height), or [EXPAND_FIT_HEIGHT_PROPORTIONAL](class_texturerect.md#class-texturerect-constant-expand-fit-height-proportional) may result in unstable behavior in some [Container](class_container.md#class-container) controls. This behavior may be re-evaluated and changed in the future.

Defines how minimum size is determined based on the texture's size.

---


<a id="class-texturerect-property-flip-h"></a>

[bool](class_bool.md#class-bool) **flip_h** = `false` [🔗](class_texturerect.md#class-texturerect-property-flip-h)

- void **set_flip_h**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_flipped_h**()

If `true`, texture is flipped horizontally.

---


<a id="class-texturerect-property-flip-v"></a>

[bool](class_bool.md#class-bool) **flip_v** = `false` [🔗](class_texturerect.md#class-texturerect-property-flip-v)

- void **set_flip_v**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_flipped_v**()

If `true`, texture is flipped vertically.

---


<a id="class-texturerect-property-stretch-mode"></a>

[StretchMode](class_texturerect.md#enum-texturerect-stretchmode) **stretch_mode** = `0` [🔗](class_texturerect.md#class-texturerect-property-stretch-mode)

- void **set_stretch_mode**(value: [StretchMode](class_texturerect.md#enum-texturerect-stretchmode))
- [StretchMode](class_texturerect.md#enum-texturerect-stretchmode) **get_stretch_mode**()

Controls the texture's behavior when resizing the node's bounding rectangle.

---


<a id="class-texturerect-property-texture"></a>

[Texture2D](class_texture2d.md#class-texture2d) **texture** [🔗](class_texturerect.md#class-texturerect-property-texture)

- void **set_texture**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_texture**()

The node's [Texture2D](class_texture2d.md#class-texture2d) resource.
