> Source: https://docs.godotengine.org/en/4.7/classes/class_physicsserver3dmanager.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="physicsserver3dmanager"></a>

<a id="class-physicsserver3dmanager"></a>

# PhysicsServer3DManager

**Inherits:** [Object](class_object.md#class-object)

A singleton for managing [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d) implementations.

<a id="description"></a>

## Description

**PhysicsServer3DManager** is the API for registering [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d) implementations and for setting the default implementation.

**Note:** It is not possible to switch physics servers at runtime. This class is only used on startup at the server initialization level, by Godot itself and possibly by GDExtensions.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [register_server](class_physicsserver3dmanager.md#class-physicsserver3dmanager-method-register-server)(name: [String](class_string.md#class-string), create_callback: [Callable](class_callable.md#class-callable)) |
| void | [set_default_server](class_physicsserver3dmanager.md#class-physicsserver3dmanager-method-set-default-server)(name: [String](class_string.md#class-string), priority: [int](class_int.md#class-int)) |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-physicsserver3dmanager-method-register-server"></a>

void **register_server**(name: [String](class_string.md#class-string), create_callback: [Callable](class_callable.md#class-callable)) [🔗](class_physicsserver3dmanager.md#class-physicsserver3dmanager-method-register-server)

Register a [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d) implementation by passing a `name` and a [Callable](class_callable.md#class-callable) that returns a [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d) object.

---


<a id="class-physicsserver3dmanager-method-set-default-server"></a>

void **set_default_server**(name: [String](class_string.md#class-string), priority: [int](class_int.md#class-int)) [🔗](class_physicsserver3dmanager.md#class-physicsserver3dmanager-method-set-default-server)

Set the default [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d) implementation to the one identified by `name`, if `priority` is greater than the priority of the current default implementation.
