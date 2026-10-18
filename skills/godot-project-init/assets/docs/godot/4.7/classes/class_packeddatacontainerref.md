> Source: https://docs.godotengine.org/en/4.7/classes/class_packeddatacontainerref.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="packeddatacontainerref"></a>

<a id="class-packeddatacontainerref"></a>

# PackedDataContainerRef

**Deprecated:** Use [@GlobalScope.var_to_bytes()](class_@globalscope.md#class-globalscope-method-var-to-bytes) or [FileAccess.store_var()](class_fileaccess.md#class-fileaccess-method-store-var) instead. To enable data compression, use [PackedByteArray.compress()](class_packedbytearray.md#class-packedbytearray-method-compress) or [FileAccess.open_compressed()](class_fileaccess.md#class-fileaccess-method-open-compressed).

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

An internal class used by [PackedDataContainer](class_packeddatacontainer.md#class-packeddatacontainer) to pack nested arrays and dictionaries.

<a id="description"></a>

## Description

When packing nested containers using [PackedDataContainer](class_packeddatacontainer.md#class-packeddatacontainer), they are recursively packed into **PackedDataContainerRef** (only applies to [Array](class_array.md#class-array) and [Dictionary](class_dictionary.md#class-dictionary)). Their data can be retrieved the same way as from [PackedDataContainer](class_packeddatacontainer.md#class-packeddatacontainer).

```gdscript
var packed = PackedDataContainer.new()
packed.pack([1, 2, 3, ["nested1", "nested2"], 4, 5, 6])

for element in packed:
    if element is PackedDataContainerRef:
        for subelement in element:
            print("::", subelement)
    else:
        print(element)
```

Prints:

```text
1
2
3
::nested1
::nested2
4
5
6
```

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [int](class_int.md#class-int) | [size](class_packeddatacontainerref.md#class-packeddatacontainerref-method-size)() const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-packeddatacontainerref-method-size"></a>

[int](class_int.md#class-int) **size**() const [🔗](class_packeddatacontainerref.md#class-packeddatacontainerref-method-size)

Returns the size of the packed container (see [Array.size()](class_array.md#class-array-method-size) and [Dictionary.size()](class_dictionary.md#class-dictionary-method-size)).
