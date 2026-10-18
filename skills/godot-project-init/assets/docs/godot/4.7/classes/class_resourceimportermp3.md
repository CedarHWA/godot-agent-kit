> Source: https://docs.godotengine.org/en/4.7/classes/class_resourceimportermp3.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="resourceimportermp3"></a>

<a id="class-resourceimportermp3"></a>

# ResourceImporterMP3

**Inherits:** [ResourceImporter](class_resourceimporter.md#class-resourceimporter) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Imports an MP3 audio file for playback.

<a id="description"></a>

## Description

MP3 is a lossy audio format, with worse audio quality compared to [ResourceImporterOggVorbis](class_resourceimporteroggvorbis.md#class-resourceimporteroggvorbis) at a given bitrate.

In most cases, it's recommended to use Ogg Vorbis over MP3. However, if you're using an MP3 sound source with no higher quality source available, then it's recommended to use the MP3 file directly to avoid double lossy compression.

MP3 requires more CPU to decode than [ResourceImporterWAV](class_resourceimporterwav.md#class-resourceimporterwav). If you need to play a lot of simultaneous sounds, it's recommended to use WAV for those sounds instead, especially if targeting low-end devices.

<a id="tutorials"></a>

## Tutorials

- [Importing audio samples](../tutorials/assets_pipeline/importing_audio_samples.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [bar_beats](class_resourceimportermp3.md#class-resourceimportermp3-property-bar-beats) | `4` |
| [int](class_int.md#class-int) | [beat_count](class_resourceimportermp3.md#class-resourceimportermp3-property-beat-count) | `0` |
| [float](class_float.md#class-float) | [bpm](class_resourceimportermp3.md#class-resourceimportermp3-property-bpm) | `0` |
| [bool](class_bool.md#class-bool) | [loop](class_resourceimportermp3.md#class-resourceimportermp3-property-loop) | `false` |
| [float](class_float.md#class-float) | [loop_offset](class_resourceimportermp3.md#class-resourceimportermp3-property-loop-offset) | `0` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-resourceimportermp3-property-bar-beats"></a>

[int](class_int.md#class-int) **bar_beats** = `4` [🔗](class_resourceimportermp3.md#class-resourceimportermp3-property-bar-beats)

The number of beats within a single bar in the audio track. This is only relevant for music that wishes to make use of interactive music functionality, not sound effects.

A more convenient editor for [bar_beats](class_resourceimportermp3.md#class-resourceimportermp3-property-bar-beats) is provided in the **Advanced Import Settings** dialog, as it lets you preview your changes without having to reimport the audio.

---


<a id="class-resourceimportermp3-property-beat-count"></a>

[int](class_int.md#class-int) **beat_count** = `0` [🔗](class_resourceimportermp3.md#class-resourceimportermp3-property-beat-count)

The length of the audio track, in beats. The actual duration of the audio file might be longer than what is indicated by this property. This is only relevant for music that wishes to make use of interactive music functionality, not sound effects.

A more convenient editor for [beat_count](class_resourceimportermp3.md#class-resourceimportermp3-property-beat-count) is provided in the **Advanced Import Settings** dialog, as it lets you preview your changes without having to reimport the audio.

---


<a id="class-resourceimportermp3-property-bpm"></a>

[float](class_float.md#class-float) **bpm** = `0` [🔗](class_resourceimportermp3.md#class-resourceimportermp3-property-bpm)

The tempo of the audio track, measured in beats per minute. This should match the BPM measure that was used to compose the track. This is only relevant for music that wishes to make use of interactive music functionality, not sound effects.

A more convenient editor for [bpm](class_resourceimportermp3.md#class-resourceimportermp3-property-bpm) is provided in the **Advanced Import Settings** dialog, as it lets you preview your changes without having to reimport the audio.

---


<a id="class-resourceimportermp3-property-loop"></a>

[bool](class_bool.md#class-bool) **loop** = `false` [🔗](class_resourceimportermp3.md#class-resourceimportermp3-property-loop)

If enabled, the audio will begin playing either from the beginning or from [loop_offset](class_resourceimportermp3.md#class-resourceimportermp3-property-loop-offset), after playback ends by either reaching the end of the audio or reaching the end of the last beat according to the amount specified in [beat_count](class_resourceimportermp3.md#class-resourceimportermp3-property-beat-count).

**Note:** In [AudioStreamPlayer](class_audiostreamplayer.md#class-audiostreamplayer), the [AudioStreamPlayer.finished](class_audiostreamplayer.md#class-audiostreamplayer-signal-finished) signal won't be emitted for looping audio when it reaches the end of the audio file, as the audio will keep playing indefinitely.

---


<a id="class-resourceimportermp3-property-loop-offset"></a>

[float](class_float.md#class-float) **loop_offset** = `0` [🔗](class_resourceimportermp3.md#class-resourceimportermp3-property-loop-offset)

Determines where audio will start to loop after playback reaches the end of the audio. This can be used to only loop a part of the audio file, which is useful for some ambient sounds or music. The value is determined in seconds relative to the beginning of the audio. A value of `0.0` will loop the entire audio file.

Only has an effect if [loop](class_resourceimportermp3.md#class-resourceimportermp3-property-loop) is `true`.

A more convenient editor for [loop_offset](class_resourceimportermp3.md#class-resourceimportermp3-property-loop-offset) is provided in the **Advanced Import Settings** dialog, as it lets you preview your changes without having to reimport the audio.
