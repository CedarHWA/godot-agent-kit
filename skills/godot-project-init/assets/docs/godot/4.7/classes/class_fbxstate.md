> Source: https://docs.godotengine.org/en/4.7/classes/class_fbxstate.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="fbxstate"></a>

<a id="class-fbxstate"></a>

# FBXState

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [GLTFState](class_gltfstate.md#class-gltfstate) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

<a id="description"></a>

## Description

The FBXState handles the state data imported from FBX files.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [allow_geometry_helper_nodes](class_fbxstate.md#class-fbxstate-property-allow-geometry-helper-nodes) | `false` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-fbxstate-property-allow-geometry-helper-nodes"></a>

[bool](class_bool.md#class-bool) **allow_geometry_helper_nodes** = `false` [🔗](class_fbxstate.md#class-fbxstate-property-allow-geometry-helper-nodes)

- void **set_allow_geometry_helper_nodes**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_allow_geometry_helper_nodes**()

If `true`, the import process used auxiliary nodes called geometry helper nodes. These nodes help preserve the pivots and transformations of the original 3D model during import.
