> Source: https://docs.godotengine.org/en/4.7/classes/class_audioeffectamplify.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="audioeffectamplify"></a>

<a id="class-audioeffectamplify"></a>

# AudioEffectAmplify

**Inherits:** [AudioEffect](class_audioeffect.md#class-audioeffect) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Adds a volume manipulation audio effect to an audio bus.

<a id="description"></a>

## Description

Increases or decreases the volume being routed through the audio bus.

<a id="tutorials"></a>

## Tutorials

- [Audio buses](../tutorials/audio/audio_buses.md)
- [Audio effects](../tutorials/audio/audio_effects.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [volume_db](class_audioeffectamplify.md#class-audioeffectamplify-property-volume-db) | `0.0` |
| [float](class_float.md#class-float) | [volume_linear](class_audioeffectamplify.md#class-audioeffectamplify-property-volume-linear) |  |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-audioeffectamplify-property-volume-db"></a>

[float](class_float.md#class-float) **volume_db** = `0.0` [🔗](class_audioeffectamplify.md#class-audioeffectamplify-property-volume-db)

- void **set_volume_db**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_volume_db**()

Amount of amplification in dB. Positive values make the sound louder, negative values make it quieter. Value can range from -80 to 24.

---


<a id="class-audioeffectamplify-property-volume-linear"></a>

[float](class_float.md#class-float) **volume_linear** [🔗](class_audioeffectamplify.md#class-audioeffectamplify-property-volume-linear)

- void **set_volume_linear**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_volume_linear**()

Amount of amplification as a linear value.

**Note:** This member modifies [volume_db](class_audioeffectamplify.md#class-audioeffectamplify-property-volume-db) for convenience. The returned value is equivalent to the result of [@GlobalScope.db_to_linear()](class_@globalscope.md#class-globalscope-method-db-to-linear) on [volume_db](class_audioeffectamplify.md#class-audioeffectamplify-property-volume-db). Setting this member is equivalent to setting [volume_db](class_audioeffectamplify.md#class-audioeffectamplify-property-volume-db) to the result of [@GlobalScope.linear_to_db()](class_@globalscope.md#class-globalscope-method-linear-to-db) on a value.
