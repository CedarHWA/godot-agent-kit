> Source: https://docs.godotengine.org/en/4.7/classes/class_audiostreamplayback.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="audiostreamplayback"></a>

<a id="class-audiostreamplayback"></a>

# AudioStreamPlayback

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [AudioStreamPlaybackInteractive](class_audiostreamplaybackinteractive.md#class-audiostreamplaybackinteractive), [AudioStreamPlaybackPlaylist](class_audiostreamplaybackplaylist.md#class-audiostreamplaybackplaylist), [AudioStreamPlaybackPolyphonic](class_audiostreamplaybackpolyphonic.md#class-audiostreamplaybackpolyphonic), [AudioStreamPlaybackResampled](class_audiostreamplaybackresampled.md#class-audiostreamplaybackresampled), [AudioStreamPlaybackSynchronized](class_audiostreamplaybacksynchronized.md#class-audiostreamplaybacksynchronized)

Meta class for playing back audio.

<a id="description"></a>

## Description

Can play, loop, pause a scroll through audio. See [AudioStream](class_audiostream.md#class-audiostream) and [AudioStreamOggVorbis](class_audiostreamoggvorbis.md#class-audiostreamoggvorbis) for usage.

<a id="tutorials"></a>

## Tutorials

- [Audio Generator Demo](https://godotengine.org/asset-library/asset/2759)

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [int](class_int.md#class-int) | [_get_loop_count](class_audiostreamplayback.md#class-audiostreamplayback-private-method-get-loop-count)() virtual const |
| [Variant](class_variant.md#class-variant) | [_get_parameter](class_audiostreamplayback.md#class-audiostreamplayback-private-method-get-parameter)(name: [StringName](class_stringname.md#class-stringname)) virtual const |
| [float](class_float.md#class-float) | [_get_playback_position](class_audiostreamplayback.md#class-audiostreamplayback-private-method-get-playback-position)() virtual required const |
| [bool](class_bool.md#class-bool) | [_is_playing](class_audiostreamplayback.md#class-audiostreamplayback-private-method-is-playing)() virtual required const |
| [int](class_int.md#class-int) | [_mix](class_audiostreamplayback.md#class-audiostreamplayback-private-method-mix)(buffer: `AudioFrame*`, rate_scale: [float](class_float.md#class-float), frames: [int](class_int.md#class-int)) virtual required |
| void | [_seek](class_audiostreamplayback.md#class-audiostreamplayback-private-method-seek)(position: [float](class_float.md#class-float)) virtual |
| void | [_set_parameter](class_audiostreamplayback.md#class-audiostreamplayback-private-method-set-parameter)(name: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant)) virtual |
| void | [_start](class_audiostreamplayback.md#class-audiostreamplayback-private-method-start)(from_pos: [float](class_float.md#class-float)) virtual required |
| void | [_stop](class_audiostreamplayback.md#class-audiostreamplayback-private-method-stop)() virtual required |
| void | [_tag_used_streams](class_audiostreamplayback.md#class-audiostreamplayback-private-method-tag-used-streams)() virtual |
| [int](class_int.md#class-int) | [get_loop_count](class_audiostreamplayback.md#class-audiostreamplayback-method-get-loop-count)() const |
| [float](class_float.md#class-float) | [get_playback_position](class_audiostreamplayback.md#class-audiostreamplayback-method-get-playback-position)() const |
| [AudioSamplePlayback](class_audiosampleplayback.md#class-audiosampleplayback) | [get_sample_playback](class_audiostreamplayback.md#class-audiostreamplayback-method-get-sample-playback)() const |
| [bool](class_bool.md#class-bool) | [is_playing](class_audiostreamplayback.md#class-audiostreamplayback-method-is-playing)() const |
| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) | [mix_audio](class_audiostreamplayback.md#class-audiostreamplayback-method-mix-audio)(rate_scale: [float](class_float.md#class-float), frames: [int](class_int.md#class-int)) |
| void | [seek](class_audiostreamplayback.md#class-audiostreamplayback-method-seek)(time: [float](class_float.md#class-float) = 0.0) |
| void | [set_sample_playback](class_audiostreamplayback.md#class-audiostreamplayback-method-set-sample-playback)(playback_sample: [AudioSamplePlayback](class_audiosampleplayback.md#class-audiosampleplayback)) |
| void | [start](class_audiostreamplayback.md#class-audiostreamplayback-method-start)(from_pos: [float](class_float.md#class-float) = 0.0) |
| void | [stop](class_audiostreamplayback.md#class-audiostreamplayback-method-stop)() |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-audiostreamplayback-private-method-get-loop-count"></a>

[int](class_int.md#class-int) **_get_loop_count**() virtual const [🔗](class_audiostreamplayback.md#class-audiostreamplayback-private-method-get-loop-count)

Overridable method. Should return how many times this audio stream has looped. Most built-in playbacks always return `0`.

---


<a id="class-audiostreamplayback-private-method-get-parameter"></a>

[Variant](class_variant.md#class-variant) **_get_parameter**(name: [StringName](class_stringname.md#class-stringname)) virtual const [🔗](class_audiostreamplayback.md#class-audiostreamplayback-private-method-get-parameter)

Return the current value of a playback parameter by name (see [AudioStream._get_parameter_list()](class_audiostream.md#class-audiostream-private-method-get-parameter-list)).

---


<a id="class-audiostreamplayback-private-method-get-playback-position"></a>

[float](class_float.md#class-float) **_get_playback_position**() virtual required const [🔗](class_audiostreamplayback.md#class-audiostreamplayback-private-method-get-playback-position)

Overridable method. Should return the current progress along the audio stream, in seconds.

---


<a id="class-audiostreamplayback-private-method-is-playing"></a>

[bool](class_bool.md#class-bool) **_is_playing**() virtual required const [🔗](class_audiostreamplayback.md#class-audiostreamplayback-private-method-is-playing)

Overridable method. Should return `true` if this playback is active and playing its audio stream.

---


<a id="class-audiostreamplayback-private-method-mix"></a>

[int](class_int.md#class-int) **_mix**(buffer: `AudioFrame*`, rate_scale: [float](class_float.md#class-float), frames: [int](class_int.md#class-int)) virtual required [🔗](class_audiostreamplayback.md#class-audiostreamplayback-private-method-mix)

Override this method to customize how the audio stream is mixed. This method is called even if the playback is not active.

**Note:** It is not useful to override this method in GDScript or C#. Only GDExtension can take advantage of it.

---


<a id="class-audiostreamplayback-private-method-seek"></a>

void **_seek**(position: [float](class_float.md#class-float)) virtual [🔗](class_audiostreamplayback.md#class-audiostreamplayback-private-method-seek)

Override this method to customize what happens when seeking this audio stream at the given `position`, such as by calling [AudioStreamPlayer.seek()](class_audiostreamplayer.md#class-audiostreamplayer-method-seek).

---


<a id="class-audiostreamplayback-private-method-set-parameter"></a>

void **_set_parameter**(name: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant)) virtual [🔗](class_audiostreamplayback.md#class-audiostreamplayback-private-method-set-parameter)

Set the current value of a playback parameter by name (see [AudioStream._get_parameter_list()](class_audiostream.md#class-audiostream-private-method-get-parameter-list)).

---


<a id="class-audiostreamplayback-private-method-start"></a>

void **_start**(from_pos: [float](class_float.md#class-float)) virtual required [🔗](class_audiostreamplayback.md#class-audiostreamplayback-private-method-start)

Override this method to customize what happens when the playback starts at the given position, such as by calling [AudioStreamPlayer.play()](class_audiostreamplayer.md#class-audiostreamplayer-method-play).

---


<a id="class-audiostreamplayback-private-method-stop"></a>

void **_stop**() virtual required [🔗](class_audiostreamplayback.md#class-audiostreamplayback-private-method-stop)

Override this method to customize what happens when the playback is stopped, such as by calling [AudioStreamPlayer.stop()](class_audiostreamplayer.md#class-audiostreamplayer-method-stop).

---


<a id="class-audiostreamplayback-private-method-tag-used-streams"></a>

void **_tag_used_streams**() virtual [🔗](class_audiostreamplayback.md#class-audiostreamplayback-private-method-tag-used-streams)

Overridable method. Called whenever the audio stream is mixed if the playback is active and [AudioServer.set_enable_tagging_used_audio_streams()](class_audioserver.md#class-audioserver-method-set-enable-tagging-used-audio-streams) has been set to `true`. Editor plugins may use this method to "tag" the current position along the audio stream and display it in a preview.

---


<a id="class-audiostreamplayback-method-get-loop-count"></a>

[int](class_int.md#class-int) **get_loop_count**() const [🔗](class_audiostreamplayback.md#class-audiostreamplayback-method-get-loop-count)

Returns the number of times the stream has looped.

---


<a id="class-audiostreamplayback-method-get-playback-position"></a>

[float](class_float.md#class-float) **get_playback_position**() const [🔗](class_audiostreamplayback.md#class-audiostreamplayback-method-get-playback-position)

Returns the current position in the stream, in seconds.

---


<a id="class-audiostreamplayback-method-get-sample-playback"></a>

[AudioSamplePlayback](class_audiosampleplayback.md#class-audiosampleplayback) **get_sample_playback**() const [🔗](class_audiostreamplayback.md#class-audiostreamplayback-method-get-sample-playback)

**Experimental:** This method may be changed or removed in future versions.

Returns the [AudioSamplePlayback](class_audiosampleplayback.md#class-audiosampleplayback) associated with this **AudioStreamPlayback** for playing back the audio sample of this stream.

---


<a id="class-audiostreamplayback-method-is-playing"></a>

[bool](class_bool.md#class-bool) **is_playing**() const [🔗](class_audiostreamplayback.md#class-audiostreamplayback-method-is-playing)

Returns `true` if the stream is playing.

---


<a id="class-audiostreamplayback-method-mix-audio"></a>

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **mix_audio**(rate_scale: [float](class_float.md#class-float), frames: [int](class_int.md#class-int)) [🔗](class_audiostreamplayback.md#class-audiostreamplayback-method-mix-audio)

Mixes up to `frames` of audio from the stream from the current position, at a rate of `rate_scale`, advancing the stream.

Returns a [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) where each element holds the left and right channel volume levels of each frame.

**Note:** Can return fewer frames than requested, make sure to use the size of the return value.

---


<a id="class-audiostreamplayback-method-seek"></a>

void **seek**(time: [float](class_float.md#class-float) = 0.0) [🔗](class_audiostreamplayback.md#class-audiostreamplayback-method-seek)

Seeks the stream at the given `time`, in seconds.

---


<a id="class-audiostreamplayback-method-set-sample-playback"></a>

void **set_sample_playback**(playback_sample: [AudioSamplePlayback](class_audiosampleplayback.md#class-audiosampleplayback)) [🔗](class_audiostreamplayback.md#class-audiostreamplayback-method-set-sample-playback)

**Experimental:** This method may be changed or removed in future versions.

Associates [AudioSamplePlayback](class_audiosampleplayback.md#class-audiosampleplayback) to this **AudioStreamPlayback** for playing back the audio sample of this stream.

---


<a id="class-audiostreamplayback-method-start"></a>

void **start**(from_pos: [float](class_float.md#class-float) = 0.0) [🔗](class_audiostreamplayback.md#class-audiostreamplayback-method-start)

Starts the stream from the given `from_pos`, in seconds.

---


<a id="class-audiostreamplayback-method-stop"></a>

void **stop**() [🔗](class_audiostreamplayback.md#class-audiostreamplayback-method-stop)

Stops the stream.
