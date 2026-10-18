> Source: https://docs.godotengine.org/en/4.7/classes/class_udpserver.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="udpserver"></a>

<a id="class-udpserver"></a>

# UDPServer

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Helper class to implement a UDP server.

<a id="description"></a>

## Description

A simple server that opens a UDP socket and returns connected [PacketPeerUDP](class_packetpeerudp.md#class-packetpeerudp) upon receiving new packets. See also [PacketPeerUDP.connect_to_host()](class_packetpeerudp.md#class-packetpeerudp-method-connect-to-host).

After starting the server ([listen()](class_udpserver.md#class-udpserver-method-listen)), you will need to [poll()](class_udpserver.md#class-udpserver-method-poll) it at regular intervals (e.g. inside [Node._process()](class_node.md#class-node-private-method-process)) for it to process new packets, delivering them to the appropriate [PacketPeerUDP](class_packetpeerudp.md#class-packetpeerudp), and taking new connections.

Below a small example of how it can be used:

```gdscript
# server_node.gd
class_name ServerNode
extends Node

var server = UDPServer.new()
var peers = []

func _ready():
    server.listen(4242)

func _process(delta):
    server.poll() # Important!
    if server.is_connection_available():
        var peer = server.take_connection()
        var packet = peer.get_packet()
        print("Accepted peer: %s:%s" % [peer.get_packet_ip(), peer.get_packet_port()])
        print("Received data: %s" % [packet.get_string_from_utf8()])
        # Reply so it knows we received the message.
        peer.put_packet(packet)
        # Keep a reference so we can keep contacting the remote peer.
        peers.append(peer)

    for i in range(0, peers.size()):
        pass # Do something with the connected peers.
```

```csharp
// ServerNode.cs
using Godot;
using System.Collections.Generic;

public partial class ServerNode : Node
{
    private UdpServer _server = new UdpServer();
    private List<PacketPeerUdp> _peers  = new List<PacketPeerUdp>();

    public override void _Ready()
    {
        _server.Listen(4242);
    }

    public override void _Process(double delta)
    {
        _server.Poll(); // Important!
        if (_server.IsConnectionAvailable())
        {
            PacketPeerUdp peer = _server.TakeConnection();
            byte[] packet = peer.GetPacket();
            GD.Print($"Accepted Peer: {peer.GetPacketIP()}:{peer.GetPacketPort()}");
            GD.Print($"Received Data: {packet.GetStringFromUtf8()}");
            // Reply so it knows we received the message.
            peer.PutPacket(packet);
            // Keep a reference so we can keep contacting the remote peer.
            _peers.Add(peer);
        }
        foreach (var peer in _peers)
        {
            // Do something with the peers.
        }
    }
}
```

```gdscript
# client_node.gd
class_name ClientNode
extends Node

var udp = PacketPeerUDP.new()
var connected = false

func _ready():
    udp.connect_to_host("127.0.0.1", 4242)

func _process(delta):
    if !connected:
        # Try to contact server
        udp.put_packet("The answer is... 42!".to_utf8_buffer())
    if udp.get_available_packet_count() > 0:
        print("Connected: %s" % udp.get_packet().get_string_from_utf8())
        connected = true
```

```csharp
// ClientNode.cs
using Godot;

public partial class ClientNode : Node
{
    private PacketPeerUdp _udp = new PacketPeerUdp();
    private bool _connected = false;

    public override void _Ready()
    {
        _udp.ConnectToHost("127.0.0.1", 4242);
    }

    public override void _Process(double delta)
    {
        if (!_connected)
        {
            // Try to contact server
            _udp.PutPacket("The Answer Is..42!".ToUtf8Buffer());
        }
        if (_udp.GetAvailablePacketCount() > 0)
        {
            GD.Print($"Connected: {_udp.GetPacket().GetStringFromUtf8()}");
            _connected = true;
        }
    }
}
```

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [max_pending_connections](class_udpserver.md#class-udpserver-property-max-pending-connections) | `16` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [int](class_int.md#class-int) | [get_local_port](class_udpserver.md#class-udpserver-method-get-local-port)() const |
| [bool](class_bool.md#class-bool) | [is_connection_available](class_udpserver.md#class-udpserver-method-is-connection-available)() const |
| [bool](class_bool.md#class-bool) | [is_listening](class_udpserver.md#class-udpserver-method-is-listening)() const |
| [Error](class_@globalscope.md#enum-globalscope-error) | [listen](class_udpserver.md#class-udpserver-method-listen)(port: [int](class_int.md#class-int), bind_address: [String](class_string.md#class-string) = "\*") |
| [Error](class_@globalscope.md#enum-globalscope-error) | [poll](class_udpserver.md#class-udpserver-method-poll)() |
| void | [stop](class_udpserver.md#class-udpserver-method-stop)() |
| [PacketPeerUDP](class_packetpeerudp.md#class-packetpeerudp) | [take_connection](class_udpserver.md#class-udpserver-method-take-connection)() |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-udpserver-property-max-pending-connections"></a>

[int](class_int.md#class-int) **max_pending_connections** = `16` [🔗](class_udpserver.md#class-udpserver-property-max-pending-connections)

- void **set_max_pending_connections**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_max_pending_connections**()

Define the maximum number of pending connections, during [poll()](class_udpserver.md#class-udpserver-method-poll), any new pending connection exceeding that value will be automatically dropped. Setting this value to `0` effectively prevents any new pending connection to be accepted (e.g. when all your players have connected).

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-udpserver-method-get-local-port"></a>

[int](class_int.md#class-int) **get_local_port**() const [🔗](class_udpserver.md#class-udpserver-method-get-local-port)

Returns the local port this server is listening to.

---


<a id="class-udpserver-method-is-connection-available"></a>

[bool](class_bool.md#class-bool) **is_connection_available**() const [🔗](class_udpserver.md#class-udpserver-method-is-connection-available)

Returns `true` if a packet with a new address/port combination was received on the socket.

---


<a id="class-udpserver-method-is-listening"></a>

[bool](class_bool.md#class-bool) **is_listening**() const [🔗](class_udpserver.md#class-udpserver-method-is-listening)

Returns `true` if the socket is open and listening on a port.

---


<a id="class-udpserver-method-listen"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **listen**(port: [int](class_int.md#class-int), bind_address: [String](class_string.md#class-string) = "\*") [🔗](class_udpserver.md#class-udpserver-method-listen)

Starts the server by opening a UDP socket listening on the given `port`. You can optionally specify a `bind_address` to only listen for packets sent to that address. See also [PacketPeerUDP.bind()](class_packetpeerudp.md#class-packetpeerudp-method-bind).

---


<a id="class-udpserver-method-poll"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **poll**() [🔗](class_udpserver.md#class-udpserver-method-poll)

Call this method at regular intervals (e.g. inside [Node._process()](class_node.md#class-node-private-method-process)) to process new packets. Any packet from a known address/port pair will be delivered to the appropriate [PacketPeerUDP](class_packetpeerudp.md#class-packetpeerudp), while any packet received from an unknown address/port pair will be added as a pending connection (see [is_connection_available()](class_udpserver.md#class-udpserver-method-is-connection-available) and [take_connection()](class_udpserver.md#class-udpserver-method-take-connection)). The maximum number of pending connections is defined via [max_pending_connections](class_udpserver.md#class-udpserver-property-max-pending-connections).

---


<a id="class-udpserver-method-stop"></a>

void **stop**() [🔗](class_udpserver.md#class-udpserver-method-stop)

Stops the server, closing the UDP socket if open. Will close all connected [PacketPeerUDP](class_packetpeerudp.md#class-packetpeerudp) accepted via [take_connection()](class_udpserver.md#class-udpserver-method-take-connection) (remote peers will not be notified).

---


<a id="class-udpserver-method-take-connection"></a>

[PacketPeerUDP](class_packetpeerudp.md#class-packetpeerudp) **take_connection**() [🔗](class_udpserver.md#class-udpserver-method-take-connection)

Returns the first pending connection (connected to the appropriate address/port). Will return `null` if no new connection is available. See also [is_connection_available()](class_udpserver.md#class-udpserver-method-is-connection-available), [PacketPeerUDP.connect_to_host()](class_packetpeerudp.md#class-packetpeerudp-method-connect-to-host).
