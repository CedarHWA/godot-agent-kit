> Source: https://docs.godotengine.org/en/4.7/classes/class_engineprofiler.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="engineprofiler"></a>

<a id="class-engineprofiler"></a>

# EngineProfiler

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Base class for creating custom profilers.

<a id="description"></a>

## Description

This class can be used to implement custom profilers that are able to interact with the engine and editor debugger.

See [EngineDebugger](class_enginedebugger.md#class-enginedebugger) and [EditorDebuggerPlugin](class_editordebuggerplugin.md#class-editordebuggerplugin) for more information.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [_add_frame](class_engineprofiler.md#class-engineprofiler-private-method-add-frame)(data: [Array](class_array.md#class-array)) virtual |
| void | [_tick](class_engineprofiler.md#class-engineprofiler-private-method-tick)(frame_time: [float](class_float.md#class-float), process_time: [float](class_float.md#class-float), physics_time: [float](class_float.md#class-float), physics_frame_time: [float](class_float.md#class-float)) virtual |
| void | [_toggle](class_engineprofiler.md#class-engineprofiler-private-method-toggle)(enable: [bool](class_bool.md#class-bool), options: [Array](class_array.md#class-array)) virtual |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-engineprofiler-private-method-add-frame"></a>

void **_add_frame**(data: [Array](class_array.md#class-array)) virtual [🔗](class_engineprofiler.md#class-engineprofiler-private-method-add-frame)

Called when data is added to profiler using [EngineDebugger.profiler_add_frame_data()](class_enginedebugger.md#class-enginedebugger-method-profiler-add-frame-data).

---


<a id="class-engineprofiler-private-method-tick"></a>

void **_tick**(frame_time: [float](class_float.md#class-float), process_time: [float](class_float.md#class-float), physics_time: [float](class_float.md#class-float), physics_frame_time: [float](class_float.md#class-float)) virtual [🔗](class_engineprofiler.md#class-engineprofiler-private-method-tick)

Called once every engine iteration when the profiler is active with information about the current frame. All time values are in seconds. Lower values represent faster processing times and are therefore considered better.

---


<a id="class-engineprofiler-private-method-toggle"></a>

void **_toggle**(enable: [bool](class_bool.md#class-bool), options: [Array](class_array.md#class-array)) virtual [🔗](class_engineprofiler.md#class-engineprofiler-private-method-toggle)

Called when the profiler is enabled/disabled, along with a set of `options`.
