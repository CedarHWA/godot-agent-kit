> Source: https://docs.godotengine.org/en/4.7/classes/class_rdaccelerationstructureinstance.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="rdaccelerationstructureinstance"></a>

<a id="class-rdaccelerationstructureinstance"></a>

# RDAccelerationStructureInstance

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Acceleration structure instance (used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice)).

<a id="description"></a>

## Description

**RDAccelerationStructureInstance** describes an instance of a Bottom-Level Acceleration Structure (BLAS) used in the [RenderingDevice.tlas_build()](class_renderingdevice.md#class-renderingdevice-method-tlas-build) method.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [RID](class_rid.md#class-rid) | [blas](class_rdaccelerationstructureinstance.md#class-rdaccelerationstructureinstance-property-blas) | `RID()` |
| BitField[[AccelerationStructureInstanceFlagBits](class_renderingdevice.md#enum-renderingdevice-accelerationstructureinstanceflagbits)] | [flags](class_rdaccelerationstructureinstance.md#class-rdaccelerationstructureinstance-property-flags) | `0` |
| [int](class_int.md#class-int) | [hit_sbt_range](class_rdaccelerationstructureinstance.md#class-rdaccelerationstructureinstance-property-hit-sbt-range) | `0` |
| [int](class_int.md#class-int) | [id](class_rdaccelerationstructureinstance.md#class-rdaccelerationstructureinstance-property-id) | `0` |
| [int](class_int.md#class-int) | [mask](class_rdaccelerationstructureinstance.md#class-rdaccelerationstructureinstance-property-mask) | `255` |
| [Transform3D](class_transform3d.md#class-transform3d) | [transform](class_rdaccelerationstructureinstance.md#class-rdaccelerationstructureinstance-property-transform) | `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-rdaccelerationstructureinstance-property-blas"></a>

[RID](class_rid.md#class-rid) **blas** = `RID()` [🔗](class_rdaccelerationstructureinstance.md#class-rdaccelerationstructureinstance-property-blas)

- void **set_blas**(value: [RID](class_rid.md#class-rid))
- [RID](class_rid.md#class-rid) **get_blas**()

The BLAS referenced by this instance. If `null`, the instance is treated as a placeholder but still contributes to `gl_InstanceIndex` in GLSL.

---


<a id="class-rdaccelerationstructureinstance-property-flags"></a>

BitField[[AccelerationStructureInstanceFlagBits](class_renderingdevice.md#enum-renderingdevice-accelerationstructureinstanceflagbits)] **flags** = `0` [🔗](class_rdaccelerationstructureinstance.md#class-rdaccelerationstructureinstance-property-flags)

- void **set_flags**(value: BitField[[AccelerationStructureInstanceFlagBits](class_renderingdevice.md#enum-renderingdevice-accelerationstructureinstanceflagbits)])
- BitField[[AccelerationStructureInstanceFlagBits](class_renderingdevice.md#enum-renderingdevice-accelerationstructureinstanceflagbits)] **get_flags**()

Flags for the instance.

---


<a id="class-rdaccelerationstructureinstance-property-hit-sbt-range"></a>

[int](class_int.md#class-int) **hit_sbt_range** = `0` [🔗](class_rdaccelerationstructureinstance.md#class-rdaccelerationstructureinstance-property-hit-sbt-range)

- void **set_hit_sbt_range**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_hit_sbt_range**()

Hit shader binding table range used for this instance, allocated using the [RenderingDevice.hit_sbt_range_alloc()](class_renderingdevice.md#class-renderingdevice-method-hit-sbt-range-alloc) method.

---


<a id="class-rdaccelerationstructureinstance-property-id"></a>

[int](class_int.md#class-int) **id** = `0` [🔗](class_rdaccelerationstructureinstance.md#class-rdaccelerationstructureinstance-property-id)

- void **set_id**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_id**()

Custom instance ID that can be accessed in GLSL using `gl_InstanceCustomIndexEXT`.

---


<a id="class-rdaccelerationstructureinstance-property-mask"></a>

[int](class_int.md#class-int) **mask** = `255` [🔗](class_rdaccelerationstructureinstance.md#class-rdaccelerationstructureinstance-property-mask)

- void **set_mask**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_mask**()

Visibility mask used to control which rays can intersect this instance.

---


<a id="class-rdaccelerationstructureinstance-property-transform"></a>

[Transform3D](class_transform3d.md#class-transform3d) **transform** = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)` [🔗](class_rdaccelerationstructureinstance.md#class-rdaccelerationstructureinstance-property-transform)

- void **set_transform**(value: [Transform3D](class_transform3d.md#class-transform3d))
- [Transform3D](class_transform3d.md#class-transform3d) **get_transform**()

Transform applied to the referenced BLAS for this instance.
