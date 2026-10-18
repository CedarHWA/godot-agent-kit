> Source: https://docs.godotengine.org/en/4.7/classes/class_videostreamplayback.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="videostreamplayback"></a>

<a id="class-videostreamplayback"></a>

# VideoStreamPlayback

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Internal class used by [VideoStream](class_videostream.md#class-videostream) to manage playback state when played from a [VideoStreamPlayer](class_videostreamplayer.md#class-videostreamplayer).

<a id="description"></a>

## Description

This class is intended to be overridden by video decoder extensions with custom implementations of [VideoStream](class_videostream.md#class-videostream).

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [int](class_int.md#class-int) | [_get_channels](class_videostreamplayback.md#class-videostreamplayback-private-method-get-channels)() virtual const |
| [float](class_float.md#class-float) | [_get_length](class_videostreamplayback.md#class-videostreamplayback-private-method-get-length)() virtual const |
| [int](class_int.md#class-int) | [_get_mix_rate](class_videostreamplayback.md#class-videostreamplayback-private-method-get-mix-rate)() virtual const |
| [float](class_float.md#class-float) | [_get_playback_position](class_videostreamplayback.md#class-videostreamplayback-private-method-get-playback-position)() virtual const |
| [Texture2D](class_texture2d.md#class-texture2d) | [_get_texture](class_videostreamplayback.md#class-videostreamplayback-private-method-get-texture)() virtual const |
| [bool](class_bool.md#class-bool) | [_is_paused](class_videostreamplayback.md#class-videostreamplayback-private-method-is-paused)() virtual const |
| [bool](class_bool.md#class-bool) | [_is_playing](class_videostreamplayback.md#class-videostreamplayback-private-method-is-playing)() virtual const |
| void | [_play](class_videostreamplayback.md#class-videostreamplayback-private-method-play)() virtual |
| void | [_seek](class_videostreamplayback.md#class-videostreamplayback-private-method-seek)(time: [float](class_float.md#class-float)) virtual |
| void | [_set_audio_track](class_videostreamplayback.md#class-videostreamplayback-private-method-set-audio-track)(idx: [int](class_int.md#class-int)) virtual |
| void | [_set_paused](class_videostreamplayback.md#class-videostreamplayback-private-method-set-paused)(paused: [bool](class_bool.md#class-bool)) virtual |
| void | [_stop](class_videostreamplayback.md#class-videostreamplayback-private-method-stop)() virtual |
| void | [_update](class_videostreamplayback.md#class-videostreamplayback-private-method-update)(delta: [float](class_float.md#class-float)) virtual required |
| [int](class_int.md#class-int) | [mix_audio](class_videostreamplayback.md#class-videostreamplayback-method-mix-audio)(num_frames: [int](class_int.md#class-int), buffer: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) = PackedFloat32Array(), offset: [int](class_int.md#class-int) = 0) |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-videostreamplayback-private-method-get-channels"></a>

[int](class_int.md#class-int) **_get_channels**() virtual const [🔗](class_videostreamplayback.md#class-videostreamplayback-private-method-get-channels)

Returns the number of audio channels.

---


<a id="class-videostreamplayback-private-method-get-length"></a>

[float](class_float.md#class-float) **_get_length**() virtual const [🔗](class_videostreamplayback.md#class-videostreamplayback-private-method-get-length)

Returns the video duration in seconds, if known, or 0 if unknown.

---


<a id="class-videostreamplayback-private-method-get-mix-rate"></a>

[int](class_int.md#class-int) **_get_mix_rate**() virtual const [🔗](class_videostreamplayback.md#class-videostreamplayback-private-method-get-mix-rate)

Returns the audio sample rate used for mixing.

---


<a id="class-videostreamplayback-private-method-get-playback-position"></a>

[float](class_float.md#class-float) **_get_playback_position**() virtual const [🔗](class_videostreamplayback.md#class-videostreamplayback-private-method-get-playback-position)

Return the current playback timestamp. Called in response to the [VideoStreamPlayer.stream_position](class_videostreamplayer.md#class-videostreamplayer-property-stream-position) getter.

---


<a id="class-videostreamplayback-private-method-get-texture"></a>

[Texture2D](class_texture2d.md#class-texture2d) **_get_texture**() virtual const [🔗](class_videostreamplayback.md#class-videostreamplayback-private-method-get-texture)

Allocates a [Texture2D](class_texture2d.md#class-texture2d) in which decoded video frames will be drawn.

---


<a id="class-videostreamplayback-private-method-is-paused"></a>

[bool](class_bool.md#class-bool) **_is_paused**() virtual const [🔗](class_videostreamplayback.md#class-videostreamplayback-private-method-is-paused)

Returns the paused status, as set by [_set_paused()](class_videostreamplayback.md#class-videostreamplayback-private-method-set-paused).

---


<a id="class-videostreamplayback-private-method-is-playing"></a>

[bool](class_bool.md#class-bool) **_is_playing**() virtual const [🔗](class_videostreamplayback.md#class-videostreamplayback-private-method-is-playing)

Returns the playback state, as determined by calls to [_play()](class_videostreamplayback.md#class-videostreamplayback-private-method-play) and [_stop()](class_videostreamplayback.md#class-videostreamplayback-private-method-stop).

---


<a id="class-videostreamplayback-private-method-play"></a>

void **_play**() virtual [🔗](class_videostreamplayback.md#class-videostreamplayback-private-method-play)

Called in response to [VideoStreamPlayer.autoplay](class_videostreamplayer.md#class-videostreamplayer-property-autoplay) or [VideoStreamPlayer.play()](class_videostreamplayer.md#class-videostreamplayer-method-play). Note that manual playback may also invoke [_stop()](class_videostreamplayback.md#class-videostreamplayback-private-method-stop) multiple times before this method is called. [_is_playing()](class_videostreamplayback.md#class-videostreamplayback-private-method-is-playing) should return `true` once playing.

---


<a id="class-videostreamplayback-private-method-seek"></a>

void **_seek**(time: [float](class_float.md#class-float)) virtual [🔗](class_videostreamplayback.md#class-videostreamplayback-private-method-seek)

Seeks to `time` seconds. Called in response to the [VideoStreamPlayer.stream_position](class_videostreamplayer.md#class-videostreamplayer-property-stream-position) setter.

---


<a id="class-videostreamplayback-private-method-set-audio-track"></a>

void **_set_audio_track**(idx: [int](class_int.md#class-int)) virtual [🔗](class_videostreamplayback.md#class-videostreamplayback-private-method-set-audio-track)

Select the audio track `idx`. Called when playback starts, and in response to the [VideoStreamPlayer.audio_track](class_videostreamplayer.md#class-videostreamplayer-property-audio-track) setter.

---


<a id="class-videostreamplayback-private-method-set-paused"></a>

void **_set_paused**(paused: [bool](class_bool.md#class-bool)) virtual [🔗](class_videostreamplayback.md#class-videostreamplayback-private-method-set-paused)

Set the paused status of video playback. [_is_paused()](class_videostreamplayback.md#class-videostreamplayback-private-method-is-paused) must return `paused`. Called in response to the [VideoStreamPlayer.paused](class_videostreamplayer.md#class-videostreamplayer-property-paused) setter.

---


<a id="class-videostreamplayback-private-method-stop"></a>

void **_stop**() virtual [🔗](class_videostreamplayback.md#class-videostreamplayback-private-method-stop)

Stops playback. May be called multiple times before [_play()](class_videostreamplayback.md#class-videostreamplayback-private-method-play), or in response to [VideoStreamPlayer.stop()](class_videostreamplayer.md#class-videostreamplayer-method-stop). [_is_playing()](class_videostreamplayback.md#class-videostreamplayback-private-method-is-playing) should return `false` once stopped.

---


<a id="class-videostreamplayback-private-method-update"></a>

void **_update**(delta: [float](class_float.md#class-float)) virtual required [🔗](class_videostreamplayback.md#class-videostreamplayback-private-method-update)

Ticks video playback for `delta` seconds. Called every frame as long as both [_is_paused()](class_videostreamplayback.md#class-videostreamplayback-private-method-is-paused) and [_is_playing()](class_videostreamplayback.md#class-videostreamplayback-private-method-is-playing) return `true`.

---


<a id="class-videostreamplayback-method-mix-audio"></a>

[int](class_int.md#class-int) **mix_audio**(num_frames: [int](class_int.md#class-int), buffer: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) = PackedFloat32Array(), offset: [int](class_int.md#class-int) = 0) [🔗](class_videostreamplayback.md#class-videostreamplayback-method-mix-audio)

Render `num_frames` audio frames (of [_get_channels()](class_videostreamplayback.md#class-videostreamplayback-private-method-get-channels) floats each) from `buffer`, starting from index `offset` in the array. Returns the number of audio frames rendered, or -1 on error.
