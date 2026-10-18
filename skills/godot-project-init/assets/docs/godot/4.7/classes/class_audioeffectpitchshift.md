> Source: https://docs.godotengine.org/en/4.7/classes/class_audioeffectpitchshift.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="audioeffectpitchshift"></a>

<a id="class-audioeffectpitchshift"></a>

# AudioEffectPitchShift

**Inherits:** [AudioEffect](class_audioeffect.md#class-audioeffect) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Adds a pitch-shifting audio effect to an audio bus.

Raises or lowers the pitch of the input audio.

<a id="description"></a>

## Description

Allows modulation of pitch without modifying speed. All frequencies can be raised or lowered with minimal effect on transients.

<a id="tutorials"></a>

## Tutorials

- [Audio buses](../tutorials/audio/audio_buses.md)
- [Audio effects](../tutorials/audio/audio_effects.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [FFTSize](class_audioeffectpitchshift.md#enum-audioeffectpitchshift-fftsize) | [fft_size](class_audioeffectpitchshift.md#class-audioeffectpitchshift-property-fft-size) | `3` |
| [int](class_int.md#class-int) | [oversampling](class_audioeffectpitchshift.md#class-audioeffectpitchshift-property-oversampling) | `4` |
| [float](class_float.md#class-float) | [pitch_scale](class_audioeffectpitchshift.md#class-audioeffectpitchshift-property-pitch-scale) | `1.0` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-audioeffectpitchshift-fftsize"></a>

enum **FFTSize**: [🔗](class_audioeffectpitchshift.md#enum-audioeffectpitchshift-fftsize)

<a id="class-audioeffectpitchshift-constant-fft-size-256"></a>

[FFTSize](class_audioeffectpitchshift.md#enum-audioeffectpitchshift-fftsize) **FFT_SIZE_256** = `0`

Use a buffer of 256 samples for the Fast Fourier transform. Lowest latency, but least stable over time.

<a id="class-audioeffectpitchshift-constant-fft-size-512"></a>

[FFTSize](class_audioeffectpitchshift.md#enum-audioeffectpitchshift-fftsize) **FFT_SIZE_512** = `1`

Use a buffer of 512 samples for the Fast Fourier transform. Low latency, but less stable over time.

<a id="class-audioeffectpitchshift-constant-fft-size-1024"></a>

[FFTSize](class_audioeffectpitchshift.md#enum-audioeffectpitchshift-fftsize) **FFT_SIZE_1024** = `2`

Use a buffer of 1024 samples for the Fast Fourier transform. This is a compromise between latency and stability over time.

<a id="class-audioeffectpitchshift-constant-fft-size-2048"></a>

[FFTSize](class_audioeffectpitchshift.md#enum-audioeffectpitchshift-fftsize) **FFT_SIZE_2048** = `3`

Use a buffer of 2048 samples for the Fast Fourier transform. High latency, but stable over time.

<a id="class-audioeffectpitchshift-constant-fft-size-4096"></a>

[FFTSize](class_audioeffectpitchshift.md#enum-audioeffectpitchshift-fftsize) **FFT_SIZE_4096** = `4`

Use a buffer of 4096 samples for the Fast Fourier transform. Highest latency, but most stable over time.

<a id="class-audioeffectpitchshift-constant-fft-size-max"></a>

[FFTSize](class_audioeffectpitchshift.md#enum-audioeffectpitchshift-fftsize) **FFT_SIZE_MAX** = `5`

Represents the size of the [FFTSize](class_audioeffectpitchshift.md#enum-audioeffectpitchshift-fftsize) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-audioeffectpitchshift-property-fft-size"></a>

[FFTSize](class_audioeffectpitchshift.md#enum-audioeffectpitchshift-fftsize) **fft_size** = `3` [🔗](class_audioeffectpitchshift.md#class-audioeffectpitchshift-property-fft-size)

- void **set_fft_size**(value: [FFTSize](class_audioeffectpitchshift.md#enum-audioeffectpitchshift-fftsize))
- [FFTSize](class_audioeffectpitchshift.md#enum-audioeffectpitchshift-fftsize) **get_fft_size**()

The size of the [Fast Fourier transform](https://en.wikipedia.org/wiki/Fast_Fourier_transform) buffer. Higher values smooth out the effect over time, but have greater latency. The effects of this higher latency are especially noticeable on audio signals that have sudden amplitude changes.

---


<a id="class-audioeffectpitchshift-property-oversampling"></a>

[int](class_int.md#class-int) **oversampling** = `4` [🔗](class_audioeffectpitchshift.md#class-audioeffectpitchshift-property-oversampling)

- void **set_oversampling**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_oversampling**()

The oversampling factor to use. Higher values result in better quality, but are more demanding on the CPU and may cause audio cracking if the CPU can't keep up.

---


<a id="class-audioeffectpitchshift-property-pitch-scale"></a>

[float](class_float.md#class-float) **pitch_scale** = `1.0` [🔗](class_audioeffectpitchshift.md#class-audioeffectpitchshift-property-pitch-scale)

- void **set_pitch_scale**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_pitch_scale**()

The pitch scale to use. `1.0` is the default pitch and plays sounds unaffected. [pitch_scale](class_audioeffectpitchshift.md#class-audioeffectpitchshift-property-pitch-scale) can range from 0 (infinitely low pitch, inaudible) to 16 (16 times higher than the initial pitch).
