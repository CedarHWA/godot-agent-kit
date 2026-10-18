> Source: https://docs.godotengine.org/en/4.7/classes/class_textservermanager.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="textservermanager"></a>

<a id="class-textservermanager"></a>

# TextServerManager

**Inherits:** [Object](class_object.md#class-object)

A singleton for managing [TextServer](class_textserver.md#class-textserver) implementations.

<a id="description"></a>

## Description

**TextServerManager** is the API backend for loading, enumerating, and switching [TextServer](class_textserver.md#class-textserver)s.

**Note:** Switching text server at runtime is possible, but will invalidate all fonts and text buffers. Make sure to unload all controls, fonts, and themes before doing so.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_interface](class_textservermanager.md#class-textservermanager-method-add-interface)(interface: [TextServer](class_textserver.md#class-textserver)) |
| [TextServer](class_textserver.md#class-textserver) | [find_interface](class_textservermanager.md#class-textservermanager-method-find-interface)(name: [String](class_string.md#class-string)) const |
| [TextServer](class_textserver.md#class-textserver) | [get_interface](class_textservermanager.md#class-textservermanager-method-get-interface)(idx: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_interface_count](class_textservermanager.md#class-textservermanager-method-get-interface-count)() const |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | [get_interfaces](class_textservermanager.md#class-textservermanager-method-get-interfaces)() const |
| [TextServer](class_textserver.md#class-textserver) | [get_primary_interface](class_textservermanager.md#class-textservermanager-method-get-primary-interface)() const |
| void | [remove_interface](class_textservermanager.md#class-textservermanager-method-remove-interface)(interface: [TextServer](class_textserver.md#class-textserver)) |
| void | [set_primary_interface](class_textservermanager.md#class-textservermanager-method-set-primary-interface)(index: [TextServer](class_textserver.md#class-textserver)) |

---


<a id="signals"></a>

## Signals

<a id="class-textservermanager-signal-interface-added"></a>

**interface_added**(interface_name: [StringName](class_stringname.md#class-stringname)) [🔗](class_textservermanager.md#class-textservermanager-signal-interface-added)

Emitted when a new interface has been added.

---


<a id="class-textservermanager-signal-interface-removed"></a>

**interface_removed**(interface_name: [StringName](class_stringname.md#class-stringname)) [🔗](class_textservermanager.md#class-textservermanager-signal-interface-removed)

Emitted when an interface is removed.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-textservermanager-method-add-interface"></a>

void **add_interface**(interface: [TextServer](class_textserver.md#class-textserver)) [🔗](class_textservermanager.md#class-textservermanager-method-add-interface)

Registers a [TextServer](class_textserver.md#class-textserver) interface.

---


<a id="class-textservermanager-method-find-interface"></a>

[TextServer](class_textserver.md#class-textserver) **find_interface**(name: [String](class_string.md#class-string)) const [🔗](class_textservermanager.md#class-textservermanager-method-find-interface)

Finds an interface by its `name`.

---


<a id="class-textservermanager-method-get-interface"></a>

[TextServer](class_textserver.md#class-textserver) **get_interface**(idx: [int](class_int.md#class-int)) const [🔗](class_textservermanager.md#class-textservermanager-method-get-interface)

Returns the interface registered at a given index.

---


<a id="class-textservermanager-method-get-interface-count"></a>

[int](class_int.md#class-int) **get_interface_count**() const [🔗](class_textservermanager.md#class-textservermanager-method-get-interface-count)

Returns the number of interfaces currently registered.

---


<a id="class-textservermanager-method-get-interfaces"></a>

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **get_interfaces**() const [🔗](class_textservermanager.md#class-textservermanager-method-get-interfaces)

Returns a list of available interfaces, with the index and name of each interface.

---


<a id="class-textservermanager-method-get-primary-interface"></a>

[TextServer](class_textserver.md#class-textserver) **get_primary_interface**() const [🔗](class_textservermanager.md#class-textservermanager-method-get-primary-interface)

Returns the primary [TextServer](class_textserver.md#class-textserver) interface currently in use.

---


<a id="class-textservermanager-method-remove-interface"></a>

void **remove_interface**(interface: [TextServer](class_textserver.md#class-textserver)) [🔗](class_textservermanager.md#class-textservermanager-method-remove-interface)

Removes an interface. All fonts and shaped text caches should be freed before removing an interface.

---


<a id="class-textservermanager-method-set-primary-interface"></a>

void **set_primary_interface**(index: [TextServer](class_textserver.md#class-textserver)) [🔗](class_textservermanager.md#class-textservermanager-method-set-primary-interface)

Sets the primary [TextServer](class_textserver.md#class-textserver) interface.
