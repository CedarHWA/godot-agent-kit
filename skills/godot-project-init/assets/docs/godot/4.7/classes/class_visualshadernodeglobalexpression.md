> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodeglobalexpression.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodeglobalexpression"></a>

<a id="class-visualshadernodeglobalexpression"></a>

# VisualShaderNodeGlobalExpression

**Inherits:** [VisualShaderNodeExpression](class_visualshadernodeexpression.md#class-visualshadernodeexpression) **<** [VisualShaderNodeGroupBase](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase) **<** [VisualShaderNodeResizableBase](class_visualshadernoderesizablebase.md#class-visualshadernoderesizablebase) **<** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A custom global visual shader graph expression written in Godot Shading Language.

<a id="description"></a>

## Description

Custom Godot Shader Language expression, which is placed on top of the generated shader. You can place various function definitions inside to call later in [VisualShaderNodeExpression](class_visualshadernodeexpression.md#class-visualshadernodeexpression)s (which are injected in the main shader functions). You can also declare varyings, uniforms and global constants.
