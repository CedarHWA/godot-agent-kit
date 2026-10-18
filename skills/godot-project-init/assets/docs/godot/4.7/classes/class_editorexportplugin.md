> Source: https://docs.godotengine.org/en/4.7/classes/class_editorexportplugin.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="editorexportplugin"></a>

<a id="class-editorexportplugin"></a>

# EditorExportPlugin

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A script that is executed when exporting the project.

<a id="description"></a>

## Description

**EditorExportPlugin**s are automatically invoked whenever the user exports the project. They can be used to modify scenes and resources during project export based on what [Feature Tags](../tutorials/export/feature_tags.md) are set. For each plugin, [_export_begin()](class_editorexportplugin.md#class-editorexportplugin-private-method-export-begin) is called at the beginning of the export process and then [_export_file()](class_editorexportplugin.md#class-editorexportplugin-private-method-export-file) is called for each exported file.

Register a **EditorExportPlugin** by creating a new [EditorPlugin](class_editorplugin.md#class-editorplugin) and calling its [EditorPlugin.add_export_plugin()](class_editorplugin.md#class-editorplugin-method-add-export-plugin) method.

<a id="tutorials"></a>

## Tutorials

- [Export Android plugins](../tutorials/platform/android/android_plugin.md)

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [_begin_customize_resources](class_editorexportplugin.md#class-editorexportplugin-private-method-begin-customize-resources)(platform: [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform), features: [PackedStringArray](class_packedstringarray.md#class-packedstringarray)) virtual const |
| [bool](class_bool.md#class-bool) | [_begin_customize_scenes](class_editorexportplugin.md#class-editorexportplugin-private-method-begin-customize-scenes)(platform: [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform), features: [PackedStringArray](class_packedstringarray.md#class-packedstringarray)) virtual const |
| [Resource](class_resource.md#class-resource) | [_customize_resource](class_editorexportplugin.md#class-editorexportplugin-private-method-customize-resource)(resource: [Resource](class_resource.md#class-resource), path: [String](class_string.md#class-string)) virtual required |
| [Node](class_node.md#class-node) | [_customize_scene](class_editorexportplugin.md#class-editorexportplugin-private-method-customize-scene)(scene: [Node](class_node.md#class-node), path: [String](class_string.md#class-string)) virtual required |
| void | [_end_customize_resources](class_editorexportplugin.md#class-editorexportplugin-private-method-end-customize-resources)() virtual |
| void | [_end_customize_scenes](class_editorexportplugin.md#class-editorexportplugin-private-method-end-customize-scenes)() virtual |
| void | [_end_generate_apple_embedded_project](class_editorexportplugin.md#class-editorexportplugin-private-method-end-generate-apple-embedded-project)(path: [String](class_string.md#class-string), will_build_archive: [bool](class_bool.md#class-bool)) virtual |
| void | [_export_begin](class_editorexportplugin.md#class-editorexportplugin-private-method-export-begin)(features: [PackedStringArray](class_packedstringarray.md#class-packedstringarray), is_debug: [bool](class_bool.md#class-bool), path: [String](class_string.md#class-string), flags: [int](class_int.md#class-int)) virtual |
| void | [_export_end](class_editorexportplugin.md#class-editorexportplugin-private-method-export-end)() virtual |
| void | [_export_file](class_editorexportplugin.md#class-editorexportplugin-private-method-export-file)(path: [String](class_string.md#class-string), type: [String](class_string.md#class-string), features: [PackedStringArray](class_packedstringarray.md#class-packedstringarray)) virtual |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [_get_android_dependencies](class_editorexportplugin.md#class-editorexportplugin-private-method-get-android-dependencies)(platform: [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform), debug: [bool](class_bool.md#class-bool)) virtual const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [_get_android_dependencies_maven_repos](class_editorexportplugin.md#class-editorexportplugin-private-method-get-android-dependencies-maven-repos)(platform: [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform), debug: [bool](class_bool.md#class-bool)) virtual const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [_get_android_libraries](class_editorexportplugin.md#class-editorexportplugin-private-method-get-android-libraries)(platform: [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform), debug: [bool](class_bool.md#class-bool)) virtual const |
| [String](class_string.md#class-string) | [_get_android_manifest_activity_element_contents](class_editorexportplugin.md#class-editorexportplugin-private-method-get-android-manifest-activity-element-contents)(platform: [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform), debug: [bool](class_bool.md#class-bool)) virtual const |
| [String](class_string.md#class-string) | [_get_android_manifest_application_element_contents](class_editorexportplugin.md#class-editorexportplugin-private-method-get-android-manifest-application-element-contents)(platform: [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform), debug: [bool](class_bool.md#class-bool)) virtual const |
| [String](class_string.md#class-string) | [_get_android_manifest_element_contents](class_editorexportplugin.md#class-editorexportplugin-private-method-get-android-manifest-element-contents)(platform: [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform), debug: [bool](class_bool.md#class-bool)) virtual const |
| [int](class_int.md#class-int) | [_get_customization_configuration_hash](class_editorexportplugin.md#class-editorexportplugin-private-method-get-customization-configuration-hash)() virtual required const |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [_get_export_features](class_editorexportplugin.md#class-editorexportplugin-private-method-get-export-features)(platform: [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform), debug: [bool](class_bool.md#class-bool)) virtual const |
| [bool](class_bool.md#class-bool) | [_get_export_option_visibility](class_editorexportplugin.md#class-editorexportplugin-private-method-get-export-option-visibility)(platform: [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform), option: [String](class_string.md#class-string)) virtual const |
| [String](class_string.md#class-string) | [_get_export_option_warning](class_editorexportplugin.md#class-editorexportplugin-private-method-get-export-option-warning)(platform: [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform), option: [String](class_string.md#class-string)) virtual const |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | [_get_export_options](class_editorexportplugin.md#class-editorexportplugin-private-method-get-export-options)(platform: [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform)) virtual const |
| [Dictionary](class_dictionary.md#class-dictionary) | [_get_export_options_overrides](class_editorexportplugin.md#class-editorexportplugin-private-method-get-export-options-overrides)(platform: [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform)) virtual const |
| [String](class_string.md#class-string) | [_get_name](class_editorexportplugin.md#class-editorexportplugin-private-method-get-name)() virtual required const |
| [bool](class_bool.md#class-bool) | [_should_update_export_options](class_editorexportplugin.md#class-editorexportplugin-private-method-should-update-export-options)(platform: [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform)) virtual const |
| [bool](class_bool.md#class-bool) | [_supports_platform](class_editorexportplugin.md#class-editorexportplugin-private-method-supports-platform)(platform: [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform)) virtual const |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray) | [_update_android_prebuilt_manifest](class_editorexportplugin.md#class-editorexportplugin-private-method-update-android-prebuilt-manifest)(platform: [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform), manifest_data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray)) virtual const |
| void | [add_apple_embedded_platform_bundle_file](class_editorexportplugin.md#class-editorexportplugin-method-add-apple-embedded-platform-bundle-file)(path: [String](class_string.md#class-string)) |
| void | [add_apple_embedded_platform_cpp_code](class_editorexportplugin.md#class-editorexportplugin-method-add-apple-embedded-platform-cpp-code)(code: [String](class_string.md#class-string)) |
| void | [add_apple_embedded_platform_embedded_framework](class_editorexportplugin.md#class-editorexportplugin-method-add-apple-embedded-platform-embedded-framework)(path: [String](class_string.md#class-string)) |
| void | [add_apple_embedded_platform_framework](class_editorexportplugin.md#class-editorexportplugin-method-add-apple-embedded-platform-framework)(path: [String](class_string.md#class-string)) |
| void | [add_apple_embedded_platform_linker_flags](class_editorexportplugin.md#class-editorexportplugin-method-add-apple-embedded-platform-linker-flags)(flags: [String](class_string.md#class-string)) |
| void | [add_apple_embedded_platform_plist_content](class_editorexportplugin.md#class-editorexportplugin-method-add-apple-embedded-platform-plist-content)(plist_content: [String](class_string.md#class-string)) |
| void | [add_apple_embedded_platform_project_static_lib](class_editorexportplugin.md#class-editorexportplugin-method-add-apple-embedded-platform-project-static-lib)(path: [String](class_string.md#class-string)) |
| void | [add_file](class_editorexportplugin.md#class-editorexportplugin-method-add-file)(path: [String](class_string.md#class-string), file: [PackedByteArray](class_packedbytearray.md#class-packedbytearray), remap: [bool](class_bool.md#class-bool)) |
| void | [add_ios_bundle_file](class_editorexportplugin.md#class-editorexportplugin-method-add-ios-bundle-file)(path: [String](class_string.md#class-string)) |
| void | [add_ios_cpp_code](class_editorexportplugin.md#class-editorexportplugin-method-add-ios-cpp-code)(code: [String](class_string.md#class-string)) |
| void | [add_ios_embedded_framework](class_editorexportplugin.md#class-editorexportplugin-method-add-ios-embedded-framework)(path: [String](class_string.md#class-string)) |
| void | [add_ios_framework](class_editorexportplugin.md#class-editorexportplugin-method-add-ios-framework)(path: [String](class_string.md#class-string)) |
| void | [add_ios_linker_flags](class_editorexportplugin.md#class-editorexportplugin-method-add-ios-linker-flags)(flags: [String](class_string.md#class-string)) |
| void | [add_ios_plist_content](class_editorexportplugin.md#class-editorexportplugin-method-add-ios-plist-content)(plist_content: [String](class_string.md#class-string)) |
| void | [add_ios_project_static_lib](class_editorexportplugin.md#class-editorexportplugin-method-add-ios-project-static-lib)(path: [String](class_string.md#class-string)) |
| void | [add_macos_plugin_file](class_editorexportplugin.md#class-editorexportplugin-method-add-macos-plugin-file)(path: [String](class_string.md#class-string)) |
| void | [add_shared_object](class_editorexportplugin.md#class-editorexportplugin-method-add-shared-object)(path: [String](class_string.md#class-string), tags: [PackedStringArray](class_packedstringarray.md#class-packedstringarray), target: [String](class_string.md#class-string)) |
| [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform) | [get_export_platform](class_editorexportplugin.md#class-editorexportplugin-method-get-export-platform)() const |
| [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset) | [get_export_preset](class_editorexportplugin.md#class-editorexportplugin-method-get-export-preset)() const |
| [Variant](class_variant.md#class-variant) | [get_option](class_editorexportplugin.md#class-editorexportplugin-method-get-option)(name: [StringName](class_stringname.md#class-stringname)) const |
| void | [skip](class_editorexportplugin.md#class-editorexportplugin-method-skip)() |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-editorexportplugin-private-method-begin-customize-resources"></a>

[bool](class_bool.md#class-bool) **_begin_customize_resources**(platform: [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform), features: [PackedStringArray](class_packedstringarray.md#class-packedstringarray)) virtual const [🔗](class_editorexportplugin.md#class-editorexportplugin-private-method-begin-customize-resources)

Return `true` if this plugin will customize resources based on the platform and features used.

When enabled, [_get_customization_configuration_hash()](class_editorexportplugin.md#class-editorexportplugin-private-method-get-customization-configuration-hash) and [_customize_resource()](class_editorexportplugin.md#class-editorexportplugin-private-method-customize-resource) will be called and must be implemented.

---


<a id="class-editorexportplugin-private-method-begin-customize-scenes"></a>

[bool](class_bool.md#class-bool) **_begin_customize_scenes**(platform: [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform), features: [PackedStringArray](class_packedstringarray.md#class-packedstringarray)) virtual const [🔗](class_editorexportplugin.md#class-editorexportplugin-private-method-begin-customize-scenes)

Return `true` if this plugin will customize scenes based on the platform and features used.

When enabled, [_get_customization_configuration_hash()](class_editorexportplugin.md#class-editorexportplugin-private-method-get-customization-configuration-hash) and [_customize_scene()](class_editorexportplugin.md#class-editorexportplugin-private-method-customize-scene) will be called and must be implemented.

**Note:** [_customize_scene()](class_editorexportplugin.md#class-editorexportplugin-private-method-customize-scene) will only be called for scenes that have been modified since the last export.

---


<a id="class-editorexportplugin-private-method-customize-resource"></a>

[Resource](class_resource.md#class-resource) **_customize_resource**(resource: [Resource](class_resource.md#class-resource), path: [String](class_string.md#class-string)) virtual required [🔗](class_editorexportplugin.md#class-editorexportplugin-private-method-customize-resource)

Customize a resource. If changes are made to it, return the same or a new resource. Otherwise, return `null`. When a new resource is returned, `resource` will be replaced by a copy of the new resource.

The `path` argument is only used when customizing an actual file, otherwise this means that this resource is part of another one and it will be empty.

Implementing this method is required if [_begin_customize_resources()](class_editorexportplugin.md#class-editorexportplugin-private-method-begin-customize-resources) returns `true`.

**Note:** When customizing any of the following types and returning another resource, the other resource should not be skipped using [skip()](class_editorexportplugin.md#class-editorexportplugin-method-skip) in [_export_file()](class_editorexportplugin.md#class-editorexportplugin-private-method-export-file):

- [AtlasTexture](class_atlastexture.md#class-atlastexture)
- [CompressedCubemap](class_compressedcubemap.md#class-compressedcubemap)
- [CompressedCubemapArray](class_compressedcubemaparray.md#class-compressedcubemaparray)
- [CompressedTexture2D](class_compressedtexture2d.md#class-compressedtexture2d)
- [CompressedTexture2DArray](class_compressedtexture2darray.md#class-compressedtexture2darray)
- [CompressedTexture3D](class_compressedtexture3d.md#class-compressedtexture3d)

---


<a id="class-editorexportplugin-private-method-customize-scene"></a>

[Node](class_node.md#class-node) **_customize_scene**(scene: [Node](class_node.md#class-node), path: [String](class_string.md#class-string)) virtual required [🔗](class_editorexportplugin.md#class-editorexportplugin-private-method-customize-scene)

Customize a scene. If changes are made to it, return the same or a new scene. Otherwise, return `null`. If a new scene is returned, it is up to you to dispose of the old one.

Implementing this method is required if [_begin_customize_scenes()](class_editorexportplugin.md#class-editorexportplugin-private-method-begin-customize-scenes) returns `true`.

**Note:** To change a variable in your scene, use the `@export` annotation when declaring it.

---


<a id="class-editorexportplugin-private-method-end-customize-resources"></a>

void **_end_customize_resources**() virtual [🔗](class_editorexportplugin.md#class-editorexportplugin-private-method-end-customize-resources)

This is called when the customization process for resources ends.

---


<a id="class-editorexportplugin-private-method-end-customize-scenes"></a>

void **_end_customize_scenes**() virtual [🔗](class_editorexportplugin.md#class-editorexportplugin-private-method-end-customize-scenes)

This is called when the customization process for scenes ends.

---


<a id="class-editorexportplugin-private-method-end-generate-apple-embedded-project"></a>

void **_end_generate_apple_embedded_project**(path: [String](class_string.md#class-string), will_build_archive: [bool](class_bool.md#class-bool)) virtual [🔗](class_editorexportplugin.md#class-editorexportplugin-private-method-end-generate-apple-embedded-project)

This is called after Xcode project generation, but before it is built.

**Note:** Only supported on iOS and visionOS.

---


<a id="class-editorexportplugin-private-method-export-begin"></a>

void **_export_begin**(features: [PackedStringArray](class_packedstringarray.md#class-packedstringarray), is_debug: [bool](class_bool.md#class-bool), path: [String](class_string.md#class-string), flags: [int](class_int.md#class-int)) virtual [🔗](class_editorexportplugin.md#class-editorexportplugin-private-method-export-begin)

Virtual method to be overridden by the user. It is called when the export starts and provides all information about the export. `features` is the list of features for the export, `is_debug` is `true` for debug builds, `path` is the target path for the exported project. `flags` is only used when running a runnable profile, e.g. when using native run on Android.

---


<a id="class-editorexportplugin-private-method-export-end"></a>

void **_export_end**() virtual [🔗](class_editorexportplugin.md#class-editorexportplugin-private-method-export-end)

Virtual method to be overridden by the user. Called when the export is finished.

---


<a id="class-editorexportplugin-private-method-export-file"></a>

void **_export_file**(path: [String](class_string.md#class-string), type: [String](class_string.md#class-string), features: [PackedStringArray](class_packedstringarray.md#class-packedstringarray)) virtual [🔗](class_editorexportplugin.md#class-editorexportplugin-private-method-export-file)

Virtual method to be overridden by the user. Called for each exported file before [_customize_resource()](class_editorexportplugin.md#class-editorexportplugin-private-method-customize-resource) and [_customize_scene()](class_editorexportplugin.md#class-editorexportplugin-private-method-customize-scene). The arguments can be used to identify the file. `path` is the path of the file, `type` is the [Resource](class_resource.md#class-resource) represented by the file (e.g. [PackedScene](class_packedscene.md#class-packedscene)), and `features` is the list of features for the export.

Calling [skip()](class_editorexportplugin.md#class-editorexportplugin-method-skip) inside this callback will make the file not included in the export.

---


<a id="class-editorexportplugin-private-method-get-android-dependencies"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **_get_android_dependencies**(platform: [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform), debug: [bool](class_bool.md#class-bool)) virtual const [🔗](class_editorexportplugin.md#class-editorexportplugin-private-method-get-android-dependencies)

Virtual method to be overridden by the user. This is called to retrieve the set of Android dependencies provided by this plugin. Each returned Android dependency should have the format of an Android remote binary dependency: `org.godot.example:my-plugin:0.0.0`

For more information see [Android documentation on dependencies](https://developer.android.com/build/dependencies?agpversion=4.1#dependency-types).

**Note:** Only supported on Android and requires [EditorExportPlatformAndroid.gradle_build/use_gradle_build](class_editorexportplatformandroid.md#class-editorexportplatformandroid-property-gradle-build-use-gradle-build) to be enabled.

---


<a id="class-editorexportplugin-private-method-get-android-dependencies-maven-repos"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **_get_android_dependencies_maven_repos**(platform: [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform), debug: [bool](class_bool.md#class-bool)) virtual const [🔗](class_editorexportplugin.md#class-editorexportplugin-private-method-get-android-dependencies-maven-repos)

Virtual method to be overridden by the user. This is called to retrieve the URLs of Maven repositories for the set of Android dependencies provided by this plugin.

For more information see [Gradle documentation on dependency management](https://docs.gradle.org/current/userguide/dependency_management.html#sec:maven_repo).

**Note:** Google's Maven repo and the Maven Central repo are already included by default.

**Note:** Only supported on Android and requires [EditorExportPlatformAndroid.gradle_build/use_gradle_build](class_editorexportplatformandroid.md#class-editorexportplatformandroid-property-gradle-build-use-gradle-build) to be enabled.

---


<a id="class-editorexportplugin-private-method-get-android-libraries"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **_get_android_libraries**(platform: [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform), debug: [bool](class_bool.md#class-bool)) virtual const [🔗](class_editorexportplugin.md#class-editorexportplugin-private-method-get-android-libraries)

Virtual method to be overridden by the user. This is called to retrieve the local paths of the Android libraries archive (AAR) files provided by this plugin.

**Note:** Relative paths **must** be relative to Godot's `res://addons/` directory. For example, an AAR file located under `res://addons/hello_world_plugin/HelloWorld.release.aar` can be returned as an absolute path using `res://addons/hello_world_plugin/HelloWorld.release.aar` or a relative path using `hello_world_plugin/HelloWorld.release.aar`.

**Note:** Only supported on Android and requires [EditorExportPlatformAndroid.gradle_build/use_gradle_build](class_editorexportplatformandroid.md#class-editorexportplatformandroid-property-gradle-build-use-gradle-build) to be enabled.

---


<a id="class-editorexportplugin-private-method-get-android-manifest-activity-element-contents"></a>

[String](class_string.md#class-string) **_get_android_manifest_activity_element_contents**(platform: [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform), debug: [bool](class_bool.md#class-bool)) virtual const [🔗](class_editorexportplugin.md#class-editorexportplugin-private-method-get-android-manifest-activity-element-contents)

Virtual method to be overridden by the user. This is used at export time to update the contents of the `activity` element in the generated Android manifest.

**Note:** Only supported on Android and requires [EditorExportPlatformAndroid.gradle_build/use_gradle_build](class_editorexportplatformandroid.md#class-editorexportplatformandroid-property-gradle-build-use-gradle-build) to be enabled.

---


<a id="class-editorexportplugin-private-method-get-android-manifest-application-element-contents"></a>

[String](class_string.md#class-string) **_get_android_manifest_application_element_contents**(platform: [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform), debug: [bool](class_bool.md#class-bool)) virtual const [🔗](class_editorexportplugin.md#class-editorexportplugin-private-method-get-android-manifest-application-element-contents)

Virtual method to be overridden by the user. This is used at export time to update the contents of the `application` element in the generated Android manifest.

**Note:** Only supported on Android and requires [EditorExportPlatformAndroid.gradle_build/use_gradle_build](class_editorexportplatformandroid.md#class-editorexportplatformandroid-property-gradle-build-use-gradle-build) to be enabled.

---


<a id="class-editorexportplugin-private-method-get-android-manifest-element-contents"></a>

[String](class_string.md#class-string) **_get_android_manifest_element_contents**(platform: [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform), debug: [bool](class_bool.md#class-bool)) virtual const [🔗](class_editorexportplugin.md#class-editorexportplugin-private-method-get-android-manifest-element-contents)

Virtual method to be overridden by the user. This is used at export time to update the contents of the `manifest` element in the generated Android manifest.

**Note:** Only supported on Android and requires [EditorExportPlatformAndroid.gradle_build/use_gradle_build](class_editorexportplatformandroid.md#class-editorexportplatformandroid-property-gradle-build-use-gradle-build) to be enabled.

---


<a id="class-editorexportplugin-private-method-get-customization-configuration-hash"></a>

[int](class_int.md#class-int) **_get_customization_configuration_hash**() virtual required const [🔗](class_editorexportplugin.md#class-editorexportplugin-private-method-get-customization-configuration-hash)

Return a hash based on the configuration passed (for both scenes and resources). This helps keep separate caches for separate export configurations.

Implementing this method is required if [_begin_customize_resources()](class_editorexportplugin.md#class-editorexportplugin-private-method-begin-customize-resources) returns `true`.

**Note:** [_customize_resource()](class_editorexportplugin.md#class-editorexportplugin-private-method-customize-resource) and [_customize_scene()](class_editorexportplugin.md#class-editorexportplugin-private-method-customize-scene) will not be called when the **EditorExportPlugin** script is modified unless this hash changes too.

---


<a id="class-editorexportplugin-private-method-get-export-features"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **_get_export_features**(platform: [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform), debug: [bool](class_bool.md#class-bool)) virtual const [🔗](class_editorexportplugin.md#class-editorexportplugin-private-method-get-export-features)

Return a [PackedStringArray](class_packedstringarray.md#class-packedstringarray) of additional features this preset, for the given `platform`, should have.

---


<a id="class-editorexportplugin-private-method-get-export-option-visibility"></a>

[bool](class_bool.md#class-bool) **_get_export_option_visibility**(platform: [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform), option: [String](class_string.md#class-string)) virtual const [🔗](class_editorexportplugin.md#class-editorexportplugin-private-method-get-export-option-visibility)

Validates `option` and returns the visibility for the specified `platform`. The default implementation returns `true` for all options.

---


<a id="class-editorexportplugin-private-method-get-export-option-warning"></a>

[String](class_string.md#class-string) **_get_export_option_warning**(platform: [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform), option: [String](class_string.md#class-string)) virtual const [🔗](class_editorexportplugin.md#class-editorexportplugin-private-method-get-export-option-warning)

Check the requirements for the given `option` and return a non-empty warning string if they are not met.

**Note:** Use [get_option()](class_editorexportplugin.md#class-editorexportplugin-method-get-option) to check the value of the export options.

---


<a id="class-editorexportplugin-private-method-get-export-options"></a>

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **_get_export_options**(platform: [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform)) virtual const [🔗](class_editorexportplugin.md#class-editorexportplugin-private-method-get-export-options)

Return a list of export options that can be configured for this export plugin.

Each element in the return value is a [Dictionary](class_dictionary.md#class-dictionary) with the following keys:

- `option`: A dictionary with the structure documented by [Object.get_property_list()](class_object.md#class-object-method-get-property-list), but all keys are optional.
- `default_value`: The default value for this option.
- `update_visibility`: An optional boolean value. If set to `true`, the preset will emit [Object.property_list_changed](class_object.md#class-object-signal-property-list-changed) when the option is changed.

---


<a id="class-editorexportplugin-private-method-get-export-options-overrides"></a>

[Dictionary](class_dictionary.md#class-dictionary) **_get_export_options_overrides**(platform: [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform)) virtual const [🔗](class_editorexportplugin.md#class-editorexportplugin-private-method-get-export-options-overrides)

Return a [Dictionary](class_dictionary.md#class-dictionary) of override values for export options, that will be used instead of user-provided values. Overridden options will be hidden from the user interface.

```gdscript
class MyExportPlugin extends EditorExportPlugin:
    func _get_name() -> String:
        return "MyExportPlugin"

    func _supports_platform(platform) -> bool:
        if platform is EditorExportPlatformPC:
            # Run on all desktop platforms including Windows, MacOS and Linux.
            return true
        return false

    func _get_export_options_overrides(platform) -> Dictionary:
        # Override "Embed PCK" to always be enabled.
        return {
            "binary_format/embed_pck": true,
        }
```

---


<a id="class-editorexportplugin-private-method-get-name"></a>

[String](class_string.md#class-string) **_get_name**() virtual required const [🔗](class_editorexportplugin.md#class-editorexportplugin-private-method-get-name)

Return the name identifier of this plugin (for future identification by the exporter). The plugins are sorted by name before exporting.

Implementing this method is required.

---


<a id="class-editorexportplugin-private-method-should-update-export-options"></a>

[bool](class_bool.md#class-bool) **_should_update_export_options**(platform: [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform)) virtual const [🔗](class_editorexportplugin.md#class-editorexportplugin-private-method-should-update-export-options)

Return `true` if the result of [_get_export_options()](class_editorexportplugin.md#class-editorexportplugin-private-method-get-export-options) has changed and the export options of the preset corresponding to `platform` should be updated.

---


<a id="class-editorexportplugin-private-method-supports-platform"></a>

[bool](class_bool.md#class-bool) **_supports_platform**(platform: [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform)) virtual const [🔗](class_editorexportplugin.md#class-editorexportplugin-private-method-supports-platform)

Return `true` if the plugin supports the given `platform`.

---


<a id="class-editorexportplugin-private-method-update-android-prebuilt-manifest"></a>

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **_update_android_prebuilt_manifest**(platform: [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform), manifest_data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray)) virtual const [🔗](class_editorexportplugin.md#class-editorexportplugin-private-method-update-android-prebuilt-manifest)

Provide access to the Android prebuilt manifest and allows the plugin to modify it if needed.

Implementers of this virtual method should take the binary manifest data from `manifest_data`, copy it, modify it, and then return it with the modifications.

If no modifications are needed, then an empty [PackedByteArray](class_packedbytearray.md#class-packedbytearray) should be returned.

---


<a id="class-editorexportplugin-method-add-apple-embedded-platform-bundle-file"></a>

void **add_apple_embedded_platform_bundle_file**(path: [String](class_string.md#class-string)) [🔗](class_editorexportplugin.md#class-editorexportplugin-method-add-apple-embedded-platform-bundle-file)

Adds an Apple embedded platform bundle file from the given `path` to the exported project.

---


<a id="class-editorexportplugin-method-add-apple-embedded-platform-cpp-code"></a>

void **add_apple_embedded_platform_cpp_code**(code: [String](class_string.md#class-string)) [🔗](class_editorexportplugin.md#class-editorexportplugin-method-add-apple-embedded-platform-cpp-code)

Adds C++ code to the Apple embedded platform export. The final code is created from the code appended by each active export plugin.

---


<a id="class-editorexportplugin-method-add-apple-embedded-platform-embedded-framework"></a>

void **add_apple_embedded_platform_embedded_framework**(path: [String](class_string.md#class-string)) [🔗](class_editorexportplugin.md#class-editorexportplugin-method-add-apple-embedded-platform-embedded-framework)

Adds a dynamic library (\*.dylib, \*.framework) to the Linking Phase in the Apple embedded platform's Xcode project and embeds it into the resulting binary.

**Note:** For static libraries (\*.a), this works in the same way as [add_apple_embedded_platform_framework()](class_editorexportplugin.md#class-editorexportplugin-method-add-apple-embedded-platform-framework).

**Note:** This method should not be used for System libraries as they are already present on the device.

---


<a id="class-editorexportplugin-method-add-apple-embedded-platform-framework"></a>

void **add_apple_embedded_platform_framework**(path: [String](class_string.md#class-string)) [🔗](class_editorexportplugin.md#class-editorexportplugin-method-add-apple-embedded-platform-framework)

Adds a static library (\*.a) or a dynamic library (\*.dylib, \*.framework) to the Linking Phase to the Apple embedded platform's Xcode project.

---


<a id="class-editorexportplugin-method-add-apple-embedded-platform-linker-flags"></a>

void **add_apple_embedded_platform_linker_flags**(flags: [String](class_string.md#class-string)) [🔗](class_editorexportplugin.md#class-editorexportplugin-method-add-apple-embedded-platform-linker-flags)

Adds linker flags for the Apple embedded platform export.

---


<a id="class-editorexportplugin-method-add-apple-embedded-platform-plist-content"></a>

void **add_apple_embedded_platform_plist_content**(plist_content: [String](class_string.md#class-string)) [🔗](class_editorexportplugin.md#class-editorexportplugin-method-add-apple-embedded-platform-plist-content)

Adds additional fields to the Apple embedded platform's project Info.plist file.

---


<a id="class-editorexportplugin-method-add-apple-embedded-platform-project-static-lib"></a>

void **add_apple_embedded_platform_project_static_lib**(path: [String](class_string.md#class-string)) [🔗](class_editorexportplugin.md#class-editorexportplugin-method-add-apple-embedded-platform-project-static-lib)

Adds a static library from the given `path` to the Apple embedded platform project.

---


<a id="class-editorexportplugin-method-add-file"></a>

void **add_file**(path: [String](class_string.md#class-string), file: [PackedByteArray](class_packedbytearray.md#class-packedbytearray), remap: [bool](class_bool.md#class-bool)) [🔗](class_editorexportplugin.md#class-editorexportplugin-method-add-file)

Adds a custom file to be exported. `path` is the virtual path that can be used to load the file, `file` is the binary data of the file.

When called inside [_export_file()](class_editorexportplugin.md#class-editorexportplugin-private-method-export-file) and `remap` is `true`, the current file will not be exported, but instead remapped to this custom file. `remap` is ignored when called in other places.

`file` will not be imported, so consider using [_customize_resource()](class_editorexportplugin.md#class-editorexportplugin-private-method-customize-resource) to remap imported resources.

---


<a id="class-editorexportplugin-method-add-ios-bundle-file"></a>

void **add_ios_bundle_file**(path: [String](class_string.md#class-string)) [🔗](class_editorexportplugin.md#class-editorexportplugin-method-add-ios-bundle-file)

**Deprecated:** Use [add_apple_embedded_platform_bundle_file()](class_editorexportplugin.md#class-editorexportplugin-method-add-apple-embedded-platform-bundle-file) instead.

Adds an iOS bundle file from the given `path` to the exported project.

---


<a id="class-editorexportplugin-method-add-ios-cpp-code"></a>

void **add_ios_cpp_code**(code: [String](class_string.md#class-string)) [🔗](class_editorexportplugin.md#class-editorexportplugin-method-add-ios-cpp-code)

**Deprecated:** Use [add_apple_embedded_platform_cpp_code()](class_editorexportplugin.md#class-editorexportplugin-method-add-apple-embedded-platform-cpp-code) instead.

Adds C++ code to the iOS export. The final code is created from the code appended by each active export plugin.

---


<a id="class-editorexportplugin-method-add-ios-embedded-framework"></a>

void **add_ios_embedded_framework**(path: [String](class_string.md#class-string)) [🔗](class_editorexportplugin.md#class-editorexportplugin-method-add-ios-embedded-framework)

**Deprecated:** Use [add_apple_embedded_platform_embedded_framework()](class_editorexportplugin.md#class-editorexportplugin-method-add-apple-embedded-platform-embedded-framework) instead.

Adds a dynamic library (\*.dylib, \*.framework) to Linking Phase in iOS's Xcode project and embeds it into resulting binary.

**Note:** For static libraries (\*.a), this works the in same way as [add_apple_embedded_platform_framework()](class_editorexportplugin.md#class-editorexportplugin-method-add-apple-embedded-platform-framework).

**Note:** This method should not be used for System libraries as they are already present on the device.

---


<a id="class-editorexportplugin-method-add-ios-framework"></a>

void **add_ios_framework**(path: [String](class_string.md#class-string)) [🔗](class_editorexportplugin.md#class-editorexportplugin-method-add-ios-framework)

**Deprecated:** Use [add_apple_embedded_platform_framework()](class_editorexportplugin.md#class-editorexportplugin-method-add-apple-embedded-platform-framework) instead.

Adds a static library (\*.a) or a dynamic library (\*.dylib, \*.framework) to the Linking Phase to the iOS Xcode project.

---


<a id="class-editorexportplugin-method-add-ios-linker-flags"></a>

void **add_ios_linker_flags**(flags: [String](class_string.md#class-string)) [🔗](class_editorexportplugin.md#class-editorexportplugin-method-add-ios-linker-flags)

**Deprecated:** Use [add_apple_embedded_platform_linker_flags()](class_editorexportplugin.md#class-editorexportplugin-method-add-apple-embedded-platform-linker-flags) instead.

Adds linker flags for the iOS export.

---


<a id="class-editorexportplugin-method-add-ios-plist-content"></a>

void **add_ios_plist_content**(plist_content: [String](class_string.md#class-string)) [🔗](class_editorexportplugin.md#class-editorexportplugin-method-add-ios-plist-content)

**Deprecated:** Use [add_apple_embedded_platform_plist_content()](class_editorexportplugin.md#class-editorexportplugin-method-add-apple-embedded-platform-plist-content) instead.

Adds additional fields to the iOS project Info.plist file.

---


<a id="class-editorexportplugin-method-add-ios-project-static-lib"></a>

void **add_ios_project_static_lib**(path: [String](class_string.md#class-string)) [🔗](class_editorexportplugin.md#class-editorexportplugin-method-add-ios-project-static-lib)

**Deprecated:** Use [add_apple_embedded_platform_project_static_lib()](class_editorexportplugin.md#class-editorexportplugin-method-add-apple-embedded-platform-project-static-lib) instead.

Adds a static library from the given `path` to the iOS project.

---


<a id="class-editorexportplugin-method-add-macos-plugin-file"></a>

void **add_macos_plugin_file**(path: [String](class_string.md#class-string)) [🔗](class_editorexportplugin.md#class-editorexportplugin-method-add-macos-plugin-file)

Adds file or directory matching `path` to `PlugIns` directory of macOS app bundle.

**Note:** This is useful only for macOS exports.

---


<a id="class-editorexportplugin-method-add-shared-object"></a>

void **add_shared_object**(path: [String](class_string.md#class-string), tags: [PackedStringArray](class_packedstringarray.md#class-packedstringarray), target: [String](class_string.md#class-string)) [🔗](class_editorexportplugin.md#class-editorexportplugin-method-add-shared-object)

Adds a shared object or a directory containing only shared objects with the given `tags` and destination `path`.

**Note:** In case of macOS exports, those shared objects will be added to `Frameworks` directory of app bundle.

In case of a directory code-sign will error if you place non code object in directory.

---


<a id="class-editorexportplugin-method-get-export-platform"></a>

[EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform) **get_export_platform**() const [🔗](class_editorexportplugin.md#class-editorexportplugin-method-get-export-platform)

Returns currently used export platform.

---


<a id="class-editorexportplugin-method-get-export-preset"></a>

[EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset) **get_export_preset**() const [🔗](class_editorexportplugin.md#class-editorexportplugin-method-get-export-preset)

Returns currently used export preset.

---


<a id="class-editorexportplugin-method-get-option"></a>

[Variant](class_variant.md#class-variant) **get_option**(name: [StringName](class_stringname.md#class-stringname)) const [🔗](class_editorexportplugin.md#class-editorexportplugin-method-get-option)

Returns the current value of an export option supplied by [_get_export_options()](class_editorexportplugin.md#class-editorexportplugin-private-method-get-export-options).

---


<a id="class-editorexportplugin-method-skip"></a>

void **skip**() [🔗](class_editorexportplugin.md#class-editorexportplugin-method-skip)

To be called inside [_export_file()](class_editorexportplugin.md#class-editorexportplugin-private-method-export-file). Skips the current file, so it's not included in the export.
