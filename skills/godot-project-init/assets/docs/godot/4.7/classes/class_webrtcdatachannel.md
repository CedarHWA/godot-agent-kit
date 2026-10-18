> Source: https://docs.godotengine.org/en/4.7/classes/class_webrtcdatachannel.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="webrtcdatachannel"></a>

<a id="class-webrtcdatachannel"></a>

# WebRTCDataChannel

**Inherits:** [PacketPeer](class_packetpeer.md#class-packetpeer) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [WebRTCDataChannelExtension](class_webrtcdatachannelextension.md#class-webrtcdatachannelextension)

There is currently no description for this class. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [WriteMode](class_webrtcdatachannel.md#enum-webrtcdatachannel-writemode) | [write_mode](class_webrtcdatachannel.md#class-webrtcdatachannel-property-write-mode) | `1` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [close](class_webrtcdatachannel.md#class-webrtcdatachannel-method-close)() |
| [int](class_int.md#class-int) | [get_buffered_amount](class_webrtcdatachannel.md#class-webrtcdatachannel-method-get-buffered-amount)() const |
| [int](class_int.md#class-int) | [get_id](class_webrtcdatachannel.md#class-webrtcdatachannel-method-get-id)() const |
| [String](class_string.md#class-string) | [get_label](class_webrtcdatachannel.md#class-webrtcdatachannel-method-get-label)() const |
| [int](class_int.md#class-int) | [get_max_packet_life_time](class_webrtcdatachannel.md#class-webrtcdatachannel-method-get-max-packet-life-time)() const |
| [int](class_int.md#class-int) | [get_max_retransmits](class_webrtcdatachannel.md#class-webrtcdatachannel-method-get-max-retransmits)() const |
| [String](class_string.md#class-string) | [get_protocol](class_webrtcdatachannel.md#class-webrtcdatachannel-method-get-protocol)() const |
| [ChannelState](class_webrtcdatachannel.md#enum-webrtcdatachannel-channelstate) | [get_ready_state](class_webrtcdatachannel.md#class-webrtcdatachannel-method-get-ready-state)() const |
| [bool](class_bool.md#class-bool) | [is_negotiated](class_webrtcdatachannel.md#class-webrtcdatachannel-method-is-negotiated)() const |
| [bool](class_bool.md#class-bool) | [is_ordered](class_webrtcdatachannel.md#class-webrtcdatachannel-method-is-ordered)() const |
| [Error](class_@globalscope.md#enum-globalscope-error) | [poll](class_webrtcdatachannel.md#class-webrtcdatachannel-method-poll)() |
| [bool](class_bool.md#class-bool) | [was_string_packet](class_webrtcdatachannel.md#class-webrtcdatachannel-method-was-string-packet)() const |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-webrtcdatachannel-writemode"></a>

enum **WriteMode**: [🔗](class_webrtcdatachannel.md#enum-webrtcdatachannel-writemode)

<a id="class-webrtcdatachannel-constant-write-mode-text"></a>

[WriteMode](class_webrtcdatachannel.md#enum-webrtcdatachannel-writemode) **WRITE_MODE_TEXT** = `0`

Tells the channel to send data over this channel as text. An external peer (non-Godot) would receive this as a string.

<a id="class-webrtcdatachannel-constant-write-mode-binary"></a>

[WriteMode](class_webrtcdatachannel.md#enum-webrtcdatachannel-writemode) **WRITE_MODE_BINARY** = `1`

Tells the channel to send data over this channel as binary. An external peer (non-Godot) would receive this as array buffer or blob.

---


<a id="enum-webrtcdatachannel-channelstate"></a>

enum **ChannelState**: [🔗](class_webrtcdatachannel.md#enum-webrtcdatachannel-channelstate)

<a id="class-webrtcdatachannel-constant-state-connecting"></a>

[ChannelState](class_webrtcdatachannel.md#enum-webrtcdatachannel-channelstate) **STATE_CONNECTING** = `0`

The channel was created, but it's still trying to connect.

<a id="class-webrtcdatachannel-constant-state-open"></a>

[ChannelState](class_webrtcdatachannel.md#enum-webrtcdatachannel-channelstate) **STATE_OPEN** = `1`

The channel is currently open, and data can flow over it.

<a id="class-webrtcdatachannel-constant-state-closing"></a>

[ChannelState](class_webrtcdatachannel.md#enum-webrtcdatachannel-channelstate) **STATE_CLOSING** = `2`

The channel is being closed, no new messages will be accepted, but those already in queue will be flushed.

<a id="class-webrtcdatachannel-constant-state-closed"></a>

[ChannelState](class_webrtcdatachannel.md#enum-webrtcdatachannel-channelstate) **STATE_CLOSED** = `3`

The channel was closed, or connection failed.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-webrtcdatachannel-property-write-mode"></a>

[WriteMode](class_webrtcdatachannel.md#enum-webrtcdatachannel-writemode) **write_mode** = `1` [🔗](class_webrtcdatachannel.md#class-webrtcdatachannel-property-write-mode)

- void **set_write_mode**(value: [WriteMode](class_webrtcdatachannel.md#enum-webrtcdatachannel-writemode))
- [WriteMode](class_webrtcdatachannel.md#enum-webrtcdatachannel-writemode) **get_write_mode**()

The transfer mode to use when sending outgoing packet. Either text or binary.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-webrtcdatachannel-method-close"></a>

void **close**() [🔗](class_webrtcdatachannel.md#class-webrtcdatachannel-method-close)

Closes this data channel, notifying the other peer.

---


<a id="class-webrtcdatachannel-method-get-buffered-amount"></a>

[int](class_int.md#class-int) **get_buffered_amount**() const [🔗](class_webrtcdatachannel.md#class-webrtcdatachannel-method-get-buffered-amount)

Returns the number of bytes currently queued to be sent over this channel.

---


<a id="class-webrtcdatachannel-method-get-id"></a>

[int](class_int.md#class-int) **get_id**() const [🔗](class_webrtcdatachannel.md#class-webrtcdatachannel-method-get-id)

Returns the ID assigned to this channel during creation (or auto-assigned during negotiation).

If the channel is not negotiated out-of-band the ID will only be available after the connection is established (will return `65535` until then).

---


<a id="class-webrtcdatachannel-method-get-label"></a>

[String](class_string.md#class-string) **get_label**() const [🔗](class_webrtcdatachannel.md#class-webrtcdatachannel-method-get-label)

Returns the label assigned to this channel during creation.

---


<a id="class-webrtcdatachannel-method-get-max-packet-life-time"></a>

[int](class_int.md#class-int) **get_max_packet_life_time**() const [🔗](class_webrtcdatachannel.md#class-webrtcdatachannel-method-get-max-packet-life-time)

Returns the `maxPacketLifeTime` value assigned to this channel during creation.

Will be `65535` if not specified.

---


<a id="class-webrtcdatachannel-method-get-max-retransmits"></a>

[int](class_int.md#class-int) **get_max_retransmits**() const [🔗](class_webrtcdatachannel.md#class-webrtcdatachannel-method-get-max-retransmits)

Returns the `maxRetransmits` value assigned to this channel during creation.

Will be `65535` if not specified.

---


<a id="class-webrtcdatachannel-method-get-protocol"></a>

[String](class_string.md#class-string) **get_protocol**() const [🔗](class_webrtcdatachannel.md#class-webrtcdatachannel-method-get-protocol)

Returns the sub-protocol assigned to this channel during creation. An empty string if not specified.

---


<a id="class-webrtcdatachannel-method-get-ready-state"></a>

[ChannelState](class_webrtcdatachannel.md#enum-webrtcdatachannel-channelstate) **get_ready_state**() const [🔗](class_webrtcdatachannel.md#class-webrtcdatachannel-method-get-ready-state)

Returns the current state of this channel.

---


<a id="class-webrtcdatachannel-method-is-negotiated"></a>

[bool](class_bool.md#class-bool) **is_negotiated**() const [🔗](class_webrtcdatachannel.md#class-webrtcdatachannel-method-is-negotiated)

Returns `true` if this channel was created with out-of-band configuration.

---


<a id="class-webrtcdatachannel-method-is-ordered"></a>

[bool](class_bool.md#class-bool) **is_ordered**() const [🔗](class_webrtcdatachannel.md#class-webrtcdatachannel-method-is-ordered)

Returns `true` if this channel was created with ordering enabled (default).

---


<a id="class-webrtcdatachannel-method-poll"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **poll**() [🔗](class_webrtcdatachannel.md#class-webrtcdatachannel-method-poll)

Reserved, but not used for now.

---


<a id="class-webrtcdatachannel-method-was-string-packet"></a>

[bool](class_bool.md#class-bool) **was_string_packet**() const [🔗](class_webrtcdatachannel.md#class-webrtcdatachannel-method-was-string-packet)

Returns `true` if the last received packet was transferred as text. See [write_mode](class_webrtcdatachannel.md#class-webrtcdatachannel-property-write-mode).
