> Source: https://docs.godotengine.org/en/4.7/classes/class_audioeffectdistortion.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="audioeffectdistortion"></a>

<a id="class-audioeffectdistortion"></a>

# AudioEffectDistortion

**Inherits:** [AudioEffect](class_audioeffect.md#class-audioeffect) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Adds a distortion audio effect to an audio bus.

Remaps audio samples using a nonlinear function to achieve a distorted sound.

<a id="description"></a>

## Description

A "distortion" effect modifies the waveform via a nonlinear mathematical function (see available ones in [Mode](class_audioeffectdistortion.md#enum-audioeffectdistortion-mode)), based on the amplitude of the waveform's samples.

**Note:** In a nonlinear function, an input sample at *x* amplitude value, will either have its amplitude increased or decreased to a *y* value, based on the function value at *x*, which is why even at the same [drive](class_audioeffectdistortion.md#class-audioeffectdistortion-property-drive), the output sound will vary depending on the input's volume. To change the volume while maintaining the output waveform, use [post_gain](class_audioeffectdistortion.md#class-audioeffectdistortion-property-post-gain).

In this effect, each type is a different nonlinear function. The different types available are: clip, atan, lofi (bitcrush), overdrive, and waveshape. Every distortion type available here is symmetric: negative amplitude values are affected the same way as positive ones.

Although distortion will always change frequency content, usually by introducing high harmonics, different distortion types offer a range of sound qualities; from "soft" and "warm", to "crunchy" and "abrasive".

For games, it can help simulate sound coming from some saturated device or speaker very efficiently. It can also help the audio stand out in a mix, by introducing higher frequencies and increasing the volume.

**Note:** Although usually imperceptible, an enabled distortion effect still changes the sound even when [drive](class_audioeffectdistortion.md#class-audioeffectdistortion-property-drive) is set to 0. This is not a bug. If this behavior is undesirable, consider disabling the effect using [AudioServer.set_bus_effect_enabled()](class_audioserver.md#class-audioserver-method-set-bus-effect-enabled).

<a id="tutorials"></a>

## Tutorials

- [Audio buses](../tutorials/audio/audio_buses.md)
- [Audio effects](../tutorials/audio/audio_effects.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [drive](class_audioeffectdistortion.md#class-audioeffectdistortion-property-drive) | `0.0` |
| [float](class_float.md#class-float) | [keep_hf_hz](class_audioeffectdistortion.md#class-audioeffectdistortion-property-keep-hf-hz) | `16000.0` |
| [Mode](class_audioeffectdistortion.md#enum-audioeffectdistortion-mode) | [mode](class_audioeffectdistortion.md#class-audioeffectdistortion-property-mode) | `0` |
| [float](class_float.md#class-float) | [post_gain](class_audioeffectdistortion.md#class-audioeffectdistortion-property-post-gain) | `0.0` |
| [float](class_float.md#class-float) | [pre_gain](class_audioeffectdistortion.md#class-audioeffectdistortion-property-pre-gain) | `0.0` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-audioeffectdistortion-mode"></a>

enum **Mode**: [🔗](class_audioeffectdistortion.md#enum-audioeffectdistortion-mode)

<a id="class-audioeffectdistortion-constant-mode-clip"></a>

[Mode](class_audioeffectdistortion.md#enum-audioeffectdistortion-mode) **MODE_CLIP** = `0`

Flattens the waveform at 0 dB in a sharp manner. [drive](class_audioeffectdistortion.md#class-audioeffectdistortion-property-drive) increases amplitude of samples exponentially. This mode functions as a hard clipper if [drive](class_audioeffectdistortion.md#class-audioeffectdistortion-property-drive) is set to 0, and is the only mode that clips audio signals at 0 dB.

<a id="class-audioeffectdistortion-constant-mode-atan"></a>

[Mode](class_audioeffectdistortion.md#enum-audioeffectdistortion-mode) **MODE_ATAN** = `1`

Flattens the waveform in a smooth manner, following an arctangent curve. The audio decreases in volume, before flattening peaks to `PI * 4.0` (linear value), if it was normalized beforehand.

<a id="class-audioeffectdistortion-constant-mode-lofi"></a>

[Mode](class_audioeffectdistortion.md#enum-audioeffectdistortion-mode) **MODE_LOFI** = `2`

Decreases audio bit depth to achieve a low-resolution audio signal, going from 16-bit to 2-bit. Can be used to emulate the sound of early digital audio devices.

<a id="class-audioeffectdistortion-constant-mode-overdrive"></a>

[Mode](class_audioeffectdistortion.md#enum-audioeffectdistortion-mode) **MODE_OVERDRIVE** = `3`

Emulates the warm distortion produced by a field effect transistor, which is commonly used in solid-state musical instrument amplifiers. [drive](class_audioeffectdistortion.md#class-audioeffectdistortion-property-drive) has no effect in this mode.

<a id="class-audioeffectdistortion-constant-mode-waveshape"></a>

[Mode](class_audioeffectdistortion.md#enum-audioeffectdistortion-mode) **MODE_WAVESHAPE** = `4`

Flattens the waveform in a smooth manner, until it reaches a sharp peak at `drive = 1`, following a generic absolute sigmoid function.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-audioeffectdistortion-property-drive"></a>

[float](class_float.md#class-float) **drive** = `0.0` [🔗](class_audioeffectdistortion.md#class-audioeffectdistortion-property-drive)

- void **set_drive**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_drive**()

Distortion intensity. Controls how much of the input audio is affected by the distortion curve by moving from a linear function to a nonlinear one. Value can range from 0 to 1.

---


<a id="class-audioeffectdistortion-property-keep-hf-hz"></a>

[float](class_float.md#class-float) **keep_hf_hz** = `16000.0` [🔗](class_audioeffectdistortion.md#class-audioeffectdistortion-property-keep-hf-hz)

- void **set_keep_hf_hz**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_keep_hf_hz**()

High-pass filter, in Hz. Frequencies higher than this value will not be affected by the distortion. Value can range from 1 to 20000.

---


<a id="class-audioeffectdistortion-property-mode"></a>

[Mode](class_audioeffectdistortion.md#enum-audioeffectdistortion-mode) **mode** = `0` [🔗](class_audioeffectdistortion.md#class-audioeffectdistortion-property-mode)

- void **set_mode**(value: [Mode](class_audioeffectdistortion.md#enum-audioeffectdistortion-mode))
- [Mode](class_audioeffectdistortion.md#enum-audioeffectdistortion-mode) **get_mode**()

Distortion type. Changes the nonlinear function used to distort the waveform. See [Mode](class_audioeffectdistortion.md#enum-audioeffectdistortion-mode).

---


<a id="class-audioeffectdistortion-property-post-gain"></a>

[float](class_float.md#class-float) **post_gain** = `0.0` [🔗](class_audioeffectdistortion.md#class-audioeffectdistortion-property-post-gain)

- void **set_post_gain**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_post_gain**()

Gain after the effect, in dB. Value can range from -80 to 24.

---


<a id="class-audioeffectdistortion-property-pre-gain"></a>

[float](class_float.md#class-float) **pre_gain** = `0.0` [🔗](class_audioeffectdistortion.md#class-audioeffectdistortion-property-pre-gain)

- void **set_pre_gain**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_pre_gain**()

Gain before the effect, in dB. Value can range from -60 to 60.
