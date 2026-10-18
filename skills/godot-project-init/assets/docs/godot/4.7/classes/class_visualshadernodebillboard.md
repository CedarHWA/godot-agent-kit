> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodebillboard.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodebillboard"></a>

<a id="class-visualshadernodebillboard"></a>

# VisualShaderNodeBillboard

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A node that controls how the object faces the camera to be used within the visual shader graph.

<a id="description"></a>

## Description

The output port of this node needs to be connected to `Model View Matrix` port of [VisualShaderNodeOutput](class_visualshadernodeoutput.md#class-visualshadernodeoutput).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [BillboardType](class_visualshadernodebillboard.md#enum-visualshadernodebillboard-billboardtype) | [billboard_type](class_visualshadernodebillboard.md#class-visualshadernodebillboard-property-billboard-type) | `1` |
| [bool](class_bool.md#class-bool) | [keep_scale](class_visualshadernodebillboard.md#class-visualshadernodebillboard-property-keep-scale) | `false` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-visualshadernodebillboard-billboardtype"></a>

enum **BillboardType**: [🔗](class_visualshadernodebillboard.md#enum-visualshadernodebillboard-billboardtype)

<a id="class-visualshadernodebillboard-constant-billboard-type-disabled"></a>

[BillboardType](class_visualshadernodebillboard.md#enum-visualshadernodebillboard-billboardtype) **BILLBOARD_TYPE_DISABLED** = `0`

Billboarding is disabled and the node does nothing.

<a id="class-visualshadernodebillboard-constant-billboard-type-enabled"></a>

[BillboardType](class_visualshadernodebillboard.md#enum-visualshadernodebillboard-billboardtype) **BILLBOARD_TYPE_ENABLED** = `1`

A standard billboarding algorithm is enabled.

<a id="class-visualshadernodebillboard-constant-billboard-type-fixed-y"></a>

[BillboardType](class_visualshadernodebillboard.md#enum-visualshadernodebillboard-billboardtype) **BILLBOARD_TYPE_FIXED_Y** = `2`

A billboarding algorithm to rotate around Y-axis is enabled.

<a id="class-visualshadernodebillboard-constant-billboard-type-particles"></a>

[BillboardType](class_visualshadernodebillboard.md#enum-visualshadernodebillboard-billboardtype) **BILLBOARD_TYPE_PARTICLES** = `3`

A billboarding algorithm designed to use on particles is enabled.

<a id="class-visualshadernodebillboard-constant-billboard-type-max"></a>

[BillboardType](class_visualshadernodebillboard.md#enum-visualshadernodebillboard-billboardtype) **BILLBOARD_TYPE_MAX** = `4`

Represents the size of the [BillboardType](class_visualshadernodebillboard.md#enum-visualshadernodebillboard-billboardtype) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodebillboard-property-billboard-type"></a>

[BillboardType](class_visualshadernodebillboard.md#enum-visualshadernodebillboard-billboardtype) **billboard_type** = `1` [🔗](class_visualshadernodebillboard.md#class-visualshadernodebillboard-property-billboard-type)

- void **set_billboard_type**(value: [BillboardType](class_visualshadernodebillboard.md#enum-visualshadernodebillboard-billboardtype))
- [BillboardType](class_visualshadernodebillboard.md#enum-visualshadernodebillboard-billboardtype) **get_billboard_type**()

Controls how the object faces the camera.

---


<a id="class-visualshadernodebillboard-property-keep-scale"></a>

[bool](class_bool.md#class-bool) **keep_scale** = `false` [🔗](class_visualshadernodebillboard.md#class-visualshadernodebillboard-property-keep-scale)

- void **set_keep_scale_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_keep_scale_enabled**()

If `true`, the shader will keep the scale set for the mesh. Otherwise, the scale is lost when billboarding.
