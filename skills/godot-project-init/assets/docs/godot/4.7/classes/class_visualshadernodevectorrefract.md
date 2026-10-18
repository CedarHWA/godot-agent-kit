> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodevectorrefract.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodevectorrefract"></a>

<a id="class-visualshadernodevectorrefract"></a>

# VisualShaderNodeVectorRefract

**Inherits:** [VisualShaderNodeVectorBase](class_visualshadernodevectorbase.md#class-visualshadernodevectorbase) **<** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Returns the vector that points in the direction of refraction. For use within the visual shader graph.

<a id="description"></a>

## Description

Translated to `refract(I, N, eta)` in the shader language, where `I` is the incident vector, `N` is the normal vector and `eta` is the ratio of the indices of the refraction.
