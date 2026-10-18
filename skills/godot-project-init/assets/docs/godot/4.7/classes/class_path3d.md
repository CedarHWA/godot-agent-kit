> Source: https://docs.godotengine.org/en/4.7/classes/class_path3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="path3d"></a>

<a id="class-path3d"></a>

# Path3D

**Inherits:** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Contains a [Curve3D](class_curve3d.md#class-curve3d) path for [PathFollow3D](class_pathfollow3d.md#class-pathfollow3d) nodes to follow.

<a id="description"></a>

## Description

Can have [PathFollow3D](class_pathfollow3d.md#class-pathfollow3d) child nodes moving along the [Curve3D](class_curve3d.md#class-curve3d). See [PathFollow3D](class_pathfollow3d.md#class-pathfollow3d) for more information on the usage.

Note that the path is considered as relative to the moved nodes (children of [PathFollow3D](class_pathfollow3d.md#class-pathfollow3d)). As such, the curve should usually start with a zero vector `(0, 0, 0)`.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Curve3D](class_curve3d.md#class-curve3d) | [curve](class_path3d.md#class-path3d-property-curve) |  |
| [Color](class_color.md#class-color) | [debug_custom_color](class_path3d.md#class-path3d-property-debug-custom-color) | `Color(0, 0, 0, 1)` |

---


<a id="signals"></a>

## Signals

<a id="class-path3d-signal-curve-changed"></a>

**curve_changed**() [🔗](class_path3d.md#class-path3d-signal-curve-changed)

Emitted when the [curve](class_path3d.md#class-path3d-property-curve) changes.

---


<a id="class-path3d-signal-debug-color-changed"></a>

**debug_color_changed**() [🔗](class_path3d.md#class-path3d-signal-debug-color-changed)

Emitted when the [debug_custom_color](class_path3d.md#class-path3d-property-debug-custom-color) changes.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-path3d-property-curve"></a>

[Curve3D](class_curve3d.md#class-curve3d) **curve** [🔗](class_path3d.md#class-path3d-property-curve)

- void **set_curve**(value: [Curve3D](class_curve3d.md#class-curve3d))
- [Curve3D](class_curve3d.md#class-curve3d) **get_curve**()

A [Curve3D](class_curve3d.md#class-curve3d) describing the path.

---


<a id="class-path3d-property-debug-custom-color"></a>

[Color](class_color.md#class-color) **debug_custom_color** = `Color(0, 0, 0, 1)` [🔗](class_path3d.md#class-path3d-property-debug-custom-color)

- void **set_debug_custom_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_debug_custom_color**()

The custom color used to draw the path in the editor. If set to [Color.BLACK](class_color.md#class-color-constant-black) (as by default), the color set in [ProjectSettings.debug/shapes/paths/geometry_color](class_projectsettings.md#class-projectsettings-property-debug-shapes-paths-geometry-color) is used.
