> Source: https://docs.godotengine.org/en/4.7/classes/class_physicsdirectspacestate2dextension.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="physicsdirectspacestate2dextension"></a>

<a id="class-physicsdirectspacestate2dextension"></a>

# PhysicsDirectSpaceState2DExtension

**Inherits:** [PhysicsDirectSpaceState2D](class_physicsdirectspacestate2d.md#class-physicsdirectspacestate2d) **<** [Object](class_object.md#class-object)

Provides virtual methods that can be overridden to create custom [PhysicsDirectSpaceState2D](class_physicsdirectspacestate2d.md#class-physicsdirectspacestate2d) implementations.

<a id="description"></a>

## Description

This class extends [PhysicsDirectSpaceState2D](class_physicsdirectspacestate2d.md#class-physicsdirectspacestate2d) by providing additional virtual methods that can be overridden. When these methods are overridden, they will be called instead of the internal methods of the physics server.

Intended for use with GDExtension to create custom implementations of [PhysicsDirectSpaceState2D](class_physicsdirectspacestate2d.md#class-physicsdirectspacestate2d).

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [_cast_motion](class_physicsdirectspacestate2dextension.md#class-physicsdirectspacestate2dextension-private-method-cast-motion)(shape_rid: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d), motion: [Vector2](class_vector2.md#class-vector2), margin: [float](class_float.md#class-float), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), r_closest_safe: `float*`, r_closest_unsafe: `float*`) virtual required |
| [bool](class_bool.md#class-bool) | [_collide_shape](class_physicsdirectspacestate2dextension.md#class-physicsdirectspacestate2dextension-private-method-collide-shape)(shape_rid: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d), motion: [Vector2](class_vector2.md#class-vector2), margin: [float](class_float.md#class-float), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), r_results: `void*`, max_results: [int](class_int.md#class-int), r_result_count: `int32_t*`) virtual required |
| [int](class_int.md#class-int) | [_intersect_point](class_physicsdirectspacestate2dextension.md#class-physicsdirectspacestate2dextension-private-method-intersect-point)(position: [Vector2](class_vector2.md#class-vector2), canvas_instance_id: [int](class_int.md#class-int), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), r_results: `PhysicsServer2DExtensionShapeResult*`, max_results: [int](class_int.md#class-int)) virtual required |
| [bool](class_bool.md#class-bool) | [_intersect_ray](class_physicsdirectspacestate2dextension.md#class-physicsdirectspacestate2dextension-private-method-intersect-ray)(from: [Vector2](class_vector2.md#class-vector2), to: [Vector2](class_vector2.md#class-vector2), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), hit_from_inside: [bool](class_bool.md#class-bool), r_result: `PhysicsServer2DExtensionRayResult*`) virtual required |
| [int](class_int.md#class-int) | [_intersect_shape](class_physicsdirectspacestate2dextension.md#class-physicsdirectspacestate2dextension-private-method-intersect-shape)(shape_rid: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d), motion: [Vector2](class_vector2.md#class-vector2), margin: [float](class_float.md#class-float), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), r_result: `PhysicsServer2DExtensionShapeResult*`, max_results: [int](class_int.md#class-int)) virtual required |
| [bool](class_bool.md#class-bool) | [_rest_info](class_physicsdirectspacestate2dextension.md#class-physicsdirectspacestate2dextension-private-method-rest-info)(shape_rid: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d), motion: [Vector2](class_vector2.md#class-vector2), margin: [float](class_float.md#class-float), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), r_rest_info: `PhysicsServer2DExtensionShapeRestInfo*`) virtual required |
| [bool](class_bool.md#class-bool) | [is_body_excluded_from_query](class_physicsdirectspacestate2dextension.md#class-physicsdirectspacestate2dextension-method-is-body-excluded-from-query)(body: [RID](class_rid.md#class-rid)) const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-physicsdirectspacestate2dextension-private-method-cast-motion"></a>

[bool](class_bool.md#class-bool) **_cast_motion**(shape_rid: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d), motion: [Vector2](class_vector2.md#class-vector2), margin: [float](class_float.md#class-float), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), r_closest_safe: `float*`, r_closest_unsafe: `float*`) virtual required [🔗](class_physicsdirectspacestate2dextension.md#class-physicsdirectspacestate2dextension-private-method-cast-motion)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectspacestate2dextension-private-method-collide-shape"></a>

[bool](class_bool.md#class-bool) **_collide_shape**(shape_rid: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d), motion: [Vector2](class_vector2.md#class-vector2), margin: [float](class_float.md#class-float), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), r_results: `void*`, max_results: [int](class_int.md#class-int), r_result_count: `int32_t*`) virtual required [🔗](class_physicsdirectspacestate2dextension.md#class-physicsdirectspacestate2dextension-private-method-collide-shape)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectspacestate2dextension-private-method-intersect-point"></a>

[int](class_int.md#class-int) **_intersect_point**(position: [Vector2](class_vector2.md#class-vector2), canvas_instance_id: [int](class_int.md#class-int), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), r_results: `PhysicsServer2DExtensionShapeResult*`, max_results: [int](class_int.md#class-int)) virtual required [🔗](class_physicsdirectspacestate2dextension.md#class-physicsdirectspacestate2dextension-private-method-intersect-point)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectspacestate2dextension-private-method-intersect-ray"></a>

[bool](class_bool.md#class-bool) **_intersect_ray**(from: [Vector2](class_vector2.md#class-vector2), to: [Vector2](class_vector2.md#class-vector2), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), hit_from_inside: [bool](class_bool.md#class-bool), r_result: `PhysicsServer2DExtensionRayResult*`) virtual required [🔗](class_physicsdirectspacestate2dextension.md#class-physicsdirectspacestate2dextension-private-method-intersect-ray)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectspacestate2dextension-private-method-intersect-shape"></a>

[int](class_int.md#class-int) **_intersect_shape**(shape_rid: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d), motion: [Vector2](class_vector2.md#class-vector2), margin: [float](class_float.md#class-float), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), r_result: `PhysicsServer2DExtensionShapeResult*`, max_results: [int](class_int.md#class-int)) virtual required [🔗](class_physicsdirectspacestate2dextension.md#class-physicsdirectspacestate2dextension-private-method-intersect-shape)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectspacestate2dextension-private-method-rest-info"></a>

[bool](class_bool.md#class-bool) **_rest_info**(shape_rid: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d), motion: [Vector2](class_vector2.md#class-vector2), margin: [float](class_float.md#class-float), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), r_rest_info: `PhysicsServer2DExtensionShapeRestInfo*`) virtual required [🔗](class_physicsdirectspacestate2dextension.md#class-physicsdirectspacestate2dextension-private-method-rest-info)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-physicsdirectspacestate2dextension-method-is-body-excluded-from-query"></a>

[bool](class_bool.md#class-bool) **is_body_excluded_from_query**(body: [RID](class_rid.md#class-rid)) const [🔗](class_physicsdirectspacestate2dextension.md#class-physicsdirectspacestate2dextension-method-is-body-excluded-from-query)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!
