> Source: https://docs.godotengine.org/en/4.7/classes/class_audiostream.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="audiostream"></a>

<a id="class-audiostream"></a>

# AudioStream

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [AudioStreamGenerator](class_audiostreamgenerator.md#class-audiostreamgenerator), [AudioStreamInteractive](class_audiostreaminteractive.md#class-audiostreaminteractive), [AudioStreamMicrophone](class_audiostreammicrophone.md#class-audiostreammicrophone), [AudioStreamMP3](class_audiostreammp3.md#class-audiostreammp3), [AudioStreamOggVorbis](class_audiostreamoggvorbis.md#class-audiostreamoggvorbis), [AudioStreamPlaylist](class_audiostreamplaylist.md#class-audiostreamplaylist), [AudioStreamPolyphonic](class_audiostreampolyphonic.md#class-audiostreampolyphonic), [AudioStreamRandomizer](class_audiostreamrandomizer.md#class-audiostreamrandomizer), [AudioStreamSynchronized](class_audiostreamsynchronized.md#class-audiostreamsynchronized), [AudioStreamWAV](class_audiostreamwav.md#class-audiostreamwav)

Base class for audio streams.

<a id="description"></a>

## Description

Base class for audio streams. Audio streams are used for sound effects and music playback, and support WAV (via [AudioStreamWAV](class_audiostreamwav.md#class-audiostreamwav)), Ogg (via [AudioStreamOggVorbis](class_audiostreamoggvorbis.md#class-audiostreamoggvorbis)), and MP3 (via [AudioStreamMP3](class_audiostreammp3.md#class-audiostreammp3)) file formats.

<a id="tutorials"></a>

## Tutorials

- [Audio streams](../tutorials/audio/audio_streams.md)
- [Audio Generator Demo](https://godotengine.org/asset-library/asset/2759)
- [Audio Microphone Record Demo](https://godotengine.org/asset-library/asset/2760)
- [Audio Spectrum Visualizer Demo](https://godotengine.org/asset-library/asset/2762)

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [int](class_int.md#class-int) | [_get_bar_beats](class_audiostream.md#class-audiostream-private-method-get-bar-beats)() virtual const |
| [int](class_int.md#class-int) | [_get_beat_count](class_audiostream.md#class-audiostream-private-method-get-beat-count)() virtual const |
| [float](class_float.md#class-float) | [_get_bpm](class_audiostream.md#class-audiostream-private-method-get-bpm)() virtual const |
| [float](class_float.md#class-float) | [_get_length](class_audiostream.md#class-audiostream-private-method-get-length)() virtual const |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | [_get_parameter_list](class_audiostream.md#class-audiostream-private-method-get-parameter-list)() virtual const |
| [String](class_string.md#class-string) | [_get_stream_name](class_audiostream.md#class-audiostream-private-method-get-stream-name)() virtual const |
| [Dictionary](class_dictionary.md#class-dictionary) | [_get_tags](class_audiostream.md#class-audiostream-private-method-get-tags)() virtual const |
| [bool](class_bool.md#class-bool) | [_has_loop](class_audiostream.md#class-audiostream-private-method-has-loop)() virtual const |
| [AudioStreamPlayback](class_audiostreamplayback.md#class-audiostreamplayback) | [_instantiate_playback](class_audiostream.md#class-audiostream-private-method-instantiate-playback)() virtual required const |
| [bool](class_bool.md#class-bool) | [_is_monophonic](class_audiostream.md#class-audiostream-private-method-is-monophonic)() virtual const |
| [bool](class_bool.md#class-bool) | [can_be_sampled](class_audiostream.md#class-audiostream-method-can-be-sampled)() const |
| [AudioSample](class_audiosample.md#class-audiosample) | [generate_sample](class_audiostream.md#class-audiostream-method-generate-sample)() const |
| [float](class_float.md#class-float) | [get_length](class_audiostream.md#class-audiostream-method-get-length)() const |
| [AudioStreamPlayback](class_audiostreamplayback.md#class-audiostreamplayback) | [instantiate_playback](class_audiostream.md#class-audiostream-method-instantiate-playback)() |
| [bool](class_bool.md#class-bool) | [is_meta_stream](class_audiostream.md#class-audiostream-method-is-meta-stream)() const |
| [bool](class_bool.md#class-bool) | [is_monophonic](class_audiostream.md#class-audiostream-method-is-monophonic)() const |

---


<a id="signals"></a>

## Signals

<a id="class-audiostream-signal-parameter-list-changed"></a>

**parameter_list_changed**() [🔗](class_audiostream.md#class-audiostream-signal-parameter-list-changed)

Signal to be emitted to notify when the parameter list changed.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-audiostream-private-method-get-bar-beats"></a>

[int](class_int.md#class-int) **_get_bar_beats**() virtual const [🔗](class_audiostream.md#class-audiostream-private-method-get-bar-beats)

Override this method to return the bar beats of this stream.

---


<a id="class-audiostream-private-method-get-beat-count"></a>

[int](class_int.md#class-int) **_get_beat_count**() virtual const [🔗](class_audiostream.md#class-audiostream-private-method-get-beat-count)

Overridable method. Should return the total number of beats of this audio stream. Used by the engine to determine the position of every beat.

Ideally, the returned value should be based off the stream's sample rate ([AudioStreamWAV.mix_rate](class_audiostreamwav.md#class-audiostreamwav-property-mix-rate), for example).

---


<a id="class-audiostream-private-method-get-bpm"></a>

[float](class_float.md#class-float) **_get_bpm**() virtual const [🔗](class_audiostream.md#class-audiostream-private-method-get-bpm)

Overridable method. Should return the tempo of this audio stream, in beats per minute (BPM). Used by the engine to determine the position of every beat.

Ideally, the returned value should be based off the stream's sample rate ([AudioStreamWAV.mix_rate](class_audiostreamwav.md#class-audiostreamwav-property-mix-rate), for example).

---


<a id="class-audiostream-private-method-get-length"></a>

[float](class_float.md#class-float) **_get_length**() virtual const [🔗](class_audiostream.md#class-audiostream-private-method-get-length)

Override this method to customize the returned value of [get_length()](class_audiostream.md#class-audiostream-method-get-length). Should return the length of this audio stream, in seconds.

---


<a id="class-audiostream-private-method-get-parameter-list"></a>

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **_get_parameter_list**() virtual const [🔗](class_audiostream.md#class-audiostream-private-method-get-parameter-list)

Return the controllable parameters of this stream. This array contains dictionaries with a property info description format (see [Object.get_property_list()](class_object.md#class-object-method-get-property-list)). Additionally, the default value for this parameter must be added tho each dictionary in "default_value" field.

---


<a id="class-audiostream-private-method-get-stream-name"></a>

[String](class_string.md#class-string) **_get_stream_name**() virtual const [🔗](class_audiostream.md#class-audiostream-private-method-get-stream-name)

Override this method to customize the name assigned to this audio stream. Unused by the engine.

---


<a id="class-audiostream-private-method-get-tags"></a>

[Dictionary](class_dictionary.md#class-dictionary) **_get_tags**() virtual const [🔗](class_audiostream.md#class-audiostream-private-method-get-tags)

Override this method to customize the tags for this audio stream. Should return a [Dictionary](class_dictionary.md#class-dictionary) of strings with the tag as the key and its content as the value.

Commonly used tags include `title`, `artist`, `album`, `tracknumber`, and `date`.

---


<a id="class-audiostream-private-method-has-loop"></a>

[bool](class_bool.md#class-bool) **_has_loop**() virtual const [🔗](class_audiostream.md#class-audiostream-private-method-has-loop)

Override this method to return `true` if this stream has a loop.

---


<a id="class-audiostream-private-method-instantiate-playback"></a>

[AudioStreamPlayback](class_audiostreamplayback.md#class-audiostreamplayback) **_instantiate_playback**() virtual required const [🔗](class_audiostream.md#class-audiostream-private-method-instantiate-playback)

Override this method to customize the returned value of [instantiate_playback()](class_audiostream.md#class-audiostream-method-instantiate-playback). Should return a new [AudioStreamPlayback](class_audiostreamplayback.md#class-audiostreamplayback) created when the stream is played (such as by an [AudioStreamPlayer](class_audiostreamplayer.md#class-audiostreamplayer)).

---


<a id="class-audiostream-private-method-is-monophonic"></a>

[bool](class_bool.md#class-bool) **_is_monophonic**() virtual const [🔗](class_audiostream.md#class-audiostream-private-method-is-monophonic)

Override this method to customize the returned value of [is_monophonic()](class_audiostream.md#class-audiostream-method-is-monophonic). Should return `true` if this audio stream only supports one channel.

---


<a id="class-audiostream-method-can-be-sampled"></a>

[bool](class_bool.md#class-bool) **can_be_sampled**() const [🔗](class_audiostream.md#class-audiostream-method-can-be-sampled)

**Experimental:** This method may be changed or removed in future versions.

Returns if the current **AudioStream** can be used as a sample. Only static streams can be sampled.

---


<a id="class-audiostream-method-generate-sample"></a>

[AudioSample](class_audiosample.md#class-audiosample) **generate_sample**() const [🔗](class_audiostream.md#class-audiostream-method-generate-sample)

**Experimental:** This method may be changed or removed in future versions.

Generates an [AudioSample](class_audiosample.md#class-audiosample) based on the current stream.

---


<a id="class-audiostream-method-get-length"></a>

[float](class_float.md#class-float) **get_length**() const [🔗](class_audiostream.md#class-audiostream-method-get-length)

Returns the length of the audio stream in seconds. If this stream is an [AudioStreamRandomizer](class_audiostreamrandomizer.md#class-audiostreamrandomizer), returns the length of the last played stream. If this stream has an indefinite length (such as for [AudioStreamGenerator](class_audiostreamgenerator.md#class-audiostreamgenerator) and [AudioStreamMicrophone](class_audiostreammicrophone.md#class-audiostreammicrophone)), returns `0.0`.

---


<a id="class-audiostream-method-instantiate-playback"></a>

[AudioStreamPlayback](class_audiostreamplayback.md#class-audiostreamplayback) **instantiate_playback**() [🔗](class_audiostream.md#class-audiostream-method-instantiate-playback)

Returns a newly created [AudioStreamPlayback](class_audiostreamplayback.md#class-audiostreamplayback) intended to play this audio stream. Useful for when you want to extend [_instantiate_playback()](class_audiostream.md#class-audiostream-private-method-instantiate-playback) but call [instantiate_playback()](class_audiostream.md#class-audiostream-method-instantiate-playback) from an internally held AudioStream subresource. An example of this can be found in the source code for `AudioStreamRandomPitch::instantiate_playback`.

---


<a id="class-audiostream-method-is-meta-stream"></a>

[bool](class_bool.md#class-bool) **is_meta_stream**() const [🔗](class_audiostream.md#class-audiostream-method-is-meta-stream)

Returns `true` if the stream is a collection of other streams, `false` otherwise.

---


<a id="class-audiostream-method-is-monophonic"></a>

[bool](class_bool.md#class-bool) **is_monophonic**() const [🔗](class_audiostream.md#class-audiostream-method-is-monophonic)

Returns `true` if this audio stream only supports one channel (*monophony*), or `false` if the audio stream supports two or more channels (*polyphony*).
