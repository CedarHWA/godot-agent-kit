> Source: https://docs.godotengine.org/en/4.7/classes/class_openxrinteractionprofile.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxrinteractionprofile"></a>

<a id="class-openxrinteractionprofile"></a>

# OpenXRInteractionProfile

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Suggested bindings object for OpenXR.

<a id="description"></a>

## Description

This object stores suggested bindings for an interaction profile. Interaction profiles define the metadata for a tracked XR device such as an XR controller.

For more information see the [interaction profiles info in the OpenXR specification](https://www.khronos.org/registry/OpenXR/specs/1.0/html/xrspec.html#semantic-path-interaction-profiles).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Array](class_array.md#class-array) | [binding_modifiers](class_openxrinteractionprofile.md#class-openxrinteractionprofile-property-binding-modifiers) | `[]` |
| [Array](class_array.md#class-array) | [bindings](class_openxrinteractionprofile.md#class-openxrinteractionprofile-property-bindings) | `[]` |
| [String](class_string.md#class-string) | [interaction_profile_path](class_openxrinteractionprofile.md#class-openxrinteractionprofile-property-interaction-profile-path) | `""` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [OpenXRIPBinding](class_openxripbinding.md#class-openxripbinding) | [get_binding](class_openxrinteractionprofile.md#class-openxrinteractionprofile-method-get-binding)(index: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_binding_count](class_openxrinteractionprofile.md#class-openxrinteractionprofile-method-get-binding-count)() const |
| [OpenXRIPBindingModifier](class_openxripbindingmodifier.md#class-openxripbindingmodifier) | [get_binding_modifier](class_openxrinteractionprofile.md#class-openxrinteractionprofile-method-get-binding-modifier)(index: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_binding_modifier_count](class_openxrinteractionprofile.md#class-openxrinteractionprofile-method-get-binding-modifier-count)() const |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-openxrinteractionprofile-property-binding-modifiers"></a>

[Array](class_array.md#class-array) **binding_modifiers** = `[]` [🔗](class_openxrinteractionprofile.md#class-openxrinteractionprofile-property-binding-modifiers)

- void **set_binding_modifiers**(value: [Array](class_array.md#class-array))
- [Array](class_array.md#class-array) **get_binding_modifiers**()

Binding modifiers for this interaction profile.

---


<a id="class-openxrinteractionprofile-property-bindings"></a>

[Array](class_array.md#class-array) **bindings** = `[]` [🔗](class_openxrinteractionprofile.md#class-openxrinteractionprofile-property-bindings)

- void **set_bindings**(value: [Array](class_array.md#class-array))
- [Array](class_array.md#class-array) **get_bindings**()

Action bindings for this interaction profile.

---


<a id="class-openxrinteractionprofile-property-interaction-profile-path"></a>

[String](class_string.md#class-string) **interaction_profile_path** = `""` [🔗](class_openxrinteractionprofile.md#class-openxrinteractionprofile-property-interaction-profile-path)

- void **set_interaction_profile_path**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_interaction_profile_path**()

The interaction profile path identifying the XR device.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-openxrinteractionprofile-method-get-binding"></a>

[OpenXRIPBinding](class_openxripbinding.md#class-openxripbinding) **get_binding**(index: [int](class_int.md#class-int)) const [🔗](class_openxrinteractionprofile.md#class-openxrinteractionprofile-method-get-binding)

Retrieve the binding at this index.

---


<a id="class-openxrinteractionprofile-method-get-binding-count"></a>

[int](class_int.md#class-int) **get_binding_count**() const [🔗](class_openxrinteractionprofile.md#class-openxrinteractionprofile-method-get-binding-count)

Get the number of bindings in this interaction profile.

---


<a id="class-openxrinteractionprofile-method-get-binding-modifier"></a>

[OpenXRIPBindingModifier](class_openxripbindingmodifier.md#class-openxripbindingmodifier) **get_binding_modifier**(index: [int](class_int.md#class-int)) const [🔗](class_openxrinteractionprofile.md#class-openxrinteractionprofile-method-get-binding-modifier)

Get the [OpenXRBindingModifier](class_openxrbindingmodifier.md#class-openxrbindingmodifier) at this index.

---


<a id="class-openxrinteractionprofile-method-get-binding-modifier-count"></a>

[int](class_int.md#class-int) **get_binding_modifier_count**() const [🔗](class_openxrinteractionprofile.md#class-openxrinteractionprofile-method-get-binding-modifier-count)

Get the number of binding modifiers in this interaction profile.
