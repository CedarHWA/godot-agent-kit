> Source: https://docs.godotengine.org/en/4.7/classes/class_placeholdermesh.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="placeholdermesh"></a>

<a id="class-placeholdermesh"></a>

# PlaceholderMesh

**Inherits:** [Mesh](class_mesh.md#class-mesh) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Placeholder class for a mesh.

<a id="description"></a>

## Description

This class is used when loading a project that uses a [Mesh](class_mesh.md#class-mesh) subclass in 2 conditions:

- When running the project exported in dedicated server mode, only the texture's dimensions are kept (as they may be relied upon for gameplay purposes or positioning of other elements). This allows reducing the exported PCK's size significantly.
- When this subclass is missing due to using a different engine version or build (e.g. modules disabled).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [AABB](class_aabb.md#class-aabb) | [aabb](class_placeholdermesh.md#class-placeholdermesh-property-aabb) | `AABB(0, 0, 0, 0, 0, 0)` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-placeholdermesh-property-aabb"></a>

[AABB](class_aabb.md#class-aabb) **aabb** = `AABB(0, 0, 0, 0, 0, 0)` [🔗](class_placeholdermesh.md#class-placeholdermesh-property-aabb)

- void **set_aabb**(value: [AABB](class_aabb.md#class-aabb))
- [AABB](class_aabb.md#class-aabb) **get_aabb**()

The smallest [AABB](class_aabb.md#class-aabb) enclosing this mesh in local space.
