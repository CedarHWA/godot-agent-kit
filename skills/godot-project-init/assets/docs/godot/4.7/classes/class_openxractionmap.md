> Source: https://docs.godotengine.org/en/4.7/classes/class_openxractionmap.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxractionmap"></a>

<a id="class-openxractionmap"></a>

# OpenXRActionMap

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Collection of [OpenXRActionSet](class_openxractionset.md#class-openxractionset) and [OpenXRInteractionProfile](class_openxrinteractionprofile.md#class-openxrinteractionprofile) resources for the OpenXR module.

<a id="description"></a>

## Description

OpenXR uses an action system similar to Godots Input map system to bind inputs and outputs on various types of XR controllers to named actions. OpenXR specifies more detail on these inputs and outputs than Godot supports.

Another important distinction is that OpenXR offers no control over these bindings. The bindings we register are suggestions, it is up to the XR runtime to offer users the ability to change these bindings. This allows the XR runtime to fill in the gaps if new hardware becomes available.

The action map therefore needs to be loaded at startup and can't be changed afterwards. This resource is a container for the entire action map.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Array](class_array.md#class-array) | [action_sets](class_openxractionmap.md#class-openxractionmap-property-action-sets) | `[]` |
| [Array](class_array.md#class-array) | [interaction_profiles](class_openxractionmap.md#class-openxractionmap-property-interaction-profiles) | `[]` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_action_set](class_openxractionmap.md#class-openxractionmap-method-add-action-set)(action_set: [OpenXRActionSet](class_openxractionset.md#class-openxractionset)) |
| void | [add_interaction_profile](class_openxractionmap.md#class-openxractionmap-method-add-interaction-profile)(interaction_profile: [OpenXRInteractionProfile](class_openxrinteractionprofile.md#class-openxrinteractionprofile)) |
| void | [create_default_action_sets](class_openxractionmap.md#class-openxractionmap-method-create-default-action-sets)() |
| [OpenXRActionSet](class_openxractionset.md#class-openxractionset) | [find_action_set](class_openxractionmap.md#class-openxractionmap-method-find-action-set)(name: [String](class_string.md#class-string)) const |
| [OpenXRInteractionProfile](class_openxrinteractionprofile.md#class-openxrinteractionprofile) | [find_interaction_profile](class_openxractionmap.md#class-openxractionmap-method-find-interaction-profile)(name: [String](class_string.md#class-string)) const |
| [OpenXRActionSet](class_openxractionset.md#class-openxractionset) | [get_action_set](class_openxractionmap.md#class-openxractionmap-method-get-action-set)(idx: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_action_set_count](class_openxractionmap.md#class-openxractionmap-method-get-action-set-count)() const |
| [OpenXRInteractionProfile](class_openxrinteractionprofile.md#class-openxrinteractionprofile) | [get_interaction_profile](class_openxractionmap.md#class-openxractionmap-method-get-interaction-profile)(idx: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_interaction_profile_count](class_openxractionmap.md#class-openxractionmap-method-get-interaction-profile-count)() const |
| void | [remove_action_set](class_openxractionmap.md#class-openxractionmap-method-remove-action-set)(action_set: [OpenXRActionSet](class_openxractionset.md#class-openxractionset)) |
| void | [remove_interaction_profile](class_openxractionmap.md#class-openxractionmap-method-remove-interaction-profile)(interaction_profile: [OpenXRInteractionProfile](class_openxrinteractionprofile.md#class-openxrinteractionprofile)) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-openxractionmap-property-action-sets"></a>

[Array](class_array.md#class-array) **action_sets** = `[]` [🔗](class_openxractionmap.md#class-openxractionmap-property-action-sets)

- void **set_action_sets**(value: [Array](class_array.md#class-array))
- [Array](class_array.md#class-array) **get_action_sets**()

Collection of [OpenXRActionSet](class_openxractionset.md#class-openxractionset)s that are part of this action map.

---


<a id="class-openxractionmap-property-interaction-profiles"></a>

[Array](class_array.md#class-array) **interaction_profiles** = `[]` [🔗](class_openxractionmap.md#class-openxractionmap-property-interaction-profiles)

- void **set_interaction_profiles**(value: [Array](class_array.md#class-array))
- [Array](class_array.md#class-array) **get_interaction_profiles**()

Collection of [OpenXRInteractionProfile](class_openxrinteractionprofile.md#class-openxrinteractionprofile)s that are part of this action map.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-openxractionmap-method-add-action-set"></a>

void **add_action_set**(action_set: [OpenXRActionSet](class_openxractionset.md#class-openxractionset)) [🔗](class_openxractionmap.md#class-openxractionmap-method-add-action-set)

Add an action set.

---


<a id="class-openxractionmap-method-add-interaction-profile"></a>

void **add_interaction_profile**(interaction_profile: [OpenXRInteractionProfile](class_openxrinteractionprofile.md#class-openxrinteractionprofile)) [🔗](class_openxractionmap.md#class-openxractionmap-method-add-interaction-profile)

Add an interaction profile.

---


<a id="class-openxractionmap-method-create-default-action-sets"></a>

void **create_default_action_sets**() [🔗](class_openxractionmap.md#class-openxractionmap-method-create-default-action-sets)

Setup this action set with our default actions.

---


<a id="class-openxractionmap-method-find-action-set"></a>

[OpenXRActionSet](class_openxractionset.md#class-openxractionset) **find_action_set**(name: [String](class_string.md#class-string)) const [🔗](class_openxractionmap.md#class-openxractionmap-method-find-action-set)

Retrieve an action set by name.

---


<a id="class-openxractionmap-method-find-interaction-profile"></a>

[OpenXRInteractionProfile](class_openxrinteractionprofile.md#class-openxrinteractionprofile) **find_interaction_profile**(name: [String](class_string.md#class-string)) const [🔗](class_openxractionmap.md#class-openxractionmap-method-find-interaction-profile)

Find an interaction profile by its name (path).

---


<a id="class-openxractionmap-method-get-action-set"></a>

[OpenXRActionSet](class_openxractionset.md#class-openxractionset) **get_action_set**(idx: [int](class_int.md#class-int)) const [🔗](class_openxractionmap.md#class-openxractionmap-method-get-action-set)

Retrieve the action set at this index.

---


<a id="class-openxractionmap-method-get-action-set-count"></a>

[int](class_int.md#class-int) **get_action_set_count**() const [🔗](class_openxractionmap.md#class-openxractionmap-method-get-action-set-count)

Retrieve the number of actions sets in our action map.

---


<a id="class-openxractionmap-method-get-interaction-profile"></a>

[OpenXRInteractionProfile](class_openxrinteractionprofile.md#class-openxrinteractionprofile) **get_interaction_profile**(idx: [int](class_int.md#class-int)) const [🔗](class_openxractionmap.md#class-openxractionmap-method-get-interaction-profile)

Get the interaction profile at this index.

---


<a id="class-openxractionmap-method-get-interaction-profile-count"></a>

[int](class_int.md#class-int) **get_interaction_profile_count**() const [🔗](class_openxractionmap.md#class-openxractionmap-method-get-interaction-profile-count)

Retrieve the number of interaction profiles in our action map.

---


<a id="class-openxractionmap-method-remove-action-set"></a>

void **remove_action_set**(action_set: [OpenXRActionSet](class_openxractionset.md#class-openxractionset)) [🔗](class_openxractionmap.md#class-openxractionmap-method-remove-action-set)

Remove an action set.

---


<a id="class-openxractionmap-method-remove-interaction-profile"></a>

void **remove_interaction_profile**(interaction_profile: [OpenXRInteractionProfile](class_openxrinteractionprofile.md#class-openxrinteractionprofile)) [🔗](class_openxractionmap.md#class-openxractionmap-method-remove-interaction-profile)

Remove an interaction profile.
