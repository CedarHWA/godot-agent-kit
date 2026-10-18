> Source: https://docs.godotengine.org/en/4.7/classes/class_audioeffectchorus.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="audioeffectchorus"></a>

<a id="class-audioeffectchorus"></a>

# AudioEffectChorus

**Inherits:** [AudioEffect](class_audioeffect.md#class-audioeffect) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Adds a chorus audio effect to an audio bus.

Gives the impression of multiple audio sources.

<a id="description"></a>

## Description

A "chorus" effect creates multiple copies of the original audio (called "voices") with variations in pitch, and layers on top of the original, giving the impression that the sound comes from multiple sources. This creates spectral and spatial movement.

Each voice is played a short period of time after the original audio, controlled by `delay`. An internal low-frequency oscillator (LFO) controls their pitch, and `depth` controls the LFO's maximum amount.

In the real world, this kind of effect is found in pianos, choirs, and instrument ensembles.

This effect can also be used to widen mono audio and make digital sounds have a more natural or analog quality.

<a id="tutorials"></a>

## Tutorials

- [Audio buses](../tutorials/audio/audio_buses.md)
- [Audio effects](../tutorials/audio/audio_effects.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [dry](class_audioeffectchorus.md#class-audioeffectchorus-property-dry) | `1.0` |
| [float](class_float.md#class-float) | [voice/1/cutoff_hz](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-1-cutoff-hz) | `8000.0` |
| [float](class_float.md#class-float) | [voice/1/delay_ms](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-1-delay-ms) | `15.0` |
| [float](class_float.md#class-float) | [voice/1/depth_ms](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-1-depth-ms) | `2.0` |
| [float](class_float.md#class-float) | [voice/1/level_db](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-1-level-db) | `0.0` |
| [float](class_float.md#class-float) | [voice/1/pan](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-1-pan) | `-0.5` |
| [float](class_float.md#class-float) | [voice/1/rate_hz](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-1-rate-hz) | `0.8` |
| [float](class_float.md#class-float) | [voice/2/cutoff_hz](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-2-cutoff-hz) | `8000.0` |
| [float](class_float.md#class-float) | [voice/2/delay_ms](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-2-delay-ms) | `20.0` |
| [float](class_float.md#class-float) | [voice/2/depth_ms](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-2-depth-ms) | `3.0` |
| [float](class_float.md#class-float) | [voice/2/level_db](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-2-level-db) | `0.0` |
| [float](class_float.md#class-float) | [voice/2/pan](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-2-pan) | `0.5` |
| [float](class_float.md#class-float) | [voice/2/rate_hz](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-2-rate-hz) | `1.2` |
| [float](class_float.md#class-float) | [voice/3/cutoff_hz](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-3-cutoff-hz) |  |
| [float](class_float.md#class-float) | [voice/3/delay_ms](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-3-delay-ms) |  |
| [float](class_float.md#class-float) | [voice/3/depth_ms](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-3-depth-ms) |  |
| [float](class_float.md#class-float) | [voice/3/level_db](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-3-level-db) |  |
| [float](class_float.md#class-float) | [voice/3/pan](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-3-pan) |  |
| [float](class_float.md#class-float) | [voice/3/rate_hz](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-3-rate-hz) |  |
| [float](class_float.md#class-float) | [voice/4/cutoff_hz](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-4-cutoff-hz) |  |
| [float](class_float.md#class-float) | [voice/4/delay_ms](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-4-delay-ms) |  |
| [float](class_float.md#class-float) | [voice/4/depth_ms](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-4-depth-ms) |  |
| [float](class_float.md#class-float) | [voice/4/level_db](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-4-level-db) |  |
| [float](class_float.md#class-float) | [voice/4/pan](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-4-pan) |  |
| [float](class_float.md#class-float) | [voice/4/rate_hz](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-4-rate-hz) |  |
| [int](class_int.md#class-int) | [voice_count](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-count) | `2` |
| [float](class_float.md#class-float) | [wet](class_audioeffectchorus.md#class-audioeffectchorus-property-wet) | `0.5` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [float](class_float.md#class-float) | [get_voice_cutoff_hz](class_audioeffectchorus.md#class-audioeffectchorus-method-get-voice-cutoff-hz)(voice_idx: [int](class_int.md#class-int)) const |
| [float](class_float.md#class-float) | [get_voice_delay_ms](class_audioeffectchorus.md#class-audioeffectchorus-method-get-voice-delay-ms)(voice_idx: [int](class_int.md#class-int)) const |
| [float](class_float.md#class-float) | [get_voice_depth_ms](class_audioeffectchorus.md#class-audioeffectchorus-method-get-voice-depth-ms)(voice_idx: [int](class_int.md#class-int)) const |
| [float](class_float.md#class-float) | [get_voice_level_db](class_audioeffectchorus.md#class-audioeffectchorus-method-get-voice-level-db)(voice_idx: [int](class_int.md#class-int)) const |
| [float](class_float.md#class-float) | [get_voice_pan](class_audioeffectchorus.md#class-audioeffectchorus-method-get-voice-pan)(voice_idx: [int](class_int.md#class-int)) const |
| [float](class_float.md#class-float) | [get_voice_rate_hz](class_audioeffectchorus.md#class-audioeffectchorus-method-get-voice-rate-hz)(voice_idx: [int](class_int.md#class-int)) const |
| void | [set_voice_cutoff_hz](class_audioeffectchorus.md#class-audioeffectchorus-method-set-voice-cutoff-hz)(voice_idx: [int](class_int.md#class-int), cutoff_hz: [float](class_float.md#class-float)) |
| void | [set_voice_delay_ms](class_audioeffectchorus.md#class-audioeffectchorus-method-set-voice-delay-ms)(voice_idx: [int](class_int.md#class-int), delay_ms: [float](class_float.md#class-float)) |
| void | [set_voice_depth_ms](class_audioeffectchorus.md#class-audioeffectchorus-method-set-voice-depth-ms)(voice_idx: [int](class_int.md#class-int), depth_ms: [float](class_float.md#class-float)) |
| void | [set_voice_level_db](class_audioeffectchorus.md#class-audioeffectchorus-method-set-voice-level-db)(voice_idx: [int](class_int.md#class-int), level_db: [float](class_float.md#class-float)) |
| void | [set_voice_pan](class_audioeffectchorus.md#class-audioeffectchorus-method-set-voice-pan)(voice_idx: [int](class_int.md#class-int), pan: [float](class_float.md#class-float)) |
| void | [set_voice_rate_hz](class_audioeffectchorus.md#class-audioeffectchorus-method-set-voice-rate-hz)(voice_idx: [int](class_int.md#class-int), rate_hz: [float](class_float.md#class-float)) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-audioeffectchorus-property-dry"></a>

[float](class_float.md#class-float) **dry** = `1.0` [🔗](class_audioeffectchorus.md#class-audioeffectchorus-property-dry)

- void **set_dry**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_dry**()

The volume ratio of the original audio. Value can range from 0 to 1.

---


<a id="class-audioeffectchorus-property-voice-1-cutoff-hz"></a>

[float](class_float.md#class-float) **voice/1/cutoff_hz** = `8000.0` [🔗](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-1-cutoff-hz)

- void **set_voice_cutoff_hz**(voice_idx: [int](class_int.md#class-int), cutoff_hz: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_cutoff_hz**(voice_idx: [int](class_int.md#class-int)) const

The frequency threshold of the voice's low-pass filter in Hz.

---


<a id="class-audioeffectchorus-property-voice-1-delay-ms"></a>

[float](class_float.md#class-float) **voice/1/delay_ms** = `15.0` [🔗](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-1-delay-ms)

- void **set_voice_delay_ms**(voice_idx: [int](class_int.md#class-int), delay_ms: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_delay_ms**(voice_idx: [int](class_int.md#class-int)) const

The delay of the voice in milliseconds, compared to the original audio.

---


<a id="class-audioeffectchorus-property-voice-1-depth-ms"></a>

[float](class_float.md#class-float) **voice/1/depth_ms** = `2.0` [🔗](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-1-depth-ms)

- void **set_voice_depth_ms**(voice_idx: [int](class_int.md#class-int), depth_ms: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_depth_ms**(voice_idx: [int](class_int.md#class-int)) const

The depth of the voice's low-frequency oscillator in milliseconds.

---


<a id="class-audioeffectchorus-property-voice-1-level-db"></a>

[float](class_float.md#class-float) **voice/1/level_db** = `0.0` [🔗](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-1-level-db)

- void **set_voice_level_db**(voice_idx: [int](class_int.md#class-int), level_db: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_level_db**(voice_idx: [int](class_int.md#class-int)) const

The gain of the voice in dB.

---


<a id="class-audioeffectchorus-property-voice-1-pan"></a>

[float](class_float.md#class-float) **voice/1/pan** = `-0.5` [🔗](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-1-pan)

- void **set_voice_pan**(voice_idx: [int](class_int.md#class-int), pan: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_pan**(voice_idx: [int](class_int.md#class-int)) const

The pan position of the voice.

---


<a id="class-audioeffectchorus-property-voice-1-rate-hz"></a>

[float](class_float.md#class-float) **voice/1/rate_hz** = `0.8` [🔗](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-1-rate-hz)

- void **set_voice_rate_hz**(voice_idx: [int](class_int.md#class-int), rate_hz: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_rate_hz**(voice_idx: [int](class_int.md#class-int)) const

The rate of the voice's low-frequency oscillator in Hz.

---


<a id="class-audioeffectchorus-property-voice-2-cutoff-hz"></a>

[float](class_float.md#class-float) **voice/2/cutoff_hz** = `8000.0` [🔗](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-2-cutoff-hz)

- void **set_voice_cutoff_hz**(voice_idx: [int](class_int.md#class-int), cutoff_hz: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_cutoff_hz**(voice_idx: [int](class_int.md#class-int)) const

The frequency threshold of the voice's low-pass filter in Hz.

---


<a id="class-audioeffectchorus-property-voice-2-delay-ms"></a>

[float](class_float.md#class-float) **voice/2/delay_ms** = `20.0` [🔗](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-2-delay-ms)

- void **set_voice_delay_ms**(voice_idx: [int](class_int.md#class-int), delay_ms: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_delay_ms**(voice_idx: [int](class_int.md#class-int)) const

The delay of the voice in milliseconds, compared to the original audio.

---


<a id="class-audioeffectchorus-property-voice-2-depth-ms"></a>

[float](class_float.md#class-float) **voice/2/depth_ms** = `3.0` [🔗](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-2-depth-ms)

- void **set_voice_depth_ms**(voice_idx: [int](class_int.md#class-int), depth_ms: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_depth_ms**(voice_idx: [int](class_int.md#class-int)) const

The depth of the voice's low-frequency oscillator in milliseconds.

---


<a id="class-audioeffectchorus-property-voice-2-level-db"></a>

[float](class_float.md#class-float) **voice/2/level_db** = `0.0` [🔗](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-2-level-db)

- void **set_voice_level_db**(voice_idx: [int](class_int.md#class-int), level_db: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_level_db**(voice_idx: [int](class_int.md#class-int)) const

The gain of the voice in dB.

---


<a id="class-audioeffectchorus-property-voice-2-pan"></a>

[float](class_float.md#class-float) **voice/2/pan** = `0.5` [🔗](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-2-pan)

- void **set_voice_pan**(voice_idx: [int](class_int.md#class-int), pan: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_pan**(voice_idx: [int](class_int.md#class-int)) const

The pan position of the voice.

---


<a id="class-audioeffectchorus-property-voice-2-rate-hz"></a>

[float](class_float.md#class-float) **voice/2/rate_hz** = `1.2` [🔗](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-2-rate-hz)

- void **set_voice_rate_hz**(voice_idx: [int](class_int.md#class-int), rate_hz: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_rate_hz**(voice_idx: [int](class_int.md#class-int)) const

The rate of the voice's low-frequency oscillator in Hz.

---


<a id="class-audioeffectchorus-property-voice-3-cutoff-hz"></a>

[float](class_float.md#class-float) **voice/3/cutoff_hz** [🔗](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-3-cutoff-hz)

- void **set_voice_cutoff_hz**(voice_idx: [int](class_int.md#class-int), cutoff_hz: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_cutoff_hz**(voice_idx: [int](class_int.md#class-int)) const

The frequency threshold of the voice's low-pass filter in Hz.

---


<a id="class-audioeffectchorus-property-voice-3-delay-ms"></a>

[float](class_float.md#class-float) **voice/3/delay_ms** [🔗](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-3-delay-ms)

- void **set_voice_delay_ms**(voice_idx: [int](class_int.md#class-int), delay_ms: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_delay_ms**(voice_idx: [int](class_int.md#class-int)) const

The delay of the voice in milliseconds, compared to the original audio.

---


<a id="class-audioeffectchorus-property-voice-3-depth-ms"></a>

[float](class_float.md#class-float) **voice/3/depth_ms** [🔗](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-3-depth-ms)

- void **set_voice_depth_ms**(voice_idx: [int](class_int.md#class-int), depth_ms: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_depth_ms**(voice_idx: [int](class_int.md#class-int)) const

The depth of the voice's low-frequency oscillator in milliseconds.

---


<a id="class-audioeffectchorus-property-voice-3-level-db"></a>

[float](class_float.md#class-float) **voice/3/level_db** [🔗](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-3-level-db)

- void **set_voice_level_db**(voice_idx: [int](class_int.md#class-int), level_db: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_level_db**(voice_idx: [int](class_int.md#class-int)) const

The gain of the voice in dB.

---


<a id="class-audioeffectchorus-property-voice-3-pan"></a>

[float](class_float.md#class-float) **voice/3/pan** [🔗](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-3-pan)

- void **set_voice_pan**(voice_idx: [int](class_int.md#class-int), pan: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_pan**(voice_idx: [int](class_int.md#class-int)) const

The pan position of the voice.

---


<a id="class-audioeffectchorus-property-voice-3-rate-hz"></a>

[float](class_float.md#class-float) **voice/3/rate_hz** [🔗](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-3-rate-hz)

- void **set_voice_rate_hz**(voice_idx: [int](class_int.md#class-int), rate_hz: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_rate_hz**(voice_idx: [int](class_int.md#class-int)) const

The rate of the voice's low-frequency oscillator in Hz.

---


<a id="class-audioeffectchorus-property-voice-4-cutoff-hz"></a>

[float](class_float.md#class-float) **voice/4/cutoff_hz** [🔗](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-4-cutoff-hz)

- void **set_voice_cutoff_hz**(voice_idx: [int](class_int.md#class-int), cutoff_hz: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_cutoff_hz**(voice_idx: [int](class_int.md#class-int)) const

The frequency threshold of the voice's low-pass filter in Hz.

---


<a id="class-audioeffectchorus-property-voice-4-delay-ms"></a>

[float](class_float.md#class-float) **voice/4/delay_ms** [🔗](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-4-delay-ms)

- void **set_voice_delay_ms**(voice_idx: [int](class_int.md#class-int), delay_ms: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_delay_ms**(voice_idx: [int](class_int.md#class-int)) const

The delay of the voice in milliseconds, compared to the original audio.

---


<a id="class-audioeffectchorus-property-voice-4-depth-ms"></a>

[float](class_float.md#class-float) **voice/4/depth_ms** [🔗](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-4-depth-ms)

- void **set_voice_depth_ms**(voice_idx: [int](class_int.md#class-int), depth_ms: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_depth_ms**(voice_idx: [int](class_int.md#class-int)) const

The depth of the voice's low-frequency oscillator in milliseconds.

---


<a id="class-audioeffectchorus-property-voice-4-level-db"></a>

[float](class_float.md#class-float) **voice/4/level_db** [🔗](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-4-level-db)

- void **set_voice_level_db**(voice_idx: [int](class_int.md#class-int), level_db: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_level_db**(voice_idx: [int](class_int.md#class-int)) const

The gain of the voice in dB.

---


<a id="class-audioeffectchorus-property-voice-4-pan"></a>

[float](class_float.md#class-float) **voice/4/pan** [🔗](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-4-pan)

- void **set_voice_pan**(voice_idx: [int](class_int.md#class-int), pan: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_pan**(voice_idx: [int](class_int.md#class-int)) const

The pan position of the voice.

---


<a id="class-audioeffectchorus-property-voice-4-rate-hz"></a>

[float](class_float.md#class-float) **voice/4/rate_hz** [🔗](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-4-rate-hz)

- void **set_voice_rate_hz**(voice_idx: [int](class_int.md#class-int), rate_hz: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_rate_hz**(voice_idx: [int](class_int.md#class-int)) const

The rate of the voice's low-frequency oscillator in Hz.

---


<a id="class-audioeffectchorus-property-voice-count"></a>

[int](class_int.md#class-int) **voice_count** = `2` [🔗](class_audioeffectchorus.md#class-audioeffectchorus-property-voice-count)

- void **set_voice_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_voice_count**()

The number of voices in the effect. Value can range from 1 to 4.

---


<a id="class-audioeffectchorus-property-wet"></a>

[float](class_float.md#class-float) **wet** = `0.5` [🔗](class_audioeffectchorus.md#class-audioeffectchorus-property-wet)

- void **set_wet**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_wet**()

The volume ratio of all voices. Value can range from 0 to 1.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-audioeffectchorus-method-get-voice-cutoff-hz"></a>

[float](class_float.md#class-float) **get_voice_cutoff_hz**(voice_idx: [int](class_int.md#class-int)) const [🔗](class_audioeffectchorus.md#class-audioeffectchorus-method-get-voice-cutoff-hz)

Returns the frequency threshold of a given `voice_idx`'s low-pass filter in Hz. Frequencies above this value are removed from the voice.

---


<a id="class-audioeffectchorus-method-get-voice-delay-ms"></a>

[float](class_float.md#class-float) **get_voice_delay_ms**(voice_idx: [int](class_int.md#class-int)) const [🔗](class_audioeffectchorus.md#class-audioeffectchorus-method-get-voice-delay-ms)

Returns the delay of a given `voice_idx` in milliseconds, compared to the original audio.

---


<a id="class-audioeffectchorus-method-get-voice-depth-ms"></a>

[float](class_float.md#class-float) **get_voice_depth_ms**(voice_idx: [int](class_int.md#class-int)) const [🔗](class_audioeffectchorus.md#class-audioeffectchorus-method-get-voice-depth-ms)

Returns the depth of a given `voice_idx`'s low-frequency oscillator in milliseconds.

---


<a id="class-audioeffectchorus-method-get-voice-level-db"></a>

[float](class_float.md#class-float) **get_voice_level_db**(voice_idx: [int](class_int.md#class-int)) const [🔗](class_audioeffectchorus.md#class-audioeffectchorus-method-get-voice-level-db)

Returns the gain of a given `voice_idx` in dB.

---


<a id="class-audioeffectchorus-method-get-voice-pan"></a>

[float](class_float.md#class-float) **get_voice_pan**(voice_idx: [int](class_int.md#class-int)) const [🔗](class_audioeffectchorus.md#class-audioeffectchorus-method-get-voice-pan)

Returns the pan position of a given `voice_idx`. Negative values mean the left channel, positive mean the right.

---


<a id="class-audioeffectchorus-method-get-voice-rate-hz"></a>

[float](class_float.md#class-float) **get_voice_rate_hz**(voice_idx: [int](class_int.md#class-int)) const [🔗](class_audioeffectchorus.md#class-audioeffectchorus-method-get-voice-rate-hz)

Returns the rate of a given `voice_idx`'s low-frequency oscillator in Hz.

---


<a id="class-audioeffectchorus-method-set-voice-cutoff-hz"></a>

void **set_voice_cutoff_hz**(voice_idx: [int](class_int.md#class-int), cutoff_hz: [float](class_float.md#class-float)) [🔗](class_audioeffectchorus.md#class-audioeffectchorus-method-set-voice-cutoff-hz)

Sets the frequency threshold of a given `voice_idx`'s low-pass filter in Hz. Frequencies above `cutoff_hz` are removed from `voice_idx`. Value can range from 1 to 20500.

---


<a id="class-audioeffectchorus-method-set-voice-delay-ms"></a>

void **set_voice_delay_ms**(voice_idx: [int](class_int.md#class-int), delay_ms: [float](class_float.md#class-float)) [🔗](class_audioeffectchorus.md#class-audioeffectchorus-method-set-voice-delay-ms)

Sets the delay of a given `voice_idx` in milliseconds, compared to the original audio. Value can range from 0 to 50.

---


<a id="class-audioeffectchorus-method-set-voice-depth-ms"></a>

void **set_voice_depth_ms**(voice_idx: [int](class_int.md#class-int), depth_ms: [float](class_float.md#class-float)) [🔗](class_audioeffectchorus.md#class-audioeffectchorus-method-set-voice-depth-ms)

Sets the depth of a given `voice_idx`'s low-frequency oscillator in milliseconds. Value can range from 0 to 20.

---


<a id="class-audioeffectchorus-method-set-voice-level-db"></a>

void **set_voice_level_db**(voice_idx: [int](class_int.md#class-int), level_db: [float](class_float.md#class-float)) [🔗](class_audioeffectchorus.md#class-audioeffectchorus-method-set-voice-level-db)

Sets the gain of a given `voice_idx` in dB. Value can range from -60 to 24.

---


<a id="class-audioeffectchorus-method-set-voice-pan"></a>

void **set_voice_pan**(voice_idx: [int](class_int.md#class-int), pan: [float](class_float.md#class-float)) [🔗](class_audioeffectchorus.md#class-audioeffectchorus-method-set-voice-pan)

Sets the pan position of a given `voice_idx`. Negative values pan the sound to the left, positive pan to the right. Value can range from -1 to 1.

---


<a id="class-audioeffectchorus-method-set-voice-rate-hz"></a>

void **set_voice_rate_hz**(voice_idx: [int](class_int.md#class-int), rate_hz: [float](class_float.md#class-float)) [🔗](class_audioeffectchorus.md#class-audioeffectchorus-method-set-voice-rate-hz)

Sets the rate of a given `voice_idx`'s low-frequency oscillator in Hz. Value can range from 0.1 to 20.
