> Source: https://docs.godotengine.org/en/4.7/classes/class_openxrfutureresult.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxrfutureresult"></a>

<a id="class-openxrfutureresult"></a>

# OpenXRFutureResult

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Result object tracking the asynchronous result of an OpenXR Future object.

<a id="description"></a>

## Description

Result object tracking the asynchronous result of an OpenXR Future object, you can use this object to track the result status.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [cancel_future](class_openxrfutureresult.md#class-openxrfutureresult-method-cancel-future)() |
| [int](class_int.md#class-int) | [get_future](class_openxrfutureresult.md#class-openxrfutureresult-method-get-future)() const |
| [Variant](class_variant.md#class-variant) | [get_result_value](class_openxrfutureresult.md#class-openxrfutureresult-method-get-result-value)() const |
| [ResultStatus](class_openxrfutureresult.md#enum-openxrfutureresult-resultstatus) | [get_status](class_openxrfutureresult.md#class-openxrfutureresult-method-get-status)() const |
| void | [set_result_value](class_openxrfutureresult.md#class-openxrfutureresult-method-set-result-value)(result_value: [Variant](class_variant.md#class-variant)) |

---


<a id="signals"></a>

## Signals

<a id="class-openxrfutureresult-signal-completed"></a>

**completed**(result: [OpenXRFutureResult](class_openxrfutureresult.md#class-openxrfutureresult)) [🔗](class_openxrfutureresult.md#class-openxrfutureresult-signal-completed)

Emitted when the asynchronous function is finished or has been cancelled.

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-openxrfutureresult-resultstatus"></a>

enum **ResultStatus**: [🔗](class_openxrfutureresult.md#enum-openxrfutureresult-resultstatus)

<a id="class-openxrfutureresult-constant-result-running"></a>

[ResultStatus](class_openxrfutureresult.md#enum-openxrfutureresult-resultstatus) **RESULT_RUNNING** = `0`

The asynchronous function is running.

<a id="class-openxrfutureresult-constant-result-finished"></a>

[ResultStatus](class_openxrfutureresult.md#enum-openxrfutureresult-resultstatus) **RESULT_FINISHED** = `1`

The asynchronous function has finished.

<a id="class-openxrfutureresult-constant-result-cancelled"></a>

[ResultStatus](class_openxrfutureresult.md#enum-openxrfutureresult-resultstatus) **RESULT_CANCELLED** = `2`

The asynchronous function has been cancelled.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-openxrfutureresult-method-cancel-future"></a>

void **cancel_future**() [🔗](class_openxrfutureresult.md#class-openxrfutureresult-method-cancel-future)

Cancel this future, this will interrupt and stop the asynchronous function.

---


<a id="class-openxrfutureresult-method-get-future"></a>

[int](class_int.md#class-int) **get_future**() const [🔗](class_openxrfutureresult.md#class-openxrfutureresult-method-get-future)

Return the `XrFutureEXT` value this result relates to.

---


<a id="class-openxrfutureresult-method-get-result-value"></a>

[Variant](class_variant.md#class-variant) **get_result_value**() const [🔗](class_openxrfutureresult.md#class-openxrfutureresult-method-get-result-value)

Returns the result value of our asynchronous function (if set by the extension). The type of this result value depends on the function being called. Consult the documentation of the relevant function.

---


<a id="class-openxrfutureresult-method-get-status"></a>

[ResultStatus](class_openxrfutureresult.md#enum-openxrfutureresult-resultstatus) **get_status**() const [🔗](class_openxrfutureresult.md#class-openxrfutureresult-method-get-status)

Returns the status of this result.

---


<a id="class-openxrfutureresult-method-set-result-value"></a>

void **set_result_value**(result_value: [Variant](class_variant.md#class-variant)) [🔗](class_openxrfutureresult.md#class-openxrfutureresult-method-set-result-value)

Stores the result value we expose to the user.

**Note:** This method should only be called by an OpenXR extension that implements an asynchronous function.
