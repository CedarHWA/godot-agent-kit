> Source: https://docs.godotengine.org/en/4.7/classes/class_occluderpolygon2d.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="occluderpolygon2d"></a>

<a id="class-occluderpolygon2d"></a>

# OccluderPolygon2D

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Defines a 2D polygon for LightOccluder2D.

<a id="description"></a>

## Description

Editor facility that helps you draw a 2D polygon used as resource for [LightOccluder2D](class_lightoccluder2d.md#class-lightoccluder2d).

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [bool](class_bool.md#class-bool) | [closed](class_occluderpolygon2d.md#class-occluderpolygon2d-property-closed) | `true` |
| [CullMode](class_occluderpolygon2d.md#enum-occluderpolygon2d-cullmode) | [cull_mode](class_occluderpolygon2d.md#class-occluderpolygon2d-property-cull-mode) | `0` |
| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) | [polygon](class_occluderpolygon2d.md#class-occluderpolygon2d-property-polygon) | `PackedVector2Array()` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-occluderpolygon2d-cullmode"></a>

enum **CullMode**: [🔗](class_occluderpolygon2d.md#enum-occluderpolygon2d-cullmode)

<a id="class-occluderpolygon2d-constant-cull-disabled"></a>

[CullMode](class_occluderpolygon2d.md#enum-occluderpolygon2d-cullmode) **CULL_DISABLED** = `0`

Culling is disabled. See [cull_mode](class_occluderpolygon2d.md#class-occluderpolygon2d-property-cull-mode).

<a id="class-occluderpolygon2d-constant-cull-clockwise"></a>

[CullMode](class_occluderpolygon2d.md#enum-occluderpolygon2d-cullmode) **CULL_CLOCKWISE** = `1`

Culling is performed in the clockwise direction. See [cull_mode](class_occluderpolygon2d.md#class-occluderpolygon2d-property-cull-mode).

<a id="class-occluderpolygon2d-constant-cull-counter-clockwise"></a>

[CullMode](class_occluderpolygon2d.md#enum-occluderpolygon2d-cullmode) **CULL_COUNTER_CLOCKWISE** = `2`

Culling is performed in the counterclockwise direction. See [cull_mode](class_occluderpolygon2d.md#class-occluderpolygon2d-property-cull-mode).

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-occluderpolygon2d-property-closed"></a>

[bool](class_bool.md#class-bool) **closed** = `true` [🔗](class_occluderpolygon2d.md#class-occluderpolygon2d-property-closed)

- void **set_closed**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_closed**()

If `true`, closes the polygon. A closed OccluderPolygon2D occludes the light coming from any direction. An opened OccluderPolygon2D occludes the light only at its outline's direction.

---


<a id="class-occluderpolygon2d-property-cull-mode"></a>

[CullMode](class_occluderpolygon2d.md#enum-occluderpolygon2d-cullmode) **cull_mode** = `0` [🔗](class_occluderpolygon2d.md#class-occluderpolygon2d-property-cull-mode)

- void **set_cull_mode**(value: [CullMode](class_occluderpolygon2d.md#enum-occluderpolygon2d-cullmode))
- [CullMode](class_occluderpolygon2d.md#enum-occluderpolygon2d-cullmode) **get_cull_mode**()

The culling mode to use.

---


<a id="class-occluderpolygon2d-property-polygon"></a>

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **polygon** = `PackedVector2Array()` [🔗](class_occluderpolygon2d.md#class-occluderpolygon2d-property-polygon)

- void **set_polygon**(value: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array))
- [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **get_polygon**()

A [Vector2](class_vector2.md#class-vector2) array with the index for polygon's vertices positions.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) for more details.
