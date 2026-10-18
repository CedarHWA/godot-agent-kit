> Source: https://docs.godotengine.org/en/4.7/classes/class_gltfmesh.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="gltfmesh"></a>

<a id="class-gltfmesh"></a>

# GLTFMesh

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

GLTFMesh represents a glTF mesh.

<a id="description"></a>

## Description

GLTFMesh handles 3D mesh data imported from glTF files. It includes properties for blend channels, blend weights, instance materials, and the mesh itself.

<a id="tutorials"></a>

## Tutorials

- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) | [blend_weights](class_gltfmesh.md#class-gltfmesh-property-blend-weights) | `PackedFloat32Array()` |
| [Array](class_array.md#class-array)[[Material](class_material.md#class-material)] | [instance_materials](class_gltfmesh.md#class-gltfmesh-property-instance-materials) | `[]` |
| [ImporterMesh](class_importermesh.md#class-importermesh) | [mesh](class_gltfmesh.md#class-gltfmesh-property-mesh) |  |
| [String](class_string.md#class-string) | [original_name](class_gltfmesh.md#class-gltfmesh-property-original-name) | `""` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Variant](class_variant.md#class-variant) | [get_additional_data](class_gltfmesh.md#class-gltfmesh-method-get-additional-data)(extension_name: [StringName](class_stringname.md#class-stringname)) |
| void | [set_additional_data](class_gltfmesh.md#class-gltfmesh-method-set-additional-data)(extension_name: [StringName](class_stringname.md#class-stringname), additional_data: [Variant](class_variant.md#class-variant)) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-gltfmesh-property-blend-weights"></a>

[PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) **blend_weights** = `PackedFloat32Array()` [🔗](class_gltfmesh.md#class-gltfmesh-property-blend-weights)

- void **set_blend_weights**(value: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array))
- [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) **get_blend_weights**()

An array of floats representing the blend weights of the mesh.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) for more details.

---


<a id="class-gltfmesh-property-instance-materials"></a>

[Array](class_array.md#class-array)[[Material](class_material.md#class-material)] **instance_materials** = `[]` [🔗](class_gltfmesh.md#class-gltfmesh-property-instance-materials)

- void **set_instance_materials**(value: [Array](class_array.md#class-array)[[Material](class_material.md#class-material)])
- [Array](class_array.md#class-array)[[Material](class_material.md#class-material)] **get_instance_materials**()

An array of Material objects representing the materials used in the mesh.

---


<a id="class-gltfmesh-property-mesh"></a>

[ImporterMesh](class_importermesh.md#class-importermesh) **mesh** [🔗](class_gltfmesh.md#class-gltfmesh-property-mesh)

- void **set_mesh**(value: [ImporterMesh](class_importermesh.md#class-importermesh))
- [ImporterMesh](class_importermesh.md#class-importermesh) **get_mesh**()

The [ImporterMesh](class_importermesh.md#class-importermesh) object representing the mesh itself.

---


<a id="class-gltfmesh-property-original-name"></a>

[String](class_string.md#class-string) **original_name** = `""` [🔗](class_gltfmesh.md#class-gltfmesh-property-original-name)

- void **set_original_name**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_original_name**()

The original name of the mesh.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-gltfmesh-method-get-additional-data"></a>

[Variant](class_variant.md#class-variant) **get_additional_data**(extension_name: [StringName](class_stringname.md#class-stringname)) [🔗](class_gltfmesh.md#class-gltfmesh-method-get-additional-data)

Gets additional arbitrary data in this **GLTFMesh** instance. This can be used to keep per-node state data in [GLTFDocumentExtension](class_gltfdocumentextension.md#class-gltfdocumentextension) classes, which is important because they are stateless.

The argument should be the [GLTFDocumentExtension](class_gltfdocumentextension.md#class-gltfdocumentextension) name (does not have to match the extension name in the glTF file), and the return value can be anything you set. If nothing was set, the return value is `null`.

---


<a id="class-gltfmesh-method-set-additional-data"></a>

void **set_additional_data**(extension_name: [StringName](class_stringname.md#class-stringname), additional_data: [Variant](class_variant.md#class-variant)) [🔗](class_gltfmesh.md#class-gltfmesh-method-set-additional-data)

Sets additional arbitrary data in this **GLTFMesh** instance. This can be used to keep per-node state data in [GLTFDocumentExtension](class_gltfdocumentextension.md#class-gltfdocumentextension) classes, which is important because they are stateless.

The first argument should be the [GLTFDocumentExtension](class_gltfdocumentextension.md#class-gltfdocumentextension) name (does not have to match the extension name in the glTF file), and the second argument can be anything you want.
