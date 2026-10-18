> Source: https://docs.godotengine.org/en/4.7/classes/class_audiostreamplaybackresampled.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="audiostreamplaybackresampled"></a>

<a id="class-audiostreamplaybackresampled"></a>

# AudioStreamPlaybackResampled

**Inherits:** [AudioStreamPlayback](class_audiostreamplayback.md#class-audiostreamplayback) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [AudioStreamGeneratorPlayback](class_audiostreamgeneratorplayback.md#class-audiostreamgeneratorplayback), [AudioStreamPlaybackOggVorbis](class_audiostreamplaybackoggvorbis.md#class-audiostreamplaybackoggvorbis)

Playback class used for resampled [AudioStream](class_audiostream.md#class-audiostream)s.

<a id="description"></a>

## Description

Playback class used to mix an [AudioStream](class_audiostream.md#class-audiostream)'s audio samples to [AudioServer.get_mix_rate()](class_audioserver.md#class-audioserver-method-get-mix-rate) using cubic interpolation.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [float](class_float.md#class-float) | [_get_stream_sampling_rate](class_audiostreamplaybackresampled.md#class-audiostreamplaybackresampled-private-method-get-stream-sampling-rate)() virtual required const |
| [int](class_int.md#class-int) | [_mix_resampled](class_audiostreamplaybackresampled.md#class-audiostreamplaybackresampled-private-method-mix-resampled)(dst_buffer: `AudioFrame*`, frame_count: [int](class_int.md#class-int)) virtual required |
| void | [begin_resample](class_audiostreamplaybackresampled.md#class-audiostreamplaybackresampled-method-begin-resample)() |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-audiostreamplaybackresampled-private-method-get-stream-sampling-rate"></a>

[float](class_float.md#class-float) **_get_stream_sampling_rate**() virtual required const [🔗](class_audiostreamplaybackresampled.md#class-audiostreamplaybackresampled-private-method-get-stream-sampling-rate)

Returns an [AudioStream](class_audiostream.md#class-audiostream)'s sample rate, in Hz. Used to perform resampling.

---


<a id="class-audiostreamplaybackresampled-private-method-mix-resampled"></a>

[int](class_int.md#class-int) **_mix_resampled**(dst_buffer: `AudioFrame*`, frame_count: [int](class_int.md#class-int)) virtual required [🔗](class_audiostreamplaybackresampled.md#class-audiostreamplaybackresampled-private-method-mix-resampled)

Called by [begin_resample()](class_audiostreamplaybackresampled.md#class-audiostreamplaybackresampled-method-begin-resample) to mix an [AudioStream](class_audiostream.md#class-audiostream) to [AudioServer.get_mix_rate()](class_audioserver.md#class-audioserver-method-get-mix-rate). Uses [_get_stream_sampling_rate()](class_audiostreamplaybackresampled.md#class-audiostreamplaybackresampled-private-method-get-stream-sampling-rate) as the source sample rate. Returns the number of mixed frames.

---


<a id="class-audiostreamplaybackresampled-method-begin-resample"></a>

void **begin_resample**() [🔗](class_audiostreamplaybackresampled.md#class-audiostreamplaybackresampled-method-begin-resample)

Called when an [AudioStream](class_audiostream.md#class-audiostream) is played. Clears the cubic interpolation history and starts mixing by calling [_mix_resampled()](class_audiostreamplaybackresampled.md#class-audiostreamplaybackresampled-private-method-mix-resampled).
