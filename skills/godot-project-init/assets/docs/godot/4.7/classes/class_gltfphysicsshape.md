> Source: https://docs.godotengine.org/en/4.7/classes/class_gltfphysicsshape.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="gltfphysicsshape"></a>

<a id="class-gltfphysicsshape"></a>

# GLTFPhysicsShape

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Represents a glTF physics shape.

<a id="description"></a>

## Description

Represents a physics shape as defined by the `OMI_physics_shape` or `OMI_collider` glTF extensions. This class is an intermediary between the glTF data and Godot's nodes, and it's abstracted in a way that allows adding support for different glTF physics extensions in the future.

<a id="tutorials"></a>

## Tutorials

- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving.md)
- [OMI_physics_shape glTF extension](https://github.com/omigroup/gltf-extensions/tree/main/extensions/2.0/OMI_physics_shape)
- [OMI_collider glTF extension](https://github.com/omigroup/gltf-extensions/tree/main/extensions/2.0/Archived/OMI_collider)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [height](class_gltfphysicsshape.md#class-gltfphysicsshape-property-height) | `2.0` |
| [ImporterMesh](class_importermesh.md#class-importermesh) | [importer_mesh](class_gltfphysicsshape.md#class-gltfphysicsshape-property-importer-mesh) |  |
| [bool](class_bool.md#class-bool) | [is_trigger](class_gltfphysicsshape.md#class-gltfphysicsshape-property-is-trigger) | `false` |
| [int](class_int.md#class-int) | [mesh_index](class_gltfphysicsshape.md#class-gltfphysicsshape-property-mesh-index) | `-1` |
| [float](class_float.md#class-float) | [radius](class_gltfphysicsshape.md#class-gltfphysicsshape-property-radius) | `0.5` |
| [String](class_string.md#class-string) | [shape_type](class_gltfphysicsshape.md#class-gltfphysicsshape-property-shape-type) | `""` |
| [Vector3](class_vector3.md#class-vector3) | [size](class_gltfphysicsshape.md#class-gltfphysicsshape-property-size) | `Vector3(1, 1, 1)` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [GLTFPhysicsShape](class_gltfphysicsshape.md#class-gltfphysicsshape) | [from_dictionary](class_gltfphysicsshape.md#class-gltfphysicsshape-method-from-dictionary)(dictionary: [Dictionary](class_dictionary.md#class-dictionary)) static |
| [GLTFPhysicsShape](class_gltfphysicsshape.md#class-gltfphysicsshape) | [from_node](class_gltfphysicsshape.md#class-gltfphysicsshape-method-from-node)(shape_node: [CollisionShape3D](class_collisionshape3d.md#class-collisionshape3d)) static |
| [GLTFPhysicsShape](class_gltfphysicsshape.md#class-gltfphysicsshape) | [from_resource](class_gltfphysicsshape.md#class-gltfphysicsshape-method-from-resource)(shape_resource: [Shape3D](class_shape3d.md#class-shape3d)) static |
| [Dictionary](class_dictionary.md#class-dictionary) | [to_dictionary](class_gltfphysicsshape.md#class-gltfphysicsshape-method-to-dictionary)() const |
| [CollisionShape3D](class_collisionshape3d.md#class-collisionshape3d) | [to_node](class_gltfphysicsshape.md#class-gltfphysicsshape-method-to-node)(cache_shapes: [bool](class_bool.md#class-bool) = false) |
| [Shape3D](class_shape3d.md#class-shape3d) | [to_resource](class_gltfphysicsshape.md#class-gltfphysicsshape-method-to-resource)(cache_shapes: [bool](class_bool.md#class-bool) = false) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-gltfphysicsshape-property-height"></a>

[float](class_float.md#class-float) **height** = `2.0` [🔗](class_gltfphysicsshape.md#class-gltfphysicsshape-property-height)

- void **set_height**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_height**()

The height of the shape, in meters. This is only used when the shape type is `"capsule"` or `"cylinder"`. This value should not be negative, and for `"capsule"` it should be at least twice the radius.

---


<a id="class-gltfphysicsshape-property-importer-mesh"></a>

[ImporterMesh](class_importermesh.md#class-importermesh) **importer_mesh** [🔗](class_gltfphysicsshape.md#class-gltfphysicsshape-property-importer-mesh)

- void **set_importer_mesh**(value: [ImporterMesh](class_importermesh.md#class-importermesh))
- [ImporterMesh](class_importermesh.md#class-importermesh) **get_importer_mesh**()

The [ImporterMesh](class_importermesh.md#class-importermesh) resource of the shape. This is only used when the shape type is `"hull"` (convex hull) or `"trimesh"` (concave trimesh).

---


<a id="class-gltfphysicsshape-property-is-trigger"></a>

[bool](class_bool.md#class-bool) **is_trigger** = `false` [🔗](class_gltfphysicsshape.md#class-gltfphysicsshape-property-is-trigger)

- void **set_is_trigger**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_is_trigger**()

If `true`, indicates that this shape is a trigger. For Godot, this means that the shape should be a child of an [Area3D](class_area3d.md#class-area3d) node.

This is the only variable not used in the [to_node()](class_gltfphysicsshape.md#class-gltfphysicsshape-method-to-node) method, it's intended to be used alongside when deciding where to add the generated node as a child.

---


<a id="class-gltfphysicsshape-property-mesh-index"></a>

[int](class_int.md#class-int) **mesh_index** = `-1` [🔗](class_gltfphysicsshape.md#class-gltfphysicsshape-property-mesh-index)

- void **set_mesh_index**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_mesh_index**()

The index of the shape's mesh in the glTF file. This is only used when the shape type is `"hull"` (convex hull) or `"trimesh"` (concave trimesh).

---


<a id="class-gltfphysicsshape-property-radius"></a>

[float](class_float.md#class-float) **radius** = `0.5` [🔗](class_gltfphysicsshape.md#class-gltfphysicsshape-property-radius)

- void **set_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_radius**()

The radius of the shape, in meters. This is only used when the shape type is `"capsule"`, `"cylinder"`, or `"sphere"`. This value should not be negative.

---


<a id="class-gltfphysicsshape-property-shape-type"></a>

[String](class_string.md#class-string) **shape_type** = `""` [🔗](class_gltfphysicsshape.md#class-gltfphysicsshape-property-shape-type)

- void **set_shape_type**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_shape_type**()

The type of shape this shape represents. Valid values are `"box"`, `"capsule"`, `"cylinder"`, `"sphere"`, `"hull"`, and `"trimesh"`.

---


<a id="class-gltfphysicsshape-property-size"></a>

[Vector3](class_vector3.md#class-vector3) **size** = `Vector3(1, 1, 1)` [🔗](class_gltfphysicsshape.md#class-gltfphysicsshape-property-size)

- void **set_size**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_size**()

The size of the shape, in meters. This is only used when the shape type is `"box"`, and it represents the `"diameter"` of the box. This value should not be negative.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-gltfphysicsshape-method-from-dictionary"></a>

[GLTFPhysicsShape](class_gltfphysicsshape.md#class-gltfphysicsshape) **from_dictionary**(dictionary: [Dictionary](class_dictionary.md#class-dictionary)) static [🔗](class_gltfphysicsshape.md#class-gltfphysicsshape-method-from-dictionary)

Creates a new GLTFPhysicsShape instance by parsing the given [Dictionary](class_dictionary.md#class-dictionary).

---


<a id="class-gltfphysicsshape-method-from-node"></a>

[GLTFPhysicsShape](class_gltfphysicsshape.md#class-gltfphysicsshape) **from_node**(shape_node: [CollisionShape3D](class_collisionshape3d.md#class-collisionshape3d)) static [🔗](class_gltfphysicsshape.md#class-gltfphysicsshape-method-from-node)

Creates a new GLTFPhysicsShape instance from the given Godot [CollisionShape3D](class_collisionshape3d.md#class-collisionshape3d) node.

---


<a id="class-gltfphysicsshape-method-from-resource"></a>

[GLTFPhysicsShape](class_gltfphysicsshape.md#class-gltfphysicsshape) **from_resource**(shape_resource: [Shape3D](class_shape3d.md#class-shape3d)) static [🔗](class_gltfphysicsshape.md#class-gltfphysicsshape-method-from-resource)

Creates a new GLTFPhysicsShape instance from the given Godot [Shape3D](class_shape3d.md#class-shape3d) resource.

---


<a id="class-gltfphysicsshape-method-to-dictionary"></a>

[Dictionary](class_dictionary.md#class-dictionary) **to_dictionary**() const [🔗](class_gltfphysicsshape.md#class-gltfphysicsshape-method-to-dictionary)

Serializes this GLTFPhysicsShape instance into a [Dictionary](class_dictionary.md#class-dictionary) in the format defined by `OMI_physics_shape`.

---


<a id="class-gltfphysicsshape-method-to-node"></a>

[CollisionShape3D](class_collisionshape3d.md#class-collisionshape3d) **to_node**(cache_shapes: [bool](class_bool.md#class-bool) = false) [🔗](class_gltfphysicsshape.md#class-gltfphysicsshape-method-to-node)

Converts this GLTFPhysicsShape instance into a Godot [CollisionShape3D](class_collisionshape3d.md#class-collisionshape3d) node.

---


<a id="class-gltfphysicsshape-method-to-resource"></a>

[Shape3D](class_shape3d.md#class-shape3d) **to_resource**(cache_shapes: [bool](class_bool.md#class-bool) = false) [🔗](class_gltfphysicsshape.md#class-gltfphysicsshape-method-to-resource)

Converts this GLTFPhysicsShape instance into a Godot [Shape3D](class_shape3d.md#class-shape3d) resource.
