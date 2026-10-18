> Source: https://docs.godotengine.org/en/4.7/classes/class_animationnodeblend3.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="animationnodeblend3"></a>

<a id="class-animationnodeblend3"></a>

# AnimationNodeBlend3

**Inherits:** [AnimationNodeSync](class_animationnodesync.md#class-animationnodesync) **<** [AnimationNode](class_animationnode.md#class-animationnode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Blends two of three animations linearly inside of an [AnimationNodeBlendTree](class_animationnodeblendtree.md#class-animationnodeblendtree).

<a id="description"></a>

## Description

A resource to add to an [AnimationNodeBlendTree](class_animationnodeblendtree.md#class-animationnodeblendtree). Blends two animations out of three linearly out of three based on the amount value.

This animation node has three inputs:

- The base animation to blend with
- A "-blend" animation to blend with when the blend amount is negative value
- A "+blend" animation to blend with when the blend amount is positive value

In general, the blend value should be in the `[-1.0, 1.0]` range. Values outside of this range can blend amplified animations, however, [AnimationNodeAdd3](class_animationnodeadd3.md#class-animationnodeadd3) works better for this purpose.

<a id="tutorials"></a>

## Tutorials

- [Using AnimationTree](../tutorials/animation/animation_tree.md)
