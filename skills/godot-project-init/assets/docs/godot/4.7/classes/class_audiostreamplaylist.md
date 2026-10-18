> Source: https://docs.godotengine.org/en/4.7/classes/class_audiostreamplaylist.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="audiostreamplaylist"></a>

<a id="class-audiostreamplaylist"></a>

# AudioStreamPlaylist

**Inherits:** [AudioStream](class_audiostream.md#class-audiostream) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

[AudioStream](class_audiostream.md#class-audiostream) that includes sub-streams and plays them back like a playlist.

<a id="description"></a>

## Description

An audio stream that can play back sub-streams in sequence. Streams can be added to the Playlist with [set_list_stream()](class_audiostreamplaylist.md#class-audiostreamplaylist-method-set-list-stream), and shuffled with [shuffle](class_audiostreamplaylist.md#class-audiostreamplaylist-property-shuffle).

<a id="tutorials"></a>

## Tutorials

- [Audio streams](../tutorials/audio/audio_streams.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [fade_time](class_audiostreamplaylist.md#class-audiostreamplaylist-property-fade-time) | `0.3` |
| [bool](class_bool.md#class-bool) | [loop](class_audiostreamplaylist.md#class-audiostreamplaylist-property-loop) | `true` |
| [bool](class_bool.md#class-bool) | [shuffle](class_audiostreamplaylist.md#class-audiostreamplaylist-property-shuffle) | `false` |
| [int](class_int.md#class-int) | [stream_count](class_audiostreamplaylist.md#class-audiostreamplaylist-property-stream-count) | `0` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [float](class_float.md#class-float) | [get_bpm](class_audiostreamplaylist.md#class-audiostreamplaylist-method-get-bpm)() const |
| [AudioStream](class_audiostream.md#class-audiostream) | [get_list_stream](class_audiostreamplaylist.md#class-audiostreamplaylist-method-get-list-stream)(stream_index: [int](class_int.md#class-int)) const |
| void | [set_list_stream](class_audiostreamplaylist.md#class-audiostreamplaylist-method-set-list-stream)(stream_index: [int](class_int.md#class-int), audio_stream: [AudioStream](class_audiostream.md#class-audiostream)) |

---


<a id="constants"></a>

## Constants

<a id="class-audiostreamplaylist-constant-max-streams"></a>

**MAX_STREAMS** = `64` [🔗](class_audiostreamplaylist.md#class-audiostreamplaylist-constant-max-streams)

Maximum amount of streams supported in the playlist.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-audiostreamplaylist-property-fade-time"></a>

[float](class_float.md#class-float) **fade_time** = `0.3` [🔗](class_audiostreamplaylist.md#class-audiostreamplaylist-property-fade-time)

- void **set_fade_time**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_fade_time**()

Fade time used when a stream ends, when going to the next one. Streams are expected to have an extra bit of audio after the end to help with fading.

---


<a id="class-audiostreamplaylist-property-loop"></a>

[bool](class_bool.md#class-bool) **loop** = `true` [🔗](class_audiostreamplaylist.md#class-audiostreamplaylist-property-loop)

- void **set_loop**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **has_loop**()

If `true`, the playlist will loop, otherwise the playlist will end when the last stream is finished.

---


<a id="class-audiostreamplaylist-property-shuffle"></a>

[bool](class_bool.md#class-bool) **shuffle** = `false` [🔗](class_audiostreamplaylist.md#class-audiostreamplaylist-property-shuffle)

- void **set_shuffle**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_shuffle**()

If `true`, the playlist will shuffle each time playback starts and each time it loops.

---


<a id="class-audiostreamplaylist-property-stream-count"></a>

[int](class_int.md#class-int) **stream_count** = `0` [🔗](class_audiostreamplaylist.md#class-audiostreamplaylist-property-stream-count)

- void **set_stream_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_stream_count**()

Amount of streams in the playlist.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-audiostreamplaylist-method-get-bpm"></a>

[float](class_float.md#class-float) **get_bpm**() const [🔗](class_audiostreamplaylist.md#class-audiostreamplaylist-method-get-bpm)

Returns the BPM of the playlist, which can vary depending on the clip being played.

---


<a id="class-audiostreamplaylist-method-get-list-stream"></a>

[AudioStream](class_audiostream.md#class-audiostream) **get_list_stream**(stream_index: [int](class_int.md#class-int)) const [🔗](class_audiostreamplaylist.md#class-audiostreamplaylist-method-get-list-stream)

Returns the stream at playback position index.

---


<a id="class-audiostreamplaylist-method-set-list-stream"></a>

void **set_list_stream**(stream_index: [int](class_int.md#class-int), audio_stream: [AudioStream](class_audiostream.md#class-audiostream)) [🔗](class_audiostreamplaylist.md#class-audiostreamplaylist-method-set-list-stream)

Sets the stream at playback position index.
