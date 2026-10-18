> Source: https://docs.godotengine.org/en/4.7/classes/class_blitmaterial.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="blitmaterial"></a>

<a id="class-blitmaterial"></a>

# BlitMaterial

**Inherits:** [Material](class_material.md#class-material) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A material that processes blit calls to a DrawableTexture.

<a id="description"></a>

## Description

A material resource that can be used by DrawableTextures when processing blit calls to draw.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [BlendMode](class_blitmaterial.md#enum-blitmaterial-blendmode) | [blend_mode](class_blitmaterial.md#class-blitmaterial-property-blend-mode) | `0` |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-blitmaterial-blendmode"></a>

enum **BlendMode**: [🔗](class_blitmaterial.md#enum-blitmaterial-blendmode)

<a id="class-blitmaterial-constant-blend-mode-mix"></a>

[BlendMode](class_blitmaterial.md#enum-blitmaterial-blendmode) **BLEND_MODE_MIX** = `0`

Mix blending mode. Colors are assumed to be independent of the alpha (opacity) value.

<a id="class-blitmaterial-constant-blend-mode-add"></a>

[BlendMode](class_blitmaterial.md#enum-blitmaterial-blendmode) **BLEND_MODE_ADD** = `1`

Additive blending mode.

<a id="class-blitmaterial-constant-blend-mode-sub"></a>

[BlendMode](class_blitmaterial.md#enum-blitmaterial-blendmode) **BLEND_MODE_SUB** = `2`

Subtractive blending mode.

<a id="class-blitmaterial-constant-blend-mode-mul"></a>

[BlendMode](class_blitmaterial.md#enum-blitmaterial-blendmode) **BLEND_MODE_MUL** = `3`

Multiplicative blending mode.

<a id="class-blitmaterial-constant-blend-mode-disabled"></a>

[BlendMode](class_blitmaterial.md#enum-blitmaterial-blendmode) **BLEND_MODE_DISABLED** = `4`

No blending mode, direct color copy.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-blitmaterial-property-blend-mode"></a>

[BlendMode](class_blitmaterial.md#enum-blitmaterial-blendmode) **blend_mode** = `0` [🔗](class_blitmaterial.md#class-blitmaterial-property-blend-mode)

- void **set_blend_mode**(value: [BlendMode](class_blitmaterial.md#enum-blitmaterial-blendmode))
- [BlendMode](class_blitmaterial.md#enum-blitmaterial-blendmode) **get_blend_mode**()

The manner in which the newly blitted texture is blended with the original DrawableTexture.
