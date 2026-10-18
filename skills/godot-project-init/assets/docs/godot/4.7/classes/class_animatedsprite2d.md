> Source: https://docs.godotengine.org/en/4.7/classes/class_animatedsprite2d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="animatedsprite2d"></a>

<a id="class-animatedsprite2d"></a>

# AnimatedSprite2D

**Inherits:** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Sprite node that contains multiple textures as frames to play for animation.

<a id="description"></a>

## Description

**AnimatedSprite2D** is similar to the [Sprite2D](class_sprite2d.md#class-sprite2d) node, except it carries multiple textures as animation frames. Animations are created using a [SpriteFrames](class_spriteframes.md#class-spriteframes) resource, which allows you to import image files (or a folder containing said files) to provide the animation frames for the sprite. The [SpriteFrames](class_spriteframes.md#class-spriteframes) resource can be configured in the editor via the SpriteFrames bottom panel.

<a id="tutorials"></a>

## Tutorials

- [2D Sprite animation](../tutorials/2d/2d_sprite_animation.md)
- [2D Dodge The Creeps Demo](https://godotengine.org/asset-library/asset/2712)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [StringName](class_stringname.md#class-stringname) | [animation](class_animatedsprite2d.md#class-animatedsprite2d-property-animation) | `&"default"` |
| [String](class_string.md#class-string) | [autoplay](class_animatedsprite2d.md#class-animatedsprite2d-property-autoplay) | `""` |
| [bool](class_bool.md#class-bool) | [centered](class_animatedsprite2d.md#class-animatedsprite2d-property-centered) | `true` |
| [bool](class_bool.md#class-bool) | [flip_h](class_animatedsprite2d.md#class-animatedsprite2d-property-flip-h) | `false` |
| [bool](class_bool.md#class-bool) | [flip_v](class_animatedsprite2d.md#class-animatedsprite2d-property-flip-v) | `false` |
| [int](class_int.md#class-int) | [frame](class_animatedsprite2d.md#class-animatedsprite2d-property-frame) | `0` |
| [float](class_float.md#class-float) | [frame_progress](class_animatedsprite2d.md#class-animatedsprite2d-property-frame-progress) | `0.0` |
| [Vector2](class_vector2.md#class-vector2) | [offset](class_animatedsprite2d.md#class-animatedsprite2d-property-offset) | `Vector2(0, 0)` |
| [float](class_float.md#class-float) | [speed_scale](class_animatedsprite2d.md#class-animatedsprite2d-property-speed-scale) | `1.0` |
| [SpriteFrames](class_spriteframes.md#class-spriteframes) | [sprite_frames](class_animatedsprite2d.md#class-animatedsprite2d-property-sprite-frames) |  |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [float](class_float.md#class-float) | [get_playing_speed](class_animatedsprite2d.md#class-animatedsprite2d-method-get-playing-speed)() const |
| [bool](class_bool.md#class-bool) | [is_playing](class_animatedsprite2d.md#class-animatedsprite2d-method-is-playing)() const |
| void | [pause](class_animatedsprite2d.md#class-animatedsprite2d-method-pause)() |
| void | [play](class_animatedsprite2d.md#class-animatedsprite2d-method-play)(name: [StringName](class_stringname.md#class-stringname) = &"", custom_speed: [float](class_float.md#class-float) = 1.0, from_end: [bool](class_bool.md#class-bool) = false) |
| void | [play_backwards](class_animatedsprite2d.md#class-animatedsprite2d-method-play-backwards)(name: [StringName](class_stringname.md#class-stringname) = &"") |
| void | [set_frame_and_progress](class_animatedsprite2d.md#class-animatedsprite2d-method-set-frame-and-progress)(frame: [int](class_int.md#class-int), progress: [float](class_float.md#class-float)) |
| void | [stop](class_animatedsprite2d.md#class-animatedsprite2d-method-stop)() |

---


<a id="signals"></a>

## Signals

<a id="class-animatedsprite2d-signal-animation-changed"></a>

**animation_changed**() [🔗](class_animatedsprite2d.md#class-animatedsprite2d-signal-animation-changed)

Emitted when [animation](class_animatedsprite2d.md#class-animatedsprite2d-property-animation) changes.

---


<a id="class-animatedsprite2d-signal-animation-finished"></a>

**animation_finished**() [🔗](class_animatedsprite2d.md#class-animatedsprite2d-signal-animation-finished)

Emitted when the animation reaches the end, or the start if it is played in reverse. When the animation finishes, it pauses the playback.

**Note:** This signal is not emitted if an animation is looping.

---


<a id="class-animatedsprite2d-signal-animation-looped"></a>

**animation_looped**() [🔗](class_animatedsprite2d.md#class-animatedsprite2d-signal-animation-looped)

Emitted when the animation loops.

---


<a id="class-animatedsprite2d-signal-frame-changed"></a>

**frame_changed**() [🔗](class_animatedsprite2d.md#class-animatedsprite2d-signal-frame-changed)

Emitted when [frame](class_animatedsprite2d.md#class-animatedsprite2d-property-frame) changes.

---


<a id="class-animatedsprite2d-signal-sprite-frames-changed"></a>

**sprite_frames_changed**() [🔗](class_animatedsprite2d.md#class-animatedsprite2d-signal-sprite-frames-changed)

Emitted when [sprite_frames](class_animatedsprite2d.md#class-animatedsprite2d-property-sprite-frames) changes.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-animatedsprite2d-property-animation"></a>

[StringName](class_stringname.md#class-stringname) **animation** = `&"default"` [🔗](class_animatedsprite2d.md#class-animatedsprite2d-property-animation)

- void **set_animation**(value: [StringName](class_stringname.md#class-stringname))
- [StringName](class_stringname.md#class-stringname) **get_animation**()

The current animation from the [sprite_frames](class_animatedsprite2d.md#class-animatedsprite2d-property-sprite-frames) resource. If this value is changed, the [frame](class_animatedsprite2d.md#class-animatedsprite2d-property-frame) counter and the [frame_progress](class_animatedsprite2d.md#class-animatedsprite2d-property-frame-progress) are reset.

---


<a id="class-animatedsprite2d-property-autoplay"></a>

[String](class_string.md#class-string) **autoplay** = `""` [🔗](class_animatedsprite2d.md#class-animatedsprite2d-property-autoplay)

- void **set_autoplay**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_autoplay**()

The key of the animation to play when the scene loads.

---


<a id="class-animatedsprite2d-property-centered"></a>

[bool](class_bool.md#class-bool) **centered** = `true` [🔗](class_animatedsprite2d.md#class-animatedsprite2d-property-centered)

- void **set_centered**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_centered**()

If `true`, texture will be centered.

**Note:** For games with a pixel art aesthetic, textures may appear deformed when centered. This is caused by their position being between pixels. To prevent this, set this property to `false`, or consider enabling [ProjectSettings.rendering/2d/snap/snap_2d_vertices_to_pixel](class_projectsettings.md#class-projectsettings-property-rendering-2d-snap-snap-2d-vertices-to-pixel) and [ProjectSettings.rendering/2d/snap/snap_2d_transforms_to_pixel](class_projectsettings.md#class-projectsettings-property-rendering-2d-snap-snap-2d-transforms-to-pixel).

---


<a id="class-animatedsprite2d-property-flip-h"></a>

[bool](class_bool.md#class-bool) **flip_h** = `false` [🔗](class_animatedsprite2d.md#class-animatedsprite2d-property-flip-h)

- void **set_flip_h**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_flipped_h**()

If `true`, texture is flipped horizontally.

---


<a id="class-animatedsprite2d-property-flip-v"></a>

[bool](class_bool.md#class-bool) **flip_v** = `false` [🔗](class_animatedsprite2d.md#class-animatedsprite2d-property-flip-v)

- void **set_flip_v**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_flipped_v**()

If `true`, texture is flipped vertically.

---


<a id="class-animatedsprite2d-property-frame"></a>

[int](class_int.md#class-int) **frame** = `0` [🔗](class_animatedsprite2d.md#class-animatedsprite2d-property-frame)

- void **set_frame**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_frame**()

The displayed animation frame's index. Setting this property also resets [frame_progress](class_animatedsprite2d.md#class-animatedsprite2d-property-frame-progress). If this is not desired, use [set_frame_and_progress()](class_animatedsprite2d.md#class-animatedsprite2d-method-set-frame-and-progress).

---


<a id="class-animatedsprite2d-property-frame-progress"></a>

[float](class_float.md#class-float) **frame_progress** = `0.0` [🔗](class_animatedsprite2d.md#class-animatedsprite2d-property-frame-progress)

- void **set_frame_progress**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_frame_progress**()

The progress value between `0.0` and `1.0` until the current frame transitions to the next frame. If the animation is playing backwards, the value transitions from `1.0` to `0.0`.

---


<a id="class-animatedsprite2d-property-offset"></a>

[Vector2](class_vector2.md#class-vector2) **offset** = `Vector2(0, 0)` [🔗](class_animatedsprite2d.md#class-animatedsprite2d-property-offset)

- void **set_offset**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_offset**()

The texture's drawing offset.

---


<a id="class-animatedsprite2d-property-speed-scale"></a>

[float](class_float.md#class-float) **speed_scale** = `1.0` [🔗](class_animatedsprite2d.md#class-animatedsprite2d-property-speed-scale)

- void **set_speed_scale**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_speed_scale**()

The speed scaling ratio. For example, if this value is `1`, then the animation plays at normal speed. If it's `0.5`, then it plays at half speed. If it's `2`, then it plays at double speed.

If set to a negative value, the animation is played in reverse. If set to `0`, the animation will not advance.

---


<a id="class-animatedsprite2d-property-sprite-frames"></a>

[SpriteFrames](class_spriteframes.md#class-spriteframes) **sprite_frames** [🔗](class_animatedsprite2d.md#class-animatedsprite2d-property-sprite-frames)

- void **set_sprite_frames**(value: [SpriteFrames](class_spriteframes.md#class-spriteframes))
- [SpriteFrames](class_spriteframes.md#class-spriteframes) **get_sprite_frames**()

The [SpriteFrames](class_spriteframes.md#class-spriteframes) resource containing the animation(s). Allows you the option to load, edit, clear, make unique and save the states of the [SpriteFrames](class_spriteframes.md#class-spriteframes) resource.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-animatedsprite2d-method-get-playing-speed"></a>

[float](class_float.md#class-float) **get_playing_speed**() const [🔗](class_animatedsprite2d.md#class-animatedsprite2d-method-get-playing-speed)

Returns the actual playing speed of current animation or `0` if not playing. This speed is the [speed_scale](class_animatedsprite2d.md#class-animatedsprite2d-property-speed-scale) property multiplied by `custom_speed` argument specified when calling the [play()](class_animatedsprite2d.md#class-animatedsprite2d-method-play) method.

Returns a negative value if the current animation is playing backwards.

---


<a id="class-animatedsprite2d-method-is-playing"></a>

[bool](class_bool.md#class-bool) **is_playing**() const [🔗](class_animatedsprite2d.md#class-animatedsprite2d-method-is-playing)

Returns `true` if an animation is currently playing (even if [speed_scale](class_animatedsprite2d.md#class-animatedsprite2d-property-speed-scale) and/or `custom_speed` are `0`).

---


<a id="class-animatedsprite2d-method-pause"></a>

void **pause**() [🔗](class_animatedsprite2d.md#class-animatedsprite2d-method-pause)

Pauses the currently playing animation. The [frame](class_animatedsprite2d.md#class-animatedsprite2d-property-frame) and [frame_progress](class_animatedsprite2d.md#class-animatedsprite2d-property-frame-progress) will be kept and calling [play()](class_animatedsprite2d.md#class-animatedsprite2d-method-play) or [play_backwards()](class_animatedsprite2d.md#class-animatedsprite2d-method-play-backwards) without arguments will resume the animation from the current playback position.

See also [stop()](class_animatedsprite2d.md#class-animatedsprite2d-method-stop).

---


<a id="class-animatedsprite2d-method-play"></a>

void **play**(name: [StringName](class_stringname.md#class-stringname) = &"", custom_speed: [float](class_float.md#class-float) = 1.0, from_end: [bool](class_bool.md#class-bool) = false) [🔗](class_animatedsprite2d.md#class-animatedsprite2d-method-play)

Plays the animation with key `name`. If `custom_speed` is negative and `from_end` is `true`, the animation will play backwards (which is equivalent to calling [play_backwards()](class_animatedsprite2d.md#class-animatedsprite2d-method-play-backwards)).

If this method is called with that same animation `name`, or with no `name` parameter, the assigned animation will resume playing if it was paused.

---


<a id="class-animatedsprite2d-method-play-backwards"></a>

void **play_backwards**(name: [StringName](class_stringname.md#class-stringname) = &"") [🔗](class_animatedsprite2d.md#class-animatedsprite2d-method-play-backwards)

Plays the animation with key `name` in reverse.

This method is a shorthand for [play()](class_animatedsprite2d.md#class-animatedsprite2d-method-play) with `custom_speed = -1.0` and `from_end = true`, so see its description for more information.

---


<a id="class-animatedsprite2d-method-set-frame-and-progress"></a>

void **set_frame_and_progress**(frame: [int](class_int.md#class-int), progress: [float](class_float.md#class-float)) [🔗](class_animatedsprite2d.md#class-animatedsprite2d-method-set-frame-and-progress)

Sets [frame](class_animatedsprite2d.md#class-animatedsprite2d-property-frame) and [frame_progress](class_animatedsprite2d.md#class-animatedsprite2d-property-frame-progress) to the given values. Unlike setting [frame](class_animatedsprite2d.md#class-animatedsprite2d-property-frame), this method does not reset the [frame_progress](class_animatedsprite2d.md#class-animatedsprite2d-property-frame-progress) to `0.0` implicitly.

**Example:** Change the animation while keeping the same [frame](class_animatedsprite2d.md#class-animatedsprite2d-property-frame) and [frame_progress](class_animatedsprite2d.md#class-animatedsprite2d-property-frame-progress):

```gdscript
var current_frame = animated_sprite.get_frame()
var current_progress = animated_sprite.get_frame_progress()
animated_sprite.play("walk_another_skin")
animated_sprite.set_frame_and_progress(current_frame, current_progress)
```

---


<a id="class-animatedsprite2d-method-stop"></a>

void **stop**() [🔗](class_animatedsprite2d.md#class-animatedsprite2d-method-stop)

Stops the currently playing animation. The animation position is reset to `0` and the `custom_speed` is reset to `1.0`. See also [pause()](class_animatedsprite2d.md#class-animatedsprite2d-method-pause).
