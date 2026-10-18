> Source: https://docs.godotengine.org/en/4.7/classes/class_scenetreetimer.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="scenetreetimer"></a>

<a id="class-scenetreetimer"></a>

# SceneTreeTimer

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

One-shot timer.

<a id="description"></a>

## Description

A one-shot timer managed by the scene tree, which emits [timeout](class_scenetreetimer.md#class-scenetreetimer-signal-timeout) on completion. See also [SceneTree.create_timer()](class_scenetree.md#class-scenetree-method-create-timer).

As opposed to [Timer](class_timer.md#class-timer), it does not require the instantiation of a node. Commonly used to create a one-shot delay timer as in the following example:

```gdscript
func some_function():
    print("Timer started.")
    await get_tree().create_timer(1.0).timeout
    print("Timer ended.")
```

```csharp
public async Task SomeFunction()
{
    GD.Print("Timer started.");
    await ToSignal(GetTree().CreateTimer(1.0f), SceneTreeTimer.SignalName.Timeout);
    GD.Print("Timer ended.");
}
```

The timer will be dereferenced after its time elapses. To preserve the timer, you can keep a reference to it. See [RefCounted](class_refcounted.md#class-refcounted).

**Note:** The timer is processed after all of the nodes in the current frame, i.e. node's [Node._process()](class_node.md#class-node-private-method-process) method would be called before the timer (or [Node._physics_process()](class_node.md#class-node-private-method-physics-process) if `process_in_physics` in [SceneTree.create_timer()](class_scenetree.md#class-scenetree-method-create-timer) has been set to `true`).

<a id="properties"></a>

## Properties

|  |  |
| --- | --- |
| [float](class_float.md#class-float) | [time_left](class_scenetreetimer.md#class-scenetreetimer-property-time-left) |

---


<a id="signals"></a>

## Signals

<a id="class-scenetreetimer-signal-timeout"></a>

**timeout**() [🔗](class_scenetreetimer.md#class-scenetreetimer-signal-timeout)

Emitted when the timer reaches 0.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-scenetreetimer-property-time-left"></a>

[float](class_float.md#class-float) **time_left** [🔗](class_scenetreetimer.md#class-scenetreetimer-property-time-left)

- void **set_time_left**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_time_left**()

The time remaining (in seconds).
