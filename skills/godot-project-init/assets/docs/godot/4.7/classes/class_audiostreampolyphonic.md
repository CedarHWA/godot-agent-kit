> Source: https://docs.godotengine.org/en/4.7/classes/class_audiostreampolyphonic.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="audiostreampolyphonic"></a>

<a id="class-audiostreampolyphonic"></a>

# AudioStreamPolyphonic

**Inherits:** [AudioStream](class_audiostream.md#class-audiostream) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

AudioStream that lets the user play custom streams at any time from code, simultaneously using a single player.

<a id="description"></a>

## Description

AudioStream that lets the user play custom streams at any time from code, simultaneously using a single player.

Playback control is done via the [AudioStreamPlaybackPolyphonic](class_audiostreamplaybackpolyphonic.md#class-audiostreamplaybackpolyphonic) instance set inside the player, which can be obtained via [AudioStreamPlayer.get_stream_playback()](class_audiostreamplayer.md#class-audiostreamplayer-method-get-stream-playback), [AudioStreamPlayer2D.get_stream_playback()](class_audiostreamplayer2d.md#class-audiostreamplayer2d-method-get-stream-playback) or [AudioStreamPlayer3D.get_stream_playback()](class_audiostreamplayer3d.md#class-audiostreamplayer3d-method-get-stream-playback) methods. Obtaining the playback instance is only valid after the `stream` property is set as an **AudioStreamPolyphonic** in those players.

<a id="tutorials"></a>

## Tutorials

- [Audio streams](../tutorials/audio/audio_streams.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [polyphony](class_audiostreampolyphonic.md#class-audiostreampolyphonic-property-polyphony) | `32` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-audiostreampolyphonic-property-polyphony"></a>

[int](class_int.md#class-int) **polyphony** = `32` [🔗](class_audiostreampolyphonic.md#class-audiostreampolyphonic-property-polyphony)

- void **set_polyphony**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_polyphony**()

Maximum amount of simultaneous streams that can be played.
