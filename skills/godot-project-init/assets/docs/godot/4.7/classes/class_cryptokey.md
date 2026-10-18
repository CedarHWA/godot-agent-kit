> Source: https://docs.godotengine.org/en/4.7/classes/class_cryptokey.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="cryptokey"></a>

<a id="class-cryptokey"></a>

# CryptoKey

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A cryptographic key (RSA or elliptic-curve).

<a id="description"></a>

## Description

The CryptoKey class represents a cryptographic key. Keys can be loaded and saved like any other [Resource](class_resource.md#class-resource).

They can be used to generate a self-signed [X509Certificate](class_x509certificate.md#class-x509certificate) via [Crypto.generate_self_signed_certificate()](class_crypto.md#class-crypto-method-generate-self-signed-certificate) and as private key in [StreamPeerTLS.accept_stream()](class_streampeertls.md#class-streampeertls-method-accept-stream) along with the appropriate certificate.

<a id="tutorials"></a>

## Tutorials

- [SSL certificates](../tutorials/networking/ssl_certificates.md)

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [is_public_only](class_cryptokey.md#class-cryptokey-method-is-public-only)() const |
| [Error](class_@globalscope.md#enum-globalscope-error) | [load](class_cryptokey.md#class-cryptokey-method-load)(path: [String](class_string.md#class-string), public_only: [bool](class_bool.md#class-bool) = false) |
| [Error](class_@globalscope.md#enum-globalscope-error) | [load_from_string](class_cryptokey.md#class-cryptokey-method-load-from-string)(string_key: [String](class_string.md#class-string), public_only: [bool](class_bool.md#class-bool) = false) |
| [Error](class_@globalscope.md#enum-globalscope-error) | [save](class_cryptokey.md#class-cryptokey-method-save)(path: [String](class_string.md#class-string), public_only: [bool](class_bool.md#class-bool) = false) |
| [String](class_string.md#class-string) | [save_to_string](class_cryptokey.md#class-cryptokey-method-save-to-string)(public_only: [bool](class_bool.md#class-bool) = false) |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-cryptokey-method-is-public-only"></a>

[bool](class_bool.md#class-bool) **is_public_only**() const [🔗](class_cryptokey.md#class-cryptokey-method-is-public-only)

Returns `true` if this CryptoKey only has the public part, and not the private one.

---


<a id="class-cryptokey-method-load"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **load**(path: [String](class_string.md#class-string), public_only: [bool](class_bool.md#class-bool) = false) [🔗](class_cryptokey.md#class-cryptokey-method-load)

Loads a key from `path`. If `public_only` is `true`, only the public key will be loaded.

**Note:** `path` should be a "\*.pub" file if `public_only` is `true`, a "\*.key" file otherwise.

---


<a id="class-cryptokey-method-load-from-string"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **load_from_string**(string_key: [String](class_string.md#class-string), public_only: [bool](class_bool.md#class-bool) = false) [🔗](class_cryptokey.md#class-cryptokey-method-load-from-string)

Loads a key from the given `string_key`. If `public_only` is `true`, only the public key will be loaded.

---


<a id="class-cryptokey-method-save"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **save**(path: [String](class_string.md#class-string), public_only: [bool](class_bool.md#class-bool) = false) [🔗](class_cryptokey.md#class-cryptokey-method-save)

Saves a key to the given `path`. If `public_only` is `true`, only the public key will be saved.

**Note:** `path` should be a "\*.pub" file if `public_only` is `true`, a "\*.key" file otherwise.

---


<a id="class-cryptokey-method-save-to-string"></a>

[String](class_string.md#class-string) **save_to_string**(public_only: [bool](class_bool.md#class-bool) = false) [🔗](class_cryptokey.md#class-cryptokey-method-save-to-string)

Returns a string containing the key in PEM format. If `public_only` is `true`, only the public key will be included.
