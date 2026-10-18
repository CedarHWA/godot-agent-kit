> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodeworldpositionfromdepth.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodeworldpositionfromdepth"></a>

<a id="class-visualshadernodeworldpositionfromdepth"></a>

# VisualShaderNodeWorldPositionFromDepth

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A visual shader node that calculates the position of the pixel in world space using the depth texture.

<a id="description"></a>

## Description

The WorldPositionFromDepth node reconstructs the depth position of the pixel in world space. This can be used to obtain world space UVs for projection mapping like Caustics.
