> Source: https://docs.godotengine.org/en/4.7/classes/class_audioeffectcapture.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="audioeffectcapture"></a>

<a id="class-audioeffectcapture"></a>

# AudioEffectCapture

**Inherits:** [AudioEffect](class_audioeffect.md#class-audioeffect) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Exposes audio samples from an audio bus in real-time, such that it can be accessed as data.

<a id="description"></a>

## Description

Copies all audio frames, also known as "samples" or "audio samples", from the attached audio bus into its internal ring buffer. This effect does not alter the audio. Can be used for storing real-time audio data for playback, and for creating real-time audio visualizations, like an oscilloscope.

Application code should consume these audio frames from this ring buffer using [get_buffer()](class_audioeffectcapture.md#class-audioeffectcapture-method-get-buffer) and process it as needed, for example to capture data from an [AudioStreamMicrophone](class_audiostreammicrophone.md#class-audiostreammicrophone), implement application-defined effects, or to transmit audio over the network. When capturing audio data from a microphone, the format of the samples will be stereo 32-bit floating-point PCM.

Unlike [AudioEffectRecord](class_audioeffectrecord.md#class-audioeffectrecord), this effect only returns the raw audio samples instead of encoding them into an [AudioStream](class_audiostream.md#class-audiostream).

<a id="tutorials"></a>

## Tutorials

- [Audio buses](../tutorials/audio/audio_buses.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [buffer_length](class_audioeffectcapture.md#class-audioeffectcapture-property-buffer-length) | `0.1` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [can_get_buffer](class_audioeffectcapture.md#class-audioeffectcapture-method-can-get-buffer)(frames: [int](class_int.md#class-int)) const |
| void | [clear_buffer](class_audioeffectcapture.md#class-audioeffectcapture-method-clear-buffer)() |
| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) | [get_buffer](class_audioeffectcapture.md#class-audioeffectcapture-method-get-buffer)(frames: [int](class_int.md#class-int)) |
| [int](class_int.md#class-int) | [get_buffer_length_frames](class_audioeffectcapture.md#class-audioeffectcapture-method-get-buffer-length-frames)() const |
| [int](class_int.md#class-int) | [get_discarded_frames](class_audioeffectcapture.md#class-audioeffectcapture-method-get-discarded-frames)() const |
| [int](class_int.md#class-int) | [get_frames_available](class_audioeffectcapture.md#class-audioeffectcapture-method-get-frames-available)() const |
| [int](class_int.md#class-int) | [get_pushed_frames](class_audioeffectcapture.md#class-audioeffectcapture-method-get-pushed-frames)() const |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-audioeffectcapture-property-buffer-length"></a>

[float](class_float.md#class-float) **buffer_length** = `0.1` [🔗](class_audioeffectcapture.md#class-audioeffectcapture-property-buffer-length)

- void **set_buffer_length**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_buffer_length**()

Length of the internal ring buffer, in seconds. Higher values keep data around for longer, but require more memory. Value can range from 0.01 to 10.

**Note:** Setting the buffer length will have no effect if already initialized.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-audioeffectcapture-method-can-get-buffer"></a>

[bool](class_bool.md#class-bool) **can_get_buffer**(frames: [int](class_int.md#class-int)) const [🔗](class_audioeffectcapture.md#class-audioeffectcapture-method-can-get-buffer)

Returns `true` if at least `frames` samples are available to read in the internal ring buffer.

---


<a id="class-audioeffectcapture-method-clear-buffer"></a>

void **clear_buffer**() [🔗](class_audioeffectcapture.md#class-audioeffectcapture-method-clear-buffer)

Clears the internal ring buffer.

**Note:** Calling this during a capture can cause the loss of samples which causes popping in the playback.

---


<a id="class-audioeffectcapture-method-get-buffer"></a>

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **get_buffer**(frames: [int](class_int.md#class-int)) [🔗](class_audioeffectcapture.md#class-audioeffectcapture-method-get-buffer)

Gets the next `frames` samples from the internal ring buffer.

Returns a [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) containing exactly `frames` samples if available, or an empty [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) if insufficient data was available.

The samples are signed floating-point PCM between `-1` and `1`. You will have to scale them if you want to use them as 8 or 16-bit integer samples. (`v = 0x7fff * samples[0].x`)

---


<a id="class-audioeffectcapture-method-get-buffer-length-frames"></a>

[int](class_int.md#class-int) **get_buffer_length_frames**() const [🔗](class_audioeffectcapture.md#class-audioeffectcapture-method-get-buffer-length-frames)

Returns the total size of the internal ring buffer in number of samples.

---


<a id="class-audioeffectcapture-method-get-discarded-frames"></a>

[int](class_int.md#class-int) **get_discarded_frames**() const [🔗](class_audioeffectcapture.md#class-audioeffectcapture-method-get-discarded-frames)

Returns the number of samples discarded from the audio bus due to full buffer.

---


<a id="class-audioeffectcapture-method-get-frames-available"></a>

[int](class_int.md#class-int) **get_frames_available**() const [🔗](class_audioeffectcapture.md#class-audioeffectcapture-method-get-frames-available)

Returns the number of samples available to read using [get_buffer()](class_audioeffectcapture.md#class-audioeffectcapture-method-get-buffer).

---


<a id="class-audioeffectcapture-method-get-pushed-frames"></a>

[int](class_int.md#class-int) **get_pushed_frames**() const [🔗](class_audioeffectcapture.md#class-audioeffectcapture-method-get-pushed-frames)

Returns the number of samples inserted from the audio bus.
