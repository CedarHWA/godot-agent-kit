> Source: https://docs.godotengine.org/en/4.7/classes/class_openxrvisibilitymask.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxrvisibilitymask"></a>

<a id="class-openxrvisibilitymask"></a>

# OpenXRVisibilityMask

**Inherits:** [VisualInstance3D](class_visualinstance3d.md#class-visualinstance3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Draws a stereo correct visibility mask.

<a id="description"></a>

## Description

The visibility mask allows us to black out the part of the render result that is invisible due to lens distortion.

As this is rendered first, it prevents fragments with expensive lighting calculations to be processed as they are discarded through z-checking.
