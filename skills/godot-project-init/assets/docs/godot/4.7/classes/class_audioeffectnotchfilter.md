> Source: https://docs.godotengine.org/en/4.7/classes/class_audioeffectnotchfilter.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="audioeffectnotchfilter"></a>

<a id="class-audioeffectnotchfilter"></a>

# AudioEffectNotchFilter

**Inherits:** [AudioEffectFilter](class_audioeffectfilter.md#class-audioeffectfilter) **<** [AudioEffect](class_audioeffect.md#class-audioeffect) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Adds a notch filter to an audio bus.

<a id="description"></a>

## Description

A "notch" filter attenuates frequencies at [AudioEffectFilter.cutoff_hz](class_audioeffectfilter.md#class-audioeffectfilter-property-cutoff-hz) and allows frequencies outside the frequency threshold to pass unchanged. It is a narrower and stronger version of [AudioEffectBandLimitFilter](class_audioeffectbandlimitfilter.md#class-audioeffectbandlimitfilter), and is the opposite of [AudioEffectBandPassFilter](class_audioeffectbandpassfilter.md#class-audioeffectbandpassfilter).

This filter can be used to give more room for other sounds to play at that frequency. Because of how much it attenuates frequencies, it can also be used to completely remove undesired frequencies.

<a id="tutorials"></a>

## Tutorials

- [Audio buses](../tutorials/audio/audio_buses.md)
- [Audio effects](../tutorials/audio/audio_effects.md)
