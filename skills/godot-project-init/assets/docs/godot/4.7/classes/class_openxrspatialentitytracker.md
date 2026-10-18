> Source: https://docs.godotengine.org/en/4.7/classes/class_openxrspatialentitytracker.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxrspatialentitytracker"></a>

<a id="class-openxrspatialentitytracker"></a>

# OpenXRSpatialEntityTracker

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [XRPositionalTracker](class_xrpositionaltracker.md#class-xrpositionaltracker) **<** [XRTracker](class_xrtracker.md#class-xrtracker) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [OpenXRAnchorTracker](class_openxranchortracker.md#class-openxranchortracker), [OpenXRMarkerTracker](class_openxrmarkertracker.md#class-openxrmarkertracker), [OpenXRPlaneTracker](class_openxrplanetracker.md#class-openxrplanetracker)

Base class for Positional trackers managed by OpenXR's spatial entity extensions.

<a id="description"></a>

## Description

These are trackers created and managed by OpenXR's spatial entity extensions that give access to specific data related to OpenXR's spatial entities. They will always be of type `TRACKER_ANCHOR`.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [RID](class_rid.md#class-rid) | [entity](class_openxrspatialentitytracker.md#class-openxrspatialentitytracker-property-entity) | `RID()` |
| [EntityTrackingState](class_openxrspatialentitytracker.md#enum-openxrspatialentitytracker-entitytrackingstate) | [spatial_tracking_state](class_openxrspatialentitytracker.md#class-openxrspatialentitytracker-property-spatial-tracking-state) | `2` |
| [TrackerType](class_xrserver.md#enum-xrserver-trackertype) | type | `8` (overrides [XRTracker](class_xrtracker.md#class-xrtracker-property-type)) |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_next](class_openxrspatialentitytracker.md#class-openxrspatialentitytracker-method-add-next)(next: [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase)) |
| [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) | [get_next](class_openxrspatialentitytracker.md#class-openxrspatialentitytracker-method-get-next)() const |
| [RID](class_rid.md#class-rid) | [get_spatial_context](class_openxrspatialentitytracker.md#class-openxrspatialentitytracker-method-get-spatial-context)() const |
| void | [remove_next](class_openxrspatialentitytracker.md#class-openxrspatialentitytracker-method-remove-next)(next: [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase)) |
| void | [set_spatial_context](class_openxrspatialentitytracker.md#class-openxrspatialentitytracker-method-set-spatial-context)(spatial_context: [RID](class_rid.md#class-rid)) |

---


<a id="signals"></a>

## Signals

<a id="class-openxrspatialentitytracker-signal-next-changed"></a>

**next_changed**() [🔗](class_openxrspatialentitytracker.md#class-openxrspatialentitytracker-signal-next-changed)

Emitted when the next-chain changes, from either [add_next()](class_openxrspatialentitytracker.md#class-openxrspatialentitytracker-method-add-next) or [remove_next()](class_openxrspatialentitytracker.md#class-openxrspatialentitytracker-method-remove-next).

---


<a id="class-openxrspatialentitytracker-signal-spatial-tracking-state-changed"></a>

**spatial_tracking_state_changed**(spatial_tracking_state: [int](class_int.md#class-int)) [🔗](class_openxrspatialentitytracker.md#class-openxrspatialentitytracker-signal-spatial-tracking-state-changed)

There is currently no description for this signal. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-openxrspatialentitytracker-entitytrackingstate"></a>

enum **EntityTrackingState**: [🔗](class_openxrspatialentitytracker.md#enum-openxrspatialentitytracker-entitytrackingstate)

<a id="class-openxrspatialentitytracker-constant-entity-tracking-state-stopped"></a>

[EntityTrackingState](class_openxrspatialentitytracker.md#enum-openxrspatialentitytracker-entitytrackingstate) **ENTITY_TRACKING_STATE_STOPPED** = `1`

This anchor has stopped tracking.

<a id="class-openxrspatialentitytracker-constant-entity-tracking-state-paused"></a>

[EntityTrackingState](class_openxrspatialentitytracker.md#enum-openxrspatialentitytracker-entitytrackingstate) **ENTITY_TRACKING_STATE_PAUSED** = `2`

Tracking is currently paused.

<a id="class-openxrspatialentitytracker-constant-entity-tracking-state-tracking"></a>

[EntityTrackingState](class_openxrspatialentitytracker.md#enum-openxrspatialentitytracker-entitytrackingstate) **ENTITY_TRACKING_STATE_TRACKING** = `3`

This anchor is currently being tracked.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-openxrspatialentitytracker-property-entity"></a>

[RID](class_rid.md#class-rid) **entity** = `RID()` [🔗](class_openxrspatialentitytracker.md#class-openxrspatialentitytracker-property-entity)

- void **set_entity**(value: [RID](class_rid.md#class-rid))
- [RID](class_rid.md#class-rid) **get_entity**()

The spatial entity associated with this tracker.

---


<a id="class-openxrspatialentitytracker-property-spatial-tracking-state"></a>

[EntityTrackingState](class_openxrspatialentitytracker.md#enum-openxrspatialentitytracker-entitytrackingstate) **spatial_tracking_state** = `2` [🔗](class_openxrspatialentitytracker.md#class-openxrspatialentitytracker-property-spatial-tracking-state)

- void **set_spatial_tracking_state**(value: [EntityTrackingState](class_openxrspatialentitytracker.md#enum-openxrspatialentitytracker-entitytrackingstate))
- [EntityTrackingState](class_openxrspatialentitytracker.md#enum-openxrspatialentitytracker-entitytrackingstate) **get_spatial_tracking_state**()

The spatial tracking state for this tracker.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-openxrspatialentitytracker-method-add-next"></a>

void **add_next**(next: [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase)) [🔗](class_openxrspatialentitytracker.md#class-openxrspatialentitytracker-method-add-next)

Adds a new [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) to the next-chain.

[get_next()](class_openxrspatialentitytracker.md#class-openxrspatialentitytracker-method-get-next) will return this `next` until either [add_next()](class_openxrspatialentitytracker.md#class-openxrspatialentitytracker-method-add-next) is called again or it's removed in [remove_next()](class_openxrspatialentitytracker.md#class-openxrspatialentitytracker-method-remove-next).

---


<a id="class-openxrspatialentitytracker-method-get-next"></a>

[OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) **get_next**() const [🔗](class_openxrspatialentitytracker.md#class-openxrspatialentitytracker-method-get-next)

Gets the head [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) in the next-chain.

See also [add_next()](class_openxrspatialentitytracker.md#class-openxrspatialentitytracker-method-add-next) and [remove_next()](class_openxrspatialentitytracker.md#class-openxrspatialentitytracker-method-remove-next).

---


<a id="class-openxrspatialentitytracker-method-get-spatial-context"></a>

[RID](class_rid.md#class-rid) **get_spatial_context**() const [🔗](class_openxrspatialentitytracker.md#class-openxrspatialentitytracker-method-get-spatial-context)

Gets the spatial context used to create this **OpenXRSpatialEntityTracker**.

---


<a id="class-openxrspatialentitytracker-method-remove-next"></a>

void **remove_next**(next: [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase)) [🔗](class_openxrspatialentitytracker.md#class-openxrspatialentitytracker-method-remove-next)

Removes a `next` object previously added in [add_next()](class_openxrspatialentitytracker.md#class-openxrspatialentitytracker-method-add-next) from the next-chain.

---


<a id="class-openxrspatialentitytracker-method-set-spatial-context"></a>

void **set_spatial_context**(spatial_context: [RID](class_rid.md#class-rid)) [🔗](class_openxrspatialentitytracker.md#class-openxrspatialentitytracker-method-set-spatial-context)

Sets the spatial context used to create this tracker.
