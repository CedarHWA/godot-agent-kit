> Source: https://docs.godotengine.org/en/4.7/classes/class_editorsceneformatimporterfbx2gltf.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="editorsceneformatimporterfbx2gltf"></a>

<a id="class-editorsceneformatimporterfbx2gltf"></a>

# EditorSceneFormatImporterFBX2GLTF

**Inherits:** [EditorSceneFormatImporter](class_editorsceneformatimporter.md#class-editorsceneformatimporter) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Importer for the `.fbx` scene file format.

<a id="description"></a>

## Description

Imports Autodesk FBX 3D scenes by way of converting them to glTF 2.0 using the FBX2glTF command line tool.

The location of the FBX2glTF binary is set via the [EditorSettings.filesystem/import/fbx/fbx2gltf_path](class_editorsettings.md#class-editorsettings-property-filesystem-import-fbx-fbx2gltf-path) editor setting.

This importer is only used if [ProjectSettings.filesystem/import/fbx2gltf/enabled](class_projectsettings.md#class-projectsettings-property-filesystem-import-fbx2gltf-enabled) is set to `true`.
