> Source: https://docs.godotengine.org/en/4.7/engine_details/development/debugging/vulkan/vulkan_validation_layers.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="validation-layers"></a>

<a id="doc-vulkan-validation-layers"></a>

# Validation layers

Validation layers enable developers to verify their application's correct use of
the Vulkan API. Validation layers can be enabled in both debug and release
builds, including in exported projects.

Note

Enabling validation layers has a performance impact, so only enable them
when you actually need the output to debug the application.

<a id="windows"></a>

## Windows

Install the Vulkan SDK <https://vulkan.lunarg.com/sdk/home>, which contains
validation layers as part of its default installation. No need to enable any
optional features in the installer; installing the core Vulkan SDK suffices. You
don't need to reboot after installing the SDK, but you may need to close and
reopen your current terminal.

After installing the Vulkan SDK, run Godot with the `--gpu-validation`
[command line argument](../../../../tutorials/editor/command_line_tutorial.md#doc-command-line-tutorial). You can also specify
`--gpu-abort` which will make Godot quit as soon as a validation error happens.
This can prevent your system from freezing if a validation error occurs.

<a id="macos"></a>

## macOS

Warning

Official Godot macOS builds do **not** support validation layers, as these
are statically linked against the Vulkan SDK. Dynamic linking must be used
instead.

In practice, this means that using validation layers on macOS **requires**
you to use a Godot build compiled with the `use_volk=yes` SCons option.
[Compiling for macOS](../../compiling/compiling_for_macos.md#doc-compiling-for-macos). If testing validation layers on an exported
project, you must recompile the export template and specify it as a custom
export template in your project's macOS export preset.

Install the Vulkan SDK <https://vulkan.lunarg.com/sdk/home>, which contains
validation layers as part of its default installation. No need to enable any
optional features in the installer; installing the core Vulkan SDK suffices. You
don't need to reboot after installing the SDK, but you may need to close and
reopen your current terminal.

After installing the Vulkan SDK, run a Godot binary that was compiled with
`use_volk=yes` SCons option. Specify the `--gpu-validation`
[command line argument](../../../../tutorials/editor/command_line_tutorial.md#doc-command-line-tutorial).
You can also specify `--gpu-abort` which will make Godot quit as soon
as a validation error happens. This can prevent your system from freezing
if a validation error occurs.

<a id="linux-bsd"></a>

## Linux, \*BSD

Install Vulkan validation layers from your distribution's repositories:

```gdscript
vulkan-validation-layers
```

```gdscript
pacman -S vulkan-validation-layers
```

```gdscript
apt install vulkan-validationlayers
```

```gdscript
dnf install vulkan-validation-layers
```

```gdscript
pkg install graphics/vulkan-validation-layers
```

```gdscript
emerge -an media-libs/vulkan-layers
```

```gdscript
urpmi vulkan-validation-layers
```

```gdscript
pkg_add graphics/vulkan-validation-layers
```

```gdscript
zypper install vulkan-validationlayers
```

```gdscript
eopkg install -c vulkan-validation-layers
```

You don't need to reboot after installing the validation layers, but you may
need to close and reopen your current terminal.

After installing the package, run Godot with the `--gpu-validation`
[command line argument](../../../../tutorials/editor/command_line_tutorial.md#doc-command-line-tutorial). You can also specify
`--gpu-abort` which will make Godot quit as soon as a validation error happens.
This can prevent your system from freezing if a validation error occurs.

<a id="ios"></a>

## iOS

Validation layers are currently **not** supported on iOS.

<a id="web"></a>

## Web

Validation layers are **not** supported on the web platform, as there is no support
for Vulkan there.

<a id="android"></a>

<a id="doc-vulkan-validation-layers-android"></a>

## Android

After enabling validation layers on Android, a developer can see errors and
warning messages in the `adb logcat` output.

<a id="enabling-validation-layers"></a>

### Enabling validation layers

<a id="build-validation-layers-from-official-sources"></a>

#### Build validation layers from official sources

To build Android libraries, follow the instructions on
[Khronos' repository](https://github.com/KhronosGroup/Vulkan-ValidationLayers/blob/master/BUILD.md#building-on-android).
After a successful build, the libraries will be located in `Vulkan-ValidationLayers/build-android/libs`.

<a id="copy-libraries"></a>

#### Copy libraries

Copy libraries from `Vulkan-ValidationLayers/build-android/libs` to
`godot/platform/android/java/app/libs/debug/vulkan_validation_layers`.

Your Godot source directory tree should look like on the example below:

```gdscript
godot
|-- platform
    |-- android
        |-- java
            |-- app
                |-- libs
                    |-- debug
                        |-- vulkan_validation_layers
                            |-- arm64-v8a
                            |-- armeabi-v7a
                            |-- x86
                            |-- x86_64
```

If the subdirectory `libs/debug/vulkan_validation_layers` doesn't exist, create it.

<a id="compile-and-run-the-android-app"></a>

#### Compile and run the Android app

Linked validation layers are automatically loaded and enabled in Android debug builds.
You can use Godot's [One-click deploy](../../../../tutorials/export/one-click_deploy.md#doc-one-click-deploy) feature to quickly test your project with the validation layers enabled.
