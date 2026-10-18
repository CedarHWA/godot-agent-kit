> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodeparticlemeshemitter.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodeparticlemeshemitter"></a>

<a id="class-visualshadernodeparticlemeshemitter"></a>

# VisualShaderNodeParticleMeshEmitter

**Inherits:** [VisualShaderNodeParticleEmitter](class_visualshadernodeparticleemitter.md#class-visualshadernodeparticleemitter) **<** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A visual shader node that makes particles emitted in a shape defined by a [Mesh](class_mesh.md#class-mesh).

<a id="description"></a>

## Description

[VisualShaderNodeParticleEmitter](class_visualshadernodeparticleemitter.md#class-visualshadernodeparticleemitter) that makes the particles emitted in a shape of the assigned [mesh](class_visualshadernodeparticlemeshemitter.md#class-visualshadernodeparticlemeshemitter-property-mesh). It will emit from the mesh's surfaces, either all or only the specified one.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Mesh](class_mesh.md#class-mesh) | [mesh](class_visualshadernodeparticlemeshemitter.md#class-visualshadernodeparticlemeshemitter-property-mesh) |  |
| [int](class_int.md#class-int) | [surface_index](class_visualshadernodeparticlemeshemitter.md#class-visualshadernodeparticlemeshemitter-property-surface-index) | `0` |
| [bool](class_bool.md#class-bool) | [use_all_surfaces](class_visualshadernodeparticlemeshemitter.md#class-visualshadernodeparticlemeshemitter-property-use-all-surfaces) | `true` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodeparticlemeshemitter-property-mesh"></a>

[Mesh](class_mesh.md#class-mesh) **mesh** [🔗](class_visualshadernodeparticlemeshemitter.md#class-visualshadernodeparticlemeshemitter-property-mesh)

- void **set_mesh**(value: [Mesh](class_mesh.md#class-mesh))
- [Mesh](class_mesh.md#class-mesh) **get_mesh**()

The [Mesh](class_mesh.md#class-mesh) that defines emission shape.

---


<a id="class-visualshadernodeparticlemeshemitter-property-surface-index"></a>

[int](class_int.md#class-int) **surface_index** = `0` [🔗](class_visualshadernodeparticlemeshemitter.md#class-visualshadernodeparticlemeshemitter-property-surface-index)

- void **set_surface_index**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_surface_index**()

Index of the surface that emits particles. [use_all_surfaces](class_visualshadernodeparticlemeshemitter.md#class-visualshadernodeparticlemeshemitter-property-use-all-surfaces) must be `false` for this to take effect.

---


<a id="class-visualshadernodeparticlemeshemitter-property-use-all-surfaces"></a>

[bool](class_bool.md#class-bool) **use_all_surfaces** = `true` [🔗](class_visualshadernodeparticlemeshemitter.md#class-visualshadernodeparticlemeshemitter-property-use-all-surfaces)

- void **set_use_all_surfaces**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_use_all_surfaces**()

If `true`, the particles will emit from all surfaces of the mesh.
