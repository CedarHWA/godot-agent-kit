> Source: https://docs.godotengine.org/en/4.7/classes/class_audiostreamsynchronized.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="audiostreamsynchronized"></a>

<a id="class-audiostreamsynchronized"></a>

# AudioStreamSynchronized

**Inherits:** [AudioStream](class_audiostream.md#class-audiostream) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Stream that can be fitted with sub-streams, which will be played in-sync.

<a id="description"></a>

## Description

This is a stream that can be fitted with sub-streams, which will be played in-sync. The streams begin at exactly the same time when play is pressed, and will end when the last of them ends. If one of the sub-streams loops, then playback will continue.

<a id="tutorials"></a>

## Tutorials

- [Audio streams](../tutorials/audio/audio_streams.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [stream_count](class_audiostreamsynchronized.md#class-audiostreamsynchronized-property-stream-count) | `0` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [AudioStream](class_audiostream.md#class-audiostream) | [get_sync_stream](class_audiostreamsynchronized.md#class-audiostreamsynchronized-method-get-sync-stream)(stream_index: [int](class_int.md#class-int)) const |
| [float](class_float.md#class-float) | [get_sync_stream_volume](class_audiostreamsynchronized.md#class-audiostreamsynchronized-method-get-sync-stream-volume)(stream_index: [int](class_int.md#class-int)) const |
| void | [set_sync_stream](class_audiostreamsynchronized.md#class-audiostreamsynchronized-method-set-sync-stream)(stream_index: [int](class_int.md#class-int), audio_stream: [AudioStream](class_audiostream.md#class-audiostream)) |
| void | [set_sync_stream_volume](class_audiostreamsynchronized.md#class-audiostreamsynchronized-method-set-sync-stream-volume)(stream_index: [int](class_int.md#class-int), volume_db: [float](class_float.md#class-float)) |

---


<a id="constants"></a>

## Constants

<a id="class-audiostreamsynchronized-constant-max-streams"></a>

**MAX_STREAMS** = `32` [🔗](class_audiostreamsynchronized.md#class-audiostreamsynchronized-constant-max-streams)

Maximum amount of streams that can be synchronized.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-audiostreamsynchronized-property-stream-count"></a>

[int](class_int.md#class-int) **stream_count** = `0` [🔗](class_audiostreamsynchronized.md#class-audiostreamsynchronized-property-stream-count)

- void **set_stream_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_stream_count**()

Set the total amount of streams that will be played back synchronized.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-audiostreamsynchronized-method-get-sync-stream"></a>

[AudioStream](class_audiostream.md#class-audiostream) **get_sync_stream**(stream_index: [int](class_int.md#class-int)) const [🔗](class_audiostreamsynchronized.md#class-audiostreamsynchronized-method-get-sync-stream)

Get one of the synchronized streams, by index.

---


<a id="class-audiostreamsynchronized-method-get-sync-stream-volume"></a>

[float](class_float.md#class-float) **get_sync_stream_volume**(stream_index: [int](class_int.md#class-int)) const [🔗](class_audiostreamsynchronized.md#class-audiostreamsynchronized-method-get-sync-stream-volume)

Get the volume of one of the synchronized streams, by index.

---


<a id="class-audiostreamsynchronized-method-set-sync-stream"></a>

void **set_sync_stream**(stream_index: [int](class_int.md#class-int), audio_stream: [AudioStream](class_audiostream.md#class-audiostream)) [🔗](class_audiostreamsynchronized.md#class-audiostreamsynchronized-method-set-sync-stream)

Set one of the synchronized streams, by index.

---


<a id="class-audiostreamsynchronized-method-set-sync-stream-volume"></a>

void **set_sync_stream_volume**(stream_index: [int](class_int.md#class-int), volume_db: [float](class_float.md#class-float)) [🔗](class_audiostreamsynchronized.md#class-audiostreamsynchronized-method-set-sync-stream-volume)

Set the volume of one of the synchronized streams, by index.
