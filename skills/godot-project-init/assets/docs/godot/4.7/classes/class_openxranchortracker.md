> Source: https://docs.godotengine.org/en/4.7/classes/class_openxranchortracker.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxranchortracker"></a>

<a id="class-openxranchortracker"></a>

# OpenXRAnchorTracker

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialEntityTracker](class_openxrspatialentitytracker.md#class-openxrspatialentitytracker) **<** [XRPositionalTracker](class_xrpositionaltracker.md#class-xrpositionaltracker) **<** [XRTracker](class_xrtracker.md#class-xrtracker) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Positional tracker for our spatial entity anchor extension.

<a id="description"></a>

## Description

Positional tracker for our OpenXR spatial entity anchor extension, it tracks a user defined location in real space and maps it to our virtual space.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [String](class_string.md#class-string) | [uuid](class_openxranchortracker.md#class-openxranchortracker-property-uuid) | `""` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [has_uuid](class_openxranchortracker.md#class-openxranchortracker-method-has-uuid)() const |

---


<a id="signals"></a>

## Signals

<a id="class-openxranchortracker-signal-uuid-changed"></a>

**uuid_changed**() [🔗](class_openxranchortracker.md#class-openxranchortracker-signal-uuid-changed)

Emitted when the UUID for this anchor was changed.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-openxranchortracker-property-uuid"></a>

[String](class_string.md#class-string) **uuid** = `""` [🔗](class_openxranchortracker.md#class-openxranchortracker-property-uuid)

- void **set_uuid**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_uuid**()

The UUID provided for persistent anchors.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-openxranchortracker-method-has-uuid"></a>

[bool](class_bool.md#class-bool) **has_uuid**() const [🔗](class_openxranchortracker.md#class-openxranchortracker-method-has-uuid)

Returns `true` if a non-zero UUID is set.
