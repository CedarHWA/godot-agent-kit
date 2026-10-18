> Source: https://docs.godotengine.org/en/4.7/classes/class_openxractionset.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxractionset"></a>

<a id="class-openxractionset"></a>

# OpenXRActionSet

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Collection of [OpenXRAction](class_openxraction.md#class-openxraction) resources that make up an action set.

<a id="description"></a>

## Description

Action sets in OpenXR define a collection of actions that can be activated in unison. This allows games to easily change between different states that require different inputs or need to reinterpret inputs. For instance we could have an action set that is active when a menu is open, an action set that is active when the player is freely walking around and an action set that is active when the player is controlling a vehicle.

Action sets can contain the same action with the same name, if such action sets are active at the same time the action set with the highest priority defines which binding is active.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Array](class_array.md#class-array) | [actions](class_openxractionset.md#class-openxractionset-property-actions) | `[]` |
| [String](class_string.md#class-string) | [localized_name](class_openxractionset.md#class-openxractionset-property-localized-name) | `""` |
| [int](class_int.md#class-int) | [priority](class_openxractionset.md#class-openxractionset-property-priority) | `0` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_action](class_openxractionset.md#class-openxractionset-method-add-action)(action: [OpenXRAction](class_openxraction.md#class-openxraction)) |
| [int](class_int.md#class-int) | [get_action_count](class_openxractionset.md#class-openxractionset-method-get-action-count)() const |
| void | [remove_action](class_openxractionset.md#class-openxractionset-method-remove-action)(action: [OpenXRAction](class_openxraction.md#class-openxraction)) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-openxractionset-property-actions"></a>

[Array](class_array.md#class-array) **actions** = `[]` [🔗](class_openxractionset.md#class-openxractionset-property-actions)

- void **set_actions**(value: [Array](class_array.md#class-array))
- [Array](class_array.md#class-array) **get_actions**()

Collection of actions for this action set.

---


<a id="class-openxractionset-property-localized-name"></a>

[String](class_string.md#class-string) **localized_name** = `""` [🔗](class_openxractionset.md#class-openxractionset-property-localized-name)

- void **set_localized_name**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_localized_name**()

The localized name of this action set.

---


<a id="class-openxractionset-property-priority"></a>

[int](class_int.md#class-int) **priority** = `0` [🔗](class_openxractionset.md#class-openxractionset-property-priority)

- void **set_priority**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_priority**()

The priority for this action set.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-openxractionset-method-add-action"></a>

void **add_action**(action: [OpenXRAction](class_openxraction.md#class-openxraction)) [🔗](class_openxractionset.md#class-openxractionset-method-add-action)

Add an action to this action set.

---


<a id="class-openxractionset-method-get-action-count"></a>

[int](class_int.md#class-int) **get_action_count**() const [🔗](class_openxractionset.md#class-openxractionset-method-get-action-count)

Retrieve the number of actions in our action set.

---


<a id="class-openxractionset-method-remove-action"></a>

void **remove_action**(action: [OpenXRAction](class_openxraction.md#class-openxraction)) [🔗](class_openxractionset.md#class-openxractionset-method-remove-action)

Remove an action from this action set.
