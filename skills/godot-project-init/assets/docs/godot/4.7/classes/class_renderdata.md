> Source: https://docs.godotengine.org/en/4.7/classes/class_renderdata.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="renderdata"></a>

<a id="class-renderdata"></a>

# RenderData

**Inherits:** [Object](class_object.md#class-object)

**Inherited By:** [RenderDataExtension](class_renderdataextension.md#class-renderdataextension), [RenderDataRD](class_renderdatard.md#class-renderdatard)

Abstract render data object, holds frame data related to rendering a single frame of a viewport.

<a id="description"></a>

## Description

Abstract render data object, exists for the duration of rendering a single viewport. See also [RenderDataRD](class_renderdatard.md#class-renderdatard), [RenderSceneData](class_renderscenedata.md#class-renderscenedata), and [RenderSceneDataRD](class_renderscenedatard.md#class-renderscenedatard).

**Note:** This is an internal rendering server object. Do not instantiate this class from a script.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [RID](class_rid.md#class-rid) | [get_camera_attributes](class_renderdata.md#class-renderdata-method-get-camera-attributes)() const |
| [RID](class_rid.md#class-rid) | [get_environment](class_renderdata.md#class-renderdata-method-get-environment)() const |
| [RenderSceneBuffers](class_renderscenebuffers.md#class-renderscenebuffers) | [get_render_scene_buffers](class_renderdata.md#class-renderdata-method-get-render-scene-buffers)() const |
| [RenderSceneData](class_renderscenedata.md#class-renderscenedata) | [get_render_scene_data](class_renderdata.md#class-renderdata-method-get-render-scene-data)() const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-renderdata-method-get-camera-attributes"></a>

[RID](class_rid.md#class-rid) **get_camera_attributes**() const [🔗](class_renderdata.md#class-renderdata-method-get-camera-attributes)

Returns the [RID](class_rid.md#class-rid) of the camera attributes object in the [RenderingServer](class_renderingserver.md#class-renderingserver) being used to render this viewport.

---


<a id="class-renderdata-method-get-environment"></a>

[RID](class_rid.md#class-rid) **get_environment**() const [🔗](class_renderdata.md#class-renderdata-method-get-environment)

Returns the [RID](class_rid.md#class-rid) of the environment object in the [RenderingServer](class_renderingserver.md#class-renderingserver) being used to render this viewport.

---


<a id="class-renderdata-method-get-render-scene-buffers"></a>

[RenderSceneBuffers](class_renderscenebuffers.md#class-renderscenebuffers) **get_render_scene_buffers**() const [🔗](class_renderdata.md#class-renderdata-method-get-render-scene-buffers)

Returns the [RenderSceneBuffers](class_renderscenebuffers.md#class-renderscenebuffers) object managing the scene buffers for rendering this viewport.

---


<a id="class-renderdata-method-get-render-scene-data"></a>

[RenderSceneData](class_renderscenedata.md#class-renderscenedata) **get_render_scene_data**() const [🔗](class_renderdata.md#class-renderdata-method-get-render-scene-data)

Returns the [RenderSceneData](class_renderscenedata.md#class-renderscenedata) object managing this frames scene data.
