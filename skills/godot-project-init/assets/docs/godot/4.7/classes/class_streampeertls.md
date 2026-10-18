> Source: https://docs.godotengine.org/en/4.7/classes/class_streampeertls.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="streampeertls"></a>

<a id="class-streampeertls"></a>

# StreamPeerTLS

**Inherits:** [StreamPeer](class_streampeer.md#class-streampeer) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A stream peer that handles TLS connections.

<a id="description"></a>

## Description

A stream peer that handles TLS connections. This object can be used to connect to a TLS server or accept a single TLS client connection.

**Note:** When exporting to Android, make sure to enable the `INTERNET` permission in the Android export preset before exporting the project or using one-click deploy. Otherwise, network communication of any kind will be blocked by Android.

<a id="tutorials"></a>

## Tutorials

- [TLS certificates](../tutorials/networking/ssl_certificates.md)

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Error](class_@globalscope.md#enum-globalscope-error) | [accept_stream](class_streampeertls.md#class-streampeertls-method-accept-stream)(stream: [StreamPeer](class_streampeer.md#class-streampeer), server_options: [TLSOptions](class_tlsoptions.md#class-tlsoptions)) |
| [Error](class_@globalscope.md#enum-globalscope-error) | [connect_to_stream](class_streampeertls.md#class-streampeertls-method-connect-to-stream)(stream: [StreamPeer](class_streampeer.md#class-streampeer), common_name: [String](class_string.md#class-string), client_options: [TLSOptions](class_tlsoptions.md#class-tlsoptions) = null) |
| void | [disconnect_from_stream](class_streampeertls.md#class-streampeertls-method-disconnect-from-stream)() |
| [Status](class_streampeertls.md#enum-streampeertls-status) | [get_status](class_streampeertls.md#class-streampeertls-method-get-status)() const |
| [StreamPeer](class_streampeer.md#class-streampeer) | [get_stream](class_streampeertls.md#class-streampeertls-method-get-stream)() const |
| void | [poll](class_streampeertls.md#class-streampeertls-method-poll)() |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-streampeertls-status"></a>

enum **Status**: [🔗](class_streampeertls.md#enum-streampeertls-status)

<a id="class-streampeertls-constant-status-disconnected"></a>

[Status](class_streampeertls.md#enum-streampeertls-status) **STATUS_DISCONNECTED** = `0`

A status representing a **StreamPeerTLS** that is disconnected.

<a id="class-streampeertls-constant-status-handshaking"></a>

[Status](class_streampeertls.md#enum-streampeertls-status) **STATUS_HANDSHAKING** = `1`

A status representing a **StreamPeerTLS** during handshaking.

<a id="class-streampeertls-constant-status-connected"></a>

[Status](class_streampeertls.md#enum-streampeertls-status) **STATUS_CONNECTED** = `2`

A status representing a **StreamPeerTLS** that is connected to a host.

<a id="class-streampeertls-constant-status-error"></a>

[Status](class_streampeertls.md#enum-streampeertls-status) **STATUS_ERROR** = `3`

A status representing a **StreamPeerTLS** in error state.

<a id="class-streampeertls-constant-status-error-hostname-mismatch"></a>

[Status](class_streampeertls.md#enum-streampeertls-status) **STATUS_ERROR_HOSTNAME_MISMATCH** = `4`

An error status that shows a mismatch in the TLS certificate domain presented by the host and the domain requested for validation.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-streampeertls-method-accept-stream"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **accept_stream**(stream: [StreamPeer](class_streampeer.md#class-streampeer), server_options: [TLSOptions](class_tlsoptions.md#class-tlsoptions)) [🔗](class_streampeertls.md#class-streampeertls-method-accept-stream)

Accepts a peer connection as a server using the given `server_options`. See [TLSOptions.server()](class_tlsoptions.md#class-tlsoptions-method-server).

---


<a id="class-streampeertls-method-connect-to-stream"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **connect_to_stream**(stream: [StreamPeer](class_streampeer.md#class-streampeer), common_name: [String](class_string.md#class-string), client_options: [TLSOptions](class_tlsoptions.md#class-tlsoptions) = null) [🔗](class_streampeertls.md#class-streampeertls-method-connect-to-stream)

Connects to a peer using an underlying [StreamPeer](class_streampeer.md#class-streampeer) `stream` and verifying the remote certificate is correctly signed for the given `common_name`. You can pass the optional `client_options` parameter to customize the trusted certification authorities, or disable the common name verification. See [TLSOptions.client()](class_tlsoptions.md#class-tlsoptions-method-client) and [TLSOptions.client_unsafe()](class_tlsoptions.md#class-tlsoptions-method-client-unsafe).

---


<a id="class-streampeertls-method-disconnect-from-stream"></a>

void **disconnect_from_stream**() [🔗](class_streampeertls.md#class-streampeertls-method-disconnect-from-stream)

Disconnects from host.

---


<a id="class-streampeertls-method-get-status"></a>

[Status](class_streampeertls.md#enum-streampeertls-status) **get_status**() const [🔗](class_streampeertls.md#class-streampeertls-method-get-status)

Returns the status of the connection.

---


<a id="class-streampeertls-method-get-stream"></a>

[StreamPeer](class_streampeer.md#class-streampeer) **get_stream**() const [🔗](class_streampeertls.md#class-streampeertls-method-get-stream)

Returns the underlying [StreamPeer](class_streampeer.md#class-streampeer) connection, used in [accept_stream()](class_streampeertls.md#class-streampeertls-method-accept-stream) or [connect_to_stream()](class_streampeertls.md#class-streampeertls-method-connect-to-stream).

---


<a id="class-streampeertls-method-poll"></a>

void **poll**() [🔗](class_streampeertls.md#class-streampeertls-method-poll)

Poll the connection to check for incoming bytes. Call this right before [StreamPeer.get_available_bytes()](class_streampeer.md#class-streampeer-method-get-available-bytes) for it to work properly.
