> Source: https://docs.godotengine.org/en/4.7/classes/class_animatedtexture.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="animatedtexture"></a>

<a id="class-animatedtexture"></a>

# AnimatedTexture

**Deprecated:** This class does not work properly in current versions and may be removed in the future. There is currently no equivalent workaround.

**Inherits:** [Texture2D](class_texture2d.md#class-texture2d) **<** [Texture](class_texture.md#class-texture) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Proxy texture for simple frame-based animations.

<a id="description"></a>

## Description

**AnimatedTexture** is a resource format for frame-based animations, where multiple textures can be chained automatically with a predefined delay for each frame. Unlike [AnimationPlayer](class_animationplayer.md#class-animationplayer) or [AnimatedSprite2D](class_animatedsprite2d.md#class-animatedsprite2d), it isn't a [Node](class_node.md#class-node), but has the advantage of being usable anywhere a [Texture2D](class_texture2d.md#class-texture2d) resource can be used, e.g. in a [TileSet](class_tileset.md#class-tileset).

The playback of the animation is controlled by the [speed_scale](class_animatedtexture.md#class-animatedtexture-property-speed-scale) property, as well as each frame's duration (see [set_frame_duration()](class_animatedtexture.md#class-animatedtexture-method-set-frame-duration)). The animation loops, i.e. it will restart at frame 0 automatically after playing the last frame.

**AnimatedTexture** currently requires all frame textures to have the same size, otherwise the bigger ones will be cropped to match the smallest one.

**Note:** AnimatedTexture doesn't support using [AtlasTexture](class_atlastexture.md#class-atlastexture)s. Each frame needs to be a separate [Texture2D](class_texture2d.md#class-texture2d).

**Warning:** The current implementation is not efficient for the modern renderers.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [current_frame](class_animatedtexture.md#class-animatedtexture-property-current-frame) |  |
| [int](class_int.md#class-int) | [frames](class_animatedtexture.md#class-animatedtexture-property-frames) | `1` |
| [bool](class_bool.md#class-bool) | [one_shot](class_animatedtexture.md#class-animatedtexture-property-one-shot) | `false` |
| [bool](class_bool.md#class-bool) | [pause](class_animatedtexture.md#class-animatedtexture-property-pause) | `false` |
| [bool](class_bool.md#class-bool) | resource_local_to_scene | `false` (overrides [Resource](class_resource.md#class-resource-property-resource-local-to-scene)) |
| [float](class_float.md#class-float) | [speed_scale](class_animatedtexture.md#class-animatedtexture-property-speed-scale) | `1.0` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [float](class_float.md#class-float) | [get_frame_duration](class_animatedtexture.md#class-animatedtexture-method-get-frame-duration)(frame: [int](class_int.md#class-int)) const |
| [Texture2D](class_texture2d.md#class-texture2d) | [get_frame_texture](class_animatedtexture.md#class-animatedtexture-method-get-frame-texture)(frame: [int](class_int.md#class-int)) const |
| void | [set_frame_duration](class_animatedtexture.md#class-animatedtexture-method-set-frame-duration)(frame: [int](class_int.md#class-int), duration: [float](class_float.md#class-float)) |
| void | [set_frame_texture](class_animatedtexture.md#class-animatedtexture-method-set-frame-texture)(frame: [int](class_int.md#class-int), texture: [Texture2D](class_texture2d.md#class-texture2d)) |

---


<a id="constants"></a>

## Constants

<a id="class-animatedtexture-constant-max-frames"></a>

**MAX_FRAMES** = `256` [🔗](class_animatedtexture.md#class-animatedtexture-constant-max-frames)

The maximum number of frames supported by **AnimatedTexture**. If you need more frames in your animation, use [AnimationPlayer](class_animationplayer.md#class-animationplayer) or [AnimatedSprite2D](class_animatedsprite2d.md#class-animatedsprite2d).

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-animatedtexture-property-current-frame"></a>

[int](class_int.md#class-int) **current_frame** [🔗](class_animatedtexture.md#class-animatedtexture-property-current-frame)

- void **set_current_frame**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_current_frame**()

Sets the currently visible frame of the texture. Setting this frame while playing resets the current frame time, so the newly selected frame plays for its whole configured frame duration.

---


<a id="class-animatedtexture-property-frames"></a>

[int](class_int.md#class-int) **frames** = `1` [🔗](class_animatedtexture.md#class-animatedtexture-property-frames)

- void **set_frames**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_frames**()

Number of frames to use in the animation. While you can create the frames independently with [set_frame_texture()](class_animatedtexture.md#class-animatedtexture-method-set-frame-texture), you need to set this value for the animation to take new frames into account. The maximum number of frames is [MAX_FRAMES](class_animatedtexture.md#class-animatedtexture-constant-max-frames).

---


<a id="class-animatedtexture-property-one-shot"></a>

[bool](class_bool.md#class-bool) **one_shot** = `false` [🔗](class_animatedtexture.md#class-animatedtexture-property-one-shot)

- void **set_one_shot**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_one_shot**()

If `true`, the animation will only play once and will not loop back to the first frame after reaching the end. Note that reaching the end will not set [pause](class_animatedtexture.md#class-animatedtexture-property-pause) to `true`.

---


<a id="class-animatedtexture-property-pause"></a>

[bool](class_bool.md#class-bool) **pause** = `false` [🔗](class_animatedtexture.md#class-animatedtexture-property-pause)

- void **set_pause**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_pause**()

If `true`, the animation will pause where it currently is (i.e. at [current_frame](class_animatedtexture.md#class-animatedtexture-property-current-frame)). The animation will continue from where it was paused when changing this property to `false`.

---


<a id="class-animatedtexture-property-speed-scale"></a>

[float](class_float.md#class-float) **speed_scale** = `1.0` [🔗](class_animatedtexture.md#class-animatedtexture-property-speed-scale)

- void **set_speed_scale**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_speed_scale**()

The animation speed is multiplied by this value. If set to a negative value, the animation is played in reverse.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-animatedtexture-method-get-frame-duration"></a>

[float](class_float.md#class-float) **get_frame_duration**(frame: [int](class_int.md#class-int)) const [🔗](class_animatedtexture.md#class-animatedtexture-method-get-frame-duration)

Returns the given `frame`'s duration, in seconds.

---


<a id="class-animatedtexture-method-get-frame-texture"></a>

[Texture2D](class_texture2d.md#class-texture2d) **get_frame_texture**(frame: [int](class_int.md#class-int)) const [🔗](class_animatedtexture.md#class-animatedtexture-method-get-frame-texture)

Returns the given frame's [Texture2D](class_texture2d.md#class-texture2d).

---


<a id="class-animatedtexture-method-set-frame-duration"></a>

void **set_frame_duration**(frame: [int](class_int.md#class-int), duration: [float](class_float.md#class-float)) [🔗](class_animatedtexture.md#class-animatedtexture-method-set-frame-duration)

Sets the duration of any given `frame`. The final duration is affected by the [speed_scale](class_animatedtexture.md#class-animatedtexture-property-speed-scale). If set to `0`, the frame is skipped during playback.

---


<a id="class-animatedtexture-method-set-frame-texture"></a>

void **set_frame_texture**(frame: [int](class_int.md#class-int), texture: [Texture2D](class_texture2d.md#class-texture2d)) [🔗](class_animatedtexture.md#class-animatedtexture-method-set-frame-texture)

Assigns a [Texture2D](class_texture2d.md#class-texture2d) to the given frame. Frame IDs start at 0, so the first frame has ID 0, and the last frame of the animation has ID [frames](class_animatedtexture.md#class-animatedtexture-property-frames) - 1.

You can define any number of textures up to [MAX_FRAMES](class_animatedtexture.md#class-animatedtexture-constant-max-frames), but keep in mind that only frames from 0 to [frames](class_animatedtexture.md#class-animatedtexture-property-frames) - 1 will be part of the animation.
