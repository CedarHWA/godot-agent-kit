> Source: https://docs.godotengine.org/en/4.7/classes/class_renderscenedataextension.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="renderscenedataextension"></a>

<a id="class-renderscenedataextension"></a>

# RenderSceneDataExtension

**Inherits:** [RenderSceneData](class_renderscenedata.md#class-renderscenedata) **<** [Object](class_object.md#class-object)

This class allows for a RenderSceneData implementation to be made in GDExtension.

<a id="description"></a>

## Description

This class allows for a RenderSceneData implementation to be made in GDExtension.

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Projection](class_projection.md#class-projection) | [_get_cam_projection](class_renderscenedataextension.md#class-renderscenedataextension-private-method-get-cam-projection)() virtual const |
| [Transform3D](class_transform3d.md#class-transform3d) | [_get_cam_transform](class_renderscenedataextension.md#class-renderscenedataextension-private-method-get-cam-transform)() virtual const |
| [RID](class_rid.md#class-rid) | [_get_uniform_buffer](class_renderscenedataextension.md#class-renderscenedataextension-private-method-get-uniform-buffer)() virtual const |
| [int](class_int.md#class-int) | [_get_view_count](class_renderscenedataextension.md#class-renderscenedataextension-private-method-get-view-count)() virtual const |
| [Vector3](class_vector3.md#class-vector3) | [_get_view_eye_offset](class_renderscenedataextension.md#class-renderscenedataextension-private-method-get-view-eye-offset)(view: [int](class_int.md#class-int)) virtual const |
| [Projection](class_projection.md#class-projection) | [_get_view_projection](class_renderscenedataextension.md#class-renderscenedataextension-private-method-get-view-projection)(view: [int](class_int.md#class-int)) virtual const |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-renderscenedataextension-private-method-get-cam-projection"></a>

[Projection](class_projection.md#class-projection) **_get_cam_projection**() virtual const [🔗](class_renderscenedataextension.md#class-renderscenedataextension-private-method-get-cam-projection)

Implement this in GDExtension to return the camera [Projection](class_projection.md#class-projection).

---


<a id="class-renderscenedataextension-private-method-get-cam-transform"></a>

[Transform3D](class_transform3d.md#class-transform3d) **_get_cam_transform**() virtual const [🔗](class_renderscenedataextension.md#class-renderscenedataextension-private-method-get-cam-transform)

Implement this in GDExtension to return the camera [Transform3D](class_transform3d.md#class-transform3d).

---


<a id="class-renderscenedataextension-private-method-get-uniform-buffer"></a>

[RID](class_rid.md#class-rid) **_get_uniform_buffer**() virtual const [🔗](class_renderscenedataextension.md#class-renderscenedataextension-private-method-get-uniform-buffer)

Implement this in GDExtension to return the [RID](class_rid.md#class-rid) of the uniform buffer containing the scene data as a UBO.

---


<a id="class-renderscenedataextension-private-method-get-view-count"></a>

[int](class_int.md#class-int) **_get_view_count**() virtual const [🔗](class_renderscenedataextension.md#class-renderscenedataextension-private-method-get-view-count)

Implement this in GDExtension to return the view count.

---


<a id="class-renderscenedataextension-private-method-get-view-eye-offset"></a>

[Vector3](class_vector3.md#class-vector3) **_get_view_eye_offset**(view: [int](class_int.md#class-int)) virtual const [🔗](class_renderscenedataextension.md#class-renderscenedataextension-private-method-get-view-eye-offset)

Implement this in GDExtension to return the eye offset for the given `view`.

---


<a id="class-renderscenedataextension-private-method-get-view-projection"></a>

[Projection](class_projection.md#class-projection) **_get_view_projection**(view: [int](class_int.md#class-int)) virtual const [🔗](class_renderscenedataextension.md#class-renderscenedataextension-private-method-get-view-projection)

Implement this in GDExtension to return the view [Projection](class_projection.md#class-projection) for the given `view`.
