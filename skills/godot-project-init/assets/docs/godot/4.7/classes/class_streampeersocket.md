> Source: https://docs.godotengine.org/en/4.7/classes/class_streampeersocket.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="streampeersocket"></a>

<a id="class-streampeersocket"></a>

# StreamPeerSocket

**Inherits:** [StreamPeer](class_streampeer.md#class-streampeer) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [StreamPeerTCP](class_streampeertcp.md#class-streampeertcp), [StreamPeerUDS](class_streampeeruds.md#class-streampeeruds)

Abstract base class for interacting with socket streams.

<a id="description"></a>

## Description

StreamPeerSocket is an abstract base class that defines common behavior for socket-based streams.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [disconnect_from_host](class_streampeersocket.md#class-streampeersocket-method-disconnect-from-host)() |
| [Status](class_streampeersocket.md#enum-streampeersocket-status) | [get_status](class_streampeersocket.md#class-streampeersocket-method-get-status)() const |
| [Error](class_@globalscope.md#enum-globalscope-error) | [poll](class_streampeersocket.md#class-streampeersocket-method-poll)() |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-streampeersocket-status"></a>

enum **Status**: [🔗](class_streampeersocket.md#enum-streampeersocket-status)

<a id="class-streampeersocket-constant-status-none"></a>

[Status](class_streampeersocket.md#enum-streampeersocket-status) **STATUS_NONE** = `0`

The initial status of the **StreamPeerSocket**. This is also the status after disconnecting.

<a id="class-streampeersocket-constant-status-connecting"></a>

[Status](class_streampeersocket.md#enum-streampeersocket-status) **STATUS_CONNECTING** = `1`

A status representing a **StreamPeerSocket** that is connecting to a host.

<a id="class-streampeersocket-constant-status-connected"></a>

[Status](class_streampeersocket.md#enum-streampeersocket-status) **STATUS_CONNECTED** = `2`

A status representing a **StreamPeerSocket** that is connected to a host.

<a id="class-streampeersocket-constant-status-error"></a>

[Status](class_streampeersocket.md#enum-streampeersocket-status) **STATUS_ERROR** = `3`

A status representing a **StreamPeerSocket** in error state.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-streampeersocket-method-disconnect-from-host"></a>

void **disconnect_from_host**() [🔗](class_streampeersocket.md#class-streampeersocket-method-disconnect-from-host)

Disconnects from host.

---


<a id="class-streampeersocket-method-get-status"></a>

[Status](class_streampeersocket.md#enum-streampeersocket-status) **get_status**() const [🔗](class_streampeersocket.md#class-streampeersocket-method-get-status)

Returns the status of the connection.

---


<a id="class-streampeersocket-method-poll"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **poll**() [🔗](class_streampeersocket.md#class-streampeersocket-method-poll)

Polls the socket, updating its state. See [get_status()](class_streampeersocket.md#class-streampeersocket-method-get-status).
