> Source: https://docs.godotengine.org/en/4.7/classes/class_audioeffecteq.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="audioeffecteq"></a>

<a id="class-audioeffecteq"></a>

# AudioEffectEQ

**Inherits:** [AudioEffect](class_audioeffect.md#class-audioeffect) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [AudioEffectEQ10](class_audioeffecteq10.md#class-audioeffecteq10), [AudioEffectEQ21](class_audioeffecteq21.md#class-audioeffecteq21), [AudioEffectEQ6](class_audioeffecteq6.md#class-audioeffecteq6)

Base class for audio equalizers (EQ). Gives you control over frequencies.

Use it to create a custom equalizer if [AudioEffectEQ6](class_audioeffecteq6.md#class-audioeffecteq6), [AudioEffectEQ10](class_audioeffecteq10.md#class-audioeffecteq10), or [AudioEffectEQ21](class_audioeffecteq21.md#class-audioeffecteq21) don't fit your needs.

<a id="description"></a>

## Description

An "equalizer" gives you control over the gain of frequencies in the entire spectrum, by allowing their adjustment through bands. A band is a point in the frequency spectrum, and each band means a division of the spectrum that can be adjusted.

Use equalizers to compensate for existing deficiencies in the audio, make room for other elements, or remove undesirable frequencies. AudioEffectEQs are useful on the Master bus to balance the entire mix or give it more character. They are also useful when a game is run on a mobile device, to adjust the mix to that kind of speakers (it can be disabled when headphones are plugged in).

<a id="tutorials"></a>

## Tutorials

- [Audio buses](../tutorials/audio/audio_buses.md)
- [Audio effects](../tutorials/audio/audio_effects.md)

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [int](class_int.md#class-int) | [get_band_count](class_audioeffecteq.md#class-audioeffecteq-method-get-band-count)() const |
| [float](class_float.md#class-float) | [get_band_gain_db](class_audioeffecteq.md#class-audioeffecteq-method-get-band-gain-db)(band_idx: [int](class_int.md#class-int)) const |
| void | [set_band_gain_db](class_audioeffecteq.md#class-audioeffecteq-method-set-band-gain-db)(band_idx: [int](class_int.md#class-int), volume_db: [float](class_float.md#class-float)) |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-audioeffecteq-method-get-band-count"></a>

[int](class_int.md#class-int) **get_band_count**() const [🔗](class_audioeffecteq.md#class-audioeffecteq-method-get-band-count)

Returns the number of bands of the equalizer.

---


<a id="class-audioeffecteq-method-get-band-gain-db"></a>

[float](class_float.md#class-float) **get_band_gain_db**(band_idx: [int](class_int.md#class-int)) const [🔗](class_audioeffecteq.md#class-audioeffecteq-method-get-band-gain-db)

Returns the band's gain at the specified index, in dB.

---


<a id="class-audioeffecteq-method-set-band-gain-db"></a>

void **set_band_gain_db**(band_idx: [int](class_int.md#class-int), volume_db: [float](class_float.md#class-float)) [🔗](class_audioeffecteq.md#class-audioeffecteq-method-set-band-gain-db)

Sets band's gain at the specified index, in dB.
