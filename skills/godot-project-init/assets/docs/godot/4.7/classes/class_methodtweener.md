> Source: https://docs.godotengine.org/en/4.7/classes/class_methodtweener.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="methodtweener"></a>

<a id="class-methodtweener"></a>

# MethodTweener

**Inherits:** [Tweener](class_tweener.md#class-tweener) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Interpolates an abstract value and supplies it to a method called over time.

<a id="description"></a>

## Description

**MethodTweener** is similar to a combination of [CallbackTweener](class_callbacktweener.md#class-callbacktweener) and [PropertyTweener](class_propertytweener.md#class-propertytweener). It calls a method providing an interpolated value as a parameter. See [Tween.tween_method()](class_tween.md#class-tween-method-tween-method) for more usage information.

The tweener will finish automatically if the callback's target object is freed.

**Note:** [Tween.tween_method()](class_tween.md#class-tween-method-tween-method) is the only correct way to create **MethodTweener**. Any **MethodTweener** created manually will not function correctly.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [MethodTweener](class_methodtweener.md#class-methodtweener) | [set_delay](class_methodtweener.md#class-methodtweener-method-set-delay)(delay: [float](class_float.md#class-float)) |
| [MethodTweener](class_methodtweener.md#class-methodtweener) | [set_ease](class_methodtweener.md#class-methodtweener-method-set-ease)(ease: [EaseType](class_tween.md#enum-tween-easetype)) |
| [MethodTweener](class_methodtweener.md#class-methodtweener) | [set_trans](class_methodtweener.md#class-methodtweener-method-set-trans)(trans: [TransitionType](class_tween.md#enum-tween-transitiontype)) |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-methodtweener-method-set-delay"></a>

[MethodTweener](class_methodtweener.md#class-methodtweener) **set_delay**(delay: [float](class_float.md#class-float)) [🔗](class_methodtweener.md#class-methodtweener-method-set-delay)

Sets the time in seconds after which the **MethodTweener** will start interpolating. By default there's no delay.

---


<a id="class-methodtweener-method-set-ease"></a>

[MethodTweener](class_methodtweener.md#class-methodtweener) **set_ease**(ease: [EaseType](class_tween.md#enum-tween-easetype)) [🔗](class_methodtweener.md#class-methodtweener-method-set-ease)

Sets the type of used easing from [EaseType](class_tween.md#enum-tween-easetype). If not set, the default easing is used from the [Tween](class_tween.md#class-tween) that contains this Tweener.

---


<a id="class-methodtweener-method-set-trans"></a>

[MethodTweener](class_methodtweener.md#class-methodtweener) **set_trans**(trans: [TransitionType](class_tween.md#enum-tween-transitiontype)) [🔗](class_methodtweener.md#class-methodtweener-method-set-trans)

Sets the type of used transition from [TransitionType](class_tween.md#enum-tween-transitiontype). If not set, the default transition is used from the [Tween](class_tween.md#class-tween) that contains this Tweener.
