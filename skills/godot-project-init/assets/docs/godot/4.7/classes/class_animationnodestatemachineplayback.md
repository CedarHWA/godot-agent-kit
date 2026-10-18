> Source: https://docs.godotengine.org/en/4.7/classes/class_animationnodestatemachineplayback.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="animationnodestatemachineplayback"></a>

<a id="class-animationnodestatemachineplayback"></a>

# AnimationNodeStateMachinePlayback

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Provides playback control for an [AnimationNodeStateMachine](class_animationnodestatemachine.md#class-animationnodestatemachine).

<a id="description"></a>

## Description

Allows control of [AnimationTree](class_animationtree.md#class-animationtree) state machines created with [AnimationNodeStateMachine](class_animationnodestatemachine.md#class-animationnodestatemachine). Retrieve with `$AnimationTree.get("parameters/playback")`.

```gdscript
var state_machine = $AnimationTree.get("parameters/playback")
state_machine.travel("some_state")
```

```csharp
var stateMachine = GetNode<AnimationTree>("AnimationTree").Get("parameters/playback").As<AnimationNodeStateMachinePlayback>();
stateMachine.Travel("some_state");
```

<a id="tutorials"></a>

## Tutorials

- [Using AnimationTree](../tutorials/animation/animation_tree.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | resource_local_to_scene | `true` (overrides [Resource](class_resource.md#class-resource-property-resource-local-to-scene)) |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [float](class_float.md#class-float) | [get_current_length](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-method-get-current-length)() const |
| [StringName](class_stringname.md#class-stringname) | [get_current_node](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-method-get-current-node)() const |
| [float](class_float.md#class-float) | [get_current_play_position](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-method-get-current-play-position)() const |
| [float](class_float.md#class-float) | [get_fading_from_length](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-method-get-fading-from-length)() const |
| [StringName](class_stringname.md#class-stringname) | [get_fading_from_node](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-method-get-fading-from-node)() const |
| [float](class_float.md#class-float) | [get_fading_from_play_position](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-method-get-fading-from-play-position)() const |
| [float](class_float.md#class-float) | [get_fading_length](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-method-get-fading-length)() const |
| [float](class_float.md#class-float) | [get_fading_position](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-method-get-fading-position)() const |
| [Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] | [get_travel_path](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-method-get-travel-path)() const |
| [bool](class_bool.md#class-bool) | [is_playing](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-method-is-playing)() const |
| void | [next](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-method-next)() |
| void | [start](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-method-start)(node: [StringName](class_stringname.md#class-stringname), reset: [bool](class_bool.md#class-bool) = true) |
| void | [stop](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-method-stop)() |
| void | [travel](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-method-travel)(to_node: [StringName](class_stringname.md#class-stringname), reset_on_teleport: [bool](class_bool.md#class-bool) = true) |

---


<a id="signals"></a>

## Signals

<a id="class-animationnodestatemachineplayback-signal-state-finished"></a>

**state_finished**(state: [StringName](class_stringname.md#class-stringname)) [🔗](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-signal-state-finished)

Emitted when the `state` finishes playback. If `state` is a state machine set to grouped mode, its signals are passed through with its name prefixed.

If there is a crossfade, this will be fired when the influence of the [get_fading_from_node()](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-method-get-fading-from-node) animation is no longer present.

---


<a id="class-animationnodestatemachineplayback-signal-state-started"></a>

**state_started**(state: [StringName](class_stringname.md#class-stringname)) [🔗](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-signal-state-started)

Emitted when the `state` starts playback. If `state` is a state machine set to grouped mode, its signals are passed through with its name prefixed.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-animationnodestatemachineplayback-method-get-current-length"></a>

[float](class_float.md#class-float) **get_current_length**() const [🔗](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-method-get-current-length)

Returns the current state length.

**Note:** It is possible that any [AnimationRootNode](class_animationrootnode.md#class-animationrootnode) can be nodes as well as animations. This means that there can be multiple animations within a single state. Which animation length has priority depends on the nodes connected inside it. Also, if a transition does not reset, the remaining length at that point will be returned.

---


<a id="class-animationnodestatemachineplayback-method-get-current-node"></a>

[StringName](class_stringname.md#class-stringname) **get_current_node**() const [🔗](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-method-get-current-node)

Returns the currently playing animation state.

**Note:** When using a cross-fade, the current state changes to the next state immediately after the cross-fade begins.

---


<a id="class-animationnodestatemachineplayback-method-get-current-play-position"></a>

[float](class_float.md#class-float) **get_current_play_position**() const [🔗](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-method-get-current-play-position)

Returns the playback position within the current animation state.

---


<a id="class-animationnodestatemachineplayback-method-get-fading-from-length"></a>

[float](class_float.md#class-float) **get_fading_from_length**() const [🔗](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-method-get-fading-from-length)

Returns the playback state length of the node from [get_fading_from_node()](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-method-get-fading-from-node). Returns `0` if no animation fade is occurring.

---


<a id="class-animationnodestatemachineplayback-method-get-fading-from-node"></a>

[StringName](class_stringname.md#class-stringname) **get_fading_from_node**() const [🔗](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-method-get-fading-from-node)

Returns the starting state of currently fading animation.

---


<a id="class-animationnodestatemachineplayback-method-get-fading-from-play-position"></a>

[float](class_float.md#class-float) **get_fading_from_play_position**() const [🔗](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-method-get-fading-from-play-position)

Returns the playback position of the node from [get_fading_from_node()](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-method-get-fading-from-node). Returns `0` if no animation fade is occurring.

---


<a id="class-animationnodestatemachineplayback-method-get-fading-length"></a>

[float](class_float.md#class-float) **get_fading_length**() const [🔗](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-method-get-fading-length)

Returns the length of the current fade animation. Returns `0` if no animation fade is occurring.

---


<a id="class-animationnodestatemachineplayback-method-get-fading-position"></a>

[float](class_float.md#class-float) **get_fading_position**() const [🔗](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-method-get-fading-position)

Returns the playback position of the current fade animation. Returns `0` if no animation fade is occurring.

---


<a id="class-animationnodestatemachineplayback-method-get-travel-path"></a>

[Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] **get_travel_path**() const [🔗](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-method-get-travel-path)

Returns the current travel path as computed internally by the A\* algorithm.

---


<a id="class-animationnodestatemachineplayback-method-is-playing"></a>

[bool](class_bool.md#class-bool) **is_playing**() const [🔗](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-method-is-playing)

Returns `true` if an animation is playing.

---


<a id="class-animationnodestatemachineplayback-method-next"></a>

void **next**() [🔗](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-method-next)

If there is a next path by travel or auto advance, immediately transitions from the current state to the next state.

---


<a id="class-animationnodestatemachineplayback-method-start"></a>

void **start**(node: [StringName](class_stringname.md#class-stringname), reset: [bool](class_bool.md#class-bool) = true) [🔗](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-method-start)

Starts playing the given animation.

If `reset` is `true`, the animation is played from the beginning.

---


<a id="class-animationnodestatemachineplayback-method-stop"></a>

void **stop**() [🔗](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-method-stop)

Stops the currently playing animation.

---


<a id="class-animationnodestatemachineplayback-method-travel"></a>

void **travel**(to_node: [StringName](class_stringname.md#class-stringname), reset_on_teleport: [bool](class_bool.md#class-bool) = true) [🔗](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-method-travel)

Transitions from the current state to another one, following the shortest path.

If the path does not connect from the current state, the animation will play after the state teleports.

If `reset_on_teleport` is `true`, the animation is played from the beginning when the travel cause a teleportation.
