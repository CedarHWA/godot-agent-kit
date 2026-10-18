> Source: https://docs.godotengine.org/en/4.7/classes/class_animatablebody3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="animatablebody3d"></a>

<a id="class-animatablebody3d"></a>

# AnimatableBody3D

**Inherits:** [StaticBody3D](class_staticbody3d.md#class-staticbody3d) **<** [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d) **<** [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A 3D physics body that can't be moved by external forces. When moved manually, it affects other bodies in its path.

<a id="description"></a>

## Description

An animatable 3D physics body. It can't be moved by external forces or contacts, but can be moved manually by other means such as code, [AnimationMixer](class_animationmixer.md#class-animationmixer)s (with [AnimationMixer.callback_mode_process](class_animationmixer.md#class-animationmixer-property-callback-mode-process) set to [AnimationMixer.ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS](class_animationmixer.md#class-animationmixer-constant-animation-callback-mode-process-physics)), and [RemoteTransform3D](class_remotetransform3d.md#class-remotetransform3d).

When **AnimatableBody3D** is moved, its linear and angular velocity are estimated and used to affect other physics bodies in its path. This makes it useful for moving platforms, doors, and other moving objects.

<a id="tutorials"></a>

## Tutorials

- [Physics introduction](../tutorials/physics/physics_introduction.md)
- [Troubleshooting physics issues](../tutorials/physics/troubleshooting_physics_issues.md)
- [3D Physics Tests Demo](https://godotengine.org/asset-library/asset/2747)
- [Third Person Shooter (TPS) Demo](https://godotengine.org/asset-library/asset/2710)
- [3D Voxel Demo](https://godotengine.org/asset-library/asset/2755)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [sync_to_physics](class_animatablebody3d.md#class-animatablebody3d-property-sync-to-physics) | `true` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-animatablebody3d-property-sync-to-physics"></a>

[bool](class_bool.md#class-bool) **sync_to_physics** = `true` [🔗](class_animatablebody3d.md#class-animatablebody3d-property-sync-to-physics)

- void **set_sync_to_physics**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_sync_to_physics_enabled**()

If `true`, the body's movement will be synchronized to the physics frame. This is useful when animating movement via [AnimationPlayer](class_animationplayer.md#class-animationplayer), for example on moving platforms. Do **not** use together with [PhysicsBody3D.move_and_collide()](class_physicsbody3d.md#class-physicsbody3d-method-move-and-collide).
