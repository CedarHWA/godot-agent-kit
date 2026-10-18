> Source: https://docs.godotengine.org/en/4.7/classes/class_renderdataextension.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="renderdataextension"></a>

<a id="class-renderdataextension"></a>

# RenderDataExtension

**Inherits:** [RenderData](class_renderdata.md#class-renderdata) **<** [Object](class_object.md#class-object)

This class allows for a RenderData implementation to be made in GDExtension.

<a id="description"></a>

## Description

This class allows for a RenderData implementation to be made in GDExtension.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [RID](class_rid.md#class-rid) | [_get_camera_attributes](class_renderdataextension.md#class-renderdataextension-private-method-get-camera-attributes)() virtual const |
| [RID](class_rid.md#class-rid) | [_get_environment](class_renderdataextension.md#class-renderdataextension-private-method-get-environment)() virtual const |
| [RenderSceneBuffers](class_renderscenebuffers.md#class-renderscenebuffers) | [_get_render_scene_buffers](class_renderdataextension.md#class-renderdataextension-private-method-get-render-scene-buffers)() virtual const |
| [RenderSceneData](class_renderscenedata.md#class-renderscenedata) | [_get_render_scene_data](class_renderdataextension.md#class-renderdataextension-private-method-get-render-scene-data)() virtual const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-renderdataextension-private-method-get-camera-attributes"></a>

[RID](class_rid.md#class-rid) **_get_camera_attributes**() virtual const [🔗](class_renderdataextension.md#class-renderdataextension-private-method-get-camera-attributes)

Implement this in GDExtension to return the [RID](class_rid.md#class-rid) for the implementation's camera attributes object.

---


<a id="class-renderdataextension-private-method-get-environment"></a>

[RID](class_rid.md#class-rid) **_get_environment**() virtual const [🔗](class_renderdataextension.md#class-renderdataextension-private-method-get-environment)

Implement this in GDExtension to return the [RID](class_rid.md#class-rid) of the implementation's environment object.

---


<a id="class-renderdataextension-private-method-get-render-scene-buffers"></a>

[RenderSceneBuffers](class_renderscenebuffers.md#class-renderscenebuffers) **_get_render_scene_buffers**() virtual const [🔗](class_renderdataextension.md#class-renderdataextension-private-method-get-render-scene-buffers)

Implement this in GDExtension to return the implementation's [RenderSceneBuffers](class_renderscenebuffers.md#class-renderscenebuffers) object.

---


<a id="class-renderdataextension-private-method-get-render-scene-data"></a>

[RenderSceneData](class_renderscenedata.md#class-renderscenedata) **_get_render_scene_data**() virtual const [🔗](class_renderdataextension.md#class-renderdataextension-private-method-get-render-scene-data)

Implement this in GDExtension to return the implementation's [RenderSceneDataExtension](class_renderscenedataextension.md#class-renderscenedataextension) object.
