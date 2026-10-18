> Source: https://docs.godotengine.org/en/4.7/classes/class_webrtcdatachannelextension.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="webrtcdatachannelextension"></a>

<a id="class-webrtcdatachannelextension"></a>

# WebRTCDataChannelExtension

**Inherits:** [WebRTCDataChannel](class_webrtcdatachannel.md#class-webrtcdatachannel) **<** [PacketPeer](class_packetpeer.md#class-packetpeer) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

There is currently no description for this class. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [_close](class_webrtcdatachannelextension.md#class-webrtcdatachannelextension-private-method-close)() virtual required |
| [int](class_int.md#class-int) | [_get_available_packet_count](class_webrtcdatachannelextension.md#class-webrtcdatachannelextension-private-method-get-available-packet-count)() virtual required const |
| [int](class_int.md#class-int) | [_get_buffered_amount](class_webrtcdatachannelextension.md#class-webrtcdatachannelextension-private-method-get-buffered-amount)() virtual required const |
| [int](class_int.md#class-int) | [_get_id](class_webrtcdatachannelextension.md#class-webrtcdatachannelextension-private-method-get-id)() virtual required const |
| [String](class_string.md#class-string) | [_get_label](class_webrtcdatachannelextension.md#class-webrtcdatachannelextension-private-method-get-label)() virtual required const |
| [int](class_int.md#class-int) | [_get_max_packet_life_time](class_webrtcdatachannelextension.md#class-webrtcdatachannelextension-private-method-get-max-packet-life-time)() virtual required const |
| [int](class_int.md#class-int) | [_get_max_packet_size](class_webrtcdatachannelextension.md#class-webrtcdatachannelextension-private-method-get-max-packet-size)() virtual required const |
| [int](class_int.md#class-int) | [_get_max_retransmits](class_webrtcdatachannelextension.md#class-webrtcdatachannelextension-private-method-get-max-retransmits)() virtual required const |
| [Error](class_@globalscope.md#enum-globalscope-error) | [_get_packet](class_webrtcdatachannelextension.md#class-webrtcdatachannelextension-private-method-get-packet)(r_buffer: `const uint8_t **`, r_buffer_size: `int32_t*`) virtual |
| [String](class_string.md#class-string) | [_get_protocol](class_webrtcdatachannelextension.md#class-webrtcdatachannelextension-private-method-get-protocol)() virtual required const |
| [ChannelState](class_webrtcdatachannel.md#enum-webrtcdatachannel-channelstate) | [_get_ready_state](class_webrtcdatachannelextension.md#class-webrtcdatachannelextension-private-method-get-ready-state)() virtual required const |
| [WriteMode](class_webrtcdatachannel.md#enum-webrtcdatachannel-writemode) | [_get_write_mode](class_webrtcdatachannelextension.md#class-webrtcdatachannelextension-private-method-get-write-mode)() virtual required const |
| [bool](class_bool.md#class-bool) | [_is_negotiated](class_webrtcdatachannelextension.md#class-webrtcdatachannelextension-private-method-is-negotiated)() virtual required const |
| [bool](class_bool.md#class-bool) | [_is_ordered](class_webrtcdatachannelextension.md#class-webrtcdatachannelextension-private-method-is-ordered)() virtual required const |
| [Error](class_@globalscope.md#enum-globalscope-error) | [_poll](class_webrtcdatachannelextension.md#class-webrtcdatachannelextension-private-method-poll)() virtual required |
| [Error](class_@globalscope.md#enum-globalscope-error) | [_put_packet](class_webrtcdatachannelextension.md#class-webrtcdatachannelextension-private-method-put-packet)(buffer: `const uint8_t*`, buffer_size: [int](class_int.md#class-int)) virtual |
| void | [_set_write_mode](class_webrtcdatachannelextension.md#class-webrtcdatachannelextension-private-method-set-write-mode)(write_mode: [WriteMode](class_webrtcdatachannel.md#enum-webrtcdatachannel-writemode)) virtual required |
| [bool](class_bool.md#class-bool) | [_was_string_packet](class_webrtcdatachannelextension.md#class-webrtcdatachannelextension-private-method-was-string-packet)() virtual required const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-webrtcdatachannelextension-private-method-close"></a>

void **_close**() virtual required [🔗](class_webrtcdatachannelextension.md#class-webrtcdatachannelextension-private-method-close)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-webrtcdatachannelextension-private-method-get-available-packet-count"></a>

[int](class_int.md#class-int) **_get_available_packet_count**() virtual required const [🔗](class_webrtcdatachannelextension.md#class-webrtcdatachannelextension-private-method-get-available-packet-count)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-webrtcdatachannelextension-private-method-get-buffered-amount"></a>

[int](class_int.md#class-int) **_get_buffered_amount**() virtual required const [🔗](class_webrtcdatachannelextension.md#class-webrtcdatachannelextension-private-method-get-buffered-amount)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-webrtcdatachannelextension-private-method-get-id"></a>

[int](class_int.md#class-int) **_get_id**() virtual required const [🔗](class_webrtcdatachannelextension.md#class-webrtcdatachannelextension-private-method-get-id)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-webrtcdatachannelextension-private-method-get-label"></a>

[String](class_string.md#class-string) **_get_label**() virtual required const [🔗](class_webrtcdatachannelextension.md#class-webrtcdatachannelextension-private-method-get-label)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-webrtcdatachannelextension-private-method-get-max-packet-life-time"></a>

[int](class_int.md#class-int) **_get_max_packet_life_time**() virtual required const [🔗](class_webrtcdatachannelextension.md#class-webrtcdatachannelextension-private-method-get-max-packet-life-time)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-webrtcdatachannelextension-private-method-get-max-packet-size"></a>

[int](class_int.md#class-int) **_get_max_packet_size**() virtual required const [🔗](class_webrtcdatachannelextension.md#class-webrtcdatachannelextension-private-method-get-max-packet-size)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-webrtcdatachannelextension-private-method-get-max-retransmits"></a>

[int](class_int.md#class-int) **_get_max_retransmits**() virtual required const [🔗](class_webrtcdatachannelextension.md#class-webrtcdatachannelextension-private-method-get-max-retransmits)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-webrtcdatachannelextension-private-method-get-packet"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **_get_packet**(r_buffer: `const uint8_t **`, r_buffer_size: `int32_t*`) virtual [🔗](class_webrtcdatachannelextension.md#class-webrtcdatachannelextension-private-method-get-packet)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-webrtcdatachannelextension-private-method-get-protocol"></a>

[String](class_string.md#class-string) **_get_protocol**() virtual required const [🔗](class_webrtcdatachannelextension.md#class-webrtcdatachannelextension-private-method-get-protocol)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-webrtcdatachannelextension-private-method-get-ready-state"></a>

[ChannelState](class_webrtcdatachannel.md#enum-webrtcdatachannel-channelstate) **_get_ready_state**() virtual required const [🔗](class_webrtcdatachannelextension.md#class-webrtcdatachannelextension-private-method-get-ready-state)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-webrtcdatachannelextension-private-method-get-write-mode"></a>

[WriteMode](class_webrtcdatachannel.md#enum-webrtcdatachannel-writemode) **_get_write_mode**() virtual required const [🔗](class_webrtcdatachannelextension.md#class-webrtcdatachannelextension-private-method-get-write-mode)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-webrtcdatachannelextension-private-method-is-negotiated"></a>

[bool](class_bool.md#class-bool) **_is_negotiated**() virtual required const [🔗](class_webrtcdatachannelextension.md#class-webrtcdatachannelextension-private-method-is-negotiated)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-webrtcdatachannelextension-private-method-is-ordered"></a>

[bool](class_bool.md#class-bool) **_is_ordered**() virtual required const [🔗](class_webrtcdatachannelextension.md#class-webrtcdatachannelextension-private-method-is-ordered)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-webrtcdatachannelextension-private-method-poll"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **_poll**() virtual required [🔗](class_webrtcdatachannelextension.md#class-webrtcdatachannelextension-private-method-poll)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-webrtcdatachannelextension-private-method-put-packet"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **_put_packet**(buffer: `const uint8_t*`, buffer_size: [int](class_int.md#class-int)) virtual [🔗](class_webrtcdatachannelextension.md#class-webrtcdatachannelextension-private-method-put-packet)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-webrtcdatachannelextension-private-method-set-write-mode"></a>

void **_set_write_mode**(write_mode: [WriteMode](class_webrtcdatachannel.md#enum-webrtcdatachannel-writemode)) virtual required [🔗](class_webrtcdatachannelextension.md#class-webrtcdatachannelextension-private-method-set-write-mode)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-webrtcdatachannelextension-private-method-was-string-packet"></a>

[bool](class_bool.md#class-bool) **_was_string_packet**() virtual required const [🔗](class_webrtcdatachannelextension.md#class-webrtcdatachannelextension-private-method-was-string-packet)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!
