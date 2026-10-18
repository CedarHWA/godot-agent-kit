> Source: https://docs.godotengine.org/en/4.7/classes/class_worldboundaryshape3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="worldboundaryshape3d"></a>

<a id="class-worldboundaryshape3d"></a>

# WorldBoundaryShape3D

**Inherits:** [Shape3D](class_shape3d.md#class-shape3d) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A 3D world boundary (half-space) shape used for physics collision.

<a id="description"></a>

## Description

A 3D world boundary shape, intended for use in physics. **WorldBoundaryShape3D** works like an infinite plane that forces all physics bodies to stay above it. The [plane](class_worldboundaryshape3d.md#class-worldboundaryshape3d-property-plane)'s normal determines which direction is considered as "above" and in the editor, the line over the plane represents this direction. It can for example be used for endless flat floors.

**Note:** When the physics engine is set to **Jolt Physics** in the project settings ([ProjectSettings.physics/3d/physics_engine](class_projectsettings.md#class-projectsettings-property-physics-3d-physics-engine)), **WorldBoundaryShape3D** has a finite size (centered at the shape's origin). It can be adjusted by changing [ProjectSettings.physics/jolt_physics_3d/limits/world_boundary_shape_size](class_projectsettings.md#class-projectsettings-property-physics-jolt-physics-3d-limits-world-boundary-shape-size).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Plane](class_plane.md#class-plane) | [plane](class_worldboundaryshape3d.md#class-worldboundaryshape3d-property-plane) | `Plane(0, 1, 0, 0)` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-worldboundaryshape3d-property-plane"></a>

[Plane](class_plane.md#class-plane) **plane** = `Plane(0, 1, 0, 0)` [🔗](class_worldboundaryshape3d.md#class-worldboundaryshape3d-property-plane)

- void **set_plane**(value: [Plane](class_plane.md#class-plane))
- [Plane](class_plane.md#class-plane) **get_plane**()

The [Plane](class_plane.md#class-plane) used by the **WorldBoundaryShape3D** for collision.
