> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodeouterproduct.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodeouterproduct"></a>

<a id="class-visualshadernodeouterproduct"></a>

# VisualShaderNodeOuterProduct

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Calculates an outer product of two vectors within the visual shader graph.

<a id="description"></a>

## Description

`OuterProduct` treats the first parameter `c` as a column vector (matrix with one column) and the second parameter `r` as a row vector (matrix with one row) and does a linear algebraic matrix multiply `c * r`, yielding a matrix whose number of rows is the number of components in `c` and whose number of columns is the number of components in `r`.
