> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodetransformcompose.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodetransformcompose"></a>

<a id="class-visualshadernodetransformcompose"></a>

# VisualShaderNodeTransformCompose

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Composes a [Transform3D](class_transform3d.md#class-transform3d) from four [Vector3](class_vector3.md#class-vector3)s within the visual shader graph.

<a id="description"></a>

## Description

Creates a 4×4 transform matrix using four vectors of type `vec3`. Each vector is one row in the matrix and the last column is a `vec4(0, 0, 0, 1)`.
