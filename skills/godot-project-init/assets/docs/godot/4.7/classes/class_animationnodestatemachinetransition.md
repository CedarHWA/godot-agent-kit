> Source: https://docs.godotengine.org/en/4.7/classes/class_animationnodestatemachinetransition.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="animationnodestatemachinetransition"></a>

<a id="class-animationnodestatemachinetransition"></a>

# AnimationNodeStateMachineTransition

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A transition within an [AnimationNodeStateMachine](class_animationnodestatemachine.md#class-animationnodestatemachine) connecting two [AnimationRootNode](class_animationrootnode.md#class-animationrootnode)s.

<a id="description"></a>

## Description

The path generated when using [AnimationNodeStateMachinePlayback.travel()](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-method-travel) is limited to the nodes connected by **AnimationNodeStateMachineTransition**.

You can set the timing and conditions of the transition in detail.

<a id="tutorials"></a>

## Tutorials

- [Using AnimationTree](../tutorials/animation/animation_tree.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [StringName](class_stringname.md#class-stringname) | [advance_condition](class_animationnodestatemachinetransition.md#class-animationnodestatemachinetransition-property-advance-condition) | `&""` |
| [String](class_string.md#class-string) | [advance_expression](class_animationnodestatemachinetransition.md#class-animationnodestatemachinetransition-property-advance-expression) | `""` |
| [AdvanceMode](class_animationnodestatemachinetransition.md#enum-animationnodestatemachinetransition-advancemode) | [advance_mode](class_animationnodestatemachinetransition.md#class-animationnodestatemachinetransition-property-advance-mode) | `1` |
| [bool](class_bool.md#class-bool) | [break_loop_at_end](class_animationnodestatemachinetransition.md#class-animationnodestatemachinetransition-property-break-loop-at-end) | `false` |
| [int](class_int.md#class-int) | [priority](class_animationnodestatemachinetransition.md#class-animationnodestatemachinetransition-property-priority) | `1` |
| [bool](class_bool.md#class-bool) | [reset](class_animationnodestatemachinetransition.md#class-animationnodestatemachinetransition-property-reset) | `true` |
| [SwitchMode](class_animationnodestatemachinetransition.md#enum-animationnodestatemachinetransition-switchmode) | [switch_mode](class_animationnodestatemachinetransition.md#class-animationnodestatemachinetransition-property-switch-mode) | `0` |
| [Curve](class_curve.md#class-curve) | [xfade_curve](class_animationnodestatemachinetransition.md#class-animationnodestatemachinetransition-property-xfade-curve) |  |
| [float](class_float.md#class-float) | [xfade_time](class_animationnodestatemachinetransition.md#class-animationnodestatemachinetransition-property-xfade-time) | `0.0` |

---


<a id="signals"></a>

## Signals

<a id="class-animationnodestatemachinetransition-signal-advance-condition-changed"></a>

**advance_condition_changed**() [🔗](class_animationnodestatemachinetransition.md#class-animationnodestatemachinetransition-signal-advance-condition-changed)

Emitted when [advance_condition](class_animationnodestatemachinetransition.md#class-animationnodestatemachinetransition-property-advance-condition) is changed.

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-animationnodestatemachinetransition-switchmode"></a>

enum **SwitchMode**: [🔗](class_animationnodestatemachinetransition.md#enum-animationnodestatemachinetransition-switchmode)

<a id="class-animationnodestatemachinetransition-constant-switch-mode-immediate"></a>

[SwitchMode](class_animationnodestatemachinetransition.md#enum-animationnodestatemachinetransition-switchmode) **SWITCH_MODE_IMMEDIATE** = `0`

Switch to the next state immediately. The current state will end and blend into the beginning of the new one.

<a id="class-animationnodestatemachinetransition-constant-switch-mode-sync"></a>

[SwitchMode](class_animationnodestatemachinetransition.md#enum-animationnodestatemachinetransition-switchmode) **SWITCH_MODE_SYNC** = `1`

Switch to the next state immediately, but will seek the new state to the playback position of the old state.

<a id="class-animationnodestatemachinetransition-constant-switch-mode-at-end"></a>

[SwitchMode](class_animationnodestatemachinetransition.md#enum-animationnodestatemachinetransition-switchmode) **SWITCH_MODE_AT_END** = `2`

Wait for the current state playback to end, then switch to the beginning of the next state animation.

---


<a id="enum-animationnodestatemachinetransition-advancemode"></a>

enum **AdvanceMode**: [🔗](class_animationnodestatemachinetransition.md#enum-animationnodestatemachinetransition-advancemode)

<a id="class-animationnodestatemachinetransition-constant-advance-mode-disabled"></a>

[AdvanceMode](class_animationnodestatemachinetransition.md#enum-animationnodestatemachinetransition-advancemode) **ADVANCE_MODE_DISABLED** = `0`

Don't use this transition.

<a id="class-animationnodestatemachinetransition-constant-advance-mode-enabled"></a>

[AdvanceMode](class_animationnodestatemachinetransition.md#enum-animationnodestatemachinetransition-advancemode) **ADVANCE_MODE_ENABLED** = `1`

Only use this transition during [AnimationNodeStateMachinePlayback.travel()](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-method-travel).

<a id="class-animationnodestatemachinetransition-constant-advance-mode-auto"></a>

[AdvanceMode](class_animationnodestatemachinetransition.md#enum-animationnodestatemachinetransition-advancemode) **ADVANCE_MODE_AUTO** = `2`

Automatically use this transition if the [advance_condition](class_animationnodestatemachinetransition.md#class-animationnodestatemachinetransition-property-advance-condition) and [advance_expression](class_animationnodestatemachinetransition.md#class-animationnodestatemachinetransition-property-advance-expression) checks are `true` (if assigned).

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-animationnodestatemachinetransition-property-advance-condition"></a>

[StringName](class_stringname.md#class-stringname) **advance_condition** = `&""` [🔗](class_animationnodestatemachinetransition.md#class-animationnodestatemachinetransition-property-advance-condition)

- void **set_advance_condition**(value: [StringName](class_stringname.md#class-stringname))
- [StringName](class_stringname.md#class-stringname) **get_advance_condition**()

Turn on auto advance when this condition is set. The provided name will become a boolean parameter on the [AnimationTree](class_animationtree.md#class-animationtree) that can be controlled from code (see [Using AnimationTree](../tutorials/animation/animation_tree.md#controlling-from-code)). For example, if [AnimationTree.tree_root](class_animationtree.md#class-animationtree-property-tree-root) is an [AnimationNodeStateMachine](class_animationnodestatemachine.md#class-animationnodestatemachine) and [advance_condition](class_animationnodestatemachinetransition.md#class-animationnodestatemachinetransition-property-advance-condition) is set to `"idle"`:

```gdscript
$animation_tree.set("parameters/conditions/idle", is_on_floor and (linear_velocity.x == 0))
```

```csharp
GetNode<AnimationTree>("animation_tree").Set("parameters/conditions/idle", IsOnFloor && (LinearVelocity.X == 0));
```

---


<a id="class-animationnodestatemachinetransition-property-advance-expression"></a>

[String](class_string.md#class-string) **advance_expression** = `""` [🔗](class_animationnodestatemachinetransition.md#class-animationnodestatemachinetransition-property-advance-expression)

- void **set_advance_expression**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_advance_expression**()

Use an expression as a condition for state machine transitions. It is possible to create complex animation advance conditions for switching between states and gives much greater flexibility for creating complex state machines by directly interfacing with the script code.

---


<a id="class-animationnodestatemachinetransition-property-advance-mode"></a>

[AdvanceMode](class_animationnodestatemachinetransition.md#enum-animationnodestatemachinetransition-advancemode) **advance_mode** = `1` [🔗](class_animationnodestatemachinetransition.md#class-animationnodestatemachinetransition-property-advance-mode)

- void **set_advance_mode**(value: [AdvanceMode](class_animationnodestatemachinetransition.md#enum-animationnodestatemachinetransition-advancemode))
- [AdvanceMode](class_animationnodestatemachinetransition.md#enum-animationnodestatemachinetransition-advancemode) **get_advance_mode**()

Determines whether the transition should be disabled, enabled when using [AnimationNodeStateMachinePlayback.travel()](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-method-travel), or traversed automatically if the [advance_condition](class_animationnodestatemachinetransition.md#class-animationnodestatemachinetransition-property-advance-condition) and [advance_expression](class_animationnodestatemachinetransition.md#class-animationnodestatemachinetransition-property-advance-expression) checks are `true` (if assigned).

---


<a id="class-animationnodestatemachinetransition-property-break-loop-at-end"></a>

[bool](class_bool.md#class-bool) **break_loop_at_end** = `false` [🔗](class_animationnodestatemachinetransition.md#class-animationnodestatemachinetransition-property-break-loop-at-end)

- void **set_break_loop_at_end**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_loop_broken_at_end**()

If `true`, breaks the loop at the end of the loop cycle for transition, even if the animation is looping.

---


<a id="class-animationnodestatemachinetransition-property-priority"></a>

[int](class_int.md#class-int) **priority** = `1` [🔗](class_animationnodestatemachinetransition.md#class-animationnodestatemachinetransition-property-priority)

- void **set_priority**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_priority**()

Lower priority transitions are preferred when travelling through the tree via [AnimationNodeStateMachinePlayback.travel()](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-method-travel) or [advance_mode](class_animationnodestatemachinetransition.md#class-animationnodestatemachinetransition-property-advance-mode) is set to [ADVANCE_MODE_AUTO](class_animationnodestatemachinetransition.md#class-animationnodestatemachinetransition-constant-advance-mode-auto).

---


<a id="class-animationnodestatemachinetransition-property-reset"></a>

[bool](class_bool.md#class-bool) **reset** = `true` [🔗](class_animationnodestatemachinetransition.md#class-animationnodestatemachinetransition-property-reset)

- void **set_reset**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_reset**()

If `true`, the destination animation is played back from the beginning when switched.

---


<a id="class-animationnodestatemachinetransition-property-switch-mode"></a>

[SwitchMode](class_animationnodestatemachinetransition.md#enum-animationnodestatemachinetransition-switchmode) **switch_mode** = `0` [🔗](class_animationnodestatemachinetransition.md#class-animationnodestatemachinetransition-property-switch-mode)

- void **set_switch_mode**(value: [SwitchMode](class_animationnodestatemachinetransition.md#enum-animationnodestatemachinetransition-switchmode))
- [SwitchMode](class_animationnodestatemachinetransition.md#enum-animationnodestatemachinetransition-switchmode) **get_switch_mode**()

The transition type.

---


<a id="class-animationnodestatemachinetransition-property-xfade-curve"></a>

[Curve](class_curve.md#class-curve) **xfade_curve** [🔗](class_animationnodestatemachinetransition.md#class-animationnodestatemachinetransition-property-xfade-curve)

- void **set_xfade_curve**(value: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_xfade_curve**()

Ease curve for better control over cross-fade between this state and the next. Should be a unit [Curve](class_curve.md#class-curve).

---


<a id="class-animationnodestatemachinetransition-property-xfade-time"></a>

[float](class_float.md#class-float) **xfade_time** = `0.0` [🔗](class_animationnodestatemachinetransition.md#class-animationnodestatemachinetransition-property-xfade-time)

- void **set_xfade_time**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_xfade_time**()

The time to cross-fade between this state and the next.

**Note:** [AnimationNodeStateMachine](class_animationnodestatemachine.md#class-animationnodestatemachine) transitions the current state immediately after the start of the fading. The precise remaining time can only be inferred from the main animation. When [AnimationNodeOutput](class_animationnodeoutput.md#class-animationnodeoutput) is considered as the most upstream, so the [xfade_time](class_animationnodestatemachinetransition.md#class-animationnodestatemachinetransition-property-xfade-time) is not scaled depending on the downstream delta. See also [AnimationNodeOneShot.fadeout_time](class_animationnodeoneshot.md#class-animationnodeoneshot-property-fadeout-time).
