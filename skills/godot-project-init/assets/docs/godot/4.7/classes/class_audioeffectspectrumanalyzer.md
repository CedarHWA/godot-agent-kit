> Source: https://docs.godotengine.org/en/4.7/classes/class_audioeffectspectrumanalyzer.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="audioeffectspectrumanalyzer"></a>

<a id="class-audioeffectspectrumanalyzer"></a>

# AudioEffectSpectrumAnalyzer

**Inherits:** [AudioEffect](class_audioeffect.md#class-audioeffect) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Creates an [AudioEffectInstance](class_audioeffectinstance.md#class-audioeffectinstance) which performs frequency analysis and exposes results to be accessed in real-time.

<a id="description"></a>

## Description

Calculates a Fourier Transform of the audio signal. This effect does not alter the audio. Can be used for creating real-time audio visualizations, like a spectrogram.

This resource configures an [AudioEffectSpectrumAnalyzerInstance](class_audioeffectspectrumanalyzerinstance.md#class-audioeffectspectrumanalyzerinstance), which performs the actual analysis at runtime. An instance should be obtained with [AudioServer.get_bus_effect_instance()](class_audioserver.md#class-audioserver-method-get-bus-effect-instance) to make use of this effect.

<a id="tutorials"></a>

## Tutorials

- [Audio buses](../tutorials/audio/audio_buses.md)
- [Audio effects](../tutorials/audio/audio_effects.md)
- [Audio Spectrum Visualizer Demo](https://godotengine.org/asset-library/asset/2762)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [buffer_length](class_audioeffectspectrumanalyzer.md#class-audioeffectspectrumanalyzer-property-buffer-length) | `2.0` |
| [FFTSize](class_audioeffectspectrumanalyzer.md#enum-audioeffectspectrumanalyzer-fftsize) | [fft_size](class_audioeffectspectrumanalyzer.md#class-audioeffectspectrumanalyzer-property-fft-size) | `2` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-audioeffectspectrumanalyzer-fftsize"></a>

enum **FFTSize**: [🔗](class_audioeffectspectrumanalyzer.md#enum-audioeffectspectrumanalyzer-fftsize)

<a id="class-audioeffectspectrumanalyzer-constant-fft-size-256"></a>

[FFTSize](class_audioeffectspectrumanalyzer.md#enum-audioeffectspectrumanalyzer-fftsize) **FFT_SIZE_256** = `0`

Use a buffer of 256 samples for the Fast Fourier transform. Lowest latency, but least stable over time.

<a id="class-audioeffectspectrumanalyzer-constant-fft-size-512"></a>

[FFTSize](class_audioeffectspectrumanalyzer.md#enum-audioeffectspectrumanalyzer-fftsize) **FFT_SIZE_512** = `1`

Use a buffer of 512 samples for the Fast Fourier transform. Low latency, but less stable over time.

<a id="class-audioeffectspectrumanalyzer-constant-fft-size-1024"></a>

[FFTSize](class_audioeffectspectrumanalyzer.md#enum-audioeffectspectrumanalyzer-fftsize) **FFT_SIZE_1024** = `2`

Use a buffer of 1024 samples for the Fast Fourier transform. This is a compromise between latency and stability over time.

<a id="class-audioeffectspectrumanalyzer-constant-fft-size-2048"></a>

[FFTSize](class_audioeffectspectrumanalyzer.md#enum-audioeffectspectrumanalyzer-fftsize) **FFT_SIZE_2048** = `3`

Use a buffer of 2048 samples for the Fast Fourier transform. High latency, but stable over time.

<a id="class-audioeffectspectrumanalyzer-constant-fft-size-4096"></a>

[FFTSize](class_audioeffectspectrumanalyzer.md#enum-audioeffectspectrumanalyzer-fftsize) **FFT_SIZE_4096** = `4`

Use a buffer of 4096 samples for the Fast Fourier transform. Highest latency, but most stable over time.

<a id="class-audioeffectspectrumanalyzer-constant-fft-size-max"></a>

[FFTSize](class_audioeffectspectrumanalyzer.md#enum-audioeffectspectrumanalyzer-fftsize) **FFT_SIZE_MAX** = `5`

Represents the size of the [FFTSize](class_audioeffectspectrumanalyzer.md#enum-audioeffectspectrumanalyzer-fftsize) enum.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-audioeffectspectrumanalyzer-property-buffer-length"></a>

[float](class_float.md#class-float) **buffer_length** = `2.0` [🔗](class_audioeffectspectrumanalyzer.md#class-audioeffectspectrumanalyzer-property-buffer-length)

- void **set_buffer_length**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_buffer_length**()

The length of the buffer to keep, in seconds. Higher values keep data around for longer, but require more memory. Value can range from 0.1 to 4.

---


<a id="class-audioeffectspectrumanalyzer-property-fft-size"></a>

[FFTSize](class_audioeffectspectrumanalyzer.md#enum-audioeffectspectrumanalyzer-fftsize) **fft_size** = `2` [🔗](class_audioeffectspectrumanalyzer.md#class-audioeffectspectrumanalyzer-property-fft-size)

- void **set_fft_size**(value: [FFTSize](class_audioeffectspectrumanalyzer.md#enum-audioeffectspectrumanalyzer-fftsize))
- [FFTSize](class_audioeffectspectrumanalyzer.md#enum-audioeffectspectrumanalyzer-fftsize) **get_fft_size**()

The size of the [Fast Fourier transform](https://en.wikipedia.org/wiki/Fast_Fourier_transform) buffer. Higher values smooth out the spectrum analysis over time, but have greater latency. The effects of this higher latency are especially noticeable with sudden amplitude changes.
