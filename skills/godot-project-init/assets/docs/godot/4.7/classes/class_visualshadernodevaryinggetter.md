> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodevaryinggetter.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodevaryinggetter"></a>

<a id="class-visualshadernodevaryinggetter"></a>

# VisualShaderNodeVaryingGetter

**Inherits:** [VisualShaderNodeVarying](class_visualshadernodevarying.md#class-visualshadernodevarying) **<** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A visual shader node that gets a value of a varying.

<a id="description"></a>

## Description

Outputs a value of a varying defined in the shader. You need to first create a varying that can be used in the given function, e.g. varying getter in Fragment shader requires a varying with mode set to [VisualShader.VARYING_MODE_VERTEX_TO_FRAG_LIGHT](class_visualshader.md#class-visualshader-constant-varying-mode-vertex-to-frag-light).
