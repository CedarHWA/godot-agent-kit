> Source: https://docs.godotengine.org/en/4.7/classes/class_editorresourcepreview.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="editorresourcepreview"></a>

<a id="class-editorresourcepreview"></a>

# EditorResourcePreview

**Inherits:** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A node used to generate previews of resources or files.

<a id="description"></a>

## Description

This node is used to generate previews for resources or files.

**Note:** This class shouldn't be instantiated directly. Instead, access the singleton using [EditorInterface.get_resource_previewer()](class_editorinterface.md#class-editorinterface-method-get-resource-previewer).

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_preview_generator](class_editorresourcepreview.md#class-editorresourcepreview-method-add-preview-generator)(generator: [EditorResourcePreviewGenerator](class_editorresourcepreviewgenerator.md#class-editorresourcepreviewgenerator)) |
| void | [check_for_invalidation](class_editorresourcepreview.md#class-editorresourcepreview-method-check-for-invalidation)(path: [String](class_string.md#class-string)) |
| void | [queue_edited_resource_preview](class_editorresourcepreview.md#class-editorresourcepreview-method-queue-edited-resource-preview)(resource: [Resource](class_resource.md#class-resource), receiver: [Object](class_object.md#class-object), receiver_func: [StringName](class_stringname.md#class-stringname), userdata: [Variant](class_variant.md#class-variant)) |
| void | [queue_resource_preview](class_editorresourcepreview.md#class-editorresourcepreview-method-queue-resource-preview)(path: [String](class_string.md#class-string), receiver: [Object](class_object.md#class-object), receiver_func: [StringName](class_stringname.md#class-stringname), userdata: [Variant](class_variant.md#class-variant)) |
| void | [remove_preview_generator](class_editorresourcepreview.md#class-editorresourcepreview-method-remove-preview-generator)(generator: [EditorResourcePreviewGenerator](class_editorresourcepreviewgenerator.md#class-editorresourcepreviewgenerator)) |

---


<a id="signals"></a>

## Signals

<a id="class-editorresourcepreview-signal-preview-invalidated"></a>

**preview_invalidated**(path: [String](class_string.md#class-string)) [🔗](class_editorresourcepreview.md#class-editorresourcepreview-signal-preview-invalidated)

Emitted if a preview was invalidated (changed). `path` corresponds to the path of the preview.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-editorresourcepreview-method-add-preview-generator"></a>

void **add_preview_generator**(generator: [EditorResourcePreviewGenerator](class_editorresourcepreviewgenerator.md#class-editorresourcepreviewgenerator)) [🔗](class_editorresourcepreview.md#class-editorresourcepreview-method-add-preview-generator)

Create an own, custom preview generator.

---


<a id="class-editorresourcepreview-method-check-for-invalidation"></a>

void **check_for_invalidation**(path: [String](class_string.md#class-string)) [🔗](class_editorresourcepreview.md#class-editorresourcepreview-method-check-for-invalidation)

Check if the resource changed, if so, it will be invalidated and the corresponding signal emitted.

---


<a id="class-editorresourcepreview-method-queue-edited-resource-preview"></a>

void **queue_edited_resource_preview**(resource: [Resource](class_resource.md#class-resource), receiver: [Object](class_object.md#class-object), receiver_func: [StringName](class_stringname.md#class-stringname), userdata: [Variant](class_variant.md#class-variant)) [🔗](class_editorresourcepreview.md#class-editorresourcepreview-method-queue-edited-resource-preview)

Queue the `resource` being edited for preview. Once the preview is ready, the `receiver`'s `receiver_func` will be called. The `receiver_func` must take the following four arguments: [String](class_string.md#class-string) path, [Texture2D](class_texture2d.md#class-texture2d) preview, [Texture2D](class_texture2d.md#class-texture2d) thumbnail_preview, [Variant](class_variant.md#class-variant) userdata. `userdata` can be anything, and will be returned when `receiver_func` is called.

**Note:** If it was not possible to create the preview the `receiver_func` will still be called, but the preview will be `null`.

---


<a id="class-editorresourcepreview-method-queue-resource-preview"></a>

void **queue_resource_preview**(path: [String](class_string.md#class-string), receiver: [Object](class_object.md#class-object), receiver_func: [StringName](class_stringname.md#class-stringname), userdata: [Variant](class_variant.md#class-variant)) [🔗](class_editorresourcepreview.md#class-editorresourcepreview-method-queue-resource-preview)

Queue a resource file located at `path` for preview. Once the preview is ready, the `receiver`'s `receiver_func` will be called. The `receiver_func` must take the following four arguments: [String](class_string.md#class-string) path, [Texture2D](class_texture2d.md#class-texture2d) preview, [Texture2D](class_texture2d.md#class-texture2d) thumbnail_preview, [Variant](class_variant.md#class-variant) userdata. `userdata` can be anything, and will be returned when `receiver_func` is called.

**Note:** If it was not possible to create the preview the `receiver_func` will still be called, but the preview will be `null`.

---


<a id="class-editorresourcepreview-method-remove-preview-generator"></a>

void **remove_preview_generator**(generator: [EditorResourcePreviewGenerator](class_editorresourcepreviewgenerator.md#class-editorresourcepreviewgenerator)) [🔗](class_editorresourcepreview.md#class-editorresourcepreview-method-remove-preview-generator)

Removes a custom preview generator.
