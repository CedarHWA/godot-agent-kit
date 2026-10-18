> Source: https://docs.godotengine.org/en/4.7/classes/class_zippacker.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="zippacker"></a>

<a id="class-zippacker"></a>

# ZIPPacker

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Allows the creation of ZIP files.

<a id="description"></a>

## Description

This class implements a writer that allows storing the multiple blobs in a ZIP archive. See also [ZIPReader](class_zipreader.md#class-zipreader) and [PCKPacker](class_pckpacker.md#class-pckpacker).

```gdscript
# Create a ZIP archive with a single file at its root.
func write_zip_file():
    var writer = ZIPPacker.new()
    var err = writer.open("user://archive.zip")
    if err != OK:
        return err
    writer.start_file("hello.txt")
    writer.write_file("Hello World".to_utf8_buffer())
    writer.close_file()

    writer.close()
    return OK
```

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [int](class_int.md#class-int) | [compression_level](class_zippacker.md#class-zippacker-property-compression-level) | `-1` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Error](class_@globalscope.md#enum-globalscope-error) | [add_directory](class_zippacker.md#class-zippacker-method-add-directory)(path: [String](class_string.md#class-string), permissions: BitField[[UnixPermissionFlags](class_fileaccess.md#enum-fileaccess-unixpermissionflags)] = 493, modified_time: [int](class_int.md#class-int) = 0) |
| [Error](class_@globalscope.md#enum-globalscope-error) | [close](class_zippacker.md#class-zippacker-method-close)() |
| [Error](class_@globalscope.md#enum-globalscope-error) | [close_file](class_zippacker.md#class-zippacker-method-close-file)() |
| [Error](class_@globalscope.md#enum-globalscope-error) | [open](class_zippacker.md#class-zippacker-method-open)(path: [String](class_string.md#class-string), append: [ZipAppend](class_zippacker.md#enum-zippacker-zipappend) = 0) |
| [Error](class_@globalscope.md#enum-globalscope-error) | [start_file](class_zippacker.md#class-zippacker-method-start-file)(path: [String](class_string.md#class-string), permissions: BitField[[UnixPermissionFlags](class_fileaccess.md#enum-fileaccess-unixpermissionflags)] = 420, modified_time: [int](class_int.md#class-int) = 0) |
| [Error](class_@globalscope.md#enum-globalscope-error) | [write_file](class_zippacker.md#class-zippacker-method-write-file)(data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray)) |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-zippacker-zipappend"></a>

enum **ZipAppend**: [🔗](class_zippacker.md#enum-zippacker-zipappend)

<a id="class-zippacker-constant-append-create"></a>

[ZipAppend](class_zippacker.md#enum-zippacker-zipappend) **APPEND_CREATE** = `0`

Create a new zip archive at the given path.

<a id="class-zippacker-constant-append-createafter"></a>

[ZipAppend](class_zippacker.md#enum-zippacker-zipappend) **APPEND_CREATEAFTER** = `1`

Append a new zip archive to the end of the already existing file at the given path.

<a id="class-zippacker-constant-append-addinzip"></a>

[ZipAppend](class_zippacker.md#enum-zippacker-zipappend) **APPEND_ADDINZIP** = `2`

Add new files to the existing zip archive at the given path.

---


<a id="enum-zippacker-compressionlevel"></a>

enum **CompressionLevel**: [🔗](class_zippacker.md#enum-zippacker-compressionlevel)

<a id="class-zippacker-constant-compression-default"></a>

[CompressionLevel](class_zippacker.md#enum-zippacker-compressionlevel) **COMPRESSION_DEFAULT** = `-1`

Start a file with the default Deflate compression level (`6`). This is a good compromise between speed and file size.

<a id="class-zippacker-constant-compression-none"></a>

[CompressionLevel](class_zippacker.md#enum-zippacker-compressionlevel) **COMPRESSION_NONE** = `0`

Start a file with no compression. This is also known as the "Store" compression mode and is the fastest method of packing files inside a ZIP archive. Consider using this mode for files that are already compressed (such as JPEG, PNG, MP3, or Ogg Vorbis files).

<a id="class-zippacker-constant-compression-fast"></a>

[CompressionLevel](class_zippacker.md#enum-zippacker-compressionlevel) **COMPRESSION_FAST** = `1`

Start a file with the fastest Deflate compression level (`1`). This is fast to compress, but results in larger file sizes than [COMPRESSION_DEFAULT](class_zippacker.md#class-zippacker-constant-compression-default). Decompression speed is generally unaffected by the chosen compression level.

<a id="class-zippacker-constant-compression-best"></a>

[CompressionLevel](class_zippacker.md#enum-zippacker-compressionlevel) **COMPRESSION_BEST** = `9`

Start a file with the best Deflate compression level (`9`). This is slow to compress, but results in smaller file sizes than [COMPRESSION_DEFAULT](class_zippacker.md#class-zippacker-constant-compression-default). Decompression speed is generally unaffected by the chosen compression level.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-zippacker-property-compression-level"></a>

[int](class_int.md#class-int) **compression_level** = `-1` [🔗](class_zippacker.md#class-zippacker-property-compression-level)

- void **set_compression_level**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_compression_level**()

The compression level used when [start_file()](class_zippacker.md#class-zippacker-method-start-file) is called. Use [CompressionLevel](class_zippacker.md#enum-zippacker-compressionlevel) as a reference.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-zippacker-method-add-directory"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **add_directory**(path: [String](class_string.md#class-string), permissions: BitField[[UnixPermissionFlags](class_fileaccess.md#enum-fileaccess-unixpermissionflags)] = 493, modified_time: [int](class_int.md#class-int) = 0) [🔗](class_zippacker.md#class-zippacker-method-add-directory)

Adds directory to the archive. If `modified_time` is set to `0`, current system time is used.

**Note:** Directories are automatically created when [start_file()](class_zippacker.md#class-zippacker-method-start-file) is called, use this function before adding files to create directories with custom permissions and modification time.

---


<a id="class-zippacker-method-close"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **close**() [🔗](class_zippacker.md#class-zippacker-method-close)

Closes the underlying resources used by this instance.

---


<a id="class-zippacker-method-close-file"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **close_file**() [🔗](class_zippacker.md#class-zippacker-method-close-file)

Stops writing to a file within the archive.

It will fail if there is no open file.

---


<a id="class-zippacker-method-open"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **open**(path: [String](class_string.md#class-string), append: [ZipAppend](class_zippacker.md#enum-zippacker-zipappend) = 0) [🔗](class_zippacker.md#class-zippacker-method-open)

Opens a zip file for writing at the given path using the specified write mode.

This must be called before everything else.

---


<a id="class-zippacker-method-start-file"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **start_file**(path: [String](class_string.md#class-string), permissions: BitField[[UnixPermissionFlags](class_fileaccess.md#enum-fileaccess-unixpermissionflags)] = 420, modified_time: [int](class_int.md#class-int) = 0) [🔗](class_zippacker.md#class-zippacker-method-start-file)

Starts writing to a file within the archive. Only one file can be written at the same time. If `modified_time` is set to `0`, current system time is used.

Must be called after [open()](class_zippacker.md#class-zippacker-method-open).

---


<a id="class-zippacker-method-write-file"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **write_file**(data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray)) [🔗](class_zippacker.md#class-zippacker-method-write-file)

Write the given `data` to the file.

Needs to be called after [start_file()](class_zippacker.md#class-zippacker-method-start-file).
