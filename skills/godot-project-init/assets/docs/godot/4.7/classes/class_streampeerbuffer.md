> Source: https://docs.godotengine.org/en/4.7/classes/class_streampeerbuffer.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="streampeerbuffer"></a>

<a id="class-streampeerbuffer"></a>

# StreamPeerBuffer

**Inherits:** [StreamPeer](class_streampeer.md#class-streampeer) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A stream peer used to handle binary data streams.

<a id="description"></a>

## Description

A data buffer stream peer that uses a byte array as the stream. This object can be used to handle binary data from network sessions. To handle binary data stored in files, [FileAccess](class_fileaccess.md#class-fileaccess) can be used directly.

A **StreamPeerBuffer** object keeps an internal cursor which is the offset in bytes to the start of the buffer. Get and put operations are performed at the cursor position and will move the cursor accordingly.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray) | [data_array](class_streampeerbuffer.md#class-streampeerbuffer-property-data-array) | `PackedByteArray()` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [clear](class_streampeerbuffer.md#class-streampeerbuffer-method-clear)() |
| [StreamPeerBuffer](class_streampeerbuffer.md#class-streampeerbuffer) | [duplicate](class_streampeerbuffer.md#class-streampeerbuffer-method-duplicate)() const |
| [int](class_int.md#class-int) | [get_position](class_streampeerbuffer.md#class-streampeerbuffer-method-get-position)() const |
| [int](class_int.md#class-int) | [get_size](class_streampeerbuffer.md#class-streampeerbuffer-method-get-size)() const |
| void | [resize](class_streampeerbuffer.md#class-streampeerbuffer-method-resize)(size: [int](class_int.md#class-int)) |
| void | [seek](class_streampeerbuffer.md#class-streampeerbuffer-method-seek)(position: [int](class_int.md#class-int)) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-streampeerbuffer-property-data-array"></a>

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **data_array** = `PackedByteArray()` [🔗](class_streampeerbuffer.md#class-streampeerbuffer-property-data-array)

- void **set_data_array**(value: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))
- [PackedByteArray](class_packedbytearray.md#class-packedbytearray) **get_data_array**()

The underlying data buffer. Setting this value resets the cursor.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray](class_packedbytearray.md#class-packedbytearray) for more details.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-streampeerbuffer-method-clear"></a>

void **clear**() [🔗](class_streampeerbuffer.md#class-streampeerbuffer-method-clear)

Clears the [data_array](class_streampeerbuffer.md#class-streampeerbuffer-property-data-array) and resets the cursor.

---


<a id="class-streampeerbuffer-method-duplicate"></a>

[StreamPeerBuffer](class_streampeerbuffer.md#class-streampeerbuffer) **duplicate**() const [🔗](class_streampeerbuffer.md#class-streampeerbuffer-method-duplicate)

Returns a new **StreamPeerBuffer** with the same [data_array](class_streampeerbuffer.md#class-streampeerbuffer-property-data-array) content.

---


<a id="class-streampeerbuffer-method-get-position"></a>

[int](class_int.md#class-int) **get_position**() const [🔗](class_streampeerbuffer.md#class-streampeerbuffer-method-get-position)

Returns the current cursor position.

---


<a id="class-streampeerbuffer-method-get-size"></a>

[int](class_int.md#class-int) **get_size**() const [🔗](class_streampeerbuffer.md#class-streampeerbuffer-method-get-size)

Returns the size of [data_array](class_streampeerbuffer.md#class-streampeerbuffer-property-data-array).

---


<a id="class-streampeerbuffer-method-resize"></a>

void **resize**(size: [int](class_int.md#class-int)) [🔗](class_streampeerbuffer.md#class-streampeerbuffer-method-resize)

Resizes the [data_array](class_streampeerbuffer.md#class-streampeerbuffer-property-data-array). This *doesn't* update the cursor.

---


<a id="class-streampeerbuffer-method-seek"></a>

void **seek**(position: [int](class_int.md#class-int)) [🔗](class_streampeerbuffer.md#class-streampeerbuffer-method-seek)

Moves the cursor to the specified position. `position` must be a valid index of [data_array](class_streampeerbuffer.md#class-streampeerbuffer-property-data-array).
