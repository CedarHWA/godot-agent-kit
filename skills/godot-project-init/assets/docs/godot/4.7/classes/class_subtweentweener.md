> Source: https://docs.godotengine.org/en/4.7/classes/class_subtweentweener.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="subtweentweener"></a>

<a id="class-subtweentweener"></a>

# SubtweenTweener

**Inherits:** [Tweener](class_tweener.md#class-tweener) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Runs a [Tween](class_tween.md#class-tween) nested within another [Tween](class_tween.md#class-tween).

<a id="description"></a>

## Description

**SubtweenTweener** is used to execute a [Tween](class_tween.md#class-tween) as one step in a sequence defined by another [Tween](class_tween.md#class-tween). See [Tween.tween_subtween()](class_tween.md#class-tween-method-tween-subtween) for more usage information.

**Note:** [Tween.tween_subtween()](class_tween.md#class-tween-method-tween-subtween) is the only correct way to create **SubtweenTweener**. Any **SubtweenTweener** created manually will not function correctly.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [SubtweenTweener](class_subtweentweener.md#class-subtweentweener) | [set_delay](class_subtweentweener.md#class-subtweentweener-method-set-delay)(delay: [float](class_float.md#class-float)) |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-subtweentweener-method-set-delay"></a>

[SubtweenTweener](class_subtweentweener.md#class-subtweentweener) **set_delay**(delay: [float](class_float.md#class-float)) [🔗](class_subtweentweener.md#class-subtweentweener-method-set-delay)

Sets the time in seconds after which the **SubtweenTweener** will start running the subtween. By default there's no delay.
