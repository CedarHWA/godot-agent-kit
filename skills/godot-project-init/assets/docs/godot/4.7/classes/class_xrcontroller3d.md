> Source: https://docs.godotengine.org/en/4.7/classes/class_xrcontroller3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="xrcontroller3d"></a>

<a id="class-xrcontroller3d"></a>

# XRController3D

**Inherits:** [XRNode3D](class_xrnode3d.md#class-xrnode3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A 3D node representing a spatially-tracked controller.

<a id="description"></a>

## Description

This is a helper 3D node that is linked to the tracking of controllers. It also offers several handy passthroughs to the state of buttons and such on the controllers.

Controllers are linked by their ID. You can create controller nodes before the controllers are available. If your game always uses two controllers (one for each hand), you can predefine the controllers with ID 1 and 2; they will become active as soon as the controllers are identified. If you expect additional controllers to be used, you should react to the signals and add XRController3D nodes to your scene.

The position of the controller node is automatically updated by the [XRServer](class_xrserver.md#class-xrserver). This makes this node ideal to add child nodes to visualize the controller.

The current [XRInterface](class_xrinterface.md#class-xrinterface) defines the names of inputs. In the case of OpenXR, these are the names of actions in the current action set from the OpenXR action map.

<a id="tutorials"></a>

## Tutorials

- [XR documentation index](../tutorials/xr/index.md)

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [float](class_float.md#class-float) | [get_float](class_xrcontroller3d.md#class-xrcontroller3d-method-get-float)(name: [StringName](class_stringname.md#class-stringname)) const |
| [Variant](class_variant.md#class-variant) | [get_input](class_xrcontroller3d.md#class-xrcontroller3d-method-get-input)(name: [StringName](class_stringname.md#class-stringname)) const |
| [TrackerHand](class_xrpositionaltracker.md#enum-xrpositionaltracker-trackerhand) | [get_tracker_hand](class_xrcontroller3d.md#class-xrcontroller3d-method-get-tracker-hand)() const |
| [Vector2](class_vector2.md#class-vector2) | [get_vector2](class_xrcontroller3d.md#class-xrcontroller3d-method-get-vector2)(name: [StringName](class_stringname.md#class-stringname)) const |
| [bool](class_bool.md#class-bool) | [is_button_pressed](class_xrcontroller3d.md#class-xrcontroller3d-method-is-button-pressed)(name: [StringName](class_stringname.md#class-stringname)) const |

---


<a id="signals"></a>

## Signals

<a id="class-xrcontroller3d-signal-button-pressed"></a>

**button_pressed**(action_name: [String](class_string.md#class-string)) [🔗](class_xrcontroller3d.md#class-xrcontroller3d-signal-button-pressed)

Emitted when a button on this controller is pressed.

---


<a id="class-xrcontroller3d-signal-button-released"></a>

**button_released**(action_name: [String](class_string.md#class-string)) [🔗](class_xrcontroller3d.md#class-xrcontroller3d-signal-button-released)

Emitted when a button on this controller is released.

---


<a id="class-xrcontroller3d-signal-input-float-changed"></a>

**input_float_changed**(action_name: [String](class_string.md#class-string), value: [float](class_float.md#class-float)) [🔗](class_xrcontroller3d.md#class-xrcontroller3d-signal-input-float-changed)

Emitted when a trigger or similar input on this controller changes value.

---


<a id="class-xrcontroller3d-signal-input-vector2-changed"></a>

**input_vector2_changed**(action_name: [String](class_string.md#class-string), value: [Vector2](class_vector2.md#class-vector2)) [🔗](class_xrcontroller3d.md#class-xrcontroller3d-signal-input-vector2-changed)

Emitted when a thumbstick or thumbpad on this controller is moved.

---


<a id="class-xrcontroller3d-signal-profile-changed"></a>

**profile_changed**(role: [String](class_string.md#class-string)) [🔗](class_xrcontroller3d.md#class-xrcontroller3d-signal-profile-changed)

Emitted when the interaction profile on this controller is changed.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-xrcontroller3d-method-get-float"></a>

[float](class_float.md#class-float) **get_float**(name: [StringName](class_stringname.md#class-stringname)) const [🔗](class_xrcontroller3d.md#class-xrcontroller3d-method-get-float)

Returns a numeric value for the input with the given `name`. This is used for triggers and grip sensors.

**Note:** The current [XRInterface](class_xrinterface.md#class-xrinterface) defines the `name` for each input. In the case of OpenXR, these are the names of actions in the current action set.

---


<a id="class-xrcontroller3d-method-get-input"></a>

[Variant](class_variant.md#class-variant) **get_input**(name: [StringName](class_stringname.md#class-stringname)) const [🔗](class_xrcontroller3d.md#class-xrcontroller3d-method-get-input)

Returns a [Variant](class_variant.md#class-variant) for the input with the given `name`. This works for any input type, the variant will be typed according to the actions configuration.

**Note:** The current [XRInterface](class_xrinterface.md#class-xrinterface) defines the `name` for each input. In the case of OpenXR, these are the names of actions in the current action set.

---


<a id="class-xrcontroller3d-method-get-tracker-hand"></a>

[TrackerHand](class_xrpositionaltracker.md#enum-xrpositionaltracker-trackerhand) **get_tracker_hand**() const [🔗](class_xrcontroller3d.md#class-xrcontroller3d-method-get-tracker-hand)

Returns the hand holding this controller, if known.

---


<a id="class-xrcontroller3d-method-get-vector2"></a>

[Vector2](class_vector2.md#class-vector2) **get_vector2**(name: [StringName](class_stringname.md#class-stringname)) const [🔗](class_xrcontroller3d.md#class-xrcontroller3d-method-get-vector2)

Returns a [Vector2](class_vector2.md#class-vector2) for the input with the given `name`. This is used for thumbsticks and thumbpads found on many controllers.

**Note:** The current [XRInterface](class_xrinterface.md#class-xrinterface) defines the `name` for each input. In the case of OpenXR, these are the names of actions in the current action set.

---


<a id="class-xrcontroller3d-method-is-button-pressed"></a>

[bool](class_bool.md#class-bool) **is_button_pressed**(name: [StringName](class_stringname.md#class-stringname)) const [🔗](class_xrcontroller3d.md#class-xrcontroller3d-method-is-button-pressed)

Returns `true` if the button with the given `name` is pressed.

**Note:** The current [XRInterface](class_xrinterface.md#class-xrinterface) defines the `name` for each input. In the case of OpenXR, these are the names of actions in the current action set.
