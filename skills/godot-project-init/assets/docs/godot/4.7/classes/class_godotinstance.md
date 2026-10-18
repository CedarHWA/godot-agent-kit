> Source: https://docs.godotengine.org/en/4.7/classes/class_godotinstance.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="godotinstance"></a>

<a id="class-godotinstance"></a>

# GodotInstance

**Inherits:** [Object](class_object.md#class-object)

Provides access to an embedded Godot instance.

<a id="description"></a>

## Description

GodotInstance represents a running Godot instance that is controlled from an outside codebase, without a perpetual main loop. It is created by the C API `libgodot_create_godot_instance`. Only one may be created per process.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [focus_in](class_godotinstance.md#class-godotinstance-method-focus-in)() |
| void | [focus_out](class_godotinstance.md#class-godotinstance-method-focus-out)() |
| [bool](class_bool.md#class-bool) | [is_started](class_godotinstance.md#class-godotinstance-method-is-started)() |
| [bool](class_bool.md#class-bool) | [iteration](class_godotinstance.md#class-godotinstance-method-iteration)() |
| void | [pause](class_godotinstance.md#class-godotinstance-method-pause)() |
| void | [resume](class_godotinstance.md#class-godotinstance-method-resume)() |
| [bool](class_bool.md#class-bool) | [start](class_godotinstance.md#class-godotinstance-method-start)() |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-godotinstance-method-focus-in"></a>

void **focus_in**() [🔗](class_godotinstance.md#class-godotinstance-method-focus-in)

Notifies the instance that it is now in focus.

---


<a id="class-godotinstance-method-focus-out"></a>

void **focus_out**() [🔗](class_godotinstance.md#class-godotinstance-method-focus-out)

Notifies the instance that it is now not in focus.

---


<a id="class-godotinstance-method-is-started"></a>

[bool](class_bool.md#class-bool) **is_started**() [🔗](class_godotinstance.md#class-godotinstance-method-is-started)

Returns `true` if this instance has been fully started.

---


<a id="class-godotinstance-method-iteration"></a>

[bool](class_bool.md#class-bool) **iteration**() [🔗](class_godotinstance.md#class-godotinstance-method-iteration)

Runs a single iteration of the main loop. Returns `true` if the engine is attempting to quit.

---


<a id="class-godotinstance-method-pause"></a>

void **pause**() [🔗](class_godotinstance.md#class-godotinstance-method-pause)

Notifies the instance that it is going to be paused.

---


<a id="class-godotinstance-method-resume"></a>

void **resume**() [🔗](class_godotinstance.md#class-godotinstance-method-resume)

Notifies the instance that it is being resumed.

---


<a id="class-godotinstance-method-start"></a>

[bool](class_bool.md#class-bool) **start**() [🔗](class_godotinstance.md#class-godotinstance-method-start)

Finishes this instance's startup sequence. Returns `true` on success.
