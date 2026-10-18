> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodeif.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodeif"></a>

<a id="class-visualshadernodeif"></a>

# VisualShaderNodeIf

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Outputs a 3D vector based on the result of a floating-point comparison within the visual shader graph.

<a id="description"></a>

## Description

This visual shader node has six input ports:

- Port **1** and **2** provide the two floating-point numbers `a` and `b` that will be compared.
- Port **3** is the tolerance, which allows similar floating-point numbers to be considered equal.
- Ports **4**, **5**, and **6** are the possible outputs, returned if `a == b`, `a > b`, or `a < b` respectively.
