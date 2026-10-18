> Source: https://docs.godotengine.org/en/4.7/classes/class_animationlibrary.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="animationlibrary"></a>

<a id="class-animationlibrary"></a>

# AnimationLibrary

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Container for [Animation](class_animation.md#class-animation) resources.

<a id="description"></a>

## Description

An animation library stores a set of animations accessible through [StringName](class_stringname.md#class-stringname) keys, for use with [AnimationPlayer](class_animationplayer.md#class-animationplayer) nodes.

<a id="tutorials"></a>

## Tutorials

- [Animation tutorial index](../tutorials/animation/index.md)

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Error](class_@globalscope.md#enum-globalscope-error) | [add_animation](class_animationlibrary.md#class-animationlibrary-method-add-animation)(name: [StringName](class_stringname.md#class-stringname), animation: [Animation](class_animation.md#class-animation)) |
| [Animation](class_animation.md#class-animation) | [get_animation](class_animationlibrary.md#class-animationlibrary-method-get-animation)(name: [StringName](class_stringname.md#class-stringname)) const |
| [Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] | [get_animation_list](class_animationlibrary.md#class-animationlibrary-method-get-animation-list)() const |
| [int](class_int.md#class-int) | [get_animation_list_size](class_animationlibrary.md#class-animationlibrary-method-get-animation-list-size)() const |
| [bool](class_bool.md#class-bool) | [has_animation](class_animationlibrary.md#class-animationlibrary-method-has-animation)(name: [StringName](class_stringname.md#class-stringname)) const |
| void | [remove_animation](class_animationlibrary.md#class-animationlibrary-method-remove-animation)(name: [StringName](class_stringname.md#class-stringname)) |
| void | [rename_animation](class_animationlibrary.md#class-animationlibrary-method-rename-animation)(name: [StringName](class_stringname.md#class-stringname), newname: [StringName](class_stringname.md#class-stringname)) |

---


<a id="signals"></a>

## Signals

<a id="class-animationlibrary-signal-animation-added"></a>

**animation_added**(anim_name: [StringName](class_stringname.md#class-stringname)) [🔗](class_animationlibrary.md#class-animationlibrary-signal-animation-added)

Emitted when an [Animation](class_animation.md#class-animation) is added, under the key `anim_name`.

---


<a id="class-animationlibrary-signal-animation-changed"></a>

**animation_changed**(anim_name: [StringName](class_stringname.md#class-stringname)) [🔗](class_animationlibrary.md#class-animationlibrary-signal-animation-changed)

Emitted when there's a change in one of the animations, e.g. tracks are added, moved or have changed paths. `anim_name` is the key of the animation that was changed.

See also [Resource.changed](class_resource.md#class-resource-signal-changed), which this acts as a relay for.

---


<a id="class-animationlibrary-signal-animation-removed"></a>

**animation_removed**(anim_name: [StringName](class_stringname.md#class-stringname)) [🔗](class_animationlibrary.md#class-animationlibrary-signal-animation-removed)

Emitted when an [Animation](class_animation.md#class-animation) stored with the key `anim_name` is removed.

---


<a id="class-animationlibrary-signal-animation-renamed"></a>

**animation_renamed**(old_name: [StringName](class_stringname.md#class-stringname), new_name: [StringName](class_stringname.md#class-stringname)) [🔗](class_animationlibrary.md#class-animationlibrary-signal-animation-renamed)

Emitted when the key for an [Animation](class_animation.md#class-animation) is changed, from `old_name` to `new_name`.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-animationlibrary-method-add-animation"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **add_animation**(name: [StringName](class_stringname.md#class-stringname), animation: [Animation](class_animation.md#class-animation)) [🔗](class_animationlibrary.md#class-animationlibrary-method-add-animation)

Adds the `animation` to the library, accessible by the key `name`.

---


<a id="class-animationlibrary-method-get-animation"></a>

[Animation](class_animation.md#class-animation) **get_animation**(name: [StringName](class_stringname.md#class-stringname)) const [🔗](class_animationlibrary.md#class-animationlibrary-method-get-animation)

Returns the [Animation](class_animation.md#class-animation) with the key `name`. If the animation does not exist, `null` is returned and an error is logged.

---


<a id="class-animationlibrary-method-get-animation-list"></a>

[Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] **get_animation_list**() const [🔗](class_animationlibrary.md#class-animationlibrary-method-get-animation-list)

Returns the keys for the [Animation](class_animation.md#class-animation)s stored in the library.

---


<a id="class-animationlibrary-method-get-animation-list-size"></a>

[int](class_int.md#class-int) **get_animation_list_size**() const [🔗](class_animationlibrary.md#class-animationlibrary-method-get-animation-list-size)

Returns the key count for the [Animation](class_animation.md#class-animation)s stored in the library.

---


<a id="class-animationlibrary-method-has-animation"></a>

[bool](class_bool.md#class-bool) **has_animation**(name: [StringName](class_stringname.md#class-stringname)) const [🔗](class_animationlibrary.md#class-animationlibrary-method-has-animation)

Returns `true` if the library stores an [Animation](class_animation.md#class-animation) with `name` as the key.

---


<a id="class-animationlibrary-method-remove-animation"></a>

void **remove_animation**(name: [StringName](class_stringname.md#class-stringname)) [🔗](class_animationlibrary.md#class-animationlibrary-method-remove-animation)

Removes the [Animation](class_animation.md#class-animation) with the key `name`.

---


<a id="class-animationlibrary-method-rename-animation"></a>

void **rename_animation**(name: [StringName](class_stringname.md#class-stringname), newname: [StringName](class_stringname.md#class-stringname)) [🔗](class_animationlibrary.md#class-animationlibrary-method-rename-animation)

Changes the key of the [Animation](class_animation.md#class-animation) associated with the key `name` to `newname`.
