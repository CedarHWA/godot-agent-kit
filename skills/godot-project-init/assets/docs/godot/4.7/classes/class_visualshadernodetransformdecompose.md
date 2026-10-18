> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodetransformdecompose.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodetransformdecompose"></a>

<a id="class-visualshadernodetransformdecompose"></a>

# VisualShaderNodeTransformDecompose

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Decomposes a [Transform3D](class_transform3d.md#class-transform3d) into four [Vector3](class_vector3.md#class-vector3)s within the visual shader graph.

<a id="description"></a>

## Description

Takes a 4×4 transform matrix and decomposes it into four `vec3` values, one from each row of the matrix.
