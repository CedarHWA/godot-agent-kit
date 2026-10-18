> Source: https://docs.godotengine.org/en/4.7/classes/class_imageformatloaderextension.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="imageformatloaderextension"></a>

<a id="class-imageformatloaderextension"></a>

# ImageFormatLoaderExtension

**Inherits:** [ImageFormatLoader](class_imageformatloader.md#class-imageformatloader) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Base class for creating [ImageFormatLoader](class_imageformatloader.md#class-imageformatloader) extensions (adding support for extra image formats).

<a id="description"></a>

## Description

The engine supports multiple image formats out of the box (PNG, SVG, JPEG, WebP to name a few), but you can choose to implement support for additional image formats by extending this class.

Be sure to respect the documented return types and values. You should create an instance of it, and call [add_format_loader()](class_imageformatloaderextension.md#class-imageformatloaderextension-method-add-format-loader) to register that loader during the initialization phase.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [_get_recognized_extensions](class_imageformatloaderextension.md#class-imageformatloaderextension-private-method-get-recognized-extensions)() virtual const |
| [Error](class_@globalscope.md#enum-globalscope-error) | [_load_image](class_imageformatloaderextension.md#class-imageformatloaderextension-private-method-load-image)(image: [Image](class_image.md#class-image), fileaccess: [FileAccess](class_fileaccess.md#class-fileaccess), flags: BitField[[LoaderFlags](class_imageformatloader.md#enum-imageformatloader-loaderflags)], scale: [float](class_float.md#class-float)) virtual |
| void | [add_format_loader](class_imageformatloaderextension.md#class-imageformatloaderextension-method-add-format-loader)() |
| void | [remove_format_loader](class_imageformatloaderextension.md#class-imageformatloaderextension-method-remove-format-loader)() |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-imageformatloaderextension-private-method-get-recognized-extensions"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **_get_recognized_extensions**() virtual const [🔗](class_imageformatloaderextension.md#class-imageformatloaderextension-private-method-get-recognized-extensions)

Returns the list of file extensions for this image format. Files with the given extensions will be treated as image file and loaded using this class.

---


<a id="class-imageformatloaderextension-private-method-load-image"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **_load_image**(image: [Image](class_image.md#class-image), fileaccess: [FileAccess](class_fileaccess.md#class-fileaccess), flags: BitField[[LoaderFlags](class_imageformatloader.md#enum-imageformatloader-loaderflags)], scale: [float](class_float.md#class-float)) virtual [🔗](class_imageformatloaderextension.md#class-imageformatloaderextension-private-method-load-image)

Loads the content of `fileaccess` into the provided `image`.

---


<a id="class-imageformatloaderextension-method-add-format-loader"></a>

void **add_format_loader**() [🔗](class_imageformatloaderextension.md#class-imageformatloaderextension-method-add-format-loader)

Add this format loader to the engine, allowing it to recognize the file extensions returned by [_get_recognized_extensions()](class_imageformatloaderextension.md#class-imageformatloaderextension-private-method-get-recognized-extensions).

---


<a id="class-imageformatloaderextension-method-remove-format-loader"></a>

void **remove_format_loader**() [🔗](class_imageformatloaderextension.md#class-imageformatloaderextension-method-remove-format-loader)

Remove this format loader from the engine.
