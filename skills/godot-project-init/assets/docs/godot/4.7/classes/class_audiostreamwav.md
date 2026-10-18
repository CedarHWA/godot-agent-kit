> Source: https://docs.godotengine.org/en/4.7/classes/class_audiostreamwav.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="audiostreamwav"></a>

<a id="class-audiostreamwav"></a>

# AudioStreamWAV

**Inherits:** [AudioStream](class_audiostream.md#class-audiostream) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Stores audio data loaded from WAV files.

<a id="description"></a>

## Description

AudioStreamWAV stores sound samples loaded from WAV files. To play the stored sound, use an [AudioStreamPlayer](class_audiostreamplayer.md#class-audiostreamplayer) (for non-positional audio) or [AudioStreamPlayer2D](class_audiostreamplayer2d.md#class-audiostreamplayer2d)/[AudioStreamPlayer3D](class_audiostreamplayer3d.md#class-audiostreamplayer3d) (for positional audio). The sound can be looped.

This class can also be used to store dynamically-generated PCM audio data. See also [AudioStreamGenerator](class_audiostreamgenerator.md#class-audiostreamgenerator) for procedural audio generation.

<a id="tutorials"></a>

## Tutorials

- [Audio streams](../tutorials/audio/audio_streams.md)
- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray) | [data](class_audiostreamwav.md#class-audiostreamwav-property-data) | `PackedByteArray()` |
| [Format](class_audiostreamwav.md#enum-audiostreamwav-format) | [format](class_audiostreamwav.md#class-audiostreamwav-property-format) | `0` |
| [int](class_int.md#class-int) | [loop_begin](class_audiostreamwav.md#class-audiostreamwav-property-loop-begin) | `0` |
| [int](class_int.md#class-int) | [loop_end](class_audiostreamwav.md#class-audiostreamwav-property-loop-end) | `0` |
| [LoopMode](class_audiostreamwav.md#enum-audiostreamwav-loopmode) | [loop_mode](class_audiostreamwav.md#class-audiostreamwav-property-loop-mode) | `0` |
| [int](class_int.md#class-int) | [mix_rate](class_audiostreamwav.md#class-audiostreamwav-property-mix-rate) | `44100` |
| [bool](class_bool.md#class-bool) | [stereo](class_audiostreamwav.md#class-audiostreamwav-property-stereo) | `false` |
| [Dictionary](class_dictionary.md#class-dictionary) | [tags](class_audiostreamwav.md#class-audiostreamwav-property-tags) | `{}` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [AudioStreamWAV](class_audiostreamwav.md#class-audiostreamwav) | [load_from_buffer](class_audiostreamwav.md#class-audiostreamwav-method-load-from-buffer)(stream_data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray), options: [Dictionary](class_dictionary.md#class-dictionary) = {}) static |
| [AudioStreamWAV](class_audiostreamwav.md#class-audiostreamwav) | [load_from_file](class_audiostreamwav.md#class-audiostreamwav-method-load-from-file)(path: [String](class_string.md#class-string), options: [Dictionary](class_dictionary.md#class-dictionary) = {}) static |
| [Error](class_@globalscope.md#enum-globalscope-error) | [save_to_wav](class_audiostreamwav.md#class-audiostreamwav-method-save-to-wav)(path: [String](class_string.md#class-string)) |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-audiostreamwav-format"></a>

enum **Format**: [🔗](class_audiostreamwav.md#enum-audiostreamwav-format)

<a id="class-audiostreamwav-constant-format-8-bits"></a>

[Format](class_audiostreamwav.md#enum-audiostreamwav-format) **FORMAT_8_BITS** = `0`

8-bit PCM audio codec.

<a id="class-audiostreamwav-constant-format-16-bits"></a>

[Format](class_audiostreamwav.md#enum-audiostreamwav-format) **FORMAT_16_BITS** = `1`

16-bit PCM audio codec.

<a id="class-audiostreamwav-constant-format-ima-adpcm"></a>

[Format](class_audiostreamwav.md#enum-audiostreamwav-format) **FORMAT_IMA_ADPCM** = `2`

Audio is lossily compressed as IMA ADPCM.

<a id="class-audiostreamwav-constant-format-qoa"></a>

[Format](class_audiostreamwav.md#enum-audiostreamwav-format) **FORMAT_QOA** = `3`

Audio is lossily compressed as [Quite OK Audio](https://qoaformat.org/).

---


<a id="enum-audiostreamwav-loopmode"></a>

enum **LoopMode**: [🔗](class_audiostreamwav.md#enum-audiostreamwav-loopmode)

<a id="class-audiostreamwav-constant-loop-disabled"></a>

[LoopMode](class_audiostreamwav.md#enum-audiostreamwav-loopmode) **LOOP_DISABLED** = `0`

Audio does not loop.

<a id="class-audiostreamwav-constant-loop-forward"></a>

[LoopMode](class_audiostreamwav.md#enum-audiostreamwav-loopmode) **LOOP_FORWARD** = `1`

Audio loops the data between [loop_begin](class_audiostreamwav.md#class-audiostreamwav-property-loop-begin) and [loop_end](class_audiostreamwav.md#class-audiostreamwav-property-loop-end), playing forward only.

<a id="class-audiostreamwav-constant-loop-pingpong"></a>

[LoopMode](class_audiostreamwav.md#enum-audiostreamwav-loopmode) **LOOP_PINGPONG** = `2`

Audio loops the data between [loop_begin](class_audiostreamwav.md#class-audiostreamwav-property-loop-begin) and [loop_end](class_audiostreamwav.md#class-audiostreamwav-property-loop-end), playing back and forth.

<a id="class-audiostreamwav-constant-loop-backward"></a>

[LoopMode](class_audiostreamwav.md#enum-audiostreamwav-loopmode) **LOOP_BACKWARD** = `3`

Audio loops the data between [loop_begin](class_audiostreamwav.md#class-audiostreamwav-property-loop-begin) and [loop_end](class_audiostreamwav.md#class-audiostreamwav-property-loop-end), playing backward only.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-audiostreamwav-property-data"></a>

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **data** = `PackedByteArray()` [🔗](class_audiostreamwav.md#class-audiostreamwav-property-data)

- void **set_data**(value: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))
- [PackedByteArray](class_packedbytearray.md#class-packedbytearray) **get_data**()

Contains the audio data in bytes.

**Note:** If [format](class_audiostreamwav.md#class-audiostreamwav-property-format) is set to [FORMAT_8_BITS](class_audiostreamwav.md#class-audiostreamwav-constant-format-8-bits), this property expects signed 8-bit PCM data. To convert from unsigned 8-bit PCM, subtract 128 from each byte.

**Note:** If [format](class_audiostreamwav.md#class-audiostreamwav-property-format) is set to [FORMAT_QOA](class_audiostreamwav.md#class-audiostreamwav-constant-format-qoa), this property expects data from a full QOA file.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray](class_packedbytearray.md#class-packedbytearray) for more details.

---


<a id="class-audiostreamwav-property-format"></a>

[Format](class_audiostreamwav.md#enum-audiostreamwav-format) **format** = `0` [🔗](class_audiostreamwav.md#class-audiostreamwav-property-format)

- void **set_format**(value: [Format](class_audiostreamwav.md#enum-audiostreamwav-format))
- [Format](class_audiostreamwav.md#enum-audiostreamwav-format) **get_format**()

Audio format.

---


<a id="class-audiostreamwav-property-loop-begin"></a>

[int](class_int.md#class-int) **loop_begin** = `0` [🔗](class_audiostreamwav.md#class-audiostreamwav-property-loop-begin)

- void **set_loop_begin**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_loop_begin**()

The loop start point (in number of samples, relative to the beginning of the stream).

---


<a id="class-audiostreamwav-property-loop-end"></a>

[int](class_int.md#class-int) **loop_end** = `0` [🔗](class_audiostreamwav.md#class-audiostreamwav-property-loop-end)

- void **set_loop_end**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_loop_end**()

The loop end point (in number of samples, relative to the beginning of the stream).

---


<a id="class-audiostreamwav-property-loop-mode"></a>

[LoopMode](class_audiostreamwav.md#enum-audiostreamwav-loopmode) **loop_mode** = `0` [🔗](class_audiostreamwav.md#class-audiostreamwav-property-loop-mode)

- void **set_loop_mode**(value: [LoopMode](class_audiostreamwav.md#enum-audiostreamwav-loopmode))
- [LoopMode](class_audiostreamwav.md#enum-audiostreamwav-loopmode) **get_loop_mode**()

The loop mode.

---


<a id="class-audiostreamwav-property-mix-rate"></a>

[int](class_int.md#class-int) **mix_rate** = `44100` [🔗](class_audiostreamwav.md#class-audiostreamwav-property-mix-rate)

- void **set_mix_rate**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_mix_rate**()

The sample rate for mixing this audio. Higher values require more storage space, but result in better quality.

In games, common sample rates in use are `11025`, `16000`, `22050`, `32000`, `44100`, and `48000`.

According to the [Nyquist-Shannon sampling theorem](https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem), there is no quality difference to human hearing when going past 40,000 Hz (since most humans can only hear up to ~20,000 Hz, often less). If you are using lower-pitched sounds such as voices, lower sample rates such as `32000` or `22050` may be usable with no loss in quality.

---


<a id="class-audiostreamwav-property-stereo"></a>

[bool](class_bool.md#class-bool) **stereo** = `false` [🔗](class_audiostreamwav.md#class-audiostreamwav-property-stereo)

- void **set_stereo**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_stereo**()

If `true`, audio is stereo.

---


<a id="class-audiostreamwav-property-tags"></a>

[Dictionary](class_dictionary.md#class-dictionary) **tags** = `{}` [🔗](class_audiostreamwav.md#class-audiostreamwav-property-tags)

- void **set_tags**(value: [Dictionary](class_dictionary.md#class-dictionary))
- [Dictionary](class_dictionary.md#class-dictionary) **get_tags**()

Contains user-defined tags if found in the WAV data.

Commonly used tags include `title`, `artist`, `album`, `tracknumber`, and `date` (`date` does not have a standard date format).

**Note:** No tag is *guaranteed* to be present in every file, so make sure to account for the keys not always existing.

**Note:** Only WAV files using a `LIST` chunk with an identifier of `INFO` to encode the tags are currently supported.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-audiostreamwav-method-load-from-buffer"></a>

[AudioStreamWAV](class_audiostreamwav.md#class-audiostreamwav) **load_from_buffer**(stream_data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray), options: [Dictionary](class_dictionary.md#class-dictionary) = {}) static [🔗](class_audiostreamwav.md#class-audiostreamwav-method-load-from-buffer)

Creates a new **AudioStreamWAV** instance from the given buffer. The buffer must contain WAV data.

The keys and values of `options` match the properties of [ResourceImporterWAV](class_resourceimporterwav.md#class-resourceimporterwav). The usage of `options` is identical to [load_from_file()](class_audiostreamwav.md#class-audiostreamwav-method-load-from-file).

---


<a id="class-audiostreamwav-method-load-from-file"></a>

[AudioStreamWAV](class_audiostreamwav.md#class-audiostreamwav) **load_from_file**(path: [String](class_string.md#class-string), options: [Dictionary](class_dictionary.md#class-dictionary) = {}) static [🔗](class_audiostreamwav.md#class-audiostreamwav-method-load-from-file)

Creates a new **AudioStreamWAV** instance from the given file path. The file must be in WAV format.

The keys and values of `options` match the properties of [ResourceImporterWAV](class_resourceimporterwav.md#class-resourceimporterwav).

**Example:** Load the first file dropped as a WAV and play it:

```gdscript
@onready var audio_player = $AudioStreamPlayer

func _ready():
    get_window().files_dropped.connect(_on_files_dropped)

func _on_files_dropped(files):
    if files[0].get_extension() == "wav":
        audio_player.stream = AudioStreamWAV.load_from_file(files[0], {
                "force/max_rate": true,
                "force/max_rate_hz": 11025
            })
        audio_player.play()
```

---


<a id="class-audiostreamwav-method-save-to-wav"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **save_to_wav**(path: [String](class_string.md#class-string)) [🔗](class_audiostreamwav.md#class-audiostreamwav-method-save-to-wav)

Saves the AudioStreamWAV as a WAV file to `path`. Samples with IMA ADPCM or Quite OK Audio formats can't be saved.

**Note:** A `.wav` extension is automatically appended to `path` if it is missing.
