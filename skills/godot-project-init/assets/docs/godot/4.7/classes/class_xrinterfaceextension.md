> Source: https://docs.godotengine.org/en/4.7/classes/class_xrinterfaceextension.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="xrinterfaceextension"></a>

<a id="class-xrinterfaceextension"></a>

# XRInterfaceExtension

**Inherits:** [XRInterface](class_xrinterface.md#class-xrinterface) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Base class for XR interface extensions (plugins).

<a id="description"></a>

## Description

External XR interface plugins should inherit from this class.

<a id="tutorials"></a>

## Tutorials

- [XR documentation index](../tutorials/xr/index.md)

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [_end_frame](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-end-frame)() virtual |
| [bool](class_bool.md#class-bool) | [_get_anchor_detection_is_enabled](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-get-anchor-detection-is-enabled)() virtual const |
| [int](class_int.md#class-int) | [_get_camera_feed_id](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-get-camera-feed-id)() virtual const |
| [Transform3D](class_transform3d.md#class-transform3d) | [_get_camera_transform](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-get-camera-transform)() virtual |
| [int](class_int.md#class-int) | [_get_capabilities](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-get-capabilities)() virtual const |
| [RID](class_rid.md#class-rid) | [_get_color_texture](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-get-color-texture)() virtual |
| [RID](class_rid.md#class-rid) | [_get_depth_texture](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-get-depth-texture)() virtual |
| [StringName](class_stringname.md#class-stringname) | [_get_name](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-get-name)() virtual const |
| [PackedVector3Array](class_packedvector3array.md#class-packedvector3array) | [_get_play_area](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-get-play-area)() virtual const |
| [PlayAreaMode](class_xrinterface.md#enum-xrinterface-playareamode) | [_get_play_area_mode](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-get-play-area-mode)() virtual const |
| [PackedFloat64Array](class_packedfloat64array.md#class-packedfloat64array) | [_get_projection_for_view](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-get-projection-for-view)(view: [int](class_int.md#class-int), aspect: [float](class_float.md#class-float), z_near: [float](class_float.md#class-float), z_far: [float](class_float.md#class-float)) virtual |
| [Vector2](class_vector2.md#class-vector2) | [_get_render_target_size](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-get-render-target-size)() virtual |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [_get_suggested_pose_names](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-get-suggested-pose-names)(tracker_name: [StringName](class_stringname.md#class-stringname)) virtual const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [_get_suggested_tracker_names](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-get-suggested-tracker-names)() virtual const |
| [Dictionary](class_dictionary.md#class-dictionary) | [_get_system_info](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-get-system-info)() virtual const |
| [TrackingStatus](class_xrinterface.md#enum-xrinterface-trackingstatus) | [_get_tracking_status](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-get-tracking-status)() virtual const |
| [Transform3D](class_transform3d.md#class-transform3d) | [_get_transform_for_view](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-get-transform-for-view)(view: [int](class_int.md#class-int), cam_transform: [Transform3D](class_transform3d.md#class-transform3d)) virtual |
| [RID](class_rid.md#class-rid) | [_get_velocity_texture](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-get-velocity-texture)() virtual |
| [int](class_int.md#class-int) | [_get_view_count](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-get-view-count)() virtual |
| [RID](class_rid.md#class-rid) | [_get_vrs_texture](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-get-vrs-texture)() virtual |
| [VRSTextureFormat](class_xrinterface.md#enum-xrinterface-vrstextureformat) | [_get_vrs_texture_format](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-get-vrs-texture-format)() virtual |
| [bool](class_bool.md#class-bool) | [_initialize](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-initialize)() virtual |
| [bool](class_bool.md#class-bool) | [_is_initialized](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-is-initialized)() virtual const |
| void | [_post_draw_viewport](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-post-draw-viewport)(render_target: [RID](class_rid.md#class-rid), screen_rect: [Rect2](class_rect2.md#class-rect2)) virtual |
| [bool](class_bool.md#class-bool) | [_pre_draw_viewport](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-pre-draw-viewport)(render_target: [RID](class_rid.md#class-rid)) virtual |
| void | [_pre_render](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-pre-render)() virtual |
| void | [_process](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-process)() virtual |
| void | [_set_anchor_detection_is_enabled](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-set-anchor-detection-is-enabled)(enabled: [bool](class_bool.md#class-bool)) virtual |
| [bool](class_bool.md#class-bool) | [_set_play_area_mode](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-set-play-area-mode)(mode: [PlayAreaMode](class_xrinterface.md#enum-xrinterface-playareamode)) virtual const |
| [bool](class_bool.md#class-bool) | [_supports_play_area_mode](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-supports-play-area-mode)(mode: [PlayAreaMode](class_xrinterface.md#enum-xrinterface-playareamode)) virtual const |
| void | [_trigger_haptic_pulse](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-trigger-haptic-pulse)(action_name: [String](class_string.md#class-string), tracker_name: [StringName](class_stringname.md#class-stringname), frequency: [float](class_float.md#class-float), amplitude: [float](class_float.md#class-float), duration_sec: [float](class_float.md#class-float), delay_sec: [float](class_float.md#class-float)) virtual |
| void | [_uninitialize](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-uninitialize)() virtual |
| void | [add_blit](class_xrinterfaceextension.md#class-xrinterfaceextension-method-add-blit)(render_target: [RID](class_rid.md#class-rid), src_rect: [Rect2](class_rect2.md#class-rect2), dst_rect: [Rect2i](class_rect2i.md#class-rect2i), use_layer: [bool](class_bool.md#class-bool), layer: [int](class_int.md#class-int), apply_lens_distortion: [bool](class_bool.md#class-bool), eye_center: [Vector2](class_vector2.md#class-vector2), k1: [float](class_float.md#class-float), k2: [float](class_float.md#class-float), upscale: [float](class_float.md#class-float), aspect_ratio: [float](class_float.md#class-float)) |
| [RID](class_rid.md#class-rid) | [get_color_texture](class_xrinterfaceextension.md#class-xrinterfaceextension-method-get-color-texture)() |
| [RID](class_rid.md#class-rid) | [get_depth_texture](class_xrinterfaceextension.md#class-xrinterfaceextension-method-get-depth-texture)() |
| [RID](class_rid.md#class-rid) | [get_render_target_texture](class_xrinterfaceextension.md#class-xrinterfaceextension-method-get-render-target-texture)(render_target: [RID](class_rid.md#class-rid)) |
| [RID](class_rid.md#class-rid) | [get_velocity_texture](class_xrinterfaceextension.md#class-xrinterfaceextension-method-get-velocity-texture)() |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-xrinterfaceextension-private-method-end-frame"></a>

void **_end_frame**() virtual [🔗](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-end-frame)

Called if interface is active and queues have been submitted.

---


<a id="class-xrinterfaceextension-private-method-get-anchor-detection-is-enabled"></a>

[bool](class_bool.md#class-bool) **_get_anchor_detection_is_enabled**() virtual const [🔗](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-get-anchor-detection-is-enabled)

Return `true` if anchor detection is enabled for this interface.

---


<a id="class-xrinterfaceextension-private-method-get-camera-feed-id"></a>

[int](class_int.md#class-int) **_get_camera_feed_id**() virtual const [🔗](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-get-camera-feed-id)

Returns the camera feed ID for the [CameraFeed](class_camerafeed.md#class-camerafeed) registered with the [CameraServer](class_cameraserver.md#class-cameraserver) that should be presented as the background on an AR capable device (if applicable).

---


<a id="class-xrinterfaceextension-private-method-get-camera-transform"></a>

[Transform3D](class_transform3d.md#class-transform3d) **_get_camera_transform**() virtual [🔗](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-get-camera-transform)

Returns the [Transform3D](class_transform3d.md#class-transform3d) that positions the [XRCamera3D](class_xrcamera3d.md#class-xrcamera3d) in the world.

---


<a id="class-xrinterfaceextension-private-method-get-capabilities"></a>

[int](class_int.md#class-int) **_get_capabilities**() virtual const [🔗](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-get-capabilities)

Returns the capabilities of this interface.

---


<a id="class-xrinterfaceextension-private-method-get-color-texture"></a>

[RID](class_rid.md#class-rid) **_get_color_texture**() virtual [🔗](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-get-color-texture)

Return color texture into which to render (if applicable).

---


<a id="class-xrinterfaceextension-private-method-get-depth-texture"></a>

[RID](class_rid.md#class-rid) **_get_depth_texture**() virtual [🔗](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-get-depth-texture)

Return depth texture into which to render (if applicable).

---


<a id="class-xrinterfaceextension-private-method-get-name"></a>

[StringName](class_stringname.md#class-stringname) **_get_name**() virtual const [🔗](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-get-name)

Returns the name of this interface.

---


<a id="class-xrinterfaceextension-private-method-get-play-area"></a>

[PackedVector3Array](class_packedvector3array.md#class-packedvector3array) **_get_play_area**() virtual const [🔗](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-get-play-area)

Returns a [PackedVector3Array](class_packedvector3array.md#class-packedvector3array) that represents the play areas boundaries (if applicable).

---


<a id="class-xrinterfaceextension-private-method-get-play-area-mode"></a>

[PlayAreaMode](class_xrinterface.md#enum-xrinterface-playareamode) **_get_play_area_mode**() virtual const [🔗](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-get-play-area-mode)

Returns the play area mode that sets up our play area.

---


<a id="class-xrinterfaceextension-private-method-get-projection-for-view"></a>

[PackedFloat64Array](class_packedfloat64array.md#class-packedfloat64array) **_get_projection_for_view**(view: [int](class_int.md#class-int), aspect: [float](class_float.md#class-float), z_near: [float](class_float.md#class-float), z_far: [float](class_float.md#class-float)) virtual [🔗](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-get-projection-for-view)

Returns the projection matrix for the given view as a [PackedFloat64Array](class_packedfloat64array.md#class-packedfloat64array).

---


<a id="class-xrinterfaceextension-private-method-get-render-target-size"></a>

[Vector2](class_vector2.md#class-vector2) **_get_render_target_size**() virtual [🔗](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-get-render-target-size)

Returns the size of our render target for this interface, this overrides the size of the [Viewport](class_viewport.md#class-viewport) marked as the xr viewport.

---


<a id="class-xrinterfaceextension-private-method-get-suggested-pose-names"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **_get_suggested_pose_names**(tracker_name: [StringName](class_stringname.md#class-stringname)) virtual const [🔗](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-get-suggested-pose-names)

Returns a [PackedStringArray](class_packedstringarray.md#class-packedstringarray) with pose names configured by this interface. Note that user configuration can override this list.

---


<a id="class-xrinterfaceextension-private-method-get-suggested-tracker-names"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **_get_suggested_tracker_names**() virtual const [🔗](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-get-suggested-tracker-names)

Returns a [PackedStringArray](class_packedstringarray.md#class-packedstringarray) with tracker names configured by this interface. Note that user configuration can override this list.

---


<a id="class-xrinterfaceextension-private-method-get-system-info"></a>

[Dictionary](class_dictionary.md#class-dictionary) **_get_system_info**() virtual const [🔗](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-get-system-info)

Returns a [Dictionary](class_dictionary.md#class-dictionary) with system information related to this interface.

---


<a id="class-xrinterfaceextension-private-method-get-tracking-status"></a>

[TrackingStatus](class_xrinterface.md#enum-xrinterface-trackingstatus) **_get_tracking_status**() virtual const [🔗](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-get-tracking-status)

Returns the current status of our tracking.

---


<a id="class-xrinterfaceextension-private-method-get-transform-for-view"></a>

[Transform3D](class_transform3d.md#class-transform3d) **_get_transform_for_view**(view: [int](class_int.md#class-int), cam_transform: [Transform3D](class_transform3d.md#class-transform3d)) virtual [🔗](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-get-transform-for-view)

Returns a [Transform3D](class_transform3d.md#class-transform3d) for a given view.

---


<a id="class-xrinterfaceextension-private-method-get-velocity-texture"></a>

[RID](class_rid.md#class-rid) **_get_velocity_texture**() virtual [🔗](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-get-velocity-texture)

Return velocity texture into which to render (if applicable).

---


<a id="class-xrinterfaceextension-private-method-get-view-count"></a>

[int](class_int.md#class-int) **_get_view_count**() virtual [🔗](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-get-view-count)

Returns the number of views this interface requires, 1 for mono, 2 for stereoscopic.

---


<a id="class-xrinterfaceextension-private-method-get-vrs-texture"></a>

[RID](class_rid.md#class-rid) **_get_vrs_texture**() virtual [🔗](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-get-vrs-texture)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-xrinterfaceextension-private-method-get-vrs-texture-format"></a>

[VRSTextureFormat](class_xrinterface.md#enum-xrinterface-vrstextureformat) **_get_vrs_texture_format**() virtual [🔗](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-get-vrs-texture-format)

Returns the format of the texture returned by [_get_vrs_texture()](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-get-vrs-texture).

---


<a id="class-xrinterfaceextension-private-method-initialize"></a>

[bool](class_bool.md#class-bool) **_initialize**() virtual [🔗](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-initialize)

Initializes the interface, returns `true` on success.

---


<a id="class-xrinterfaceextension-private-method-is-initialized"></a>

[bool](class_bool.md#class-bool) **_is_initialized**() virtual const [🔗](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-is-initialized)

Returns `true` if this interface has been initialized.

---


<a id="class-xrinterfaceextension-private-method-post-draw-viewport"></a>

void **_post_draw_viewport**(render_target: [RID](class_rid.md#class-rid), screen_rect: [Rect2](class_rect2.md#class-rect2)) virtual [🔗](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-post-draw-viewport)

Called after the XR [Viewport](class_viewport.md#class-viewport) draw logic has completed.

---


<a id="class-xrinterfaceextension-private-method-pre-draw-viewport"></a>

[bool](class_bool.md#class-bool) **_pre_draw_viewport**(render_target: [RID](class_rid.md#class-rid)) virtual [🔗](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-pre-draw-viewport)

Called if this is our primary **XRInterfaceExtension** before we start processing a [Viewport](class_viewport.md#class-viewport) for every active XR [Viewport](class_viewport.md#class-viewport), returns `true` if that viewport should be rendered. An XR interface may return `false` if the user has taken off their headset and we can pause rendering.

---


<a id="class-xrinterfaceextension-private-method-pre-render"></a>

void **_pre_render**() virtual [🔗](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-pre-render)

Called if this **XRInterfaceExtension** is active before rendering starts. Most XR interfaces will sync tracking at this point in time.

---


<a id="class-xrinterfaceextension-private-method-process"></a>

void **_process**() virtual [🔗](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-process)

Called if this **XRInterfaceExtension** is active before our physics and game process is called. Most XR interfaces will update its [XRPositionalTracker](class_xrpositionaltracker.md#class-xrpositionaltracker)s at this point in time.

---


<a id="class-xrinterfaceextension-private-method-set-anchor-detection-is-enabled"></a>

void **_set_anchor_detection_is_enabled**(enabled: [bool](class_bool.md#class-bool)) virtual [🔗](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-set-anchor-detection-is-enabled)

Enables anchor detection on this interface if supported.

---


<a id="class-xrinterfaceextension-private-method-set-play-area-mode"></a>

[bool](class_bool.md#class-bool) **_set_play_area_mode**(mode: [PlayAreaMode](class_xrinterface.md#enum-xrinterface-playareamode)) virtual const [🔗](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-set-play-area-mode)

Set the play area mode for this interface.

---


<a id="class-xrinterfaceextension-private-method-supports-play-area-mode"></a>

[bool](class_bool.md#class-bool) **_supports_play_area_mode**(mode: [PlayAreaMode](class_xrinterface.md#enum-xrinterface-playareamode)) virtual const [🔗](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-supports-play-area-mode)

Returns `true` if this interface supports this play area mode.

---


<a id="class-xrinterfaceextension-private-method-trigger-haptic-pulse"></a>

void **_trigger_haptic_pulse**(action_name: [String](class_string.md#class-string), tracker_name: [StringName](class_stringname.md#class-stringname), frequency: [float](class_float.md#class-float), amplitude: [float](class_float.md#class-float), duration_sec: [float](class_float.md#class-float), delay_sec: [float](class_float.md#class-float)) virtual [🔗](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-trigger-haptic-pulse)

Triggers a haptic pulse to be emitted on the specified tracker.

---


<a id="class-xrinterfaceextension-private-method-uninitialize"></a>

void **_uninitialize**() virtual [🔗](class_xrinterfaceextension.md#class-xrinterfaceextension-private-method-uninitialize)

Uninitialize the interface.

---


<a id="class-xrinterfaceextension-method-add-blit"></a>

void **add_blit**(render_target: [RID](class_rid.md#class-rid), src_rect: [Rect2](class_rect2.md#class-rect2), dst_rect: [Rect2i](class_rect2i.md#class-rect2i), use_layer: [bool](class_bool.md#class-bool), layer: [int](class_int.md#class-int), apply_lens_distortion: [bool](class_bool.md#class-bool), eye_center: [Vector2](class_vector2.md#class-vector2), k1: [float](class_float.md#class-float), k2: [float](class_float.md#class-float), upscale: [float](class_float.md#class-float), aspect_ratio: [float](class_float.md#class-float)) [🔗](class_xrinterfaceextension.md#class-xrinterfaceextension-method-add-blit)

Blits our render results to screen optionally applying lens distortion. This can only be called while processing `_commit_views`.

---


<a id="class-xrinterfaceextension-method-get-color-texture"></a>

[RID](class_rid.md#class-rid) **get_color_texture**() [🔗](class_xrinterfaceextension.md#class-xrinterfaceextension-method-get-color-texture)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-xrinterfaceextension-method-get-depth-texture"></a>

[RID](class_rid.md#class-rid) **get_depth_texture**() [🔗](class_xrinterfaceextension.md#class-xrinterfaceextension-method-get-depth-texture)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-xrinterfaceextension-method-get-render-target-texture"></a>

[RID](class_rid.md#class-rid) **get_render_target_texture**(render_target: [RID](class_rid.md#class-rid)) [🔗](class_xrinterfaceextension.md#class-xrinterfaceextension-method-get-render-target-texture)

Returns a valid [RID](class_rid.md#class-rid) for a texture to which we should render the current frame if supported by the interface.

---


<a id="class-xrinterfaceextension-method-get-velocity-texture"></a>

[RID](class_rid.md#class-rid) **get_velocity_texture**() [🔗](class_xrinterfaceextension.md#class-xrinterfaceextension-method-get-velocity-texture)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!
