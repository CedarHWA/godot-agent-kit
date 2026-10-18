> Source: https://docs.godotengine.org/en/4.7/classes/class_audiolistener3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="audiolistener3d"></a>

<a id="class-audiolistener3d"></a>

# AudioListener3D

**Inherits:** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Overrides the location sounds are heard from.

<a id="description"></a>

## Description

Once added to the scene tree and enabled using [make_current()](class_audiolistener3d.md#class-audiolistener3d-method-make-current), this node will override the location sounds are heard from. This can be used to listen from a location different from the [Camera3D](class_camera3d.md#class-camera3d).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [DopplerTracking](class_audiolistener3d.md#enum-audiolistener3d-dopplertracking) | [doppler_tracking](class_audiolistener3d.md#class-audiolistener3d-property-doppler-tracking) | `0` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [clear_current](class_audiolistener3d.md#class-audiolistener3d-method-clear-current)() |
| [Transform3D](class_transform3d.md#class-transform3d) | [get_listener_transform](class_audiolistener3d.md#class-audiolistener3d-method-get-listener-transform)() const |
| [bool](class_bool.md#class-bool) | [is_current](class_audiolistener3d.md#class-audiolistener3d-method-is-current)() const |
| void | [make_current](class_audiolistener3d.md#class-audiolistener3d-method-make-current)() |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-audiolistener3d-dopplertracking"></a>

enum **DopplerTracking**: [🔗](class_audiolistener3d.md#enum-audiolistener3d-dopplertracking)

<a id="class-audiolistener3d-constant-doppler-tracking-disabled"></a>

[DopplerTracking](class_audiolistener3d.md#enum-audiolistener3d-dopplertracking) **DOPPLER_TRACKING_DISABLED** = `0`

Disables [Doppler effect](https://en.wikipedia.org/wiki/Doppler_effect) simulation (default).

<a id="class-audiolistener3d-constant-doppler-tracking-idle-step"></a>

[DopplerTracking](class_audiolistener3d.md#enum-audiolistener3d-dopplertracking) **DOPPLER_TRACKING_IDLE_STEP** = `1`

Simulate [Doppler effect](https://en.wikipedia.org/wiki/Doppler_effect) by tracking positions of objects that are changed in `_process`. Changes in the relative velocity of this listener compared to those objects affect how audio is perceived (changing the audio's [AudioStreamPlayer3D.pitch_scale](class_audiostreamplayer3d.md#class-audiostreamplayer3d-property-pitch-scale)).

<a id="class-audiolistener3d-constant-doppler-tracking-physics-step"></a>

[DopplerTracking](class_audiolistener3d.md#enum-audiolistener3d-dopplertracking) **DOPPLER_TRACKING_PHYSICS_STEP** = `2`

Simulate [Doppler effect](https://en.wikipedia.org/wiki/Doppler_effect) by tracking positions of objects that are changed in `_physics_process`. Changes in the relative velocity of this listener compared to those objects affect how audio is perceived (changing the audio's [AudioStreamPlayer3D.pitch_scale](class_audiostreamplayer3d.md#class-audiostreamplayer3d-property-pitch-scale)).

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-audiolistener3d-property-doppler-tracking"></a>

[DopplerTracking](class_audiolistener3d.md#enum-audiolistener3d-dopplertracking) **doppler_tracking** = `0` [🔗](class_audiolistener3d.md#class-audiolistener3d-property-doppler-tracking)

- void **set_doppler_tracking**(value: [DopplerTracking](class_audiolistener3d.md#enum-audiolistener3d-dopplertracking))
- [DopplerTracking](class_audiolistener3d.md#enum-audiolistener3d-dopplertracking) **get_doppler_tracking**()

If not [DOPPLER_TRACKING_DISABLED](class_audiolistener3d.md#class-audiolistener3d-constant-doppler-tracking-disabled), this listener will simulate the [Doppler effect](https://en.wikipedia.org/wiki/Doppler_effect) for objects changed in particular `_process` methods.

**Note:** The Doppler effect will only be heard on [AudioStreamPlayer3D](class_audiostreamplayer3d.md#class-audiostreamplayer3d)s if [AudioStreamPlayer3D.doppler_tracking](class_audiostreamplayer3d.md#class-audiostreamplayer3d-property-doppler-tracking) is not set to [AudioStreamPlayer3D.DOPPLER_TRACKING_DISABLED](class_audiostreamplayer3d.md#class-audiostreamplayer3d-constant-doppler-tracking-disabled).

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-audiolistener3d-method-clear-current"></a>

void **clear_current**() [🔗](class_audiolistener3d.md#class-audiolistener3d-method-clear-current)

Disables the listener to use the current camera's listener instead.

---


<a id="class-audiolistener3d-method-get-listener-transform"></a>

[Transform3D](class_transform3d.md#class-transform3d) **get_listener_transform**() const [🔗](class_audiolistener3d.md#class-audiolistener3d-method-get-listener-transform)

Returns the listener's global orthonormalized [Transform3D](class_transform3d.md#class-transform3d).

---


<a id="class-audiolistener3d-method-is-current"></a>

[bool](class_bool.md#class-bool) **is_current**() const [🔗](class_audiolistener3d.md#class-audiolistener3d-method-is-current)

Returns `true` if the listener was made current using [make_current()](class_audiolistener3d.md#class-audiolistener3d-method-make-current), `false` otherwise.

**Note:** There may be more than one AudioListener3D marked as "current" in the scene tree, but only the one that was made current last will be used.

---


<a id="class-audiolistener3d-method-make-current"></a>

void **make_current**() [🔗](class_audiolistener3d.md#class-audiolistener3d-method-make-current)

Enables the listener. This will override the current camera's listener.
