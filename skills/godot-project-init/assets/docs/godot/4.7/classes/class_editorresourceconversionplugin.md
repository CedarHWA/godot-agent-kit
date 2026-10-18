> Source: https://docs.godotengine.org/en/4.7/classes/class_editorresourceconversionplugin.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="editorresourceconversionplugin"></a>

<a id="class-editorresourceconversionplugin"></a>

# EditorResourceConversionPlugin

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Plugin for adding custom converters from one resource format to another in the editor resource picker context menu; for example, converting a [StandardMaterial3D](class_standardmaterial3d.md#class-standardmaterial3d) to a [ShaderMaterial](class_shadermaterial.md#class-shadermaterial).

<a id="description"></a>

## Description

**EditorResourceConversionPlugin** is invoked when the context menu is brought up for a resource in the editor inspector. Relevant conversion plugins will appear as menu options to convert the given resource to a target type.

Below shows an example of a basic plugin that will convert an [ImageTexture](class_imagetexture.md#class-imagetexture) to a [PortableCompressedTexture2D](class_portablecompressedtexture2d.md#class-portablecompressedtexture2d).

```gdscript
extends EditorResourceConversionPlugin

func _handles(resource: Resource):
    return resource is ImageTexture

func _converts_to():
    return "PortableCompressedTexture2D"

func _convert(itex: Resource):
    var ptex = PortableCompressedTexture2D.new()
    ptex.create_from_image(itex.get_image(), PortableCompressedTexture2D.COMPRESSION_MODE_LOSSLESS)
    return ptex
```

To use an **EditorResourceConversionPlugin**, register it using the [EditorPlugin.add_resource_conversion_plugin()](class_editorplugin.md#class-editorplugin-method-add-resource-conversion-plugin) method first.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Resource](class_resource.md#class-resource) | [_convert](class_editorresourceconversionplugin.md#class-editorresourceconversionplugin-private-method-convert)(resource: [Resource](class_resource.md#class-resource)) virtual const |
| [String](class_string.md#class-string) | [_converts_to](class_editorresourceconversionplugin.md#class-editorresourceconversionplugin-private-method-converts-to)() virtual const |
| [bool](class_bool.md#class-bool) | [_handles](class_editorresourceconversionplugin.md#class-editorresourceconversionplugin-private-method-handles)(resource: [Resource](class_resource.md#class-resource)) virtual const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-editorresourceconversionplugin-private-method-convert"></a>

[Resource](class_resource.md#class-resource) **_convert**(resource: [Resource](class_resource.md#class-resource)) virtual const [🔗](class_editorresourceconversionplugin.md#class-editorresourceconversionplugin-private-method-convert)

Takes an input [Resource](class_resource.md#class-resource) and converts it to the type given in [_converts_to()](class_editorresourceconversionplugin.md#class-editorresourceconversionplugin-private-method-converts-to). The returned [Resource](class_resource.md#class-resource) is the result of the conversion, and the input [Resource](class_resource.md#class-resource) remains unchanged.

---


<a id="class-editorresourceconversionplugin-private-method-converts-to"></a>

[String](class_string.md#class-string) **_converts_to**() virtual const [🔗](class_editorresourceconversionplugin.md#class-editorresourceconversionplugin-private-method-converts-to)

Returns the class name of the target type of [Resource](class_resource.md#class-resource) that this plugin converts source resources to.

---


<a id="class-editorresourceconversionplugin-private-method-handles"></a>

[bool](class_bool.md#class-bool) **_handles**(resource: [Resource](class_resource.md#class-resource)) virtual const [🔗](class_editorresourceconversionplugin.md#class-editorresourceconversionplugin-private-method-handles)

Called to determine whether a particular [Resource](class_resource.md#class-resource) can be converted to the target resource type by this plugin.
