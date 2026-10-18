> Source: https://docs.godotengine.org/en/4.7/classes/class_fbxdocument.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="fbxdocument"></a>

<a id="class-fbxdocument"></a>

# FBXDocument

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [GLTFDocument](class_gltfdocument.md#class-gltfdocument) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Handles FBX documents.

<a id="description"></a>

## Description

The FBXDocument handles FBX documents. It provides methods to append data from buffers or files, generate scenes, and register/unregister document extensions.

When exporting FBX from Blender, use the "FBX Units Scale" option. The "FBX Units Scale" option sets the correct scale factor and avoids manual adjustments when re-importing into Blender, such as through glTF export.
