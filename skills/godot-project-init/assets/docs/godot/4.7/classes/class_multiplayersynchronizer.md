> Source: https://docs.godotengine.org/en/4.7/classes/class_multiplayersynchronizer.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="multiplayersynchronizer"></a>

<a id="class-multiplayersynchronizer"></a>

# MultiplayerSynchronizer

**Inherits:** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Synchronizes properties from the multiplayer authority to the remote peers.

<a id="description"></a>

## Description

By default, **MultiplayerSynchronizer** synchronizes configured properties to all peers.

Visibility can be handled directly with [set_visibility_for()](class_multiplayersynchronizer.md#class-multiplayersynchronizer-method-set-visibility-for) or as-needed with [add_visibility_filter()](class_multiplayersynchronizer.md#class-multiplayersynchronizer-method-add-visibility-filter) and [update_visibility()](class_multiplayersynchronizer.md#class-multiplayersynchronizer-method-update-visibility).

[MultiplayerSpawner](class_multiplayerspawner.md#class-multiplayerspawner)s will handle nodes according to visibility of synchronizers as long as the node at [root_path](class_multiplayersynchronizer.md#class-multiplayersynchronizer-property-root-path) was spawned by one.

Internally, **MultiplayerSynchronizer** uses [MultiplayerAPI.object_configuration_add()](class_multiplayerapi.md#class-multiplayerapi-method-object-configuration-add) to notify synchronization start passing the [Node](class_node.md#class-node) at [root_path](class_multiplayersynchronizer.md#class-multiplayersynchronizer-property-root-path) as the `object` and itself as the `configuration`, and uses [MultiplayerAPI.object_configuration_remove()](class_multiplayerapi.md#class-multiplayerapi-method-object-configuration-remove) to notify synchronization end in a similar way.

**Note:** Synchronization is not supported for [Object](class_object.md#class-object) type properties, like [Resource](class_resource.md#class-resource). Properties that are unique to each peer, like the instance IDs of [Object](class_object.md#class-object)s (see [Object.get_instance_id()](class_object.md#class-object-method-get-instance-id)) or [RID](class_rid.md#class-rid)s, will also not work in synchronization.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [delta_interval](class_multiplayersynchronizer.md#class-multiplayersynchronizer-property-delta-interval) | `0.0` |
| [bool](class_bool.md#class-bool) | [public_visibility](class_multiplayersynchronizer.md#class-multiplayersynchronizer-property-public-visibility) | `true` |
| [SceneReplicationConfig](class_scenereplicationconfig.md#class-scenereplicationconfig) | [replication_config](class_multiplayersynchronizer.md#class-multiplayersynchronizer-property-replication-config) |  |
| [float](class_float.md#class-float) | [replication_interval](class_multiplayersynchronizer.md#class-multiplayersynchronizer-property-replication-interval) | `0.0` |
| [NodePath](class_nodepath.md#class-nodepath) | [root_path](class_multiplayersynchronizer.md#class-multiplayersynchronizer-property-root-path) | `NodePath("..")` |
| [VisibilityUpdateMode](class_multiplayersynchronizer.md#enum-multiplayersynchronizer-visibilityupdatemode) | [visibility_update_mode](class_multiplayersynchronizer.md#class-multiplayersynchronizer-property-visibility-update-mode) | `0` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_visibility_filter](class_multiplayersynchronizer.md#class-multiplayersynchronizer-method-add-visibility-filter)(filter: [Callable](class_callable.md#class-callable)) |
| [bool](class_bool.md#class-bool) | [get_visibility_for](class_multiplayersynchronizer.md#class-multiplayersynchronizer-method-get-visibility-for)(peer: [int](class_int.md#class-int)) const |
| void | [remove_visibility_filter](class_multiplayersynchronizer.md#class-multiplayersynchronizer-method-remove-visibility-filter)(filter: [Callable](class_callable.md#class-callable)) |
| void | [set_visibility_for](class_multiplayersynchronizer.md#class-multiplayersynchronizer-method-set-visibility-for)(peer: [int](class_int.md#class-int), visible: [bool](class_bool.md#class-bool)) |
| void | [update_visibility](class_multiplayersynchronizer.md#class-multiplayersynchronizer-method-update-visibility)(for_peer: [int](class_int.md#class-int) = 0) |

---


<a id="signals"></a>

## Signals

<a id="class-multiplayersynchronizer-signal-delta-synchronized"></a>

**delta_synchronized**() [🔗](class_multiplayersynchronizer.md#class-multiplayersynchronizer-signal-delta-synchronized)

Emitted when a new delta synchronization state is received by this synchronizer after the properties have been updated.

---


<a id="class-multiplayersynchronizer-signal-synchronized"></a>

**synchronized**() [🔗](class_multiplayersynchronizer.md#class-multiplayersynchronizer-signal-synchronized)

Emitted when a new synchronization state is received by this synchronizer after the properties have been updated.

---


<a id="class-multiplayersynchronizer-signal-visibility-changed"></a>

**visibility_changed**(for_peer: [int](class_int.md#class-int)) [🔗](class_multiplayersynchronizer.md#class-multiplayersynchronizer-signal-visibility-changed)

Emitted when visibility of `for_peer` is updated. See [update_visibility()](class_multiplayersynchronizer.md#class-multiplayersynchronizer-method-update-visibility).

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-multiplayersynchronizer-visibilityupdatemode"></a>

enum **VisibilityUpdateMode**: [🔗](class_multiplayersynchronizer.md#enum-multiplayersynchronizer-visibilityupdatemode)

<a id="class-multiplayersynchronizer-constant-visibility-process-idle"></a>

[VisibilityUpdateMode](class_multiplayersynchronizer.md#enum-multiplayersynchronizer-visibilityupdatemode) **VISIBILITY_PROCESS_IDLE** = `0`

Visibility filters are updated during process frames (see [Node.NOTIFICATION_INTERNAL_PROCESS](class_node.md#class-node-constant-notification-internal-process)).

<a id="class-multiplayersynchronizer-constant-visibility-process-physics"></a>

[VisibilityUpdateMode](class_multiplayersynchronizer.md#enum-multiplayersynchronizer-visibilityupdatemode) **VISIBILITY_PROCESS_PHYSICS** = `1`

Visibility filters are updated during physics frames (see [Node.NOTIFICATION_INTERNAL_PHYSICS_PROCESS](class_node.md#class-node-constant-notification-internal-physics-process)).

<a id="class-multiplayersynchronizer-constant-visibility-process-none"></a>

[VisibilityUpdateMode](class_multiplayersynchronizer.md#enum-multiplayersynchronizer-visibilityupdatemode) **VISIBILITY_PROCESS_NONE** = `2`

Visibility filters are not updated automatically, and must be updated manually by calling [update_visibility()](class_multiplayersynchronizer.md#class-multiplayersynchronizer-method-update-visibility).

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-multiplayersynchronizer-property-delta-interval"></a>

[float](class_float.md#class-float) **delta_interval** = `0.0` [🔗](class_multiplayersynchronizer.md#class-multiplayersynchronizer-property-delta-interval)

- void **set_delta_interval**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_delta_interval**()

Time interval between delta synchronizations. Used when the replication is set to [SceneReplicationConfig.REPLICATION_MODE_ON_CHANGE](class_scenereplicationconfig.md#class-scenereplicationconfig-constant-replication-mode-on-change). If set to `0.0` (the default), delta synchronizations happen every network process frame.

---


<a id="class-multiplayersynchronizer-property-public-visibility"></a>

[bool](class_bool.md#class-bool) **public_visibility** = `true` [🔗](class_multiplayersynchronizer.md#class-multiplayersynchronizer-property-public-visibility)

- void **set_visibility_public**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_visibility_public**()

Whether synchronization should be visible to all peers by default. See [set_visibility_for()](class_multiplayersynchronizer.md#class-multiplayersynchronizer-method-set-visibility-for) and [add_visibility_filter()](class_multiplayersynchronizer.md#class-multiplayersynchronizer-method-add-visibility-filter) for ways of configuring fine-grained visibility options.

---


<a id="class-multiplayersynchronizer-property-replication-config"></a>

[SceneReplicationConfig](class_scenereplicationconfig.md#class-scenereplicationconfig) **replication_config** [🔗](class_multiplayersynchronizer.md#class-multiplayersynchronizer-property-replication-config)

- void **set_replication_config**(value: [SceneReplicationConfig](class_scenereplicationconfig.md#class-scenereplicationconfig))
- [SceneReplicationConfig](class_scenereplicationconfig.md#class-scenereplicationconfig) **get_replication_config**()

Resource containing which properties to synchronize.

---


<a id="class-multiplayersynchronizer-property-replication-interval"></a>

[float](class_float.md#class-float) **replication_interval** = `0.0` [🔗](class_multiplayersynchronizer.md#class-multiplayersynchronizer-property-replication-interval)

- void **set_replication_interval**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_replication_interval**()

Time interval between synchronizations. Used when the replication is set to [SceneReplicationConfig.REPLICATION_MODE_ALWAYS](class_scenereplicationconfig.md#class-scenereplicationconfig-constant-replication-mode-always). If set to `0.0` (the default), synchronizations happen every network process frame.

---


<a id="class-multiplayersynchronizer-property-root-path"></a>

[NodePath](class_nodepath.md#class-nodepath) **root_path** = `NodePath("..")` [🔗](class_multiplayersynchronizer.md#class-multiplayersynchronizer-property-root-path)

- void **set_root_path**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_root_path**()

Node path that replicated properties are relative to.

If [root_path](class_multiplayersynchronizer.md#class-multiplayersynchronizer-property-root-path) was spawned by a [MultiplayerSpawner](class_multiplayerspawner.md#class-multiplayerspawner), the node will be also be spawned and despawned based on this synchronizer visibility options.

---


<a id="class-multiplayersynchronizer-property-visibility-update-mode"></a>

[VisibilityUpdateMode](class_multiplayersynchronizer.md#enum-multiplayersynchronizer-visibilityupdatemode) **visibility_update_mode** = `0` [🔗](class_multiplayersynchronizer.md#class-multiplayersynchronizer-property-visibility-update-mode)

- void **set_visibility_update_mode**(value: [VisibilityUpdateMode](class_multiplayersynchronizer.md#enum-multiplayersynchronizer-visibilityupdatemode))
- [VisibilityUpdateMode](class_multiplayersynchronizer.md#enum-multiplayersynchronizer-visibilityupdatemode) **get_visibility_update_mode**()

Specifies when visibility filters are updated.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-multiplayersynchronizer-method-add-visibility-filter"></a>

void **add_visibility_filter**(filter: [Callable](class_callable.md#class-callable)) [🔗](class_multiplayersynchronizer.md#class-multiplayersynchronizer-method-add-visibility-filter)

Adds a peer visibility filter for this synchronizer.

`filter` should take a peer ID [int](class_int.md#class-int) and return a [bool](class_bool.md#class-bool).

---


<a id="class-multiplayersynchronizer-method-get-visibility-for"></a>

[bool](class_bool.md#class-bool) **get_visibility_for**(peer: [int](class_int.md#class-int)) const [🔗](class_multiplayersynchronizer.md#class-multiplayersynchronizer-method-get-visibility-for)

Queries the current visibility for peer `peer`.

---


<a id="class-multiplayersynchronizer-method-remove-visibility-filter"></a>

void **remove_visibility_filter**(filter: [Callable](class_callable.md#class-callable)) [🔗](class_multiplayersynchronizer.md#class-multiplayersynchronizer-method-remove-visibility-filter)

Removes a peer visibility filter from this synchronizer.

---


<a id="class-multiplayersynchronizer-method-set-visibility-for"></a>

void **set_visibility_for**(peer: [int](class_int.md#class-int), visible: [bool](class_bool.md#class-bool)) [🔗](class_multiplayersynchronizer.md#class-multiplayersynchronizer-method-set-visibility-for)

Sets the visibility of `peer` to `visible`. If `peer` is `0`, the value of [public_visibility](class_multiplayersynchronizer.md#class-multiplayersynchronizer-property-public-visibility) will be updated instead.

---


<a id="class-multiplayersynchronizer-method-update-visibility"></a>

void **update_visibility**(for_peer: [int](class_int.md#class-int) = 0) [🔗](class_multiplayersynchronizer.md#class-multiplayersynchronizer-method-update-visibility)

Updates the visibility of `for_peer` according to visibility filters. If `for_peer` is `0` (the default), all peers' visibilties are updated.
