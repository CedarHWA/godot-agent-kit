> Source: https://docs.godotengine.org/en/4.7/classes/class_canvasitem.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="canvasitem"></a>

<a id="class-canvasitem"></a>

# CanvasItem

**Inherits:** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [Control](class_control.md#class-control), [Node2D](class_node2d.md#class-node2d)

Abstract base class for everything in 2D space.

<a id="description"></a>

## Description

Abstract base class for everything in 2D space. Canvas items are laid out in a tree; children inherit and extend their parent's transform. **CanvasItem** is extended by [Control](class_control.md#class-control) for GUI-related nodes, and by [Node2D](class_node2d.md#class-node2d) for 2D game objects.

Any **CanvasItem** can draw. For this, [queue_redraw()](class_canvasitem.md#class-canvasitem-method-queue-redraw) is called by the engine, then [NOTIFICATION_DRAW](class_canvasitem.md#class-canvasitem-constant-notification-draw) will be received on idle time to request a redraw. Because of this, canvas items don't need to be redrawn on every frame, improving the performance significantly. Several functions for drawing on the **CanvasItem** are provided (see `draw_*` functions). However, they can only be used inside [_draw()](class_canvasitem.md#class-canvasitem-private-method-draw), its corresponding [Object._notification()](class_object.md#class-object-private-method-notification) or methods connected to the [draw](class_canvasitem.md#class-canvasitem-signal-draw) signal.

Canvas items are drawn in tree order on their canvas layer. By default, children are on top of their parents, so a root **CanvasItem** will be drawn behind everything. This behavior can be changed on a per-item basis.

A **CanvasItem** can be hidden, which will also hide its children. By adjusting various other properties of a **CanvasItem**, you can also modulate its color (via [modulate](class_canvasitem.md#class-canvasitem-property-modulate) or [self_modulate](class_canvasitem.md#class-canvasitem-property-self-modulate)), change its Z-index, blend mode, and more.

Note that properties like transform, modulation, and visibility are only propagated to *direct* **CanvasItem** child nodes. If there is a non-**CanvasItem** node in between, like [Node](class_node.md#class-node) or [AnimationPlayer](class_animationplayer.md#class-animationplayer), the **CanvasItem** nodes below will have an independent position and [modulate](class_canvasitem.md#class-canvasitem-property-modulate) chain. See also [top_level](class_canvasitem.md#class-canvasitem-property-top-level).

<a id="tutorials"></a>

## Tutorials

- [Viewport and canvas transforms](../tutorials/2d/2d_transforms.md)
- [Custom drawing in 2D](../tutorials/2d/custom_drawing_in_2d.md)
- [Audio Spectrum Visualizer Demo](https://godotengine.org/asset-library/asset/2762)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [ClipChildrenMode](class_canvasitem.md#enum-canvasitem-clipchildrenmode) | [clip_children](class_canvasitem.md#class-canvasitem-property-clip-children) | `0` |
| [int](class_int.md#class-int) | [light_mask](class_canvasitem.md#class-canvasitem-property-light-mask) | `1` |
| [Material](class_material.md#class-material) | [material](class_canvasitem.md#class-canvasitem-property-material) |  |
| [Color](class_color.md#class-color) | [modulate](class_canvasitem.md#class-canvasitem-property-modulate) | `Color(1, 1, 1, 1)` |
| [OversamplingWithScale](class_canvasitem.md#enum-canvasitem-oversamplingwithscale) | [oversampling_with_scale](class_canvasitem.md#class-canvasitem-property-oversampling-with-scale) | `0` |
| [Color](class_color.md#class-color) | [self_modulate](class_canvasitem.md#class-canvasitem-property-self-modulate) | `Color(1, 1, 1, 1)` |
| [bool](class_bool.md#class-bool) | [show_behind_parent](class_canvasitem.md#class-canvasitem-property-show-behind-parent) | `false` |
| [TextureFilter](class_canvasitem.md#enum-canvasitem-texturefilter) | [texture_filter](class_canvasitem.md#class-canvasitem-property-texture-filter) | `0` |
| [TextureRepeat](class_canvasitem.md#enum-canvasitem-texturerepeat) | [texture_repeat](class_canvasitem.md#class-canvasitem-property-texture-repeat) | `0` |
| [bool](class_bool.md#class-bool) | [top_level](class_canvasitem.md#class-canvasitem-property-top-level) | `false` |
| [bool](class_bool.md#class-bool) | [use_parent_material](class_canvasitem.md#class-canvasitem-property-use-parent-material) | `false` |
| [int](class_int.md#class-int) | [visibility_layer](class_canvasitem.md#class-canvasitem-property-visibility-layer) | `1` |
| [bool](class_bool.md#class-bool) | [visible](class_canvasitem.md#class-canvasitem-property-visible) | `true` |
| [bool](class_bool.md#class-bool) | [y_sort_enabled](class_canvasitem.md#class-canvasitem-property-y-sort-enabled) | `false` |
| [bool](class_bool.md#class-bool) | [z_as_relative](class_canvasitem.md#class-canvasitem-property-z-as-relative) | `true` |
| [int](class_int.md#class-int) | [z_index](class_canvasitem.md#class-canvasitem-property-z-index) | `0` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [_draw](class_canvasitem.md#class-canvasitem-private-method-draw)() virtual |
| void | [draw_animation_slice](class_canvasitem.md#class-canvasitem-method-draw-animation-slice)(animation_length: [float](class_float.md#class-float), slice_begin: [float](class_float.md#class-float), slice_end: [float](class_float.md#class-float), offset: [float](class_float.md#class-float) = 0.0) |
| void | [draw_arc](class_canvasitem.md#class-canvasitem-method-draw-arc)(center: [Vector2](class_vector2.md#class-vector2), radius: [float](class_float.md#class-float), start_angle: [float](class_float.md#class-float), end_angle: [float](class_float.md#class-float), point_count: [int](class_int.md#class-int), color: [Color](class_color.md#class-color), width: [float](class_float.md#class-float) = -1.0, antialiased: [bool](class_bool.md#class-bool) = false) |
| void | [draw_char](class_canvasitem.md#class-canvasitem-method-draw-char)(font: [Font](class_font.md#class-font), pos: [Vector2](class_vector2.md#class-vector2), char: [String](class_string.md#class-string), font_size: [int](class_int.md#class-int) = 16, modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0) const |
| void | [draw_char_outline](class_canvasitem.md#class-canvasitem-method-draw-char-outline)(font: [Font](class_font.md#class-font), pos: [Vector2](class_vector2.md#class-vector2), char: [String](class_string.md#class-string), font_size: [int](class_int.md#class-int) = 16, size: [int](class_int.md#class-int) = -1, modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0) const |
| void | [draw_circle](class_canvasitem.md#class-canvasitem-method-draw-circle)(position: [Vector2](class_vector2.md#class-vector2), radius: [float](class_float.md#class-float), color: [Color](class_color.md#class-color), filled: [bool](class_bool.md#class-bool) = true, width: [float](class_float.md#class-float) = -1.0, antialiased: [bool](class_bool.md#class-bool) = false) |
| void | [draw_colored_polygon](class_canvasitem.md#class-canvasitem-method-draw-colored-polygon)(points: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), color: [Color](class_color.md#class-color), uvs: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) = PackedVector2Array(), texture: [Texture2D](class_texture2d.md#class-texture2d) = null) |
| void | [draw_dashed_line](class_canvasitem.md#class-canvasitem-method-draw-dashed-line)(from: [Vector2](class_vector2.md#class-vector2), to: [Vector2](class_vector2.md#class-vector2), color: [Color](class_color.md#class-color), width: [float](class_float.md#class-float) = -1.0, dash: [float](class_float.md#class-float) = 2.0, aligned: [bool](class_bool.md#class-bool) = true, antialiased: [bool](class_bool.md#class-bool) = false) |
| void | [draw_ellipse](class_canvasitem.md#class-canvasitem-method-draw-ellipse)(position: [Vector2](class_vector2.md#class-vector2), major: [float](class_float.md#class-float), minor: [float](class_float.md#class-float), color: [Color](class_color.md#class-color), filled: [bool](class_bool.md#class-bool) = true, width: [float](class_float.md#class-float) = -1.0, antialiased: [bool](class_bool.md#class-bool) = false) |
| void | [draw_ellipse_arc](class_canvasitem.md#class-canvasitem-method-draw-ellipse-arc)(center: [Vector2](class_vector2.md#class-vector2), major: [float](class_float.md#class-float), minor: [float](class_float.md#class-float), start_angle: [float](class_float.md#class-float), end_angle: [float](class_float.md#class-float), point_count: [int](class_int.md#class-int), color: [Color](class_color.md#class-color), width: [float](class_float.md#class-float) = -1.0, antialiased: [bool](class_bool.md#class-bool) = false) |
| void | [draw_end_animation](class_canvasitem.md#class-canvasitem-method-draw-end-animation)() |
| void | [draw_lcd_texture_rect_region](class_canvasitem.md#class-canvasitem-method-draw-lcd-texture-rect-region)(texture: [Texture2D](class_texture2d.md#class-texture2d), rect: [Rect2](class_rect2.md#class-rect2), src_rect: [Rect2](class_rect2.md#class-rect2), modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1)) |
| void | [draw_line](class_canvasitem.md#class-canvasitem-method-draw-line)(from: [Vector2](class_vector2.md#class-vector2), to: [Vector2](class_vector2.md#class-vector2), color: [Color](class_color.md#class-color), width: [float](class_float.md#class-float) = -1.0, antialiased: [bool](class_bool.md#class-bool) = false) |
| void | [draw_mesh](class_canvasitem.md#class-canvasitem-method-draw-mesh)(mesh: [Mesh](class_mesh.md#class-mesh), texture: [Texture2D](class_texture2d.md#class-texture2d), transform: [Transform2D](class_transform2d.md#class-transform2d) = Transform2D(1, 0, 0, 1, 0, 0), modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1)) |
| void | [draw_msdf_texture_rect_region](class_canvasitem.md#class-canvasitem-method-draw-msdf-texture-rect-region)(texture: [Texture2D](class_texture2d.md#class-texture2d), rect: [Rect2](class_rect2.md#class-rect2), src_rect: [Rect2](class_rect2.md#class-rect2), modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), outline: [float](class_float.md#class-float) = 0.0, pixel_range: [float](class_float.md#class-float) = 4.0, scale: [float](class_float.md#class-float) = 1.0) |
| void | [draw_multiline](class_canvasitem.md#class-canvasitem-method-draw-multiline)(points: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), color: [Color](class_color.md#class-color), width: [float](class_float.md#class-float) = -1.0, antialiased: [bool](class_bool.md#class-bool) = false) |
| void | [draw_multiline_colors](class_canvasitem.md#class-canvasitem-method-draw-multiline-colors)(points: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), colors: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray), width: [float](class_float.md#class-float) = -1.0, antialiased: [bool](class_bool.md#class-bool) = false) |
| void | [draw_multiline_string](class_canvasitem.md#class-canvasitem-method-draw-multiline-string)(font: [Font](class_font.md#class-font), pos: [Vector2](class_vector2.md#class-vector2), text: [String](class_string.md#class-string), alignment: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) = 0, width: [float](class_float.md#class-float) = -1, font_size: [int](class_int.md#class-int) = 16, max_lines: [int](class_int.md#class-int) = -1, modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), brk_flags: BitField[[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)] = 3, justification_flags: BitField[[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] = 3, direction: [Direction](class_textserver.md#enum-textserver-direction) = 0, orientation: [Orientation](class_textserver.md#enum-textserver-orientation) = 0, oversampling: [float](class_float.md#class-float) = 0.0) const |
| void | [draw_multiline_string_outline](class_canvasitem.md#class-canvasitem-method-draw-multiline-string-outline)(font: [Font](class_font.md#class-font), pos: [Vector2](class_vector2.md#class-vector2), text: [String](class_string.md#class-string), alignment: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) = 0, width: [float](class_float.md#class-float) = -1, font_size: [int](class_int.md#class-int) = 16, max_lines: [int](class_int.md#class-int) = -1, size: [int](class_int.md#class-int) = 1, modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), brk_flags: BitField[[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)] = 3, justification_flags: BitField[[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] = 3, direction: [Direction](class_textserver.md#enum-textserver-direction) = 0, orientation: [Orientation](class_textserver.md#enum-textserver-orientation) = 0, oversampling: [float](class_float.md#class-float) = 0.0) const |
| void | [draw_multimesh](class_canvasitem.md#class-canvasitem-method-draw-multimesh)(multimesh: [MultiMesh](class_multimesh.md#class-multimesh), texture: [Texture2D](class_texture2d.md#class-texture2d)) |
| void | [draw_polygon](class_canvasitem.md#class-canvasitem-method-draw-polygon)(points: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), colors: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray), uvs: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) = PackedVector2Array(), texture: [Texture2D](class_texture2d.md#class-texture2d) = null) |
| void | [draw_polyline](class_canvasitem.md#class-canvasitem-method-draw-polyline)(points: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), color: [Color](class_color.md#class-color), width: [float](class_float.md#class-float) = -1.0, antialiased: [bool](class_bool.md#class-bool) = false) |
| void | [draw_polyline_colors](class_canvasitem.md#class-canvasitem-method-draw-polyline-colors)(points: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), colors: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray), width: [float](class_float.md#class-float) = -1.0, antialiased: [bool](class_bool.md#class-bool) = false) |
| void | [draw_primitive](class_canvasitem.md#class-canvasitem-method-draw-primitive)(points: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), colors: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray), uvs: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), texture: [Texture2D](class_texture2d.md#class-texture2d) = null) |
| void | [draw_rect](class_canvasitem.md#class-canvasitem-method-draw-rect)(rect: [Rect2](class_rect2.md#class-rect2), color: [Color](class_color.md#class-color), filled: [bool](class_bool.md#class-bool) = true, width: [float](class_float.md#class-float) = -1.0, antialiased: [bool](class_bool.md#class-bool) = false) |
| void | [draw_set_transform](class_canvasitem.md#class-canvasitem-method-draw-set-transform)(position: [Vector2](class_vector2.md#class-vector2), rotation: [float](class_float.md#class-float) = 0.0, scale: [Vector2](class_vector2.md#class-vector2) = Vector2(1, 1)) |
| void | [draw_set_transform_matrix](class_canvasitem.md#class-canvasitem-method-draw-set-transform-matrix)(xform: [Transform2D](class_transform2d.md#class-transform2d)) |
| void | [draw_string](class_canvasitem.md#class-canvasitem-method-draw-string)(font: [Font](class_font.md#class-font), pos: [Vector2](class_vector2.md#class-vector2), text: [String](class_string.md#class-string), alignment: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) = 0, width: [float](class_float.md#class-float) = -1, font_size: [int](class_int.md#class-int) = 16, modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), justification_flags: BitField[[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] = 3, direction: [Direction](class_textserver.md#enum-textserver-direction) = 0, orientation: [Orientation](class_textserver.md#enum-textserver-orientation) = 0, oversampling: [float](class_float.md#class-float) = 0.0) const |
| void | [draw_string_outline](class_canvasitem.md#class-canvasitem-method-draw-string-outline)(font: [Font](class_font.md#class-font), pos: [Vector2](class_vector2.md#class-vector2), text: [String](class_string.md#class-string), alignment: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) = 0, width: [float](class_float.md#class-float) = -1, font_size: [int](class_int.md#class-int) = 16, size: [int](class_int.md#class-int) = 1, modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), justification_flags: BitField[[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] = 3, direction: [Direction](class_textserver.md#enum-textserver-direction) = 0, orientation: [Orientation](class_textserver.md#enum-textserver-orientation) = 0, oversampling: [float](class_float.md#class-float) = 0.0) const |
| void | [draw_style_box](class_canvasitem.md#class-canvasitem-method-draw-style-box)(style_box: [StyleBox](class_stylebox.md#class-stylebox), rect: [Rect2](class_rect2.md#class-rect2)) |
| void | [draw_texture](class_canvasitem.md#class-canvasitem-method-draw-texture)(texture: [Texture2D](class_texture2d.md#class-texture2d), position: [Vector2](class_vector2.md#class-vector2), modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1)) |
| void | [draw_texture_rect](class_canvasitem.md#class-canvasitem-method-draw-texture-rect)(texture: [Texture2D](class_texture2d.md#class-texture2d), rect: [Rect2](class_rect2.md#class-rect2), tile: [bool](class_bool.md#class-bool), modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), transpose: [bool](class_bool.md#class-bool) = false) |
| void | [draw_texture_rect_region](class_canvasitem.md#class-canvasitem-method-draw-texture-rect-region)(texture: [Texture2D](class_texture2d.md#class-texture2d), rect: [Rect2](class_rect2.md#class-rect2), src_rect: [Rect2](class_rect2.md#class-rect2), modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), transpose: [bool](class_bool.md#class-bool) = false, clip_uv: [bool](class_bool.md#class-bool) = true) |
| void | [force_update_transform](class_canvasitem.md#class-canvasitem-method-force-update-transform)() |
| [RID](class_rid.md#class-rid) | [get_canvas](class_canvasitem.md#class-canvasitem-method-get-canvas)() const |
| [RID](class_rid.md#class-rid) | [get_canvas_item](class_canvasitem.md#class-canvasitem-method-get-canvas-item)() const |
| [CanvasLayer](class_canvaslayer.md#class-canvaslayer) | [get_canvas_layer_node](class_canvasitem.md#class-canvasitem-method-get-canvas-layer-node)() const |
| [Transform2D](class_transform2d.md#class-transform2d) | [get_canvas_transform](class_canvasitem.md#class-canvasitem-method-get-canvas-transform)() const |
| [Vector2](class_vector2.md#class-vector2) | [get_global_mouse_position](class_canvasitem.md#class-canvasitem-method-get-global-mouse-position)() const |
| [Transform2D](class_transform2d.md#class-transform2d) | [get_global_transform](class_canvasitem.md#class-canvasitem-method-get-global-transform)() const |
| [Transform2D](class_transform2d.md#class-transform2d) | [get_global_transform_with_canvas](class_canvasitem.md#class-canvasitem-method-get-global-transform-with-canvas)() const |
| [Variant](class_variant.md#class-variant) | [get_instance_shader_parameter](class_canvasitem.md#class-canvasitem-method-get-instance-shader-parameter)(name: [StringName](class_stringname.md#class-stringname)) const |
| [Vector2](class_vector2.md#class-vector2) | [get_local_mouse_position](class_canvasitem.md#class-canvasitem-method-get-local-mouse-position)() const |
| [Transform2D](class_transform2d.md#class-transform2d) | [get_screen_transform](class_canvasitem.md#class-canvasitem-method-get-screen-transform)() const |
| [Transform2D](class_transform2d.md#class-transform2d) | [get_transform](class_canvasitem.md#class-canvasitem-method-get-transform)() const |
| [Rect2](class_rect2.md#class-rect2) | [get_viewport_rect](class_canvasitem.md#class-canvasitem-method-get-viewport-rect)() const |
| [Transform2D](class_transform2d.md#class-transform2d) | [get_viewport_transform](class_canvasitem.md#class-canvasitem-method-get-viewport-transform)() const |
| [bool](class_bool.md#class-bool) | [get_visibility_layer_bit](class_canvasitem.md#class-canvasitem-method-get-visibility-layer-bit)(layer: [int](class_int.md#class-int)) const |
| [World2D](class_world2d.md#class-world2d) | [get_world_2d](class_canvasitem.md#class-canvasitem-method-get-world-2d)() const |
| void | [hide](class_canvasitem.md#class-canvasitem-method-hide)() |
| [bool](class_bool.md#class-bool) | [is_local_transform_notification_enabled](class_canvasitem.md#class-canvasitem-method-is-local-transform-notification-enabled)() const |
| [bool](class_bool.md#class-bool) | [is_transform_notification_enabled](class_canvasitem.md#class-canvasitem-method-is-transform-notification-enabled)() const |
| [bool](class_bool.md#class-bool) | [is_visible_in_tree](class_canvasitem.md#class-canvasitem-method-is-visible-in-tree)() const |
| [Vector2](class_vector2.md#class-vector2) | [make_canvas_position_local](class_canvasitem.md#class-canvasitem-method-make-canvas-position-local)(viewport_point: [Vector2](class_vector2.md#class-vector2)) const |
| [InputEvent](class_inputevent.md#class-inputevent) | [make_input_local](class_canvasitem.md#class-canvasitem-method-make-input-local)(event: [InputEvent](class_inputevent.md#class-inputevent)) const |
| void | [move_to_front](class_canvasitem.md#class-canvasitem-method-move-to-front)() |
| void | [queue_redraw](class_canvasitem.md#class-canvasitem-method-queue-redraw)() |
| void | [set_instance_shader_parameter](class_canvasitem.md#class-canvasitem-method-set-instance-shader-parameter)(name: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant)) |
| void | [set_notify_local_transform](class_canvasitem.md#class-canvasitem-method-set-notify-local-transform)(enable: [bool](class_bool.md#class-bool)) |
| void | [set_notify_transform](class_canvasitem.md#class-canvasitem-method-set-notify-transform)(enable: [bool](class_bool.md#class-bool)) |
| void | [set_visibility_layer_bit](class_canvasitem.md#class-canvasitem-method-set-visibility-layer-bit)(layer: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool)) |
| void | [show](class_canvasitem.md#class-canvasitem-method-show)() |

---


<a id="signals"></a>

## Signals

<a id="class-canvasitem-signal-draw"></a>

**draw**() [🔗](class_canvasitem.md#class-canvasitem-signal-draw)

Emitted when the **CanvasItem** must redraw, *after* the related [NOTIFICATION_DRAW](class_canvasitem.md#class-canvasitem-constant-notification-draw) notification, and *before* [_draw()](class_canvasitem.md#class-canvasitem-private-method-draw) is called.

**Note:** Deferred connections do not allow drawing through the `draw_*` methods.

---


<a id="class-canvasitem-signal-hidden"></a>

**hidden**() [🔗](class_canvasitem.md#class-canvasitem-signal-hidden)

Emitted when this node becomes hidden, i.e. it's no longer visible in the tree (see [is_visible_in_tree()](class_canvasitem.md#class-canvasitem-method-is-visible-in-tree)).

---


<a id="class-canvasitem-signal-item-rect-changed"></a>

**item_rect_changed**() [🔗](class_canvasitem.md#class-canvasitem-signal-item-rect-changed)

Emitted when the **CanvasItem**'s boundaries (position or size) change, or when an action took place that may have affected these boundaries (e.g. changing [Sprite2D.texture](class_sprite2d.md#class-sprite2d-property-texture)).

---


<a id="class-canvasitem-signal-visibility-changed"></a>

**visibility_changed**() [🔗](class_canvasitem.md#class-canvasitem-signal-visibility-changed)

Emitted when the **CanvasItem**'s visibility changes, either because its own [visible](class_canvasitem.md#class-canvasitem-property-visible) property changed or because its visibility in the tree changed (see [is_visible_in_tree()](class_canvasitem.md#class-canvasitem-method-is-visible-in-tree)).

This signal is emitted *after* the related [NOTIFICATION_VISIBILITY_CHANGED](class_canvasitem.md#class-canvasitem-constant-notification-visibility-changed) notification.

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-canvasitem-texturefilter"></a>

enum **TextureFilter**: [🔗](class_canvasitem.md#enum-canvasitem-texturefilter)

<a id="class-canvasitem-constant-texture-filter-parent-node"></a>

[TextureFilter](class_canvasitem.md#enum-canvasitem-texturefilter) **TEXTURE_FILTER_PARENT_NODE** = `0`

The **CanvasItem** will inherit the filter from its parent.

<a id="class-canvasitem-constant-texture-filter-nearest"></a>

[TextureFilter](class_canvasitem.md#enum-canvasitem-texturefilter) **TEXTURE_FILTER_NEAREST** = `1`

The texture filter reads from the nearest pixel only. This makes the texture look pixelated from up close, and grainy from a distance (due to mipmaps not being sampled).

<a id="class-canvasitem-constant-texture-filter-linear"></a>

[TextureFilter](class_canvasitem.md#enum-canvasitem-texturefilter) **TEXTURE_FILTER_LINEAR** = `2`

The texture filter blends between the nearest 4 pixels. This makes the texture look smooth from up close, and grainy from a distance (due to mipmaps not being sampled).

<a id="class-canvasitem-constant-texture-filter-nearest-with-mipmaps"></a>

[TextureFilter](class_canvasitem.md#enum-canvasitem-texturefilter) **TEXTURE_FILTER_NEAREST_WITH_MIPMAPS** = `3`

The texture filter reads from the nearest pixel and blends between the nearest 2 mipmaps (or uses the nearest mipmap if [ProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filter](class_projectsettings.md#class-projectsettings-property-rendering-textures-default-filters-use-nearest-mipmap-filter) is `true`). This makes the texture look pixelated from up close, and smooth from a distance.

Use this for non-pixel art textures that may be viewed at a low scale (e.g. due to [Camera2D](class_camera2d.md#class-camera2d) zoom or sprite scaling), as mipmaps are important to smooth out pixels that are smaller than on-screen pixels.

<a id="class-canvasitem-constant-texture-filter-linear-with-mipmaps"></a>

[TextureFilter](class_canvasitem.md#enum-canvasitem-texturefilter) **TEXTURE_FILTER_LINEAR_WITH_MIPMAPS** = `4`

The texture filter blends between the nearest 4 pixels and between the nearest 2 mipmaps (or uses the nearest mipmap if [ProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filter](class_projectsettings.md#class-projectsettings-property-rendering-textures-default-filters-use-nearest-mipmap-filter) is `true`). This makes the texture look smooth from up close, and smooth from a distance.

Use this for non-pixel art textures that may be viewed at a low scale (e.g. due to [Camera2D](class_camera2d.md#class-camera2d) zoom or sprite scaling), as mipmaps are important to smooth out pixels that are smaller than on-screen pixels.

<a id="class-canvasitem-constant-texture-filter-nearest-with-mipmaps-anisotropic"></a>

[TextureFilter](class_canvasitem.md#enum-canvasitem-texturefilter) **TEXTURE_FILTER_NEAREST_WITH_MIPMAPS_ANISOTROPIC** = `5`

The texture filter reads from the nearest pixel and blends between 2 mipmaps (or uses the nearest mipmap if [ProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filter](class_projectsettings.md#class-projectsettings-property-rendering-textures-default-filters-use-nearest-mipmap-filter) is `true`) based on the angle between the surface and the camera view. This makes the texture look pixelated from up close, and smooth from a distance. Anisotropic filtering improves texture quality on surfaces that are almost in line with the camera, but is slightly slower. The anisotropic filtering level can be changed by adjusting [ProjectSettings.rendering/textures/default_filters/anisotropic_filtering_level](class_projectsettings.md#class-projectsettings-property-rendering-textures-default-filters-anisotropic-filtering-level).

**Note:** This texture filter is rarely useful in 2D projects. [TEXTURE_FILTER_NEAREST_WITH_MIPMAPS](class_canvasitem.md#class-canvasitem-constant-texture-filter-nearest-with-mipmaps) is usually more appropriate in this case.

<a id="class-canvasitem-constant-texture-filter-linear-with-mipmaps-anisotropic"></a>

[TextureFilter](class_canvasitem.md#enum-canvasitem-texturefilter) **TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC** = `6`

The texture filter blends between the nearest 4 pixels and blends between 2 mipmaps (or uses the nearest mipmap if [ProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filter](class_projectsettings.md#class-projectsettings-property-rendering-textures-default-filters-use-nearest-mipmap-filter) is `true`) based on the angle between the surface and the camera view. This makes the texture look smooth from up close, and smooth from a distance. Anisotropic filtering improves texture quality on surfaces that are almost in line with the camera, but is slightly slower. The anisotropic filtering level can be changed by adjusting [ProjectSettings.rendering/textures/default_filters/anisotropic_filtering_level](class_projectsettings.md#class-projectsettings-property-rendering-textures-default-filters-anisotropic-filtering-level).

**Note:** This texture filter is rarely useful in 2D projects. [TEXTURE_FILTER_LINEAR_WITH_MIPMAPS](class_canvasitem.md#class-canvasitem-constant-texture-filter-linear-with-mipmaps) is usually more appropriate in this case.

<a id="class-canvasitem-constant-texture-filter-max"></a>

[TextureFilter](class_canvasitem.md#enum-canvasitem-texturefilter) **TEXTURE_FILTER_MAX** = `7`

Represents the size of the [TextureFilter](class_canvasitem.md#enum-canvasitem-texturefilter) enum.

---


<a id="enum-canvasitem-texturerepeat"></a>

enum **TextureRepeat**: [🔗](class_canvasitem.md#enum-canvasitem-texturerepeat)

<a id="class-canvasitem-constant-texture-repeat-parent-node"></a>

[TextureRepeat](class_canvasitem.md#enum-canvasitem-texturerepeat) **TEXTURE_REPEAT_PARENT_NODE** = `0`

The **CanvasItem** will inherit the repeat mode from its parent.

<a id="class-canvasitem-constant-texture-repeat-disabled"></a>

[TextureRepeat](class_canvasitem.md#enum-canvasitem-texturerepeat) **TEXTURE_REPEAT_DISABLED** = `1`

The texture does not repeat. Sampling the texture outside its extents will result in "stretching" of the edge pixels. You can avoid this by ensuring a 1-pixel fully transparent border on each side of the texture.

<a id="class-canvasitem-constant-texture-repeat-enabled"></a>

[TextureRepeat](class_canvasitem.md#enum-canvasitem-texturerepeat) **TEXTURE_REPEAT_ENABLED** = `2`

The texture repeats when exceeding the texture's size.

<a id="class-canvasitem-constant-texture-repeat-mirror"></a>

[TextureRepeat](class_canvasitem.md#enum-canvasitem-texturerepeat) **TEXTURE_REPEAT_MIRROR** = `3`

The texture repeats when the exceeding the texture's size in a "2×2 tiled mode". Repeated textures at even positions are mirrored.

<a id="class-canvasitem-constant-texture-repeat-max"></a>

[TextureRepeat](class_canvasitem.md#enum-canvasitem-texturerepeat) **TEXTURE_REPEAT_MAX** = `4`

Represents the size of the [TextureRepeat](class_canvasitem.md#enum-canvasitem-texturerepeat) enum.

---


<a id="enum-canvasitem-clipchildrenmode"></a>

enum **ClipChildrenMode**: [🔗](class_canvasitem.md#enum-canvasitem-clipchildrenmode)

<a id="class-canvasitem-constant-clip-children-disabled"></a>

[ClipChildrenMode](class_canvasitem.md#enum-canvasitem-clipchildrenmode) **CLIP_CHILDREN_DISABLED** = `0`

Children are drawn over this node and are not clipped.

<a id="class-canvasitem-constant-clip-children-only"></a>

[ClipChildrenMode](class_canvasitem.md#enum-canvasitem-clipchildrenmode) **CLIP_CHILDREN_ONLY** = `1`

This node is used as a mask and is **not** drawn. The mask is based on this node's alpha channel: Opaque pixels are kept, transparent pixels are discarded, and semi-transparent pixels are blended in according to their opacity. Children are clipped to this node's drawn area.

<a id="class-canvasitem-constant-clip-children-and-draw"></a>

[ClipChildrenMode](class_canvasitem.md#enum-canvasitem-clipchildrenmode) **CLIP_CHILDREN_AND_DRAW** = `2`

This node is used as a mask and is also drawn. The mask is based on this node's alpha channel: Opaque pixels are kept, transparent pixels are discarded, and semi-transparent pixels are blended in according to their opacity. Children are clipped to the parent's drawn area.

<a id="class-canvasitem-constant-clip-children-max"></a>

[ClipChildrenMode](class_canvasitem.md#enum-canvasitem-clipchildrenmode) **CLIP_CHILDREN_MAX** = `3`

Represents the size of the [ClipChildrenMode](class_canvasitem.md#enum-canvasitem-clipchildrenmode) enum.

---


<a id="enum-canvasitem-oversamplingwithscale"></a>

enum **OversamplingWithScale**: [🔗](class_canvasitem.md#enum-canvasitem-oversamplingwithscale)

<a id="class-canvasitem-constant-oversampling-with-scale-parent-node"></a>

[OversamplingWithScale](class_canvasitem.md#enum-canvasitem-oversamplingwithscale) **OVERSAMPLING_WITH_SCALE_PARENT_NODE** = `0`

The **CanvasItem** will inherit the oversampling mode from its parent.

<a id="class-canvasitem-constant-oversampling-with-scale-disabled"></a>

[OversamplingWithScale](class_canvasitem.md#enum-canvasitem-oversamplingwithscale) **OVERSAMPLING_WITH_SCALE_DISABLED** = `1`

The oversampling is not affected by **CanvasItem** scale, and is equal to the [Viewport](class_viewport.md#class-viewport) oversampling.

<a id="class-canvasitem-constant-oversampling-with-scale-enabled"></a>

[OversamplingWithScale](class_canvasitem.md#enum-canvasitem-oversamplingwithscale) **OVERSAMPLING_WITH_SCALE_ENABLED** = `2`

The oversampling is a product of **CanvasItem** scale and [Viewport](class_viewport.md#class-viewport) oversampling.

<a id="class-canvasitem-constant-oversampling-with-scale-max"></a>

[OversamplingWithScale](class_canvasitem.md#enum-canvasitem-oversamplingwithscale) **OVERSAMPLING_WITH_SCALE_MAX** = `3`

Represents the size of the [OversamplingWithScale](class_canvasitem.md#enum-canvasitem-oversamplingwithscale) enum.

---


<a id="constants"></a>

## Constants

<a id="class-canvasitem-constant-notification-transform-changed"></a>

**NOTIFICATION_TRANSFORM_CHANGED** = `2000` [🔗](class_canvasitem.md#class-canvasitem-constant-notification-transform-changed)

Notification received when this node's global transform changes, if [is_transform_notification_enabled()](class_canvasitem.md#class-canvasitem-method-is-transform-notification-enabled) is `true`. See also [set_notify_transform()](class_canvasitem.md#class-canvasitem-method-set-notify-transform) and [get_transform()](class_canvasitem.md#class-canvasitem-method-get-transform).

**Note:** Many canvas items such as [Camera2D](class_camera2d.md#class-camera2d) or [CollisionObject2D](class_collisionobject2d.md#class-collisionobject2d) automatically enable this in order to function correctly.

<a id="class-canvasitem-constant-notification-local-transform-changed"></a>

**NOTIFICATION_LOCAL_TRANSFORM_CHANGED** = `35` [🔗](class_canvasitem.md#class-canvasitem-constant-notification-local-transform-changed)

Notification received when this node's transform changes, if [is_local_transform_notification_enabled()](class_canvasitem.md#class-canvasitem-method-is-local-transform-notification-enabled) is `true`. This is not received when a parent [Node2D](class_node2d.md#class-node2d)'s transform changes. See also [set_notify_local_transform()](class_canvasitem.md#class-canvasitem-method-set-notify-local-transform).

**Note:** Many canvas items such as [Camera2D](class_camera2d.md#class-camera2d) or [CollisionShape2D](class_collisionshape2d.md#class-collisionshape2d) automatically enable this in order to function correctly.

<a id="class-canvasitem-constant-notification-draw"></a>

**NOTIFICATION_DRAW** = `30` [🔗](class_canvasitem.md#class-canvasitem-constant-notification-draw)

The **CanvasItem** is requested to draw (see [_draw()](class_canvasitem.md#class-canvasitem-private-method-draw)).

<a id="class-canvasitem-constant-notification-visibility-changed"></a>

**NOTIFICATION_VISIBILITY_CHANGED** = `31` [🔗](class_canvasitem.md#class-canvasitem-constant-notification-visibility-changed)

Notification received when this node's visibility changes (see [visible](class_canvasitem.md#class-canvasitem-property-visible) and [is_visible_in_tree()](class_canvasitem.md#class-canvasitem-method-is-visible-in-tree)).

This notification is received *before* the related [visibility_changed](class_canvasitem.md#class-canvasitem-signal-visibility-changed) signal.

<a id="class-canvasitem-constant-notification-enter-canvas"></a>

**NOTIFICATION_ENTER_CANVAS** = `32` [🔗](class_canvasitem.md#class-canvasitem-constant-notification-enter-canvas)

The **CanvasItem** has entered the canvas.

<a id="class-canvasitem-constant-notification-exit-canvas"></a>

**NOTIFICATION_EXIT_CANVAS** = `33` [🔗](class_canvasitem.md#class-canvasitem-constant-notification-exit-canvas)

The **CanvasItem** has exited the canvas.

This notification is sent in reversed order.

<a id="class-canvasitem-constant-notification-world-2d-changed"></a>

**NOTIFICATION_WORLD_2D_CHANGED** = `36` [🔗](class_canvasitem.md#class-canvasitem-constant-notification-world-2d-changed)

Notification received when this **CanvasItem** is registered to a new [World2D](class_world2d.md#class-world2d) (see [get_world_2d()](class_canvasitem.md#class-canvasitem-method-get-world-2d)).

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-canvasitem-property-clip-children"></a>

[ClipChildrenMode](class_canvasitem.md#enum-canvasitem-clipchildrenmode) **clip_children** = `0` [🔗](class_canvasitem.md#class-canvasitem-property-clip-children)

- void **set_clip_children_mode**(value: [ClipChildrenMode](class_canvasitem.md#enum-canvasitem-clipchildrenmode))
- [ClipChildrenMode](class_canvasitem.md#enum-canvasitem-clipchildrenmode) **get_clip_children_mode**()

The mode in which this node clips its children, acting as a mask.

**Note:** Clipping nodes cannot be nested or placed within a [CanvasGroup](class_canvasgroup.md#class-canvasgroup). If an ancestor of this node clips its children or is a [CanvasGroup](class_canvasgroup.md#class-canvasgroup), then this node's clip mode should be set to [CLIP_CHILDREN_DISABLED](class_canvasitem.md#class-canvasitem-constant-clip-children-disabled) to avoid unexpected behavior.

---


<a id="class-canvasitem-property-light-mask"></a>

[int](class_int.md#class-int) **light_mask** = `1` [🔗](class_canvasitem.md#class-canvasitem-property-light-mask)

- void **set_light_mask**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_light_mask**()

The rendering layers in which this **CanvasItem** responds to [Light2D](class_light2d.md#class-light2d) nodes.

---


<a id="class-canvasitem-property-material"></a>

[Material](class_material.md#class-material) **material** [🔗](class_canvasitem.md#class-canvasitem-property-material)

- void **set_material**(value: [Material](class_material.md#class-material))
- [Material](class_material.md#class-material) **get_material**()

The material applied to this **CanvasItem**.

---


<a id="class-canvasitem-property-modulate"></a>

[Color](class_color.md#class-color) **modulate** = `Color(1, 1, 1, 1)` [🔗](class_canvasitem.md#class-canvasitem-property-modulate)

- void **set_modulate**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_modulate**()

The color applied to this **CanvasItem**. This property does affect child **CanvasItem**s, unlike [self_modulate](class_canvasitem.md#class-canvasitem-property-self-modulate) which only affects the node itself.

---


<a id="class-canvasitem-property-oversampling-with-scale"></a>

[OversamplingWithScale](class_canvasitem.md#enum-canvasitem-oversamplingwithscale) **oversampling_with_scale** = `0` [🔗](class_canvasitem.md#class-canvasitem-property-oversampling-with-scale)

- void **set_oversampling_with_scale**(value: [OversamplingWithScale](class_canvasitem.md#enum-canvasitem-oversamplingwithscale))
- [OversamplingWithScale](class_canvasitem.md#enum-canvasitem-oversamplingwithscale) **get_oversampling_with_scale**()

If enabled, oversampling for this **CanvasItem** is automatically adjusted with scale.

---


<a id="class-canvasitem-property-self-modulate"></a>

[Color](class_color.md#class-color) **self_modulate** = `Color(1, 1, 1, 1)` [🔗](class_canvasitem.md#class-canvasitem-property-self-modulate)

- void **set_self_modulate**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_self_modulate**()

The color applied to this **CanvasItem**. This property does **not** affect child **CanvasItem**s, unlike [modulate](class_canvasitem.md#class-canvasitem-property-modulate) which affects both the node itself and its children.

**Note:** Internal children are also not affected by this property (see the `include_internal` parameter in [Node.add_child()](class_node.md#class-node-method-add-child)). For built-in nodes this includes sliders in [ColorPicker](class_colorpicker.md#class-colorpicker), and the tab bar in [TabContainer](class_tabcontainer.md#class-tabcontainer).

---


<a id="class-canvasitem-property-show-behind-parent"></a>

[bool](class_bool.md#class-bool) **show_behind_parent** = `false` [🔗](class_canvasitem.md#class-canvasitem-property-show-behind-parent)

- void **set_draw_behind_parent**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_draw_behind_parent_enabled**()

If `true`, this node draws behind its parent.

---


<a id="class-canvasitem-property-texture-filter"></a>

[TextureFilter](class_canvasitem.md#enum-canvasitem-texturefilter) **texture_filter** = `0` [🔗](class_canvasitem.md#class-canvasitem-property-texture-filter)

- void **set_texture_filter**(value: [TextureFilter](class_canvasitem.md#enum-canvasitem-texturefilter))
- [TextureFilter](class_canvasitem.md#enum-canvasitem-texturefilter) **get_texture_filter**()

The filtering mode used to render this **CanvasItem**'s texture(s).

---


<a id="class-canvasitem-property-texture-repeat"></a>

[TextureRepeat](class_canvasitem.md#enum-canvasitem-texturerepeat) **texture_repeat** = `0` [🔗](class_canvasitem.md#class-canvasitem-property-texture-repeat)

- void **set_texture_repeat**(value: [TextureRepeat](class_canvasitem.md#enum-canvasitem-texturerepeat))
- [TextureRepeat](class_canvasitem.md#enum-canvasitem-texturerepeat) **get_texture_repeat**()

The repeating mode used to render this **CanvasItem**'s texture(s). It affects what happens when the texture is sampled outside its extents, for example by setting a [Sprite2D.region_rect](class_sprite2d.md#class-sprite2d-property-region-rect) that is larger than the texture or assigning [Polygon2D](class_polygon2d.md#class-polygon2d) UV points outside the texture.

**Note:** [TextureRect](class_texturerect.md#class-texturerect) is not affected by [texture_repeat](class_canvasitem.md#class-canvasitem-property-texture-repeat), as it uses its own texture repeating implementation.

---


<a id="class-canvasitem-property-top-level"></a>

[bool](class_bool.md#class-bool) **top_level** = `false` [🔗](class_canvasitem.md#class-canvasitem-property-top-level)

- void **set_as_top_level**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_set_as_top_level**()

If `true`, this **CanvasItem** will *not* inherit its transform from parent **CanvasItem**s. Its draw order will also be changed to make it draw on top of other **CanvasItem**s that do not have [top_level](class_canvasitem.md#class-canvasitem-property-top-level) set to `true`. The **CanvasItem** will effectively act as if it was placed as a child of a bare [Node](class_node.md#class-node).

---


<a id="class-canvasitem-property-use-parent-material"></a>

[bool](class_bool.md#class-bool) **use_parent_material** = `false` [🔗](class_canvasitem.md#class-canvasitem-property-use-parent-material)

- void **set_use_parent_material**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_use_parent_material**()

If `true`, the parent **CanvasItem**'s [material](class_canvasitem.md#class-canvasitem-property-material) is used as this node's material.

---


<a id="class-canvasitem-property-visibility-layer"></a>

[int](class_int.md#class-int) **visibility_layer** = `1` [🔗](class_canvasitem.md#class-canvasitem-property-visibility-layer)

- void **set_visibility_layer**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_visibility_layer**()

The rendering layer in which this **CanvasItem** is rendered by [Viewport](class_viewport.md#class-viewport) nodes. A [Viewport](class_viewport.md#class-viewport) will render a **CanvasItem** if it and all its parents share a layer with the [Viewport](class_viewport.md#class-viewport)'s canvas cull mask.

**Note:** A **CanvasItem** does not inherit its parents' visibility layers. This means that if a parent **CanvasItem** does not have all the same layers as its child, the child may not be visible even if both the parent and child have [visible](class_canvasitem.md#class-canvasitem-property-visible) set to `true`. For example, if a parent has layer 1 and a child has layer 2, the child will not be visible in a [Viewport](class_viewport.md#class-viewport) with the canvas cull mask set to layer 1 or 2 (see [Viewport.canvas_cull_mask](class_viewport.md#class-viewport-property-canvas-cull-mask)). To ensure that both the parent and child are visible, the parent must have both layers 1 and 2, or the child must have [top_level](class_canvasitem.md#class-canvasitem-property-top-level) set to `true`.

---


<a id="class-canvasitem-property-visible"></a>

[bool](class_bool.md#class-bool) **visible** = `true` [🔗](class_canvasitem.md#class-canvasitem-property-visible)

- void **set_visible**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_visible**()

If `true`, this **CanvasItem** may be drawn. Whether this **CanvasItem** is actually drawn depends on the visibility of all of its **CanvasItem** ancestors. In other words: this **CanvasItem** will be drawn when [is_visible_in_tree()](class_canvasitem.md#class-canvasitem-method-is-visible-in-tree) returns `true` and all **CanvasItem** ancestors share at least one [visibility_layer](class_canvasitem.md#class-canvasitem-property-visibility-layer) with this **CanvasItem**.

**Note:** For controls that inherit [Popup](class_popup.md#class-popup), the correct way to make them visible is to call one of the multiple `popup*()` functions instead.

---


<a id="class-canvasitem-property-y-sort-enabled"></a>

[bool](class_bool.md#class-bool) **y_sort_enabled** = `false` [🔗](class_canvasitem.md#class-canvasitem-property-y-sort-enabled)

- void **set_y_sort_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_y_sort_enabled**()

If `true`, this and child **CanvasItem** nodes with a higher Y position are rendered in front of nodes with a lower Y position. If `false`, this and child **CanvasItem** nodes are rendered normally in scene tree order.

With Y-sorting enabled on a parent node ('A') but disabled on a child node ('B'), the child node ('B') is sorted but its children ('C1', 'C2', etc.) render together on the same Y position as the child node ('B'). This allows you to organize the render order of a scene without changing the scene tree.

Nodes sort relative to each other only if they are on the same [z_index](class_canvasitem.md#class-canvasitem-property-z-index).

---


<a id="class-canvasitem-property-z-as-relative"></a>

[bool](class_bool.md#class-bool) **z_as_relative** = `true` [🔗](class_canvasitem.md#class-canvasitem-property-z-as-relative)

- void **set_z_as_relative**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_z_relative**()

If `true`, this node's final Z index is relative to its parent's Z index.

For example, if [z_index](class_canvasitem.md#class-canvasitem-property-z-index) is `2` and its parent's final Z index is `3`, then this node's final Z index will be `5` (`2 + 3`).

---


<a id="class-canvasitem-property-z-index"></a>

[int](class_int.md#class-int) **z_index** = `0` [🔗](class_canvasitem.md#class-canvasitem-property-z-index)

- void **set_z_index**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_z_index**()

The order in which this node is drawn. A node with a higher Z index will display in front of others. Must be between [RenderingServer.CANVAS_ITEM_Z_MIN](class_renderingserver.md#class-renderingserver-constant-canvas-item-z-min) and [RenderingServer.CANVAS_ITEM_Z_MAX](class_renderingserver.md#class-renderingserver-constant-canvas-item-z-max) (inclusive).

**Note:** The Z index does **not** affect the order in which **CanvasItem** nodes are processed or the way input events are handled. This is especially important to keep in mind for [Control](class_control.md#class-control) nodes.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-canvasitem-private-method-draw"></a>

void **_draw**() virtual [🔗](class_canvasitem.md#class-canvasitem-private-method-draw)

Called when **CanvasItem** has been requested to redraw (after [queue_redraw()](class_canvasitem.md#class-canvasitem-method-queue-redraw) is called, either manually or by the engine).

Corresponds to the [NOTIFICATION_DRAW](class_canvasitem.md#class-canvasitem-constant-notification-draw) notification in [Object._notification()](class_object.md#class-object-private-method-notification).

---


<a id="class-canvasitem-method-draw-animation-slice"></a>

void **draw_animation_slice**(animation_length: [float](class_float.md#class-float), slice_begin: [float](class_float.md#class-float), slice_end: [float](class_float.md#class-float), offset: [float](class_float.md#class-float) = 0.0) [🔗](class_canvasitem.md#class-canvasitem-method-draw-animation-slice)

Subsequent drawing commands will be ignored unless they fall within the specified animation slice. This is a faster way to implement animations that loop on background rather than redrawing constantly.

---


<a id="class-canvasitem-method-draw-arc"></a>

void **draw_arc**(center: [Vector2](class_vector2.md#class-vector2), radius: [float](class_float.md#class-float), start_angle: [float](class_float.md#class-float), end_angle: [float](class_float.md#class-float), point_count: [int](class_int.md#class-int), color: [Color](class_color.md#class-color), width: [float](class_float.md#class-float) = -1.0, antialiased: [bool](class_bool.md#class-bool) = false) [🔗](class_canvasitem.md#class-canvasitem-method-draw-arc)

Draws an unfilled arc between the given angles with a uniform `color` and `width` and optional antialiasing (supported only for positive `width`). The larger the value of `point_count`, the smoother the curve. `center` is defined in local space. For elliptical arcs, see [draw_ellipse_arc()](class_canvasitem.md#class-canvasitem-method-draw-ellipse-arc). See also [draw_circle()](class_canvasitem.md#class-canvasitem-method-draw-circle).

If `width` is negative, it will be ignored and the arc will be drawn using [RenderingServer.PRIMITIVE_LINE_STRIP](class_renderingserver.md#class-renderingserver-constant-primitive-line-strip). This means that when the CanvasItem is scaled, the arc will remain thin. If this behavior is not desired, then pass a positive `width` like `1.0`.

The arc is drawn from `start_angle` towards the value of `end_angle` so in clockwise direction if `start_angle < end_angle` and counter-clockwise otherwise. Passing the same angles but in reversed order will produce the same arc. If absolute difference of `start_angle` and `end_angle` is greater than [@GDScript.TAU](class_@gdscript.md#class-gdscript-constant-tau) radians, then a full circle arc is drawn (i.e. arc will not overlap itself).

---


<a id="class-canvasitem-method-draw-char"></a>

void **draw_char**(font: [Font](class_font.md#class-font), pos: [Vector2](class_vector2.md#class-vector2), char: [String](class_string.md#class-string), font_size: [int](class_int.md#class-int) = 16, modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0) const [🔗](class_canvasitem.md#class-canvasitem-method-draw-char)

Draws a string first character using a custom font. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used. `pos` is defined in local space.

---


<a id="class-canvasitem-method-draw-char-outline"></a>

void **draw_char_outline**(font: [Font](class_font.md#class-font), pos: [Vector2](class_vector2.md#class-vector2), char: [String](class_string.md#class-string), font_size: [int](class_int.md#class-int) = 16, size: [int](class_int.md#class-int) = -1, modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0) const [🔗](class_canvasitem.md#class-canvasitem-method-draw-char-outline)

Draws a string first character outline using a custom font. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used. `pos` is defined in local space.

---


<a id="class-canvasitem-method-draw-circle"></a>

void **draw_circle**(position: [Vector2](class_vector2.md#class-vector2), radius: [float](class_float.md#class-float), color: [Color](class_color.md#class-color), filled: [bool](class_bool.md#class-bool) = true, width: [float](class_float.md#class-float) = -1.0, antialiased: [bool](class_bool.md#class-bool) = false) [🔗](class_canvasitem.md#class-canvasitem-method-draw-circle)

Draws a circle, with `position` defined in local space. See also [draw_ellipse()](class_canvasitem.md#class-canvasitem-method-draw-ellipse), [draw_arc()](class_canvasitem.md#class-canvasitem-method-draw-arc), [draw_polyline()](class_canvasitem.md#class-canvasitem-method-draw-polyline), and [draw_polygon()](class_canvasitem.md#class-canvasitem-method-draw-polygon).

If `filled` is `true`, the circle will be filled with the `color` specified. If `filled` is `false`, the circle will be drawn as a stroke with the `color` and `width` specified.

If `width` is negative, then two-point primitives will be drawn instead of a four-point ones. This means that when the CanvasItem is scaled, the lines will remain thin. If this behavior is not desired, then pass a positive `width` like `1.0`.

If `antialiased` is `true`, half transparent "feathers" will be attached to the boundary, making outlines smooth.

**Note:** `width` is only effective if `filled` is `false`.

---


<a id="class-canvasitem-method-draw-colored-polygon"></a>

void **draw_colored_polygon**(points: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), color: [Color](class_color.md#class-color), uvs: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) = PackedVector2Array(), texture: [Texture2D](class_texture2d.md#class-texture2d) = null) [🔗](class_canvasitem.md#class-canvasitem-method-draw-colored-polygon)

Draws a colored polygon of any number of points, convex or concave. The points in the `points` array are defined in local space. Unlike [draw_polygon()](class_canvasitem.md#class-canvasitem-method-draw-polygon), a single color must be specified for the whole polygon.

**Note:** If you frequently redraw the same polygon with a large number of vertices, consider pre-calculating the triangulation with [Geometry2D.triangulate_polygon()](class_geometry2d.md#class-geometry2d-method-triangulate-polygon) and using [draw_mesh()](class_canvasitem.md#class-canvasitem-method-draw-mesh), [draw_multimesh()](class_canvasitem.md#class-canvasitem-method-draw-multimesh), or [RenderingServer.canvas_item_add_triangle_array()](class_renderingserver.md#class-renderingserver-method-canvas-item-add-triangle-array).

**Note:** Styleboxes, textures, and meshes stored only inside local variables should **not** be used with this method in GDScript, because the drawing operation doesn't begin immediately once this method is called. In GDScript, when the function with the local variables ends, the local variables get destroyed before the rendering takes place.

---


<a id="class-canvasitem-method-draw-dashed-line"></a>

void **draw_dashed_line**(from: [Vector2](class_vector2.md#class-vector2), to: [Vector2](class_vector2.md#class-vector2), color: [Color](class_color.md#class-color), width: [float](class_float.md#class-float) = -1.0, dash: [float](class_float.md#class-float) = 2.0, aligned: [bool](class_bool.md#class-bool) = true, antialiased: [bool](class_bool.md#class-bool) = false) [🔗](class_canvasitem.md#class-canvasitem-method-draw-dashed-line)

Draws a dashed line from a 2D point to another, with a given color and width. The `from` and `to` positions are defined in local space. See also [draw_line()](class_canvasitem.md#class-canvasitem-method-draw-line), [draw_multiline()](class_canvasitem.md#class-canvasitem-method-draw-multiline), and [draw_polyline()](class_canvasitem.md#class-canvasitem-method-draw-polyline).

If `width` is negative, then a two-point primitives will be drawn instead of a four-point ones. This means that when the CanvasItem is scaled, the line parts will remain thin. If this behavior is not desired, then pass a positive `width` like `1.0`.

`dash` is the length of each dash in pixels, with the gap between each dash being the same length. If `aligned` is `true`, the length of the first and last dashes may be shortened or lengthened to allow the line to begin and end at the precise points defined by `from` and `to`. Both ends are always symmetrical when `aligned` is `true`. If `aligned` is `false`, all dashes will have the same length, but the line may appear incomplete at the end due to the dash length not dividing evenly into the line length. Only full dashes are drawn when `aligned` is `false`.

If `antialiased` is `true`, half transparent "feathers" will be attached to the boundary, making outlines smooth.

**Note:** `antialiased` is only effective if `width` is greater than `0.0`.

---


<a id="class-canvasitem-method-draw-ellipse"></a>

void **draw_ellipse**(position: [Vector2](class_vector2.md#class-vector2), major: [float](class_float.md#class-float), minor: [float](class_float.md#class-float), color: [Color](class_color.md#class-color), filled: [bool](class_bool.md#class-bool) = true, width: [float](class_float.md#class-float) = -1.0, antialiased: [bool](class_bool.md#class-bool) = false) [🔗](class_canvasitem.md#class-canvasitem-method-draw-ellipse)

Draws an ellipse with semi-major axis `major` and semi-minor axis `minor`. See also [draw_circle()](class_canvasitem.md#class-canvasitem-method-draw-circle), [draw_ellipse_arc()](class_canvasitem.md#class-canvasitem-method-draw-ellipse-arc), [draw_polyline()](class_canvasitem.md#class-canvasitem-method-draw-polyline), and [draw_polygon()](class_canvasitem.md#class-canvasitem-method-draw-polygon).

If `filled` is `true`, the ellipse will be filled with the `color` specified. If `filled` is `false`, the ellipse will be drawn as a stroke with the `color` and `width` specified.

If `width` is negative, then two-point primitives will be drawn instead of four-point ones. This means that when the CanvasItem is scaled, the lines will remain thin. If this behavior is not desired, then pass a positive `width` like `1.0`.

If `antialiased` is `true`, half transparent "feathers" will be attached to the boundary, making outlines smooth.

**Note:** `width` is only effective if `filled` is `false`.

---


<a id="class-canvasitem-method-draw-ellipse-arc"></a>

void **draw_ellipse_arc**(center: [Vector2](class_vector2.md#class-vector2), major: [float](class_float.md#class-float), minor: [float](class_float.md#class-float), start_angle: [float](class_float.md#class-float), end_angle: [float](class_float.md#class-float), point_count: [int](class_int.md#class-int), color: [Color](class_color.md#class-color), width: [float](class_float.md#class-float) = -1.0, antialiased: [bool](class_bool.md#class-bool) = false) [🔗](class_canvasitem.md#class-canvasitem-method-draw-ellipse-arc)

Draws an unfilled elliptical arc between the given angles with a uniform `color` and `width` and optional antialiasing (supported only for positive `width`). The larger the value of `point_count`, the smoother the curve. For circular arcs, see [draw_arc()](class_canvasitem.md#class-canvasitem-method-draw-arc). See also [draw_ellipse()](class_canvasitem.md#class-canvasitem-method-draw-ellipse).

If `width` is negative, it will be ignored and the arc will be drawn using [RenderingServer.PRIMITIVE_LINE_STRIP](class_renderingserver.md#class-renderingserver-constant-primitive-line-strip). This means that when the CanvasItem is scaled, the arc will remain thin. If this behavior is not desired, then pass a positive `width` like `1.0`.

The arc is drawn from `start_angle` towards the value of `end_angle` so in clockwise direction if `start_angle < end_angle` and counter-clockwise otherwise. Passing the same angles but in reversed order will produce the same arc. If absolute difference of `start_angle` and `end_angle` is greater than [@GDScript.TAU](class_@gdscript.md#class-gdscript-constant-tau) radians, then a full ellipse is drawn (i.e. arc will not overlap itself).

---


<a id="class-canvasitem-method-draw-end-animation"></a>

void **draw_end_animation**() [🔗](class_canvasitem.md#class-canvasitem-method-draw-end-animation)

After submitting all animations slices via [draw_animation_slice()](class_canvasitem.md#class-canvasitem-method-draw-animation-slice), this function can be used to revert drawing to its default state (all subsequent drawing commands will be visible). If you don't care about this particular use case, usage of this function after submitting the slices is not required.

---


<a id="class-canvasitem-method-draw-lcd-texture-rect-region"></a>

void **draw_lcd_texture_rect_region**(texture: [Texture2D](class_texture2d.md#class-texture2d), rect: [Rect2](class_rect2.md#class-rect2), src_rect: [Rect2](class_rect2.md#class-rect2), modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1)) [🔗](class_canvasitem.md#class-canvasitem-method-draw-lcd-texture-rect-region)

Draws a textured rectangle region of the font texture with LCD subpixel anti-aliasing at a given position, optionally modulated by a color. The `rect` is defined in local space.

Texture is drawn using the following blend operation, blend mode of the [CanvasItemMaterial](class_canvasitemmaterial.md#class-canvasitemmaterial) is ignored:

```gdscript
dst.r = texture.r * modulate.r * modulate.a + dst.r * (1.0 - texture.r * modulate.a);
dst.g = texture.g * modulate.g * modulate.a + dst.g * (1.0 - texture.g * modulate.a);
dst.b = texture.b * modulate.b * modulate.a + dst.b * (1.0 - texture.b * modulate.a);
dst.a = modulate.a + dst.a * (1.0 - modulate.a);
```

**Note:** Styleboxes, textures, and meshes stored only inside local variables should **not** be used with this method in GDScript, because the drawing operation doesn't begin immediately once this method is called. In GDScript, when the function with the local variables ends, the local variables get destroyed before the rendering takes place.

---


<a id="class-canvasitem-method-draw-line"></a>

void **draw_line**(from: [Vector2](class_vector2.md#class-vector2), to: [Vector2](class_vector2.md#class-vector2), color: [Color](class_color.md#class-color), width: [float](class_float.md#class-float) = -1.0, antialiased: [bool](class_bool.md#class-bool) = false) [🔗](class_canvasitem.md#class-canvasitem-method-draw-line)

Draws a line from a 2D point to another, with a given color and width. It can be optionally antialiased. The `from` and `to` positions are defined in local space. See also [draw_dashed_line()](class_canvasitem.md#class-canvasitem-method-draw-dashed-line), [draw_multiline()](class_canvasitem.md#class-canvasitem-method-draw-multiline), and [draw_polyline()](class_canvasitem.md#class-canvasitem-method-draw-polyline).

If `width` is negative, then a two-point primitive will be drawn instead of a four-point one. This means that when the CanvasItem is scaled, the line will remain thin. If this behavior is not desired, then pass a positive `width` like `1.0`.

---


<a id="class-canvasitem-method-draw-mesh"></a>

void **draw_mesh**(mesh: [Mesh](class_mesh.md#class-mesh), texture: [Texture2D](class_texture2d.md#class-texture2d), transform: [Transform2D](class_transform2d.md#class-transform2d) = Transform2D(1, 0, 0, 1, 0, 0), modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1)) [🔗](class_canvasitem.md#class-canvasitem-method-draw-mesh)

Draws a [Mesh](class_mesh.md#class-mesh) in 2D, using the provided texture. See [MeshInstance2D](class_meshinstance2d.md#class-meshinstance2d) for related documentation. The `transform` is defined in local space.

**Note:** Styleboxes, textures, and meshes stored only inside local variables should **not** be used with this method in GDScript, because the drawing operation doesn't begin immediately once this method is called. In GDScript, when the function with the local variables ends, the local variables get destroyed before the rendering takes place.

---


<a id="class-canvasitem-method-draw-msdf-texture-rect-region"></a>

void **draw_msdf_texture_rect_region**(texture: [Texture2D](class_texture2d.md#class-texture2d), rect: [Rect2](class_rect2.md#class-rect2), src_rect: [Rect2](class_rect2.md#class-rect2), modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), outline: [float](class_float.md#class-float) = 0.0, pixel_range: [float](class_float.md#class-float) = 4.0, scale: [float](class_float.md#class-float) = 1.0) [🔗](class_canvasitem.md#class-canvasitem-method-draw-msdf-texture-rect-region)

Draws a textured rectangle region of the multichannel signed distance field texture at a given position, optionally modulated by a color. The `rect` is defined in local space. See [FontFile.multichannel_signed_distance_field](class_fontfile.md#class-fontfile-property-multichannel-signed-distance-field) for more information and caveats about MSDF font rendering.

If `outline` is positive, each alpha channel value of pixel in region is set to maximum value of true distance in the `outline` radius.

Value of the `pixel_range` should the same that was used during distance field texture generation.

**Note:** Styleboxes, textures, and meshes stored only inside local variables should **not** be used with this method in GDScript, because the drawing operation doesn't begin immediately once this method is called. In GDScript, when the function with the local variables ends, the local variables get destroyed before the rendering takes place.

---


<a id="class-canvasitem-method-draw-multiline"></a>

void **draw_multiline**(points: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), color: [Color](class_color.md#class-color), width: [float](class_float.md#class-float) = -1.0, antialiased: [bool](class_bool.md#class-bool) = false) [🔗](class_canvasitem.md#class-canvasitem-method-draw-multiline)

Draws multiple disconnected lines with a uniform `width` and `color`. Each line is defined by two consecutive points from `points` array in local space, i.e. i-th segment consists of `points[2 * i]`, `points[2 * i + 1]` endpoints. When drawing large amounts of lines, this is faster than using individual [draw_line()](class_canvasitem.md#class-canvasitem-method-draw-line) calls. To draw interconnected lines, use [draw_polyline()](class_canvasitem.md#class-canvasitem-method-draw-polyline) instead.

If `width` is negative, then two-point primitives will be drawn instead of a four-point ones. This means that when the CanvasItem is scaled, the lines will remain thin. If this behavior is not desired, then pass a positive `width` like `1.0`.

**Note:** `antialiased` is only effective if `width` is greater than `0.0`.

---


<a id="class-canvasitem-method-draw-multiline-colors"></a>

void **draw_multiline_colors**(points: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), colors: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray), width: [float](class_float.md#class-float) = -1.0, antialiased: [bool](class_bool.md#class-bool) = false) [🔗](class_canvasitem.md#class-canvasitem-method-draw-multiline-colors)

Draws multiple disconnected lines with a uniform `width` and segment-by-segment coloring. Each segment is defined by two consecutive points from `points` array in local space and a corresponding color from `colors` array, i.e. i-th segment consists of `points[2 * i]`, `points[2 * i + 1]` endpoints and has `colors[i]` color. When drawing large amounts of lines, this is faster than using individual [draw_line()](class_canvasitem.md#class-canvasitem-method-draw-line) calls. To draw interconnected lines, use [draw_polyline_colors()](class_canvasitem.md#class-canvasitem-method-draw-polyline-colors) instead.

If `width` is negative, then two-point primitives will be drawn instead of a four-point ones. This means that when the CanvasItem is scaled, the lines will remain thin. If this behavior is not desired, then pass a positive `width` like `1.0`.

**Note:** `antialiased` is only effective if `width` is greater than `0.0`.

---


<a id="class-canvasitem-method-draw-multiline-string"></a>

void **draw_multiline_string**(font: [Font](class_font.md#class-font), pos: [Vector2](class_vector2.md#class-vector2), text: [String](class_string.md#class-string), alignment: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) = 0, width: [float](class_float.md#class-float) = -1, font_size: [int](class_int.md#class-int) = 16, max_lines: [int](class_int.md#class-int) = -1, modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), brk_flags: BitField[[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)] = 3, justification_flags: BitField[[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] = 3, direction: [Direction](class_textserver.md#enum-textserver-direction) = 0, orientation: [Orientation](class_textserver.md#enum-textserver-orientation) = 0, oversampling: [float](class_float.md#class-float) = 0.0) const [🔗](class_canvasitem.md#class-canvasitem-method-draw-multiline-string)

Breaks `text` into lines and draws it using the specified `font` at the `pos` in local space (top-left corner). The text will have its color multiplied by `modulate`. If `width` is greater than or equal to 0, the text will be clipped if it exceeds the specified width. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

---


<a id="class-canvasitem-method-draw-multiline-string-outline"></a>

void **draw_multiline_string_outline**(font: [Font](class_font.md#class-font), pos: [Vector2](class_vector2.md#class-vector2), text: [String](class_string.md#class-string), alignment: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) = 0, width: [float](class_float.md#class-float) = -1, font_size: [int](class_int.md#class-int) = 16, max_lines: [int](class_int.md#class-int) = -1, size: [int](class_int.md#class-int) = 1, modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), brk_flags: BitField[[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)] = 3, justification_flags: BitField[[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] = 3, direction: [Direction](class_textserver.md#enum-textserver-direction) = 0, orientation: [Orientation](class_textserver.md#enum-textserver-orientation) = 0, oversampling: [float](class_float.md#class-float) = 0.0) const [🔗](class_canvasitem.md#class-canvasitem-method-draw-multiline-string-outline)

Breaks `text` to the lines and draws text outline using the specified `font` at the `pos` in local space (top-left corner). The text will have its color multiplied by `modulate`. If `width` is greater than or equal to 0, the text will be clipped if it exceeds the specified width. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

---


<a id="class-canvasitem-method-draw-multimesh"></a>

void **draw_multimesh**(multimesh: [MultiMesh](class_multimesh.md#class-multimesh), texture: [Texture2D](class_texture2d.md#class-texture2d)) [🔗](class_canvasitem.md#class-canvasitem-method-draw-multimesh)

Draws a [MultiMesh](class_multimesh.md#class-multimesh) in 2D with the provided texture. See [MultiMeshInstance2D](class_multimeshinstance2d.md#class-multimeshinstance2d) for related documentation.

**Note:** Styleboxes, textures, and meshes stored only inside local variables should **not** be used with this method in GDScript, because the drawing operation doesn't begin immediately once this method is called. In GDScript, when the function with the local variables ends, the local variables get destroyed before the rendering takes place.

---


<a id="class-canvasitem-method-draw-polygon"></a>

void **draw_polygon**(points: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), colors: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray), uvs: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) = PackedVector2Array(), texture: [Texture2D](class_texture2d.md#class-texture2d) = null) [🔗](class_canvasitem.md#class-canvasitem-method-draw-polygon)

Draws a solid polygon of any number of points, convex or concave. Unlike [draw_colored_polygon()](class_canvasitem.md#class-canvasitem-method-draw-colored-polygon), each point's color can be changed individually. The `points` array is defined in local space. See also [draw_polyline()](class_canvasitem.md#class-canvasitem-method-draw-polyline) and [draw_polyline_colors()](class_canvasitem.md#class-canvasitem-method-draw-polyline-colors). If you need more flexibility (such as being able to use bones), use [RenderingServer.canvas_item_add_triangle_array()](class_renderingserver.md#class-renderingserver-method-canvas-item-add-triangle-array) instead.

**Note:** If you frequently redraw the same polygon with a large number of vertices, consider pre-calculating the triangulation with [Geometry2D.triangulate_polygon()](class_geometry2d.md#class-geometry2d-method-triangulate-polygon) and using [draw_mesh()](class_canvasitem.md#class-canvasitem-method-draw-mesh), [draw_multimesh()](class_canvasitem.md#class-canvasitem-method-draw-multimesh), or [RenderingServer.canvas_item_add_triangle_array()](class_renderingserver.md#class-renderingserver-method-canvas-item-add-triangle-array).

**Note:** Styleboxes, textures, and meshes stored only inside local variables should **not** be used with this method in GDScript, because the drawing operation doesn't begin immediately once this method is called. In GDScript, when the function with the local variables ends, the local variables get destroyed before the rendering takes place.

---


<a id="class-canvasitem-method-draw-polyline"></a>

void **draw_polyline**(points: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), color: [Color](class_color.md#class-color), width: [float](class_float.md#class-float) = -1.0, antialiased: [bool](class_bool.md#class-bool) = false) [🔗](class_canvasitem.md#class-canvasitem-method-draw-polyline)

Draws interconnected line segments with a uniform `color` and `width` and optional antialiasing (supported only for positive `width`). The `points` array is defined in local space. When drawing large amounts of lines, this is faster than using individual [draw_line()](class_canvasitem.md#class-canvasitem-method-draw-line) calls. To draw disconnected lines, use [draw_multiline()](class_canvasitem.md#class-canvasitem-method-draw-multiline) instead. See also [draw_polygon()](class_canvasitem.md#class-canvasitem-method-draw-polygon).

If `width` is negative, it will be ignored and the polyline will be drawn using [RenderingServer.PRIMITIVE_LINE_STRIP](class_renderingserver.md#class-renderingserver-constant-primitive-line-strip). This means that when the CanvasItem is scaled, the polyline will remain thin. If this behavior is not desired, then pass a positive `width` like `1.0`.

---


<a id="class-canvasitem-method-draw-polyline-colors"></a>

void **draw_polyline_colors**(points: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), colors: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray), width: [float](class_float.md#class-float) = -1.0, antialiased: [bool](class_bool.md#class-bool) = false) [🔗](class_canvasitem.md#class-canvasitem-method-draw-polyline-colors)

Draws interconnected line segments with a uniform `width`, point-by-point coloring, and optional antialiasing (supported only for positive `width`). Colors assigned to line points match by index between `points` and `colors`, i.e. each line segment is filled with a gradient between the colors of the endpoints. The `points` array is defined in local space. When drawing large amounts of lines, this is faster than using individual [draw_line()](class_canvasitem.md#class-canvasitem-method-draw-line) calls. To draw disconnected lines, use [draw_multiline_colors()](class_canvasitem.md#class-canvasitem-method-draw-multiline-colors) instead. See also [draw_polygon()](class_canvasitem.md#class-canvasitem-method-draw-polygon).

If `width` is negative, it will be ignored and the polyline will be drawn using [RenderingServer.PRIMITIVE_LINE_STRIP](class_renderingserver.md#class-renderingserver-constant-primitive-line-strip). This means that when the CanvasItem is scaled, the polyline will remain thin. If this behavior is not desired, then pass a positive `width` like `1.0`.

---


<a id="class-canvasitem-method-draw-primitive"></a>

void **draw_primitive**(points: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), colors: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray), uvs: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), texture: [Texture2D](class_texture2d.md#class-texture2d) = null) [🔗](class_canvasitem.md#class-canvasitem-method-draw-primitive)

Draws a custom primitive. 1 point for a point, 2 points for a line, 3 points for a triangle, and 4 points for a quad. If 0 points or more than 4 points are specified, nothing will be drawn and an error message will be printed. The `points` array is defined in local space. See also [draw_line()](class_canvasitem.md#class-canvasitem-method-draw-line), [draw_polyline()](class_canvasitem.md#class-canvasitem-method-draw-polyline), [draw_polygon()](class_canvasitem.md#class-canvasitem-method-draw-polygon), and [draw_rect()](class_canvasitem.md#class-canvasitem-method-draw-rect).

**Note:** Styleboxes, textures, and meshes stored only inside local variables should **not** be used with this method in GDScript, because the drawing operation doesn't begin immediately once this method is called. In GDScript, when the function with the local variables ends, the local variables get destroyed before the rendering takes place.

---


<a id="class-canvasitem-method-draw-rect"></a>

void **draw_rect**(rect: [Rect2](class_rect2.md#class-rect2), color: [Color](class_color.md#class-color), filled: [bool](class_bool.md#class-bool) = true, width: [float](class_float.md#class-float) = -1.0, antialiased: [bool](class_bool.md#class-bool) = false) [🔗](class_canvasitem.md#class-canvasitem-method-draw-rect)

Draws a rectangle. If `filled` is `true`, the rectangle will be filled with the `color` specified. If `filled` is `false`, the rectangle will be drawn as a stroke with the `color` and `width` specified. The `rect` is specified in local space. See also [draw_texture_rect()](class_canvasitem.md#class-canvasitem-method-draw-texture-rect).

If `width` is negative, then two-point primitives will be drawn instead of a four-point ones. This means that when the CanvasItem is scaled, the lines will remain thin. If this behavior is not desired, then pass a positive `width` like `1.0`.

If `antialiased` is `true`, half transparent "feathers" will be attached to the boundary, making outlines smooth.

**Note:** `width` is only effective if `filled` is `false`.

**Note:** Unfilled rectangles drawn with a negative `width` may not display perfectly. For example, corners may be missing or brighter due to overlapping lines (for a translucent `color`).

---


<a id="class-canvasitem-method-draw-set-transform"></a>

void **draw_set_transform**(position: [Vector2](class_vector2.md#class-vector2), rotation: [float](class_float.md#class-float) = 0.0, scale: [Vector2](class_vector2.md#class-vector2) = Vector2(1, 1)) [🔗](class_canvasitem.md#class-canvasitem-method-draw-set-transform)

Sets a custom local transform for drawing via components. Anything drawn afterwards will be transformed by this.

**Note:** [FontFile.oversampling](class_fontfile.md#class-fontfile-property-oversampling) does *not* take `scale` into account. This means that scaling up/down will cause bitmap fonts and rasterized (non-MSDF) dynamic fonts to appear blurry or pixelated. To ensure text remains crisp regardless of scale, you can enable MSDF font rendering by enabling [ProjectSettings.gui/theme/default_font_multichannel_signed_distance_field](class_projectsettings.md#class-projectsettings-property-gui-theme-default-font-multichannel-signed-distance-field) (applies to the default project font only), or enabling **Multichannel Signed Distance Field** in the import options of a DynamicFont for custom fonts. On system fonts, [SystemFont.multichannel_signed_distance_field](class_systemfont.md#class-systemfont-property-multichannel-signed-distance-field) can be enabled in the inspector.

---


<a id="class-canvasitem-method-draw-set-transform-matrix"></a>

void **draw_set_transform_matrix**(xform: [Transform2D](class_transform2d.md#class-transform2d)) [🔗](class_canvasitem.md#class-canvasitem-method-draw-set-transform-matrix)

Sets a custom local transform for drawing via matrix. Anything drawn afterwards will be transformed by this.

---


<a id="class-canvasitem-method-draw-string"></a>

void **draw_string**(font: [Font](class_font.md#class-font), pos: [Vector2](class_vector2.md#class-vector2), text: [String](class_string.md#class-string), alignment: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) = 0, width: [float](class_float.md#class-float) = -1, font_size: [int](class_int.md#class-int) = 16, modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), justification_flags: BitField[[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] = 3, direction: [Direction](class_textserver.md#enum-textserver-direction) = 0, orientation: [Orientation](class_textserver.md#enum-textserver-orientation) = 0, oversampling: [float](class_float.md#class-float) = 0.0) const [🔗](class_canvasitem.md#class-canvasitem-method-draw-string)

Draws `text` using the specified `font` at the `pos` in local space (bottom-left corner using the baseline of the font). The text will have its color multiplied by `modulate`. If `width` is greater than or equal to 0, the text will be clipped if it exceeds the specified width. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

**Example:** Draw "Hello world", using the project's default font:

```gdscript
draw_string(ThemeDB.fallback_font, Vector2(64, 64), "Hello world", HORIZONTAL_ALIGNMENT_LEFT, -1, ThemeDB.fallback_font_size)
```

```csharp
DrawString(ThemeDB.FallbackFont, new Vector2(64, 64), "Hello world", HorizontalAlignment.Left, -1, ThemeDB.FallbackFontSize);
```

See also [Font.draw_string()](class_font.md#class-font-method-draw-string).

---


<a id="class-canvasitem-method-draw-string-outline"></a>

void **draw_string_outline**(font: [Font](class_font.md#class-font), pos: [Vector2](class_vector2.md#class-vector2), text: [String](class_string.md#class-string), alignment: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) = 0, width: [float](class_float.md#class-float) = -1, font_size: [int](class_int.md#class-int) = 16, size: [int](class_int.md#class-int) = 1, modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), justification_flags: BitField[[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] = 3, direction: [Direction](class_textserver.md#enum-textserver-direction) = 0, orientation: [Orientation](class_textserver.md#enum-textserver-orientation) = 0, oversampling: [float](class_float.md#class-float) = 0.0) const [🔗](class_canvasitem.md#class-canvasitem-method-draw-string-outline)

Draws `text` outline using the specified `font` at the `pos` in local space (bottom-left corner using the baseline of the font). The text will have its color multiplied by `modulate`. If `width` is greater than or equal to 0, the text will be clipped if it exceeds the specified width. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

---


<a id="class-canvasitem-method-draw-style-box"></a>

void **draw_style_box**(style_box: [StyleBox](class_stylebox.md#class-stylebox), rect: [Rect2](class_rect2.md#class-rect2)) [🔗](class_canvasitem.md#class-canvasitem-method-draw-style-box)

Draws a styled rectangle. The `rect` is defined in local space.

**Note:** Styleboxes, textures, and meshes stored only inside local variables should **not** be used with this method in GDScript, because the drawing operation doesn't begin immediately once this method is called. In GDScript, when the function with the local variables ends, the local variables get destroyed before the rendering takes place.

---


<a id="class-canvasitem-method-draw-texture"></a>

void **draw_texture**(texture: [Texture2D](class_texture2d.md#class-texture2d), position: [Vector2](class_vector2.md#class-vector2), modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1)) [🔗](class_canvasitem.md#class-canvasitem-method-draw-texture)

Draws a texture at a given position. The `position` is defined in local space.

**Note:** Styleboxes, textures, and meshes stored only inside local variables should **not** be used with this method in GDScript, because the drawing operation doesn't begin immediately once this method is called. In GDScript, when the function with the local variables ends, the local variables get destroyed before the rendering takes place.

---


<a id="class-canvasitem-method-draw-texture-rect"></a>

void **draw_texture_rect**(texture: [Texture2D](class_texture2d.md#class-texture2d), rect: [Rect2](class_rect2.md#class-rect2), tile: [bool](class_bool.md#class-bool), modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), transpose: [bool](class_bool.md#class-bool) = false) [🔗](class_canvasitem.md#class-canvasitem-method-draw-texture-rect)

Draws a textured rectangle at a given position, optionally modulated by a color. The `rect` is defined in local space. If `transpose` is `true`, the texture will have its X and Y coordinates swapped. See also [draw_rect()](class_canvasitem.md#class-canvasitem-method-draw-rect) and [draw_texture_rect_region()](class_canvasitem.md#class-canvasitem-method-draw-texture-rect-region).

**Note:** Styleboxes, textures, and meshes stored only inside local variables should **not** be used with this method in GDScript, because the drawing operation doesn't begin immediately once this method is called. In GDScript, when the function with the local variables ends, the local variables get destroyed before the rendering takes place.

---


<a id="class-canvasitem-method-draw-texture-rect-region"></a>

void **draw_texture_rect_region**(texture: [Texture2D](class_texture2d.md#class-texture2d), rect: [Rect2](class_rect2.md#class-rect2), src_rect: [Rect2](class_rect2.md#class-rect2), modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), transpose: [bool](class_bool.md#class-bool) = false, clip_uv: [bool](class_bool.md#class-bool) = true) [🔗](class_canvasitem.md#class-canvasitem-method-draw-texture-rect-region)

Draws a textured rectangle from a texture's region (specified by `src_rect`) at a given position in local space, optionally modulated by a color. If `transpose` is `true`, the texture will have its X and Y coordinates swapped. See also [draw_texture_rect()](class_canvasitem.md#class-canvasitem-method-draw-texture-rect).

**Note:** Styleboxes, textures, and meshes stored only inside local variables should **not** be used with this method in GDScript, because the drawing operation doesn't begin immediately once this method is called. In GDScript, when the function with the local variables ends, the local variables get destroyed before the rendering takes place.

---


<a id="class-canvasitem-method-force-update-transform"></a>

void **force_update_transform**() [🔗](class_canvasitem.md#class-canvasitem-method-force-update-transform)

Forces the node's transform to update. Fails if the node is not inside the tree. See also [get_transform()](class_canvasitem.md#class-canvasitem-method-get-transform).

**Note:** For performance reasons, transform changes are usually accumulated and applied *once* at the end of the frame. The update propagates through **CanvasItem** children, as well. Therefore, use this method only when you need an up-to-date transform (such as during physics operations).

---


<a id="class-canvasitem-method-get-canvas"></a>

[RID](class_rid.md#class-rid) **get_canvas**() const [🔗](class_canvasitem.md#class-canvasitem-method-get-canvas)

Returns the [RID](class_rid.md#class-rid) of the [World2D](class_world2d.md#class-world2d) canvas where this node is registered to, used by the [RenderingServer](class_renderingserver.md#class-renderingserver).

---


<a id="class-canvasitem-method-get-canvas-item"></a>

[RID](class_rid.md#class-rid) **get_canvas_item**() const [🔗](class_canvasitem.md#class-canvasitem-method-get-canvas-item)

Returns the internal canvas item [RID](class_rid.md#class-rid) used by the [RenderingServer](class_renderingserver.md#class-renderingserver) for this node.

---


<a id="class-canvasitem-method-get-canvas-layer-node"></a>

[CanvasLayer](class_canvaslayer.md#class-canvaslayer) **get_canvas_layer_node**() const [🔗](class_canvasitem.md#class-canvasitem-method-get-canvas-layer-node)

Returns the [CanvasLayer](class_canvaslayer.md#class-canvaslayer) that contains this node, or `null` if the node is not in any [CanvasLayer](class_canvaslayer.md#class-canvaslayer).

---


<a id="class-canvasitem-method-get-canvas-transform"></a>

[Transform2D](class_transform2d.md#class-transform2d) **get_canvas_transform**() const [🔗](class_canvasitem.md#class-canvasitem-method-get-canvas-transform)

Returns the transform of this node, converted from its registered canvas's coordinate system to its viewport's coordinate system. See also [Node.get_viewport()](class_node.md#class-node-method-get-viewport).

---


<a id="class-canvasitem-method-get-global-mouse-position"></a>

[Vector2](class_vector2.md#class-vector2) **get_global_mouse_position**() const [🔗](class_canvasitem.md#class-canvasitem-method-get-global-mouse-position)

Returns mouse cursor's global position relative to the [CanvasLayer](class_canvaslayer.md#class-canvaslayer) that contains this node.

**Note:** For screen-space coordinates (e.g. when using a non-embedded [Popup](class_popup.md#class-popup)), you can use [DisplayServer.mouse_get_position()](class_displayserver.md#class-displayserver-method-mouse-get-position).

---


<a id="class-canvasitem-method-get-global-transform"></a>

[Transform2D](class_transform2d.md#class-transform2d) **get_global_transform**() const [🔗](class_canvasitem.md#class-canvasitem-method-get-global-transform)

Returns the global transform matrix of this item, i.e. the combined transform up to the topmost **CanvasItem** node. The topmost item is a **CanvasItem** that either has no parent, has non-**CanvasItem** parent or it has [top_level](class_canvasitem.md#class-canvasitem-property-top-level) enabled.

---


<a id="class-canvasitem-method-get-global-transform-with-canvas"></a>

[Transform2D](class_transform2d.md#class-transform2d) **get_global_transform_with_canvas**() const [🔗](class_canvasitem.md#class-canvasitem-method-get-global-transform-with-canvas)

Returns the transform from the local coordinate system of this **CanvasItem** to the [Viewport](class_viewport.md#class-viewport)s coordinate system.

---


<a id="class-canvasitem-method-get-instance-shader-parameter"></a>

[Variant](class_variant.md#class-variant) **get_instance_shader_parameter**(name: [StringName](class_stringname.md#class-stringname)) const [🔗](class_canvasitem.md#class-canvasitem-method-get-instance-shader-parameter)

Get the value of a shader parameter as set on this instance.

---


<a id="class-canvasitem-method-get-local-mouse-position"></a>

[Vector2](class_vector2.md#class-vector2) **get_local_mouse_position**() const [🔗](class_canvasitem.md#class-canvasitem-method-get-local-mouse-position)

Returns the mouse's position in this **CanvasItem** using the local coordinate system of this **CanvasItem**.

---


<a id="class-canvasitem-method-get-screen-transform"></a>

[Transform2D](class_transform2d.md#class-transform2d) **get_screen_transform**() const [🔗](class_canvasitem.md#class-canvasitem-method-get-screen-transform)

Returns the transform of this **CanvasItem** in global screen coordinates (i.e. taking window position into account). Mostly useful for editor plugins.

Equivalent to [get_global_transform_with_canvas()](class_canvasitem.md#class-canvasitem-method-get-global-transform-with-canvas) if the window is embedded (see [Viewport.gui_embed_subwindows](class_viewport.md#class-viewport-property-gui-embed-subwindows)).

---


<a id="class-canvasitem-method-get-transform"></a>

[Transform2D](class_transform2d.md#class-transform2d) **get_transform**() const [🔗](class_canvasitem.md#class-canvasitem-method-get-transform)

Returns the transform matrix of this **CanvasItem**.

---


<a id="class-canvasitem-method-get-viewport-rect"></a>

[Rect2](class_rect2.md#class-rect2) **get_viewport_rect**() const [🔗](class_canvasitem.md#class-canvasitem-method-get-viewport-rect)

Returns this node's viewport boundaries as a [Rect2](class_rect2.md#class-rect2). See also [Node.get_viewport()](class_node.md#class-node-method-get-viewport).

---


<a id="class-canvasitem-method-get-viewport-transform"></a>

[Transform2D](class_transform2d.md#class-transform2d) **get_viewport_transform**() const [🔗](class_canvasitem.md#class-canvasitem-method-get-viewport-transform)

Returns the transform of this node, converted from its registered canvas's coordinate system to its viewport embedder's coordinate system. See also [Viewport.get_final_transform()](class_viewport.md#class-viewport-method-get-final-transform) and [Node.get_viewport()](class_node.md#class-node-method-get-viewport).

---


<a id="class-canvasitem-method-get-visibility-layer-bit"></a>

[bool](class_bool.md#class-bool) **get_visibility_layer_bit**(layer: [int](class_int.md#class-int)) const [🔗](class_canvasitem.md#class-canvasitem-method-get-visibility-layer-bit)

Returns `true` if the layer at the given index is set in [visibility_layer](class_canvasitem.md#class-canvasitem-property-visibility-layer).

---


<a id="class-canvasitem-method-get-world-2d"></a>

[World2D](class_world2d.md#class-world2d) **get_world_2d**() const [🔗](class_canvasitem.md#class-canvasitem-method-get-world-2d)

Returns the [World2D](class_world2d.md#class-world2d) this node is registered to.

Usually, this is the same as this node's viewport (see [Node.get_viewport()](class_node.md#class-node-method-get-viewport) and [Viewport.find_world_2d()](class_viewport.md#class-viewport-method-find-world-2d)).

---


<a id="class-canvasitem-method-hide"></a>

void **hide**() [🔗](class_canvasitem.md#class-canvasitem-method-hide)

Hide the **CanvasItem** if it's currently visible. This is equivalent to setting [visible](class_canvasitem.md#class-canvasitem-property-visible) to `false`.

---


<a id="class-canvasitem-method-is-local-transform-notification-enabled"></a>

[bool](class_bool.md#class-bool) **is_local_transform_notification_enabled**() const [🔗](class_canvasitem.md#class-canvasitem-method-is-local-transform-notification-enabled)

Returns `true` if the node receives [NOTIFICATION_LOCAL_TRANSFORM_CHANGED](class_canvasitem.md#class-canvasitem-constant-notification-local-transform-changed) whenever its local transform changes. This is enabled with [set_notify_local_transform()](class_canvasitem.md#class-canvasitem-method-set-notify-local-transform).

---


<a id="class-canvasitem-method-is-transform-notification-enabled"></a>

[bool](class_bool.md#class-bool) **is_transform_notification_enabled**() const [🔗](class_canvasitem.md#class-canvasitem-method-is-transform-notification-enabled)

Returns `true` if the node receives [NOTIFICATION_TRANSFORM_CHANGED](class_canvasitem.md#class-canvasitem-constant-notification-transform-changed) whenever its global transform changes. This is enabled with [set_notify_transform()](class_canvasitem.md#class-canvasitem-method-set-notify-transform).

---


<a id="class-canvasitem-method-is-visible-in-tree"></a>

[bool](class_bool.md#class-bool) **is_visible_in_tree**() const [🔗](class_canvasitem.md#class-canvasitem-method-is-visible-in-tree)

Returns `true` if the node is present in the [SceneTree](class_scenetree.md#class-scenetree), its [visible](class_canvasitem.md#class-canvasitem-property-visible) property is `true` and all its ancestors are also visible. If any ancestor is hidden, this node will not be visible in the scene tree, and is therefore not drawn (see [_draw()](class_canvasitem.md#class-canvasitem-private-method-draw)).

Visibility is checked only in parent nodes that inherit from **CanvasItem**, [CanvasLayer](class_canvaslayer.md#class-canvaslayer), and [Window](class_window.md#class-window). If the parent is of any other type (such as [Node](class_node.md#class-node), [AnimationPlayer](class_animationplayer.md#class-animationplayer), or [Node3D](class_node3d.md#class-node3d)), it is assumed to be visible.

**Note:** This method does not take [visibility_layer](class_canvasitem.md#class-canvasitem-property-visibility-layer) into account, so even if this method returns `true`, the node might end up not being rendered.

---


<a id="class-canvasitem-method-make-canvas-position-local"></a>

[Vector2](class_vector2.md#class-vector2) **make_canvas_position_local**(viewport_point: [Vector2](class_vector2.md#class-vector2)) const [🔗](class_canvasitem.md#class-canvasitem-method-make-canvas-position-local)

Transforms `viewport_point` from the viewport's coordinates to this node's local coordinates.

For the opposite operation, use [get_global_transform_with_canvas()](class_canvasitem.md#class-canvasitem-method-get-global-transform-with-canvas).

```gdscript
var viewport_point = get_global_transform_with_canvas() * local_point
```

---


<a id="class-canvasitem-method-make-input-local"></a>

[InputEvent](class_inputevent.md#class-inputevent) **make_input_local**(event: [InputEvent](class_inputevent.md#class-inputevent)) const [🔗](class_canvasitem.md#class-canvasitem-method-make-input-local)

Returns a copy of the given `event` with its coordinates converted from global space to this **CanvasItem**'s local space. If not possible, returns the same [InputEvent](class_inputevent.md#class-inputevent) unchanged.

---


<a id="class-canvasitem-method-move-to-front"></a>

void **move_to_front**() [🔗](class_canvasitem.md#class-canvasitem-method-move-to-front)

Moves this node below its siblings, usually causing the node to draw on top of its siblings. Does nothing if this node does not have a parent. See also [Node.move_child()](class_node.md#class-node-method-move-child).

---


<a id="class-canvasitem-method-queue-redraw"></a>

void **queue_redraw**() [🔗](class_canvasitem.md#class-canvasitem-method-queue-redraw)

Queues the **CanvasItem** to redraw. During idle time, if **CanvasItem** is visible, [NOTIFICATION_DRAW](class_canvasitem.md#class-canvasitem-constant-notification-draw) is sent and [_draw()](class_canvasitem.md#class-canvasitem-private-method-draw) is called. This only occurs **once** per frame, even if this method has been called multiple times.

---


<a id="class-canvasitem-method-set-instance-shader-parameter"></a>

void **set_instance_shader_parameter**(name: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant)) [🔗](class_canvasitem.md#class-canvasitem-method-set-instance-shader-parameter)

Set the value of a shader uniform for this instance only ([per-instance uniform](../tutorials/shaders/shader_reference/shading_language.md#per-instance-uniforms)). See also [ShaderMaterial.set_shader_parameter()](class_shadermaterial.md#class-shadermaterial-method-set-shader-parameter) to assign a uniform on all instances using the same [ShaderMaterial](class_shadermaterial.md#class-shadermaterial).

**Note:** For a shader uniform to be assignable on a per-instance basis, it *must* be defined with `instance uniform ...` rather than `uniform ...` in the shader code.

**Note:** `name` is case-sensitive and must match the name of the uniform in the code exactly (not the capitalized name in the inspector).

---


<a id="class-canvasitem-method-set-notify-local-transform"></a>

void **set_notify_local_transform**(enable: [bool](class_bool.md#class-bool)) [🔗](class_canvasitem.md#class-canvasitem-method-set-notify-local-transform)

If `true`, the node will receive [NOTIFICATION_LOCAL_TRANSFORM_CHANGED](class_canvasitem.md#class-canvasitem-constant-notification-local-transform-changed) whenever its local transform changes.

**Note:** Many canvas items such as [Bone2D](class_bone2d.md#class-bone2d) or [CollisionShape2D](class_collisionshape2d.md#class-collisionshape2d) automatically enable this in order to function correctly.

---


<a id="class-canvasitem-method-set-notify-transform"></a>

void **set_notify_transform**(enable: [bool](class_bool.md#class-bool)) [🔗](class_canvasitem.md#class-canvasitem-method-set-notify-transform)

If `true`, the node will receive [NOTIFICATION_TRANSFORM_CHANGED](class_canvasitem.md#class-canvasitem-constant-notification-transform-changed) whenever its global transform changes.

**Note:** Many canvas items such as [Camera2D](class_camera2d.md#class-camera2d) or [Light2D](class_light2d.md#class-light2d) automatically enable this in order to function correctly.

---


<a id="class-canvasitem-method-set-visibility-layer-bit"></a>

void **set_visibility_layer_bit**(layer: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool)) [🔗](class_canvasitem.md#class-canvasitem-method-set-visibility-layer-bit)

Set/clear individual bits on the rendering visibility layer. This simplifies editing this **CanvasItem**'s visibility layer.

---


<a id="class-canvasitem-method-show"></a>

void **show**() [🔗](class_canvasitem.md#class-canvasitem-method-show)

Show the **CanvasItem** if it's currently hidden. This is equivalent to setting [visible](class_canvasitem.md#class-canvasitem-property-visible) to `true`.

**Note:** For controls that inherit [Popup](class_popup.md#class-popup), the correct way to make them visible is to call one of the multiple `popup*()` functions instead.
