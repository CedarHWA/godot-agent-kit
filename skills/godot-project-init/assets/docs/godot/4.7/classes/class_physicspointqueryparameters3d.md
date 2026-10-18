> Source: https://docs.godotengine.org/en/4.7/classes/class_physicspointqueryparameters3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="physicspointqueryparameters3d"></a>

<a id="class-physicspointqueryparameters3d"></a>

# PhysicsPointQueryParameters3D

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Provides parameters for [PhysicsDirectSpaceState3D.intersect_point()](class_physicsdirectspacestate3d.md#class-physicsdirectspacestate3d-method-intersect-point).

<a id="description"></a>

## Description

By changing various properties of this object, such as the point position, you can configure the parameters for [PhysicsDirectSpaceState3D.intersect_point()](class_physicsdirectspacestate3d.md#class-physicsdirectspacestate3d-method-intersect-point).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [collide_with_areas](class_physicspointqueryparameters3d.md#class-physicspointqueryparameters3d-property-collide-with-areas) | `false` |
| [bool](class_bool.md#class-bool) | [collide_with_bodies](class_physicspointqueryparameters3d.md#class-physicspointqueryparameters3d-property-collide-with-bodies) | `true` |
| [int](class_int.md#class-int) | [collision_mask](class_physicspointqueryparameters3d.md#class-physicspointqueryparameters3d-property-collision-mask) | `4294967295` |
| [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] | [exclude](class_physicspointqueryparameters3d.md#class-physicspointqueryparameters3d-property-exclude) | `[]` |
| [Vector3](class_vector3.md#class-vector3) | [position](class_physicspointqueryparameters3d.md#class-physicspointqueryparameters3d-property-position) | `Vector3(0, 0, 0)` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-physicspointqueryparameters3d-property-collide-with-areas"></a>

[bool](class_bool.md#class-bool) **collide_with_areas** = `false` [🔗](class_physicspointqueryparameters3d.md#class-physicspointqueryparameters3d-property-collide-with-areas)

- void **set_collide_with_areas**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_collide_with_areas_enabled**()

If `true`, the query will take [Area3D](class_area3d.md#class-area3d)s into account.

---


<a id="class-physicspointqueryparameters3d-property-collide-with-bodies"></a>

[bool](class_bool.md#class-bool) **collide_with_bodies** = `true` [🔗](class_physicspointqueryparameters3d.md#class-physicspointqueryparameters3d-property-collide-with-bodies)

- void **set_collide_with_bodies**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_collide_with_bodies_enabled**()

If `true`, the query will take [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d)s into account.

---


<a id="class-physicspointqueryparameters3d-property-collision-mask"></a>

[int](class_int.md#class-int) **collision_mask** = `4294967295` [🔗](class_physicspointqueryparameters3d.md#class-physicspointqueryparameters3d-property-collision-mask)

- void **set_collision_mask**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_collision_mask**()

The physics layers the query will detect (as a bitmask). By default, all collision layers are detected. See [Collision layers and masks](../tutorials/physics/physics_introduction.md#collision-layers-and-masks) in the documentation for more information.

---


<a id="class-physicspointqueryparameters3d-property-exclude"></a>

[Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] **exclude** = `[]` [🔗](class_physicspointqueryparameters3d.md#class-physicspointqueryparameters3d-property-exclude)

- void **set_exclude**(value: [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)])
- [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] **get_exclude**()

The list of object [RID](class_rid.md#class-rid)s that will be excluded from collisions. Use [CollisionObject3D.get_rid()](class_collisionobject3d.md#class-collisionobject3d-method-get-rid) to get the [RID](class_rid.md#class-rid) associated with a [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d)-derived node.

**Note:** The returned array is copied and any changes to it will not update the original property value. To update the value you need to modify the returned array, and then assign it to the property again.

---


<a id="class-physicspointqueryparameters3d-property-position"></a>

[Vector3](class_vector3.md#class-vector3) **position** = `Vector3(0, 0, 0)` [🔗](class_physicspointqueryparameters3d.md#class-physicspointqueryparameters3d-property-position)

- void **set_position**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_position**()

The position being queried for, in global coordinates.
