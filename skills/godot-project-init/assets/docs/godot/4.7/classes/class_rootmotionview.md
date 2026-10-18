> Source: https://docs.godotengine.org/en/4.7/classes/class_rootmotionview.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="rootmotionview"></a>

<a id="class-rootmotionview"></a>

# RootMotionView

**Inherits:** [VisualInstance3D](class_visualinstance3d.md#class-visualinstance3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Editor-only helper for setting up root motion in [AnimationMixer](class_animationmixer.md#class-animationmixer).

<a id="description"></a>

## Description

*Root motion* refers to an animation technique where a mesh's skeleton is used to give impulse to a character. When working with 3D animations, a popular technique is for animators to use the root skeleton bone to give motion to the rest of the skeleton. This allows animating characters in a way where steps actually match the floor below. It also allows precise interaction with objects during cinematics. See also [AnimationMixer](class_animationmixer.md#class-animationmixer).

**Note:** **RootMotionView** is only visible in the editor. It will be hidden automatically in the running project.

<a id="tutorials"></a>

## Tutorials

- [Using AnimationTree - Root motion](../tutorials/animation/animation_tree.md#root-motion)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [NodePath](class_nodepath.md#class-nodepath) | [animation_path](class_rootmotionview.md#class-rootmotionview-property-animation-path) | `NodePath("")` |
| [float](class_float.md#class-float) | [cell_size](class_rootmotionview.md#class-rootmotionview-property-cell-size) | `1.0` |
| [Color](class_color.md#class-color) | [color](class_rootmotionview.md#class-rootmotionview-property-color) | `Color(0.5, 0.5, 1, 1)` |
| [float](class_float.md#class-float) | [radius](class_rootmotionview.md#class-rootmotionview-property-radius) | `10.0` |
| [bool](class_bool.md#class-bool) | [zero_y](class_rootmotionview.md#class-rootmotionview-property-zero-y) | `true` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-rootmotionview-property-animation-path"></a>

[NodePath](class_nodepath.md#class-nodepath) **animation_path** = `NodePath("")` [🔗](class_rootmotionview.md#class-rootmotionview-property-animation-path)

- void **set_animation_path**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_animation_path**()

Path to an [AnimationMixer](class_animationmixer.md#class-animationmixer) node to use as a basis for root motion.

---


<a id="class-rootmotionview-property-cell-size"></a>

[float](class_float.md#class-float) **cell_size** = `1.0` [🔗](class_rootmotionview.md#class-rootmotionview-property-cell-size)

- void **set_cell_size**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_cell_size**()

The grid's cell size in 3D units.

---


<a id="class-rootmotionview-property-color"></a>

[Color](class_color.md#class-color) **color** = `Color(0.5, 0.5, 1, 1)` [🔗](class_rootmotionview.md#class-rootmotionview-property-color)

- void **set_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_color**()

The grid's color.

---


<a id="class-rootmotionview-property-radius"></a>

[float](class_float.md#class-float) **radius** = `10.0` [🔗](class_rootmotionview.md#class-rootmotionview-property-radius)

- void **set_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_radius**()

The grid's radius in 3D units. The grid's opacity will fade gradually as the distance from the origin increases until this [radius](class_rootmotionview.md#class-rootmotionview-property-radius) is reached.

---


<a id="class-rootmotionview-property-zero-y"></a>

[bool](class_bool.md#class-bool) **zero_y** = `true` [🔗](class_rootmotionview.md#class-rootmotionview-property-zero-y)

- void **set_zero_y**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_zero_y**()

If `true`, the grid's points will all be on the same Y coordinate (*local* Y = 0). If `false`, the points' original Y coordinate is preserved.
