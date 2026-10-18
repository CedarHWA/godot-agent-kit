> Source: https://docs.godotengine.org/en/4.7/classes/class_rid.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="rid"></a>

<a id="class-rid"></a>

# RID

A handle for a [Resource](class_resource.md#class-resource)'s unique identifier.

<a id="description"></a>

## Description

The RID [Variant](class_variant.md#class-variant) type is used to access a low-level resource by its unique ID. RIDs are opaque, which means they do not grant access to the resource by themselves. They are used by the low-level server classes, such as [DisplayServer](class_displayserver.md#class-displayserver), [RenderingServer](class_renderingserver.md#class-renderingserver), [TextServer](class_textserver.md#class-textserver), etc.

A low-level resource may correspond to a high-level [Resource](class_resource.md#class-resource), such as [Texture](class_texture.md#class-texture) or [Mesh](class_mesh.md#class-mesh).

**Note:** RIDs are only useful during the current session. It won't correspond to a similar resource if sent over a network, or loaded from a file at a later time.

**Note:** In a boolean context, an RID will evaluate to `false` if it has the invalid ID `0`. Otherwise, an RID will always evaluate to `true`. This is equivalent to calling [is_valid()](class_rid.md#class-rid-method-is-valid).

Note

There are notable differences when using this API with C#. See [C# API differences to GDScript](../tutorials/scripting/c_sharp/c_sharp_differences.md#doc-c-sharp-differences) for more information.

<a id="constructors"></a>

## Constructors

|  |  |
| --- | --- |
| [RID](class_rid.md#class-rid) | [RID](class_rid.md#class-rid-constructor-rid)() |
| [RID](class_rid.md#class-rid) | [RID](class_rid.md#class-rid-constructor-rid)(from: [RID](class_rid.md#class-rid)) |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [int](class_int.md#class-int) | [get_id](class_rid.md#class-rid-method-get-id)() const |
| [bool](class_bool.md#class-bool) | [is_valid](class_rid.md#class-rid-method-is-valid)() const |

<a id="operators"></a>

## Operators

|  |  |
| --- | --- |
| [bool](class_bool.md#class-bool) | [operator !=](class_rid.md#class-rid-operator-neq-rid)(right: [RID](class_rid.md#class-rid)) |
| [bool](class_bool.md#class-bool) | [operator <](class_rid.md#class-rid-operator-lt-rid)(right: [RID](class_rid.md#class-rid)) |
| [bool](class_bool.md#class-bool) | [operator <=](class_rid.md#class-rid-operator-lte-rid)(right: [RID](class_rid.md#class-rid)) |
| [bool](class_bool.md#class-bool) | [operator ==](class_rid.md#class-rid-operator-eq-rid)(right: [RID](class_rid.md#class-rid)) |
| [bool](class_bool.md#class-bool) | [operator >](class_rid.md#class-rid-operator-gt-rid)(right: [RID](class_rid.md#class-rid)) |
| [bool](class_bool.md#class-bool) | [operator >=](class_rid.md#class-rid-operator-gte-rid)(right: [RID](class_rid.md#class-rid)) |

---


<a id="constructor-descriptions"></a>

## Constructor Descriptions

<a id="class-rid-constructor-rid"></a>

[RID](class_rid.md#class-rid) **RID**() [🔗](class_rid.md#class-rid-constructor-rid)

Constructs an empty **RID** with the invalid ID `0`.

---

[RID](class_rid.md#class-rid) **RID**(from: [RID](class_rid.md#class-rid))

Constructs an **RID** as a copy of the given **RID**.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-rid-method-get-id"></a>

[int](class_int.md#class-int) **get_id**() const [🔗](class_rid.md#class-rid-method-get-id)

Returns the ID of the referenced low-level resource.

---


<a id="class-rid-method-is-valid"></a>

[bool](class_bool.md#class-bool) **is_valid**() const [🔗](class_rid.md#class-rid-method-is-valid)

Returns `true` if the **RID** is not `0`.

---


<a id="operator-descriptions"></a>

## Operator Descriptions

<a id="class-rid-operator-neq-rid"></a>

[bool](class_bool.md#class-bool) **operator !=**(right: [RID](class_rid.md#class-rid)) [🔗](class_rid.md#class-rid-operator-neq-rid)

Returns `true` if the **RID**s are not equal.

---


<a id="class-rid-operator-lt-rid"></a>

[bool](class_bool.md#class-bool) **operator <**(right: [RID](class_rid.md#class-rid)) [🔗](class_rid.md#class-rid-operator-lt-rid)

Returns `true` if the **RID**'s ID is less than `right`'s ID.

---


<a id="class-rid-operator-lte-rid"></a>

[bool](class_bool.md#class-bool) **operator <=**(right: [RID](class_rid.md#class-rid)) [🔗](class_rid.md#class-rid-operator-lte-rid)

Returns `true` if the **RID**'s ID is less than or equal to `right`'s ID.

---


<a id="class-rid-operator-eq-rid"></a>

[bool](class_bool.md#class-bool) **operator ==**(right: [RID](class_rid.md#class-rid)) [🔗](class_rid.md#class-rid-operator-eq-rid)

Returns `true` if both **RID**s are equal, which means they both refer to the same low-level resource.

---


<a id="class-rid-operator-gt-rid"></a>

[bool](class_bool.md#class-bool) **operator >**(right: [RID](class_rid.md#class-rid)) [🔗](class_rid.md#class-rid-operator-gt-rid)

Returns `true` if the **RID**'s ID is greater than `right`'s ID.

---


<a id="class-rid-operator-gte-rid"></a>

[bool](class_bool.md#class-bool) **operator >=**(right: [RID](class_rid.md#class-rid)) [🔗](class_rid.md#class-rid-operator-gte-rid)

Returns `true` if the **RID**'s ID is greater than or equal to `right`'s ID.
