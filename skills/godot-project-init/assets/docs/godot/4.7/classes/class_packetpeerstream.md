> Source: https://docs.godotengine.org/en/4.7/classes/class_packetpeerstream.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="packetpeerstream"></a>

<a id="class-packetpeerstream"></a>

# PacketPeerStream

**Inherits:** [PacketPeer](class_packetpeer.md#class-packetpeer) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Wrapper to use a PacketPeer over a StreamPeer.

<a id="description"></a>

## Description

PacketStreamPeer provides a wrapper for working using packets over a stream. This allows for using packet based code with StreamPeers. PacketPeerStream implements a custom protocol over the StreamPeer, so the user should not read or write to the wrapped StreamPeer directly.

**Note:** When exporting to Android, make sure to enable the `INTERNET` permission in the Android export preset before exporting the project or using one-click deploy. Otherwise, network communication of any kind will be blocked by Android.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [input_buffer_max_size](class_packetpeerstream.md#class-packetpeerstream-property-input-buffer-max-size) | `65532` |
| [int](class_int.md#class-int) | [output_buffer_max_size](class_packetpeerstream.md#class-packetpeerstream-property-output-buffer-max-size) | `65532` |
| [StreamPeer](class_streampeer.md#class-streampeer) | [stream_peer](class_packetpeerstream.md#class-packetpeerstream-property-stream-peer) |  |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-packetpeerstream-property-input-buffer-max-size"></a>

[int](class_int.md#class-int) **input_buffer_max_size** = `65532` [🔗](class_packetpeerstream.md#class-packetpeerstream-property-input-buffer-max-size)

- void **set_input_buffer_max_size**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_input_buffer_max_size**()

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-packetpeerstream-property-output-buffer-max-size"></a>

[int](class_int.md#class-int) **output_buffer_max_size** = `65532` [🔗](class_packetpeerstream.md#class-packetpeerstream-property-output-buffer-max-size)

- void **set_output_buffer_max_size**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_output_buffer_max_size**()

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-packetpeerstream-property-stream-peer"></a>

[StreamPeer](class_streampeer.md#class-streampeer) **stream_peer** [🔗](class_packetpeerstream.md#class-packetpeerstream-property-stream-peer)

- void **set_stream_peer**(value: [StreamPeer](class_streampeer.md#class-streampeer))
- [StreamPeer](class_streampeer.md#class-streampeer) **get_stream_peer**()

The wrapped [StreamPeer](class_streampeer.md#class-streampeer) object.
