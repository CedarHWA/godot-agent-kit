> Source: https://docs.godotengine.org/en/4.7/classes/class_audioeffecthighpassfilter.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="audioeffecthighpassfilter"></a>

<a id="class-audioeffecthighpassfilter"></a>

# AudioEffectHighPassFilter

**Inherits:** [AudioEffectFilter](class_audioeffectfilter.md#class-audioeffectfilter) **<** [AudioEffect](class_audioeffect.md#class-audioeffect) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Adds a high-pass filter to an audio bus.

<a id="description"></a>

## Description

A "high-pass" filter attenuates frequencies lower than [AudioEffectFilter.cutoff_hz](class_audioeffectfilter.md#class-audioeffectfilter-property-cutoff-hz) and allows higher frequencies to pass unchanged.

This filter can be used to remove "strength" from a sound, and give low-end space for basses and impact sounds.

<a id="tutorials"></a>

## Tutorials

- [Audio buses](../tutorials/audio/audio_buses.md)
- [Audio effects](../tutorials/audio/audio_effects.md)
