> Source: https://docs.godotengine.org/en/4.7/classes/class_renderscenebuffers.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="renderscenebuffers"></a>

<a id="class-renderscenebuffers"></a>

# RenderSceneBuffers

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [RenderSceneBuffersExtension](class_renderscenebuffersextension.md#class-renderscenebuffersextension), [RenderSceneBuffersRD](class_renderscenebuffersrd.md#class-renderscenebuffersrd)

Abstract scene buffers object, created for each viewport for which 3D rendering is done.

<a id="description"></a>

## Description

Abstract scene buffers object, created for each viewport for which 3D rendering is done. It manages any additional buffers used during rendering and will discard buffers when the viewport is resized. See also [RenderSceneBuffersRD](class_renderscenebuffersrd.md#class-renderscenebuffersrd).

**Note:** This is an internal rendering server object. Do not instantiate this class from a script.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [configure](class_renderscenebuffers.md#class-renderscenebuffers-method-configure)(config: [RenderSceneBuffersConfiguration](class_renderscenebuffersconfiguration.md#class-renderscenebuffersconfiguration)) |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-renderscenebuffers-method-configure"></a>

void **configure**(config: [RenderSceneBuffersConfiguration](class_renderscenebuffersconfiguration.md#class-renderscenebuffersconfiguration)) [🔗](class_renderscenebuffers.md#class-renderscenebuffers-method-configure)

This method is called by the rendering server when the associated viewport's configuration is changed. It will discard the old buffers and recreate the internal buffers used.
