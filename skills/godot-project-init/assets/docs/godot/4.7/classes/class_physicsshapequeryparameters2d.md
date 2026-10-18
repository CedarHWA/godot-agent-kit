> Source: https://docs.godotengine.org/en/4.7/classes/class_physicsshapequeryparameters2d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="physicsshapequeryparameters2d"></a>

<a id="class-physicsshapequeryparameters2d"></a>

# PhysicsShapeQueryParameters2D

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Provides parameters for [PhysicsDirectSpaceState2D](class_physicsdirectspacestate2d.md#class-physicsdirectspacestate2d)'s methods.

<a id="description"></a>

## Description

By changing various properties of this object, such as the shape, you can configure the parameters for [PhysicsDirectSpaceState2D](class_physicsdirectspacestate2d.md#class-physicsdirectspacestate2d)'s methods.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [collide_with_areas](class_physicsshapequeryparameters2d.md#class-physicsshapequeryparameters2d-property-collide-with-areas) | `false` |
| [bool](class_bool.md#class-bool) | [collide_with_bodies](class_physicsshapequeryparameters2d.md#class-physicsshapequeryparameters2d-property-collide-with-bodies) | `true` |
| [int](class_int.md#class-int) | [collision_mask](class_physicsshapequeryparameters2d.md#class-physicsshapequeryparameters2d-property-collision-mask) | `4294967295` |
| [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] | [exclude](class_physicsshapequeryparameters2d.md#class-physicsshapequeryparameters2d-property-exclude) | `[]` |
| [float](class_float.md#class-float) | [margin](class_physicsshapequeryparameters2d.md#class-physicsshapequeryparameters2d-property-margin) | `0.0` |
| [Vector2](class_vector2.md#class-vector2) | [motion](class_physicsshapequeryparameters2d.md#class-physicsshapequeryparameters2d-property-motion) | `Vector2(0, 0)` |
| [Resource](class_resource.md#class-resource) | [shape](class_physicsshapequeryparameters2d.md#class-physicsshapequeryparameters2d-property-shape) |  |
| [RID](class_rid.md#class-rid) | [shape_rid](class_physicsshapequeryparameters2d.md#class-physicsshapequeryparameters2d-property-shape-rid) | `RID()` |
| [Transform2D](class_transform2d.md#class-transform2d) | [transform](class_physicsshapequeryparameters2d.md#class-physicsshapequeryparameters2d-property-transform) | `Transform2D(1, 0, 0, 1, 0, 0)` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-physicsshapequeryparameters2d-property-collide-with-areas"></a>

[bool](class_bool.md#class-bool) **collide_with_areas** = `false` [🔗](class_physicsshapequeryparameters2d.md#class-physicsshapequeryparameters2d-property-collide-with-areas)

- void **set_collide_with_areas**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_collide_with_areas_enabled**()

If `true`, the query will take [Area2D](class_area2d.md#class-area2d)s into account.

---


<a id="class-physicsshapequeryparameters2d-property-collide-with-bodies"></a>

[bool](class_bool.md#class-bool) **collide_with_bodies** = `true` [🔗](class_physicsshapequeryparameters2d.md#class-physicsshapequeryparameters2d-property-collide-with-bodies)

- void **set_collide_with_bodies**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_collide_with_bodies_enabled**()

If `true`, the query will take [PhysicsBody2D](class_physicsbody2d.md#class-physicsbody2d)s into account.

---


<a id="class-physicsshapequeryparameters2d-property-collision-mask"></a>

[int](class_int.md#class-int) **collision_mask** = `4294967295` [🔗](class_physicsshapequeryparameters2d.md#class-physicsshapequeryparameters2d-property-collision-mask)

- void **set_collision_mask**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_collision_mask**()

The physics layers the query will detect (as a bitmask). By default, all collision layers are detected. See [Collision layers and masks](../tutorials/physics/physics_introduction.md#collision-layers-and-masks) in the documentation for more information.

---


<a id="class-physicsshapequeryparameters2d-property-exclude"></a>

[Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] **exclude** = `[]` [🔗](class_physicsshapequeryparameters2d.md#class-physicsshapequeryparameters2d-property-exclude)

- void **set_exclude**(value: [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)])
- [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] **get_exclude**()

The list of object [RID](class_rid.md#class-rid)s that will be excluded from collisions. Use [CollisionObject2D.get_rid()](class_collisionobject2d.md#class-collisionobject2d-method-get-rid) to get the [RID](class_rid.md#class-rid) associated with a [CollisionObject2D](class_collisionobject2d.md#class-collisionobject2d)-derived node.

**Note:** The returned array is copied and any changes to it will not update the original property value. To update the value you need to modify the returned array, and then assign it to the property again.

---


<a id="class-physicsshapequeryparameters2d-property-margin"></a>

[float](class_float.md#class-float) **margin** = `0.0` [🔗](class_physicsshapequeryparameters2d.md#class-physicsshapequeryparameters2d-property-margin)

- void **set_margin**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_margin**()

The collision margin for the shape.

---


<a id="class-physicsshapequeryparameters2d-property-motion"></a>

[Vector2](class_vector2.md#class-vector2) **motion** = `Vector2(0, 0)` [🔗](class_physicsshapequeryparameters2d.md#class-physicsshapequeryparameters2d-property-motion)

- void **set_motion**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_motion**()

The motion of the shape being queried for.

---


<a id="class-physicsshapequeryparameters2d-property-shape"></a>

[Resource](class_resource.md#class-resource) **shape** [🔗](class_physicsshapequeryparameters2d.md#class-physicsshapequeryparameters2d-property-shape)

- void **set_shape**(value: [Resource](class_resource.md#class-resource))
- [Resource](class_resource.md#class-resource) **get_shape**()

The [Shape2D](class_shape2d.md#class-shape2d) that will be used for collision/intersection queries. This stores the actual reference which avoids the shape to be released while being used for queries, so always prefer using this over [shape_rid](class_physicsshapequeryparameters2d.md#class-physicsshapequeryparameters2d-property-shape-rid).

---


<a id="class-physicsshapequeryparameters2d-property-shape-rid"></a>

[RID](class_rid.md#class-rid) **shape_rid** = `RID()` [🔗](class_physicsshapequeryparameters2d.md#class-physicsshapequeryparameters2d-property-shape-rid)

- void **set_shape_rid**(value: [RID](class_rid.md#class-rid))
- [RID](class_rid.md#class-rid) **get_shape_rid**()

The queried shape's [RID](class_rid.md#class-rid) that will be used for collision/intersection queries. Use this over [shape](class_physicsshapequeryparameters2d.md#class-physicsshapequeryparameters2d-property-shape) if you want to optimize for performance using the Servers API:

```gdscript
var shape_rid = PhysicsServer2D.circle_shape_create()
var radius = 64
PhysicsServer2D.shape_set_data(shape_rid, radius)

var params = PhysicsShapeQueryParameters2D.new()
params.shape_rid = shape_rid

# Execute physics queries here...

# Release the shape when done with physics queries.
PhysicsServer2D.free_rid(shape_rid)
```

```csharp
RID shapeRid = PhysicsServer2D.CircleShapeCreate();
int radius = 64;
PhysicsServer2D.ShapeSetData(shapeRid, radius);

var params = new PhysicsShapeQueryParameters2D();
params.ShapeRid = shapeRid;

// Execute physics queries here...

// Release the shape when done with physics queries.
PhysicsServer2D.FreeRid(shapeRid);
```

---


<a id="class-physicsshapequeryparameters2d-property-transform"></a>

[Transform2D](class_transform2d.md#class-transform2d) **transform** = `Transform2D(1, 0, 0, 1, 0, 0)` [🔗](class_physicsshapequeryparameters2d.md#class-physicsshapequeryparameters2d-property-transform)

- void **set_transform**(value: [Transform2D](class_transform2d.md#class-transform2d))
- [Transform2D](class_transform2d.md#class-transform2d) **get_transform**()

The queried shape's transform matrix.
