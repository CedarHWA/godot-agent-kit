> Source: https://docs.godotengine.org/en/4.7/classes/class_audiostreamplaybackinteractive.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="audiostreamplaybackinteractive"></a>

<a id="class-audiostreamplaybackinteractive"></a>

# AudioStreamPlaybackInteractive

**Inherits:** [AudioStreamPlayback](class_audiostreamplayback.md#class-audiostreamplayback) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Playback component of [AudioStreamInteractive](class_audiostreaminteractive.md#class-audiostreaminteractive).

<a id="description"></a>

## Description

Playback component of [AudioStreamInteractive](class_audiostreaminteractive.md#class-audiostreaminteractive). Contains functions to change the currently played clip.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [int](class_int.md#class-int) | [get_current_clip_index](class_audiostreamplaybackinteractive.md#class-audiostreamplaybackinteractive-method-get-current-clip-index)() const |
| void | [switch_to_clip](class_audiostreamplaybackinteractive.md#class-audiostreamplaybackinteractive-method-switch-to-clip)(clip_index: [int](class_int.md#class-int)) |
| void | [switch_to_clip_by_name](class_audiostreamplaybackinteractive.md#class-audiostreamplaybackinteractive-method-switch-to-clip-by-name)(clip_name: [StringName](class_stringname.md#class-stringname)) |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-audiostreamplaybackinteractive-method-get-current-clip-index"></a>

[int](class_int.md#class-int) **get_current_clip_index**() const [🔗](class_audiostreamplaybackinteractive.md#class-audiostreamplaybackinteractive-method-get-current-clip-index)

Return the index of the currently playing clip. You can use this to get the name of the currently playing clip with [AudioStreamInteractive.get_clip_name()](class_audiostreaminteractive.md#class-audiostreaminteractive-method-get-clip-name).

**Example:** Get the currently playing clip name from inside an [AudioStreamPlayer](class_audiostreamplayer.md#class-audiostreamplayer) node.

```gdscript
var playing_clip_name = stream.get_clip_name(get_stream_playback().get_current_clip_index())
```

---


<a id="class-audiostreamplaybackinteractive-method-switch-to-clip"></a>

void **switch_to_clip**(clip_index: [int](class_int.md#class-int)) [🔗](class_audiostreamplaybackinteractive.md#class-audiostreamplaybackinteractive-method-switch-to-clip)

Switch to a clip (by index).

---


<a id="class-audiostreamplaybackinteractive-method-switch-to-clip-by-name"></a>

void **switch_to_clip_by_name**(clip_name: [StringName](class_stringname.md#class-stringname)) [🔗](class_audiostreamplaybackinteractive.md#class-audiostreamplaybackinteractive-method-switch-to-clip-by-name)

Switch to a clip (by name).
