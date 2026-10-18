> Source: https://docs.godotengine.org/en/4.7/classes/class_imagetexture.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="imagetexture"></a>

<a id="class-imagetexture"></a>

# ImageTexture

**Inherits:** [Texture2D](class_texture2d.md#class-texture2d) **<** [Texture](class_texture.md#class-texture) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A [Texture2D](class_texture2d.md#class-texture2d) based on an [Image](class_image.md#class-image).

<a id="description"></a>

## Description

A [Texture2D](class_texture2d.md#class-texture2d) based on an [Image](class_image.md#class-image). For an image to be displayed, an **ImageTexture** has to be created from it using the [create_from_image()](class_imagetexture.md#class-imagetexture-method-create-from-image) method:

```gdscript
var image = Image.load_from_file("res://icon.svg")
var texture = ImageTexture.create_from_image(image)
$Sprite2D.texture = texture
```

This way, textures can be created at run-time by loading images both from within the editor and externally.

**Warning:** Prefer to load imported textures with [@GDScript.load()](class_@gdscript.md#class-gdscript-method-load) over loading them from within the filesystem dynamically with [Image.load()](class_image.md#class-image-method-load), as it may not work in exported projects:

```gdscript
var texture = load("res://icon.svg")
$Sprite2D.texture = texture
```

This is because images have to be imported as a [CompressedTexture2D](class_compressedtexture2d.md#class-compressedtexture2d) first to be loaded with [@GDScript.load()](class_@gdscript.md#class-gdscript-method-load). If you'd still like to load an image file just like any other [Resource](class_resource.md#class-resource), import it as an [Image](class_image.md#class-image) resource instead, and then load it normally using the [@GDScript.load()](class_@gdscript.md#class-gdscript-method-load) method.

**Note:** The image can be retrieved from an imported texture using the [Texture2D.get_image()](class_texture2d.md#class-texture2d-method-get-image) method, which returns a copy of the image:

```gdscript
var texture = load("res://icon.svg")
var image = texture.get_image()
```

An **ImageTexture** is not meant to be operated from within the editor interface directly, and is mostly useful for rendering images on screen dynamically via code. If you need to generate images procedurally from within the editor, consider saving and importing images as custom texture resources implementing a new [EditorImportPlugin](class_editorimportplugin.md#class-editorimportplugin).

**Note:** The maximum texture size is 16384×16384 pixels due to graphics hardware limitations.

<a id="tutorials"></a>

## Tutorials

- [Importing images](../tutorials/assets_pipeline/importing_images.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | resource_local_to_scene | `false` (overrides [Resource](class_resource.md#class-resource-property-resource-local-to-scene)) |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [ImageTexture](class_imagetexture.md#class-imagetexture) | [create_from_image](class_imagetexture.md#class-imagetexture-method-create-from-image)(image: [Image](class_image.md#class-image)) static |
| void | [set_image](class_imagetexture.md#class-imagetexture-method-set-image)(image: [Image](class_image.md#class-image)) |
| void | [set_size_override](class_imagetexture.md#class-imagetexture-method-set-size-override)(size: [Vector2i](class_vector2i.md#class-vector2i)) |
| void | [update](class_imagetexture.md#class-imagetexture-method-update)(image: [Image](class_image.md#class-image)) |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-imagetexture-method-create-from-image"></a>

[ImageTexture](class_imagetexture.md#class-imagetexture) **create_from_image**(image: [Image](class_image.md#class-image)) static [🔗](class_imagetexture.md#class-imagetexture-method-create-from-image)

Creates a new **ImageTexture** and initializes it by allocating and setting the data from an [Image](class_image.md#class-image).

---


<a id="class-imagetexture-method-set-image"></a>

void **set_image**(image: [Image](class_image.md#class-image)) [🔗](class_imagetexture.md#class-imagetexture-method-set-image)

Replaces the texture's data with a new [Image](class_image.md#class-image). This will re-allocate new memory for the texture.

If you want to update the image, but don't need to change its parameters (format, size), use [update()](class_imagetexture.md#class-imagetexture-method-update) instead for better performance.

---


<a id="class-imagetexture-method-set-size-override"></a>

void **set_size_override**(size: [Vector2i](class_vector2i.md#class-vector2i)) [🔗](class_imagetexture.md#class-imagetexture-method-set-size-override)

Resizes the texture to the specified dimensions.

---


<a id="class-imagetexture-method-update"></a>

void **update**(image: [Image](class_image.md#class-image)) [🔗](class_imagetexture.md#class-imagetexture-method-update)

Replaces the texture's data with a new [Image](class_image.md#class-image).

**Note:** The texture has to be created using [create_from_image()](class_imagetexture.md#class-imagetexture-method-create-from-image) or initialized first with the [set_image()](class_imagetexture.md#class-imagetexture-method-set-image) method before it can be updated. The new image dimensions, format, and mipmaps configuration should match the existing texture's image configuration.

Use this method over [set_image()](class_imagetexture.md#class-imagetexture-method-set-image) if you need to update the texture frequently, which is faster than allocating additional memory for a new texture each time.
