> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodeparticleaccelerator.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodeparticleaccelerator"></a>

<a id="class-visualshadernodeparticleaccelerator"></a>

# VisualShaderNodeParticleAccelerator

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A visual shader node that accelerates particles.

<a id="description"></a>

## Description

Particle accelerator can be used in "process" step of particle shader. It will accelerate the particles. Connect it to the Velocity output port.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Mode](class_visualshadernodeparticleaccelerator.md#enum-visualshadernodeparticleaccelerator-mode) | [mode](class_visualshadernodeparticleaccelerator.md#class-visualshadernodeparticleaccelerator-property-mode) | `0` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-visualshadernodeparticleaccelerator-mode"></a>

enum **Mode**: [🔗](class_visualshadernodeparticleaccelerator.md#enum-visualshadernodeparticleaccelerator-mode)

<a id="class-visualshadernodeparticleaccelerator-constant-mode-linear"></a>

[Mode](class_visualshadernodeparticleaccelerator.md#enum-visualshadernodeparticleaccelerator-mode) **MODE_LINEAR** = `0`

The particles will be accelerated based on their velocity.

<a id="class-visualshadernodeparticleaccelerator-constant-mode-radial"></a>

[Mode](class_visualshadernodeparticleaccelerator.md#enum-visualshadernodeparticleaccelerator-mode) **MODE_RADIAL** = `1`

The particles will be accelerated towards or away from the center.

<a id="class-visualshadernodeparticleaccelerator-constant-mode-tangential"></a>

[Mode](class_visualshadernodeparticleaccelerator.md#enum-visualshadernodeparticleaccelerator-mode) **MODE_TANGENTIAL** = `2`

The particles will be accelerated tangentially to the radius vector from center to their position.

<a id="class-visualshadernodeparticleaccelerator-constant-mode-max"></a>

[Mode](class_visualshadernodeparticleaccelerator.md#enum-visualshadernodeparticleaccelerator-mode) **MODE_MAX** = `3`

Represents the size of the [Mode](class_visualshadernodeparticleaccelerator.md#enum-visualshadernodeparticleaccelerator-mode) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodeparticleaccelerator-property-mode"></a>

[Mode](class_visualshadernodeparticleaccelerator.md#enum-visualshadernodeparticleaccelerator-mode) **mode** = `0` [🔗](class_visualshadernodeparticleaccelerator.md#class-visualshadernodeparticleaccelerator-property-mode)

- void **set_mode**(value: [Mode](class_visualshadernodeparticleaccelerator.md#enum-visualshadernodeparticleaccelerator-mode))
- [Mode](class_visualshadernodeparticleaccelerator.md#enum-visualshadernodeparticleaccelerator-mode) **get_mode**()

Defines in what manner the particles will be accelerated.
