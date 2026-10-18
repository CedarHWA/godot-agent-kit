> Source: https://docs.godotengine.org/en/4.7/classes/class_enetconnection.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="enetconnection"></a>

<a id="class-enetconnection"></a>

# ENetConnection

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A wrapper class for an [ENetHost](http://enet.bespin.org/group__host.html).

<a id="description"></a>

## Description

ENet's purpose is to provide a relatively thin, simple and robust network communication layer on top of UDP (User Datagram Protocol).

<a id="tutorials"></a>

## Tutorials

- [API documentation on the ENet website](http://enet.bespin.org/usergroup0.html)

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [bandwidth_limit](class_enetconnection.md#class-enetconnection-method-bandwidth-limit)(in_bandwidth: [int](class_int.md#class-int) = 0, out_bandwidth: [int](class_int.md#class-int) = 0) |
| void | [broadcast](class_enetconnection.md#class-enetconnection-method-broadcast)(channel: [int](class_int.md#class-int), packet: [PackedByteArray](class_packedbytearray.md#class-packedbytearray), flags: [int](class_int.md#class-int)) |
| void | [channel_limit](class_enetconnection.md#class-enetconnection-method-channel-limit)(limit: [int](class_int.md#class-int)) |
| void | [compress](class_enetconnection.md#class-enetconnection-method-compress)(mode: [CompressionMode](class_enetconnection.md#enum-enetconnection-compressionmode)) |
| [ENetPacketPeer](class_enetpacketpeer.md#class-enetpacketpeer) | [connect_to_host](class_enetconnection.md#class-enetconnection-method-connect-to-host)(address: [String](class_string.md#class-string), port: [int](class_int.md#class-int), channels: [int](class_int.md#class-int) = 0, data: [int](class_int.md#class-int) = 0) |
| [Error](class_@globalscope.md#enum-globalscope-error) | [create_host](class_enetconnection.md#class-enetconnection-method-create-host)(max_peers: [int](class_int.md#class-int) = 32, max_channels: [int](class_int.md#class-int) = 0, in_bandwidth: [int](class_int.md#class-int) = 0, out_bandwidth: [int](class_int.md#class-int) = 0) |
| [Error](class_@globalscope.md#enum-globalscope-error) | [create_host_bound](class_enetconnection.md#class-enetconnection-method-create-host-bound)(bind_address: [String](class_string.md#class-string), bind_port: [int](class_int.md#class-int), max_peers: [int](class_int.md#class-int) = 32, max_channels: [int](class_int.md#class-int) = 0, in_bandwidth: [int](class_int.md#class-int) = 0, out_bandwidth: [int](class_int.md#class-int) = 0) |
| void | [destroy](class_enetconnection.md#class-enetconnection-method-destroy)() |
| [Error](class_@globalscope.md#enum-globalscope-error) | [dtls_client_setup](class_enetconnection.md#class-enetconnection-method-dtls-client-setup)(hostname: [String](class_string.md#class-string), client_options: [TLSOptions](class_tlsoptions.md#class-tlsoptions) = null) |
| [Error](class_@globalscope.md#enum-globalscope-error) | [dtls_server_setup](class_enetconnection.md#class-enetconnection-method-dtls-server-setup)(server_options: [TLSOptions](class_tlsoptions.md#class-tlsoptions)) |
| void | [flush](class_enetconnection.md#class-enetconnection-method-flush)() |
| [int](class_int.md#class-int) | [get_local_port](class_enetconnection.md#class-enetconnection-method-get-local-port)() const |
| [int](class_int.md#class-int) | [get_max_channels](class_enetconnection.md#class-enetconnection-method-get-max-channels)() const |
| [Array](class_array.md#class-array)[[ENetPacketPeer](class_enetpacketpeer.md#class-enetpacketpeer)] | [get_peers](class_enetconnection.md#class-enetconnection-method-get-peers)() |
| [float](class_float.md#class-float) | [pop_statistic](class_enetconnection.md#class-enetconnection-method-pop-statistic)(statistic: [HostStatistic](class_enetconnection.md#enum-enetconnection-hoststatistic)) |
| void | [refuse_new_connections](class_enetconnection.md#class-enetconnection-method-refuse-new-connections)(refuse: [bool](class_bool.md#class-bool)) |
| [Array](class_array.md#class-array) | [service](class_enetconnection.md#class-enetconnection-method-service)(timeout: [int](class_int.md#class-int) = 0) |
| void | [socket_send](class_enetconnection.md#class-enetconnection-method-socket-send)(destination_address: [String](class_string.md#class-string), destination_port: [int](class_int.md#class-int), packet: [PackedByteArray](class_packedbytearray.md#class-packedbytearray)) |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-enetconnection-compressionmode"></a>

enum **CompressionMode**: [🔗](class_enetconnection.md#enum-enetconnection-compressionmode)

<a id="class-enetconnection-constant-compress-none"></a>

[CompressionMode](class_enetconnection.md#enum-enetconnection-compressionmode) **COMPRESS_NONE** = `0`

No compression. This uses the most bandwidth, but has the upside of requiring the fewest CPU resources. This option may also be used to make network debugging using tools like Wireshark easier.

<a id="class-enetconnection-constant-compress-range-coder"></a>

[CompressionMode](class_enetconnection.md#enum-enetconnection-compressionmode) **COMPRESS_RANGE_CODER** = `1`

ENet's built-in range encoding. Works well on small packets, but is not the most efficient algorithm on packets larger than 4 KB.

<a id="class-enetconnection-constant-compress-fastlz"></a>

[CompressionMode](class_enetconnection.md#enum-enetconnection-compressionmode) **COMPRESS_FASTLZ** = `2`

[FastLZ](https://fastlz.org/) compression. This option uses less CPU resources compared to [COMPRESS_ZLIB](class_enetconnection.md#class-enetconnection-constant-compress-zlib), at the expense of using more bandwidth.

<a id="class-enetconnection-constant-compress-zlib"></a>

[CompressionMode](class_enetconnection.md#enum-enetconnection-compressionmode) **COMPRESS_ZLIB** = `3`

[Zlib](https://www.zlib.net/) compression. This option uses less bandwidth compared to [COMPRESS_FASTLZ](class_enetconnection.md#class-enetconnection-constant-compress-fastlz), at the expense of using more CPU resources.

<a id="class-enetconnection-constant-compress-zstd"></a>

[CompressionMode](class_enetconnection.md#enum-enetconnection-compressionmode) **COMPRESS_ZSTD** = `4`

[Zstandard](https://facebook.github.io/zstd/) compression. Note that this algorithm is not very efficient on packets smaller than 4 KB. Therefore, it's recommended to use other compression algorithms in most cases.

---


<a id="enum-enetconnection-eventtype"></a>

enum **EventType**: [🔗](class_enetconnection.md#enum-enetconnection-eventtype)

<a id="class-enetconnection-constant-event-error"></a>

[EventType](class_enetconnection.md#enum-enetconnection-eventtype) **EVENT_ERROR** = `-1`

An error occurred during [service()](class_enetconnection.md#class-enetconnection-method-service). You will likely need to [destroy()](class_enetconnection.md#class-enetconnection-method-destroy) the host and recreate it.

<a id="class-enetconnection-constant-event-none"></a>

[EventType](class_enetconnection.md#enum-enetconnection-eventtype) **EVENT_NONE** = `0`

No event occurred within the specified time limit.

<a id="class-enetconnection-constant-event-connect"></a>

[EventType](class_enetconnection.md#enum-enetconnection-eventtype) **EVENT_CONNECT** = `1`

A connection request initiated by enet_host_connect has completed. The array will contain the peer which successfully connected.

<a id="class-enetconnection-constant-event-disconnect"></a>

[EventType](class_enetconnection.md#enum-enetconnection-eventtype) **EVENT_DISCONNECT** = `2`

A peer has disconnected. This event is generated on a successful completion of a disconnect initiated by [ENetPacketPeer.peer_disconnect()](class_enetpacketpeer.md#class-enetpacketpeer-method-peer-disconnect), if a peer has timed out, or if a connection request initialized by [connect_to_host()](class_enetconnection.md#class-enetconnection-method-connect-to-host) has timed out. The array will contain the peer which disconnected. The data field contains user supplied data describing the disconnection, or 0, if none is available.

<a id="class-enetconnection-constant-event-receive"></a>

[EventType](class_enetconnection.md#enum-enetconnection-eventtype) **EVENT_RECEIVE** = `3`

A packet has been received from a peer. The array will contain the peer which sent the packet and the channel number upon which the packet was received. The received packet will be queued to the associated [ENetPacketPeer](class_enetpacketpeer.md#class-enetpacketpeer).

---


<a id="enum-enetconnection-hoststatistic"></a>

enum **HostStatistic**: [🔗](class_enetconnection.md#enum-enetconnection-hoststatistic)

<a id="class-enetconnection-constant-host-total-sent-data"></a>

[HostStatistic](class_enetconnection.md#enum-enetconnection-hoststatistic) **HOST_TOTAL_SENT_DATA** = `0`

Total data sent.

<a id="class-enetconnection-constant-host-total-sent-packets"></a>

[HostStatistic](class_enetconnection.md#enum-enetconnection-hoststatistic) **HOST_TOTAL_SENT_PACKETS** = `1`

Total UDP packets sent.

<a id="class-enetconnection-constant-host-total-received-data"></a>

[HostStatistic](class_enetconnection.md#enum-enetconnection-hoststatistic) **HOST_TOTAL_RECEIVED_DATA** = `2`

Total data received.

<a id="class-enetconnection-constant-host-total-received-packets"></a>

[HostStatistic](class_enetconnection.md#enum-enetconnection-hoststatistic) **HOST_TOTAL_RECEIVED_PACKETS** = `3`

Total UDP packets received.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-enetconnection-method-bandwidth-limit"></a>

void **bandwidth_limit**(in_bandwidth: [int](class_int.md#class-int) = 0, out_bandwidth: [int](class_int.md#class-int) = 0) [🔗](class_enetconnection.md#class-enetconnection-method-bandwidth-limit)

Adjusts the bandwidth limits of a host.

---


<a id="class-enetconnection-method-broadcast"></a>

void **broadcast**(channel: [int](class_int.md#class-int), packet: [PackedByteArray](class_packedbytearray.md#class-packedbytearray), flags: [int](class_int.md#class-int)) [🔗](class_enetconnection.md#class-enetconnection-method-broadcast)

Queues a `packet` to be sent to all peers associated with the host over the specified `channel`. See [ENetPacketPeer](class_enetpacketpeer.md#class-enetpacketpeer) `FLAG_*` constants for available packet flags.

---


<a id="class-enetconnection-method-channel-limit"></a>

void **channel_limit**(limit: [int](class_int.md#class-int)) [🔗](class_enetconnection.md#class-enetconnection-method-channel-limit)

Limits the maximum allowed channels of future incoming connections.

---


<a id="class-enetconnection-method-compress"></a>

void **compress**(mode: [CompressionMode](class_enetconnection.md#enum-enetconnection-compressionmode)) [🔗](class_enetconnection.md#class-enetconnection-method-compress)

Sets the compression method used for network packets. These have different tradeoffs of compression speed versus bandwidth, you may need to test which one works best for your use case if you use compression at all.

**Note:** Most games' network design involve sending many small packets frequently (smaller than 4 KB each). If in doubt, it is recommended to keep the default compression algorithm as it works best on these small packets.

**Note:** The compression mode must be set to the same value on both the server and all its clients. Clients will fail to connect if the compression mode set on the client differs from the one set on the server.

---


<a id="class-enetconnection-method-connect-to-host"></a>

[ENetPacketPeer](class_enetpacketpeer.md#class-enetpacketpeer) **connect_to_host**(address: [String](class_string.md#class-string), port: [int](class_int.md#class-int), channels: [int](class_int.md#class-int) = 0, data: [int](class_int.md#class-int) = 0) [🔗](class_enetconnection.md#class-enetconnection-method-connect-to-host)

Initiates a connection to a foreign `address` using the specified `port` and allocating the requested `channels`. Optional `data` can be passed during connection in the form of a 32 bit integer.

**Note:** You must call either [create_host()](class_enetconnection.md#class-enetconnection-method-create-host) or [create_host_bound()](class_enetconnection.md#class-enetconnection-method-create-host-bound) on both ends before calling this method.

---


<a id="class-enetconnection-method-create-host"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **create_host**(max_peers: [int](class_int.md#class-int) = 32, max_channels: [int](class_int.md#class-int) = 0, in_bandwidth: [int](class_int.md#class-int) = 0, out_bandwidth: [int](class_int.md#class-int) = 0) [🔗](class_enetconnection.md#class-enetconnection-method-create-host)

Creates an ENetHost that allows up to `max_peers` connected peers, each allocating up to `max_channels` channels, optionally limiting bandwidth to `in_bandwidth` and `out_bandwidth` (if greater than zero).

This method binds a random available dynamic UDP port on the host machine at the *unspecified* address. Use [create_host_bound()](class_enetconnection.md#class-enetconnection-method-create-host-bound) to specify the address and port.

**Note:** It is necessary to create a host in both client and server in order to establish a connection.

---


<a id="class-enetconnection-method-create-host-bound"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **create_host_bound**(bind_address: [String](class_string.md#class-string), bind_port: [int](class_int.md#class-int), max_peers: [int](class_int.md#class-int) = 32, max_channels: [int](class_int.md#class-int) = 0, in_bandwidth: [int](class_int.md#class-int) = 0, out_bandwidth: [int](class_int.md#class-int) = 0) [🔗](class_enetconnection.md#class-enetconnection-method-create-host-bound)

Creates an ENetHost bound to the given `bind_address` and `bind_port` that allows up to `max_peers` connected peers, each allocating up to `max_channels` channels, optionally limiting bandwidth to `in_bandwidth` and `out_bandwidth` (if greater than zero).

**Note:** It is necessary to create a host in both client and server in order to establish a connection.

---


<a id="class-enetconnection-method-destroy"></a>

void **destroy**() [🔗](class_enetconnection.md#class-enetconnection-method-destroy)

Destroys the host and all resources associated with it.

---


<a id="class-enetconnection-method-dtls-client-setup"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **dtls_client_setup**(hostname: [String](class_string.md#class-string), client_options: [TLSOptions](class_tlsoptions.md#class-tlsoptions) = null) [🔗](class_enetconnection.md#class-enetconnection-method-dtls-client-setup)

Configure this ENetHost to use the custom Godot extension allowing DTLS encryption for ENet clients. Call this before [connect_to_host()](class_enetconnection.md#class-enetconnection-method-connect-to-host) to have ENet connect using DTLS validating the server certificate against `hostname`. You can pass the optional `client_options` parameter to customize the trusted certification authorities, or disable the common name verification. See [TLSOptions.client()](class_tlsoptions.md#class-tlsoptions-method-client) and [TLSOptions.client_unsafe()](class_tlsoptions.md#class-tlsoptions-method-client-unsafe).

---


<a id="class-enetconnection-method-dtls-server-setup"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **dtls_server_setup**(server_options: [TLSOptions](class_tlsoptions.md#class-tlsoptions)) [🔗](class_enetconnection.md#class-enetconnection-method-dtls-server-setup)

Configure this ENetHost to use the custom Godot extension allowing DTLS encryption for ENet servers. Call this right after [create_host_bound()](class_enetconnection.md#class-enetconnection-method-create-host-bound) to have ENet expect peers to connect using DTLS. See [TLSOptions.server()](class_tlsoptions.md#class-tlsoptions-method-server).

---


<a id="class-enetconnection-method-flush"></a>

void **flush**() [🔗](class_enetconnection.md#class-enetconnection-method-flush)

Sends any queued packets on the host specified to its designated peers.

---


<a id="class-enetconnection-method-get-local-port"></a>

[int](class_int.md#class-int) **get_local_port**() const [🔗](class_enetconnection.md#class-enetconnection-method-get-local-port)

Returns the local port to which this peer is bound.

---


<a id="class-enetconnection-method-get-max-channels"></a>

[int](class_int.md#class-int) **get_max_channels**() const [🔗](class_enetconnection.md#class-enetconnection-method-get-max-channels)

Returns the maximum number of channels allowed for connected peers.

---


<a id="class-enetconnection-method-get-peers"></a>

[Array](class_array.md#class-array)[[ENetPacketPeer](class_enetpacketpeer.md#class-enetpacketpeer)] **get_peers**() [🔗](class_enetconnection.md#class-enetconnection-method-get-peers)

Returns the list of peers associated with this host.

**Note:** This list might include some peers that are not fully connected or are still being disconnected.

---


<a id="class-enetconnection-method-pop-statistic"></a>

[float](class_float.md#class-float) **pop_statistic**(statistic: [HostStatistic](class_enetconnection.md#enum-enetconnection-hoststatistic)) [🔗](class_enetconnection.md#class-enetconnection-method-pop-statistic)

Returns and resets host statistics.

---


<a id="class-enetconnection-method-refuse-new-connections"></a>

void **refuse_new_connections**(refuse: [bool](class_bool.md#class-bool)) [🔗](class_enetconnection.md#class-enetconnection-method-refuse-new-connections)

Configures the DTLS server to automatically drop new connections.

**Note:** This method is only relevant after calling [dtls_server_setup()](class_enetconnection.md#class-enetconnection-method-dtls-server-setup).

---


<a id="class-enetconnection-method-service"></a>

[Array](class_array.md#class-array) **service**(timeout: [int](class_int.md#class-int) = 0) [🔗](class_enetconnection.md#class-enetconnection-method-service)

Waits for events on this connection and shuttles packets between the host and its peers, with the given `timeout` (in milliseconds). The returned [Array](class_array.md#class-array) will have 4 elements. An [EventType](class_enetconnection.md#enum-enetconnection-eventtype), the [ENetPacketPeer](class_enetpacketpeer.md#class-enetpacketpeer) which generated the event, the event associated data (if any), the event associated channel (if any). If the generated event is [EVENT_RECEIVE](class_enetconnection.md#class-enetconnection-constant-event-receive), the received packet will be queued to the associated [ENetPacketPeer](class_enetpacketpeer.md#class-enetpacketpeer).

Call this function regularly to handle connections, disconnections, and to receive new packets.

**Note:** This method must be called on both ends involved in the event (sending and receiving hosts).

---


<a id="class-enetconnection-method-socket-send"></a>

void **socket_send**(destination_address: [String](class_string.md#class-string), destination_port: [int](class_int.md#class-int), packet: [PackedByteArray](class_packedbytearray.md#class-packedbytearray)) [🔗](class_enetconnection.md#class-enetconnection-method-socket-send)

Sends a `packet` toward a destination from the address and port currently bound by this ENetConnection instance.

This is useful as it serves to establish entries in NAT routing tables on all devices between this bound instance and the public facing internet, allowing a prospective client's connection packets to be routed backward through the NAT device(s) between the public internet and this host.

This requires forward knowledge of a prospective client's address and communication port as seen by the public internet - after any NAT devices have handled their connection request. This information can be obtained by a [STUN](https://en.wikipedia.org/wiki/STUN) service, and must be handed off to your host by an entity that is not the prospective client. This will never work for a client behind a Symmetric NAT due to the nature of the Symmetric NAT routing algorithm, as their IP and Port cannot be known beforehand.
