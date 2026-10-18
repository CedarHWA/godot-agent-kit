> Source: https://docs.godotengine.org/en/4.7/classes/class_awaittweener.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="awaittweener"></a>

<a id="class-awaittweener"></a>

# AwaitTweener

**Inherits:** [Tweener](class_tweener.md#class-tweener) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Awaits a specified signal.

<a id="description"></a>

## Description

**AwaitTweener** is used to await a specified signal, allowing asynchronous steps in [Tween](class_tween.md#class-tween) animation. See [Tween.tween_await()](class_tween.md#class-tween-method-tween-await) for more usage information.

The [Tweener.finished](class_tweener.md#class-tweener-signal-finished) signal is emitted when either the awaited signal is received, when timeout is reached, or when the target object is freed.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [AwaitTweener](class_awaittweener.md#class-awaittweener) | [set_timeout](class_awaittweener.md#class-awaittweener-method-set-timeout)(timeout: [float](class_float.md#class-float)) |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-awaittweener-method-set-timeout"></a>

[AwaitTweener](class_awaittweener.md#class-awaittweener) **set_timeout**(timeout: [float](class_float.md#class-float)) [🔗](class_awaittweener.md#class-awaittweener-method-set-timeout)

Sets the maximum time an **AwaitTweener** can wait for the signal. Can be used as a safeguard for signals that may never be emitted. If not specified, the tweener will wait indefinitely.
