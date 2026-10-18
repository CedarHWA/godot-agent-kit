> Source: https://docs.godotengine.org/en/4.7/classes/class_physicsrayqueryparameters3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="physicsrayqueryparameters3d"></a>

<a id="class-physicsrayqueryparameters3d"></a>

# PhysicsRayQueryParameters3D

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Provides parameters for [PhysicsDirectSpaceState3D.intersect_ray()](class_physicsdirectspacestate3d.md#class-physicsdirectspacestate3d-method-intersect-ray).

<a id="description"></a>

## Description

By changing various properties of this object, such as the ray position, you can configure the parameters for [PhysicsDirectSpaceState3D.intersect_ray()](class_physicsdirectspacestate3d.md#class-physicsdirectspacestate3d-method-intersect-ray).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [collide_with_areas](class_physicsrayqueryparameters3d.md#class-physicsrayqueryparameters3d-property-collide-with-areas) | `false` |
| [bool](class_bool.md#class-bool) | [collide_with_bodies](class_physicsrayqueryparameters3d.md#class-physicsrayqueryparameters3d-property-collide-with-bodies) | `true` |
| [int](class_int.md#class-int) | [collision_mask](class_physicsrayqueryparameters3d.md#class-physicsrayqueryparameters3d-property-collision-mask) | `4294967295` |
| [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] | [exclude](class_physicsrayqueryparameters3d.md#class-physicsrayqueryparameters3d-property-exclude) | `[]` |
| [Vector3](class_vector3.md#class-vector3) | [from](class_physicsrayqueryparameters3d.md#class-physicsrayqueryparameters3d-property-from) | `Vector3(0, 0, 0)` |
| [bool](class_bool.md#class-bool) | [hit_back_faces](class_physicsrayqueryparameters3d.md#class-physicsrayqueryparameters3d-property-hit-back-faces) | `true` |
| [bool](class_bool.md#class-bool) | [hit_from_inside](class_physicsrayqueryparameters3d.md#class-physicsrayqueryparameters3d-property-hit-from-inside) | `false` |
| [Vector3](class_vector3.md#class-vector3) | [to](class_physicsrayqueryparameters3d.md#class-physicsrayqueryparameters3d-property-to) | `Vector3(0, 0, 0)` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [PhysicsRayQueryParameters3D](class_physicsrayqueryparameters3d.md#class-physicsrayqueryparameters3d) | [create](class_physicsrayqueryparameters3d.md#class-physicsrayqueryparameters3d-method-create)(from: [Vector3](class_vector3.md#class-vector3), to: [Vector3](class_vector3.md#class-vector3), collision_mask: [int](class_int.md#class-int) = 4294967295, exclude: [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] = []) static |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-physicsrayqueryparameters3d-property-collide-with-areas"></a>

[bool](class_bool.md#class-bool) **collide_with_areas** = `false` [🔗](class_physicsrayqueryparameters3d.md#class-physicsrayqueryparameters3d-property-collide-with-areas)

- void **set_collide_with_areas**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_collide_with_areas_enabled**()

If `true`, the query will take [Area3D](class_area3d.md#class-area3d)s into account.

---


<a id="class-physicsrayqueryparameters3d-property-collide-with-bodies"></a>

[bool](class_bool.md#class-bool) **collide_with_bodies** = `true` [🔗](class_physicsrayqueryparameters3d.md#class-physicsrayqueryparameters3d-property-collide-with-bodies)

- void **set_collide_with_bodies**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_collide_with_bodies_enabled**()

If `true`, the query will take [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d)s into account.

---


<a id="class-physicsrayqueryparameters3d-property-collision-mask"></a>

[int](class_int.md#class-int) **collision_mask** = `4294967295` [🔗](class_physicsrayqueryparameters3d.md#class-physicsrayqueryparameters3d-property-collision-mask)

- void **set_collision_mask**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_collision_mask**()

The physics layers the query will detect (as a bitmask). By default, all collision layers are detected. See [Collision layers and masks](../tutorials/physics/physics_introduction.md#collision-layers-and-masks) in the documentation for more information.

---


<a id="class-physicsrayqueryparameters3d-property-exclude"></a>

[Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] **exclude** = `[]` [🔗](class_physicsrayqueryparameters3d.md#class-physicsrayqueryparameters3d-property-exclude)

- void **set_exclude**(value: [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)])
- [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] **get_exclude**()

The list of object [RID](class_rid.md#class-rid)s that will be excluded from collisions. Use [CollisionObject3D.get_rid()](class_collisionobject3d.md#class-collisionobject3d-method-get-rid) to get the [RID](class_rid.md#class-rid) associated with a [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d)-derived node.

**Note:** The returned array is copied and any changes to it will not update the original property value. To update the value you need to modify the returned array, and then assign it to the property again.

---


<a id="class-physicsrayqueryparameters3d-property-from"></a>

[Vector3](class_vector3.md#class-vector3) **from** = `Vector3(0, 0, 0)` [🔗](class_physicsrayqueryparameters3d.md#class-physicsrayqueryparameters3d-property-from)

- void **set_from**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_from**()

The starting point of the ray being queried for, in global coordinates.

---


<a id="class-physicsrayqueryparameters3d-property-hit-back-faces"></a>

[bool](class_bool.md#class-bool) **hit_back_faces** = `true` [🔗](class_physicsrayqueryparameters3d.md#class-physicsrayqueryparameters3d-property-hit-back-faces)

- void **set_hit_back_faces**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_hit_back_faces_enabled**()

If `true`, the query will hit back faces with concave polygon shapes with back face enabled or heightmap shapes.

---


<a id="class-physicsrayqueryparameters3d-property-hit-from-inside"></a>

[bool](class_bool.md#class-bool) **hit_from_inside** = `false` [🔗](class_physicsrayqueryparameters3d.md#class-physicsrayqueryparameters3d-property-hit-from-inside)

- void **set_hit_from_inside**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_hit_from_inside_enabled**()

If `true`, the query will detect a hit when starting inside shapes. In this case the collision normal will be `Vector3(0, 0, 0)`. Does not affect concave polygon shapes or heightmap shapes.

---


<a id="class-physicsrayqueryparameters3d-property-to"></a>

[Vector3](class_vector3.md#class-vector3) **to** = `Vector3(0, 0, 0)` [🔗](class_physicsrayqueryparameters3d.md#class-physicsrayqueryparameters3d-property-to)

- void **set_to**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_to**()

The ending point of the ray being queried for, in global coordinates.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-physicsrayqueryparameters3d-method-create"></a>

[PhysicsRayQueryParameters3D](class_physicsrayqueryparameters3d.md#class-physicsrayqueryparameters3d) **create**(from: [Vector3](class_vector3.md#class-vector3), to: [Vector3](class_vector3.md#class-vector3), collision_mask: [int](class_int.md#class-int) = 4294967295, exclude: [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] = []) static [🔗](class_physicsrayqueryparameters3d.md#class-physicsrayqueryparameters3d-method-create)

Returns a new, pre-configured **PhysicsRayQueryParameters3D** object. Use it to quickly create query parameters using the most common options.

```gdscript
var query = PhysicsRayQueryParameters3D.create(position, position + Vector3(0, -10, 0))
var collision = get_world_3d().direct_space_state.intersect_ray(query)
```
