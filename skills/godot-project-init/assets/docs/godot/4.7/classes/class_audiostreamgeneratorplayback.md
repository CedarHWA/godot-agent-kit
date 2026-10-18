> Source: https://docs.godotengine.org/en/4.7/classes/class_audiostreamgeneratorplayback.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="audiostreamgeneratorplayback"></a>

<a id="class-audiostreamgeneratorplayback"></a>

# AudioStreamGeneratorPlayback

**Inherits:** [AudioStreamPlaybackResampled](class_audiostreamplaybackresampled.md#class-audiostreamplaybackresampled) **<** [AudioStreamPlayback](class_audiostreamplayback.md#class-audiostreamplayback) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Plays back audio generated using [AudioStreamGenerator](class_audiostreamgenerator.md#class-audiostreamgenerator).

<a id="description"></a>

## Description

This class is meant to be used with [AudioStreamGenerator](class_audiostreamgenerator.md#class-audiostreamgenerator) to play back the generated audio in real-time.

<a id="tutorials"></a>

## Tutorials

- [Audio Generator Demo](https://godotengine.org/asset-library/asset/2759)
- [Godot 3.2 will get new audio features](https://godotengine.org/article/godot-32-will-get-new-audio-features)

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [can_push_buffer](class_audiostreamgeneratorplayback.md#class-audiostreamgeneratorplayback-method-can-push-buffer)(amount: [int](class_int.md#class-int)) const |
| void | [clear_buffer](class_audiostreamgeneratorplayback.md#class-audiostreamgeneratorplayback-method-clear-buffer)() |
| [int](class_int.md#class-int) | [get_frames_available](class_audiostreamgeneratorplayback.md#class-audiostreamgeneratorplayback-method-get-frames-available)() const |
| [int](class_int.md#class-int) | [get_skips](class_audiostreamgeneratorplayback.md#class-audiostreamgeneratorplayback-method-get-skips)() const |
| [bool](class_bool.md#class-bool) | [push_buffer](class_audiostreamgeneratorplayback.md#class-audiostreamgeneratorplayback-method-push-buffer)(frames: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array)) |
| [bool](class_bool.md#class-bool) | [push_frame](class_audiostreamgeneratorplayback.md#class-audiostreamgeneratorplayback-method-push-frame)(frame: [Vector2](class_vector2.md#class-vector2)) |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-audiostreamgeneratorplayback-method-can-push-buffer"></a>

[bool](class_bool.md#class-bool) **can_push_buffer**(amount: [int](class_int.md#class-int)) const [🔗](class_audiostreamgeneratorplayback.md#class-audiostreamgeneratorplayback-method-can-push-buffer)

Returns `true` if a buffer of the size `amount` can be pushed to the audio sample data buffer without overflowing it, `false` otherwise.

---


<a id="class-audiostreamgeneratorplayback-method-clear-buffer"></a>

void **clear_buffer**() [🔗](class_audiostreamgeneratorplayback.md#class-audiostreamgeneratorplayback-method-clear-buffer)

Clears the audio sample data buffer.

---


<a id="class-audiostreamgeneratorplayback-method-get-frames-available"></a>

[int](class_int.md#class-int) **get_frames_available**() const [🔗](class_audiostreamgeneratorplayback.md#class-audiostreamgeneratorplayback-method-get-frames-available)

Returns the number of frames that can be pushed to the audio sample data buffer without overflowing it. If the result is `0`, the buffer is full.

---


<a id="class-audiostreamgeneratorplayback-method-get-skips"></a>

[int](class_int.md#class-int) **get_skips**() const [🔗](class_audiostreamgeneratorplayback.md#class-audiostreamgeneratorplayback-method-get-skips)

Returns the number of times the playback skipped due to a buffer underrun in the audio sample data. This value is reset at the start of the playback.

---


<a id="class-audiostreamgeneratorplayback-method-push-buffer"></a>

[bool](class_bool.md#class-bool) **push_buffer**(frames: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array)) [🔗](class_audiostreamgeneratorplayback.md#class-audiostreamgeneratorplayback-method-push-buffer)

Pushes several audio data frames to the buffer. This is usually more efficient than [push_frame()](class_audiostreamgeneratorplayback.md#class-audiostreamgeneratorplayback-method-push-frame) in C# and compiled languages via GDExtension, but [push_buffer()](class_audiostreamgeneratorplayback.md#class-audiostreamgeneratorplayback-method-push-buffer) may be *less* efficient in GDScript.

---


<a id="class-audiostreamgeneratorplayback-method-push-frame"></a>

[bool](class_bool.md#class-bool) **push_frame**(frame: [Vector2](class_vector2.md#class-vector2)) [🔗](class_audiostreamgeneratorplayback.md#class-audiostreamgeneratorplayback-method-push-frame)

Pushes a single audio data frame to the buffer. This is usually less efficient than [push_buffer()](class_audiostreamgeneratorplayback.md#class-audiostreamgeneratorplayback-method-push-buffer) in C# and compiled languages via GDExtension, but [push_frame()](class_audiostreamgeneratorplayback.md#class-audiostreamgeneratorplayback-method-push-frame) may be *more* efficient in GDScript.
