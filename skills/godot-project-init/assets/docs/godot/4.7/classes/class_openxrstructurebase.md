> Source: https://docs.godotengine.org/en/4.7/classes/class_openxrstructurebase.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxrstructurebase"></a>

<a id="class-openxrstructurebase"></a>

# OpenXRStructureBase

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [OpenXRSpatialContextPersistenceConfig](class_openxrspatialcontextpersistenceconfig.md#class-openxrspatialcontextpersistenceconfig)

Object for storing OpenXR structure data.

<a id="description"></a>

## Description

Object for storing OpenXR structure data that is passed when calling into OpenXR APIs.

<a id="properties"></a>

## Properties

|  |  |
| --- | --- |
| [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) | [next](class_openxrstructurebase.md#class-openxrstructurebase-property-next) |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [int](class_int.md#class-int) | [_get_header](class_openxrstructurebase.md#class-openxrstructurebase-private-method-get-header)(next: [int](class_int.md#class-int)) virtual |
| [int](class_int.md#class-int) | [get_structure_type](class_openxrstructurebase.md#class-openxrstructurebase-method-get-structure-type)() |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-openxrstructurebase-property-next"></a>

[OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) **next** [🔗](class_openxrstructurebase.md#class-openxrstructurebase-property-next)

- void **set_next**(value: [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase))
- [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) **get_next**()

Setting another structure object here chains these structures together to extend the API functionality. Consult the OpenXR documentation for which structures can be used with a given API call.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-openxrstructurebase-private-method-get-header"></a>

[int](class_int.md#class-int) **_get_header**(next: [int](class_int.md#class-int)) virtual [🔗](class_openxrstructurebase.md#class-openxrstructurebase-private-method-get-header)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---


<a id="class-openxrstructurebase-method-get-structure-type"></a>

[int](class_int.md#class-int) **get_structure_type**() [🔗](class_openxrstructurebase.md#class-openxrstructurebase-method-get-structure-type)

Returns the structure type (OpenXR `XrStructureType`) used for this structure.
