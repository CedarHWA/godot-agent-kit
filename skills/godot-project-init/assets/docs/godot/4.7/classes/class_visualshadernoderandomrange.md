> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernoderandomrange.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernoderandomrange"></a>

<a id="class-visualshadernoderandomrange"></a>

# VisualShaderNodeRandomRange

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A visual shader node that generates a pseudo-random scalar.

<a id="description"></a>

## Description

Random range node will output a pseudo-random scalar value in the specified range, based on the seed. The value is always the same for the given seed and range, so you should provide a changing input, e.g. by using time.
