> Source: https://docs.godotengine.org/en/4.7/classes/class_remotetransform3d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="remotetransform3d"></a>

<a id="class-remotetransform3d"></a>

# RemoteTransform3D

**Inherits:** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

RemoteTransform3D pushes its own [Transform3D](class_transform3d.md#class-transform3d) to another [Node3D](class_node3d.md#class-node3d) derived Node in the scene.

<a id="description"></a>

## Description

RemoteTransform3D pushes its own [Transform3D](class_transform3d.md#class-transform3d) to another [Node3D](class_node3d.md#class-node3d) derived Node (called the remote node) in the scene.

It can be set to update another Node's position, rotation and/or scale. It can use either global or local coordinates.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [NodePath](class_nodepath.md#class-nodepath) | [remote_path](class_remotetransform3d.md#class-remotetransform3d-property-remote-path) | `NodePath("")` |
| [bool](class_bool.md#class-bool) | [update_position](class_remotetransform3d.md#class-remotetransform3d-property-update-position) | `true` |
| [bool](class_bool.md#class-bool) | [update_rotation](class_remotetransform3d.md#class-remotetransform3d-property-update-rotation) | `true` |
| [bool](class_bool.md#class-bool) | [update_scale](class_remotetransform3d.md#class-remotetransform3d-property-update-scale) | `true` |
| [bool](class_bool.md#class-bool) | [use_global_coordinates](class_remotetransform3d.md#class-remotetransform3d-property-use-global-coordinates) | `true` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [force_update_cache](class_remotetransform3d.md#class-remotetransform3d-method-force-update-cache)() |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-remotetransform3d-property-remote-path"></a>

[NodePath](class_nodepath.md#class-nodepath) **remote_path** = `NodePath("")` [🔗](class_remotetransform3d.md#class-remotetransform3d-property-remote-path)

- void **set_remote_node**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_remote_node**()

The [NodePath](class_nodepath.md#class-nodepath) to the remote node, relative to the RemoteTransform3D's position in the scene.

---


<a id="class-remotetransform3d-property-update-position"></a>

[bool](class_bool.md#class-bool) **update_position** = `true` [🔗](class_remotetransform3d.md#class-remotetransform3d-property-update-position)

- void **set_update_position**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_update_position**()

If `true`, the remote node's position is updated.

---


<a id="class-remotetransform3d-property-update-rotation"></a>

[bool](class_bool.md#class-bool) **update_rotation** = `true` [🔗](class_remotetransform3d.md#class-remotetransform3d-property-update-rotation)

- void **set_update_rotation**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_update_rotation**()

If `true`, the remote node's rotation is updated.

---


<a id="class-remotetransform3d-property-update-scale"></a>

[bool](class_bool.md#class-bool) **update_scale** = `true` [🔗](class_remotetransform3d.md#class-remotetransform3d-property-update-scale)

- void **set_update_scale**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_update_scale**()

If `true`, the remote node's scale is updated.

---


<a id="class-remotetransform3d-property-use-global-coordinates"></a>

[bool](class_bool.md#class-bool) **use_global_coordinates** = `true` [🔗](class_remotetransform3d.md#class-remotetransform3d-property-use-global-coordinates)

- void **set_use_global_coordinates**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_use_global_coordinates**()

If `true`, global coordinates are used. If `false`, local coordinates are used.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-remotetransform3d-method-force-update-cache"></a>

void **force_update_cache**() [🔗](class_remotetransform3d.md#class-remotetransform3d-method-force-update-cache)

**RemoteTransform3D** caches the remote node. It may not notice if the remote node disappears; [force_update_cache()](class_remotetransform3d.md#class-remotetransform3d-method-force-update-cache) forces it to update the cache again.
