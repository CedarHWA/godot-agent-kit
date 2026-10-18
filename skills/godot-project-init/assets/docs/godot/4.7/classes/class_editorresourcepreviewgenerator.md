> Source: https://docs.godotengine.org/en/4.7/classes/class_editorresourcepreviewgenerator.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="editorresourcepreviewgenerator"></a>

<a id="class-editorresourcepreviewgenerator"></a>

# EditorResourcePreviewGenerator

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Custom generator of previews.

<a id="description"></a>

## Description

Custom code to generate previews. Check [EditorSettings.filesystem/file_dialog/thumbnail_size](class_editorsettings.md#class-editorsettings-property-filesystem-file-dialog-thumbnail-size) to find a proper size to generate previews at.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [_can_generate_small_preview](class_editorresourcepreviewgenerator.md#class-editorresourcepreviewgenerator-private-method-can-generate-small-preview)() virtual const |
| [Texture2D](class_texture2d.md#class-texture2d) | [_generate](class_editorresourcepreviewgenerator.md#class-editorresourcepreviewgenerator-private-method-generate)(resource: [Resource](class_resource.md#class-resource), size: [Vector2i](class_vector2i.md#class-vector2i), metadata: [Dictionary](class_dictionary.md#class-dictionary)) virtual required const |
| [Texture2D](class_texture2d.md#class-texture2d) | [_generate_from_path](class_editorresourcepreviewgenerator.md#class-editorresourcepreviewgenerator-private-method-generate-from-path)(path: [String](class_string.md#class-string), size: [Vector2i](class_vector2i.md#class-vector2i), metadata: [Dictionary](class_dictionary.md#class-dictionary)) virtual const |
| [bool](class_bool.md#class-bool) | [_generate_small_preview_automatically](class_editorresourcepreviewgenerator.md#class-editorresourcepreviewgenerator-private-method-generate-small-preview-automatically)() virtual const |
| [bool](class_bool.md#class-bool) | [_handles](class_editorresourcepreviewgenerator.md#class-editorresourcepreviewgenerator-private-method-handles)(type: [String](class_string.md#class-string)) virtual required const |
| void | [request_draw_and_wait](class_editorresourcepreviewgenerator.md#class-editorresourcepreviewgenerator-method-request-draw-and-wait)(viewport: [RID](class_rid.md#class-rid)) const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-editorresourcepreviewgenerator-private-method-can-generate-small-preview"></a>

[bool](class_bool.md#class-bool) **_can_generate_small_preview**() virtual const [🔗](class_editorresourcepreviewgenerator.md#class-editorresourcepreviewgenerator-private-method-can-generate-small-preview)

If this function returns `true`, the generator will call [_generate()](class_editorresourcepreviewgenerator.md#class-editorresourcepreviewgenerator-private-method-generate) or [_generate_from_path()](class_editorresourcepreviewgenerator.md#class-editorresourcepreviewgenerator-private-method-generate-from-path) for small previews as well.

By default, it returns `false`.

---


<a id="class-editorresourcepreviewgenerator-private-method-generate"></a>

[Texture2D](class_texture2d.md#class-texture2d) **_generate**(resource: [Resource](class_resource.md#class-resource), size: [Vector2i](class_vector2i.md#class-vector2i), metadata: [Dictionary](class_dictionary.md#class-dictionary)) virtual required const [🔗](class_editorresourcepreviewgenerator.md#class-editorresourcepreviewgenerator-private-method-generate)

Generate a preview from a given resource with the specified size. This must always be implemented.

Returning `null` is an OK way to fail and let another generator take care.

Care must be taken because this function is always called from a thread (not the main thread).

`metadata` dictionary can be modified to store file-specific metadata that can be used in [EditorResourceTooltipPlugin._make_tooltip_for_path()](class_editorresourcetooltipplugin.md#class-editorresourcetooltipplugin-private-method-make-tooltip-for-path) (like image size, sample length etc.).

---


<a id="class-editorresourcepreviewgenerator-private-method-generate-from-path"></a>

[Texture2D](class_texture2d.md#class-texture2d) **_generate_from_path**(path: [String](class_string.md#class-string), size: [Vector2i](class_vector2i.md#class-vector2i), metadata: [Dictionary](class_dictionary.md#class-dictionary)) virtual const [🔗](class_editorresourcepreviewgenerator.md#class-editorresourcepreviewgenerator-private-method-generate-from-path)

Generate a preview directly from a path with the specified size. Implementing this is optional, as default code will load and call [_generate()](class_editorresourcepreviewgenerator.md#class-editorresourcepreviewgenerator-private-method-generate).

Returning `null` is an OK way to fail and let another generator take care.

Care must be taken because this function is always called from a thread (not the main thread).

`metadata` dictionary can be modified to store file-specific metadata that can be used in [EditorResourceTooltipPlugin._make_tooltip_for_path()](class_editorresourcetooltipplugin.md#class-editorresourcetooltipplugin-private-method-make-tooltip-for-path) (like image size, sample length etc.).

---


<a id="class-editorresourcepreviewgenerator-private-method-generate-small-preview-automatically"></a>

[bool](class_bool.md#class-bool) **_generate_small_preview_automatically**() virtual const [🔗](class_editorresourcepreviewgenerator.md#class-editorresourcepreviewgenerator-private-method-generate-small-preview-automatically)

If this function returns `true`, the generator will automatically generate the small previews from the normal preview texture generated by the methods [_generate()](class_editorresourcepreviewgenerator.md#class-editorresourcepreviewgenerator-private-method-generate) or [_generate_from_path()](class_editorresourcepreviewgenerator.md#class-editorresourcepreviewgenerator-private-method-generate-from-path).

By default, it returns `false`.

---


<a id="class-editorresourcepreviewgenerator-private-method-handles"></a>

[bool](class_bool.md#class-bool) **_handles**(type: [String](class_string.md#class-string)) virtual required const [🔗](class_editorresourcepreviewgenerator.md#class-editorresourcepreviewgenerator-private-method-handles)

Returns `true` if your generator supports the resource of type `type`.

---


<a id="class-editorresourcepreviewgenerator-method-request-draw-and-wait"></a>

void **request_draw_and_wait**(viewport: [RID](class_rid.md#class-rid)) const [🔗](class_editorresourcepreviewgenerator.md#class-editorresourcepreviewgenerator-method-request-draw-and-wait)

Call from within [_generate()](class_editorresourcepreviewgenerator.md#class-editorresourcepreviewgenerator-private-method-generate) to request the rendering server draw to the `viewport`.
