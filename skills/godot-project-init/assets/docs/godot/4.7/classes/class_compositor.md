> Source: https://docs.godotengine.org/en/4.7/classes/class_compositor.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="compositor"></a>

<a id="class-compositor"></a>

# Compositor

**Experimental:** More customization of the rendering pipeline will be added in the future.

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Stores attributes used to customize how a Viewport is rendered.

<a id="description"></a>

## Description

The compositor resource stores attributes used to customize how a [Viewport](class_viewport.md#class-viewport) is rendered.

<a id="tutorials"></a>

## Tutorials

- [The Compositor](../tutorials/rendering/compositor.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [Array](class_array.md#class-array)[[CompositorEffect](class_compositoreffect.md#class-compositoreffect)] | [compositor_effects](class_compositor.md#class-compositor-property-compositor-effects) | `[]` |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-compositor-property-compositor-effects"></a>

[Array](class_array.md#class-array)[[CompositorEffect](class_compositoreffect.md#class-compositoreffect)] **compositor_effects** = `[]` [🔗](class_compositor.md#class-compositor-property-compositor-effects)

- void **set_compositor_effects**(value: [Array](class_array.md#class-array)[[CompositorEffect](class_compositoreffect.md#class-compositoreffect)])
- [Array](class_array.md#class-array)[[CompositorEffect](class_compositoreffect.md#class-compositoreffect)] **get_compositor_effects**()

The custom [CompositorEffect](class_compositoreffect.md#class-compositoreffect)s that are applied during rendering of viewports using this compositor.
