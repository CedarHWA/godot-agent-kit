> Source: https://docs.godotengine.org/en/4.7/classes/class_udsserver.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="udsserver"></a>

<a id="class-udsserver"></a>

# UDSServer

**Inherits:** [SocketServer](class_socketserver.md#class-socketserver) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A Unix Domain Socket (UDS) server.

<a id="description"></a>

## Description

A Unix Domain Socket (UDS) server. Listens to connections on a socket path and returns a [StreamPeerUDS](class_streampeeruds.md#class-streampeeruds) when it gets an incoming connection. Unix Domain Sockets provide inter-process communication on the same machine using the filesystem namespace.

**Note:** Unix Domain Sockets are only available on Unix-like systems (Linux, macOS, etc.) and are not supported on Windows.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Error](class_@globalscope.md#enum-globalscope-error) | [listen](class_udsserver.md#class-udsserver-method-listen)(path: [String](class_string.md#class-string)) |
| [StreamPeerUDS](class_streampeeruds.md#class-streampeeruds) | [take_connection](class_udsserver.md#class-udsserver-method-take-connection)() |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-udsserver-method-listen"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **listen**(path: [String](class_string.md#class-string)) [🔗](class_udsserver.md#class-udsserver-method-listen)

Listens on the socket at `path`. The socket file will be created at the specified path.

**Note:** The socket file must not already exist at the specified path. You may need to remove any existing socket file before calling this method.

---


<a id="class-udsserver-method-take-connection"></a>

[StreamPeerUDS](class_streampeeruds.md#class-streampeeruds) **take_connection**() [🔗](class_udsserver.md#class-udsserver-method-take-connection)

If a connection is available, returns a StreamPeerUDS with the connection.
