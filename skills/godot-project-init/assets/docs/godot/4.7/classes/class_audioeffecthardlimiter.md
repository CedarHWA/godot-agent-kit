> Source: https://docs.godotengine.org/en/4.7/classes/class_audioeffecthardlimiter.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="audioeffecthardlimiter"></a>

<a id="class-audioeffecthardlimiter"></a>

# AudioEffectHardLimiter

**Inherits:** [AudioEffect](class_audioeffect.md#class-audioeffect) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Adds a limiter audio effect to an audio bus.

Prevents audio signals from exceeding a specified volume level.

<a id="description"></a>

## Description

A "limiter" disallows audio signals from exceeding a given volume threshold level in dB. Hard limiters predict volume peaks, and will smoothly apply gain reduction when a peak crosses the ceiling threshold level to prevent clipping. It preserves the waveform and prevents it from crossing the ceiling threshold level. Adding one in the Master bus is recommended as a safety measure to prevent sudden volume peaks from occurring, and to prevent distortion caused by clipping, when the volume exceeds 0 dB.

If clipping is desired, consider [AudioEffectDistortion.MODE_CLIP](class_audioeffectdistortion.md#class-audioeffectdistortion-constant-mode-clip).

<a id="tutorials"></a>

## Tutorials

- [Audio buses](../tutorials/audio/audio_buses.md)
- [Audio effects](../tutorials/audio/audio_effects.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [ceiling_db](class_audioeffecthardlimiter.md#class-audioeffecthardlimiter-property-ceiling-db) | `-0.3` |
| [float](class_float.md#class-float) | [pre_gain_db](class_audioeffecthardlimiter.md#class-audioeffecthardlimiter-property-pre-gain-db) | `0.0` |
| [float](class_float.md#class-float) | [release](class_audioeffecthardlimiter.md#class-audioeffecthardlimiter-property-release) | `0.1` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-audioeffecthardlimiter-property-ceiling-db"></a>

[float](class_float.md#class-float) **ceiling_db** = `-0.3` [🔗](class_audioeffecthardlimiter.md#class-audioeffecthardlimiter-property-ceiling-db)

- void **set_ceiling_db**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_ceiling_db**()

The waveform's maximum allowed value, in dB. This value can range from -24 to 0.

The default value of -0.3 prevents potential inter-sample peaks (ISP) from crossing over 0 dB, which can cause slight distortion on some older hardware.

---


<a id="class-audioeffecthardlimiter-property-pre-gain-db"></a>

[float](class_float.md#class-float) **pre_gain_db** = `0.0` [🔗](class_audioeffecthardlimiter.md#class-audioeffecthardlimiter-property-pre-gain-db)

- void **set_pre_gain_db**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_pre_gain_db**()

Gain before limiting, in dB. Value can range from -24 to 24.

---


<a id="class-audioeffecthardlimiter-property-release"></a>

[float](class_float.md#class-float) **release** = `0.1` [🔗](class_audioeffecthardlimiter.md#class-audioeffecthardlimiter-property-release)

- void **set_release**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_release**()

Time it takes in seconds for the gain reduction to fully release. Value can range from 0.01 to 3.
