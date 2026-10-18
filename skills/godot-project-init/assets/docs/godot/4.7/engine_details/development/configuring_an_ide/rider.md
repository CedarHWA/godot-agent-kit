> Source: https://docs.godotengine.org/en/4.7/engine_details/development/configuring_an_ide/rider.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="jetbrains-rider"></a>

<a id="doc-configuring-an-ide-rider"></a>

# JetBrains Rider

[JetBrains Rider](https://www.jetbrains.com/rider/) is a commercial
[JetBrains](https://www.jetbrains.com/) IDE for C++, C# and GDScript that uses the same solution system as Visual Studio.

Note

This documentation is for contributing to the game engine, not for using
JetBrains Rider as a C# or GDScript editor. To code C# or GDScript in an external editor, see
[the C# guide to configure an external editor](../../../tutorials/scripting/c_sharp/c_sharp_basics.md#doc-c-sharp-setup-external-editor).

<a id="importing-the-project"></a>

## Importing the project

Tip

If you already use Visual Studio as your main IDE, you can use the same solution file in Rider.
Rider and Visual Studio use the same solution format, so you can switch between the two IDEs without rebuilding the solution file.
Debug configurations need to be changed when going from one IDE to another.

If you are starting from the scratch, please follow [instructions](../compiling/index.md#doc-compiling-index), specifically:

- Install all the dependencies.
- Figure out the scons command for compiling to target a specific platform.

Provide scons with additional arguments to request a solution file generation:

- Add vsproj=yes dev_build=yes to the scons command

The `vsproj` parameter signals that you want Visual Studio solution generated.
The `dev_build` parameter ensures the debug symbols are included, allowing to e.g. step through code using breakpoints.

Note

Each SCons run only generates the `.generated.props` file for a single
Solution Configuration. Please run SCons once per target you plan to use:

```shell
scons vsproj=yes dev_build=yes target=editor
scons vsproj=yes dev_build=yes target=template_debug
scons vsproj=yes dev_build=yes target=template_release
```

- Open the generated `godot.sln` in Rider.

Note

Ensure that the appropriate Solution configuration is selected on the
Rider toolbar. It affects resolve of the SDKs, code analysis, build, run,
etc.

<a id="compiling-and-debugging-the-project"></a>

## Compiling and debugging the project

Rider comes with a built-in debugger that can be used to debug the Godot project. You can launch the debugger
by pressing the **Debug** icon at the top of the screen, this only works for the Project Manager,
if you want to debug the editor, you need to configure the debugger first.

![../../../_images/rider_run_debug.webp](https://docs.godotengine.org/en/4.7/_images/rider_run_debug.webp)

- Click on the **Godot > Edit Configurations** option at the top of the screen.

![../../../_images/rider_configurations.webp](https://docs.godotengine.org/en/4.7/_images/rider_configurations.webp)

- Ensure the following values for the C++ Project Run Configuration:

  > - Exe Path : `$(LocalDebuggerCommand)`
  > - Program Arguments: `-e --path <path to the Godot project>`
  > - Working Directory: `$(LocalDebuggerWorkingDirectory)`
  > - Before Launch has a value of "Build Project"

This will tell the executable to debug the specified project without opening the Project Manager.
Use the root path to the project folder, not `project.godot` file path.

![../../../_images/rider_configurations_changed.webp](https://docs.godotengine.org/en/4.7/_images/rider_configurations_changed.webp)

- Finally click on "Apply" and "OK" to save the changes.
- When you press the **Debug** icon at the top of the screen, JetBrains Rider will launch the Godot editor with the debugger attached.

Alternatively you can use **Run > Attach to Process** to attach the debugger to a running Godot instance.

![../../../_images/rider_attach_to_process.webp](https://docs.godotengine.org/en/4.7/_images/rider_attach_to_process.webp)

- You can find the Godot instance by searching for `godot.editor` and then clicking `Attach with LLDB`

![../../../_images/rider_attach_to_process_dialog.webp](https://docs.godotengine.org/en/4.7/_images/rider_attach_to_process_dialog.webp)

<a id="debug-visualizers"></a>

## Debug visualizers

Debug visualizers customize how complex data structures are displayed during debugging.
The "natvis" (short for "Native Visualization") files built-in with Godot are automatically used.

Note

On macOS and Linux, natvis support requires Rider 2026.2 or later.

<a id="unit-testing"></a>

## Unit testing

Leverage Rider [doctest](../../architecture/unit_testing.md#doc-unit-testing) support.
Please refer to [the instructions](https://github.com/JetBrains/godot-support/wiki/Godot-doctest-Unit-Tests).

<a id="profiling"></a>

## Profiling

Please refer to [the profiling instructions](https://github.com/JetBrains/godot-support/wiki/Profiling-Godot-engine-(native-code)-with-dotTrace-or-JetBrains-Rider).

Please consult the [JetBrains Rider documentation](https://www.jetbrains.com/rider/documentation/) for any specific information about the JetBrains IDE.

<a id="known-issues"></a>

## Known issues

Debugging Windows MinGV build - symbols are not loaded. Reported [RIDER-106816](https://youtrack.jetbrains.com/issue/RIDER-106816/Upgrade-LLDB-to-actual-version).
