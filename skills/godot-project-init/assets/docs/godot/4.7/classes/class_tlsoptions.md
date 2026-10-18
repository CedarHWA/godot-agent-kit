> Source: https://docs.godotengine.org/en/4.7/classes/class_tlsoptions.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="tlsoptions"></a>

<a id="class-tlsoptions"></a>

# TLSOptions

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

TLS configuration for clients and servers.

<a id="description"></a>

## Description

TLSOptions abstracts the configuration options for the [StreamPeerTLS](class_streampeertls.md#class-streampeertls) and [PacketPeerDTLS](class_packetpeerdtls.md#class-packetpeerdtls) classes.

Objects of this class cannot be instantiated directly, and one of the static methods [client()](class_tlsoptions.md#class-tlsoptions-method-client), [client_unsafe()](class_tlsoptions.md#class-tlsoptions-method-client-unsafe), or [server()](class_tlsoptions.md#class-tlsoptions-method-server) should be used instead.

```gdscript
# Create a TLS client configuration which uses our custom trusted CA chain.
var client_trusted_cas = load("res://my_trusted_cas.crt")
var client_tls_options = TLSOptions.client(client_trusted_cas)

# Create a TLS server configuration.
var server_certs = load("res://my_server_cas.crt")
var server_key = load("res://my_server_key.key")
var server_tls_options = TLSOptions.server(server_key, server_certs)
```

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [TLSOptions](class_tlsoptions.md#class-tlsoptions) | [client](class_tlsoptions.md#class-tlsoptions-method-client)(trusted_chain: [X509Certificate](class_x509certificate.md#class-x509certificate) = null, common_name_override: [String](class_string.md#class-string) = "") static |
| [TLSOptions](class_tlsoptions.md#class-tlsoptions) | [client_unsafe](class_tlsoptions.md#class-tlsoptions-method-client-unsafe)(trusted_chain: [X509Certificate](class_x509certificate.md#class-x509certificate) = null) static |
| [String](class_string.md#class-string) | [get_common_name_override](class_tlsoptions.md#class-tlsoptions-method-get-common-name-override)() const |
| [X509Certificate](class_x509certificate.md#class-x509certificate) | [get_own_certificate](class_tlsoptions.md#class-tlsoptions-method-get-own-certificate)() const |
| [CryptoKey](class_cryptokey.md#class-cryptokey) | [get_private_key](class_tlsoptions.md#class-tlsoptions-method-get-private-key)() const |
| [X509Certificate](class_x509certificate.md#class-x509certificate) | [get_trusted_ca_chain](class_tlsoptions.md#class-tlsoptions-method-get-trusted-ca-chain)() const |
| [bool](class_bool.md#class-bool) | [is_server](class_tlsoptions.md#class-tlsoptions-method-is-server)() const |
| [bool](class_bool.md#class-bool) | [is_unsafe_client](class_tlsoptions.md#class-tlsoptions-method-is-unsafe-client)() const |
| [TLSOptions](class_tlsoptions.md#class-tlsoptions) | [server](class_tlsoptions.md#class-tlsoptions-method-server)(key: [CryptoKey](class_cryptokey.md#class-cryptokey), certificate: [X509Certificate](class_x509certificate.md#class-x509certificate)) static |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-tlsoptions-method-client"></a>

[TLSOptions](class_tlsoptions.md#class-tlsoptions) **client**(trusted_chain: [X509Certificate](class_x509certificate.md#class-x509certificate) = null, common_name_override: [String](class_string.md#class-string) = "") static [🔗](class_tlsoptions.md#class-tlsoptions-method-client)

Creates a TLS client configuration which validates certificates and their common names (fully qualified domain names).

You can specify a custom `trusted_chain` of certification authorities (the default CA list will be used if `null`), and optionally provide a `common_name_override` if you expect the certificate to have a common name other than the server FQDN.

**Note:** On the Web platform, TLS verification is always enforced against the CA list of the web browser. This is considered a security feature.

---


<a id="class-tlsoptions-method-client-unsafe"></a>

[TLSOptions](class_tlsoptions.md#class-tlsoptions) **client_unsafe**(trusted_chain: [X509Certificate](class_x509certificate.md#class-x509certificate) = null) static [🔗](class_tlsoptions.md#class-tlsoptions-method-client-unsafe)

Creates an **unsafe** TLS client configuration where certificate validation is optional. You can optionally provide a valid `trusted_chain`, but the common name of the certificates will never be checked. Using this configuration for purposes other than testing **is not recommended**.

**Note:** On the Web platform, TLS verification is always enforced against the CA list of the web browser. This is considered a security feature.

---


<a id="class-tlsoptions-method-get-common-name-override"></a>

[String](class_string.md#class-string) **get_common_name_override**() const [🔗](class_tlsoptions.md#class-tlsoptions-method-get-common-name-override)

Returns the common name (domain name) override specified when creating with [client()](class_tlsoptions.md#class-tlsoptions-method-client).

---


<a id="class-tlsoptions-method-get-own-certificate"></a>

[X509Certificate](class_x509certificate.md#class-x509certificate) **get_own_certificate**() const [🔗](class_tlsoptions.md#class-tlsoptions-method-get-own-certificate)

Returns the [X509Certificate](class_x509certificate.md#class-x509certificate) specified when creating with [server()](class_tlsoptions.md#class-tlsoptions-method-server).

---


<a id="class-tlsoptions-method-get-private-key"></a>

[CryptoKey](class_cryptokey.md#class-cryptokey) **get_private_key**() const [🔗](class_tlsoptions.md#class-tlsoptions-method-get-private-key)

Returns the [CryptoKey](class_cryptokey.md#class-cryptokey) specified when creating with [server()](class_tlsoptions.md#class-tlsoptions-method-server).

---


<a id="class-tlsoptions-method-get-trusted-ca-chain"></a>

[X509Certificate](class_x509certificate.md#class-x509certificate) **get_trusted_ca_chain**() const [🔗](class_tlsoptions.md#class-tlsoptions-method-get-trusted-ca-chain)

Returns the CA [X509Certificate](class_x509certificate.md#class-x509certificate) chain specified when creating with [client()](class_tlsoptions.md#class-tlsoptions-method-client) or [client_unsafe()](class_tlsoptions.md#class-tlsoptions-method-client-unsafe).

---


<a id="class-tlsoptions-method-is-server"></a>

[bool](class_bool.md#class-bool) **is_server**() const [🔗](class_tlsoptions.md#class-tlsoptions-method-is-server)

Returns `true` if created with [server()](class_tlsoptions.md#class-tlsoptions-method-server), `false` otherwise.

---


<a id="class-tlsoptions-method-is-unsafe-client"></a>

[bool](class_bool.md#class-bool) **is_unsafe_client**() const [🔗](class_tlsoptions.md#class-tlsoptions-method-is-unsafe-client)

Returns `true` if created with [client_unsafe()](class_tlsoptions.md#class-tlsoptions-method-client-unsafe), `false` otherwise.

---


<a id="class-tlsoptions-method-server"></a>

[TLSOptions](class_tlsoptions.md#class-tlsoptions) **server**(key: [CryptoKey](class_cryptokey.md#class-cryptokey), certificate: [X509Certificate](class_x509certificate.md#class-x509certificate)) static [🔗](class_tlsoptions.md#class-tlsoptions-method-server)

Creates a TLS server configuration using the provided `key` and `certificate`.

**Note:** The `certificate` should include the full certificate chain up to the signing CA (certificates file can be concatenated using a general purpose text editor).
