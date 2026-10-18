> Source: https://docs.godotengine.org/en/4.7/classes/class_openxrrendermodelmanager.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="openxrrendermodelmanager"></a>

<a id="class-openxrrendermodelmanager"></a>

# OpenXRRenderModelManager

**Inherits:** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Helper node that will automatically manage displaying render models.

<a id="description"></a>

## Description

This helper node will automatically manage displaying render models. It will create new [OpenXRRenderModel](class_openxrrendermodel.md#class-openxrrendermodel) nodes as controllers and other hand held devices are detected, and remove those nodes when they are deactivated.

**Note:** If you want more control over this logic you can alternatively call [OpenXRRenderModelExtension.render_model_get_all()](class_openxrrendermodelextension.md#class-openxrrendermodelextension-method-render-model-get-all) to obtain a list of active render model ids and create [OpenXRRenderModel](class_openxrrendermodel.md#class-openxrrendermodel) instances for each render model id provided.

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [String](class_string.md#class-string) | [make_local_to_pose](class_openxrrendermodelmanager.md#class-openxrrendermodelmanager-property-make-local-to-pose) | `""` |
| [RenderModelTracker](class_openxrrendermodelmanager.md#enum-openxrrendermodelmanager-rendermodeltracker) | [tracker](class_openxrrendermodelmanager.md#class-openxrrendermodelmanager-property-tracker) | `0` |

---


<a id="signals"></a>

## Signals

<a id="class-openxrrendermodelmanager-signal-render-model-added"></a>

**render_model_added**(render_model: [OpenXRRenderModel](class_openxrrendermodel.md#class-openxrrendermodel)) [🔗](class_openxrrendermodelmanager.md#class-openxrrendermodelmanager-signal-render-model-added)

Emitted when a render model node is added as a child to this node.

---


<a id="class-openxrrendermodelmanager-signal-render-model-removed"></a>

**render_model_removed**(render_model: [OpenXRRenderModel](class_openxrrendermodel.md#class-openxrrendermodel)) [🔗](class_openxrrendermodelmanager.md#class-openxrrendermodelmanager-signal-render-model-removed)

Emitted when a render model child node is about to be removed from this node.

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-openxrrendermodelmanager-rendermodeltracker"></a>

enum **RenderModelTracker**: [🔗](class_openxrrendermodelmanager.md#enum-openxrrendermodelmanager-rendermodeltracker)

<a id="class-openxrrendermodelmanager-constant-render-model-tracker-any"></a>

[RenderModelTracker](class_openxrrendermodelmanager.md#enum-openxrrendermodelmanager-rendermodeltracker) **RENDER_MODEL_TRACKER_ANY** = `0`

All active render models are shown regardless of what tracker they relate to.

<a id="class-openxrrendermodelmanager-constant-render-model-tracker-none-set"></a>

[RenderModelTracker](class_openxrrendermodelmanager.md#enum-openxrrendermodelmanager-rendermodeltracker) **RENDER_MODEL_TRACKER_NONE_SET** = `1`

Only active render models are shown that are not related to any tracker we manage.

<a id="class-openxrrendermodelmanager-constant-render-model-tracker-left-hand"></a>

[RenderModelTracker](class_openxrrendermodelmanager.md#enum-openxrrendermodelmanager-rendermodeltracker) **RENDER_MODEL_TRACKER_LEFT_HAND** = `2`

Only active render models are shown that are related to the left hand tracker.

<a id="class-openxrrendermodelmanager-constant-render-model-tracker-right-hand"></a>

[RenderModelTracker](class_openxrrendermodelmanager.md#enum-openxrrendermodelmanager-rendermodeltracker) **RENDER_MODEL_TRACKER_RIGHT_HAND** = `3`

Only active render models are shown that are related to the right hand tracker.

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-openxrrendermodelmanager-property-make-local-to-pose"></a>

[String](class_string.md#class-string) **make_local_to_pose** = `""` [🔗](class_openxrrendermodelmanager.md#class-openxrrendermodelmanager-property-make-local-to-pose)

- void **set_make_local_to_pose**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_make_local_to_pose**()

Position render models local to this pose (this will adjust the position of the render models container node).

---


<a id="class-openxrrendermodelmanager-property-tracker"></a>

[RenderModelTracker](class_openxrrendermodelmanager.md#enum-openxrrendermodelmanager-rendermodeltracker) **tracker** = `0` [🔗](class_openxrrendermodelmanager.md#class-openxrrendermodelmanager-property-tracker)

- void **set_tracker**(value: [RenderModelTracker](class_openxrrendermodelmanager.md#enum-openxrrendermodelmanager-rendermodeltracker))
- [RenderModelTracker](class_openxrrendermodelmanager.md#enum-openxrrendermodelmanager-rendermodeltracker) **get_tracker**()

Limits render models to the specified tracker. Include: 0 = All render models, 1 = Render models not related to a tracker, 2 = Render models related to the left hand tracker, 3 = Render models related to the right hand tracker.
