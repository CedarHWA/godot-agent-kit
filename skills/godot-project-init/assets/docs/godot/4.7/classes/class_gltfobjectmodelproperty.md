> Source: https://docs.godotengine.org/en/4.7/classes/class_gltfobjectmodelproperty.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="gltfobjectmodelproperty"></a>

<a id="class-gltfobjectmodelproperty"></a>

# GLTFObjectModelProperty

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Describes how to access a property as defined in the glTF object model.

<a id="description"></a>

## Description

GLTFObjectModelProperty defines a mapping between a property in the glTF object model and a NodePath in the Godot scene tree. This can be used to animate properties in a glTF file using the `KHR_animation_pointer` extension, or to access them through an engine-agnostic script such as a behavior graph as defined by the `KHR_interactivity` extension.

The glTF property is identified by JSON pointer(s) stored in [json_pointers](class_gltfobjectmodelproperty.md#class-gltfobjectmodelproperty-property-json-pointers), while the Godot property it maps to is defined by [node_paths](class_gltfobjectmodelproperty.md#class-gltfobjectmodelproperty-property-node-paths). In most cases [json_pointers](class_gltfobjectmodelproperty.md#class-gltfobjectmodelproperty-property-json-pointers) and [node_paths](class_gltfobjectmodelproperty.md#class-gltfobjectmodelproperty-property-node-paths) will each only have one item, but in some cases a single glTF JSON pointer will map to multiple Godot properties, or a single Godot property will be mapped to multiple glTF JSON pointers, or it might be a many-to-many relationship.

[Expression](class_expression.md#class-expression) objects can be used to define conversions between the data, such as when glTF defines an angle in radians and Godot uses degrees. The [object_model_type](class_gltfobjectmodelproperty.md#class-gltfobjectmodelproperty-property-object-model-type) property defines the type of data stored in the glTF file as defined by the object model, see [GLTFObjectModelType](class_gltfobjectmodelproperty.md#enum-gltfobjectmodelproperty-gltfobjectmodeltype) for possible values.

<a id="tutorials"></a>

## Tutorials

- [GLTF Object Model](https://github.com/KhronosGroup/glTF/blob/main/specification/2.0/ObjectModel.adoc)
- [KHR_animation_pointer GLTF extension](https://github.com/KhronosGroup/glTF/tree/main/extensions/2.0/Khronos/KHR_animation_pointer)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Expression](class_expression.md#class-expression) | [gltf_to_godot_expression](class_gltfobjectmodelproperty.md#class-gltfobjectmodelproperty-property-gltf-to-godot-expression) |  |
| [Expression](class_expression.md#class-expression) | [godot_to_gltf_expression](class_gltfobjectmodelproperty.md#class-gltfobjectmodelproperty-property-godot-to-gltf-expression) |  |
| [Array](class_array.md#class-array)[[PackedStringArray](class_packedstringarray.md#class-packedstringarray)] | [json_pointers](class_gltfobjectmodelproperty.md#class-gltfobjectmodelproperty-property-json-pointers) | `[]` |
| [Array](class_array.md#class-array)[[NodePath](class_nodepath.md#class-nodepath)] | [node_paths](class_gltfobjectmodelproperty.md#class-gltfobjectmodelproperty-property-node-paths) | `[]` |
| [GLTFObjectModelType](class_gltfobjectmodelproperty.md#enum-gltfobjectmodelproperty-gltfobjectmodeltype) | [object_model_type](class_gltfobjectmodelproperty.md#class-gltfobjectmodelproperty-property-object-model-type) | `0` |
| [Variant.Type](class_@globalscope.md#enum-globalscope-variant-type) | [variant_type](class_gltfobjectmodelproperty.md#class-gltfobjectmodelproperty-property-variant-type) | `0` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [append_node_path](class_gltfobjectmodelproperty.md#class-gltfobjectmodelproperty-method-append-node-path)(node_path: [NodePath](class_nodepath.md#class-nodepath)) |
| void | [append_path_to_property](class_gltfobjectmodelproperty.md#class-gltfobjectmodelproperty-method-append-path-to-property)(node_path: [NodePath](class_nodepath.md#class-nodepath), prop_name: [StringName](class_stringname.md#class-stringname)) |
| [GLTFAccessorType](class_gltfaccessor.md#enum-gltfaccessor-gltfaccessortype) | [get_accessor_type](class_gltfobjectmodelproperty.md#class-gltfobjectmodelproperty-method-get-accessor-type)() const |
| [bool](class_bool.md#class-bool) | [has_json_pointers](class_gltfobjectmodelproperty.md#class-gltfobjectmodelproperty-method-has-json-pointers)() const |
| [bool](class_bool.md#class-bool) | [has_node_paths](class_gltfobjectmodelproperty.md#class-gltfobjectmodelproperty-method-has-node-paths)() const |
| void | [set_types](class_gltfobjectmodelproperty.md#class-gltfobjectmodelproperty-method-set-types)(variant_type: [Variant.Type](class_@globalscope.md#enum-globalscope-variant-type), obj_model_type: [GLTFObjectModelType](class_gltfobjectmodelproperty.md#enum-gltfobjectmodelproperty-gltfobjectmodeltype)) |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-gltfobjectmodelproperty-gltfobjectmodeltype"></a>

enum **GLTFObjectModelType**: [🔗](class_gltfobjectmodelproperty.md#enum-gltfobjectmodelproperty-gltfobjectmodeltype)

<a id="class-gltfobjectmodelproperty-constant-gltf-object-model-type-unknown"></a>

[GLTFObjectModelType](class_gltfobjectmodelproperty.md#enum-gltfobjectmodelproperty-gltfobjectmodeltype) **GLTF_OBJECT_MODEL_TYPE_UNKNOWN** = `0`

Unknown or not set object model type. If the object model type is set to this value, the real type still needs to be determined.

<a id="class-gltfobjectmodelproperty-constant-gltf-object-model-type-bool"></a>

[GLTFObjectModelType](class_gltfobjectmodelproperty.md#enum-gltfobjectmodelproperty-gltfobjectmodeltype) **GLTF_OBJECT_MODEL_TYPE_BOOL** = `1`

Object model type "bool". Represented in the glTF JSON as a boolean, and encoded in a [GLTFAccessor](class_gltfaccessor.md#class-gltfaccessor) as "SCALAR". When encoded in an accessor, a value of `0` is `false`, and any other value is `true`.

<a id="class-gltfobjectmodelproperty-constant-gltf-object-model-type-float"></a>

[GLTFObjectModelType](class_gltfobjectmodelproperty.md#enum-gltfobjectmodelproperty-gltfobjectmodeltype) **GLTF_OBJECT_MODEL_TYPE_FLOAT** = `2`

Object model type "float". Represented in the glTF JSON as a number, and encoded in a [GLTFAccessor](class_gltfaccessor.md#class-gltfaccessor) as "SCALAR".

<a id="class-gltfobjectmodelproperty-constant-gltf-object-model-type-float-array"></a>

[GLTFObjectModelType](class_gltfobjectmodelproperty.md#enum-gltfobjectmodelproperty-gltfobjectmodeltype) **GLTF_OBJECT_MODEL_TYPE_FLOAT_ARRAY** = `3`

Object model type "float[]". Represented in the glTF JSON as an array of numbers, and encoded in a [GLTFAccessor](class_gltfaccessor.md#class-gltfaccessor) as "SCALAR".

<a id="class-gltfobjectmodelproperty-constant-gltf-object-model-type-float2"></a>

[GLTFObjectModelType](class_gltfobjectmodelproperty.md#enum-gltfobjectmodelproperty-gltfobjectmodeltype) **GLTF_OBJECT_MODEL_TYPE_FLOAT2** = `4`

Object model type "float2". Represented in the glTF JSON as an array of two numbers, and encoded in a [GLTFAccessor](class_gltfaccessor.md#class-gltfaccessor) as "VEC2".

<a id="class-gltfobjectmodelproperty-constant-gltf-object-model-type-float3"></a>

[GLTFObjectModelType](class_gltfobjectmodelproperty.md#enum-gltfobjectmodelproperty-gltfobjectmodeltype) **GLTF_OBJECT_MODEL_TYPE_FLOAT3** = `5`

Object model type "float3". Represented in the glTF JSON as an array of three numbers, and encoded in a [GLTFAccessor](class_gltfaccessor.md#class-gltfaccessor) as "VEC3".

<a id="class-gltfobjectmodelproperty-constant-gltf-object-model-type-float4"></a>

[GLTFObjectModelType](class_gltfobjectmodelproperty.md#enum-gltfobjectmodelproperty-gltfobjectmodeltype) **GLTF_OBJECT_MODEL_TYPE_FLOAT4** = `6`

Object model type "float4". Represented in the glTF JSON as an array of four numbers, and encoded in a [GLTFAccessor](class_gltfaccessor.md#class-gltfaccessor) as "VEC4".

<a id="class-gltfobjectmodelproperty-constant-gltf-object-model-type-float2x2"></a>

[GLTFObjectModelType](class_gltfobjectmodelproperty.md#enum-gltfobjectmodelproperty-gltfobjectmodeltype) **GLTF_OBJECT_MODEL_TYPE_FLOAT2X2** = `7`

Object model type "float2x2". Represented in the glTF JSON as an array of four numbers, and encoded in a [GLTFAccessor](class_gltfaccessor.md#class-gltfaccessor) as "MAT2".

<a id="class-gltfobjectmodelproperty-constant-gltf-object-model-type-float3x3"></a>

[GLTFObjectModelType](class_gltfobjectmodelproperty.md#enum-gltfobjectmodelproperty-gltfobjectmodeltype) **GLTF_OBJECT_MODEL_TYPE_FLOAT3X3** = `8`

Object model type "float3x3". Represented in the glTF JSON as an array of nine numbers, and encoded in a [GLTFAccessor](class_gltfaccessor.md#class-gltfaccessor) as "MAT3".

<a id="class-gltfobjectmodelproperty-constant-gltf-object-model-type-float4x4"></a>

[GLTFObjectModelType](class_gltfobjectmodelproperty.md#enum-gltfobjectmodelproperty-gltfobjectmodeltype) **GLTF_OBJECT_MODEL_TYPE_FLOAT4X4** = `9`

Object model type "float4x4". Represented in the glTF JSON as an array of sixteen numbers, and encoded in a [GLTFAccessor](class_gltfaccessor.md#class-gltfaccessor) as "MAT4".

<a id="class-gltfobjectmodelproperty-constant-gltf-object-model-type-int"></a>

[GLTFObjectModelType](class_gltfobjectmodelproperty.md#enum-gltfobjectmodelproperty-gltfobjectmodeltype) **GLTF_OBJECT_MODEL_TYPE_INT** = `10`

Object model type "int". Represented in the glTF JSON as a number, and encoded in a [GLTFAccessor](class_gltfaccessor.md#class-gltfaccessor) as "SCALAR". The range of values is limited to signed integers. For `KHR_interactivity`, only 32-bit integers are supported.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-gltfobjectmodelproperty-property-gltf-to-godot-expression"></a>

[Expression](class_expression.md#class-expression) **gltf_to_godot_expression** [🔗](class_gltfobjectmodelproperty.md#class-gltfobjectmodelproperty-property-gltf-to-godot-expression)

- void **set_gltf_to_godot_expression**(value: [Expression](class_expression.md#class-expression))
- [Expression](class_expression.md#class-expression) **get_gltf_to_godot_expression**()

If set, this [Expression](class_expression.md#class-expression) will be used to convert the property value from the glTF object model to the value expected by the Godot property. This is useful when the glTF object model uses a different unit system, or when the data needs to be transformed in some way. If `null`, the value will be copied as-is.

---


<a id="class-gltfobjectmodelproperty-property-godot-to-gltf-expression"></a>

[Expression](class_expression.md#class-expression) **godot_to_gltf_expression** [🔗](class_gltfobjectmodelproperty.md#class-gltfobjectmodelproperty-property-godot-to-gltf-expression)

- void **set_godot_to_gltf_expression**(value: [Expression](class_expression.md#class-expression))
- [Expression](class_expression.md#class-expression) **get_godot_to_gltf_expression**()

If set, this [Expression](class_expression.md#class-expression) will be used to convert the property value from the Godot property to the value expected by the glTF object model. This is useful when the glTF object model uses a different unit system, or when the data needs to be transformed in some way. If `null`, the value will be copied as-is.

---


<a id="class-gltfobjectmodelproperty-property-json-pointers"></a>

[Array](class_array.md#class-array)[[PackedStringArray](class_packedstringarray.md#class-packedstringarray)] **json_pointers** = `[]` [🔗](class_gltfobjectmodelproperty.md#class-gltfobjectmodelproperty-property-json-pointers)

- void **set_json_pointers**(value: [Array](class_array.md#class-array)[[PackedStringArray](class_packedstringarray.md#class-packedstringarray)])
- [Array](class_array.md#class-array)[[PackedStringArray](class_packedstringarray.md#class-packedstringarray)] **get_json_pointers**()

The glTF object model JSON pointers used to identify the property in the glTF object model. In most cases, there will be only one item in this array, but specific cases may require multiple pointers. The items are themselves arrays which represent the JSON pointer split into its components.

---


<a id="class-gltfobjectmodelproperty-property-node-paths"></a>

[Array](class_array.md#class-array)[[NodePath](class_nodepath.md#class-nodepath)] **node_paths** = `[]` [🔗](class_gltfobjectmodelproperty.md#class-gltfobjectmodelproperty-property-node-paths)

- void **set_node_paths**(value: [Array](class_array.md#class-array)[[NodePath](class_nodepath.md#class-nodepath)])
- [Array](class_array.md#class-array)[[NodePath](class_nodepath.md#class-nodepath)] **get_node_paths**()

An array of [NodePath](class_nodepath.md#class-nodepath)s that point to a property, or multiple properties, in the Godot scene tree. On import, this will either be set by [GLTFDocument](class_gltfdocument.md#class-gltfdocument), or by a [GLTFDocumentExtension](class_gltfdocumentextension.md#class-gltfdocumentextension) class. For simple cases, use [append_path_to_property()](class_gltfobjectmodelproperty.md#class-gltfobjectmodelproperty-method-append-path-to-property) to add properties to this array.

In most cases [node_paths](class_gltfobjectmodelproperty.md#class-gltfobjectmodelproperty-property-node-paths) will only have one item, but in some cases a single glTF JSON pointer will map to multiple Godot properties. For example, a [GLTFCamera](class_gltfcamera.md#class-gltfcamera) or [GLTFLight](class_gltflight.md#class-gltflight) used on multiple glTF nodes will be represented by multiple Godot nodes.

---


<a id="class-gltfobjectmodelproperty-property-object-model-type"></a>

[GLTFObjectModelType](class_gltfobjectmodelproperty.md#enum-gltfobjectmodelproperty-gltfobjectmodeltype) **object_model_type** = `0` [🔗](class_gltfobjectmodelproperty.md#class-gltfobjectmodelproperty-property-object-model-type)

- void **set_object_model_type**(value: [GLTFObjectModelType](class_gltfobjectmodelproperty.md#enum-gltfobjectmodelproperty-gltfobjectmodeltype))
- [GLTFObjectModelType](class_gltfobjectmodelproperty.md#enum-gltfobjectmodelproperty-gltfobjectmodeltype) **get_object_model_type**()

The type of data stored in the glTF file as defined by the object model. This is a superset of the available accessor types, and determines the accessor type.

---


<a id="class-gltfobjectmodelproperty-property-variant-type"></a>

[Variant.Type](class_@globalscope.md#enum-globalscope-variant-type) **variant_type** = `0` [🔗](class_gltfobjectmodelproperty.md#class-gltfobjectmodelproperty-property-variant-type)

- void **set_variant_type**(value: [Variant.Type](class_@globalscope.md#enum-globalscope-variant-type))
- [Variant.Type](class_@globalscope.md#enum-globalscope-variant-type) **get_variant_type**()

The type of data stored in the Godot property. This is the type of the property that the [node_paths](class_gltfobjectmodelproperty.md#class-gltfobjectmodelproperty-property-node-paths) point to.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-gltfobjectmodelproperty-method-append-node-path"></a>

void **append_node_path**(node_path: [NodePath](class_nodepath.md#class-nodepath)) [🔗](class_gltfobjectmodelproperty.md#class-gltfobjectmodelproperty-method-append-node-path)

Appends a [NodePath](class_nodepath.md#class-nodepath) to [node_paths](class_gltfobjectmodelproperty.md#class-gltfobjectmodelproperty-property-node-paths). This can be used by [GLTFDocumentExtension](class_gltfdocumentextension.md#class-gltfdocumentextension) classes to define how a glTF object model property maps to a Godot property, or multiple Godot properties. Prefer using [append_path_to_property()](class_gltfobjectmodelproperty.md#class-gltfobjectmodelproperty-method-append-path-to-property) for simple cases. Be sure to also call [set_types()](class_gltfobjectmodelproperty.md#class-gltfobjectmodelproperty-method-set-types) once (the order does not matter).

---


<a id="class-gltfobjectmodelproperty-method-append-path-to-property"></a>

void **append_path_to_property**(node_path: [NodePath](class_nodepath.md#class-nodepath), prop_name: [StringName](class_stringname.md#class-stringname)) [🔗](class_gltfobjectmodelproperty.md#class-gltfobjectmodelproperty-method-append-path-to-property)

High-level wrapper over [append_node_path()](class_gltfobjectmodelproperty.md#class-gltfobjectmodelproperty-method-append-node-path) that handles the most common cases. It constructs a new [NodePath](class_nodepath.md#class-nodepath) using `node_path` as a base and appends `prop_name` to the subpath. Be sure to also call [set_types()](class_gltfobjectmodelproperty.md#class-gltfobjectmodelproperty-method-set-types) once (the order does not matter).

---


<a id="class-gltfobjectmodelproperty-method-get-accessor-type"></a>

[GLTFAccessorType](class_gltfaccessor.md#enum-gltfaccessor-gltfaccessortype) **get_accessor_type**() const [🔗](class_gltfobjectmodelproperty.md#class-gltfobjectmodelproperty-method-get-accessor-type)

The GLTF accessor type associated with this property's [object_model_type](class_gltfobjectmodelproperty.md#class-gltfobjectmodelproperty-property-object-model-type). See [GLTFAccessor.accessor_type](class_gltfaccessor.md#class-gltfaccessor-property-accessor-type) for possible values, and see [GLTFObjectModelType](class_gltfobjectmodelproperty.md#enum-gltfobjectmodelproperty-gltfobjectmodeltype) for how the object model type maps to accessor types.

---


<a id="class-gltfobjectmodelproperty-method-has-json-pointers"></a>

[bool](class_bool.md#class-bool) **has_json_pointers**() const [🔗](class_gltfobjectmodelproperty.md#class-gltfobjectmodelproperty-method-has-json-pointers)

Returns `true` if [json_pointers](class_gltfobjectmodelproperty.md#class-gltfobjectmodelproperty-property-json-pointers) is not empty. This is used during export to determine if a **GLTFObjectModelProperty** can handle converting a Godot property to a glTF object model property.

---


<a id="class-gltfobjectmodelproperty-method-has-node-paths"></a>

[bool](class_bool.md#class-bool) **has_node_paths**() const [🔗](class_gltfobjectmodelproperty.md#class-gltfobjectmodelproperty-method-has-node-paths)

Returns `true` if [node_paths](class_gltfobjectmodelproperty.md#class-gltfobjectmodelproperty-property-node-paths) is not empty. This is used during import to determine if a **GLTFObjectModelProperty** can handle converting a glTF object model property to a Godot property.

---


<a id="class-gltfobjectmodelproperty-method-set-types"></a>

void **set_types**(variant_type: [Variant.Type](class_@globalscope.md#enum-globalscope-variant-type), obj_model_type: [GLTFObjectModelType](class_gltfobjectmodelproperty.md#enum-gltfobjectmodelproperty-gltfobjectmodeltype)) [🔗](class_gltfobjectmodelproperty.md#class-gltfobjectmodelproperty-method-set-types)

Sets the [variant_type](class_gltfobjectmodelproperty.md#class-gltfobjectmodelproperty-property-variant-type) and [object_model_type](class_gltfobjectmodelproperty.md#class-gltfobjectmodelproperty-property-object-model-type) properties. This is a convenience method to set both properties at once, since they are almost always known at the same time. This method should be called once. Calling it again with the same values will have no effect.
