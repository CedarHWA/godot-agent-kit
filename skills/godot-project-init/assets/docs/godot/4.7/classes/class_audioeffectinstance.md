> Source: https://docs.godotengine.org/en/4.7/classes/class_audioeffectinstance.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="audioeffectinstance"></a>

<a id="class-audioeffectinstance"></a>

# AudioEffectInstance

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [AudioEffectSpectrumAnalyzerInstance](class_audioeffectspectrumanalyzerinstance.md#class-audioeffectspectrumanalyzerinstance)

Manipulates the audio it receives for a given effect.

<a id="description"></a>

## Description

An audio effect instance manipulates the audio it receives for a given effect. This instance is automatically created by an [AudioEffect](class_audioeffect.md#class-audioeffect) when it is added to a bus, and should usually not be created directly. If necessary, it can be fetched at run-time with [AudioServer.get_bus_effect_instance()](class_audioserver.md#class-audioserver-method-get-bus-effect-instance).

<a id="tutorials"></a>

## Tutorials

- [Audio buses](../tutorials/audio/audio_buses.md)
- [Audio effects](../tutorials/audio/audio_effects.md)

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [_process](class_audioeffectinstance.md#class-audioeffectinstance-private-method-process)(src_buffer: `const void*`, r_dst_buffer: `AudioFrame*`, frame_count: [int](class_int.md#class-int)) virtual required |
| [bool](class_bool.md#class-bool) | [_process_silence](class_audioeffectinstance.md#class-audioeffectinstance-private-method-process-silence)() virtual const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-audioeffectinstance-private-method-process"></a>

void **_process**(src_buffer: `const void*`, r_dst_buffer: `AudioFrame*`, frame_count: [int](class_int.md#class-int)) virtual required [🔗](class_audioeffectinstance.md#class-audioeffectinstance-private-method-process)

Called by the [AudioServer](class_audioserver.md#class-audioserver) to process this effect. When [_process_silence()](class_audioeffectinstance.md#class-audioeffectinstance-private-method-process-silence) is not overridden or it returns `false`, this method is called only when the bus is active.

**Note:** It is not useful to override this method in GDScript or C#. Only GDExtension can take advantage of it.

---


<a id="class-audioeffectinstance-private-method-process-silence"></a>

[bool](class_bool.md#class-bool) **_process_silence**() virtual const [🔗](class_audioeffectinstance.md#class-audioeffectinstance-private-method-process-silence)

Override this method to customize the processing behavior of this effect instance.

Should return `true` to force the [AudioServer](class_audioserver.md#class-audioserver) to always call [_process()](class_audioeffectinstance.md#class-audioeffectinstance-private-method-process), even if the bus has been muted or cannot otherwise be heard.
