> Source: https://docs.godotengine.org/en/4.7/classes/class_enginedebugger.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="enginedebugger"></a>

<a id="class-enginedebugger"></a>

# EngineDebugger

**Inherits:** [Object](class_object.md#class-object)

Exposes the internal debugger.

<a id="description"></a>

## Description

**EngineDebugger** handles the communication between the editor and the running game. It is active in the running game. Messages can be sent/received through it. It also manages the profilers.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [clear_breakpoints](class_enginedebugger.md#class-enginedebugger-method-clear-breakpoints)() |
| void | [debug](class_enginedebugger.md#class-enginedebugger-method-debug)(can_continue: [bool](class_bool.md#class-bool) = true, is_error_breakpoint: [bool](class_bool.md#class-bool) = false) |
| [int](class_int.md#class-int) | [get_depth](class_enginedebugger.md#class-enginedebugger-method-get-depth)() const |
| [int](class_int.md#class-int) | [get_lines_left](class_enginedebugger.md#class-enginedebugger-method-get-lines-left)() const |
| [bool](class_bool.md#class-bool) | [has_capture](class_enginedebugger.md#class-enginedebugger-method-has-capture)(name: [StringName](class_stringname.md#class-stringname)) |
| [bool](class_bool.md#class-bool) | [has_profiler](class_enginedebugger.md#class-enginedebugger-method-has-profiler)(name: [StringName](class_stringname.md#class-stringname)) |
| void | [insert_breakpoint](class_enginedebugger.md#class-enginedebugger-method-insert-breakpoint)(line: [int](class_int.md#class-int), source: [StringName](class_stringname.md#class-stringname)) |
| [bool](class_bool.md#class-bool) | [is_active](class_enginedebugger.md#class-enginedebugger-method-is-active)() |
| [bool](class_bool.md#class-bool) | [is_breakpoint](class_enginedebugger.md#class-enginedebugger-method-is-breakpoint)(line: [int](class_int.md#class-int), source: [StringName](class_stringname.md#class-stringname)) const |
| [bool](class_bool.md#class-bool) | [is_profiling](class_enginedebugger.md#class-enginedebugger-method-is-profiling)(name: [StringName](class_stringname.md#class-stringname)) |
| [bool](class_bool.md#class-bool) | [is_skipping_breakpoints](class_enginedebugger.md#class-enginedebugger-method-is-skipping-breakpoints)() const |
| void | [line_poll](class_enginedebugger.md#class-enginedebugger-method-line-poll)() |
| void | [profiler_add_frame_data](class_enginedebugger.md#class-enginedebugger-method-profiler-add-frame-data)(name: [StringName](class_stringname.md#class-stringname), data: [Array](class_array.md#class-array)) |
| void | [profiler_enable](class_enginedebugger.md#class-enginedebugger-method-profiler-enable)(name: [StringName](class_stringname.md#class-stringname), enable: [bool](class_bool.md#class-bool), arguments: [Array](class_array.md#class-array) = []) |
| void | [register_message_capture](class_enginedebugger.md#class-enginedebugger-method-register-message-capture)(name: [StringName](class_stringname.md#class-stringname), callable: [Callable](class_callable.md#class-callable)) |
| void | [register_profiler](class_enginedebugger.md#class-enginedebugger-method-register-profiler)(name: [StringName](class_stringname.md#class-stringname), profiler: [EngineProfiler](class_engineprofiler.md#class-engineprofiler)) |
| void | [remove_breakpoint](class_enginedebugger.md#class-enginedebugger-method-remove-breakpoint)(line: [int](class_int.md#class-int), source: [StringName](class_stringname.md#class-stringname)) |
| void | [script_debug](class_enginedebugger.md#class-enginedebugger-method-script-debug)(language: [ScriptLanguage](class_scriptlanguage.md#class-scriptlanguage), can_continue: [bool](class_bool.md#class-bool) = true, is_error_breakpoint: [bool](class_bool.md#class-bool) = false) |
| void | [send_message](class_enginedebugger.md#class-enginedebugger-method-send-message)(message: [String](class_string.md#class-string), data: [Array](class_array.md#class-array)) |
| void | [set_depth](class_enginedebugger.md#class-enginedebugger-method-set-depth)(depth: [int](class_int.md#class-int)) |
| void | [set_lines_left](class_enginedebugger.md#class-enginedebugger-method-set-lines-left)(lines: [int](class_int.md#class-int)) |
| void | [unregister_message_capture](class_enginedebugger.md#class-enginedebugger-method-unregister-message-capture)(name: [StringName](class_stringname.md#class-stringname)) |
| void | [unregister_profiler](class_enginedebugger.md#class-enginedebugger-method-unregister-profiler)(name: [StringName](class_stringname.md#class-stringname)) |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-enginedebugger-method-clear-breakpoints"></a>

void **clear_breakpoints**() [🔗](class_enginedebugger.md#class-enginedebugger-method-clear-breakpoints)

Clears all breakpoints.

---


<a id="class-enginedebugger-method-debug"></a>

void **debug**(can_continue: [bool](class_bool.md#class-bool) = true, is_error_breakpoint: [bool](class_bool.md#class-bool) = false) [🔗](class_enginedebugger.md#class-enginedebugger-method-debug)

Starts a debug break in script execution, optionally specifying whether the program can continue based on `can_continue` and whether the break was due to a breakpoint.

---


<a id="class-enginedebugger-method-get-depth"></a>

[int](class_int.md#class-int) **get_depth**() const [🔗](class_enginedebugger.md#class-enginedebugger-method-get-depth)

**Experimental:** This method may be changed or removed in future versions.

Returns the current debug depth.

---


<a id="class-enginedebugger-method-get-lines-left"></a>

[int](class_int.md#class-int) **get_lines_left**() const [🔗](class_enginedebugger.md#class-enginedebugger-method-get-lines-left)

**Experimental:** This method may be changed or removed in future versions.

Returns the number of lines that remain.

---


<a id="class-enginedebugger-method-has-capture"></a>

[bool](class_bool.md#class-bool) **has_capture**(name: [StringName](class_stringname.md#class-stringname)) [🔗](class_enginedebugger.md#class-enginedebugger-method-has-capture)

Returns `true` if a capture with the given name is present otherwise `false`.

---


<a id="class-enginedebugger-method-has-profiler"></a>

[bool](class_bool.md#class-bool) **has_profiler**(name: [StringName](class_stringname.md#class-stringname)) [🔗](class_enginedebugger.md#class-enginedebugger-method-has-profiler)

Returns `true` if a profiler with the given name is present otherwise `false`.

---


<a id="class-enginedebugger-method-insert-breakpoint"></a>

void **insert_breakpoint**(line: [int](class_int.md#class-int), source: [StringName](class_stringname.md#class-stringname)) [🔗](class_enginedebugger.md#class-enginedebugger-method-insert-breakpoint)

Inserts a new breakpoint with the given `source` and `line`.

---


<a id="class-enginedebugger-method-is-active"></a>

[bool](class_bool.md#class-bool) **is_active**() [🔗](class_enginedebugger.md#class-enginedebugger-method-is-active)

Returns `true` if the debugger is active otherwise `false`.

---


<a id="class-enginedebugger-method-is-breakpoint"></a>

[bool](class_bool.md#class-bool) **is_breakpoint**(line: [int](class_int.md#class-int), source: [StringName](class_stringname.md#class-stringname)) const [🔗](class_enginedebugger.md#class-enginedebugger-method-is-breakpoint)

Returns `true` if the given `source` and `line` represent an existing breakpoint.

---


<a id="class-enginedebugger-method-is-profiling"></a>

[bool](class_bool.md#class-bool) **is_profiling**(name: [StringName](class_stringname.md#class-stringname)) [🔗](class_enginedebugger.md#class-enginedebugger-method-is-profiling)

Returns `true` if a profiler with the given name is present and active otherwise `false`.

---


<a id="class-enginedebugger-method-is-skipping-breakpoints"></a>

[bool](class_bool.md#class-bool) **is_skipping_breakpoints**() const [🔗](class_enginedebugger.md#class-enginedebugger-method-is-skipping-breakpoints)

Returns `true` if the debugger is skipping breakpoints otherwise `false`.

---


<a id="class-enginedebugger-method-line-poll"></a>

void **line_poll**() [🔗](class_enginedebugger.md#class-enginedebugger-method-line-poll)

Forces a processing loop of debugger events. The purpose of this method is just processing events every now and then when the script might get too busy, so that bugs like infinite loops can be caught.

---


<a id="class-enginedebugger-method-profiler-add-frame-data"></a>

void **profiler_add_frame_data**(name: [StringName](class_stringname.md#class-stringname), data: [Array](class_array.md#class-array)) [🔗](class_enginedebugger.md#class-enginedebugger-method-profiler-add-frame-data)

Calls the `add` callable of the profiler with given `name` and `data`.

---


<a id="class-enginedebugger-method-profiler-enable"></a>

void **profiler_enable**(name: [StringName](class_stringname.md#class-stringname), enable: [bool](class_bool.md#class-bool), arguments: [Array](class_array.md#class-array) = []) [🔗](class_enginedebugger.md#class-enginedebugger-method-profiler-enable)

Calls the `toggle` callable of the profiler with given `name` and `arguments`. Enables/Disables the same profiler depending on `enable` argument.

---


<a id="class-enginedebugger-method-register-message-capture"></a>

void **register_message_capture**(name: [StringName](class_stringname.md#class-stringname), callable: [Callable](class_callable.md#class-callable)) [🔗](class_enginedebugger.md#class-enginedebugger-method-register-message-capture)

Registers a message capture with given `name`. If `name` is "my_message" then messages starting with "my_message:" will be called with the given callable.

The callable must accept a message string and a data array as argument. The callable should return `true` if the message is recognized.

**Note:** The callable will receive the message with the prefix stripped, unlike [EditorDebuggerPlugin._capture()](class_editordebuggerplugin.md#class-editordebuggerplugin-private-method-capture). See the [EditorDebuggerPlugin](class_editordebuggerplugin.md#class-editordebuggerplugin) description for an example.

---


<a id="class-enginedebugger-method-register-profiler"></a>

void **register_profiler**(name: [StringName](class_stringname.md#class-stringname), profiler: [EngineProfiler](class_engineprofiler.md#class-engineprofiler)) [🔗](class_enginedebugger.md#class-enginedebugger-method-register-profiler)

Registers a profiler with the given `name`. See [EngineProfiler](class_engineprofiler.md#class-engineprofiler) for more information.

---


<a id="class-enginedebugger-method-remove-breakpoint"></a>

void **remove_breakpoint**(line: [int](class_int.md#class-int), source: [StringName](class_stringname.md#class-stringname)) [🔗](class_enginedebugger.md#class-enginedebugger-method-remove-breakpoint)

Removes a breakpoint with the given `source` and `line`.

---


<a id="class-enginedebugger-method-script-debug"></a>

void **script_debug**(language: [ScriptLanguage](class_scriptlanguage.md#class-scriptlanguage), can_continue: [bool](class_bool.md#class-bool) = true, is_error_breakpoint: [bool](class_bool.md#class-bool) = false) [🔗](class_enginedebugger.md#class-enginedebugger-method-script-debug)

Starts a debug break in script execution, optionally specifying whether the program can continue based on `can_continue` and whether the break was due to a breakpoint.

---


<a id="class-enginedebugger-method-send-message"></a>

void **send_message**(message: [String](class_string.md#class-string), data: [Array](class_array.md#class-array)) [🔗](class_enginedebugger.md#class-enginedebugger-method-send-message)

Sends a message with given `message` and `data` array.

---


<a id="class-enginedebugger-method-set-depth"></a>

void **set_depth**(depth: [int](class_int.md#class-int)) [🔗](class_enginedebugger.md#class-enginedebugger-method-set-depth)

**Experimental:** This method may be changed or removed in future versions.

Sets the current debugging depth.

---


<a id="class-enginedebugger-method-set-lines-left"></a>

void **set_lines_left**(lines: [int](class_int.md#class-int)) [🔗](class_enginedebugger.md#class-enginedebugger-method-set-lines-left)

**Experimental:** This method may be changed or removed in future versions.

Sets the current debugging lines that remain.

---


<a id="class-enginedebugger-method-unregister-message-capture"></a>

void **unregister_message_capture**(name: [StringName](class_stringname.md#class-stringname)) [🔗](class_enginedebugger.md#class-enginedebugger-method-unregister-message-capture)

Unregisters the message capture with given `name`.

---


<a id="class-enginedebugger-method-unregister-profiler"></a>

void **unregister_profiler**(name: [StringName](class_stringname.md#class-stringname)) [🔗](class_enginedebugger.md#class-enginedebugger-method-unregister-profiler)

Unregisters a profiler with given `name`.
