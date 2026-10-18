> Source: https://docs.godotengine.org/en/4.7/classes/class_physicsserver2dmanager.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="physicsserver2dmanager"></a>

<a id="class-physicsserver2dmanager"></a>

# PhysicsServer2DManager

**Inherits:** [Object](class_object.md#class-object)

A singleton for managing [PhysicsServer2D](class_physicsserver2d.md#class-physicsserver2d) implementations.

<a id="description"></a>

## Description

**PhysicsServer2DManager** is the API for registering [PhysicsServer2D](class_physicsserver2d.md#class-physicsserver2d) implementations and for setting the default implementation.

**Note:** It is not possible to switch physics servers at runtime. This class is only used on startup at the server initialization level, by Godot itself and possibly by GDExtensions.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [register_server](class_physicsserver2dmanager.md#class-physicsserver2dmanager-method-register-server)(name: [String](class_string.md#class-string), create_callback: [Callable](class_callable.md#class-callable)) |
| void | [set_default_server](class_physicsserver2dmanager.md#class-physicsserver2dmanager-method-set-default-server)(name: [String](class_string.md#class-string), priority: [int](class_int.md#class-int)) |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-physicsserver2dmanager-method-register-server"></a>

void **register_server**(name: [String](class_string.md#class-string), create_callback: [Callable](class_callable.md#class-callable)) [🔗](class_physicsserver2dmanager.md#class-physicsserver2dmanager-method-register-server)

Register a [PhysicsServer2D](class_physicsserver2d.md#class-physicsserver2d) implementation by passing a `name` and a [Callable](class_callable.md#class-callable) that returns a [PhysicsServer2D](class_physicsserver2d.md#class-physicsserver2d) object.

---


<a id="class-physicsserver2dmanager-method-set-default-server"></a>

void **set_default_server**(name: [String](class_string.md#class-string), priority: [int](class_int.md#class-int)) [🔗](class_physicsserver2dmanager.md#class-physicsserver2dmanager-method-set-default-server)

Set the default [PhysicsServer2D](class_physicsserver2d.md#class-physicsserver2d) implementation to the one identified by `name`, if `priority` is greater than the priority of the current default implementation.
