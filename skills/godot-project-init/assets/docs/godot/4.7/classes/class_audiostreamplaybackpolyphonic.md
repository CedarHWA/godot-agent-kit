> Source: https://docs.godotengine.org/en/4.7/classes/class_audiostreamplaybackpolyphonic.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="audiostreamplaybackpolyphonic"></a>

<a id="class-audiostreamplaybackpolyphonic"></a>

# AudioStreamPlaybackPolyphonic

**Inherits:** [AudioStreamPlayback](class_audiostreamplayback.md#class-audiostreamplayback) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Playback instance for [AudioStreamPolyphonic](class_audiostreampolyphonic.md#class-audiostreampolyphonic).

<a id="description"></a>

## Description

Playback instance for [AudioStreamPolyphonic](class_audiostreampolyphonic.md#class-audiostreampolyphonic). After setting the `stream` property of [AudioStreamPlayer](class_audiostreamplayer.md#class-audiostreamplayer), [AudioStreamPlayer2D](class_audiostreamplayer2d.md#class-audiostreamplayer2d), or [AudioStreamPlayer3D](class_audiostreamplayer3d.md#class-audiostreamplayer3d), the playback instance can be obtained by calling [AudioStreamPlayer.get_stream_playback()](class_audiostreamplayer.md#class-audiostreamplayer-method-get-stream-playback), [AudioStreamPlayer2D.get_stream_playback()](class_audiostreamplayer2d.md#class-audiostreamplayer2d-method-get-stream-playback) or [AudioStreamPlayer3D.get_stream_playback()](class_audiostreamplayer3d.md#class-audiostreamplayer3d-method-get-stream-playback) methods.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [is_stream_playing](class_audiostreamplaybackpolyphonic.md#class-audiostreamplaybackpolyphonic-method-is-stream-playing)(stream: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [play_stream](class_audiostreamplaybackpolyphonic.md#class-audiostreamplaybackpolyphonic-method-play-stream)(stream: [AudioStream](class_audiostream.md#class-audiostream), from_offset: [float](class_float.md#class-float) = 0, volume_db: [float](class_float.md#class-float) = 0, pitch_scale: [float](class_float.md#class-float) = 1.0, playback_type: [PlaybackType](class_audioserver.md#enum-audioserver-playbacktype) = 0, bus: [StringName](class_stringname.md#class-stringname) = &"Master") |
| void | [set_stream_pitch_scale](class_audiostreamplaybackpolyphonic.md#class-audiostreamplaybackpolyphonic-method-set-stream-pitch-scale)(stream: [int](class_int.md#class-int), pitch_scale: [float](class_float.md#class-float)) |
| void | [set_stream_volume](class_audiostreamplaybackpolyphonic.md#class-audiostreamplaybackpolyphonic-method-set-stream-volume)(stream: [int](class_int.md#class-int), volume_db: [float](class_float.md#class-float)) |
| void | [stop_stream](class_audiostreamplaybackpolyphonic.md#class-audiostreamplaybackpolyphonic-method-stop-stream)(stream: [int](class_int.md#class-int)) |

---


<a id="constants"></a>

## Constants

<a id="class-audiostreamplaybackpolyphonic-constant-invalid-id"></a>

**INVALID_ID** = `-1` [🔗](class_audiostreamplaybackpolyphonic.md#class-audiostreamplaybackpolyphonic-constant-invalid-id)

Returned by [play_stream()](class_audiostreamplaybackpolyphonic.md#class-audiostreamplaybackpolyphonic-method-play-stream) in case it could not allocate a stream for playback.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-audiostreamplaybackpolyphonic-method-is-stream-playing"></a>

[bool](class_bool.md#class-bool) **is_stream_playing**(stream: [int](class_int.md#class-int)) const [🔗](class_audiostreamplaybackpolyphonic.md#class-audiostreamplaybackpolyphonic-method-is-stream-playing)

Returns `true` if the stream associated with the given integer ID is still playing. Check [play_stream()](class_audiostreamplaybackpolyphonic.md#class-audiostreamplaybackpolyphonic-method-play-stream) for information on when this ID becomes invalid.

---


<a id="class-audiostreamplaybackpolyphonic-method-play-stream"></a>

[int](class_int.md#class-int) **play_stream**(stream: [AudioStream](class_audiostream.md#class-audiostream), from_offset: [float](class_float.md#class-float) = 0, volume_db: [float](class_float.md#class-float) = 0, pitch_scale: [float](class_float.md#class-float) = 1.0, playback_type: [PlaybackType](class_audioserver.md#enum-audioserver-playbacktype) = 0, bus: [StringName](class_stringname.md#class-stringname) = &"Master") [🔗](class_audiostreamplaybackpolyphonic.md#class-audiostreamplaybackpolyphonic-method-play-stream)

Play an [AudioStream](class_audiostream.md#class-audiostream) at a given offset, volume, pitch scale, playback type, and bus. Playback starts immediately.

The return value is a unique integer ID that is associated to this playback stream and which can be used to control it.

This ID becomes invalid when the stream ends (if it does not loop), when the **AudioStreamPlaybackPolyphonic** is stopped, or when [stop_stream()](class_audiostreamplaybackpolyphonic.md#class-audiostreamplaybackpolyphonic-method-stop-stream) is called.

This function returns [INVALID_ID](class_audiostreamplaybackpolyphonic.md#class-audiostreamplaybackpolyphonic-constant-invalid-id) if the amount of streams currently playing equals [AudioStreamPolyphonic.polyphony](class_audiostreampolyphonic.md#class-audiostreampolyphonic-property-polyphony). If you need a higher amount of maximum polyphony, raise this value.

---


<a id="class-audiostreamplaybackpolyphonic-method-set-stream-pitch-scale"></a>

void **set_stream_pitch_scale**(stream: [int](class_int.md#class-int), pitch_scale: [float](class_float.md#class-float)) [🔗](class_audiostreamplaybackpolyphonic.md#class-audiostreamplaybackpolyphonic-method-set-stream-pitch-scale)

Change the stream pitch scale. The `stream` argument is an integer ID returned by [play_stream()](class_audiostreamplaybackpolyphonic.md#class-audiostreamplaybackpolyphonic-method-play-stream).

---


<a id="class-audiostreamplaybackpolyphonic-method-set-stream-volume"></a>

void **set_stream_volume**(stream: [int](class_int.md#class-int), volume_db: [float](class_float.md#class-float)) [🔗](class_audiostreamplaybackpolyphonic.md#class-audiostreamplaybackpolyphonic-method-set-stream-volume)

Change the stream volume (in db). The `stream` argument is an integer ID returned by [play_stream()](class_audiostreamplaybackpolyphonic.md#class-audiostreamplaybackpolyphonic-method-play-stream).

---


<a id="class-audiostreamplaybackpolyphonic-method-stop-stream"></a>

void **stop_stream**(stream: [int](class_int.md#class-int)) [🔗](class_audiostreamplaybackpolyphonic.md#class-audiostreamplaybackpolyphonic-method-stop-stream)

Stop a stream. The `stream` argument is an integer ID returned by [play_stream()](class_audiostreamplaybackpolyphonic.md#class-audiostreamplaybackpolyphonic-method-play-stream), which becomes invalid after calling this function.
