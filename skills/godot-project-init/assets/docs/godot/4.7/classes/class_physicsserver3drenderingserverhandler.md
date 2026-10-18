> Source: https://docs.godotengine.org/en/4.7/classes/class_physicsserver3drenderingserverhandler.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="physicsserver3drenderingserverhandler"></a>

<a id="class-physicsserver3drenderingserverhandler"></a>

# PhysicsServer3DRenderingServerHandler

**Inherits:** [Object](class_object.md#class-object)

A class used to provide [PhysicsServer3DExtension._soft_body_update_rendering_server()](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-update-rendering-server) with a rendering handler for soft bodies.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [_set_aabb](class_physicsserver3drenderingserverhandler.md#class-physicsserver3drenderingserverhandler-private-method-set-aabb)(aabb: [AABB](class_aabb.md#class-aabb)) virtual required |
| void | [_set_normal](class_physicsserver3drenderingserverhandler.md#class-physicsserver3drenderingserverhandler-private-method-set-normal)(vertex_id: [int](class_int.md#class-int), normal: [Vector3](class_vector3.md#class-vector3)) virtual required |
| void | [_set_vertex](class_physicsserver3drenderingserverhandler.md#class-physicsserver3drenderingserverhandler-private-method-set-vertex)(vertex_id: [int](class_int.md#class-int), vertex: [Vector3](class_vector3.md#class-vector3)) virtual required |
| void | [set_aabb](class_physicsserver3drenderingserverhandler.md#class-physicsserver3drenderingserverhandler-method-set-aabb)(aabb: [AABB](class_aabb.md#class-aabb)) |
| void | [set_normal](class_physicsserver3drenderingserverhandler.md#class-physicsserver3drenderingserverhandler-method-set-normal)(vertex_id: [int](class_int.md#class-int), normal: [Vector3](class_vector3.md#class-vector3)) |
| void | [set_vertex](class_physicsserver3drenderingserverhandler.md#class-physicsserver3drenderingserverhandler-method-set-vertex)(vertex_id: [int](class_int.md#class-int), vertex: [Vector3](class_vector3.md#class-vector3)) |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-physicsserver3drenderingserverhandler-private-method-set-aabb"></a>

void **_set_aabb**(aabb: [AABB](class_aabb.md#class-aabb)) virtual required [🔗](class_physicsserver3drenderingserverhandler.md#class-physicsserver3drenderingserverhandler-private-method-set-aabb)

Called by the [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d) to set the bounding box for the [SoftBody3D](class_softbody3d.md#class-softbody3d).

---


<a id="class-physicsserver3drenderingserverhandler-private-method-set-normal"></a>

void **_set_normal**(vertex_id: [int](class_int.md#class-int), normal: [Vector3](class_vector3.md#class-vector3)) virtual required [🔗](class_physicsserver3drenderingserverhandler.md#class-physicsserver3drenderingserverhandler-private-method-set-normal)

Called by the [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d) to set the normal for the [SoftBody3D](class_softbody3d.md#class-softbody3d) vertex at the index specified by `vertex_id`.

**Note:** The `normal` parameter used to be of type `const void*` prior to Godot 4.2.

---


<a id="class-physicsserver3drenderingserverhandler-private-method-set-vertex"></a>

void **_set_vertex**(vertex_id: [int](class_int.md#class-int), vertex: [Vector3](class_vector3.md#class-vector3)) virtual required [🔗](class_physicsserver3drenderingserverhandler.md#class-physicsserver3drenderingserverhandler-private-method-set-vertex)

Called by the [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d) to set the position for the [SoftBody3D](class_softbody3d.md#class-softbody3d) vertex at the index specified by `vertex_id`.

**Note:** The `vertex` parameter used to be of type `const void*` prior to Godot 4.2.

---


<a id="class-physicsserver3drenderingserverhandler-method-set-aabb"></a>

void **set_aabb**(aabb: [AABB](class_aabb.md#class-aabb)) [🔗](class_physicsserver3drenderingserverhandler.md#class-physicsserver3drenderingserverhandler-method-set-aabb)

Sets the bounding box for the [SoftBody3D](class_softbody3d.md#class-softbody3d).

---


<a id="class-physicsserver3drenderingserverhandler-method-set-normal"></a>

void **set_normal**(vertex_id: [int](class_int.md#class-int), normal: [Vector3](class_vector3.md#class-vector3)) [🔗](class_physicsserver3drenderingserverhandler.md#class-physicsserver3drenderingserverhandler-method-set-normal)

Sets the normal for the [SoftBody3D](class_softbody3d.md#class-softbody3d) vertex at the index specified by `vertex_id`.

---


<a id="class-physicsserver3drenderingserverhandler-method-set-vertex"></a>

void **set_vertex**(vertex_id: [int](class_int.md#class-int), vertex: [Vector3](class_vector3.md#class-vector3)) [🔗](class_physicsserver3drenderingserverhandler.md#class-physicsserver3drenderingserverhandler-method-set-vertex)

Sets the position for the [SoftBody3D](class_softbody3d.md#class-softbody3d) vertex at the index specified by `vertex_id`.
