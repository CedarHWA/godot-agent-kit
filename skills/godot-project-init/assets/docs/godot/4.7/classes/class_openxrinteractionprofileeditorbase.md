> Source: https://docs.godotengine.org/en/4.7/classes/class_openxrinteractionprofileeditorbase.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxrinteractionprofileeditorbase"></a>

<a id="class-openxrinteractionprofileeditorbase"></a>

# OpenXRInteractionProfileEditorBase

**Inherits:** [HBoxContainer](class_hboxcontainer.md#class-hboxcontainer) **<** [BoxContainer](class_boxcontainer.md#class-boxcontainer) **<** [Container](class_container.md#class-container) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [OpenXRInteractionProfileEditor](class_openxrinteractionprofileeditor.md#class-openxrinteractionprofileeditor)

Base class for editing interaction profiles.

<a id="description"></a>

## Description

This is a base class for interaction profile editors used by the OpenXR action map editor. It can be used to create bespoke editors for specific interaction profiles.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [setup](class_openxrinteractionprofileeditorbase.md#class-openxrinteractionprofileeditorbase-method-setup)(action_map: [OpenXRActionMap](class_openxractionmap.md#class-openxractionmap), interaction_profile: [OpenXRInteractionProfile](class_openxrinteractionprofile.md#class-openxrinteractionprofile)) |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-openxrinteractionprofileeditorbase-method-setup"></a>

void **setup**(action_map: [OpenXRActionMap](class_openxractionmap.md#class-openxractionmap), interaction_profile: [OpenXRInteractionProfile](class_openxrinteractionprofile.md#class-openxrinteractionprofile)) [🔗](class_openxrinteractionprofileeditorbase.md#class-openxrinteractionprofileeditorbase-method-setup)

Setup this editor for the provided `action_map` and `interaction_profile`.
