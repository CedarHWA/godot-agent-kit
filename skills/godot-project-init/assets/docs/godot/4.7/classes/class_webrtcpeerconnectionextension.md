> Source: https://docs.godotengine.org/en/4.7/classes/class_webrtcpeerconnectionextension.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="webrtcpeerconnectionextension"></a>

<a id="class-webrtcpeerconnectionextension"></a>

# WebRTCPeerConnectionExtension

**Inherits:** [WebRTCPeerConnection](class_webrtcpeerconnection.md#class-webrtcpeerconnection) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

There is currently no description for this class. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Error](class_@globalscope.md#enum-globalscope-error) | [_add_ice_candidate](class_webrtcpeerconnectionextension.md#class-webrtcpeerconnectionextension-private-method-add-ice-candidate)(sdp_mid_name: [String](class_string.md#class-string), sdp_mline_index: [int](class_int.md#class-int), sdp_name: [String](class_string.md#class-string)) virtual required |
| void | [_close](class_webrtcpeerconnectionextension.md#class-webrtcpeerconnectionextension-private-method-close)() virtual required |
| [WebRTCDataChannel](class_webrtcdatachannel.md#class-webrtcdatachannel) | [_create_data_channel](class_webrtcpeerconnectionextension.md#class-webrtcpeerconnectionextension-private-method-create-data-channel)(label: [String](class_string.md#class-string), config: [Dictionary](class_dictionary.md#class-dictionary)) virtual required |
| [Error](class_@globalscope.md#enum-globalscope-error) | [_create_offer](class_webrtcpeerconnectionextension.md#class-webrtcpeerconnectionextension-private-method-create-offer)() virtual required |
| [ConnectionState](class_webrtcpeerconnection.md#enum-webrtcpeerconnection-connectionstate) | [_get_connection_state](class_webrtcpeerconnectionextension.md#class-webrtcpeerconnectionextension-private-method-get-connection-state)() virtual required const |
| [GatheringState](class_webrtcpeerconnection.md#enum-webrtcpeerconnection-gatheringstate) | [_get_gathering_state](class_webrtcpeerconnectionextension.md#class-webrtcpeerconnectionextension-private-method-get-gathering-state)() virtual required const |
| [SignalingState](class_webrtcpeerconnection.md#enum-webrtcpeerconnection-signalingstate) | [_get_signaling_state](class_webrtcpeerconnectionextension.md#class-webrtcpeerconnectionextension-private-method-get-signaling-state)() virtual required const |
| [Error](class_@globalscope.md#enum-globalscope-error) | [_initialize](class_webrtcpeerconnectionextension.md#class-webrtcpeerconnectionextension-private-method-initialize)(config: [Dictionary](class_dictionary.md#class-dictionary)) virtual required |
| [Error](class_@globalscope.md#enum-globalscope-error) | [_poll](class_webrtcpeerconnectionextension.md#class-webrtcpeerconnectionextension-private-method-poll)() virtual required |
| [Error](class_@globalscope.md#enum-globalscope-error) | [_set_local_description](class_webrtcpeerconnectionextension.md#class-webrtcpeerconnectionextension-private-method-set-local-description)(type: [String](class_string.md#class-string), sdp: [String](class_string.md#class-string)) virtual required |
| [Error](class_@globalscope.md#enum-globalscope-error) | [_set_remote_description](class_webrtcpeerconnectionextension.md#class-webrtcpeerconnectionextension-private-method-set-remote-description)(type: [String](class_string.md#class-string), sdp: [String](class_string.md#class-string)) virtual required |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-webrtcpeerconnectionextension-private-method-add-ice-candidate"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **_add_ice_candidate**(sdp_mid_name: [String](class_string.md#class-string), sdp_mline_index: [int](class_int.md#class-int), sdp_name: [String](class_string.md#class-string)) virtual required [🔗](class_webrtcpeerconnectionextension.md#class-webrtcpeerconnectionextension-private-method-add-ice-candidate)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-webrtcpeerconnectionextension-private-method-close"></a>

void **_close**() virtual required [🔗](class_webrtcpeerconnectionextension.md#class-webrtcpeerconnectionextension-private-method-close)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-webrtcpeerconnectionextension-private-method-create-data-channel"></a>

[WebRTCDataChannel](class_webrtcdatachannel.md#class-webrtcdatachannel) **_create_data_channel**(label: [String](class_string.md#class-string), config: [Dictionary](class_dictionary.md#class-dictionary)) virtual required [🔗](class_webrtcpeerconnectionextension.md#class-webrtcpeerconnectionextension-private-method-create-data-channel)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-webrtcpeerconnectionextension-private-method-create-offer"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **_create_offer**() virtual required [🔗](class_webrtcpeerconnectionextension.md#class-webrtcpeerconnectionextension-private-method-create-offer)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-webrtcpeerconnectionextension-private-method-get-connection-state"></a>

[ConnectionState](class_webrtcpeerconnection.md#enum-webrtcpeerconnection-connectionstate) **_get_connection_state**() virtual required const [🔗](class_webrtcpeerconnectionextension.md#class-webrtcpeerconnectionextension-private-method-get-connection-state)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-webrtcpeerconnectionextension-private-method-get-gathering-state"></a>

[GatheringState](class_webrtcpeerconnection.md#enum-webrtcpeerconnection-gatheringstate) **_get_gathering_state**() virtual required const [🔗](class_webrtcpeerconnectionextension.md#class-webrtcpeerconnectionextension-private-method-get-gathering-state)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-webrtcpeerconnectionextension-private-method-get-signaling-state"></a>

[SignalingState](class_webrtcpeerconnection.md#enum-webrtcpeerconnection-signalingstate) **_get_signaling_state**() virtual required const [🔗](class_webrtcpeerconnectionextension.md#class-webrtcpeerconnectionextension-private-method-get-signaling-state)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-webrtcpeerconnectionextension-private-method-initialize"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **_initialize**(config: [Dictionary](class_dictionary.md#class-dictionary)) virtual required [🔗](class_webrtcpeerconnectionextension.md#class-webrtcpeerconnectionextension-private-method-initialize)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-webrtcpeerconnectionextension-private-method-poll"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **_poll**() virtual required [🔗](class_webrtcpeerconnectionextension.md#class-webrtcpeerconnectionextension-private-method-poll)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-webrtcpeerconnectionextension-private-method-set-local-description"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **_set_local_description**(type: [String](class_string.md#class-string), sdp: [String](class_string.md#class-string)) virtual required [🔗](class_webrtcpeerconnectionextension.md#class-webrtcpeerconnectionextension-private-method-set-local-description)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-webrtcpeerconnectionextension-private-method-set-remote-description"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **_set_remote_description**(type: [String](class_string.md#class-string), sdp: [String](class_string.md#class-string)) virtual required [🔗](class_webrtcpeerconnectionextension.md#class-webrtcpeerconnectionextension-private-method-set-remote-description)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!
