> Source: https://docs.godotengine.org/en/4.7/classes/class_audiostreammp3.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="audiostreammp3"></a>

<a id="class-audiostreammp3"></a>

# AudioStreamMP3

**Inherits:** [AudioStream](class_audiostream.md#class-audiostream) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

MP3 audio stream driver.

<a id="description"></a>

## Description

MP3 audio stream driver. See [data](class_audiostreammp3.md#class-audiostreammp3-property-data) if you want to load an MP3 file at run-time. More info can be found in [ResourceImporterMP3](class_resourceimportermp3.md#class-resourceimportermp3).

**Note:** This class can optionally support legacy MP1 and MP2 formats, provided that the engine is compiled with the `minimp3_extra_formats=yes` SCons option. These extra formats are not enabled by default.

<a id="tutorials"></a>

## Tutorials

- [Audio streams](../tutorials/audio/audio_streams.md)
- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [bar_beats](class_audiostreammp3.md#class-audiostreammp3-property-bar-beats) | `4` |
| [int](class_int.md#class-int) | [beat_count](class_audiostreammp3.md#class-audiostreammp3-property-beat-count) | `0` |
| [float](class_float.md#class-float) | [bpm](class_audiostreammp3.md#class-audiostreammp3-property-bpm) | `0.0` |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray) | [data](class_audiostreammp3.md#class-audiostreammp3-property-data) | `PackedByteArray()` |
| [bool](class_bool.md#class-bool) | [loop](class_audiostreammp3.md#class-audiostreammp3-property-loop) | `false` |
| [float](class_float.md#class-float) | [loop_offset](class_audiostreammp3.md#class-audiostreammp3-property-loop-offset) | `0.0` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [AudioStreamMP3](class_audiostreammp3.md#class-audiostreammp3) | [load_from_buffer](class_audiostreammp3.md#class-audiostreammp3-method-load-from-buffer)(stream_data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray)) static |
| [AudioStreamMP3](class_audiostreammp3.md#class-audiostreammp3) | [load_from_file](class_audiostreammp3.md#class-audiostreammp3-method-load-from-file)(path: [String](class_string.md#class-string)) static |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-audiostreammp3-property-bar-beats"></a>

[int](class_int.md#class-int) **bar_beats** = `4` [🔗](class_audiostreammp3.md#class-audiostreammp3-property-bar-beats)

- void **set_bar_beats**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_bar_beats**()

The number of beats within a single bar in the audio track.

---


<a id="class-audiostreammp3-property-beat-count"></a>

[int](class_int.md#class-int) **beat_count** = `0` [🔗](class_audiostreammp3.md#class-audiostreammp3-property-beat-count)

- void **set_beat_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_beat_count**()

The length of the audio track, in beats. The actual duration of the audio file might be longer than what is indicated by this property. It defines the end of the audio for looping, [AudioStreamPlaylist](class_audiostreamplaylist.md#class-audiostreamplaylist), and [AudioStreamInteractive](class_audiostreaminteractive.md#class-audiostreaminteractive).

---


<a id="class-audiostreammp3-property-bpm"></a>

[float](class_float.md#class-float) **bpm** = `0.0` [🔗](class_audiostreammp3.md#class-audiostreammp3-property-bpm)

- void **set_bpm**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_bpm**()

The tempo of the audio track, measured in beats per minute.

---


<a id="class-audiostreammp3-property-data"></a>

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **data** = `PackedByteArray()` [🔗](class_audiostreammp3.md#class-audiostreammp3-property-data)

- void **set_data**(value: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))
- [PackedByteArray](class_packedbytearray.md#class-packedbytearray) **get_data**()

Contains the audio data in bytes.

You can load a file without having to import it beforehand using the code snippet below. Keep in mind that this snippet loads the whole file into memory and may not be ideal for huge files (hundreds of megabytes or more).

```gdscript
func load_mp3(path):
    var file = FileAccess.open(path, FileAccess.READ)
    var sound = AudioStreamMP3.new()
    sound.data = file.get_buffer(file.get_length())
    return sound
```

```csharp
public AudioStreamMP3 LoadMP3(string path)
{
    using var file = FileAccess.Open(path, FileAccess.ModeFlags.Read);
    var sound = new AudioStreamMP3();
    sound.Data = file.GetBuffer(file.GetLength());
    return sound;
}
```

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray](class_packedbytearray.md#class-packedbytearray) for more details.

---


<a id="class-audiostreammp3-property-loop"></a>

[bool](class_bool.md#class-bool) **loop** = `false` [🔗](class_audiostreammp3.md#class-audiostreammp3-property-loop)

- void **set_loop**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **has_loop**()

If `true`, the stream will play again from the specified [loop_offset](class_audiostreammp3.md#class-audiostreammp3-property-loop-offset) once it reaches the end of the audio track, or once it reaches the end of the last beat according to the amount specified in [beat_count](class_audiostreammp3.md#class-audiostreammp3-property-beat-count). Useful for ambient sounds and background music.

---


<a id="class-audiostreammp3-property-loop-offset"></a>

[float](class_float.md#class-float) **loop_offset** = `0.0` [🔗](class_audiostreammp3.md#class-audiostreammp3-property-loop-offset)

- void **set_loop_offset**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_loop_offset**()

Time in seconds at which the stream starts after being looped.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-audiostreammp3-method-load-from-buffer"></a>

[AudioStreamMP3](class_audiostreammp3.md#class-audiostreammp3) **load_from_buffer**(stream_data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray)) static [🔗](class_audiostreammp3.md#class-audiostreammp3-method-load-from-buffer)

Creates a new **AudioStreamMP3** instance from the given buffer. The buffer must contain MP3 data.

---


<a id="class-audiostreammp3-method-load-from-file"></a>

[AudioStreamMP3](class_audiostreammp3.md#class-audiostreammp3) **load_from_file**(path: [String](class_string.md#class-string)) static [🔗](class_audiostreammp3.md#class-audiostreammp3-method-load-from-file)

Creates a new **AudioStreamMP3** instance from the given file path. The file must be in MP3 format.
