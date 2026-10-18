> Source: https://docs.godotengine.org/en/4.7/classes/class_animation.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="animation"></a>

<a id="class-animation"></a>

# Animation

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Holds data that can be used to animate anything in the engine.

<a id="description"></a>

## Description

This resource holds data that can be used to animate anything in the engine. Animations are divided into tracks and each track must be linked to a node. The state of that node can be changed through time, by adding timed keys (events) to the track.

```gdscript
# This creates an animation that makes the node "Enemy" move to the right by
# 100 pixels in 2.0 seconds.
var animation = Animation.new()
var track_index = animation.add_track(Animation.TYPE_VALUE)
animation.track_set_path(track_index, "Enemy:position:x")
animation.track_insert_key(track_index, 0.0, 0)
animation.track_insert_key(track_index, 2.0, 100)
animation.length = 2.0
```

```csharp
// This creates an animation that makes the node "Enemy" move to the right by
// 100 pixels in 2.0 seconds.
var animation = new Animation();
int trackIndex = animation.AddTrack(Animation.TrackType.Value);
animation.TrackSetPath(trackIndex, "Enemy:position:x");
animation.TrackInsertKey(trackIndex, 0.0f, 0);
animation.TrackInsertKey(trackIndex, 2.0f, 100);
animation.Length = 2.0f;
```

Animations are just data containers, and must be added to nodes such as an [AnimationPlayer](class_animationplayer.md#class-animationplayer) to be played back. Animation tracks have different types, each with its own set of dedicated methods. Check [TrackType](class_animation.md#enum-animation-tracktype) to see available types.

**Note:** For 3D position/rotation/scale, using the dedicated [TYPE_POSITION_3D](class_animation.md#class-animation-constant-type-position-3d), [TYPE_ROTATION_3D](class_animation.md#class-animation-constant-type-rotation-3d) and [TYPE_SCALE_3D](class_animation.md#class-animation-constant-type-scale-3d) track types instead of [TYPE_VALUE](class_animation.md#class-animation-constant-type-value) is recommended for performance reasons.

<a id="tutorials"></a>

## Tutorials

- [Animation documentation index](../tutorials/animation/index.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [capture_included](class_animation.md#class-animation-property-capture-included) | `false` |
| [float](class_float.md#class-float) | [length](class_animation.md#class-animation-property-length) | `1.0` |
| [LoopMode](class_animation.md#enum-animation-loopmode) | [loop_mode](class_animation.md#class-animation-property-loop-mode) | `0` |
| [float](class_float.md#class-float) | [step](class_animation.md#class-animation-property-step) | `0.033333335` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_marker](class_animation.md#class-animation-method-add-marker)(name: [StringName](class_stringname.md#class-stringname), time: [float](class_float.md#class-float)) |
| [int](class_int.md#class-int) | [add_track](class_animation.md#class-animation-method-add-track)(type: [TrackType](class_animation.md#enum-animation-tracktype), at_position: [int](class_int.md#class-int) = -1) |
| [StringName](class_stringname.md#class-stringname) | [animation_track_get_key_animation](class_animation.md#class-animation-method-animation-track-get-key-animation)(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [animation_track_insert_key](class_animation.md#class-animation-method-animation-track-insert-key)(track_idx: [int](class_int.md#class-int), time: [float](class_float.md#class-float), animation: [StringName](class_stringname.md#class-stringname)) |
| void | [animation_track_set_key_animation](class_animation.md#class-animation-method-animation-track-set-key-animation)(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int), animation: [StringName](class_stringname.md#class-stringname)) |
| [float](class_float.md#class-float) | [audio_track_get_key_end_offset](class_animation.md#class-animation-method-audio-track-get-key-end-offset)(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int)) const |
| [float](class_float.md#class-float) | [audio_track_get_key_start_offset](class_animation.md#class-animation-method-audio-track-get-key-start-offset)(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int)) const |
| [Resource](class_resource.md#class-resource) | [audio_track_get_key_stream](class_animation.md#class-animation-method-audio-track-get-key-stream)(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [audio_track_insert_key](class_animation.md#class-animation-method-audio-track-insert-key)(track_idx: [int](class_int.md#class-int), time: [float](class_float.md#class-float), stream: [Resource](class_resource.md#class-resource), start_offset: [float](class_float.md#class-float) = 0, end_offset: [float](class_float.md#class-float) = 0) |
| [bool](class_bool.md#class-bool) | [audio_track_is_use_blend](class_animation.md#class-animation-method-audio-track-is-use-blend)(track_idx: [int](class_int.md#class-int)) const |
| void | [audio_track_set_key_end_offset](class_animation.md#class-animation-method-audio-track-set-key-end-offset)(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int), offset: [float](class_float.md#class-float)) |
| void | [audio_track_set_key_start_offset](class_animation.md#class-animation-method-audio-track-set-key-start-offset)(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int), offset: [float](class_float.md#class-float)) |
| void | [audio_track_set_key_stream](class_animation.md#class-animation-method-audio-track-set-key-stream)(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int), stream: [Resource](class_resource.md#class-resource)) |
| void | [audio_track_set_use_blend](class_animation.md#class-animation-method-audio-track-set-use-blend)(track_idx: [int](class_int.md#class-int), enable: [bool](class_bool.md#class-bool)) |
| [Vector2](class_vector2.md#class-vector2) | [bezier_track_get_key_in_handle](class_animation.md#class-animation-method-bezier-track-get-key-in-handle)(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int)) const |
| [Vector2](class_vector2.md#class-vector2) | [bezier_track_get_key_out_handle](class_animation.md#class-animation-method-bezier-track-get-key-out-handle)(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int)) const |
| [float](class_float.md#class-float) | [bezier_track_get_key_value](class_animation.md#class-animation-method-bezier-track-get-key-value)(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [bezier_track_insert_key](class_animation.md#class-animation-method-bezier-track-insert-key)(track_idx: [int](class_int.md#class-int), time: [float](class_float.md#class-float), value: [float](class_float.md#class-float), in_handle: [Vector2](class_vector2.md#class-vector2) = Vector2(0, 0), out_handle: [Vector2](class_vector2.md#class-vector2) = Vector2(0, 0)) |
| [float](class_float.md#class-float) | [bezier_track_interpolate](class_animation.md#class-animation-method-bezier-track-interpolate)(track_idx: [int](class_int.md#class-int), time: [float](class_float.md#class-float)) const |
| void | [bezier_track_set_key_in_handle](class_animation.md#class-animation-method-bezier-track-set-key-in-handle)(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int), in_handle: [Vector2](class_vector2.md#class-vector2), balanced_value_time_ratio: [float](class_float.md#class-float) = 1.0) |
| void | [bezier_track_set_key_out_handle](class_animation.md#class-animation-method-bezier-track-set-key-out-handle)(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int), out_handle: [Vector2](class_vector2.md#class-vector2), balanced_value_time_ratio: [float](class_float.md#class-float) = 1.0) |
| void | [bezier_track_set_key_value](class_animation.md#class-animation-method-bezier-track-set-key-value)(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int), value: [float](class_float.md#class-float)) |
| [int](class_int.md#class-int) | [blend_shape_track_insert_key](class_animation.md#class-animation-method-blend-shape-track-insert-key)(track_idx: [int](class_int.md#class-int), time: [float](class_float.md#class-float), amount: [float](class_float.md#class-float)) |
| [float](class_float.md#class-float) | [blend_shape_track_interpolate](class_animation.md#class-animation-method-blend-shape-track-interpolate)(track_idx: [int](class_int.md#class-int), time_sec: [float](class_float.md#class-float), backward: [bool](class_bool.md#class-bool) = false) const |
| void | [clear](class_animation.md#class-animation-method-clear)() |
| void | [compress](class_animation.md#class-animation-method-compress)(page_size: [int](class_int.md#class-int) = 8192, fps: [int](class_int.md#class-int) = 120, split_tolerance: [float](class_float.md#class-float) = 4.0) |
| void | [copy_track](class_animation.md#class-animation-method-copy-track)(track_idx: [int](class_int.md#class-int), to_animation: [Animation](class_animation.md#class-animation)) |
| [int](class_int.md#class-int) | [find_track](class_animation.md#class-animation-method-find-track)(path: [NodePath](class_nodepath.md#class-nodepath), type: [TrackType](class_animation.md#enum-animation-tracktype)) const |
| [StringName](class_stringname.md#class-stringname) | [get_marker_at_time](class_animation.md#class-animation-method-get-marker-at-time)(time: [float](class_float.md#class-float)) const |
| [Color](class_color.md#class-color) | [get_marker_color](class_animation.md#class-animation-method-get-marker-color)(name: [StringName](class_stringname.md#class-stringname)) const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [get_marker_names](class_animation.md#class-animation-method-get-marker-names)() const |
| [float](class_float.md#class-float) | [get_marker_time](class_animation.md#class-animation-method-get-marker-time)(name: [StringName](class_stringname.md#class-stringname)) const |
| [StringName](class_stringname.md#class-stringname) | [get_next_marker](class_animation.md#class-animation-method-get-next-marker)(time: [float](class_float.md#class-float)) const |
| [StringName](class_stringname.md#class-stringname) | [get_prev_marker](class_animation.md#class-animation-method-get-prev-marker)(time: [float](class_float.md#class-float)) const |
| [int](class_int.md#class-int) | [get_track_count](class_animation.md#class-animation-method-get-track-count)() const |
| [bool](class_bool.md#class-bool) | [has_marker](class_animation.md#class-animation-method-has-marker)(name: [StringName](class_stringname.md#class-stringname)) const |
| [StringName](class_stringname.md#class-stringname) | [method_track_get_name](class_animation.md#class-animation-method-method-track-get-name)(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int)) const |
| [Array](class_array.md#class-array) | [method_track_get_params](class_animation.md#class-animation-method-method-track-get-params)(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int)) const |
| void | [optimize](class_animation.md#class-animation-method-optimize)(allowed_velocity_err: [float](class_float.md#class-float) = 0.01, allowed_angular_err: [float](class_float.md#class-float) = 0.01, precision: [int](class_int.md#class-int) = 3) |
| [int](class_int.md#class-int) | [position_track_insert_key](class_animation.md#class-animation-method-position-track-insert-key)(track_idx: [int](class_int.md#class-int), time: [float](class_float.md#class-float), position: [Vector3](class_vector3.md#class-vector3)) |
| [Vector3](class_vector3.md#class-vector3) | [position_track_interpolate](class_animation.md#class-animation-method-position-track-interpolate)(track_idx: [int](class_int.md#class-int), time_sec: [float](class_float.md#class-float), backward: [bool](class_bool.md#class-bool) = false) const |
| void | [remove_marker](class_animation.md#class-animation-method-remove-marker)(name: [StringName](class_stringname.md#class-stringname)) |
| void | [remove_track](class_animation.md#class-animation-method-remove-track)(track_idx: [int](class_int.md#class-int)) |
| [int](class_int.md#class-int) | [rotation_track_insert_key](class_animation.md#class-animation-method-rotation-track-insert-key)(track_idx: [int](class_int.md#class-int), time: [float](class_float.md#class-float), rotation: [Quaternion](class_quaternion.md#class-quaternion)) |
| [Quaternion](class_quaternion.md#class-quaternion) | [rotation_track_interpolate](class_animation.md#class-animation-method-rotation-track-interpolate)(track_idx: [int](class_int.md#class-int), time_sec: [float](class_float.md#class-float), backward: [bool](class_bool.md#class-bool) = false) const |
| [int](class_int.md#class-int) | [scale_track_insert_key](class_animation.md#class-animation-method-scale-track-insert-key)(track_idx: [int](class_int.md#class-int), time: [float](class_float.md#class-float), scale: [Vector3](class_vector3.md#class-vector3)) |
| [Vector3](class_vector3.md#class-vector3) | [scale_track_interpolate](class_animation.md#class-animation-method-scale-track-interpolate)(track_idx: [int](class_int.md#class-int), time_sec: [float](class_float.md#class-float), backward: [bool](class_bool.md#class-bool) = false) const |
| void | [set_marker_color](class_animation.md#class-animation-method-set-marker-color)(name: [StringName](class_stringname.md#class-stringname), color: [Color](class_color.md#class-color)) |
| [int](class_int.md#class-int) | [track_find_key](class_animation.md#class-animation-method-track-find-key)(track_idx: [int](class_int.md#class-int), time: [float](class_float.md#class-float), find_mode: [FindMode](class_animation.md#enum-animation-findmode) = 0, limit: [bool](class_bool.md#class-bool) = false, backward: [bool](class_bool.md#class-bool) = false) const |
| [bool](class_bool.md#class-bool) | [track_get_interpolation_loop_wrap](class_animation.md#class-animation-method-track-get-interpolation-loop-wrap)(track_idx: [int](class_int.md#class-int)) const |
| [InterpolationType](class_animation.md#enum-animation-interpolationtype) | [track_get_interpolation_type](class_animation.md#class-animation-method-track-get-interpolation-type)(track_idx: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [track_get_key_count](class_animation.md#class-animation-method-track-get-key-count)(track_idx: [int](class_int.md#class-int)) const |
| [float](class_float.md#class-float) | [track_get_key_time](class_animation.md#class-animation-method-track-get-key-time)(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int)) const |
| [float](class_float.md#class-float) | [track_get_key_transition](class_animation.md#class-animation-method-track-get-key-transition)(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int)) const |
| [Variant](class_variant.md#class-variant) | [track_get_key_value](class_animation.md#class-animation-method-track-get-key-value)(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int)) const |
| [NodePath](class_nodepath.md#class-nodepath) | [track_get_path](class_animation.md#class-animation-method-track-get-path)(track_idx: [int](class_int.md#class-int)) const |
| [TrackType](class_animation.md#enum-animation-tracktype) | [track_get_type](class_animation.md#class-animation-method-track-get-type)(track_idx: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [track_insert_key](class_animation.md#class-animation-method-track-insert-key)(track_idx: [int](class_int.md#class-int), time: [float](class_float.md#class-float), key: [Variant](class_variant.md#class-variant), transition: [float](class_float.md#class-float) = 1) |
| [bool](class_bool.md#class-bool) | [track_is_compressed](class_animation.md#class-animation-method-track-is-compressed)(track_idx: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [track_is_enabled](class_animation.md#class-animation-method-track-is-enabled)(track_idx: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [track_is_imported](class_animation.md#class-animation-method-track-is-imported)(track_idx: [int](class_int.md#class-int)) const |
| void | [track_move_down](class_animation.md#class-animation-method-track-move-down)(track_idx: [int](class_int.md#class-int)) |
| void | [track_move_to](class_animation.md#class-animation-method-track-move-to)(track_idx: [int](class_int.md#class-int), to_idx: [int](class_int.md#class-int)) |
| void | [track_move_up](class_animation.md#class-animation-method-track-move-up)(track_idx: [int](class_int.md#class-int)) |
| void | [track_remove_key](class_animation.md#class-animation-method-track-remove-key)(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int)) |
| void | [track_remove_key_at_time](class_animation.md#class-animation-method-track-remove-key-at-time)(track_idx: [int](class_int.md#class-int), time: [float](class_float.md#class-float)) |
| void | [track_set_enabled](class_animation.md#class-animation-method-track-set-enabled)(track_idx: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool)) |
| void | [track_set_imported](class_animation.md#class-animation-method-track-set-imported)(track_idx: [int](class_int.md#class-int), imported: [bool](class_bool.md#class-bool)) |
| void | [track_set_interpolation_loop_wrap](class_animation.md#class-animation-method-track-set-interpolation-loop-wrap)(track_idx: [int](class_int.md#class-int), interpolation: [bool](class_bool.md#class-bool)) |
| void | [track_set_interpolation_type](class_animation.md#class-animation-method-track-set-interpolation-type)(track_idx: [int](class_int.md#class-int), interpolation: [InterpolationType](class_animation.md#enum-animation-interpolationtype)) |
| void | [track_set_key_time](class_animation.md#class-animation-method-track-set-key-time)(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int), time: [float](class_float.md#class-float)) |
| void | [track_set_key_transition](class_animation.md#class-animation-method-track-set-key-transition)(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int), transition: [float](class_float.md#class-float)) |
| void | [track_set_key_value](class_animation.md#class-animation-method-track-set-key-value)(track_idx: [int](class_int.md#class-int), key: [int](class_int.md#class-int), value: [Variant](class_variant.md#class-variant)) |
| void | [track_set_path](class_animation.md#class-animation-method-track-set-path)(track_idx: [int](class_int.md#class-int), path: [NodePath](class_nodepath.md#class-nodepath)) |
| void | [track_swap](class_animation.md#class-animation-method-track-swap)(track_idx: [int](class_int.md#class-int), with_idx: [int](class_int.md#class-int)) |
| [UpdateMode](class_animation.md#enum-animation-updatemode) | [value_track_get_update_mode](class_animation.md#class-animation-method-value-track-get-update-mode)(track_idx: [int](class_int.md#class-int)) const |
| [Variant](class_variant.md#class-variant) | [value_track_interpolate](class_animation.md#class-animation-method-value-track-interpolate)(track_idx: [int](class_int.md#class-int), time_sec: [float](class_float.md#class-float), backward: [bool](class_bool.md#class-bool) = false) const |
| void | [value_track_set_update_mode](class_animation.md#class-animation-method-value-track-set-update-mode)(track_idx: [int](class_int.md#class-int), mode: [UpdateMode](class_animation.md#enum-animation-updatemode)) |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-animation-tracktype"></a>

enum **TrackType**: [🔗](class_animation.md#enum-animation-tracktype)

<a id="class-animation-constant-type-value"></a>

[TrackType](class_animation.md#enum-animation-tracktype) **TYPE_VALUE** = `0`

Value tracks set values in node properties, but only those which can be interpolated. For 3D position/rotation/scale, using the dedicated [TYPE_POSITION_3D](class_animation.md#class-animation-constant-type-position-3d), [TYPE_ROTATION_3D](class_animation.md#class-animation-constant-type-rotation-3d) and [TYPE_SCALE_3D](class_animation.md#class-animation-constant-type-scale-3d) track types instead of [TYPE_VALUE](class_animation.md#class-animation-constant-type-value) is recommended for performance reasons.

<a id="class-animation-constant-type-position-3d"></a>

[TrackType](class_animation.md#enum-animation-tracktype) **TYPE_POSITION_3D** = `1`

3D position track (values are stored in [Vector3](class_vector3.md#class-vector3)s).

<a id="class-animation-constant-type-rotation-3d"></a>

[TrackType](class_animation.md#enum-animation-tracktype) **TYPE_ROTATION_3D** = `2`

3D rotation track (values are stored in [Quaternion](class_quaternion.md#class-quaternion)s).

<a id="class-animation-constant-type-scale-3d"></a>

[TrackType](class_animation.md#enum-animation-tracktype) **TYPE_SCALE_3D** = `3`

3D scale track (values are stored in [Vector3](class_vector3.md#class-vector3)s).

<a id="class-animation-constant-type-blend-shape"></a>

[TrackType](class_animation.md#enum-animation-tracktype) **TYPE_BLEND_SHAPE** = `4`

Blend shape track.

<a id="class-animation-constant-type-method"></a>

[TrackType](class_animation.md#enum-animation-tracktype) **TYPE_METHOD** = `5`

Method tracks call functions with given arguments per key.

<a id="class-animation-constant-type-bezier"></a>

[TrackType](class_animation.md#enum-animation-tracktype) **TYPE_BEZIER** = `6`

Bezier tracks are used to interpolate a value using custom curves. They can also be used to animate sub-properties of vectors and colors (e.g. alpha value of a [Color](class_color.md#class-color)).

<a id="class-animation-constant-type-audio"></a>

[TrackType](class_animation.md#enum-animation-tracktype) **TYPE_AUDIO** = `7`

Audio tracks are used to play an audio stream with either type of [AudioStreamPlayer](class_audiostreamplayer.md#class-audiostreamplayer). The stream can be trimmed and previewed in the animation.

<a id="class-animation-constant-type-animation"></a>

[TrackType](class_animation.md#enum-animation-tracktype) **TYPE_ANIMATION** = `8`

Animation tracks play animations in other [AnimationPlayer](class_animationplayer.md#class-animationplayer) nodes.

---


<a id="enum-animation-interpolationtype"></a>

enum **InterpolationType**: [🔗](class_animation.md#enum-animation-interpolationtype)

<a id="class-animation-constant-interpolation-nearest"></a>

[InterpolationType](class_animation.md#enum-animation-interpolationtype) **INTERPOLATION_NEAREST** = `0`

No interpolation (nearest value).

<a id="class-animation-constant-interpolation-linear"></a>

[InterpolationType](class_animation.md#enum-animation-interpolationtype) **INTERPOLATION_LINEAR** = `1`

Linear interpolation.

<a id="class-animation-constant-interpolation-cubic"></a>

[InterpolationType](class_animation.md#enum-animation-interpolationtype) **INTERPOLATION_CUBIC** = `2`

Cubic interpolation. This looks smoother than linear interpolation, but is more expensive to interpolate. Stick to [INTERPOLATION_LINEAR](class_animation.md#class-animation-constant-interpolation-linear) for complex 3D animations imported from external software, even if it requires using a higher animation framerate in return.

<a id="class-animation-constant-interpolation-linear-angle"></a>

[InterpolationType](class_animation.md#enum-animation-interpolationtype) **INTERPOLATION_LINEAR_ANGLE** = `3`

Linear interpolation with shortest path rotation.

**Note:** The result value is always normalized and may not match the key value.

<a id="class-animation-constant-interpolation-cubic-angle"></a>

[InterpolationType](class_animation.md#enum-animation-interpolationtype) **INTERPOLATION_CUBIC_ANGLE** = `4`

Cubic interpolation with shortest path rotation.

**Note:** The result value is always normalized and may not match the key value.

---


<a id="enum-animation-updatemode"></a>

enum **UpdateMode**: [🔗](class_animation.md#enum-animation-updatemode)

<a id="class-animation-constant-update-continuous"></a>

[UpdateMode](class_animation.md#enum-animation-updatemode) **UPDATE_CONTINUOUS** = `0`

Update between keyframes and hold the value.

<a id="class-animation-constant-update-discrete"></a>

[UpdateMode](class_animation.md#enum-animation-updatemode) **UPDATE_DISCRETE** = `1`

Update at the keyframes.

<a id="class-animation-constant-update-capture"></a>

[UpdateMode](class_animation.md#enum-animation-updatemode) **UPDATE_CAPTURE** = `2`

Same as [UPDATE_CONTINUOUS](class_animation.md#class-animation-constant-update-continuous) but works as a flag to capture the value of the current object and perform interpolation in some methods. See also [AnimationMixer.capture()](class_animationmixer.md#class-animationmixer-method-capture), [AnimationPlayer.playback_auto_capture](class_animationplayer.md#class-animationplayer-property-playback-auto-capture), and [AnimationPlayer.play_with_capture()](class_animationplayer.md#class-animationplayer-method-play-with-capture).

---


<a id="enum-animation-loopmode"></a>

enum **LoopMode**: [🔗](class_animation.md#enum-animation-loopmode)

<a id="class-animation-constant-loop-none"></a>

[LoopMode](class_animation.md#enum-animation-loopmode) **LOOP_NONE** = `0`

At both ends of the animation, the animation will stop playing.

<a id="class-animation-constant-loop-linear"></a>

[LoopMode](class_animation.md#enum-animation-loopmode) **LOOP_LINEAR** = `1`

At both ends of the animation, the animation will be repeated without changing the playback direction.

<a id="class-animation-constant-loop-pingpong"></a>

[LoopMode](class_animation.md#enum-animation-loopmode) **LOOP_PINGPONG** = `2`

Repeats playback and reverse playback at both ends of the animation.

---


<a id="enum-animation-loopedflag"></a>

enum **LoopedFlag**: [🔗](class_animation.md#enum-animation-loopedflag)

<a id="class-animation-constant-looped-flag-none"></a>

[LoopedFlag](class_animation.md#enum-animation-loopedflag) **LOOPED_FLAG_NONE** = `0`

This flag indicates that the animation proceeds without any looping.

<a id="class-animation-constant-looped-flag-end"></a>

[LoopedFlag](class_animation.md#enum-animation-loopedflag) **LOOPED_FLAG_END** = `1`

This flag indicates that the animation has reached the end of the animation and just after loop processed.

<a id="class-animation-constant-looped-flag-start"></a>

[LoopedFlag](class_animation.md#enum-animation-loopedflag) **LOOPED_FLAG_START** = `2`

This flag indicates that the animation has reached the start of the animation and just after loop processed.

---


<a id="enum-animation-findmode"></a>

enum **FindMode**: [🔗](class_animation.md#enum-animation-findmode)

<a id="class-animation-constant-find-mode-nearest"></a>

[FindMode](class_animation.md#enum-animation-findmode) **FIND_MODE_NEAREST** = `0`

Finds the nearest time key.

<a id="class-animation-constant-find-mode-approx"></a>

[FindMode](class_animation.md#enum-animation-findmode) **FIND_MODE_APPROX** = `1`

Finds only the key with approximating the time.

<a id="class-animation-constant-find-mode-exact"></a>

[FindMode](class_animation.md#enum-animation-findmode) **FIND_MODE_EXACT** = `2`

Finds only the key with matching the time.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-animation-property-capture-included"></a>

[bool](class_bool.md#class-bool) **capture_included** = `false` [🔗](class_animation.md#class-animation-property-capture-included)

- [bool](class_bool.md#class-bool) **is_capture_included**()

Returns `true` if the capture track is included. This is a cached readonly value for performance.

---


<a id="class-animation-property-length"></a>

[float](class_float.md#class-float) **length** = `1.0` [🔗](class_animation.md#class-animation-property-length)

- void **set_length**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_length**()

The total length of the animation (in seconds).

**Note:** Length is not delimited by the last key, as this one may be before or after the end to ensure correct interpolation and looping.

---


<a id="class-animation-property-loop-mode"></a>

[LoopMode](class_animation.md#enum-animation-loopmode) **loop_mode** = `0` [🔗](class_animation.md#class-animation-property-loop-mode)

- void **set_loop_mode**(value: [LoopMode](class_animation.md#enum-animation-loopmode))
- [LoopMode](class_animation.md#enum-animation-loopmode) **get_loop_mode**()

Determines the behavior of both ends of the animation timeline during animation playback. This indicates whether and how the animation should be restarted, and is also used to correctly interpolate animation cycles.

---


<a id="class-animation-property-step"></a>

[float](class_float.md#class-float) **step** = `0.033333335` [🔗](class_animation.md#class-animation-property-step)

- void **set_step**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_step**()

The animation step value.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-animation-method-add-marker"></a>

void **add_marker**(name: [StringName](class_stringname.md#class-stringname), time: [float](class_float.md#class-float)) [🔗](class_animation.md#class-animation-method-add-marker)

Adds a marker to this Animation.

---


<a id="class-animation-method-add-track"></a>

[int](class_int.md#class-int) **add_track**(type: [TrackType](class_animation.md#enum-animation-tracktype), at_position: [int](class_int.md#class-int) = -1) [🔗](class_animation.md#class-animation-method-add-track)

Adds a track to the Animation.

---


<a id="class-animation-method-animation-track-get-key-animation"></a>

[StringName](class_stringname.md#class-stringname) **animation_track_get_key_animation**(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int)) const [🔗](class_animation.md#class-animation-method-animation-track-get-key-animation)

Returns the animation name at the key identified by `key_idx`. The `track_idx` must be the index of an Animation Track.

---


<a id="class-animation-method-animation-track-insert-key"></a>

[int](class_int.md#class-int) **animation_track_insert_key**(track_idx: [int](class_int.md#class-int), time: [float](class_float.md#class-float), animation: [StringName](class_stringname.md#class-stringname)) [🔗](class_animation.md#class-animation-method-animation-track-insert-key)

Inserts a key with value `animation` at the given `time` (in seconds). The `track_idx` must be the index of an Animation Track.

---


<a id="class-animation-method-animation-track-set-key-animation"></a>

void **animation_track_set_key_animation**(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int), animation: [StringName](class_stringname.md#class-stringname)) [🔗](class_animation.md#class-animation-method-animation-track-set-key-animation)

Sets the key identified by `key_idx` to value `animation`. The `track_idx` must be the index of an Animation Track.

---


<a id="class-animation-method-audio-track-get-key-end-offset"></a>

[float](class_float.md#class-float) **audio_track_get_key_end_offset**(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int)) const [🔗](class_animation.md#class-animation-method-audio-track-get-key-end-offset)

Returns the end offset of the key identified by `key_idx`. The `track_idx` must be the index of an Audio Track.

End offset is the number of seconds cut off at the ending of the audio stream.

---


<a id="class-animation-method-audio-track-get-key-start-offset"></a>

[float](class_float.md#class-float) **audio_track_get_key_start_offset**(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int)) const [🔗](class_animation.md#class-animation-method-audio-track-get-key-start-offset)

Returns the start offset of the key identified by `key_idx`. The `track_idx` must be the index of an Audio Track.

Start offset is the number of seconds cut off at the beginning of the audio stream.

---


<a id="class-animation-method-audio-track-get-key-stream"></a>

[Resource](class_resource.md#class-resource) **audio_track_get_key_stream**(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int)) const [🔗](class_animation.md#class-animation-method-audio-track-get-key-stream)

Returns the audio stream of the key identified by `key_idx`. The `track_idx` must be the index of an Audio Track.

---


<a id="class-animation-method-audio-track-insert-key"></a>

[int](class_int.md#class-int) **audio_track_insert_key**(track_idx: [int](class_int.md#class-int), time: [float](class_float.md#class-float), stream: [Resource](class_resource.md#class-resource), start_offset: [float](class_float.md#class-float) = 0, end_offset: [float](class_float.md#class-float) = 0) [🔗](class_animation.md#class-animation-method-audio-track-insert-key)

Inserts an Audio Track key at the given `time` in seconds. The `track_idx` must be the index of an Audio Track.

`stream` is the [AudioStream](class_audiostream.md#class-audiostream) resource to play. `start_offset` is the number of seconds cut off at the beginning of the audio stream, while `end_offset` is at the ending.

---


<a id="class-animation-method-audio-track-is-use-blend"></a>

[bool](class_bool.md#class-bool) **audio_track_is_use_blend**(track_idx: [int](class_int.md#class-int)) const [🔗](class_animation.md#class-animation-method-audio-track-is-use-blend)

Returns `true` if the track at `track_idx` will be blended with other animations.

---


<a id="class-animation-method-audio-track-set-key-end-offset"></a>

void **audio_track_set_key_end_offset**(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int), offset: [float](class_float.md#class-float)) [🔗](class_animation.md#class-animation-method-audio-track-set-key-end-offset)

Sets the end offset of the key identified by `key_idx` to value `offset`. The `track_idx` must be the index of an Audio Track.

---


<a id="class-animation-method-audio-track-set-key-start-offset"></a>

void **audio_track_set_key_start_offset**(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int), offset: [float](class_float.md#class-float)) [🔗](class_animation.md#class-animation-method-audio-track-set-key-start-offset)

Sets the start offset of the key identified by `key_idx` to value `offset`. The `track_idx` must be the index of an Audio Track.

---


<a id="class-animation-method-audio-track-set-key-stream"></a>

void **audio_track_set_key_stream**(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int), stream: [Resource](class_resource.md#class-resource)) [🔗](class_animation.md#class-animation-method-audio-track-set-key-stream)

Sets the stream of the key identified by `key_idx` to value `stream`. The `track_idx` must be the index of an Audio Track.

---


<a id="class-animation-method-audio-track-set-use-blend"></a>

void **audio_track_set_use_blend**(track_idx: [int](class_int.md#class-int), enable: [bool](class_bool.md#class-bool)) [🔗](class_animation.md#class-animation-method-audio-track-set-use-blend)

Sets whether the track will be blended with other animations. If `true`, the audio playback volume changes depending on the blend value.

---


<a id="class-animation-method-bezier-track-get-key-in-handle"></a>

[Vector2](class_vector2.md#class-vector2) **bezier_track_get_key_in_handle**(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int)) const [🔗](class_animation.md#class-animation-method-bezier-track-get-key-in-handle)

Returns the in handle of the key identified by `key_idx`. The `track_idx` must be the index of a Bezier Track.

---


<a id="class-animation-method-bezier-track-get-key-out-handle"></a>

[Vector2](class_vector2.md#class-vector2) **bezier_track_get_key_out_handle**(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int)) const [🔗](class_animation.md#class-animation-method-bezier-track-get-key-out-handle)

Returns the out handle of the key identified by `key_idx`. The `track_idx` must be the index of a Bezier Track.

---


<a id="class-animation-method-bezier-track-get-key-value"></a>

[float](class_float.md#class-float) **bezier_track_get_key_value**(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int)) const [🔗](class_animation.md#class-animation-method-bezier-track-get-key-value)

Returns the value of the key identified by `key_idx`. The `track_idx` must be the index of a Bezier Track.

---


<a id="class-animation-method-bezier-track-insert-key"></a>

[int](class_int.md#class-int) **bezier_track_insert_key**(track_idx: [int](class_int.md#class-int), time: [float](class_float.md#class-float), value: [float](class_float.md#class-float), in_handle: [Vector2](class_vector2.md#class-vector2) = Vector2(0, 0), out_handle: [Vector2](class_vector2.md#class-vector2) = Vector2(0, 0)) [🔗](class_animation.md#class-animation-method-bezier-track-insert-key)

Inserts a Bezier Track key at the given `time` in seconds. The `track_idx` must be the index of a Bezier Track.

`in_handle` is the left-side weight of the added Bezier curve point, `out_handle` is the right-side one, while `value` is the actual value at this point.

---


<a id="class-animation-method-bezier-track-interpolate"></a>

[float](class_float.md#class-float) **bezier_track_interpolate**(track_idx: [int](class_int.md#class-int), time: [float](class_float.md#class-float)) const [🔗](class_animation.md#class-animation-method-bezier-track-interpolate)

Returns the interpolated value at the given `time` (in seconds). The `track_idx` must be the index of a Bezier Track.

---


<a id="class-animation-method-bezier-track-set-key-in-handle"></a>

void **bezier_track_set_key_in_handle**(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int), in_handle: [Vector2](class_vector2.md#class-vector2), balanced_value_time_ratio: [float](class_float.md#class-float) = 1.0) [🔗](class_animation.md#class-animation-method-bezier-track-set-key-in-handle)

Sets the in handle of the key identified by `key_idx` to value `in_handle`. The `track_idx` must be the index of a Bezier Track.

---


<a id="class-animation-method-bezier-track-set-key-out-handle"></a>

void **bezier_track_set_key_out_handle**(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int), out_handle: [Vector2](class_vector2.md#class-vector2), balanced_value_time_ratio: [float](class_float.md#class-float) = 1.0) [🔗](class_animation.md#class-animation-method-bezier-track-set-key-out-handle)

Sets the out handle of the key identified by `key_idx` to value `out_handle`. The `track_idx` must be the index of a Bezier Track.

---


<a id="class-animation-method-bezier-track-set-key-value"></a>

void **bezier_track_set_key_value**(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int), value: [float](class_float.md#class-float)) [🔗](class_animation.md#class-animation-method-bezier-track-set-key-value)

Sets the value of the key identified by `key_idx` to the given value. The `track_idx` must be the index of a Bezier Track.

---


<a id="class-animation-method-blend-shape-track-insert-key"></a>

[int](class_int.md#class-int) **blend_shape_track_insert_key**(track_idx: [int](class_int.md#class-int), time: [float](class_float.md#class-float), amount: [float](class_float.md#class-float)) [🔗](class_animation.md#class-animation-method-blend-shape-track-insert-key)

Inserts a key in a given blend shape track. Returns the key index.

---


<a id="class-animation-method-blend-shape-track-interpolate"></a>

[float](class_float.md#class-float) **blend_shape_track_interpolate**(track_idx: [int](class_int.md#class-int), time_sec: [float](class_float.md#class-float), backward: [bool](class_bool.md#class-bool) = false) const [🔗](class_animation.md#class-animation-method-blend-shape-track-interpolate)

Returns the interpolated blend shape value at the given time (in seconds). The `track_idx` must be the index of a blend shape track.

---


<a id="class-animation-method-clear"></a>

void **clear**() [🔗](class_animation.md#class-animation-method-clear)

Clear the animation (clear all tracks and reset all).

---


<a id="class-animation-method-compress"></a>

void **compress**(page_size: [int](class_int.md#class-int) = 8192, fps: [int](class_int.md#class-int) = 120, split_tolerance: [float](class_float.md#class-float) = 4.0) [🔗](class_animation.md#class-animation-method-compress)

Compress the animation and all its tracks in-place. This will make [track_is_compressed()](class_animation.md#class-animation-method-track-is-compressed) return `true` once called on this **Animation**. Compressed tracks require less memory to be played, and are designed to be used for complex 3D animations (such as cutscenes) imported from external 3D software. Compression is lossy, but the difference is usually not noticeable in real world conditions.

**Note:** Compressed tracks have various limitations (such as not being editable from the editor), so only use compressed animations if you actually need them.

---


<a id="class-animation-method-copy-track"></a>

void **copy_track**(track_idx: [int](class_int.md#class-int), to_animation: [Animation](class_animation.md#class-animation)) [🔗](class_animation.md#class-animation-method-copy-track)

Adds a new track to `to_animation` that is a copy of the given track from this animation.

---


<a id="class-animation-method-find-track"></a>

[int](class_int.md#class-int) **find_track**(path: [NodePath](class_nodepath.md#class-nodepath), type: [TrackType](class_animation.md#enum-animation-tracktype)) const [🔗](class_animation.md#class-animation-method-find-track)

Returns the index of the specified track. If the track is not found, return -1.

---


<a id="class-animation-method-get-marker-at-time"></a>

[StringName](class_stringname.md#class-stringname) **get_marker_at_time**(time: [float](class_float.md#class-float)) const [🔗](class_animation.md#class-animation-method-get-marker-at-time)

Returns the name of the marker located at the given time.

---


<a id="class-animation-method-get-marker-color"></a>

[Color](class_color.md#class-color) **get_marker_color**(name: [StringName](class_stringname.md#class-stringname)) const [🔗](class_animation.md#class-animation-method-get-marker-color)

Returns the given marker's color.

---


<a id="class-animation-method-get-marker-names"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_marker_names**() const [🔗](class_animation.md#class-animation-method-get-marker-names)

Returns every marker in this Animation, sorted ascending by time.

---


<a id="class-animation-method-get-marker-time"></a>

[float](class_float.md#class-float) **get_marker_time**(name: [StringName](class_stringname.md#class-stringname)) const [🔗](class_animation.md#class-animation-method-get-marker-time)

Returns the given marker's time.

---


<a id="class-animation-method-get-next-marker"></a>

[StringName](class_stringname.md#class-stringname) **get_next_marker**(time: [float](class_float.md#class-float)) const [🔗](class_animation.md#class-animation-method-get-next-marker)

Returns the closest marker that comes after the given time. If no such marker exists, an empty string is returned.

---


<a id="class-animation-method-get-prev-marker"></a>

[StringName](class_stringname.md#class-stringname) **get_prev_marker**(time: [float](class_float.md#class-float)) const [🔗](class_animation.md#class-animation-method-get-prev-marker)

Returns the closest marker that comes before the given time. If no such marker exists, an empty string is returned.

---


<a id="class-animation-method-get-track-count"></a>

[int](class_int.md#class-int) **get_track_count**() const [🔗](class_animation.md#class-animation-method-get-track-count)

Returns the amount of tracks in the animation.

---


<a id="class-animation-method-has-marker"></a>

[bool](class_bool.md#class-bool) **has_marker**(name: [StringName](class_stringname.md#class-stringname)) const [🔗](class_animation.md#class-animation-method-has-marker)

Returns `true` if this Animation contains a marker with the given name.

---


<a id="class-animation-method-method-track-get-name"></a>

[StringName](class_stringname.md#class-stringname) **method_track_get_name**(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int)) const [🔗](class_animation.md#class-animation-method-method-track-get-name)

Returns the method name of a method track.

---


<a id="class-animation-method-method-track-get-params"></a>

[Array](class_array.md#class-array) **method_track_get_params**(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int)) const [🔗](class_animation.md#class-animation-method-method-track-get-params)

Returns the arguments values to be called on a method track for a given key in a given track.

---


<a id="class-animation-method-optimize"></a>

void **optimize**(allowed_velocity_err: [float](class_float.md#class-float) = 0.01, allowed_angular_err: [float](class_float.md#class-float) = 0.01, precision: [int](class_int.md#class-int) = 3) [🔗](class_animation.md#class-animation-method-optimize)

Optimize the animation and all its tracks in-place. This will preserve only as many keys as are necessary to keep the animation within the specified bounds.

---


<a id="class-animation-method-position-track-insert-key"></a>

[int](class_int.md#class-int) **position_track_insert_key**(track_idx: [int](class_int.md#class-int), time: [float](class_float.md#class-float), position: [Vector3](class_vector3.md#class-vector3)) [🔗](class_animation.md#class-animation-method-position-track-insert-key)

Inserts a key in a given 3D position track. Returns the key index.

---


<a id="class-animation-method-position-track-interpolate"></a>

[Vector3](class_vector3.md#class-vector3) **position_track_interpolate**(track_idx: [int](class_int.md#class-int), time_sec: [float](class_float.md#class-float), backward: [bool](class_bool.md#class-bool) = false) const [🔗](class_animation.md#class-animation-method-position-track-interpolate)

Returns the interpolated position value at the given time (in seconds). The `track_idx` must be the index of a 3D position track.

---


<a id="class-animation-method-remove-marker"></a>

void **remove_marker**(name: [StringName](class_stringname.md#class-stringname)) [🔗](class_animation.md#class-animation-method-remove-marker)

Removes the marker with the given name from this Animation.

---


<a id="class-animation-method-remove-track"></a>

void **remove_track**(track_idx: [int](class_int.md#class-int)) [🔗](class_animation.md#class-animation-method-remove-track)

Removes a track by specifying the track index.

---


<a id="class-animation-method-rotation-track-insert-key"></a>

[int](class_int.md#class-int) **rotation_track_insert_key**(track_idx: [int](class_int.md#class-int), time: [float](class_float.md#class-float), rotation: [Quaternion](class_quaternion.md#class-quaternion)) [🔗](class_animation.md#class-animation-method-rotation-track-insert-key)

Inserts a key in a given 3D rotation track. Returns the key index.

---


<a id="class-animation-method-rotation-track-interpolate"></a>

[Quaternion](class_quaternion.md#class-quaternion) **rotation_track_interpolate**(track_idx: [int](class_int.md#class-int), time_sec: [float](class_float.md#class-float), backward: [bool](class_bool.md#class-bool) = false) const [🔗](class_animation.md#class-animation-method-rotation-track-interpolate)

Returns the interpolated rotation value at the given time (in seconds). The `track_idx` must be the index of a 3D rotation track.

---


<a id="class-animation-method-scale-track-insert-key"></a>

[int](class_int.md#class-int) **scale_track_insert_key**(track_idx: [int](class_int.md#class-int), time: [float](class_float.md#class-float), scale: [Vector3](class_vector3.md#class-vector3)) [🔗](class_animation.md#class-animation-method-scale-track-insert-key)

Inserts a key in a given 3D scale track. Returns the key index.

---


<a id="class-animation-method-scale-track-interpolate"></a>

[Vector3](class_vector3.md#class-vector3) **scale_track_interpolate**(track_idx: [int](class_int.md#class-int), time_sec: [float](class_float.md#class-float), backward: [bool](class_bool.md#class-bool) = false) const [🔗](class_animation.md#class-animation-method-scale-track-interpolate)

Returns the interpolated scale value at the given time (in seconds). The `track_idx` must be the index of a 3D scale track.

---


<a id="class-animation-method-set-marker-color"></a>

void **set_marker_color**(name: [StringName](class_stringname.md#class-stringname), color: [Color](class_color.md#class-color)) [🔗](class_animation.md#class-animation-method-set-marker-color)

Sets the given marker's color.

---


<a id="class-animation-method-track-find-key"></a>

[int](class_int.md#class-int) **track_find_key**(track_idx: [int](class_int.md#class-int), time: [float](class_float.md#class-float), find_mode: [FindMode](class_animation.md#enum-animation-findmode) = 0, limit: [bool](class_bool.md#class-bool) = false, backward: [bool](class_bool.md#class-bool) = false) const [🔗](class_animation.md#class-animation-method-track-find-key)

Finds the key index by time in a given track. Optionally, only find it if the approx/exact time is given.

If `limit` is `true`, it does not return keys outside the animation range.

If `backward` is `true`, the direction is reversed in methods that rely on one directional processing.

For example, in case `find_mode` is [FIND_MODE_NEAREST](class_animation.md#class-animation-constant-find-mode-nearest), if there is no key in the current position just after seeked, the first key found is retrieved by searching before the position, but if `backward` is `true`, the first key found is retrieved after the position.

---


<a id="class-animation-method-track-get-interpolation-loop-wrap"></a>

[bool](class_bool.md#class-bool) **track_get_interpolation_loop_wrap**(track_idx: [int](class_int.md#class-int)) const [🔗](class_animation.md#class-animation-method-track-get-interpolation-loop-wrap)

Returns `true` if the track at `track_idx` wraps the interpolation loop. New tracks wrap the interpolation loop by default.

---


<a id="class-animation-method-track-get-interpolation-type"></a>

[InterpolationType](class_animation.md#enum-animation-interpolationtype) **track_get_interpolation_type**(track_idx: [int](class_int.md#class-int)) const [🔗](class_animation.md#class-animation-method-track-get-interpolation-type)

Returns the interpolation type of a given track.

---


<a id="class-animation-method-track-get-key-count"></a>

[int](class_int.md#class-int) **track_get_key_count**(track_idx: [int](class_int.md#class-int)) const [🔗](class_animation.md#class-animation-method-track-get-key-count)

Returns the number of keys in a given track.

---


<a id="class-animation-method-track-get-key-time"></a>

[float](class_float.md#class-float) **track_get_key_time**(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int)) const [🔗](class_animation.md#class-animation-method-track-get-key-time)

Returns the time at which the key is located.

---


<a id="class-animation-method-track-get-key-transition"></a>

[float](class_float.md#class-float) **track_get_key_transition**(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int)) const [🔗](class_animation.md#class-animation-method-track-get-key-transition)

Returns the transition curve (easing) for a specific key (see the built-in math function [@GlobalScope.ease()](class_@globalscope.md#class-globalscope-method-ease)).

---


<a id="class-animation-method-track-get-key-value"></a>

[Variant](class_variant.md#class-variant) **track_get_key_value**(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int)) const [🔗](class_animation.md#class-animation-method-track-get-key-value)

Returns the value of a given key in a given track.

---


<a id="class-animation-method-track-get-path"></a>

[NodePath](class_nodepath.md#class-nodepath) **track_get_path**(track_idx: [int](class_int.md#class-int)) const [🔗](class_animation.md#class-animation-method-track-get-path)

Gets the path of a track. For more information on the path format, see [track_set_path()](class_animation.md#class-animation-method-track-set-path).

---


<a id="class-animation-method-track-get-type"></a>

[TrackType](class_animation.md#enum-animation-tracktype) **track_get_type**(track_idx: [int](class_int.md#class-int)) const [🔗](class_animation.md#class-animation-method-track-get-type)

Gets the type of a track.

---


<a id="class-animation-method-track-insert-key"></a>

[int](class_int.md#class-int) **track_insert_key**(track_idx: [int](class_int.md#class-int), time: [float](class_float.md#class-float), key: [Variant](class_variant.md#class-variant), transition: [float](class_float.md#class-float) = 1) [🔗](class_animation.md#class-animation-method-track-insert-key)

Inserts a generic key in a given track. Returns the key index.

---


<a id="class-animation-method-track-is-compressed"></a>

[bool](class_bool.md#class-bool) **track_is_compressed**(track_idx: [int](class_int.md#class-int)) const [🔗](class_animation.md#class-animation-method-track-is-compressed)

Returns `true` if the track is compressed, `false` otherwise. See also [compress()](class_animation.md#class-animation-method-compress).

---


<a id="class-animation-method-track-is-enabled"></a>

[bool](class_bool.md#class-bool) **track_is_enabled**(track_idx: [int](class_int.md#class-int)) const [🔗](class_animation.md#class-animation-method-track-is-enabled)

Returns `true` if the track at index `track_idx` is enabled.

---


<a id="class-animation-method-track-is-imported"></a>

[bool](class_bool.md#class-bool) **track_is_imported**(track_idx: [int](class_int.md#class-int)) const [🔗](class_animation.md#class-animation-method-track-is-imported)

Returns `true` if the given track is imported. Else, return `false`.

---


<a id="class-animation-method-track-move-down"></a>

void **track_move_down**(track_idx: [int](class_int.md#class-int)) [🔗](class_animation.md#class-animation-method-track-move-down)

Moves a track down.

---


<a id="class-animation-method-track-move-to"></a>

void **track_move_to**(track_idx: [int](class_int.md#class-int), to_idx: [int](class_int.md#class-int)) [🔗](class_animation.md#class-animation-method-track-move-to)

Changes the index position of track `track_idx` to the one defined in `to_idx`.

---


<a id="class-animation-method-track-move-up"></a>

void **track_move_up**(track_idx: [int](class_int.md#class-int)) [🔗](class_animation.md#class-animation-method-track-move-up)

Moves a track up.

---


<a id="class-animation-method-track-remove-key"></a>

void **track_remove_key**(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int)) [🔗](class_animation.md#class-animation-method-track-remove-key)

Removes a key by index in a given track.

---


<a id="class-animation-method-track-remove-key-at-time"></a>

void **track_remove_key_at_time**(track_idx: [int](class_int.md#class-int), time: [float](class_float.md#class-float)) [🔗](class_animation.md#class-animation-method-track-remove-key-at-time)

Removes a key at `time` in a given track.

---


<a id="class-animation-method-track-set-enabled"></a>

void **track_set_enabled**(track_idx: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool)) [🔗](class_animation.md#class-animation-method-track-set-enabled)

Enables/disables the given track. Tracks are enabled by default.

---


<a id="class-animation-method-track-set-imported"></a>

void **track_set_imported**(track_idx: [int](class_int.md#class-int), imported: [bool](class_bool.md#class-bool)) [🔗](class_animation.md#class-animation-method-track-set-imported)

Sets the given track as imported or not.

---


<a id="class-animation-method-track-set-interpolation-loop-wrap"></a>

void **track_set_interpolation_loop_wrap**(track_idx: [int](class_int.md#class-int), interpolation: [bool](class_bool.md#class-bool)) [🔗](class_animation.md#class-animation-method-track-set-interpolation-loop-wrap)

If `true`, the track at `track_idx` wraps the interpolation loop.

---


<a id="class-animation-method-track-set-interpolation-type"></a>

void **track_set_interpolation_type**(track_idx: [int](class_int.md#class-int), interpolation: [InterpolationType](class_animation.md#enum-animation-interpolationtype)) [🔗](class_animation.md#class-animation-method-track-set-interpolation-type)

Sets the interpolation type of a given track.

---


<a id="class-animation-method-track-set-key-time"></a>

void **track_set_key_time**(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int), time: [float](class_float.md#class-float)) [🔗](class_animation.md#class-animation-method-track-set-key-time)

Sets the time of an existing key.

---


<a id="class-animation-method-track-set-key-transition"></a>

void **track_set_key_transition**(track_idx: [int](class_int.md#class-int), key_idx: [int](class_int.md#class-int), transition: [float](class_float.md#class-float)) [🔗](class_animation.md#class-animation-method-track-set-key-transition)

Sets the transition curve (easing) for a specific key (see the built-in math function [@GlobalScope.ease()](class_@globalscope.md#class-globalscope-method-ease)).

---


<a id="class-animation-method-track-set-key-value"></a>

void **track_set_key_value**(track_idx: [int](class_int.md#class-int), key: [int](class_int.md#class-int), value: [Variant](class_variant.md#class-variant)) [🔗](class_animation.md#class-animation-method-track-set-key-value)

Sets the value of an existing key.

---


<a id="class-animation-method-track-set-path"></a>

void **track_set_path**(track_idx: [int](class_int.md#class-int), path: [NodePath](class_nodepath.md#class-nodepath)) [🔗](class_animation.md#class-animation-method-track-set-path)

Sets the path of a track. Paths must be valid scene-tree paths to a node and must be specified starting from the [AnimationMixer.root_node](class_animationmixer.md#class-animationmixer-property-root-node) that will reproduce the animation. Tracks that control properties or bones must append their name after the path, separated by `":"`.

For example, `"character/skeleton:ankle"` or `"character/mesh:transform/local"`.

---


<a id="class-animation-method-track-swap"></a>

void **track_swap**(track_idx: [int](class_int.md#class-int), with_idx: [int](class_int.md#class-int)) [🔗](class_animation.md#class-animation-method-track-swap)

Swaps the track `track_idx`'s index position with the track `with_idx`.

---


<a id="class-animation-method-value-track-get-update-mode"></a>

[UpdateMode](class_animation.md#enum-animation-updatemode) **value_track_get_update_mode**(track_idx: [int](class_int.md#class-int)) const [🔗](class_animation.md#class-animation-method-value-track-get-update-mode)

Returns the update mode of a value track.

---


<a id="class-animation-method-value-track-interpolate"></a>

[Variant](class_variant.md#class-variant) **value_track_interpolate**(track_idx: [int](class_int.md#class-int), time_sec: [float](class_float.md#class-float), backward: [bool](class_bool.md#class-bool) = false) const [🔗](class_animation.md#class-animation-method-value-track-interpolate)

Returns the interpolated value at the given time (in seconds). The `track_idx` must be the index of a value track.

A `backward` mainly affects the direction of key retrieval of the track with [UPDATE_DISCRETE](class_animation.md#class-animation-constant-update-discrete) converted by [AnimationMixer.ANIMATION_CALLBACK_MODE_DISCRETE_FORCE_CONTINUOUS](class_animationmixer.md#class-animationmixer-constant-animation-callback-mode-discrete-force-continuous) to match the result with [track_find_key()](class_animation.md#class-animation-method-track-find-key).

---


<a id="class-animation-method-value-track-set-update-mode"></a>

void **value_track_set_update_mode**(track_idx: [int](class_int.md#class-int), mode: [UpdateMode](class_animation.md#enum-animation-updatemode)) [🔗](class_animation.md#class-animation-method-value-track-set-update-mode)

Sets the update mode of a value track.
