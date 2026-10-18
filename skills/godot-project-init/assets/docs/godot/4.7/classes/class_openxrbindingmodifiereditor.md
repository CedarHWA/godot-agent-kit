> Source: https://docs.godotengine.org/en/4.7/classes/class_openxrbindingmodifiereditor.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxrbindingmodifiereditor"></a>

<a id="class-openxrbindingmodifiereditor"></a>

# OpenXRBindingModifierEditor

**Inherits:** [PanelContainer](class_panelcontainer.md#class-panelcontainer) **<** [Container](class_container.md#class-container) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Binding modifier editor.

<a id="description"></a>

## Description

This is the default binding modifier editor used in the OpenXR action map.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [OpenXRBindingModifier](class_openxrbindingmodifier.md#class-openxrbindingmodifier) | [get_binding_modifier](class_openxrbindingmodifiereditor.md#class-openxrbindingmodifiereditor-method-get-binding-modifier)() const |
| void | [setup](class_openxrbindingmodifiereditor.md#class-openxrbindingmodifiereditor-method-setup)(action_map: [OpenXRActionMap](class_openxractionmap.md#class-openxractionmap), binding_modifier: [OpenXRBindingModifier](class_openxrbindingmodifier.md#class-openxrbindingmodifier)) |

---


<a id="signals"></a>

## Signals

<a id="class-openxrbindingmodifiereditor-signal-binding-modifier-removed"></a>

**binding_modifier_removed**(binding_modifier_editor: [Object](class_object.md#class-object)) [🔗](class_openxrbindingmodifiereditor.md#class-openxrbindingmodifiereditor-signal-binding-modifier-removed)

Signal emitted when the user presses the delete binding modifier button for this modifier.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-openxrbindingmodifiereditor-method-get-binding-modifier"></a>

[OpenXRBindingModifier](class_openxrbindingmodifier.md#class-openxrbindingmodifier) **get_binding_modifier**() const [🔗](class_openxrbindingmodifiereditor.md#class-openxrbindingmodifiereditor-method-get-binding-modifier)

Returns the [OpenXRBindingModifier](class_openxrbindingmodifier.md#class-openxrbindingmodifier) currently being edited.

---


<a id="class-openxrbindingmodifiereditor-method-setup"></a>

void **setup**(action_map: [OpenXRActionMap](class_openxractionmap.md#class-openxractionmap), binding_modifier: [OpenXRBindingModifier](class_openxrbindingmodifier.md#class-openxrbindingmodifier)) [🔗](class_openxrbindingmodifiereditor.md#class-openxrbindingmodifiereditor-method-setup)

Setup this editor for the provided `action_map` and `binding_modifier`.
