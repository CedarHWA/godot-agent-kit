> Source: https://docs.godotengine.org/en/4.7/classes/class_spriteframes.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="spriteframes"></a>

<a id="class-spriteframes"></a>

# SpriteFrames

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Sprite frame library for AnimatedSprite2D and AnimatedSprite3D.

<a id="description"></a>

## Description

Sprite frame library for an [AnimatedSprite2D](class_animatedsprite2d.md#class-animatedsprite2d) or [AnimatedSprite3D](class_animatedsprite3d.md#class-animatedsprite3d) node. Contains frames and animation data for playback.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_animation](class_spriteframes.md#class-spriteframes-method-add-animation)(anim: [StringName](class_stringname.md#class-stringname)) |
| void | [add_frame](class_spriteframes.md#class-spriteframes-method-add-frame)(anim: [StringName](class_stringname.md#class-stringname), texture: [Texture2D](class_texture2d.md#class-texture2d), duration: [float](class_float.md#class-float) = 1.0, at_position: [int](class_int.md#class-int) = -1) |
| void | [clear](class_spriteframes.md#class-spriteframes-method-clear)(anim: [StringName](class_stringname.md#class-stringname)) |
| void | [clear_all](class_spriteframes.md#class-spriteframes-method-clear-all)() |
| void | [duplicate_animation](class_spriteframes.md#class-spriteframes-method-duplicate-animation)(anim_from: [StringName](class_stringname.md#class-stringname), anim_to: [StringName](class_stringname.md#class-stringname)) |
| [bool](class_bool.md#class-bool) | [get_animation_loop](class_spriteframes.md#class-spriteframes-method-get-animation-loop)(anim: [StringName](class_stringname.md#class-stringname)) const |
| [LoopMode](class_spriteframes.md#enum-spriteframes-loopmode) | [get_animation_loop_mode](class_spriteframes.md#class-spriteframes-method-get-animation-loop-mode)(anim: [StringName](class_stringname.md#class-stringname)) const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [get_animation_names](class_spriteframes.md#class-spriteframes-method-get-animation-names)() const |
| [float](class_float.md#class-float) | [get_animation_speed](class_spriteframes.md#class-spriteframes-method-get-animation-speed)(anim: [StringName](class_stringname.md#class-stringname)) const |
| [int](class_int.md#class-int) | [get_frame_count](class_spriteframes.md#class-spriteframes-method-get-frame-count)(anim: [StringName](class_stringname.md#class-stringname)) const |
| [float](class_float.md#class-float) | [get_frame_duration](class_spriteframes.md#class-spriteframes-method-get-frame-duration)(anim: [StringName](class_stringname.md#class-stringname), idx: [int](class_int.md#class-int)) const |
| [Texture2D](class_texture2d.md#class-texture2d) | [get_frame_texture](class_spriteframes.md#class-spriteframes-method-get-frame-texture)(anim: [StringName](class_stringname.md#class-stringname), idx: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [has_animation](class_spriteframes.md#class-spriteframes-method-has-animation)(anim: [StringName](class_stringname.md#class-stringname)) const |
| void | [remove_animation](class_spriteframes.md#class-spriteframes-method-remove-animation)(anim: [StringName](class_stringname.md#class-stringname)) |
| void | [remove_frame](class_spriteframes.md#class-spriteframes-method-remove-frame)(anim: [StringName](class_stringname.md#class-stringname), idx: [int](class_int.md#class-int)) |
| void | [rename_animation](class_spriteframes.md#class-spriteframes-method-rename-animation)(anim: [StringName](class_stringname.md#class-stringname), newname: [StringName](class_stringname.md#class-stringname)) |
| void | [set_animation_loop](class_spriteframes.md#class-spriteframes-method-set-animation-loop)(anim: [StringName](class_stringname.md#class-stringname), loop: [bool](class_bool.md#class-bool)) |
| void | [set_animation_loop_mode](class_spriteframes.md#class-spriteframes-method-set-animation-loop-mode)(anim: [StringName](class_stringname.md#class-stringname), loop_mode: [LoopMode](class_spriteframes.md#enum-spriteframes-loopmode)) |
| void | [set_animation_speed](class_spriteframes.md#class-spriteframes-method-set-animation-speed)(anim: [StringName](class_stringname.md#class-stringname), fps: [float](class_float.md#class-float)) |
| void | [set_frame](class_spriteframes.md#class-spriteframes-method-set-frame)(anim: [StringName](class_stringname.md#class-stringname), idx: [int](class_int.md#class-int), texture: [Texture2D](class_texture2d.md#class-texture2d), duration: [float](class_float.md#class-float) = 1.0) |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-spriteframes-loopmode"></a>

enum **LoopMode**: [🔗](class_spriteframes.md#enum-spriteframes-loopmode)

<a id="class-spriteframes-constant-loop-none"></a>

[LoopMode](class_spriteframes.md#enum-spriteframes-loopmode) **LOOP_NONE** = `0`

The animation plays once and stops when it reaches the end, or the start if played in reverse.

<a id="class-spriteframes-constant-loop-linear"></a>

[LoopMode](class_spriteframes.md#enum-spriteframes-loopmode) **LOOP_LINEAR** = `1`

The animation restarts from the beginning when it reaches the end, or from the end if played in reverse, repeating continuously.

<a id="class-spriteframes-constant-loop-pingpong"></a>

[LoopMode](class_spriteframes.md#enum-spriteframes-loopmode) **LOOP_PINGPONG** = `2`

The animation alternates direction each time it reaches the end or start, playing forward and then in reverse repeatedly.

**Note:** Both [AnimatedSprite2D](class_animatedsprite2d.md#class-animatedsprite2d) and [AnimatedSprite3D](class_animatedsprite3d.md#class-animatedsprite3d) play the first/last frame for its duration only once at each end of the animation loop (instead of twice, once per forward/backward animation direction).

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-spriteframes-method-add-animation"></a>

void **add_animation**(anim: [StringName](class_stringname.md#class-stringname)) [🔗](class_spriteframes.md#class-spriteframes-method-add-animation)

Adds a new `anim` animation to the library.

---


<a id="class-spriteframes-method-add-frame"></a>

void **add_frame**(anim: [StringName](class_stringname.md#class-stringname), texture: [Texture2D](class_texture2d.md#class-texture2d), duration: [float](class_float.md#class-float) = 1.0, at_position: [int](class_int.md#class-int) = -1) [🔗](class_spriteframes.md#class-spriteframes-method-add-frame)

Adds a frame to the `anim` animation. If `at_position` is `-1`, the frame will be added to the end of the animation. `duration` specifies the relative duration, see [get_frame_duration()](class_spriteframes.md#class-spriteframes-method-get-frame-duration) for details.

---


<a id="class-spriteframes-method-clear"></a>

void **clear**(anim: [StringName](class_stringname.md#class-stringname)) [🔗](class_spriteframes.md#class-spriteframes-method-clear)

Removes all frames from the `anim` animation.

---


<a id="class-spriteframes-method-clear-all"></a>

void **clear_all**() [🔗](class_spriteframes.md#class-spriteframes-method-clear-all)

Removes all animations. An empty `default` animation will be created.

---


<a id="class-spriteframes-method-duplicate-animation"></a>

void **duplicate_animation**(anim_from: [StringName](class_stringname.md#class-stringname), anim_to: [StringName](class_stringname.md#class-stringname)) [🔗](class_spriteframes.md#class-spriteframes-method-duplicate-animation)

Duplicates the animation `anim_from` to a new animation named `anim_to`. Fails if `anim_to` already exists, or if `anim_from` does not exist.

---


<a id="class-spriteframes-method-get-animation-loop"></a>

[bool](class_bool.md#class-bool) **get_animation_loop**(anim: [StringName](class_stringname.md#class-stringname)) const [🔗](class_spriteframes.md#class-spriteframes-method-get-animation-loop)

**Deprecated:** Use [get_animation_loop_mode()](class_spriteframes.md#class-spriteframes-method-get-animation-loop-mode) instead.

Returns `true` if `get_animation_loop_mode(anim) == LOOP_LINEAR`. Otherwise, returns `false`.

---


<a id="class-spriteframes-method-get-animation-loop-mode"></a>

[LoopMode](class_spriteframes.md#enum-spriteframes-loopmode) **get_animation_loop_mode**(anim: [StringName](class_stringname.md#class-stringname)) const [🔗](class_spriteframes.md#class-spriteframes-method-get-animation-loop-mode)

Returns the loop mode for the `anim` animation.

---


<a id="class-spriteframes-method-get-animation-names"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_animation_names**() const [🔗](class_spriteframes.md#class-spriteframes-method-get-animation-names)

Returns an array containing the names associated to each animation. Values are placed in alphabetical order.

---


<a id="class-spriteframes-method-get-animation-speed"></a>

[float](class_float.md#class-float) **get_animation_speed**(anim: [StringName](class_stringname.md#class-stringname)) const [🔗](class_spriteframes.md#class-spriteframes-method-get-animation-speed)

Returns the speed in frames per second for the `anim` animation.

---


<a id="class-spriteframes-method-get-frame-count"></a>

[int](class_int.md#class-int) **get_frame_count**(anim: [StringName](class_stringname.md#class-stringname)) const [🔗](class_spriteframes.md#class-spriteframes-method-get-frame-count)

Returns the number of frames for the `anim` animation.

---


<a id="class-spriteframes-method-get-frame-duration"></a>

[float](class_float.md#class-float) **get_frame_duration**(anim: [StringName](class_stringname.md#class-stringname), idx: [int](class_int.md#class-int)) const [🔗](class_spriteframes.md#class-spriteframes-method-get-frame-duration)

Returns a relative duration of the frame `idx` in the `anim` animation (defaults to `1.0`). For example, a frame with a duration of `2.0` is displayed twice as long as a frame with a duration of `1.0`. You can calculate the absolute duration (in seconds) of a frame using the following formula:

```gdscript
absolute_duration = relative_duration / (animation_fps * abs(playing_speed))
```

In this example, `playing_speed` refers to either [AnimatedSprite2D.get_playing_speed()](class_animatedsprite2d.md#class-animatedsprite2d-method-get-playing-speed) or [AnimatedSprite3D.get_playing_speed()](class_animatedsprite3d.md#class-animatedsprite3d-method-get-playing-speed).

---


<a id="class-spriteframes-method-get-frame-texture"></a>

[Texture2D](class_texture2d.md#class-texture2d) **get_frame_texture**(anim: [StringName](class_stringname.md#class-stringname), idx: [int](class_int.md#class-int)) const [🔗](class_spriteframes.md#class-spriteframes-method-get-frame-texture)

Returns the texture of the frame `idx` in the `anim` animation.

---


<a id="class-spriteframes-method-has-animation"></a>

[bool](class_bool.md#class-bool) **has_animation**(anim: [StringName](class_stringname.md#class-stringname)) const [🔗](class_spriteframes.md#class-spriteframes-method-has-animation)

Returns `true` if the `anim` animation exists.

---


<a id="class-spriteframes-method-remove-animation"></a>

void **remove_animation**(anim: [StringName](class_stringname.md#class-stringname)) [🔗](class_spriteframes.md#class-spriteframes-method-remove-animation)

Removes the `anim` animation.

---


<a id="class-spriteframes-method-remove-frame"></a>

void **remove_frame**(anim: [StringName](class_stringname.md#class-stringname), idx: [int](class_int.md#class-int)) [🔗](class_spriteframes.md#class-spriteframes-method-remove-frame)

Removes the `anim` animation's frame `idx`.

---


<a id="class-spriteframes-method-rename-animation"></a>

void **rename_animation**(anim: [StringName](class_stringname.md#class-stringname), newname: [StringName](class_stringname.md#class-stringname)) [🔗](class_spriteframes.md#class-spriteframes-method-rename-animation)

Changes the `anim` animation's name to `newname`.

---


<a id="class-spriteframes-method-set-animation-loop"></a>

void **set_animation_loop**(anim: [StringName](class_stringname.md#class-stringname), loop: [bool](class_bool.md#class-bool)) [🔗](class_spriteframes.md#class-spriteframes-method-set-animation-loop)

**Deprecated:** Use [set_animation_loop_mode()](class_spriteframes.md#class-spriteframes-method-set-animation-loop-mode) instead.

If `loop` is `false` equivalent to `set_animation_loop_mode(LOOP_NONE)`.

If `loop` is `true` equivalent to `set_animation_loop_mode(LOOP_LINEAR)`.

---


<a id="class-spriteframes-method-set-animation-loop-mode"></a>

void **set_animation_loop_mode**(anim: [StringName](class_stringname.md#class-stringname), loop_mode: [LoopMode](class_spriteframes.md#enum-spriteframes-loopmode)) [🔗](class_spriteframes.md#class-spriteframes-method-set-animation-loop-mode)

Sets the `loop_mode` for the `anim` animation.

---


<a id="class-spriteframes-method-set-animation-speed"></a>

void **set_animation_speed**(anim: [StringName](class_stringname.md#class-stringname), fps: [float](class_float.md#class-float)) [🔗](class_spriteframes.md#class-spriteframes-method-set-animation-speed)

Sets the speed for the `anim` animation in frames per second.

---


<a id="class-spriteframes-method-set-frame"></a>

void **set_frame**(anim: [StringName](class_stringname.md#class-stringname), idx: [int](class_int.md#class-int), texture: [Texture2D](class_texture2d.md#class-texture2d), duration: [float](class_float.md#class-float) = 1.0) [🔗](class_spriteframes.md#class-spriteframes-method-set-frame)

Sets the `texture` and the `duration` of the frame `idx` in the `anim` animation. `duration` specifies the relative duration, see [get_frame_duration()](class_spriteframes.md#class-spriteframes-method-get-frame-duration) for details.
