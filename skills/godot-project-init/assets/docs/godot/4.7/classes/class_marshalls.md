> Source: https://docs.godotengine.org/en/4.7/classes/class_marshalls.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="marshalls"></a>

<a id="class-marshalls"></a>

# Marshalls

**Inherits:** [Object](class_object.md#class-object)

Data transformation (marshaling) and encoding helpers.

<a id="description"></a>

## Description

Provides data transformation and encoding utility functions.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray) | [base64_to_raw](class_marshalls.md#class-marshalls-method-base64-to-raw)(base64_str: [String](class_string.md#class-string)) |
| [String](class_string.md#class-string) | [base64_to_utf8](class_marshalls.md#class-marshalls-method-base64-to-utf8)(base64_str: [String](class_string.md#class-string)) |
| [Variant](class_variant.md#class-variant) | [base64_to_variant](class_marshalls.md#class-marshalls-method-base64-to-variant)(base64_str: [String](class_string.md#class-string), allow_objects: [bool](class_bool.md#class-bool) = false) |
| [String](class_string.md#class-string) | [raw_to_base64](class_marshalls.md#class-marshalls-method-raw-to-base64)(array: [PackedByteArray](class_packedbytearray.md#class-packedbytearray)) |
| [String](class_string.md#class-string) | [utf8_to_base64](class_marshalls.md#class-marshalls-method-utf8-to-base64)(utf8_str: [String](class_string.md#class-string)) |
| [String](class_string.md#class-string) | [variant_to_base64](class_marshalls.md#class-marshalls-method-variant-to-base64)(variant: [Variant](class_variant.md#class-variant), full_objects: [bool](class_bool.md#class-bool) = false) |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-marshalls-method-base64-to-raw"></a>

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **base64_to_raw**(base64_str: [String](class_string.md#class-string)) [🔗](class_marshalls.md#class-marshalls-method-base64-to-raw)

Returns a decoded [PackedByteArray](class_packedbytearray.md#class-packedbytearray) corresponding to the Base64-encoded string `base64_str`.

---


<a id="class-marshalls-method-base64-to-utf8"></a>

[String](class_string.md#class-string) **base64_to_utf8**(base64_str: [String](class_string.md#class-string)) [🔗](class_marshalls.md#class-marshalls-method-base64-to-utf8)

Returns a decoded string corresponding to the Base64-encoded string `base64_str`.

---


<a id="class-marshalls-method-base64-to-variant"></a>

[Variant](class_variant.md#class-variant) **base64_to_variant**(base64_str: [String](class_string.md#class-string), allow_objects: [bool](class_bool.md#class-bool) = false) [🔗](class_marshalls.md#class-marshalls-method-base64-to-variant)

Returns a decoded [Variant](class_variant.md#class-variant) corresponding to the Base64-encoded string `base64_str`. If `allow_objects` is `true`, decoding objects is allowed.

Internally, this uses the same decoding mechanism as the [@GlobalScope.bytes_to_var()](class_@globalscope.md#class-globalscope-method-bytes-to-var) method.

**Warning:** Deserialized objects can contain code which gets executed. Do not use this option if the serialized object comes from untrusted sources to avoid potential security threats such as remote code execution.

---


<a id="class-marshalls-method-raw-to-base64"></a>

[String](class_string.md#class-string) **raw_to_base64**(array: [PackedByteArray](class_packedbytearray.md#class-packedbytearray)) [🔗](class_marshalls.md#class-marshalls-method-raw-to-base64)

Returns a Base64-encoded string of a given [PackedByteArray](class_packedbytearray.md#class-packedbytearray).

---


<a id="class-marshalls-method-utf8-to-base64"></a>

[String](class_string.md#class-string) **utf8_to_base64**(utf8_str: [String](class_string.md#class-string)) [🔗](class_marshalls.md#class-marshalls-method-utf8-to-base64)

Returns a Base64-encoded string of the UTF-8 string `utf8_str`.

---


<a id="class-marshalls-method-variant-to-base64"></a>

[String](class_string.md#class-string) **variant_to_base64**(variant: [Variant](class_variant.md#class-variant), full_objects: [bool](class_bool.md#class-bool) = false) [🔗](class_marshalls.md#class-marshalls-method-variant-to-base64)

Returns a Base64-encoded string of the [Variant](class_variant.md#class-variant) `variant`. If `full_objects` is `true`, encoding objects is allowed (and can potentially include code).

Internally, this uses the same encoding mechanism as the [@GlobalScope.var_to_bytes()](class_@globalscope.md#class-globalscope-method-var-to-bytes) method.
