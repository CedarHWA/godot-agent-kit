> Source: https://docs.godotengine.org/en/4.7/engine_details/development/compiling/compiling_for_ios.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="compiling-for-ios"></a>

<a id="doc-compiling-for-ios"></a>

# Compiling for iOS

See also

This page describes how to compile iOS export template binaries from source.
If you're looking to export your project to iOS instead, read [Exporting for iOS](../../../tutorials/export/exporting_for_ios.md#doc-exporting-for-ios).

<a id="requirements"></a>

## Requirements

- [Python 3.9+](https://www.python.org/downloads/macos/).
- [SCons 4.4+](https://scons.org/pages/download.html) build system.
- [Xcode](https://apps.apple.com/us/app/xcode/id497799835).
  :   - Launch Xcode once and install iOS support. If you have already launched
        Xcode and need to install iOS support, go to *Xcode -> Settings... -> Platforms*.
      - Go to *Xcode -> Settings... -> Locations -> Command Line Tools* and select
        an installed version. Even if one is already selected, re-select it.
- Download and follow README instructions to build a static `.xcframework`
  from the [MoltenVK SDK](https://github.com/KhronosGroup/MoltenVK#fetching-moltenvk-source-code).

Note

If you have [Homebrew](https://brew.sh/) installed, you can easily
install SCons using the following command:

```shell
brew install scons
```

Installing Homebrew will also fetch the Command Line Tools
for Xcode automatically if you don't have them already.

Similarly, if you have [MacPorts](https://www.macports.org/)
installed, you can easily install SCons using the
following command:

```shell
sudo port install scons
```

See also

To get the Godot source code for compiling, see
[Getting the source](getting_source.md#doc-getting-source).

For a general overview of SCons usage for Godot, see
[Introduction to the buildsystem](introduction_to_the_buildsystem.md#doc-introduction-to-the-buildsystem).

<a id="compiling"></a>

## Compiling

Open a Terminal, go to the root folder of the engine source code and type
the following to compile a debug build:

```shell
scons platform=ios target=template_debug generate_bundle=yes
```

To compile a release build:

```shell
scons platform=ios target=template_release generate_bundle=yes
```

To create an Xcode project like in the official builds, you need to use the
template located in `misc/dist/apple_embedded_xcode`. The release and debug libraries
should be placed in `libgodot.ios.debug.xcframework` and
`libgodot.ios.release.xcframework` respectively. Camera module libraries
should be placed in `libgodot_camera.ios.debug.xcframework` and
`libgodot_camera.ios.release.xcframework`. This process can be automated
by using the `generate_bundle=yes` option on the *last* SCons command used to
build export templates (so that all binaries can be included).

The MoltenVK static `.xcframework` folder must also be placed in the
`apple_embedded_xcode` folder once it has been created. MoltenVK is always statically
linked on iOS; there is no dynamic linking option available, unlike macOS.

Warning

The iOS simulator only supports the `Compatibility` renderer.

Apple Silicon Macs can run iOS apps natively, so you can run exported iOS projects
directly on an Apple Silicon Mac without iOS simulator limitations.

<a id="run"></a>

## Run

To run on a device, follow these instructions:
[Exporting for iOS](../../../tutorials/export/exporting_for_ios.md#doc-exporting-for-ios).

iOS exports can run directly on an Apple Silicon Mac. To run exported iOS project
on Mac, open exported project in Xcode and select `My Mac` in the `Run Destinations`
dropdown.

<a id="troubleshooting"></a>

## Troubleshooting

<a id="fatal-error-cstdint-file-not-found"></a>

### Fatal error: 'cstdint' file not found

If you get a compilation error of this form early on, it's likely because
the Xcode command line tools installation needs to be repaired after
a macOS or Xcode update:

```shell
./core/typedefs.h:45:10: fatal error: 'cstdint' file not found
45 | #include <cstdint>
   |          ^~~~~~~~~
```

Run these two commands to reinstall Xcode command line tools
(enter your administrator password as needed):

```shell
sudo rm -rf /Library/Developer/CommandLineTools
sudo xcode-select --install
```

If it still does not work, try updating Xcode from the Mac App Store and try again.
