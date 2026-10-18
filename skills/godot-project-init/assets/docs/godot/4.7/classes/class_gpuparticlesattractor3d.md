> Source: https://docs.godotengine.org/en/4.7/classes/class_gpuparticlesattractor3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="gpuparticlesattractor3d"></a>

<a id="class-gpuparticlesattractor3d"></a>

# GPUParticlesAttractor3D

**Inherits:** [VisualInstance3D](class_visualinstance3d.md#class-visualinstance3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [GPUParticlesAttractorBox3D](class_gpuparticlesattractorbox3d.md#class-gpuparticlesattractorbox3d), [GPUParticlesAttractorSphere3D](class_gpuparticlesattractorsphere3d.md#class-gpuparticlesattractorsphere3d), [GPUParticlesAttractorVectorField3D](class_gpuparticlesattractorvectorfield3d.md#class-gpuparticlesattractorvectorfield3d)

Abstract base class for 3D particle attractors.

<a id="description"></a>

## Description

Particle attractors can be used to attract particles towards the attractor's origin, or to push them away from the attractor's origin.

Particle attractors work in real-time and can be moved, rotated and scaled during gameplay. Unlike collision shapes, non-uniform scaling of attractors is also supported.

Attractors can be temporarily disabled by hiding them, or by setting their [strength](class_gpuparticlesattractor3d.md#class-gpuparticlesattractor3d-property-strength) to `0.0`.

**Note:** Particle attractors only affect [GPUParticles3D](class_gpuparticles3d.md#class-gpuparticles3d), not [CPUParticles3D](class_cpuparticles3d.md#class-cpuparticles3d).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [attenuation](class_gpuparticlesattractor3d.md#class-gpuparticlesattractor3d-property-attenuation) | `1.0` |
| [int](class_int.md#class-int) | [cull_mask](class_gpuparticlesattractor3d.md#class-gpuparticlesattractor3d-property-cull-mask) | `4294967295` |
| [float](class_float.md#class-float) | [directionality](class_gpuparticlesattractor3d.md#class-gpuparticlesattractor3d-property-directionality) | `0.0` |
| [float](class_float.md#class-float) | [strength](class_gpuparticlesattractor3d.md#class-gpuparticlesattractor3d-property-strength) | `1.0` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-gpuparticlesattractor3d-property-attenuation"></a>

[float](class_float.md#class-float) **attenuation** = `1.0` [🔗](class_gpuparticlesattractor3d.md#class-gpuparticlesattractor3d-property-attenuation)

- void **set_attenuation**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_attenuation**()

The particle attractor's attenuation. Higher values result in more gradual pushing of particles as they come closer to the attractor's origin. Zero or negative values will cause particles to be pushed very fast as soon as the touch the attractor's edges.

---


<a id="class-gpuparticlesattractor3d-property-cull-mask"></a>

[int](class_int.md#class-int) **cull_mask** = `4294967295` [🔗](class_gpuparticlesattractor3d.md#class-gpuparticlesattractor3d-property-cull-mask)

- void **set_cull_mask**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_cull_mask**()

The particle rendering layers ([VisualInstance3D.layers](class_visualinstance3d.md#class-visualinstance3d-property-layers)) that will be affected by the attractor. By default, all particles are affected by an attractor.

After configuring particle nodes accordingly, specific layers can be unchecked to prevent certain particles from being affected by attractors. For example, this can be used if you're using an attractor as part of a spell effect but don't want the attractor to affect unrelated weather particles at the same position.

Particle attraction can also be disabled on a per-process material basis by setting [ParticleProcessMaterial.attractor_interaction_enabled](class_particleprocessmaterial.md#class-particleprocessmaterial-property-attractor-interaction-enabled) on the [GPUParticles3D](class_gpuparticles3d.md#class-gpuparticles3d) node.

---


<a id="class-gpuparticlesattractor3d-property-directionality"></a>

[float](class_float.md#class-float) **directionality** = `0.0` [🔗](class_gpuparticlesattractor3d.md#class-gpuparticlesattractor3d-property-directionality)

- void **set_directionality**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_directionality**()

Adjusts how directional the attractor is. At `0.0`, the attractor is not directional at all: it will attract particles towards its center. At `1.0`, the attractor is fully directional: particles will always be pushed towards local -Z (or +Z if [strength](class_gpuparticlesattractor3d.md#class-gpuparticlesattractor3d-property-strength) is negative).

**Note:** If [directionality](class_gpuparticlesattractor3d.md#class-gpuparticlesattractor3d-property-directionality) is greater than `0.0`, the direction in which particles are pushed can be changed by rotating the **GPUParticlesAttractor3D** node.

---


<a id="class-gpuparticlesattractor3d-property-strength"></a>

[float](class_float.md#class-float) **strength** = `1.0` [🔗](class_gpuparticlesattractor3d.md#class-gpuparticlesattractor3d-property-strength)

- void **set_strength**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_strength**()

Adjusts the strength of the attractor. If [strength](class_gpuparticlesattractor3d.md#class-gpuparticlesattractor3d-property-strength) is negative, particles will be pushed in the opposite direction. Particles will be pushed *away* from the attractor's origin if [directionality](class_gpuparticlesattractor3d.md#class-gpuparticlesattractor3d-property-directionality) is `0.0`, or towards local +Z if [directionality](class_gpuparticlesattractor3d.md#class-gpuparticlesattractor3d-property-directionality) is greater than `0.0`.
