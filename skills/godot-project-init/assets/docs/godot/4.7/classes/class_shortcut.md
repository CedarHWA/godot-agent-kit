> Source: https://docs.godotengine.org/en/4.7/classes/class_shortcut.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="shortcut"></a>

<a id="class-shortcut"></a>

# Shortcut

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A shortcut for binding input.

<a id="description"></a>

## Description

Shortcuts (also known as hotkeys) are containers of [InputEvent](class_inputevent.md#class-inputevent) resources. They are commonly used to interact with a [Control](class_control.md#class-control) element from an [InputEvent](class_inputevent.md#class-inputevent).

One shortcut can contain multiple [InputEvent](class_inputevent.md#class-inputevent) resources, making it possible to trigger one action with multiple different inputs.

**Example:** Capture the `Ctrl + S` shortcut using a **Shortcut** resource:

```gdscript
extends Node

var save_shortcut = Shortcut.new()
func _ready():
    var key_event = InputEventKey.new()
    key_event.keycode = KEY_S
    key_event.ctrl_pressed = true
    key_event.command_or_control_autoremap = true # Swaps Ctrl for Command on Mac.
    save_shortcut.events = [key_event]

func _input(event):
    if save_shortcut.matches_event(event) and event.is_pressed() and not event.is_echo():
        print("Save shortcut pressed!")
        get_viewport().set_input_as_handled()
```

```csharp
using Godot;

public partial class MyNode : Node
{
    private readonly Shortcut _saveShortcut = new Shortcut();

    public override void _Ready()
    {
        InputEventKey keyEvent = new InputEventKey
        {
            Keycode = Key.S,
            CtrlPressed = true,
            CommandOrControlAutoremap = true, // Swaps Ctrl for Command on Mac.
        };

        _saveShortcut.Events = [keyEvent];
    }

    public override void _Input(InputEvent @event)
    {
        if (@event is InputEventKey keyEvent &&
            _saveShortcut.MatchesEvent(@event) &&
            keyEvent.Pressed && !keyEvent.Echo)
        {
            GD.Print("Save shortcut pressed!");
            GetViewport().SetInputAsHandled();
        }
    }
}
```

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Array](class_array.md#class-array) | [events](class_shortcut.md#class-shortcut-property-events) | `[]` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [String](class_string.md#class-string) | [get_as_text](class_shortcut.md#class-shortcut-method-get-as-text)() const |
| [bool](class_bool.md#class-bool) | [has_valid_event](class_shortcut.md#class-shortcut-method-has-valid-event)() const |
| [bool](class_bool.md#class-bool) | [matches_event](class_shortcut.md#class-shortcut-method-matches-event)(event: [InputEvent](class_inputevent.md#class-inputevent)) const |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-shortcut-property-events"></a>

[Array](class_array.md#class-array) **events** = `[]` [🔗](class_shortcut.md#class-shortcut-property-events)

- void **set_events**(value: [Array](class_array.md#class-array))
- [Array](class_array.md#class-array) **get_events**()

The shortcut's [InputEvent](class_inputevent.md#class-inputevent) array.

Generally the [InputEvent](class_inputevent.md#class-inputevent) used is an [InputEventKey](class_inputeventkey.md#class-inputeventkey), though it can be any [InputEvent](class_inputevent.md#class-inputevent), including an [InputEventAction](class_inputeventaction.md#class-inputeventaction).

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-shortcut-method-get-as-text"></a>

[String](class_string.md#class-string) **get_as_text**() const [🔗](class_shortcut.md#class-shortcut-method-get-as-text)

Returns the shortcut's first valid [InputEvent](class_inputevent.md#class-inputevent) as a [String](class_string.md#class-string).

---


<a id="class-shortcut-method-has-valid-event"></a>

[bool](class_bool.md#class-bool) **has_valid_event**() const [🔗](class_shortcut.md#class-shortcut-method-has-valid-event)

Returns whether [events](class_shortcut.md#class-shortcut-property-events) contains an [InputEvent](class_inputevent.md#class-inputevent) which is valid.

---


<a id="class-shortcut-method-matches-event"></a>

[bool](class_bool.md#class-bool) **matches_event**(event: [InputEvent](class_inputevent.md#class-inputevent)) const [🔗](class_shortcut.md#class-shortcut-method-matches-event)

Returns whether any [InputEvent](class_inputevent.md#class-inputevent) in [events](class_shortcut.md#class-shortcut-property-events) equals `event`. This uses [InputEvent.is_match()](class_inputevent.md#class-inputevent-method-is-match) to compare events.
