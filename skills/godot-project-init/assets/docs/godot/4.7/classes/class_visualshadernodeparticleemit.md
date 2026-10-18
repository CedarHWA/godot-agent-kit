> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodeparticleemit.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodeparticleemit"></a>

<a id="class-visualshadernodeparticleemit"></a>

# VisualShaderNodeParticleEmit

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A visual shader node that forces to emit a particle from a sub-emitter.

<a id="description"></a>

## Description

This node internally calls `emit_subparticle` shader method. It will emit a particle from the configured sub-emitter and also allows to customize how its emitted. Requires a sub-emitter assigned to the particles node with this shader.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [EmitFlags](class_visualshadernodeparticleemit.md#enum-visualshadernodeparticleemit-emitflags) | [flags](class_visualshadernodeparticleemit.md#class-visualshadernodeparticleemit-property-flags) | `31` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-visualshadernodeparticleemit-emitflags"></a>

enum **EmitFlags**: [🔗](class_visualshadernodeparticleemit.md#enum-visualshadernodeparticleemit-emitflags)

<a id="class-visualshadernodeparticleemit-constant-emit-flag-position"></a>

[EmitFlags](class_visualshadernodeparticleemit.md#enum-visualshadernodeparticleemit-emitflags) **EMIT_FLAG_POSITION** = `1`

If enabled, the particle starts with the position defined by this node.

<a id="class-visualshadernodeparticleemit-constant-emit-flag-rot-scale"></a>

[EmitFlags](class_visualshadernodeparticleemit.md#enum-visualshadernodeparticleemit-emitflags) **EMIT_FLAG_ROT_SCALE** = `2`

If enabled, the particle starts with the rotation and scale defined by this node.

<a id="class-visualshadernodeparticleemit-constant-emit-flag-velocity"></a>

[EmitFlags](class_visualshadernodeparticleemit.md#enum-visualshadernodeparticleemit-emitflags) **EMIT_FLAG_VELOCITY** = `4`

If enabled,the particle starts with the velocity defined by this node.

<a id="class-visualshadernodeparticleemit-constant-emit-flag-color"></a>

[EmitFlags](class_visualshadernodeparticleemit.md#enum-visualshadernodeparticleemit-emitflags) **EMIT_FLAG_COLOR** = `8`

If enabled, the particle starts with the color defined by this node.

<a id="class-visualshadernodeparticleemit-constant-emit-flag-custom"></a>

[EmitFlags](class_visualshadernodeparticleemit.md#enum-visualshadernodeparticleemit-emitflags) **EMIT_FLAG_CUSTOM** = `16`

If enabled, the particle starts with the `CUSTOM` data defined by this node.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodeparticleemit-property-flags"></a>

[EmitFlags](class_visualshadernodeparticleemit.md#enum-visualshadernodeparticleemit-emitflags) **flags** = `31` [🔗](class_visualshadernodeparticleemit.md#class-visualshadernodeparticleemit-property-flags)

- void **set_flags**(value: [EmitFlags](class_visualshadernodeparticleemit.md#enum-visualshadernodeparticleemit-emitflags))
- [EmitFlags](class_visualshadernodeparticleemit.md#enum-visualshadernodeparticleemit-emitflags) **get_flags**()

Flags used to override the properties defined in the sub-emitter's process material.
