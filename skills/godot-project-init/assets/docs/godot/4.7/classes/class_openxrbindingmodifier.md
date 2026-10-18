> Source: https://docs.godotengine.org/en/4.7/classes/class_openxrbindingmodifier.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxrbindingmodifier"></a>

<a id="class-openxrbindingmodifier"></a>

# OpenXRBindingModifier

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [OpenXRActionBindingModifier](class_openxractionbindingmodifier.md#class-openxractionbindingmodifier), [OpenXRIPBindingModifier](class_openxripbindingmodifier.md#class-openxripbindingmodifier)

Binding modifier base class.

<a id="description"></a>

## Description

Binding modifier base class. Subclasses implement various modifiers that alter how an OpenXR runtime processes inputs.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [String](class_string.md#class-string) | [_get_description](class_openxrbindingmodifier.md#class-openxrbindingmodifier-private-method-get-description)() virtual required const |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray) | [_get_ip_modification](class_openxrbindingmodifier.md#class-openxrbindingmodifier-private-method-get-ip-modification)() virtual required |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-openxrbindingmodifier-private-method-get-description"></a>

[String](class_string.md#class-string) **_get_description**() virtual required const [🔗](class_openxrbindingmodifier.md#class-openxrbindingmodifier-private-method-get-description)

Return the description of this class that is used for the title bar of the binding modifier editor.

---


<a id="class-openxrbindingmodifier-private-method-get-ip-modification"></a>

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **_get_ip_modification**() virtual required [🔗](class_openxrbindingmodifier.md#class-openxrbindingmodifier-private-method-get-ip-modification)

Returns the data that is sent to OpenXR when submitting the suggested interacting bindings this modifier is a part of.

**Note:** This must be data compatible with an `XrBindingModificationBaseHeaderKHR` structure.
