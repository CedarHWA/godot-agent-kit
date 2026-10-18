> Source: https://docs.godotengine.org/en/4.7/classes/class_audioeffectrecord.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="audioeffectrecord"></a>

<a id="class-audioeffectrecord"></a>

# AudioEffectRecord

**Inherits:** [AudioEffect](class_audioeffect.md#class-audioeffect) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Audio effect used for recording the sound from an audio bus.

<a id="description"></a>

## Description

Allows the user to record the sound from an audio bus into an [AudioStreamWAV](class_audiostreamwav.md#class-audiostreamwav). When used on the Master audio bus, this includes all audio output by Godot.

Unlike [AudioEffectCapture](class_audioeffectcapture.md#class-audioeffectcapture), this effect encodes the recording with the given format (8-bit, 16-bit, or compressed) instead of giving access to the raw audio samples.

Can be used (with an [AudioStreamMicrophone](class_audiostreammicrophone.md#class-audiostreammicrophone)) to record from a microphone.

**Note:** [ProjectSettings.audio/driver/enable_input](class_projectsettings.md#class-projectsettings-property-audio-driver-enable-input) must be `true` for audio input to work. See also that setting's description for caveats related to permissions and operating system privacy settings.

<a id="tutorials"></a>

## Tutorials

- [Recording with microphone](../tutorials/audio/recording_with_microphone.md)
- [Audio Microphone Record Demo](https://godotengine.org/asset-library/asset/2760)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Format](class_audiostreamwav.md#enum-audiostreamwav-format) | [format](class_audioeffectrecord.md#class-audioeffectrecord-property-format) | `1` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [AudioStreamWAV](class_audiostreamwav.md#class-audiostreamwav) | [get_recording](class_audioeffectrecord.md#class-audioeffectrecord-method-get-recording)() const |
| [bool](class_bool.md#class-bool) | [is_recording_active](class_audioeffectrecord.md#class-audioeffectrecord-method-is-recording-active)() const |
| void | [set_recording_active](class_audioeffectrecord.md#class-audioeffectrecord-method-set-recording-active)(record: [bool](class_bool.md#class-bool)) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-audioeffectrecord-property-format"></a>

[Format](class_audiostreamwav.md#enum-audiostreamwav-format) **format** = `1` [🔗](class_audioeffectrecord.md#class-audioeffectrecord-property-format)

- void **set_format**(value: [Format](class_audiostreamwav.md#enum-audiostreamwav-format))
- [Format](class_audiostreamwav.md#enum-audiostreamwav-format) **get_format**()

Specifies the format in which the sample will be recorded.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-audioeffectrecord-method-get-recording"></a>

[AudioStreamWAV](class_audiostreamwav.md#class-audiostreamwav) **get_recording**() const [🔗](class_audioeffectrecord.md#class-audioeffectrecord-method-get-recording)

Returns the recorded sample.

---


<a id="class-audioeffectrecord-method-is-recording-active"></a>

[bool](class_bool.md#class-bool) **is_recording_active**() const [🔗](class_audioeffectrecord.md#class-audioeffectrecord-method-is-recording-active)

Returns whether the recording is active or not.

---


<a id="class-audioeffectrecord-method-set-recording-active"></a>

void **set_recording_active**(record: [bool](class_bool.md#class-bool)) [🔗](class_audioeffectrecord.md#class-audioeffectrecord-method-set-recording-active)

If `true`, the sound will be recorded. Note that restarting the recording will remove the previously recorded sample.
