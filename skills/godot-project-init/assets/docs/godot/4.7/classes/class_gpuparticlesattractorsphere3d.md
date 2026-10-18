> Source: https://docs.godotengine.org/en/4.7/classes/class_gpuparticlesattractorsphere3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="gpuparticlesattractorsphere3d"></a>

<a id="class-gpuparticlesattractorsphere3d"></a>

# GPUParticlesAttractorSphere3D

**Inherits:** [GPUParticlesAttractor3D](class_gpuparticlesattractor3d.md#class-gpuparticlesattractor3d) **<** [VisualInstance3D](class_visualinstance3d.md#class-visualinstance3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A spheroid-shaped attractor that influences particles from [GPUParticles3D](class_gpuparticles3d.md#class-gpuparticles3d) nodes.

<a id="description"></a>

## Description

A spheroid-shaped attractor that influences particles from [GPUParticles3D](class_gpuparticles3d.md#class-gpuparticles3d) nodes. Can be used to attract particles towards its origin, or to push them away from its origin.

Particle attractors work in real-time and can be moved, rotated and scaled during gameplay. Unlike collision shapes, non-uniform scaling of attractors is also supported.

**Note:** Particle attractors only affect [GPUParticles3D](class_gpuparticles3d.md#class-gpuparticles3d), not [CPUParticles3D](class_cpuparticles3d.md#class-cpuparticles3d).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [radius](class_gpuparticlesattractorsphere3d.md#class-gpuparticlesattractorsphere3d-property-radius) | `1.0` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-gpuparticlesattractorsphere3d-property-radius"></a>

[float](class_float.md#class-float) **radius** = `1.0` [🔗](class_gpuparticlesattractorsphere3d.md#class-gpuparticlesattractorsphere3d-property-radius)

- void **set_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_radius**()

The attractor sphere's radius in 3D units.

**Note:** Stretched ellipses can be obtained by using non-uniform scaling on the **GPUParticlesAttractorSphere3D** node.
