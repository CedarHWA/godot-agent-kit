> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodegroupbase.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodegroupbase"></a>

<a id="class-visualshadernodegroupbase"></a>

# VisualShaderNodeGroupBase

**Inherits:** [VisualShaderNodeResizableBase](class_visualshadernoderesizablebase.md#class-visualshadernoderesizablebase) **<** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [VisualShaderNodeExpression](class_visualshadernodeexpression.md#class-visualshadernodeexpression)

Base class for a family of nodes with variable number of input and output ports within the visual shader graph.

<a id="description"></a>

## Description

Currently, has no direct usage, use the derived classes instead.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [add_input_port](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-add-input-port)(id: [int](class_int.md#class-int), type: [int](class_int.md#class-int), name: [String](class_string.md#class-string)) |
| void | [add_output_port](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-add-output-port)(id: [int](class_int.md#class-int), type: [int](class_int.md#class-int), name: [String](class_string.md#class-string)) |
| void | [clear_input_ports](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-clear-input-ports)() |
| void | [clear_output_ports](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-clear-output-ports)() |
| [int](class_int.md#class-int) | [get_free_input_port_id](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-get-free-input-port-id)() const |
| [int](class_int.md#class-int) | [get_free_output_port_id](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-get-free-output-port-id)() const |
| [int](class_int.md#class-int) | [get_input_port_count](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-get-input-port-count)() const |
| [String](class_string.md#class-string) | [get_inputs](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-get-inputs)() const |
| [int](class_int.md#class-int) | [get_output_port_count](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-get-output-port-count)() const |
| [String](class_string.md#class-string) | [get_outputs](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-get-outputs)() const |
| [bool](class_bool.md#class-bool) | [has_input_port](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-has-input-port)(id: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [has_output_port](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-has-output-port)(id: [int](class_int.md#class-int)) const |
| [bool](class_bool.md#class-bool) | [is_valid_port_name](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-is-valid-port-name)(name: [String](class_string.md#class-string)) const |
| void | [remove_input_port](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-remove-input-port)(id: [int](class_int.md#class-int)) |
| void | [remove_output_port](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-remove-output-port)(id: [int](class_int.md#class-int)) |
| void | [set_input_port_name](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-set-input-port-name)(id: [int](class_int.md#class-int), name: [String](class_string.md#class-string)) |
| void | [set_input_port_type](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-set-input-port-type)(id: [int](class_int.md#class-int), type: [int](class_int.md#class-int)) |
| void | [set_inputs](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-set-inputs)(inputs: [String](class_string.md#class-string)) |
| void | [set_output_port_name](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-set-output-port-name)(id: [int](class_int.md#class-int), name: [String](class_string.md#class-string)) |
| void | [set_output_port_type](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-set-output-port-type)(id: [int](class_int.md#class-int), type: [int](class_int.md#class-int)) |
| void | [set_outputs](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-set-outputs)(outputs: [String](class_string.md#class-string)) |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-visualshadernodegroupbase-method-add-input-port"></a>

void **add_input_port**(id: [int](class_int.md#class-int), type: [int](class_int.md#class-int), name: [String](class_string.md#class-string)) [🔗](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-add-input-port)

Adds an input port with the specified `type` (see [PortType](class_visualshadernode.md#enum-visualshadernode-porttype)) and `name`.

---


<a id="class-visualshadernodegroupbase-method-add-output-port"></a>

void **add_output_port**(id: [int](class_int.md#class-int), type: [int](class_int.md#class-int), name: [String](class_string.md#class-string)) [🔗](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-add-output-port)

Adds an output port with the specified `type` (see [PortType](class_visualshadernode.md#enum-visualshadernode-porttype)) and `name`.

---


<a id="class-visualshadernodegroupbase-method-clear-input-ports"></a>

void **clear_input_ports**() [🔗](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-clear-input-ports)

Removes all previously specified input ports.

---


<a id="class-visualshadernodegroupbase-method-clear-output-ports"></a>

void **clear_output_ports**() [🔗](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-clear-output-ports)

Removes all previously specified output ports.

---


<a id="class-visualshadernodegroupbase-method-get-free-input-port-id"></a>

[int](class_int.md#class-int) **get_free_input_port_id**() const [🔗](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-get-free-input-port-id)

Returns a free input port ID which can be used in [add_input_port()](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-add-input-port).

---


<a id="class-visualshadernodegroupbase-method-get-free-output-port-id"></a>

[int](class_int.md#class-int) **get_free_output_port_id**() const [🔗](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-get-free-output-port-id)

Returns a free output port ID which can be used in [add_output_port()](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-add-output-port).

---


<a id="class-visualshadernodegroupbase-method-get-input-port-count"></a>

[int](class_int.md#class-int) **get_input_port_count**() const [🔗](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-get-input-port-count)

Returns the number of input ports in use. Alternative for [get_free_input_port_id()](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-get-free-input-port-id).

---


<a id="class-visualshadernodegroupbase-method-get-inputs"></a>

[String](class_string.md#class-string) **get_inputs**() const [🔗](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-get-inputs)

Returns a [String](class_string.md#class-string) description of the input ports as a colon-separated list using the format `id,type,name;` (see [add_input_port()](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-add-input-port)).

---


<a id="class-visualshadernodegroupbase-method-get-output-port-count"></a>

[int](class_int.md#class-int) **get_output_port_count**() const [🔗](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-get-output-port-count)

Returns the number of output ports in use. Alternative for [get_free_output_port_id()](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-get-free-output-port-id).

---


<a id="class-visualshadernodegroupbase-method-get-outputs"></a>

[String](class_string.md#class-string) **get_outputs**() const [🔗](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-get-outputs)

Returns a [String](class_string.md#class-string) description of the output ports as a colon-separated list using the format `id,type,name;` (see [add_output_port()](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-add-output-port)).

---


<a id="class-visualshadernodegroupbase-method-has-input-port"></a>

[bool](class_bool.md#class-bool) **has_input_port**(id: [int](class_int.md#class-int)) const [🔗](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-has-input-port)

Returns `true` if the specified input port exists.

---


<a id="class-visualshadernodegroupbase-method-has-output-port"></a>

[bool](class_bool.md#class-bool) **has_output_port**(id: [int](class_int.md#class-int)) const [🔗](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-has-output-port)

Returns `true` if the specified output port exists.

---


<a id="class-visualshadernodegroupbase-method-is-valid-port-name"></a>

[bool](class_bool.md#class-bool) **is_valid_port_name**(name: [String](class_string.md#class-string)) const [🔗](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-is-valid-port-name)

Returns `true` if the specified port name does not override an existed port name and is valid within the shader.

---


<a id="class-visualshadernodegroupbase-method-remove-input-port"></a>

void **remove_input_port**(id: [int](class_int.md#class-int)) [🔗](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-remove-input-port)

Removes the specified input port.

---


<a id="class-visualshadernodegroupbase-method-remove-output-port"></a>

void **remove_output_port**(id: [int](class_int.md#class-int)) [🔗](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-remove-output-port)

Removes the specified output port.

---


<a id="class-visualshadernodegroupbase-method-set-input-port-name"></a>

void **set_input_port_name**(id: [int](class_int.md#class-int), name: [String](class_string.md#class-string)) [🔗](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-set-input-port-name)

Renames the specified input port.

---


<a id="class-visualshadernodegroupbase-method-set-input-port-type"></a>

void **set_input_port_type**(id: [int](class_int.md#class-int), type: [int](class_int.md#class-int)) [🔗](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-set-input-port-type)

Sets the specified input port's type (see [PortType](class_visualshadernode.md#enum-visualshadernode-porttype)).

---


<a id="class-visualshadernodegroupbase-method-set-inputs"></a>

void **set_inputs**(inputs: [String](class_string.md#class-string)) [🔗](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-set-inputs)

Defines all input ports using a [String](class_string.md#class-string) formatted as a colon-separated list: `id,type,name;` (see [add_input_port()](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-add-input-port)).

---


<a id="class-visualshadernodegroupbase-method-set-output-port-name"></a>

void **set_output_port_name**(id: [int](class_int.md#class-int), name: [String](class_string.md#class-string)) [🔗](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-set-output-port-name)

Renames the specified output port.

---


<a id="class-visualshadernodegroupbase-method-set-output-port-type"></a>

void **set_output_port_type**(id: [int](class_int.md#class-int), type: [int](class_int.md#class-int)) [🔗](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-set-output-port-type)

Sets the specified output port's type (see [PortType](class_visualshadernode.md#enum-visualshadernode-porttype)).

---


<a id="class-visualshadernodegroupbase-method-set-outputs"></a>

void **set_outputs**(outputs: [String](class_string.md#class-string)) [🔗](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-set-outputs)

Defines all output ports using a [String](class_string.md#class-string) formatted as a colon-separated list: `id,type,name;` (see [add_output_port()](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase-method-add-output-port)).
