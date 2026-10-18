> Source: https://docs.godotengine.org/en/4.7/classes/class_audiostreamplayer2d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="audiostreamplayer2d"></a>

<a id="class-audiostreamplayer2d"></a>

# AudioStreamPlayer2D

**Inherits:** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Plays positional sound in 2D space.

<a id="description"></a>

## Description

Plays audio that is attenuated with distance to the listener.

By default, audio is heard from the screen center. This can be changed by adding an [AudioListener2D](class_audiolistener2d.md#class-audiolistener2d) node to the scene and enabling it by calling [AudioListener2D.make_current()](class_audiolistener2d.md#class-audiolistener2d-method-make-current) on it.

See also [AudioStreamPlayer](class_audiostreamplayer.md#class-audiostreamplayer) to play a sound non-positionally.

**Note:** Hiding an **AudioStreamPlayer2D** node does not disable its audio output. To temporarily disable an **AudioStreamPlayer2D**'s audio output, set [volume_db](class_audiostreamplayer2d.md#class-audiostreamplayer2d-property-volume-db) to a very low value like `-100` (which isn't audible to human hearing).

<a id="tutorials"></a>

## Tutorials

- [Audio streams](../tutorials/audio/audio_streams.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [area_mask](class_audiostreamplayer2d.md#class-audiostreamplayer2d-property-area-mask) | `0` |
| [float](class_float.md#class-float) | [attenuation](class_audiostreamplayer2d.md#class-audiostreamplayer2d-property-attenuation) | `1.0` |
| [bool](class_bool.md#class-bool) | [autoplay](class_audiostreamplayer2d.md#class-audiostreamplayer2d-property-autoplay) | `false` |
| [StringName](class_stringname.md#class-stringname) | [bus](class_audiostreamplayer2d.md#class-audiostreamplayer2d-property-bus) | `&"Master"` |
| [float](class_float.md#class-float) | [max_distance](class_audiostreamplayer2d.md#class-audiostreamplayer2d-property-max-distance) | `2000.0` |
| [int](class_int.md#class-int) | [max_polyphony](class_audiostreamplayer2d.md#class-audiostreamplayer2d-property-max-polyphony) | `1` |
| [float](class_float.md#class-float) | [panning_strength](class_audiostreamplayer2d.md#class-audiostreamplayer2d-property-panning-strength) | `1.0` |
| [float](class_float.md#class-float) | [pitch_scale](class_audiostreamplayer2d.md#class-audiostreamplayer2d-property-pitch-scale) | `1.0` |
| [PlaybackType](class_audioserver.md#enum-audioserver-playbacktype) | [playback_type](class_audiostreamplayer2d.md#class-audiostreamplayer2d-property-playback-type) | `0` |
| [bool](class_bool.md#class-bool) | [playing](class_audiostreamplayer2d.md#class-audiostreamplayer2d-property-playing) | `false` |
| [AudioStream](class_audiostream.md#class-audiostream) | [stream](class_audiostreamplayer2d.md#class-audiostreamplayer2d-property-stream) |  |
| [bool](class_bool.md#class-bool) | [stream_paused](class_audiostreamplayer2d.md#class-audiostreamplayer2d-property-stream-paused) | `false` |
| [float](class_float.md#class-float) | [volume_db](class_audiostreamplayer2d.md#class-audiostreamplayer2d-property-volume-db) | `0.0` |
| [float](class_float.md#class-float) | [volume_linear](class_audiostreamplayer2d.md#class-audiostreamplayer2d-property-volume-linear) |  |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [float](class_float.md#class-float) | [get_playback_position](class_audiostreamplayer2d.md#class-audiostreamplayer2d-method-get-playback-position)() |
| [AudioStreamPlayback](class_audiostreamplayback.md#class-audiostreamplayback) | [get_stream_playback](class_audiostreamplayer2d.md#class-audiostreamplayer2d-method-get-stream-playback)() |
| [bool](class_bool.md#class-bool) | [has_stream_playback](class_audiostreamplayer2d.md#class-audiostreamplayer2d-method-has-stream-playback)() |
| void | [play](class_audiostreamplayer2d.md#class-audiostreamplayer2d-method-play)(from_position: [float](class_float.md#class-float) = 0.0) |
| void | [seek](class_audiostreamplayer2d.md#class-audiostreamplayer2d-method-seek)(to_position: [float](class_float.md#class-float)) |
| void | [stop](class_audiostreamplayer2d.md#class-audiostreamplayer2d-method-stop)() |

---


<a id="signals"></a>

## Signals

<a id="class-audiostreamplayer2d-signal-finished"></a>

**finished**() [🔗](class_audiostreamplayer2d.md#class-audiostreamplayer2d-signal-finished)

Emitted when the audio stops playing.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-audiostreamplayer2d-property-area-mask"></a>

[int](class_int.md#class-int) **area_mask** = `0` [🔗](class_audiostreamplayer2d.md#class-audiostreamplayer2d-property-area-mask)

- void **set_area_mask**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_area_mask**()

Determines which [Area2D](class_area2d.md#class-area2d) layers affect the sound for reverb and audio bus effects. Areas can be used to redirect [AudioStream](class_audiostream.md#class-audiostream)s so that they play in a certain audio bus. An example of how you might use this is making a "water" area so that sounds played in the water are redirected through an audio bus to make them sound like they are being played underwater.

---


<a id="class-audiostreamplayer2d-property-attenuation"></a>

[float](class_float.md#class-float) **attenuation** = `1.0` [🔗](class_audiostreamplayer2d.md#class-audiostreamplayer2d-property-attenuation)

- void **set_attenuation**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_attenuation**()

The volume is attenuated over distance with this as an exponent.

---


<a id="class-audiostreamplayer2d-property-autoplay"></a>

[bool](class_bool.md#class-bool) **autoplay** = `false` [🔗](class_audiostreamplayer2d.md#class-audiostreamplayer2d-property-autoplay)

- void **set_autoplay**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_autoplay_enabled**()

If `true`, audio plays when added to scene tree.

---


<a id="class-audiostreamplayer2d-property-bus"></a>

[StringName](class_stringname.md#class-stringname) **bus** = `&"Master"` [🔗](class_audiostreamplayer2d.md#class-audiostreamplayer2d-property-bus)

- void **set_bus**(value: [StringName](class_stringname.md#class-stringname))
- [StringName](class_stringname.md#class-stringname) **get_bus**()

Bus on which this audio is playing.

**Note:** When setting this property, keep in mind that no validation is performed to see if the given name matches an existing bus. This is because audio bus layouts might be loaded after this property is set. If this given name can't be resolved at runtime, it will fall back to `"Master"`.

---


<a id="class-audiostreamplayer2d-property-max-distance"></a>

[float](class_float.md#class-float) **max_distance** = `2000.0` [🔗](class_audiostreamplayer2d.md#class-audiostreamplayer2d-property-max-distance)

- void **set_max_distance**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_max_distance**()

Maximum distance from which audio is still hearable.

---


<a id="class-audiostreamplayer2d-property-max-polyphony"></a>

[int](class_int.md#class-int) **max_polyphony** = `1` [🔗](class_audiostreamplayer2d.md#class-audiostreamplayer2d-property-max-polyphony)

- void **set_max_polyphony**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_max_polyphony**()

The maximum number of sounds this node can play at the same time. Playing additional sounds after this value is reached will cut off the oldest sounds.

---


<a id="class-audiostreamplayer2d-property-panning-strength"></a>

[float](class_float.md#class-float) **panning_strength** = `1.0` [🔗](class_audiostreamplayer2d.md#class-audiostreamplayer2d-property-panning-strength)

- void **set_panning_strength**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_panning_strength**()

Scales the panning strength for this node by multiplying the base [ProjectSettings.audio/general/2d_panning_strength](class_projectsettings.md#class-projectsettings-property-audio-general-2d-panning-strength) with this factor. Higher values will pan audio from left to right more dramatically than lower values.

---


<a id="class-audiostreamplayer2d-property-pitch-scale"></a>

[float](class_float.md#class-float) **pitch_scale** = `1.0` [🔗](class_audiostreamplayer2d.md#class-audiostreamplayer2d-property-pitch-scale)

- void **set_pitch_scale**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_pitch_scale**()

The pitch and the tempo of the audio, as a multiplier of the audio sample's sample rate.

---


<a id="class-audiostreamplayer2d-property-playback-type"></a>

[PlaybackType](class_audioserver.md#enum-audioserver-playbacktype) **playback_type** = `0` [🔗](class_audiostreamplayer2d.md#class-audiostreamplayer2d-property-playback-type)

- void **set_playback_type**(value: [PlaybackType](class_audioserver.md#enum-audioserver-playbacktype))
- [PlaybackType](class_audioserver.md#enum-audioserver-playbacktype) **get_playback_type**()

**Experimental:** This property may be changed or removed in future versions.

The playback type of the stream player. If set other than to the default value, it will force that playback type.

---


<a id="class-audiostreamplayer2d-property-playing"></a>

[bool](class_bool.md#class-bool) **playing** = `false` [🔗](class_audiostreamplayer2d.md#class-audiostreamplayer2d-property-playing)

- void **set_playing**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_playing**()

If `true`, audio is playing or is queued to be played (see [play()](class_audiostreamplayer2d.md#class-audiostreamplayer2d-method-play)).

---


<a id="class-audiostreamplayer2d-property-stream"></a>

[AudioStream](class_audiostream.md#class-audiostream) **stream** [🔗](class_audiostreamplayer2d.md#class-audiostreamplayer2d-property-stream)

- void **set_stream**(value: [AudioStream](class_audiostream.md#class-audiostream))
- [AudioStream](class_audiostream.md#class-audiostream) **get_stream**()

The [AudioStream](class_audiostream.md#class-audiostream) object to be played.

---


<a id="class-audiostreamplayer2d-property-stream-paused"></a>

[bool](class_bool.md#class-bool) **stream_paused** = `false` [🔗](class_audiostreamplayer2d.md#class-audiostreamplayer2d-property-stream-paused)

- void **set_stream_paused**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_stream_paused**()

If `true`, the playback is paused. You can resume it by setting [stream_paused](class_audiostreamplayer2d.md#class-audiostreamplayer2d-property-stream-paused) to `false`.

---


<a id="class-audiostreamplayer2d-property-volume-db"></a>

[float](class_float.md#class-float) **volume_db** = `0.0` [🔗](class_audiostreamplayer2d.md#class-audiostreamplayer2d-property-volume-db)

- void **set_volume_db**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_volume_db**()

Base volume before attenuation, in decibels.

---


<a id="class-audiostreamplayer2d-property-volume-linear"></a>

[float](class_float.md#class-float) **volume_linear** [🔗](class_audiostreamplayer2d.md#class-audiostreamplayer2d-property-volume-linear)

- void **set_volume_linear**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_volume_linear**()

Base volume before attenuation, as a linear value.

**Note:** This member modifies [volume_db](class_audiostreamplayer2d.md#class-audiostreamplayer2d-property-volume-db) for convenience. The returned value is equivalent to the result of [@GlobalScope.db_to_linear()](class_@globalscope.md#class-globalscope-method-db-to-linear) on [volume_db](class_audiostreamplayer2d.md#class-audiostreamplayer2d-property-volume-db). Setting this member is equivalent to setting [volume_db](class_audiostreamplayer2d.md#class-audiostreamplayer2d-property-volume-db) to the result of [@GlobalScope.linear_to_db()](class_@globalscope.md#class-globalscope-method-linear-to-db) on a value.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-audiostreamplayer2d-method-get-playback-position"></a>

[float](class_float.md#class-float) **get_playback_position**() [🔗](class_audiostreamplayer2d.md#class-audiostreamplayer2d-method-get-playback-position)

Returns the position in the [AudioStream](class_audiostream.md#class-audiostream).

---


<a id="class-audiostreamplayer2d-method-get-stream-playback"></a>

[AudioStreamPlayback](class_audiostreamplayback.md#class-audiostreamplayback) **get_stream_playback**() [🔗](class_audiostreamplayer2d.md#class-audiostreamplayer2d-method-get-stream-playback)

Returns the [AudioStreamPlayback](class_audiostreamplayback.md#class-audiostreamplayback) object associated with this **AudioStreamPlayer2D**.

---


<a id="class-audiostreamplayer2d-method-has-stream-playback"></a>

[bool](class_bool.md#class-bool) **has_stream_playback**() [🔗](class_audiostreamplayer2d.md#class-audiostreamplayer2d-method-has-stream-playback)

Returns whether the [AudioStreamPlayer](class_audiostreamplayer.md#class-audiostreamplayer) can return the [AudioStreamPlayback](class_audiostreamplayback.md#class-audiostreamplayback) object or not.

---


<a id="class-audiostreamplayer2d-method-play"></a>

void **play**(from_position: [float](class_float.md#class-float) = 0.0) [🔗](class_audiostreamplayer2d.md#class-audiostreamplayer2d-method-play)

Queues the audio to play on the next physics frame, from the given position `from_position`, in seconds.

---


<a id="class-audiostreamplayer2d-method-seek"></a>

void **seek**(to_position: [float](class_float.md#class-float)) [🔗](class_audiostreamplayer2d.md#class-audiostreamplayer2d-method-seek)

Sets the position from which audio will be played, in seconds.

---


<a id="class-audiostreamplayer2d-method-stop"></a>

void **stop**() [🔗](class_audiostreamplayer2d.md#class-audiostreamplayer2d-method-stop)

Stops the audio.
