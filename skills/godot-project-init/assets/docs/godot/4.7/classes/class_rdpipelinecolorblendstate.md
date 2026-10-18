> Source: https://docs.godotengine.org/en/4.7/classes/class_rdpipelinecolorblendstate.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="rdpipelinecolorblendstate"></a>

<a id="class-rdpipelinecolorblendstate"></a>

# RDPipelineColorBlendState

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Pipeline color blend state (used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice)).

<a id="description"></a>

## Description

This object is used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Array](class_array.md#class-array)[[RDPipelineColorBlendStateAttachment](class_rdpipelinecolorblendstateattachment.md#class-rdpipelinecolorblendstateattachment)] | [attachments](class_rdpipelinecolorblendstate.md#class-rdpipelinecolorblendstate-property-attachments) | `[]` |
| [Color](class_color.md#class-color) | [blend_constant](class_rdpipelinecolorblendstate.md#class-rdpipelinecolorblendstate-property-blend-constant) | `Color(0, 0, 0, 1)` |
| [bool](class_bool.md#class-bool) | [enable_logic_op](class_rdpipelinecolorblendstate.md#class-rdpipelinecolorblendstate-property-enable-logic-op) | `false` |
| [LogicOperation](class_renderingdevice.md#enum-renderingdevice-logicoperation) | [logic_op](class_rdpipelinecolorblendstate.md#class-rdpipelinecolorblendstate-property-logic-op) | `0` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-rdpipelinecolorblendstate-property-attachments"></a>

[Array](class_array.md#class-array)[[RDPipelineColorBlendStateAttachment](class_rdpipelinecolorblendstateattachment.md#class-rdpipelinecolorblendstateattachment)] **attachments** = `[]` [🔗](class_rdpipelinecolorblendstate.md#class-rdpipelinecolorblendstate-property-attachments)

- void **set_attachments**(value: [Array](class_array.md#class-array)[[RDPipelineColorBlendStateAttachment](class_rdpipelinecolorblendstateattachment.md#class-rdpipelinecolorblendstateattachment)])
- [Array](class_array.md#class-array)[[RDPipelineColorBlendStateAttachment](class_rdpipelinecolorblendstateattachment.md#class-rdpipelinecolorblendstateattachment)] **get_attachments**()

The attachments that are blended together.

---


<a id="class-rdpipelinecolorblendstate-property-blend-constant"></a>

[Color](class_color.md#class-color) **blend_constant** = `Color(0, 0, 0, 1)` [🔗](class_rdpipelinecolorblendstate.md#class-rdpipelinecolorblendstate-property-blend-constant)

- void **set_blend_constant**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_blend_constant**()

The constant color to blend with. See also [RenderingDevice.draw_list_set_blend_constants()](class_renderingdevice.md#class-renderingdevice-method-draw-list-set-blend-constants).

---


<a id="class-rdpipelinecolorblendstate-property-enable-logic-op"></a>

[bool](class_bool.md#class-bool) **enable_logic_op** = `false` [🔗](class_rdpipelinecolorblendstate.md#class-rdpipelinecolorblendstate-property-enable-logic-op)

- void **set_enable_logic_op**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_enable_logic_op**()

If `true`, performs the logic operation defined in [logic_op](class_rdpipelinecolorblendstate.md#class-rdpipelinecolorblendstate-property-logic-op).

---


<a id="class-rdpipelinecolorblendstate-property-logic-op"></a>

[LogicOperation](class_renderingdevice.md#enum-renderingdevice-logicoperation) **logic_op** = `0` [🔗](class_rdpipelinecolorblendstate.md#class-rdpipelinecolorblendstate-property-logic-op)

- void **set_logic_op**(value: [LogicOperation](class_renderingdevice.md#enum-renderingdevice-logicoperation))
- [LogicOperation](class_renderingdevice.md#enum-renderingdevice-logicoperation) **get_logic_op**()

The logic operation to perform for blending. Only effective if [enable_logic_op](class_rdpipelinecolorblendstate.md#class-rdpipelinecolorblendstate-property-enable-logic-op) is `true`.
