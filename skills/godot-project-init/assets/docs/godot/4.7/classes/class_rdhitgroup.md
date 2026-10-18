> Source: https://docs.godotengine.org/en/4.7/classes/class_rdhitgroup.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="rdhitgroup"></a>

<a id="class-rdhitgroup"></a>

# RDHitGroup

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Hit group (used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice)).

<a id="description"></a>

## Description

Defines a hit group for use with [RenderingDevice.raytracing_pipeline_create()](class_renderingdevice.md#class-renderingdevice-method-raytracing-pipeline-create).

A hit group combines shaders that are executed when a ray intersects geometry. It may include a closest-hit shader, any-hit shader, and intersection shader.

Hit groups are referenced by index when populating hit shader binding tables using [RenderingDevice.hit_sbt_range_update()](class_renderingdevice.md#class-renderingdevice-method-hit-sbt-range-update).

<a id="properties"></a>

## Properties

|  |  |
| --- | --- |
| [RDPipelineShader](class_rdpipelineshader.md#class-rdpipelineshader) | [any_hit_shader](class_rdhitgroup.md#class-rdhitgroup-property-any-hit-shader) |
| [RDPipelineShader](class_rdpipelineshader.md#class-rdpipelineshader) | [closest_hit_shader](class_rdhitgroup.md#class-rdhitgroup-property-closest-hit-shader) |
| [RDPipelineShader](class_rdpipelineshader.md#class-rdpipelineshader) | [intersection_shader](class_rdhitgroup.md#class-rdhitgroup-property-intersection-shader) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-rdhitgroup-property-any-hit-shader"></a>

[RDPipelineShader](class_rdpipelineshader.md#class-rdpipelineshader) **any_hit_shader** [🔗](class_rdhitgroup.md#class-rdhitgroup-property-any-hit-shader)

- void **set_any_hit_shader**(value: [RDPipelineShader](class_rdpipelineshader.md#class-rdpipelineshader))
- [RDPipelineShader](class_rdpipelineshader.md#class-rdpipelineshader) **get_any_hit_shader**()

Any-hit shader for this hit group. Executed for each potential intersection. Can be `null`.

---


<a id="class-rdhitgroup-property-closest-hit-shader"></a>

[RDPipelineShader](class_rdpipelineshader.md#class-rdpipelineshader) **closest_hit_shader** [🔗](class_rdhitgroup.md#class-rdhitgroup-property-closest-hit-shader)

- void **set_closest_hit_shader**(value: [RDPipelineShader](class_rdpipelineshader.md#class-rdpipelineshader))
- [RDPipelineShader](class_rdpipelineshader.md#class-rdpipelineshader) **get_closest_hit_shader**()

Closest-hit shader for this hit group. Executed for the closest intersection. Can be `null`.

---


<a id="class-rdhitgroup-property-intersection-shader"></a>

[RDPipelineShader](class_rdpipelineshader.md#class-rdpipelineshader) **intersection_shader** [🔗](class_rdhitgroup.md#class-rdhitgroup-property-intersection-shader)

- void **set_intersection_shader**(value: [RDPipelineShader](class_rdpipelineshader.md#class-rdpipelineshader))
- [RDPipelineShader](class_rdpipelineshader.md#class-rdpipelineshader) **get_intersection_shader**()

Intersection shader for this hit group. Required for non-triangle geometry. Must be `null` when using for triangle geometry.
