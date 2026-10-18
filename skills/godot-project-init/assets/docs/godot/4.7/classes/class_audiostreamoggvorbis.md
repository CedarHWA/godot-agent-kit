> Source: https://docs.godotengine.org/en/4.7/classes/class_audiostreamoggvorbis.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="audiostreamoggvorbis"></a>

<a id="class-audiostreamoggvorbis"></a>

# AudioStreamOggVorbis

**Inherits:** [AudioStream](class_audiostream.md#class-audiostream) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A class representing an Ogg Vorbis audio stream.

<a id="description"></a>

## Description

The AudioStreamOggVorbis class is a specialized [AudioStream](class_audiostream.md#class-audiostream) for handling Ogg Vorbis file formats. It offers functionality for loading and playing back Ogg Vorbis files, as well as managing looping and other playback properties. More info can be found in [ResourceImporterOggVorbis](class_resourceimporteroggvorbis.md#class-resourceimporteroggvorbis).

This class is part of the audio stream system, which also supports WAV files through the [AudioStreamWAV](class_audiostreamwav.md#class-audiostreamwav) class, and MP3 files through the [AudioStreamMP3](class_audiostreammp3.md#class-audiostreammp3) class.

<a id="tutorials"></a>

## Tutorials

- [Audio streams](../tutorials/audio/audio_streams.md)
- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [bar_beats](class_audiostreamoggvorbis.md#class-audiostreamoggvorbis-property-bar-beats) | `4` |
| [int](class_int.md#class-int) | [beat_count](class_audiostreamoggvorbis.md#class-audiostreamoggvorbis-property-beat-count) | `0` |
| [float](class_float.md#class-float) | [bpm](class_audiostreamoggvorbis.md#class-audiostreamoggvorbis-property-bpm) | `0.0` |
| [bool](class_bool.md#class-bool) | [loop](class_audiostreamoggvorbis.md#class-audiostreamoggvorbis-property-loop) | `false` |
| [float](class_float.md#class-float) | [loop_offset](class_audiostreamoggvorbis.md#class-audiostreamoggvorbis-property-loop-offset) | `0.0` |
| [OggPacketSequence](class_oggpacketsequence.md#class-oggpacketsequence) | [packet_sequence](class_audiostreamoggvorbis.md#class-audiostreamoggvorbis-property-packet-sequence) |  |
| [Dictionary](class_dictionary.md#class-dictionary) | [tags](class_audiostreamoggvorbis.md#class-audiostreamoggvorbis-property-tags) | `{}` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [AudioStreamOggVorbis](class_audiostreamoggvorbis.md#class-audiostreamoggvorbis) | [load_from_buffer](class_audiostreamoggvorbis.md#class-audiostreamoggvorbis-method-load-from-buffer)(stream_data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray)) static |
| [AudioStreamOggVorbis](class_audiostreamoggvorbis.md#class-audiostreamoggvorbis) | [load_from_file](class_audiostreamoggvorbis.md#class-audiostreamoggvorbis-method-load-from-file)(path: [String](class_string.md#class-string)) static |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-audiostreamoggvorbis-property-bar-beats"></a>

[int](class_int.md#class-int) **bar_beats** = `4` [🔗](class_audiostreamoggvorbis.md#class-audiostreamoggvorbis-property-bar-beats)

- void **set_bar_beats**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_bar_beats**()

The number of beats within a single bar in the audio track.

---


<a id="class-audiostreamoggvorbis-property-beat-count"></a>

[int](class_int.md#class-int) **beat_count** = `0` [🔗](class_audiostreamoggvorbis.md#class-audiostreamoggvorbis-property-beat-count)

- void **set_beat_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_beat_count**()

The length of the audio track, in beats. The actual duration of the audio file might be longer than what is indicated by this property. It defines the end of the audio for looping, [AudioStreamPlaylist](class_audiostreamplaylist.md#class-audiostreamplaylist), and [AudioStreamInteractive](class_audiostreaminteractive.md#class-audiostreaminteractive).

---


<a id="class-audiostreamoggvorbis-property-bpm"></a>

[float](class_float.md#class-float) **bpm** = `0.0` [🔗](class_audiostreamoggvorbis.md#class-audiostreamoggvorbis-property-bpm)

- void **set_bpm**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_bpm**()

The tempo of the audio track, measured in beats per minute.

---


<a id="class-audiostreamoggvorbis-property-loop"></a>

[bool](class_bool.md#class-bool) **loop** = `false` [🔗](class_audiostreamoggvorbis.md#class-audiostreamoggvorbis-property-loop)

- void **set_loop**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **has_loop**()

If `true`, the stream will play again from the specified [loop_offset](class_audiostreamoggvorbis.md#class-audiostreamoggvorbis-property-loop-offset) once it reaches the end of the audio track, or once it reaches the end of the last beat according to the amount specified in [beat_count](class_audiostreamoggvorbis.md#class-audiostreamoggvorbis-property-beat-count). Useful for ambient sounds and background music.

---


<a id="class-audiostreamoggvorbis-property-loop-offset"></a>

[float](class_float.md#class-float) **loop_offset** = `0.0` [🔗](class_audiostreamoggvorbis.md#class-audiostreamoggvorbis-property-loop-offset)

- void **set_loop_offset**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_loop_offset**()

Time in seconds at which the stream starts after being looped.

---


<a id="class-audiostreamoggvorbis-property-packet-sequence"></a>

[OggPacketSequence](class_oggpacketsequence.md#class-oggpacketsequence) **packet_sequence** [🔗](class_audiostreamoggvorbis.md#class-audiostreamoggvorbis-property-packet-sequence)

- void **set_packet_sequence**(value: [OggPacketSequence](class_oggpacketsequence.md#class-oggpacketsequence))
- [OggPacketSequence](class_oggpacketsequence.md#class-oggpacketsequence) **get_packet_sequence**()

Contains the raw Ogg data for this stream.

---


<a id="class-audiostreamoggvorbis-property-tags"></a>

[Dictionary](class_dictionary.md#class-dictionary) **tags** = `{}` [🔗](class_audiostreamoggvorbis.md#class-audiostreamoggvorbis-property-tags)

- void **set_tags**(value: [Dictionary](class_dictionary.md#class-dictionary))
- [Dictionary](class_dictionary.md#class-dictionary) **get_tags**()

Contains user-defined tags if found in the Ogg Vorbis data.

Commonly used tags include `title`, `artist`, `album`, `tracknumber`, and `date` (`date` does not have a standard date format).

**Note:** No tag is *guaranteed* to be present in every file, so make sure to account for the keys not always existing.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-audiostreamoggvorbis-method-load-from-buffer"></a>

[AudioStreamOggVorbis](class_audiostreamoggvorbis.md#class-audiostreamoggvorbis) **load_from_buffer**(stream_data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray)) static [🔗](class_audiostreamoggvorbis.md#class-audiostreamoggvorbis-method-load-from-buffer)

Creates a new **AudioStreamOggVorbis** instance from the given buffer. The buffer must contain Ogg Vorbis data.

---


<a id="class-audiostreamoggvorbis-method-load-from-file"></a>

[AudioStreamOggVorbis](class_audiostreamoggvorbis.md#class-audiostreamoggvorbis) **load_from_file**(path: [String](class_string.md#class-string)) static [🔗](class_audiostreamoggvorbis.md#class-audiostreamoggvorbis-method-load-from-file)

Creates a new **AudioStreamOggVorbis** instance from the given file path. The file must be in Ogg Vorbis format.
