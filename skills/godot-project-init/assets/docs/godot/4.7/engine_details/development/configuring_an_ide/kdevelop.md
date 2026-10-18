> Source: https://docs.godotengine.org/en/4.7/engine_details/development/configuring_an_ide/kdevelop.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="kdevelop"></a>

<a id="doc-configuring-an-ide-kdevelop"></a>

# KDevelop

[KDevelop](https://www.kdevelop.org) is a free, open source IDE for all desktop platforms.

<a id="importing-the-project"></a>

## Importing the project

- From the KDevelop's main screen select **Open Project**.

<a id="id2"></a>
![../../../_images/kdevelop_newproject.webp](https://docs.godotengine.org/en/4.7/_images/kdevelop_newproject.webp)


KDevelop's main screen.

- Navigate to the Godot root folder and select it.
- On the next screen, choose **Custom Build System** for the **Project Manager**.

![../../../_images/kdevelop_custombuild.webp](https://docs.godotengine.org/en/4.7/_images/kdevelop_custombuild.webp)

- After the project has been imported, open the project configuration by right-clicking
  on it in the **Projects** panel and selecting **Open Configuration..** option.

![../../../_images/kdevelop_openconfig.webp](https://docs.godotengine.org/en/4.7/_images/kdevelop_openconfig.webp)

- Under **Language Support** open the **Includes/Imports** tab and add the following paths:

  ```none
  .  // A dot, to indicate the root of the Godot project
  core/
  core/os/
  core/math/
  drivers/
  platform/<your_platform>/  // Replace <your_platform> with a folder
                                corresponding to your current platform
  ```

![../../../_images/kdevelop_addincludes.webp](https://docs.godotengine.org/en/4.7/_images/kdevelop_addincludes.webp)

- Apply the changes.
- Under **Custom Build System** add a new build configuration with the following settings:

  |  |  |
  | --- | --- |
  | Build Directory | *blank* |
  | Enable | **True** |
  | Executable | **scons** |
  | Arguments | See [Introduction to the buildsystem](../compiling/introduction_to_the_buildsystem.md#doc-introduction-to-the-buildsystem) for a full list of arguments. |

![../../../_images/kdevelop_buildconfig.webp](https://docs.godotengine.org/en/4.7/_images/kdevelop_buildconfig.webp)

- Apply the changes and close the configuration window.

<a id="debugging-the-project"></a>

## Debugging the project

- Select **Run > Configure Launches...** from the top menu.

![../../../_images/kdevelop_configlaunches.webp](https://docs.godotengine.org/en/4.7/_images/kdevelop_configlaunches.webp)

- Click **Add** to create a new launch configuration.
- Select **Executable** option and specify the path to your executable located in
  the `<Godot root directory>/bin` folder. The name depends on your build configuration,
  e.g. `godot.linuxbsd.editor.dev.x86_64` for 64-bit LinuxBSD platform with
  `platform=linuxbsd`, `target=editor`, and `dev_build=yes`.

![../../../_images/kdevelop_configlaunches2.webp](https://docs.godotengine.org/en/4.7/_images/kdevelop_configlaunches2.webp)

If you run into any issues, ask for help in one of
[Godot's community channels](https://godotengine.org/community).
