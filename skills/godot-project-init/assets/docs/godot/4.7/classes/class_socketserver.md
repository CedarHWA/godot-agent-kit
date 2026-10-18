> Source: https://docs.godotengine.org/en/4.7/classes/class_socketserver.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="socketserver"></a>

<a id="class-socketserver"></a>

# SocketServer

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [TCPServer](class_tcpserver.md#class-tcpserver), [UDSServer](class_udsserver.md#class-udsserver)

An abstract class for servers based on sockets.

<a id="description"></a>

## Description

A socket server.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [is_connection_available](class_socketserver.md#class-socketserver-method-is-connection-available)() const |
| [bool](class_bool.md#class-bool) | [is_listening](class_socketserver.md#class-socketserver-method-is-listening)() const |
| void | [stop](class_socketserver.md#class-socketserver-method-stop)() |
| [StreamPeerSocket](class_streampeersocket.md#class-streampeersocket) | [take_socket_connection](class_socketserver.md#class-socketserver-method-take-socket-connection)() |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-socketserver-method-is-connection-available"></a>

[bool](class_bool.md#class-bool) **is_connection_available**() const [🔗](class_socketserver.md#class-socketserver-method-is-connection-available)

Returns `true` if a connection is available for taking.

---


<a id="class-socketserver-method-is-listening"></a>

[bool](class_bool.md#class-bool) **is_listening**() const [🔗](class_socketserver.md#class-socketserver-method-is-listening)

Returns `true` if the server is currently listening for connections.

---


<a id="class-socketserver-method-stop"></a>

void **stop**() [🔗](class_socketserver.md#class-socketserver-method-stop)

Stops listening.

---


<a id="class-socketserver-method-take-socket-connection"></a>

[StreamPeerSocket](class_streampeersocket.md#class-streampeersocket) **take_socket_connection**() [🔗](class_socketserver.md#class-socketserver-method-take-socket-connection)

If a connection is available, returns a StreamPeerSocket with the connection.
