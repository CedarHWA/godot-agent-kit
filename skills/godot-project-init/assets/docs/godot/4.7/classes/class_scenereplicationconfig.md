> Source: https://docs.godotengine.org/en/4.7/classes/class_scenereplicationconfig.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="scenereplicationconfig"></a>

<a id="class-scenereplicationconfig"></a>

# SceneReplicationConfig

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Configuration for properties to synchronize with a [MultiplayerSynchronizer](class_multiplayersynchronizer.md#class-multiplayersynchronizer).

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_property](class_scenereplicationconfig.md#class-scenereplicationconfig-method-add-property)(path: [NodePath](class_nodepath.md#class-nodepath), index: [int](class_int.md#class-int) = -1) |
| [Array](class_array.md#class-array)[[NodePath](class_nodepath.md#class-nodepath)] | [get_properties](class_scenereplicationconfig.md#class-scenereplicationconfig-method-get-properties)() const |
| [bool](class_bool.md#class-bool) | [has_property](class_scenereplicationconfig.md#class-scenereplicationconfig-method-has-property)(path: [NodePath](class_nodepath.md#class-nodepath)) const |
| [int](class_int.md#class-int) | [property_get_index](class_scenereplicationconfig.md#class-scenereplicationconfig-method-property-get-index)(path: [NodePath](class_nodepath.md#class-nodepath)) const |
| [ReplicationMode](class_scenereplicationconfig.md#enum-scenereplicationconfig-replicationmode) | [property_get_replication_mode](class_scenereplicationconfig.md#class-scenereplicationconfig-method-property-get-replication-mode)(path: [NodePath](class_nodepath.md#class-nodepath)) |
| [bool](class_bool.md#class-bool) | [property_get_spawn](class_scenereplicationconfig.md#class-scenereplicationconfig-method-property-get-spawn)(path: [NodePath](class_nodepath.md#class-nodepath)) |
| [bool](class_bool.md#class-bool) | [property_get_sync](class_scenereplicationconfig.md#class-scenereplicationconfig-method-property-get-sync)(path: [NodePath](class_nodepath.md#class-nodepath)) |
| [bool](class_bool.md#class-bool) | [property_get_watch](class_scenereplicationconfig.md#class-scenereplicationconfig-method-property-get-watch)(path: [NodePath](class_nodepath.md#class-nodepath)) |
| void | [property_set_replication_mode](class_scenereplicationconfig.md#class-scenereplicationconfig-method-property-set-replication-mode)(path: [NodePath](class_nodepath.md#class-nodepath), mode: [ReplicationMode](class_scenereplicationconfig.md#enum-scenereplicationconfig-replicationmode)) |
| void | [property_set_spawn](class_scenereplicationconfig.md#class-scenereplicationconfig-method-property-set-spawn)(path: [NodePath](class_nodepath.md#class-nodepath), enabled: [bool](class_bool.md#class-bool)) |
| void | [property_set_sync](class_scenereplicationconfig.md#class-scenereplicationconfig-method-property-set-sync)(path: [NodePath](class_nodepath.md#class-nodepath), enabled: [bool](class_bool.md#class-bool)) |
| void | [property_set_watch](class_scenereplicationconfig.md#class-scenereplicationconfig-method-property-set-watch)(path: [NodePath](class_nodepath.md#class-nodepath), enabled: [bool](class_bool.md#class-bool)) |
| void | [remove_property](class_scenereplicationconfig.md#class-scenereplicationconfig-method-remove-property)(path: [NodePath](class_nodepath.md#class-nodepath)) |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-scenereplicationconfig-replicationmode"></a>

enum **ReplicationMode**: [🔗](class_scenereplicationconfig.md#enum-scenereplicationconfig-replicationmode)

<a id="class-scenereplicationconfig-constant-replication-mode-never"></a>

[ReplicationMode](class_scenereplicationconfig.md#enum-scenereplicationconfig-replicationmode) **REPLICATION_MODE_NEVER** = `0`

Do not keep the given property synchronized.

<a id="class-scenereplicationconfig-constant-replication-mode-always"></a>

[ReplicationMode](class_scenereplicationconfig.md#enum-scenereplicationconfig-replicationmode) **REPLICATION_MODE_ALWAYS** = `1`

Replicate the given property on process by constantly sending updates using unreliable transfer mode.

<a id="class-scenereplicationconfig-constant-replication-mode-on-change"></a>

[ReplicationMode](class_scenereplicationconfig.md#enum-scenereplicationconfig-replicationmode) **REPLICATION_MODE_ON_CHANGE** = `2`

Replicate the given property on process by sending updates using reliable transfer mode when its value changes.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-scenereplicationconfig-method-add-property"></a>

void **add_property**(path: [NodePath](class_nodepath.md#class-nodepath), index: [int](class_int.md#class-int) = -1) [🔗](class_scenereplicationconfig.md#class-scenereplicationconfig-method-add-property)

Adds the property identified by the given `path` to the list of the properties being synchronized, optionally passing an `index`.

**Note:** For details on restrictions and limitations on property synchronization, see [MultiplayerSynchronizer](class_multiplayersynchronizer.md#class-multiplayersynchronizer).

---


<a id="class-scenereplicationconfig-method-get-properties"></a>

[Array](class_array.md#class-array)[[NodePath](class_nodepath.md#class-nodepath)] **get_properties**() const [🔗](class_scenereplicationconfig.md#class-scenereplicationconfig-method-get-properties)

Returns a list of synchronized property [NodePath](class_nodepath.md#class-nodepath)s.

---


<a id="class-scenereplicationconfig-method-has-property"></a>

[bool](class_bool.md#class-bool) **has_property**(path: [NodePath](class_nodepath.md#class-nodepath)) const [🔗](class_scenereplicationconfig.md#class-scenereplicationconfig-method-has-property)

Returns `true` if the given `path` is configured for synchronization.

---


<a id="class-scenereplicationconfig-method-property-get-index"></a>

[int](class_int.md#class-int) **property_get_index**(path: [NodePath](class_nodepath.md#class-nodepath)) const [🔗](class_scenereplicationconfig.md#class-scenereplicationconfig-method-property-get-index)

Finds the index of the given `path`.

---


<a id="class-scenereplicationconfig-method-property-get-replication-mode"></a>

[ReplicationMode](class_scenereplicationconfig.md#enum-scenereplicationconfig-replicationmode) **property_get_replication_mode**(path: [NodePath](class_nodepath.md#class-nodepath)) [🔗](class_scenereplicationconfig.md#class-scenereplicationconfig-method-property-get-replication-mode)

Returns the replication mode for the property identified by the given `path`.

---


<a id="class-scenereplicationconfig-method-property-get-spawn"></a>

[bool](class_bool.md#class-bool) **property_get_spawn**(path: [NodePath](class_nodepath.md#class-nodepath)) [🔗](class_scenereplicationconfig.md#class-scenereplicationconfig-method-property-get-spawn)

Returns `true` if the property identified by the given `path` is configured to be synchronized on spawn.

---


<a id="class-scenereplicationconfig-method-property-get-sync"></a>

[bool](class_bool.md#class-bool) **property_get_sync**(path: [NodePath](class_nodepath.md#class-nodepath)) [🔗](class_scenereplicationconfig.md#class-scenereplicationconfig-method-property-get-sync)

**Deprecated:** Use [property_get_replication_mode()](class_scenereplicationconfig.md#class-scenereplicationconfig-method-property-get-replication-mode) instead.

Returns `true` if the property identified by the given `path` is configured to be synchronized on process.

---


<a id="class-scenereplicationconfig-method-property-get-watch"></a>

[bool](class_bool.md#class-bool) **property_get_watch**(path: [NodePath](class_nodepath.md#class-nodepath)) [🔗](class_scenereplicationconfig.md#class-scenereplicationconfig-method-property-get-watch)

**Deprecated:** Use [property_get_replication_mode()](class_scenereplicationconfig.md#class-scenereplicationconfig-method-property-get-replication-mode) instead.

Returns `true` if the property identified by the given `path` is configured to be reliably synchronized when changes are detected on process.

---


<a id="class-scenereplicationconfig-method-property-set-replication-mode"></a>

void **property_set_replication_mode**(path: [NodePath](class_nodepath.md#class-nodepath), mode: [ReplicationMode](class_scenereplicationconfig.md#enum-scenereplicationconfig-replicationmode)) [🔗](class_scenereplicationconfig.md#class-scenereplicationconfig-method-property-set-replication-mode)

Sets the synchronization mode for the property identified by the given `path`.

---


<a id="class-scenereplicationconfig-method-property-set-spawn"></a>

void **property_set_spawn**(path: [NodePath](class_nodepath.md#class-nodepath), enabled: [bool](class_bool.md#class-bool)) [🔗](class_scenereplicationconfig.md#class-scenereplicationconfig-method-property-set-spawn)

Sets whether the property identified by the given `path` is configured to be synchronized on spawn.

---


<a id="class-scenereplicationconfig-method-property-set-sync"></a>

void **property_set_sync**(path: [NodePath](class_nodepath.md#class-nodepath), enabled: [bool](class_bool.md#class-bool)) [🔗](class_scenereplicationconfig.md#class-scenereplicationconfig-method-property-set-sync)

**Deprecated:** Use [property_set_replication_mode()](class_scenereplicationconfig.md#class-scenereplicationconfig-method-property-set-replication-mode) with [REPLICATION_MODE_ALWAYS](class_scenereplicationconfig.md#class-scenereplicationconfig-constant-replication-mode-always) instead.

Sets whether the property identified by the given `path` is configured to be synchronized on process.

---


<a id="class-scenereplicationconfig-method-property-set-watch"></a>

void **property_set_watch**(path: [NodePath](class_nodepath.md#class-nodepath), enabled: [bool](class_bool.md#class-bool)) [🔗](class_scenereplicationconfig.md#class-scenereplicationconfig-method-property-set-watch)

**Deprecated:** Use [property_set_replication_mode()](class_scenereplicationconfig.md#class-scenereplicationconfig-method-property-set-replication-mode) with [REPLICATION_MODE_ON_CHANGE](class_scenereplicationconfig.md#class-scenereplicationconfig-constant-replication-mode-on-change) instead.

Sets whether the property identified by the given `path` is configured to be reliably synchronized when changes are detected on process.

---


<a id="class-scenereplicationconfig-method-remove-property"></a>

void **remove_property**(path: [NodePath](class_nodepath.md#class-nodepath)) [🔗](class_scenereplicationconfig.md#class-scenereplicationconfig-method-remove-property)

Removes the property identified by the given `path` from the configuration.
