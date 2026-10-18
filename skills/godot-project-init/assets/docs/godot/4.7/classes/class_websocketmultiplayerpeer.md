> Source: https://docs.godotengine.org/en/4.7/classes/class_websocketmultiplayerpeer.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="websocketmultiplayerpeer"></a>

<a id="class-websocketmultiplayerpeer"></a>

# WebSocketMultiplayerPeer

**Inherits:** [MultiplayerPeer](class_multiplayerpeer.md#class-multiplayerpeer) **<** [PacketPeer](class_packetpeer.md#class-packetpeer) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Base class for WebSocket server and client.

<a id="description"></a>

## Description

Base class for WebSocket server and client, allowing them to be used as multiplayer peer for the [MultiplayerAPI](class_multiplayerapi.md#class-multiplayerapi).

**Note:** When exporting to Android, make sure to enable the `INTERNET` permission in the Android export preset before exporting the project or using one-click deploy. Otherwise, network communication of any kind will be blocked by Android.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [handshake_headers](class_websocketmultiplayerpeer.md#class-websocketmultiplayerpeer-property-handshake-headers) | `PackedStringArray()` |
| [float](class_float.md#class-float) | [handshake_timeout](class_websocketmultiplayerpeer.md#class-websocketmultiplayerpeer-property-handshake-timeout) | `3.0` |
| [int](class_int.md#class-int) | [inbound_buffer_size](class_websocketmultiplayerpeer.md#class-websocketmultiplayerpeer-property-inbound-buffer-size) | `65535` |
| [int](class_int.md#class-int) | [max_queued_packets](class_websocketmultiplayerpeer.md#class-websocketmultiplayerpeer-property-max-queued-packets) | `4096` |
| [int](class_int.md#class-int) | [outbound_buffer_size](class_websocketmultiplayerpeer.md#class-websocketmultiplayerpeer-property-outbound-buffer-size) | `65535` |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [supported_protocols](class_websocketmultiplayerpeer.md#class-websocketmultiplayerpeer-property-supported-protocols) | `PackedStringArray()` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Error](class_@globalscope.md#enum-globalscope-error) | [create_client](class_websocketmultiplayerpeer.md#class-websocketmultiplayerpeer-method-create-client)(url: [String](class_string.md#class-string), tls_client_options: [TLSOptions](class_tlsoptions.md#class-tlsoptions) = null) |
| [Error](class_@globalscope.md#enum-globalscope-error) | [create_server](class_websocketmultiplayerpeer.md#class-websocketmultiplayerpeer-method-create-server)(port: [int](class_int.md#class-int), bind_address: [String](class_string.md#class-string) = "\*", tls_server_options: [TLSOptions](class_tlsoptions.md#class-tlsoptions) = null) |
| [WebSocketPeer](class_websocketpeer.md#class-websocketpeer) | [get_peer](class_websocketmultiplayerpeer.md#class-websocketmultiplayerpeer-method-get-peer)(peer_id: [int](class_int.md#class-int)) const |
| [String](class_string.md#class-string) | [get_peer_address](class_websocketmultiplayerpeer.md#class-websocketmultiplayerpeer-method-get-peer-address)(id: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_peer_port](class_websocketmultiplayerpeer.md#class-websocketmultiplayerpeer-method-get-peer-port)(id: [int](class_int.md#class-int)) const |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-websocketmultiplayerpeer-property-handshake-headers"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **handshake_headers** = `PackedStringArray()` [🔗](class_websocketmultiplayerpeer.md#class-websocketmultiplayerpeer-property-handshake-headers)

- void **set_handshake_headers**(value: [PackedStringArray](class_packedstringarray.md#class-packedstringarray))
- [PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_handshake_headers**()

The extra headers to use during handshake. See [WebSocketPeer.handshake_headers](class_websocketpeer.md#class-websocketpeer-property-handshake-headers) for more details.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedStringArray](class_packedstringarray.md#class-packedstringarray) for more details.

---


<a id="class-websocketmultiplayerpeer-property-handshake-timeout"></a>

[float](class_float.md#class-float) **handshake_timeout** = `3.0` [🔗](class_websocketmultiplayerpeer.md#class-websocketmultiplayerpeer-property-handshake-timeout)

- void **set_handshake_timeout**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_handshake_timeout**()

The maximum time each peer can stay in a connecting state before being dropped.

---


<a id="class-websocketmultiplayerpeer-property-inbound-buffer-size"></a>

[int](class_int.md#class-int) **inbound_buffer_size** = `65535` [🔗](class_websocketmultiplayerpeer.md#class-websocketmultiplayerpeer-property-inbound-buffer-size)

- void **set_inbound_buffer_size**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_inbound_buffer_size**()

The inbound buffer size for connected peers. See [WebSocketPeer.inbound_buffer_size](class_websocketpeer.md#class-websocketpeer-property-inbound-buffer-size) for more details.

---


<a id="class-websocketmultiplayerpeer-property-max-queued-packets"></a>

[int](class_int.md#class-int) **max_queued_packets** = `4096` [🔗](class_websocketmultiplayerpeer.md#class-websocketmultiplayerpeer-property-max-queued-packets)

- void **set_max_queued_packets**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_max_queued_packets**()

The maximum number of queued packets for connected peers. See [WebSocketPeer.max_queued_packets](class_websocketpeer.md#class-websocketpeer-property-max-queued-packets) for more details.

---


<a id="class-websocketmultiplayerpeer-property-outbound-buffer-size"></a>

[int](class_int.md#class-int) **outbound_buffer_size** = `65535` [🔗](class_websocketmultiplayerpeer.md#class-websocketmultiplayerpeer-property-outbound-buffer-size)

- void **set_outbound_buffer_size**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_outbound_buffer_size**()

The outbound buffer size for connected peers. See [WebSocketPeer.outbound_buffer_size](class_websocketpeer.md#class-websocketpeer-property-outbound-buffer-size) for more details.

---


<a id="class-websocketmultiplayerpeer-property-supported-protocols"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **supported_protocols** = `PackedStringArray()` [🔗](class_websocketmultiplayerpeer.md#class-websocketmultiplayerpeer-property-supported-protocols)

- void **set_supported_protocols**(value: [PackedStringArray](class_packedstringarray.md#class-packedstringarray))
- [PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_supported_protocols**()

The supported WebSocket sub-protocols. See [WebSocketPeer.supported_protocols](class_websocketpeer.md#class-websocketpeer-property-supported-protocols) for more details.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedStringArray](class_packedstringarray.md#class-packedstringarray) for more details.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-websocketmultiplayerpeer-method-create-client"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **create_client**(url: [String](class_string.md#class-string), tls_client_options: [TLSOptions](class_tlsoptions.md#class-tlsoptions) = null) [🔗](class_websocketmultiplayerpeer.md#class-websocketmultiplayerpeer-method-create-client)

Starts a new multiplayer client connecting to the given `url`. TLS certificates will be verified against the hostname when connecting using the `wss://` protocol. You can pass the optional `tls_client_options` parameter to customize the trusted certification authorities, or disable the common name verification. See [TLSOptions.client()](class_tlsoptions.md#class-tlsoptions-method-client) and [TLSOptions.client_unsafe()](class_tlsoptions.md#class-tlsoptions-method-client-unsafe).

**Note:** It is recommended to specify the scheme part of the URL, i.e. the `url` should start with either `ws://` or `wss://`.

---


<a id="class-websocketmultiplayerpeer-method-create-server"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **create_server**(port: [int](class_int.md#class-int), bind_address: [String](class_string.md#class-string) = "\*", tls_server_options: [TLSOptions](class_tlsoptions.md#class-tlsoptions) = null) [🔗](class_websocketmultiplayerpeer.md#class-websocketmultiplayerpeer-method-create-server)

Starts a new multiplayer server listening on the given `port`. You can optionally specify a `bind_address`, and provide valid `tls_server_options` to use TLS. See [TLSOptions.server()](class_tlsoptions.md#class-tlsoptions-method-server).

---


<a id="class-websocketmultiplayerpeer-method-get-peer"></a>

[WebSocketPeer](class_websocketpeer.md#class-websocketpeer) **get_peer**(peer_id: [int](class_int.md#class-int)) const [🔗](class_websocketmultiplayerpeer.md#class-websocketmultiplayerpeer-method-get-peer)

Returns the [WebSocketPeer](class_websocketpeer.md#class-websocketpeer) associated to the given `peer_id`.

---


<a id="class-websocketmultiplayerpeer-method-get-peer-address"></a>

[String](class_string.md#class-string) **get_peer_address**(id: [int](class_int.md#class-int)) const [🔗](class_websocketmultiplayerpeer.md#class-websocketmultiplayerpeer-method-get-peer-address)

Returns the IP address of the given peer.

---


<a id="class-websocketmultiplayerpeer-method-get-peer-port"></a>

[int](class_int.md#class-int) **get_peer_port**(id: [int](class_int.md#class-int)) const [🔗](class_websocketmultiplayerpeer.md#class-websocketmultiplayerpeer-method-get-peer-port)

Returns the remote port of the given peer.
