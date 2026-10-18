> Source: https://docs.godotengine.org/en/4.7/classes/class_gltfskeleton.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="gltfskeleton"></a>

<a id="class-gltfskeleton"></a>

# GLTFSkeleton

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

There is currently no description for this class. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="tutorials"></a>

## Tutorials

- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array) | [joints](class_gltfskeleton.md#class-gltfskeleton-property-joints) | `PackedInt32Array()` |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array) | [roots](class_gltfskeleton.md#class-gltfskeleton-property-roots) | `PackedInt32Array()` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [BoneAttachment3D](class_boneattachment3d.md#class-boneattachment3d) | [get_bone_attachment](class_gltfskeleton.md#class-gltfskeleton-method-get-bone-attachment)(idx: [int](class_int.md#class-int)) |
| [int](class_int.md#class-int) | [get_bone_attachment_count](class_gltfskeleton.md#class-gltfskeleton-method-get-bone-attachment-count)() |
| [Dictionary](class_dictionary.md#class-dictionary) | [get_godot_bone_node](class_gltfskeleton.md#class-gltfskeleton-method-get-godot-bone-node)() |
| [Skeleton3D](class_skeleton3d.md#class-skeleton3d) | [get_godot_skeleton](class_gltfskeleton.md#class-gltfskeleton-method-get-godot-skeleton)() |
| [Array](class_array.md#class-array)[[String](class_string.md#class-string)] | [get_unique_names](class_gltfskeleton.md#class-gltfskeleton-method-get-unique-names)() |
| void | [set_godot_bone_node](class_gltfskeleton.md#class-gltfskeleton-method-set-godot-bone-node)(godot_bone_node: [Dictionary](class_dictionary.md#class-dictionary)) |
| void | [set_unique_names](class_gltfskeleton.md#class-gltfskeleton-method-set-unique-names)(unique_names: [Array](class_array.md#class-array)[[String](class_string.md#class-string)]) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-gltfskeleton-property-joints"></a>

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **joints** = `PackedInt32Array()` [🔗](class_gltfskeleton.md#class-gltfskeleton-property-joints)

- void **set_joints**(value: [PackedInt32Array](class_packedint32array.md#class-packedint32array))
- [PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_joints**()

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array](class_packedint32array.md#class-packedint32array) for more details.

---


<a id="class-gltfskeleton-property-roots"></a>

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **roots** = `PackedInt32Array()` [🔗](class_gltfskeleton.md#class-gltfskeleton-property-roots)

- void **set_roots**(value: [PackedInt32Array](class_packedint32array.md#class-packedint32array))
- [PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_roots**()

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array](class_packedint32array.md#class-packedint32array) for more details.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-gltfskeleton-method-get-bone-attachment"></a>

[BoneAttachment3D](class_boneattachment3d.md#class-boneattachment3d) **get_bone_attachment**(idx: [int](class_int.md#class-int)) [🔗](class_gltfskeleton.md#class-gltfskeleton-method-get-bone-attachment)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-gltfskeleton-method-get-bone-attachment-count"></a>

[int](class_int.md#class-int) **get_bone_attachment_count**() [🔗](class_gltfskeleton.md#class-gltfskeleton-method-get-bone-attachment-count)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-gltfskeleton-method-get-godot-bone-node"></a>

[Dictionary](class_dictionary.md#class-dictionary) **get_godot_bone_node**() [🔗](class_gltfskeleton.md#class-gltfskeleton-method-get-godot-bone-node)

Returns a [Dictionary](class_dictionary.md#class-dictionary) that maps skeleton bone indices to the indices of glTF nodes. This property is unused during import, and only set during export. In a glTF file, a bone is a node, so Godot converts skeleton bones to glTF nodes.

---


<a id="class-gltfskeleton-method-get-godot-skeleton"></a>

[Skeleton3D](class_skeleton3d.md#class-skeleton3d) **get_godot_skeleton**() [🔗](class_gltfskeleton.md#class-gltfskeleton-method-get-godot-skeleton)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-gltfskeleton-method-get-unique-names"></a>

[Array](class_array.md#class-array)[[String](class_string.md#class-string)] **get_unique_names**() [🔗](class_gltfskeleton.md#class-gltfskeleton-method-get-unique-names)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-gltfskeleton-method-set-godot-bone-node"></a>

void **set_godot_bone_node**(godot_bone_node: [Dictionary](class_dictionary.md#class-dictionary)) [🔗](class_gltfskeleton.md#class-gltfskeleton-method-set-godot-bone-node)

Sets a [Dictionary](class_dictionary.md#class-dictionary) that maps skeleton bone indices to the indices of glTF nodes. This property is unused during import, and only set during export. In a glTF file, a bone is a node, so Godot converts skeleton bones to glTF nodes.

---


<a id="class-gltfskeleton-method-set-unique-names"></a>

void **set_unique_names**(unique_names: [Array](class_array.md#class-array)[[String](class_string.md#class-string)]) [🔗](class_gltfskeleton.md#class-gltfskeleton-method-set-unique-names)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!
