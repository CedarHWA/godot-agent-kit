> Source: https://docs.godotengine.org/en/4.7/classes/class_audioeffectcompressor.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="audioeffectcompressor"></a>

<a id="class-audioeffectcompressor"></a>

# AudioEffectCompressor

**Inherits:** [AudioEffect](class_audioeffect.md#class-audioeffect) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Adds a downward compressor audio effect to an audio bus.

Allows control of the dynamic range via a volume threshold and timing controls.

<a id="description"></a>

## Description

A "compressor" decreases the volume of sounds when it exceeds a certain volume threshold level.

A compressor can have many uses in a mix:

- To compress the whole volume in the Master bus (although an [AudioEffectHardLimiter](class_audioeffecthardlimiter.md#class-audioeffecthardlimiter) is probably better).
- To ensure balance of voice audio clips.
- To sidechain, using another bus as a trigger. This decreases the volume of the bus it is attached to, by using the volume from another audio bus for threshold detection. This technique is common in video game mixing to decrease the volume of music and SFX while voices are being heard. This effect is also known as "ducking".
- To accentuate transients by using a long attack, letting sounds exceed the volume threshold level for a short period before compressing them. This can be used to make SFX more punchy.

<a id="tutorials"></a>

## Tutorials

- [Audio buses](../tutorials/audio/audio_buses.md)
- [Audio effects](../tutorials/audio/audio_effects.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [attack_us](class_audioeffectcompressor.md#class-audioeffectcompressor-property-attack-us) | `20.0` |
| [float](class_float.md#class-float) | [gain](class_audioeffectcompressor.md#class-audioeffectcompressor-property-gain) | `0.0` |
| [float](class_float.md#class-float) | [mix](class_audioeffectcompressor.md#class-audioeffectcompressor-property-mix) | `1.0` |
| [float](class_float.md#class-float) | [ratio](class_audioeffectcompressor.md#class-audioeffectcompressor-property-ratio) | `4.0` |
| [float](class_float.md#class-float) | [release_ms](class_audioeffectcompressor.md#class-audioeffectcompressor-property-release-ms) | `250.0` |
| [StringName](class_stringname.md#class-stringname) | [sidechain](class_audioeffectcompressor.md#class-audioeffectcompressor-property-sidechain) | `&""` |
| [float](class_float.md#class-float) | [threshold](class_audioeffectcompressor.md#class-audioeffectcompressor-property-threshold) | `0.0` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-audioeffectcompressor-property-attack-us"></a>

[float](class_float.md#class-float) **attack_us** = `20.0` [🔗](class_audioeffectcompressor.md#class-audioeffectcompressor-property-attack-us)

- void **set_attack_us**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_attack_us**()

Compressor's reaction time when the audio exceeds the volume threshold level, in microseconds. Value can range from 20 to 2000.

---


<a id="class-audioeffectcompressor-property-gain"></a>

[float](class_float.md#class-float) **gain** = `0.0` [🔗](class_audioeffectcompressor.md#class-audioeffectcompressor-property-gain)

- void **set_gain**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_gain**()

Gain of the audio signal, in dB. Value can range from -20 to 20.

---


<a id="class-audioeffectcompressor-property-mix"></a>

[float](class_float.md#class-float) **mix** = `1.0` [🔗](class_audioeffectcompressor.md#class-audioeffectcompressor-property-mix)

- void **set_mix**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_mix**()

Balance between the original audio and the compressed audio. Value can range from 0 (totally dry) to 1 (totally wet).

---


<a id="class-audioeffectcompressor-property-ratio"></a>

[float](class_float.md#class-float) **ratio** = `4.0` [🔗](class_audioeffectcompressor.md#class-audioeffectcompressor-property-ratio)

- void **set_ratio**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_ratio**()

Amount of compression applied to the audio once it passes the volume threshold level. The higher the ratio, the stronger the compression applied to audio signals that pass the volume threshold level. Value can range from 1 to 48.

---


<a id="class-audioeffectcompressor-property-release-ms"></a>

[float](class_float.md#class-float) **release_ms** = `250.0` [🔗](class_audioeffectcompressor.md#class-audioeffectcompressor-property-release-ms)

- void **set_release_ms**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_release_ms**()

Compressor's delay time to stop decreasing the volume after the it falls below the volume threshold level, in milliseconds. Value can range from 20 to 2000.

---


<a id="class-audioeffectcompressor-property-sidechain"></a>

[StringName](class_stringname.md#class-stringname) **sidechain** = `&""` [🔗](class_audioeffectcompressor.md#class-audioeffectcompressor-property-sidechain)

- void **set_sidechain**(value: [StringName](class_stringname.md#class-stringname))
- [StringName](class_stringname.md#class-stringname) **get_sidechain**()

Audio bus to use for the volume threshold detection.

---


<a id="class-audioeffectcompressor-property-threshold"></a>

[float](class_float.md#class-float) **threshold** = `0.0` [🔗](class_audioeffectcompressor.md#class-audioeffectcompressor-property-threshold)

- void **set_threshold**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_threshold**()

The volume level above which compression is applied to the audio, in dB. Value can range from -60 to 0.
