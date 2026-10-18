> Source: https://docs.godotengine.org/en/4.7/classes/class_scriptbacktrace.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="scriptbacktrace"></a>

<a id="class-scriptbacktrace"></a>

# ScriptBacktrace

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A captured backtrace of a specific script language.

<a id="description"></a>

## Description

**ScriptBacktrace** holds an already captured backtrace of a specific script language, such as GDScript or C#, which are captured using [Engine.capture_script_backtraces()](class_engine.md#class-engine-method-capture-script-backtraces).

See [ProjectSettings.debug/settings/gdscript/always_track_call_stacks](class_projectsettings.md#class-projectsettings-property-debug-settings-gdscript-always-track-call-stacks) and [ProjectSettings.debug/settings/gdscript/always_track_local_variables](class_projectsettings.md#class-projectsettings-property-debug-settings-gdscript-always-track-local-variables) for ways of controlling the contents of this class.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [String](class_string.md#class-string) | [format](class_scriptbacktrace.md#class-scriptbacktrace-method-format)(indent_all: [int](class_int.md#class-int) = 0, indent_frames: [int](class_int.md#class-int) = 4) const |
| [int](class_int.md#class-int) | [get_frame_count](class_scriptbacktrace.md#class-scriptbacktrace-method-get-frame-count)() const |
| [String](class_string.md#class-string) | [get_frame_file](class_scriptbacktrace.md#class-scriptbacktrace-method-get-frame-file)(index: [int](class_int.md#class-int)) const |
| [String](class_string.md#class-string) | [get_frame_function](class_scriptbacktrace.md#class-scriptbacktrace-method-get-frame-function)(index: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_frame_line](class_scriptbacktrace.md#class-scriptbacktrace-method-get-frame-line)(index: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_global_variable_count](class_scriptbacktrace.md#class-scriptbacktrace-method-get-global-variable-count)() const |
| [String](class_string.md#class-string) | [get_global_variable_name](class_scriptbacktrace.md#class-scriptbacktrace-method-get-global-variable-name)(variable_index: [int](class_int.md#class-int)) const |
| [Variant](class_variant.md#class-variant) | [get_global_variable_value](class_scriptbacktrace.md#class-scriptbacktrace-method-get-global-variable-value)(variable_index: [int](class_int.md#class-int)) const |
| [String](class_string.md#class-string) | [get_language_name](class_scriptbacktrace.md#class-scriptbacktrace-method-get-language-name)() const |
| [int](class_int.md#class-int) | [get_local_variable_count](class_scriptbacktrace.md#class-scriptbacktrace-method-get-local-variable-count)(frame_index: [int](class_int.md#class-int)) const |
| [String](class_string.md#class-string) | [get_local_variable_name](class_scriptbacktrace.md#class-scriptbacktrace-method-get-local-variable-name)(frame_index: [int](class_int.md#class-int), variable_index: [int](class_int.md#class-int)) const |
| [Variant](class_variant.md#class-variant) | [get_local_variable_value](class_scriptbacktrace.md#class-scriptbacktrace-method-get-local-variable-value)(frame_index: [int](class_int.md#class-int), variable_index: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_member_variable_count](class_scriptbacktrace.md#class-scriptbacktrace-method-get-member-variable-count)(frame_index: [int](class_int.md#class-int)) const |
| [String](class_string.md#class-string) | [get_member_variable_name](class_scriptbacktrace.md#class-scriptbacktrace-method-get-member-variable-name)(frame_index: [int](class_int.md#class-int), variable_index: [int](class_int.md#class-int)) const |
| [Variant](class_variant.md#class-variant) | [get_member_variable_value](class_scriptbacktrace.md#class-scriptbacktrace-method-get-member-variable-value)(frame_index: [int](class_int.md#class-int), variable_index: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [is_empty](class_scriptbacktrace.md#class-scriptbacktrace-method-is-empty)() const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-scriptbacktrace-method-format"></a>

[String](class_string.md#class-string) **format**(indent_all: [int](class_int.md#class-int) = 0, indent_frames: [int](class_int.md#class-int) = 4) const [🔗](class_scriptbacktrace.md#class-scriptbacktrace-method-format)

Converts the backtrace to a [String](class_string.md#class-string), where the entire string will be indented by `indent_all` number of spaces, and the individual stack frames will be additionally indented by `indent_frames` number of spaces.

**Note:** Calling [Object.to_string()](class_object.md#class-object-method-to-string) on a **ScriptBacktrace** will produce the same output as calling [format()](class_scriptbacktrace.md#class-scriptbacktrace-method-format) with all parameters left at their default values.

---


<a id="class-scriptbacktrace-method-get-frame-count"></a>

[int](class_int.md#class-int) **get_frame_count**() const [🔗](class_scriptbacktrace.md#class-scriptbacktrace-method-get-frame-count)

Returns the number of stack frames in the backtrace.

---


<a id="class-scriptbacktrace-method-get-frame-file"></a>

[String](class_string.md#class-string) **get_frame_file**(index: [int](class_int.md#class-int)) const [🔗](class_scriptbacktrace.md#class-scriptbacktrace-method-get-frame-file)

Returns the file name of the call site represented by the stack frame at the specified index.

---


<a id="class-scriptbacktrace-method-get-frame-function"></a>

[String](class_string.md#class-string) **get_frame_function**(index: [int](class_int.md#class-int)) const [🔗](class_scriptbacktrace.md#class-scriptbacktrace-method-get-frame-function)

Returns the name of the function called at the stack frame at the specified index.

---


<a id="class-scriptbacktrace-method-get-frame-line"></a>

[int](class_int.md#class-int) **get_frame_line**(index: [int](class_int.md#class-int)) const [🔗](class_scriptbacktrace.md#class-scriptbacktrace-method-get-frame-line)

Returns the line number of the call site represented by the stack frame at the specified index.

---


<a id="class-scriptbacktrace-method-get-global-variable-count"></a>

[int](class_int.md#class-int) **get_global_variable_count**() const [🔗](class_scriptbacktrace.md#class-scriptbacktrace-method-get-global-variable-count)

Returns the number of global variables (e.g. autoload singletons) in the backtrace.

**Note:** This will be non-zero only if the `include_variables` parameter was `true` when capturing the backtrace with [Engine.capture_script_backtraces()](class_engine.md#class-engine-method-capture-script-backtraces).

---


<a id="class-scriptbacktrace-method-get-global-variable-name"></a>

[String](class_string.md#class-string) **get_global_variable_name**(variable_index: [int](class_int.md#class-int)) const [🔗](class_scriptbacktrace.md#class-scriptbacktrace-method-get-global-variable-name)

Returns the name of the global variable at the specified index.

---


<a id="class-scriptbacktrace-method-get-global-variable-value"></a>

[Variant](class_variant.md#class-variant) **get_global_variable_value**(variable_index: [int](class_int.md#class-int)) const [🔗](class_scriptbacktrace.md#class-scriptbacktrace-method-get-global-variable-value)

Returns the value of the global variable at the specified index.

**Warning:** With GDScript backtraces, the returned [Variant](class_variant.md#class-variant) will be the variable's actual value, including any object references. This means that storing the returned [Variant](class_variant.md#class-variant) will prevent any such object from being deallocated, so it's generally recommended not to do so.

---


<a id="class-scriptbacktrace-method-get-language-name"></a>

[String](class_string.md#class-string) **get_language_name**() const [🔗](class_scriptbacktrace.md#class-scriptbacktrace-method-get-language-name)

Returns the name of the script language that this backtrace was captured from.

---


<a id="class-scriptbacktrace-method-get-local-variable-count"></a>

[int](class_int.md#class-int) **get_local_variable_count**(frame_index: [int](class_int.md#class-int)) const [🔗](class_scriptbacktrace.md#class-scriptbacktrace-method-get-local-variable-count)

Returns the number of local variables in the stack frame at the specified index.

**Note:** This will be non-zero only if the `include_variables` parameter was `true` when capturing the backtrace with [Engine.capture_script_backtraces()](class_engine.md#class-engine-method-capture-script-backtraces).

---


<a id="class-scriptbacktrace-method-get-local-variable-name"></a>

[String](class_string.md#class-string) **get_local_variable_name**(frame_index: [int](class_int.md#class-int), variable_index: [int](class_int.md#class-int)) const [🔗](class_scriptbacktrace.md#class-scriptbacktrace-method-get-local-variable-name)

Returns the name of the local variable at the specified `variable_index` in the stack frame at the specified `frame_index`.

---


<a id="class-scriptbacktrace-method-get-local-variable-value"></a>

[Variant](class_variant.md#class-variant) **get_local_variable_value**(frame_index: [int](class_int.md#class-int), variable_index: [int](class_int.md#class-int)) const [🔗](class_scriptbacktrace.md#class-scriptbacktrace-method-get-local-variable-value)

Returns the value of the local variable at the specified `variable_index` in the stack frame at the specified `frame_index`.

**Warning:** With GDScript backtraces, the returned [Variant](class_variant.md#class-variant) will be the variable's actual value, including any object references. This means that storing the returned [Variant](class_variant.md#class-variant) will prevent any such object from being deallocated, so it's generally recommended not to do so.

---


<a id="class-scriptbacktrace-method-get-member-variable-count"></a>

[int](class_int.md#class-int) **get_member_variable_count**(frame_index: [int](class_int.md#class-int)) const [🔗](class_scriptbacktrace.md#class-scriptbacktrace-method-get-member-variable-count)

Returns the number of member variables in the stack frame at the specified index.

**Note:** This will be non-zero only if the `include_variables` parameter was `true` when capturing the backtrace with [Engine.capture_script_backtraces()](class_engine.md#class-engine-method-capture-script-backtraces).

---


<a id="class-scriptbacktrace-method-get-member-variable-name"></a>

[String](class_string.md#class-string) **get_member_variable_name**(frame_index: [int](class_int.md#class-int), variable_index: [int](class_int.md#class-int)) const [🔗](class_scriptbacktrace.md#class-scriptbacktrace-method-get-member-variable-name)

Returns the name of the member variable at the specified `variable_index` in the stack frame at the specified `frame_index`.

---


<a id="class-scriptbacktrace-method-get-member-variable-value"></a>

[Variant](class_variant.md#class-variant) **get_member_variable_value**(frame_index: [int](class_int.md#class-int), variable_index: [int](class_int.md#class-int)) const [🔗](class_scriptbacktrace.md#class-scriptbacktrace-method-get-member-variable-value)

Returns the value of the member variable at the specified `variable_index` in the stack frame at the specified `frame_index`.

**Warning:** With GDScript backtraces, the returned [Variant](class_variant.md#class-variant) will be the variable's actual value, including any object references. This means that storing the returned [Variant](class_variant.md#class-variant) will prevent any such object from being deallocated, so it's generally recommended not to do so.

---


<a id="class-scriptbacktrace-method-is-empty"></a>

[bool](class_bool.md#class-bool) **is_empty**() const [🔗](class_scriptbacktrace.md#class-scriptbacktrace-method-is-empty)

Returns `true` if the backtrace has no stack frames.
