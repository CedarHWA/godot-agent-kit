> Source: https://docs.godotengine.org/en/4.7/classes/class_aescontext.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="aescontext"></a>

<a id="class-aescontext"></a>

# AESContext

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Provides access to AES encryption/decryption of raw data.

<a id="description"></a>

## Description

This class holds the context information required for encryption and decryption operations with AES (Advanced Encryption Standard). Both AES-ECB and AES-CBC modes are supported.

```gdscript
extends Node

var aes = AESContext.new()

func _ready():
    var key = "My secret key!!!" # Key must be either 16 or 32 bytes.
    var data = "My secret text!!" # Data size must be multiple of 16 bytes, apply padding if needed.
    # Encrypt ECB
    aes.start(AESContext.MODE_ECB_ENCRYPT, key.to_utf8_buffer())
    var encrypted = aes.update(data.to_utf8_buffer())
    aes.finish()
    # Decrypt ECB
    aes.start(AESContext.MODE_ECB_DECRYPT, key.to_utf8_buffer())
    var decrypted = aes.update(encrypted)
    aes.finish()
    # Check ECB
    assert(decrypted == data.to_utf8_buffer())

    var iv = "My secret iv!!!!" # IV must be of exactly 16 bytes.
    # Encrypt CBC
    aes.start(AESContext.MODE_CBC_ENCRYPT, key.to_utf8_buffer(), iv.to_utf8_buffer())
    encrypted = aes.update(data.to_utf8_buffer())
    aes.finish()
    # Decrypt CBC
    aes.start(AESContext.MODE_CBC_DECRYPT, key.to_utf8_buffer(), iv.to_utf8_buffer())
    decrypted = aes.update(encrypted)
    aes.finish()
    # Check CBC
    assert(decrypted == data.to_utf8_buffer())
```

```csharp
using Godot;
using System.Diagnostics;

public partial class MyNode : Node
{
    private AesContext _aes = new AesContext();

    public override void _Ready()
    {
        string key = "My secret key!!!"; // Key must be either 16 or 32 bytes.
        string data = "My secret text!!"; // Data size must be multiple of 16 bytes, apply padding if needed.
        // Encrypt ECB
        _aes.Start(AesContext.Mode.EcbEncrypt, key.ToUtf8Buffer());
        byte[] encrypted = _aes.Update(data.ToUtf8Buffer());
        _aes.Finish();
        // Decrypt ECB
        _aes.Start(AesContext.Mode.EcbDecrypt, key.ToUtf8Buffer());
        byte[] decrypted = _aes.Update(encrypted);
        _aes.Finish();
        // Check ECB
        Debug.Assert(decrypted == data.ToUtf8Buffer());

        string iv = "My secret iv!!!!"; // IV must be of exactly 16 bytes.
        // Encrypt CBC
        _aes.Start(AesContext.Mode.EcbEncrypt, key.ToUtf8Buffer(), iv.ToUtf8Buffer());
        encrypted = _aes.Update(data.ToUtf8Buffer());
        _aes.Finish();
        // Decrypt CBC
        _aes.Start(AesContext.Mode.EcbDecrypt, key.ToUtf8Buffer(), iv.ToUtf8Buffer());
        decrypted = _aes.Update(encrypted);
        _aes.Finish();
        // Check CBC
        Debug.Assert(decrypted == data.ToUtf8Buffer());
    }
}
```

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [finish](class_aescontext.md#class-aescontext-method-finish)() |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray) | [get_iv_state](class_aescontext.md#class-aescontext-method-get-iv-state)() |
| [Error](class_@globalscope.md#enum-globalscope-error) | [start](class_aescontext.md#class-aescontext-method-start)(mode: [Mode](class_aescontext.md#enum-aescontext-mode), key: [PackedByteArray](class_packedbytearray.md#class-packedbytearray), iv: [PackedByteArray](class_packedbytearray.md#class-packedbytearray) = PackedByteArray()) |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray) | [update](class_aescontext.md#class-aescontext-method-update)(src: [PackedByteArray](class_packedbytearray.md#class-packedbytearray)) |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-aescontext-mode"></a>

enum **Mode**: [🔗](class_aescontext.md#enum-aescontext-mode)

<a id="class-aescontext-constant-mode-ecb-encrypt"></a>

[Mode](class_aescontext.md#enum-aescontext-mode) **MODE_ECB_ENCRYPT** = `0`

AES electronic codebook encryption mode.

<a id="class-aescontext-constant-mode-ecb-decrypt"></a>

[Mode](class_aescontext.md#enum-aescontext-mode) **MODE_ECB_DECRYPT** = `1`

AES electronic codebook decryption mode.

<a id="class-aescontext-constant-mode-cbc-encrypt"></a>

[Mode](class_aescontext.md#enum-aescontext-mode) **MODE_CBC_ENCRYPT** = `2`

AES cipher block chaining encryption mode.

<a id="class-aescontext-constant-mode-cbc-decrypt"></a>

[Mode](class_aescontext.md#enum-aescontext-mode) **MODE_CBC_DECRYPT** = `3`

AES cipher block chaining decryption mode.

<a id="class-aescontext-constant-mode-max"></a>

[Mode](class_aescontext.md#enum-aescontext-mode) **MODE_MAX** = `4`

Maximum value for the mode enum.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-aescontext-method-finish"></a>

void **finish**() [🔗](class_aescontext.md#class-aescontext-method-finish)

Close this AES context so it can be started again. See [start()](class_aescontext.md#class-aescontext-method-start).

---


<a id="class-aescontext-method-get-iv-state"></a>

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **get_iv_state**() [🔗](class_aescontext.md#class-aescontext-method-get-iv-state)

Get the current IV state for this context (IV gets updated when calling [update()](class_aescontext.md#class-aescontext-method-update)). You normally don't need this function.

**Note:** This function only makes sense when the context is started with [MODE_CBC_ENCRYPT](class_aescontext.md#class-aescontext-constant-mode-cbc-encrypt) or [MODE_CBC_DECRYPT](class_aescontext.md#class-aescontext-constant-mode-cbc-decrypt).

---


<a id="class-aescontext-method-start"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **start**(mode: [Mode](class_aescontext.md#enum-aescontext-mode), key: [PackedByteArray](class_packedbytearray.md#class-packedbytearray), iv: [PackedByteArray](class_packedbytearray.md#class-packedbytearray) = PackedByteArray()) [🔗](class_aescontext.md#class-aescontext-method-start)

Start the AES context in the given `mode`. A `key` of either 16 or 32 bytes must always be provided, while an `iv` (initialization vector) of exactly 16 bytes, is only needed when `mode` is either [MODE_CBC_ENCRYPT](class_aescontext.md#class-aescontext-constant-mode-cbc-encrypt) or [MODE_CBC_DECRYPT](class_aescontext.md#class-aescontext-constant-mode-cbc-decrypt).

---


<a id="class-aescontext-method-update"></a>

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **update**(src: [PackedByteArray](class_packedbytearray.md#class-packedbytearray)) [🔗](class_aescontext.md#class-aescontext-method-update)

Run the desired operation for this AES context. Will return a [PackedByteArray](class_packedbytearray.md#class-packedbytearray) containing the result of encrypting (or decrypting) the given `src`. See [start()](class_aescontext.md#class-aescontext-method-start) for mode of operation.

**Note:** The size of `src` must be a multiple of 16. Apply some padding if needed.
