> Source: https://docs.godotengine.org/en/4.7/classes/class_ip.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="ip"></a>

<a id="class-ip"></a>

# IP

**Inherits:** [Object](class_object.md#class-object)

Internet protocol (IP) support functions such as DNS resolution.

<a id="description"></a>

## Description

IP contains support functions for the Internet Protocol (IP). TCP/IP support is in different classes (see [StreamPeerTCP](class_streampeertcp.md#class-streampeertcp) and [TCPServer](class_tcpserver.md#class-tcpserver)). IP provides DNS hostname resolution support, both blocking and threaded.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [clear_cache](class_ip.md#class-ip-method-clear-cache)(hostname: [String](class_string.md#class-string) = "") |
| void | [erase_resolve_item](class_ip.md#class-ip-method-erase-resolve-item)(id: [int](class_int.md#class-int)) |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [get_local_addresses](class_ip.md#class-ip-method-get-local-addresses)() const |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | [get_local_interfaces](class_ip.md#class-ip-method-get-local-interfaces)() const |
| [String](class_string.md#class-string) | [get_resolve_item_address](class_ip.md#class-ip-method-get-resolve-item-address)(id: [int](class_int.md#class-int)) const |
| [Array](class_array.md#class-array) | [get_resolve_item_addresses](class_ip.md#class-ip-method-get-resolve-item-addresses)(id: [int](class_int.md#class-int)) const |
| [ResolverStatus](class_ip.md#enum-ip-resolverstatus) | [get_resolve_item_status](class_ip.md#class-ip-method-get-resolve-item-status)(id: [int](class_int.md#class-int)) const |
| [String](class_string.md#class-string) | [resolve_hostname](class_ip.md#class-ip-method-resolve-hostname)(host: [String](class_string.md#class-string), ip_type: [Type](class_ip.md#enum-ip-type) = 3) |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | [resolve_hostname_addresses](class_ip.md#class-ip-method-resolve-hostname-addresses)(host: [String](class_string.md#class-string), ip_type: [Type](class_ip.md#enum-ip-type) = 3) |
| [int](class_int.md#class-int) | [resolve_hostname_queue_item](class_ip.md#class-ip-method-resolve-hostname-queue-item)(host: [String](class_string.md#class-string), ip_type: [Type](class_ip.md#enum-ip-type) = 3) |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-ip-resolverstatus"></a>

enum **ResolverStatus**: [🔗](class_ip.md#enum-ip-resolverstatus)

<a id="class-ip-constant-resolver-status-none"></a>

[ResolverStatus](class_ip.md#enum-ip-resolverstatus) **RESOLVER_STATUS_NONE** = `0`

DNS hostname resolver status: No status.

<a id="class-ip-constant-resolver-status-waiting"></a>

[ResolverStatus](class_ip.md#enum-ip-resolverstatus) **RESOLVER_STATUS_WAITING** = `1`

DNS hostname resolver status: Waiting.

<a id="class-ip-constant-resolver-status-done"></a>

[ResolverStatus](class_ip.md#enum-ip-resolverstatus) **RESOLVER_STATUS_DONE** = `2`

DNS hostname resolver status: Done.

<a id="class-ip-constant-resolver-status-error"></a>

[ResolverStatus](class_ip.md#enum-ip-resolverstatus) **RESOLVER_STATUS_ERROR** = `3`

DNS hostname resolver status: Error.

---


<a id="enum-ip-type"></a>

enum **Type**: [🔗](class_ip.md#enum-ip-type)

<a id="class-ip-constant-type-none"></a>

[Type](class_ip.md#enum-ip-type) **TYPE_NONE** = `0`

Address type: None.

<a id="class-ip-constant-type-ipv4"></a>

[Type](class_ip.md#enum-ip-type) **TYPE_IPV4** = `1`

Address type: Internet protocol version 4 (IPv4).

<a id="class-ip-constant-type-ipv6"></a>

[Type](class_ip.md#enum-ip-type) **TYPE_IPV6** = `2`

Address type: Internet protocol version 6 (IPv6).

<a id="class-ip-constant-type-any"></a>

[Type](class_ip.md#enum-ip-type) **TYPE_ANY** = `3`

Address type: Any.

---


<a id="constants"></a>

## Constants

<a id="class-ip-constant-resolver-max-queries"></a>

**RESOLVER_MAX_QUERIES** = `256` [🔗](class_ip.md#class-ip-constant-resolver-max-queries)

Maximum number of concurrent DNS resolver queries allowed, [RESOLVER_INVALID_ID](class_ip.md#class-ip-constant-resolver-invalid-id) is returned if exceeded.

<a id="class-ip-constant-resolver-invalid-id"></a>

**RESOLVER_INVALID_ID** = `-1` [🔗](class_ip.md#class-ip-constant-resolver-invalid-id)

Invalid ID constant. Returned if [RESOLVER_MAX_QUERIES](class_ip.md#class-ip-constant-resolver-max-queries) is exceeded.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-ip-method-clear-cache"></a>

void **clear_cache**(hostname: [String](class_string.md#class-string) = "") [🔗](class_ip.md#class-ip-method-clear-cache)

Removes all of a `hostname`'s cached references. If no `hostname` is given, all cached IP addresses are removed.

---


<a id="class-ip-method-erase-resolve-item"></a>

void **erase_resolve_item**(id: [int](class_int.md#class-int)) [🔗](class_ip.md#class-ip-method-erase-resolve-item)

Removes a given item `id` from the queue. This should be used to free a queue after it has completed to enable more queries to happen.

---


<a id="class-ip-method-get-local-addresses"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_local_addresses**() const [🔗](class_ip.md#class-ip-method-get-local-addresses)

Returns all the user's current IPv4 and IPv6 addresses as an array.

---


<a id="class-ip-method-get-local-interfaces"></a>

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **get_local_interfaces**() const [🔗](class_ip.md#class-ip-method-get-local-interfaces)

Returns all network adapters as an array.

Each adapter is a dictionary of the form:

```gdscript
{
    "index": "1", # Interface index.
    "name": "eth0", # Interface name.
    "friendly": "Ethernet One", # A friendly name (might be empty).
    "addresses": ["192.168.1.101"], # An array of IP addresses associated to this interface.
}
```

---


<a id="class-ip-method-get-resolve-item-address"></a>

[String](class_string.md#class-string) **get_resolve_item_address**(id: [int](class_int.md#class-int)) const [🔗](class_ip.md#class-ip-method-get-resolve-item-address)

Returns a queued hostname's IP address, given its queue `id`. Returns an empty string on error or if resolution hasn't happened yet (see [get_resolve_item_status()](class_ip.md#class-ip-method-get-resolve-item-status)).

---


<a id="class-ip-method-get-resolve-item-addresses"></a>

[Array](class_array.md#class-array) **get_resolve_item_addresses**(id: [int](class_int.md#class-int)) const [🔗](class_ip.md#class-ip-method-get-resolve-item-addresses)

Returns resolved addresses, or an empty array if an error happened or resolution didn't happen yet (see [get_resolve_item_status()](class_ip.md#class-ip-method-get-resolve-item-status)).

---


<a id="class-ip-method-get-resolve-item-status"></a>

[ResolverStatus](class_ip.md#enum-ip-resolverstatus) **get_resolve_item_status**(id: [int](class_int.md#class-int)) const [🔗](class_ip.md#class-ip-method-get-resolve-item-status)

Returns a queued hostname's status as a [ResolverStatus](class_ip.md#enum-ip-resolverstatus) constant, given its queue `id`.

---


<a id="class-ip-method-resolve-hostname"></a>

[String](class_string.md#class-string) **resolve_hostname**(host: [String](class_string.md#class-string), ip_type: [Type](class_ip.md#enum-ip-type) = 3) [🔗](class_ip.md#class-ip-method-resolve-hostname)

Returns a given hostname's IPv4 or IPv6 address when resolved (blocking-type method). The address type returned depends on the [Type](class_ip.md#enum-ip-type) constant given as `ip_type`.

---


<a id="class-ip-method-resolve-hostname-addresses"></a>

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **resolve_hostname_addresses**(host: [String](class_string.md#class-string), ip_type: [Type](class_ip.md#enum-ip-type) = 3) [🔗](class_ip.md#class-ip-method-resolve-hostname-addresses)

Resolves a given hostname in a blocking way. Addresses are returned as an [Array](class_array.md#class-array) of IPv4 or IPv6 addresses depending on `ip_type`.

---


<a id="class-ip-method-resolve-hostname-queue-item"></a>

[int](class_int.md#class-int) **resolve_hostname_queue_item**(host: [String](class_string.md#class-string), ip_type: [Type](class_ip.md#enum-ip-type) = 3) [🔗](class_ip.md#class-ip-method-resolve-hostname-queue-item)

Creates a queue item to resolve a hostname to an IPv4 or IPv6 address depending on the [Type](class_ip.md#enum-ip-type) constant given as `ip_type`. Returns the queue ID if successful, or [RESOLVER_INVALID_ID](class_ip.md#class-ip-constant-resolver-invalid-id) on error.
