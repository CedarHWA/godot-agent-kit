> Source: https://docs.godotengine.org/en/4.7/classes/class_animationnodestatemachine.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="animationnodestatemachine"></a>

<a id="class-animationnodestatemachine"></a>

# AnimationNodeStateMachine

**Inherits:** [AnimationRootNode](class_animationrootnode.md#class-animationrootnode) **<** [AnimationNode](class_animationnode.md#class-animationnode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A state machine with multiple [AnimationRootNode](class_animationrootnode.md#class-animationrootnode)s, used by [AnimationTree](class_animationtree.md#class-animationtree).

<a id="description"></a>

## Description

Contains multiple [AnimationRootNode](class_animationrootnode.md#class-animationrootnode)s representing animation states, connected in a graph. State transitions can be configured to happen automatically or via code, using a shortest-path algorithm. Retrieve the [AnimationNodeStateMachinePlayback](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback) object from the [AnimationTree](class_animationtree.md#class-animationtree) node to control it programmatically.

```gdscript
var state_machine = $AnimationTree.get("parameters/playback")
state_machine.travel("some_state")
```

```csharp
var stateMachine = GetNode<AnimationTree>("AnimationTree").Get("parameters/playback") as AnimationNodeStateMachinePlayback;
stateMachine.Travel("some_state");
```

<a id="tutorials"></a>

## Tutorials

- [Using AnimationTree](../tutorials/animation/animation_tree.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [allow_transition_to_self](class_animationnodestatemachine.md#class-animationnodestatemachine-property-allow-transition-to-self) | `false` |
| [bool](class_bool.md#class-bool) | [reset_ends](class_animationnodestatemachine.md#class-animationnodestatemachine-property-reset-ends) | `false` |
| [StateMachineType](class_animationnodestatemachine.md#enum-animationnodestatemachine-statemachinetype) | [state_machine_type](class_animationnodestatemachine.md#class-animationnodestatemachine-property-state-machine-type) | `0` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_node](class_animationnodestatemachine.md#class-animationnodestatemachine-method-add-node)(name: [StringName](class_stringname.md#class-stringname), node: [AnimationNode](class_animationnode.md#class-animationnode), position: [Vector2](class_vector2.md#class-vector2) = Vector2(0, 0)) |
| void | [add_transition](class_animationnodestatemachine.md#class-animationnodestatemachine-method-add-transition)(from: [StringName](class_stringname.md#class-stringname), to: [StringName](class_stringname.md#class-stringname), transition: [AnimationNodeStateMachineTransition](class_animationnodestatemachinetransition.md#class-animationnodestatemachinetransition)) |
| [Vector2](class_vector2.md#class-vector2) | [get_graph_offset](class_animationnodestatemachine.md#class-animationnodestatemachine-method-get-graph-offset)() const |
| [AnimationNode](class_animationnode.md#class-animationnode) | [get_node](class_animationnodestatemachine.md#class-animationnodestatemachine-method-get-node)(name: [StringName](class_stringname.md#class-stringname)) const |
| [Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] | [get_node_list](class_animationnodestatemachine.md#class-animationnodestatemachine-method-get-node-list)() const |
| [StringName](class_stringname.md#class-stringname) | [get_node_name](class_animationnodestatemachine.md#class-animationnodestatemachine-method-get-node-name)(node: [AnimationNode](class_animationnode.md#class-animationnode)) const |
| [Vector2](class_vector2.md#class-vector2) | [get_node_position](class_animationnodestatemachine.md#class-animationnodestatemachine-method-get-node-position)(name: [StringName](class_stringname.md#class-stringname)) const |
| [AnimationNodeStateMachineTransition](class_animationnodestatemachinetransition.md#class-animationnodestatemachinetransition) | [get_transition](class_animationnodestatemachine.md#class-animationnodestatemachine-method-get-transition)(idx: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_transition_count](class_animationnodestatemachine.md#class-animationnodestatemachine-method-get-transition-count)() const |
| [StringName](class_stringname.md#class-stringname) | [get_transition_from](class_animationnodestatemachine.md#class-animationnodestatemachine-method-get-transition-from)(idx: [int](class_int.md#class-int)) const |
| [StringName](class_stringname.md#class-stringname) | [get_transition_to](class_animationnodestatemachine.md#class-animationnodestatemachine-method-get-transition-to)(idx: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [has_node](class_animationnodestatemachine.md#class-animationnodestatemachine-method-has-node)(name: [StringName](class_stringname.md#class-stringname)) const |
| [bool](class_bool.md#class-bool) | [has_transition](class_animationnodestatemachine.md#class-animationnodestatemachine-method-has-transition)(from: [StringName](class_stringname.md#class-stringname), to: [StringName](class_stringname.md#class-stringname)) const |
| void | [remove_node](class_animationnodestatemachine.md#class-animationnodestatemachine-method-remove-node)(name: [StringName](class_stringname.md#class-stringname)) |
| void | [remove_transition](class_animationnodestatemachine.md#class-animationnodestatemachine-method-remove-transition)(from: [StringName](class_stringname.md#class-stringname), to: [StringName](class_stringname.md#class-stringname)) |
| void | [remove_transition_by_index](class_animationnodestatemachine.md#class-animationnodestatemachine-method-remove-transition-by-index)(idx: [int](class_int.md#class-int)) |
| void | [rename_node](class_animationnodestatemachine.md#class-animationnodestatemachine-method-rename-node)(name: [StringName](class_stringname.md#class-stringname), new_name: [StringName](class_stringname.md#class-stringname)) |
| void | [replace_node](class_animationnodestatemachine.md#class-animationnodestatemachine-method-replace-node)(name: [StringName](class_stringname.md#class-stringname), node: [AnimationNode](class_animationnode.md#class-animationnode)) |
| void | [set_graph_offset](class_animationnodestatemachine.md#class-animationnodestatemachine-method-set-graph-offset)(offset: [Vector2](class_vector2.md#class-vector2)) |
| void | [set_node_position](class_animationnodestatemachine.md#class-animationnodestatemachine-method-set-node-position)(name: [StringName](class_stringname.md#class-stringname), position: [Vector2](class_vector2.md#class-vector2)) |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-animationnodestatemachine-statemachinetype"></a>

enum **StateMachineType**: [🔗](class_animationnodestatemachine.md#enum-animationnodestatemachine-statemachinetype)

<a id="class-animationnodestatemachine-constant-state-machine-type-root"></a>

[StateMachineType](class_animationnodestatemachine.md#enum-animationnodestatemachine-statemachinetype) **STATE_MACHINE_TYPE_ROOT** = `0`

Seeking to the beginning is treated as playing from the start state. Transition to the end state is treated as exiting the state machine.

<a id="class-animationnodestatemachine-constant-state-machine-type-nested"></a>

[StateMachineType](class_animationnodestatemachine.md#enum-animationnodestatemachine-statemachinetype) **STATE_MACHINE_TYPE_NESTED** = `1`

Seeking to the beginning is treated as seeking to the beginning of the animation in the current state. Transition to the end state, or the absence of transitions in each state, is treated as exiting the state machine.

<a id="class-animationnodestatemachine-constant-state-machine-type-grouped"></a>

[StateMachineType](class_animationnodestatemachine.md#enum-animationnodestatemachine-statemachinetype) **STATE_MACHINE_TYPE_GROUPED** = `2`

This is a grouped state machine that can be controlled from a parent state machine. It does not work independently. There must be a state machine with [state_machine_type](class_animationnodestatemachine.md#class-animationnodestatemachine-property-state-machine-type) of [STATE_MACHINE_TYPE_ROOT](class_animationnodestatemachine.md#class-animationnodestatemachine-constant-state-machine-type-root) or [STATE_MACHINE_TYPE_NESTED](class_animationnodestatemachine.md#class-animationnodestatemachine-constant-state-machine-type-nested) in the parent or ancestor.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-animationnodestatemachine-property-allow-transition-to-self"></a>

[bool](class_bool.md#class-bool) **allow_transition_to_self** = `false` [🔗](class_animationnodestatemachine.md#class-animationnodestatemachine-property-allow-transition-to-self)

- void **set_allow_transition_to_self**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_allow_transition_to_self**()

If `true`, allows teleport to the self state with [AnimationNodeStateMachinePlayback.travel()](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-method-travel). When the reset option is enabled in [AnimationNodeStateMachinePlayback.travel()](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-method-travel), the animation is restarted. If `false`, nothing happens on the teleportation to the self state.

---


<a id="class-animationnodestatemachine-property-reset-ends"></a>

[bool](class_bool.md#class-bool) **reset_ends** = `false` [🔗](class_animationnodestatemachine.md#class-animationnodestatemachine-property-reset-ends)

- void **set_reset_ends**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **are_ends_reset**()

If `true`, treat the cross-fade to the start and end nodes as a blend with the RESET animation.

In most cases, when additional cross-fades are performed in the parent [AnimationNode](class_animationnode.md#class-animationnode) of the state machine, setting this property to `false` and matching the cross-fade time of the parent [AnimationNode](class_animationnode.md#class-animationnode) and the state machine's start node and end node gives good results.

---


<a id="class-animationnodestatemachine-property-state-machine-type"></a>

[StateMachineType](class_animationnodestatemachine.md#enum-animationnodestatemachine-statemachinetype) **state_machine_type** = `0` [🔗](class_animationnodestatemachine.md#class-animationnodestatemachine-property-state-machine-type)

- void **set_state_machine_type**(value: [StateMachineType](class_animationnodestatemachine.md#enum-animationnodestatemachine-statemachinetype))
- [StateMachineType](class_animationnodestatemachine.md#enum-animationnodestatemachine-statemachinetype) **get_state_machine_type**()

This property can define the process of transitions for different use cases. See also [StateMachineType](class_animationnodestatemachine.md#enum-animationnodestatemachine-statemachinetype).

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-animationnodestatemachine-method-add-node"></a>

void **add_node**(name: [StringName](class_stringname.md#class-stringname), node: [AnimationNode](class_animationnode.md#class-animationnode), position: [Vector2](class_vector2.md#class-vector2) = Vector2(0, 0)) [🔗](class_animationnodestatemachine.md#class-animationnodestatemachine-method-add-node)

Adds a new animation node to the graph. The `position` is used for display in the editor.

---


<a id="class-animationnodestatemachine-method-add-transition"></a>

void **add_transition**(from: [StringName](class_stringname.md#class-stringname), to: [StringName](class_stringname.md#class-stringname), transition: [AnimationNodeStateMachineTransition](class_animationnodestatemachinetransition.md#class-animationnodestatemachinetransition)) [🔗](class_animationnodestatemachine.md#class-animationnodestatemachine-method-add-transition)

Adds a transition between the given animation nodes.

---


<a id="class-animationnodestatemachine-method-get-graph-offset"></a>

[Vector2](class_vector2.md#class-vector2) **get_graph_offset**() const [🔗](class_animationnodestatemachine.md#class-animationnodestatemachine-method-get-graph-offset)

Returns the draw offset of the graph. Used for display in the editor.

---


<a id="class-animationnodestatemachine-method-get-node"></a>

[AnimationNode](class_animationnode.md#class-animationnode) **get_node**(name: [StringName](class_stringname.md#class-stringname)) const [🔗](class_animationnodestatemachine.md#class-animationnodestatemachine-method-get-node)

Returns the animation node with the given name.

---


<a id="class-animationnodestatemachine-method-get-node-list"></a>

[Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] **get_node_list**() const [🔗](class_animationnodestatemachine.md#class-animationnodestatemachine-method-get-node-list)

Returns a list containing the names of all animation nodes in this state machine.

---


<a id="class-animationnodestatemachine-method-get-node-name"></a>

[StringName](class_stringname.md#class-stringname) **get_node_name**(node: [AnimationNode](class_animationnode.md#class-animationnode)) const [🔗](class_animationnodestatemachine.md#class-animationnodestatemachine-method-get-node-name)

Returns the given animation node's name.

---


<a id="class-animationnodestatemachine-method-get-node-position"></a>

[Vector2](class_vector2.md#class-vector2) **get_node_position**(name: [StringName](class_stringname.md#class-stringname)) const [🔗](class_animationnodestatemachine.md#class-animationnodestatemachine-method-get-node-position)

Returns the given animation node's coordinates. Used for display in the editor.

---


<a id="class-animationnodestatemachine-method-get-transition"></a>

[AnimationNodeStateMachineTransition](class_animationnodestatemachinetransition.md#class-animationnodestatemachinetransition) **get_transition**(idx: [int](class_int.md#class-int)) const [🔗](class_animationnodestatemachine.md#class-animationnodestatemachine-method-get-transition)

Returns the given transition.

---


<a id="class-animationnodestatemachine-method-get-transition-count"></a>

[int](class_int.md#class-int) **get_transition_count**() const [🔗](class_animationnodestatemachine.md#class-animationnodestatemachine-method-get-transition-count)

Returns the number of connections in the graph.

---


<a id="class-animationnodestatemachine-method-get-transition-from"></a>

[StringName](class_stringname.md#class-stringname) **get_transition_from**(idx: [int](class_int.md#class-int)) const [🔗](class_animationnodestatemachine.md#class-animationnodestatemachine-method-get-transition-from)

Returns the given transition's start node.

---


<a id="class-animationnodestatemachine-method-get-transition-to"></a>

[StringName](class_stringname.md#class-stringname) **get_transition_to**(idx: [int](class_int.md#class-int)) const [🔗](class_animationnodestatemachine.md#class-animationnodestatemachine-method-get-transition-to)

Returns the given transition's end node.

---


<a id="class-animationnodestatemachine-method-has-node"></a>

[bool](class_bool.md#class-bool) **has_node**(name: [StringName](class_stringname.md#class-stringname)) const [🔗](class_animationnodestatemachine.md#class-animationnodestatemachine-method-has-node)

Returns `true` if the graph contains the given animation node.

---


<a id="class-animationnodestatemachine-method-has-transition"></a>

[bool](class_bool.md#class-bool) **has_transition**(from: [StringName](class_stringname.md#class-stringname), to: [StringName](class_stringname.md#class-stringname)) const [🔗](class_animationnodestatemachine.md#class-animationnodestatemachine-method-has-transition)

Returns `true` if there is a transition between the given animation nodes.

---


<a id="class-animationnodestatemachine-method-remove-node"></a>

void **remove_node**(name: [StringName](class_stringname.md#class-stringname)) [🔗](class_animationnodestatemachine.md#class-animationnodestatemachine-method-remove-node)

Deletes the given animation node from the graph.

---


<a id="class-animationnodestatemachine-method-remove-transition"></a>

void **remove_transition**(from: [StringName](class_stringname.md#class-stringname), to: [StringName](class_stringname.md#class-stringname)) [🔗](class_animationnodestatemachine.md#class-animationnodestatemachine-method-remove-transition)

Deletes the transition between the two specified animation nodes.

---


<a id="class-animationnodestatemachine-method-remove-transition-by-index"></a>

void **remove_transition_by_index**(idx: [int](class_int.md#class-int)) [🔗](class_animationnodestatemachine.md#class-animationnodestatemachine-method-remove-transition-by-index)

Deletes the given transition by index.

---


<a id="class-animationnodestatemachine-method-rename-node"></a>

void **rename_node**(name: [StringName](class_stringname.md#class-stringname), new_name: [StringName](class_stringname.md#class-stringname)) [🔗](class_animationnodestatemachine.md#class-animationnodestatemachine-method-rename-node)

Renames the given animation node.

---


<a id="class-animationnodestatemachine-method-replace-node"></a>

void **replace_node**(name: [StringName](class_stringname.md#class-stringname), node: [AnimationNode](class_animationnode.md#class-animationnode)) [🔗](class_animationnodestatemachine.md#class-animationnodestatemachine-method-replace-node)

Replaces the given animation node with a new animation node.

---


<a id="class-animationnodestatemachine-method-set-graph-offset"></a>

void **set_graph_offset**(offset: [Vector2](class_vector2.md#class-vector2)) [🔗](class_animationnodestatemachine.md#class-animationnodestatemachine-method-set-graph-offset)

Sets the draw offset of the graph. Used for display in the editor.

---


<a id="class-animationnodestatemachine-method-set-node-position"></a>

void **set_node_position**(name: [StringName](class_stringname.md#class-stringname), position: [Vector2](class_vector2.md#class-vector2)) [🔗](class_animationnodestatemachine.md#class-animationnodestatemachine-method-set-node-position)

Sets the animation node's coordinates. Used for display in the editor.
