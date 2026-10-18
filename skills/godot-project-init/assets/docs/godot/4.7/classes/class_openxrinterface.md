> Source: https://docs.godotengine.org/en/4.7/classes/class_openxrinterface.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxrinterface"></a>

<a id="class-openxrinterface"></a>

# OpenXRInterface

**Inherits:** [XRInterface](class_xrinterface.md#class-xrinterface) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Our OpenXR interface.

<a id="description"></a>

## Description

The OpenXR interface allows Godot to interact with OpenXR runtimes and make it possible to create XR experiences and games.

Due to the needs of OpenXR this interface works slightly different than other plugin based XR interfaces. It needs to be initialized when Godot starts. You need to enable OpenXR, settings for this can be found in your games project settings under the XR heading. You do need to mark a viewport for use with XR in order for Godot to know which render result should be output to the headset.

<a id="tutorials"></a>

## Tutorials

- [Setting up XR](../tutorials/xr/setting_up_xr.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [display_refresh_rate](class_openxrinterface.md#class-openxrinterface-property-display-refresh-rate) | `0.0` |
| [bool](class_bool.md#class-bool) | [foveation_dynamic](class_openxrinterface.md#class-openxrinterface-property-foveation-dynamic) | `false` |
| [int](class_int.md#class-int) | [foveation_level](class_openxrinterface.md#class-openxrinterface-property-foveation-level) | `0` |
| [bool](class_bool.md#class-bool) | [foveation_with_subsampled_images](class_openxrinterface.md#class-openxrinterface-property-foveation-with-subsampled-images) | `false` |
| [float](class_float.md#class-float) | [render_target_size_multiplier](class_openxrinterface.md#class-openxrinterface-property-render-target-size-multiplier) | `1.0` |
| [float](class_float.md#class-float) | [vrs_min_radius](class_openxrinterface.md#class-openxrinterface-property-vrs-min-radius) | `20.0` |
| [float](class_float.md#class-float) | [vrs_strength](class_openxrinterface.md#class-openxrinterface-property-vrs-strength) | `1.0` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Array](class_array.md#class-array) | [get_action_sets](class_openxrinterface.md#class-openxrinterface-method-get-action-sets)() const |
| [Array](class_array.md#class-array) | [get_available_display_refresh_rates](class_openxrinterface.md#class-openxrinterface-method-get-available-display-refresh-rates)() const |
| [Vector3](class_vector3.md#class-vector3) | [get_hand_joint_angular_velocity](class_openxrinterface.md#class-openxrinterface-method-get-hand-joint-angular-velocity)(hand: [Hand](class_openxrinterface.md#enum-openxrinterface-hand), joint: [HandJoints](class_openxrinterface.md#enum-openxrinterface-handjoints)) const |
| BitField[[HandJointFlags](class_openxrinterface.md#enum-openxrinterface-handjointflags)] | [get_hand_joint_flags](class_openxrinterface.md#class-openxrinterface-method-get-hand-joint-flags)(hand: [Hand](class_openxrinterface.md#enum-openxrinterface-hand), joint: [HandJoints](class_openxrinterface.md#enum-openxrinterface-handjoints)) const |
| [Vector3](class_vector3.md#class-vector3) | [get_hand_joint_linear_velocity](class_openxrinterface.md#class-openxrinterface-method-get-hand-joint-linear-velocity)(hand: [Hand](class_openxrinterface.md#enum-openxrinterface-hand), joint: [HandJoints](class_openxrinterface.md#enum-openxrinterface-handjoints)) const |
| [Vector3](class_vector3.md#class-vector3) | [get_hand_joint_position](class_openxrinterface.md#class-openxrinterface-method-get-hand-joint-position)(hand: [Hand](class_openxrinterface.md#enum-openxrinterface-hand), joint: [HandJoints](class_openxrinterface.md#enum-openxrinterface-handjoints)) const |
| [float](class_float.md#class-float) | [get_hand_joint_radius](class_openxrinterface.md#class-openxrinterface-method-get-hand-joint-radius)(hand: [Hand](class_openxrinterface.md#enum-openxrinterface-hand), joint: [HandJoints](class_openxrinterface.md#enum-openxrinterface-handjoints)) const |
| [Quaternion](class_quaternion.md#class-quaternion) | [get_hand_joint_rotation](class_openxrinterface.md#class-openxrinterface-method-get-hand-joint-rotation)(hand: [Hand](class_openxrinterface.md#enum-openxrinterface-hand), joint: [HandJoints](class_openxrinterface.md#enum-openxrinterface-handjoints)) const |
| [HandTrackedSource](class_openxrinterface.md#enum-openxrinterface-handtrackedsource) | [get_hand_tracking_source](class_openxrinterface.md#class-openxrinterface-method-get-hand-tracking-source)(hand: [Hand](class_openxrinterface.md#enum-openxrinterface-hand)) const |
| [HandMotionRange](class_openxrinterface.md#enum-openxrinterface-handmotionrange) | [get_motion_range](class_openxrinterface.md#class-openxrinterface-method-get-motion-range)(hand: [Hand](class_openxrinterface.md#enum-openxrinterface-hand)) const |
| [SessionState](class_openxrinterface.md#enum-openxrinterface-sessionstate) | [get_session_state](class_openxrinterface.md#class-openxrinterface-method-get-session-state)() |
| [bool](class_bool.md#class-bool) | [is_action_set_active](class_openxrinterface.md#class-openxrinterface-method-is-action-set-active)(name: [String](class_string.md#class-string)) const |
| [bool](class_bool.md#class-bool) | [is_eye_gaze_interaction_supported](class_openxrinterface.md#class-openxrinterface-method-is-eye-gaze-interaction-supported)() |
| [bool](class_bool.md#class-bool) | [is_foveation_supported](class_openxrinterface.md#class-openxrinterface-method-is-foveation-supported)() const |
| [bool](class_bool.md#class-bool) | [is_hand_interaction_supported](class_openxrinterface.md#class-openxrinterface-method-is-hand-interaction-supported)() const |
| [bool](class_bool.md#class-bool) | [is_hand_tracking_supported](class_openxrinterface.md#class-openxrinterface-method-is-hand-tracking-supported)() |
| [bool](class_bool.md#class-bool) | [is_user_presence_supported](class_openxrinterface.md#class-openxrinterface-method-is-user-presence-supported)() const |
| [bool](class_bool.md#class-bool) | [is_user_present](class_openxrinterface.md#class-openxrinterface-method-is-user-present)() const |
| void | [set_action_set_active](class_openxrinterface.md#class-openxrinterface-method-set-action-set-active)(name: [String](class_string.md#class-string), active: [bool](class_bool.md#class-bool)) |
| void | [set_cpu_level](class_openxrinterface.md#class-openxrinterface-method-set-cpu-level)(level: [PerfSettingsLevel](class_openxrinterface.md#enum-openxrinterface-perfsettingslevel)) |
| void | [set_gpu_level](class_openxrinterface.md#class-openxrinterface-method-set-gpu-level)(level: [PerfSettingsLevel](class_openxrinterface.md#enum-openxrinterface-perfsettingslevel)) |
| void | [set_motion_range](class_openxrinterface.md#class-openxrinterface-method-set-motion-range)(hand: [Hand](class_openxrinterface.md#enum-openxrinterface-hand), motion_range: [HandMotionRange](class_openxrinterface.md#enum-openxrinterface-handmotionrange)) |

---


<a id="signals"></a>

## Signals

<a id="class-openxrinterface-signal-cpu-level-changed"></a>

**cpu_level_changed**(sub_domain: [int](class_int.md#class-int), from_level: [int](class_int.md#class-int), to_level: [int](class_int.md#class-int)) [🔗](class_openxrinterface.md#class-openxrinterface-signal-cpu-level-changed)

Informs the device CPU performance level has changed in the specified subdomain.

---


<a id="class-openxrinterface-signal-gpu-level-changed"></a>

**gpu_level_changed**(sub_domain: [int](class_int.md#class-int), from_level: [int](class_int.md#class-int), to_level: [int](class_int.md#class-int)) [🔗](class_openxrinterface.md#class-openxrinterface-signal-gpu-level-changed)

Informs the device GPU performance level has changed in the specified subdomain.

---


<a id="class-openxrinterface-signal-instance-exiting"></a>

**instance_exiting**() [🔗](class_openxrinterface.md#class-openxrinterface-signal-instance-exiting)

Informs our OpenXR instance is exiting.

---


<a id="class-openxrinterface-signal-pose-recentered"></a>

**pose_recentered**() [🔗](class_openxrinterface.md#class-openxrinterface-signal-pose-recentered)

Informs the user queued a recenter of the player position.

---


<a id="class-openxrinterface-signal-refresh-rate-changed"></a>

**refresh_rate_changed**(refresh_rate: [float](class_float.md#class-float)) [🔗](class_openxrinterface.md#class-openxrinterface-signal-refresh-rate-changed)

Informs the user the HMD refresh rate has changed.

**Note:** Only emitted if XR runtime supports the refresh rate extension.

---


<a id="class-openxrinterface-signal-session-begun"></a>

**session_begun**() [🔗](class_openxrinterface.md#class-openxrinterface-signal-session-begun)

Informs our OpenXR session has been started.

---


<a id="class-openxrinterface-signal-session-focussed"></a>

**session_focussed**() [🔗](class_openxrinterface.md#class-openxrinterface-signal-session-focussed)

Informs our OpenXR session now has focus, for example output is sent to the HMD and we're receiving XR input.

---


<a id="class-openxrinterface-signal-session-loss-pending"></a>

**session_loss_pending**() [🔗](class_openxrinterface.md#class-openxrinterface-signal-session-loss-pending)

Informs our OpenXR session is in the process of being lost.

---


<a id="class-openxrinterface-signal-session-stopping"></a>

**session_stopping**() [🔗](class_openxrinterface.md#class-openxrinterface-signal-session-stopping)

Informs our OpenXR session is stopping.

---


<a id="class-openxrinterface-signal-session-synchronized"></a>

**session_synchronized**() [🔗](class_openxrinterface.md#class-openxrinterface-signal-session-synchronized)

Informs our OpenXR session has been synchronized.

---


<a id="class-openxrinterface-signal-session-visible"></a>

**session_visible**() [🔗](class_openxrinterface.md#class-openxrinterface-signal-session-visible)

Informs our OpenXR session is now visible, for example output is sent to the HMD but we don't receive XR input.

---


<a id="class-openxrinterface-signal-user-presence-changed"></a>

**user_presence_changed**(is_user_present: [bool](class_bool.md#class-bool)) [🔗](class_openxrinterface.md#class-openxrinterface-signal-user-presence-changed)

Signal emitted when the user presence value changes.

**Note:** This signal will not be emitted during application startup and application shutdown. Developers should assume user presence is gained on startup and lost on shutdown.

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-openxrinterface-sessionstate"></a>

enum **SessionState**: [🔗](class_openxrinterface.md#enum-openxrinterface-sessionstate)

<a id="class-openxrinterface-constant-session-state-unknown"></a>

[SessionState](class_openxrinterface.md#enum-openxrinterface-sessionstate) **SESSION_STATE_UNKNOWN** = `0`

The state of the session is unknown, we haven't tried setting up OpenXR yet.

<a id="class-openxrinterface-constant-session-state-idle"></a>

[SessionState](class_openxrinterface.md#enum-openxrinterface-sessionstate) **SESSION_STATE_IDLE** = `1`

The initial state after the OpenXR session is created or after the session is destroyed.

<a id="class-openxrinterface-constant-session-state-ready"></a>

[SessionState](class_openxrinterface.md#enum-openxrinterface-sessionstate) **SESSION_STATE_READY** = `2`

OpenXR is ready to begin our session. [session_begun](class_openxrinterface.md#class-openxrinterface-signal-session-begun) is emitted when we change to this state.

<a id="class-openxrinterface-constant-session-state-synchronized"></a>

[SessionState](class_openxrinterface.md#enum-openxrinterface-sessionstate) **SESSION_STATE_SYNCHRONIZED** = `3`

The application has synched its frame loop with the runtime but we're not rendering anything. [session_synchronized](class_openxrinterface.md#class-openxrinterface-signal-session-synchronized) is emitted when we change to this state.

<a id="class-openxrinterface-constant-session-state-visible"></a>

[SessionState](class_openxrinterface.md#enum-openxrinterface-sessionstate) **SESSION_STATE_VISIBLE** = `4`

The application has synched its frame loop with the runtime and we're rendering output to the user, however we receive no user input. [session_visible](class_openxrinterface.md#class-openxrinterface-signal-session-visible) is emitted when we change to this state.

**Note:** This is the current state just before we get the focused state, whenever the user opens a system menu, switches to another application, or takes off their headset.

<a id="class-openxrinterface-constant-session-state-focused"></a>

[SessionState](class_openxrinterface.md#enum-openxrinterface-sessionstate) **SESSION_STATE_FOCUSED** = `5`

The application has synched its frame loop with the runtime, we're rendering output to the user and we're receiving XR input. [session_focussed](class_openxrinterface.md#class-openxrinterface-signal-session-focussed) is emitted when we change to this state.

**Note:** This is the state OpenXR will be in when the user can fully interact with your game.

<a id="class-openxrinterface-constant-session-state-stopping"></a>

[SessionState](class_openxrinterface.md#enum-openxrinterface-sessionstate) **SESSION_STATE_STOPPING** = `6`

Our session is being stopped. [session_stopping](class_openxrinterface.md#class-openxrinterface-signal-session-stopping) is emitted when we change to this state.

<a id="class-openxrinterface-constant-session-state-loss-pending"></a>

[SessionState](class_openxrinterface.md#enum-openxrinterface-sessionstate) **SESSION_STATE_LOSS_PENDING** = `7`

The session is about to be lost. [session_loss_pending](class_openxrinterface.md#class-openxrinterface-signal-session-loss-pending) is emitted when we change to this state.

<a id="class-openxrinterface-constant-session-state-exiting"></a>

[SessionState](class_openxrinterface.md#enum-openxrinterface-sessionstate) **SESSION_STATE_EXITING** = `8`

The OpenXR instance is about to be destroyed and we're exiting. [instance_exiting](class_openxrinterface.md#class-openxrinterface-signal-instance-exiting) is emitted when we change to this state.

---


<a id="enum-openxrinterface-hand"></a>

enum **Hand**: [🔗](class_openxrinterface.md#enum-openxrinterface-hand)

<a id="class-openxrinterface-constant-hand-left"></a>

[Hand](class_openxrinterface.md#enum-openxrinterface-hand) **HAND_LEFT** = `0`

Left hand.

<a id="class-openxrinterface-constant-hand-right"></a>

[Hand](class_openxrinterface.md#enum-openxrinterface-hand) **HAND_RIGHT** = `1`

Right hand.

<a id="class-openxrinterface-constant-hand-max"></a>

[Hand](class_openxrinterface.md#enum-openxrinterface-hand) **HAND_MAX** = `2`

Maximum value for the hand enum.

---


<a id="enum-openxrinterface-handmotionrange"></a>

enum **HandMotionRange**: [🔗](class_openxrinterface.md#enum-openxrinterface-handmotionrange)

<a id="class-openxrinterface-constant-hand-motion-range-unobstructed"></a>

[HandMotionRange](class_openxrinterface.md#enum-openxrinterface-handmotionrange) **HAND_MOTION_RANGE_UNOBSTRUCTED** = `0`

Full hand range, if user closes their hands, we make a full fist.

<a id="class-openxrinterface-constant-hand-motion-range-conform-to-controller"></a>

[HandMotionRange](class_openxrinterface.md#enum-openxrinterface-handmotionrange) **HAND_MOTION_RANGE_CONFORM_TO_CONTROLLER** = `1`

Conform to controller, if user closes their hands, the tracked data conforms to the shape of the controller.

<a id="class-openxrinterface-constant-hand-motion-range-max"></a>

[HandMotionRange](class_openxrinterface.md#enum-openxrinterface-handmotionrange) **HAND_MOTION_RANGE_MAX** = `2`

Maximum value for the motion range enum.

---


<a id="enum-openxrinterface-handtrackedsource"></a>

enum **HandTrackedSource**: [🔗](class_openxrinterface.md#enum-openxrinterface-handtrackedsource)

<a id="class-openxrinterface-constant-hand-tracked-source-unknown"></a>

[HandTrackedSource](class_openxrinterface.md#enum-openxrinterface-handtrackedsource) **HAND_TRACKED_SOURCE_UNKNOWN** = `0`

The source of hand tracking data is unknown (the extension is likely unsupported).

<a id="class-openxrinterface-constant-hand-tracked-source-unobstructed"></a>

[HandTrackedSource](class_openxrinterface.md#enum-openxrinterface-handtrackedsource) **HAND_TRACKED_SOURCE_UNOBSTRUCTED** = `1`

The source of hand tracking is unobstructed, this means that an accurate method of hand tracking is used, e.g. optical hand tracking, data gloves, etc.

<a id="class-openxrinterface-constant-hand-tracked-source-controller"></a>

[HandTrackedSource](class_openxrinterface.md#enum-openxrinterface-handtrackedsource) **HAND_TRACKED_SOURCE_CONTROLLER** = `2`

The source of hand tracking is a controller, bone positions are inferred from controller inputs.

<a id="class-openxrinterface-constant-hand-tracked-source-max"></a>

[HandTrackedSource](class_openxrinterface.md#enum-openxrinterface-handtrackedsource) **HAND_TRACKED_SOURCE_MAX** = `3`

Represents the size of the [HandTrackedSource](class_openxrinterface.md#enum-openxrinterface-handtrackedsource) enum.

---


<a id="enum-openxrinterface-handjoints"></a>

enum **HandJoints**: [🔗](class_openxrinterface.md#enum-openxrinterface-handjoints)

<a id="class-openxrinterface-constant-hand-joint-palm"></a>

[HandJoints](class_openxrinterface.md#enum-openxrinterface-handjoints) **HAND_JOINT_PALM** = `0`

Palm joint.

<a id="class-openxrinterface-constant-hand-joint-wrist"></a>

[HandJoints](class_openxrinterface.md#enum-openxrinterface-handjoints) **HAND_JOINT_WRIST** = `1`

Wrist joint.

<a id="class-openxrinterface-constant-hand-joint-thumb-metacarpal"></a>

[HandJoints](class_openxrinterface.md#enum-openxrinterface-handjoints) **HAND_JOINT_THUMB_METACARPAL** = `2`

Thumb metacarpal joint.

<a id="class-openxrinterface-constant-hand-joint-thumb-proximal"></a>

[HandJoints](class_openxrinterface.md#enum-openxrinterface-handjoints) **HAND_JOINT_THUMB_PROXIMAL** = `3`

Thumb proximal joint.

<a id="class-openxrinterface-constant-hand-joint-thumb-distal"></a>

[HandJoints](class_openxrinterface.md#enum-openxrinterface-handjoints) **HAND_JOINT_THUMB_DISTAL** = `4`

Thumb distal joint.

<a id="class-openxrinterface-constant-hand-joint-thumb-tip"></a>

[HandJoints](class_openxrinterface.md#enum-openxrinterface-handjoints) **HAND_JOINT_THUMB_TIP** = `5`

Thumb tip joint.

<a id="class-openxrinterface-constant-hand-joint-index-metacarpal"></a>

[HandJoints](class_openxrinterface.md#enum-openxrinterface-handjoints) **HAND_JOINT_INDEX_METACARPAL** = `6`

Index finger metacarpal joint.

<a id="class-openxrinterface-constant-hand-joint-index-proximal"></a>

[HandJoints](class_openxrinterface.md#enum-openxrinterface-handjoints) **HAND_JOINT_INDEX_PROXIMAL** = `7`

Index finger phalanx proximal joint.

<a id="class-openxrinterface-constant-hand-joint-index-intermediate"></a>

[HandJoints](class_openxrinterface.md#enum-openxrinterface-handjoints) **HAND_JOINT_INDEX_INTERMEDIATE** = `8`

Index finger phalanx intermediate joint.

<a id="class-openxrinterface-constant-hand-joint-index-distal"></a>

[HandJoints](class_openxrinterface.md#enum-openxrinterface-handjoints) **HAND_JOINT_INDEX_DISTAL** = `9`

Index finger phalanx distal joint.

<a id="class-openxrinterface-constant-hand-joint-index-tip"></a>

[HandJoints](class_openxrinterface.md#enum-openxrinterface-handjoints) **HAND_JOINT_INDEX_TIP** = `10`

Index finger tip joint.

<a id="class-openxrinterface-constant-hand-joint-middle-metacarpal"></a>

[HandJoints](class_openxrinterface.md#enum-openxrinterface-handjoints) **HAND_JOINT_MIDDLE_METACARPAL** = `11`

Middle finger metacarpal joint.

<a id="class-openxrinterface-constant-hand-joint-middle-proximal"></a>

[HandJoints](class_openxrinterface.md#enum-openxrinterface-handjoints) **HAND_JOINT_MIDDLE_PROXIMAL** = `12`

Middle finger phalanx proximal joint.

<a id="class-openxrinterface-constant-hand-joint-middle-intermediate"></a>

[HandJoints](class_openxrinterface.md#enum-openxrinterface-handjoints) **HAND_JOINT_MIDDLE_INTERMEDIATE** = `13`

Middle finger phalanx intermediate joint.

<a id="class-openxrinterface-constant-hand-joint-middle-distal"></a>

[HandJoints](class_openxrinterface.md#enum-openxrinterface-handjoints) **HAND_JOINT_MIDDLE_DISTAL** = `14`

Middle finger phalanx distal joint.

<a id="class-openxrinterface-constant-hand-joint-middle-tip"></a>

[HandJoints](class_openxrinterface.md#enum-openxrinterface-handjoints) **HAND_JOINT_MIDDLE_TIP** = `15`

Middle finger tip joint.

<a id="class-openxrinterface-constant-hand-joint-ring-metacarpal"></a>

[HandJoints](class_openxrinterface.md#enum-openxrinterface-handjoints) **HAND_JOINT_RING_METACARPAL** = `16`

Ring finger metacarpal joint.

<a id="class-openxrinterface-constant-hand-joint-ring-proximal"></a>

[HandJoints](class_openxrinterface.md#enum-openxrinterface-handjoints) **HAND_JOINT_RING_PROXIMAL** = `17`

Ring finger phalanx proximal joint.

<a id="class-openxrinterface-constant-hand-joint-ring-intermediate"></a>

[HandJoints](class_openxrinterface.md#enum-openxrinterface-handjoints) **HAND_JOINT_RING_INTERMEDIATE** = `18`

Ring finger phalanx intermediate joint.

<a id="class-openxrinterface-constant-hand-joint-ring-distal"></a>

[HandJoints](class_openxrinterface.md#enum-openxrinterface-handjoints) **HAND_JOINT_RING_DISTAL** = `19`

Ring finger phalanx distal joint.

<a id="class-openxrinterface-constant-hand-joint-ring-tip"></a>

[HandJoints](class_openxrinterface.md#enum-openxrinterface-handjoints) **HAND_JOINT_RING_TIP** = `20`

Ring finger tip joint.

<a id="class-openxrinterface-constant-hand-joint-little-metacarpal"></a>

[HandJoints](class_openxrinterface.md#enum-openxrinterface-handjoints) **HAND_JOINT_LITTLE_METACARPAL** = `21`

Pinky finger metacarpal joint.

<a id="class-openxrinterface-constant-hand-joint-little-proximal"></a>

[HandJoints](class_openxrinterface.md#enum-openxrinterface-handjoints) **HAND_JOINT_LITTLE_PROXIMAL** = `22`

Pinky finger phalanx proximal joint.

<a id="class-openxrinterface-constant-hand-joint-little-intermediate"></a>

[HandJoints](class_openxrinterface.md#enum-openxrinterface-handjoints) **HAND_JOINT_LITTLE_INTERMEDIATE** = `23`

Pinky finger phalanx intermediate joint.

<a id="class-openxrinterface-constant-hand-joint-little-distal"></a>

[HandJoints](class_openxrinterface.md#enum-openxrinterface-handjoints) **HAND_JOINT_LITTLE_DISTAL** = `24`

Pinky finger phalanx distal joint.

<a id="class-openxrinterface-constant-hand-joint-little-tip"></a>

[HandJoints](class_openxrinterface.md#enum-openxrinterface-handjoints) **HAND_JOINT_LITTLE_TIP** = `25`

Pinky finger tip joint.

<a id="class-openxrinterface-constant-hand-joint-max"></a>

[HandJoints](class_openxrinterface.md#enum-openxrinterface-handjoints) **HAND_JOINT_MAX** = `26`

Represents the size of the [HandJoints](class_openxrinterface.md#enum-openxrinterface-handjoints) enum.

---


<a id="enum-openxrinterface-perfsettingslevel"></a>

enum **PerfSettingsLevel**: [🔗](class_openxrinterface.md#enum-openxrinterface-perfsettingslevel)

<a id="class-openxrinterface-constant-perf-settings-level-power-savings"></a>

[PerfSettingsLevel](class_openxrinterface.md#enum-openxrinterface-perfsettingslevel) **PERF_SETTINGS_LEVEL_POWER_SAVINGS** = `0`

The application has entered a non-XR section (head-locked / static screen), during which power savings are to be prioritized.

<a id="class-openxrinterface-constant-perf-settings-level-sustained-low"></a>

[PerfSettingsLevel](class_openxrinterface.md#enum-openxrinterface-perfsettingslevel) **PERF_SETTINGS_LEVEL_SUSTAINED_LOW** = `1`

The application has entered a low and stable complexity section, during which reducing power is more important than occasional late rendering frames.

<a id="class-openxrinterface-constant-perf-settings-level-sustained-high"></a>

[PerfSettingsLevel](class_openxrinterface.md#enum-openxrinterface-perfsettingslevel) **PERF_SETTINGS_LEVEL_SUSTAINED_HIGH** = `2`

The application has entered a high or dynamic complexity section, during which the XR Runtime strives for consistent XR compositing and frame rendering within a thermally sustainable range.

<a id="class-openxrinterface-constant-perf-settings-level-boost"></a>

[PerfSettingsLevel](class_openxrinterface.md#enum-openxrinterface-perfsettingslevel) **PERF_SETTINGS_LEVEL_BOOST** = `3`

The application has entered a section with very high complexity, during which the XR Runtime is allowed to step up beyond the thermally sustainable range.

---


<a id="enum-openxrinterface-perfsettingssubdomain"></a>

enum **PerfSettingsSubDomain**: [🔗](class_openxrinterface.md#enum-openxrinterface-perfsettingssubdomain)

<a id="class-openxrinterface-constant-perf-settings-sub-domain-compositing"></a>

[PerfSettingsSubDomain](class_openxrinterface.md#enum-openxrinterface-perfsettingssubdomain) **PERF_SETTINGS_SUB_DOMAIN_COMPOSITING** = `0`

The compositing performance within the runtime has reached a new level.

<a id="class-openxrinterface-constant-perf-settings-sub-domain-rendering"></a>

[PerfSettingsSubDomain](class_openxrinterface.md#enum-openxrinterface-perfsettingssubdomain) **PERF_SETTINGS_SUB_DOMAIN_RENDERING** = `1`

The application rendering performance has reached a new level.

<a id="class-openxrinterface-constant-perf-settings-sub-domain-thermal"></a>

[PerfSettingsSubDomain](class_openxrinterface.md#enum-openxrinterface-perfsettingssubdomain) **PERF_SETTINGS_SUB_DOMAIN_THERMAL** = `2`

The temperature of the device has reached a new level.

---


<a id="enum-openxrinterface-perfsettingsnotificationlevel"></a>

enum **PerfSettingsNotificationLevel**: [🔗](class_openxrinterface.md#enum-openxrinterface-perfsettingsnotificationlevel)

<a id="class-openxrinterface-constant-perf-settings-notif-level-normal"></a>

[PerfSettingsNotificationLevel](class_openxrinterface.md#enum-openxrinterface-perfsettingsnotificationlevel) **PERF_SETTINGS_NOTIF_LEVEL_NORMAL** = `0`

The sub-domain has reached a level where no further actions other than currently applied are necessary.

<a id="class-openxrinterface-constant-perf-settings-notif-level-warning"></a>

[PerfSettingsNotificationLevel](class_openxrinterface.md#enum-openxrinterface-perfsettingsnotificationlevel) **PERF_SETTINGS_NOTIF_LEVEL_WARNING** = `1`

The sub-domain has reached an early warning level where the application should start proactive mitigation actions.

<a id="class-openxrinterface-constant-perf-settings-notif-level-impaired"></a>

[PerfSettingsNotificationLevel](class_openxrinterface.md#enum-openxrinterface-perfsettingsnotificationlevel) **PERF_SETTINGS_NOTIF_LEVEL_IMPAIRED** = `2`

The sub-domain has reached a critical level where the application should start drastic mitigation actions.

---


<a id="enum-openxrinterface-handjointflags"></a>

flags **HandJointFlags**: [🔗](class_openxrinterface.md#enum-openxrinterface-handjointflags)

<a id="class-openxrinterface-constant-hand-joint-none"></a>

[HandJointFlags](class_openxrinterface.md#enum-openxrinterface-handjointflags) **HAND_JOINT_NONE** = `0`

No flags are set.

<a id="class-openxrinterface-constant-hand-joint-orientation-valid"></a>

[HandJointFlags](class_openxrinterface.md#enum-openxrinterface-handjointflags) **HAND_JOINT_ORIENTATION_VALID** = `1`

If set, the orientation data is valid, otherwise, the orientation data is unreliable and should not be used.

<a id="class-openxrinterface-constant-hand-joint-orientation-tracked"></a>

[HandJointFlags](class_openxrinterface.md#enum-openxrinterface-handjointflags) **HAND_JOINT_ORIENTATION_TRACKED** = `2`

If set, the orientation data comes from tracking data, otherwise, the orientation data contains predicted data.

<a id="class-openxrinterface-constant-hand-joint-position-valid"></a>

[HandJointFlags](class_openxrinterface.md#enum-openxrinterface-handjointflags) **HAND_JOINT_POSITION_VALID** = `4`

If set, the positional data is valid, otherwise, the positional data is unreliable and should not be used.

<a id="class-openxrinterface-constant-hand-joint-position-tracked"></a>

[HandJointFlags](class_openxrinterface.md#enum-openxrinterface-handjointflags) **HAND_JOINT_POSITION_TRACKED** = `8`

If set, the positional data comes from tracking data, otherwise, the positional data contains predicted data.

<a id="class-openxrinterface-constant-hand-joint-linear-velocity-valid"></a>

[HandJointFlags](class_openxrinterface.md#enum-openxrinterface-handjointflags) **HAND_JOINT_LINEAR_VELOCITY_VALID** = `16`

If set, our linear velocity data is valid, otherwise, the linear velocity data is unreliable and should not be used.

<a id="class-openxrinterface-constant-hand-joint-angular-velocity-valid"></a>

[HandJointFlags](class_openxrinterface.md#enum-openxrinterface-handjointflags) **HAND_JOINT_ANGULAR_VELOCITY_VALID** = `32`

If set, our angular velocity data is valid, otherwise, the angular velocity data is unreliable and should not be used.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-openxrinterface-property-display-refresh-rate"></a>

[float](class_float.md#class-float) **display_refresh_rate** = `0.0` [🔗](class_openxrinterface.md#class-openxrinterface-property-display-refresh-rate)

- void **set_display_refresh_rate**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_display_refresh_rate**()

The display refresh rate for the current HMD. Only functional if this feature is supported by the OpenXR runtime and after the interface has been initialized.

---


<a id="class-openxrinterface-property-foveation-dynamic"></a>

[bool](class_bool.md#class-bool) **foveation_dynamic** = `false` [🔗](class_openxrinterface.md#class-openxrinterface-property-foveation-dynamic)

- void **set_foveation_dynamic**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_foveation_dynamic**()

If `true`, enables dynamic foveation adjustment. The interface must be initialized before this is accessible. If enabled, foveation will automatically be adjusted between low and [foveation_level](class_openxrinterface.md#class-openxrinterface-property-foveation-level).

---


<a id="class-openxrinterface-property-foveation-level"></a>

[int](class_int.md#class-int) **foveation_level** = `0` [🔗](class_openxrinterface.md#class-openxrinterface-property-foveation-level)

- void **set_foveation_level**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_foveation_level**()

The foveation level, from `0` (off) to `3` (high). The interface must be initialized before this is accessible.

---


<a id="class-openxrinterface-property-foveation-with-subsampled-images"></a>

[bool](class_bool.md#class-bool) **foveation_with_subsampled_images** = `false` [🔗](class_openxrinterface.md#class-openxrinterface-property-foveation-with-subsampled-images)

- void **set_foveation_with_subsampled_images**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_foveation_with_subsampled_images**()

If `true`, enables subsampled images with foveation, which can provide a performance boost on Vulkan.

---


<a id="class-openxrinterface-property-render-target-size-multiplier"></a>

[float](class_float.md#class-float) **render_target_size_multiplier** = `1.0` [🔗](class_openxrinterface.md#class-openxrinterface-property-render-target-size-multiplier)

- void **set_render_target_size_multiplier**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_render_target_size_multiplier**()

The render size multiplier for the current HMD. Must be set before the interface has been initialized.

---


<a id="class-openxrinterface-property-vrs-min-radius"></a>

[float](class_float.md#class-float) **vrs_min_radius** = `20.0` [🔗](class_openxrinterface.md#class-openxrinterface-property-vrs-min-radius)

- void **set_vrs_min_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_vrs_min_radius**()

The minimum radius around the focal point where full quality is guaranteed if VRS is used as a percentage of screen size.

**Note:** Mobile and Forward+ renderers only. Requires [Viewport.vrs_mode](class_viewport.md#class-viewport-property-vrs-mode) to be set to [Viewport.VRS_XR](class_viewport.md#class-viewport-constant-vrs-xr).

---


<a id="class-openxrinterface-property-vrs-strength"></a>

[float](class_float.md#class-float) **vrs_strength** = `1.0` [🔗](class_openxrinterface.md#class-openxrinterface-property-vrs-strength)

- void **set_vrs_strength**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_vrs_strength**()

The strength used to calculate the VRS density map. The greater this value, the more noticeable VRS is. This improves performance at the cost of quality.

**Note:** Mobile and Forward+ renderers only. Requires [Viewport.vrs_mode](class_viewport.md#class-viewport-property-vrs-mode) to be set to [Viewport.VRS_XR](class_viewport.md#class-viewport-constant-vrs-xr).

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-openxrinterface-method-get-action-sets"></a>

[Array](class_array.md#class-array) **get_action_sets**() const [🔗](class_openxrinterface.md#class-openxrinterface-method-get-action-sets)

Returns a list of action sets registered with Godot (loaded from the action map at runtime).

---


<a id="class-openxrinterface-method-get-available-display-refresh-rates"></a>

[Array](class_array.md#class-array) **get_available_display_refresh_rates**() const [🔗](class_openxrinterface.md#class-openxrinterface-method-get-available-display-refresh-rates)

Returns a list of display refresh rates supported by the current HMD. Only returned if this feature is supported by the OpenXR runtime and after the interface has been initialized.

---


<a id="class-openxrinterface-method-get-hand-joint-angular-velocity"></a>

[Vector3](class_vector3.md#class-vector3) **get_hand_joint_angular_velocity**(hand: [Hand](class_openxrinterface.md#enum-openxrinterface-hand), joint: [HandJoints](class_openxrinterface.md#enum-openxrinterface-handjoints)) const [🔗](class_openxrinterface.md#class-openxrinterface-method-get-hand-joint-angular-velocity)

**Deprecated:** Use [XRHandTracker.get_hand_joint_angular_velocity()](class_xrhandtracker.md#class-xrhandtracker-method-get-hand-joint-angular-velocity) obtained from [XRServer.get_tracker()](class_xrserver.md#class-xrserver-method-get-tracker) instead.

If handtracking is enabled, returns the angular velocity of a joint (`joint`) of a hand (`hand`) as provided by OpenXR. This is relative to [XROrigin3D](class_xrorigin3d.md#class-xrorigin3d)!

---


<a id="class-openxrinterface-method-get-hand-joint-flags"></a>

BitField[[HandJointFlags](class_openxrinterface.md#enum-openxrinterface-handjointflags)] **get_hand_joint_flags**(hand: [Hand](class_openxrinterface.md#enum-openxrinterface-hand), joint: [HandJoints](class_openxrinterface.md#enum-openxrinterface-handjoints)) const [🔗](class_openxrinterface.md#class-openxrinterface-method-get-hand-joint-flags)

**Deprecated:** Use [XRHandTracker.get_hand_joint_flags()](class_xrhandtracker.md#class-xrhandtracker-method-get-hand-joint-flags) obtained from [XRServer.get_tracker()](class_xrserver.md#class-xrserver-method-get-tracker) instead.

If handtracking is enabled, returns flags that inform us of the validity of the tracking data.

---


<a id="class-openxrinterface-method-get-hand-joint-linear-velocity"></a>

[Vector3](class_vector3.md#class-vector3) **get_hand_joint_linear_velocity**(hand: [Hand](class_openxrinterface.md#enum-openxrinterface-hand), joint: [HandJoints](class_openxrinterface.md#enum-openxrinterface-handjoints)) const [🔗](class_openxrinterface.md#class-openxrinterface-method-get-hand-joint-linear-velocity)

**Deprecated:** Use [XRHandTracker.get_hand_joint_linear_velocity()](class_xrhandtracker.md#class-xrhandtracker-method-get-hand-joint-linear-velocity) obtained from [XRServer.get_tracker()](class_xrserver.md#class-xrserver-method-get-tracker) instead.

If handtracking is enabled, returns the linear velocity of a joint (`joint`) of a hand (`hand`) as provided by OpenXR. This is relative to [XROrigin3D](class_xrorigin3d.md#class-xrorigin3d) without worldscale applied!

---


<a id="class-openxrinterface-method-get-hand-joint-position"></a>

[Vector3](class_vector3.md#class-vector3) **get_hand_joint_position**(hand: [Hand](class_openxrinterface.md#enum-openxrinterface-hand), joint: [HandJoints](class_openxrinterface.md#enum-openxrinterface-handjoints)) const [🔗](class_openxrinterface.md#class-openxrinterface-method-get-hand-joint-position)

**Deprecated:** Use [XRHandTracker.get_hand_joint_transform()](class_xrhandtracker.md#class-xrhandtracker-method-get-hand-joint-transform) obtained from [XRServer.get_tracker()](class_xrserver.md#class-xrserver-method-get-tracker) instead.

If handtracking is enabled, returns the position of a joint (`joint`) of a hand (`hand`) as provided by OpenXR. This is relative to [XROrigin3D](class_xrorigin3d.md#class-xrorigin3d) without worldscale applied!

---


<a id="class-openxrinterface-method-get-hand-joint-radius"></a>

[float](class_float.md#class-float) **get_hand_joint_radius**(hand: [Hand](class_openxrinterface.md#enum-openxrinterface-hand), joint: [HandJoints](class_openxrinterface.md#enum-openxrinterface-handjoints)) const [🔗](class_openxrinterface.md#class-openxrinterface-method-get-hand-joint-radius)

**Deprecated:** Use [XRHandTracker.get_hand_joint_radius()](class_xrhandtracker.md#class-xrhandtracker-method-get-hand-joint-radius) obtained from [XRServer.get_tracker()](class_xrserver.md#class-xrserver-method-get-tracker) instead.

If handtracking is enabled, returns the radius of a joint (`joint`) of a hand (`hand`) as provided by OpenXR. This is without worldscale applied!

---


<a id="class-openxrinterface-method-get-hand-joint-rotation"></a>

[Quaternion](class_quaternion.md#class-quaternion) **get_hand_joint_rotation**(hand: [Hand](class_openxrinterface.md#enum-openxrinterface-hand), joint: [HandJoints](class_openxrinterface.md#enum-openxrinterface-handjoints)) const [🔗](class_openxrinterface.md#class-openxrinterface-method-get-hand-joint-rotation)

**Deprecated:** Use [XRHandTracker.get_hand_joint_transform()](class_xrhandtracker.md#class-xrhandtracker-method-get-hand-joint-transform) obtained from [XRServer.get_tracker()](class_xrserver.md#class-xrserver-method-get-tracker) instead.

If handtracking is enabled, returns the rotation of a joint (`joint`) of a hand (`hand`) as provided by OpenXR.

---


<a id="class-openxrinterface-method-get-hand-tracking-source"></a>

[HandTrackedSource](class_openxrinterface.md#enum-openxrinterface-handtrackedsource) **get_hand_tracking_source**(hand: [Hand](class_openxrinterface.md#enum-openxrinterface-hand)) const [🔗](class_openxrinterface.md#class-openxrinterface-method-get-hand-tracking-source)

**Deprecated:** Use [XRHandTracker.hand_tracking_source](class_xrhandtracker.md#class-xrhandtracker-property-hand-tracking-source) obtained from [XRServer.get_tracker()](class_xrserver.md#class-xrserver-method-get-tracker) instead.

If handtracking is enabled and hand tracking source is supported, gets the source of the hand tracking data for `hand`.

---


<a id="class-openxrinterface-method-get-motion-range"></a>

[HandMotionRange](class_openxrinterface.md#enum-openxrinterface-handmotionrange) **get_motion_range**(hand: [Hand](class_openxrinterface.md#enum-openxrinterface-hand)) const [🔗](class_openxrinterface.md#class-openxrinterface-method-get-motion-range)

If handtracking is enabled and motion range is supported, gets the currently configured motion range for `hand`.

---


<a id="class-openxrinterface-method-get-session-state"></a>

[SessionState](class_openxrinterface.md#enum-openxrinterface-sessionstate) **get_session_state**() [🔗](class_openxrinterface.md#class-openxrinterface-method-get-session-state)

Returns the current state of our OpenXR session.

---


<a id="class-openxrinterface-method-is-action-set-active"></a>

[bool](class_bool.md#class-bool) **is_action_set_active**(name: [String](class_string.md#class-string)) const [🔗](class_openxrinterface.md#class-openxrinterface-method-is-action-set-active)

Returns `true` if the given action set is active.

---


<a id="class-openxrinterface-method-is-eye-gaze-interaction-supported"></a>

[bool](class_bool.md#class-bool) **is_eye_gaze_interaction_supported**() [🔗](class_openxrinterface.md#class-openxrinterface-method-is-eye-gaze-interaction-supported)

Returns the capabilities of the eye gaze interaction extension.

**Note:** This only returns a valid value after OpenXR has been initialized.

---


<a id="class-openxrinterface-method-is-foveation-supported"></a>

[bool](class_bool.md#class-bool) **is_foveation_supported**() const [🔗](class_openxrinterface.md#class-openxrinterface-method-is-foveation-supported)

Returns `true` if OpenXR's foveation extension is supported. The interface must be initialized before this returns a valid value.

**Note:** When using the Vulkan rendering driver, [Viewport.vrs_mode](class_viewport.md#class-viewport-property-vrs-mode) must be set to [Viewport.VRS_XR](class_viewport.md#class-viewport-constant-vrs-xr) to support foveation.

---


<a id="class-openxrinterface-method-is-hand-interaction-supported"></a>

[bool](class_bool.md#class-bool) **is_hand_interaction_supported**() const [🔗](class_openxrinterface.md#class-openxrinterface-method-is-hand-interaction-supported)

Returns `true` if OpenXR's hand interaction profile is supported and enabled.

**Note:** This only returns a valid value after OpenXR has been initialized.

---


<a id="class-openxrinterface-method-is-hand-tracking-supported"></a>

[bool](class_bool.md#class-bool) **is_hand_tracking_supported**() [🔗](class_openxrinterface.md#class-openxrinterface-method-is-hand-tracking-supported)

Returns `true` if OpenXR's hand tracking is supported and enabled.

**Note:** This only returns a valid value after OpenXR has been initialized.

---


<a id="class-openxrinterface-method-is-user-presence-supported"></a>

[bool](class_bool.md#class-bool) **is_user_presence_supported**() const [🔗](class_openxrinterface.md#class-openxrinterface-method-is-user-presence-supported)

Returns `true` if OpenXR's user presence extension is supported and enabled.

**Note:** This only returns a valid value after OpenXR has been initialized.

---


<a id="class-openxrinterface-method-is-user-present"></a>

[bool](class_bool.md#class-bool) **is_user_present**() const [🔗](class_openxrinterface.md#class-openxrinterface-method-is-user-present)

Returns `true` if system has detected the presence of a user in the XR experience.

---


<a id="class-openxrinterface-method-set-action-set-active"></a>

void **set_action_set_active**(name: [String](class_string.md#class-string), active: [bool](class_bool.md#class-bool)) [🔗](class_openxrinterface.md#class-openxrinterface-method-set-action-set-active)

Sets the given action set as active or inactive.

---


<a id="class-openxrinterface-method-set-cpu-level"></a>

void **set_cpu_level**(level: [PerfSettingsLevel](class_openxrinterface.md#enum-openxrinterface-perfsettingslevel)) [🔗](class_openxrinterface.md#class-openxrinterface-method-set-cpu-level)

Sets the CPU performance level of the OpenXR device.

---


<a id="class-openxrinterface-method-set-gpu-level"></a>

void **set_gpu_level**(level: [PerfSettingsLevel](class_openxrinterface.md#enum-openxrinterface-perfsettingslevel)) [🔗](class_openxrinterface.md#class-openxrinterface-method-set-gpu-level)

Sets the GPU performance level of the OpenXR device.

---


<a id="class-openxrinterface-method-set-motion-range"></a>

void **set_motion_range**(hand: [Hand](class_openxrinterface.md#enum-openxrinterface-hand), motion_range: [HandMotionRange](class_openxrinterface.md#enum-openxrinterface-handmotionrange)) [🔗](class_openxrinterface.md#class-openxrinterface-method-set-motion-range)

If handtracking is enabled and motion range is supported, sets the currently configured motion range for `hand` to `motion_range`.
