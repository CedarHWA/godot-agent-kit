> Source: https://docs.godotengine.org/en/4.7/classes/class_splineik3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="splineik3d"></a>

<a id="class-splineik3d"></a>

# SplineIK3D

**Inherits:** [ChainIK3D](class_chainik3d.md#class-chainik3d) **<** [IKModifier3D](class_ikmodifier3d.md#class-ikmodifier3d) **<** [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) for aligning bones along a [Path3D](class_path3d.md#class-path3d).

<a id="description"></a>

## Description

A [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) for aligning bones along a [Path3D](class_path3d.md#class-path3d). The smoothness of the fitting depends on the [Curve3D.bake_interval](class_curve3d.md#class-curve3d-property-bake-interval).

If you want the [Path3D](class_path3d.md#class-path3d) to attach to a specific bone, it is recommended to place a [ModifierBoneTarget3D](class_modifierbonetarget3d.md#class-modifierbonetarget3d) before the **SplineIK3D** in the [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) list (children of the [Skeleton3D](class_skeleton3d.md#class-skeleton3d)), and then place a [Path3D](class_path3d.md#class-path3d) as the [ModifierBoneTarget3D](class_modifierbonetarget3d.md#class-modifierbonetarget3d)'s child.

Bone twist is determined based on the [Curve3D.get_point_tilt()](class_curve3d.md#class-curve3d-method-get-point-tilt).

If the root bone joint and the start point of the [Curve3D](class_curve3d.md#class-curve3d) are separated, it assumes that there is a linear line segment between them. This means that the vector pointing toward the start point of the [Curve3D](class_curve3d.md#class-curve3d) takes precedence over the shortest intersection point along the [Curve3D](class_curve3d.md#class-curve3d).

If the end bone joint exceeds the path length, it is bent as close as possible to the end point of the [Curve3D](class_curve3d.md#class-curve3d).

**Note:** All the methods in this class take an `index` parameter. This parameter specifies which setting list entry to return if the IK has multiple entries (e.g. `settings/<index>/root_bone_name`).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [setting_count](class_splineik3d.md#class-splineik3d-property-setting-count) | `0` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [NodePath](class_nodepath.md#class-nodepath) | [get_path_3d](class_splineik3d.md#class-splineik3d-method-get-path-3d)(index: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_tilt_fade_in](class_splineik3d.md#class-splineik3d-method-get-tilt-fade-in)(index: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_tilt_fade_out](class_splineik3d.md#class-splineik3d-method-get-tilt-fade-out)(index: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [is_tilt_enabled](class_splineik3d.md#class-splineik3d-method-is-tilt-enabled)(index: [int](class_int.md#class-int)) const |
| void | [set_path_3d](class_splineik3d.md#class-splineik3d-method-set-path-3d)(index: [int](class_int.md#class-int), path_3d: [NodePath](class_nodepath.md#class-nodepath)) |
| void | [set_tilt_enabled](class_splineik3d.md#class-splineik3d-method-set-tilt-enabled)(index: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool)) |
| void | [set_tilt_fade_in](class_splineik3d.md#class-splineik3d-method-set-tilt-fade-in)(index: [int](class_int.md#class-int), size: [int](class_int.md#class-int)) |
| void | [set_tilt_fade_out](class_splineik3d.md#class-splineik3d-method-set-tilt-fade-out)(index: [int](class_int.md#class-int), size: [int](class_int.md#class-int)) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-splineik3d-property-setting-count"></a>

[int](class_int.md#class-int) **setting_count** = `0` [🔗](class_splineik3d.md#class-splineik3d-property-setting-count)

- void **set_setting_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_setting_count**()

The number of settings.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-splineik3d-method-get-path-3d"></a>

[NodePath](class_nodepath.md#class-nodepath) **get_path_3d**(index: [int](class_int.md#class-int)) const [🔗](class_splineik3d.md#class-splineik3d-method-get-path-3d)

Returns the node path of the [Path3D](class_path3d.md#class-path3d) which is describing the path.

---


<a id="class-splineik3d-method-get-tilt-fade-in"></a>

[int](class_int.md#class-int) **get_tilt_fade_in**(index: [int](class_int.md#class-int)) const [🔗](class_splineik3d.md#class-splineik3d-method-get-tilt-fade-in)

Returns the tilt interpolation method used between the root bone and the start point of the [Curve3D](class_curve3d.md#class-curve3d) when they are apart. See also [set_tilt_fade_in()](class_splineik3d.md#class-splineik3d-method-set-tilt-fade-in).

---


<a id="class-splineik3d-method-get-tilt-fade-out"></a>

[int](class_int.md#class-int) **get_tilt_fade_out**(index: [int](class_int.md#class-int)) const [🔗](class_splineik3d.md#class-splineik3d-method-get-tilt-fade-out)

Returns the tilt interpolation method used between the end bone and the end point of the [Curve3D](class_curve3d.md#class-curve3d) when they are apart. See also [set_tilt_fade_out()](class_splineik3d.md#class-splineik3d-method-set-tilt-fade-out).

---


<a id="class-splineik3d-method-is-tilt-enabled"></a>

[bool](class_bool.md#class-bool) **is_tilt_enabled**(index: [int](class_int.md#class-int)) const [🔗](class_splineik3d.md#class-splineik3d-method-is-tilt-enabled)

Returns if the tilt property of the [Curve3D](class_curve3d.md#class-curve3d) affects the bone twist.

---


<a id="class-splineik3d-method-set-path-3d"></a>

void **set_path_3d**(index: [int](class_int.md#class-int), path_3d: [NodePath](class_nodepath.md#class-nodepath)) [🔗](class_splineik3d.md#class-splineik3d-method-set-path-3d)

Sets the node path of the [Path3D](class_path3d.md#class-path3d) which is describing the path.

---


<a id="class-splineik3d-method-set-tilt-enabled"></a>

void **set_tilt_enabled**(index: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool)) [🔗](class_splineik3d.md#class-splineik3d-method-set-tilt-enabled)

Sets if the tilt property of the [Curve3D](class_curve3d.md#class-curve3d) should affect the bone twist.

---


<a id="class-splineik3d-method-set-tilt-fade-in"></a>

void **set_tilt_fade_in**(index: [int](class_int.md#class-int), size: [int](class_int.md#class-int)) [🔗](class_splineik3d.md#class-splineik3d-method-set-tilt-fade-in)

If `size` is greater than `0`, the tilt is interpolated between `size` start bones from the start point of the [Curve3D](class_curve3d.md#class-curve3d) when they are apart.

If `size` is equal `0`, the tilts between the root bone head and the start point of the [Curve3D](class_curve3d.md#class-curve3d) are unified with a tilt of the start point of the [Curve3D](class_curve3d.md#class-curve3d).

If `size` is less than `0`, the tilts between the root bone and the start point of the [Curve3D](class_curve3d.md#class-curve3d) are `0.0`.

---


<a id="class-splineik3d-method-set-tilt-fade-out"></a>

void **set_tilt_fade_out**(index: [int](class_int.md#class-int), size: [int](class_int.md#class-int)) [🔗](class_splineik3d.md#class-splineik3d-method-set-tilt-fade-out)

If `size` is greater than `0`, the tilt is interpolated between `size` end bones from the end point of the [Curve3D](class_curve3d.md#class-curve3d) when they are apart.

If `size` is equal `0`, the tilts between the end bone tail and the end point of the [Curve3D](class_curve3d.md#class-curve3d) are unified with a tilt of the end point of the [Curve3D](class_curve3d.md#class-curve3d).

If `size` is less than `0`, the tilts between the end bone and the end point of the [Curve3D](class_curve3d.md#class-curve3d) are `0.0`.
