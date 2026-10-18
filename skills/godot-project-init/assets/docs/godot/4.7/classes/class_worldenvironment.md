> Source: https://docs.godotengine.org/en/4.7/classes/class_worldenvironment.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="worldenvironment"></a>

<a id="class-worldenvironment"></a>

# WorldEnvironment

**Inherits:** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Default environment properties for the entire scene (post-processing effects, lighting and background settings).

<a id="description"></a>

## Description

The **WorldEnvironment** node is used to configure the default [Environment](class_environment.md#class-environment) for the scene.

The parameters defined in the **WorldEnvironment** can be overridden by an [Environment](class_environment.md#class-environment) node set on the current [Camera3D](class_camera3d.md#class-camera3d). Additionally, only one **WorldEnvironment** may be instantiated in a given scene at a time.

The **WorldEnvironment** allows the user to specify default lighting parameters (e.g. ambient lighting), various post-processing effects (e.g. SSAO, DOF, Tonemapping), and how to draw the background (e.g. solid color, skybox). Usually, these are added in order to improve the realism/color balance of the scene.

<a id="tutorials"></a>

## Tutorials

- [Environment and post-processing](../tutorials/3d/environment_and_post_processing.md)
- [3D Material Testers Demo](https://godotengine.org/asset-library/asset/2742)
- [Third Person Shooter (TPS) Demo](https://godotengine.org/asset-library/asset/2710)

<a id="properties"></a>

## Properties

|  |  |
| --- | --- |
| [CameraAttributes](class_cameraattributes.md#class-cameraattributes) | [camera_attributes](class_worldenvironment.md#class-worldenvironment-property-camera-attributes) |
| [Compositor](class_compositor.md#class-compositor) | [compositor](class_worldenvironment.md#class-worldenvironment-property-compositor) |
| [Environment](class_environment.md#class-environment) | [environment](class_worldenvironment.md#class-worldenvironment-property-environment) |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-worldenvironment-property-camera-attributes"></a>

[CameraAttributes](class_cameraattributes.md#class-cameraattributes) **camera_attributes** [🔗](class_worldenvironment.md#class-worldenvironment-property-camera-attributes)

- void **set_camera_attributes**(value: [CameraAttributes](class_cameraattributes.md#class-cameraattributes))
- [CameraAttributes](class_cameraattributes.md#class-cameraattributes) **get_camera_attributes**()

The default [CameraAttributes](class_cameraattributes.md#class-cameraattributes) resource to use if none set on the [Camera3D](class_camera3d.md#class-camera3d).

---


<a id="class-worldenvironment-property-compositor"></a>

[Compositor](class_compositor.md#class-compositor) **compositor** [🔗](class_worldenvironment.md#class-worldenvironment-property-compositor)

- void **set_compositor**(value: [Compositor](class_compositor.md#class-compositor))
- [Compositor](class_compositor.md#class-compositor) **get_compositor**()

The default [Compositor](class_compositor.md#class-compositor) resource to use if none set on the [Camera3D](class_camera3d.md#class-camera3d).

---


<a id="class-worldenvironment-property-environment"></a>

[Environment](class_environment.md#class-environment) **environment** [🔗](class_worldenvironment.md#class-worldenvironment-property-environment)

- void **set_environment**(value: [Environment](class_environment.md#class-environment))
- [Environment](class_environment.md#class-environment) **get_environment**()

The [Environment](class_environment.md#class-environment) resource used by this **WorldEnvironment**, defining the default properties.
