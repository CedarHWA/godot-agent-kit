> Source: https://docs.godotengine.org/en/4.7/classes/class_foldablegroup.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="foldablegroup"></a>

<a id="class-foldablegroup"></a>

# FoldableGroup

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A group of foldable containers that doesn't allow more than one container to be expanded at a time.

<a id="description"></a>

## Description

A group of [FoldableContainer](class_foldablecontainer.md#class-foldablecontainer)-derived nodes. Only one container can be expanded at a time.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [allow_folding_all](class_foldablegroup.md#class-foldablegroup-property-allow-folding-all) | `false` |
| [bool](class_bool.md#class-bool) | resource_local_to_scene | `true` (overrides [Resource](class_resource.md#class-resource-property-resource-local-to-scene)) |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Array](class_array.md#class-array)[[FoldableContainer](class_foldablecontainer.md#class-foldablecontainer)] | [get_containers](class_foldablegroup.md#class-foldablegroup-method-get-containers)() const |
| [FoldableContainer](class_foldablecontainer.md#class-foldablecontainer) | [get_expanded_container](class_foldablegroup.md#class-foldablegroup-method-get-expanded-container)() const |

---


<a id="signals"></a>

## Signals

<a id="class-foldablegroup-signal-expanded"></a>

**expanded**(container: [FoldableContainer](class_foldablecontainer.md#class-foldablecontainer)) [🔗](class_foldablegroup.md#class-foldablegroup-signal-expanded)

Emitted when one of the containers of the group is expanded.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-foldablegroup-property-allow-folding-all"></a>

[bool](class_bool.md#class-bool) **allow_folding_all** = `false` [🔗](class_foldablegroup.md#class-foldablegroup-property-allow-folding-all)

- void **set_allow_folding_all**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_allow_folding_all**()

If `true`, it is possible to fold all containers in this FoldableGroup.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-foldablegroup-method-get-containers"></a>

[Array](class_array.md#class-array)[[FoldableContainer](class_foldablecontainer.md#class-foldablecontainer)] **get_containers**() const [🔗](class_foldablegroup.md#class-foldablegroup-method-get-containers)

Returns an [Array](class_array.md#class-array) of [FoldableContainer](class_foldablecontainer.md#class-foldablecontainer)s that have this as their FoldableGroup (see [FoldableContainer.foldable_group](class_foldablecontainer.md#class-foldablecontainer-property-foldable-group)). This is equivalent to [ButtonGroup](class_buttongroup.md#class-buttongroup) but for FoldableContainers.

---


<a id="class-foldablegroup-method-get-expanded-container"></a>

[FoldableContainer](class_foldablecontainer.md#class-foldablecontainer) **get_expanded_container**() const [🔗](class_foldablegroup.md#class-foldablegroup-method-get-expanded-container)

Returns the current expanded container.
