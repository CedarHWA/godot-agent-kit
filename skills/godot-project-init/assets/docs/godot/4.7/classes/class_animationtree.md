> Source: https://docs.godotengine.org/en/4.7/classes/class_animationtree.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="animationtree"></a>

<a id="class-animationtree"></a>

# AnimationTree

**Inherits:** [AnimationMixer](class_animationmixer.md#class-animationmixer) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A node used for advanced animation transitions in an [AnimationPlayer](class_animationplayer.md#class-animationplayer).

<a id="description"></a>

## Description

A node used for advanced animation transitions in an [AnimationPlayer](class_animationplayer.md#class-animationplayer).

**Note:** When linked with an [AnimationPlayer](class_animationplayer.md#class-animationplayer), several properties and methods of the corresponding [AnimationPlayer](class_animationplayer.md#class-animationplayer) will not function as expected. Playback and transitions should be handled using only the **AnimationTree** and its constituent [AnimationNode](class_animationnode.md#class-animationnode)(s). The [AnimationPlayer](class_animationplayer.md#class-animationplayer) node should be used solely for adding, deleting, and editing animations.

<a id="tutorials"></a>

## Tutorials

- [Using AnimationTree](../tutorials/animation/animation_tree.md)
- [Third Person Shooter (TPS) Demo](https://godotengine.org/asset-library/asset/2710)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [NodePath](class_nodepath.md#class-nodepath) | [advance_expression_base_node](class_animationtree.md#class-animationtree-property-advance-expression-base-node) | `NodePath(".")` |
| [NodePath](class_nodepath.md#class-nodepath) | [anim_player](class_animationtree.md#class-animationtree-property-anim-player) | `NodePath("")` |
| [AnimationCallbackModeDiscrete](class_animationmixer.md#enum-animationmixer-animationcallbackmodediscrete) | callback_mode_discrete | `2` (overrides [AnimationMixer](class_animationmixer.md#class-animationmixer-property-callback-mode-discrete)) |
| [bool](class_bool.md#class-bool) | deterministic | `true` (overrides [AnimationMixer](class_animationmixer.md#class-animationmixer-property-deterministic)) |
| [AnimationRootNode](class_animationrootnode.md#class-animationrootnode) | [tree_root](class_animationtree.md#class-animationtree-property-tree-root) |  |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [AnimationProcessCallback](class_animationtree.md#enum-animationtree-animationprocesscallback) | [get_process_callback](class_animationtree.md#class-animationtree-method-get-process-callback)() const |
| void | [set_process_callback](class_animationtree.md#class-animationtree-method-set-process-callback)(mode: [AnimationProcessCallback](class_animationtree.md#enum-animationtree-animationprocesscallback)) |

---


<a id="signals"></a>

## Signals

<a id="class-animationtree-signal-animation-player-changed"></a>

**animation_player_changed**() [🔗](class_animationtree.md#class-animationtree-signal-animation-player-changed)

Emitted when the [anim_player](class_animationtree.md#class-animationtree-property-anim-player) is changed.

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-animationtree-animationprocesscallback"></a>

enum **AnimationProcessCallback**: [🔗](class_animationtree.md#enum-animationtree-animationprocesscallback)

<a id="class-animationtree-constant-animation-process-physics"></a>

[AnimationProcessCallback](class_animationtree.md#enum-animationtree-animationprocesscallback) **ANIMATION_PROCESS_PHYSICS** = `0`

**Deprecated:** See [AnimationMixer.ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS](class_animationmixer.md#class-animationmixer-constant-animation-callback-mode-process-physics).

<a id="class-animationtree-constant-animation-process-idle"></a>

[AnimationProcessCallback](class_animationtree.md#enum-animationtree-animationprocesscallback) **ANIMATION_PROCESS_IDLE** = `1`

**Deprecated:** See [AnimationMixer.ANIMATION_CALLBACK_MODE_PROCESS_IDLE](class_animationmixer.md#class-animationmixer-constant-animation-callback-mode-process-idle).

<a id="class-animationtree-constant-animation-process-manual"></a>

[AnimationProcessCallback](class_animationtree.md#enum-animationtree-animationprocesscallback) **ANIMATION_PROCESS_MANUAL** = `2`

**Deprecated:** See [AnimationMixer.ANIMATION_CALLBACK_MODE_PROCESS_MANUAL](class_animationmixer.md#class-animationmixer-constant-animation-callback-mode-process-manual).

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-animationtree-property-advance-expression-base-node"></a>

[NodePath](class_nodepath.md#class-nodepath) **advance_expression_base_node** = `NodePath(".")` [🔗](class_animationtree.md#class-animationtree-property-advance-expression-base-node)

- void **set_advance_expression_base_node**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_advance_expression_base_node**()

The path to the [Node](class_node.md#class-node) used to evaluate the [AnimationNode](class_animationnode.md#class-animationnode) [Expression](class_expression.md#class-expression) if one is not explicitly specified internally.

---


<a id="class-animationtree-property-anim-player"></a>

[NodePath](class_nodepath.md#class-nodepath) **anim_player** = `NodePath("")` [🔗](class_animationtree.md#class-animationtree-property-anim-player)

- void **set_animation_player**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_animation_player**()

The path to the [AnimationPlayer](class_animationplayer.md#class-animationplayer) used for animating.

---


<a id="class-animationtree-property-tree-root"></a>

[AnimationRootNode](class_animationrootnode.md#class-animationrootnode) **tree_root** [🔗](class_animationtree.md#class-animationtree-property-tree-root)

- void **set_tree_root**(value: [AnimationRootNode](class_animationrootnode.md#class-animationrootnode))
- [AnimationRootNode](class_animationrootnode.md#class-animationrootnode) **get_tree_root**()

The root animation node of this **AnimationTree**. See [AnimationRootNode](class_animationrootnode.md#class-animationrootnode).

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-animationtree-method-get-process-callback"></a>

[AnimationProcessCallback](class_animationtree.md#enum-animationtree-animationprocesscallback) **get_process_callback**() const [🔗](class_animationtree.md#class-animationtree-method-get-process-callback)

**Deprecated:** Use [AnimationMixer.callback_mode_process](class_animationmixer.md#class-animationmixer-property-callback-mode-process) instead.

Returns the process notification in which to update animations.

---


<a id="class-animationtree-method-set-process-callback"></a>

void **set_process_callback**(mode: [AnimationProcessCallback](class_animationtree.md#enum-animationtree-animationprocesscallback)) [🔗](class_animationtree.md#class-animationtree-method-set-process-callback)

**Deprecated:** Use [AnimationMixer.callback_mode_process](class_animationmixer.md#class-animationmixer-property-callback-mode-process) instead.

Sets the process notification in which to update animations.
