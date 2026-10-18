> Source: https://docs.godotengine.org/en/4.7/classes/class_tcpserver.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="tcpserver"></a>

<a id="class-tcpserver"></a>

# TCPServer

**Inherits:** [SocketServer](class_socketserver.md#class-socketserver) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A TCP server.

<a id="description"></a>

## Description

A TCP server. Listens to connections on a port and returns a [StreamPeerTCP](class_streampeertcp.md#class-streampeertcp) when it gets an incoming connection.

**Note:** When exporting to Android, make sure to enable the `INTERNET` permission in the Android export preset before exporting the project or using one-click deploy. Otherwise, network communication of any kind will be blocked by Android.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [int](class_int.md#class-int) | [get_local_port](class_tcpserver.md#class-tcpserver-method-get-local-port)() const |
| [Error](class_@globalscope.md#enum-globalscope-error) | [listen](class_tcpserver.md#class-tcpserver-method-listen)(port: [int](class_int.md#class-int), bind_address: [String](class_string.md#class-string) = "\*") |
| [StreamPeerTCP](class_streampeertcp.md#class-streampeertcp) | [take_connection](class_tcpserver.md#class-tcpserver-method-take-connection)() |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-tcpserver-method-get-local-port"></a>

[int](class_int.md#class-int) **get_local_port**() const [🔗](class_tcpserver.md#class-tcpserver-method-get-local-port)

Returns the local port this server is listening to.

---


<a id="class-tcpserver-method-listen"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **listen**(port: [int](class_int.md#class-int), bind_address: [String](class_string.md#class-string) = "\*") [🔗](class_tcpserver.md#class-tcpserver-method-listen)

Listen on the `port` binding to `bind_address`.

If `bind_address` is set as `"*"` (default), the server will listen on all available addresses (both IPv4 and IPv6).

If `bind_address` is set as `"0.0.0.0"` (for IPv4) or `"::"` (for IPv6), the server will listen on all available addresses matching that IP type.

If `bind_address` is set to any valid address (e.g. `"192.168.1.101"`, `"::1"`, etc.), the server will only listen on the interface with that address (or fail if no interface with the given address exists).

---


<a id="class-tcpserver-method-take-connection"></a>

[StreamPeerTCP](class_streampeertcp.md#class-streampeertcp) **take_connection**() [🔗](class_tcpserver.md#class-tcpserver-method-take-connection)

If a connection is available, returns a StreamPeerTCP with the connection.
