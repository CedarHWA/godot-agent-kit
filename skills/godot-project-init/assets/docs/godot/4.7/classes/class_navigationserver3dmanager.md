> Source: https://docs.godotengine.org/en/4.7/classes/class_navigationserver3dmanager.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="navigationserver3dmanager"></a>

<a id="class-navigationserver3dmanager"></a>

# NavigationServer3DManager

**Inherits:** [Object](class_object.md#class-object)

A singleton for managing [NavigationServer3D](class_navigationserver3d.md#class-navigationserver3d) implementations.

<a id="description"></a>

## Description

**NavigationServer3DManager** is the API for registering [NavigationServer3D](class_navigationserver3d.md#class-navigationserver3d) implementations and setting the default implementation.

**Note:** It is not possible to switch servers at runtime. This class is only used on startup at the server initialization level.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [register_server](class_navigationserver3dmanager.md#class-navigationserver3dmanager-method-register-server)(name: [String](class_string.md#class-string), create_callback: [Callable](class_callable.md#class-callable)) |
| void | [set_default_server](class_navigationserver3dmanager.md#class-navigationserver3dmanager-method-set-default-server)(name: [String](class_string.md#class-string), priority: [int](class_int.md#class-int)) |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-navigationserver3dmanager-method-register-server"></a>

void **register_server**(name: [String](class_string.md#class-string), create_callback: [Callable](class_callable.md#class-callable)) [🔗](class_navigationserver3dmanager.md#class-navigationserver3dmanager-method-register-server)

Registers a [NavigationServer3D](class_navigationserver3d.md#class-navigationserver3d) implementation by passing a `name` and a [Callable](class_callable.md#class-callable) that returns a [NavigationServer3D](class_navigationserver3d.md#class-navigationserver3d) object.

---


<a id="class-navigationserver3dmanager-method-set-default-server"></a>

void **set_default_server**(name: [String](class_string.md#class-string), priority: [int](class_int.md#class-int)) [🔗](class_navigationserver3dmanager.md#class-navigationserver3dmanager-method-set-default-server)

Sets the default [NavigationServer3D](class_navigationserver3d.md#class-navigationserver3d) implementation to the one identified by `name`, if `priority` is greater than the priority of the current default implementation.
