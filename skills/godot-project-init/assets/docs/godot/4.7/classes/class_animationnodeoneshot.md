> Source: https://docs.godotengine.org/en/4.7/classes/class_animationnodeoneshot.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="animationnodeoneshot"></a>

<a id="class-animationnodeoneshot"></a>

# AnimationNodeOneShot

**Inherits:** [AnimationNodeSync](class_animationnodesync.md#class-animationnodesync) **<** [AnimationNode](class_animationnode.md#class-animationnode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Plays an animation once in an [AnimationNodeBlendTree](class_animationnodeblendtree.md#class-animationnodeblendtree).

<a id="description"></a>

## Description

A resource to add to an [AnimationNodeBlendTree](class_animationnodeblendtree.md#class-animationnodeblendtree). This animation node will execute a sub-animation and return once it finishes. Blend times for fading in and out can be customized, as well as filters.

After setting the request and changing the animation playback, the one-shot node automatically clears the request on the next process frame by setting its `request` value to [ONE_SHOT_REQUEST_NONE](class_animationnodeoneshot.md#class-animationnodeoneshot-constant-one-shot-request-none).

```gdscript
# Play child animation connected to "shot" port.
animation_tree.set("parameters/OneShot/request", AnimationNodeOneShot.ONE_SHOT_REQUEST_FIRE)
# Alternative syntax (same result as above).
animation_tree["parameters/OneShot/request"] = AnimationNodeOneShot.ONE_SHOT_REQUEST_FIRE

# Abort child animation connected to "shot" port.
animation_tree.set("parameters/OneShot/request", AnimationNodeOneShot.ONE_SHOT_REQUEST_ABORT)
# Alternative syntax (same result as above).
animation_tree["parameters/OneShot/request"] = AnimationNodeOneShot.ONE_SHOT_REQUEST_ABORT

# Abort child animation with fading out connected to "shot" port.
animation_tree.set("parameters/OneShot/request", AnimationNodeOneShot.ONE_SHOT_REQUEST_FADE_OUT)
# Alternative syntax (same result as above).
animation_tree["parameters/OneShot/request"] = AnimationNodeOneShot.ONE_SHOT_REQUEST_FADE_OUT

# Get current state (read-only).
animation_tree.get("parameters/OneShot/active")
# Alternative syntax (same result as above).
animation_tree["parameters/OneShot/active"]

# Get current internal state (read-only).
animation_tree.get("parameters/OneShot/internal_active")
# Alternative syntax (same result as above).
animation_tree["parameters/OneShot/internal_active"]
```

```csharp
// Play child animation connected to "shot" port.
animationTree.Set("parameters/OneShot/request", (int)AnimationNodeOneShot.OneShotRequest.Fire);

// Abort child animation connected to "shot" port.
animationTree.Set("parameters/OneShot/request", (int)AnimationNodeOneShot.OneShotRequest.Abort);

// Abort child animation with fading out connected to "shot" port.
animationTree.Set("parameters/OneShot/request", (int)AnimationNodeOneShot.OneShotRequest.FadeOut);

// Get current state (read-only).
animationTree.Get("parameters/OneShot/active");

// Get current internal state (read-only).
animationTree.Get("parameters/OneShot/internal_active");
```

<a id="tutorials"></a>

## Tutorials

- [Using AnimationTree](../tutorials/animation/animation_tree.md)
- [Third Person Shooter (TPS) Demo](https://godotengine.org/asset-library/asset/2710)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [abort_on_reset](class_animationnodeoneshot.md#class-animationnodeoneshot-property-abort-on-reset) | `false` |
| [bool](class_bool.md#class-bool) | [autorestart](class_animationnodeoneshot.md#class-animationnodeoneshot-property-autorestart) | `false` |
| [float](class_float.md#class-float) | [autorestart_delay](class_animationnodeoneshot.md#class-animationnodeoneshot-property-autorestart-delay) | `1.0` |
| [float](class_float.md#class-float) | [autorestart_random_delay](class_animationnodeoneshot.md#class-animationnodeoneshot-property-autorestart-random-delay) | `0.0` |
| [bool](class_bool.md#class-bool) | [break_loop_at_end](class_animationnodeoneshot.md#class-animationnodeoneshot-property-break-loop-at-end) | `false` |
| [Curve](class_curve.md#class-curve) | [fadein_curve](class_animationnodeoneshot.md#class-animationnodeoneshot-property-fadein-curve) |  |
| [float](class_float.md#class-float) | [fadein_time](class_animationnodeoneshot.md#class-animationnodeoneshot-property-fadein-time) | `0.0` |
| [Curve](class_curve.md#class-curve) | [fadeout_curve](class_animationnodeoneshot.md#class-animationnodeoneshot-property-fadeout-curve) |  |
| [float](class_float.md#class-float) | [fadeout_time](class_animationnodeoneshot.md#class-animationnodeoneshot-property-fadeout-time) | `0.0` |
| [MixMode](class_animationnodeoneshot.md#enum-animationnodeoneshot-mixmode) | [mix_mode](class_animationnodeoneshot.md#class-animationnodeoneshot-property-mix-mode) | `0` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-animationnodeoneshot-oneshotrequest"></a>

enum **OneShotRequest**: [🔗](class_animationnodeoneshot.md#enum-animationnodeoneshot-oneshotrequest)

<a id="class-animationnodeoneshot-constant-one-shot-request-none"></a>

[OneShotRequest](class_animationnodeoneshot.md#enum-animationnodeoneshot-oneshotrequest) **ONE_SHOT_REQUEST_NONE** = `0`

The default state of the request. Nothing is done.

<a id="class-animationnodeoneshot-constant-one-shot-request-fire"></a>

[OneShotRequest](class_animationnodeoneshot.md#enum-animationnodeoneshot-oneshotrequest) **ONE_SHOT_REQUEST_FIRE** = `1`

The request to play the animation connected to "shot" port.

<a id="class-animationnodeoneshot-constant-one-shot-request-abort"></a>

[OneShotRequest](class_animationnodeoneshot.md#enum-animationnodeoneshot-oneshotrequest) **ONE_SHOT_REQUEST_ABORT** = `2`

The request to stop the animation connected to "shot" port.

<a id="class-animationnodeoneshot-constant-one-shot-request-fade-out"></a>

[OneShotRequest](class_animationnodeoneshot.md#enum-animationnodeoneshot-oneshotrequest) **ONE_SHOT_REQUEST_FADE_OUT** = `3`

The request to fade out the animation connected to "shot" port.

---


<a id="enum-animationnodeoneshot-mixmode"></a>

enum **MixMode**: [🔗](class_animationnodeoneshot.md#enum-animationnodeoneshot-mixmode)

<a id="class-animationnodeoneshot-constant-mix-mode-blend"></a>

[MixMode](class_animationnodeoneshot.md#enum-animationnodeoneshot-mixmode) **MIX_MODE_BLEND** = `0`

Blends two animations. See also [AnimationNodeBlend2](class_animationnodeblend2.md#class-animationnodeblend2).

<a id="class-animationnodeoneshot-constant-mix-mode-add"></a>

[MixMode](class_animationnodeoneshot.md#enum-animationnodeoneshot-mixmode) **MIX_MODE_ADD** = `1`

Blends two animations additively. See also [AnimationNodeAdd2](class_animationnodeadd2.md#class-animationnodeadd2).

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-animationnodeoneshot-property-abort-on-reset"></a>

[bool](class_bool.md#class-bool) **abort_on_reset** = `false` [🔗](class_animationnodeoneshot.md#class-animationnodeoneshot-property-abort-on-reset)

- void **set_abort_on_reset**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_aborted_on_reset**()

If `true`, the sub-animation will abort if resumed with a reset after a prior interruption.

---


<a id="class-animationnodeoneshot-property-autorestart"></a>

[bool](class_bool.md#class-bool) **autorestart** = `false` [🔗](class_animationnodeoneshot.md#class-animationnodeoneshot-property-autorestart)

- void **set_autorestart**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **has_autorestart**()

If `true`, the sub-animation will restart automatically after finishing.

In other words, to start auto restarting, the animation must be played once with the [ONE_SHOT_REQUEST_FIRE](class_animationnodeoneshot.md#class-animationnodeoneshot-constant-one-shot-request-fire) request. The [ONE_SHOT_REQUEST_ABORT](class_animationnodeoneshot.md#class-animationnodeoneshot-constant-one-shot-request-abort) request stops the auto restarting, but it does not disable the [autorestart](class_animationnodeoneshot.md#class-animationnodeoneshot-property-autorestart) itself. So, the [ONE_SHOT_REQUEST_FIRE](class_animationnodeoneshot.md#class-animationnodeoneshot-constant-one-shot-request-fire) request will start auto restarting again.

---


<a id="class-animationnodeoneshot-property-autorestart-delay"></a>

[float](class_float.md#class-float) **autorestart_delay** = `1.0` [🔗](class_animationnodeoneshot.md#class-animationnodeoneshot-property-autorestart-delay)

- void **set_autorestart_delay**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_autorestart_delay**()

The delay after which the automatic restart is triggered, in seconds.

---


<a id="class-animationnodeoneshot-property-autorestart-random-delay"></a>

[float](class_float.md#class-float) **autorestart_random_delay** = `0.0` [🔗](class_animationnodeoneshot.md#class-animationnodeoneshot-property-autorestart-random-delay)

- void **set_autorestart_random_delay**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_autorestart_random_delay**()

If [autorestart](class_animationnodeoneshot.md#class-animationnodeoneshot-property-autorestart) is `true`, a random additional delay (in seconds) between 0 and this value will be added to [autorestart_delay](class_animationnodeoneshot.md#class-animationnodeoneshot-property-autorestart-delay).

---


<a id="class-animationnodeoneshot-property-break-loop-at-end"></a>

[bool](class_bool.md#class-bool) **break_loop_at_end** = `false` [🔗](class_animationnodeoneshot.md#class-animationnodeoneshot-property-break-loop-at-end)

- void **set_break_loop_at_end**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_loop_broken_at_end**()

If `true`, breaks the loop at the end of the loop cycle for transition, even if the animation is looping.

---


<a id="class-animationnodeoneshot-property-fadein-curve"></a>

[Curve](class_curve.md#class-curve) **fadein_curve** [🔗](class_animationnodeoneshot.md#class-animationnodeoneshot-property-fadein-curve)

- void **set_fadein_curve**(value: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_fadein_curve**()

Determines how cross-fading between animations is eased. If empty, the transition will be linear. Should be a unit [Curve](class_curve.md#class-curve).

---


<a id="class-animationnodeoneshot-property-fadein-time"></a>

[float](class_float.md#class-float) **fadein_time** = `0.0` [🔗](class_animationnodeoneshot.md#class-animationnodeoneshot-property-fadein-time)

- void **set_fadein_time**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_fadein_time**()

The fade-in duration. For example, setting this to `1.0` for a 5 second length animation will produce a cross-fade that starts at 0 second and ends at 1 second during the animation.

**Note:** **AnimationNodeOneShot** transitions the current state after the fading has finished.

---


<a id="class-animationnodeoneshot-property-fadeout-curve"></a>

[Curve](class_curve.md#class-curve) **fadeout_curve** [🔗](class_animationnodeoneshot.md#class-animationnodeoneshot-property-fadeout-curve)

- void **set_fadeout_curve**(value: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_fadeout_curve**()

Determines how cross-fading between animations is eased. If empty, the transition will be linear. Should be a unit [Curve](class_curve.md#class-curve).

---


<a id="class-animationnodeoneshot-property-fadeout-time"></a>

[float](class_float.md#class-float) **fadeout_time** = `0.0` [🔗](class_animationnodeoneshot.md#class-animationnodeoneshot-property-fadeout-time)

- void **set_fadeout_time**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_fadeout_time**()

The fade-out duration. For example, setting this to `1.0` for a 5 second length animation will produce a cross-fade that starts at 4 second and ends at 5 second during the animation.

**Note:** **AnimationNodeOneShot** transitions the current state after the fading has finished.

---


<a id="class-animationnodeoneshot-property-mix-mode"></a>

[MixMode](class_animationnodeoneshot.md#enum-animationnodeoneshot-mixmode) **mix_mode** = `0` [🔗](class_animationnodeoneshot.md#class-animationnodeoneshot-property-mix-mode)

- void **set_mix_mode**(value: [MixMode](class_animationnodeoneshot.md#enum-animationnodeoneshot-mixmode))
- [MixMode](class_animationnodeoneshot.md#enum-animationnodeoneshot-mixmode) **get_mix_mode**()

The blend type.
