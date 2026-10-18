> Source: https://docs.godotengine.org/en/4.7/classes/class_multiplayerspawner.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="multiplayerspawner"></a>

<a id="class-multiplayerspawner"></a>

# MultiplayerSpawner

**Inherits:** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Automatically replicates spawnable nodes from the authority to other multiplayer peers.

<a id="description"></a>

## Description

Spawnable scenes can be configured in the editor or through code (see [add_spawnable_scene()](class_multiplayerspawner.md#class-multiplayerspawner-method-add-spawnable-scene)).

Also supports custom node spawns through [spawn()](class_multiplayerspawner.md#class-multiplayerspawner-method-spawn), calling [spawn_function](class_multiplayerspawner.md#class-multiplayerspawner-property-spawn-function) on all peers.

Internally, **MultiplayerSpawner** uses [MultiplayerAPI.object_configuration_add()](class_multiplayerapi.md#class-multiplayerapi-method-object-configuration-add) to notify spawns passing the spawned node as the `object` and itself as the `configuration`, and [MultiplayerAPI.object_configuration_remove()](class_multiplayerapi.md#class-multiplayerapi-method-object-configuration-remove) to notify despawns in a similar way.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Callable](class_callable.md#class-callable) | [spawn_function](class_multiplayerspawner.md#class-multiplayerspawner-property-spawn-function) |  |
| [int](class_int.md#class-int) | [spawn_limit](class_multiplayerspawner.md#class-multiplayerspawner-property-spawn-limit) | `0` |
| [NodePath](class_nodepath.md#class-nodepath) | [spawn_path](class_multiplayerspawner.md#class-multiplayerspawner-property-spawn-path) | `NodePath("")` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_spawnable_scene](class_multiplayerspawner.md#class-multiplayerspawner-method-add-spawnable-scene)(path: [String](class_string.md#class-string)) |
| void | [clear_spawnable_scenes](class_multiplayerspawner.md#class-multiplayerspawner-method-clear-spawnable-scenes)() |
| [String](class_string.md#class-string) | [get_spawnable_scene](class_multiplayerspawner.md#class-multiplayerspawner-method-get-spawnable-scene)(index: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_spawnable_scene_count](class_multiplayerspawner.md#class-multiplayerspawner-method-get-spawnable-scene-count)() const |
| [Node](class_node.md#class-node) | [spawn](class_multiplayerspawner.md#class-multiplayerspawner-method-spawn)(data: [Variant](class_variant.md#class-variant) = null) |

---


<a id="signals"></a>

## Signals

<a id="class-multiplayerspawner-signal-despawned"></a>

**despawned**(node: [Node](class_node.md#class-node)) [🔗](class_multiplayerspawner.md#class-multiplayerspawner-signal-despawned)

Emitted when a spawnable scene or custom spawn was despawned by the multiplayer authority. Only called on remote peers.

---


<a id="class-multiplayerspawner-signal-spawned"></a>

**spawned**(node: [Node](class_node.md#class-node)) [🔗](class_multiplayerspawner.md#class-multiplayerspawner-signal-spawned)

Emitted when a spawnable scene or custom spawn was spawned by the multiplayer authority. Only called on remote peers.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-multiplayerspawner-property-spawn-function"></a>

[Callable](class_callable.md#class-callable) **spawn_function** [🔗](class_multiplayerspawner.md#class-multiplayerspawner-property-spawn-function)

- void **set_spawn_function**(value: [Callable](class_callable.md#class-callable))
- [Callable](class_callable.md#class-callable) **get_spawn_function**()

Method called on all peers when a custom [spawn()](class_multiplayerspawner.md#class-multiplayerspawner-method-spawn) is requested by the authority. Will receive the `data` parameter, and should return a [Node](class_node.md#class-node) that is not in the scene tree.

**Note:** The returned node should **not** be added to the scene with [Node.add_child()](class_node.md#class-node-method-add-child). This is done automatically.

---


<a id="class-multiplayerspawner-property-spawn-limit"></a>

[int](class_int.md#class-int) **spawn_limit** = `0` [🔗](class_multiplayerspawner.md#class-multiplayerspawner-property-spawn-limit)

- void **set_spawn_limit**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_spawn_limit**()

Maximum number of nodes allowed to be spawned by this spawner. Includes both spawnable scenes and custom spawns.

When set to `0` (the default), there is no limit.

---


<a id="class-multiplayerspawner-property-spawn-path"></a>

[NodePath](class_nodepath.md#class-nodepath) **spawn_path** = `NodePath("")` [🔗](class_multiplayerspawner.md#class-multiplayerspawner-property-spawn-path)

- void **set_spawn_path**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_spawn_path**()

Path to the spawn root. Spawnable scenes that are added as direct children are replicated to other peers.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-multiplayerspawner-method-add-spawnable-scene"></a>

void **add_spawnable_scene**(path: [String](class_string.md#class-string)) [🔗](class_multiplayerspawner.md#class-multiplayerspawner-method-add-spawnable-scene)

Adds a scene path to spawnable scenes, making it automatically replicated from the multiplayer authority to other peers when added as children of the node pointed by [spawn_path](class_multiplayerspawner.md#class-multiplayerspawner-property-spawn-path).

---


<a id="class-multiplayerspawner-method-clear-spawnable-scenes"></a>

void **clear_spawnable_scenes**() [🔗](class_multiplayerspawner.md#class-multiplayerspawner-method-clear-spawnable-scenes)

Clears all spawnable scenes. Does not despawn existing instances on remote peers.

---


<a id="class-multiplayerspawner-method-get-spawnable-scene"></a>

[String](class_string.md#class-string) **get_spawnable_scene**(index: [int](class_int.md#class-int)) const [🔗](class_multiplayerspawner.md#class-multiplayerspawner-method-get-spawnable-scene)

Returns the spawnable scene path by index.

---


<a id="class-multiplayerspawner-method-get-spawnable-scene-count"></a>

[int](class_int.md#class-int) **get_spawnable_scene_count**() const [🔗](class_multiplayerspawner.md#class-multiplayerspawner-method-get-spawnable-scene-count)

Returns the count of spawnable scene paths.

---


<a id="class-multiplayerspawner-method-spawn"></a>

[Node](class_node.md#class-node) **spawn**(data: [Variant](class_variant.md#class-variant) = null) [🔗](class_multiplayerspawner.md#class-multiplayerspawner-method-spawn)

Requests a custom spawn, with `data` passed to [spawn_function](class_multiplayerspawner.md#class-multiplayerspawner-property-spawn-function) on all peers. Returns the locally spawned node instance already inside the scene tree, and added as a child of the node pointed by [spawn_path](class_multiplayerspawner.md#class-multiplayerspawner-property-spawn-path).

**Note:** Spawnable scenes are spawned automatically. [spawn()](class_multiplayerspawner.md#class-multiplayerspawner-method-spawn) is only needed for custom spawns.
