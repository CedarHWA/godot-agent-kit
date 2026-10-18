> Source: https://docs.godotengine.org/en/4.7/classes/class_inputeventkey.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="inputeventkey"></a>

<a id="class-inputeventkey"></a>

# InputEventKey

**Inherits:** [InputEventWithModifiers](class_inputeventwithmodifiers.md#class-inputeventwithmodifiers) **<** [InputEventFromWindow](class_inputeventfromwindow.md#class-inputeventfromwindow) **<** [InputEvent](class_inputevent.md#class-inputevent) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Represents a key on a keyboard being pressed or released.

<a id="description"></a>

## Description

An input event for keys on a keyboard. Supports key presses, key releases and [echo](class_inputeventkey.md#class-inputeventkey-property-echo) events. It can also be received in [Node._unhandled_key_input()](class_node.md#class-node-private-method-unhandled-key-input).

**Note:** Events received from the keyboard usually have all properties set. Event mappings should have only one of the [keycode](class_inputeventkey.md#class-inputeventkey-property-keycode), [physical_keycode](class_inputeventkey.md#class-inputeventkey-property-physical-keycode) or [unicode](class_inputeventkey.md#class-inputeventkey-property-unicode) set.

When events are compared, properties are checked in the following priority - [keycode](class_inputeventkey.md#class-inputeventkey-property-keycode), [physical_keycode](class_inputeventkey.md#class-inputeventkey-property-physical-keycode) and [unicode](class_inputeventkey.md#class-inputeventkey-property-unicode). Events with the first matching value will be considered equal.

<a id="tutorials"></a>

## Tutorials

- [Using InputEvent](../tutorials/inputs/inputevent.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [echo](class_inputeventkey.md#class-inputeventkey-property-echo) | `false` |
| [Key](class_@globalscope.md#enum-globalscope-key) | [key_label](class_inputeventkey.md#class-inputeventkey-property-key-label) | `0` |
| [Key](class_@globalscope.md#enum-globalscope-key) | [keycode](class_inputeventkey.md#class-inputeventkey-property-keycode) | `0` |
| [KeyLocation](class_@globalscope.md#enum-globalscope-keylocation) | [location](class_inputeventkey.md#class-inputeventkey-property-location) | `0` |
| [Key](class_@globalscope.md#enum-globalscope-key) | [physical_keycode](class_inputeventkey.md#class-inputeventkey-property-physical-keycode) | `0` |
| [bool](class_bool.md#class-bool) | [pressed](class_inputeventkey.md#class-inputeventkey-property-pressed) | `false` |
| [int](class_int.md#class-int) | [unicode](class_inputeventkey.md#class-inputeventkey-property-unicode) | `0` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [String](class_string.md#class-string) | [as_text_key_label](class_inputeventkey.md#class-inputeventkey-method-as-text-key-label)() const |
| [String](class_string.md#class-string) | [as_text_keycode](class_inputeventkey.md#class-inputeventkey-method-as-text-keycode)() const |
| [String](class_string.md#class-string) | [as_text_location](class_inputeventkey.md#class-inputeventkey-method-as-text-location)() const |
| [String](class_string.md#class-string) | [as_text_physical_keycode](class_inputeventkey.md#class-inputeventkey-method-as-text-physical-keycode)() const |
| [Key](class_@globalscope.md#enum-globalscope-key) | [get_key_label_with_modifiers](class_inputeventkey.md#class-inputeventkey-method-get-key-label-with-modifiers)() const |
| [Key](class_@globalscope.md#enum-globalscope-key) | [get_keycode_with_modifiers](class_inputeventkey.md#class-inputeventkey-method-get-keycode-with-modifiers)() const |
| [Key](class_@globalscope.md#enum-globalscope-key) | [get_physical_keycode_with_modifiers](class_inputeventkey.md#class-inputeventkey-method-get-physical-keycode-with-modifiers)() const |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-inputeventkey-property-echo"></a>

[bool](class_bool.md#class-bool) **echo** = `false` [🔗](class_inputeventkey.md#class-inputeventkey-property-echo)

- void **set_echo**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_echo**()

If `true`, the key was already pressed before this event. An echo event is a repeated key event sent when the user is holding down the key.

**Note:** The rate at which echo events are sent is typically around 20 events per second (after holding down the key for roughly half a second). However, the key repeat delay/speed can be changed by the user or disabled entirely in the operating system settings. To ensure your project works correctly on all configurations, do not assume the user has a specific key repeat configuration in your project's behavior.

---


<a id="class-inputeventkey-property-key-label"></a>

[Key](class_@globalscope.md#enum-globalscope-key) **key_label** = `0` [🔗](class_inputeventkey.md#class-inputeventkey-property-key-label)

- void **set_key_label**(value: [Key](class_@globalscope.md#enum-globalscope-key))
- [Key](class_@globalscope.md#enum-globalscope-key) **get_key_label**()

Represents the localized label printed on the key in the current keyboard layout, which corresponds to one of the [Key](class_@globalscope.md#enum-globalscope-key) constants or any valid Unicode character. Key labels are meant for key prompts.

For keyboard layouts with a single label on the key, it is equivalent to [keycode](class_inputeventkey.md#class-inputeventkey-property-keycode).

To get a human-readable representation of the **InputEventKey**, use `OS.get_keycode_string(event.key_label)` where `event` is the **InputEventKey**.

```text
+-----+ +-----+
| Q   | | Q   | - "Q" - keycode
|   Й | |  ض | - "Й" and "ض" - key_label
+-----+ +-----+
```

---


<a id="class-inputeventkey-property-keycode"></a>

[Key](class_@globalscope.md#enum-globalscope-key) **keycode** = `0` [🔗](class_inputeventkey.md#class-inputeventkey-property-keycode)

- void **set_keycode**(value: [Key](class_@globalscope.md#enum-globalscope-key))
- [Key](class_@globalscope.md#enum-globalscope-key) **get_keycode**()

Latin label printed on the key in the current keyboard layout, which corresponds to one of the [Key](class_@globalscope.md#enum-globalscope-key) constants. Key codes are meant for shortcuts expressed with a standard Latin keyboard, such as `Ctrl + S` for a "Save" shortcut.

To get a human-readable representation of the **InputEventKey**, use `OS.get_keycode_string(event.keycode)` where `event` is the **InputEventKey**.

```text
+-----+ +-----+
| Q   | | Q   | - "Q" - keycode
|   Й | |  ض | - "Й" and "ض" - key_label
+-----+ +-----+
```

---


<a id="class-inputeventkey-property-location"></a>

[KeyLocation](class_@globalscope.md#enum-globalscope-keylocation) **location** = `0` [🔗](class_inputeventkey.md#class-inputeventkey-property-location)

- void **set_location**(value: [KeyLocation](class_@globalscope.md#enum-globalscope-keylocation))
- [KeyLocation](class_@globalscope.md#enum-globalscope-keylocation) **get_location**()

Represents the location of a key which has both left and right versions, such as `Shift` or `Alt`.

---


<a id="class-inputeventkey-property-physical-keycode"></a>

[Key](class_@globalscope.md#enum-globalscope-key) **physical_keycode** = `0` [🔗](class_inputeventkey.md#class-inputeventkey-property-physical-keycode)

- void **set_physical_keycode**(value: [Key](class_@globalscope.md#enum-globalscope-key))
- [Key](class_@globalscope.md#enum-globalscope-key) **get_physical_keycode**()

Represents the physical location of a key on the 101/102-key US QWERTY keyboard, which corresponds to one of the [Key](class_@globalscope.md#enum-globalscope-key) constants. Physical key codes meant for game input, such as WASD movement, where only the location of the keys is important.

To get a human-readable representation of the **InputEventKey**, use [OS.get_keycode_string()](class_os.md#class-os-method-get-keycode-string) in combination with [DisplayServer.keyboard_get_keycode_from_physical()](class_displayserver.md#class-displayserver-method-keyboard-get-keycode-from-physical) or [DisplayServer.keyboard_get_label_from_physical()](class_displayserver.md#class-displayserver-method-keyboard-get-label-from-physical):

```gdscript
func _input(event):
    if event is InputEventKey:
        var keycode = DisplayServer.keyboard_get_keycode_from_physical(event.physical_keycode)
        var label = DisplayServer.keyboard_get_label_from_physical(event.physical_keycode)
        print(OS.get_keycode_string(keycode))
        print(OS.get_keycode_string(label))
```

```csharp
public override void _Input(InputEvent @event)
{
    if (@event is InputEventKey inputEventKey)
    {
        var keycode = DisplayServer.KeyboardGetKeycodeFromPhysical(inputEventKey.PhysicalKeycode);
        var label = DisplayServer.KeyboardGetLabelFromPhysical(inputEventKey.PhysicalKeycode);
        GD.Print(OS.GetKeycodeString(keycode));
        GD.Print(OS.GetKeycodeString(label));
    }
}
```

---


<a id="class-inputeventkey-property-pressed"></a>

[bool](class_bool.md#class-bool) **pressed** = `false` [🔗](class_inputeventkey.md#class-inputeventkey-property-pressed)

- void **set_pressed**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_pressed**()

If `true`, the key's state is pressed. If `false`, the key's state is released.

---


<a id="class-inputeventkey-property-unicode"></a>

[int](class_int.md#class-int) **unicode** = `0` [🔗](class_inputeventkey.md#class-inputeventkey-property-unicode)

- void **set_unicode**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_unicode**()

The key Unicode character code (when relevant), shifted by modifier keys. Unicode character codes for composite characters and complex scripts may not be available unless IME input mode is active. See [Window.set_ime_active()](class_window.md#class-window-method-set-ime-active) for more information. Unicode character codes are meant for text input.

**Note:** This property is set by the engine only for a pressed event. If the event is sent by an IME or a virtual keyboard, no corresponding key released event is sent.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-inputeventkey-method-as-text-key-label"></a>

[String](class_string.md#class-string) **as_text_key_label**() const [🔗](class_inputeventkey.md#class-inputeventkey-method-as-text-key-label)

Returns a [String](class_string.md#class-string) representation of the event's [key_label](class_inputeventkey.md#class-inputeventkey-property-key-label) and modifiers.

---


<a id="class-inputeventkey-method-as-text-keycode"></a>

[String](class_string.md#class-string) **as_text_keycode**() const [🔗](class_inputeventkey.md#class-inputeventkey-method-as-text-keycode)

Returns a [String](class_string.md#class-string) representation of the event's [keycode](class_inputeventkey.md#class-inputeventkey-property-keycode) and modifiers.

---


<a id="class-inputeventkey-method-as-text-location"></a>

[String](class_string.md#class-string) **as_text_location**() const [🔗](class_inputeventkey.md#class-inputeventkey-method-as-text-location)

Returns a [String](class_string.md#class-string) representation of the event's [location](class_inputeventkey.md#class-inputeventkey-property-location). This will be a blank string if the event is not specific to a location.

---


<a id="class-inputeventkey-method-as-text-physical-keycode"></a>

[String](class_string.md#class-string) **as_text_physical_keycode**() const [🔗](class_inputeventkey.md#class-inputeventkey-method-as-text-physical-keycode)

Returns a [String](class_string.md#class-string) representation of the event's [physical_keycode](class_inputeventkey.md#class-inputeventkey-property-physical-keycode) and modifiers.

---


<a id="class-inputeventkey-method-get-key-label-with-modifiers"></a>

[Key](class_@globalscope.md#enum-globalscope-key) **get_key_label_with_modifiers**() const [🔗](class_inputeventkey.md#class-inputeventkey-method-get-key-label-with-modifiers)

Returns the localized key label combined with modifier keys such as `Shift` or `Alt`. See also [InputEventWithModifiers](class_inputeventwithmodifiers.md#class-inputeventwithmodifiers).

To get a human-readable representation of the **InputEventKey** with modifiers, use `OS.get_keycode_string(event.get_key_label_with_modifiers())` where `event` is the **InputEventKey**.

---


<a id="class-inputeventkey-method-get-keycode-with-modifiers"></a>

[Key](class_@globalscope.md#enum-globalscope-key) **get_keycode_with_modifiers**() const [🔗](class_inputeventkey.md#class-inputeventkey-method-get-keycode-with-modifiers)

Returns the Latin keycode combined with modifier keys such as `Shift` or `Alt`. See also [InputEventWithModifiers](class_inputeventwithmodifiers.md#class-inputeventwithmodifiers).

To get a human-readable representation of the **InputEventKey** with modifiers, use `OS.get_keycode_string(event.get_keycode_with_modifiers())` where `event` is the **InputEventKey**.

---


<a id="class-inputeventkey-method-get-physical-keycode-with-modifiers"></a>

[Key](class_@globalscope.md#enum-globalscope-key) **get_physical_keycode_with_modifiers**() const [🔗](class_inputeventkey.md#class-inputeventkey-method-get-physical-keycode-with-modifiers)

Returns the physical keycode combined with modifier keys such as `Shift` or `Alt`. See also [InputEventWithModifiers](class_inputeventwithmodifiers.md#class-inputeventwithmodifiers).

To get a human-readable representation of the **InputEventKey** with modifiers, use `OS.get_keycode_string(event.get_physical_keycode_with_modifiers())` where `event` is the **InputEventKey**.
