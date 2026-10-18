> Source: https://docs.godotengine.org/en/4.7/classes/class_imageformatloader.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="imageformatloader"></a>

<a id="class-imageformatloader"></a>

# ImageFormatLoader

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [ImageFormatLoaderExtension](class_imageformatloaderextension.md#class-imageformatloaderextension)

Base class to add support for specific image formats.

<a id="description"></a>

## Description

The engine supports multiple image formats out of the box (PNG, SVG, JPEG, WebP to name a few), but you can choose to implement support for additional image formats by extending [ImageFormatLoaderExtension](class_imageformatloaderextension.md#class-imageformatloaderextension).

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-imageformatloader-loaderflags"></a>

flags **LoaderFlags**: [🔗](class_imageformatloader.md#enum-imageformatloader-loaderflags)

<a id="class-imageformatloader-constant-flag-none"></a>

[LoaderFlags](class_imageformatloader.md#enum-imageformatloader-loaderflags) **FLAG_NONE** = `0`

Default loading behavior. No processing is applied to the image.

<a id="class-imageformatloader-constant-flag-force-linear"></a>

[LoaderFlags](class_imageformatloader.md#enum-imageformatloader-loaderflags) **FLAG_FORCE_LINEAR** = `1`

If set, the image is converted from sRGB to linear encoding.

<a id="class-imageformatloader-constant-flag-convert-colors"></a>

[LoaderFlags](class_imageformatloader.md#enum-imageformatloader-loaderflags) **FLAG_CONVERT_COLORS** = `2`

If set, a predefined color map is applied to the image. Used when [ResourceImporterTexture.editor/convert_colors_with_editor_theme](class_resourceimportertexture.md#class-resourceimportertexture-property-editor-convert-colors-with-editor-theme) is `true`.
