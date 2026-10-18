> Source: https://docs.godotengine.org/en/4.7/classes/class_resourcepreloader.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="resourcepreloader"></a>

<a id="class-resourcepreloader"></a>

# ResourcePreloader

**Inherits:** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A node used to preload sub-resources inside a scene.

<a id="description"></a>

## Description

This node is used to preload sub-resources inside a scene, so when the scene is loaded, all the resources are ready to use and can be retrieved from the preloader. You can add the resources using the ResourcePreloader tab when the node is selected.

GDScript has a simplified [@GDScript.preload()](class_@gdscript.md#class-gdscript-method-preload) built-in method which can be used in most situations, leaving the use of **ResourcePreloader** for more advanced scenarios.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_resource](class_resourcepreloader.md#class-resourcepreloader-method-add-resource)(name: [StringName](class_stringname.md#class-stringname), resource: [Resource](class_resource.md#class-resource)) |
| [Resource](class_resource.md#class-resource) | [get_resource](class_resourcepreloader.md#class-resourcepreloader-method-get-resource)(name: [StringName](class_stringname.md#class-stringname)) const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [get_resource_list](class_resourcepreloader.md#class-resourcepreloader-method-get-resource-list)() const |
| [bool](class_bool.md#class-bool) | [has_resource](class_resourcepreloader.md#class-resourcepreloader-method-has-resource)(name: [StringName](class_stringname.md#class-stringname)) const |
| void | [remove_resource](class_resourcepreloader.md#class-resourcepreloader-method-remove-resource)(name: [StringName](class_stringname.md#class-stringname)) |
| void | [rename_resource](class_resourcepreloader.md#class-resourcepreloader-method-rename-resource)(name: [StringName](class_stringname.md#class-stringname), newname: [StringName](class_stringname.md#class-stringname)) |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-resourcepreloader-method-add-resource"></a>

void **add_resource**(name: [StringName](class_stringname.md#class-stringname), resource: [Resource](class_resource.md#class-resource)) [🔗](class_resourcepreloader.md#class-resourcepreloader-method-add-resource)

Adds a resource to the preloader with the given `name`. If a resource with the given `name` already exists, the new resource will be renamed to "`name` N" where N is an incrementing number starting from 2.

---


<a id="class-resourcepreloader-method-get-resource"></a>

[Resource](class_resource.md#class-resource) **get_resource**(name: [StringName](class_stringname.md#class-stringname)) const [🔗](class_resourcepreloader.md#class-resourcepreloader-method-get-resource)

Returns the resource associated to `name`.

---


<a id="class-resourcepreloader-method-get-resource-list"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_resource_list**() const [🔗](class_resourcepreloader.md#class-resourcepreloader-method-get-resource-list)

Returns the list of resources inside the preloader.

---


<a id="class-resourcepreloader-method-has-resource"></a>

[bool](class_bool.md#class-bool) **has_resource**(name: [StringName](class_stringname.md#class-stringname)) const [🔗](class_resourcepreloader.md#class-resourcepreloader-method-has-resource)

Returns `true` if the preloader contains a resource associated to `name`.

---


<a id="class-resourcepreloader-method-remove-resource"></a>

void **remove_resource**(name: [StringName](class_stringname.md#class-stringname)) [🔗](class_resourcepreloader.md#class-resourcepreloader-method-remove-resource)

Removes the resource associated to `name` from the preloader.

---


<a id="class-resourcepreloader-method-rename-resource"></a>

void **rename_resource**(name: [StringName](class_stringname.md#class-stringname), newname: [StringName](class_stringname.md#class-stringname)) [🔗](class_resourcepreloader.md#class-resourcepreloader-method-rename-resource)

Renames a resource inside the preloader from `name` to `newname`.
