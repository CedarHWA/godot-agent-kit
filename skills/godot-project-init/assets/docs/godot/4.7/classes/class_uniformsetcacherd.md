> Source: https://docs.godotengine.org/en/4.7/classes/class_uniformsetcacherd.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="uniformsetcacherd"></a>

<a id="class-uniformsetcacherd"></a>

# UniformSetCacheRD

**Inherits:** [Object](class_object.md#class-object)

Uniform set cache manager for Rendering Device based renderers.

<a id="description"></a>

## Description

Uniform set cache manager for [RenderingDevice](class_renderingdevice.md#class-renderingdevice)-based renderers. Provides a way to create a uniform set and reuse it in subsequent calls for as long as the uniform set exists. Uniform set will automatically be cleaned up when dependent objects are freed.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [RID](class_rid.md#class-rid) | [get_cache](class_uniformsetcacherd.md#class-uniformsetcacherd-method-get-cache)(shader: [RID](class_rid.md#class-rid), set: [int](class_int.md#class-int), uniforms: [Array](class_array.md#class-array)[[RDUniform](class_rduniform.md#class-rduniform)]) static |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-uniformsetcacherd-method-get-cache"></a>

[RID](class_rid.md#class-rid) **get_cache**(shader: [RID](class_rid.md#class-rid), set: [int](class_int.md#class-int), uniforms: [Array](class_array.md#class-array)[[RDUniform](class_rduniform.md#class-rduniform)]) static [🔗](class_uniformsetcacherd.md#class-uniformsetcacherd-method-get-cache)

Creates/returns a cached uniform set based on the provided uniforms for a given shader.
