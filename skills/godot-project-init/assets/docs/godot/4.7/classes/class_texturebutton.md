> Source: https://docs.godotengine.org/en/4.7/classes/class_texturebutton.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="texturebutton"></a>

<a id="class-texturebutton"></a>

# TextureButton

**Inherits:** [BaseButton](class_basebutton.md#class-basebutton) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Texture-based button. Supports Pressed, Hover, Disabled and Focused states.

<a id="description"></a>

## Description

**TextureButton** has the same functionality as [Button](class_button.md#class-button), except it uses sprites instead of Godot's [Theme](class_theme.md#class-theme) resource. It is faster to create, but it doesn't support localization like more complex [Control](class_control.md#class-control)s.

See also [BaseButton](class_basebutton.md#class-basebutton) which contains common properties and methods associated with this node.

**Note:** Setting a texture for the "normal" state ([texture_normal](class_texturebutton.md#class-texturebutton-property-texture-normal)) is recommended. If [texture_normal](class_texturebutton.md#class-texturebutton-property-texture-normal) is not set, the **TextureButton** will still receive input events and be clickable, but the user will not be able to see it unless they activate another one of its states with a texture assigned (e.g., hover over it to show [texture_hover](class_texturebutton.md#class-texturebutton-property-texture-hover)).

<a id="tutorials"></a>

## Tutorials

- [3D Voxel Demo](https://godotengine.org/asset-library/asset/2755)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [flip_h](class_texturebutton.md#class-texturebutton-property-flip-h) | `false` |
| [bool](class_bool.md#class-bool) | [flip_v](class_texturebutton.md#class-texturebutton-property-flip-v) | `false` |
| [bool](class_bool.md#class-bool) | [ignore_texture_size](class_texturebutton.md#class-texturebutton-property-ignore-texture-size) | `false` |
| [StretchMode](class_texturebutton.md#enum-texturebutton-stretchmode) | [stretch_mode](class_texturebutton.md#class-texturebutton-property-stretch-mode) | `2` |
| [BitMap](class_bitmap.md#class-bitmap) | [texture_click_mask](class_texturebutton.md#class-texturebutton-property-texture-click-mask) |  |
| [Texture2D](class_texture2d.md#class-texture2d) | [texture_disabled](class_texturebutton.md#class-texturebutton-property-texture-disabled) |  |
| [Texture2D](class_texture2d.md#class-texture2d) | [texture_focused](class_texturebutton.md#class-texturebutton-property-texture-focused) |  |
| [Texture2D](class_texture2d.md#class-texture2d) | [texture_hover](class_texturebutton.md#class-texturebutton-property-texture-hover) |  |
| [Texture2D](class_texture2d.md#class-texture2d) | [texture_normal](class_texturebutton.md#class-texturebutton-property-texture-normal) |  |
| [Texture2D](class_texture2d.md#class-texture2d) | [texture_pressed](class_texturebutton.md#class-texturebutton-property-texture-pressed) |  |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-texturebutton-stretchmode"></a>

enum **StretchMode**: [🔗](class_texturebutton.md#enum-texturebutton-stretchmode)

<a id="class-texturebutton-constant-stretch-scale"></a>

[StretchMode](class_texturebutton.md#enum-texturebutton-stretchmode) **STRETCH_SCALE** = `0`

Scale to fit the node's bounding rectangle.

<a id="class-texturebutton-constant-stretch-tile"></a>

[StretchMode](class_texturebutton.md#enum-texturebutton-stretchmode) **STRETCH_TILE** = `1`

Tile inside the node's bounding rectangle.

<a id="class-texturebutton-constant-stretch-keep"></a>

[StretchMode](class_texturebutton.md#enum-texturebutton-stretchmode) **STRETCH_KEEP** = `2`

The texture keeps its original size and stays in the bounding rectangle's top-left corner.

<a id="class-texturebutton-constant-stretch-keep-centered"></a>

[StretchMode](class_texturebutton.md#enum-texturebutton-stretchmode) **STRETCH_KEEP_CENTERED** = `3`

The texture keeps its original size and stays centered in the node's bounding rectangle.

<a id="class-texturebutton-constant-stretch-keep-aspect"></a>

[StretchMode](class_texturebutton.md#enum-texturebutton-stretchmode) **STRETCH_KEEP_ASPECT** = `4`

Scale the texture to fit the node's bounding rectangle, but maintain the texture's aspect ratio.

<a id="class-texturebutton-constant-stretch-keep-aspect-centered"></a>

[StretchMode](class_texturebutton.md#enum-texturebutton-stretchmode) **STRETCH_KEEP_ASPECT_CENTERED** = `5`

Scale the texture to fit the node's bounding rectangle, center it, and maintain its aspect ratio.

<a id="class-texturebutton-constant-stretch-keep-aspect-covered"></a>

[StretchMode](class_texturebutton.md#enum-texturebutton-stretchmode) **STRETCH_KEEP_ASPECT_COVERED** = `6`

Scale the texture so that the shorter side fits the bounding rectangle. The other side clips to the node's limits.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-texturebutton-property-flip-h"></a>

[bool](class_bool.md#class-bool) **flip_h** = `false` [🔗](class_texturebutton.md#class-texturebutton-property-flip-h)

- void **set_flip_h**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_flipped_h**()

If `true`, texture is flipped horizontally.

---


<a id="class-texturebutton-property-flip-v"></a>

[bool](class_bool.md#class-bool) **flip_v** = `false` [🔗](class_texturebutton.md#class-texturebutton-property-flip-v)

- void **set_flip_v**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_flipped_v**()

If `true`, texture is flipped vertically.

---


<a id="class-texturebutton-property-ignore-texture-size"></a>

[bool](class_bool.md#class-bool) **ignore_texture_size** = `false` [🔗](class_texturebutton.md#class-texturebutton-property-ignore-texture-size)

- void **set_ignore_texture_size**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_ignore_texture_size**()

If `true`, the size of the texture won't be considered for minimum size calculation, so the **TextureButton** can be shrunk down past the texture size.

---


<a id="class-texturebutton-property-stretch-mode"></a>

[StretchMode](class_texturebutton.md#enum-texturebutton-stretchmode) **stretch_mode** = `2` [🔗](class_texturebutton.md#class-texturebutton-property-stretch-mode)

- void **set_stretch_mode**(value: [StretchMode](class_texturebutton.md#enum-texturebutton-stretchmode))
- [StretchMode](class_texturebutton.md#enum-texturebutton-stretchmode) **get_stretch_mode**()

Controls the texture's behavior when you resize the node's bounding rectangle. See the [StretchMode](class_texturebutton.md#enum-texturebutton-stretchmode) constants for available options.

---


<a id="class-texturebutton-property-texture-click-mask"></a>

[BitMap](class_bitmap.md#class-bitmap) **texture_click_mask** [🔗](class_texturebutton.md#class-texturebutton-property-texture-click-mask)

- void **set_click_mask**(value: [BitMap](class_bitmap.md#class-bitmap))
- [BitMap](class_bitmap.md#class-bitmap) **get_click_mask**()

Pure black and white [BitMap](class_bitmap.md#class-bitmap) image to use for click detection. On the mask, white pixels represent the button's clickable area. Use it to create buttons with curved shapes.

---


<a id="class-texturebutton-property-texture-disabled"></a>

[Texture2D](class_texture2d.md#class-texture2d) **texture_disabled** [🔗](class_texturebutton.md#class-texturebutton-property-texture-disabled)

- void **set_texture_disabled**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_texture_disabled**()

Texture to display when the node is disabled. See [BaseButton.disabled](class_basebutton.md#class-basebutton-property-disabled). If not assigned, the **TextureButton** displays [texture_normal](class_texturebutton.md#class-texturebutton-property-texture-normal) instead.

---


<a id="class-texturebutton-property-texture-focused"></a>

[Texture2D](class_texture2d.md#class-texture2d) **texture_focused** [🔗](class_texturebutton.md#class-texturebutton-property-texture-focused)

- void **set_texture_focused**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_texture_focused**()

Texture to *overlay on the base texture* when the node has mouse or keyboard focus. Because [texture_focused](class_texturebutton.md#class-texturebutton-property-texture-focused) is displayed on top of the base texture, a partially transparent texture should be used to ensure the base texture remains visible. A texture that represents an outline or an underline works well for this purpose. To disable the focus visual effect, assign a fully transparent texture of any size. Note that disabling the focus visual effect will harm keyboard/controller navigation usability, so this is not recommended for accessibility reasons.

---


<a id="class-texturebutton-property-texture-hover"></a>

[Texture2D](class_texture2d.md#class-texture2d) **texture_hover** [🔗](class_texturebutton.md#class-texturebutton-property-texture-hover)

- void **set_texture_hover**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_texture_hover**()

Texture to display when the mouse hovers over the node. If not assigned, the **TextureButton** displays [texture_normal](class_texturebutton.md#class-texturebutton-property-texture-normal) instead when hovered over.

---


<a id="class-texturebutton-property-texture-normal"></a>

[Texture2D](class_texture2d.md#class-texture2d) **texture_normal** [🔗](class_texturebutton.md#class-texturebutton-property-texture-normal)

- void **set_texture_normal**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_texture_normal**()

Texture to display by default, when the node is **not** in the disabled, hover or pressed state. This texture is still displayed in the focused state, with [texture_focused](class_texturebutton.md#class-texturebutton-property-texture-focused) drawn on top.

---


<a id="class-texturebutton-property-texture-pressed"></a>

[Texture2D](class_texture2d.md#class-texture2d) **texture_pressed** [🔗](class_texturebutton.md#class-texturebutton-property-texture-pressed)

- void **set_texture_pressed**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_texture_pressed**()

Texture to display on mouse down over the node, if the node has keyboard focus and the player presses the Enter key or if the player presses the [BaseButton.shortcut](class_basebutton.md#class-basebutton-property-shortcut) key. If not assigned, the **TextureButton** displays [texture_hover](class_texturebutton.md#class-texturebutton-property-texture-hover) instead when pressed.
