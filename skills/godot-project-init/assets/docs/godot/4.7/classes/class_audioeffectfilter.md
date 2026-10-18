> Source: https://docs.godotengine.org/en/4.7/classes/class_audioeffectfilter.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="audioeffectfilter"></a>

<a id="class-audioeffectfilter"></a>

# AudioEffectFilter

**Inherits:** [AudioEffect](class_audioeffect.md#class-audioeffect) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [AudioEffectBandLimitFilter](class_audioeffectbandlimitfilter.md#class-audioeffectbandlimitfilter), [AudioEffectBandPassFilter](class_audioeffectbandpassfilter.md#class-audioeffectbandpassfilter), [AudioEffectHighPassFilter](class_audioeffecthighpassfilter.md#class-audioeffecthighpassfilter), [AudioEffectHighShelfFilter](class_audioeffecthighshelffilter.md#class-audioeffecthighshelffilter), [AudioEffectLowPassFilter](class_audioeffectlowpassfilter.md#class-audioeffectlowpassfilter), [AudioEffectLowShelfFilter](class_audioeffectlowshelffilter.md#class-audioeffectlowshelffilter), [AudioEffectNotchFilter](class_audioeffectnotchfilter.md#class-audioeffectnotchfilter)

Base class for filters. Use effects that inherit this class instead of using it directly.

<a id="description"></a>

## Description

A "filter" controls the gain of frequencies, using [cutoff_hz](class_audioeffectfilter.md#class-audioeffectfilter-property-cutoff-hz) as a frequency threshold. Filters can help to give room for each sound, and create interesting effects.

There are different types of filter that inherit this class:

Shelf filters: [AudioEffectLowShelfFilter](class_audioeffectlowshelffilter.md#class-audioeffectlowshelffilter) and [AudioEffectHighShelfFilter](class_audioeffecthighshelffilter.md#class-audioeffecthighshelffilter)

Band-pass and notch filters: [AudioEffectBandPassFilter](class_audioeffectbandpassfilter.md#class-audioeffectbandpassfilter), [AudioEffectBandLimitFilter](class_audioeffectbandlimitfilter.md#class-audioeffectbandlimitfilter), and [AudioEffectNotchFilter](class_audioeffectnotchfilter.md#class-audioeffectnotchfilter)

Low/high-pass filters: [AudioEffectLowPassFilter](class_audioeffectlowpassfilter.md#class-audioeffectlowpassfilter) and [AudioEffectHighPassFilter](class_audioeffecthighpassfilter.md#class-audioeffecthighpassfilter)

<a id="tutorials"></a>

## Tutorials

- [Audio buses](../tutorials/audio/audio_buses.md)
- [Audio effects](../tutorials/audio/audio_effects.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [cutoff_hz](class_audioeffectfilter.md#class-audioeffectfilter-property-cutoff-hz) | `2000.0` |
| [FilterDB](class_audioeffectfilter.md#enum-audioeffectfilter-filterdb) | [db](class_audioeffectfilter.md#class-audioeffectfilter-property-db) | `0` |
| [float](class_float.md#class-float) | [gain](class_audioeffectfilter.md#class-audioeffectfilter-property-gain) | `1.0` |
| [float](class_float.md#class-float) | [resonance](class_audioeffectfilter.md#class-audioeffectfilter-property-resonance) | `0.5` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-audioeffectfilter-filterdb"></a>

enum **FilterDB**: [🔗](class_audioeffectfilter.md#enum-audioeffectfilter-filterdb)

<a id="class-audioeffectfilter-constant-filter-6db"></a>

[FilterDB](class_audioeffectfilter.md#enum-audioeffectfilter-filterdb) **FILTER_6DB** = `0`

Cutting off at 6 dB per octave. One octave is twice the frequency above [cutoff_hz](class_audioeffectfilter.md#class-audioeffectfilter-property-cutoff-hz), or half the frequency below [cutoff_hz](class_audioeffectfilter.md#class-audioeffectfilter-property-cutoff-hz).

<a id="class-audioeffectfilter-constant-filter-12db"></a>

[FilterDB](class_audioeffectfilter.md#enum-audioeffectfilter-filterdb) **FILTER_12DB** = `1`

Cutting off at 12 dB per octave. One octave is twice the frequency above [cutoff_hz](class_audioeffectfilter.md#class-audioeffectfilter-property-cutoff-hz), or half the frequency below [cutoff_hz](class_audioeffectfilter.md#class-audioeffectfilter-property-cutoff-hz).

<a id="class-audioeffectfilter-constant-filter-18db"></a>

[FilterDB](class_audioeffectfilter.md#enum-audioeffectfilter-filterdb) **FILTER_18DB** = `2`

Cutting off at 18 dB per octave. One octave is twice the frequency above [cutoff_hz](class_audioeffectfilter.md#class-audioeffectfilter-property-cutoff-hz), or half the frequency below [cutoff_hz](class_audioeffectfilter.md#class-audioeffectfilter-property-cutoff-hz).

<a id="class-audioeffectfilter-constant-filter-24db"></a>

[FilterDB](class_audioeffectfilter.md#enum-audioeffectfilter-filterdb) **FILTER_24DB** = `3`

Cutting off at 24 dB per octave. One octave is twice the frequency above [cutoff_hz](class_audioeffectfilter.md#class-audioeffectfilter-property-cutoff-hz), or half the frequency below [cutoff_hz](class_audioeffectfilter.md#class-audioeffectfilter-property-cutoff-hz).

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-audioeffectfilter-property-cutoff-hz"></a>

[float](class_float.md#class-float) **cutoff_hz** = `2000.0` [🔗](class_audioeffectfilter.md#class-audioeffectfilter-property-cutoff-hz)

- void **set_cutoff**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_cutoff**()

Frequency threshold for the filter, in Hz. Value can range from 1 to 20500.

---


<a id="class-audioeffectfilter-property-db"></a>

[FilterDB](class_audioeffectfilter.md#enum-audioeffectfilter-filterdb) **db** = `0` [🔗](class_audioeffectfilter.md#class-audioeffectfilter-property-db)

- void **set_db**(value: [FilterDB](class_audioeffectfilter.md#enum-audioeffectfilter-filterdb))
- [FilterDB](class_audioeffectfilter.md#enum-audioeffectfilter-filterdb) **get_db**()

Steepness of the cutoff curve in dB per octave (twice the frequency above [cutoff_hz](class_audioeffectfilter.md#class-audioeffectfilter-property-cutoff-hz), or half the frequency below [cutoff_hz](class_audioeffectfilter.md#class-audioeffectfilter-property-cutoff-hz)), also known as the "order" of the filter. Higher orders have a more aggressive cutoff.

---


<a id="class-audioeffectfilter-property-gain"></a>

[float](class_float.md#class-float) **gain** = `1.0` [🔗](class_audioeffectfilter.md#class-audioeffectfilter-property-gain)

- void **set_gain**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_gain**()

Gain of the frequencies affected by the filter. This property is only available for [AudioEffectLowShelfFilter](class_audioeffectlowshelffilter.md#class-audioeffectlowshelffilter) and [AudioEffectHighShelfFilter](class_audioeffecthighshelffilter.md#class-audioeffecthighshelffilter). Value can range from 0 to 4.

---


<a id="class-audioeffectfilter-property-resonance"></a>

[float](class_float.md#class-float) **resonance** = `0.5` [🔗](class_audioeffectfilter.md#class-audioeffectfilter-property-resonance)

- void **set_resonance**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_resonance**()

Gain at or directly next to the [cutoff_hz](class_audioeffectfilter.md#class-audioeffectfilter-property-cutoff-hz) frequency threshold. Value can range from 0 to 1.

Its exact behavior depends on the selected filter type:

- For shelf filters, it accentuates or masks the order by increasing frequencies right next to the [cutoff_hz](class_audioeffectfilter.md#class-audioeffectfilter-property-cutoff-hz) frequency and decreasing frequencies on the opposite side.
- For the band-pass and notch filters, it widens or narrows the filter at the [cutoff_hz](class_audioeffectfilter.md#class-audioeffectfilter-property-cutoff-hz) frequency threshold.
- For low/high-pass filters, it increases or decreases frequencies at the [cutoff_hz](class_audioeffectfilter.md#class-audioeffectfilter-property-cutoff-hz) frequency threshold.
