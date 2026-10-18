> Source: https://docs.godotengine.org/en/4.7/classes/class_gdextension.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="gdextension"></a>

<a id="class-gdextension"></a>

# GDExtension

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A native library for GDExtension.

<a id="description"></a>

## Description

The **GDExtension** resource type represents a [shared library](https://en.wikipedia.org/wiki/Shared_library) which can expand the functionality of the engine. The [GDExtensionManager](class_gdextensionmanager.md#class-gdextensionmanager) singleton is responsible for loading, reloading, and unloading **GDExtension** resources.

**Note:** GDExtension itself is not a scripting language and has no relation to [GDScript](class_gdscript.md#class-gdscript) resources.

<a id="tutorials"></a>

## Tutorials

- [GDExtension overview](../engine_details/engine_api/gdextension/what_is_gdextension.md)
- [GDExtension example in C++](../tutorials/scripting/cpp/gdextension_cpp_example.md)

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [InitializationLevel](class_gdextension.md#enum-gdextension-initializationlevel) | [get_minimum_library_initialization_level](class_gdextension.md#class-gdextension-method-get-minimum-library-initialization-level)() const |
| [bool](class_bool.md#class-bool) | [is_library_open](class_gdextension.md#class-gdextension-method-is-library-open)() const |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-gdextension-initializationlevel"></a>

enum **InitializationLevel**: [🔗](class_gdextension.md#enum-gdextension-initializationlevel)

<a id="class-gdextension-constant-initialization-level-core"></a>

[InitializationLevel](class_gdextension.md#enum-gdextension-initializationlevel) **INITIALIZATION_LEVEL_CORE** = `0`

The library is initialized at the same time as the core features of the engine.

<a id="class-gdextension-constant-initialization-level-servers"></a>

[InitializationLevel](class_gdextension.md#enum-gdextension-initializationlevel) **INITIALIZATION_LEVEL_SERVERS** = `1`

The library is initialized at the same time as the engine's servers (such as [RenderingServer](class_renderingserver.md#class-renderingserver) or [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d)).

<a id="class-gdextension-constant-initialization-level-scene"></a>

[InitializationLevel](class_gdextension.md#enum-gdextension-initializationlevel) **INITIALIZATION_LEVEL_SCENE** = `2`

The library is initialized at the same time as the engine's scene-related classes.

<a id="class-gdextension-constant-initialization-level-editor"></a>

[InitializationLevel](class_gdextension.md#enum-gdextension-initializationlevel) **INITIALIZATION_LEVEL_EDITOR** = `3`

The library is initialized at the same time as the engine's editor classes. Only happens when loading the GDExtension in the editor.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-gdextension-method-get-minimum-library-initialization-level"></a>

[InitializationLevel](class_gdextension.md#enum-gdextension-initializationlevel) **get_minimum_library_initialization_level**() const [🔗](class_gdextension.md#class-gdextension-method-get-minimum-library-initialization-level)

Returns the lowest level required for this extension to be properly initialized (see the [InitializationLevel](class_gdextension.md#enum-gdextension-initializationlevel) enum).

---


<a id="class-gdextension-method-is-library-open"></a>

[bool](class_bool.md#class-bool) **is_library_open**() const [🔗](class_gdextension.md#class-gdextension-method-is-library-open)

Returns `true` if this extension's library has been opened.
