> Source: https://docs.godotengine.org/en/4.7/classes/class_gpuparticlesattractorvectorfield3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="gpuparticlesattractorvectorfield3d"></a>

<a id="class-gpuparticlesattractorvectorfield3d"></a>

# GPUParticlesAttractorVectorField3D

**Inherits:** [GPUParticlesAttractor3D](class_gpuparticlesattractor3d.md#class-gpuparticlesattractor3d) **<** [VisualInstance3D](class_visualinstance3d.md#class-visualinstance3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A box-shaped attractor with varying directions and strengths defined in it that influences particles from [GPUParticles3D](class_gpuparticles3d.md#class-gpuparticles3d) nodes.

<a id="description"></a>

## Description

A box-shaped attractor with varying directions and strengths defined in it that influences particles from [GPUParticles3D](class_gpuparticles3d.md#class-gpuparticles3d) nodes.

Unlike [GPUParticlesAttractorBox3D](class_gpuparticlesattractorbox3d.md#class-gpuparticlesattractorbox3d), **GPUParticlesAttractorVectorField3D** uses a [texture](class_gpuparticlesattractorvectorfield3d.md#class-gpuparticlesattractorvectorfield3d-property-texture) to affect attraction strength within the box. This can be used to create complex attraction scenarios where particles travel in different directions depending on their location. This can be useful for weather effects such as sandstorms.

Particle attractors work in real-time and can be moved, rotated and scaled during gameplay. Unlike collision shapes, non-uniform scaling of attractors is also supported.

**Note:** Particle attractors only affect [GPUParticles3D](class_gpuparticles3d.md#class-gpuparticles3d), not [CPUParticles3D](class_cpuparticles3d.md#class-cpuparticles3d).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Vector3](class_vector3.md#class-vector3) | [size](class_gpuparticlesattractorvectorfield3d.md#class-gpuparticlesattractorvectorfield3d-property-size) | `Vector3(2, 2, 2)` |
| [Texture3D](class_texture3d.md#class-texture3d) | [texture](class_gpuparticlesattractorvectorfield3d.md#class-gpuparticlesattractorvectorfield3d-property-texture) |  |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-gpuparticlesattractorvectorfield3d-property-size"></a>

[Vector3](class_vector3.md#class-vector3) **size** = `Vector3(2, 2, 2)` [🔗](class_gpuparticlesattractorvectorfield3d.md#class-gpuparticlesattractorvectorfield3d-property-size)

- void **set_size**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_size**()

The size of the vector field box in 3D units.

---


<a id="class-gpuparticlesattractorvectorfield3d-property-texture"></a>

[Texture3D](class_texture3d.md#class-texture3d) **texture** [🔗](class_gpuparticlesattractorvectorfield3d.md#class-gpuparticlesattractorvectorfield3d-property-texture)

- void **set_texture**(value: [Texture3D](class_texture3d.md#class-texture3d))
- [Texture3D](class_texture3d.md#class-texture3d) **get_texture**()

The 3D texture to be used. Values are linearly interpolated between the texture's pixels.

**Note:** To get better performance, the 3D texture's resolution should reflect the [size](class_gpuparticlesattractorvectorfield3d.md#class-gpuparticlesattractorvectorfield3d-property-size) of the attractor. Since particle attraction is usually low-frequency data, the texture can be kept at a low resolution such as 64×64×64.
