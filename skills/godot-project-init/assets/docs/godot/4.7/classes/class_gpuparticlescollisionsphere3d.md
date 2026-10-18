> Source: https://docs.godotengine.org/en/4.7/classes/class_gpuparticlescollisionsphere3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="gpuparticlescollisionsphere3d"></a>

<a id="class-gpuparticlescollisionsphere3d"></a>

# GPUParticlesCollisionSphere3D

**Inherits:** [GPUParticlesCollision3D](class_gpuparticlescollision3d.md#class-gpuparticlescollision3d) **<** [VisualInstance3D](class_visualinstance3d.md#class-visualinstance3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A sphere-shaped 3D particle collision shape affecting [GPUParticles3D](class_gpuparticles3d.md#class-gpuparticles3d) nodes.

<a id="description"></a>

## Description

A sphere-shaped 3D particle collision shape affecting [GPUParticles3D](class_gpuparticles3d.md#class-gpuparticles3d) nodes.

Particle collision shapes work in real-time and can be moved, rotated and scaled during gameplay. Unlike attractors, non-uniform scaling of collision shapes is *not* supported.

**Note:** [ParticleProcessMaterial.collision_mode](class_particleprocessmaterial.md#class-particleprocessmaterial-property-collision-mode) must be [ParticleProcessMaterial.COLLISION_RIGID](class_particleprocessmaterial.md#class-particleprocessmaterial-constant-collision-rigid) or [ParticleProcessMaterial.COLLISION_HIDE_ON_CONTACT](class_particleprocessmaterial.md#class-particleprocessmaterial-constant-collision-hide-on-contact) on the [GPUParticles3D](class_gpuparticles3d.md#class-gpuparticles3d)'s process material for collision to work.

**Note:** Particle collision only affects [GPUParticles3D](class_gpuparticles3d.md#class-gpuparticles3d), not [CPUParticles3D](class_cpuparticles3d.md#class-cpuparticles3d).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [radius](class_gpuparticlescollisionsphere3d.md#class-gpuparticlescollisionsphere3d-property-radius) | `1.0` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-gpuparticlescollisionsphere3d-property-radius"></a>

[float](class_float.md#class-float) **radius** = `1.0` [🔗](class_gpuparticlescollisionsphere3d.md#class-gpuparticlescollisionsphere3d-property-radius)

- void **set_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_radius**()

The collision sphere's radius in 3D units.
