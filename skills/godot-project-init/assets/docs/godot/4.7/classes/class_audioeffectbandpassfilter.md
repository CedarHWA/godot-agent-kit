> Source: https://docs.godotengine.org/en/4.7/classes/class_audioeffectbandpassfilter.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="audioeffectbandpassfilter"></a>

<a id="class-audioeffectbandpassfilter"></a>

# AudioEffectBandPassFilter

**Inherits:** [AudioEffectFilter](class_audioeffectfilter.md#class-audioeffectfilter) **<** [AudioEffect](class_audioeffect.md#class-audioeffect) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Adds a band-pass filter to an audio bus.

<a id="description"></a>

## Description

A "band-pass" filter allows the frequencies at [AudioEffectFilter.cutoff_hz](class_audioeffectfilter.md#class-audioeffectfilter-property-cutoff-hz) to pass unchanged, and attenuates frequencies outside the frequency threshold. It is the opposite of [AudioEffectBandLimitFilter](class_audioeffectbandlimitfilter.md#class-audioeffectbandlimitfilter) and [AudioEffectNotchFilter](class_audioeffectnotchfilter.md#class-audioeffectnotchfilter).

This filter can be used to emulate sounds coming from weak speakers.

<a id="tutorials"></a>

## Tutorials

- [Audio buses](../tutorials/audio/audio_buses.md)
- [Audio effects](../tutorials/audio/audio_effects.md)
