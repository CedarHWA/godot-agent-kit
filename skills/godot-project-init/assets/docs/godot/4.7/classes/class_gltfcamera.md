> Source: https://docs.godotengine.org/en/4.7/classes/class_gltfcamera.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="gltfcamera"></a>

<a id="class-gltfcamera"></a>

# GLTFCamera

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Represents a glTF camera.

<a id="description"></a>

## Description

Represents a camera as defined by the base glTF spec.

<a id="tutorials"></a>

## Tutorials

- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving.md)
- [glTF camera detailed specification](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-camera)
- [glTF camera spec and example file](https://github.com/KhronosGroup/glTF-Tutorials/blob/master/gltfTutorial/gltfTutorial_015_SimpleCameras.md)

<a id="properties"></a>

## Properties

|  |  |  |
| --- | --- | --- |
| [float](class_float.md#class-float) | [depth_far](class_gltfcamera.md#class-gltfcamera-property-depth-far) | `4000.0` |
| [float](class_float.md#class-float) | [depth_near](class_gltfcamera.md#class-gltfcamera-property-depth-near) | `0.05` |
| [float](class_float.md#class-float) | [fov](class_gltfcamera.md#class-gltfcamera-property-fov) | `1.3089969` |
| [bool](class_bool.md#class-bool) | [perspective](class_gltfcamera.md#class-gltfcamera-property-perspective) | `true` |
| [float](class_float.md#class-float) | [size_mag](class_gltfcamera.md#class-gltfcamera-property-size-mag) | `0.5` |

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [GLTFCamera](class_gltfcamera.md#class-gltfcamera) | [from_dictionary](class_gltfcamera.md#class-gltfcamera-method-from-dictionary)(dictionary: [Dictionary](class_dictionary.md#class-dictionary)) static |
| [GLTFCamera](class_gltfcamera.md#class-gltfcamera) | [from_node](class_gltfcamera.md#class-gltfcamera-method-from-node)(camera_node: [Camera3D](class_camera3d.md#class-camera3d)) static |
| [Dictionary](class_dictionary.md#class-dictionary) | [to_dictionary](class_gltfcamera.md#class-gltfcamera-method-to-dictionary)() const |
| [Camera3D](class_camera3d.md#class-camera3d) | [to_node](class_gltfcamera.md#class-gltfcamera-method-to-node)() const |

---


<a id="property-descriptions"></a>

## Property Descriptions

<a id="class-gltfcamera-property-depth-far"></a>

[float](class_float.md#class-float) **depth_far** = `4000.0` [🔗](class_gltfcamera.md#class-gltfcamera-property-depth-far)

- void **set_depth_far**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_depth_far**()

The distance to the far culling boundary for this camera relative to its local Z axis, in meters. This maps to glTF's `zfar` property.

---


<a id="class-gltfcamera-property-depth-near"></a>

[float](class_float.md#class-float) **depth_near** = `0.05` [🔗](class_gltfcamera.md#class-gltfcamera-property-depth-near)

- void **set_depth_near**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_depth_near**()

The distance to the near culling boundary for this camera relative to its local Z axis, in meters. This maps to glTF's `znear` property.

---


<a id="class-gltfcamera-property-fov"></a>

[float](class_float.md#class-float) **fov** = `1.3089969` [🔗](class_gltfcamera.md#class-gltfcamera-property-fov)

- void **set_fov**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_fov**()

The FOV of the camera. This class and glTF define the camera FOV in radians, while Godot uses degrees. This maps to glTF's `yfov` property. This value is only used for perspective cameras, when [perspective](class_gltfcamera.md#class-gltfcamera-property-perspective) is `true`.

---


<a id="class-gltfcamera-property-perspective"></a>

[bool](class_bool.md#class-bool) **perspective** = `true` [🔗](class_gltfcamera.md#class-gltfcamera-property-perspective)

- void **set_perspective**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_perspective**()

If `true`, the camera is in perspective mode. Otherwise, the camera is in orthographic/orthogonal mode. This maps to glTF's camera `type` property. See [Camera3D.projection](class_camera3d.md#class-camera3d-property-projection) and the glTF spec for more information.

---


<a id="class-gltfcamera-property-size-mag"></a>

[float](class_float.md#class-float) **size_mag** = `0.5` [🔗](class_gltfcamera.md#class-gltfcamera-property-size-mag)

- void **set_size_mag**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_size_mag**()

The size of the camera. This class and glTF define the camera size magnitude as a radius in meters, while Godot defines it as a diameter in meters. This maps to glTF's `ymag` property. This value is only used for orthographic/orthogonal cameras, when [perspective](class_gltfcamera.md#class-gltfcamera-property-perspective) is `false`.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-gltfcamera-method-from-dictionary"></a>

[GLTFCamera](class_gltfcamera.md#class-gltfcamera) **from_dictionary**(dictionary: [Dictionary](class_dictionary.md#class-dictionary)) static [🔗](class_gltfcamera.md#class-gltfcamera-method-from-dictionary)

Creates a new GLTFCamera instance by parsing the given [Dictionary](class_dictionary.md#class-dictionary).

---


<a id="class-gltfcamera-method-from-node"></a>

[GLTFCamera](class_gltfcamera.md#class-gltfcamera) **from_node**(camera_node: [Camera3D](class_camera3d.md#class-camera3d)) static [🔗](class_gltfcamera.md#class-gltfcamera-method-from-node)

Create a new GLTFCamera instance from the given Godot [Camera3D](class_camera3d.md#class-camera3d) node.

---


<a id="class-gltfcamera-method-to-dictionary"></a>

[Dictionary](class_dictionary.md#class-dictionary) **to_dictionary**() const [🔗](class_gltfcamera.md#class-gltfcamera-method-to-dictionary)

Serializes this GLTFCamera instance into a [Dictionary](class_dictionary.md#class-dictionary).

---


<a id="class-gltfcamera-method-to-node"></a>

[Camera3D](class_camera3d.md#class-camera3d) **to_node**() const [🔗](class_gltfcamera.md#class-gltfcamera-method-to-node)

Converts this GLTFCamera instance into a Godot [Camera3D](class_camera3d.md#class-camera3d) node.
