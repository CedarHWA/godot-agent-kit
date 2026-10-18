> Source: https://docs.godotengine.org/en/4.7/classes/class_xrfacemodifier3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="xrfacemodifier3d"></a>

<a id="class-xrfacemodifier3d"></a>

# XRFaceModifier3D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A node for driving standard face meshes from [XRFaceTracker](class_xrfacetracker.md#class-xrfacetracker) weights.

<a id="description"></a>

## Description

This node applies weights from an [XRFaceTracker](class_xrfacetracker.md#class-xrfacetracker) to a mesh with supporting face blend shapes.

The [Unified Expressions](https://docs.vrcft.io/docs/tutorial-avatars/tutorial-avatars-extras/unified-blendshapes) blend shapes are supported, as well as ARKit and SRanipal blend shapes.

The node attempts to identify blend shapes based on name matching. Blend shapes should match the names listed in the [Unified Expressions Compatibility](https://docs.vrcft.io/docs/tutorial-avatars/tutorial-avatars-extras/compatibility/overview) chart.

<a id="tutorials"></a>

## Tutorials

- [XR documentation index](../tutorials/xr/index.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [StringName](class_stringname.md#class-stringname) | [face_tracker](class_xrfacemodifier3d.md#class-xrfacemodifier3d-property-face-tracker) | `&"/user/face_tracker"` |
| [NodePath](class_nodepath.md#class-nodepath) | [target](class_xrfacemodifier3d.md#class-xrfacemodifier3d-property-target) | `NodePath("")` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-xrfacemodifier3d-property-face-tracker"></a>

[StringName](class_stringname.md#class-stringname) **face_tracker** = `&"/user/face_tracker"` [🔗](class_xrfacemodifier3d.md#class-xrfacemodifier3d-property-face-tracker)

- void **set_face_tracker**(value: [StringName](class_stringname.md#class-stringname))
- [StringName](class_stringname.md#class-stringname) **get_face_tracker**()

The [XRFaceTracker](class_xrfacetracker.md#class-xrfacetracker) path.

---


<a id="class-xrfacemodifier3d-property-target"></a>

[NodePath](class_nodepath.md#class-nodepath) **target** = `NodePath("")` [🔗](class_xrfacemodifier3d.md#class-xrfacemodifier3d-property-target)

- void **set_target**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_target**()

The [NodePath](class_nodepath.md#class-nodepath) of the face [MeshInstance3D](class_meshinstance3d.md#class-meshinstance3d).
