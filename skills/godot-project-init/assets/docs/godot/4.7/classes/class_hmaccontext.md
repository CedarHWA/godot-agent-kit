> Source: https://docs.godotengine.org/en/4.7/classes/class_hmaccontext.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="hmaccontext"></a>

<a id="class-hmaccontext"></a>

# HMACContext

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Used to create an HMAC for a message using a key.

<a id="description"></a>

## Description

The HMACContext class is useful for advanced HMAC use cases, such as streaming the message as it supports creating the message over time rather than providing it all at once.

```gdscript
extends Node
var ctx = HMACContext.new()

func _ready():
    var key = "supersecret".to_utf8_buffer()
    var err = ctx.start(HashingContext.HASH_SHA256, key)
    assert(err == OK)
    var msg1 = "this is ".to_utf8_buffer()
    var msg2 = "super duper secret".to_utf8_buffer()
    err = ctx.update(msg1)
    assert(err == OK)
    err = ctx.update(msg2)
    assert(err == OK)
    var hmac = ctx.finish()
    print(hmac.hex_encode())
```

```csharp
using Godot;
using System.Diagnostics;

public partial class MyNode : Node
{
    private HmacContext _ctx = new HmacContext();

    public override void _Ready()
    {
        byte[] key = "supersecret".ToUtf8Buffer();
        Error err = _ctx.Start(HashingContext.HashType.Sha256, key);
        Debug.Assert(err == Error.Ok);
        byte[] msg1 = "this is ".ToUtf8Buffer();
        byte[] msg2 = "super duper secret".ToUtf8Buffer();
        err = _ctx.Update(msg1);
        Debug.Assert(err == Error.Ok);
        err = _ctx.Update(msg2);
        Debug.Assert(err == Error.Ok);
        byte[] hmac = _ctx.Finish();
        GD.Print(hmac.HexEncode());
    }
}
```

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray) | [finish](class_hmaccontext.md#class-hmaccontext-method-finish)() |
| [Error](class_@globalscope.md#enum-globalscope-error) | [start](class_hmaccontext.md#class-hmaccontext-method-start)(hash_type: [HashType](class_hashingcontext.md#enum-hashingcontext-hashtype), key: [PackedByteArray](class_packedbytearray.md#class-packedbytearray)) |
| [Error](class_@globalscope.md#enum-globalscope-error) | [update](class_hmaccontext.md#class-hmaccontext-method-update)(data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray)) |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-hmaccontext-method-finish"></a>

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **finish**() [🔗](class_hmaccontext.md#class-hmaccontext-method-finish)

Returns the resulting HMAC. If the HMAC failed, an empty [PackedByteArray](class_packedbytearray.md#class-packedbytearray) is returned.

---


<a id="class-hmaccontext-method-start"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **start**(hash_type: [HashType](class_hashingcontext.md#enum-hashingcontext-hashtype), key: [PackedByteArray](class_packedbytearray.md#class-packedbytearray)) [🔗](class_hmaccontext.md#class-hmaccontext-method-start)

Initializes the HMACContext. This method cannot be called again on the same HMACContext until [finish()](class_hmaccontext.md#class-hmaccontext-method-finish) has been called.

---


<a id="class-hmaccontext-method-update"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **update**(data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray)) [🔗](class_hmaccontext.md#class-hmaccontext-method-update)

Updates the message to be HMACed. This can be called multiple times before [finish()](class_hmaccontext.md#class-hmaccontext-method-finish) is called to append `data` to the message, but cannot be called until [start()](class_hmaccontext.md#class-hmaccontext-method-start) has been called.
