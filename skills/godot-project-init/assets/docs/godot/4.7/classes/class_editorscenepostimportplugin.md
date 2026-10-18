> Source: https://docs.godotengine.org/en/4.7/classes/class_editorscenepostimportplugin.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="editorscenepostimportplugin"></a>

<a id="class-editorscenepostimportplugin"></a>

# EditorScenePostImportPlugin

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Plugin to control and modifying the process of importing a scene.

<a id="description"></a>

## Description

This plugin type exists to modify the process of importing scenes, allowing to change the content as well as add importer options at every stage of the process.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [_get_import_options](class_editorscenepostimportplugin.md#class-editorscenepostimportplugin-private-method-get-import-options)(path: [String](class_string.md#class-string)) virtual |
| void | [_get_internal_import_options](class_editorscenepostimportplugin.md#class-editorscenepostimportplugin-private-method-get-internal-import-options)(category: [int](class_int.md#class-int)) virtual |
| [Variant](class_variant.md#class-variant) | [_get_internal_option_update_view_required](class_editorscenepostimportplugin.md#class-editorscenepostimportplugin-private-method-get-internal-option-update-view-required)(category: [int](class_int.md#class-int), option: [String](class_string.md#class-string)) virtual const |
| [Variant](class_variant.md#class-variant) | [_get_internal_option_visibility](class_editorscenepostimportplugin.md#class-editorscenepostimportplugin-private-method-get-internal-option-visibility)(category: [int](class_int.md#class-int), for_animation: [bool](class_bool.md#class-bool), option: [String](class_string.md#class-string)) virtual const |
| [Variant](class_variant.md#class-variant) | [_get_option_visibility](class_editorscenepostimportplugin.md#class-editorscenepostimportplugin-private-method-get-option-visibility)(path: [String](class_string.md#class-string), for_animation: [bool](class_bool.md#class-bool), option: [String](class_string.md#class-string)) virtual const |
| void | [_internal_process](class_editorscenepostimportplugin.md#class-editorscenepostimportplugin-private-method-internal-process)(category: [int](class_int.md#class-int), base_node: [Node](class_node.md#class-node), node: [Node](class_node.md#class-node), resource: [Resource](class_resource.md#class-resource)) virtual |
| void | [_post_process](class_editorscenepostimportplugin.md#class-editorscenepostimportplugin-private-method-post-process)(scene: [Node](class_node.md#class-node)) virtual |
| void | [_pre_process](class_editorscenepostimportplugin.md#class-editorscenepostimportplugin-private-method-pre-process)(scene: [Node](class_node.md#class-node)) virtual |
| void | [add_import_option](class_editorscenepostimportplugin.md#class-editorscenepostimportplugin-method-add-import-option)(name: [String](class_string.md#class-string), value: [Variant](class_variant.md#class-variant)) |
| void | [add_import_option_advanced](class_editorscenepostimportplugin.md#class-editorscenepostimportplugin-method-add-import-option-advanced)(type: [Variant.Type](class_@globalscope.md#enum-globalscope-variant-type), name: [String](class_string.md#class-string), default_value: [Variant](class_variant.md#class-variant), hint: [PropertyHint](class_@globalscope.md#enum-globalscope-propertyhint) = 0, hint_string: [String](class_string.md#class-string) = "", usage_flags: [int](class_int.md#class-int) = 6) |
| [Variant](class_variant.md#class-variant) | [get_option_value](class_editorscenepostimportplugin.md#class-editorscenepostimportplugin-method-get-option-value)(name: [StringName](class_stringname.md#class-stringname)) const |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-editorscenepostimportplugin-internalimportcategory"></a>

enum **InternalImportCategory**: [🔗](class_editorscenepostimportplugin.md#enum-editorscenepostimportplugin-internalimportcategory)

<a id="class-editorscenepostimportplugin-constant-internal-import-category-node"></a>

[InternalImportCategory](class_editorscenepostimportplugin.md#enum-editorscenepostimportplugin-internalimportcategory) **INTERNAL_IMPORT_CATEGORY_NODE** = `0`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="class-editorscenepostimportplugin-constant-internal-import-category-mesh-3d-node"></a>

[InternalImportCategory](class_editorscenepostimportplugin.md#enum-editorscenepostimportplugin-internalimportcategory) **INTERNAL_IMPORT_CATEGORY_MESH_3D_NODE** = `1`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="class-editorscenepostimportplugin-constant-internal-import-category-mesh"></a>

[InternalImportCategory](class_editorscenepostimportplugin.md#enum-editorscenepostimportplugin-internalimportcategory) **INTERNAL_IMPORT_CATEGORY_MESH** = `2`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="class-editorscenepostimportplugin-constant-internal-import-category-material"></a>

[InternalImportCategory](class_editorscenepostimportplugin.md#enum-editorscenepostimportplugin-internalimportcategory) **INTERNAL_IMPORT_CATEGORY_MATERIAL** = `3`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="class-editorscenepostimportplugin-constant-internal-import-category-animation"></a>

[InternalImportCategory](class_editorscenepostimportplugin.md#enum-editorscenepostimportplugin-internalimportcategory) **INTERNAL_IMPORT_CATEGORY_ANIMATION** = `4`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="class-editorscenepostimportplugin-constant-internal-import-category-animation-node"></a>

[InternalImportCategory](class_editorscenepostimportplugin.md#enum-editorscenepostimportplugin-internalimportcategory) **INTERNAL_IMPORT_CATEGORY_ANIMATION_NODE** = `5`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="class-editorscenepostimportplugin-constant-internal-import-category-skeleton-3d-node"></a>

[InternalImportCategory](class_editorscenepostimportplugin.md#enum-editorscenepostimportplugin-internalimportcategory) **INTERNAL_IMPORT_CATEGORY_SKELETON_3D_NODE** = `6`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="class-editorscenepostimportplugin-constant-internal-import-category-max"></a>

[InternalImportCategory](class_editorscenepostimportplugin.md#enum-editorscenepostimportplugin-internalimportcategory) **INTERNAL_IMPORT_CATEGORY_MAX** = `7`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-editorscenepostimportplugin-private-method-get-import-options"></a>

void **_get_import_options**(path: [String](class_string.md#class-string)) virtual [🔗](class_editorscenepostimportplugin.md#class-editorscenepostimportplugin-private-method-get-import-options)

Override to add general import options. These will appear in the main import dock on the editor. Add options via [add_import_option()](class_editorscenepostimportplugin.md#class-editorscenepostimportplugin-method-add-import-option) and [add_import_option_advanced()](class_editorscenepostimportplugin.md#class-editorscenepostimportplugin-method-add-import-option-advanced).

---


<a id="class-editorscenepostimportplugin-private-method-get-internal-import-options"></a>

void **_get_internal_import_options**(category: [int](class_int.md#class-int)) virtual [🔗](class_editorscenepostimportplugin.md#class-editorscenepostimportplugin-private-method-get-internal-import-options)

Override to add internal import options. These will appear in the 3D scene import dialog. Add options via [add_import_option()](class_editorscenepostimportplugin.md#class-editorscenepostimportplugin-method-add-import-option) and [add_import_option_advanced()](class_editorscenepostimportplugin.md#class-editorscenepostimportplugin-method-add-import-option-advanced).

---


<a id="class-editorscenepostimportplugin-private-method-get-internal-option-update-view-required"></a>

[Variant](class_variant.md#class-variant) **_get_internal_option_update_view_required**(category: [int](class_int.md#class-int), option: [String](class_string.md#class-string)) virtual const [🔗](class_editorscenepostimportplugin.md#class-editorscenepostimportplugin-private-method-get-internal-option-update-view-required)

Should return `true` if the 3D view of the import dialog needs to update when changing the given option.

---


<a id="class-editorscenepostimportplugin-private-method-get-internal-option-visibility"></a>

[Variant](class_variant.md#class-variant) **_get_internal_option_visibility**(category: [int](class_int.md#class-int), for_animation: [bool](class_bool.md#class-bool), option: [String](class_string.md#class-string)) virtual const [🔗](class_editorscenepostimportplugin.md#class-editorscenepostimportplugin-private-method-get-internal-option-visibility)

Should return `true` to show the given option, `false` to hide the given option, or `null` to ignore.

---


<a id="class-editorscenepostimportplugin-private-method-get-option-visibility"></a>

[Variant](class_variant.md#class-variant) **_get_option_visibility**(path: [String](class_string.md#class-string), for_animation: [bool](class_bool.md#class-bool), option: [String](class_string.md#class-string)) virtual const [🔗](class_editorscenepostimportplugin.md#class-editorscenepostimportplugin-private-method-get-option-visibility)

Should return `true` to show the given option, `false` to hide the given option, or `null` to ignore.

---


<a id="class-editorscenepostimportplugin-private-method-internal-process"></a>

void **_internal_process**(category: [int](class_int.md#class-int), base_node: [Node](class_node.md#class-node), node: [Node](class_node.md#class-node), resource: [Resource](class_resource.md#class-resource)) virtual [🔗](class_editorscenepostimportplugin.md#class-editorscenepostimportplugin-private-method-internal-process)

Process a specific node or resource for a given category.

---


<a id="class-editorscenepostimportplugin-private-method-post-process"></a>

void **_post_process**(scene: [Node](class_node.md#class-node)) virtual [🔗](class_editorscenepostimportplugin.md#class-editorscenepostimportplugin-private-method-post-process)

Post-process the scene. This function is called after the final scene has been configured.

---


<a id="class-editorscenepostimportplugin-private-method-pre-process"></a>

void **_pre_process**(scene: [Node](class_node.md#class-node)) virtual [🔗](class_editorscenepostimportplugin.md#class-editorscenepostimportplugin-private-method-pre-process)

Pre-process the scene. This function is called right after the scene format loader loaded the scene and no changes have been made.

Pre-process may be used to adjust internal import options in the `"nodes"`, `"meshes"`, `"animations"` or `"materials"` keys inside `get_option_value("_subresources")`.

---


<a id="class-editorscenepostimportplugin-method-add-import-option"></a>

void **add_import_option**(name: [String](class_string.md#class-string), value: [Variant](class_variant.md#class-variant)) [🔗](class_editorscenepostimportplugin.md#class-editorscenepostimportplugin-method-add-import-option)

Add a specific import option (name and default value only). This function can only be called from [_get_import_options()](class_editorscenepostimportplugin.md#class-editorscenepostimportplugin-private-method-get-import-options) and [_get_internal_import_options()](class_editorscenepostimportplugin.md#class-editorscenepostimportplugin-private-method-get-internal-import-options).

---


<a id="class-editorscenepostimportplugin-method-add-import-option-advanced"></a>

void **add_import_option_advanced**(type: [Variant.Type](class_@globalscope.md#enum-globalscope-variant-type), name: [String](class_string.md#class-string), default_value: [Variant](class_variant.md#class-variant), hint: [PropertyHint](class_@globalscope.md#enum-globalscope-propertyhint) = 0, hint_string: [String](class_string.md#class-string) = "", usage_flags: [int](class_int.md#class-int) = 6) [🔗](class_editorscenepostimportplugin.md#class-editorscenepostimportplugin-method-add-import-option-advanced)

Add a specific import option. This function can only be called from [_get_import_options()](class_editorscenepostimportplugin.md#class-editorscenepostimportplugin-private-method-get-import-options) and [_get_internal_import_options()](class_editorscenepostimportplugin.md#class-editorscenepostimportplugin-private-method-get-internal-import-options).

---


<a id="class-editorscenepostimportplugin-method-get-option-value"></a>

[Variant](class_variant.md#class-variant) **get_option_value**(name: [StringName](class_stringname.md#class-stringname)) const [🔗](class_editorscenepostimportplugin.md#class-editorscenepostimportplugin-method-get-option-value)

Query the value of an option. This function can only be called from those querying visibility, or processing.
