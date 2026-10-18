> Source: https://docs.godotengine.org/en/4.7/classes/class_animationnodetimeseek.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="animationnodetimeseek"></a>

<a id="class-animationnodetimeseek"></a>

# AnimationNodeTimeSeek

**Inherits:** [AnimationNode](class_animationnode.md#class-animationnode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A time-seeking animation node used in [AnimationTree](class_animationtree.md#class-animationtree).

<a id="description"></a>

## Description

This animation node can be used to cause a seek command to happen to any sub-children of the animation graph. Use to play an [Animation](class_animation.md#class-animation) from the start or a certain playback position inside the [AnimationNodeBlendTree](class_animationnodeblendtree.md#class-animationnodeblendtree).

After setting the time and changing the animation playback, the time seek node automatically goes into sleep mode on the next process frame by setting its `seek_request` value to `-1.0`.

```gdscript
# Play child animation from the start.
animation_tree.set("parameters/TimeSeek/seek_request", 0.0)
# Alternative syntax (same result as above).
animation_tree["parameters/TimeSeek/seek_request"] = 0.0

# Play child animation from 12 second timestamp.
animation_tree.set("parameters/TimeSeek/seek_request", 12.0)
# Alternative syntax (same result as above).
animation_tree["parameters/TimeSeek/seek_request"] = 12.0
```

```csharp
// Play child animation from the start.
animationTree.Set("parameters/TimeSeek/seek_request", 0.0);

// Play child animation from 12 second timestamp.
animationTree.Set("parameters/TimeSeek/seek_request", 12.0);
```

<a id="tutorials"></a>

## Tutorials

- [Using AnimationTree](../tutorials/animation/animation_tree.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [explicit_elapse](class_animationnodetimeseek.md#class-animationnodetimeseek-property-explicit-elapse) | `true` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-animationnodetimeseek-property-explicit-elapse"></a>

[bool](class_bool.md#class-bool) **explicit_elapse** = `true` [🔗](class_animationnodetimeseek.md#class-animationnodetimeseek-property-explicit-elapse)

- void **set_explicit_elapse**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_explicit_elapse**()

If `true`, some processes are executed to handle keys between seeks, such as calculating root motion and finding the nearest discrete key.
