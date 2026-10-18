> Source: https://docs.godotengine.org/en/4.7/classes/class_editorfeatureprofile.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="editorfeatureprofile"></a>

<a id="class-editorfeatureprofile"></a>

# EditorFeatureProfile

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

An editor feature profile which can be used to disable specific features.

<a id="description"></a>

## Description

An editor feature profile can be used to disable specific features of the Godot editor. When disabled, the features won't appear in the editor, which makes the editor less cluttered. This is useful in education settings to reduce confusion or when working in a team. For example, artists and level designers could use a feature profile that disables the script editor to avoid accidentally making changes to files they aren't supposed to edit.

To manage editor feature profiles visually, use **Editor > Manage Feature Profiles...** at the top of the editor window.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [String](class_string.md#class-string) | [get_feature_name](class_editorfeatureprofile.md#class-editorfeatureprofile-method-get-feature-name)(feature: [Feature](class_editorfeatureprofile.md#enum-editorfeatureprofile-feature)) |
| [bool](class_bool.md#class-bool) | [is_class_disabled](class_editorfeatureprofile.md#class-editorfeatureprofile-method-is-class-disabled)(class_name: [StringName](class_stringname.md#class-stringname)) const |
| [bool](class_bool.md#class-bool) | [is_class_editor_disabled](class_editorfeatureprofile.md#class-editorfeatureprofile-method-is-class-editor-disabled)(class_name: [StringName](class_stringname.md#class-stringname)) const |
| [bool](class_bool.md#class-bool) | [is_class_property_disabled](class_editorfeatureprofile.md#class-editorfeatureprofile-method-is-class-property-disabled)(class_name: [StringName](class_stringname.md#class-stringname), property: [StringName](class_stringname.md#class-stringname)) const |
| [bool](class_bool.md#class-bool) | [is_feature_disabled](class_editorfeatureprofile.md#class-editorfeatureprofile-method-is-feature-disabled)(feature: [Feature](class_editorfeatureprofile.md#enum-editorfeatureprofile-feature)) const |
| [Error](class_@globalscope.md#enum-globalscope-error) | [load_from_file](class_editorfeatureprofile.md#class-editorfeatureprofile-method-load-from-file)(path: [String](class_string.md#class-string)) |
| [Error](class_@globalscope.md#enum-globalscope-error) | [save_to_file](class_editorfeatureprofile.md#class-editorfeatureprofile-method-save-to-file)(path: [String](class_string.md#class-string)) |
| void | [set_disable_class](class_editorfeatureprofile.md#class-editorfeatureprofile-method-set-disable-class)(class_name: [StringName](class_stringname.md#class-stringname), disable: [bool](class_bool.md#class-bool)) |
| void | [set_disable_class_editor](class_editorfeatureprofile.md#class-editorfeatureprofile-method-set-disable-class-editor)(class_name: [StringName](class_stringname.md#class-stringname), disable: [bool](class_bool.md#class-bool)) |
| void | [set_disable_class_property](class_editorfeatureprofile.md#class-editorfeatureprofile-method-set-disable-class-property)(class_name: [StringName](class_stringname.md#class-stringname), property: [StringName](class_stringname.md#class-stringname), disable: [bool](class_bool.md#class-bool)) |
| void | [set_disable_feature](class_editorfeatureprofile.md#class-editorfeatureprofile-method-set-disable-feature)(feature: [Feature](class_editorfeatureprofile.md#enum-editorfeatureprofile-feature), disable: [bool](class_bool.md#class-bool)) |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-editorfeatureprofile-feature"></a>

enum **Feature**: [🔗](class_editorfeatureprofile.md#enum-editorfeatureprofile-feature)

<a id="class-editorfeatureprofile-constant-feature-3d"></a>

[Feature](class_editorfeatureprofile.md#enum-editorfeatureprofile-feature) **FEATURE_3D** = `0`

The 3D editor. If this feature is disabled, the 3D editor won't display but 3D nodes will still display in the Create New Node dialog.

<a id="class-editorfeatureprofile-constant-feature-script"></a>

[Feature](class_editorfeatureprofile.md#enum-editorfeatureprofile-feature) **FEATURE_SCRIPT** = `1`

The Script tab, which contains the script editor and class reference browser. If this feature is disabled, the Script tab won't display.

<a id="class-editorfeatureprofile-constant-feature-asset-lib"></a>

[Feature](class_editorfeatureprofile.md#enum-editorfeatureprofile-feature) **FEATURE_ASSET_LIB** = `2`

The Asset Store tab. If this feature is disabled, the Asset Store tab won't display.

<a id="class-editorfeatureprofile-constant-feature-scene-tree"></a>

[Feature](class_editorfeatureprofile.md#enum-editorfeatureprofile-feature) **FEATURE_SCENE_TREE** = `3`

Scene tree editing. If this feature is disabled, the Scene tree dock will still be visible but will be read-only.

<a id="class-editorfeatureprofile-constant-feature-node-dock"></a>

[Feature](class_editorfeatureprofile.md#enum-editorfeatureprofile-feature) **FEATURE_NODE_DOCK** = `4`

**Deprecated:** Replaced by the Signals and Groups docks.

The Node dock. If this feature is disabled, signals and groups won't be visible and modifiable from the editor.

<a id="class-editorfeatureprofile-constant-feature-filesystem-dock"></a>

[Feature](class_editorfeatureprofile.md#enum-editorfeatureprofile-feature) **FEATURE_FILESYSTEM_DOCK** = `5`

The FileSystem dock. If this feature is disabled, the FileSystem dock won't be visible.

<a id="class-editorfeatureprofile-constant-feature-import-dock"></a>

[Feature](class_editorfeatureprofile.md#enum-editorfeatureprofile-feature) **FEATURE_IMPORT_DOCK** = `6`

The Import dock. If this feature is disabled, the Import dock won't be visible.

<a id="class-editorfeatureprofile-constant-feature-history-dock"></a>

[Feature](class_editorfeatureprofile.md#enum-editorfeatureprofile-feature) **FEATURE_HISTORY_DOCK** = `7`

The History dock. If this feature is disabled, the History dock won't be visible.

<a id="class-editorfeatureprofile-constant-feature-game"></a>

[Feature](class_editorfeatureprofile.md#enum-editorfeatureprofile-feature) **FEATURE_GAME** = `8`

The Game tab, which allows embedding the game window and selecting nodes by clicking inside of it. If this feature is disabled, the Game tab won't display.

<a id="class-editorfeatureprofile-constant-feature-signals-dock"></a>

[Feature](class_editorfeatureprofile.md#enum-editorfeatureprofile-feature) **FEATURE_SIGNALS_DOCK** = `9`

The Signals dock. If this feature is disabled, signals won't be visible and modifiable from the editor.

<a id="class-editorfeatureprofile-constant-feature-groups-dock"></a>

[Feature](class_editorfeatureprofile.md#enum-editorfeatureprofile-feature) **FEATURE_GROUPS_DOCK** = `10`

The Groups dock. If this feature is disabled, groups won't be visible and modifiable from the editor.

<a id="class-editorfeatureprofile-constant-feature-max"></a>

[Feature](class_editorfeatureprofile.md#enum-editorfeatureprofile-feature) **FEATURE_MAX** = `11`

Represents the size of the [Feature](class_editorfeatureprofile.md#enum-editorfeatureprofile-feature) enum.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-editorfeatureprofile-method-get-feature-name"></a>

[String](class_string.md#class-string) **get_feature_name**(feature: [Feature](class_editorfeatureprofile.md#enum-editorfeatureprofile-feature)) [🔗](class_editorfeatureprofile.md#class-editorfeatureprofile-method-get-feature-name)

Returns the specified `feature`'s human-readable name.

---


<a id="class-editorfeatureprofile-method-is-class-disabled"></a>

[bool](class_bool.md#class-bool) **is_class_disabled**(class_name: [StringName](class_stringname.md#class-stringname)) const [🔗](class_editorfeatureprofile.md#class-editorfeatureprofile-method-is-class-disabled)

Returns `true` if the class specified by `class_name` is disabled. When disabled, the class won't appear in the Create New Node dialog.

---


<a id="class-editorfeatureprofile-method-is-class-editor-disabled"></a>

[bool](class_bool.md#class-bool) **is_class_editor_disabled**(class_name: [StringName](class_stringname.md#class-stringname)) const [🔗](class_editorfeatureprofile.md#class-editorfeatureprofile-method-is-class-editor-disabled)

Returns `true` if editing for the class specified by `class_name` is disabled. When disabled, the class will still appear in the Create New Node dialog but the Inspector will be read-only when selecting a node that extends the class.

---


<a id="class-editorfeatureprofile-method-is-class-property-disabled"></a>

[bool](class_bool.md#class-bool) **is_class_property_disabled**(class_name: [StringName](class_stringname.md#class-stringname), property: [StringName](class_stringname.md#class-stringname)) const [🔗](class_editorfeatureprofile.md#class-editorfeatureprofile-method-is-class-property-disabled)

Returns `true` if `property` is disabled in the class specified by `class_name`. When a property is disabled, it won't appear in the Inspector when selecting a node that extends the class specified by `class_name`.

---


<a id="class-editorfeatureprofile-method-is-feature-disabled"></a>

[bool](class_bool.md#class-bool) **is_feature_disabled**(feature: [Feature](class_editorfeatureprofile.md#enum-editorfeatureprofile-feature)) const [🔗](class_editorfeatureprofile.md#class-editorfeatureprofile-method-is-feature-disabled)

Returns `true` if the `feature` is disabled. When a feature is disabled, it will disappear from the editor entirely.

---


<a id="class-editorfeatureprofile-method-load-from-file"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **load_from_file**(path: [String](class_string.md#class-string)) [🔗](class_editorfeatureprofile.md#class-editorfeatureprofile-method-load-from-file)

Loads an editor feature profile from a file. The file must follow the JSON format obtained by using the feature profile manager's **Export** button or the [save_to_file()](class_editorfeatureprofile.md#class-editorfeatureprofile-method-save-to-file) method.

**Note:** Feature profiles created via the user interface are loaded from the `feature_profiles` directory, as a file with the `.profile` extension. The editor configuration folder can be found by using [EditorPaths.get_config_dir()](class_editorpaths.md#class-editorpaths-method-get-config-dir).

---


<a id="class-editorfeatureprofile-method-save-to-file"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **save_to_file**(path: [String](class_string.md#class-string)) [🔗](class_editorfeatureprofile.md#class-editorfeatureprofile-method-save-to-file)

Saves the editor feature profile to a file in JSON format. It can then be imported using the feature profile manager's **Import** button or the [load_from_file()](class_editorfeatureprofile.md#class-editorfeatureprofile-method-load-from-file) method.

**Note:** Feature profiles created via the user interface are saved in the `feature_profiles` directory, as a file with the `.profile` extension. The editor configuration folder can be found by using [EditorPaths.get_config_dir()](class_editorpaths.md#class-editorpaths-method-get-config-dir).

---


<a id="class-editorfeatureprofile-method-set-disable-class"></a>

void **set_disable_class**(class_name: [StringName](class_stringname.md#class-stringname), disable: [bool](class_bool.md#class-bool)) [🔗](class_editorfeatureprofile.md#class-editorfeatureprofile-method-set-disable-class)

If `disable` is `true`, disables the class specified by `class_name`. When disabled, the class won't appear in the Create New Node dialog.

---


<a id="class-editorfeatureprofile-method-set-disable-class-editor"></a>

void **set_disable_class_editor**(class_name: [StringName](class_stringname.md#class-stringname), disable: [bool](class_bool.md#class-bool)) [🔗](class_editorfeatureprofile.md#class-editorfeatureprofile-method-set-disable-class-editor)

If `disable` is `true`, disables editing for the class specified by `class_name`. When disabled, the class will still appear in the Create New Node dialog but the Inspector will be read-only when selecting a node that extends the class.

---


<a id="class-editorfeatureprofile-method-set-disable-class-property"></a>

void **set_disable_class_property**(class_name: [StringName](class_stringname.md#class-stringname), property: [StringName](class_stringname.md#class-stringname), disable: [bool](class_bool.md#class-bool)) [🔗](class_editorfeatureprofile.md#class-editorfeatureprofile-method-set-disable-class-property)

If `disable` is `true`, disables editing for `property` in the class specified by `class_name`. When a property is disabled, it won't appear in the Inspector when selecting a node that extends the class specified by `class_name`.

---


<a id="class-editorfeatureprofile-method-set-disable-feature"></a>

void **set_disable_feature**(feature: [Feature](class_editorfeatureprofile.md#enum-editorfeatureprofile-feature), disable: [bool](class_bool.md#class-bool)) [🔗](class_editorfeatureprofile.md#class-editorfeatureprofile-method-set-disable-feature)

If `disable` is `true`, disables the editor feature specified in `feature`. When a feature is disabled, it will disappear from the editor entirely.
