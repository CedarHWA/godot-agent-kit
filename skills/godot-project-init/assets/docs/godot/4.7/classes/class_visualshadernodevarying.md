> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodevarying.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodevarying"></a>

<a id="class-visualshadernodevarying"></a>

# VisualShaderNodeVarying

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [VisualShaderNodeVaryingGetter](class_visualshadernodevaryinggetter.md#class-visualshadernodevaryinggetter), [VisualShaderNodeVaryingSetter](class_visualshadernodevaryingsetter.md#class-visualshadernodevaryingsetter)

A visual shader node that represents a "varying" shader value.

<a id="description"></a>

## Description

Varying values are shader variables that can be passed between shader functions, e.g. from Vertex shader to Fragment shader.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [String](class_string.md#class-string) | [varying_name](class_visualshadernodevarying.md#class-visualshadernodevarying-property-varying-name) | `"[None]"` |
| [VaryingType](class_visualshader.md#enum-visualshader-varyingtype) | [varying_type](class_visualshadernodevarying.md#class-visualshadernodevarying-property-varying-type) | `0` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodevarying-property-varying-name"></a>

[String](class_string.md#class-string) **varying_name** = `"[None]"` [🔗](class_visualshadernodevarying.md#class-visualshadernodevarying-property-varying-name)

- void **set_varying_name**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_varying_name**()

Name of the variable. Must be unique.

---


<a id="class-visualshadernodevarying-property-varying-type"></a>

[VaryingType](class_visualshader.md#enum-visualshader-varyingtype) **varying_type** = `0` [🔗](class_visualshadernodevarying.md#class-visualshadernodevarying-property-varying-type)

- void **set_varying_type**(value: [VaryingType](class_visualshader.md#enum-visualshader-varyingtype))
- [VaryingType](class_visualshader.md#enum-visualshader-varyingtype) **get_varying_type**()

Type of the variable. Determines where the variable can be accessed.
