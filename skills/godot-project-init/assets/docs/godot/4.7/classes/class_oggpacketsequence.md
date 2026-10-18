> Source: https://docs.godotengine.org/en/4.7/classes/class_oggpacketsequence.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="oggpacketsequence"></a>

<a id="class-oggpacketsequence"></a>

# OggPacketSequence

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A sequence of Ogg packets.

<a id="description"></a>

## Description

A sequence of Ogg packets.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [PackedInt64Array](class_packedint64array.md#class-packedint64array) | [granule_positions](class_oggpacketsequence.md#class-oggpacketsequence-property-granule-positions) | `PackedInt64Array()` |
| [Array](class_array.md#class-array)[[Array](class_array.md#class-array)] | [packet_data](class_oggpacketsequence.md#class-oggpacketsequence-property-packet-data) | `[]` |
| [float](class_float.md#class-float) | [sampling_rate](class_oggpacketsequence.md#class-oggpacketsequence-property-sampling-rate) | `0.0` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [float](class_float.md#class-float) | [get_length](class_oggpacketsequence.md#class-oggpacketsequence-method-get-length)() const |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-oggpacketsequence-property-granule-positions"></a>

[PackedInt64Array](class_packedint64array.md#class-packedint64array) **granule_positions** = `PackedInt64Array()` [🔗](class_oggpacketsequence.md#class-oggpacketsequence-property-granule-positions)

- void **set_packet_granule_positions**(value: [PackedInt64Array](class_packedint64array.md#class-packedint64array))
- [PackedInt64Array](class_packedint64array.md#class-packedint64array) **get_packet_granule_positions**()

Contains the granule positions for each page in this packet sequence.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt64Array](class_packedint64array.md#class-packedint64array) for more details.

---


<a id="class-oggpacketsequence-property-packet-data"></a>

[Array](class_array.md#class-array)[[Array](class_array.md#class-array)] **packet_data** = `[]` [🔗](class_oggpacketsequence.md#class-oggpacketsequence-property-packet-data)

- void **set_packet_data**(value: [Array](class_array.md#class-array)[[Array](class_array.md#class-array)])
- [Array](class_array.md#class-array)[[Array](class_array.md#class-array)] **get_packet_data**()

Contains the raw packets that make up this OggPacketSequence.

---


<a id="class-oggpacketsequence-property-sampling-rate"></a>

[float](class_float.md#class-float) **sampling_rate** = `0.0` [🔗](class_oggpacketsequence.md#class-oggpacketsequence-property-sampling-rate)

- void **set_sampling_rate**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_sampling_rate**()

Holds sample rate information about this sequence. Must be set by another class that actually understands the codec.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-oggpacketsequence-method-get-length"></a>

[float](class_float.md#class-float) **get_length**() const [🔗](class_oggpacketsequence.md#class-oggpacketsequence-method-get-length)

The length of this stream, in seconds.
