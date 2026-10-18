> Source: https://docs.godotengine.org/en/4.7/classes/class_physicsdirectspacestate3dextension.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="physicsdirectspacestate3dextension"></a>

<a id="class-physicsdirectspacestate3dextension"></a>

# PhysicsDirectSpaceState3DExtension

**Inherits:** [PhysicsDirectSpaceState3D](class_physicsdirectspacestate3d.md#class-physicsdirectspacestate3d) **<** [Object](class_object.md#class-object)

Provides virtual methods that can be overridden to create custom [PhysicsDirectSpaceState3D](class_physicsdirectspacestate3d.md#class-physicsdirectspacestate3d) implementations.

<a id="description"></a>

## Description

This class extends [PhysicsDirectSpaceState3D](class_physicsdirectspacestate3d.md#class-physicsdirectspacestate3d) by providing additional virtual methods that can be overridden. When these methods are overridden, they will be called instead of the internal methods of the physics server.

Intended for use with GDExtension to create custom implementations of [PhysicsDirectSpaceState3D](class_physicsdirectspacestate3d.md#class-physicsdirectspacestate3d).

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [_cast_motion](class_physicsdirectspacestate3dextension.md#class-physicsdirectspacestate3dextension-private-method-cast-motion)(shape_rid: [RID](class_rid.md#class-rid), transform: [Transform3D](class_transform3d.md#class-transform3d), motion: [Vector3](class_vector3.md#class-vector3), margin: [float](class_float.md#class-float), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), r_closest_safe: `float*`, r_closest_unsafe: `float*`, r_info: `PhysicsServer3DExtensionShapeRestInfo*`) virtual required |
| [bool](class_bool.md#class-bool) | [_collide_shape](class_physicsdirectspacestate3dextension.md#class-physicsdirectspacestate3dextension-private-method-collide-shape)(shape_rid: [RID](class_rid.md#class-rid), transform: [Transform3D](class_transform3d.md#class-transform3d), motion: [Vector3](class_vector3.md#class-vector3), margin: [float](class_float.md#class-float), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), r_results: `void*`, max_results: [int](class_int.md#class-int), r_result_count: `int32_t*`) virtual required |
| [Vector3](class_vector3.md#class-vector3) | [_get_closest_point_to_object_volume](class_physicsdirectspacestate3dextension.md#class-physicsdirectspacestate3dextension-private-method-get-closest-point-to-object-volume)(object: [RID](class_rid.md#class-rid), point: [Vector3](class_vector3.md#class-vector3)) virtual required const |
| [int](class_int.md#class-int) | [_intersect_point](class_physicsdirectspacestate3dextension.md#class-physicsdirectspacestate3dextension-private-method-intersect-point)(position: [Vector3](class_vector3.md#class-vector3), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), r_results: `PhysicsServer3DExtensionShapeResult*`, max_results: [int](class_int.md#class-int)) virtual required |
| [bool](class_bool.md#class-bool) | [_intersect_ray](class_physicsdirectspacestate3dextension.md#class-physicsdirectspacestate3dextension-private-method-intersect-ray)(from: [Vector3](class_vector3.md#class-vector3), to: [Vector3](class_vector3.md#class-vector3), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), hit_from_inside: [bool](class_bool.md#class-bool), hit_back_faces: [bool](class_bool.md#class-bool), pick_ray: [bool](class_bool.md#class-bool), r_result: `PhysicsServer3DExtensionRayResult*`) virtual required |
| [int](class_int.md#class-int) | [_intersect_shape](class_physicsdirectspacestate3dextension.md#class-physicsdirectspacestate3dextension-private-method-intersect-shape)(shape_rid: [RID](class_rid.md#class-rid), transform: [Transform3D](class_transform3d.md#class-transform3d), motion: [Vector3](class_vector3.md#class-vector3), margin: [float](class_float.md#class-float), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), r_result_count: `PhysicsServer3DExtensionShapeResult*`, max_results: [int](class_int.md#class-int)) virtual required |
| [bool](class_bool.md#class-bool) | [_rest_info](class_physicsdirectspacestate3dextension.md#class-physicsdirectspacestate3dextension-private-method-rest-info)(shape_rid: [RID](class_rid.md#class-rid), transform: [Transform3D](class_transform3d.md#class-transform3d), motion: [Vector3](class_vector3.md#class-vector3), margin: [float](class_float.md#class-float), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), r_rest_info: `PhysicsServer3DExtensionShapeRestInfo*`) virtual required |
| [bool](class_bool.md#class-bool) | [is_body_excluded_from_query](class_physicsdirectspacestate3dextension.md#class-physicsdirectspacestate3dextension-method-is-body-excluded-from-query)(body: [RID](class_rid.md#class-rid)) const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-physicsdirectspacestate3dextension-private-method-cast-motion"></a>

[bool](class_bool.md#class-bool) **_cast_motion**(shape_rid: [RID](class_rid.md#class-rid), transform: [Transform3D](class_transform3d.md#class-transform3d), motion: [Vector3](class_vector3.md#class-vector3), margin: [float](class_float.md#class-float), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), r_closest_safe: `float*`, r_closest_unsafe: `float*`, r_info: `PhysicsServer3DExtensionShapeRestInfo*`) virtual required [🔗](class_physicsdirectspacestate3dextension.md#class-physicsdirectspacestate3dextension-private-method-cast-motion)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectspacestate3dextension-private-method-collide-shape"></a>

[bool](class_bool.md#class-bool) **_collide_shape**(shape_rid: [RID](class_rid.md#class-rid), transform: [Transform3D](class_transform3d.md#class-transform3d), motion: [Vector3](class_vector3.md#class-vector3), margin: [float](class_float.md#class-float), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), r_results: `void*`, max_results: [int](class_int.md#class-int), r_result_count: `int32_t*`) virtual required [🔗](class_physicsdirectspacestate3dextension.md#class-physicsdirectspacestate3dextension-private-method-collide-shape)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectspacestate3dextension-private-method-get-closest-point-to-object-volume"></a>

[Vector3](class_vector3.md#class-vector3) **_get_closest_point_to_object_volume**(object: [RID](class_rid.md#class-rid), point: [Vector3](class_vector3.md#class-vector3)) virtual required const [🔗](class_physicsdirectspacestate3dextension.md#class-physicsdirectspacestate3dextension-private-method-get-closest-point-to-object-volume)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectspacestate3dextension-private-method-intersect-point"></a>

[int](class_int.md#class-int) **_intersect_point**(position: [Vector3](class_vector3.md#class-vector3), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), r_results: `PhysicsServer3DExtensionShapeResult*`, max_results: [int](class_int.md#class-int)) virtual required [🔗](class_physicsdirectspacestate3dextension.md#class-physicsdirectspacestate3dextension-private-method-intersect-point)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectspacestate3dextension-private-method-intersect-ray"></a>

[bool](class_bool.md#class-bool) **_intersect_ray**(from: [Vector3](class_vector3.md#class-vector3), to: [Vector3](class_vector3.md#class-vector3), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), hit_from_inside: [bool](class_bool.md#class-bool), hit_back_faces: [bool](class_bool.md#class-bool), pick_ray: [bool](class_bool.md#class-bool), r_result: `PhysicsServer3DExtensionRayResult*`) virtual required [🔗](class_physicsdirectspacestate3dextension.md#class-physicsdirectspacestate3dextension-private-method-intersect-ray)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectspacestate3dextension-private-method-intersect-shape"></a>

[int](class_int.md#class-int) **_intersect_shape**(shape_rid: [RID](class_rid.md#class-rid), transform: [Transform3D](class_transform3d.md#class-transform3d), motion: [Vector3](class_vector3.md#class-vector3), margin: [float](class_float.md#class-float), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), r_result_count: `PhysicsServer3DExtensionShapeResult*`, max_results: [int](class_int.md#class-int)) virtual required [🔗](class_physicsdirectspacestate3dextension.md#class-physicsdirectspacestate3dextension-private-method-intersect-shape)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectspacestate3dextension-private-method-rest-info"></a>

[bool](class_bool.md#class-bool) **_rest_info**(shape_rid: [RID](class_rid.md#class-rid), transform: [Transform3D](class_transform3d.md#class-transform3d), motion: [Vector3](class_vector3.md#class-vector3), margin: [float](class_float.md#class-float), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), r_rest_info: `PhysicsServer3DExtensionShapeRestInfo*`) virtual required [🔗](class_physicsdirectspacestate3dextension.md#class-physicsdirectspacestate3dextension-private-method-rest-info)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectspacestate3dextension-method-is-body-excluded-from-query"></a>

[bool](class_bool.md#class-bool) **is_body_excluded_from_query**(body: [RID](class_rid.md#class-rid)) const [🔗](class_physicsdirectspacestate3dextension.md#class-physicsdirectspacestate3dextension-method-is-body-excluded-from-query)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!
