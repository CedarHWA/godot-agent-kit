> Source: https://docs.godotengine.org/en/4.7/classes/class_gltfphysicsbody.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="gltfphysicsbody"></a>

<a id="class-gltfphysicsbody"></a>

# GLTFPhysicsBody

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Represents a glTF physics body.

<a id="description"></a>

## Description

Represents a physics body as an intermediary between the `OMI_physics_body` glTF data and Godot's nodes, and it's abstracted in a way that allows adding support for different glTF physics extensions in the future.

<a id="tutorials"></a>

## Tutorials

- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving.md)
- [OMI_physics_body glTF extension](https://github.com/omigroup/gltf-extensions/tree/main/extensions/2.0/OMI_physics_body)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Vector3](class_vector3.md#class-vector3) | [angular_velocity](class_gltfphysicsbody.md#class-gltfphysicsbody-property-angular-velocity) | `Vector3(0, 0, 0)` |
| [String](class_string.md#class-string) | [body_type](class_gltfphysicsbody.md#class-gltfphysicsbody-property-body-type) | `"rigid"` |
| [Vector3](class_vector3.md#class-vector3) | [center_of_mass](class_gltfphysicsbody.md#class-gltfphysicsbody-property-center-of-mass) | `Vector3(0, 0, 0)` |
| [Vector3](class_vector3.md#class-vector3) | [inertia_diagonal](class_gltfphysicsbody.md#class-gltfphysicsbody-property-inertia-diagonal) | `Vector3(0, 0, 0)` |
| [Quaternion](class_quaternion.md#class-quaternion) | [inertia_orientation](class_gltfphysicsbody.md#class-gltfphysicsbody-property-inertia-orientation) | `Quaternion(0, 0, 0, 1)` |
| [Basis](class_basis.md#class-basis) | [inertia_tensor](class_gltfphysicsbody.md#class-gltfphysicsbody-property-inertia-tensor) | `Basis(0, 0, 0, 0, 0, 0, 0, 0, 0)` |
| [Vector3](class_vector3.md#class-vector3) | [linear_velocity](class_gltfphysicsbody.md#class-gltfphysicsbody-property-linear-velocity) | `Vector3(0, 0, 0)` |
| [float](class_float.md#class-float) | [mass](class_gltfphysicsbody.md#class-gltfphysicsbody-property-mass) | `1.0` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [GLTFPhysicsBody](class_gltfphysicsbody.md#class-gltfphysicsbody) | [from_dictionary](class_gltfphysicsbody.md#class-gltfphysicsbody-method-from-dictionary)(dictionary: [Dictionary](class_dictionary.md#class-dictionary)) static |
| [GLTFPhysicsBody](class_gltfphysicsbody.md#class-gltfphysicsbody) | [from_node](class_gltfphysicsbody.md#class-gltfphysicsbody-method-from-node)(body_node: [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d)) static |
| [Dictionary](class_dictionary.md#class-dictionary) | [to_dictionary](class_gltfphysicsbody.md#class-gltfphysicsbody-method-to-dictionary)() const |
| [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d) | [to_node](class_gltfphysicsbody.md#class-gltfphysicsbody-method-to-node)() const |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-gltfphysicsbody-property-angular-velocity"></a>

[Vector3](class_vector3.md#class-vector3) **angular_velocity** = `Vector3(0, 0, 0)` [🔗](class_gltfphysicsbody.md#class-gltfphysicsbody-property-angular-velocity)

- void **set_angular_velocity**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_angular_velocity**()

The angular velocity of the physics body, in radians per second. This is only used when the body type is "rigid" or "vehicle".

---


<a id="class-gltfphysicsbody-property-body-type"></a>

[String](class_string.md#class-string) **body_type** = `"rigid"` [🔗](class_gltfphysicsbody.md#class-gltfphysicsbody-property-body-type)

- void **set_body_type**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_body_type**()

The type of the body.

When importing, this controls what type of [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d) node Godot should generate. Valid values are `"static"`, `"animatable"`, `"character"`, `"rigid"`, `"vehicle"`, and `"trigger"`.

When exporting, this will be squashed down to one of `"static"`, `"kinematic"`, or `"dynamic"` motion types, or the `"trigger"` property.

---


<a id="class-gltfphysicsbody-property-center-of-mass"></a>

[Vector3](class_vector3.md#class-vector3) **center_of_mass** = `Vector3(0, 0, 0)` [🔗](class_gltfphysicsbody.md#class-gltfphysicsbody-property-center-of-mass)

- void **set_center_of_mass**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_center_of_mass**()

The center of mass of the body, in meters. This is in local space relative to the body. By default, the center of the mass is the body's origin.

---


<a id="class-gltfphysicsbody-property-inertia-diagonal"></a>

[Vector3](class_vector3.md#class-vector3) **inertia_diagonal** = `Vector3(0, 0, 0)` [🔗](class_gltfphysicsbody.md#class-gltfphysicsbody-property-inertia-diagonal)

- void **set_inertia_diagonal**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_inertia_diagonal**()

The inertia strength of the physics body, in kilogram meter squared (kg⋅m²). This represents the inertia around the principle axes, the diagonal of the inertia tensor matrix. This is only used when the body type is "rigid" or "vehicle".

When converted to a Godot [RigidBody3D](class_rigidbody3d.md#class-rigidbody3d) node, if this value is zero, then the inertia will be calculated automatically.

---


<a id="class-gltfphysicsbody-property-inertia-orientation"></a>

[Quaternion](class_quaternion.md#class-quaternion) **inertia_orientation** = `Quaternion(0, 0, 0, 1)` [🔗](class_gltfphysicsbody.md#class-gltfphysicsbody-property-inertia-orientation)

- void **set_inertia_orientation**(value: [Quaternion](class_quaternion.md#class-quaternion))
- [Quaternion](class_quaternion.md#class-quaternion) **get_inertia_orientation**()

The inertia orientation of the physics body. This defines the rotation of the inertia's principle axes relative to the object's local axes. This is only used when the body type is "rigid" or "vehicle" and [inertia_diagonal](class_gltfphysicsbody.md#class-gltfphysicsbody-property-inertia-diagonal) is set to a non-zero value.

---


<a id="class-gltfphysicsbody-property-inertia-tensor"></a>

[Basis](class_basis.md#class-basis) **inertia_tensor** = `Basis(0, 0, 0, 0, 0, 0, 0, 0, 0)` [🔗](class_gltfphysicsbody.md#class-gltfphysicsbody-property-inertia-tensor)

- void **set_inertia_tensor**(value: [Basis](class_basis.md#class-basis))
- [Basis](class_basis.md#class-basis) **get_inertia_tensor**()

**Deprecated:** This property may be changed or removed in future versions.

The inertia tensor of the physics body, in kilogram meter squared (kg⋅m²). This is only used when the body type is "rigid" or "vehicle".

When converted to a Godot [RigidBody3D](class_rigidbody3d.md#class-rigidbody3d) node, if this value is zero, then the inertia will be calculated automatically.

---


<a id="class-gltfphysicsbody-property-linear-velocity"></a>

[Vector3](class_vector3.md#class-vector3) **linear_velocity** = `Vector3(0, 0, 0)` [🔗](class_gltfphysicsbody.md#class-gltfphysicsbody-property-linear-velocity)

- void **set_linear_velocity**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_linear_velocity**()

The linear velocity of the physics body, in meters per second. This is only used when the body type is "rigid" or "vehicle".

---


<a id="class-gltfphysicsbody-property-mass"></a>

[float](class_float.md#class-float) **mass** = `1.0` [🔗](class_gltfphysicsbody.md#class-gltfphysicsbody-property-mass)

- void **set_mass**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_mass**()

The mass of the physics body, in kilograms. This is only used when the body type is "rigid" or "vehicle".

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-gltfphysicsbody-method-from-dictionary"></a>

[GLTFPhysicsBody](class_gltfphysicsbody.md#class-gltfphysicsbody) **from_dictionary**(dictionary: [Dictionary](class_dictionary.md#class-dictionary)) static [🔗](class_gltfphysicsbody.md#class-gltfphysicsbody-method-from-dictionary)

Creates a new GLTFPhysicsBody instance by parsing the given [Dictionary](class_dictionary.md#class-dictionary) in the `OMI_physics_body` glTF extension format.

---


<a id="class-gltfphysicsbody-method-from-node"></a>

[GLTFPhysicsBody](class_gltfphysicsbody.md#class-gltfphysicsbody) **from_node**(body_node: [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d)) static [🔗](class_gltfphysicsbody.md#class-gltfphysicsbody-method-from-node)

Creates a new GLTFPhysicsBody instance from the given Godot [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d) node.

---


<a id="class-gltfphysicsbody-method-to-dictionary"></a>

[Dictionary](class_dictionary.md#class-dictionary) **to_dictionary**() const [🔗](class_gltfphysicsbody.md#class-gltfphysicsbody-method-to-dictionary)

Serializes this GLTFPhysicsBody instance into a [Dictionary](class_dictionary.md#class-dictionary). It will be in the format expected by the `OMI_physics_body` glTF extension.

---


<a id="class-gltfphysicsbody-method-to-node"></a>

[CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d) **to_node**() const [🔗](class_gltfphysicsbody.md#class-gltfphysicsbody-method-to-node)

Converts this GLTFPhysicsBody instance into a Godot [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d) node.
