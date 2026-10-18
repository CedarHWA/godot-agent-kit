> Source: https://docs.godotengine.org/en/4.7/classes/class_gltfanimation.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="gltfanimation"></a>

<a id="class-gltfanimation"></a>

# GLTFAnimation

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

There is currently no description for this class. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="tutorials"></a>

## Tutorials

- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [loop](class_gltfanimation.md#class-gltfanimation-property-loop) | `false` |
| [String](class_string.md#class-string) | [original_name](class_gltfanimation.md#class-gltfanimation-property-original-name) | `""` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Variant](class_variant.md#class-variant) | [get_additional_data](class_gltfanimation.md#class-gltfanimation-method-get-additional-data)(extension_name: [StringName](class_stringname.md#class-stringname)) |
| void | [set_additional_data](class_gltfanimation.md#class-gltfanimation-method-set-additional-data)(extension_name: [StringName](class_stringname.md#class-stringname), additional_data: [Variant](class_variant.md#class-variant)) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-gltfanimation-property-loop"></a>

[bool](class_bool.md#class-bool) **loop** = `false` [🔗](class_gltfanimation.md#class-gltfanimation-property-loop)

- void **set_loop**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_loop**()

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-gltfanimation-property-original-name"></a>

[String](class_string.md#class-string) **original_name** = `""` [🔗](class_gltfanimation.md#class-gltfanimation-property-original-name)

- void **set_original_name**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_original_name**()

The original name of the animation.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-gltfanimation-method-get-additional-data"></a>

[Variant](class_variant.md#class-variant) **get_additional_data**(extension_name: [StringName](class_stringname.md#class-stringname)) [🔗](class_gltfanimation.md#class-gltfanimation-method-get-additional-data)

Gets additional arbitrary data in this **GLTFAnimation** instance. This can be used to keep per-node state data in [GLTFDocumentExtension](class_gltfdocumentextension.md#class-gltfdocumentextension) classes, which is important because they are stateless.

The argument should be the [GLTFDocumentExtension](class_gltfdocumentextension.md#class-gltfdocumentextension) name (does not have to match the extension name in the glTF file), and the return value can be anything you set. If nothing was set, the return value is `null`.

---


<a id="class-gltfanimation-method-set-additional-data"></a>

void **set_additional_data**(extension_name: [StringName](class_stringname.md#class-stringname), additional_data: [Variant](class_variant.md#class-variant)) [🔗](class_gltfanimation.md#class-gltfanimation-method-set-additional-data)

Sets additional arbitrary data in this **GLTFAnimation** instance. This can be used to keep per-node state data in [GLTFDocumentExtension](class_gltfdocumentextension.md#class-gltfdocumentextension) classes, which is important because they are stateless.

The first argument should be the [GLTFDocumentExtension](class_gltfdocumentextension.md#class-gltfdocumentextension) name (does not have to match the extension name in the glTF file), and the second argument can be anything you want.
