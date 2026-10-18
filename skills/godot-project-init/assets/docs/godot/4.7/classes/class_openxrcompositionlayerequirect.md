> Source: https://docs.godotengine.org/en/4.7/classes/class_openxrcompositionlayerequirect.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxrcompositionlayerequirect"></a>

<a id="class-openxrcompositionlayerequirect"></a>

# OpenXRCompositionLayerEquirect

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRCompositionLayer](class_openxrcompositionlayer.md#class-openxrcompositionlayer) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

An OpenXR composition layer that is rendered as an internal slice of a sphere.

<a id="description"></a>

## Description

An OpenXR composition layer that allows rendering a [SubViewport](class_subviewport.md#class-subviewport) on an internal slice of a sphere.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [central_horizontal_angle](class_openxrcompositionlayerequirect.md#class-openxrcompositionlayerequirect-property-central-horizontal-angle) | `1.5707964` |
| [int](class_int.md#class-int) | [fallback_segments](class_openxrcompositionlayerequirect.md#class-openxrcompositionlayerequirect-property-fallback-segments) | `10` |
| [float](class_float.md#class-float) | [lower_vertical_angle](class_openxrcompositionlayerequirect.md#class-openxrcompositionlayerequirect-property-lower-vertical-angle) | `0.7853982` |
| [float](class_float.md#class-float) | [radius](class_openxrcompositionlayerequirect.md#class-openxrcompositionlayerequirect-property-radius) | `1.0` |
| [float](class_float.md#class-float) | [upper_vertical_angle](class_openxrcompositionlayerequirect.md#class-openxrcompositionlayerequirect-property-upper-vertical-angle) | `0.7853982` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-openxrcompositionlayerequirect-property-central-horizontal-angle"></a>

[float](class_float.md#class-float) **central_horizontal_angle** = `1.5707964` [🔗](class_openxrcompositionlayerequirect.md#class-openxrcompositionlayerequirect-property-central-horizontal-angle)

- void **set_central_horizontal_angle**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_central_horizontal_angle**()

The central horizontal angle of the sphere. Used to set the width.

---


<a id="class-openxrcompositionlayerequirect-property-fallback-segments"></a>

[int](class_int.md#class-int) **fallback_segments** = `10` [🔗](class_openxrcompositionlayerequirect.md#class-openxrcompositionlayerequirect-property-fallback-segments)

- void **set_fallback_segments**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_fallback_segments**()

The number of segments to use in the fallback mesh.

---


<a id="class-openxrcompositionlayerequirect-property-lower-vertical-angle"></a>

[float](class_float.md#class-float) **lower_vertical_angle** = `0.7853982` [🔗](class_openxrcompositionlayerequirect.md#class-openxrcompositionlayerequirect-property-lower-vertical-angle)

- void **set_lower_vertical_angle**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_lower_vertical_angle**()

The lower vertical angle of the sphere. Used (together with [upper_vertical_angle](class_openxrcompositionlayerequirect.md#class-openxrcompositionlayerequirect-property-upper-vertical-angle)) to set the height.

---


<a id="class-openxrcompositionlayerequirect-property-radius"></a>

[float](class_float.md#class-float) **radius** = `1.0` [🔗](class_openxrcompositionlayerequirect.md#class-openxrcompositionlayerequirect-property-radius)

- void **set_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_radius**()

The radius of the sphere.

---


<a id="class-openxrcompositionlayerequirect-property-upper-vertical-angle"></a>

[float](class_float.md#class-float) **upper_vertical_angle** = `0.7853982` [🔗](class_openxrcompositionlayerequirect.md#class-openxrcompositionlayerequirect-property-upper-vertical-angle)

- void **set_upper_vertical_angle**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_upper_vertical_angle**()

The upper vertical angle of the sphere. Used (together with [lower_vertical_angle](class_openxrcompositionlayerequirect.md#class-openxrcompositionlayerequirect-property-lower-vertical-angle)) to set the height.
