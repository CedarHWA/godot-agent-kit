> Source: https://docs.godotengine.org/en/4.7/classes/class_signal.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="signal"></a>

<a id="class-signal"></a>

# Signal

A built-in type representing a signal of an [Object](class_object.md#class-object).

<a id="description"></a>

## Description

**Signal** is a built-in [Variant](class_variant.md#class-variant) type that represents a signal of an [Object](class_object.md#class-object) instance. Like all [Variant](class_variant.md#class-variant) types, it can be stored in variables and passed to functions. Signals allow all connected [Callable](class_callable.md#class-callable)s (and by extension their respective objects) to listen and react to events, without directly referencing one another. This keeps the code flexible and easier to manage. You can check whether an [Object](class_object.md#class-object) has a given signal name using [Object.has_signal()](class_object.md#class-object-method-has-signal).

In GDScript, signals can be declared with the `signal` keyword. In C#, you may use the `[Signal]` attribute on a delegate.

```gdscript
signal attacked

# Additional arguments may be declared.
# These arguments must be passed when the signal is emitted.
signal item_dropped(item_name, amount)
```

```csharp
[Signal]
delegate void AttackedEventHandler();

// Additional arguments may be declared.
// These arguments must be passed when the signal is emitted.
[Signal]
delegate void ItemDroppedEventHandler(string itemName, int amount);
```

Connecting signals is one of the most common operations in Godot and the API gives many options to do so, which are described further down. The code block below shows the recommended approach.

```gdscript
func _ready():
    var button = Button.new()
    # `button_down` here is a Signal Variant type. We therefore call the Signal.connect() method, not Object.connect().
    # See discussion below for a more in-depth overview of the API.
    button.button_down.connect(_on_button_down)

    # This assumes that a `Player` class exists, which defines a `hit` signal.
    var player = Player.new()
    # We use Signal.connect() again, and we also use the Callable.bind() method,
    # which returns a new Callable with the parameter binds.
    player.hit.connect(_on_player_hit.bind("sword", 100))

func _on_button_down():
    print("Button down!")

func _on_player_hit(weapon_type, damage):
    print("Hit with weapon %s for %d damage." % [weapon_type, damage])
```

```csharp
public override void _Ready()
{
    var button = new Button();
    // C# supports passing signals as events, so we can use this idiomatic construct:
    button.ButtonDown += OnButtonDown;

    // This assumes that a `Player` class exists, which defines a `Hit` signal.
    var player = new Player();
    // We can use lambdas when we need to bind additional parameters.
    player.Hit += () => OnPlayerHit("sword", 100);
}

private void OnButtonDown()
{
    GD.Print("Button down!");
}

private void OnPlayerHit(string weaponType, int damage)
{
    GD.Print($"Hit with weapon {weaponType} for {damage} damage.");
}
```

`Object.connect()` **or** `Signal.connect()`**?**

As seen above, the recommended method to connect signals is not [Object.connect()](class_object.md#class-object-method-connect). The code block below shows the four options for connecting signals, using either this legacy method or the recommended [connect()](class_signal.md#class-signal-method-connect), and using either an implicit [Callable](class_callable.md#class-callable) or a manually defined one.

```gdscript
func _ready():
    var button = Button.new()
    # Option 1: Object.connect() with an implicit Callable for the defined function.
    button.connect("button_down", _on_button_down)
    # Option 2: Object.connect() with a constructed Callable using a target object and method name.
    button.connect("button_down", Callable(self, "_on_button_down"))
    # Option 3: Signal.connect() with an implicit Callable for the defined function.
    button.button_down.connect(_on_button_down)
    # Option 4: Signal.connect() with a constructed Callable using a target object and method name.
    button.button_down.connect(Callable(self, "_on_button_down"))

func _on_button_down():
    print("Button down!")
```

```csharp
public override void _Ready()
{
    var button = new Button();
    // Option 1: In C#, we can use signals as events and connect with this idiomatic syntax:
    button.ButtonDown += OnButtonDown;
    // Option 2: GodotObject.Connect() with a constructed Callable from a method group.
    button.Connect(Button.SignalName.ButtonDown, Callable.From(OnButtonDown));
    // Option 3: GodotObject.Connect() with a constructed Callable using a target object and method name.
    button.Connect(Button.SignalName.ButtonDown, new Callable(this, MethodName.OnButtonDown));
}

private void OnButtonDown()
{
    GD.Print("Button down!");
}
```

While all options have the same outcome (`button`'s [BaseButton.button_down](class_basebutton.md#class-basebutton-signal-button-down) signal will be connected to `_on_button_down`), **option 3** offers the best validation: it will print a compile-time error if either the `button_down` **Signal** or the `_on_button_down` [Callable](class_callable.md#class-callable) are not defined. On the other hand, **option 2** only relies on string names and will only be able to validate either names at runtime: it will generate an error at runtime if `"button_down"` is not a signal, or if `"_on_button_down"` is not a method in the object `self`. The main reason for using options 1, 2, or 4 would be if you actually need to use strings (e.g. to connect signals programmatically based on strings read from a configuration file). Otherwise, option 3 is the recommended (and fastest) method.

**Binding and passing parameters:**

The syntax to bind parameters is through [Callable.bind()](class_callable.md#class-callable-method-bind), which returns a copy of the [Callable](class_callable.md#class-callable) with its parameters bound.

When calling [emit()](class_signal.md#class-signal-method-emit) or [Object.emit_signal()](class_object.md#class-object-method-emit-signal), the signal parameters can be also passed. The examples below show the relationship between these signal parameters and bound parameters.

```gdscript
func _ready():
    # This assumes that a `Player` class exists, which defines a `hit` signal.
    var player = Player.new()
    # Using Callable.bind().
    player.hit.connect(_on_player_hit.bind("sword", 100))

    # Parameters added when emitting the signal are passed first.
    player.hit.emit("Dark lord", 5)

# We pass two arguments when emitting (`hit_by`, `level`),
# and bind two more arguments when connecting (`weapon_type`, `damage`).
func _on_player_hit(hit_by, level, weapon_type, damage):
    print("Hit by %s (level %d) with weapon %s for %d damage." % [hit_by, level, weapon_type, damage])
```

```csharp
public override void _Ready()
{
    // This assumes that a `Player` class exists, which defines a `Hit` signal.
    var player = new Player();
    // Using lambda expressions that create a closure that captures the additional parameters.
    // The lambda only receives the parameters defined by the signal's delegate.
    player.Hit += (hitBy, level) => OnPlayerHit(hitBy, level, "sword", 100);

    // Parameters added when emitting the signal are passed first.
    player.EmitSignal(SignalName.Hit, "Dark lord", 5);
}

// We pass two arguments when emitting (`hit_by`, `level`),
// and bind two more arguments when connecting (`weapon_type`, `damage`).
private void OnPlayerHit(string hitBy, int level, string weaponType, int damage)
{
    GD.Print($"Hit by {hitBy} (level {level}) with weapon {weaponType} for {damage} damage.");
}
```

**Note:** In a boolean context, a signal will evaluate to `false` if it's null (see [is_null()](class_signal.md#class-signal-method-is-null)). Otherwise, a signal will always evaluate to `true`.

Note

There are notable differences when using this API with C#. See [C# API differences to GDScript](../tutorials/scripting/c_sharp/c_sharp_differences.md#doc-c-sharp-differences) for more information.

<a id="tutorials"></a>

## Tutorials

- [Using Signals](../getting_started/step_by_step/signals.md)
- [GDScript Basics](../tutorials/scripting/gdscript/gdscript_basics.md#signals)

<a id="constructors"></a>

## Constructors

|  |  |
| --- | --- |
| [Signal](class_signal.md#class-signal) | [Signal](class_signal.md#class-signal-constructor-signal)() |
| [Signal](class_signal.md#class-signal) | [Signal](class_signal.md#class-signal-constructor-signal)(from: [Signal](class_signal.md#class-signal)) |
| [Signal](class_signal.md#class-signal) | [Signal](class_signal.md#class-signal-constructor-signal)(object: [Object](class_object.md#class-object), signal: [StringName](class_stringname.md#class-stringname)) |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [int](class_int.md#class-int) | [connect](class_signal.md#class-signal-method-connect)(callable: [Callable](class_callable.md#class-callable), flags: [int](class_int.md#class-int) = 0) |
| void | [disconnect](class_signal.md#class-signal-method-disconnect)(callable: [Callable](class_callable.md#class-callable)) |
| void | [emit](class_signal.md#class-signal-method-emit)(...) vararg const |
| [Array](class_array.md#class-array) | [get_connections](class_signal.md#class-signal-method-get-connections)() const |
| [StringName](class_stringname.md#class-stringname) | [get_name](class_signal.md#class-signal-method-get-name)() const |
| [Object](class_object.md#class-object) | [get_object](class_signal.md#class-signal-method-get-object)() const |
| [int](class_int.md#class-int) | [get_object_id](class_signal.md#class-signal-method-get-object-id)() const |
| [bool](class_bool.md#class-bool) | [has_connections](class_signal.md#class-signal-method-has-connections)() const |
| [bool](class_bool.md#class-bool) | [is_connected](class_signal.md#class-signal-method-is-connected)(callable: [Callable](class_callable.md#class-callable)) const |
| [bool](class_bool.md#class-bool) | [is_null](class_signal.md#class-signal-method-is-null)() const |

<a id="operators"></a>

## Operators

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [operator !=](class_signal.md#class-signal-operator-neq-signal)(right: [Signal](class_signal.md#class-signal)) |
| [bool](class_bool.md#class-bool) | [operator ==](class_signal.md#class-signal-operator-eq-signal)(right: [Signal](class_signal.md#class-signal)) |

---


<a id="constructor-descriptions"></a>

## Constructor Descriptions

<a id="class-signal-constructor-signal"></a>

[Signal](class_signal.md#class-signal) **Signal**() [🔗](class_signal.md#class-signal-constructor-signal)

Constructs an empty **Signal** with no object nor signal name bound.

---

[Signal](class_signal.md#class-signal) **Signal**(from: [Signal](class_signal.md#class-signal))

Constructs a **Signal** as a copy of the given **Signal**.

---

[Signal](class_signal.md#class-signal) **Signal**(object: [Object](class_object.md#class-object), signal: [StringName](class_stringname.md#class-stringname))

Creates a **Signal** object referencing a signal named `signal` in the specified `object`.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-signal-method-connect"></a>

[int](class_int.md#class-int) **connect**(callable: [Callable](class_callable.md#class-callable), flags: [int](class_int.md#class-int) = 0) [🔗](class_signal.md#class-signal-method-connect)

Connects this signal to the specified `callable`. Optional `flags` can be also added to configure the connection's behavior (see [ConnectFlags](class_object.md#enum-object-connectflags) constants). You can provide additional arguments to the connected `callable` by using [Callable.bind()](class_callable.md#class-callable-method-bind).

A signal can only be connected once to the same [Callable](class_callable.md#class-callable). If the signal is already connected, this method returns [@GlobalScope.ERR_INVALID_PARAMETER](class_@globalscope.md#class-globalscope-constant-err-invalid-parameter) and generates an error, unless the signal is connected with [Object.CONNECT_REFERENCE_COUNTED](class_object.md#class-object-constant-connect-reference-counted). To prevent this, use [is_connected()](class_signal.md#class-signal-method-is-connected) first to check for existing connections.

```gdscript
for button in $Buttons.get_children():
    button.pressed.connect(_on_pressed.bind(button))

func _on_pressed(button):
    print(button.name, " was pressed")
```

**Note:** If the `callable`'s object is freed, the connection will be lost.

---


<a id="class-signal-method-disconnect"></a>

void **disconnect**(callable: [Callable](class_callable.md#class-callable)) [🔗](class_signal.md#class-signal-method-disconnect)

Disconnects this signal from the specified [Callable](class_callable.md#class-callable). If the connection does not exist, generates an error. Use [is_connected()](class_signal.md#class-signal-method-is-connected) to make sure that the connection exists.

---


<a id="class-signal-method-emit"></a>

void **emit**(...) vararg const [🔗](class_signal.md#class-signal-method-emit)

Emits this signal. All [Callable](class_callable.md#class-callable)s connected to this signal will be triggered. This method supports a variable number of arguments, so parameters can be passed as a comma separated list.

---


<a id="class-signal-method-get-connections"></a>

[Array](class_array.md#class-array) **get_connections**() const [🔗](class_signal.md#class-signal-method-get-connections)

Returns an [Array](class_array.md#class-array) of connections for this signal. Each connection is represented as a [Dictionary](class_dictionary.md#class-dictionary) that contains three entries:

- `signal` is a reference to this signal;
- `callable` is a reference to the connected [Callable](class_callable.md#class-callable);
- `flags` is a combination of [ConnectFlags](class_object.md#enum-object-connectflags).

---


<a id="class-signal-method-get-name"></a>

[StringName](class_stringname.md#class-stringname) **get_name**() const [🔗](class_signal.md#class-signal-method-get-name)

Returns the name of this signal.

---


<a id="class-signal-method-get-object"></a>

[Object](class_object.md#class-object) **get_object**() const [🔗](class_signal.md#class-signal-method-get-object)

Returns the object emitting this signal.

---


<a id="class-signal-method-get-object-id"></a>

[int](class_int.md#class-int) **get_object_id**() const [🔗](class_signal.md#class-signal-method-get-object-id)

Returns the ID of the object emitting this signal (see [Object.get_instance_id()](class_object.md#class-object-method-get-instance-id)).

---


<a id="class-signal-method-has-connections"></a>

[bool](class_bool.md#class-bool) **has_connections**() const [🔗](class_signal.md#class-signal-method-has-connections)

Returns `true` if any [Callable](class_callable.md#class-callable) is connected to this signal.

---


<a id="class-signal-method-is-connected"></a>

[bool](class_bool.md#class-bool) **is_connected**(callable: [Callable](class_callable.md#class-callable)) const [🔗](class_signal.md#class-signal-method-is-connected)

Returns `true` if the specified [Callable](class_callable.md#class-callable) is connected to this signal.

---


<a id="class-signal-method-is-null"></a>

[bool](class_bool.md#class-bool) **is_null**() const [🔗](class_signal.md#class-signal-method-is-null)

Returns `true` if this **Signal** has no object and the signal name is empty. Equivalent to `signal == Signal()`.

---


<a id="operator-descriptions"></a>

## Operator Descriptions

<a id="class-signal-operator-neq-signal"></a>

[bool](class_bool.md#class-bool) **operator !=**(right: [Signal](class_signal.md#class-signal)) [🔗](class_signal.md#class-signal-operator-neq-signal)

Returns `true` if the signals do not share the same object and name.

---


<a id="class-signal-operator-eq-signal"></a>

[bool](class_bool.md#class-bool) **operator ==**(right: [Signal](class_signal.md#class-signal)) [🔗](class_signal.md#class-signal-operator-eq-signal)

Returns `true` if both signals share the same object and name.
