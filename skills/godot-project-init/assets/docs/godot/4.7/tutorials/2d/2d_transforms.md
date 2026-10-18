> Source: https://docs.godotengine.org/en/4.7/tutorials/2d/2d_transforms.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="viewport-and-canvas-transforms"></a>

<a id="doc-viewport-and-canvas-transforms"></a>

# Viewport and canvas transforms

<a id="introduction"></a>

## Introduction

This is an overview of the 2D transforms going on for nodes from the
moment they draw their content locally to the time they are drawn onto
the screen. This overview discusses very low-level details of the engine.

The goal of this tutorial is to teach a way for feeding input events to the
Input with a position in the correct coordinate system.

A more extensive description of all coordinate systems and 2d transforms is
available in [2D coordinate systems and 2D transforms](../../engine_details/architecture/2d_coordinate_systems.md#doc-2d-coordinate-systems).

<a id="canvas-transform"></a>

## Canvas transform

As mentioned in the previous tutorial, [Canvas layers](canvas_layers.md#doc-canvas-layers), every
CanvasItem node (remember that Node2D and Control based nodes use
CanvasItem as their common root) will reside in a *Canvas Layer*. Every
canvas layer has a transform (translation, rotation, scale, etc.) that
can be accessed as a [Transform2D](../../classes/class_transform2d.md#class-transform2d).

Also covered in the previous tutorial, nodes are drawn by default in Layer 0,
in the built-in canvas. To put nodes in a different layer, a [CanvasLayer](../../classes/class_canvaslayer.md#class-canvaslayer) node can be used.

<a id="global-canvas-transform"></a>

## Global canvas transform

Viewports also have a Global Canvas transform (also a
[Transform2D](../../classes/class_transform2d.md#class-transform2d)). This is the master transform and
affects all individual *Canvas Layer* transforms. Generally, this is primarily
used in Godot's CanvasItem Editor.

<a id="stretch-transform"></a>

## Stretch transform

Finally, viewports have a *Stretch Transform*, which is used when
resizing or stretching the screen. This transform is used internally (as
described in [Multiple resolutions](../rendering/multiple_resolutions.md#doc-multiple-resolutions)), but can also be manually set
on each viewport.

Input events are multiplied by this transform, but lack the ones above. To
convert InputEvent coordinates to local CanvasItem coordinates, the
[CanvasItem.make_input_local()](../../classes/class_canvasitem.md#class-canvasitem-method-make-input-local)
function was added for convenience.

<a id="window-transform"></a>

## Window transform

The root viewport is a [Window](../../classes/class_window.md#class-window). In order to scale and
position the *Window's* content as described in [Multiple resolutions](../rendering/multiple_resolutions.md#doc-multiple-resolutions),
each [Window](../../classes/class_window.md#class-window) contains a *window transform*. It is for
example responsible for the black bars at the *Window's* sides so that the
*Viewport* is displayed with a fixed aspect ratio.

<a id="transform-order"></a>

## Transform order

To convert a CanvasItem local coordinate to an actual screen coordinate,
the following chain of transforms must be applied:

![../../_images/viewport_transforms3.webp](https://docs.godotengine.org/en/4.7/_images/viewport_transforms3.webp)

<a id="transform-functions"></a>

## Transform functions

The above graphic shows some available transform functions. All transforms are directed from right
to left, this means multiplying a transform with a coordinate results in a coordinate system
further to the left, multiplying the [affine inverse](../../classes/class_transform2d.md#class-transform2d-method-affine-inverse)
of a transform results in a coordinate system further to the right:

```gdscript
# Called from a CanvasItem.
canvas_pos = get_global_transform() * local_pos
local_pos = get_global_transform().affine_inverse() * canvas_pos
```

```csharp
// Called from a CanvasItem.
canvasPos = GetGlobalTransform() * localPos;
localPos = GetGlobalTransform().AffineInverse() * canvasPos;
```

Finally, then, to convert a CanvasItem local coordinates to screen coordinates, just multiply in
the following order:

```gdscript
var screen_coord = get_viewport().get_screen_transform() * get_global_transform_with_canvas() * local_pos
```

```csharp
var screenCoord = GetViewport().GetScreenTransform() * GetGlobalTransformWithCanvas() * localPos;
```

Keep in mind, however, that it is generally not desired to work with screen coordinates. The
recommended approach is to simply work in Canvas coordinates
(`CanvasItem.get_global_transform()`), to allow automatic screen resolution resizing to work
properly.

<a id="feeding-custom-input-events"></a>

## Feeding custom input events

It is often desired to feed custom input events to the game. With the above knowledge, to correctly
do this in the focused window, it must be done the following way:

```gdscript
var local_pos = Vector2(10, 20) # Local to Control/Node2D.
var ie = InputEventMouseButton.new()
ie.button_index = MOUSE_BUTTON_LEFT
ie.position = get_viewport().get_screen_transform() * get_global_transform_with_canvas() * local_pos
Input.parse_input_event(ie)
```

```csharp
var localPos = new Vector2(10,20); // Local to Control/Node2D.
var ie = new InputEventMouseButton()
{
    ButtonIndex = MouseButton.Left,
    Position = GetViewport().GetScreenTransform() * GetGlobalTransformWithCanvas() * localPos,
};
Input.ParseInputEvent(ie);
```
