> Source: https://docs.godotengine.org/en/4.7/classes/class_callbacktweener.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="callbacktweener"></a>

<a id="class-callbacktweener"></a>

# CallbackTweener

**Inherits:** [Tweener](class_tweener.md#class-tweener) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Calls the specified method after optional delay.

<a id="description"></a>

## Description

**CallbackTweener** is used to call a method in a tweening sequence. See [Tween.tween_callback()](class_tween.md#class-tween-method-tween-callback) for more usage information.

The tweener will finish automatically if the callback's target object is freed.

**Note:** [Tween.tween_callback()](class_tween.md#class-tween-method-tween-callback) is the only correct way to create **CallbackTweener**. Any **CallbackTweener** created manually will not function correctly.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [CallbackTweener](class_callbacktweener.md#class-callbacktweener) | [set_delay](class_callbacktweener.md#class-callbacktweener-method-set-delay)(delay: [float](class_float.md#class-float)) |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-callbacktweener-method-set-delay"></a>

[CallbackTweener](class_callbacktweener.md#class-callbacktweener) **set_delay**(delay: [float](class_float.md#class-float)) [🔗](class_callbacktweener.md#class-callbacktweener-method-set-delay)

Makes the callback call delayed by given time in seconds.

**Example:** Call [Node.queue_free()](class_node.md#class-node-method-queue-free) after 2 seconds:

```gdscript
var tween = get_tree().create_tween()
tween.tween_callback(queue_free).set_delay(2)
```
