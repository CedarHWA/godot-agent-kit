> Source: https://docs.godotengine.org/en/4.7/classes/class_openxrapiextension.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxrapiextension"></a>

<a id="class-openxrapiextension"></a>

# OpenXRAPIExtension

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Makes the OpenXR API available for GDExtension.

<a id="description"></a>

## Description

**OpenXRAPIExtension** makes OpenXR available for GDExtension. It provides the OpenXR API to GDExtension through the [get_instance_proc_addr()](class_openxrapiextension.md#class-openxrapiextension-method-get-instance-proc-addr) method, and the OpenXR instance through [get_instance()](class_openxrapiextension.md#class-openxrapiextension-method-get-instance).

It also provides methods for querying the status of OpenXR initialization, and helper methods for ease of use of the API with GDExtension.

<a id="tutorials"></a>

## Tutorials

- [XrResult documentation](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrResult.html)
- [XrInstance documentation](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrInstance.html)
- [XrSpace documentation](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrSpace.html)
- [XrSession documentation](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrSession.html)
- [XrSystemId documentation](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrSystemId.html)
- [xrBeginSession documentation](https://registry.khronos.org/OpenXR/specs/1.0/man/html/xrBeginSession.html)
- [XrPosef documentation](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrPosef.html)

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [int](class_int.md#class-int) | [action_get_handle](class_openxrapiextension.md#class-openxrapiextension-method-action-get-handle)(action: [RID](class_rid.md#class-rid)) |
| void | [begin_debug_label_region](class_openxrapiextension.md#class-openxrapiextension-method-begin-debug-label-region)(label_name: [String](class_string.md#class-string)) |
| [bool](class_bool.md#class-bool) | [can_render](class_openxrapiextension.md#class-openxrapiextension-method-can-render)() |
| void | [end_debug_label_region](class_openxrapiextension.md#class-openxrapiextension-method-end-debug-label-region)() |
| [RID](class_rid.md#class-rid) | [find_action](class_openxrapiextension.md#class-openxrapiextension-method-find-action)(name: [String](class_string.md#class-string), action_set: [RID](class_rid.md#class-rid)) |
| [String](class_string.md#class-string) | [get_error_string](class_openxrapiextension.md#class-openxrapiextension-method-get-error-string)(result: [int](class_int.md#class-int)) |
| [int](class_int.md#class-int) | [get_hand_tracker](class_openxrapiextension.md#class-openxrapiextension-method-get-hand-tracker)(hand_index: [int](class_int.md#class-int)) |
| [int](class_int.md#class-int) | [get_instance](class_openxrapiextension.md#class-openxrapiextension-method-get-instance)() |
| [int](class_int.md#class-int) | [get_instance_proc_addr](class_openxrapiextension.md#class-openxrapiextension-method-get-instance-proc-addr)(name: [String](class_string.md#class-string)) |
| [int](class_int.md#class-int) | [get_next_frame_time](class_openxrapiextension.md#class-openxrapiextension-method-get-next-frame-time)() |
| [int](class_int.md#class-int) | [get_openxr_version](class_openxrapiextension.md#class-openxrapiextension-method-get-openxr-version)() |
| [int](class_int.md#class-int) | [get_play_space](class_openxrapiextension.md#class-openxrapiextension-method-get-play-space)() |
| [int](class_int.md#class-int) | [get_predicted_display_time](class_openxrapiextension.md#class-openxrapiextension-method-get-predicted-display-time)() |
| [int](class_int.md#class-int) | [get_projection_layer](class_openxrapiextension.md#class-openxrapiextension-method-get-projection-layer)() |
| [float](class_float.md#class-float) | [get_render_state_z_far](class_openxrapiextension.md#class-openxrapiextension-method-get-render-state-z-far)() |
| [float](class_float.md#class-float) | [get_render_state_z_near](class_openxrapiextension.md#class-openxrapiextension-method-get-render-state-z-near)() |
| [int](class_int.md#class-int) | [get_session](class_openxrapiextension.md#class-openxrapiextension-method-get-session)() |
| [PackedInt64Array](class_packedint64array.md#class-packedint64array) | [get_supported_swapchain_formats](class_openxrapiextension.md#class-openxrapiextension-method-get-supported-swapchain-formats)() |
| [String](class_string.md#class-string) | [get_swapchain_format_name](class_openxrapiextension.md#class-openxrapiextension-method-get-swapchain-format-name)(swapchain_format: [int](class_int.md#class-int)) |
| [int](class_int.md#class-int) | [get_system_id](class_openxrapiextension.md#class-openxrapiextension-method-get-system-id)() |
| [int](class_int.md#class-int) | [get_view_configuration](class_openxrapiextension.md#class-openxrapiextension-method-get-view-configuration)() const |
| [int](class_int.md#class-int) | [get_view_count](class_openxrapiextension.md#class-openxrapiextension-method-get-view-count)() const |
| void | [insert_debug_label](class_openxrapiextension.md#class-openxrapiextension-method-insert-debug-label)(label_name: [String](class_string.md#class-string)) |
| [OpenXRAlphaBlendModeSupport](class_openxrapiextension.md#enum-openxrapiextension-openxralphablendmodesupport) | [is_environment_blend_mode_alpha_supported](class_openxrapiextension.md#class-openxrapiextension-method-is-environment-blend-mode-alpha-supported)() |
| [bool](class_bool.md#class-bool) | [is_initialized](class_openxrapiextension.md#class-openxrapiextension-method-is-initialized)() |
| [bool](class_bool.md#class-bool) | [is_running](class_openxrapiextension.md#class-openxrapiextension-method-is-running)() |
| [bool](class_bool.md#class-bool) | [openxr_is_enabled](class_openxrapiextension.md#class-openxrapiextension-method-openxr-is-enabled)(check_run_in_editor: [bool](class_bool.md#class-bool)) static |
| void | [openxr_swapchain_acquire](class_openxrapiextension.md#class-openxrapiextension-method-openxr-swapchain-acquire)(swapchain: [int](class_int.md#class-int)) |
| [int](class_int.md#class-int) | [openxr_swapchain_create](class_openxrapiextension.md#class-openxrapiextension-method-openxr-swapchain-create)(create_flags: [int](class_int.md#class-int), usage_flags: [int](class_int.md#class-int), swapchain_format: [int](class_int.md#class-int), width: [int](class_int.md#class-int), height: [int](class_int.md#class-int), sample_count: [int](class_int.md#class-int), array_size: [int](class_int.md#class-int)) |
| void | [openxr_swapchain_free](class_openxrapiextension.md#class-openxrapiextension-method-openxr-swapchain-free)(swapchain: [int](class_int.md#class-int)) |
| [RID](class_rid.md#class-rid) | [openxr_swapchain_get_image](class_openxrapiextension.md#class-openxrapiextension-method-openxr-swapchain-get-image)(swapchain: [int](class_int.md#class-int)) |
| [int](class_int.md#class-int) | [openxr_swapchain_get_swapchain](class_openxrapiextension.md#class-openxrapiextension-method-openxr-swapchain-get-swapchain)(swapchain: [int](class_int.md#class-int)) |
| void | [openxr_swapchain_release](class_openxrapiextension.md#class-openxrapiextension-method-openxr-swapchain-release)(swapchain: [int](class_int.md#class-int)) |
| void | [register_composition_layer_provider](class_openxrapiextension.md#class-openxrapiextension-method-register-composition-layer-provider)(extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class-openxrextensionwrapper)) |
| void | [register_frame_info_extension](class_openxrapiextension.md#class-openxrapiextension-method-register-frame-info-extension)(extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class-openxrextensionwrapper)) |
| void | [register_projection_layer_extension](class_openxrapiextension.md#class-openxrapiextension-method-register-projection-layer-extension)(extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class-openxrextensionwrapper)) |
| void | [register_projection_views_extension](class_openxrapiextension.md#class-openxrapiextension-method-register-projection-views-extension)(extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class-openxrextensionwrapper)) |
| void | [set_custom_play_space](class_openxrapiextension.md#class-openxrapiextension-method-set-custom-play-space)(space: `const void*`) |
| void | [set_emulate_environment_blend_mode_alpha_blend](class_openxrapiextension.md#class-openxrapiextension-method-set-emulate-environment-blend-mode-alpha-blend)(enabled: [bool](class_bool.md#class-bool)) |
| void | [set_object_name](class_openxrapiextension.md#class-openxrapiextension-method-set-object-name)(object_type: [int](class_int.md#class-int), object_handle: [int](class_int.md#class-int), object_name: [String](class_string.md#class-string)) |
| void | [set_render_region](class_openxrapiextension.md#class-openxrapiextension-method-set-render-region)(render_region: [Rect2i](class_rect2i.md#class-rect2i)) |
| void | [set_velocity_depth_texture](class_openxrapiextension.md#class-openxrapiextension-method-set-velocity-depth-texture)(render_target: [RID](class_rid.md#class-rid)) |
| void | [set_velocity_target_size](class_openxrapiextension.md#class-openxrapiextension-method-set-velocity-target-size)(target_size: [Vector2i](class_vector2i.md#class-vector2i)) |
| void | [set_velocity_texture](class_openxrapiextension.md#class-openxrapiextension-method-set-velocity-texture)(render_target: [RID](class_rid.md#class-rid)) |
| [Transform3D](class_transform3d.md#class-transform3d) | [transform_from_pose](class_openxrapiextension.md#class-openxrapiextension-method-transform-from-pose)(pose: `const void*`) |
| void | [unregister_composition_layer_provider](class_openxrapiextension.md#class-openxrapiextension-method-unregister-composition-layer-provider)(extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class-openxrextensionwrapper)) |
| void | [unregister_frame_info_extension](class_openxrapiextension.md#class-openxrapiextension-method-unregister-frame-info-extension)(extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class-openxrextensionwrapper)) |
| void | [unregister_projection_layer_extension](class_openxrapiextension.md#class-openxrapiextension-method-unregister-projection-layer-extension)(extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class-openxrextensionwrapper)) |
| void | [unregister_projection_views_extension](class_openxrapiextension.md#class-openxrapiextension-method-unregister-projection-views-extension)(extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class-openxrextensionwrapper)) |
| void | [update_main_swapchain_size](class_openxrapiextension.md#class-openxrapiextension-method-update-main-swapchain-size)() |
| [bool](class_bool.md#class-bool) | [xr_result](class_openxrapiextension.md#class-openxrapiextension-method-xr-result)(result: [int](class_int.md#class-int), format: [String](class_string.md#class-string), args: [Array](class_array.md#class-array)) |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-openxrapiextension-openxralphablendmodesupport"></a>

enum **OpenXRAlphaBlendModeSupport**: [🔗](class_openxrapiextension.md#enum-openxrapiextension-openxralphablendmodesupport)

<a id="class-openxrapiextension-constant-openxr-alpha-blend-mode-support-none"></a>

[OpenXRAlphaBlendModeSupport](class_openxrapiextension.md#enum-openxrapiextension-openxralphablendmodesupport) **OPENXR_ALPHA_BLEND_MODE_SUPPORT_NONE** = `0`

Means that [XRInterface.XR_ENV_BLEND_MODE_ALPHA_BLEND](class_xrinterface.md#class-xrinterface-constant-xr-env-blend-mode-alpha-blend) isn't supported at all.

<a id="class-openxrapiextension-constant-openxr-alpha-blend-mode-support-real"></a>

[OpenXRAlphaBlendModeSupport](class_openxrapiextension.md#enum-openxrapiextension-openxralphablendmodesupport) **OPENXR_ALPHA_BLEND_MODE_SUPPORT_REAL** = `1`

Means that [XRInterface.XR_ENV_BLEND_MODE_ALPHA_BLEND](class_xrinterface.md#class-xrinterface-constant-xr-env-blend-mode-alpha-blend) is really supported.

<a id="class-openxrapiextension-constant-openxr-alpha-blend-mode-support-emulating"></a>

[OpenXRAlphaBlendModeSupport](class_openxrapiextension.md#enum-openxrapiextension-openxralphablendmodesupport) **OPENXR_ALPHA_BLEND_MODE_SUPPORT_EMULATING** = `2`

Means that [XRInterface.XR_ENV_BLEND_MODE_ALPHA_BLEND](class_xrinterface.md#class-xrinterface-constant-xr-env-blend-mode-alpha-blend) is emulated.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-openxrapiextension-method-action-get-handle"></a>

[int](class_int.md#class-int) **action_get_handle**(action: [RID](class_rid.md#class-rid)) [🔗](class_openxrapiextension.md#class-openxrapiextension-method-action-get-handle)

Returns the corresponding `XrAction` OpenXR handle for the given action RID.

---


<a id="class-openxrapiextension-method-begin-debug-label-region"></a>

void **begin_debug_label_region**(label_name: [String](class_string.md#class-string)) [🔗](class_openxrapiextension.md#class-openxrapiextension-method-begin-debug-label-region)

Begins a new debug label region, this label will be reported in debug messages for any calls following this until [end_debug_label_region()](class_openxrapiextension.md#class-openxrapiextension-method-end-debug-label-region) is called. Debug labels can be stacked.

---


<a id="class-openxrapiextension-method-can-render"></a>

[bool](class_bool.md#class-bool) **can_render**() [🔗](class_openxrapiextension.md#class-openxrapiextension-method-can-render)

Returns `true` if OpenXR is initialized for rendering with an XR viewport.

---


<a id="class-openxrapiextension-method-end-debug-label-region"></a>

void **end_debug_label_region**() [🔗](class_openxrapiextension.md#class-openxrapiextension-method-end-debug-label-region)

Marks the end of a debug label region. Removes the latest debug label region added by calling [begin_debug_label_region()](class_openxrapiextension.md#class-openxrapiextension-method-begin-debug-label-region).

---


<a id="class-openxrapiextension-method-find-action"></a>

[RID](class_rid.md#class-rid) **find_action**(name: [String](class_string.md#class-string), action_set: [RID](class_rid.md#class-rid)) [🔗](class_openxrapiextension.md#class-openxrapiextension-method-find-action)

Returns the [RID](class_rid.md#class-rid) corresponding to an `Action` of a matching name, optionally limited to a specified action set.

---


<a id="class-openxrapiextension-method-get-error-string"></a>

[String](class_string.md#class-string) **get_error_string**(result: [int](class_int.md#class-int)) [🔗](class_openxrapiextension.md#class-openxrapiextension-method-get-error-string)

Returns an error string for the given [XrResult](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrResult.html).

---


<a id="class-openxrapiextension-method-get-hand-tracker"></a>

[int](class_int.md#class-int) **get_hand_tracker**(hand_index: [int](class_int.md#class-int)) [🔗](class_openxrapiextension.md#class-openxrapiextension-method-get-hand-tracker)

Returns the corresponding `XRHandTrackerEXT` handle for the given hand index value.

---


<a id="class-openxrapiextension-method-get-instance"></a>

[int](class_int.md#class-int) **get_instance**() [🔗](class_openxrapiextension.md#class-openxrapiextension-method-get-instance)

Returns the [XrInstance](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrInstance.html) created during the initialization of the OpenXR API.

---


<a id="class-openxrapiextension-method-get-instance-proc-addr"></a>

[int](class_int.md#class-int) **get_instance_proc_addr**(name: [String](class_string.md#class-string)) [🔗](class_openxrapiextension.md#class-openxrapiextension-method-get-instance-proc-addr)

Returns the function pointer of the OpenXR function with the specified name, cast to an integer. If the function with the given name does not exist, the method returns `0`.

**Note:** `openxr/util.h` contains utility macros for acquiring OpenXR functions, e.g. `GDEXTENSION_INIT_XR_FUNC_V(xrCreateAction)`.

---


<a id="class-openxrapiextension-method-get-next-frame-time"></a>

[int](class_int.md#class-int) **get_next_frame_time**() [🔗](class_openxrapiextension.md#class-openxrapiextension-method-get-next-frame-time)

Returns the predicted display timing for the next frame.

---


<a id="class-openxrapiextension-method-get-openxr-version"></a>

[int](class_int.md#class-int) **get_openxr_version**() [🔗](class_openxrapiextension.md#class-openxrapiextension-method-get-openxr-version)

Returns the version of OpenXR that was initialized. Only valid after the OpenXR instance has been created. See [XR_MAKE_VERSION](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_MAKE_VERSION) for how the version is calculated.

---


<a id="class-openxrapiextension-method-get-play-space"></a>

[int](class_int.md#class-int) **get_play_space**() [🔗](class_openxrapiextension.md#class-openxrapiextension-method-get-play-space)

Returns the play space, which is an [XrSpace](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrSpace.html) cast to an integer.

---


<a id="class-openxrapiextension-method-get-predicted-display-time"></a>

[int](class_int.md#class-int) **get_predicted_display_time**() [🔗](class_openxrapiextension.md#class-openxrapiextension-method-get-predicted-display-time)

Returns the predicted display timing for the current frame.

---


<a id="class-openxrapiextension-method-get-projection-layer"></a>

[int](class_int.md#class-int) **get_projection_layer**() [🔗](class_openxrapiextension.md#class-openxrapiextension-method-get-projection-layer)

Returns a pointer to the render state's `XrCompositionLayerProjection` struct.

**Note:** This method should only be called from the rendering thread.

---


<a id="class-openxrapiextension-method-get-render-state-z-far"></a>

[float](class_float.md#class-float) **get_render_state_z_far**() [🔗](class_openxrapiextension.md#class-openxrapiextension-method-get-render-state-z-far)

Returns the far boundary value of the camera frustum.

**Note:** This is only accessible in the render thread.

---


<a id="class-openxrapiextension-method-get-render-state-z-near"></a>

[float](class_float.md#class-float) **get_render_state_z_near**() [🔗](class_openxrapiextension.md#class-openxrapiextension-method-get-render-state-z-near)

Returns the near boundary value of the camera frustum.

**Note:** This is only accessible in the render thread.

---


<a id="class-openxrapiextension-method-get-session"></a>

[int](class_int.md#class-int) **get_session**() [🔗](class_openxrapiextension.md#class-openxrapiextension-method-get-session)

Returns the OpenXR session, which is an [XrSession](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrSession.html) cast to an integer.

---


<a id="class-openxrapiextension-method-get-supported-swapchain-formats"></a>

[PackedInt64Array](class_packedint64array.md#class-packedint64array) **get_supported_swapchain_formats**() [🔗](class_openxrapiextension.md#class-openxrapiextension-method-get-supported-swapchain-formats)

Returns an array of supported swapchain formats.

---


<a id="class-openxrapiextension-method-get-swapchain-format-name"></a>

[String](class_string.md#class-string) **get_swapchain_format_name**(swapchain_format: [int](class_int.md#class-int)) [🔗](class_openxrapiextension.md#class-openxrapiextension-method-get-swapchain-format-name)

Returns the name of the specified swapchain format.

---


<a id="class-openxrapiextension-method-get-system-id"></a>

[int](class_int.md#class-int) **get_system_id**() [🔗](class_openxrapiextension.md#class-openxrapiextension-method-get-system-id)

Returns the ID of the system, which is an [XrSystemId](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrSystemId.html) cast to an integer.

---


<a id="class-openxrapiextension-method-get-view-configuration"></a>

[int](class_int.md#class-int) **get_view_configuration**() const [🔗](class_openxrapiextension.md#class-openxrapiextension-method-get-view-configuration)

Returns the view configuration type, which is an [XrViewConfigurationType](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrViewConfigurationType.html) cast to an integer.

---


<a id="class-openxrapiextension-method-get-view-count"></a>

[int](class_int.md#class-int) **get_view_count**() const [🔗](class_openxrapiextension.md#class-openxrapiextension-method-get-view-count)

Returns the number of views. It is usually two, one for each eye, but may differ with different view configurations.

---


<a id="class-openxrapiextension-method-insert-debug-label"></a>

void **insert_debug_label**(label_name: [String](class_string.md#class-string)) [🔗](class_openxrapiextension.md#class-openxrapiextension-method-insert-debug-label)

Inserts a debug label, this label is reported in any debug message resulting from the OpenXR calls that follows, until any of [begin_debug_label_region()](class_openxrapiextension.md#class-openxrapiextension-method-begin-debug-label-region), [end_debug_label_region()](class_openxrapiextension.md#class-openxrapiextension-method-end-debug-label-region), or [insert_debug_label()](class_openxrapiextension.md#class-openxrapiextension-method-insert-debug-label) is called.

---


<a id="class-openxrapiextension-method-is-environment-blend-mode-alpha-supported"></a>

[OpenXRAlphaBlendModeSupport](class_openxrapiextension.md#enum-openxrapiextension-openxralphablendmodesupport) **is_environment_blend_mode_alpha_supported**() [🔗](class_openxrapiextension.md#class-openxrapiextension-method-is-environment-blend-mode-alpha-supported)

Returns [OpenXRAlphaBlendModeSupport](class_openxrapiextension.md#enum-openxrapiextension-openxralphablendmodesupport) denoting if [XRInterface.XR_ENV_BLEND_MODE_ALPHA_BLEND](class_xrinterface.md#class-xrinterface-constant-xr-env-blend-mode-alpha-blend) is really supported, emulated or not supported at all.

---


<a id="class-openxrapiextension-method-is-initialized"></a>

[bool](class_bool.md#class-bool) **is_initialized**() [🔗](class_openxrapiextension.md#class-openxrapiextension-method-is-initialized)

Returns `true` if OpenXR is initialized.

---


<a id="class-openxrapiextension-method-is-running"></a>

[bool](class_bool.md#class-bool) **is_running**() [🔗](class_openxrapiextension.md#class-openxrapiextension-method-is-running)

Returns `true` if OpenXR is running ([xrBeginSession](https://registry.khronos.org/OpenXR/specs/1.0/man/html/xrBeginSession.html) was successfully called and the swapchains were created).

---


<a id="class-openxrapiextension-method-openxr-is-enabled"></a>

[bool](class_bool.md#class-bool) **openxr_is_enabled**(check_run_in_editor: [bool](class_bool.md#class-bool)) static [🔗](class_openxrapiextension.md#class-openxrapiextension-method-openxr-is-enabled)

Returns `true` if OpenXR is enabled.

---


<a id="class-openxrapiextension-method-openxr-swapchain-acquire"></a>

void **openxr_swapchain_acquire**(swapchain: [int](class_int.md#class-int)) [🔗](class_openxrapiextension.md#class-openxrapiextension-method-openxr-swapchain-acquire)

Acquires the image of the provided swapchain.

---


<a id="class-openxrapiextension-method-openxr-swapchain-create"></a>

[int](class_int.md#class-int) **openxr_swapchain_create**(create_flags: [int](class_int.md#class-int), usage_flags: [int](class_int.md#class-int), swapchain_format: [int](class_int.md#class-int), width: [int](class_int.md#class-int), height: [int](class_int.md#class-int), sample_count: [int](class_int.md#class-int), array_size: [int](class_int.md#class-int)) [🔗](class_openxrapiextension.md#class-openxrapiextension-method-openxr-swapchain-create)

Returns a pointer to a new swapchain created using the provided parameters.

---


<a id="class-openxrapiextension-method-openxr-swapchain-free"></a>

void **openxr_swapchain_free**(swapchain: [int](class_int.md#class-int)) [🔗](class_openxrapiextension.md#class-openxrapiextension-method-openxr-swapchain-free)

Destroys the provided swapchain and frees it from memory.

---


<a id="class-openxrapiextension-method-openxr-swapchain-get-image"></a>

[RID](class_rid.md#class-rid) **openxr_swapchain_get_image**(swapchain: [int](class_int.md#class-int)) [🔗](class_openxrapiextension.md#class-openxrapiextension-method-openxr-swapchain-get-image)

Returns the RID of the provided swapchain's image.

---


<a id="class-openxrapiextension-method-openxr-swapchain-get-swapchain"></a>

[int](class_int.md#class-int) **openxr_swapchain_get_swapchain**(swapchain: [int](class_int.md#class-int)) [🔗](class_openxrapiextension.md#class-openxrapiextension-method-openxr-swapchain-get-swapchain)

Returns the `XrSwapchain` handle of the provided swapchain.

---


<a id="class-openxrapiextension-method-openxr-swapchain-release"></a>

void **openxr_swapchain_release**(swapchain: [int](class_int.md#class-int)) [🔗](class_openxrapiextension.md#class-openxrapiextension-method-openxr-swapchain-release)

Releases the image of the provided swapchain.

---


<a id="class-openxrapiextension-method-register-composition-layer-provider"></a>

void **register_composition_layer_provider**(extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class-openxrextensionwrapper)) [🔗](class_openxrapiextension.md#class-openxrapiextension-method-register-composition-layer-provider)

Registers the given extension as a composition layer provider.

**Note:** This cannot be called after the OpenXR session has started. However, it can be called in [OpenXRExtensionWrapper._on_session_created()](class_openxrextensionwrapper.md#class-openxrextensionwrapper-private-method-on-session-created).

---


<a id="class-openxrapiextension-method-register-frame-info-extension"></a>

void **register_frame_info_extension**(extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class-openxrextensionwrapper)) [🔗](class_openxrapiextension.md#class-openxrapiextension-method-register-frame-info-extension)

Registers the given extension as modifying frame info via the [OpenXRExtensionWrapper._set_frame_wait_info_and_get_next_pointer()](class_openxrextensionwrapper.md#class-openxrextensionwrapper-private-method-set-frame-wait-info-and-get-next-pointer), [OpenXRExtensionWrapper._set_view_locate_info_and_get_next_pointer()](class_openxrextensionwrapper.md#class-openxrextensionwrapper-private-method-set-view-locate-info-and-get-next-pointer), or [OpenXRExtensionWrapper._set_frame_end_info_and_get_next_pointer()](class_openxrextensionwrapper.md#class-openxrextensionwrapper-private-method-set-frame-end-info-and-get-next-pointer) virtual methods.

**Note:** This cannot be called after the OpenXR session has started. However, it can be called in [OpenXRExtensionWrapper._on_session_created()](class_openxrextensionwrapper.md#class-openxrextensionwrapper-private-method-on-session-created).

---


<a id="class-openxrapiextension-method-register-projection-layer-extension"></a>

void **register_projection_layer_extension**(extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class-openxrextensionwrapper)) [🔗](class_openxrapiextension.md#class-openxrapiextension-method-register-projection-layer-extension)

Registers the given extension as modifying `XrCompositionLayerProjection` via the [OpenXRExtensionWrapper._set_projection_layer_and_get_next_pointer()](class_openxrextensionwrapper.md#class-openxrextensionwrapper-private-method-set-projection-layer-and-get-next-pointer) virtual method.

**Note:** This cannot be called after the OpenXR session has started. However, it can be called in [OpenXRExtensionWrapper._on_session_created()](class_openxrextensionwrapper.md#class-openxrextensionwrapper-private-method-on-session-created).

---


<a id="class-openxrapiextension-method-register-projection-views-extension"></a>

void **register_projection_views_extension**(extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class-openxrextensionwrapper)) [🔗](class_openxrapiextension.md#class-openxrapiextension-method-register-projection-views-extension)

Registers the given extension as a provider of additional data structures to projections views.

**Note:** This cannot be called after the OpenXR session has started. However, it can be called in [OpenXRExtensionWrapper._on_session_created()](class_openxrextensionwrapper.md#class-openxrextensionwrapper-private-method-on-session-created).

---


<a id="class-openxrapiextension-method-set-custom-play-space"></a>

void **set_custom_play_space**(space: `const void*`) [🔗](class_openxrapiextension.md#class-openxrapiextension-method-set-custom-play-space)

Sets the reference space used by OpenXR to the given [XrSpace](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrSpace.html) (cast to a `void *`).

---


<a id="class-openxrapiextension-method-set-emulate-environment-blend-mode-alpha-blend"></a>

void **set_emulate_environment_blend_mode_alpha_blend**(enabled: [bool](class_bool.md#class-bool)) [🔗](class_openxrapiextension.md#class-openxrapiextension-method-set-emulate-environment-blend-mode-alpha-blend)

If set to `true`, an OpenXR extension is loaded which is capable of emulating the [XRInterface.XR_ENV_BLEND_MODE_ALPHA_BLEND](class_xrinterface.md#class-xrinterface-constant-xr-env-blend-mode-alpha-blend) blend mode.

---


<a id="class-openxrapiextension-method-set-object-name"></a>

void **set_object_name**(object_type: [int](class_int.md#class-int), object_handle: [int](class_int.md#class-int), object_name: [String](class_string.md#class-string)) [🔗](class_openxrapiextension.md#class-openxrapiextension-method-set-object-name)

Set the object name of an OpenXR object, used for debug output. `object_type` must be a valid OpenXR `XrObjectType` enum and `object_handle` must be a valid OpenXR object handle.

---


<a id="class-openxrapiextension-method-set-render-region"></a>

void **set_render_region**(render_region: [Rect2i](class_rect2i.md#class-rect2i)) [🔗](class_openxrapiextension.md#class-openxrapiextension-method-set-render-region)

Sets the render region to `render_region`, overriding the normal render target's rect.

---


<a id="class-openxrapiextension-method-set-velocity-depth-texture"></a>

void **set_velocity_depth_texture**(render_target: [RID](class_rid.md#class-rid)) [🔗](class_openxrapiextension.md#class-openxrapiextension-method-set-velocity-depth-texture)

Sets the render target of the velocity depth texture.

---


<a id="class-openxrapiextension-method-set-velocity-target-size"></a>

void **set_velocity_target_size**(target_size: [Vector2i](class_vector2i.md#class-vector2i)) [🔗](class_openxrapiextension.md#class-openxrapiextension-method-set-velocity-target-size)

Sets the target size of the velocity and velocity depth textures.

---


<a id="class-openxrapiextension-method-set-velocity-texture"></a>

void **set_velocity_texture**(render_target: [RID](class_rid.md#class-rid)) [🔗](class_openxrapiextension.md#class-openxrapiextension-method-set-velocity-texture)

Sets the render target of the velocity texture.

---


<a id="class-openxrapiextension-method-transform-from-pose"></a>

[Transform3D](class_transform3d.md#class-transform3d) **transform_from_pose**(pose: `const void*`) [🔗](class_openxrapiextension.md#class-openxrapiextension-method-transform-from-pose)

Creates a [Transform3D](class_transform3d.md#class-transform3d) from an [XrPosef](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrPosef.html).

---


<a id="class-openxrapiextension-method-unregister-composition-layer-provider"></a>

void **unregister_composition_layer_provider**(extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class-openxrextensionwrapper)) [🔗](class_openxrapiextension.md#class-openxrapiextension-method-unregister-composition-layer-provider)

Unregisters the given extension as a composition layer provider.

**Note:** This cannot be called while the OpenXR session is still running.

---


<a id="class-openxrapiextension-method-unregister-frame-info-extension"></a>

void **unregister_frame_info_extension**(extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class-openxrextensionwrapper)) [🔗](class_openxrapiextension.md#class-openxrapiextension-method-unregister-frame-info-extension)

Unregisters the given extension as modifying frame info.

**Note:** This cannot be called while the OpenXR session is still running.

---


<a id="class-openxrapiextension-method-unregister-projection-layer-extension"></a>

void **unregister_projection_layer_extension**(extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class-openxrextensionwrapper)) [🔗](class_openxrapiextension.md#class-openxrapiextension-method-unregister-projection-layer-extension)

Unregisters the given extension as modifying `XrCompositionLayerProjection`.

**Note:** This cannot be called while the OpenXR session is still running.

---


<a id="class-openxrapiextension-method-unregister-projection-views-extension"></a>

void **unregister_projection_views_extension**(extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class-openxrextensionwrapper)) [🔗](class_openxrapiextension.md#class-openxrapiextension-method-unregister-projection-views-extension)

Unregisters the given extension as a provider of additional data structures to projections views.

**Note:** This cannot be called while the OpenXR session is still running.

---


<a id="class-openxrapiextension-method-update-main-swapchain-size"></a>

void **update_main_swapchain_size**() [🔗](class_openxrapiextension.md#class-openxrapiextension-method-update-main-swapchain-size)

Request the recommended resolution from the OpenXR runtime and update the main swapchain size if it has changed.

---


<a id="class-openxrapiextension-method-xr-result"></a>

[bool](class_bool.md#class-bool) **xr_result**(result: [int](class_int.md#class-int), format: [String](class_string.md#class-string), args: [Array](class_array.md#class-array)) [🔗](class_openxrapiextension.md#class-openxrapiextension-method-xr-result)

Returns `true` if the provided [XrResult](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrResult.html) (cast to an integer) is successful. Otherwise returns `false` and prints the [XrResult](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrResult.html) converted to a string, with the specified additional information.
