> Source: https://docs.godotengine.org/en/4.7/classes/class_resourceimporter.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="resourceimporter"></a>

<a id="class-resourceimporter"></a>

# ResourceImporter

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [EditorImportPlugin](class_editorimportplugin.md#class-editorimportplugin), [ResourceImporterBitMap](class_resourceimporterbitmap.md#class-resourceimporterbitmap), [ResourceImporterBMFont](class_resourceimporterbmfont.md#class-resourceimporterbmfont), [ResourceImporterCSVTranslation](class_resourceimportercsvtranslation.md#class-resourceimportercsvtranslation), [ResourceImporterDynamicFont](class_resourceimporterdynamicfont.md#class-resourceimporterdynamicfont), [ResourceImporterImage](class_resourceimporterimage.md#class-resourceimporterimage), [ResourceImporterImageFont](class_resourceimporterimagefont.md#class-resourceimporterimagefont), [ResourceImporterLayeredTexture](class_resourceimporterlayeredtexture.md#class-resourceimporterlayeredtexture), [ResourceImporterMP3](class_resourceimportermp3.md#class-resourceimportermp3), [ResourceImporterOBJ](class_resourceimporterobj.md#class-resourceimporterobj), [ResourceImporterOggVorbis](class_resourceimporteroggvorbis.md#class-resourceimporteroggvorbis), [ResourceImporterScene](class_resourceimporterscene.md#class-resourceimporterscene), [ResourceImporterShaderFile](class_resourceimportershaderfile.md#class-resourceimportershaderfile), [ResourceImporterSVG](class_resourceimportersvg.md#class-resourceimportersvg), [ResourceImporterTexture](class_resourceimportertexture.md#class-resourceimportertexture), [ResourceImporterTextureAtlas](class_resourceimportertextureatlas.md#class-resourceimportertextureatlas), [ResourceImporterWAV](class_resourceimporterwav.md#class-resourceimporterwav)

Base class for resource importers.

<a id="description"></a>

## Description

This is the base class for Godot's resource importers. To implement your own resource importers using editor plugins, see [EditorImportPlugin](class_editorimportplugin.md#class-editorimportplugin).

<a id="tutorials"></a>

## Tutorials

- [Import plugins](../tutorials/plugins/editor/import_plugins.md)

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [_get_build_dependencies](class_resourceimporter.md#class-resourceimporter-private-method-get-build-dependencies)(path: [String](class_string.md#class-string)) virtual const |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-resourceimporter-importorder"></a>

enum **ImportOrder**: [🔗](class_resourceimporter.md#enum-resourceimporter-importorder)

<a id="class-resourceimporter-constant-import-order-default"></a>

[ImportOrder](class_resourceimporter.md#enum-resourceimporter-importorder) **IMPORT_ORDER_DEFAULT** = `0`

The default import order.

<a id="class-resourceimporter-constant-import-order-scene"></a>

[ImportOrder](class_resourceimporter.md#enum-resourceimporter-importorder) **IMPORT_ORDER_SCENE** = `100`

The import order for scenes, which ensures scenes are imported *after* all other core resources such as textures. Custom importers should generally have an import order lower than `100` to avoid issues when importing scenes that rely on custom resources.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-resourceimporter-private-method-get-build-dependencies"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **_get_build_dependencies**(path: [String](class_string.md#class-string)) virtual const [🔗](class_resourceimporter.md#class-resourceimporter-private-method-get-build-dependencies)

Called when the engine compilation profile editor wants to check what build options an imported resource needs. For example, [ResourceImporterDynamicFont](class_resourceimporterdynamicfont.md#class-resourceimporterdynamicfont) has a property called [ResourceImporterDynamicFont.multichannel_signed_distance_field](class_resourceimporterdynamicfont.md#class-resourceimporterdynamicfont-property-multichannel-signed-distance-field), that depends on the engine to be build with the "msdfgen" module. If that resource happened to be a custom one, it would be handled like this:

```gdscript
func _get_build_dependencies(path):
    var resource = load(path)
    var dependencies = PackedStringArray()

    if resource.multichannel_signed_distance_field:
        dependencies.push_back("module_msdfgen_enabled")

    return dependencies
```
