> Source: https://docs.godotengine.org/en/4.7/classes/class_missingresource.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="missingresource"></a>

<a id="class-missingresource"></a>

# MissingResource

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

An internal editor class intended for keeping the data of unrecognized resources.

<a id="description"></a>

## Description

This is an internal editor class intended for keeping data of resources of unknown type (most likely this type was supplied by an extension that is no longer loaded). It can't be manually instantiated or placed in a scene.

**Warning:** Ignore missing resources unless you know what you are doing. Existing properties on a missing resource can be freely modified in code, regardless of the type they are intended to be.

<a id="properties"></a>

## Properties

|  |  |
| --- | --- |
| [String](class_string.md#class-string) | [original_class](class_missingresource.md#class-missingresource-property-original-class) |
| [bool](class_bool.md#class-bool) | [recording_properties](class_missingresource.md#class-missingresource-property-recording-properties) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-missingresource-property-original-class"></a>

[String](class_string.md#class-string) **original_class** [🔗](class_missingresource.md#class-missingresource-property-original-class)

- void **set_original_class**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_original_class**()

The name of the class this resource was supposed to be (see [Object.get_class()](class_object.md#class-object-method-get-class)).

---


<a id="class-missingresource-property-recording-properties"></a>

[bool](class_bool.md#class-bool) **recording_properties** [🔗](class_missingresource.md#class-missingresource-property-recording-properties)

- void **set_recording_properties**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_recording_properties**()

If set to `true`, allows new properties to be added on top of the existing ones with [Object.set()](class_object.md#class-object-method-set).
