> Source: https://docs.godotengine.org/en/4.7/classes/class_audioeffectstereoenhance.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="audioeffectstereoenhance"></a>

<a id="class-audioeffectstereoenhance"></a>

# AudioEffectStereoEnhance

**Inherits:** [AudioEffect](class_audioeffect.md#class-audioeffect) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Adds a stereo manipulation audio effect to an audio bus.

Controls gain of the side channels, and widens the stereo image.

<a id="description"></a>

## Description

Adjusts gain of the left and right channels, and makes mono sounds stereo through phase shifting.

<a id="tutorials"></a>

## Tutorials

- [Audio buses](../tutorials/audio/audio_buses.md)
- [Audio effects](../tutorials/audio/audio_effects.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [pan_pullout](class_audioeffectstereoenhance.md#class-audioeffectstereoenhance-property-pan-pullout) | `1.0` |
| [float](class_float.md#class-float) | [surround](class_audioeffectstereoenhance.md#class-audioeffectstereoenhance-property-surround) | `0.0` |
| [float](class_float.md#class-float) | [time_pullout_ms](class_audioeffectstereoenhance.md#class-audioeffectstereoenhance-property-time-pullout-ms) | `0.0` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-audioeffectstereoenhance-property-pan-pullout"></a>

[float](class_float.md#class-float) **pan_pullout** = `1.0` [🔗](class_audioeffectstereoenhance.md#class-audioeffectstereoenhance-property-pan-pullout)

- void **set_pan_pullout**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_pan_pullout**()

Gain of the side channels, if they exist. A value of 0 will downmix stereo to mono. Value can range from 0 to 4.

---


<a id="class-audioeffectstereoenhance-property-surround"></a>

[float](class_float.md#class-float) **surround** = `0.0` [🔗](class_audioeffectstereoenhance.md#class-audioeffectstereoenhance-property-surround)

- void **set_surround**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_surround**()

Widens the stereo image through phase shifting in conjunction with [time_pullout_ms](class_audioeffectstereoenhance.md#class-audioeffectstereoenhance-property-time-pullout-ms). Just pans sound to the left channel if [time_pullout_ms](class_audioeffectstereoenhance.md#class-audioeffectstereoenhance-property-time-pullout-ms) is 0. Value can range from 0 to 1.

---


<a id="class-audioeffectstereoenhance-property-time-pullout-ms"></a>

[float](class_float.md#class-float) **time_pullout_ms** = `0.0` [🔗](class_audioeffectstereoenhance.md#class-audioeffectstereoenhance-property-time-pullout-ms)

- void **set_time_pullout**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_time_pullout**()

Widens the stereo image through phase shifting in conjunction with [surround](class_audioeffectstereoenhance.md#class-audioeffectstereoenhance-property-surround). Just delays the right channel if [surround](class_audioeffectstereoenhance.md#class-audioeffectstereoenhance-property-surround) is 0. Value is in milliseconds, and can range from 0 to 50.
