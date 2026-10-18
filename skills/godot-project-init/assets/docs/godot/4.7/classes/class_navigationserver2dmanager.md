> Source: https://docs.godotengine.org/en/4.7/classes/class_navigationserver2dmanager.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="navigationserver2dmanager"></a>

<a id="class-navigationserver2dmanager"></a>

# NavigationServer2DManager

**Inherits:** [Object](class_object.md#class-object)

A singleton for managing [NavigationServer2D](class_navigationserver2d.md#class-navigationserver2d) implementations.

<a id="description"></a>

## Description

**NavigationServer2DManager** is the API for registering [NavigationServer2D](class_navigationserver2d.md#class-navigationserver2d) implementations and setting the default implementation.

**Note:** It is not possible to switch servers at runtime. This class is only used on startup at the server initialization level.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [register_server](class_navigationserver2dmanager.md#class-navigationserver2dmanager-method-register-server)(name: [String](class_string.md#class-string), create_callback: [Callable](class_callable.md#class-callable)) |
| void | [set_default_server](class_navigationserver2dmanager.md#class-navigationserver2dmanager-method-set-default-server)(name: [String](class_string.md#class-string), priority: [int](class_int.md#class-int)) |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-navigationserver2dmanager-method-register-server"></a>

void **register_server**(name: [String](class_string.md#class-string), create_callback: [Callable](class_callable.md#class-callable)) [🔗](class_navigationserver2dmanager.md#class-navigationserver2dmanager-method-register-server)

Registers a [NavigationServer2D](class_navigationserver2d.md#class-navigationserver2d) implementation by passing a `name` and a [Callable](class_callable.md#class-callable) that returns a [NavigationServer2D](class_navigationserver2d.md#class-navigationserver2d) object.

---


<a id="class-navigationserver2dmanager-method-set-default-server"></a>

void **set_default_server**(name: [String](class_string.md#class-string), priority: [int](class_int.md#class-int)) [🔗](class_navigationserver2dmanager.md#class-navigationserver2dmanager-method-set-default-server)

Sets the default [NavigationServer2D](class_navigationserver2d.md#class-navigationserver2d) implementation to the one identified by `name`, if `priority` is greater than the priority of the current default implementation.
