> Source: https://docs.godotengine.org/en/4.7/classes/class_packedscene.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="packedscene"></a>

<a id="class-packedscene"></a>

# PackedScene

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

An abstraction of a serialized scene.

<a id="description"></a>

## Description

A simplified interface to a scene file. Provides access to operations and checks that can be performed on the scene resource itself.

Can be used to save a node to a file. When saving, the node as well as all the nodes it owns get saved (see [Node.owner](class_node.md#class-node-property-owner) property).

**Note:** The node doesn't need to own itself.

**Example:** Load a saved scene:

```gdscript
# Use load() instead of preload() if the path isn't known at compile-time.
var scene = preload("res://scene.tscn").instantiate()
# Add the node as a child of the node the script is attached to.
add_child(scene)
```

```csharp
// C# has no preload, so you have to always use ResourceLoader.Load<PackedScene>().
var scene = ResourceLoader.Load<PackedScene>("res://scene.tscn").Instantiate();
// Add the node as a child of the node the script is attached to.
AddChild(scene);
```

**Example:** Save a node with different owners. The following example creates 3 objects: [Node2D](class_node2d.md#class-node2d) (`node`), [RigidBody2D](class_rigidbody2d.md#class-rigidbody2d) (`body`) and [CollisionObject2D](class_collisionobject2d.md#class-collisionobject2d) (`collision`). `collision` is a child of `body` which is a child of `node`. Only `body` is owned by `node` and [pack()](class_packedscene.md#class-packedscene-method-pack) will therefore only save those two nodes, but not `collision`.

```gdscript
# Create the objects.
var node = Node2D.new()
var body = RigidBody2D.new()
var collision = CollisionShape2D.new()

# Create the object hierarchy.
body.add_child(collision)
node.add_child(body)

# Change owner of `body`, but not of `collision`.
body.owner = node
var scene = PackedScene.new()

# Only `node` and `body` are now packed.
var result = scene.pack(node)
if result == OK:
    var error = ResourceSaver.save(scene, "res://path/name.tscn")  # Or "user://..."
    if error != OK:
        push_error("An error occurred while saving the scene to disk.")
```

```csharp
// Create the objects.
var node = new Node2D();
var body = new RigidBody2D();
var collision = new CollisionShape2D();

// Create the object hierarchy.
body.AddChild(collision);
node.AddChild(body);

// Change owner of `body`, but not of `collision`.
body.Owner = node;
var scene = new PackedScene();

// Only `node` and `body` are now packed.
Error result = scene.Pack(node);
if (result == Error.Ok)
{
    Error error = ResourceSaver.Save(scene, "res://path/name.tscn"); // Or "user://..."
    if (error != Error.Ok)
    {
        GD.PushError("An error occurred while saving the scene to disk.");
    }
}
```

<a id="tutorials"></a>

## Tutorials

- [2D Role Playing Game (RPG) Demo](https://godotengine.org/asset-library/asset/2729)

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [can_instantiate](class_packedscene.md#class-packedscene-method-can-instantiate)() const |
| [SceneState](class_scenestate.md#class-scenestate) | [get_state](class_packedscene.md#class-packedscene-method-get-state)() const |
| [Node](class_node.md#class-node) | [instantiate](class_packedscene.md#class-packedscene-method-instantiate)(edit_state: [GenEditState](class_packedscene.md#enum-packedscene-geneditstate) = 0) const |
| [Error](class_@globalscope.md#enum-globalscope-error) | [pack](class_packedscene.md#class-packedscene-method-pack)(path: [Node](class_node.md#class-node)) |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-packedscene-geneditstate"></a>

enum **GenEditState**: [🔗](class_packedscene.md#enum-packedscene-geneditstate)

<a id="class-packedscene-constant-gen-edit-state-disabled"></a>

[GenEditState](class_packedscene.md#enum-packedscene-geneditstate) **GEN_EDIT_STATE_DISABLED** = `0`

If passed to [instantiate()](class_packedscene.md#class-packedscene-method-instantiate), blocks edits to the scene state.

<a id="class-packedscene-constant-gen-edit-state-instance"></a>

[GenEditState](class_packedscene.md#enum-packedscene-geneditstate) **GEN_EDIT_STATE_INSTANCE** = `1`

If passed to [instantiate()](class_packedscene.md#class-packedscene-method-instantiate), provides local scene resources to the local scene.

**Note:** Only available in editor builds.

<a id="class-packedscene-constant-gen-edit-state-main"></a>

[GenEditState](class_packedscene.md#enum-packedscene-geneditstate) **GEN_EDIT_STATE_MAIN** = `2`

If passed to [instantiate()](class_packedscene.md#class-packedscene-method-instantiate), provides local scene resources to the local scene. Only the main scene should receive the main edit state.

**Note:** Only available in editor builds.

<a id="class-packedscene-constant-gen-edit-state-main-inherited"></a>

[GenEditState](class_packedscene.md#enum-packedscene-geneditstate) **GEN_EDIT_STATE_MAIN_INHERITED** = `3`

It's similar to [GEN_EDIT_STATE_MAIN](class_packedscene.md#class-packedscene-constant-gen-edit-state-main), but for the case where the scene is being instantiated to be the base of another one.

**Note:** Only available in editor builds.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-packedscene-method-can-instantiate"></a>

[bool](class_bool.md#class-bool) **can_instantiate**() const [🔗](class_packedscene.md#class-packedscene-method-can-instantiate)

Returns `true` if the scene file has nodes.

---


<a id="class-packedscene-method-get-state"></a>

[SceneState](class_scenestate.md#class-scenestate) **get_state**() const [🔗](class_packedscene.md#class-packedscene-method-get-state)

Returns the [SceneState](class_scenestate.md#class-scenestate) representing the scene file contents.

---


<a id="class-packedscene-method-instantiate"></a>

[Node](class_node.md#class-node) **instantiate**(edit_state: [GenEditState](class_packedscene.md#enum-packedscene-geneditstate) = 0) const [🔗](class_packedscene.md#class-packedscene-method-instantiate)

Instantiates the scene's node hierarchy. Triggers child scene instantiation(s). Triggers a [Node.NOTIFICATION_SCENE_INSTANTIATED](class_node.md#class-node-constant-notification-scene-instantiated) notification on the root node.

---


<a id="class-packedscene-method-pack"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **pack**(path: [Node](class_node.md#class-node)) [🔗](class_packedscene.md#class-packedscene-method-pack)

Packs the `path` node, and all owned sub-nodes, into this **PackedScene**. Any existing data will be cleared. See [Node.owner](class_node.md#class-node-property-owner).
