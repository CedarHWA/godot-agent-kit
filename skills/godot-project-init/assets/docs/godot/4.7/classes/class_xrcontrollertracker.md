> Source: https://docs.godotengine.org/en/4.7/classes/class_xrcontrollertracker.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="xrcontrollertracker"></a>

<a id="class-xrcontrollertracker"></a>

# XRControllerTracker

**Inherits:** [XRPositionalTracker](class_xrpositionaltracker.md#class-xrpositionaltracker) **<** [XRTracker](class_xrtracker.md#class-xrtracker) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A tracked controller.

<a id="description"></a>

## Description

An instance of this object represents a controller that is tracked.

As controllers are turned on and the [XRInterface](class_xrinterface.md#class-xrinterface) detects them, instances of this object are automatically added to this list of active tracking objects accessible through the [XRServer](class_xrserver.md#class-xrserver).

The [XRController3D](class_xrcontroller3d.md#class-xrcontroller3d) consumes objects of this type and should be used in your project.

<a id="tutorials"></a>

## Tutorials

- [XR documentation index](../tutorials/xr/index.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [TrackerType](class_xrserver.md#enum-xrserver-trackertype) | type | `2` (overrides [XRTracker](class_xrtracker.md#class-xrtracker-property-type)) |
