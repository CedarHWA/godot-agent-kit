> Source: https://docs.godotengine.org/en/4.7/classes/class_visualshadernodereroute.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="visualshadernodereroute"></a>

<a id="class-visualshadernodereroute"></a>

# VisualShaderNodeReroute

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A node that allows rerouting a connection within the visual shader graph.

<a id="description"></a>

## Description

Automatically adapts its port type to the type of the incoming connection and ensures valid connections.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [PortType](class_visualshadernode.md#enum-visualshadernode-porttype) | [get_port_type](class_visualshadernodereroute.md#class-visualshadernodereroute-method-get-port-type)() const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-visualshadernodereroute-method-get-port-type"></a>

[PortType](class_visualshadernode.md#enum-visualshadernode-porttype) **get_port_type**() const [🔗](class_visualshadernodereroute.md#class-visualshadernodereroute-method-get-port-type)

Returns the port type of the reroute node.
