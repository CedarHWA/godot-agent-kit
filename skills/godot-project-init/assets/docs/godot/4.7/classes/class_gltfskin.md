> Source: https://docs.godotengine.org/en/4.7/classes/class_gltfskin.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="gltfskin"></a>

<a id="class-gltfskin"></a>

# GLTFSkin

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

There is currently no description for this class. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="tutorials"></a>

## Tutorials

- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Skin](class_skin.md#class-skin) | [godot_skin](class_gltfskin.md#class-gltfskin-property-godot-skin) |  |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array) | [joints](class_gltfskin.md#class-gltfskin-property-joints) | `PackedInt32Array()` |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array) | [joints_original](class_gltfskin.md#class-gltfskin-property-joints-original) | `PackedInt32Array()` |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array) | [non_joints](class_gltfskin.md#class-gltfskin-property-non-joints) | `PackedInt32Array()` |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array) | [roots](class_gltfskin.md#class-gltfskin-property-roots) | `PackedInt32Array()` |
| [int](class_int.md#class-int) | [skeleton](class_gltfskin.md#class-gltfskin-property-skeleton) | `-1` |
| [int](class_int.md#class-int) | [skin_root](class_gltfskin.md#class-gltfskin-property-skin-root) | `-1` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Array](class_array.md#class-array)[[Transform3D](class_transform3d.md#class-transform3d)] | [get_inverse_binds](class_gltfskin.md#class-gltfskin-method-get-inverse-binds)() |
| [Dictionary](class_dictionary.md#class-dictionary) | [get_joint_i_to_bone_i](class_gltfskin.md#class-gltfskin-method-get-joint-i-to-bone-i)() |
| [Dictionary](class_dictionary.md#class-dictionary) | [get_joint_i_to_name](class_gltfskin.md#class-gltfskin-method-get-joint-i-to-name)() |
| void | [set_inverse_binds](class_gltfskin.md#class-gltfskin-method-set-inverse-binds)(inverse_binds: [Array](class_array.md#class-array)[[Transform3D](class_transform3d.md#class-transform3d)]) |
| void | [set_joint_i_to_bone_i](class_gltfskin.md#class-gltfskin-method-set-joint-i-to-bone-i)(joint_i_to_bone_i: [Dictionary](class_dictionary.md#class-dictionary)) |
| void | [set_joint_i_to_name](class_gltfskin.md#class-gltfskin-method-set-joint-i-to-name)(joint_i_to_name: [Dictionary](class_dictionary.md#class-dictionary)) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-gltfskin-property-godot-skin"></a>

[Skin](class_skin.md#class-skin) **godot_skin** [🔗](class_gltfskin.md#class-gltfskin-property-godot-skin)

- void **set_godot_skin**(value: [Skin](class_skin.md#class-skin))
- [Skin](class_skin.md#class-skin) **get_godot_skin**()

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-gltfskin-property-joints"></a>

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **joints** = `PackedInt32Array()` [🔗](class_gltfskin.md#class-gltfskin-property-joints)

- void **set_joints**(value: [PackedInt32Array](class_packedint32array.md#class-packedint32array))
- [PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_joints**()

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array](class_packedint32array.md#class-packedint32array) for more details.

---


<a id="class-gltfskin-property-joints-original"></a>

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **joints_original** = `PackedInt32Array()` [🔗](class_gltfskin.md#class-gltfskin-property-joints-original)

- void **set_joints_original**(value: [PackedInt32Array](class_packedint32array.md#class-packedint32array))
- [PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_joints_original**()

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array](class_packedint32array.md#class-packedint32array) for more details.

---


<a id="class-gltfskin-property-non-joints"></a>

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **non_joints** = `PackedInt32Array()` [🔗](class_gltfskin.md#class-gltfskin-property-non-joints)

- void **set_non_joints**(value: [PackedInt32Array](class_packedint32array.md#class-packedint32array))
- [PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_non_joints**()

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array](class_packedint32array.md#class-packedint32array) for more details.

---


<a id="class-gltfskin-property-roots"></a>

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **roots** = `PackedInt32Array()` [🔗](class_gltfskin.md#class-gltfskin-property-roots)

- void **set_roots**(value: [PackedInt32Array](class_packedint32array.md#class-packedint32array))
- [PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_roots**()

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array](class_packedint32array.md#class-packedint32array) for more details.

---


<a id="class-gltfskin-property-skeleton"></a>

[int](class_int.md#class-int) **skeleton** = `-1` [🔗](class_gltfskin.md#class-gltfskin-property-skeleton)

- void **set_skeleton**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_skeleton**()

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-gltfskin-property-skin-root"></a>

[int](class_int.md#class-int) **skin_root** = `-1` [🔗](class_gltfskin.md#class-gltfskin-property-skin-root)

- void **set_skin_root**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_skin_root**()

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-gltfskin-method-get-inverse-binds"></a>

[Array](class_array.md#class-array)[[Transform3D](class_transform3d.md#class-transform3d)] **get_inverse_binds**() [🔗](class_gltfskin.md#class-gltfskin-method-get-inverse-binds)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-gltfskin-method-get-joint-i-to-bone-i"></a>

[Dictionary](class_dictionary.md#class-dictionary) **get_joint_i_to_bone_i**() [🔗](class_gltfskin.md#class-gltfskin-method-get-joint-i-to-bone-i)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-gltfskin-method-get-joint-i-to-name"></a>

[Dictionary](class_dictionary.md#class-dictionary) **get_joint_i_to_name**() [🔗](class_gltfskin.md#class-gltfskin-method-get-joint-i-to-name)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-gltfskin-method-set-inverse-binds"></a>

void **set_inverse_binds**(inverse_binds: [Array](class_array.md#class-array)[[Transform3D](class_transform3d.md#class-transform3d)]) [🔗](class_gltfskin.md#class-gltfskin-method-set-inverse-binds)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-gltfskin-method-set-joint-i-to-bone-i"></a>

void **set_joint_i_to_bone_i**(joint_i_to_bone_i: [Dictionary](class_dictionary.md#class-dictionary)) [🔗](class_gltfskin.md#class-gltfskin-method-set-joint-i-to-bone-i)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-gltfskin-method-set-joint-i-to-name"></a>

void **set_joint_i_to_name**(joint_i_to_name: [Dictionary](class_dictionary.md#class-dictionary)) [🔗](class_gltfskin.md#class-gltfskin-method-set-joint-i-to-name)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!
