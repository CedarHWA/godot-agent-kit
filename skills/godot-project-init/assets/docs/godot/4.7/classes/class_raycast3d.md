> Source: https://docs.godotengine.org/en/4.7/classes/class_raycast3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="raycast3d"></a>

<a id="class-raycast3d"></a>

# RayCast3D

**Inherits:** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A ray in 3D space, used to find the first collision object it intersects.

<a id="description"></a>

## Description

A raycast represents a ray from its origin to its [target_position](class_raycast3d.md#class-raycast3d-property-target-position) that finds the closest object along its path, if it intersects any.

**RayCast3D** can ignore some objects by adding them to an exception list, by making its detection reporting ignore [Area3D](class_area3d.md#class-area3d)s ([collide_with_areas](class_raycast3d.md#class-raycast3d-property-collide-with-areas)) or [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d)s ([collide_with_bodies](class_raycast3d.md#class-raycast3d-property-collide-with-bodies)), or by configuring physics layers.

**RayCast3D** calculates intersection every physics frame, and it holds the result until the next physics frame. For an immediate raycast, or if you want to configure a **RayCast3D** multiple times within the same physics frame, use [force_raycast_update()](class_raycast3d.md#class-raycast3d-method-force-raycast-update).

To sweep over a region of 3D space, you can approximate the region with multiple **RayCast3D**s or use [ShapeCast3D](class_shapecast3d.md#class-shapecast3d).

<a id="tutorials"></a>

## Tutorials

- [Ray-casting](../tutorials/physics/ray-casting.md)
- [3D Voxel Demo](https://godotengine.org/asset-library/asset/2755)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [collide_with_areas](class_raycast3d.md#class-raycast3d-property-collide-with-areas) | `false` |
| [bool](class_bool.md#class-bool) | [collide_with_bodies](class_raycast3d.md#class-raycast3d-property-collide-with-bodies) | `true` |
| [int](class_int.md#class-int) | [collision_mask](class_raycast3d.md#class-raycast3d-property-collision-mask) | `1` |
| [Color](class_color.md#class-color) | [debug_shape_custom_color](class_raycast3d.md#class-raycast3d-property-debug-shape-custom-color) | `Color(0, 0, 0, 1)` |
| [int](class_int.md#class-int) | [debug_shape_thickness](class_raycast3d.md#class-raycast3d-property-debug-shape-thickness) | `2` |
| [bool](class_bool.md#class-bool) | [enabled](class_raycast3d.md#class-raycast3d-property-enabled) | `true` |
| [bool](class_bool.md#class-bool) | [exclude_parent](class_raycast3d.md#class-raycast3d-property-exclude-parent) | `true` |
| [bool](class_bool.md#class-bool) | [hit_back_faces](class_raycast3d.md#class-raycast3d-property-hit-back-faces) | `true` |
| [bool](class_bool.md#class-bool) | [hit_from_inside](class_raycast3d.md#class-raycast3d-property-hit-from-inside) | `false` |
| [Vector3](class_vector3.md#class-vector3) | [target_position](class_raycast3d.md#class-raycast3d-property-target-position) | `Vector3(0, -1, 0)` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_exception](class_raycast3d.md#class-raycast3d-method-add-exception)(node: [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d)) |
| void | [add_exception_rid](class_raycast3d.md#class-raycast3d-method-add-exception-rid)(rid: [RID](class_rid.md#class-rid)) |
| void | [clear_exceptions](class_raycast3d.md#class-raycast3d-method-clear-exceptions)() |
| void | [force_raycast_update](class_raycast3d.md#class-raycast3d-method-force-raycast-update)() |
| [Object](class_object.md#class-object) | [get_collider](class_raycast3d.md#class-raycast3d-method-get-collider)() const |
| [RID](class_rid.md#class-rid) | [get_collider_rid](class_raycast3d.md#class-raycast3d-method-get-collider-rid)() const |
| [int](class_int.md#class-int) | [get_collider_shape](class_raycast3d.md#class-raycast3d-method-get-collider-shape)() const |
| [int](class_int.md#class-int) | [get_collision_face_index](class_raycast3d.md#class-raycast3d-method-get-collision-face-index)() const |
| [bool](class_bool.md#class-bool) | [get_collision_mask_value](class_raycast3d.md#class-raycast3d-method-get-collision-mask-value)(layer_number: [int](class_int.md#class-int)) const |
| [Vector3](class_vector3.md#class-vector3) | [get_collision_normal](class_raycast3d.md#class-raycast3d-method-get-collision-normal)() const |
| [Vector3](class_vector3.md#class-vector3) | [get_collision_point](class_raycast3d.md#class-raycast3d-method-get-collision-point)() const |
| [bool](class_bool.md#class-bool) | [is_colliding](class_raycast3d.md#class-raycast3d-method-is-colliding)() const |
| void | [remove_exception](class_raycast3d.md#class-raycast3d-method-remove-exception)(node: [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d)) |
| void | [remove_exception_rid](class_raycast3d.md#class-raycast3d-method-remove-exception-rid)(rid: [RID](class_rid.md#class-rid)) |
| void | [set_collision_mask_value](class_raycast3d.md#class-raycast3d-method-set-collision-mask-value)(layer_number: [int](class_int.md#class-int), value: [bool](class_bool.md#class-bool)) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-raycast3d-property-collide-with-areas"></a>

[bool](class_bool.md#class-bool) **collide_with_areas** = `false` [🔗](class_raycast3d.md#class-raycast3d-property-collide-with-areas)

- void **set_collide_with_areas**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_collide_with_areas_enabled**()

If `true`, collisions with [Area3D](class_area3d.md#class-area3d)s will be reported.

---


<a id="class-raycast3d-property-collide-with-bodies"></a>

[bool](class_bool.md#class-bool) **collide_with_bodies** = `true` [🔗](class_raycast3d.md#class-raycast3d-property-collide-with-bodies)

- void **set_collide_with_bodies**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_collide_with_bodies_enabled**()

If `true`, collisions with [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d)s will be reported.

---


<a id="class-raycast3d-property-collision-mask"></a>

[int](class_int.md#class-int) **collision_mask** = `1` [🔗](class_raycast3d.md#class-raycast3d-property-collision-mask)

- void **set_collision_mask**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_collision_mask**()

The ray's collision mask. Only objects in at least one collision layer enabled in the mask will be detected. See [Collision layers and masks](../tutorials/physics/physics_introduction.md#collision-layers-and-masks) in the documentation for more information.

---


<a id="class-raycast3d-property-debug-shape-custom-color"></a>

[Color](class_color.md#class-color) **debug_shape_custom_color** = `Color(0, 0, 0, 1)` [🔗](class_raycast3d.md#class-raycast3d-property-debug-shape-custom-color)

- void **set_debug_shape_custom_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_debug_shape_custom_color**()

The custom color to use to draw the shape in the editor and at run-time if **Visible Collision Shapes** is enabled in the **Debug** menu. This color will be highlighted at run-time if the **RayCast3D** is colliding with something.

If set to `Color(0.0, 0.0, 0.0)` (by default), the color set in [ProjectSettings.debug/shapes/collision/shape_color](class_projectsettings.md#class-projectsettings-property-debug-shapes-collision-shape-color) is used.

---


<a id="class-raycast3d-property-debug-shape-thickness"></a>

[int](class_int.md#class-int) **debug_shape_thickness** = `2` [🔗](class_raycast3d.md#class-raycast3d-property-debug-shape-thickness)

- void **set_debug_shape_thickness**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_debug_shape_thickness**()

If set to `1`, a line is used as the debug shape. Otherwise, a truncated pyramid is drawn to represent the **RayCast3D**. Requires **Visible Collision Shapes** to be enabled in the **Debug** menu for the debug shape to be visible at run-time.

---


<a id="class-raycast3d-property-enabled"></a>

[bool](class_bool.md#class-bool) **enabled** = `true` [🔗](class_raycast3d.md#class-raycast3d-property-enabled)

- void **set_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_enabled**()

If `true`, collisions will be reported.

---


<a id="class-raycast3d-property-exclude-parent"></a>

[bool](class_bool.md#class-bool) **exclude_parent** = `true` [🔗](class_raycast3d.md#class-raycast3d-property-exclude-parent)

- void **set_exclude_parent_body**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_exclude_parent_body**()

If `true`, this raycast will not report collisions with its parent node. This property only has an effect if the parent node is a [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d). See also [Node.get_parent()](class_node.md#class-node-method-get-parent) and [add_exception()](class_raycast3d.md#class-raycast3d-method-add-exception).

---


<a id="class-raycast3d-property-hit-back-faces"></a>

[bool](class_bool.md#class-bool) **hit_back_faces** = `true` [🔗](class_raycast3d.md#class-raycast3d-property-hit-back-faces)

- void **set_hit_back_faces**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_hit_back_faces_enabled**()

If `true`, the ray will hit back faces with concave polygon shapes with back face enabled or heightmap shapes.

---


<a id="class-raycast3d-property-hit-from-inside"></a>

[bool](class_bool.md#class-bool) **hit_from_inside** = `false` [🔗](class_raycast3d.md#class-raycast3d-property-hit-from-inside)

- void **set_hit_from_inside**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_hit_from_inside_enabled**()

If `true`, the ray will detect a hit when starting inside shapes. In this case the collision normal will be `Vector3(0, 0, 0)`. Does not affect shapes with no volume like concave polygon or heightmap.

---


<a id="class-raycast3d-property-target-position"></a>

[Vector3](class_vector3.md#class-vector3) **target_position** = `Vector3(0, -1, 0)` [🔗](class_raycast3d.md#class-raycast3d-property-target-position)

- void **set_target_position**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_target_position**()

The ray's destination point, relative to this raycast's [Node3D.position](class_node3d.md#class-node3d-property-position).

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-raycast3d-method-add-exception"></a>

void **add_exception**(node: [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d)) [🔗](class_raycast3d.md#class-raycast3d-method-add-exception)

Adds a collision exception so the ray does not report collisions with the specified `node`.

---


<a id="class-raycast3d-method-add-exception-rid"></a>

void **add_exception_rid**(rid: [RID](class_rid.md#class-rid)) [🔗](class_raycast3d.md#class-raycast3d-method-add-exception-rid)

Adds a collision exception so the ray does not report collisions with the specified [RID](class_rid.md#class-rid).

---


<a id="class-raycast3d-method-clear-exceptions"></a>

void **clear_exceptions**() [🔗](class_raycast3d.md#class-raycast3d-method-clear-exceptions)

Removes all collision exceptions for this ray.

---


<a id="class-raycast3d-method-force-raycast-update"></a>

void **force_raycast_update**() [🔗](class_raycast3d.md#class-raycast3d-method-force-raycast-update)

Updates the collision information for the ray immediately, without waiting for the next `_physics_process` call. Use this method, for example, when the ray or its parent has changed state.

**Note:** [enabled](class_raycast3d.md#class-raycast3d-property-enabled) does not need to be `true` for this to work.

---


<a id="class-raycast3d-method-get-collider"></a>

[Object](class_object.md#class-object) **get_collider**() const [🔗](class_raycast3d.md#class-raycast3d-method-get-collider)

Returns the first object that the ray intersects, or `null` if no object is intersecting the ray (i.e. [is_colliding()](class_raycast3d.md#class-raycast3d-method-is-colliding) returns `false`).

**Note:** This object is not guaranteed to be a [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d). For example, if the ray intersects a [CSGShape3D](class_csgshape3d.md#class-csgshape3d) or a [GridMap](class_gridmap.md#class-gridmap), the method will return a [CSGShape3D](class_csgshape3d.md#class-csgshape3d) or [GridMap](class_gridmap.md#class-gridmap) instance.

---


<a id="class-raycast3d-method-get-collider-rid"></a>

[RID](class_rid.md#class-rid) **get_collider_rid**() const [🔗](class_raycast3d.md#class-raycast3d-method-get-collider-rid)

Returns the [RID](class_rid.md#class-rid) of the first object that the ray intersects, or an empty [RID](class_rid.md#class-rid) if no object is intersecting the ray (i.e. [is_colliding()](class_raycast3d.md#class-raycast3d-method-is-colliding) returns `false`).

---


<a id="class-raycast3d-method-get-collider-shape"></a>

[int](class_int.md#class-int) **get_collider_shape**() const [🔗](class_raycast3d.md#class-raycast3d-method-get-collider-shape)

Returns the shape ID of the first object that the ray intersects, or `0` if no object is intersecting the ray (i.e. [is_colliding()](class_raycast3d.md#class-raycast3d-method-is-colliding) returns `false`).

To get the intersected shape node, for a [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d) target, use:

```gdscript
var target = get_collider() # A CollisionObject3D.
var shape_id = get_collider_shape() # The shape index in the collider.
var owner_id = target.shape_find_owner(shape_id) # The owner ID in the collider.
var shape = target.shape_owner_get_owner(owner_id)
```

```csharp
var target = (CollisionObject3D)GetCollider(); // A CollisionObject3D.
var shapeId = GetColliderShape(); // The shape index in the collider.
var ownerId = target.ShapeFindOwner(shapeId); // The owner ID in the collider.
var shape = target.ShapeOwnerGetOwner(ownerId);
```

---


<a id="class-raycast3d-method-get-collision-face-index"></a>

[int](class_int.md#class-int) **get_collision_face_index**() const [🔗](class_raycast3d.md#class-raycast3d-method-get-collision-face-index)

Returns the collision object's face index at the collision point, or `-1` if the shape intersecting the ray is not a [ConcavePolygonShape3D](class_concavepolygonshape3d.md#class-concavepolygonshape3d).

---


<a id="class-raycast3d-method-get-collision-mask-value"></a>

[bool](class_bool.md#class-bool) **get_collision_mask_value**(layer_number: [int](class_int.md#class-int)) const [🔗](class_raycast3d.md#class-raycast3d-method-get-collision-mask-value)

Returns whether or not the specified layer of the [collision_mask](class_raycast3d.md#class-raycast3d-property-collision-mask) is enabled, given a `layer_number` between 1 and 32.

---


<a id="class-raycast3d-method-get-collision-normal"></a>

[Vector3](class_vector3.md#class-vector3) **get_collision_normal**() const [🔗](class_raycast3d.md#class-raycast3d-method-get-collision-normal)

Returns the normal of the intersecting object's shape at the collision point, or `Vector3(0, 0, 0)` if the ray starts inside the shape and [hit_from_inside](class_raycast3d.md#class-raycast3d-property-hit-from-inside) is `true`.

**Note:** Check that [is_colliding()](class_raycast3d.md#class-raycast3d-method-is-colliding) returns `true` before calling this method to ensure the returned normal is valid and up-to-date.

---


<a id="class-raycast3d-method-get-collision-point"></a>

[Vector3](class_vector3.md#class-vector3) **get_collision_point**() const [🔗](class_raycast3d.md#class-raycast3d-method-get-collision-point)

Returns the collision point at which the ray intersects the closest object, in the global coordinate system. If [hit_from_inside](class_raycast3d.md#class-raycast3d-property-hit-from-inside) is `true` and the ray starts inside of a collision shape, this function will return the origin point of the ray.

**Note:** Check that [is_colliding()](class_raycast3d.md#class-raycast3d-method-is-colliding) returns `true` before calling this method to ensure the returned point is valid and up-to-date.

---


<a id="class-raycast3d-method-is-colliding"></a>

[bool](class_bool.md#class-bool) **is_colliding**() const [🔗](class_raycast3d.md#class-raycast3d-method-is-colliding)

Returns whether any object is intersecting with the ray's vector (considering the vector length).

---


<a id="class-raycast3d-method-remove-exception"></a>

void **remove_exception**(node: [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d)) [🔗](class_raycast3d.md#class-raycast3d-method-remove-exception)

Removes a collision exception so the ray can report collisions with the specified `node`.

---


<a id="class-raycast3d-method-remove-exception-rid"></a>

void **remove_exception_rid**(rid: [RID](class_rid.md#class-rid)) [🔗](class_raycast3d.md#class-raycast3d-method-remove-exception-rid)

Removes a collision exception so the ray can report collisions with the specified [RID](class_rid.md#class-rid).

---


<a id="class-raycast3d-method-set-collision-mask-value"></a>

void **set_collision_mask_value**(layer_number: [int](class_int.md#class-int), value: [bool](class_bool.md#class-bool)) [🔗](class_raycast3d.md#class-raycast3d-method-set-collision-mask-value)

Based on `value`, enables or disables the specified layer in the [collision_mask](class_raycast3d.md#class-raycast3d-property-collision-mask), given a `layer_number` between 1 and 32.
