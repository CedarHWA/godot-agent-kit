> Source: https://docs.godotengine.org/en/4.7/classes/class_resourceimporteroggvorbis.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="resourceimporteroggvorbis"></a>

<a id="class-resourceimporteroggvorbis"></a>

# ResourceImporterOggVorbis

**Inherits:** [ResourceImporter](class_resourceimporter.md#class-resourceimporter) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Imports an Ogg Vorbis audio file for playback.

<a id="description"></a>

## Description

Ogg Vorbis is a lossy audio format, with better audio quality compared to [ResourceImporterMP3](class_resourceimportermp3.md#class-resourceimportermp3) at a given bitrate.

In most cases, it's recommended to use Ogg Vorbis over MP3. However, if you're using an MP3 sound source with no higher quality source available, then it's recommended to use the MP3 file directly to avoid double lossy compression.

Ogg Vorbis requires more CPU to decode than [ResourceImporterWAV](class_resourceimporterwav.md#class-resourceimporterwav). If you need to play a lot of simultaneous sounds, it's recommended to use WAV for those sounds instead, especially if targeting low-end devices.

<a id="tutorials"></a>

## Tutorials

- [Importing audio samples](../tutorials/assets_pipeline/importing_audio_samples.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [bar_beats](class_resourceimporteroggvorbis.md#class-resourceimporteroggvorbis-property-bar-beats) | `4` |
| [int](class_int.md#class-int) | [beat_count](class_resourceimporteroggvorbis.md#class-resourceimporteroggvorbis-property-beat-count) | `0` |
| [float](class_float.md#class-float) | [bpm](class_resourceimporteroggvorbis.md#class-resourceimporteroggvorbis-property-bpm) | `0` |
| [bool](class_bool.md#class-bool) | [loop](class_resourceimporteroggvorbis.md#class-resourceimporteroggvorbis-property-loop) | `false` |
| [float](class_float.md#class-float) | [loop_offset](class_resourceimporteroggvorbis.md#class-resourceimporteroggvorbis-property-loop-offset) | `0` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [AudioStreamOggVorbis](class_audiostreamoggvorbis.md#class-audiostreamoggvorbis) | [load_from_buffer](class_resourceimporteroggvorbis.md#class-resourceimporteroggvorbis-method-load-from-buffer)(stream_data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray)) static |
| [AudioStreamOggVorbis](class_audiostreamoggvorbis.md#class-audiostreamoggvorbis) | [load_from_file](class_resourceimporteroggvorbis.md#class-resourceimporteroggvorbis-method-load-from-file)(path: [String](class_string.md#class-string)) static |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-resourceimporteroggvorbis-property-bar-beats"></a>

[int](class_int.md#class-int) **bar_beats** = `4` [🔗](class_resourceimporteroggvorbis.md#class-resourceimporteroggvorbis-property-bar-beats)

The number of beats within a single bar in the audio track. This is only relevant for music that wishes to make use of interactive music functionality, not sound effects.

A more convenient editor for [bar_beats](class_resourceimporteroggvorbis.md#class-resourceimporteroggvorbis-property-bar-beats) is provided in the **Advanced Import Settings** dialog, as it lets you preview your changes without having to reimport the audio.

---


<a id="class-resourceimporteroggvorbis-property-beat-count"></a>

[int](class_int.md#class-int) **beat_count** = `0` [🔗](class_resourceimporteroggvorbis.md#class-resourceimporteroggvorbis-property-beat-count)

The length of the audio track, in beats. The actual duration of the audio file might be longer than what is indicated by this property. This is only relevant for music that wishes to make use of interactive music functionality, not sound effects.

A more convenient editor for [beat_count](class_resourceimporteroggvorbis.md#class-resourceimporteroggvorbis-property-beat-count) is provided in the **Advanced Import Settings** dialog, as it lets you preview your changes without having to reimport the audio.

---


<a id="class-resourceimporteroggvorbis-property-bpm"></a>

[float](class_float.md#class-float) **bpm** = `0` [🔗](class_resourceimporteroggvorbis.md#class-resourceimporteroggvorbis-property-bpm)

The tempo of the audio track, measured in beats per minute. This should match the BPM measure that was used to compose the track. This is only relevant for music that wishes to make use of interactive music functionality, not sound effects.

A more convenient editor for [bpm](class_resourceimporteroggvorbis.md#class-resourceimporteroggvorbis-property-bpm) is provided in the **Advanced Import Settings** dialog, as it lets you preview your changes without having to reimport the audio.

---


<a id="class-resourceimporteroggvorbis-property-loop"></a>

[bool](class_bool.md#class-bool) **loop** = `false` [🔗](class_resourceimporteroggvorbis.md#class-resourceimporteroggvorbis-property-loop)

If enabled, the audio will begin playing either from the beginning or from [loop_offset](class_resourceimporteroggvorbis.md#class-resourceimporteroggvorbis-property-loop-offset), after playback ends by either reaching the end of the audio or reaching the end of the last beat according to the amount specified in [beat_count](class_resourceimporteroggvorbis.md#class-resourceimporteroggvorbis-property-beat-count).

**Note:** In [AudioStreamPlayer](class_audiostreamplayer.md#class-audiostreamplayer), the [AudioStreamPlayer.finished](class_audiostreamplayer.md#class-audiostreamplayer-signal-finished) signal won't be emitted for looping audio when it reaches the end of the audio file, as the audio will keep playing indefinitely.

---


<a id="class-resourceimporteroggvorbis-property-loop-offset"></a>

[float](class_float.md#class-float) **loop_offset** = `0` [🔗](class_resourceimporteroggvorbis.md#class-resourceimporteroggvorbis-property-loop-offset)

Determines where audio will start to loop after playback reaches the end of the audio. This can be used to only loop a part of the audio file, which is useful for some ambient sounds or music. The value is determined in seconds relative to the beginning of the audio. A value of `0.0` will loop the entire audio file.

Only has an effect if [loop](class_resourceimporteroggvorbis.md#class-resourceimporteroggvorbis-property-loop) is `true`.

A more convenient editor for [loop_offset](class_resourceimporteroggvorbis.md#class-resourceimporteroggvorbis-property-loop-offset) is provided in the **Advanced Import Settings** dialog, as it lets you preview your changes without having to reimport the audio.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-resourceimporteroggvorbis-method-load-from-buffer"></a>

[AudioStreamOggVorbis](class_audiostreamoggvorbis.md#class-audiostreamoggvorbis) **load_from_buffer**(stream_data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray)) static [🔗](class_resourceimporteroggvorbis.md#class-resourceimporteroggvorbis-method-load-from-buffer)

**Deprecated:** Use [AudioStreamOggVorbis.load_from_buffer()](class_audiostreamoggvorbis.md#class-audiostreamoggvorbis-method-load-from-buffer) instead.

Creates a new [AudioStreamOggVorbis](class_audiostreamoggvorbis.md#class-audiostreamoggvorbis) instance from the given buffer. The buffer must contain Ogg Vorbis data.

---


<a id="class-resourceimporteroggvorbis-method-load-from-file"></a>

[AudioStreamOggVorbis](class_audiostreamoggvorbis.md#class-audiostreamoggvorbis) **load_from_file**(path: [String](class_string.md#class-string)) static [🔗](class_resourceimporteroggvorbis.md#class-resourceimporteroggvorbis-method-load-from-file)

**Deprecated:** Use [AudioStreamOggVorbis.load_from_file()](class_audiostreamoggvorbis.md#class-audiostreamoggvorbis-method-load-from-file) instead.

Creates a new [AudioStreamOggVorbis](class_audiostreamoggvorbis.md#class-audiostreamoggvorbis) instance from the given file path. The file must be in Ogg Vorbis format.
