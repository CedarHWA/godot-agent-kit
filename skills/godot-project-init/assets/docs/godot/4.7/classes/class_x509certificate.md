> Source: https://docs.godotengine.org/en/4.7/classes/class_x509certificate.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="x509certificate"></a>

<a id="class-x509certificate"></a>

# X509Certificate

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

An X509 certificate (e.g. for TLS).

<a id="description"></a>

## Description

The X509Certificate class represents an X509 certificate. Certificates can be loaded and saved like any other [Resource](class_resource.md#class-resource).

They can be used as the server certificate in [StreamPeerTLS.accept_stream()](class_streampeertls.md#class-streampeertls-method-accept-stream) (along with the proper [CryptoKey](class_cryptokey.md#class-cryptokey)), and to specify the only certificate that should be accepted when connecting to a TLS server via [StreamPeerTLS.connect_to_stream()](class_streampeertls.md#class-streampeertls-method-connect-to-stream).

<a id="tutorials"></a>

## Tutorials

- [SSL certificates](../tutorials/networking/ssl_certificates.md)

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Error](class_@globalscope.md#enum-globalscope-error) | [load](class_x509certificate.md#class-x509certificate-method-load)(path: [String](class_string.md#class-string)) |
| [Error](class_@globalscope.md#enum-globalscope-error) | [load_from_string](class_x509certificate.md#class-x509certificate-method-load-from-string)(string: [String](class_string.md#class-string)) |
| [Error](class_@globalscope.md#enum-globalscope-error) | [save](class_x509certificate.md#class-x509certificate-method-save)(path: [String](class_string.md#class-string)) |
| [String](class_string.md#class-string) | [save_to_string](class_x509certificate.md#class-x509certificate-method-save-to-string)() |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-x509certificate-method-load"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **load**(path: [String](class_string.md#class-string)) [🔗](class_x509certificate.md#class-x509certificate-method-load)

Loads a certificate from `path` ("\*.crt" file).

---


<a id="class-x509certificate-method-load-from-string"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **load_from_string**(string: [String](class_string.md#class-string)) [🔗](class_x509certificate.md#class-x509certificate-method-load-from-string)

Loads a certificate from the given `string`.

---


<a id="class-x509certificate-method-save"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **save**(path: [String](class_string.md#class-string)) [🔗](class_x509certificate.md#class-x509certificate-method-save)

Saves a certificate to the given `path` (should be a "\*.crt" file).

---


<a id="class-x509certificate-method-save-to-string"></a>

[String](class_string.md#class-string) **save_to_string**() [🔗](class_x509certificate.md#class-x509certificate-method-save-to-string)

Returns a string representation of the certificate, or an empty string if the certificate is invalid.
