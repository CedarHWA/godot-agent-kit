> Source: https://docs.godotengine.org/en/4.7/classes/class_softbody3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="softbody3d"></a>

<a id="class-softbody3d"></a>

# SoftBody3D

**Inherits:** [MeshInstance3D](class_meshinstance3d.md#class-meshinstance3d) **<** [GeometryInstance3D](class_geometryinstance3d.md#class-geometryinstance3d) **<** [VisualInstance3D](class_visualinstance3d.md#class-visualinstance3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A deformable 3D physics mesh.

<a id="description"></a>

## Description

A deformable 3D physics mesh. Used to create elastic or deformable objects such as cloth, rubber, or other flexible materials.

Additionally, **SoftBody3D** is subject to wind forces defined in [Area3D](class_area3d.md#class-area3d) (see [Area3D.wind_source_path](class_area3d.md#class-area3d-property-wind-source-path), [Area3D.wind_force_magnitude](class_area3d.md#class-area3d-property-wind-force-magnitude), and [Area3D.wind_attenuation_factor](class_area3d.md#class-area3d-property-wind-attenuation-factor)).

**Note:** It's recommended to use Jolt Physics when using **SoftBody3D** instead of the default GodotPhysics3D, as Jolt Physics' soft body implementation is faster and more reliable. You can switch the physics engine using the [ProjectSettings.physics/3d/physics_engine](class_projectsettings.md#class-projectsettings-property-physics-3d-physics-engine) project setting.

<a id="tutorials"></a>

## Tutorials

- [SoftBody](../tutorials/physics/soft_body.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [collision_layer](class_softbody3d.md#class-softbody3d-property-collision-layer) | `1` |
| [int](class_int.md#class-int) | [collision_mask](class_softbody3d.md#class-softbody3d-property-collision-mask) | `1` |
| [float](class_float.md#class-float) | [damping_coefficient](class_softbody3d.md#class-softbody3d-property-damping-coefficient) | `0.01` |
| [DisableMode](class_softbody3d.md#enum-softbody3d-disablemode) | [disable_mode](class_softbody3d.md#class-softbody3d-property-disable-mode) | `0` |
| [float](class_float.md#class-float) | [drag_coefficient](class_softbody3d.md#class-softbody3d-property-drag-coefficient) | `0.0` |
| [float](class_float.md#class-float) | [linear_stiffness](class_softbody3d.md#class-softbody3d-property-linear-stiffness) | `0.5` |
| [NodePath](class_nodepath.md#class-nodepath) | [parent_collision_ignore](class_softbody3d.md#class-softbody3d-property-parent-collision-ignore) | `NodePath("")` |
| [float](class_float.md#class-float) | [pressure_coefficient](class_softbody3d.md#class-softbody3d-property-pressure-coefficient) | `0.0` |
| [bool](class_bool.md#class-bool) | [ray_pickable](class_softbody3d.md#class-softbody3d-property-ray-pickable) | `true` |
| [float](class_float.md#class-float) | [shrinking_factor](class_softbody3d.md#class-softbody3d-property-shrinking-factor) | `0.0` |
| [int](class_int.md#class-int) | [simulation_precision](class_softbody3d.md#class-softbody3d-property-simulation-precision) | `5` |
| [float](class_float.md#class-float) | [total_mass](class_softbody3d.md#class-softbody3d-property-total-mass) | `1.0` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_collision_exception_with](class_softbody3d.md#class-softbody3d-method-add-collision-exception-with)(body: [Node](class_node.md#class-node)) |
| void | [apply_central_force](class_softbody3d.md#class-softbody3d-method-apply-central-force)(force: [Vector3](class_vector3.md#class-vector3)) |
| void | [apply_central_impulse](class_softbody3d.md#class-softbody3d-method-apply-central-impulse)(impulse: [Vector3](class_vector3.md#class-vector3)) |
| void | [apply_force](class_softbody3d.md#class-softbody3d-method-apply-force)(point_index: [int](class_int.md#class-int), force: [Vector3](class_vector3.md#class-vector3)) |
| void | [apply_impulse](class_softbody3d.md#class-softbody3d-method-apply-impulse)(point_index: [int](class_int.md#class-int), impulse: [Vector3](class_vector3.md#class-vector3)) |
| [Array](class_array.md#class-array)[[PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d)] | [get_collision_exceptions](class_softbody3d.md#class-softbody3d-method-get-collision-exceptions)() |
| [bool](class_bool.md#class-bool) | [get_collision_layer_value](class_softbody3d.md#class-softbody3d-method-get-collision-layer-value)(layer_number: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [get_collision_mask_value](class_softbody3d.md#class-softbody3d-method-get-collision-mask-value)(layer_number: [int](class_int.md#class-int)) const |
| [RID](class_rid.md#class-rid) | [get_physics_rid](class_softbody3d.md#class-softbody3d-method-get-physics-rid)() const |
| [Vector3](class_vector3.md#class-vector3) | [get_point_transform](class_softbody3d.md#class-softbody3d-method-get-point-transform)(point_index: [int](class_int.md#class-int)) |
| [bool](class_bool.md#class-bool) | [is_point_pinned](class_softbody3d.md#class-softbody3d-method-is-point-pinned)(point_index: [int](class_int.md#class-int)) const |
| void | [remove_collision_exception_with](class_softbody3d.md#class-softbody3d-method-remove-collision-exception-with)(body: [Node](class_node.md#class-node)) |
| void | [set_collision_layer_value](class_softbody3d.md#class-softbody3d-method-set-collision-layer-value)(layer_number: [int](class_int.md#class-int), value: [bool](class_bool.md#class-bool)) |
| void | [set_collision_mask_value](class_softbody3d.md#class-softbody3d-method-set-collision-mask-value)(layer_number: [int](class_int.md#class-int), value: [bool](class_bool.md#class-bool)) |
| void | [set_point_pinned](class_softbody3d.md#class-softbody3d-method-set-point-pinned)(point_index: [int](class_int.md#class-int), pinned: [bool](class_bool.md#class-bool), attachment_path: [NodePath](class_nodepath.md#class-nodepath) = NodePath(""), insert_at: [int](class_int.md#class-int) = -1) |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-softbody3d-disablemode"></a>

enum **DisableMode**: [🔗](class_softbody3d.md#enum-softbody3d-disablemode)

<a id="class-softbody3d-constant-disable-mode-remove"></a>

[DisableMode](class_softbody3d.md#enum-softbody3d-disablemode) **DISABLE_MODE_REMOVE** = `0`

When [Node.process_mode](class_node.md#class-node-property-process-mode) is set to [Node.PROCESS_MODE_DISABLED](class_node.md#class-node-constant-process-mode-disabled), remove from the physics simulation to stop all physics interactions with this **SoftBody3D**.

Automatically re-added to the physics simulation when the [Node](class_node.md#class-node) is processed again.

<a id="class-softbody3d-constant-disable-mode-keep-active"></a>

[DisableMode](class_softbody3d.md#enum-softbody3d-disablemode) **DISABLE_MODE_KEEP_ACTIVE** = `1`

When [Node.process_mode](class_node.md#class-node-property-process-mode) is set to [Node.PROCESS_MODE_DISABLED](class_node.md#class-node-constant-process-mode-disabled), do not affect the physics simulation.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-softbody3d-property-collision-layer"></a>

[int](class_int.md#class-int) **collision_layer** = `1` [🔗](class_softbody3d.md#class-softbody3d-property-collision-layer)

- void **set_collision_layer**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_collision_layer**()

The physics layers this SoftBody3D **is in**. Collision objects can exist in one or more of 32 different layers. See also [collision_mask](class_softbody3d.md#class-softbody3d-property-collision-mask).

**Note:** Object A can detect a contact with object B only if object B is in any of the layers that object A scans. See [Collision layers and masks](../tutorials/physics/physics_introduction.md#collision-layers-and-masks) in the documentation for more information.

---


<a id="class-softbody3d-property-collision-mask"></a>

[int](class_int.md#class-int) **collision_mask** = `1` [🔗](class_softbody3d.md#class-softbody3d-property-collision-mask)

- void **set_collision_mask**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_collision_mask**()

The physics layers this SoftBody3D **scans**. Collision objects can scan one or more of 32 different layers. See also [collision_layer](class_softbody3d.md#class-softbody3d-property-collision-layer).

**Note:** Object A can detect a contact with object B only if object B is in any of the layers that object A scans. See [Collision layers and masks](../tutorials/physics/physics_introduction.md#collision-layers-and-masks) in the documentation for more information.

---


<a id="class-softbody3d-property-damping-coefficient"></a>

[float](class_float.md#class-float) **damping_coefficient** = `0.01` [🔗](class_softbody3d.md#class-softbody3d-property-damping-coefficient)

- void **set_damping_coefficient**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_damping_coefficient**()

The body's damping coefficient. Higher values will slow down the body more noticeably when forces are applied.

---


<a id="class-softbody3d-property-disable-mode"></a>

[DisableMode](class_softbody3d.md#enum-softbody3d-disablemode) **disable_mode** = `0` [🔗](class_softbody3d.md#class-softbody3d-property-disable-mode)

- void **set_disable_mode**(value: [DisableMode](class_softbody3d.md#enum-softbody3d-disablemode))
- [DisableMode](class_softbody3d.md#enum-softbody3d-disablemode) **get_disable_mode**()

Defines the behavior in physics when [Node.process_mode](class_node.md#class-node-property-process-mode) is set to [Node.PROCESS_MODE_DISABLED](class_node.md#class-node-constant-process-mode-disabled).

---


<a id="class-softbody3d-property-drag-coefficient"></a>

[float](class_float.md#class-float) **drag_coefficient** = `0.0` [🔗](class_softbody3d.md#class-softbody3d-property-drag-coefficient)

- void **set_drag_coefficient**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_drag_coefficient**()

The body's drag coefficient. Higher values increase this body's air resistance.

**Note:** This value is currently unused by Godot's default physics implementation.

---


<a id="class-softbody3d-property-linear-stiffness"></a>

[float](class_float.md#class-float) **linear_stiffness** = `0.5` [🔗](class_softbody3d.md#class-softbody3d-property-linear-stiffness)

- void **set_linear_stiffness**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_linear_stiffness**()

Higher values will result in a stiffer body, while lower values will increase the body's ability to bend. The value can be between `0.0` and `1.0` (inclusive).

---


<a id="class-softbody3d-property-parent-collision-ignore"></a>

[NodePath](class_nodepath.md#class-nodepath) **parent_collision_ignore** = `NodePath("")` [🔗](class_softbody3d.md#class-softbody3d-property-parent-collision-ignore)

- void **set_parent_collision_ignore**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_parent_collision_ignore**()

[NodePath](class_nodepath.md#class-nodepath) to a [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d) this SoftBody3D should avoid clipping.

---


<a id="class-softbody3d-property-pressure-coefficient"></a>

[float](class_float.md#class-float) **pressure_coefficient** = `0.0` [🔗](class_softbody3d.md#class-softbody3d-property-pressure-coefficient)

- void **set_pressure_coefficient**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_pressure_coefficient**()

The pressure coefficient of this soft body. Simulate pressure build-up from inside this body. Higher values increase the strength of this effect.

---


<a id="class-softbody3d-property-ray-pickable"></a>

[bool](class_bool.md#class-bool) **ray_pickable** = `true` [🔗](class_softbody3d.md#class-softbody3d-property-ray-pickable)

- void **set_ray_pickable**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_ray_pickable**()

If `true`, the **SoftBody3D** will respond to [RayCast3D](class_raycast3d.md#class-raycast3d)s.

---


<a id="class-softbody3d-property-shrinking-factor"></a>

[float](class_float.md#class-float) **shrinking_factor** = `0.0` [🔗](class_softbody3d.md#class-softbody3d-property-shrinking-factor)

- void **set_shrinking_factor**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_shrinking_factor**()

Scales the rest lengths of **SoftBody3D**'s edge constraints. Positive values shrink the mesh, while negative values expand it. For example, a value of `0.1` shortens the edges of the mesh by 10%, while `-0.1` expands the edges by 10%.

**Note:** [shrinking_factor](class_softbody3d.md#class-softbody3d-property-shrinking-factor) is best used on surface meshes with pinned points.

---


<a id="class-softbody3d-property-simulation-precision"></a>

[int](class_int.md#class-int) **simulation_precision** = `5` [🔗](class_softbody3d.md#class-softbody3d-property-simulation-precision)

- void **set_simulation_precision**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_simulation_precision**()

Increasing this value will improve the resulting simulation, but can affect performance. Use with care.

---


<a id="class-softbody3d-property-total-mass"></a>

[float](class_float.md#class-float) **total_mass** = `1.0` [🔗](class_softbody3d.md#class-softbody3d-property-total-mass)

- void **set_total_mass**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_total_mass**()

The SoftBody3D's mass.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-softbody3d-method-add-collision-exception-with"></a>

void **add_collision_exception_with**(body: [Node](class_node.md#class-node)) [🔗](class_softbody3d.md#class-softbody3d-method-add-collision-exception-with)

Adds a body to the list of bodies that this body can't collide with.

---


<a id="class-softbody3d-method-apply-central-force"></a>

void **apply_central_force**(force: [Vector3](class_vector3.md#class-vector3)) [🔗](class_softbody3d.md#class-softbody3d-method-apply-central-force)

Distributes and applies a force to all points. A force is time dependent and meant to be applied every physics update.

---


<a id="class-softbody3d-method-apply-central-impulse"></a>

void **apply_central_impulse**(impulse: [Vector3](class_vector3.md#class-vector3)) [🔗](class_softbody3d.md#class-softbody3d-method-apply-central-impulse)

Distributes and applies an impulse to all points.

An impulse is time-independent! Applying an impulse every frame would result in a framerate-dependent force. For this reason, it should only be used when simulating one-time impacts (use the "_force" functions otherwise).

---


<a id="class-softbody3d-method-apply-force"></a>

void **apply_force**(point_index: [int](class_int.md#class-int), force: [Vector3](class_vector3.md#class-vector3)) [🔗](class_softbody3d.md#class-softbody3d-method-apply-force)

Applies a force to a point. A force is time dependent and meant to be applied every physics update.

---


<a id="class-softbody3d-method-apply-impulse"></a>

void **apply_impulse**(point_index: [int](class_int.md#class-int), impulse: [Vector3](class_vector3.md#class-vector3)) [🔗](class_softbody3d.md#class-softbody3d-method-apply-impulse)

Applies an impulse to a point.

An impulse is time-independent! Applying an impulse every frame would result in a framerate-dependent force. For this reason, it should only be used when simulating one-time impacts (use the "_force" functions otherwise).

---


<a id="class-softbody3d-method-get-collision-exceptions"></a>

[Array](class_array.md#class-array)[[PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d)] **get_collision_exceptions**() [🔗](class_softbody3d.md#class-softbody3d-method-get-collision-exceptions)

Returns an array of nodes that were added as collision exceptions for this body.

---


<a id="class-softbody3d-method-get-collision-layer-value"></a>

[bool](class_bool.md#class-bool) **get_collision_layer_value**(layer_number: [int](class_int.md#class-int)) const [🔗](class_softbody3d.md#class-softbody3d-method-get-collision-layer-value)

Returns whether or not the specified layer of the [collision_layer](class_softbody3d.md#class-softbody3d-property-collision-layer) is enabled, given a `layer_number` between 1 and 32.

---


<a id="class-softbody3d-method-get-collision-mask-value"></a>

[bool](class_bool.md#class-bool) **get_collision_mask_value**(layer_number: [int](class_int.md#class-int)) const [🔗](class_softbody3d.md#class-softbody3d-method-get-collision-mask-value)

Returns whether or not the specified layer of the [collision_mask](class_softbody3d.md#class-softbody3d-property-collision-mask) is enabled, given a `layer_number` between 1 and 32.

---


<a id="class-softbody3d-method-get-physics-rid"></a>

[RID](class_rid.md#class-rid) **get_physics_rid**() const [🔗](class_softbody3d.md#class-softbody3d-method-get-physics-rid)

Returns the internal [RID](class_rid.md#class-rid) used by the [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d) for this body.

---


<a id="class-softbody3d-method-get-point-transform"></a>

[Vector3](class_vector3.md#class-vector3) **get_point_transform**(point_index: [int](class_int.md#class-int)) [🔗](class_softbody3d.md#class-softbody3d-method-get-point-transform)

Returns local translation of a vertex in the surface array.

---


<a id="class-softbody3d-method-is-point-pinned"></a>

[bool](class_bool.md#class-bool) **is_point_pinned**(point_index: [int](class_int.md#class-int)) const [🔗](class_softbody3d.md#class-softbody3d-method-is-point-pinned)

Returns `true` if vertex is set to pinned.

---


<a id="class-softbody3d-method-remove-collision-exception-with"></a>

void **remove_collision_exception_with**(body: [Node](class_node.md#class-node)) [🔗](class_softbody3d.md#class-softbody3d-method-remove-collision-exception-with)

Removes a body from the list of bodies that this body can't collide with.

---


<a id="class-softbody3d-method-set-collision-layer-value"></a>

void **set_collision_layer_value**(layer_number: [int](class_int.md#class-int), value: [bool](class_bool.md#class-bool)) [🔗](class_softbody3d.md#class-softbody3d-method-set-collision-layer-value)

Based on `value`, enables or disables the specified layer in the [collision_layer](class_softbody3d.md#class-softbody3d-property-collision-layer), given a `layer_number` between 1 and 32.

---


<a id="class-softbody3d-method-set-collision-mask-value"></a>

void **set_collision_mask_value**(layer_number: [int](class_int.md#class-int), value: [bool](class_bool.md#class-bool)) [🔗](class_softbody3d.md#class-softbody3d-method-set-collision-mask-value)

Based on `value`, enables or disables the specified layer in the [collision_mask](class_softbody3d.md#class-softbody3d-property-collision-mask), given a `layer_number` between 1 and 32.

---


<a id="class-softbody3d-method-set-point-pinned"></a>

void **set_point_pinned**(point_index: [int](class_int.md#class-int), pinned: [bool](class_bool.md#class-bool), attachment_path: [NodePath](class_nodepath.md#class-nodepath) = NodePath(""), insert_at: [int](class_int.md#class-int) = -1) [🔗](class_softbody3d.md#class-softbody3d-method-set-point-pinned)

Sets the pinned state of a surface vertex. When set to `true`, the optional `attachment_path` can define a [Node3D](class_node3d.md#class-node3d) the pinned vertex will be attached to.
