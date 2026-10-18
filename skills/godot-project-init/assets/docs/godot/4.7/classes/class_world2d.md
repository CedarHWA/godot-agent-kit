> Source: https://docs.godotengine.org/en/4.7/classes/class_world2d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="world2d"></a>

<a id="class-world2d"></a>

# World2D

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A resource that holds all components of a 2D world, such as a canvas and a physics space.

<a id="description"></a>

## Description

Class that has everything pertaining to a 2D world: A physics space, a canvas, and a sound space. 2D nodes register their resources into the current 2D world.

<a id="tutorials"></a>

## Tutorials

- [Ray-casting](../tutorials/physics/ray-casting.md)

<a id="properties"></a>

## Properties

|  |  |
| --- | --- |
| [RID](class_rid.md#class-rid) | [canvas](class_world2d.md#class-world2d-property-canvas) |
| [PhysicsDirectSpaceState2D](class_physicsdirectspacestate2d.md#class-physicsdirectspacestate2d) | [direct_space_state](class_world2d.md#class-world2d-property-direct-space-state) |
| [RID](class_rid.md#class-rid) | [navigation_map](class_world2d.md#class-world2d-property-navigation-map) |
| [RID](class_rid.md#class-rid) | [space](class_world2d.md#class-world2d-property-space) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-world2d-property-canvas"></a>

[RID](class_rid.md#class-rid) **canvas** [🔗](class_world2d.md#class-world2d-property-canvas)

- [RID](class_rid.md#class-rid) **get_canvas**()

The [RID](class_rid.md#class-rid) of this world's canvas resource. Used by the [RenderingServer](class_renderingserver.md#class-renderingserver) for 2D drawing.

---


<a id="class-world2d-property-direct-space-state"></a>

[PhysicsDirectSpaceState2D](class_physicsdirectspacestate2d.md#class-physicsdirectspacestate2d) **direct_space_state** [🔗](class_world2d.md#class-world2d-property-direct-space-state)

- [PhysicsDirectSpaceState2D](class_physicsdirectspacestate2d.md#class-physicsdirectspacestate2d) **get_direct_space_state**()

Direct access to the world's physics 2D space state. Used for querying current and potential collisions. When using multi-threaded physics, access is limited to [Node._physics_process()](class_node.md#class-node-private-method-physics-process) in the main thread.

---


<a id="class-world2d-property-navigation-map"></a>

[RID](class_rid.md#class-rid) **navigation_map** [🔗](class_world2d.md#class-world2d-property-navigation-map)

- [RID](class_rid.md#class-rid) **get_navigation_map**()

The [RID](class_rid.md#class-rid) of this world's navigation map. Used by the [NavigationServer2D](class_navigationserver2d.md#class-navigationserver2d).

---


<a id="class-world2d-property-space"></a>

[RID](class_rid.md#class-rid) **space** [🔗](class_world2d.md#class-world2d-property-space)

- [RID](class_rid.md#class-rid) **get_space**()

The [RID](class_rid.md#class-rid) of this world's physics space resource. Used by the [PhysicsServer2D](class_physicsserver2d.md#class-physicsserver2d) for 2D physics, treating it as both a space and an area.
