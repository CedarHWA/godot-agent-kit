> Source: https://docs.godotengine.org/en/4.7/classes/class_timer.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="timer"></a>

<a id="class-timer"></a>

# Timer

**Inherits:** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A countdown timer.

<a id="description"></a>

## Description

The **Timer** node is a countdown timer and is the simplest way to handle time-based logic in the engine. When a timer reaches the end of its [wait_time](class_timer.md#class-timer-property-wait-time), it will emit the [timeout](class_timer.md#class-timer-signal-timeout) signal.

After a timer enters the scene tree, it can be manually started with [start()](class_timer.md#class-timer-method-start). A timer node is also started automatically if [autostart](class_timer.md#class-timer-property-autostart) is `true`.

Without requiring much code, a timer node can be added and configured in the editor. The [timeout](class_timer.md#class-timer-signal-timeout) signal it emits can also be connected through the Signals dock in the editor:

```gdscript
func _on_timer_timeout():
    print("Time to attack!")
```

**Note:** To create a one-shot timer without instantiating a node, use [SceneTree.create_timer()](class_scenetree.md#class-scenetree-method-create-timer).

**Note:** Timers are affected by [Engine.time_scale](class_engine.md#class-engine-property-time-scale) unless [ignore_time_scale](class_timer.md#class-timer-property-ignore-time-scale) is `true`. The higher the time scale, the sooner timers will end. How often a timer processes may depend on the framerate or [Engine.physics_ticks_per_second](class_engine.md#class-engine-property-physics-ticks-per-second).

<a id="tutorials"></a>

## Tutorials

- [2D Dodge The Creeps Demo](https://godotengine.org/asset-library/asset/2712)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [autostart](class_timer.md#class-timer-property-autostart) | `false` |
| [bool](class_bool.md#class-bool) | [ignore_time_scale](class_timer.md#class-timer-property-ignore-time-scale) | `false` |
| [bool](class_bool.md#class-bool) | [one_shot](class_timer.md#class-timer-property-one-shot) | `false` |
| [bool](class_bool.md#class-bool) | [paused](class_timer.md#class-timer-property-paused) |  |
| [TimerProcessCallback](class_timer.md#enum-timer-timerprocesscallback) | [process_callback](class_timer.md#class-timer-property-process-callback) | `1` |
| [float](class_float.md#class-float) | [time_left](class_timer.md#class-timer-property-time-left) |  |
| [float](class_float.md#class-float) | [wait_time](class_timer.md#class-timer-property-wait-time) | `1.0` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [is_stopped](class_timer.md#class-timer-method-is-stopped)() const |
| void | [start](class_timer.md#class-timer-method-start)(time_sec: [float](class_float.md#class-float) = -1) |
| void | [stop](class_timer.md#class-timer-method-stop)() |

---


<a id="signals"></a>

## Signals

<a id="class-timer-signal-timeout"></a>

**timeout**() [🔗](class_timer.md#class-timer-signal-timeout)

Emitted when the timer reaches the end.

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-timer-timerprocesscallback"></a>

enum **TimerProcessCallback**: [🔗](class_timer.md#enum-timer-timerprocesscallback)

<a id="class-timer-constant-timer-process-physics"></a>

[TimerProcessCallback](class_timer.md#enum-timer-timerprocesscallback) **TIMER_PROCESS_PHYSICS** = `0`

Update the timer every physics process frame (see [Node.NOTIFICATION_INTERNAL_PHYSICS_PROCESS](class_node.md#class-node-constant-notification-internal-physics-process)).

<a id="class-timer-constant-timer-process-idle"></a>

[TimerProcessCallback](class_timer.md#enum-timer-timerprocesscallback) **TIMER_PROCESS_IDLE** = `1`

Update the timer every process (rendered) frame (see [Node.NOTIFICATION_INTERNAL_PROCESS](class_node.md#class-node-constant-notification-internal-process)).

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-timer-property-autostart"></a>

[bool](class_bool.md#class-bool) **autostart** = `false` [🔗](class_timer.md#class-timer-property-autostart)

- void **set_autostart**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **has_autostart**()

If `true`, the timer will start immediately when it enters the scene tree.

**Note:** After the timer enters the tree, this property is automatically set to `false`.

**Note:** This property does nothing when the timer is running in the editor.

---


<a id="class-timer-property-ignore-time-scale"></a>

[bool](class_bool.md#class-bool) **ignore_time_scale** = `false` [🔗](class_timer.md#class-timer-property-ignore-time-scale)

- void **set_ignore_time_scale**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_ignoring_time_scale**()

If `true`, the timer will ignore [Engine.time_scale](class_engine.md#class-engine-property-time-scale) and update with the real, elapsed time.

---


<a id="class-timer-property-one-shot"></a>

[bool](class_bool.md#class-bool) **one_shot** = `false` [🔗](class_timer.md#class-timer-property-one-shot)

- void **set_one_shot**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_one_shot**()

If `true`, the timer will stop after reaching the end. Otherwise, as by default, the timer will automatically restart.

---


<a id="class-timer-property-paused"></a>

[bool](class_bool.md#class-bool) **paused** [🔗](class_timer.md#class-timer-property-paused)

- void **set_paused**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_paused**()

If `true`, the timer is paused. A paused timer does not process until this property is set back to `false`, even when [start()](class_timer.md#class-timer-method-start) is called. See also [stop()](class_timer.md#class-timer-method-stop).

---


<a id="class-timer-property-process-callback"></a>

[TimerProcessCallback](class_timer.md#enum-timer-timerprocesscallback) **process_callback** = `1` [🔗](class_timer.md#class-timer-property-process-callback)

- void **set_timer_process_callback**(value: [TimerProcessCallback](class_timer.md#enum-timer-timerprocesscallback))
- [TimerProcessCallback](class_timer.md#enum-timer-timerprocesscallback) **get_timer_process_callback**()

Specifies when the timer is updated during the main loop.

---


<a id="class-timer-property-time-left"></a>

[float](class_float.md#class-float) **time_left** [🔗](class_timer.md#class-timer-property-time-left)

- [float](class_float.md#class-float) **get_time_left**()

The timer's remaining time in seconds. This is always `0` if the timer is stopped.

**Note:** This property is read-only and cannot be modified. It is based on [wait_time](class_timer.md#class-timer-property-wait-time).

---


<a id="class-timer-property-wait-time"></a>

[float](class_float.md#class-float) **wait_time** = `1.0` [🔗](class_timer.md#class-timer-property-wait-time)

- void **set_wait_time**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_wait_time**()

The time required for the timer to end, in seconds. This property can also be set every time [start()](class_timer.md#class-timer-method-start) is called.

**Note:** Timers can only process once per physics or process frame (depending on the [process_callback](class_timer.md#class-timer-property-process-callback)). An unstable framerate may cause the timer to end inconsistently, which is especially noticeable if the wait time is lower than roughly `0.05` seconds. For very short timers, it is recommended to write your own code instead of using a **Timer** node. Timers are also affected by [Engine.time_scale](class_engine.md#class-engine-property-time-scale).

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-timer-method-is-stopped"></a>

[bool](class_bool.md#class-bool) **is_stopped**() const [🔗](class_timer.md#class-timer-method-is-stopped)

Returns `true` if the timer is stopped or has not started.

---


<a id="class-timer-method-start"></a>

void **start**(time_sec: [float](class_float.md#class-float) = -1) [🔗](class_timer.md#class-timer-method-start)

Starts the timer, or resets the timer if it was started already. Fails if the timer is not inside the scene tree. If `time_sec` is greater than `0`, this value is used for the [wait_time](class_timer.md#class-timer-property-wait-time).

**Note:** This method does not resume a paused timer. See [paused](class_timer.md#class-timer-property-paused).

---


<a id="class-timer-method-stop"></a>

void **stop**() [🔗](class_timer.md#class-timer-method-stop)

Stops the timer. See also [paused](class_timer.md#class-timer-property-paused). Unlike [start()](class_timer.md#class-timer-method-start), this can safely be called if the timer is not inside the scene tree.

**Note:** Calling [stop()](class_timer.md#class-timer-method-stop) does not emit the [timeout](class_timer.md#class-timer-signal-timeout) signal, as the timer is not considered to have timed out. If this is desired, use `$Timer.timeout.emit()` after calling [stop()](class_timer.md#class-timer-method-stop) to manually emit the signal.
