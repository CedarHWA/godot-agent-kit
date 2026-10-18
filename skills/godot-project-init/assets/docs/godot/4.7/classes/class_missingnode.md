> Source: https://docs.godotengine.org/en/4.7/classes/class_missingnode.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="missingnode"></a>

<a id="class-missingnode"></a>

# MissingNode

**Inherits:** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

An internal editor class intended for keeping the data of unrecognized nodes.

<a id="description"></a>

## Description

This is an internal editor class intended for keeping data of nodes of unknown type (most likely this type was supplied by an extension that is no longer loaded). It can't be manually instantiated or placed in a scene.

**Warning:** Ignore missing nodes unless you know what you are doing. Existing properties on a missing node can be freely modified in code, regardless of the type they are intended to be.

<a id="properties"></a>

## Properties

|  |  |
| --- | --- |
| [String](class_string.md#class-string) | [original_class](class_missingnode.md#class-missingnode-property-original-class) |
| [String](class_string.md#class-string) | [original_scene](class_missingnode.md#class-missingnode-property-original-scene) |
| [bool](class_bool.md#class-bool) | [recording_properties](class_missingnode.md#class-missingnode-property-recording-properties) |
| [bool](class_bool.md#class-bool) | [recording_signals](class_missingnode.md#class-missingnode-property-recording-signals) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-missingnode-property-original-class"></a>

[String](class_string.md#class-string) **original_class** [🔗](class_missingnode.md#class-missingnode-property-original-class)

- void **set_original_class**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_original_class**()

The name of the class this node was supposed to be (see [Object.get_class()](class_object.md#class-object-method-get-class)).

---


<a id="class-missingnode-property-original-scene"></a>

[String](class_string.md#class-string) **original_scene** [🔗](class_missingnode.md#class-missingnode-property-original-scene)

- void **set_original_scene**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_original_scene**()

Returns the path of the scene this node was instance of originally.

---


<a id="class-missingnode-property-recording-properties"></a>

[bool](class_bool.md#class-bool) **recording_properties** [🔗](class_missingnode.md#class-missingnode-property-recording-properties)

- void **set_recording_properties**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_recording_properties**()

If `true`, allows new properties to be set along with existing ones. If `false`, only existing properties' values can be set, and new properties cannot be added.

---


<a id="class-missingnode-property-recording-signals"></a>

[bool](class_bool.md#class-bool) **recording_signals** [🔗](class_missingnode.md#class-missingnode-property-recording-signals)

- void **set_recording_signals**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_recording_signals**()

If `true`, allows new signals to be connected to along with existing ones. If `false`, only existing signals can be connected to, and new signals cannot be added.
