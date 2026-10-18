> Source: https://docs.godotengine.org/en/4.7/classes/class_audioeffectpanner.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="audioeffectpanner"></a>

<a id="class-audioeffectpanner"></a>

# AudioEffectPanner

**Inherits:** [AudioEffect](class_audioeffect.md#class-audioeffect) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Adds a panner audio effect to an audio bus.

Pans the sound left or right.

<a id="description"></a>

## Description

Determines how much of the audio signal is sent to the left and right channels. This helps with audio spatialization, giving sounds distinct places in a mix.

[AudioStreamPlayer2D](class_audiostreamplayer2d.md#class-audiostreamplayer2d) and [AudioStreamPlayer3D](class_audiostreamplayer3d.md#class-audiostreamplayer3d) handle panning automatically, following where the source of the sound is on the screen.

<a id="tutorials"></a>

## Tutorials

- [Audio buses](../tutorials/audio/audio_buses.md)
- [Audio effects](../tutorials/audio/audio_effects.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [pan](class_audioeffectpanner.md#class-audioeffectpanner-property-pan) | `0.0` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-audioeffectpanner-property-pan"></a>

[float](class_float.md#class-float) **pan** = `0.0` [🔗](class_audioeffectpanner.md#class-audioeffectpanner-property-pan)

- void **set_pan**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_pan**()

Pan position. Negative values pan the sound to the left, positive pan to the right. Value can range from -1 to 1.
