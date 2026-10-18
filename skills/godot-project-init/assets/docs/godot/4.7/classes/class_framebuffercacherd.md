> Source: https://docs.godotengine.org/en/4.7/classes/class_framebuffercacherd.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="framebuffercacherd"></a>

<a id="class-framebuffercacherd"></a>

# FramebufferCacheRD

**Inherits:** [Object](class_object.md#class-object)

Framebuffer cache manager for Rendering Device based renderers.

<a id="description"></a>

## Description

Framebuffer cache manager for [RenderingDevice](class_renderingdevice.md#class-renderingdevice)-based renderers. Provides a way to create a framebuffer and reuse it in subsequent calls for as long as the used textures exists. Framebuffers will automatically be cleaned up when dependent objects are freed.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [RID](class_rid.md#class-rid) | [get_cache_multipass](class_framebuffercacherd.md#class-framebuffercacherd-method-get-cache-multipass)(textures: [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)], passes: [Array](class_array.md#class-array)[[RDFramebufferPass](class_rdframebufferpass.md#class-rdframebufferpass)], views: [int](class_int.md#class-int)) static |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-framebuffercacherd-method-get-cache-multipass"></a>

[RID](class_rid.md#class-rid) **get_cache_multipass**(textures: [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)], passes: [Array](class_array.md#class-array)[[RDFramebufferPass](class_rdframebufferpass.md#class-rdframebufferpass)], views: [int](class_int.md#class-int)) static [🔗](class_framebuffercacherd.md#class-framebuffercacherd-method-get-cache-multipass)

Creates, or obtains a cached, framebuffer. `textures` lists textures accessed. `passes` defines the subpasses and texture allocation, if left empty a single pass is created and textures are allocated depending on their usage flags. `views` defines the number of views used when rendering.
