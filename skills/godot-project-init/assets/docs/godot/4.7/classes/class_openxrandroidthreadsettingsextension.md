> Source: https://docs.godotengine.org/en/4.7/classes/class_openxrandroidthreadsettingsextension.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxrandroidthreadsettingsextension"></a>

<a id="class-openxrandroidthreadsettingsextension"></a>

# OpenXRAndroidThreadSettingsExtension

**Inherits:** [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class-openxrextensionwrapper) **<** [Object](class_object.md#class-object)

Wraps the [XR_KHR_android_thread_settings](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_KHR_android_thread_settings) extension.

<a id="description"></a>

## Description

For XR to be comfortable, it is important for applications to deliver frames quickly and consistently. In order to make sure the important application threads get their full share of time, these threads must be identified to the system, which will adjust their scheduling priority accordingly.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [set_application_thread_type](class_openxrandroidthreadsettingsextension.md#class-openxrandroidthreadsettingsextension-method-set-application-thread-type)(thread_type: [ThreadType](class_openxrandroidthreadsettingsextension.md#enum-openxrandroidthreadsettingsextension-threadtype), thread_id: [int](class_int.md#class-int) = 0) |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-openxrandroidthreadsettingsextension-threadtype"></a>

enum **ThreadType**: [🔗](class_openxrandroidthreadsettingsextension.md#enum-openxrandroidthreadsettingsextension-threadtype)

<a id="class-openxrandroidthreadsettingsextension-constant-thread-type-application-main"></a>

[ThreadType](class_openxrandroidthreadsettingsextension.md#enum-openxrandroidthreadsettingsextension-threadtype) **THREAD_TYPE_APPLICATION_MAIN** = `0`

Hints to the XR runtime that the thread is doing time critical CPU tasks.

<a id="class-openxrandroidthreadsettingsextension-constant-thread-type-application-worker"></a>

[ThreadType](class_openxrandroidthreadsettingsextension.md#enum-openxrandroidthreadsettingsextension-threadtype) **THREAD_TYPE_APPLICATION_WORKER** = `1`

Hints to the XR runtime that the thread is doing background CPU tasks.

<a id="class-openxrandroidthreadsettingsextension-constant-thread-type-renderer-main"></a>

[ThreadType](class_openxrandroidthreadsettingsextension.md#enum-openxrandroidthreadsettingsextension-threadtype) **THREAD_TYPE_RENDERER_MAIN** = `2`

Hints to the XR runtime that the thread is doing time critical graphics device tasks.

<a id="class-openxrandroidthreadsettingsextension-constant-thread-type-renderer-worker"></a>

[ThreadType](class_openxrandroidthreadsettingsextension.md#enum-openxrandroidthreadsettingsextension-threadtype) **THREAD_TYPE_RENDERER_WORKER** = `3`

Hints to the XR runtime that the thread is doing background graphics device tasks.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-openxrandroidthreadsettingsextension-method-set-application-thread-type"></a>

[bool](class_bool.md#class-bool) **set_application_thread_type**(thread_type: [ThreadType](class_openxrandroidthreadsettingsextension.md#enum-openxrandroidthreadsettingsextension-threadtype), thread_id: [int](class_int.md#class-int) = 0) [🔗](class_openxrandroidthreadsettingsextension.md#class-openxrandroidthreadsettingsextension-method-set-application-thread-type)

Sets the thread type of the given thread, so that the XR runtime can adjust its scheduling priority accordingly.

`thread_id` refers to the OS thread id (ie from `gettid()`). When `thread_id` is `0`, it will set the thread type of the current thread.

**NOTE:** The id returned by [Thread.get_id()](class_thread.md#class-thread-method-get-id) is incompatible with `thread_id`.
