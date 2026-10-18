> Source: https://docs.godotengine.org/en/4.7/classes/class_physicsrayqueryparameters2d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="physicsrayqueryparameters2d"></a>

<a id="class-physicsrayqueryparameters2d"></a>

# PhysicsRayQueryParameters2D

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Provides parameters for [PhysicsDirectSpaceState2D.intersect_ray()](class_physicsdirectspacestate2d.md#class-physicsdirectspacestate2d-method-intersect-ray).

<a id="description"></a>

## Description

By changing various properties of this object, such as the ray position, you can configure the parameters for [PhysicsDirectSpaceState2D.intersect_ray()](class_physicsdirectspacestate2d.md#class-physicsdirectspacestate2d-method-intersect-ray).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [collide_with_areas](class_physicsrayqueryparameters2d.md#class-physicsrayqueryparameters2d-property-collide-with-areas) | `false` |
| [bool](class_bool.md#class-bool) | [collide_with_bodies](class_physicsrayqueryparameters2d.md#class-physicsrayqueryparameters2d-property-collide-with-bodies) | `true` |
| [int](class_int.md#class-int) | [collision_mask](class_physicsrayqueryparameters2d.md#class-physicsrayqueryparameters2d-property-collision-mask) | `4294967295` |
| [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] | [exclude](class_physicsrayqueryparameters2d.md#class-physicsrayqueryparameters2d-property-exclude) | `[]` |
| [Vector2](class_vector2.md#class-vector2) | [from](class_physicsrayqueryparameters2d.md#class-physicsrayqueryparameters2d-property-from) | `Vector2(0, 0)` |
| [bool](class_bool.md#class-bool) | [hit_from_inside](class_physicsrayqueryparameters2d.md#class-physicsrayqueryparameters2d-property-hit-from-inside) | `false` |
| [Vector2](class_vector2.md#class-vector2) | [to](class_physicsrayqueryparameters2d.md#class-physicsrayqueryparameters2d-property-to) | `Vector2(0, 0)` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [PhysicsRayQueryParameters2D](class_physicsrayqueryparameters2d.md#class-physicsrayqueryparameters2d) | [create](class_physicsrayqueryparameters2d.md#class-physicsrayqueryparameters2d-method-create)(from: [Vector2](class_vector2.md#class-vector2), to: [Vector2](class_vector2.md#class-vector2), collision_mask: [int](class_int.md#class-int) = 4294967295, exclude: [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] = []) static |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-physicsrayqueryparameters2d-property-collide-with-areas"></a>

[bool](class_bool.md#class-bool) **collide_with_areas** = `false` [🔗](class_physicsrayqueryparameters2d.md#class-physicsrayqueryparameters2d-property-collide-with-areas)

- void **set_collide_with_areas**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_collide_with_areas_enabled**()

If `true`, the query will take [Area2D](class_area2d.md#class-area2d)s into account.

---


<a id="class-physicsrayqueryparameters2d-property-collide-with-bodies"></a>

[bool](class_bool.md#class-bool) **collide_with_bodies** = `true` [🔗](class_physicsrayqueryparameters2d.md#class-physicsrayqueryparameters2d-property-collide-with-bodies)

- void **set_collide_with_bodies**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_collide_with_bodies_enabled**()

If `true`, the query will take [PhysicsBody2D](class_physicsbody2d.md#class-physicsbody2d)s into account.

---


<a id="class-physicsrayqueryparameters2d-property-collision-mask"></a>

[int](class_int.md#class-int) **collision_mask** = `4294967295` [🔗](class_physicsrayqueryparameters2d.md#class-physicsrayqueryparameters2d-property-collision-mask)

- void **set_collision_mask**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_collision_mask**()

The physics layers the query will detect (as a bitmask). By default, all collision layers are detected. See [Collision layers and masks](../tutorials/physics/physics_introduction.md#collision-layers-and-masks) in the documentation for more information.

---


<a id="class-physicsrayqueryparameters2d-property-exclude"></a>

[Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] **exclude** = `[]` [🔗](class_physicsrayqueryparameters2d.md#class-physicsrayqueryparameters2d-property-exclude)

- void **set_exclude**(value: [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)])
- [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] **get_exclude**()

The list of object [RID](class_rid.md#class-rid)s that will be excluded from collisions. Use [CollisionObject2D.get_rid()](class_collisionobject2d.md#class-collisionobject2d-method-get-rid) to get the [RID](class_rid.md#class-rid) associated with a [CollisionObject2D](class_collisionobject2d.md#class-collisionobject2d)-derived node.

**Note:** The returned array is copied and any changes to it will not update the original property value. To update the value you need to modify the returned array, and then assign it to the property again.

---


<a id="class-physicsrayqueryparameters2d-property-from"></a>

[Vector2](class_vector2.md#class-vector2) **from** = `Vector2(0, 0)` [🔗](class_physicsrayqueryparameters2d.md#class-physicsrayqueryparameters2d-property-from)

- void **set_from**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_from**()

The starting point of the ray being queried for, in global coordinates.

---


<a id="class-physicsrayqueryparameters2d-property-hit-from-inside"></a>

[bool](class_bool.md#class-bool) **hit_from_inside** = `false` [🔗](class_physicsrayqueryparameters2d.md#class-physicsrayqueryparameters2d-property-hit-from-inside)

- void **set_hit_from_inside**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_hit_from_inside_enabled**()

If `true`, the query will detect a hit when starting inside shapes. In this case the collision normal will be `Vector2(0, 0)`. Does not affect concave polygon shapes.

---


<a id="class-physicsrayqueryparameters2d-property-to"></a>

[Vector2](class_vector2.md#class-vector2) **to** = `Vector2(0, 0)` [🔗](class_physicsrayqueryparameters2d.md#class-physicsrayqueryparameters2d-property-to)

- void **set_to**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_to**()

The ending point of the ray being queried for, in global coordinates.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-physicsrayqueryparameters2d-method-create"></a>

[PhysicsRayQueryParameters2D](class_physicsrayqueryparameters2d.md#class-physicsrayqueryparameters2d) **create**(from: [Vector2](class_vector2.md#class-vector2), to: [Vector2](class_vector2.md#class-vector2), collision_mask: [int](class_int.md#class-int) = 4294967295, exclude: [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] = []) static [🔗](class_physicsrayqueryparameters2d.md#class-physicsrayqueryparameters2d-method-create)

Returns a new, pre-configured **PhysicsRayQueryParameters2D** object. Use it to quickly create query parameters using the most common options.

```gdscript
var query = PhysicsRayQueryParameters2D.create(global_position, global_position + Vector2(0, 100))
var collision = get_world_2d().direct_space_state.intersect_ray(query)
```
