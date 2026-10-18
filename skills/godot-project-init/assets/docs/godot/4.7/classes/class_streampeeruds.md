> Source: https://docs.godotengine.org/en/4.7/classes/class_streampeeruds.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="streampeeruds"></a>

<a id="class-streampeeruds"></a>

# StreamPeerUDS

**Inherits:** [StreamPeerSocket](class_streampeersocket.md#class-streampeersocket) **<** [StreamPeer](class_streampeer.md#class-streampeer) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A stream peer that handles UNIX Domain Socket (UDS) connections.

<a id="description"></a>

## Description

A stream peer that handles UNIX Domain Socket (UDS) connections. This object can be used to connect to UDS servers, or also is returned by a UDS server. Unix Domain Sockets provide inter-process communication on the same machine using the filesystem namespace.

**Note:** UNIX Domain Sockets are only available on UNIX-like systems (Linux, macOS, etc.) and are not supported on Windows.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Error](class_@globalscope.md#enum-globalscope-error) | [bind](class_streampeeruds.md#class-streampeeruds-method-bind)(path: [String](class_string.md#class-string)) |
| [Error](class_@globalscope.md#enum-globalscope-error) | [connect_to_host](class_streampeeruds.md#class-streampeeruds-method-connect-to-host)(path: [String](class_string.md#class-string)) |
| [String](class_string.md#class-string) | [get_connected_path](class_streampeeruds.md#class-streampeeruds-method-get-connected-path)() const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-streampeeruds-method-bind"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **bind**(path: [String](class_string.md#class-string)) [🔗](class_streampeeruds.md#class-streampeeruds-method-bind)

Opens the UDS socket, and binds it to the specified socket path.

This method is generally not needed, and only used to force the subsequent call to [connect_to_host()](class_streampeeruds.md#class-streampeeruds-method-connect-to-host) to use the specified `path` as the source address.

---


<a id="class-streampeeruds-method-connect-to-host"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **connect_to_host**(path: [String](class_string.md#class-string)) [🔗](class_streampeeruds.md#class-streampeeruds-method-connect-to-host)

Connects to the specified UNIX Domain Socket path. Returns [@GlobalScope.OK](class_@globalscope.md#class-globalscope-constant-ok) on success.

---


<a id="class-streampeeruds-method-get-connected-path"></a>

[String](class_string.md#class-string) **get_connected_path**() const [🔗](class_streampeeruds.md#class-streampeeruds-method-get-connected-path)

Returns the socket path of this peer.
