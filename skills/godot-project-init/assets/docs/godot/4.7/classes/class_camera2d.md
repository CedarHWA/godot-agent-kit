> Source: https://docs.godotengine.org/en/4.7/classes/class_camera2d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="camera2d"></a>

<a id="class-camera2d"></a>

# Camera2D

**Inherits:** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Camera node for 2D scenes.

<a id="description"></a>

## Description

Camera node for 2D scenes. It forces the screen (current layer) to scroll following this node. This makes it easier (and faster) to program scrollable scenes than manually changing the position of [CanvasItem](class_canvasitem.md#class-canvasitem)-based nodes.

Cameras register themselves in the nearest [Viewport](class_viewport.md#class-viewport) node (when ascending the tree). Only one camera can be active per viewport. If no viewport is available ascending the tree, the camera will register in the global viewport.

This node is intended to be a simple helper to get things going quickly, but more functionality may be desired to change how the camera works. To make your own custom camera node, inherit it from [Node2D](class_node2d.md#class-node2d) and change the transform of the canvas by setting [Viewport.canvas_transform](class_viewport.md#class-viewport-property-canvas-transform) in [Viewport](class_viewport.md#class-viewport) (you can obtain the current [Viewport](class_viewport.md#class-viewport) by using [Node.get_viewport()](class_node.md#class-node-method-get-viewport)).

Note that the **Camera2D** node's [Node2D.global_position](class_node2d.md#class-node2d-property-global-position) doesn't represent the actual position of the screen, which may differ due to applied smoothing or limits. You can use [get_screen_center_position()](class_camera2d.md#class-camera2d-method-get-screen-center-position) to get the real position. Same for the node's [Node2D.global_rotation](class_node2d.md#class-node2d-property-global-rotation) which may be different due to applied rotation smoothing. You can use [get_screen_rotation()](class_camera2d.md#class-camera2d-method-get-screen-rotation) to get the current rotation of the screen.

<a id="tutorials"></a>

## Tutorials

- [2D Platformer Demo](https://godotengine.org/asset-library/asset/2727)
- [2D Isometric Demo](https://godotengine.org/asset-library/asset/2718)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [AnchorMode](class_camera2d.md#enum-camera2d-anchormode) | [anchor_mode](class_camera2d.md#class-camera2d-property-anchor-mode) | `1` |
| [Node](class_node.md#class-node) | [custom_viewport](class_camera2d.md#class-camera2d-property-custom-viewport) |  |
| [float](class_float.md#class-float) | [drag_bottom_margin](class_camera2d.md#class-camera2d-property-drag-bottom-margin) | `0.2` |
| [bool](class_bool.md#class-bool) | [drag_horizontal_enabled](class_camera2d.md#class-camera2d-property-drag-horizontal-enabled) | `false` |
| [float](class_float.md#class-float) | [drag_horizontal_offset](class_camera2d.md#class-camera2d-property-drag-horizontal-offset) | `0.0` |
| [float](class_float.md#class-float) | [drag_left_margin](class_camera2d.md#class-camera2d-property-drag-left-margin) | `0.2` |
| [float](class_float.md#class-float) | [drag_right_margin](class_camera2d.md#class-camera2d-property-drag-right-margin) | `0.2` |
| [float](class_float.md#class-float) | [drag_top_margin](class_camera2d.md#class-camera2d-property-drag-top-margin) | `0.2` |
| [bool](class_bool.md#class-bool) | [drag_vertical_enabled](class_camera2d.md#class-camera2d-property-drag-vertical-enabled) | `false` |
| [float](class_float.md#class-float) | [drag_vertical_offset](class_camera2d.md#class-camera2d-property-drag-vertical-offset) | `0.0` |
| [bool](class_bool.md#class-bool) | [editor_draw_drag_margin](class_camera2d.md#class-camera2d-property-editor-draw-drag-margin) | `false` |
| [bool](class_bool.md#class-bool) | [editor_draw_limits](class_camera2d.md#class-camera2d-property-editor-draw-limits) | `false` |
| [bool](class_bool.md#class-bool) | [editor_draw_screen](class_camera2d.md#class-camera2d-property-editor-draw-screen) | `true` |
| [bool](class_bool.md#class-bool) | [enabled](class_camera2d.md#class-camera2d-property-enabled) | `true` |
| [bool](class_bool.md#class-bool) | [ignore_rotation](class_camera2d.md#class-camera2d-property-ignore-rotation) | `true` |
| [int](class_int.md#class-int) | [limit_bottom](class_camera2d.md#class-camera2d-property-limit-bottom) | `10000000` |
| [bool](class_bool.md#class-bool) | [limit_enabled](class_camera2d.md#class-camera2d-property-limit-enabled) | `true` |
| [int](class_int.md#class-int) | [limit_left](class_camera2d.md#class-camera2d-property-limit-left) | `-10000000` |
| [int](class_int.md#class-int) | [limit_right](class_camera2d.md#class-camera2d-property-limit-right) | `10000000` |
| [bool](class_bool.md#class-bool) | [limit_smoothed](class_camera2d.md#class-camera2d-property-limit-smoothed) | `false` |
| [int](class_int.md#class-int) | [limit_top](class_camera2d.md#class-camera2d-property-limit-top) | `-10000000` |
| [Vector2](class_vector2.md#class-vector2) | [offset](class_camera2d.md#class-camera2d-property-offset) | `Vector2(0, 0)` |
| [bool](class_bool.md#class-bool) | [position_smoothing_enabled](class_camera2d.md#class-camera2d-property-position-smoothing-enabled) | `false` |
| [float](class_float.md#class-float) | [position_smoothing_speed](class_camera2d.md#class-camera2d-property-position-smoothing-speed) | `5.0` |
| [Camera2DProcessCallback](class_camera2d.md#enum-camera2d-camera2dprocesscallback) | [process_callback](class_camera2d.md#class-camera2d-property-process-callback) | `1` |
| [bool](class_bool.md#class-bool) | [rotation_smoothing_enabled](class_camera2d.md#class-camera2d-property-rotation-smoothing-enabled) | `false` |
| [float](class_float.md#class-float) | [rotation_smoothing_speed](class_camera2d.md#class-camera2d-property-rotation-smoothing-speed) | `5.0` |
| [Vector2](class_vector2.md#class-vector2) | [zoom](class_camera2d.md#class-camera2d-property-zoom) | `Vector2(1, 1)` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [align](class_camera2d.md#class-camera2d-method-align)() |
| void | [force_update_scroll](class_camera2d.md#class-camera2d-method-force-update-scroll)() |
| [float](class_float.md#class-float) | [get_drag_margin](class_camera2d.md#class-camera2d-method-get-drag-margin)(margin: [Side](class_@globalscope.md#enum-globalscope-side)) const |
| [int](class_int.md#class-int) | [get_limit](class_camera2d.md#class-camera2d-method-get-limit)(margin: [Side](class_@globalscope.md#enum-globalscope-side)) const |
| [Vector2](class_vector2.md#class-vector2) | [get_screen_center_position](class_camera2d.md#class-camera2d-method-get-screen-center-position)() const |
| [float](class_float.md#class-float) | [get_screen_rotation](class_camera2d.md#class-camera2d-method-get-screen-rotation)() const |
| [Vector2](class_vector2.md#class-vector2) | [get_target_position](class_camera2d.md#class-camera2d-method-get-target-position)() const |
| [bool](class_bool.md#class-bool) | [is_current](class_camera2d.md#class-camera2d-method-is-current)() const |
| void | [make_current](class_camera2d.md#class-camera2d-method-make-current)() |
| void | [reset_smoothing](class_camera2d.md#class-camera2d-method-reset-smoothing)() |
| void | [set_drag_margin](class_camera2d.md#class-camera2d-method-set-drag-margin)(margin: [Side](class_@globalscope.md#enum-globalscope-side), drag_margin: [float](class_float.md#class-float)) |
| void | [set_limit](class_camera2d.md#class-camera2d-method-set-limit)(margin: [Side](class_@globalscope.md#enum-globalscope-side), limit: [int](class_int.md#class-int)) |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-camera2d-anchormode"></a>

enum **AnchorMode**: [🔗](class_camera2d.md#enum-camera2d-anchormode)

<a id="class-camera2d-constant-anchor-mode-fixed-top-left"></a>

[AnchorMode](class_camera2d.md#enum-camera2d-anchormode) **ANCHOR_MODE_FIXED_TOP_LEFT** = `0`

The camera's position is fixed so that the top-left corner is always at the origin.

<a id="class-camera2d-constant-anchor-mode-drag-center"></a>

[AnchorMode](class_camera2d.md#enum-camera2d-anchormode) **ANCHOR_MODE_DRAG_CENTER** = `1`

The camera's position takes into account vertical/horizontal offsets and the screen size.

---


<a id="enum-camera2d-camera2dprocesscallback"></a>

enum **Camera2DProcessCallback**: [🔗](class_camera2d.md#enum-camera2d-camera2dprocesscallback)

<a id="class-camera2d-constant-camera2d-process-physics"></a>

[Camera2DProcessCallback](class_camera2d.md#enum-camera2d-camera2dprocesscallback) **CAMERA2D_PROCESS_PHYSICS** = `0`

The camera updates during physics frames (see [Node.NOTIFICATION_INTERNAL_PHYSICS_PROCESS](class_node.md#class-node-constant-notification-internal-physics-process)).

<a id="class-camera2d-constant-camera2d-process-idle"></a>

[Camera2DProcessCallback](class_camera2d.md#enum-camera2d-camera2dprocesscallback) **CAMERA2D_PROCESS_IDLE** = `1`

The camera updates during process frames (see [Node.NOTIFICATION_INTERNAL_PROCESS](class_node.md#class-node-constant-notification-internal-process)).

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-camera2d-property-anchor-mode"></a>

[AnchorMode](class_camera2d.md#enum-camera2d-anchormode) **anchor_mode** = `1` [🔗](class_camera2d.md#class-camera2d-property-anchor-mode)

- void **set_anchor_mode**(value: [AnchorMode](class_camera2d.md#enum-camera2d-anchormode))
- [AnchorMode](class_camera2d.md#enum-camera2d-anchormode) **get_anchor_mode**()

The Camera2D's anchor point.

---


<a id="class-camera2d-property-custom-viewport"></a>

[Node](class_node.md#class-node) **custom_viewport** [🔗](class_camera2d.md#class-camera2d-property-custom-viewport)

- void **set_custom_viewport**(value: [Node](class_node.md#class-node))
- [Node](class_node.md#class-node) **get_custom_viewport**()

The custom [Viewport](class_viewport.md#class-viewport) node attached to the **Camera2D**. If `null` or not a [Viewport](class_viewport.md#class-viewport), uses the default viewport instead.

---


<a id="class-camera2d-property-drag-bottom-margin"></a>

[float](class_float.md#class-float) **drag_bottom_margin** = `0.2` [🔗](class_camera2d.md#class-camera2d-property-drag-bottom-margin)

- void **set_drag_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), drag_margin: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_drag_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) const

Bottom margin needed to drag the camera. A value of `1` makes the camera move only when reaching the bottom edge of the screen.

---


<a id="class-camera2d-property-drag-horizontal-enabled"></a>

[bool](class_bool.md#class-bool) **drag_horizontal_enabled** = `false` [🔗](class_camera2d.md#class-camera2d-property-drag-horizontal-enabled)

- void **set_drag_horizontal_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_drag_horizontal_enabled**()

If `true`, the camera only moves when reaching the horizontal (left and right) drag margins. If `false`, the camera moves horizontally regardless of margins.

---


<a id="class-camera2d-property-drag-horizontal-offset"></a>

[float](class_float.md#class-float) **drag_horizontal_offset** = `0.0` [🔗](class_camera2d.md#class-camera2d-property-drag-horizontal-offset)

- void **set_drag_horizontal_offset**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_drag_horizontal_offset**()

The relative horizontal drag offset of the camera between the right (`-1`) and left (`1`) drag margins.

**Note:** Used to set the initial horizontal drag offset; determine the current offset; or force the current offset. It's not automatically updated when [drag_horizontal_enabled](class_camera2d.md#class-camera2d-property-drag-horizontal-enabled) is `true` or the drag margins are changed.

---


<a id="class-camera2d-property-drag-left-margin"></a>

[float](class_float.md#class-float) **drag_left_margin** = `0.2` [🔗](class_camera2d.md#class-camera2d-property-drag-left-margin)

- void **set_drag_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), drag_margin: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_drag_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) const

Left margin needed to drag the camera. A value of `1` makes the camera move only when reaching the left edge of the screen.

---


<a id="class-camera2d-property-drag-right-margin"></a>

[float](class_float.md#class-float) **drag_right_margin** = `0.2` [🔗](class_camera2d.md#class-camera2d-property-drag-right-margin)

- void **set_drag_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), drag_margin: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_drag_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) const

Right margin needed to drag the camera. A value of `1` makes the camera move only when reaching the right edge of the screen.

---


<a id="class-camera2d-property-drag-top-margin"></a>

[float](class_float.md#class-float) **drag_top_margin** = `0.2` [🔗](class_camera2d.md#class-camera2d-property-drag-top-margin)

- void **set_drag_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), drag_margin: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_drag_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) const

Top margin needed to drag the camera. A value of `1` makes the camera move only when reaching the top edge of the screen.

---


<a id="class-camera2d-property-drag-vertical-enabled"></a>

[bool](class_bool.md#class-bool) **drag_vertical_enabled** = `false` [🔗](class_camera2d.md#class-camera2d-property-drag-vertical-enabled)

- void **set_drag_vertical_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_drag_vertical_enabled**()

If `true`, the camera only moves when reaching the vertical (top and bottom) drag margins. If `false`, the camera moves vertically regardless of the drag margins.

---


<a id="class-camera2d-property-drag-vertical-offset"></a>

[float](class_float.md#class-float) **drag_vertical_offset** = `0.0` [🔗](class_camera2d.md#class-camera2d-property-drag-vertical-offset)

- void **set_drag_vertical_offset**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_drag_vertical_offset**()

The relative vertical drag offset of the camera between the bottom (`-1`) and top (`1`) drag margins.

**Note:** Used to set the initial vertical drag offset; determine the current offset; or force the current offset. It's not automatically updated when [drag_vertical_enabled](class_camera2d.md#class-camera2d-property-drag-vertical-enabled) is `true` or the drag margins are changed.

---


<a id="class-camera2d-property-editor-draw-drag-margin"></a>

[bool](class_bool.md#class-bool) **editor_draw_drag_margin** = `false` [🔗](class_camera2d.md#class-camera2d-property-editor-draw-drag-margin)

- void **set_margin_drawing_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_margin_drawing_enabled**()

If `true`, draws the camera's drag margin rectangle in the editor.

---


<a id="class-camera2d-property-editor-draw-limits"></a>

[bool](class_bool.md#class-bool) **editor_draw_limits** = `false` [🔗](class_camera2d.md#class-camera2d-property-editor-draw-limits)

- void **set_limit_drawing_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_limit_drawing_enabled**()

If `true`, draws the camera's limits rectangle in the editor.

---


<a id="class-camera2d-property-editor-draw-screen"></a>

[bool](class_bool.md#class-bool) **editor_draw_screen** = `true` [🔗](class_camera2d.md#class-camera2d-property-editor-draw-screen)

- void **set_screen_drawing_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_screen_drawing_enabled**()

If `true`, draws the camera's screen rectangle in the editor.

---


<a id="class-camera2d-property-enabled"></a>

[bool](class_bool.md#class-bool) **enabled** = `true` [🔗](class_camera2d.md#class-camera2d-property-enabled)

- void **set_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_enabled**()

Controls whether the camera can be active or not. If `true`, the **Camera2D** will become the main camera when it enters the scene tree and there is no active camera currently (see [Viewport.get_camera_2d()](class_viewport.md#class-viewport-method-get-camera-2d)).

When the camera is currently active and [enabled](class_camera2d.md#class-camera2d-property-enabled) is set to `false`, the next enabled **Camera2D** in the scene tree will become active.

---


<a id="class-camera2d-property-ignore-rotation"></a>

[bool](class_bool.md#class-bool) **ignore_rotation** = `true` [🔗](class_camera2d.md#class-camera2d-property-ignore-rotation)

- void **set_ignore_rotation**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_ignoring_rotation**()

If `true`, the camera's rendered view is not affected by its [Node2D.rotation](class_node2d.md#class-node2d-property-rotation) and [Node2D.global_rotation](class_node2d.md#class-node2d-property-global-rotation).

---


<a id="class-camera2d-property-limit-bottom"></a>

[int](class_int.md#class-int) **limit_bottom** = `10000000` [🔗](class_camera2d.md#class-camera2d-property-limit-bottom)

- void **set_limit**(margin: [Side](class_@globalscope.md#enum-globalscope-side), limit: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_limit**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) const

Bottom scroll limit in pixels. The camera stops moving when reaching this value, but [offset](class_camera2d.md#class-camera2d-property-offset) can push the view past the limit.

---


<a id="class-camera2d-property-limit-enabled"></a>

[bool](class_bool.md#class-bool) **limit_enabled** = `true` [🔗](class_camera2d.md#class-camera2d-property-limit-enabled)

- void **set_limit_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_limit_enabled**()

If `true`, the limits will be enabled. Disabling this will allow the camera to focus anywhere, when the four `limit_*` properties will not work.

---


<a id="class-camera2d-property-limit-left"></a>

[int](class_int.md#class-int) **limit_left** = `-10000000` [🔗](class_camera2d.md#class-camera2d-property-limit-left)

- void **set_limit**(margin: [Side](class_@globalscope.md#enum-globalscope-side), limit: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_limit**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) const

Left scroll limit in pixels. The camera stops moving when reaching this value, but [offset](class_camera2d.md#class-camera2d-property-offset) can push the view past the limit.

---


<a id="class-camera2d-property-limit-right"></a>

[int](class_int.md#class-int) **limit_right** = `10000000` [🔗](class_camera2d.md#class-camera2d-property-limit-right)

- void **set_limit**(margin: [Side](class_@globalscope.md#enum-globalscope-side), limit: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_limit**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) const

Right scroll limit in pixels. The camera stops moving when reaching this value, but [offset](class_camera2d.md#class-camera2d-property-offset) can push the view past the limit.

---


<a id="class-camera2d-property-limit-smoothed"></a>

[bool](class_bool.md#class-bool) **limit_smoothed** = `false` [🔗](class_camera2d.md#class-camera2d-property-limit-smoothed)

- void **set_limit_smoothing_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_limit_smoothing_enabled**()

If `true`, the camera smoothly stops when reaches its limits.

This property has no effect if [position_smoothing_enabled](class_camera2d.md#class-camera2d-property-position-smoothing-enabled) is `false`.

**Note:** To immediately update the camera's position to be within limits without smoothing, even with this setting enabled, invoke [reset_smoothing()](class_camera2d.md#class-camera2d-method-reset-smoothing).

---


<a id="class-camera2d-property-limit-top"></a>

[int](class_int.md#class-int) **limit_top** = `-10000000` [🔗](class_camera2d.md#class-camera2d-property-limit-top)

- void **set_limit**(margin: [Side](class_@globalscope.md#enum-globalscope-side), limit: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_limit**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) const

Top scroll limit in pixels. The camera stops moving when reaching this value, but [offset](class_camera2d.md#class-camera2d-property-offset) can push the view past the limit.

---


<a id="class-camera2d-property-offset"></a>

[Vector2](class_vector2.md#class-vector2) **offset** = `Vector2(0, 0)` [🔗](class_camera2d.md#class-camera2d-property-offset)

- void **set_offset**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_offset**()

The camera's relative offset. Useful for looking around or camera shake animations. The offsetted camera can go past the limits defined in [limit_top](class_camera2d.md#class-camera2d-property-limit-top), [limit_bottom](class_camera2d.md#class-camera2d-property-limit-bottom), [limit_left](class_camera2d.md#class-camera2d-property-limit-left) and [limit_right](class_camera2d.md#class-camera2d-property-limit-right).

---


<a id="class-camera2d-property-position-smoothing-enabled"></a>

[bool](class_bool.md#class-bool) **position_smoothing_enabled** = `false` [🔗](class_camera2d.md#class-camera2d-property-position-smoothing-enabled)

- void **set_position_smoothing_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_position_smoothing_enabled**()

If `true`, the camera's view smoothly moves towards its target position at [position_smoothing_speed](class_camera2d.md#class-camera2d-property-position-smoothing-speed).

---


<a id="class-camera2d-property-position-smoothing-speed"></a>

[float](class_float.md#class-float) **position_smoothing_speed** = `5.0` [🔗](class_camera2d.md#class-camera2d-property-position-smoothing-speed)

- void **set_position_smoothing_speed**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_position_smoothing_speed**()

Speed in pixels per second of the camera's smoothing effect when [position_smoothing_enabled](class_camera2d.md#class-camera2d-property-position-smoothing-enabled) is `true`.

---


<a id="class-camera2d-property-process-callback"></a>

[Camera2DProcessCallback](class_camera2d.md#enum-camera2d-camera2dprocesscallback) **process_callback** = `1` [🔗](class_camera2d.md#class-camera2d-property-process-callback)

- void **set_process_callback**(value: [Camera2DProcessCallback](class_camera2d.md#enum-camera2d-camera2dprocesscallback))
- [Camera2DProcessCallback](class_camera2d.md#enum-camera2d-camera2dprocesscallback) **get_process_callback**()

The camera's process callback.

---


<a id="class-camera2d-property-rotation-smoothing-enabled"></a>

[bool](class_bool.md#class-bool) **rotation_smoothing_enabled** = `false` [🔗](class_camera2d.md#class-camera2d-property-rotation-smoothing-enabled)

- void **set_rotation_smoothing_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_rotation_smoothing_enabled**()

If `true`, the camera's view smoothly rotates, via asymptotic smoothing, to align with its target rotation at [rotation_smoothing_speed](class_camera2d.md#class-camera2d-property-rotation-smoothing-speed).

**Note:** This property has no effect if [ignore_rotation](class_camera2d.md#class-camera2d-property-ignore-rotation) is `true`.

---


<a id="class-camera2d-property-rotation-smoothing-speed"></a>

[float](class_float.md#class-float) **rotation_smoothing_speed** = `5.0` [🔗](class_camera2d.md#class-camera2d-property-rotation-smoothing-speed)

- void **set_rotation_smoothing_speed**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_rotation_smoothing_speed**()

The angular, asymptotic speed of the camera's rotation smoothing effect when [rotation_smoothing_enabled](class_camera2d.md#class-camera2d-property-rotation-smoothing-enabled) is `true`.

---


<a id="class-camera2d-property-zoom"></a>

[Vector2](class_vector2.md#class-vector2) **zoom** = `Vector2(1, 1)` [🔗](class_camera2d.md#class-camera2d-property-zoom)

- void **set_zoom**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_zoom**()

The camera's zoom. Higher values are more zoomed in. For example, a zoom of `Vector2(2.0, 2.0)` will be twice as zoomed in on each axis (the view covers an area four times smaller). In contrast, a zoom of `Vector2(0.5, 0.5)` will be twice as zoomed out on each axis (the view covers an area four times larger). The X and Y components should generally always be set to the same value, unless you wish to stretch the camera view.

**Note:** [FontFile.oversampling](class_fontfile.md#class-fontfile-property-oversampling) does *not* take **Camera2D** zoom into account. This means that zooming in/out will cause bitmap fonts and rasterized (non-MSDF) dynamic fonts to appear blurry or pixelated unless the font is part of a [CanvasLayer](class_canvaslayer.md#class-canvaslayer) that makes it ignore camera zoom. To ensure text remains crisp regardless of zoom, you can enable MSDF font rendering by enabling [ProjectSettings.gui/theme/default_font_multichannel_signed_distance_field](class_projectsettings.md#class-projectsettings-property-gui-theme-default-font-multichannel-signed-distance-field) (applies to the default project font only), or enabling **Multichannel Signed Distance Field** in the import options of a DynamicFont for custom fonts. On system fonts, [SystemFont.multichannel_signed_distance_field](class_systemfont.md#class-systemfont-property-multichannel-signed-distance-field) can be enabled in the inspector.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-camera2d-method-align"></a>

void **align**() [🔗](class_camera2d.md#class-camera2d-method-align)

Aligns the camera to the tracked node.

**Note:** Calling [force_update_scroll()](class_camera2d.md#class-camera2d-method-force-update-scroll) after this method is not required.

---


<a id="class-camera2d-method-force-update-scroll"></a>

void **force_update_scroll**() [🔗](class_camera2d.md#class-camera2d-method-force-update-scroll)

Forces the camera to update scroll immediately.

---


<a id="class-camera2d-method-get-drag-margin"></a>

[float](class_float.md#class-float) **get_drag_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) const [🔗](class_camera2d.md#class-camera2d-method-get-drag-margin)

Returns the specified [Side](class_@globalscope.md#enum-globalscope-side)'s margin. See also [drag_bottom_margin](class_camera2d.md#class-camera2d-property-drag-bottom-margin), [drag_top_margin](class_camera2d.md#class-camera2d-property-drag-top-margin), [drag_left_margin](class_camera2d.md#class-camera2d-property-drag-left-margin), and [drag_right_margin](class_camera2d.md#class-camera2d-property-drag-right-margin).

---


<a id="class-camera2d-method-get-limit"></a>

[int](class_int.md#class-int) **get_limit**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) const [🔗](class_camera2d.md#class-camera2d-method-get-limit)

Returns the camera limit for the specified [Side](class_@globalscope.md#enum-globalscope-side). See also [limit_bottom](class_camera2d.md#class-camera2d-property-limit-bottom), [limit_top](class_camera2d.md#class-camera2d-property-limit-top), [limit_left](class_camera2d.md#class-camera2d-property-limit-left), and [limit_right](class_camera2d.md#class-camera2d-property-limit-right).

---


<a id="class-camera2d-method-get-screen-center-position"></a>

[Vector2](class_vector2.md#class-vector2) **get_screen_center_position**() const [🔗](class_camera2d.md#class-camera2d-method-get-screen-center-position)

Returns the center of the screen from this camera's point of view, in global coordinates.

**Note:** The exact targeted position of the camera may be different. See [get_target_position()](class_camera2d.md#class-camera2d-method-get-target-position).

---


<a id="class-camera2d-method-get-screen-rotation"></a>

[float](class_float.md#class-float) **get_screen_rotation**() const [🔗](class_camera2d.md#class-camera2d-method-get-screen-rotation)

Returns the current screen rotation from this camera's point of view.

**Note:** The screen rotation can be different from [Node2D.global_rotation](class_node2d.md#class-node2d-property-global-rotation) if the camera is rotating smoothly due to [rotation_smoothing_enabled](class_camera2d.md#class-camera2d-property-rotation-smoothing-enabled).

---


<a id="class-camera2d-method-get-target-position"></a>

[Vector2](class_vector2.md#class-vector2) **get_target_position**() const [🔗](class_camera2d.md#class-camera2d-method-get-target-position)

Returns this camera's target position, in global coordinates.

**Note:** The returned value is not the same as [Node2D.global_position](class_node2d.md#class-node2d-property-global-position), as it is affected by the drag properties. It is also not the same as the current position if [position_smoothing_enabled](class_camera2d.md#class-camera2d-property-position-smoothing-enabled) is `true` (see [get_screen_center_position()](class_camera2d.md#class-camera2d-method-get-screen-center-position)).

---


<a id="class-camera2d-method-is-current"></a>

[bool](class_bool.md#class-bool) **is_current**() const [🔗](class_camera2d.md#class-camera2d-method-is-current)

Returns `true` if this **Camera2D** is the active camera (see [Viewport.get_camera_2d()](class_viewport.md#class-viewport-method-get-camera-2d)).

---


<a id="class-camera2d-method-make-current"></a>

void **make_current**() [🔗](class_camera2d.md#class-camera2d-method-make-current)

Forces this **Camera2D** to become the current active one. [enabled](class_camera2d.md#class-camera2d-property-enabled) must be `true`.

---


<a id="class-camera2d-method-reset-smoothing"></a>

void **reset_smoothing**() [🔗](class_camera2d.md#class-camera2d-method-reset-smoothing)

Sets the camera's position immediately to its current smoothing destination.

This method has no effect if [position_smoothing_enabled](class_camera2d.md#class-camera2d-property-position-smoothing-enabled) is `false`.

---


<a id="class-camera2d-method-set-drag-margin"></a>

void **set_drag_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), drag_margin: [float](class_float.md#class-float)) [🔗](class_camera2d.md#class-camera2d-method-set-drag-margin)

Sets the specified [Side](class_@globalscope.md#enum-globalscope-side)'s margin. See also [drag_bottom_margin](class_camera2d.md#class-camera2d-property-drag-bottom-margin), [drag_top_margin](class_camera2d.md#class-camera2d-property-drag-top-margin), [drag_left_margin](class_camera2d.md#class-camera2d-property-drag-left-margin), and [drag_right_margin](class_camera2d.md#class-camera2d-property-drag-right-margin).

---


<a id="class-camera2d-method-set-limit"></a>

void **set_limit**(margin: [Side](class_@globalscope.md#enum-globalscope-side), limit: [int](class_int.md#class-int)) [🔗](class_camera2d.md#class-camera2d-method-set-limit)

Sets the camera limit for the specified [Side](class_@globalscope.md#enum-globalscope-side). See also [limit_bottom](class_camera2d.md#class-camera2d-property-limit-bottom), [limit_top](class_camera2d.md#class-camera2d-property-limit-top), [limit_left](class_camera2d.md#class-camera2d-property-limit-left), and [limit_right](class_camera2d.md#class-camera2d-property-limit-right).
