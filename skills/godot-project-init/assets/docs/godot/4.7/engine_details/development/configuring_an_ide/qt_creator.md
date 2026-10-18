> Source: https://docs.godotengine.org/en/4.7/engine_details/development/configuring_an_ide/qt_creator.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="qt-creator"></a>

<a id="doc-configuring-an-ide-qtcreator"></a>

# Qt Creator

[Qt Creator](https://doc.qt.io/qtcreator/index.html) is a free, open source IDE for all desktop platforms.

<a id="importing-the-project"></a>

## Importing the project

- From the Qt Creator's main screen select **New Project > Import Project > Import Existing Project**.

![../../../_images/qtcreator-new-project.png](https://docs.godotengine.org/en/4.7/_images/qtcreator-new-project.png)

- Under **Location** select the Godot root folder.

![../../../_images/qtcreator-set-project-path.png](https://docs.godotengine.org/en/4.7/_images/qtcreator-set-project-path.png)

- Next, you can choose which folders and files will be visible to the project.
  While C/C++ files are added automatically, other extensions can be potentially useful:
  `*.glsl` for shader files, `*.py` for buildsystem files,
  `*.java` for Android platform development, `*.mm` for macOS platform development.

![../../../_images/qtcreator-apply-import-filter.png](https://docs.godotengine.org/en/4.7/_images/qtcreator-apply-import-filter.png)

Note

You can change this configuration later by right-clicking on your project
and selecting the **Edit Files...** option.

![../../../_images/qtcreator-edit-files-menu.png](https://docs.godotengine.org/en/4.7/_images/qtcreator-edit-files-menu.png)

- Finish the import.
- Open the `project_name.includes` file and add a line containing `.` to it
  to correctly enable the code completion.

![../../../_images/qtcreator-project-name-includes.png](https://docs.godotengine.org/en/4.7/_images/qtcreator-project-name-includes.png)

- From the left-side menu select **Projects** and open the **Build** tab.
- Delete the predefined `make` build step.

![../../../_images/qtcreator-projects-build.png](https://docs.godotengine.org/en/4.7/_images/qtcreator-projects-build.png)

- Click **Add Build Step > Custom Process Step** to add a new build step
  with the following settings:

  |  |  |
  | --- | --- |
  | Command | **scons** |
  | Arguments | See [Introduction to the buildsystem](../compiling/introduction_to_the_buildsystem.md#doc-introduction-to-the-buildsystem) for a full list of arguments. |

![../../../_images/qtcreator-set-scons-command.png](https://docs.godotengine.org/en/4.7/_images/qtcreator-set-scons-command.png)

Note

If the build fails with `Could not start process "scons"`, it can mean that `scons`
is not in your `PATH` environment variable. In this case, you'll have to specify the
full path to the SCons binary.

<a id="debugging-the-project"></a>

## Debugging the project

- From the left-side menu select **Projects** and open the **Run** tab.
- Under **Executable** specify the path to your executable located in
  the `<Godot root directory>/bin` folder. The name depends on your build configuration,
  e.g. `godot.linuxbsd.editor.dev.x86_64` for 64-bit LinuxBSD platform with
  `platform=editor` and `dev_build=yes`.
  You can use `%{buildDir}` to reference the project root, e.g: `%{buildDir}/bin/godot.linuxbsd.editor.dev.x86_64`.
- If you want to run a specific project, specify its root folder under **Working directory**.
- If you want to run the editor, add `-e` to the **Command line arguments** field.

![../../../_images/qtcreator-run-command.png](https://docs.godotengine.org/en/4.7/_images/qtcreator-run-command.png)

To learn more about command line arguments, refer to the
[command line tutorial](../../../tutorials/editor/command_line_tutorial.md#doc-command-line-tutorial).

<a id="code-style-configuration"></a>

## Code style configuration

Developers must follow the project's [code style](https://contributing.godotengine.org/en/latest/engine/guidelines/code_style.html)
and the IDE should help them follow it. By default, Qt Creator uses spaces
for indentation which doesn't match the Godot code style guidelines. You can
change this behavior by changing the **Code Style** in **Tools > Options > C++**.

![../../../_images/qtcreator-options-cpp.png](https://docs.godotengine.org/en/4.7/_images/qtcreator-options-cpp.png)

Click on **Edit** to change the current settings, then click on
**Copy Built-in Code Style** button to set a new code style. Set a name for it
(e.g. Godot) and change the Tab policy to be **Tabs Only**.

![../../../_images/qtcreator-edit-codestyle.png](https://docs.godotengine.org/en/4.7/_images/qtcreator-edit-codestyle.png)

If you run into any issues, ask for help in one of
[Godot's community channels](https://godotengine.org/community).
