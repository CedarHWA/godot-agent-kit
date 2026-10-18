> Source: https://docs.godotengine.org/en/4.7/classes/class_texture2d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="texture2d"></a>

<a id="class-texture2d"></a>

# Texture2D

**Inherits:** [Texture](class_texture.md#class-texture) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [AnimatedTexture](class_animatedtexture.md#class-animatedtexture), [AtlasTexture](class_atlastexture.md#class-atlastexture), [CameraTexture](class_cameratexture.md#class-cameratexture), [CanvasTexture](class_canvastexture.md#class-canvastexture), [CompressedTexture2D](class_compressedtexture2d.md#class-compressedtexture2d), [CurveTexture](class_curvetexture.md#class-curvetexture), [CurveXYZTexture](class_curvexyztexture.md#class-curvexyztexture), [DPITexture](class_dpitexture.md#class-dpitexture), [DrawableTexture2D](class_drawabletexture2d.md#class-drawabletexture2d), [ExternalTexture](class_externaltexture.md#class-externaltexture), [GradientTexture1D](class_gradienttexture1d.md#class-gradienttexture1d), [GradientTexture2D](class_gradienttexture2d.md#class-gradienttexture2d), [ImageTexture](class_imagetexture.md#class-imagetexture), [MeshTexture](class_meshtexture.md#class-meshtexture), [NoiseTexture2D](class_noisetexture2d.md#class-noisetexture2d), [PlaceholderTexture2D](class_placeholdertexture2d.md#class-placeholdertexture2d), [PortableCompressedTexture2D](class_portablecompressedtexture2d.md#class-portablecompressedtexture2d), [Texture2DRD](class_texture2drd.md#class-texture2drd), [ViewportTexture](class_viewporttexture.md#class-viewporttexture)

Texture for 2D and 3D.

<a id="description"></a>

## Description

A texture works by registering an image in the video hardware, which then can be used in 3D models or 2D [Sprite2D](class_sprite2d.md#class-sprite2d) or GUI [Control](class_control.md#class-control).

Textures are often created by loading them from a file. See [@GDScript.load()](class_@gdscript.md#class-gdscript-method-load).

**Texture2D** is a base for other resources. It cannot be used directly.

**Note:** The maximum texture size is 16384×16384 pixels due to graphics hardware limitations. Larger textures may fail to import.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [_draw](class_texture2d.md#class-texture2d-private-method-draw)(to_canvas_item: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), modulate: [Color](class_color.md#class-color), transpose: [bool](class_bool.md#class-bool)) virtual const |
| void | [_draw_rect](class_texture2d.md#class-texture2d-private-method-draw-rect)(to_canvas_item: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2), tile: [bool](class_bool.md#class-bool), modulate: [Color](class_color.md#class-color), transpose: [bool](class_bool.md#class-bool)) virtual const |
| void | [_draw_rect_region](class_texture2d.md#class-texture2d-private-method-draw-rect-region)(to_canvas_item: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2), src_rect: [Rect2](class_rect2.md#class-rect2), modulate: [Color](class_color.md#class-color), transpose: [bool](class_bool.md#class-bool), clip_uv: [bool](class_bool.md#class-bool)) virtual const |
| [Format](class_image.md#enum-image-format) | [_get_format](class_texture2d.md#class-texture2d-private-method-get-format)() virtual const |
| [int](class_int.md#class-int) | [_get_height](class_texture2d.md#class-texture2d-private-method-get-height)() virtual required const |
| [Image](class_image.md#class-image) | [_get_image](class_texture2d.md#class-texture2d-private-method-get-image)() virtual const |
| [int](class_int.md#class-int) | [_get_mipmap_count](class_texture2d.md#class-texture2d-private-method-get-mipmap-count)() virtual const |
| [int](class_int.md#class-int) | [_get_width](class_texture2d.md#class-texture2d-private-method-get-width)() virtual required const |
| [bool](class_bool.md#class-bool) | [_has_alpha](class_texture2d.md#class-texture2d-private-method-has-alpha)() virtual const |
| [bool](class_bool.md#class-bool) | [_has_mipmaps](class_texture2d.md#class-texture2d-private-method-has-mipmaps)() virtual const |
| [bool](class_bool.md#class-bool) | [_is_pixel_opaque](class_texture2d.md#class-texture2d-private-method-is-pixel-opaque)(x: [int](class_int.md#class-int), y: [int](class_int.md#class-int)) virtual const |
| [Resource](class_resource.md#class-resource) | [create_placeholder](class_texture2d.md#class-texture2d-method-create-placeholder)() const |
| void | [draw](class_texture2d.md#class-texture2d-method-draw)(canvas_item: [RID](class_rid.md#class-rid), position: [Vector2](class_vector2.md#class-vector2), modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), transpose: [bool](class_bool.md#class-bool) = false) const |
| void | [draw_rect](class_texture2d.md#class-texture2d-method-draw-rect)(canvas_item: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2), tile: [bool](class_bool.md#class-bool), modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), transpose: [bool](class_bool.md#class-bool) = false) const |
| void | [draw_rect_region](class_texture2d.md#class-texture2d-method-draw-rect-region)(canvas_item: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2), src_rect: [Rect2](class_rect2.md#class-rect2), modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), transpose: [bool](class_bool.md#class-bool) = false, clip_uv: [bool](class_bool.md#class-bool) = true) const |
| [Format](class_image.md#enum-image-format) | [get_format](class_texture2d.md#class-texture2d-method-get-format)() const |
| [int](class_int.md#class-int) | [get_height](class_texture2d.md#class-texture2d-method-get-height)() const |
| [Image](class_image.md#class-image) | [get_image](class_texture2d.md#class-texture2d-method-get-image)() const |
| [int](class_int.md#class-int) | [get_mipmap_count](class_texture2d.md#class-texture2d-method-get-mipmap-count)() const |
| [Vector2](class_vector2.md#class-vector2) | [get_size](class_texture2d.md#class-texture2d-method-get-size)() const |
| [int](class_int.md#class-int) | [get_width](class_texture2d.md#class-texture2d-method-get-width)() const |
| [bool](class_bool.md#class-bool) | [has_alpha](class_texture2d.md#class-texture2d-method-has-alpha)() const |
| [bool](class_bool.md#class-bool) | [has_mipmaps](class_texture2d.md#class-texture2d-method-has-mipmaps)() const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-texture2d-private-method-draw"></a>

void **_draw**(to_canvas_item: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), modulate: [Color](class_color.md#class-color), transpose: [bool](class_bool.md#class-bool)) virtual const [🔗](class_texture2d.md#class-texture2d-private-method-draw)

Called when the entire **Texture2D** is requested to be drawn over a [CanvasItem](class_canvasitem.md#class-canvasitem), with the top-left offset specified in `pos`. `modulate` specifies a multiplier for the colors being drawn, while `transpose` specifies whether drawing should be performed in column-major order instead of row-major order (resulting in 90-degree clockwise rotation).

**Note:** This is only used in 2D rendering, not 3D.

---


<a id="class-texture2d-private-method-draw-rect"></a>

void **_draw_rect**(to_canvas_item: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2), tile: [bool](class_bool.md#class-bool), modulate: [Color](class_color.md#class-color), transpose: [bool](class_bool.md#class-bool)) virtual const [🔗](class_texture2d.md#class-texture2d-private-method-draw-rect)

Called when the **Texture2D** is requested to be drawn onto [CanvasItem](class_canvasitem.md#class-canvasitem)'s specified `rect`. `modulate` specifies a multiplier for the colors being drawn, while `transpose` specifies whether drawing should be performed in column-major order instead of row-major order (resulting in 90-degree clockwise rotation).

**Note:** This is only used in 2D rendering, not 3D.

---


<a id="class-texture2d-private-method-draw-rect-region"></a>

void **_draw_rect_region**(to_canvas_item: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2), src_rect: [Rect2](class_rect2.md#class-rect2), modulate: [Color](class_color.md#class-color), transpose: [bool](class_bool.md#class-bool), clip_uv: [bool](class_bool.md#class-bool)) virtual const [🔗](class_texture2d.md#class-texture2d-private-method-draw-rect-region)

Called when a part of the **Texture2D** specified by `src_rect`'s coordinates is requested to be drawn onto [CanvasItem](class_canvasitem.md#class-canvasitem)'s specified `rect`. `modulate` specifies a multiplier for the colors being drawn, while `transpose` specifies whether drawing should be performed in column-major order instead of row-major order (resulting in 90-degree clockwise rotation).

**Note:** This is only used in 2D rendering, not 3D.

---


<a id="class-texture2d-private-method-get-format"></a>

[Format](class_image.md#enum-image-format) **_get_format**() virtual const [🔗](class_texture2d.md#class-texture2d-private-method-get-format)

Called when [get_format()](class_texture2d.md#class-texture2d-method-get-format) is called.

---


<a id="class-texture2d-private-method-get-height"></a>

[int](class_int.md#class-int) **_get_height**() virtual required const [🔗](class_texture2d.md#class-texture2d-private-method-get-height)

Called when the **Texture2D**'s height is queried.

---


<a id="class-texture2d-private-method-get-image"></a>

[Image](class_image.md#class-image) **_get_image**() virtual const [🔗](class_texture2d.md#class-texture2d-private-method-get-image)

Called when [get_image()](class_texture2d.md#class-texture2d-method-get-image) is called.

---


<a id="class-texture2d-private-method-get-mipmap-count"></a>

[int](class_int.md#class-int) **_get_mipmap_count**() virtual const [🔗](class_texture2d.md#class-texture2d-private-method-get-mipmap-count)

Called when [get_mipmap_count()](class_texture2d.md#class-texture2d-method-get-mipmap-count) is called.

---


<a id="class-texture2d-private-method-get-width"></a>

[int](class_int.md#class-int) **_get_width**() virtual required const [🔗](class_texture2d.md#class-texture2d-private-method-get-width)

Called when the **Texture2D**'s width is queried.

---


<a id="class-texture2d-private-method-has-alpha"></a>

[bool](class_bool.md#class-bool) **_has_alpha**() virtual const [🔗](class_texture2d.md#class-texture2d-private-method-has-alpha)

Called when the presence of an alpha channel in the **Texture2D** is queried.

---


<a id="class-texture2d-private-method-has-mipmaps"></a>

[bool](class_bool.md#class-bool) **_has_mipmaps**() virtual const [🔗](class_texture2d.md#class-texture2d-private-method-has-mipmaps)

Called when [has_mipmaps()](class_texture2d.md#class-texture2d-method-has-mipmaps) is called.

---


<a id="class-texture2d-private-method-is-pixel-opaque"></a>

[bool](class_bool.md#class-bool) **_is_pixel_opaque**(x: [int](class_int.md#class-int), y: [int](class_int.md#class-int)) virtual const [🔗](class_texture2d.md#class-texture2d-private-method-is-pixel-opaque)

Called when a pixel's opaque state in the **Texture2D** is queried at the specified `(x, y)` position.

---


<a id="class-texture2d-method-create-placeholder"></a>

[Resource](class_resource.md#class-resource) **create_placeholder**() const [🔗](class_texture2d.md#class-texture2d-method-create-placeholder)

Creates a placeholder version of this resource ([PlaceholderTexture2D](class_placeholdertexture2d.md#class-placeholdertexture2d)).

---


<a id="class-texture2d-method-draw"></a>

void **draw**(canvas_item: [RID](class_rid.md#class-rid), position: [Vector2](class_vector2.md#class-vector2), modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), transpose: [bool](class_bool.md#class-bool) = false) const [🔗](class_texture2d.md#class-texture2d-method-draw)

Draws the texture using a [CanvasItem](class_canvasitem.md#class-canvasitem) with the [RenderingServer](class_renderingserver.md#class-renderingserver) API at the specified `position`.

---


<a id="class-texture2d-method-draw-rect"></a>

void **draw_rect**(canvas_item: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2), tile: [bool](class_bool.md#class-bool), modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), transpose: [bool](class_bool.md#class-bool) = false) const [🔗](class_texture2d.md#class-texture2d-method-draw-rect)

Draws the texture using a [CanvasItem](class_canvasitem.md#class-canvasitem) with the [RenderingServer](class_renderingserver.md#class-renderingserver) API.

---


<a id="class-texture2d-method-draw-rect-region"></a>

void **draw_rect_region**(canvas_item: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2), src_rect: [Rect2](class_rect2.md#class-rect2), modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), transpose: [bool](class_bool.md#class-bool) = false, clip_uv: [bool](class_bool.md#class-bool) = true) const [🔗](class_texture2d.md#class-texture2d-method-draw-rect-region)

Draws a part of the texture using a [CanvasItem](class_canvasitem.md#class-canvasitem) with the [RenderingServer](class_renderingserver.md#class-renderingserver) API.

---


<a id="class-texture2d-method-get-format"></a>

[Format](class_image.md#enum-image-format) **get_format**() const [🔗](class_texture2d.md#class-texture2d-method-get-format)

Returns the image format of the texture.

---


<a id="class-texture2d-method-get-height"></a>

[int](class_int.md#class-int) **get_height**() const [🔗](class_texture2d.md#class-texture2d-method-get-height)

Returns the texture height in pixels.

---


<a id="class-texture2d-method-get-image"></a>

[Image](class_image.md#class-image) **get_image**() const [🔗](class_texture2d.md#class-texture2d-method-get-image)

Returns an [Image](class_image.md#class-image) that is a copy of data from this **Texture2D** (a new [Image](class_image.md#class-image) is created each time). [Image](class_image.md#class-image)s can be accessed and manipulated directly.

**Note:** This will return `null` if this **Texture2D** is invalid.

**Note:** This will fetch the texture data from the GPU, which might cause performance problems when overused. Avoid calling [get_image()](class_texture2d.md#class-texture2d-method-get-image) every frame, especially on large textures.

---


<a id="class-texture2d-method-get-mipmap-count"></a>

[int](class_int.md#class-int) **get_mipmap_count**() const [🔗](class_texture2d.md#class-texture2d-method-get-mipmap-count)

Returns the number of mipmaps of the texture.

---


<a id="class-texture2d-method-get-size"></a>

[Vector2](class_vector2.md#class-vector2) **get_size**() const [🔗](class_texture2d.md#class-texture2d-method-get-size)

Returns the texture size in pixels.

---


<a id="class-texture2d-method-get-width"></a>

[int](class_int.md#class-int) **get_width**() const [🔗](class_texture2d.md#class-texture2d-method-get-width)

Returns the texture width in pixels.

---


<a id="class-texture2d-method-has-alpha"></a>

[bool](class_bool.md#class-bool) **has_alpha**() const [🔗](class_texture2d.md#class-texture2d-method-has-alpha)

Returns `true` if this **Texture2D** has an alpha channel.

---


<a id="class-texture2d-method-has-mipmaps"></a>

[bool](class_bool.md#class-bool) **has_mipmaps**() const [🔗](class_texture2d.md#class-texture2d-method-has-mipmaps)

Returns `true` if the texture has mipmaps.
