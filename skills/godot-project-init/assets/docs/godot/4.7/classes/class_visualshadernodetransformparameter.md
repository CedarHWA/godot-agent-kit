> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodetransformparameter.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodetransformparameter"></a>

<a id="class-visualshadernodetransformparameter"></a>

# VisualShaderNodeTransformParameter

**Inherits:** [VisualShaderNodeParameter](class_visualshadernodeparameter.md#class-visualshadernodeparameter) **<** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A [Transform3D](class_transform3d.md#class-transform3d) parameter for use within the visual shader graph.

<a id="description"></a>

## Description

Translated to `uniform mat4` in the shader language.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Transform3D](class_transform3d.md#class-transform3d) | [default_value](class_visualshadernodetransformparameter.md#class-visualshadernodetransformparameter-property-default-value) | `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)` |
| [bool](class_bool.md#class-bool) | [default_value_enabled](class_visualshadernodetransformparameter.md#class-visualshadernodetransformparameter-property-default-value-enabled) | `false` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-visualshadernodetransformparameter-property-default-value"></a>

[Transform3D](class_transform3d.md#class-transform3d) **default_value** = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)` [🔗](class_visualshadernodetransformparameter.md#class-visualshadernodetransformparameter-property-default-value)

- void **set_default_value**(value: [Transform3D](class_transform3d.md#class-transform3d))
- [Transform3D](class_transform3d.md#class-transform3d) **get_default_value**()

A default value to be assigned within the shader.

---


<a id="class-visualshadernodetransformparameter-property-default-value-enabled"></a>

[bool](class_bool.md#class-bool) **default_value_enabled** = `false` [🔗](class_visualshadernodetransformparameter.md#class-visualshadernodetransformparameter-property-default-value-enabled)

- void **set_default_value_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_default_value_enabled**()

Enables usage of the [default_value](class_visualshadernodetransformparameter.md#class-visualshadernodetransformparameter-property-default-value).
