> Source: https://docs.godotengine.org/en/4.7/classes/class_animationnodeadd2.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="animationnodeadd2"></a>

<a id="class-animationnodeadd2"></a>

# AnimationNodeAdd2

**Inherits:** [AnimationNodeSync](class_animationnodesync.md#class-animationnodesync) **<** [AnimationNode](class_animationnode.md#class-animationnode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Blends two animations additively inside of an [AnimationNodeBlendTree](class_animationnodeblendtree.md#class-animationnodeblendtree).

<a id="description"></a>

## Description

A resource to add to an [AnimationNodeBlendTree](class_animationnodeblendtree.md#class-animationnodeblendtree). Blends two animations additively based on the amount value.

If the amount is greater than `1.0`, the animation connected to "in" port is blended with the amplified animation connected to "add" port.

If the amount is less than `0.0`, the animation connected to "in" port is blended with the inverted animation connected to "add" port.

<a id="tutorials"></a>

## Tutorials

- [Using AnimationTree](../tutorials/animation/animation_tree.md)
