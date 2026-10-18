> Source: https://docs.godotengine.org/en/4.7/classes/class_gpuparticlesattractorbox3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="gpuparticlesattractorbox3d"></a>

<a id="class-gpuparticlesattractorbox3d"></a>

# GPUParticlesAttractorBox3D

**Inherits:** [GPUParticlesAttractor3D](class_gpuparticlesattractor3d.md#class-gpuparticlesattractor3d) **<** [VisualInstance3D](class_visualinstance3d.md#class-visualinstance3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A box-shaped attractor that influences particles from [GPUParticles3D](class_gpuparticles3d.md#class-gpuparticles3d) nodes.

<a id="description"></a>

## Description

A box-shaped attractor that influences particles from [GPUParticles3D](class_gpuparticles3d.md#class-gpuparticles3d) nodes. Can be used to attract particles towards its origin, or to push them away from its origin.

Particle attractors work in real-time and can be moved, rotated and scaled during gameplay. Unlike collision shapes, non-uniform scaling of attractors is also supported.

**Note:** Particle attractors only affect [GPUParticles3D](class_gpuparticles3d.md#class-gpuparticles3d), not [CPUParticles3D](class_cpuparticles3d.md#class-cpuparticles3d).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Vector3](class_vector3.md#class-vector3) | [size](class_gpuparticlesattractorbox3d.md#class-gpuparticlesattractorbox3d-property-size) | `Vector3(2, 2, 2)` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-gpuparticlesattractorbox3d-property-size"></a>

[Vector3](class_vector3.md#class-vector3) **size** = `Vector3(2, 2, 2)` [🔗](class_gpuparticlesattractorbox3d.md#class-gpuparticlesattractorbox3d-property-size)

- void **set_size**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_size**()

The attractor box's size in 3D units.
