> Source: https://docs.godotengine.org/en/4.7/classes/class_renderscenebuffersextension.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="renderscenebuffersextension"></a>

<a id="class-renderscenebuffersextension"></a>

# RenderSceneBuffersExtension

**Inherits:** [RenderSceneBuffers](class_renderscenebuffers.md#class-renderscenebuffers) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

This class allows for a RenderSceneBuffer implementation to be made in GDExtension.

<a id="description"></a>

## Description

This class allows for a RenderSceneBuffer implementation to be made in GDExtension.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [_configure](class_renderscenebuffersextension.md#class-renderscenebuffersextension-private-method-configure)(config: [RenderSceneBuffersConfiguration](class_renderscenebuffersconfiguration.md#class-renderscenebuffersconfiguration)) virtual |
| void | [_set_anisotropic_filtering_level](class_renderscenebuffersextension.md#class-renderscenebuffersextension-private-method-set-anisotropic-filtering-level)(anisotropic_filtering_level: [int](class_int.md#class-int)) virtual |
| void | [_set_fsr_sharpness](class_renderscenebuffersextension.md#class-renderscenebuffersextension-private-method-set-fsr-sharpness)(fsr_sharpness: [float](class_float.md#class-float)) virtual |
| void | [_set_texture_mipmap_bias](class_renderscenebuffersextension.md#class-renderscenebuffersextension-private-method-set-texture-mipmap-bias)(texture_mipmap_bias: [float](class_float.md#class-float)) virtual |
| void | [_set_use_debanding](class_renderscenebuffersextension.md#class-renderscenebuffersextension-private-method-set-use-debanding)(use_debanding: [bool](class_bool.md#class-bool)) virtual |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-renderscenebuffersextension-private-method-configure"></a>

void **_configure**(config: [RenderSceneBuffersConfiguration](class_renderscenebuffersconfiguration.md#class-renderscenebuffersconfiguration)) virtual [🔗](class_renderscenebuffersextension.md#class-renderscenebuffersextension-private-method-configure)

Implement this in GDExtension to handle the (re)sizing of a viewport.

---


<a id="class-renderscenebuffersextension-private-method-set-anisotropic-filtering-level"></a>

void **_set_anisotropic_filtering_level**(anisotropic_filtering_level: [int](class_int.md#class-int)) virtual [🔗](class_renderscenebuffersextension.md#class-renderscenebuffersextension-private-method-set-anisotropic-filtering-level)

Implement this in GDExtension to change the anisotropic filtering level.

---


<a id="class-renderscenebuffersextension-private-method-set-fsr-sharpness"></a>

void **_set_fsr_sharpness**(fsr_sharpness: [float](class_float.md#class-float)) virtual [🔗](class_renderscenebuffersextension.md#class-renderscenebuffersextension-private-method-set-fsr-sharpness)

Implement this in GDExtension to record a new FSR sharpness value.

---


<a id="class-renderscenebuffersextension-private-method-set-texture-mipmap-bias"></a>

void **_set_texture_mipmap_bias**(texture_mipmap_bias: [float](class_float.md#class-float)) virtual [🔗](class_renderscenebuffersextension.md#class-renderscenebuffersextension-private-method-set-texture-mipmap-bias)

Implement this in GDExtension to change the texture mipmap bias.

---


<a id="class-renderscenebuffersextension-private-method-set-use-debanding"></a>

void **_set_use_debanding**(use_debanding: [bool](class_bool.md#class-bool)) virtual [🔗](class_renderscenebuffersextension.md#class-renderscenebuffersextension-private-method-set-use-debanding)

Implement this in GDExtension to react to the debanding flag changing.
