> Source: https://docs.godotengine.org/en/4.7/classes/class_mainloop.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="mainloop"></a>

<a id="class-mainloop"></a>

# MainLoop

**Inherits:** [Object](class_object.md#class-object)

**Inherited By:** [SceneTree](class_scenetree.md#class-scenetree)

Abstract base class for the game's main loop.

<a id="description"></a>

## Description

**MainLoop** is the abstract base class for a Godot project's game loop. It is inherited by [SceneTree](class_scenetree.md#class-scenetree), which is the default game loop implementation used in Godot projects, though it is also possible to write and use one's own **MainLoop** subclass instead of the scene tree.

Upon the application start, a **MainLoop** implementation must be provided to the OS; otherwise, the application will exit. This happens automatically (and a [SceneTree](class_scenetree.md#class-scenetree) is created) unless a **MainLoop** [Script](class_script.md#class-script) is provided from the command line (with e.g. `godot -s my_loop.gd`) or the [ProjectSettings.application/run/main_loop_type](class_projectsettings.md#class-projectsettings-property-application-run-main-loop-type) project setting is overwritten.

Here is an example script implementing a simple **MainLoop**:

```gdscript
class_name CustomMainLoop
extends MainLoop

var time_elapsed = 0

func _initialize():
    print("Initialized:")
    print("  Starting time: %s" % str(time_elapsed))

func _process(delta):
    time_elapsed += delta
    # Return true to end the main loop.
    return Input.get_mouse_button_mask() != 0 || Input.is_key_pressed(KEY_ESCAPE)

func _finalize():
    print("Finalized:")
    print("  End time: %s" % str(time_elapsed))
```

```csharp
using Godot;

[GlobalClass]
public partial class CustomMainLoop : MainLoop
{
    private double _timeElapsed = 0;

    public override void _Initialize()
    {
        GD.Print("Initialized:");
        GD.Print($"  Starting Time: {_timeElapsed}");
    }

    public override bool _Process(double delta)
    {
        _timeElapsed += delta;
        // Return true to end the main loop.
        return Input.GetMouseButtonMask() != 0 || Input.IsKeyPressed(Key.Escape);
    }

    private void _Finalize()
    {
        GD.Print("Finalized:");
        GD.Print($"  End Time: {_timeElapsed}");
    }
}
```

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [_finalize](class_mainloop.md#class-mainloop-private-method-finalize)() virtual |
| void | [_initialize](class_mainloop.md#class-mainloop-private-method-initialize)() virtual |
| [bool](class_bool.md#class-bool) | [_physics_process](class_mainloop.md#class-mainloop-private-method-physics-process)(delta: [float](class_float.md#class-float)) virtual |
| [bool](class_bool.md#class-bool) | [_process](class_mainloop.md#class-mainloop-private-method-process)(delta: [float](class_float.md#class-float)) virtual |

---


<a id="signals"></a>

## Signals

<a id="class-mainloop-signal-on-request-permissions-result"></a>

**on_request_permissions_result**(permission: [String](class_string.md#class-string), granted: [bool](class_bool.md#class-bool)) [🔗](class_mainloop.md#class-mainloop-signal-on-request-permissions-result)

Emitted when a user responds to a permission request.

---


<a id="constants"></a>

## Constants

<a id="class-mainloop-constant-notification-os-memory-warning"></a>

**NOTIFICATION_OS_MEMORY_WARNING** = `2009` [🔗](class_mainloop.md#class-mainloop-constant-notification-os-memory-warning)

Notification received from the OS when the application is exceeding its allocated memory.

Specific to the iOS platform.

<a id="class-mainloop-constant-notification-translation-changed"></a>

**NOTIFICATION_TRANSLATION_CHANGED** = `2010` [🔗](class_mainloop.md#class-mainloop-constant-notification-translation-changed)

Notification received when translations may have changed. Can be triggered by the user changing the locale. Can be used to respond to language changes, for example to change the UI strings on the fly. Useful when working with the built-in translation support, like [Object.tr()](class_object.md#class-object-method-tr).

<a id="class-mainloop-constant-notification-wm-about"></a>

**NOTIFICATION_WM_ABOUT** = `2011` [🔗](class_mainloop.md#class-mainloop-constant-notification-wm-about)

Notification received from the OS when a request for "About" information is sent.

Specific to the macOS platform.

<a id="class-mainloop-constant-notification-crash"></a>

**NOTIFICATION_CRASH** = `2012` [🔗](class_mainloop.md#class-mainloop-constant-notification-crash)

Notification received from Godot's crash handler when the engine is about to crash.

Implemented on desktop platforms if the crash handler is enabled.

<a id="class-mainloop-constant-notification-os-ime-update"></a>

**NOTIFICATION_OS_IME_UPDATE** = `2013` [🔗](class_mainloop.md#class-mainloop-constant-notification-os-ime-update)

Notification received from the OS when an update of the Input Method Engine occurs (e.g. change of IME cursor position or composition string).

Implemented on desktop and web platforms.

<a id="class-mainloop-constant-notification-application-resumed"></a>

**NOTIFICATION_APPLICATION_RESUMED** = `2014` [🔗](class_mainloop.md#class-mainloop-constant-notification-application-resumed)

Notification received from the OS when the application is resumed.

Specific to the Android and iOS platforms.

<a id="class-mainloop-constant-notification-application-paused"></a>

**NOTIFICATION_APPLICATION_PAUSED** = `2015` [🔗](class_mainloop.md#class-mainloop-constant-notification-application-paused)

Notification received from the OS when the application is paused.

Specific to the Android and iOS platforms.

**Note:** On iOS, you only have approximately 5 seconds to finish a task started by this signal. If you go over this allotment, iOS will kill the app instead of pausing it.

<a id="class-mainloop-constant-notification-application-focus-in"></a>

**NOTIFICATION_APPLICATION_FOCUS_IN** = `2016` [🔗](class_mainloop.md#class-mainloop-constant-notification-application-focus-in)

Notification received from the OS when the application is focused, i.e. when changing the focus from the OS desktop or a thirdparty application to any open window of the Godot instance.

Implemented on desktop and mobile platforms.

<a id="class-mainloop-constant-notification-application-focus-out"></a>

**NOTIFICATION_APPLICATION_FOCUS_OUT** = `2017` [🔗](class_mainloop.md#class-mainloop-constant-notification-application-focus-out)

Notification received from the OS when the application is defocused, i.e. when changing the focus from any open window of the Godot instance to the OS desktop or a thirdparty application.

Implemented on desktop and mobile platforms.

<a id="class-mainloop-constant-notification-text-server-changed"></a>

**NOTIFICATION_TEXT_SERVER_CHANGED** = `2018` [🔗](class_mainloop.md#class-mainloop-constant-notification-text-server-changed)

Notification received when text server is changed.

<a id="class-mainloop-constant-notification-application-pip-mode-entered"></a>

**NOTIFICATION_APPLICATION_PIP_MODE_ENTERED** = `2019` [🔗](class_mainloop.md#class-mainloop-constant-notification-application-pip-mode-entered)

Notification received when the application enters picture-in-picture mode.

<a id="class-mainloop-constant-notification-application-pip-mode-exited"></a>

**NOTIFICATION_APPLICATION_PIP_MODE_EXITED** = `2020` [🔗](class_mainloop.md#class-mainloop-constant-notification-application-pip-mode-exited)

Notification received when the application exits picture-in-picture mode.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-mainloop-private-method-finalize"></a>

void **_finalize**() virtual [🔗](class_mainloop.md#class-mainloop-private-method-finalize)

Called before the program exits.

---


<a id="class-mainloop-private-method-initialize"></a>

void **_initialize**() virtual [🔗](class_mainloop.md#class-mainloop-private-method-initialize)

Called once during initialization.

---


<a id="class-mainloop-private-method-physics-process"></a>

[bool](class_bool.md#class-bool) **_physics_process**(delta: [float](class_float.md#class-float)) virtual [🔗](class_mainloop.md#class-mainloop-private-method-physics-process)

Called each physics tick. `delta` is the logical time between physics ticks in seconds and is equal to [Engine.time_scale](class_engine.md#class-engine-property-time-scale) / [Engine.physics_ticks_per_second](class_engine.md#class-engine-property-physics-ticks-per-second). Equivalent to [Node._physics_process()](class_node.md#class-node-private-method-physics-process).

If implemented, the method must return a boolean value. `true` ends the main loop, while `false` lets it proceed to the next step.

**Note:** [_physics_process()](class_mainloop.md#class-mainloop-private-method-physics-process) may be called up to [Engine.max_physics_steps_per_frame](class_engine.md#class-engine-property-max-physics-steps-per-frame) times per (idle) frame. This step limit may be reached when the engine is suffering performance issues.

**Note:** Accumulated `delta` may diverge from real world seconds.

---


<a id="class-mainloop-private-method-process"></a>

[bool](class_bool.md#class-bool) **_process**(delta: [float](class_float.md#class-float)) virtual [🔗](class_mainloop.md#class-mainloop-private-method-process)

Called on each idle frame, prior to rendering, and after physics ticks have been processed. `delta` is the time between frames in seconds. Equivalent to [Node._process()](class_node.md#class-node-private-method-process).

If implemented, the method must return a boolean value. `true` ends the main loop, while `false` lets it proceed to the next frame.

**Note:** When the engine is struggling and the frame rate is lowered, `delta` will increase. When `delta` is increased, it's capped at a maximum of [Engine.time_scale](class_engine.md#class-engine-property-time-scale) \* [Engine.max_physics_steps_per_frame](class_engine.md#class-engine-property-max-physics-steps-per-frame) / [Engine.physics_ticks_per_second](class_engine.md#class-engine-property-physics-ticks-per-second). As a result, accumulated `delta` may not represent real world time.

**Note:** When `--fixed-fps` is enabled or the engine is running in Movie Maker mode (see [MovieWriter](class_moviewriter.md#class-moviewriter)), process `delta` will always be the same for every frame, regardless of how much time the frame took to render.

**Note:** Frame delta may be post-processed by [OS.delta_smoothing](class_os.md#class-os-property-delta-smoothing) if this is enabled for the project.
