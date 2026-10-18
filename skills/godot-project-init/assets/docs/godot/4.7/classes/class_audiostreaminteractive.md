> Source: https://docs.godotengine.org/en/4.7/classes/class_audiostreaminteractive.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="audiostreaminteractive"></a>

<a id="class-audiostreaminteractive"></a>

# AudioStreamInteractive

**Inherits:** [AudioStream](class_audiostream.md#class-audiostream) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Audio stream that can playback music interactively, combining clips and a transition table.

<a id="description"></a>

## Description

This is an audio stream that can playback music interactively, combining clips and a transition table. Clips must be added first, and then the transition rules via the [add_transition()](class_audiostreaminteractive.md#class-audiostreaminteractive-method-add-transition). Additionally, this stream exports a property parameter to control the playback via [AudioStreamPlayer](class_audiostreamplayer.md#class-audiostreamplayer), [AudioStreamPlayer2D](class_audiostreamplayer2d.md#class-audiostreamplayer2d), or [AudioStreamPlayer3D](class_audiostreamplayer3d.md#class-audiostreamplayer3d).

The way this is used is by filling a number of clips, then configuring the transition table. From there, clips are selected for playback and the music will smoothly go from the current to the new one while using the corresponding transition rule defined in the transition table.

<a id="tutorials"></a>

## Tutorials

- [Audio streams](../tutorials/audio/audio_streams.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [clip_count](class_audiostreaminteractive.md#class-audiostreaminteractive-property-clip-count) | `0` |
| [int](class_int.md#class-int) | [initial_clip](class_audiostreaminteractive.md#class-audiostreaminteractive-property-initial-clip) | `0` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_transition](class_audiostreaminteractive.md#class-audiostreaminteractive-method-add-transition)(from_clip: [int](class_int.md#class-int), to_clip: [int](class_int.md#class-int), from_time: [TransitionFromTime](class_audiostreaminteractive.md#enum-audiostreaminteractive-transitionfromtime), to_time: [TransitionToTime](class_audiostreaminteractive.md#enum-audiostreaminteractive-transitiontotime), fade_mode: [FadeMode](class_audiostreaminteractive.md#enum-audiostreaminteractive-fademode), fade_beats: [float](class_float.md#class-float), use_filler_clip: [bool](class_bool.md#class-bool) = false, filler_clip: [int](class_int.md#class-int) = -1, hold_previous: [bool](class_bool.md#class-bool) = false) |
| void | [erase_transition](class_audiostreaminteractive.md#class-audiostreaminteractive-method-erase-transition)(from_clip: [int](class_int.md#class-int), to_clip: [int](class_int.md#class-int)) |
| [AutoAdvanceMode](class_audiostreaminteractive.md#enum-audiostreaminteractive-autoadvancemode) | [get_clip_auto_advance](class_audiostreaminteractive.md#class-audiostreaminteractive-method-get-clip-auto-advance)(clip_index: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_clip_auto_advance_next_clip](class_audiostreaminteractive.md#class-audiostreaminteractive-method-get-clip-auto-advance-next-clip)(clip_index: [int](class_int.md#class-int)) const |
| [StringName](class_stringname.md#class-stringname) | [get_clip_name](class_audiostreaminteractive.md#class-audiostreaminteractive-method-get-clip-name)(clip_index: [int](class_int.md#class-int)) const |
| [AudioStream](class_audiostream.md#class-audiostream) | [get_clip_stream](class_audiostreaminteractive.md#class-audiostreaminteractive-method-get-clip-stream)(clip_index: [int](class_int.md#class-int)) const |
| [float](class_float.md#class-float) | [get_transition_fade_beats](class_audiostreaminteractive.md#class-audiostreaminteractive-method-get-transition-fade-beats)(from_clip: [int](class_int.md#class-int), to_clip: [int](class_int.md#class-int)) const |
| [FadeMode](class_audiostreaminteractive.md#enum-audiostreaminteractive-fademode) | [get_transition_fade_mode](class_audiostreaminteractive.md#class-audiostreaminteractive-method-get-transition-fade-mode)(from_clip: [int](class_int.md#class-int), to_clip: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_transition_filler_clip](class_audiostreaminteractive.md#class-audiostreaminteractive-method-get-transition-filler-clip)(from_clip: [int](class_int.md#class-int), to_clip: [int](class_int.md#class-int)) const |
| [TransitionFromTime](class_audiostreaminteractive.md#enum-audiostreaminteractive-transitionfromtime) | [get_transition_from_time](class_audiostreaminteractive.md#class-audiostreaminteractive-method-get-transition-from-time)(from_clip: [int](class_int.md#class-int), to_clip: [int](class_int.md#class-int)) const |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array) | [get_transition_list](class_audiostreaminteractive.md#class-audiostreaminteractive-method-get-transition-list)() const |
| [TransitionToTime](class_audiostreaminteractive.md#enum-audiostreaminteractive-transitiontotime) | [get_transition_to_time](class_audiostreaminteractive.md#class-audiostreaminteractive-method-get-transition-to-time)(from_clip: [int](class_int.md#class-int), to_clip: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [has_transition](class_audiostreaminteractive.md#class-audiostreaminteractive-method-has-transition)(from_clip: [int](class_int.md#class-int), to_clip: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [is_transition_holding_previous](class_audiostreaminteractive.md#class-audiostreaminteractive-method-is-transition-holding-previous)(from_clip: [int](class_int.md#class-int), to_clip: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [is_transition_using_filler_clip](class_audiostreaminteractive.md#class-audiostreaminteractive-method-is-transition-using-filler-clip)(from_clip: [int](class_int.md#class-int), to_clip: [int](class_int.md#class-int)) const |
| void | [set_clip_auto_advance](class_audiostreaminteractive.md#class-audiostreaminteractive-method-set-clip-auto-advance)(clip_index: [int](class_int.md#class-int), mode: [AutoAdvanceMode](class_audiostreaminteractive.md#enum-audiostreaminteractive-autoadvancemode)) |
| void | [set_clip_auto_advance_next_clip](class_audiostreaminteractive.md#class-audiostreaminteractive-method-set-clip-auto-advance-next-clip)(clip_index: [int](class_int.md#class-int), auto_advance_next_clip: [int](class_int.md#class-int)) |
| void | [set_clip_name](class_audiostreaminteractive.md#class-audiostreaminteractive-method-set-clip-name)(clip_index: [int](class_int.md#class-int), name: [StringName](class_stringname.md#class-stringname)) |
| void | [set_clip_stream](class_audiostreaminteractive.md#class-audiostreaminteractive-method-set-clip-stream)(clip_index: [int](class_int.md#class-int), stream: [AudioStream](class_audiostream.md#class-audiostream)) |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-audiostreaminteractive-transitionfromtime"></a>

enum **TransitionFromTime**: [🔗](class_audiostreaminteractive.md#enum-audiostreaminteractive-transitionfromtime)

<a id="class-audiostreaminteractive-constant-transition-from-time-immediate"></a>

[TransitionFromTime](class_audiostreaminteractive.md#enum-audiostreaminteractive-transitionfromtime) **TRANSITION_FROM_TIME_IMMEDIATE** = `0`

Start transition as soon as possible, don't wait for any specific time position.

<a id="class-audiostreaminteractive-constant-transition-from-time-next-beat"></a>

[TransitionFromTime](class_audiostreaminteractive.md#enum-audiostreaminteractive-transitionfromtime) **TRANSITION_FROM_TIME_NEXT_BEAT** = `1`

Transition when the clip playback position reaches the next beat.

<a id="class-audiostreaminteractive-constant-transition-from-time-next-bar"></a>

[TransitionFromTime](class_audiostreaminteractive.md#enum-audiostreaminteractive-transitionfromtime) **TRANSITION_FROM_TIME_NEXT_BAR** = `2`

Transition when the clip playback position reaches the next bar.

<a id="class-audiostreaminteractive-constant-transition-from-time-end"></a>

[TransitionFromTime](class_audiostreaminteractive.md#enum-audiostreaminteractive-transitionfromtime) **TRANSITION_FROM_TIME_END** = `3`

Transition when the current clip finished playing.

---


<a id="enum-audiostreaminteractive-transitiontotime"></a>

enum **TransitionToTime**: [🔗](class_audiostreaminteractive.md#enum-audiostreaminteractive-transitiontotime)

<a id="class-audiostreaminteractive-constant-transition-to-time-same-position"></a>

[TransitionToTime](class_audiostreaminteractive.md#enum-audiostreaminteractive-transitiontotime) **TRANSITION_TO_TIME_SAME_POSITION** = `0`

Transition to the same position in the destination clip. This is useful when both clips have exactly the same length and the music should fade between them.

<a id="class-audiostreaminteractive-constant-transition-to-time-start"></a>

[TransitionToTime](class_audiostreaminteractive.md#enum-audiostreaminteractive-transitiontotime) **TRANSITION_TO_TIME_START** = `1`

Transition to the start of the destination clip.

<a id="class-audiostreaminteractive-constant-transition-to-time-previous-position"></a>

[TransitionToTime](class_audiostreaminteractive.md#enum-audiostreaminteractive-transitiontotime) **TRANSITION_TO_TIME_PREVIOUS_POSITION** = `2`

Transition to the last played position in the destination clip, if there was a previous transition from that clip. Otherwise, plays from the start of the destination clip.

---


<a id="enum-audiostreaminteractive-fademode"></a>

enum **FadeMode**: [🔗](class_audiostreaminteractive.md#enum-audiostreaminteractive-fademode)

<a id="class-audiostreaminteractive-constant-fade-disabled"></a>

[FadeMode](class_audiostreaminteractive.md#enum-audiostreaminteractive-fademode) **FADE_DISABLED** = `0`

Do not use fade for the transition. This is useful when transitioning from a clip-end to clip-beginning, and each clip has their begin/end.

<a id="class-audiostreaminteractive-constant-fade-in"></a>

[FadeMode](class_audiostreaminteractive.md#enum-audiostreaminteractive-fademode) **FADE_IN** = `1`

Use a fade-in in the next clip, let the current clip finish.

<a id="class-audiostreaminteractive-constant-fade-out"></a>

[FadeMode](class_audiostreaminteractive.md#enum-audiostreaminteractive-fademode) **FADE_OUT** = `2`

Use a fade-out in the current clip, the next clip will start by itself.

<a id="class-audiostreaminteractive-constant-fade-cross"></a>

[FadeMode](class_audiostreaminteractive.md#enum-audiostreaminteractive-fademode) **FADE_CROSS** = `3`

Use a cross-fade between clips.

<a id="class-audiostreaminteractive-constant-fade-automatic"></a>

[FadeMode](class_audiostreaminteractive.md#enum-audiostreaminteractive-fademode) **FADE_AUTOMATIC** = `4`

Use automatic fade logic depending on the transition from/to. It is recommended to use this by default.

---


<a id="enum-audiostreaminteractive-autoadvancemode"></a>

enum **AutoAdvanceMode**: [🔗](class_audiostreaminteractive.md#enum-audiostreaminteractive-autoadvancemode)

<a id="class-audiostreaminteractive-constant-auto-advance-disabled"></a>

[AutoAdvanceMode](class_audiostreaminteractive.md#enum-audiostreaminteractive-autoadvancemode) **AUTO_ADVANCE_DISABLED** = `0`

Disable auto-advance (default).

<a id="class-audiostreaminteractive-constant-auto-advance-enabled"></a>

[AutoAdvanceMode](class_audiostreaminteractive.md#enum-audiostreaminteractive-autoadvancemode) **AUTO_ADVANCE_ENABLED** = `1`

Enable auto-advance, a clip must be specified.

<a id="class-audiostreaminteractive-constant-auto-advance-return-to-hold"></a>

[AutoAdvanceMode](class_audiostreaminteractive.md#enum-audiostreaminteractive-autoadvancemode) **AUTO_ADVANCE_RETURN_TO_HOLD** = `2`

Enable auto-advance, but instead of specifying a clip, the playback will return to hold (see [add_transition()](class_audiostreaminteractive.md#class-audiostreaminteractive-method-add-transition)).

---


<a id="constants"></a>

## Constants

<a id="class-audiostreaminteractive-constant-clip-any"></a>

**CLIP_ANY** = `-1` [🔗](class_audiostreaminteractive.md#class-audiostreaminteractive-constant-clip-any)

This constant describes that any clip is valid for a specific transition as either source or destination.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-audiostreaminteractive-property-clip-count"></a>

[int](class_int.md#class-int) **clip_count** = `0` [🔗](class_audiostreaminteractive.md#class-audiostreaminteractive-property-clip-count)

- void **set_clip_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_clip_count**()

Amount of clips contained in this interactive player.

---


<a id="class-audiostreaminteractive-property-initial-clip"></a>

[int](class_int.md#class-int) **initial_clip** = `0` [🔗](class_audiostreaminteractive.md#class-audiostreaminteractive-property-initial-clip)

- void **set_initial_clip**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_initial_clip**()

Index of the initial clip, which will be played first when this stream is played.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-audiostreaminteractive-method-add-transition"></a>

void **add_transition**(from_clip: [int](class_int.md#class-int), to_clip: [int](class_int.md#class-int), from_time: [TransitionFromTime](class_audiostreaminteractive.md#enum-audiostreaminteractive-transitionfromtime), to_time: [TransitionToTime](class_audiostreaminteractive.md#enum-audiostreaminteractive-transitiontotime), fade_mode: [FadeMode](class_audiostreaminteractive.md#enum-audiostreaminteractive-fademode), fade_beats: [float](class_float.md#class-float), use_filler_clip: [bool](class_bool.md#class-bool) = false, filler_clip: [int](class_int.md#class-int) = -1, hold_previous: [bool](class_bool.md#class-bool) = false) [🔗](class_audiostreaminteractive.md#class-audiostreaminteractive-method-add-transition)

Add a transition between two clips. Provide the indices of the source and destination clips, or use the [CLIP_ANY](class_audiostreaminteractive.md#class-audiostreaminteractive-constant-clip-any) constant to indicate that transition happens to/from any clip to this one.

\* `from_time` indicates the moment in the current clip the transition will begin after triggered.

\* `to_time` indicates the time in the next clip that the playback will start from.

\* `fade_mode` indicates how the fade will happen between clips. If unsure, just use [FADE_AUTOMATIC](class_audiostreaminteractive.md#class-audiostreaminteractive-constant-fade-automatic) which uses the most common type of fade for each situation.

\* `fade_beats` indicates how many beats the fade will take. Using decimals is allowed.

\* `use_filler_clip` indicates that there will be a filler clip used between the source and destination clips.

\* `filler_clip` the index of the filler clip.

\* If `hold_previous` is used, then this clip will be remembered. This can be used together with [AUTO_ADVANCE_RETURN_TO_HOLD](class_audiostreaminteractive.md#class-audiostreaminteractive-constant-auto-advance-return-to-hold) to return to this clip after another is done playing.

---


<a id="class-audiostreaminteractive-method-erase-transition"></a>

void **erase_transition**(from_clip: [int](class_int.md#class-int), to_clip: [int](class_int.md#class-int)) [🔗](class_audiostreaminteractive.md#class-audiostreaminteractive-method-erase-transition)

Erase a transition by providing `from_clip` and `to_clip` clip indices. [CLIP_ANY](class_audiostreaminteractive.md#class-audiostreaminteractive-constant-clip-any) can be used for either argument or both.

---


<a id="class-audiostreaminteractive-method-get-clip-auto-advance"></a>

[AutoAdvanceMode](class_audiostreaminteractive.md#enum-audiostreaminteractive-autoadvancemode) **get_clip_auto_advance**(clip_index: [int](class_int.md#class-int)) const [🔗](class_audiostreaminteractive.md#class-audiostreaminteractive-method-get-clip-auto-advance)

Return whether a clip has auto-advance enabled. See [set_clip_auto_advance()](class_audiostreaminteractive.md#class-audiostreaminteractive-method-set-clip-auto-advance).

---


<a id="class-audiostreaminteractive-method-get-clip-auto-advance-next-clip"></a>

[int](class_int.md#class-int) **get_clip_auto_advance_next_clip**(clip_index: [int](class_int.md#class-int)) const [🔗](class_audiostreaminteractive.md#class-audiostreaminteractive-method-get-clip-auto-advance-next-clip)

Return the clip towards which the clip referenced by `clip_index` will auto-advance to.

---


<a id="class-audiostreaminteractive-method-get-clip-name"></a>

[StringName](class_stringname.md#class-stringname) **get_clip_name**(clip_index: [int](class_int.md#class-int)) const [🔗](class_audiostreaminteractive.md#class-audiostreaminteractive-method-get-clip-name)

Return the name of a clip.

---


<a id="class-audiostreaminteractive-method-get-clip-stream"></a>

[AudioStream](class_audiostream.md#class-audiostream) **get_clip_stream**(clip_index: [int](class_int.md#class-int)) const [🔗](class_audiostreaminteractive.md#class-audiostreaminteractive-method-get-clip-stream)

Return the [AudioStream](class_audiostream.md#class-audiostream) associated with a clip.

---


<a id="class-audiostreaminteractive-method-get-transition-fade-beats"></a>

[float](class_float.md#class-float) **get_transition_fade_beats**(from_clip: [int](class_int.md#class-int), to_clip: [int](class_int.md#class-int)) const [🔗](class_audiostreaminteractive.md#class-audiostreaminteractive-method-get-transition-fade-beats)

Return the time (in beats) for a transition (see [add_transition()](class_audiostreaminteractive.md#class-audiostreaminteractive-method-add-transition)).

---


<a id="class-audiostreaminteractive-method-get-transition-fade-mode"></a>

[FadeMode](class_audiostreaminteractive.md#enum-audiostreaminteractive-fademode) **get_transition_fade_mode**(from_clip: [int](class_int.md#class-int), to_clip: [int](class_int.md#class-int)) const [🔗](class_audiostreaminteractive.md#class-audiostreaminteractive-method-get-transition-fade-mode)

Return the mode for a transition (see [add_transition()](class_audiostreaminteractive.md#class-audiostreaminteractive-method-add-transition)).

---


<a id="class-audiostreaminteractive-method-get-transition-filler-clip"></a>

[int](class_int.md#class-int) **get_transition_filler_clip**(from_clip: [int](class_int.md#class-int), to_clip: [int](class_int.md#class-int)) const [🔗](class_audiostreaminteractive.md#class-audiostreaminteractive-method-get-transition-filler-clip)

Return the filler clip for a transition (see [add_transition()](class_audiostreaminteractive.md#class-audiostreaminteractive-method-add-transition)).

---


<a id="class-audiostreaminteractive-method-get-transition-from-time"></a>

[TransitionFromTime](class_audiostreaminteractive.md#enum-audiostreaminteractive-transitionfromtime) **get_transition_from_time**(from_clip: [int](class_int.md#class-int), to_clip: [int](class_int.md#class-int)) const [🔗](class_audiostreaminteractive.md#class-audiostreaminteractive-method-get-transition-from-time)

Return the source time position for a transition (see [add_transition()](class_audiostreaminteractive.md#class-audiostreaminteractive-method-add-transition)).

---


<a id="class-audiostreaminteractive-method-get-transition-list"></a>

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_transition_list**() const [🔗](class_audiostreaminteractive.md#class-audiostreaminteractive-method-get-transition-list)

Return the list of transitions (from, to interleaved).

---


<a id="class-audiostreaminteractive-method-get-transition-to-time"></a>

[TransitionToTime](class_audiostreaminteractive.md#enum-audiostreaminteractive-transitiontotime) **get_transition_to_time**(from_clip: [int](class_int.md#class-int), to_clip: [int](class_int.md#class-int)) const [🔗](class_audiostreaminteractive.md#class-audiostreaminteractive-method-get-transition-to-time)

Return the destination time position for a transition (see [add_transition()](class_audiostreaminteractive.md#class-audiostreaminteractive-method-add-transition)).

---


<a id="class-audiostreaminteractive-method-has-transition"></a>

[bool](class_bool.md#class-bool) **has_transition**(from_clip: [int](class_int.md#class-int), to_clip: [int](class_int.md#class-int)) const [🔗](class_audiostreaminteractive.md#class-audiostreaminteractive-method-has-transition)

Returns `true` if a given transition exists (was added via [add_transition()](class_audiostreaminteractive.md#class-audiostreaminteractive-method-add-transition)).

---


<a id="class-audiostreaminteractive-method-is-transition-holding-previous"></a>

[bool](class_bool.md#class-bool) **is_transition_holding_previous**(from_clip: [int](class_int.md#class-int), to_clip: [int](class_int.md#class-int)) const [🔗](class_audiostreaminteractive.md#class-audiostreaminteractive-method-is-transition-holding-previous)

Return whether a transition uses the *hold previous* functionality (see [add_transition()](class_audiostreaminteractive.md#class-audiostreaminteractive-method-add-transition)).

---


<a id="class-audiostreaminteractive-method-is-transition-using-filler-clip"></a>

[bool](class_bool.md#class-bool) **is_transition_using_filler_clip**(from_clip: [int](class_int.md#class-int), to_clip: [int](class_int.md#class-int)) const [🔗](class_audiostreaminteractive.md#class-audiostreaminteractive-method-is-transition-using-filler-clip)

Return whether a transition uses the *filler clip* functionality (see [add_transition()](class_audiostreaminteractive.md#class-audiostreaminteractive-method-add-transition)).

---


<a id="class-audiostreaminteractive-method-set-clip-auto-advance"></a>

void **set_clip_auto_advance**(clip_index: [int](class_int.md#class-int), mode: [AutoAdvanceMode](class_audiostreaminteractive.md#enum-audiostreaminteractive-autoadvancemode)) [🔗](class_audiostreaminteractive.md#class-audiostreaminteractive-method-set-clip-auto-advance)

Set whether a clip will auto-advance by changing the auto-advance mode.

---


<a id="class-audiostreaminteractive-method-set-clip-auto-advance-next-clip"></a>

void **set_clip_auto_advance_next_clip**(clip_index: [int](class_int.md#class-int), auto_advance_next_clip: [int](class_int.md#class-int)) [🔗](class_audiostreaminteractive.md#class-audiostreaminteractive-method-set-clip-auto-advance-next-clip)

Set the index of the next clip towards which this clip will auto advance to when finished. If the clip being played loops, then auto-advance will be ignored.

---


<a id="class-audiostreaminteractive-method-set-clip-name"></a>

void **set_clip_name**(clip_index: [int](class_int.md#class-int), name: [StringName](class_stringname.md#class-stringname)) [🔗](class_audiostreaminteractive.md#class-audiostreaminteractive-method-set-clip-name)

Set the name of the current clip (for easier identification).

---


<a id="class-audiostreaminteractive-method-set-clip-stream"></a>

void **set_clip_stream**(clip_index: [int](class_int.md#class-int), stream: [AudioStream](class_audiostream.md#class-audiostream)) [🔗](class_audiostreaminteractive.md#class-audiostreaminteractive-method-set-clip-stream)

Set the [AudioStream](class_audiostream.md#class-audiostream) associated with the current clip.
